#!/usr/bin/env python3
"""Shared Stop-hook guard for the find-me-a-job hunt.

Local to the career workspace: lives in <root>/.agent/hooks/ and is registered
by each supported Maestro harness. It arms only when the session cwd is the
career workspace root. Nested Maestri workers do not own ledger coordination.

It does not write the ledger. It cannot: a hook is a shell command with no
view of what happened. It guards the discipline instead.

Fires only when BOTH are true for an active ledger:
  - something under ~/career/ changed since the last time this hook ran, and
  - that change is newer than the ledger's own mtime.

That is exactly the failure mode worth catching: the hunt advanced and
nobody logged it. Silent otherwise, including when there is no active cycle.

Blocks at most once per ledger per session, so it can never loop.
"""
import json
import os
import re
import sys
import time

# Resolve the root from this file's location (<root>/.agent/hooks/this.py).
# Harness project-directory variables can point at a nested Maestri role.
CAREER = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATE = os.path.join(CAREER, "state")
STAMP = os.path.join(STATE, ".hookstamp")
WATCH = ["resumes", "reports", "jobs", "state"]
CLOSED = ("done", "applied", "abandoned")


def relevant_mtime(root, needle, ledger_path):
    newest = 0.0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            path = os.path.join(dirpath, name)
            if name.startswith(".") or path == ledger_path or needle not in name:
                continue
            try:
                m = os.path.getmtime(path)
            except OSError:
                continue
            if m > newest:
                newest = m
    return newest


def safe(token):
    """Filename-safe token. A session id or slug can carry a path separator,
    and a Stop hook that raises is worse than one that misses a reminder."""
    return re.sub(r"[^A-Za-z0-9_.-]", "_", str(token))[:80]


def phase_of(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if line.startswith("Phase:"):
                    return line.split(":", 1)[1].strip().strip("<>").lower()
                if line.startswith("## Log"):
                    break
    except OSError:
        pass
    return ""


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    session = safe(payload.get("session_id") or "nosession")

    if payload.get("stop_hook_active"):
        print("{}")
        return 0

    # Only the Maestro owns cross-seat ledger coordination. A worker can write
    # a report after another seat changes a ledger, so arming in nested role
    # directories creates false stale-ledger continuations.
    event_cwd = os.path.realpath(payload.get("cwd") or os.getcwd())
    career_root = os.path.realpath(CAREER)
    if event_cwd != career_root:
        print("{}")
        return 0

    if not os.path.isdir(STATE):
        print("{}")
        return 0

    try:
        last_run = os.path.getmtime(STAMP)
    except OSError:
        last_run = 0.0

    stale = []
    for name in sorted(os.listdir(STATE)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(STATE, name)
        phase = phase_of(path)
        # Phases are either bare ("done", "abandoned") or numbered
        # ("6-applied"). The trailing segment is the state name.
        if not phase or phase.rsplit("-", 1)[-1] in CLOSED:
            continue
        try:
            ledger_m = os.path.getmtime(path)
        except OSError:
            continue
        needle = name[:-3]
        if needle.startswith("app-"):
            needle = needle[4:]
        work = max((relevant_mtime(os.path.join(CAREER, d), needle, path)
                    for d in WATCH
                    if os.path.isdir(os.path.join(CAREER, d))), default=0.0)
        if work > last_run and work > ledger_m:
            fired = os.path.join(STATE, ".fired-%s-%s" % (session, safe(name)))
            if os.path.exists(fired):
                continue
            try:
                open(fired, "w").close()
            except OSError:
                # Cannot mark it fired, so do not fire: an unmarked block
                # would repeat every turn and trap the session in a loop.
                continue
            stale.append((name, phase))

    try:
        with open(STAMP, "w") as fh:
            fh.write(str(time.time()))
    except OSError:
        print("{}")
        return 0

    if not stale:
        print("{}")
        return 0

    lines = ["Ledger guard: work landed under ~/career/ but these ledgers did "
             "not move. Append the log line and update the head before you "
             "stop, then finish your reply."]
    for name, phase in stale:
        lines.append("  - %s (Phase: %s)" % (name, phase))
    lines.append("Format: `- HH:MM <what happened>` from `date +%H:%M`. "
                 "Append, never rewrite. If nothing happened worth logging, "
                 "touch the ledger and stop again.")

    print(json.dumps({"decision": "block", "reason": "\n".join(lines)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
