#!/usr/bin/env python3
"""Verify a built CV against the base CV and the posting spec (manifest)."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
from typing import Any


FORBIDDEN_TERMS = ("ruby", "rails")
MIN_REQUIRED_COVERAGE = 70  # Lucas, 2026-09-29. CLAUDE.md section 4.1.
DOSSIER_PATH = Path(__file__).resolve().parent.parent / "DOSSIER.md"
TIMEZONE_PATTERNS = (
    r"\bUTC\s*[+-]\s*\d+",
    r"\bGMT\s*[+-]\s*\d+",
    r"\b\d+\s*(?:hours?|hrs?)\s+(?:of\s+)?(?:time[- ]?zone\s+)?overlap\b",
)
CONTACT_VALUES = (
    "Vitória, ES, Brazil",
    "sepulchrolucas@gmail.com",
    "linkedin.com/in/queiroz-lucas",
    "github.com/queirozlc",
)
SECTION_NAMES = {
    "en": ("Summary", "Skills", "Experience", "Education", "Language"),
    "pt": ("Resumo", "Habilidades", "Experiência", "Formação", "Idiomas"),
    "es": ("Resumen", "Habilidades", "Experiencia", "Educación", "Idiomas"),
}


class GateError(RuntimeError):
    """The deterministic gate could not run."""


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def balanced_arguments(value: str, macro: str, count: int) -> list[tuple[str, ...]]:
    results: list[tuple[str, ...]] = []
    marker = f"\\{macro}"
    cursor = 0
    while True:
        start = value.find(marker, cursor)
        if start < 0:
            break
        position = start + len(marker)
        arguments: list[str] = []
        valid = True
        for _ in range(count):
            while position < len(value) and value[position].isspace():
                position += 1
            if position >= len(value) or value[position] != "{":
                valid = False
                break
            depth = 1
            begin = position + 1
            position += 1
            while position < len(value) and depth:
                if value[position] == "{" and (position == 0 or value[position - 1] != "\\"):
                    depth += 1
                elif value[position] == "}" and (position == 0 or value[position - 1] != "\\"):
                    depth -= 1
                position += 1
            if depth:
                valid = False
                break
            arguments.append(value[begin : position - 1])
        if valid:
            results.append(tuple(arguments))
            cursor = position
        else:
            cursor = start + len(marker)
    return results


def section_source(value: str, names: tuple[str, ...]) -> str:
    for name in names:
        match = re.search(rf"\\section\{{{re.escape(name)}\}}", value, re.IGNORECASE)
        if match:
            end = re.search(r"\\section\{", value[match.end() :])
            return value[match.end() : match.end() + end.start()] if end else value[match.end() :]
    return ""


def latex_to_text(value: str) -> str:
    replacements = {
        r"\%": "%",
        r"\&": "&",
        r"\_": "_",
        r"\textbar{}": "|",
        r"\textquotesingle{}": "'",
        r"\'a": "á",
        r"\'e": "é",
        r"\'i": "í",
        r"\'o": "ó",
        r"\'u": "ú",
        r"\'A": "Á",
        r"\'E": "É",
        r"\'I": "Í",
        r"\'O": "Ó",
        r"\'U": "Ú",
        r"\c{c}": "ç",
        "~": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    previous = None
    while previous != value:
        previous = value
        value = re.sub(r"\\(?:textbf|textit|small|href)\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", value)
    value = value.replace("{", " ").replace("}", " ").replace("\\", " ")
    return " ".join(value.split())


def folded(value: str) -> str:
    plain = unicodedata.normalize("NFKD", latex_to_text(value))
    plain = "".join(character for character in plain if not unicodedata.combining(character))
    plain = plain.replace("–", "-").replace("—", "-")
    return " ".join(plain.casefold().split())


def contains_token(value: str, token: str) -> bool:
    haystack = folded(value)
    needle = folded(token)
    if re.fullmatch(r"[a-z0-9+#.]+", needle):
        return re.search(rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])", haystack) is not None
    return needle in haystack


def experience_source(value: str) -> str:
    return section_source(value, ("Experience", "Experiência", r"Experi\^encia", "Experiencia"))


def skills_source(value: str) -> str:
    return section_source(value, ("Skills", "Habilidades"))


def roles(value: str) -> list[tuple[str, str, str, str]]:
    return [tuple(latex_to_text(item) for item in record) for record in balanced_arguments(experience_source(value), "resumeSubheading", 4)]


def bullets(value: str) -> list[str]:
    return [latex_to_text(item[0]).removeprefix("• ") for item in balanced_arguments(experience_source(value), "resumeItem", 1)]


def role_sources(value: str) -> dict[str, str]:
    """Experience source per role, keyed by folded company name."""
    source = experience_source(value)
    starts = [match.start() for match in re.finditer(r"\\resumeSubheading\b", source)] + [len(source)]
    result: dict[str, str] = {}
    for begin, end in zip(starts, starts[1:]):
        heading = balanced_arguments(source[begin:end], "resumeSubheading", 4)
        if heading:
            result[folded(heading[0][0])] = source[begin:end]
    return result


def metrics(value: str) -> set[str]:
    return set(re.findall(r"\b\d+(?:\.\d+)?\s*%", latex_to_text(experience_source(value))))


def layout_hash(value: str) -> str:
    preamble = value.split(r"\begin{document}", 1)[0]
    normalized = re.sub(r"(?m)^\s*%.*$", "", preamble)
    normalized = "\n".join(line.rstrip() for line in normalized.splitlines() if line.strip())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def pdf_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", str(path), "-"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        raise GateError(f"pdftotext failed: {' '.join(result.stderr.split())}")
    if not result.stdout.strip():
        raise GateError("pdftotext returned no text")
    return result.stdout


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise GateError(f"Expected a JSON object: {path}")
    return value


def protected_claim_failures(base: str, tailored: str, manifest: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for claim in manifest.get("protected_claims", []):
        patterns = [str(pattern) for pattern in claim.get("patterns", [])]
        introduced = [pattern for pattern in patterns if contains_token(tailored, pattern) and not contains_token(base, pattern)]
        if introduced and claim.get("status") != "approved":
            failures.append(f"{claim.get('id', 'unknown')}: introduced {', '.join(introduced)} without approved evidence")
    return failures


def blacklist_terms(dossier: str) -> list[str]:
    """Read blocked tokens from the DOSSIER `### Blacklist` section: the
    parenthesized examples on each bullet line and the first table column."""
    match = re.search(r"(?m)^### Blacklist\b.*$", dossier)
    if not match:
        return []
    end = re.search(r"(?m)^#{2,3} ", dossier[match.end() :])
    section = dossier[match.end() : match.end() + end.start()] if end else dossier[match.end() :]
    terms: list[str] = []
    # Bullets wrap across lines; split into items first, then flatten each.
    for item in re.split(r"\n(?=- |\|)", section):
        line = " ".join(item.split())
        if line.startswith("- "):
            for group in re.findall(r"\(([^)]*)\)", line):
                terms.extend(group.split(","))
        elif line.startswith("|") and not re.match(r"\|\s*(Token\b|-)", line):
            terms.extend(line.split("|")[1].split(","))
    return [term.strip() for term in terms if term.strip()]


def placement_points(skills: str, experience: str, token: str) -> int:
    """RUBRIC Resume Evidence Check: Skills 1, Experience 2, both 3."""
    return (1 if contains_token(skills, token) else 0) + (2 if contains_token(experience, token) else 0)


def coverage(points: list[int], gaps: int) -> int:
    total = 3 * (len(points) + gaps)
    return round(100 * sum(points) / total) if total else 100


def identity_failures(base_roles: list[tuple[str, str, str, str]], cache: dict[str, Any]) -> list[str]:
    snapshot = str(cache.get("snapshot", ""))
    failures: list[str] = []
    for company, dates, title, _location in base_roles:
        for label, value in (("company", company), ("dates", dates), ("title", title)):
            if not contains_token(snapshot, value):
                failures.append(f"LinkedIn snapshot does not contain {label}: {value}")
    return failures


def check_resume(
    base: str,
    tailored: str,
    extracted: str,
    manifest: dict[str, Any],
    identity: dict[str, Any],
    claims: dict[str, Any],
    blacklist: list[str] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    language = str(manifest.get("language", "en"))
    required_tokens = [str(token) for token in manifest.get("required_tokens", [])]
    preferred_tokens = [str(token) for token in manifest.get("preferred_tokens", [])]
    gap_tokens = [str(token) for token in manifest.get("gap_tokens", [])]
    preferred_gap_tokens = [str(token) for token in manifest.get("preferred_gap_tokens", [])]
    base_roles = roles(base)
    tailored_roles = roles(tailored)
    base_bullets = bullets(base)
    tailored_bullets = bullets(tailored)
    skills = skills_source(tailored)
    experience = experience_source(tailored)

    checks: list[dict[str, Any]] = []

    def add(name: str, failures: list[str]) -> None:
        checks.append({"name": name, "status": "PASS" if not failures else "FAIL", "failures": failures})

    add("pdf_extraction", [] if extracted.strip() else ["PDF text is empty"])
    add(
        "sections",
        [section for section in SECTION_NAMES.get(language, SECTION_NAMES["en"]) if not contains_token(extracted, section)],
    )
    add("contact", [value for value in CONTACT_VALUES if not contains_token(extracted, value)])
    add("layout", [] if layout_hash(base) == layout_hash(tailored) else ["Tailored CV changed the approved base layout"])
    add("roles", [] if tailored_roles == base_roles else ["Tailored roles, titles, dates, or locations differ from the base CV"])
    add("linkedin_identity", identity_failures(base_roles, identity))
    completeness: list[str] = []
    if len(tailored_bullets) < len(base_bullets):
        completeness.append(f"Experience bullet count fell from {len(base_bullets)} to {len(tailored_bullets)}")
    missing_metrics = sorted(metrics(base) - metrics(tailored))
    if missing_metrics:
        completeness.append(f"Missing base metrics: {', '.join(missing_metrics)}")
    add("experience_completeness", completeness)
    forbidden = [term for term in FORBIDDEN_TERMS if contains_token(tailored, term) or contains_token(extracted, term)]
    timezone = [pattern for pattern in TIMEZONE_PATTERNS if re.search(pattern, latex_to_text(tailored), re.IGNORECASE)]
    add("forbidden_terms", [f"Forbidden term: {term}" for term in forbidden] + [f"Forbidden time-zone statement: {pattern}" for pattern in timezone])
    add("claim_allowlist", protected_claim_failures(base, tailored, claims))
    token_failures: list[str] = []
    for token in required_tokens:
        missing: list[str] = []
        if not contains_token(skills, token):
            missing.append("Skills")
        if not contains_token(experience, token):
            missing.append("Experience")
        if missing:
            token_failures.append(f"{token}: missing from {' and '.join(missing)}")
    add("required_token_placement", token_failures)

    # Posting Analysis spec: each anchored token sits in its role's bullets,
    # and each stack-depth token sits in Skills.
    by_role = role_sources(tailored)
    spec_failures = [
        f"{token}: not in the {company} role"
        for token, company in dict(manifest.get("anchors", {})).items()
        if not contains_token(by_role.get(folded(str(company)), ""), str(token))
    ]
    spec_failures += [f"{token}: stack-depth token missing from Skills" for token in manifest.get("stack_depth_tokens", []) if not contains_token(skills, str(token))]
    add("spec_placement", spec_failures)

    # A token counts as written for the posting only when the base CV lacks it,
    # so facts already in the base (Java at Luizalabs) never fail these checks.
    def introduced(token: str) -> bool:
        return contains_token(tailored, token) and not contains_token(base, token)

    add("blacklist", [f"Blacklisted token added: {term}" for term in (blacklist or []) if introduced(term)])
    add("gap_tokens_written", [f"GAP token written: {token}" for token in gap_tokens + preferred_gap_tokens if introduced(token)])

    required_points = [placement_points(skills, experience, token) for token in required_tokens]
    preferred_points = [placement_points(skills, experience, token) for token in preferred_tokens]
    scores = {
        "required": coverage(required_points, len(gap_tokens)),
        "preferred": coverage(preferred_points, len(preferred_gap_tokens)),
        "minimum_required": MIN_REQUIRED_COVERAGE,
    }
    add(
        "required_coverage",
        [] if scores["required"] >= MIN_REQUIRED_COVERAGE else [f"Required coverage {scores['required']} is below {MIN_REQUIRED_COVERAGE}"],
    )

    added_bullets = [item for item in tailored_bullets if folded(item) not in {folded(base_item) for base_item in base_bullets}]
    removed_bullets = [item for item in base_bullets if folded(item) not in {folded(tailored_item) for tailored_item in tailored_bullets}]
    delta = {
        "skills": latex_to_text(skills),
        "added_or_reworded_experience_bullets": added_bullets,
        "removed_or_reworded_base_bullets": removed_bullets,
        "base_bullet_count": len(base_bullets),
        "tailored_bullet_count": len(tailored_bullets),
        "coverage": scores,
    }
    return checks, delta


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--tailored", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--identity-cache", type=Path, required=True)
    parser.add_argument("--claim-allowlist", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--sentinel", type=Path, required=True)
    parser.add_argument("--dossier", type=Path, default=DOSSIER_PATH)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        base = args.base.read_text(encoding="utf-8")
        tailored = args.tailored.read_text(encoding="utf-8")
        manifest = load_json(args.manifest)
        identity = load_json(args.identity_cache)
        claims = load_json(args.claim_allowlist)
        extracted = pdf_text(args.pdf)
        blacklist = blacklist_terms(args.dossier.read_text(encoding="utf-8"))
        checks, delta = check_resume(base, tailored, extracted, manifest, identity, claims, blacklist)
        passed = all(check["status"] == "PASS" for check in checks)
        report = {
            "schema_version": 1,
            "application_id": manifest.get("application_id"),
            "generated_at": now(),
            "status": "PASS" if passed else "FAIL",
            "checks": checks,
            "delta": delta,
        }
        write_json_atomic(args.report, report)
        write_json_atomic(
            args.sentinel,
            {
                "schema_version": 1,
                "task": "deterministic-resume-gate",
                "application_id": manifest.get("application_id"),
                "status": "complete" if passed else "blocked",
                "completed_at": now(),
                "artifacts": [str(args.report.resolve())],
            },
        )
    except (OSError, ValueError, json.JSONDecodeError, GateError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps({"status": report["status"], "report": str(args.report)}))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
