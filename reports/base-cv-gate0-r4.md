# Gate 0 r4 — base CV pair, expected final

Files under test: `~/career/resumes/base-en.pdf`, `~/career/resumes/base-pt.pdf`
and their `.tex` sources.
Rubric: `~/career/RUBRIC.md` Gate 0, all 8 checks, the 0.4 allowlist of
2026-09-01, and the **Accepted exception** of 2026-09-01.
Spec: `~/career/CV-SPEC.md` item 2, final decision of 2026-09-01.
Ground truth: `~/career/DOSSIER.md`, "LinkedIn ground truth".
Date: 2026-09-01. Analyst: ATS Analyzer. No file was edited.

Supersedes `reports/base-cv-gate0-r2.md`.

Changes since r2: role header returned to the two-column `tabular*` for visual
parity with `resumes/reference-visual.pdf`; the Fullstack Labs clause removed;
a DexCare bullet added naming Claude Code and Codex; vertical spacing opened up
per CV-SPEC item 2.

## Verdict

| File | Gate 0 under the accepted exception |
|---|---|
| `base-en.pdf` | **PASS** |
| `base-pt.pdf` | **PASS** |

Four checks fail on the raw extraction: 0.5, 0.6, 0.7 and 0.8. **In both files
the two-column header is the sole cause of all four.** No other cause was found
for any of them. Under the accepted exception these are reported, not blocking.
Nothing else blocks.

## Extraction

```
pdftotext          base-en.pdf -    pdftotext -layout base-en.pdf -
pdftotext          base-pt.pdf -    pdftotext -layout base-pt.pdf -
```
poppler 26.08.0. All judgements below are made on the raw extraction.

## Gate 0 — base-en.pdf

| # | Check | Result | Header the sole cause? | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | — | 78 lines of clean text. |
| 0.2 | Glyph integrity | PASS | — | Zero codepoints in U+FB00–U+FB06, zero NUL, zero U+FFFD. `ff`/`fi`/`fl` words intact: `fiscal flags flows notifications office workflows`. |
| 0.3 | Contact block recoverable | PASS | — | Raw line 3, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. |
| 0.4 | Section headers | PASS | — | `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, one standalone occurrence each. |
| 0.5 | Employment-block segmentation | **FAIL** | **Yes** | Each role splits into 3 blocks. Proof of sole cause below. |
| 0.6 | Date parseability | **FAIL** | **Yes** | A blank line separates every date from its title. |
| 0.7 | Reading order | **FAIL** | **Yes** | 5 diff hunks, all 5 are `tabular*` header blocks. Nothing else disagrees. |
| 0.8 | No forbidden constructs | **FAIL** | **Yes** | `base-en.tex:40` `\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}`, closed at `:43`. It is the only construct in the file. 0 images. |

## Gate 0 — base-pt.pdf

| # | Check | Result | Header the sole cause? | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | — | 77 lines of clean text. |
| 0.2 | Glyph integrity | PASS | — | Zero U+FB00–U+FB06, zero NUL, zero U+FFFD. `backoffice confiáveis filas fiscais flags fluxos notificações workflows` intact. Accents correct, no mojibake. |
| 0.3 | Contact block recoverable | PASS | — | Raw line 3, same fields, `Brasil`. |
| 0.4 | Section headers | PASS | — | `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, one standalone occurrence each. PT allowlist. |
| 0.5 | Employment-block segmentation | **FAIL** | **Yes** | Identical structure to EN. |
| 0.6 | Date parseability | **FAIL** | **Yes** | Identical to EN. |
| 0.7 | Reading order | **FAIL** | **Yes** | 5 diff hunks, all 5 are header blocks. |
| 0.8 | No forbidden constructs | **FAIL** | **Yes** | `base-pt.tex:40` and `:43`, same `tabular*`, the only construct. 0 images. |

## Proof that the header is the sole cause

The exception only holds if nothing *other* than the header produces these four
failures. Each was tested separately.

### 0.8 — no other construct exists

`grep -nE 'tabular|tabularx|includegraphics|minipage|parbox|fbox|marvosym|fontawesome'`
returns exactly two lines per file, both the header's own `tabular*` open and
close. `tabularx` and `marvosym`, present in the r1 build, are gone.
`pdfimages -list` reports 0 images in both files. No text box, no image of
text, no contact icon, no photo. The `tabular*` header is the only trigger.

### 0.7 — every disagreement is a header block

The full `diff` between the normalised raw and layout extractions produces
5 hunks per file. All 5 are `tabular*` blocks: the four role headers and the
education header. No bullet, no section header, no Summary or Skills line
disagrees. One hunk, verbatim, `<` is raw, `>` is layout:

```
< DexCare
< Senior Software Engineer
< Jan 2026 - Present
< Remote
---
> DexCare                    Jan 2026 - Present
> Senior Software Engineer   Remote
```

### 0.5 — only the header splits, the bullets do not

The raw stream is 18 blank-line-delimited blocks. Each role occupies three:

| Block | Content | Lines EN / PT |
|---|---|---|
| 5 | `EXPERIENCE` + `DexCare` + `Senior Software Engineer` | 3 / 3 |
| 6 | `Jan 2026 - Present` + `Remote` | 2 / 2 |
| 7 | 6 DexCare bullets | 12 / 11 |
| 8 | `Luizalabs` + `Mid-level Software Engineer` | 2 / 2 |
| 9 | `Jan 2024 - Jan 2026` + `Remote` | 2 / 2 |
| 10 | 4 Luizalabs bullets | 7 / 7 |
| 11 | `Lippaus Distribuidora` + `Mid-level Software Engineer` | 2 / 2 |
| 12 | `Jan 2023 - Jan 2024` + location | 2 / 2 |
| 13 | 3 bullets | 3 / 3 |
| 14 | `Lippaus Distribuidora` + `Entry-level Fullstack Software Engineer` | 2 / 2 |
| 15 | `Mar 2021 - Jan 2023` + location | 2 / 2 |
| 16 | 2 bullets | 3 / 2 |
| 17 | `EDUCATION` + `FAESA` + degree | 3 / 3 |
| 18 | `Feb 2022 - Dec 2025` + location | 2 / 2 |

Both files contain exactly **4 bullet blocks, one per role, none split.** Every
split boundary in the document falls between the header's two `tabular*` rows
or immediately after the header. The opened-up spacing from CV-SPEC item 2 did
not introduce a single new break inside a role's evidence. No page break, no
stray blank line, no other cause.

### 0.6 — the date is severed by the header, nothing else

Raw lines 19-23 of `base-en.pdf`:

```
DexCare
Senior Software Engineer

Jan 2026 - Present
Remote
```

The date string is correct and complete in all four roles. It is not on the
title line and a blank line stands between them, so it is not adjacent either.
That gap is produced by the header's second `tabular*` row. Nothing else in
the document separates a date from a title.

### Small gain since r1

The education block now emits `Feb 2022 - Dec 2025` **before**
`Vitória, ES, Brazil`. In r1 the city came first and sat between the degree and
the graduation date. The date is still one block away from the degree, but the
intervening city is gone.

## LinkedIn string match against DOSSIER ground truth

No portal run. The live profile matched `DOSSIER.md` character for character in
the r1 run and nothing has changed since. `Luizalabs` spelling is final.

| Field | DOSSIER ground truth | base-en | base-pt |
|---|---|---|---|
| Company 1 | `DexCare` | PASS | PASS |
| Title 1 | `Senior Software Engineer` | PASS | PASS |
| Dates 1 | `Jan 2026 - Present` | PASS | PASS |
| Company 2 | `Luizalabs` | PASS | PASS |
| Title 2 | `Mid-level Software Engineer` | PASS | PASS |
| Dates 2 | `Jan 2024 - Jan 2026` | PASS | PASS |
| Company 3 | `Lippaus Distribuidora` | PASS | PASS |
| Title 3 | `Mid-level Software Engineer` | PASS | PASS |
| Dates 3 | `Jan 2023 - Jan 2024` | PASS | PASS |
| Company 4 | `Lippaus Distribuidora` | PASS | PASS |
| Title 4 | `Entry-level Fullstack Software Engineer` | PASS | PASS |
| Dates 4 | `Mar 2021 - Jan 2023` | PASS | PASS |
| School | `FAESA` | PASS | PASS |
| Education dates | `Feb 2022 - Dec 2025` | PASS | PASS |

**All twelve job strings, the school name and the education date match.** Each
appears as a standalone line in the raw extraction, so every value is
individually recoverable despite the header split.

The degree string carries the two accepted deviations: the CV drops LinkedIn's
space before the comma, and the PT file translates the degree name. Not
re-flagged.

## Fullstack Labs clause — confirmed removed

`grep -icE 'fullstack labs|consultanc|consultoria'`

| Target | Hits |
|---|---|
| `base-en.tex` | **0** |
| `base-pt.tex` | **0** |
| `base-en` raw extraction | **0** |
| `base-pt` raw extraction | **0** |

The Luizalabs bullet now reads:

> `Delivered electronic invoice issuing for Magazine Luiza's e-commerce
> operation by building distributed tax microservices in Node.js, Java, and Go.`

> `Entregou a emissão de notas fiscais eletrônicas do e-commerce do Magazine
> Luiza construindo microsserviços fiscais distribuídos em Node.js, Java e Go.`

The false consultancy claim is gone from both files, in source and in the text
layer. Confirmed.

## Mechanical checks

| Check | base-en | base-pt |
|---|---|---|
| `ruby\|rails\|sidekiq\|activerecord\|rspec\|hotwire` in `.tex` | 0 | 0 |
| same, raw extraction | 0 | 0 |
| same, layout extraction | 0 | 0 |
| `[UNVERIFIED]` in `.tex` | 0 | 0 |
| `[UNVERIFIED]` in raw extraction | 0 | 0 |
| Per-term appearance cap of 3 | no token over cap | no token over cap |
| Pages (`pdfinfo`) | 1 | 1 |

36 load-bearing tokens counted case-insensitively. None exceeds three
appearances in either file. One page held despite the added bullet and the
opened-up spacing.

## Gate 2 — orphan tokens

Gate 2 was not scored; there is no posting. Step-4 stuffing input only.

| | first | r1 | r2 | **r4** |
|---|---|---|---|---|
| Skills-only tokens with no `Experience` evidence | 7 | `REST` | `Claude Code`, `Codex`, `Agentic workflows` | **`Agentic workflows`** |
| Deduction | 35 | 5 | 15 | **5** |

Both files, identical.

`Claude Code` and `Codex` are fixed. The new DexCare bullet supplies the
evidence:

> `Produce high-quality code in daily delivery by building Claude Code and
> Codex agent environments with shared rules, lint enforcement, cyclomatic
> complexity limits, and tests.`

`Agentic workflows` remains an orphan. It is in `SKILLS` under `Testing and AI
tooling`. The Summary says `Integrates AI-driven agentic workflows into daily
delivery`, and the new bullet says `agent environments`, but no `Experience`
bullet contains the token. RUBRIC step 4 counts evidence in `Experience` only.

## Gate 3 — human scan, reported not blocking

Identical in both files.

| # | Check | Points | Awarded | Note |
|---|---|---|---|---|
| 3.1 | Target title in the top 15% | 15 | 15 | `Senior Software Engineer` at raw line 6; the 15% mark is line 11 of 78. The r2 watch item is cleared: it passed by one line there, by five here. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20 | 20 | DexCare bullets 1-3: event-driven TypeScript on Express and Koa, Epic EMR integration, multi-tenant REST APIs with Auth0 JWT and OpenAPI validation. Graded generically; there is no posting. |
| 3.3 | Every bullet leads with an outcome or action verb | 15 | 15 | All 15 EN bullets: Deliver, Keep, Isolate, Serve, Reduce, Produce, Delivered, Improved, Gave, Kept, Supported, Handled, Turned, Supported, Delivered. PT equivalent verified. Zero "Responsible for". |
| 3.4 | At least 3 bullets carry a real number | 15 | **0** | **FAIL, known.** One bullet contains a digit and it is the product name `Auth0`. No metric anywhere. Blocked on Lucas. |
| 3.5 | 1 page under 10 years | 10 | 10 | 1 page, both files, after adding a bullet and opening the spacing. |
| 3.6 | No unsupported buzzwords | 10 | 10 | Zero hits. |
| 3.7 | Skills grouped by category | 10 | 10 | Six labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing and AI tooling. |
| 3.8 | Scannable spacing, bold titles, white space | 5 | 5 | Bold company, right-aligned dates, italic title and location, uniform bullets. The CV-SPEC item 2 spacing change is applied: `\vspace{2pt}` before and after the header replaces the template's `\vspace{-7pt}`, and the bullet list is `nosep`. |

**Gate 3: 85/100, both files.** The 15 missing points are 3.4 and nothing else.

## Run history

| Run | Header | Gate 0 raw | Gate 0 under exception | Gate 2 deduction | Gate 3 | UNVERIFIED |
|---|---|---|---|---|---|---|
| first | shape A | 8/8 | — | 35 | 85 | 14 |
| r1 | shape C | 4/8 | — | 5 | 75 | 9 |
| r2 | shape A | 8/8 | — | 15 | 85 | 0 |
| **r4** | **shape C** | **4/8** | **PASS** | **5** | **85** | **0** |

r4 carries the r1 header with none of the r1 collateral damage. Gate 2 and
Gate 3 are at their best measured values and the text layer is clean.

## Fix list

Gate 0 passes under the exception. Two items, neither blocking.

1. **Gate 2, 5-point orphan deduction.** `Agentic workflows` sits in `SKILLS`
   with no `Experience` bullet behind it. The DexCare AI bullet already exists;
   changing `agent environments` to name agentic workflows in that bullet, or
   dropping the term from Skills, clears it. One-line change, and it is the only
   recoverable point loss outside 3.4.

2. **Gate 3.4, numbers.** Blocked on Lucas, not on the Architect. Three bullets
   need a real, defensible figure. His own LinkedIn DexCare and Luizalabs
   entries publish two, recorded in the r1 report; they are not in
   `DOSSIER.md`, so I cannot mark them verified.

No other defect found. The pair is ready to tailor against a posting.

## Standing note, not a defect

The accepted exception is scoped to this base pair and to the header alone. Two
things follow from it, recorded so they are not lost:

- On a strict parsing ATS, this build still yields 12 fragments for 4 roles and
  a tenure the parser must infer from a date block it cannot key to a title.
  `CV-SPEC.md` item 2 keeps shape A as the fallback for a posting known to route
  that way. `reports/macro-bakeoff.md` holds the tested macro source.
- Every tailored CV built from this base inherits the same four reported
  failures. A future Gate 0 run on a tailored file should confirm the header is
  still the sole cause rather than assume it, since a new construct in a
  tailored variant would block.

## Claims I could not verify

None. `grep -c UNVERIFIED` returns 0 for both `.tex` sources and both raw
extractions. Lucas confirmed every claim on 2026-09-01, and the one claim that
was later contradicted, the Fullstack Labs consultancy clause, has been removed
and verified absent.

The Rails core and community gem contribution from the old PDFs remains absent
from both files. Still correct.
