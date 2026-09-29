# Gate 0 final (r2) — base CV pair, shape A restored

Files under test: `~/career/resumes/base-en.pdf`, `~/career/resumes/base-pt.pdf`
and their `.tex` sources.
Rubric: `~/career/RUBRIC.md` Gate 0, all 8 checks, 0.4 allowlist of 2026-09-01.
Ground truth: `~/career/DOSSIER.md`, "LinkedIn ground truth", confirmed against
the live profile in the r1 run and unchanged since.
Date: 2026-09-01. Analyst: ATS Analyzer. No file was edited.

Supersedes `reports/base-cv-gate0-r1.md`.

Changes made by the Resume Architect since r1: role header switched to shape A,
every `[UNVERIFIED]` marker cleared after Lucas confirmed the claims, six Skills
groups restored, `REST` evidence added to a DexCare bullet, AI tokens replaced
with `Claude Code | Codex | Agentic workflows`.

Settled before this run and not re-flagged: ASCII hyphen on the FAESA date is
final per the clarified `CLAUDE.md` rule 1; `Remote` is the correct location
value; the LinkedIn headline is Lucas's to edit.

## Verdict

| File | Gate 0 |
|---|---|
| `base-en.pdf` | **PASS**, 8 of 8 |
| `base-pt.pdf` | **PASS**, 8 of 8 |

Both files clear Gate 0. The r1 regression is fully reversed.

| Run | Header | Gate 0 | Gate 2 orphan deduction | Gate 3 | UNVERIFIED |
|---|---|---|---|---|---|
| first | shape A | 8/8 | 35 | 85 | 14 |
| r1 | shape C | 4/8 | 5 | 75 | 9 |
| **r2** | **shape A** | **8/8** | **15** | **85** | **0** |

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
| 0.1 | Text layer exists | PASS | 53 lines of clean text. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00–U+FB06, zero NUL, zero U+FFFD. `ff`/`fi`/`fl` words intact: `fiscal flags flows notifications office workflows`. |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, `\pagestyle{empty}` so no header or footer: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. |
| 0.4 | Section headers | PASS | `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, one standalone occurrence each. Uppercase rendering allowed under the 2026-09-01 allowlist. |
| 0.5 | **Employment-block segmentation** | PASS | 4 roles, 4 blocks. No role split, no two roles merged. See the block table below. |
| 0.6 | Date parseability | PASS | Every role carries `Mon YYYY - Mon YYYY` on the same line as its title, ASCII hyphen: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`. |
| 0.7 | Reading order | PASS | Raw and layout agree line for line after whitespace normalisation. `diff` returns nothing. |
| 0.8 | No forbidden constructs | PASS | No `tabular`, `tabularx`, `includegraphics`, `minipage`, `parbox`, `fbox`, `marvosym` or icon font anywhere in the source. `pdfimages -list` reports 0 images. |

## Gate 0 — base-pt.pdf

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 51 lines of clean text. |
| 0.2 | Glyph integrity | PASS | Zero U+FB00–U+FB06, zero NUL, zero U+FFFD. `backoffice confiáveis filas fiscais flags fluxos notificações workflows` all intact. Portuguese accents correct, no mojibake. |
| 0.3 | Contact block recoverable | PASS | Raw line 3, same fields, `Brasil`. |
| 0.4 | Section headers | PASS | `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, one standalone occurrence each. Matches the PT allowlist. |
| 0.5 | **Employment-block segmentation** | PASS | 4 roles, 4 blocks. |
| 0.6 | Date parseability | PASS | Same date strings as EN, on the title line, ASCII hyphen. |
| 0.7 | Reading order | PASS | Raw and layout agree. `diff` returns nothing. |
| 0.8 | No forbidden constructs | PASS | Same as EN. 0 images. |

## What a parser now sees, per role

Verbatim from `pdftotext base-en.pdf -`, raw lines 19-24:

```
EXPERIENCE
DexCare | Senior Software Engineer | Jan 2026 - Present | Remote
• Deliver real-time visit booking and provider availability for a healthcare scheduling platform by building event-driven TypeScript
services on Express and Koa.
• Keep bookable time slots in sync with hospital records by integrating Epic EMR interconnect and time-slot flows into the booking
pipeline.
```

Company, title, tenure and location arrive on one line, in one text run, in
reading order, immediately followed by that role's evidence. The r1 failure
mode is gone: no severed date, no three-way split, no location in an
organisation position.

Block structure of the raw stream, both files, 9 blank-line-delimited blocks:

| Block | Content | Lines (EN / PT) |
|---|---|---|
| 1 | `Lucas Queiroz` | 1 / 1 |
| 2 | contact line | 1 / 1 |
| 3 | `SUMMARY` + summary prose | 5 / 5 |
| 4 | `SKILLS` + 6 group lines | 7 / 7 |
| 5 | `EXPERIENCE` + DexCare header + 5 bullets | 12 / 11 |
| 6 | Luizalabs header + 4 bullets | 8 / 8 |
| 7 | Lippaus Mid-level header + 3 bullets | 4 / 4 |
| 8 | Lippaus Entry-level header + 2 bullets | 4 / 3 |
| 9 | `EDUCATION` + FAESA line | 2 / 2 |

Each role is exactly one block, with its header line first. Blocks 5 and 9
carry the section label above the first entry, which is the normal consequence
of a heading with no blank line after it; the same pattern holds for `SUMMARY`
and `SKILLS`. It is not a role split or a role merge, so 0.5 passes. I note it
because in r1 the equivalent block was `EXPERIENCE / DexCare / Senior Software
Engineer`, where the company sat alone on the line after the label and could be
misread. Here the header line is self-labelling with three separators, so the
same artifact carries no ambiguity.

## LinkedIn string match against DOSSIER ground truth

No portal run this time. The live profile matched `DOSSIER.md` character for
character in the r1 run and nothing has changed since.

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

**All twelve job strings, the school name and the education date match.**

The FAESA education date now passes outright. `CLAUDE.md` rule 1 was clarified
on 2026-09-01: the rule governs the periods, not the glyphs, and the separator
follows `CV-SPEC.md`. The ASCII hyphen is correct. This closes the conflict
raised in the two previous reports.

The degree string carries the two known, accepted deviations: the CV drops
LinkedIn's space before the comma, and the PT file translates the degree name.
Neither is re-flagged.

## Mechanical checks

| Check | base-en | base-pt |
|---|---|---|
| `ruby\|rails\|sidekiq\|activerecord\|rspec\|hotwire` in `.tex` | 0 | 0 |
| same, raw extraction | 0 | 0 |
| same, layout extraction | 0 | 0 |
| `[UNVERIFIED]` in `.tex` | **0** | **0** |
| `[UNVERIFIED]` in raw extraction | **0** | **0** |
| Per-term appearance cap of 3 | no token over cap | no token over cap |
| Pages (`pdfinfo`) | 1, 612 x 792 pts | 1, 612 x 792 pts |

38 load-bearing tokens were counted. None exceeds three appearances in either
file. All 14 UNVERIFIED markers from the first build and all 9 from r1 are
gone, in both the source and the text layer.

## Gate 2 — orphan tokens

Gate 2 was not scored; there is no posting. The step-4 stuffing input only.

| | first build | r1 | **r2** |
|---|---|---|---|
| Skills-only tokens with no `Experience` evidence | `JavaScript`, `SQL`, `REST`, `Swagger`, `CI/CD`, `Vitest`, `Jest` | `REST` | **`Claude Code`, `Codex`, `Agentic workflows`** |
| Deduction at 5 points each | 35 | 5 | **15** |

Both files, identical.

`REST` is fixed. The DexCare bullet now reads `securing multi-tenant REST APIs
with Auth0 JWT`, which supplies the evidence that was missing in r1.

Three new orphans replaced it. `Testing and AI tooling: Vitest | Jest | Claude
Code | Codex | Agentic workflows` puts `Claude Code`, `Codex` and `Agentic
workflows` in `SKILLS`, and no `Experience` bullet contains any of the three.
The Summary sentence `Integrates AI-driven agentic workflows to accelerate
development cycles` is the only supporting text, and RUBRIC Gate 2 step 4
counts evidence in `Experience` only.

The deduction rose from 5 to 15 points. This is the one number in the report
that moved the wrong way.

## Gate 3 — human scan, reported not blocking

Identical in both files.

| # | Check | Points | Awarded | Note |
|---|---|---|---|---|
| 3.1 | Target title in the top 15% | 15 | 15 | `Senior Software Engineer` first appears at raw line 6; the 15% mark is line 7 of 53. It passes by one line. The document has no standalone title line under the name, so the title survives only inside the Summary sentence. Any future edit that lengthens the contact area or the Summary opening will push it past the threshold. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20 | 20 | DexCare bullets 1-3 carry event-driven TypeScript on Express and Koa, Epic EMR integration, and multi-tenant REST APIs with Auth0 JWT and OpenAPI validation. Graded generically; there is no posting. |
| 3.3 | Every bullet leads with an outcome or action verb | 15 | 15 | All 14 EN bullets: Deliver, Keep, Isolate, Serve, Reduce, Delivered, Improved, Gave, Kept, Supported, Handled, Turned, Supported, Delivered. PT equivalent verified. Zero "Responsible for". |
| 3.4 | At least 3 bullets carry a real number | 15 | **0** | **FAIL, known.** One bullet contains a digit and it is the product name `Auth0`. No metric anywhere. Still blocked on Lucas. |
| 3.5 | 1 page under 10 years | 10 | 10 | `pdfinfo`: 1 page, both files. |
| 3.6 | No unsupported buzzwords | 10 | 10 | Zero hits. |
| 3.7 | Skills grouped by category | 10 | 10 | **Regression fixed.** Six labelled groups restored: Languages, Backend, Data, Frontend, Cloud and operations, Testing and AI tooling. |
| 3.8 | Scannable spacing, bold titles, white space | 5 | 5 | Bold company names, ruled section headers, uniform bullet indent, one blank line between roles. |

**Gate 3: 85/100, both files.** Back to the first build's score, and now with
zero `[UNVERIFIED]` markers in the text layer, which the first build did not
have.

The 15 missing points are 3.4 and nothing else.

## Fix list

Gate 0 passes, so nothing here blocks. Three items, ranked by cost.

1. **Gate 2, 15-point orphan deduction.** `Claude Code`, `Codex` and
   `Agentic workflows` sit in `SKILLS` with no `Experience` bullet behind them.
   Either put one of them in a true bullet in a real role, or drop the group
   from Skills. The Summary sentence does not satisfy RUBRIC step 4. This is
   the largest recoverable loss in the document and it is a two-line change.

2. **The Fullstack Labs claim is now known to be false.** Both files,
   `base-en.tex:85` and `base-pt.tex:85`:

   > `Delivered electronic invoice issuing for Magazine Luiza's e-commerce
   > operation, engaged through the consultancy Fullstack Labs, by building
   > distributed tax microservices in Node.js, Java, and Go.`

   > `Entregou a emissão de notas fiscais eletrônicas do e-commerce do Magazine
   > Luiza, alocado pela consultoria Fullstack Labs, construindo microsserviços
   > fiscais distribuídos em Node.js, Java e Go.`

   Lucas stated on 2026-09-01 that Luizalabs was a direct employment contract in
   Brazil, not a consultancy engagement, and that both DexCare and Luizalabs are
   full-time positions. The clause `engaged through the consultancy Fullstack
   Labs` / `alocado pela consultoria Fullstack Labs` contradicts that. Remove
   the clause. Lucas said the contract detail itself does not belong on the CV,
   so nothing replaces it. Not a Gate 0 defect, and the most serious factual
   defect in the pair.

3. **Gate 3.4, numbers.** Blocked on Lucas. Three bullets need a real,
   defensible figure. His own LinkedIn DexCare and Luizalabs entries already
   publish two, noted in the r1 report; they are not in `DOSSIER.md`, so I
   cannot mark them verified.

Watch item, no action needed now: 3.1 passes by one line. Line 6 against a
threshold of line 7. Any growth in the Summary opening or the contact area
drops it.

## Notes recorded, no action taken

- **`DOSSIER.md` needs an update, and it is not mine to write.** The dossier
  records under "Open discrepancy, flagged not resolved" that LinkedIn shows
  DexCare and Luizalabs as `Full-time` while Lucas stated both were engagements
  through Fullstack Labs. Lucas resolved this on 2026-09-01: Luizalabs was a
  direct CLT contract and both roles are full-time. LinkedIn was right. The
  dossier entry is now stale.

- **`CLAUDE.md` section 3 is stale on the same point.** It states
  `LuizaLabs / Magazine Luiza: Mid-level, engaged through Fullstack Labs, not a
  direct employee`. The employment-type half of that line is now known to be
  wrong. I did not edit it.

- **Company spelling, unresolved.** `CLAUDE.md` section 3 writes `LuizaLabs`.
  The live LinkedIn profile and `DOSSIER.md` both render `Luizalabs`. Both CVs
  currently write `Luizalabs`, which matches the profile and the dossier, and
  which is why the string match above passes. Lucas replied `LuizaLabs` when
  the three conflicts were put to him. I have not treated that as an
  instruction to change the CVs, because doing so would break the ground-truth
  match this report certifies. One word from Lucas settles it: if the CVs should
  read `LuizaLabs`, then `DOSSIER.md` needs the same change first, and the
  string match will then be graded against the new value.

## Claims I could not verify

None. Lucas confirmed every claim on 2026-09-01 and all `[UNVERIFIED]` markers
were cleared. `grep -c UNVERIFIED` returns 0 for both `.tex` sources and both
raw extractions.

One claim on the CVs is now positively contradicted rather than merely
unverified: the Fullstack Labs consultancy clause, fix item 2 above. It is
listed there, not here, because it needs removal rather than verification.

The Rails core and community gem contribution from the old PDFs remains absent
from both files. That is still correct.
