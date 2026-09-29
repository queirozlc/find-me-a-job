#!/usr/bin/env python3
"""Parallel LinkedIn sourcing through isolated Maestri portals.

The runner uses only the public ``maestri portal`` commands. It does not log
in, read credentials, submit an application, or contact a recruiter.

Each worker owns one portal and receives a disjoint query queue. Candidate
events are written as JSONL as soon as they are available. Deterministic hard
filters run before a candidate reaches the semantic preflight.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import datetime as dt
import hashlib
import html as html_module
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import threading
import time
from typing import Any, Iterable
from urllib.parse import parse_qs, quote, urlencode, unquote, urlparse


MAX_WORKERS = 3
ALLOWED_STACK = ("javascript", "typescript", "node.js", "nodejs", "react", "golang", " go ")
OUTSIDE_STACK = ("java", "python", "php", "c#", ".net", "ruby", "rails")
REMOTE_WORDS = ("remote", "remoto", "remota", "latam", "latin america", "brazil", "brasil")
ONSITE_WORDS = ("hybrid", "on-site", "onsite", "presencial", "híbrido", "hibrido")
AUTH_MARKERS = ("/login", "/checkpoint/", "/authwall", "sign in to continue", "captcha")

REF_RE = re.compile(r"^(@e\d+)\s")
MAIN_RE = re.compile(r"^(@e\d+) main(?:\s|$)", re.MULTILINE)
JOB_LINK_RE = re.compile(
    r'^(@e\d+) a "([^"]+)" href=(https://www\.linkedin\.com/jobs/view/(\d+)/[^ ]*)'
)
COMPANY_LINK_RE = re.compile(
    r'^(@e\d+) a "([^"]+)" href=https://www\.linkedin\.com/company/[^ ]+'
)
POST_ITEM_RE = re.compile(r'^(@e\d+) listitem "Feed post', re.MULTILINE)
REMOTE_REF_RE = re.compile(r'^(@e\d+) radio "Filter by Remote"')
OVER_100_RE = re.compile(
    r"\b(?:over\s+100\s+(?:applicants|people clicked apply)|100\+\s+applicants)\b",
    re.IGNORECASE,
)
APPLICANT_COUNT_RE = re.compile(
    r"\b(?P<count>\d[\d,]*)\s+(?:applicants|people clicked apply)\b",
    re.IGNORECASE,
)


class SourceError(RuntimeError):
    """A sourcing action failed without a safe automatic recovery."""


class AuthWall(SourceError):
    """LinkedIn requires user authentication or verification."""


@dataclasses.dataclass(frozen=True)
class Worker:
    name: str
    portal: str
    surface: str


@dataclasses.dataclass(frozen=True)
class Settings:
    cards_per_query: int
    command_timeout_seconds: int
    settle_seconds: float
    blocklist: tuple[str, ...]


class PortalHTML(HTMLParser):
    """Read stable accessibility attributes and links from portal HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.remote_checked = False
        self.anchors: list[dict[str, str]] = []
        self._anchor: dict[str, str] | None = None
        self._anchor_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if (
            values.get("role") == "radio"
            and values.get("aria-label") == "Filter by Remote"
            and values.get("aria-checked") == "true"
        ):
            self.remote_checked = True

        if self._anchor is not None:
            self._anchor_depth += 1
        elif tag == "a":
            self._anchor = {
                "href": values.get("href", ""),
                "label": values.get("aria-label", ""),
                "ref": f"@{values['data-mref']}" if values.get("data-mref") else "",
                "text": "",
            }
            self._anchor_depth = 1

    def handle_data(self, data: str) -> None:
        if self._anchor is not None:
            self._anchor["text"] += data

    def handle_endtag(self, tag: str) -> None:
        if self._anchor is None:
            return
        self._anchor_depth -= 1
        if self._anchor_depth == 0:
            self._anchor["text"] = clean_text(self._anchor["text"])
            self.anchors.append(self._anchor)
            self._anchor = None


class PortalClient:
    def __init__(self, portal: str, timeout: int, settle_seconds: float) -> None:
        self.portal = portal
        self.timeout = timeout
        self.settle_seconds = settle_seconds

    def _run(self, *args: str) -> str:
        command = ["maestri", "portal", *args, self.portal]
        if args and args[0] in {"navigate", "click", "text"}:
            command = ["maestri", "portal", args[0], self.portal, *args[1:]]
        result = subprocess.run(
            command,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=self.timeout,
        )
        if result.returncode != 0:
            raise SourceError(f"{' '.join(command[:3])} failed: {clean_text(result.stdout)}")
        return result.stdout

    def navigate(self, url: str) -> None:
        self._run("navigate", url)
        time.sleep(self.settle_seconds)

    def click(self, ref: str) -> None:
        self._run("click", ref)
        time.sleep(self.settle_seconds)

    def info(self) -> str:
        return self._run("info")

    def snapshot(self) -> str:
        return self._run("snapshot")

    def html(self) -> str:
        return self._run("html")

    def text(self, ref: str) -> str:
        return self._run("text", ref)

    def wait_for_content(self) -> str:
        last = ""
        for _ in range(6):
            last = self.snapshot()
            assert_no_auth_wall(self.info(), last)
            if MAIN_RE.search(last) or POST_ITEM_RE.search(last):
                return last
            time.sleep(self.settle_seconds)
        raise SourceError(f"Portal {self.portal!r} did not expose searchable content")

    def ensure_remote_filter(self) -> None:
        page = parse_portal_html(self.html())
        if page.remote_checked:
            return
        snapshot = self.snapshot()
        match = next((REMOTE_REF_RE.match(line) for line in snapshot.splitlines() if REMOTE_REF_RE.match(line)), None)
        if match is None:
            # LinkedIn does not expose this control on every search layout.
            # Candidate classification still rejects roles without remote proof.
            return
        self.click(match.group(1))
        for _ in range(5):
            if parse_portal_html(self.html()).remote_checked:
                return
            time.sleep(self.settle_seconds)
        # The result layout can replace the filter control after the click.
        # Candidate classification still rejects roles without remote proof.
        return


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def clean_text(value: str) -> str:
    return " ".join(html_module.unescape(value).split())


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return result[:80] or "unknown"


def stable_id(*values: str) -> str:
    payload = "\x1f".join(values).encode("utf-8", errors="replace")
    return hashlib.sha256(payload).hexdigest()[:16]


def parse_portal_html(value: str) -> PortalHTML:
    parser = PortalHTML()
    parser.feed(value)
    return parser


def assert_no_auth_wall(*values: str) -> None:
    text = "\n".join(values).casefold()
    if any(marker in text for marker in AUTH_MARKERS):
        raise AuthWall("LinkedIn authentication or verification is required")


def jobs_url(query: str, recency: str = "day") -> str:
    params = urlencode(
        {
            "keywords": query,
            "origin": "JOB_SEARCH_PAGE_JOB_FILTER",
            "f_TPR": "r86400" if recency == "day" else "r604800",
        },
        quote_via=quote,
    )
    return f"https://www.linkedin.com/jobs/search-results/?{params}"


def posts_url(query: str, recency: str = "day") -> str:
    params = urlencode(
        {
            "keywords": query,
            "origin": "GLOBAL_SEARCH_HEADER",
            "sortBy": '["date_posted"]',
            "datePosted": '["past-24h"]' if recency == "day" else '["past-week"]',
        },
        quote_via=quote,
    )
    return f"https://www.linkedin.com/search/results/content/?{params}"


def main_ref(snapshot: str) -> str:
    for line in snapshot.splitlines():
        match = MAIN_RE.match(line)
        if match:
            return match.group(1)
    raise SourceError("The accessibility snapshot has no main node")


def job_card_refs(snapshot: str) -> list[tuple[str, str]]:
    lines = snapshot.splitlines()
    cards: list[tuple[str, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r'^(@e\d+) button "([^"]+)" \[(-?\d+),', line)
        if not match or int(match.group(3)) > 500:
            continue
        nearby = "\n".join(lines[index + 1 : index + 4])
        if re.search(r'button "Dismiss .+ job"', nearby):
            cards.append((match.group(1), match.group(2)))
    return cards


def post_refs(snapshot: str) -> list[str]:
    return POST_ITEM_RE.findall("\n".join(snapshot.splitlines()))


def snapshot_segment(snapshot: str, start_ref: str, boundary: re.Pattern[str]) -> str:
    lines = snapshot.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(f"{start_ref} ")), None)
    if start is None:
        return ""
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if boundary.match(lines[index]):
            end = index
            break
    return "\n".join(lines[start:end])


def decode_external_url(value: str) -> str:
    value = html_module.unescape(value)
    parsed = urlparse(value)
    if parsed.netloc.endswith("linkedin.com") and parsed.path == "/safety/go/":
        target = parse_qs(parsed.query).get("url", [""])[0]
        return unquote(target)
    return value


def job_apply_url(page: PortalHTML) -> str:
    for anchor in page.anchors:
        label = f"{anchor.get('label', '')} {anchor.get('text', '')}".casefold()
        href = decode_external_url(anchor.get("href", ""))
        host = urlparse(href).netloc.casefold()
        if "apply" in label and host and not host.endswith("linkedin.com"):
            return href
    return ""


def selected_job_fields(snapshot: str, info: str) -> tuple[str, str, str, str]:
    match = re.search(r"currentJobId=(\d+)", info)
    current_id = match.group(1) if match else ""
    title = "not observable"
    job_url = ""
    title_line = -1
    lines = snapshot.splitlines()
    for index, line in enumerate(lines):
        job = JOB_LINK_RE.match(line)
        if job and (not current_id or job.group(4) == current_id):
            title = html_module.unescape(job.group(2))
            current_id = job.group(4)
            job_url = f"https://www.linkedin.com/jobs/view/{current_id}/"
            title_line = index
            break

    company = "not observable"
    if title_line >= 0:
        for line in reversed(lines[:title_line]):
            company_match = COMPANY_LINK_RE.match(line)
            if company_match:
                company = html_module.unescape(company_match.group(2))
                break
    return current_id or stable_id(title, company), title, company, job_url


def description_ref(snapshot: str) -> str | None:
    lines = snapshot.splitlines()
    for index, line in enumerate(lines):
        if re.match(r'^@e\d+ button "(?:…|\.\.\.) more"', line):
            for previous in reversed(lines[max(0, index - 5) : index]):
                match = re.match(r"^(@e\d+) span ", previous)
                if match:
                    return match.group(1)
    return None


def extract_job_header(main_text: str, company: str, title: str) -> str:
    pattern = re.compile(
        rf"(?:^|\n){re.escape(company)}\s*\n+{re.escape(title)}\s*\n+(?P<header>[^\n]+)",
        re.IGNORECASE,
    )
    matches = list(pattern.finditer(main_text))
    return clean_text(matches[-1].group("header")) if matches else "not observable"


def post_identity(text: str) -> tuple[str, str, str]:
    lines = [clean_text(line) for line in text.splitlines() if clean_text(line)]
    author = lines[1] if len(lines) > 1 and lines[0].casefold() == "feed post" else "not observable"
    age = next((line for line in lines[2:6] if re.search(r"\b\d+[mhdw]\b", line, re.IGNORECASE)), "not observable")
    follow_index = next((index for index, line in enumerate(lines) if line.casefold() == "follow"), 1)
    body = lines[follow_index + 1 :]
    body = body[: next((index for index, line in enumerate(body) if line.casefold() == "like"), len(body))]
    joined = "\n".join(body)
    title_match = re.search(
        r"(?:we(?:'|’)re hiring|hiring|role|position|vaga)\s*:\s*(.+)",
        joined,
        re.IGNORECASE,
    )
    if title_match:
        title = clean_text(title_match.group(1).splitlines()[0])[:180]
    else:
        title = next(
            (
                line[:180]
                for line in body
                if re.search(r"\b(?:engineer|developer|desenvolvedor|programador)\b", line, re.IGNORECASE)
            ),
            "not observable",
        )
    return author, age, title


def contains_token(text: str, tokens: Iterable[str]) -> bool:
    padded = f" {text.casefold()} "
    return any(token in padded for token in tokens)


def classify_candidate(candidate: dict[str, Any], blocklist: Iterable[str]) -> tuple[str, list[str], list[str]]:
    title = candidate.get("title", "")
    company = candidate.get("company", "")
    apply_url = candidate.get("apply_url", "")
    location = candidate.get("location", "")
    text = "\n".join(
        str(candidate.get(key, ""))
        for key in ("title", "company", "location", "header", "description")
    )
    folded = text.casefold()
    reasons: list[str] = []
    review: list[str] = []

    if re.search(r"\breposted\b", text, re.IGNORECASE):
        reasons.append("reposted")
    if OVER_100_RE.search(text):
        reasons.append("over_100_applicants")
    if clean_text(company).casefold() in {clean_text(item).casefold() for item in blocklist}:
        reasons.append("company_blocklist")
    if urlparse(apply_url).netloc.casefold().endswith("gupy.io"):
        reasons.append("gupy")
    if contains_token(f" {location} {title} ", ONSITE_WORDS):
        reasons.append("hybrid_or_onsite")

    title_folded = f" {title.casefold()} "
    if contains_token(title_folded, OUTSIDE_STACK) and not contains_token(title_folded, ALLOWED_STACK):
        reasons.append("outside_primary_stack_title")
    if not contains_token(folded, ALLOWED_STACK):
        reasons.append("allowed_stack_not_observable")
    if not contains_token(folded, REMOTE_WORDS):
        reasons.append("remote_or_latam_not_observable")

    if re.search(r"must (?:be authorized|have authorization) to work in (?:the )?(?:u\.s\.|us|united states)", folded):
        reasons.append("unsupported_us_work_authorization")
    if re.search(r"(?:remote\s*[-–]\s*(?:usa|us only)|must (?:live|reside|be located) in (?:the )?(?:usa|us|united states))", folded):
        reasons.append("mandatory_us_location")

    for marker, label in (
        (r"\bmust reside\b", "mandatory_location_needs_review"),
        (r"\blocal candidates?\b", "local_boundary_needs_review"),
        (r"\bnot for freelancers?\b", "contract_path_needs_review"),
    ):
        if re.search(marker, folded):
            review.append(label)

    if reasons:
        return "rejected", list(dict.fromkeys(reasons)), list(dict.fromkeys(review))
    if review:
        return "review", [], list(dict.fromkeys(review))
    return "preflight", [], []


def cheap_card_reasons(text: str, blocklist: Iterable[str]) -> list[str]:
    folded_lines = {clean_text(line).casefold() for line in text.splitlines() if clean_text(line)}
    reasons: list[str] = []
    if re.search(r"\breposted\b", text, re.IGNORECASE):
        reasons.append("reposted")
    if OVER_100_RE.search(text):
        reasons.append("over_100_applicants")
    if folded_lines.intersection(clean_text(item).casefold() for item in blocklist):
        reasons.append("company_blocklist")
    if contains_token(text, ONSITE_WORDS):
        reasons.append("hybrid_or_onsite")
    return reasons


class EventSink:
    def __init__(self, output_dir: Path) -> None:
        if output_dir.exists() and any(output_dir.iterdir()):
            raise SourceError(f"Output directory is not empty: {output_dir}")
        output_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir = output_dir
        self.events_path = output_dir / "events.jsonl"
        self.preflight_path = output_dir / "preflight.jsonl"
        self.completion_path = output_dir / "run.complete.json"
        self.preflight_path.touch()
        self._seen: set[str] = set()
        self._lock = threading.Lock()

    def emit(self, event: dict[str, Any]) -> None:
        with self._lock:
            event = dict(event)
            event.setdefault("at", now())
            evidence = event.pop("_evidence", None)
            if event.get("event") == "candidate":
                key = str(event.get("job_id") or event.get("url") or stable_id(json.dumps(event, sort_keys=True)))
                if key in self._seen:
                    event["status"] = "rejected"
                    event["reasons"] = list(dict.fromkeys([*event.get("reasons", []), "duplicate"]))
                else:
                    self._seen.add(key)
                if evidence is not None:
                    evidence_dir = self.output_dir / "evidence" / slug(str(event.get("worker", "worker")))
                    evidence_dir.mkdir(parents=True, exist_ok=True)
                    evidence_path = evidence_dir / f"{slug(key)}.txt"
                    evidence_path.write_text(str(evidence), encoding="utf-8")
                    event["evidence_path"] = str(evidence_path.resolve())
                description = str(event.pop("description", ""))
                if description:
                    event["description_chars"] = len(description)
                    event["description_sha256"] = hashlib.sha256(description.encode("utf-8")).hexdigest()

            line = json.dumps(event, ensure_ascii=False, sort_keys=True)
            with self.events_path.open("a", encoding="utf-8") as handle:
                handle.write(line + "\n")
            if event.get("event") == "candidate" and event.get("status") in {"preflight", "review"}:
                with self.preflight_path.open("a", encoding="utf-8") as handle:
                    handle.write(line + "\n")
            if event.get("event") == "run_finished":
                temporary = self.completion_path.with_suffix(".tmp")
                temporary.write_text(line + "\n", encoding="utf-8")
                temporary.replace(self.completion_path)
            print(line, flush=True)


def job_candidate(
    client: PortalClient,
    worker: Worker,
    query: str,
    index: int,
    snapshot: str,
    card_text: str,
) -> dict[str, Any]:
    info = client.info()
    current_id, title, company, job_url = selected_job_fields(snapshot, info)
    page_html = client.html()
    page = parse_portal_html(page_html)
    main_text = client.text(main_ref(snapshot))
    header = extract_job_header(main_text, company, title)
    description_node = description_ref(snapshot)
    description = client.text(description_node) if description_node else ""
    apply_url = job_apply_url(page)
    location = header.split("·", 1)[0].strip() if header != "not observable" else "not observable"
    candidate = {
        "event": "candidate",
        "worker": worker.name,
        "portal": worker.portal,
        "surface": worker.surface,
        "query": query,
        "position": index + 1,
        "job_id": current_id,
        "url": job_url,
        "title": title,
        "company": company,
        "location": location,
        "header": header,
        "description": description,
        "description_complete": description_node is not None,
        "apply_url": apply_url,
        "applicant_count": applicant_count(header),
        "_evidence": f"CARD\n{card_text}\n\nHEADER\n{header}\n\nDESCRIPTION\n{description}\n",
    }
    return candidate


def applicant_count(text: str) -> int | None:
    if OVER_100_RE.search(text):
        return None
    match = APPLICANT_COUNT_RE.search(text)
    if not match:
        return None
    return int(match.group("count").replace(",", ""))


def source_jobs(
    worker: Worker,
    queries: list[str],
    settings: Settings,
    sink: EventSink,
    recency: str,
) -> None:
    client = PortalClient(worker.portal, settings.command_timeout_seconds, settings.settle_seconds)
    for query in queries:
        sink.emit({"event": "query_started", "worker": worker.name, "portal": worker.portal, "surface": "jobs", "query": query})
        reviewed = 0
        client.navigate(jobs_url(query, recency))
        client.wait_for_content()
        client.ensure_remote_filter()
        first_snapshot = client.wait_for_content()
        available = len(job_card_refs(first_snapshot))
        for index in range(min(settings.cards_per_query, available)):
            snapshot = client.wait_for_content()
            cards = job_card_refs(snapshot)
            if index >= len(cards):
                break
            ref, label = cards[index]
            card_text = client.text(ref)
            reviewed += 1
            sink.emit({"event": "candidate_seen", "worker": worker.name, "portal": worker.portal, "surface": "jobs", "query": query, "position": index + 1})
            cheap = cheap_card_reasons(card_text, settings.blocklist)
            if cheap:
                candidate = {
                    "event": "candidate",
                    "worker": worker.name,
                    "portal": worker.portal,
                    "surface": "jobs",
                    "query": query,
                    "position": index + 1,
                    "job_id": stable_id(query, label, card_text),
                    "url": "",
                    "title": label,
                    "company": "not observable",
                    "location": "not observable",
                    "header": card_text,
                    "description": "",
                    "apply_url": "",
                    "applicant_count": applicant_count(card_text),
                    "status": "rejected",
                    "reasons": cheap,
                    "review_flags": [],
                    "_evidence": card_text,
                }
                sink.emit(candidate)
                continue

            client.click(ref)
            detail_snapshot = client.wait_for_content()
            candidate = job_candidate(client, worker, query, index, detail_snapshot, card_text)
            status, reasons, review = classify_candidate(candidate, settings.blocklist)
            if not candidate["description_complete"] and status != "rejected":
                status = "review"
                review.append("description_not_observable")
            candidate.update(status=status, reasons=reasons, review_flags=review)
            sink.emit(candidate)

        sink.emit(
            {
                "event": "query_finished",
                "worker": worker.name,
                "portal": worker.portal,
                "surface": "jobs",
                "query": query,
                "reviewed": reviewed,
                "visible_cards": available,
            }
        )


def source_posts(
    worker: Worker,
    queries: list[str],
    settings: Settings,
    sink: EventSink,
    recency: str,
) -> None:
    client = PortalClient(worker.portal, settings.command_timeout_seconds, settings.settle_seconds)
    for query in queries:
        sink.emit({"event": "query_started", "worker": worker.name, "portal": worker.portal, "surface": "posts", "query": query})
        client.navigate(posts_url(query, recency))
        snapshot = client.wait_for_content()
        refs = post_refs(snapshot)
        page = parse_portal_html(client.html())
        reviewed = 0
        for index in range(min(settings.cards_per_query, len(refs))):
            snapshot = client.wait_for_content()
            refs = post_refs(snapshot)
            if index >= len(refs):
                break
            ref = refs[index]
            post_text = client.text(ref)
            reviewed += 1
            sink.emit({"event": "candidate_seen", "worker": worker.name, "portal": worker.portal, "surface": "posts", "query": query, "position": index + 1})
            segment = snapshot_segment(snapshot, ref, POST_ITEM_RE)
            segment_refs = set(REF_RE.match(line).group(1) for line in segment.splitlines() if REF_RE.match(line))
            links = [
                decode_external_url(anchor["href"])
                for anchor in page.anchors
                if anchor.get("href") and anchor_ref_in_segment(anchor, segment_refs)
            ]
            links = [link for link in links if urlparse(link).netloc and not urlparse(link).netloc.endswith("linkedin.com")]
            author, age, title = post_identity(post_text)
            apply_url = links[0] if links else ""
            post_id = stable_id(author, title, apply_url or post_text)
            candidate = {
                "event": "candidate",
                "worker": worker.name,
                "portal": worker.portal,
                "surface": "posts",
                "query": query,
                "position": index + 1,
                "job_id": post_id,
                "url": apply_url,
                "title": title,
                "company": author,
                "location": "not observable",
                "header": age,
                "description": post_text,
                "apply_url": apply_url,
                "applicant_count": applicant_count(post_text),
                "author_url": next(
                    (
                        anchor["href"]
                        for anchor in page.anchors
                        if anchor_ref_in_segment(anchor, segment_refs)
                        and "/in/" in anchor.get("href", "")
                    ),
                    "",
                ),
                "contact_channels": sorted(set(re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", post_text, re.IGNORECASE))),
                "_evidence": post_text,
            }
            status, reasons, review = classify_candidate(candidate, settings.blocklist)
            candidate.update(status=status, reasons=reasons, review_flags=review)
            sink.emit(candidate)

        sink.emit(
            {
                "event": "query_finished",
                "worker": worker.name,
                "portal": worker.portal,
                "surface": "posts",
                "query": query,
                "reviewed": reviewed,
                "visible_posts": len(refs),
            }
        )


def anchor_ref_in_segment(anchor: dict[str, str], refs: set[str]) -> bool:
    return anchor.get("ref", "") in refs


def load_config(path: Path) -> tuple[list[Worker], dict[str, list[str]], Settings]:
    data = json.loads(path.read_text(encoding="utf-8"))
    workers = [Worker(**item) for item in data.get("workers", [])]
    if not 1 <= len(workers) <= MAX_WORKERS:
        raise SourceError(f"Config must define between 1 and {MAX_WORKERS} workers")
    if len({worker.portal for worker in workers}) != len(workers):
        raise SourceError("Every worker must own a different portal")
    if len({worker.name for worker in workers}) != len(workers):
        raise SourceError("Every worker must have a different name")
    if any(worker.surface not in {"jobs", "posts"} for worker in workers):
        raise SourceError("Worker surface must be jobs or posts")

    queries = data.get("queries", {})
    normalized_queries = {
        surface: [str(query) for query in queries.get(surface, [])]
        for surface in ("jobs", "posts")
    }
    for surface, items in normalized_queries.items():
        if items and not any(worker.surface == surface for worker in workers):
            raise SourceError(f"Queries for {surface} have no worker")

    limits = data.get("limits", {})
    cards = int(limits.get("cards_per_query", 5))
    if not 1 <= cards <= 20:
        raise SourceError("cards_per_query must be between 1 and 20")
    settings = Settings(
        cards_per_query=cards,
        command_timeout_seconds=int(limits.get("command_timeout_seconds", 30)),
        settle_seconds=float(limits.get("settle_seconds", 1.5)),
        blocklist=tuple(str(item) for item in data.get("blocklist", ["BairesDev"])),
    )
    return workers, normalized_queries, settings


def assign_queries(workers: list[Worker], queries: dict[str, list[str]]) -> dict[str, list[str]]:
    assignments = {worker.name: [] for worker in workers}
    for surface in ("jobs", "posts"):
        owners = [worker for worker in workers if worker.surface == surface]
        for index, query in enumerate(queries[surface]):
            assignments[owners[index % len(owners)].name].append(query)
    return assignments


def plan_document(workers: list[Worker], assignments: dict[str, list[str]]) -> dict[str, Any]:
    return {
        "worker_count": len(workers),
        "workers": [
            {
                "name": worker.name,
                "portal": worker.portal,
                "surface": worker.surface,
                "query_count": len(assignments[worker.name]),
                "queries": assignments[worker.name],
            }
            for worker in workers
        ],
    }


def run_parallel(
    config_path: Path,
    output_dir: Path,
    query_limit: int | None = None,
    cards_per_query: int | None = None,
    recency: str = "day",
) -> int:
    workers, queries, settings = load_config(config_path)
    assignments = assign_queries(workers, queries)
    if query_limit is not None:
        assignments = {name: items[:query_limit] for name, items in assignments.items()}
    if cards_per_query is not None:
        settings = dataclasses.replace(settings, cards_per_query=cards_per_query)
    sink = EventSink(output_dir)
    failures: list[str] = []

    def run_worker(worker: Worker) -> None:
        sink.emit({"event": "worker_started", "worker": worker.name, "portal": worker.portal, "surface": worker.surface})
        try:
            source = source_jobs if worker.surface == "jobs" else source_posts
            source(worker, assignments[worker.name], settings, sink, recency)
        except Exception as error:
            failures.append(f"{worker.name}: {error}")
            sink.emit(
                {
                    "event": "worker_failed",
                    "worker": worker.name,
                    "portal": worker.portal,
                    "surface": worker.surface,
                    "error": str(error),
                    "blocked": isinstance(error, AuthWall),
                }
            )
        else:
            sink.emit({"event": "worker_finished", "worker": worker.name, "portal": worker.portal, "surface": worker.surface})

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(workers)) as executor:
        futures = [executor.submit(run_worker, worker) for worker in workers]
        concurrent.futures.wait(futures)

    sink.emit({"event": "run_finished", "failures": failures, "ok": not failures})
    return 1 if failures else 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("plan", help="Validate and print the three-worker query plan")
    run_parser = subparsers.add_parser("run", help="Run the assigned queries in parallel")
    run_parser.add_argument("--output-dir", type=Path, required=True)
    run_parser.add_argument("--query-limit", type=int, choices=range(1, 101))
    run_parser.add_argument("--cards-per-query", type=int, choices=range(1, 21))
    run_parser.add_argument("--recency", choices=("day", "week"), default="day")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        workers, queries, _settings = load_config(args.config)
        assignments = assign_queries(workers, queries)
        if args.command == "plan":
            print(json.dumps(plan_document(workers, assignments), indent=2, ensure_ascii=False))
            return 0
        return run_parallel(
            args.config,
            args.output_dir,
            query_limit=args.query_limit,
            cards_per_query=args.cards_per_query,
            recency=args.recency,
        )
    except (OSError, ValueError, json.JSONDecodeError, SourceError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
