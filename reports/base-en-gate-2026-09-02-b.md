# ATS Analysis — resumes/base-en.pdf vs no-job (base-CV gate, hunt 2026-09-02-b)
Segment: n/a (base CV, no posting)   Date: 2026-09-02

Analyst: Sieve (ATS Analyzer). Scope set by Maestro: Gate 0 and Gate 3 only.
Gate 1 and Gate 2 are not run. There is no posting.

## Extraction (mandatory step)
Source file: `~/career/resumes/base-en.pdf`, 26956 bytes, 1 page, letter,
producer `xdvipdfmx (0.1)`, no metadata stream, not tagged.

```
pdftotext -layout base-en.pdf - > en-layout.txt   # 56 lines
pdftotext          base-en.pdf - > en-raw.txt     # 78 lines
```
Gate 0 is judged on `en-raw.txt`. Every quote below is verbatim from an
extraction, never from the `.tex` source and never from pasted text.

## Verdict
PASSES GATE 0 AND GATE 3.
Gate 0: 4 of 8 checks FAIL, and all 4 trace only to the `tabular*` role
header. Under the accepted exception in `RUBRIC.md` (Lucas, 2026-09-01) those
are reported and not blocking. No other cause of failure was found.
Gate 3: 99/100.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction is 78 lines of clean text. Line 1 `Lucas Queiroz`. No garbage. |
| 0.2 | Glyph integrity | PASS | Zero code points in U+FB00-U+FB06. Zero `\x00`. Zero U+FFFD. Positive proof of disabled ligatures: `back-office` (ffi carrier) at raw lines 47 and 68, `workflows` (fl carrier) at raw lines 8, 16, 34, 47, 68. Note: the canaries `profile`, `efficient` and `conflict` return zero hits because those words are absent from this document, not because of a glyph defect. |
| 0.3 | Contact block recoverable | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. In the body. Source uses `\pagestyle{empty}` and a `center` block; no `fancyhdr`, no header, no footer. |
| 0.4 | Section headers present verbatim | PASS | Standalone raw lines: 5 `SUMMARY`, 10 `SKILLS`, 18 `EXPERIENCE`, 72 `EDUCATION`. Uppercase rendering is allowed, case-insensitive. |
| 0.5 | Employment-block segmentation | **FAIL, non-blocking** | Each role splits into two raw blocks. Example, raw lines 19-23: `DexCare` / `Senior Software Engineer` / (blank) / `Jan 2026 - Present` / `Remote`. Cause is only the two-column `tabular*` in `\resumeSubheading`. **No two roles are merged.** Four company lines, four titles, correctly paired and in the right order: DexCare, Luizalabs, Lippaus Distribuidora, Lippaus Distribuidora. Accepted exception, `RUBRIC.md` and `CV-SPEC.md` item 2. |
| 0.6 | Date parseability | **FAIL, non-blocking** | The date is not on the same line as its title and is not adjacent to it. It sits two lines below, across a blank line. Raw lines 20-22: `Senior Software Engineer` / (blank) / `Jan 2026 - Present`. Same `tabular*` cause. The date strings themselves are all well formed and ASCII-hyphen: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Zero EN DASH or other non-ASCII dash anywhere in the file. |
| 0.7 | Reading order | **FAIL, non-blocking** | Raw order is Company, Title, Dates, Location. Layout order is Company, Dates, Title, Location. Layout line 19: `DexCare ... Jan 2026 - Present`; layout line 20: `Senior Software Engineer ... Remote`. The two adjacent blocks `Senior Software Engineer` and `Jan 2026 - Present` are ordered differently in the two streams. Same `tabular*` cause. |
| 0.8 | No forbidden constructs | **FAIL, non-blocking** | One construct: the `tabular*` role header. Nothing else. `pdfimages -list base-en.pdf` returns zero images, so there is no photo, no icon, and no image of text. No text box. |

## Gate 1 — Knockouts
Not run. There is no posting in this gate. Running it would require guessing
requirements, which is prohibited.

## Gate 2 — Retrieval coverage
Not run. Retrieval coverage is defined against a posting's token set. There is
no posting. No number is emitted.

## Gate 3 — Human scan: 99/100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15/15 | `Senior Software Engineer` at raw line 6 of 78, which is 7.7% into the document. It repeats in the DexCare role header at raw line 20. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20/20 | DexCare bullets 1-3 are the strongest and lead the role: event-driven TypeScript on Express and Koa; Epic EMR sync with 15%; multi-tenant REST APIs with Auth0 JWT and OpenAPI/Swagger with 25%. Two of the three carry a number. |
| 3.3 | Bullet voice and Summary voice | 15/15 | All 16 Experience bullets lead with a past-tense verb, subject omitted. Zero start with `I`. Zero present tense. Zero `Responsible for`. Zero third person. Summary opens `I am a Senior Software Engineer` and continues `I build`, `I previously built`, `I integrate`. Full list under **Voice check** below. |
| 3.4 | At least 3 bullets carry a real number | 15/15 | Seven bullets carry a number: 15%, 25%, 7%, 33%, 20%, 18%, 26%. Every one traces to `DOSSIER.md` bullet metrics (D2, D3, D5, D7, L2, L3, P2). |
| 3.5 | Length: 1 page under 10 years | 10/10 | `pdfinfo` reports `Pages: 1`. |
| 3.6 | No unsupported buzzwords | 10/10 | Zero hits for `team player`, `results-driven`, `passionate`, `detail-oriented`, `self-starter`, `synergy`, `hands-on`, `rockstar`, `ninja`. Two unsupported qualifiers exist (`nationwide`, `high-volume`) but they are claims, not the buzzwords this check names. They are reported under **Claims I could not verify**. |
| 3.7 | Skills grouped by category | 10/10 | Six labelled groups at raw lines 11-16: Languages, Backend, Data, Frontend, Cloud and operations, Testing and AI tooling. |
| 3.8 | Scannable | 4/5 | Consistent 5pt inter-role gap, bold company, italic title, one column, full width. **Minus 1: verb monotony.** `Built` opens 7 of the 16 bullets (raw lines 25, 28, 33, 44, 47, 58, 70). A recruiter scanning the left edge sees the same word repeatedly, which lowers the information value of the scan anchor. |

**Gate 3 total: 99/100.**

## Voice check (explicit, per CLAUDE.md section 9 and CV-SPEC.md)

Leading token of every Experience bullet, read from `en-raw.txt`:

| Raw line | Leading verb | Verdict |
|---|---|---|
| 25 | Built | past, subject omitted, OK |
| 27 | Integrated | OK |
| 28 | Built | OK |
| 30 | Modeled | OK |
| 32 | Reduced | OK |
| 33 | Built | OK |
| 35 | Helped | OK |
| 44 | Built | OK |
| 46 | Moved | OK |
| 47 | Built | OK |
| 49 | Deployed | OK |
| 58 | Built | OK |
| 59 | Processed | OK |
| 60 | Led | OK |
| 68 | Developed | OK |
| 70 | Built | OK |

- Bullets that break the rule: **none**. 16 of 16 pass.
- Bullets starting with `I`: **none** (`grep -E '^• *I '` returns zero).
- Present-tense bullets: **none**.
- `Responsible for` bullets: **none** (`grep -i 'responsible for'` returns zero).
- Third-person bullets: **none**.
- Summary uses `I`: **yes**. Raw line 6, `I am a Senior Software Engineer...`.

## Titles and dates against DOSSIER.md LinkedIn ground truth

| CV, raw extraction | DOSSIER LinkedIn ground truth | Match |
|---|---|---|
| `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` | `Senior Software Engineer`, `DexCare`, `Jan 2026 - Present` | exact |
| `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` | `Mid-level Software Engineer`, `Luizalabs`, `Jan 2024 - Jan 2026` | exact |
| `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | `Mid-level Software Engineer`, `Jan 2023 - Jan 2024` | exact |
| `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | `Entry-level Fullstack Software Engineer`, `Mar 2021 - Jan 2023` | exact |
| `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | dates exact after the CV-SPEC ASCII-hyphen rule; the degree string drops LinkedIn's stray space before the comma, which is a LinkedIn typo, not a date |

Company spelling `Luizalabs` is correct per DOSSIER. Both Lippaus roles are
kept separate, so the promotion signal survives.

## Stack positioning checks

| Check | Result |
|---|---|
| Ruby or Rails token anywhere (`.tex` and raw, word boundary: ruby, rails, rspec, sidekiq, activerecord, activejob, hotwire, devise, pundit, erb, gem) | **zero hits** |
| `[UNVERIFIED]` marker in `.tex` or raw | **zero hits** |
| UTC offset or `GMT` printed | **zero hits** |
| Term appearance cap of 3 (`CV-SPEC.md`) | **not exceeded.** Maximum is 3: TypeScript 3, Node.js 3, React 3, Go 3, PostgreSQL 3, AWS 3, BullMQ 3. All others are 1 or 2. |
| Every load-bearing technology in Skills and in an Experience bullet | holds for TypeScript, Node.js, React, Go, PostgreSQL, DynamoDB, Redis, Express, Koa, BullMQ, Auth0, OpenAPI/Swagger, Drizzle ORM, Sequelize, AWS, GCP, Docker, Kubernetes, ArgoCD, Datadog, LaunchDarkly, OpenFeature, Vitest, Jest, Claude Code, Codex. **RabbitMQ and AMQP appear in Skills only** (1 appearance each, raw line 12), which is the Gate 2 stuffing pattern if a posting ever indexes them. Lucas approved them as Skills-only tokens on 2026-09-01, so this is recorded, not a defect. |

## Defects, ranked by cost

1. **Lippaus role location prints an employer city, against a DOSSIER FACT** —
   Gate 3 / `DOSSIER.md` line 166. Raw lines 56 and 66 print
   `Vitória, ES, Brazil` as the location of both Lippaus roles. DOSSIER states:
   "**Role locations print `Remote` only.** ... No employer city on the CV.
   [FACT, Lucas 2026-09-01]". LinkedIn separately records Lippaus as
   `On-site`. The rule and the LinkedIn record conflict for this employer.
   **This is Lucas's decision, not the Architect's.** I do not know which he
   intends. Fix once decided: either replace both with `Remote`, or Lucas
   amends the DOSSIER rule to exempt the on-site Lippaus period.
2. **Unverifiable qualifiers in three bullets** — Gate 3 / truth handling.
   `nationwide retailer expansion`, `high-volume orders`, and
   `beverage distribution startup` are not in `DOSSIER.md`. See
   **Claims I could not verify**. Fix: confirm with Lucas, or mark
   `[UNVERIFIED]`, or drop the qualifier and keep the verified core.
3. **The pair has diverged in the Summary** — `CV-SPEC.md` Languages: "The
   bases ship as a pair ... Same facts, same structure, same dates." The PT
   Summary carries two statements this EN Summary does not:
   `sistemas backend e fullstack` and `para uma empresa dos EUA`. Same dates,
   same structure, but not the same facts. Fix: add the matching clauses here,
   or remove them from `base-pt.tex`. Lucas chooses the direction. I note that
   an explicit "for a US company" signal has no EN equivalent today, and that
   `DOSSIER.md` supports the country: LinkedIn records DexCare as
   `Seattle, Washington, United States`.
4. **Verb monotony** — Gate 3.8, minus 1 point. `Built` opens 7 of 16 bullets.
   Fix: vary the lead verb on three of them without changing the claim. For
   example raw line 44 `• Built distributed tax microservices in Node.js, Java,
   and Go...` could lead with `Delivered` or `Shipped`.
5. **`tabular*` role header, four Gate 0 findings** — Gate 0.5, 0.6, 0.7, 0.8.
   Reported, not blocking, by Lucas's 2026-09-01 decision. No action. The
   single-column shape A fallback in `reports/macro-bakeoff.md` stays available
   if a specific posting is known to route through a strict parser.

## Claims I could not verify

Traced against `DOSSIER.md`. I do not delete these and I do not defend them.
Lucas decides.

1. `5+ years` (Summary, raw line 6). Not stated in `DOSSIER.md`. It is
   arithmetically consistent with the LinkedIn ground truth: `Mar 2021` to
   today, 2026-09-02, is 5 years 6 months. Consistent, but not a recorded fact.
2. `nationwide retailer expansion` (Lippaus Mid-level, raw line 58). DOSSIER
   confirms "multi-tenant web and mobile platform on PostgreSQL". It records
   nothing about nationwide scope.
3. `high-volume orders` (Lippaus Mid-level, raw line 59). DOSSIER gives P2 as
   "26% more processing capacity". It records no volume figure, so
   `high-volume` is an added qualifier.
4. `beverage distribution startup` (Lippaus Entry-level, raw line 68). Not in
   `DOSSIER.md` in any form. `beverage` returns zero hits.
5. `Magazine Luiza's e-commerce operation` (Luizalabs, raw lines 44-45) and
   `Magazine Luiza's electronic-invoicing microservices` (Summary, raw lines
   7-8). DOSSIER confirms the fiscal / NF-e / SEFAZ domain as [FACT]. It does
   not carry the word `e-commerce`. `CV-SPEC.md` mentions "a Brazilian
   e-commerce retailer" only when retiring an older claim. Magazine Luiza being
   an e-commerce retailer is common knowledge, but it is not observable from
   this dossier, so I record it rather than assert it.
6. Pair divergence with `base-pt.pdf`, item 3 of the defect list. The PT
   Summary asserts `sistemas backend e fullstack` and `para uma empresa dos
   EUA`; this file asserts neither. Nothing here is false. The pair is not
   carrying the same facts.
7. Lippaus location, item 1 of the defect list. Recorded here as well because
   it is a factual conflict, not only a formatting one.
