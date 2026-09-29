#!/usr/bin/env python3
"""Write or verify an atomic worker completion sentinel."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import sys


class SentinelError(RuntimeError):
    """A completion sentinel is invalid."""


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def validate_artifacts(paths: list[Path]) -> list[str]:
    resolved: list[str] = []
    for path in paths:
        if not path.is_file() or path.stat().st_size == 0:
            raise SentinelError(f"Required artifact is absent or empty: {path}")
        resolved.append(str(path.resolve()))
    return resolved


def write_sentinel(path: Path, task_id: str, status: str, artifacts: list[Path]) -> None:
    if path.exists():
        raise SentinelError(f"Sentinel already exists: {path}")
    resolved = validate_artifacts(artifacts) if status == "complete" else [str(item.resolve()) for item in artifacts]
    payload = {
        "schema_version": 1,
        "task_id": task_id,
        "status": status,
        "completed_at": now(),
        "artifacts": resolved,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def verify_sentinel(path: Path, task_id: str | None) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise SentinelError("Unsupported sentinel schema")
    if task_id and payload.get("task_id") != task_id:
        raise SentinelError(f"Sentinel task mismatch: {payload.get('task_id')}")
    if payload.get("status") not in {"complete", "blocked", "failed"}:
        raise SentinelError(f"Invalid sentinel status: {payload.get('status')}")
    if payload.get("status") == "complete":
        validate_artifacts([Path(item) for item in payload.get("artifacts", [])])


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    writer = subparsers.add_parser("write")
    writer.add_argument("--path", type=Path, required=True)
    writer.add_argument("--task-id", required=True)
    writer.add_argument("--status", choices=("complete", "blocked", "failed"), required=True)
    writer.add_argument("--artifact", action="append", type=Path, default=[])
    verifier = subparsers.add_parser("verify")
    verifier.add_argument("--path", type=Path, required=True)
    verifier.add_argument("--task-id")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        if args.command == "write":
            write_sentinel(args.path, args.task_id, args.status, args.artifact)
        else:
            verify_sentinel(args.path, args.task_id)
    except (OSError, ValueError, json.JSONDecodeError, SentinelError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(str(args.path.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
