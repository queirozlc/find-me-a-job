# find-me-a-job config

Written by `/find-me-a-job init` on 2026-09-01, revised by Lucas on
2026-09-02. This file is the cache. A hunt never re-detects what is recorded
here. One `/find-me-a-job` execution is a **hunt**; the per-posting pipeline
is an **application**.

## Candidate

- Dossier: `~/career/DOSSIER.md`
- Knowledge base: `~/career/ATS-KNOWLEDGE.md`
- Rubric: `~/career/RUBRIC.md`
- Base CV: `~/career/resumes/base-en.tex` and `base-pt.tex`, built to `CV-SPEC.md`.
  Seed template (Rails-era, untrusted content): `~/career/resumes/template-rails-original.tex`.

## Segments, in weight order

1. `us-direct` — US companies contracting **directly** into LatAm, no
   consultancy in the middle. Top weight.
2. `br-pj` — Brazilian companies hiring PJ. **Equal top weight** with
   `us-direct`.
3. `agency` — consultancies and agencies. Third.

Seniority target: Senior preferred. A strong Mid role is acceptable.

## Sourcing

- Recency cut: **past 24h first, past week is the widest acceptable window.**
  Never widen it to manufacture volume.
- Reject every role labeled `Reposted`.
- Reject every role that states `Over 100 applicants`, `100+ applicants`, or
  that more than 100 people clicked Apply. An absent count is not observable.
- Surfaces: `jobs-tab`, `posts`
- Shortlist size per hunt: **5**
- Surfaces per hunt: both. One Scout seat runs them one after the other,
  Jobs first. Triage the Jobs shortlist as soon as it lands; do not wait for
  Posts.
- Approval mode: `auto-advance`. Every posting that passes Maestro triage is
  approved for tailoring (Lucas, 2026-09-04).
- Pipeline: two streaming waves. Wave 1 starts from accepted Jobs-tab results
  while the source runner searches Posts. Wave 2 starts from accepted Posts results.
- Source command: `python3 scripts/linkedin_source.py --config
  scripts/linkedin-source.example.json run --output-dir state/source-<hunt-id>`.
  `preflight.jsonl` is the live triage queue. `run.complete.json` is the source
  completion sentinel. The full `events.jsonl` remains the audit record.
- Triage knockouts, dropped by Maestro before any tailoring (Lucas,
  2026-09-04): `Reposted`; over 100 applicants or Apply clicks; company
  blocklist **BairesDev**;
  hybrid or on-site anywhere; primary language or runtime outside JavaScript,
  TypeScript, Node.js, and Go; posting knockouts (work authorization, "not for
  freelancers" with no CLT/EOR path, mandatory location). Ruby or Rails,
  Java-first, Python-first, PHP-first, and C# or .NET-first postings are
  outside the primary stack. Frameworks do not decide eligibility. Triage is
  never skipped.
- Quote characters in queries: straight ASCII only
- Query template: `("<stack>" or "<stack>") AND "<seniority>" AND "<region>"`
- Working example, verified live:
  `("javascript" or "typescript") AND "latam" AND "hiring"`

## Portals

**Created by Lucas in the Maestri UI with storage "Shared Globally"**, not by
the CLI. A UI portal with that storage keeps its LinkedIn session across
restarts; a CLI-created one does not, because `maestri portal create` has no
storage option (verified 2026-09-01: only URL, name, `--size`, `--simulator`,
and nothing at top level). Init asks for them and then runs `maestri connect`.

The source runner owns the search portals during a hunt. Never reuse a search
portal for profile work.

| Portal name | Surface | Owned by |
| ----------- | ------- | -------- |
| `Jobs Search` | LinkedIn Jobs tab | Source runner |
| `Post Search` | LinkedIn content search | Source runner | (live name on the canvas, singular, observed 2026-09-02) |
| `Profile Check` | Lucas's LinkedIn profile, read-only | Sieve |

`Profile Check` exists so the Analyzer can verify titles, dates and company
names on a CV against the live profile (Lucas, 2026-09-01). Sieve reads it and
never edits the profile. It is not a search portal.

Verified Posts-search URL shape:

```
https://www.linkedin.com/search/results/content/?keywords=<encoded>&origin=FACETED_SEARCH&datePosted=["past-24h"]
```

Set **Sort by = Latest**, never Top match. Top match reorders away from
recency and defeats the cut.

Verified Jobs-tab parameters, read from the live portal on 2026-09-02:

- Past 24 hours: `f_TPR=r86400`.
- Keyword query: `keywords=<URL-encoded query>`.
- The Remote control did not retain a distinct URL parameter.
- No sort control or sort parameter was observable.

## Seats

Harness assignment follows task weight: Claude for coordination and heavy
reasoning, Codex for light portal manipulation. Commands verified on
2026-09-01, see **Harness reference** below.

| Seat | Agent | Role | When | Launch command | Reset cmd |
| ---- | ----- | ---- | ---- | -------------- | --------- |
| Maestro | Recruiter | — | Always | `claude --model fable --effort high` (Lucas, 2026-09-02: Claude runs the Maestro seat) | `/clear` |
| ATS Analyzer | Sieve | `ATS Analyzer` | Every application | `claude --model fable --effort high` for routine Posting Analysis; `claude --model opus --effort high` only for unresolved semantic ambiguity | `/clear` |
| Resume Architect | Quill | `Resume Architect` | Every application | `claude --dangerously-skip-permissions --model "claude-fable-5-1[1m]" --effort medium` (swapped by Lucas 2026-09-04, observed live) | `/clear` |
| Market Scout | Kestrel | `Market Scout` | Fallback only when the deterministic source runner cannot parse a LinkedIn layout | `codex -m gpt-5.6-luna -c model_reasoning_effort=high -c service_tier=fast` | `/new` |
| Profile SEO | Codex | — | Only when the profile itself needs work. Not part of the application. | unchanged (luna, fast) | `/new` |

**Active seats start fresh every hunt** (decision by Lucas, 2026-09-01). If a seat
already exists on the canvas, swap it in place with `maestri recruit "<name>"
--command "<launch command>" --replace "<name>"` instead of adding a terminal.
Otherwise:
Step 0 recruits Quill and the routine Sieve with `maestri recruit "<name>"
--role "<role>" --command "<launch command>" --dir ~/career`. Recruit Kestrel
only after a parser failure. The source runner uses the existing search
portals directly. Nothing from an earlier canvas is reused. Codex seats show a
directory-trust prompt on boot; answer it with two raw calls:
`maestri ask "<name>" --raw "1"` then `maestri ask "<name>" --raw "\x0d"`.
Every raw send is two calls, text first and Enter alone second. One call
with text and terminator together arrives as a paste and the terminator
becomes a line break; the command sits unsent (verified 2026-09-02, both
`\n` and `\x0d`). Send only to an idle seat and confirm the composer is
empty with `maestri check`.

## Maestro harness and background dispatch

Claude Code runs the Maestro seat. It has `run_in_background` and `Monitor`,
so every dispatch is a tracked handle.

If Codex ever runs the Maestro seat, it must use a persistent unified exec
session for every dispatch that carries work. Start this foreground command
through `exec_command` with `yield_time_ms` near 1000. Do not put `&` inside
the command:

```
maestri ask "<seat>" "<prompt>" > ~/career/state/<slug>-<seat>.out 2>&1
```

`exec_command` returns a session ID while the ask runs. Record the session ID
in the active ledger immediately. Poll the same session with empty
`write_stdin` calls every 20 to 30 seconds until it exits. If Lucas sends a
message, the active poll can stop, but the exec session stays alive. Resume
the same session ID.

Completion requires the exec session to exit and the `.out` file to contain
the final reply. `maestri check` is a progress view, never the result. Never
copy a screen dump into a `.out` file.

Maestri can return only the visible terminal screen for a long reply. When a
worker report can exceed one screen, include a separate
`~/career/state/<slug>-<seat>.report.md` path in the original prompt. The
worker writes the complete report there and returns only a short status plus
that path. Completion requires the exec session to exit, the `.out` transport
reply to be non-empty, and the `.report.md` artifact to be complete. Read the
report artifact before the next decision. The worker never uses `maestri ask`
to report back.

Never append `&` inside the Codex exec command. Observed 2026-09-04: the
parent shell exited, the process handle disappeared, the output file stayed
empty, and Kestrel continued with no result channel. If this has already
happened, do not resend the work. Run a persistent monitor session until the
seat is idle. Then send one report-only ask through the correct persistent
exec-session form and capture its reply to the original `.out` path. If that
reply is truncated, send one report-save ask that writes the complete report
artifact and returns only its path. Do not repeat the underlying work.

Observed 2026-09-02: a Codex Maestro skipped triage, wrote a screen dump into
Quill's `.out`, and let Quill fan out five subagents nobody polled.

## Delivery shape

- Order per application (Lucas, 2026-09-29): intake, Posting Analysis
  (Sieve), go/no-go (Maestro), build (Quill), verification (script). See
  `RUBRIC.md`.
- One posting per Architect dispatch. The Architect never spawns subagents.
- One posting per Analyzer dispatch.
- Sieve analyzes posting N+1 while Quill builds posting N. Only `GO`
  postings reach Quill. `ASK` questions go to Lucas in one batch per wave.
- `batch` means a surface wave or queue. It never means multiple postings in
  one worker dispatch.
- Tailored files go under
  `resumes/hunts/<YYYY-MM-DD>/<company-role>/Lucas-Queiroz-Resume-<lang>.{tex,pdf}`.
- `resumes/hunts/<YYYY-MM-DD>/README.md` maps every role to its exact job link,
  PDF, and status. Use the LinkedIn job URL when it exists. For a post without
  a permalink, use the observed external apply link. Application ledgers and
  the hunt summary use the same links and path.
- Base CVs and prior files under `resumes/archive/` stay untouched.
- Cache the LinkedIn profile once per hunt at
  `state/<hunt-id>-linkedin-identity.json` with
  `scripts/cache_linkedin_identity.py`. Every application in that hunt uses
  the same cache. Nobody reads the portal again for each CV.
- Sieve writes the spec, `state/<application>-manifest.json`, before the
  build. Quill executes it and adds nothing outside it.
- Run `scripts/resume_gate.py` after each build. It verifies PDF extraction,
  identity fields, token and spec placement, blacklist, GAP tokens, required
  coverage, forbidden terms, base Experience completeness, metrics, approved
  layout, and `claim-allowlist.json`. A FAIL goes back to Quill, two rounds
  maximum. No LLM review runs after the build.
- Every Quill and Sieve task writes an atomic completion sentinel with
  `scripts/worker_sentinel.py`. The terminal reply is secondary evidence.
- One language per tailored CV, decided by Maestro at intake. See `CV-SPEC.md`.
- CV voice: first person, past tense, subject omitted in bullets; `I` in the
  Summary. See `CV-SPEC.md` and `CLAUDE.md` section 9.
- Never trim Experience. Preserve every verified base role, bullet, and metric.
  Page count does not override this rule.
- Put proficiency in a separate `Language` or `Idiomas` section:
  `Portuguese: Native` and `English: Fluent (C1)`.

## Ledger guard

- Shared script: `~/career/.agent/hooks/job-ledger-guard.py`.
- Claude Code registration: `~/career/.claude/settings.json`, `Stop` event.
- Codex registration: `~/career/.codex/hooks.json`, `Stop` event.
- Both registrations are synchronous and local to this workspace.
- The guard arms only for a Maestro whose cwd is exactly `~/career`. It stays
  silent in nested Maestri worker directories.
- It compares each active ledger only with artifacts that contain that hunt or
  application slug. Concurrent work on another application does not stale it.
- Codex must review and trust the exact project hook through `/hooks` after a
  definition change.

## Harness reference (verified 2026-09-01)

Do not guess these. Each was checked against the live CLI.

- `claude --model <alias|full name>` — aliases `fable`, `opus`, `sonnet`, or a
  full name such as `claude-fable-5`.
- `claude --effort <low|medium|high|xhigh|max>`.
- `codex -m <model>` — `gpt-5.6-luna` and `gpt-5.6-sol` both confirmed by
  running a real prompt.
- `codex -c model_reasoning_effort="<low|medium|high>"` — this is the correct
  key. `reasoning_model_effort` is **not** a key.
- `codex -c service_tier="fast"` — correct key, taken from the live
  `~/.codex/config.toml`.
- `codex --strict-config` does **not** reject unknown `-c` overrides in
  0.152.0, so it cannot be used to validate a key name. Run the model.

## Review checks

- **Before the build.** Posting Analysis returns `GO`: Role Eligibility
  passes and projected required coverage is at least 70. See `RUBRIC.md`
  Part 1 and `CLAUDE.md` section 4.1.
- **After the build.** `resume_gate.py` passes (`RUBRIC.md` Part 2). A failed
  check means no package.
- **Reported, not blocking.** Preferred coverage travels with the package.
- **Required explanation.** Every `NO-GO` or `ASK` quotes the exact posting
  requirement, the evidence checked, and one next action.

## Delivery

Agents **never** submit an application, never send a recruiter message, and
never click a submit button. The terminal agent action is one Maestri note per
position, filed in the `Applications` fichário, plus `maestri notify`.

## Notes

- Languages: EN and PT-BR always. Add ES when the posting is Spanish; many
  LatAm recruiter posts are.
- Contract types available: to be confirmed in the dossier.
- **Never** set LinkedIn Open to Work to "All members". Recruiters only,
  workplace type Remote.
