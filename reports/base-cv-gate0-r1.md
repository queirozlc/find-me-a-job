# Gate 0 re-run (r1) — base CV pair, rebuilt on shape C

Files under test: `~/career/resumes/base-en.pdf`, `~/career/resumes/base-pt.pdf`
Rebuilt by Quill for visual parity with `~/career/resumes/reference-visual.pdf`,
using the template `tabular*` header (shape C), on Lucas's instruction.
Rubric: `~/career/RUBRIC.md` Gate 0, all 8 checks, with the 0.4 allowlist
Lucas set 2026-09-01 (case-insensitive, PT headers permitted).
Date: 2026-09-01. Analyst: ATS Analyzer. No file was edited.

Supersedes `reports/base-cv-gate0.md`, which graded the shape A build.

## Verdict

| File | Gate 0 | Failing checks |
|---|---|---|
| `base-en.pdf` | **FAIL** | 0.5, 0.6, 0.7, 0.8 |
| `base-pt.pdf` | **FAIL** | 0.5, 0.6, 0.7, 0.8 |

4 of 8 pass. The previous build passed 8 of 8. This is the exact regression the
bake-off measured in `reports/macro-bakeoff.md` and predicted for shape C.

Lucas ordered the visual parity. That decision stands. My job is to price it,
not to reverse it. The price is below.

## Extraction

Performed by me, from the PDFs.

```
pdftotext          base-en.pdf -    pdftotext -layout base-en.pdf -
pdftotext          base-pt.pdf -    pdftotext -layout base-pt.pdf -
```
poppler 26.08.0.

## Gate 0 — base-en.pdf

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 75 lines of clean text. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00–U+FB06. Zero NUL, zero U+FFFD. `ff`/`fi`/`fl` words intact: `fiscal flags flows notifications office workflows`. |
| 0.3 | Contact block recoverable | PASS | Raw line 3, one line, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. |
| 0.4 | Section headers | PASS | `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, each a standalone line, one occurrence each. Uppercase rendering is allowed under the 2026-09-01 allowlist. |
| 0.5 | **Employment-block segmentation** | **FAIL** | See "Parser cost" below. Every role is split into 3 blocks, and the `EXPERIENCE` header is merged into the first role. |
| 0.6 | Date parseability | **FAIL** | No role has its date on the title line, and a blank line separates the date from the title in every case. |
| 0.7 | Reading order | **FAIL** | Raw and layout disagree on all 4 roles and on Education. |
| 0.8 | No forbidden constructs | **FAIL** | `base-en.tex:44` `\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}`, closed at line 47. A table construct carries every role header and the education block. `base-en.tex:12` loads `tabularx`; line 6 loads `marvosym`. 0 images, no photo. |

**0.8 note.** `marvosym` is loaded but no icon glyph reaches the text layer;
the contact line extracts as plain text. The FAIL is the `tabular*`, not the
package load.

## Gate 0 — base-pt.pdf

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 76 lines of clean text. |
| 0.2 | Glyph integrity | PASS | Zero U+FB00–U+FB06, zero NUL, zero U+FFFD. `backoffice confiáveis filas fiscais flags fluxos notificações` all intact. Portuguese accents correct, no mojibake. |
| 0.3 | Contact block recoverable | PASS | Raw line 3, same fields, `Brasil`. |
| 0.4 | Section headers | PASS | `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, one standalone occurrence each. Matches the PT allowlist. |
| 0.5 | **Employment-block segmentation** | **FAIL** | Identical structure to EN. 3 blocks per role, header merged into the first role. |
| 0.6 | Date parseability | **FAIL** | Identical to EN. |
| 0.7 | Reading order | **FAIL** | Identical to EN. |
| 0.8 | No forbidden constructs | **FAIL** | `base-pt.tex:44` and `:47`, same `tabular*`. `tabularx` at line 12, `marvosym` at line 6. 0 images. |

## Parser cost, exactly

Both files behave identically. EN is quoted; PT differs only in language.

### What the raw stream contains

The raw extraction breaks into 18 blank-line-delimited blocks. Four roles
occupy twelve of them, three blocks each:

| Block | Content | Lines |
|---|---|---|
| 5 | `EXPERIENCE` + `DexCare` + `Senior Software Engineer` | 3 |
| 6 | `Jan 2026 - Present` + `Remote` | 2 |
| 7 | the 5 DexCare bullets | 10 |
| 8 | `Luizalabs` + `Mid-level Software Engineer` | 2 |
| 9 | `Jan 2024 - Jan 2026` + `Remote` | 2 |
| 10 | the 4 Luizalabs bullets | 7 |
| 11 | `Lippaus Distribuidora` + `Mid-level Software Engineer` | 2 |
| 12 | `Jan 2023 - Jan 2024` + `Vitória, ES, Brazil` | 2 |
| 13 | the 3 Lippaus Mid-level bullets | 3 |
| 14 | `Lippaus Distribuidora` + `Entry-level Fullstack Software Engineer` | 2 |
| 15 | `Mar 2021 - Jan 2023` + `Vitória, ES, Brazil` | 2 |
| 16 | the 2 Lippaus Entry-level bullets | 3 |
| 17 | `EDUCATION` + `FAESA` + `Bachelor's degree, Information Systems` | 3 |
| 18 | `Vitória, ES, Brazil` + `Feb 2022 - Dec 2025` | 2 |

### What a parser sees, per role

Verbatim from `pdftotext base-en.pdf -`, raw lines 17-22:

```
EXPERIENCE
DexCare
Senior Software Engineer

Jan 2026 - Present
Remote
```

For each of the four roles the parser receives, in order: the company, the
title, **a block boundary**, then the date range and location. Four consequences:

1. **The date is severed from the title.** RUBRIC 0.6 requires the date on the
   title line or adjacent to it. A blank line sits between them in all four
   roles. A parser that keys tenure off "date near title" finds nothing and
   falls back to a document-wide date scan.
2. **Each role is three records, not one.** A segmenter that splits on blank
   lines produces 12 fragments for 4 roles. Identity, tenure and evidence land
   in three different records with no key joining them.
3. **The section header is inside the first role.** Block 5 is
   `EXPERIENCE / DexCare / Senior Software Engineer`. A parser that treats the
   first line of a block as its label can read the current employer as
   `EXPERIENCE`. This is a merge, and 0.5 fails on merges as well as splits.
4. **Location can be mistaken for the employer.** Blocks 6, 9, 12 and 15 open
   with a date and close with a place name. `Remote` and `Vitória, ES, Brazil`
   sit in the position a naive parser reads as an organisation field.

### Reading-order disagreement, 0.7

`diff` between the normalised raw and layout extractions. Every role disagrees.
Two examples, `<` is raw, `>` is layout:

```
< DexCare
< Senior Software Engineer
< Jan 2026 - Present
< Remote
---
> DexCare                    Jan 2026 - Present
> Senior Software Engineer   Remote
```

```
< FAESA
< Bachelor's degree, Information Systems
< Vitória, ES, Brazil
< Feb 2022 - Dec 2025
---
> FAESA                                    Vitória, ES, Brazil
> Bachelor's degree, Information Systems   Feb 2022 - Dec 2025
```

A human reads two lines with the date on the right. A parser reads four lines
with the date third or fourth. The two views of the same block do not agree,
which is the 0.7 FAIL condition.

**Education is worse than the roles.** The raw stream emits the location
*before* the date: `FAESA`, degree, `Vitória, ES, Brazil`, `Feb 2022 - Dec
2025`. The graduation date is two lines from the degree with a city in
between.

### What did not break

Worth stating plainly, because the regression is narrower than "the CV is
broken":

- The text layer, glyphs, accents and contact block are all clean.
- Every company name, job title and date string is present and correct.
- Section headers are recoverable.
- Both files are one page.
- No forbidden token, no over-cap term.

The damage is confined to structure. A keyword-search recruiter still finds
this CV. A parser that builds an employment table from it produces a wrong
table.

## Gate 2 — unevidenced-token deduction

Gate 2 was not scored; there is no posting. The step-4 stuffing input is
reported, as before.

| | Previous build | This build |
|---|---|---|
| Skills-only tokens with no `Experience` evidence | `JavaScript`, `SQL`, `REST`, `Swagger`, `CI/CD`, `Vitest`, `Jest` | `REST` |
| Deduction at 5 points each | **35 points** | **5 points** |

Both files, identical. This is a real improvement and it is independent of the
macro change. Six of the seven orphan tokens now appear in an Experience
bullet. Only `REST` remains: `REST APIs` is in `SKILLS`, and the Experience
bullets say `OpenAPI/Swagger` and `API contracts` but never `REST`.

Per-term appearance cap of 3: no token exceeds it in either file.

## Gate 3 — human scan, reported not blocking

Identical in both files.

| # | Check | Points | Awarded | Note |
|---|---|---|---|---|
| 3.1 | Target title in the top 15% | 15 | 15 | `Senior Software Engineer` first appears at raw line 6 of 75; the 15% mark is line 11. It now appears only inside the Summary sentence; the standalone title line under the name is gone. It still clears the threshold. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20 | 20 | DexCare bullets 1-3 carry event-driven TypeScript on Express and Koa, Epic EMR integration, and multi-tenant Auth0/JWT with OpenAPI validation. Graded generically; there is no posting. |
| 3.3 | Every bullet leads with an outcome or action verb | 15 | 15 | All 14 EN bullets: Deliver, Keep, Isolate, Serve, Reduce, Delivered, Improved, Gave, Kept, Supported, Handled, Turned, Supported, Delivered. No "Responsible for". |
| 3.4 | At least 3 bullets carry a real number | 15 | **0** | **Known FAIL.** One bullet contains a digit and it is the product name `Auth0`. No metric anywhere. Lucas has not supplied numbers. |
| 3.5 | 1 page under 10 years | 10 | 10 | `pdfinfo`: 1 page, 612 x 792 pts, both files. |
| 3.6 | No unsupported buzzwords | 10 | 10 | Zero hits for "team player", "results-driven", "passionate", "proven track record", "self-starter". |
| 3.7 | Skills grouped by category | 10 | **0** | **New FAIL, a regression.** `SKILLS` is now one undifferentiated wall of 29 pipe-separated terms across 3 wrapped lines. The previous build had six labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing. This is the exact condition 3.7 names. |
| 3.8 | Scannable spacing, bold titles, white space | 5 | 5 | Bold company names, ruled headers, right-aligned dates, uniform bullets. Scored on typography only. |

**Gate 3: 75/100, both files.** Down from 85/100. The 10-point loss is 3.7.

## UNVERIFIED markers

| File | Occurrences | Source lines |
|---|---|---|
| `base-en.tex` | 9 | 63, 67, 85, 94, 95, 96, 102, 103 |
| `base-pt.tex` | 9 | 63, 67, 85, 94, 95, 96, 102, 103 |
| both raw extractions | 9 | in the PDF text layer |

Down from 14. One source line carries two markers in each file (the Skills
line, `Agentic IDEs (Cursor/Windsurf)` and `LLM Integration`).

Two markers are new and were not in the previous build:

- `Agentic IDEs (Cursor/Windsurf) [UNVERIFIED]` and
  `LLM Integration [UNVERIFIED]` in `SKILLS`.
- `Integrates AI-driven agentic workflows to accelerate development cycles
  [UNVERIFIED]` in `SUMMARY`, raw line 9.

These three claims trace to the original Overleaf template's summary. They are
not in `DOSSIER.md`. They are correctly marked. They are also in the **Summary**,
which is the highest-weight field on the page.

The markers remain in the PDF text layer. Correct for the working artifact,
disqualifying for anything sent. Unchanged from the previous report.

## Task 2 — LinkedIn cross-check

Portal `Profile Check`, `https://www.linkedin.com/in/queiroz-lucas/`, title
`Lucas Queiroz | LinkedIn`. **No auth wall.** The session is logged in and the
profile rendered. Read-only: `snapshot`, `text`, and `scroll` to load the
lazily-rendered lower sections. Nothing was clicked. Nothing was edited.

### Live profile, Experience and Education, verbatim

```
Senior Software Engineer
DexCare · Full-time
Jan 2026 - Present · 9 mos
Seattle, Washington, United States · Remote

Mid-level Software Engineer
Luizalabs · Full-time
Jan 2024 - Jan 2026 · 2 yrs 1 mo
São Paulo, Brazil · Remote

Lippaus Distribuidora
Full-time · 2 yrs 11 mos
Vitória, Espírito Santo, Brazil · On-site

    Mid-level Software Engineer
    Jan 2023 - Jan 2024 · 1 yr 1 mo

    Entry-level Fullstack Software Engineer
    Mar 2021 - Jan 2023 · 1 yr 11 mos

Education

FAESA
Bachelor's degree , Information Systems
Feb 2022 – Dec 2025
```

### DOSSIER accuracy

`DOSSIER.md` "LinkedIn ground truth" matches the live profile character for
character on every company, title and date, including the space before the
comma in the degree and the EN DASH in the education date. The dossier is
accurate as of today. No correction needed there.

### Company, title and date comparison

| Field | Live LinkedIn | base-en | base-pt | Result |
|---|---|---|---|---|
| Company 1 | `DexCare` | `DexCare` | `DexCare` | match |
| Title 1 | `Senior Software Engineer` | `Senior Software Engineer` | `Senior Software Engineer` | match |
| Dates 1 | `Jan 2026 - Present` | `Jan 2026 - Present` | `Jan 2026 - Present` | match |
| Company 2 | `Luizalabs` | `Luizalabs` | `Luizalabs` | match |
| Title 2 | `Mid-level Software Engineer` | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Dates 2 | `Jan 2024 - Jan 2026` | `Jan 2024 - Jan 2026` | `Jan 2024 - Jan 2026` | match |
| Company 3 | `Lippaus Distribuidora` | `Lippaus Distribuidora` | `Lippaus Distribuidora` | match |
| Title 3 | `Mid-level Software Engineer` | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Dates 3 | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024` | match |
| Company 4 | `Lippaus Distribuidora` | `Lippaus Distribuidora` | `Lippaus Distribuidora` | match |
| Title 4 | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | match |
| Dates 4 | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023` | match |
| School | `FAESA` | `FAESA` | `FAESA` | match |

**All twelve job strings and the school name match the live profile exactly, in
both files.** The Lippaus promotion is present as two roles. Luizalabs ends
`Jan 2026`, not `Present`. DexCare is present as the current role.

### Mismatches

Three, all in Education, all previously reported and none new.

| # | Field | Live LinkedIn | base-en | base-pt |
|---|---|---|---|---|
| 1 | Degree, spacing | `Bachelor's degree , Information Systems` | `Bachelor's degree, Information Systems` | — |
| 2 | Degree, language | `Bachelor's degree , Information Systems` | — | `Bacharelado em Sistemas de Informação` |
| 3 | Education date separator | `Feb 2022 – Dec 2025` (EN DASH U+2013) | `Feb 2022 - Dec 2025` (ASCII hyphen) | `Feb 2022 - Dec 2025` (ASCII hyphen) |

Assessment, unchanged from the previous report:

- **1** is a LinkedIn display artifact, a space before a comma. Not a defect.
- **2** is required by the CV-SPEC rule that a `-pt` file ships the same facts
  in Portuguese. Not a defect.
- **3** is a genuine conflict between `CLAUDE.md` rule 1 (dates match LinkedIn
  exactly) and `CV-SPEC.md` item 5 (ASCII hyphen everywhere). The CVs follow
  CV-SPEC. Only Lucas can settle it. Recorded as question 1.

### Observations outside the compared fields

Not mismatches. The task scoped the comparison to company, title and date. These
are facts I read on the live profile that bear on the CVs, reported without
recommendation.

- **Role locations.** LinkedIn records
  `Seattle, Washington, United States · Remote` for DexCare and
  `São Paulo, Brazil · Remote` for Luizalabs. Both CVs write `Remote` /
  `Remoto`. Lippaus is `Vitória, Espírito Santo, Brazil · On-site` on LinkedIn
  and `Vitória, ES, Brazil` / `Vitória, ES, Brasil` on the CVs, with no
  `On-site`. Question 2.
- **Headline.** Live: `Senior Full-Stack Software Engineer | TypeScript |
  JavaScript | Node.js | React | Go | AWS`. The CVs present
  `Senior Software Engineer`. A headline is not an Experience title, so this is
  not a mismatch under the rule. It is a visible inconsistency to a recruiter
  holding both. Question 3.
- **Employment type.** LinkedIn marks DexCare and Luizalabs `Full-time`. The
  dossier already records this as an open item: Lucas states both were
  engagements through Fullstack Labs. The `base-en` Luizalabs bullet says
  `engaged through the consultancy Fullstack Labs`, which contradicts the
  LinkedIn `Full-time` marker on the same employer. Still open, still Lucas's
  call.
- **Rails-adjacent content on the profile.** The Activity feed carries a repost
  of a job advertisement whose must-have is `Ruby on Rails, PostgreSQL`, and a
  post announcing a first open-source contribution to `Phoenix`, the Elixir
  framework. Neither is in Experience or Education, and neither reaches the
  CVs. Both are visible to any recruiter who opens the profile, next to a CV
  positioned as TypeScript, Node, React and Go. Question 4.

## Fix list for the Resume Architect

Nothing here is mine to change, and item 1 is Lucas's decision, not yours.

1. **Gate 0.5, 0.6, 0.7 and 0.8 cannot be fixed while the `tabular*` header
   stands.** Shape B was tested and fails identically; the bake-off proved
   horizontal separation is the cause, not the environment. Two options exist,
   and only Lucas can pick:
   - revert the header to shape A and lose the right-aligned dates, or
   - keep shape C and accept that a parser reads 12 fragments for 4 roles.

   Do not attempt a third macro without a bake-off run against
   `reports/macro-bakeoff.md`. Two shapes have already been eliminated by test.

2. **Gate 3.7, Skills is a single wall.** This is independent of the header
   macro and is yours to fix. Restore the six labelled groups from the previous
   build. It costs 10 Gate 3 points and it is the fastest fix in this report.

3. **`REST` has no Experience evidence.** Both files. `REST APIs` is in
   `SKILLS`; no Experience bullet contains the token. Add it to a true bullet or
   drop it from Skills. 5 Gate 2 points.

4. **Three new `[UNVERIFIED]` claims sit in high-weight fields.** The agentic
   AI workflow sentence is in `SUMMARY`, and two agentic tokens are in `SKILLS`.
   They came from the old Overleaf template and are in no dossier entry. Correct
   to mark them; worth asking whether they should be in the two highest-weight
   sections at all before they are verified.

5. **Strip or gate the 9 `[UNVERIFIED]` markers before any outward use.**
   Unchanged from the previous report. They render and they extract.

6. **Gate 3.4 numbers.** Still blocked on Lucas. Noting one new fact: the live
   LinkedIn DexCare entry already carries a figure, `helping eliminate 34% of
   redundant support tickets`, and the Luizalabs entry carries
   `reducing average review cycles from 3–4 rounds to 1–2`. These are Lucas's
   own published claims. They are not in `DOSSIER.md`, so I cannot mark them
   verified, but they are a concrete place for him to start.

## Questions for Lucas, recorded not asked

1. **FAESA date separator.** LinkedIn shows `Feb 2022 – Dec 2025` with an EN
   DASH. `CLAUDE.md` rule 1 says dates match LinkedIn exactly. `CV-SPEC.md`
   item 5 says ASCII hyphen everywhere. Both CVs follow CV-SPEC. Confirm
   CV-SPEC wins, or accept a mixed separator on the education line.

2. **Role locations.** The CVs write `Remote` where LinkedIn writes
   `Seattle, Washington, United States · Remote` and `São Paulo, Brazil ·
   Remote`. Naming the employer city helps a posting that gates on a US
   presence and can also read as a claim of US residence. Which do you want?

3. **Headline against CV title.** Your LinkedIn headline is
   `Senior Full-Stack Software Engineer`; the CVs say `Senior Software
   Engineer`. A recruiter holding both sees two titles. Do you want them
   aligned, and if so which one wins?

4. **Rails and Elixir content on the live profile.** Your Activity feed shows a
   reposted job advertisement requiring `Ruby on Rails` and a post about
   contributing to `Phoenix`, the Elixir framework. `CLAUDE.md` rule 2 keeps
   those tokens off every document. The profile is outside my remit and I
   changed nothing. Flagging it because a recruiter reads the profile and the
   CV together.

5. **The parser-versus-human trade, restated for the record.** You chose visual
   parity with `reference-visual.pdf`. That is your call and I have not
   reversed it. The measured price is 4 of 8 Gate 0 checks and a parser that
   reads 12 fragments for 4 roles. If a target posting routes through a modern
   parsing ATS, this build will misreport your tenure. If your channel is a
   human recruiter reading a PDF, the cost is close to zero. You may want a
   shape A variant kept alongside for the first case.

## Claims I could not verify

The 9 `[UNVERIFIED]` markers, placed by the Resume Architect, restated so they
reach Lucas in one list. I deleted none and defend none.

**Summary, 1 claim.** `Integrates AI-driven agentic workflows to accelerate
development cycles`. Not in the dossier. Traces to the original Overleaf
template.

**Skills, 2 claims.** `Agentic IDEs (Cursor/Windsurf)` and `LLM Integration`.
Same origin, same status.

**Luizalabs, 1 claim.** That the distributed tax microservices were built in
`Go` alongside Node.js and Java. The dossier records Lucas's own account of
Node and Java. `Go` is the unsupported part.

**Lippaus Mid-level, 3 claims.** The multi-tenant web and mobile platform on
PostgreSQL, the asynchronous BullMQ job processing, and the project scoping and
stakeholder communication.

**Lippaus Entry-level, 2 claims.** The internal back-office dashboards in
JavaScript, and customer-facing features delivered end to end.

**Newly relevant, not on the CVs.** The live LinkedIn profile publishes two
metrics that the CVs do not use: `34%` of redundant support tickets eliminated
at DexCare, and review cycles cut `from 3–4 rounds to 1–2` at Luizalabs. They
are Lucas's own published words. They are not in `DOSSIER.md`, so I record them
as unverified rather than as evidence.

**Still open in the dossier, correctly absent from both files.** The Rails core
and community gem contribution claimed in the old PDFs.
