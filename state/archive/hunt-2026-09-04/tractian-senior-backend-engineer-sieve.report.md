# Sieve task result — tractian-senior-backend-engineer

Role: ATS Analyzer. Graded, did not edit the CV.
Date: 2026-09-04
Hunt: 2026-09-04
Application: TRACTIAN, Senior Backend Engineer
Posting: https://www.linkedin.com/jobs/view/4443416703/ (text read from the local job file, the
URL itself was not re-opened)
Full gate report: `reports/tractian-senior-backend-engineer-gate.md`

## Verdict

**BLOCKED.** Do not deliver this CV to Lucas yet. Three blockers, one of which cannot be fixed
by the Architect alone.

- Gate 0 — Parse integrity: **8/8 PASS**
- Gate 1 — Knockouts: **FAIL**, on Portuguese fluency
- Gate 2 — Retrieval coverage: **67/100, FAIL**, on non-relational database placement and on
  the absent Portuguese token
- Gate 3 — Human scan: **93/100**
- Factual integrity against live LinkedIn: **FAIL**, two role date ranges

No blended score is emitted. There is no such thing as a vendor ATS score out of 100.

## Files under test

- CV source: `resumes/hunts/2026-09-04/tractian-senior-backend-engineer/Lucas-Queiroz-Resume-en.tex`
- CV PDF: `resumes/hunts/2026-09-04/tractian-senior-backend-engineer/Lucas-Queiroz-Resume-en.pdf`
- Both artifacts exist. The mandatory extraction ran first, on the real PDF:
  `pdftotext -layout` and `pdftotext` raw. Gate 0 and Gate 2 were judged on the raw stream,
  64 lines, 1 page.

## Fix list for the Architect

Blocking, in order.

1. `Lucas-Queiroz-Resume-en.tex` line 70. Change `{DexCare}{Jan 2026 - Present}` to
   `{DexCare}{Mar 2026 - Present}`. Live LinkedIn reads `Mar 2026 - Present · 7 mos`.

2. `Lucas-Queiroz-Resume-en.tex` line 82. Change `{Luizalabs}{Jan 2024 - Jan 2026}` to
   `{Luizalabs}{Jan 2024 - Mar 2026}`. Live LinkedIn reads `Jan 2024 - Mar 2026 · 2 yrs 3 mos`.

3. Place `DynamoDB` in one DexCare Experience bullet. Today it sits in `Skills` only, on raw
   line 13. The posting requires "both relational ... and non-relational databases", which is
   cumulative, so the non-relational half must reach `Skills` plus one `Experience` bullet.
   Suggested host, source line 73, the real-time booking and availability bullet. `DynamoDB` and
   `DynamoDB Streams` are observed DexCare stack in `DOSSIER.md` and `CV-SPEC.md`, so no new
   fact is needed. Do not claim ScyllaDB, Cassandra, MongoDB or ClickHouse.

4. Portuguese fluency. **Not fixable from current sources. Escalate, do not invent.** The
   posting Requirements block states "Fluency in Portuguese." The CV carries zero Portuguese
   tokens. `DOSSIER.md` records only "English proficiency: Advanced / C1" and states no
   Portuguese level. Brazilian location and Brazilian employers are location and employer facts,
   and RUBRIC Gate 1 forbids inferring evidence from them. Lucas must state his Portuguese
   level, it must be recorded in `DOSSIER.md`, and only then may the exact token go into the
   Skills communication group on line 64 of the source, plus one Experience bullet context.

Non-blocking, worth doing in the same pass.

5. Cut one `React` and one `multi-tenant` occurrence. `React` appears 5 times, `multi-tenant` 4.
   CV-SPEC caps any term at 3. This is -10 on Gate 2 today and recovers to 77/100 once fixed.
   Lowest-value hits: the Summary `React` on source line 55, and one of the two DexCare
   `multi-tenant` uses on source lines 75 and 78.

6. `AWS` sits in the Summary and in Skills with no Experience placement. It is not a TRACTIAN
   requirement, so it costs nothing here, but it breaks the CV-SPEC rule that every load-bearing
   technology also appears in an Experience bullet.

7. Widen `\resumeRoleGap` beyond `\vspace{2pt}`. In the layout extraction the last bullet of
   each role sits directly above the next company name. Parse safety is fine, Gate 0.5 passes.
   This is a human-scan cost of 2 points, and about 15% of the page is unused.

## Not for the Architect

`DOSSIER.md` "LinkedIn ground truth", captured 2026-09-01, is now **stale** on two rows.
LinkedIn was changed after that capture, and its own duration labels are self-consistent with
today's date. Until the Maestro or Lucas refreshes that block, every future tailoring run will
reintroduce fixes 1 and 2. I did not edit `DOSSIER.md`; the ATS Analyzer does not write career
sources.

## Verification performed

LinkedIn, read-only through the `Profile Check` portal on 2026-09-04. No edit action was sent.
- https://www.linkedin.com/in/queiroz-lucas/details/experience/
- https://www.linkedin.com/in/queiroz-lucas/details/education/

Matched exactly: all four employers, all four job titles, both Lippaus date ranges, and the
FAESA education row (`Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025`; the CV's
ASCII hyphen is correct per CLAUDE.md rule 1 and CV-SPEC section 5).
Mismatched: the DexCare start month and the Luizalabs end month.

All seven CV metrics trace to `DOSSIER.md` "Bullet metrics supplied by Lucas 2026-09-01":
15%, 25%, 7%, 33%, 20%, 18%, 26%. None is invented and none is rounded. The Summary's
`5+ years` is arithmetic on the LinkedIn dates, Mar 2021 to Sep 2026, 5 yrs 6 mos, and it
survives the date correction. It is reported as derived, not as a dossier fact.

The four PDFs under `~/Documents/Resumes/` were not opened. They are invalid sources.

## Policy checks passed

Zero Ruby or Rails tokens. Zero UTC offset or time-zone overlap statement. Degree
`Information Systems`, FAESA. Location `Vitória, ES, Brazil`, nothing more. Lippaus prints
`Vitória, ES, Brazil`; DexCare and Luizalabs print `Remote`. No contract detail printed. Bullet
voice first person, past tense, subject omitted, on all 12 bullets; Summary uses `I`. English
only, matching the posting language. AI mention present in Summary and in one DexCare bullet.
The Architect claimed no unsupported alternative: zero Kafka, Python, Rust, ClickHouse,
ScyllaDB, Cassandra, MongoDB.

## One ambiguity, reported and left open

`DOSSIER.md` reads "**DexCare messaging: RabbitMQ / AMQP** used on services. Skills token only
(`RabbitMQ`, `AMQP`), no service names on the CV." The restriction that sentence names is
service names, and the CV names no DexCare service, so the current DexCare RabbitMQ bullet
complies on that reading. A stricter reading of "Skills token only" would forbid the Experience
placement, which would conflict with the Maestro brief and with RUBRIC Gate 2, both of which
demand both placements for a required token. Lucas or the Maestro should settle the wording.
I did not guess.

## Not observable

The segment; the posting file records `Segment: not observable` and `Company origin: not
stated`. Work authorization and time-zone requirements; the posting states neither. Which ATS
TRACTIAN runs, and therefore which parser handles this file.

## Recommended next step

Return the CV to the Resume Architect with fixes 1, 2 and 3, and escalate fix 4 to Lucas in
parallel. Re-run all four gates after the rebuild.

Projected Gate 2, recomputed with the RUBRIC formula:
- Today: required points 22 of 27, coverage 77, minus the 10-point stuffing penalty, **67/100,
  FAIL**.
- After fixes 3 and 5, with Portuguese still absent: required points 24 of 27, coverage
  `100 * (24*3 + 1) / 87` = **84/100**. Still **FAIL**, because Portuguese remains a required
  token at 0.
- After fixes 3, 4 and 5 together: required points 27 of 27, coverage
  `100 * (27*3 + 1) / 87` = **94/100, PASS**.

Gate 2 clears only when Lucas supplies his Portuguese proficiency level. So does Gate 1. Fixes
1 and 2 change no gate score; they are factual-integrity blockers under CLAUDE.md rule 1 and
must be made regardless.
