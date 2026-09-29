# Gate 0 parse integrity — base CV pair

Files under test: `~/career/resumes/base-en.pdf`, `~/career/resumes/base-pt.pdf`
Sources read for reference: `base-en.tex`, `base-pt.tex`
Rubric: `~/career/RUBRIC.md` Gate 0, all 8 checks
Spec: `~/career/CV-SPEC.md`
Ground truth: `~/career/DOSSIER.md`, section "LinkedIn ground truth"
Date: 2026-09-01. Analyst: ATS Analyzer. No file was edited.

Gate 1 was not run. There is no target posting.

## Verdict

| File | Gate 0 |
|---|---|
| `base-en.pdf` | **PASS**, 8 of 8 |
| `base-pt.pdf` | **PASS**, 8 of 8 |

No Gate 0 defect in either file. The fix list below carries three non-blocking
items and one item that blocks sending, not building.

## Extraction

Performed by me, from the PDFs, not from the `.raw.txt` files already sitting
in `resumes/`.

```
pdftotext          base-en.pdf -    pdftotext -layout base-en.pdf -
pdftotext          base-pt.pdf -    pdftotext -layout base-pt.pdf -
```
poppler 26.08.0. Every judgement below is made on the raw extraction.

## Gate 0 — base-en.pdf

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 50 lines of clean text. Fonts embedded and subsetted: `IHAIZV+Roboto-Bold-Identity-H`, `BZIVMZ+Roboto-Regular-Identity-H`, both `uni yes`. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00–U+FB06. Zero NUL, zero U+FFFD. `ff`/`fi`/`fl` words extract intact: `fiscal flags flows notifications office workflows`. Non-ASCII inventory is one character, `ó` U+00F3. |
| 0.3 | Contact block recoverable | PASS | Raw lines 3-4: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com` and `linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. In the body. `\pagestyle{empty}`, so no header or footer exists. |
| 0.4 | Section headers verbatim | PASS | `grep -cx` returns 1 for each of `Summary`, `Skills`, `Experience`, `Education`. All four are standalone lines. |
| 0.5 | **Employment-block segmentation** | PASS | Exactly 4 blocks. Non-blank lines following each header: DexCare 7, Luizalabs 6, Lippaus Distribuidora (Mid-level) 3, Lippaus Distribuidora (Entry-level) 2. No blank line falls inside a role. No two roles merge. |
| 0.6 | Date parseability | PASS | Every role carries `Mon YYYY - Mon YYYY` on the header line, ASCII hyphen: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`. |
| 0.7 | Reading order | PASS | Raw and layout extractions agree line for line after whitespace normalisation. `diff` returns nothing. |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` reports 0 images. No `tabular`, `includegraphics`, `minipage`, `parbox`, `fbox`, `marvosym` or icon font in the source. The one `tabular` string in `base-en.tex:30` is inside a comment and never reaches the PDF. |

## Gate 0 — base-pt.pdf

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 52 lines of clean text. Same two embedded Roboto subsets, both `uni yes`. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00–U+FB06. Zero NUL, zero U+FFFD. `ff`/`fi`/`fl` words intact: `backoffice fiscais fiscal flags fluxos notificações profissionais`. Non-ASCII inventory is 10 characters, all correct Portuguese accents: `à á â ã ç í ó ô õ ú`. No mojibake. |
| 0.3 | Contact block recoverable | PASS | Raw lines 3-4, same fields, `Brasil` for `Brazil`. In the body. |
| 0.4 | Section headers verbatim | PASS | `grep -cx` returns 1 for each of `Summary`, `Skills`, `Experience`, `Education`. Kept in English on purpose; see question 3 below. |
| 0.5 | **Employment-block segmentation** | PASS | Exactly 4 blocks. Non-blank lines after each header: 8, 6, 3, 2. No split, no merge. |
| 0.6 | Date parseability | PASS | Identical date strings to the EN file, ASCII hyphen throughout. |
| 0.7 | Reading order | PASS | Raw and layout agree. `diff` returns nothing. |
| 0.8 | No forbidden constructs | PASS | 0 images, no table, no text box, no icon font. |

The shape A macro from `reports/macro-bakeoff.md` is doing its job. The
`Company \| Title \| Dates \| Location` header extracts as one line in both
files, which is what carries 0.5, 0.6 and 0.7.

## Mechanical checks

### 1. Titles and dates against DOSSIER LinkedIn ground truth

Compared character for character against the raw extraction.

| Role | Result |
|---|---|
| `DexCare \| Senior Software Engineer \| Jan 2026 - Present` | PASS both files |
| `Luizalabs \| Mid-level Software Engineer \| Jan 2024 - Jan 2026` | PASS both files |
| `Lippaus Distribuidora \| Mid-level Software Engineer \| Jan 2023 - Jan 2024` | PASS both files |
| `Lippaus Distribuidora \| Entry-level Fullstack Software Engineer \| Mar 2021 - Jan 2023` | PASS both files |

All four job titles, all four company spellings (`Luizalabs` lowercase `l`,
`Lippaus Distribuidora` in full) and all four date ranges match exactly. The
Lippaus promotion is present as two separate roles, as the dossier requires.
DexCare is present as the current role. Luizalabs ends `Jan 2026`, not
`Present`.

**FAESA carries two character-level deviations. Neither is a Gate 0 defect.**

| Field | DOSSIER verbatim | base-en | base-pt |
|---|---|---|---|
| School | `FAESA` | `FAESA` PASS | `FAESA` PASS |
| Degree | `Bachelor's degree , Information Systems` | `Bachelor's degree, Information Systems` | `Bacharelado em Sistemas de Informação` |
| Dates | `Feb 2022 – Dec 2025` (EN DASH U+2013) | `Feb 2022 - Dec 2025` (ASCII hyphen) | `Feb 2022 - Dec 2025` (ASCII hyphen) |

Assessment of each:

- **Degree, EN.** The dossier string has a space before the comma. That is a
  LinkedIn display artifact, not a degree name. The CV drops the space. I do
  not treat this as a defect.
- **Degree, PT.** Translated, as the CV-SPEC language rule requires for a
  `-pt` pair.
- **Dates.** This is a real conflict between two rules, and it is not mine to
  settle. `CLAUDE.md` rule 1 says dates match LinkedIn exactly. `CV-SPEC.md`
  item 5 says ASCII hyphen everywhere, one separator only, and RUBRIC Gate 0.6
  is written against `Mon YYYY - Mon YYYY`. The two cannot both hold for this
  one string. The CV follows CV-SPEC. Recorded as question 1 below.

Not checked as part of this item, but observed: the DexCare and Luizalabs
location fields read `Remote` / `Remoto`, where LinkedIn records
`Seattle, Washington, United States · Remote` and `São Paulo, Brazil · Remote`.
Location is not covered by the title-and-date rule. Recorded as question 2.

### 2. Forbidden stack tokens

`grep -inE 'ruby|rails|sidekiq|activerecord|rspec|hotwire'`

| File | Hits |
|---|---|
| `base-en.tex` | 0 |
| `base-pt.tex` | 0 |
| `base-en` raw extraction | 0 |
| `base-pt` raw extraction | 0 |
| `base-en` layout extraction | 0 |
| `base-pt` layout extraction | 0 |

PASS. Zero, as required.

### 3. UNVERIFIED markers

| File | Occurrences | Lines |
|---|---|---|
| `base-en.tex` | 14 | 50, 53 (x2), 54 (x2), 72, 73, 74, 75, 80, 81, 82, 87, 88 |
| `base-pt.tex` | 14 | 49, 52 (x2), 53 (x2), 71, 72, 73, 74, 79, 80, 81, 86, 87 |
| `base-en` raw extraction | 14 | on raw lines 13, 16 (x2), 18 (x2), 33, 34, 35, 36, 39, 40, 41, 44, 45 |
| `base-pt` raw extraction | 14 | on raw lines 14, 17 (x2), 19 (x2), 35, 36, 37, 38, 41, 42, 43, 46, 47 |

12 source lines carry 14 markers. Lines with two markers: the Cloud skills line
(`Docker`, `Kubernetes`) and the Testing skills line (`Vitest`, `Jest`).

What is marked, grouped:

- **Skills**, 5 markers: `BullMQ`, `Docker`, `Kubernetes`, `Vitest`, `Jest`.
- **Luizalabs**, 4 markers: every bullet except the first. The Go tax
  microservices claim, BullMQ invoice processing, back-office dashboards, and
  Docker/Kubernetes/GCP/ArgoCD deployment.
- **Lippaus Mid-level**, 3 markers: all three bullets.
- **Lippaus Entry-level**, 2 markers: both bullets.

Every DexCare bullet is unmarked. That is consistent with the dossier, which
records the DexCare stack as observed fact read from the repos.

**These markers are in the PDF text layer.** They render, they extract, and a
recruiter would read them. That is correct for the current working state under
`CLAUDE.md` rule 4, and it is disqualifying for any outward use. See fix item 1.

### 4. Per-term appearance cap of 3

Counted on the raw extraction with word boundaries. 34 load-bearing tokens
checked in each file.

**No token exceeds the cap of 3, in either file.** Highest count is 3, reached
by: `TypeScript`, `Node.js`, `React`, `Go`, `BullMQ`, `PostgreSQL`, `DynamoDB`,
`AWS`, `multi-tenant`. Everything else is 1 or 2.

PASS both files. No Gate 2 stuffing penalty would apply on repetition count.

### 5. One page

`pdfinfo`:

| File | Pages | Page size |
|---|---|---|
| `base-en.pdf` | 1 | 612 x 792 pts (letter) |
| `base-pt.pdf` | 1 | 612 x 792 pts (letter) |

PASS both.

### 6. UTC offset (CLAUDE.md rule 3)

`grep -inE 'UTC|GMT|BRT'` on both raw extractions returns nothing. No offset is
printed. PASS both.

## Gate 3 — human scan, reported not blocking

Identical structure in both files, so the score is the same for each.

| # | Check | Points | Awarded | Note |
|---|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 15 | 15 | `Senior Software Engineer` is raw line 2 of 50. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20 | 20 | DexCare bullets 1-3 carry TypeScript/Express/Koa, Epic EMR event-driven, and the PostgreSQL/Sequelize/Drizzle/DynamoDB/Redis data layer. Graded generically; with no posting I cannot grade "most relevant" against a real target. React appears only in bullet 5 and Go only under Luizalabs, so a React- or Go-led posting would score this lower. |
| 3.3 | Every bullet leads with an outcome or action verb | 15 | 15 | All 16 EN bullets lead with a verb: Develop, Integrate, Model, Secure, Release, Access, Delivered, Built, Implemented, Developed, Deployed, Built, Designed, Led, Developed, Delivered. No "Responsible for". |
| 3.4 | At least 3 bullets carry a real, defensible number | 15 | **0** | **Known FAIL.** Zero bullets carry a metric. `AWS SDK v3` is a version string, not a result. `5+ years` sits in Summary, not a bullet. Lucas has not supplied numbers yet. |
| 3.5 | 1 page under 10 years experience | 10 | 10 | Confirmed by `pdfinfo`. |
| 3.6 | No unsupported buzzwords | 10 | 10 | No "team player", "results-driven", "passionate", "proven track record", "expert". |
| 3.7 | Skills grouped by category | 10 | 10 | Six labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing. |
| 3.8 | Scannable: consistent spacing, bold titles, white space | 5 | 5 | Bold company names, ruled section headers, uniform bullet indent, one blank line between roles. Scored on typography only. The `[UNVERIFIED]` markers are a separate defect, listed in the fix list, not folded into this row. |

**Gate 3: 85/100, both files.** 15 of the 15 missing points are 3.4.

## Advisory, not a gate that was run

Gate 2 was not requested and no posting exists, so no coverage score is given.
One input to it is already visible and worth handing over now.

Seven tokens appear in `Skills` with no supporting evidence anywhere in
`Experience`, in both files: `JavaScript`, `SQL`, `REST`, `Swagger`, `CI/CD`,
`Vitest`, `Jest`. RUBRIC Gate 2 step 4 subtracts 5 points per such token. On
the current text that is a 35-point standing deduction against any posting that
lists them. `CV-SPEC.md` also states the rule directly: every load-bearing
technology appears in `Skills` **and** in context inside an `Experience`
bullet.

## Fix list for the Resume Architect

Nothing here blocks the build. Item 1 blocks sending.

1. **Strip or gate the 14 `[UNVERIFIED]` markers before any outward use.**
   Highest cost of anything in this report. They are in the PDF text layer, so
   a recruiter reads them and a parser indexes them. The base pair may keep
   them as the working artifact. No tailored CV built from it may ship with
   them. 12 source lines, listed in mechanical check 3 above. Per `CLAUDE.md`
   rule 4 these must be surfaced to Lucas, never silently promoted to fact.

2. **Give `JavaScript`, `SQL`, `REST`, `Swagger`, `CI/CD`, `Vitest` and `Jest`
   an Experience bullet, or remove them from `Skills`.** Both files, same seven
   tokens. Either action clears the Gate 2 step 4 penalty. Do not add a bullet
   that is not true; removing the token is the safe move where the evidence
   does not exist.

3. **Gate 3.4, numbers.** Blocked on Lucas, not on you. Once he supplies
   figures, at least 3 bullets need a real defensible number. The DexCare
   bullets are the place to put them, since they are the only unmarked ones.

4. **Optional, awaiting Lucas.** The FAESA date separator and the role location
   fields, questions 1 and 2 below. Change nothing until he answers.

## Questions for Lucas, recorded not asked

1. **FAESA date separator.** LinkedIn shows `Feb 2022 – Dec 2025` with an EN
   DASH. `CLAUDE.md` rule 1 says dates match LinkedIn exactly. `CV-SPEC.md`
   item 5 says ASCII hyphen everywhere. The CV follows CV-SPEC. Confirm that
   CV-SPEC wins here, or say the education date should carry the EN DASH and
   accept the mixed separator.

2. **Role location fields.** The CV writes `Remote` for DexCare and Luizalabs.
   LinkedIn records `Seattle, Washington, United States · Remote` and
   `São Paulo, Brazil · Remote`. Naming the employer city can help a posting
   that gates on a US presence and can also read as a claim of US residence.
   Do you want the employer city on the line, or `Remote` alone?

3. **Portuguese file, English section headers.** `base-pt.pdf` renders
   `Summary`, `Skills`, `Experience`, `Education` in English over Portuguese
   body text. That is what RUBRIC Gate 0.4 asks for and it is correct for
   parsing. A Brazilian human reader will notice it. Confirm you accept it, or
   say you want Portuguese headers and a Gate 0.4 exception recorded for the
   `-pt` file.

## Claims I could not verify

The 14 `[UNVERIFIED]` markers already mark them, and the Resume Architect
placed them correctly. Restated here so they reach Lucas in one list. I did not
delete any of them and I do not defend any of them.

**Skills, 5 claims.** That Lucas used `BullMQ`, `Docker`, `Kubernetes`,
`Vitest` and `Jest`. These come from the `CLAUDE.md` stack-substitution rule
(Sidekiq to BullMQ, RSpec to Vitest/Jest), so the substituted names are
inferences from a Rails-world original, not observed facts.

**Luizalabs, 4 claims.** Distributed tax microservices in Go issuing electronic
invoices to state tax authorities. Asynchronous invoice processing with BullMQ.
Internal back-office dashboards. Docker, Kubernetes, GCP and ArgoCD deployment.
The dossier records Lucas's own statement that Luizalabs was Node and Java.

**Lippaus Mid-level, 3 claims.** Multi-tenant web and mobile platform on
PostgreSQL. Asynchronous job processing with BullMQ. Project scoping and
stakeholder communication.

**Lippaus Entry-level, 2 claims.** Internal back-office and dashboard
applications for a beverage distribution startup. Customer-facing features and
internal tools delivered end to end.

**Separately open in the dossier, and correctly absent from both files.** The
Rails core and community gem contribution claimed in `Lucas_Resume.pdf` and
`Lucas_ResumeV2.pdf`. It appears nowhere in this pair. That is the right state
while it is unresolved.
