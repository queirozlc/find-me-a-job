# ATS Analysis — resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf vs jobgether-senior-fullstack-trading-api
Segment: agency   Date: 2026-09-04

Round: layout re-review after the approved base-preamble correction. Task
`jobgether-senior-fullstack-trading-api-sieve-layout`. This report supersedes
`state/jobgether-senior-fullstack-trading-api-sieve.report.md` (17:17 local),
which was BLOCKED on one root cause: the `tabular*` role header.

Artifacts graded (all present on disk):
- PDF: `resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf` (2 pages, letter, xdvipdfmx, 0 embedded images, 28,126 bytes, built 2026-09-04 18:14:49 -03)
- Source: same directory, `Lucas-Queiroz-Resume-en.tex` (133 lines, 0 `tabular` hits)
- Raw extraction: `pdftotext Lucas-Queiroz-Resume-en.pdf -` (73 lines, one form feed at line 60)
- Layout extraction: `pdftotext -layout Lucas-Queiroz-Resume-en.pdf -` (69 lines)
- Posting: `jobs/jobgether-senior-fullstack-trading-api.md` as quoted in `state/jobgether-senior-fullstack-trading-api-review-packet.md`, captured 2026-09-04 17:01 America/Sao_Paulo from `https://www.linkedin.com/jobs/view/4461922727/`. 14 applicants. Not labeled Reposted. Not re-sourced in this round.
- Identity source: `state/hunt-2026-09-04-g-linkedin-identity.json`, unchanged since 17:01 local, `captured_at` 2026-09-04T20:01:30+00:00, `snapshot_sha256` `ea38bc6f…50b2a`. No live portal was opened.
- Deterministic gate: `state/jobgether-senior-fullstack-trading-api-deterministic-gate.json`, status PASS, 10 of 10 checks, generated 2026-09-04T21:16:01+00:00.
- Writer report: `state/jobgether-senior-fullstack-trading-api-quill-layout.report.md`.
- Application note: `resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/application-note.md`, mtime 17:09 local, unchanged by the layout round.

## Verdict
READY

## Decision Explanation
No blocking reason.

The one root cause of the prior BLOCKED verdict is gone. `\resumeSubheading`
(`.tex` lines 42-49) now prints company, title, dates, and location as four
consecutive text lines inside `\samepage`. `grep -c tabular` on the `.tex`
returns 0. `pdfimages -list` returns no rows. The preamble of the tailored
file is byte-identical to `resumes/base-en.tex` (`diff` empty), so the
`scripts/resume_gate.py` `layout` parity note from the prior report is closed.

## Delta check, prior round to this round

| Item | Prior round (17:08 build) | This round (18:14 build) | Result |
|---|---|---|---|
| Preamble | `tabular*` role header | Base preamble, single-column header | Changed, intended |
| Body from `\begin{document}` | 16 bullets, 7 metrics | Same. Every bullet, Skills line, Summary sentence, title, date, and location quoted in the prior report appears verbatim in the new raw extraction. The prior `.tex` is not retained on disk, so the body diff is confirmed by content comparison, not by `diff`. The Writer report states `diff` of old body versus new body is empty. | Unchanged |
| Review-packet delta | 6 reworded bullets, 16/16 | Identical JSON | Unchanged |
| Pages | 1 | 2 | Changed, consequence of the taller header |
| Required and preferred token placements | See prior report | Re-counted below, identical | Unchanged |

Because the body is unchanged, the Role Eligibility Check, the LinkedIn field
verification, and the Resume Evidence Check are reproduced from the prior
report after re-running the token counts on the new raw extraction. The File
Readability Check and the Recruiter Readability Score are re-graded in full.

## File Readability Check

Judged on the raw extraction.

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 73 lines of clean text across 2 pages. |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes, 0 `?`, 0 characters in U+FB00-U+FB06. Only non-ASCII characters are `•` (16) and `ó` (4). Probe words intact: `office` 2 (`back-office`), `workflow` 5. `profile`, `efficient`, `conflict` are not in this document, so 0 hits is correct. |
| 0.3 | Contact block recoverable | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. In the body, not a header or footer. No UTC offset, no time-zone sentence. |
| 0.4 | Section headers present verbatim | PASS | Standalone lines `SUMMARY` (5), `SKILLS` (10), `LANGUAGE` (18), `EXPERIENCE` (21), `EDUCATION` (68). Uppercase is `\scshape` rendering; source strings are `Summary`, `Skills`, `Language`, `Experience`, `Education`. |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks at raw lines 22, 40, 52, 60, each `Company` / `Title` / `Dates` / `Location` then its bullets, blank line between blocks. The page break falls between the two Lippaus roles; the form feed sits at the start of line 60 and page 2 opens with the complete Entry-level header plus both of its bullets. Both Lippaus roles repeat the company name, so the promotion segments unambiguously. No merge, no split. |
| 0.6 | Date parseability | PASS | Every date is `Mon YYYY - Mon YYYY` with an ASCII hyphen: `Mar 2026 - Present` (24), `Jan 2024 - Mar 2026` (42), `Jan 2023 - Jan 2024` (54), `Mar 2021 - Jan 2023` (62), `Feb 2022 - Dec 2025` (71). Each sits on the line directly after its title. |
| 0.7 | Reading order | PASS | Raw and layout streams, normalized for whitespace and blank lines, are identical (`diff` empty). Section order, role order, header line order, and bullet order all agree. |
| 0.8 | No forbidden constructs | PASS | 0 `tabular` in the `.tex`. No text box, no image of text, no contact icon, no photo. `pdfimages -list` returns zero rows. |

File Readability Check: 8 of 8 PASS.

## Role Eligibility Check

Reproduced from the prior report. The posting, the CV body, and the cached
identity snapshot are unchanged.

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | Posting: "This position is listed on behalf of a partner company, who manages all applications and next steps. Our partner is looking for a Senior Full-Stack Engineer - Trading API based in Brazil." No authorization, contract, or entity requirement stated. | not stated. `DOSSIER.md` records PJ, CLT, W-8BEN contractor, and EOR as acceptable. |
| Location or time-zone overlap | Posting: "based in Brazil"; card: "Brazil (Remote)"; benefits: "Fully remote working environment." | PASS. CV prints `Vitória, ES, Brazil`. No UTC offset and no overlap sentence on the CV. |
| Minimum years of experience | "5+ years of professional full-stack software development experience." | PASS. Summary states "5+ years of full-stack development". Cached LinkedIn span Mar 2021 to Present is 5 yrs 6 mos. |
| English proficiency requirement | Posting is silent. Posting language is English. | not stated. CV prints `English: Fluent (C1)` in the `Language` section. |
| Degree requirement | Posting is silent. | not stated. CV prints `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025`. |
| Required skill: Golang | "Strong professional experience with Golang and TypeScript/React"; "Proficiency in at least one modern systems programming language such as Golang or C#." | Present verbatim. `Go (Golang)` in Skills (11) and in the Luizalabs bullet (44). `C#` correctly absent. |
| Required skill: TypeScript | "Proficiency in TypeScript and React" | Present verbatim in Skills (11) and DexCare bullet 1 (26). |
| Required skill: React | "…including experience creating intuitive, responsive, and performant user interfaces." | Present verbatim in Skills (14) and DexCare bullet 5 (33). |
| Required skill: HTML | "Strong knowledge of HTML and modern CSS frameworks" | Present verbatim in Skills (14) and the Lippaus entry-level bullet (64). |
| Required skill: TailwindCSS or comparable | "…particularly TailwindCSS or comparable technologies." | Present verbatim. `TailwindCSS` in Skills (14) and DexCare bullet 5 (33). Source note under Match limits. |
| Required skill: SQL and relational databases | "Solid experience with SQL and relational databases, preferably PostgreSQL." | Present verbatim. `SQL` and `PostgreSQL` in Skills (11, 13); DexCare bullet 4 (31). |
| Required skill: REST APIs and API design | "Strong understanding of REST APIs and API design best practices." | Present verbatim. `REST APIs` and `API design` in Skills (12); DexCare bullet 3 (29). |
| Requirement: stakeholder requirements into features | "Demonstrated ability to gather, clarify, and translate stakeholder requirements into well-designed, fully implemented features." | Not a retrieval token. Evidence present: Lippaus mid-level bullet (58). |
| Communication, attention to detail, ownership | Soft skills. | Not graded, not tokens. |

Role Eligibility Check: no FAIL.

### LinkedIn field verification, cached snapshot of 2026-09-04T20:01:30+00:00

Headers are unchanged in content. Re-read against the same snapshot.

| CV field | CV prints | Snapshot shows | Result |
|---|---|---|---|
| Role 1 employer / title | `DexCare` / `Senior Software Engineer` | `Senior Software Engineer`, `DexCare · Full-time` | MATCH |
| Role 1 dates | `Mar 2026 - Present` | `Mar 2026 - Present · 7 mos` | MATCH |
| Role 1 location | `Remote` | `Seattle, Washington, United States · Remote` | MATCH per `CLAUDE.md` 3 |
| Role 2 employer / title | `Luizalabs` / `Mid-level Software Engineer` | `Mid-level Software Engineer`, `Luizalabs · Full-time` | MATCH |
| Role 2 dates | `Jan 2024 - Mar 2026` | `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | MATCH |
| Role 2 location | `Remote` | `São Paulo, Brazil · Remote` | MATCH per `CLAUDE.md` 3 |
| Role 3 employer / title | `Lippaus Distribuidora` / `Mid-level Software Engineer` | `Lippaus Distribuidora`, `Mid-level Software Engineer` | MATCH |
| Role 3 dates | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024 · 1 yr 1 mo` | MATCH |
| Role 3 location | `Vitória, ES, Brazil` | `Vitória, Espírito Santo, Brazil · On-site` | MATCH per `CLAUDE.md` 3 |
| Role 4 title | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | MATCH |
| Role 4 dates | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023 · 1 yr 11 mos` | MATCH |
| Education | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | `DOSSIER.md` LinkedIn ground truth 2026-09-04 | MATCH (ASCII hyphen per `CV-SPEC.md`) |

## Resume Evidence Check: 90/100, PASS

Unchanged from the prior round. Word-boundary counts re-run on the new raw
extraction and found identical. Required weight 3, preferred weight 1.

### Required tokens

| # | Token | Weight | Skills placement | Experience placement | Points |
|---|---|---|---|---|---|
| 1 | Golang | 3 | `Languages: … Go (Golang)` (11) | Luizalabs 1 (44): "Built distributed tax microservices in Go (Golang), Node.js, and Java…" | 3 |
| 2 | TypeScript | 3 | `Languages: TypeScript` (11) | DexCare 1 (26): "Built event-driven TypeScript services on Express and Koa…" | 3 |
| 3 | React | 3 | `Frontend: React` (14) | DexCare 5 (33): "…monitoring React and TailwindCSS interfaces with Datadog RUM." | 3 |
| 4 | HTML | 3 | `Frontend: … HTML` (14) | Lippaus entry-level 1 (64): "…dashboards in JavaScript, HTML, and CSS…" | 3 |
| 5 | TailwindCSS (or comparable) | 3 | `Frontend: … CSS \| TailwindCSS` (14) | DexCare 5 (33) | 3 |
| 6 | SQL / relational databases | 3 | `Languages: … SQL` (11); `Data: PostgreSQL` (13) | DexCare 4 (31): "Modeled booking reads and writes in SQL on PostgreSQL…" | 3 |
| 7 | REST APIs | 3 | `Backend: … REST APIs` (12) | DexCare 3 (29): "Built multi-tenant REST APIs with Auth0 JWT…" | 3 |
| 8 | API design | 3 | `Backend: … API design` (12) | DexCare 3 (29): "…owning API design and contracts…" | 3 |
| 9 | 5+ years full-stack | 3 | n/a, eligibility statement | Summary (6): "5+ years of full-stack development". Verified span 5 yrs 6 mos. | 3 |

Required subtotal: `sum(points * 3) = 81`, `max = 81`.

### Preferred tokens

| # | Token | Weight | Skills placement | Experience placement | Points |
|---|---|---|---|---|---|
| 1 | PostgreSQL | 1 | `Data: PostgreSQL` (13) | DexCare 4 (31) and Lippaus mid-level 1 (56) | 3 |
| 2 | Google Cloud Platform | 1 | `Cloud and operations: … Google Cloud Platform (GCP)` (15) | Luizalabs 4 (49) prints "on GCP", not the exact posting token. | 1 |
| 3 | Docker | 1 | (15) | Luizalabs 4 (49) | 3 |
| 4 | Kubernetes | 1 | (15) | Luizalabs 4 (49) | 3 |
| 5 | financial markets / fintech | 1 | absent | absent | 0 |
| 6 | algorithmic trading | 1 | absent | absent | 0 |
| 7 | startup | 1 | n/a | Lippaus entry-level 1 (65) | 2 |
| 8 | fully remote environment | 1 | n/a | `Remote` location line, DexCare (25) and Luizalabs (43) | 2 |

Preferred subtotal: `sum(points * 1) = 14`, `max = 24`.

### Score

```
coverage = 100 * (81 + 14) / (81 + 24) = 100 * 95 / 105 = 90.5 -> 90
```

Stuffing penalty: 0. Word-boundary counts on the raw extraction: `TypeScript`
3, `React` 3, `REST APIs` 3, `PostgreSQL` 3, `Go` 3, `Golang` 2, `SQL` 2,
`CSS` 2, `TailwindCSS` 2, `HTML` 2, `API design` 2, `Docker` 2, `Kubernetes`
2, `GCP` 2, `Google Cloud Platform` 1. No token at 4 or more. `workflows` 5,
not a posting token, see defect 3.

**Required tokens without Skills and Experience placement:** none.

### Absences that are correct, not defects

`C#`, `fintech`, `financial`, `trading`, `mentor`, `code review`, `Ruby`,
`Rails`, `Sidekiq`, `ActiveRecord`, `RSpec`, `UTC`, `GMT`, `time zone`,
`timezone`, `overlap` all return 0 hits. The protected claim `code-review`
(status `unverified`) is absent, as required. Spoken-language proficiency
appears only under `LANGUAGE` (19). PASS.

### Experience completeness

Deterministic gate `experience_completeness` PASS, 16 base bullets, 16
tailored bullets. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% all present at
raw lines 28, 30, 33, 37, 46, 48, 57. The six rewordings were judged in the
prior report and are unchanged; each stays inside the recorded facts.

## Recruiter Readability Score: 91/100

Re-graded on the two-page build.

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 15/15 | `Senior Software Engineer` and `full-stack` on raw line 6 of 73 (8%). The CV keeps the LinkedIn-true title, as `CLAUDE.md` 1 requires. |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | 12/20 | Unchanged. DexCare bullets 1 (TypeScript services) and 3 (REST APIs, API design) carry posting tokens; bullet 2 (Epic EMR) carries none. Frontend proof (React, TailwindCSS) sits at bullet 5, SQL/PostgreSQL at bullet 4. |
| 3.3 | Every bullet starts with a past-tense action verb and describes an outcome | 15/15 | All 16 bullets: Built, Integrated, Built, Modeled, Reduced, Built, Helped implement, Built, Moved, Built, Deployed, Built, Processed, Led, Developed, Built. Summary uses `I`. |
| 3.4 | At least 3 bullets carry a real, defensible number | 15/15 | Seven bullets, seven metrics, each traced to `DOSSIER.md`. |
| 3.5 | Experience completeness, page count | 10/10 | Nothing removed, 16 of 16. Two pages. The complete content with the approved single-column header does not fit one page; the Writer report states the corrected base also builds to two pages. `CLAUDE.md` 9.1 and `CV-SPEC.md` Length allow two pages in this case. |
| 3.6 | No unsupported buzzwords | 10/10 | No "team player", "results-driven", or "passionate". |
| 3.7 | Skills grouped by category | 10/10 | Six labelled groups. |
| 3.8 | Scannable spacing and white space | 4/5 | Headers bold and consistent; each header stays with its first bullet (`\samepage`, `\nopagebreak`). In the layout stream the last bullet of a role and the next header remain on adjacent lines (layout 38-39, 49-50, 56-57); `\resumeRoleGap` is 3pt. Page 2 carries 13 non-blank lines: the Entry-level Lippaus role and Education. |

## Application note inspection

`application-note.md` was read in full (52 lines). Findings:

| Line | Claim | Source checked | Result |
|---|---|---|---|
| 3 | `Status: DRAFT. Lucas sends it. No agent sends it.` | n/a | No statement that a submission occurred. Correct. |
| 5-6 | LinkedIn Easy Apply; Jobgether runs an AI matching process and forwards a shortlist | Posting card and "How Jobgether Works" paragraph | Sourced. |
| 15-17 | DexCare stack, Epic EMR, 33% SPI, Luizalabs Go/Node.js/Java, SEFAZ BullMQ 20%, Docker/Kubernetes on GCP through ArgoCD, Lippaus scoping | `DOSSIER.md` lines 62-79, 130-148; cached LinkedIn snapshot | Sourced. |
| 19 | "I work fully remote from Vitória, Brazil, and I own features from design through deployment." | Snapshot DexCare and Luizalabs `Remote`; `DOSSIER.md` 136 "customer-facing features end to end"; snapshot Lippaus "Delivered customer-facing features and internal tools end-to-end" | Supported. The wording mirrors the posting's "from design through deployment". No new fact. |
| 32 | `Time zone GMT-3` | `DOSSIER.md` 111; `CLAUDE.md` 3 allows it in screening answers only | Correct placement. Not on the CV. |
| 36 | "TypeScript, Node.js, and React also at Lippaus and Luizalabs" | Snapshot `Technologies:` lines for Luizalabs and Lippaus | Sourced. |
| 38 | TailwindCSS "Placed under the AGENTS.md section 4 match policy for ecosystem tokens (fix round 1, 2026-09-04)" | `AGENTS.md` section 4 is Match policy | Reference is accurate. This is internal provenance text inside a Lucas-facing screening answer, see defect 4. |
| 39, 44, 45, 48, 50, 52 | C#, fintech, algorithmic trading, mentoring, salary, notice period: "not recorded in the dossier. Lucas answers this himself." | `DOSSIER.md` 40 (notice period not recorded); no dossier entry for the others | Correct. No invented answer. |
| 42 | AWS S3, RDS, Secrets Manager, STS through AWS SDK v3 | `DOSSIER.md` 72 (S3, STS, Secrets Manager, RDS Signer) | Sourced. |
| 49 | Contract types PJ with own CNPJ, W-8BEN, CLT, EOR | `DOSSIER.md` 38-39 | Sourced. |
| 51 | English Fluent (C1), daily English-only work with US teams at DexCare | `DOSSIER.md` 36-37 | Sourced. |

No unsourced personal claim found. No statement that a submission occurred.

## Defects, ranked by cost

1. **Frontend proof is fifth in the DexCare block** — Recruiter Readability 3.2 — not blocking. Move "Reduced release risk by 7% by shipping behind LaunchDarkly/OpenFeature flags and monitoring React and TailwindCSS interfaces with Datadog RUM." to position 2 or 3, ahead of "Integrated Epic EMR time-slot flows…". Reorder only.
2. **`Google Cloud Platform` has Skills placement only** — Resume Evidence Check, preferred, not blocking. In Luizalabs bullet 4 print "on Google Cloud Platform (GCP)" in place of "on GCP". Raises coverage from 90 to 92.
3. **`workflows` appears 5 times** — human-scan repetition, not a rubric penalty. Optional: reword "fiscal workflows" (47) or "workflows of a beverage distribution startup" (65).
4. **Internal provenance text in a screening answer** — application note line 38 — not blocking. The clause "Placed under the AGENTS.md section 4 match policy for ecosystem tokens (fix round 1, 2026-09-04)" is process context, not an answer Lucas would paste. Move it to a note-level remark or drop it before Lucas uses the answer.
5. **Thin second page and tight role gap** — Recruiter Readability 3.8 — not blocking. Page 2 holds 13 lines. `\resumeRoleGap` lives in the shared base preamble, so any change is a base decision, not a per-application fix.

## Match limits

- Preferred tokens not placed: `financial markets` / `fintech` (0), `algorithmic trading` (0). No approved source records trading, market data, or fintech work. Do not add these without Lucas.
- `Google Cloud Platform` at 1 point, see defect 2.
- `TailwindCSS` is placed on the DexCare React frontend under the match policy for ecosystem tokens. `DOSSIER.md` and the cached LinkedIn snapshot list the DexCare frontend as React and do not name a CSS framework. This review does not reject the token. It records that the source is policy, so Lucas can confirm it in the screening answer where the note already states it.
- Posting title `Senior Full-Stack Engineer` is not printed; the CV prints the LinkedIn title `Senior Software Engineer` with "full-stack development" in the Summary, as the title rule requires.
