"""Run with python3 -B scripts/test_resume_gate.py."""

from pathlib import Path

from resume_gate import DOSSIER_PATH, blacklist_terms, bullets, check_resume, coverage, roles, SECTION_NAMES


for heading in ("Experience", "Experiência", r"Experi\^encia", "Experiencia"):
    source = (
        rf"\section{{{heading}}}"
        r"\resumeSubheading{Company}{Jan 2024 - Present}{Engineer}{Remote}"
        r"\resumeItem{Built TypeScript services.}"
        r"\section{Education}\resumeItem{Degree}"
    )
    assert roles(source) == [("Company", "Jan 2024 - Present", "Engineer", "Remote")]
    assert bullets(source) == ["Built TypeScript services."]
assert SECTION_NAMES["es"] == ("Resumen", "Habilidades", "Experiencia", "Educación", "Idiomas")
print("PASS: English, Portuguese, escaped Portuguese, and Spanish Experience sections")

# The live DOSSIER blacklist parses to tokens, not to prose or table headers.
terms = blacklist_terms(DOSSIER_PATH.read_text(encoding="utf-8"))
for expected in ("Zendesk", "Power BI", "Java", "Kotlin", "Ruby"):
    assert expected in terms, expected
assert "Token" not in terms and not any("Luizalabs" in term for term in terms)
print("PASS: DOSSIER blacklist parsing")

assert coverage([3, 3], 0) == 100
assert coverage([3, 3], 1) == 67
assert coverage([], 0) == 100


def cv(skills: str, bullet: str) -> str:
    return (
        rf"\section{{Skills}}\resumeItem{{{skills}}}"
        r"\section{Experience}\resumeSubheading{Luizalabs}{Jan 2024 - Mar 2026}{Engineer}{Remote}"
        rf"\resumeItem{{{bullet}}}"
        r"\section{Education}"
    )


base = cv("TypeScript", "Built tax services in Node.js and Java.")
tailored = cv("TypeScript | NestJS | Zendesk", "Built tax services in Node.js, NestJS, Java, and Zendesk.")
manifest = {"required_tokens": ["NestJS"], "gap_tokens": ["Kafka"]}
checks, delta = check_resume(base, tailored, "text", manifest, {"snapshot": ""}, {}, ["Java", "Zendesk"])
status = {check["name"]: check for check in checks}
assert status["required_token_placement"]["status"] == "PASS"
assert status["blacklist"]["failures"] == ["Blacklisted token added: Zendesk"]  # Java is in the base, so it passes
assert status["gap_tokens_written"]["status"] == "PASS"
assert delta["coverage"]["required"] == 50 and status["required_coverage"]["status"] == "FAIL"

tailored_gap = cv("TypeScript | NestJS | Kafka", "Built tax services in Node.js, NestJS, and Kafka.")
checks, _ = check_resume(base, tailored_gap, "text", manifest, {"snapshot": ""}, {}, [])
assert {check["name"]: check for check in checks}["gap_tokens_written"]["failures"] == ["GAP token written: Kafka"]
print("PASS: blacklist, GAP, and required coverage checks")
