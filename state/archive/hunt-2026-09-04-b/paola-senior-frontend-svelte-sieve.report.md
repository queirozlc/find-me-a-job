# ATS Analysis — resumes/hunts/2026-09-04-b/paola-senior-frontend-svelte/Lucas-Queiroz-Resume-en.pdf vs paola-senior-frontend-svelte
Segment: agency   Date: 2026-09-04

Analyst: Sieve, ATS Analyzer. No file was edited. No subagent was spawned.

## Artifacts under test

- Source: `resumes/hunts/2026-09-04-b/paola-senior-frontend-svelte/Lucas-Queiroz-Resume-en.tex`
- PDF: `resumes/hunts/2026-09-04-b/paola-senior-frontend-svelte/Lucas-Queiroz-Resume-en.pdf` (1 page, 612x792 pt, xdvipdfmx)
- Raw extraction: `pdftotext Lucas-Queiroz-Resume-en.pdf -` (64 lines)
- Layout extraction: `pdftotext -layout Lucas-Queiroz-Resume-en.pdf -` (60 lines)

Gate 0 and Gate 2 were judged on the raw extraction, per RUBRIC.

## Verdict

**BLOCKED at Gate 1.** The posting names Svelte as a must-have. The token is
absent from the resume: 0 occurrences in the raw extraction and 0 in the
`.tex` source. Gate 2 fails on the same token.

Gate 0 PASS. Gate 1 FAIL. Gate 2 64/100 FAIL. Gate 3 60/100.

## Profile Check — LinkedIn verification

Read from the live English profile through the `Profile Check` portal on
2026-09-04: `linkedin.com/in/queiroz-lucas/details/experience/` and the
Education card. Every employer, title, and start and end month on the CV
matches LinkedIn.

| CV line | LinkedIn | Result |
|---|---|---|
| `DexCare` / `Senior Software Engineer` / `Mar 2026 - Present` | Senior Software Engineer, DexCare, Full-time, Mar 2026 - Present, Seattle, Washington, United States, Remote | MATCH |
| `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Mar 2026` | Mid-level Software Engineer, Luizalabs, Full-time, Jan 2024 - Mar 2026, São Paulo, Brazil, Remote | MATCH |
| `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | Lippaus Distribuidora, Full-time, 2 yrs 11 mos, Vitória, Espírito Santo, Brazil, On-site; sub-role Mid-level Software Engineer, Jan 2023 - Jan 2024 | MATCH |
| `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | sub-role Entry-level Fullstack Software Engineer, Mar 2021 - Jan 2023 | MATCH |
| `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | FAESA, Bachelor's degree , Information Systems, Feb 2022 – Dec 2025 | MATCH |

Separator glyph: the CV prints an ASCII hyphen everywhere, per CV-SPEC item 5.
LinkedIn renders an EN DASH on the Education card. AGENTS.md rule 1 states the
rule is about the periods, not the glyphs. No defect.

Role locations print `Remote` for DexCare and Luizalabs, `Vitória, ES, Brazil`
for both Lippaus roles. This matches AGENTS.md section 3. The profile was not
edited.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 64 non-empty raw lines extracted |
| 0.2 | Glyph integrity | PASS | 0 null bytes, 0 U+FFFD, 0 ligature codepoints (U+FB00-FB04). Only non-ASCII characters are `ó` (x4) and `•` (x16). `office` extracts 2 times, `workflow` 5 times |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. No UTC offset, no overlap statement |
| 0.4 | Section headers verbatim | PASS | Standalone raw lines: `SUMMARY` (5), `SKILLS` (11), `LANGUAGE` (20), `EXPERIENCE` (23), `EDUCATION` (61). Uppercase rendering is allowed |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks in the raw stream. Company on its own line, then `Title \| Location \| Dates`, then bullets, then a blank line: DexCare (24-37), Luizalabs (39-47), Lippaus Mid-level (49-53), Lippaus Entry-level (55-59). No merge, no split. Single-column header, no `tabular*` in the source |
| 0.6 | Date parseability | PASS | Every role carries `Mon YYYY - Mon YYYY` on the same line as its title. Education line 63 carries `Feb 2022 - Dec 2025` |
| 0.7 | Reading order | PASS | Token-normalised diff of raw against layout is empty. The two extractions agree on every block |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` returns zero images. No `tabular`, no text box, no icon, no photo in the source |

Gate 0 is clean. This document survives extraction.

## Gate 1 — Knockouts

Posting terms are quoted from `jobs/paola-senior-frontend-svelte.md`.

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | Posting states `Remote Contract`, `Paid in USD`. It states no work-authorization or entity requirement | not stated |
| Location | Posting: `Open to candidates across Latin America`. Resume prints `Vitória, ES, Brazil` | PASS |
| Time-zone overlap | Posting is silent | not stated |
| Minimum years of experience | Posting: `5+ years of frontend experience`. Resume Summary: `I am a Senior Software Engineer with 5+ years building TypeScript, JavaScript, React, Node.js, and Go products` | PASS, weak. See defect 2 |
| English proficiency requirement | Posting says `strong communication skills`. It names no English level | not stated |
| Required skill: JavaScript | Skills line 12 and Experience line 57 | PASS |
| Required skill: TypeScript | Skills line 12 and Experience line 26 | PASS |
| Required skill: Svelte | Posting: `Must-have: JavaScript, TypeScript, Svelte` | **FAIL** |
| Degree requirement | Posting is silent | not stated |

**Blocking failure.** `grep -oi svelte` returns 0 hits on the raw extraction
and 0 hits on the `.tex`. The resume carries no Svelte evidence in Skills, in
Summary, or in any Experience bullet.

DOSSIER.md records no Svelte fact. The Architect did not fabricate one. That
is the correct behaviour under AGENTS.md section 4 and the role separation in
section 5. The gap is a candidate-fact gap, not a writing defect. Clearing it
needs a new DOSSIER entry from Lucas, or the application is abandoned. Sieve
does not decide that.

## Gate 2 — Retrieval coverage: 64/100, FAIL

Requirement classification uses the posting's own words: `Must-have` is
required, `Nice-to-have` is preferred. Soft skills are discarded from the
scored table per RUBRIC step 1 and reported separately below.

| Token | Class | Weight | Skills placement | Experience placement | Points |
|---|---|---|---|---|---|
| JavaScript | required | 3 | `Languages: TypeScript \| JavaScript \| Node.js \| Go` (line 12) | `Developed internal back-office dashboards in JavaScript ...` (line 57) | 3 |
| TypeScript | required | 3 | `Languages: ...` (line 12) | `Built event-driven TypeScript services on Express and Koa ...` (line 26) | 3 |
| **Svelte** | required | 3 | absent | absent | **0** |
| Node.js | preferred | 1 | `Languages: ...` (line 12) | `Built distributed tax microservices in Node.js, Java, and Go ...` (line 41) | 3 |
| AWS Lambda | preferred | 1 | absent as an exact token. `AWS` alone is on line 16 | absent as an exact token. `AWS SDK v3` is on line 32 | 0 |

Arithmetic:

```
numerator   = (3x3) + (3x3) + (0x3) + (3x1) + (0x1) = 21
denominator = 3 x (3 + 3 + 3 + 1 + 1)               = 33
coverage    = 100 x 21 / 33                         = 63.6 -> 64
```

**Stuffing penalty: 0.** No token reaches 4 occurrences. Counts on the raw
extraction: TypeScript 3, JavaScript 3, Node.js 3, React 3, AWS 3, UX 3,
PostgreSQL 3, BullMQ 3. The 3-appearance cap in CV-SPEC holds exactly.

**Required tokens without Skills and Experience placement: Svelte.**

**Preferred coverage: 1 of 2 placed.** Node.js scores the full 3. AWS Lambda
scores 0. DOSSIER.md records AWS SDK v3 for S3, STS, Secrets Manager, and RDS
Signer. It records no Lambda fact, so the absence is correct, not a defect.

`grep -ic 'ruby\|rails'` on the raw extraction returns 0. AGENTS.md section 2
holds.

## Gate 3 — Human scan: 60/100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 0 / 15 | The posting's target title is `Senior Frontend Developer`. It does not appear. Raw line 6 carries `Senior Software Engineer`, which is inside the top 15% but is a different title |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 0 / 20 | DexCare bullets 1-3 are backend: event-driven services on Express and Koa, Epic EMR time-slot flows, multi-tenant REST APIs with Auth0. The only frontend bullet in the role is bullet 5, `monitoring the React UX with Datadog RUM` |
| 3.3 | Past-tense action verb, outcome described | 15 / 15 | All 16 bullets open with `Built` (x7), `Integrated`, `Modeled`, `Reduced`, `Helped`, `Moved`, `Deployed`, `Processed`, `Led`, `Developed`. Subject omitted, no present tense, no `Responsible for` |
| 3.4 | At least 3 bullets carry a real number | 15 / 15 | Seven: 15%, 25%, 7%, 33%, 20%, 18%, 26% |
| 3.5 | Experience completeness | 10 / 10 | 16 bullets in the tailored file, 16 in `resumes/base-en.tex`. All four roles and all seven metrics preserved. 1 page |
| 3.6 | No unsupported buzzwords | 5 / 10 | `team player`, `results-driven`, `passionate` are absent. But `Agile teams` and `Cross-functional remote teams` were added to a new `Practices` Skills line, and `UX` and `Clean code` to the `Frontend` line, mirroring the posting's soft-skill wording with no DOSSIER claim behind them. See the unsupported-claim audit |
| 3.7 | Skills grouped by category | 10 / 10 | Seven labelled lines: Languages, Frontend, Backend, Data, Cloud and operations, Testing and AI tooling, Practices |
| 3.8 | Scannable | 5 / 5 | Consistent spacing, bold company names, one page, clear vertical gaps between role blocks in both extractions |

## Unsupported claims — audit against DOSSIER.md

DOSSIER.md is the only claim source. Each tailored phrase below was checked
against it. Reported, not fixed.

| Phrase | Location | DOSSIER support | Result |
|---|---|---|---|
| `Agile teams` | Skills `Practices` line 18 | No agile fact anywhere in DOSSIER.md | **UNSUPPORTED** |
| `in agile teams` | Luizalabs bullet 4, line 46 | Same. DOSSIER records Docker, Kubernetes, GCP, ArgoCD, Vitest, Jest for Luizalabs, and nothing about the team process | **UNSUPPORTED** |
| `Cross-functional remote teams` | Skills `Practices` line 18 | DOSSIER records DexCare and Luizalabs as Remote. It records no cross-functional team fact | **UNSUPPORTED** |
| `working in a cross-functional remote team` | DexCare bullet 1, line 27 | Same. This clause was appended to a verified bullet | **UNSUPPORTED** |
| `fast-paced remote teams` | Summary line 7 | `Remote` is supported. `fast-paced` is not a DOSSIER fact; it mirrors the posting's `fast-paced, cross-functional remote teams` | **UNSUPPORTED**, adjectival |
| `UX` | Skills `Frontend` line 13; Summary line 7 | DOSSIER records React at DexCare and `Built customer-facing features end to end` at Lippaus. It records no UX token and no UX responsibility | **UNSUPPORTED** as a Skills token |
| `Clean code` | Skills `Frontend` line 13 | DOSSIER wording is `so agentic workflows produce high-quality code`. `Clean code` is a rewording that mirrors the posting's `clean code` | **REWORDED**, posting-mirrored. Not fabricated |
| `produce clean code` | DexCare bullet 6, line 35 | Same source phrase, `high-quality code`, replaced | **REWORDED**, posting-mirrored |
| `the React UX` | DexCare bullet 5, line 33 | DOSSIER records React and `Datadog RUM and browser logs`. RUM is real user monitoring, so the underlying fact holds. The word `UX` was inserted | Supported fact, inserted term |
| `Stakeholder communication` | Skills `Practices` line 18 | DOSSIER: `project scoping and stakeholder communication` is an approved Lippaus bullet | SUPPORTED |
| `JavaScript` in Summary | Summary line 6 | DOSSIER: Lippaus back-office dashboards in JavaScript. LinkedIn technology lists carry JavaScript | SUPPORTED |
| `customer-facing web and mobile UX` | Summary line 7 | DOSSIER: `multi-tenant web and mobile platform`, `customer-facing features end to end`. `web and mobile` and `customer-facing` are supported. `UX` is not | Partly supported |
| `5+ years` | Summary line 6 | LinkedIn: Mar 2021 to Present is 5 years 6 months | SUPPORTED for total experience |

Four distinct unsupported practice claims reach the document: `Agile teams`
(twice), `Cross-functional remote teams` (twice), `fast-paced`, and `UX` as a
skill. All four mirror wording taken from the posting rather than from a
recorded fact. Under AGENTS.md section 4 a practice term is weight 1 and is
matched only `when they fit the role history`. These four have no role-history
record in DOSSIER.md.

## Defects, ranked by cost

1. **Svelte absent — Gate 1 and Gate 2, blocking.** The posting states
   `🔧 Must-have: JavaScript, TypeScript, Svelte`. The token appears 0 times.
   There is no exact fix available to the Architect: DOSSIER.md carries no
   Svelte fact, and AGENTS.md section 4 forbids inventing a framework claim.
   This escalates to the Maestro as a candidate-fact question for Lucas, or
   the application is abandoned. Do not place the token without a new
   DOSSIER entry.

2. **`5+ years of frontend experience` is claimed only as general
   experience — Gate 1, weak PASS.** The posting gates on frontend years. The
   Summary says `5+ years building TypeScript, JavaScript, React, Node.js, and
   Go products`. A reader must assemble the frontend thread themselves from
   `back-office dashboards in JavaScript` (Mar 2021 - Jan 2023),
   `multi-tenant web and mobile platform` (Jan 2023 - Jan 2024), and
   `the React UX` (Mar 2026 - Present). Luizalabs, the Jan 2024 - Mar 2026
   block, carries no frontend token at all, which leaves a visible 2-year hole
   in the frontend narrative. Fix only within recorded facts.

3. **Four unsupported practice claims — Gate 3.6 and the DOSSIER audit.**
   `Agile teams` (Skills line 18 and Luizalabs bullet 4), `Cross-functional
   remote teams` (Skills line 18 and DexCare bullet 1), `fast-paced`
   (Summary), and `UX` as a Skills token (`Frontend: React | UX | Clean
   code`). Exact text to change, quoted from the raw extraction:
   - `Practices: Agile teams | Cross-functional remote teams | Stakeholder communication`
   - `Frontend: React | UX | Clean code`
   - `... through ArgoCD in agile teams, keeping production reliable ...`
   - `... healthcare scheduling platform, working in a cross-functional remote team.`
   - `... and Go products in fast-paced remote teams.`

4. **Target title absent — Gate 3.1, 0 of 15.** `Senior Frontend Developer`
   does not appear in the top 15%. DOSSIER.md records the decision `CV title
   stays Senior Software Engineer`, and AGENTS.md section 4 forbids changing a
   title to fit a posting. This defect is therefore not fixable under current
   policy. Recorded, not actionable.

5. **Frontend relevance buried — Gate 3.2, 0 of 20.** The first three DexCare
   bullets are all backend. For a frontend posting the recruiter's first three
   lines carry no frontend signal. Reordering bullets inside the most recent
   role is permitted by AGENTS.md section 9.1, which allows reorder but not
   deletion. The Architect may move `Reduced release risk by 7% ... monitoring
   the React UX with Datadog RUM` up. That does not change the Gate 1 block.

## Match limits

Preferred tokens not placed: **AWS Lambda**. DOSSIER.md records AWS SDK v3
for S3, STS, Secrets Manager, and RDS Signer, and no Lambda fact. Correct
absence, not a defect.

Posting terms that were classified as soft skills and excluded from the Gate 2
score: `strong communication skills`, `comfortable in fast-paced,
cross-functional remote teams`, `love clean code`, `agile teams`,
`building great UX`.

Not observable from the posting: the hiring company name, the applicant count,
the work-authorization requirement, the time-zone overlap requirement, the
English-level requirement, the degree requirement, and the notice period.
