# Gate 0 r7 — base CV pair

Files under test: `~/career/resumes/base-en.pdf`, `~/career/resumes/base-pt.pdf`
and their `.tex` sources.
Rubric: `~/career/RUBRIC.md` Gate 0, all 8 checks, the 0.4 allowlist and the
**Accepted exception** of 2026-09-01.
Ground truth: `~/career/DOSSIER.md`, "LinkedIn ground truth" and
"Bullet metrics supplied by Lucas".
Date: 2026-09-01. Analyst: ATS Analyzer. No file was edited.

Supersedes `reports/base-cv-gate0-r4.md`.

Changes since r4: six bullets gained a figure (D2, D3, D5, L2, L3, P2); a new
DexCare bullet D7 covering the Shared Platform Initiative; `RabbitMQ` and
`AMQP` added to Skills; `Agentic workflows` now named in the AI bullet; spacing
changed.

## Verdict

| File | Gate 0 under the accepted exception |
|---|---|
| `base-en.pdf` | **PASS** |
| `base-pt.pdf` | **PASS** |

0.5, 0.6, 0.7 and 0.8 fail on the raw extraction. **The two-column header is the
sole cause of all four, in both files.** No other cause found. Reported, not
blocking. Nothing else blocks.

## Extraction

```
pdftotext          base-en.pdf -    pdftotext -layout base-en.pdf -
pdftotext          base-pt.pdf -    pdftotext -layout base-pt.pdf -
```
poppler 26.08.0.

## Gate 0 — base-en.pdf

| # | Check | Result | Header the sole cause? | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | — | 79 lines of clean text. |
| 0.2 | Glyph integrity | PASS | — | Zero codepoints in U+FB00–U+FB06, zero NUL, zero U+FFFD. `ff`/`fi`/`fl` words intact: `configuration fiscal flags flows notifications office workflows`. |
| 0.3 | Contact block recoverable | PASS | — | Raw line 3, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. |
| 0.4 | Section headers | PASS | — | `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, one standalone occurrence each. |
| 0.5 | Employment-block segmentation | **FAIL** | **Yes** | 3 blocks per role. 18 blocks total, of which exactly 4 are bullet blocks, one per role, none split. |
| 0.6 | Date parseability | **FAIL** | **Yes** | A blank line separates every date from its title. All four date strings are correct and complete. |
| 0.7 | Reading order | **FAIL** | **Yes** | 5 diff hunks, all 5 are `tabular*` blocks: four role headers and the education header. No bullet, section header, Summary or Skills line disagrees. |
| 0.8 | No forbidden constructs | **FAIL** | **Yes** | `base-en.tex:41` `\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}`, closed at `:44`. The only construct in the file. 0 images, no text box, no icon, no photo. |

## Gate 0 — base-pt.pdf

| # | Check | Result | Header the sole cause? | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | — | 78 lines of clean text. |
| 0.2 | Glyph integrity | PASS | — | Zero U+FB00–U+FB06, zero NUL, zero U+FFFD. `backoffice confiáveis configurações filas fiscais flags fluxos notificações workflows` intact. Accents correct, no mojibake. |
| 0.3 | Contact block recoverable | PASS | — | Raw line 3, same fields, `Brasil`. |
| 0.4 | Section headers | PASS | — | `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, one standalone occurrence each. PT allowlist. |
| 0.5 | Employment-block segmentation | **FAIL** | **Yes** | Identical structure to EN. 18 blocks, 4 bullet blocks, none split. |
| 0.6 | Date parseability | **FAIL** | **Yes** | Identical to EN. |
| 0.7 | Reading order | **FAIL** | **Yes** | 5 diff hunks, all 5 header blocks. |
| 0.8 | No forbidden constructs | **FAIL** | **Yes** | `base-pt.tex:41` and `:44`, same `tabular*`, the only construct. 0 images. |

## Header-sole-cause attribution

Each failure was tested for any cause other than the header.

**0.8.** `grep -nE 'tabular|tabularx|includegraphics|minipage|parbox|fbox|marvosym|fontawesome'`
returns exactly two lines per file, the header's own `tabular*` open and close.
`pdfimages -list` reports 0 images in both. Nothing else triggers 0.8.

**0.7.** The full `diff` between the normalised raw and layout extractions
produces 5 hunks per file. All 5 are `tabular*` blocks. Verbatim, `<` raw,
`>` layout:

```
< DexCare
< Senior Software Engineer
< Jan 2026 - Present
< Remote
---
> DexCare                    Jan 2026 - Present
> Senior Software Engineer   Remote
```

**0.5.** 18 blank-line-delimited blocks per file. Exactly 4 are bullet blocks,
one per role, none split:

| Bullet block | Lines EN / PT |
|---|---|
| DexCare, 7 bullets | 12 / 12 |
| Luizalabs, 4 bullets | 7 / 7 |
| Lippaus Mid-level, 3 bullets | 4 / 3 |
| Lippaus Entry-level, 2 bullets | 3 / 2 |

Every split boundary falls between the header's two `tabular*` rows or
immediately after the header. The added D7 bullet and the changed spacing
introduced no new break inside a role's evidence.

**0.6.** Raw lines 19-23 of `base-en.pdf`:

```
DexCare
Senior Software Engineer

Jan 2026 - Present
Remote
```

The gap is produced by the header's second `tabular*` row. Nothing else in
either document separates a date from a title.

## Figure verification against DOSSIER "Bullet metrics supplied by Lucas"

Every bullet was rejoined from its wrapped lines, then every `NN%` token in it
was compared against the dossier assignment for that bullet ID, in dossier
order.

| ID | Bullet | Dossier figure | Printed, base-en | Printed, base-pt | Result |
|---|---|---|---|---|---|
| D1 | booking services | none | none | none | OK |
| D2 | Epic EMR time-slot sync | `15%` | `15%` | `15%` | **OK** |
| D3 | Auth0 JWT multi-tenant APIs | `25%` | `25%` | `25%` | **OK** |
| D4 | data modeling | none | none | none | OK |
| D5 | feature flags | `7%` | `7%` | `7%` | **OK** |
| D6 | agentic / AI tooling | none | none | none | OK |
| D7 | Shared Platform Initiative | `33%` | `33%` | `33%` | **OK** |
| L1 | invoice issuing | none | none | none | OK |
| L2 | SEFAZ async BullMQ | `20%` | `20%` | `20%` | **OK** |
| L3 | fiscal dashboards | `18%` | `18%` | `18%` | **OK** |
| L4 | deployment | none | none | none | OK |
| P1 | multi-tenant platform | none | none | none | OK |
| P2 | Lippaus BullMQ jobs | `26%` | `26%` | `26%` | **OK** |
| P3 | project scoping | none | none | none | OK |
| E1 | backoffice dashboards | none | none | none | OK |
| E2 | customer-facing features | none | none | none | OK |

**No figure mismatch.** All seven figures match the dossier exactly, each sits
on the bullet Lucas assigned it to, and no bullet marked "no number" carries
one. Both files agree.

Each figure is also attached to the correct claim, not merely to the correct
bullet:

- D2 `reduce wrong bookings by 15%` — dossier: "reduced wrong bookings by 15%".
- D3 `reduce authentication friction by 25%` — dossier: "reduced authentication friction by 25%".
- D5 `Reduce release risk by 7%` — dossier: "release risk reduced by 7%".
- D7 `Reduce new-client pilot friction by 33%` — dossier: "reducing friction for piloting new clients by 33%".
- L2 `Improved invoice throughput by 20%` — dossier: "20% improvement in invoice processing throughput".
- L3 `cut support tickets by 18%` — dossier: "18% fewer support tickets".
- P2 `26% more processing capacity` — dossier: "26% more processing capacity".

### D7 handling constraints

The dossier attaches three constraints to D7. All three hold.

- **Describe conceptually, no technical depth.** The bullet reads
  `helping implement the Shared Platform Initiative (SPI), replacing
  per-customer environments with shared service instances and isolated
  configuration, secrets, and data stores`. That matches the dossier's own
  conceptual summary and adds no implementation detail.
- **Do not print internal customer names.** `grep -icE
  'providence|kaiser|permanente|piedmont'` returns 0 in both `.tex` files and
  both raw extractions.
- **No internal links.** `grep -icE 'atlassian\.net|confluence'` returns 0 in
  all four targets. The Confluence URLs stay in the dossier.

## LinkedIn string match against DOSSIER ground truth

No portal run. The live profile matched the dossier character for character in
the r1 run and nothing has changed since. `Luizalabs` spelling is final.

| Field | Ground truth | base-en | base-pt |
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

All twelve job strings, the school name and the education date match. Each is a
standalone line in the raw extraction, so every value stays individually
recoverable despite the header split.

Two related dossier rules also hold: role locations print `Remote` / `Remoto`
only, with no employer city anywhere (`Seattle` and `São Paulo` return 0 hits);
and the banned sentence "Works remotely from Brazil with US-based teams" and
its Portuguese equivalent are absent from both files.

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
| Fullstack Labs / consultancy clause | 0 | 0 |

38 load-bearing tokens counted case-insensitively, including the two new ones.
None exceeds three appearances. One page held after adding a seventh DexCare
bullet, seven figures and two Skills tokens.

## Gate 2 — orphan tokens

Gate 2 was not scored; there is no posting. Step-4 stuffing input only.

| | first | r1 | r2 | r4 | **r7** |
|---|---|---|---|---|---|
| Skills-only tokens with no `Experience` evidence | 7 | `REST` | 3 | `Agentic workflows` | **`Swagger`, `RabbitMQ`, `AMQP`** |
| Deduction | 35 | 5 | 15 | 5 | **15** |

Both files, identical. The 15 points split into two very different halves.

**Accepted, 10 points.** `RabbitMQ` and `AMQP` are orphans by design. The
dossier records them as Skills tokens only, with no service names on the CV
[FACT, Lucas 2026-09-01]. They sit in `Backend:` and no bullet names them.
This is the expected cost of that instruction, not a defect.

**Unintended regression, 5 points.** `Swagger` was evidenced in r4 and is not
in r7. The r4 D3 bullet read `validating requests against OpenAPI/Swagger
specs`. The r7 rewrite that added the 25% figure changed it to `using Auth0 JWT
and OpenAPI validation on multi-tenant REST APIs`, dropping the `Swagger`
token. `grep -in swagger` now returns exactly one line per file, the Skills
line. `Agentic workflows` is fixed: the D6 bullet names it.

## Gate 3 — human scan, reported not blocking

Identical in both files.

| # | Check | Points | Awarded | Note |
|---|---|---|---|---|
| 3.1 | Target title in the top 15% | 15 | 15 | `Senior Software Engineer` at raw line 6; the 15% mark is line 11 of 79. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20 | 20 | DexCare bullets 1-3: event-driven TypeScript on Express and Koa, Epic EMR sync with a 15% figure, multi-tenant REST APIs with Auth0 JWT and a 25% figure. Two of the first three now carry a number. Graded generically; there is no posting. |
| 3.3 | Every bullet leads with an outcome or action verb | 15 | 15 | All 16 bullets lead with a verb in both languages. Zero "Responsible for". |
| 3.4 | At least 3 bullets carry a real number | 15 | **15** | **Now PASS.** Seven bullets carry a percentage: D2 15%, D3 25%, D5 7%, D7 33%, L2 20%, L3 18%, P2 26%. All seven trace to `DOSSIER.md` and are marked interview-defensible by Lucas. The requirement is three. |
| 3.5 | 1 page under 10 years | 10 | 10 | 1 page, both files. |
| 3.6 | No unsupported buzzwords | 10 | 10 | Zero hits. |
| 3.7 | Skills grouped by category | 10 | 10 | Six labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing and AI tooling. |
| 3.8 | Scannable spacing, bold titles, white space | 5 | 5 | Bold company, right-aligned dates, italic title and location, uniform bullets, `\vspace{5pt}` after the header. |

**Gate 3: 100/100, both files.** First run with no Gate 3 deduction. The 3.4
failure that stood through every prior run is closed.

## Run history

| Run | Header | Gate 0 raw | Under exception | Gate 2 deduction | Gate 3 | UNVERIFIED |
|---|---|---|---|---|---|---|
| first | shape A | 8/8 | — | 35 | 85 | 14 |
| r1 | shape C | 4/8 | — | 5 | 75 | 9 |
| r2 | shape A | 8/8 | — | 15 | 85 | 0 |
| r4 | shape C | 4/8 | PASS | 5 | 85 | 0 |
| **r7** | **shape C** | **4/8** | **PASS** | **15** | **100** | **0** |

## Fix list

Gate 0 passes under the exception. One item, not blocking.

1. **`Swagger` lost its Experience evidence, 5 Gate 2 points.** Both files.
   The r7 rewrite of D3 dropped the token while adding the 25% figure. Restoring
   it costs nothing: the bullet already describes OpenAPI validation, so
   `OpenAPI/Swagger validation` in place of `OpenAPI validation` recovers the
   points without touching the figure or the claim. One word per file.

No other defect found. `RabbitMQ` and `AMQP` cost 10 more Gate 2 points and I
am not listing them as a fix, because printing them in a bullet would require
naming the services that use them, which the dossier forbids. That trade is
already Lucas's decision.

## Standing note, not a defect

Unchanged from r4, restated because it survives this run:

- On a strict parsing ATS this build still yields 12 fragments for 4 roles, and
  a tenure the parser must infer from a date block it cannot key to a title.
  `CV-SPEC.md` item 2 keeps shape A as the fallback; the tested macro source is
  in `reports/macro-bakeoff.md`.
- Every tailored CV built from this base inherits the same four reported
  failures. A Gate 0 run on a tailored file must re-confirm the header is still
  the sole cause rather than assume it. A new construct in a variant would
  block.

## Claims I could not verify

None. `grep -c UNVERIFIED` returns 0 for both `.tex` sources and both raw
extractions.

The seven figures are recorded in `DOSSIER.md` as `[FACT,
interview-defensible per Lucas]`. That is Lucas's attestation, not an
independent measurement, and I have not audited the underlying numbers. It is
the correct basis for printing them under the truth policy; it is also what
Lucas will be asked to defend in an interview.

The Rails core and community gem contribution from the old PDFs remains absent
from both files. Still correct.
