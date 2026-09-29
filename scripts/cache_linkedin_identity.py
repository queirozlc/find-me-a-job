#!/usr/bin/env python3
"""Cache one read-only LinkedIn identity snapshot for a hunt."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time


AUTH_MARKERS = ("/login", "/checkpoint/", "/authwall", "sign in to continue", "captcha")


class IdentityCacheError(RuntimeError):
    """The profile snapshot cannot be cached safely."""


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def normalize(value: str) -> str:
    return " ".join(value.split())


def portal_command(action: str, portal: str, timeout: int, *args: str) -> str:
    result = subprocess.run(
        ["maestri", "portal", action, portal, *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        raise IdentityCacheError(f"maestri portal {action} failed: {normalize(result.stdout)}")
    return result.stdout


def main_ref(snapshot: str) -> str:
    match = re.search(r'^(@e\d+) main(?:\s|$)', snapshot, re.MULTILINE)
    if not match:
        raise IdentityCacheError("The profile snapshot has no main node")
    return match.group(1)


def validate_profile(info: str, snapshot: str) -> None:
    combined = f"{info}\n{snapshot}".casefold()
    if any(marker in combined for marker in AUTH_MARKERS):
        raise IdentityCacheError("LinkedIn authentication or verification is required")
    if "linkedin.com" not in combined:
        raise IdentityCacheError("The portal is not on LinkedIn")
    if not re.search(r"\b(?:experience|experiência)\b", snapshot, re.IGNORECASE):
        raise IdentityCacheError("The snapshot does not contain the Experience section")


def write_cache(output: Path, portal: str, info: str, snapshot: str) -> None:
    if output.exists():
        raise IdentityCacheError(f"Identity cache already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "captured_at": now(),
        "portal": portal,
        "source": "LinkedIn profile, read-only Maestri portal snapshot",
        "info": info,
        "snapshot": snapshot,
        "snapshot_sha256": hashlib.sha256(snapshot.encode("utf-8")).hexdigest(),
    }
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--portal", default="Profile Check")
    parser.add_argument("--profile-url", default="https://www.linkedin.com/in/queiroz-lucas/")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument(
        "--source-file",
        type=Path,
        help="Use a saved snapshot for an offline test. The file must contain LinkedIn and Experience.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        if args.source_file:
            snapshot = args.source_file.read_text(encoding="utf-8")
            info = "offline source linkedin.com/in/queiroz-lucas"
        else:
            details_url = args.profile_url.rstrip("/") + "/details/experience/"
            portal_command("navigate", args.portal, args.timeout, details_url)
            info = ""
            accessibility = ""
            profile_text = ""
            for _ in range(6):
                info = portal_command("info", args.portal, args.timeout)
                accessibility = portal_command("snapshot", args.portal, args.timeout)
                try:
                    profile_text = portal_command("text", args.portal, args.timeout, main_ref(accessibility))
                except IdentityCacheError:
                    profile_text = ""
                if "details/experience" in info and re.search(r"\bExperience\b", profile_text, re.IGNORECASE):
                    break
                time.sleep(1)
            snapshot = f"ACCESSIBILITY\n{accessibility}\n\nPROFILE TEXT\n{profile_text}"
        validate_profile(info, snapshot)
        write_cache(args.output, args.portal, info, snapshot)
    except (OSError, subprocess.TimeoutExpired, IdentityCacheError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(str(args.output.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
