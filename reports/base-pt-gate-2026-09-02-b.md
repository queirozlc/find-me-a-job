# ATS Analysis — resumes/base-pt.pdf vs no-job (base-CV gate, hunt 2026-09-02-b)
Segment: n/a (base CV, no posting)   Date: 2026-09-02

Analyst: Sieve (ATS Analyzer). Scope set by Maestro: Gate 0 and Gate 3 only.
Gate 1 and Gate 2 are not run. There is no posting.

## Extraction (mandatory step)
Source file: `~/career/resumes/base-pt.pdf`, 28436 bytes, 1 page, letter,
producer `xdvipdfmx (0.1)`, no metadata stream, not tagged.

```
pdftotext -layout base-pt.pdf - > pt-layout.txt   # 55 lines
pdftotext          base-pt.pdf - > pt-raw.txt     # 78 lines
```
Gate 0 is judged on `pt-raw.txt`. Every quote below is verbatim from an
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
| 0.2 | Glyph integrity | PASS | Zero code points in U+FB00-U+FB06. Zero `\x00`. Zero U+FFFD. Positive proof of disabled ligatures: `backoffice` (ffi carrier) at raw lines 48 and 69, `workflows` (fl carrier) at raw lines 17 and 35. Portuguese diacritics survive intact: `Vitória` line 3, `EXPERIÊNCIA` line 19, `FORMAÇÃO` line 72, `serviços` line 7, `ciclomática` line 34, `notificações` line 60. Note: the EN canaries `profile`, `efficient` and `conflict` do not apply to a Portuguese document. |
| 0.3 | Contact block recoverable | PASS | Raw line 3: `Vitória, ES, Brasil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. In the body. Source uses `\pagestyle{empty}` and a `center` block; no `fancyhdr`, no header, no footer. |
| 0.4 | Section headers present verbatim (PT allowlist) | PASS | Standalone raw lines: 5 `RESUMO`, 11 `HABILIDADES`, 19 `EXPERIÊNCIA`, 72 `FORMAÇÃO`. All four match the `RUBRIC.md` Gate 0.4 PT allowlist. Uppercase rendering is allowed, case-insensitive. The circumflex and the cedilla-tilde both extract correctly, so the header strings are not corrupted. |
| 0.5 | Employment-block segmentation | **FAIL, non-blocking** | Each role splits into two raw blocks. Example, raw lines 20-24: `DexCare` / `Senior Software Engineer` / (blank) / `Jan 2026 - Present` / `Remoto`. Cause is only the two-column `tabular*` in `\resumeSubheading`. **No two roles are merged.** Four company lines, four titles, correctly paired and in the right order: DexCare, Luizalabs, Lippaus Distribuidora, Lippaus Distribuidora. Accepted exception, `RUBRIC.md` and `CV-SPEC.md` item 2. |
| 0.6 | Date parseability | **FAIL, non-blocking** | The date is not on the same line as its title and is not adjacent to it. It sits two lines below, across a blank line. Raw lines 21-23: `Senior Software Engineer` / (blank) / `Jan 2026 - Present`. Same `tabular*` cause. The date strings themselves are all well formed and ASCII-hyphen: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Zero EN DASH or other non-ASCII dash anywhere in the file. |
| 0.7 | Reading order | **FAIL, non-blocking** | Raw order is Company, Title, Dates, Location. Layout order is Company, Dates, Title, Location. Layout line 20: `DexCare ... Jan 2026 - Present`; layout line 21: `Senior Software Engineer ... Remoto`. The two adjacent blocks `Senior Software Engineer` and `Jan 2026 - Present` are ordered differently in the two streams. Same `tabular*` cause. |
| 0.8 | No forbidden constructs | **FAIL, non-blocking** | One construct: the `tabular*` role header. Nothing else. `pdfimages -list base-pt.pdf` returns zero images, so there is no photo, no icon, and no image of text. No text box. |

## Gate 1 — Knockouts
Not run. There is no posting in this gate. Running it would require guessing
requirements, which is prohibited.

## Gate 2 — Retrieval coverage
Not run. Retrieval coverage is defined against a posting's token set. There is
no posting. No number is emitted.

## Gate 3 — Human scan: 99/100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15/15 | `Senior Software Engineer` at raw line 6 of 78, which is 7.7% into the document. It repeats in the DexCare role header at raw line 21. The title stays in English, which is correct: `CLAUDE.md` rule 1 and `CV-SPEC.md` require the LinkedIn string verbatim, never translated. It is also the retrieval token a recruiter searches. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20/20 | DexCare bullets 1-3 are the strongest and lead the role: event-driven TypeScript on Express and Koa; EMR Epic sync with 15%; multi-tenant REST APIs with Auth0 JWT and OpenAPI/Swagger with 25%. Two of the three carry a number. Structure is identical to the EN pair. |
| 3.3 | Bullet voice and Summary voice | 15/15 | All 16 Experience bullets lead with a first-person past-tense verb (pretérito perfeito), subject omitted. Zero start with `Eu`. Zero present tense. Zero `Responsável por`. Zero third person. Summary opens `Eu sou Senior Software Engineer`. Full list under **Voice check** below. |
| 3.4 | At least 3 bullets carry a real number | 15/15 | Seven bullets carry a number: 15%, 25%, 7%, 33%, 20%, 18%, 26%. Every one traces to `DOSSIER.md` bullet metrics (D2, D3, D5, D7, L2, L3, P2). Same seven values as the EN pair. |
| 3.5 | Length: 1 page under 10 years | 10/10 | `pdfinfo` reports `Pages: 1`. |
| 3.6 | No unsupported buzzwords | 10/10 | Zero hits for `proativo`, `apaixonado`, `dinâmico`, `comunicativo`, and for the EN list `team player`, `results-driven`, `passionate`, `hands-on`. One unsupported qualifier exists (`expansão nacional`) but it is a claim, not a buzzword this check names. It is reported under **Claims I could not verify**. |
| 3.7 | Skills grouped by category | 10/10 | Six labelled groups at raw lines 12-17: Linguagens, Backend, Dados, Frontend, Cloud e operação, Testes e ferramentas de IA. |
| 3.8 | Scannable | 4/5 | Consistent 5pt inter-role gap, bold company, italic title, one column, full width. **Minus 1: verb monotony.** `Construí` opens 7 of the 16 bullets (raw lines 26, 29, 34, 45, 48, 59, 70). A recruiter scanning the left edge sees the same word repeatedly, which lowers the information value of the scan anchor. |

**Gate 3 total: 99/100.**

## Voice check (explicit, per CLAUDE.md section 9 and CV-SPEC.md)

Leading token of every Experience bullet, read from `pt-raw.txt`:

| Raw line | Leading verb | Verdict |
|---|---|---|
| 26 | Construí | 1st person past, subject omitted, OK |
| 28 | Integrei | OK |
| 29 | Construí | OK |
| 31 | Modelei | OK |
| 33 | Reduzi | OK |
| 34 | Construí | OK |
| 36 | Ajudei | OK |
| 45 | Construí | OK |
| 47 | Migrei | OK |
| 48 | Construí | OK |
| 50 | Implantei | OK |
| 59 | Construí | OK |
| 60 | Processei | OK |
| 61 | Liderei | OK |
| 69 | Desenvolvi | OK |
| 70 | Construí | OK |

- Bullets that break the rule: **none**. 16 of 16 pass.
- Bullets starting with `Eu`: **none** (`grep -E '^• *Eu '` returns zero).
- Present-tense bullets: **none**.
- `Responsável por` bullets: **none** (`grep -i 'respons[áa]vel por'` returns zero).
- Third-person bullets: **none**.
- Summary uses `Eu`: **yes**. Raw line 6, `Eu sou Senior Software Engineer...`,
  then `Eu construo`, `eu construí`, `Eu integro`. The present-tense verbs in
  the Summary are correct: `CV-SPEC.md` sets present tense for what Lucas does
  today and past tense for what he did.

## Titles and dates against DOSSIER.md LinkedIn ground truth

| CV, raw extraction | DOSSIER LinkedIn ground truth | Match |
|---|---|---|
| `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` | `Senior Software Engineer`, `DexCare`, `Jan 2026 - Present` | exact |
| `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` | `Mid-level Software Engineer`, `Luizalabs`, `Jan 2024 - Jan 2026` | exact |
| `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | `Mid-level Software Engineer`, `Jan 2023 - Jan 2024` | exact |
| `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | `Entry-level Fullstack Software Engineer`, `Mar 2021 - Jan 2023` | exact |
| `FAESA` / `Bacharelado em Sistemas de Informação` / `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | dates exact after the CV-SPEC ASCII-hyphen rule; the degree name is translated, see note below |

Job titles stay in English and unmodified. That is correct and required.
`CLAUDE.md` rule 1 and the `DOSSIER.md` LinkedIn ground truth both say the
strings are not normalized, translated, or tidied.

**Note on the degree string.** The PT file translates the degree to
`Bacharelado em Sistemas de Informação`. Rule 1 binds "every job title and
every date". A degree name is neither. `DOSSIER.md` confirms the degree as
**Information Systems, FAESA [FACT]**, and the translation is faithful. I
record this as an observation, not a defect.

**Note on `Present` and the month abbreviations.** The PT file prints
`Jan 2026 - Present`, and `Feb`, `Mar`, `Dec`. These are English strings in a
Portuguese document. `CLAUDE.md` rule 1 requires the LinkedIn date verbatim
and outranks language consistency, so the file as built is compliant. I report
the tension so Lucas can decide, and I do not deduct a point for it.

## Stack positioning checks

| Check | Result |
|---|---|
| Ruby or Rails token anywhere (`.tex` and raw, word boundary: ruby, rails, rspec, sidekiq, activerecord, activejob, hotwire, devise, pundit, erb, gem) | **zero hits** |
| `[UNVERIFIED]` marker in `.tex` or raw | **zero hits** |
| UTC offset or `GMT` printed | **zero hits** |
| Term appearance cap of 3 (`CV-SPEC.md`) | **not exceeded.** Maximum is 3: TypeScript 3, Node.js 3, React 3, Go 3, PostgreSQL 3, AWS 3, BullMQ 3. All others are 1 or 2. Counts are identical to the EN pair. |
| Every load-bearing technology in Skills and in an Experience bullet | holds for the same set as the EN pair. **RabbitMQ and AMQP appear in Skills only** (1 appearance each, raw line 13). Lucas approved them as Skills-only tokens on 2026-09-01, so this is recorded, not a defect. |

## Defects, ranked by cost

1. **Lippaus role location prints an employer city, against a DOSSIER FACT** —
   Gate 3 / `DOSSIER.md` line 166. Raw lines 57 and 67 print
   `Vitória, ES, Brasil` as the location of both Lippaus roles. DOSSIER states:
   "**Role locations print `Remote` only.** ... No employer city on the CV.
   [FACT, Lucas 2026-09-01]". LinkedIn separately records Lippaus as
   `On-site`. The rule and the LinkedIn record conflict for this employer.
   **This is Lucas's decision, not the Architect's.** I do not know which he
   intends. Fix once decided: either replace both with `Remoto`, or Lucas
   amends the DOSSIER rule to exempt the on-site Lippaus period.
   Present in both language files.
2. **The pair has diverged in the Summary** — `CV-SPEC.md` Languages: "The
   bases ship as a pair ... Same facts, same structure, same dates." The PT
   Summary carries two statements the EN Summary does not:
   `sistemas backend e fullstack` (raw line 6) and
   `para uma empresa dos EUA` (raw line 7). The EN Summary has no equivalent
   of either. Same dates, same structure, but not the same facts. Fix: add the
   matching clauses to `base-en.tex`, or remove them from `base-pt.tex`.
   Lucas chooses which direction. I note that
   `para uma empresa dos EUA` is a useful signal for a Brazilian reader and
   the EN file may want the equivalent.
3. **Unverifiable qualifier in one bullet** — Gate 3 / truth handling.
   `expansão nacional de varejistas` (raw line 59) is not in `DOSSIER.md`.
   See **Claims I could not verify**. Fix: confirm with Lucas, or mark
   `[UNVERIFIED]`, or drop the qualifier and keep the verified core.
4. **Verb monotony** — Gate 3.8, minus 1 point. `Construí` opens 7 of 16
   bullets. Fix: vary the lead verb on three of them without changing the
   claim. For example raw line 45 `• Construí microsserviços fiscais
   distribuídos em Node.js, Java e Go...` could lead with `Entreguei` or
   `Desenvolvi`.
5. **`tabular*` role header, four Gate 0 findings** — Gate 0.5, 0.6, 0.7, 0.8.
   Reported, not blocking, by Lucas's 2026-09-01 decision. No action. The
   single-column shape A fallback in `reports/macro-bakeoff.md` stays available
   if a specific posting is known to route through a strict parser.
6. **`Present` and English month abbreviations in a Portuguese document** —
   observation only, no point deducted. Rule 1 requires the LinkedIn string
   verbatim and outranks language consistency. Raised so Lucas can rule on it.

## Claims I could not verify

Traced against `DOSSIER.md`. I do not delete these and I do not defend them.
Lucas decides.

1. `mais de 5 anos` (Summary, raw line 6). Not stated in `DOSSIER.md`. It is
   arithmetically consistent with the LinkedIn ground truth: `Mar 2021` to
   today, 2026-09-02, is 5 years 6 months. Consistent, but not a recorded fact.
2. `expansão nacional de varejistas` (Lippaus Mid-level, raw line 59). DOSSIER
   confirms "multi-tenant web and mobile platform on PostgreSQL". It records
   nothing about nationwide scope.
3. `startup de distribuição de bebidas` (Lippaus Entry-level, raw line 69).
   Not in `DOSSIER.md` in any form. `bebida` returns zero hits.
4. `para uma empresa dos EUA` (Summary, raw line 7). The country is supported:
   the LinkedIn ground truth records DexCare as
   `Seattle, Washington, United States`. The phrase itself is a PT-only
   addition with no EN counterpart, so it is listed here as well as in defect 2.
5. `os microsserviços fiscais da emissão de notas eletrônicas no Magazine
   Luiza` (Summary, raw lines 8-9) and `a emissão de notas fiscais eletrônicas
   do e-commerce do Magazine Luiza` (Luizalabs, raw lines 45-46). DOSSIER
   confirms the fiscal / NF-e / SEFAZ domain as [FACT]. It does not carry the
   word `e-commerce`. `CV-SPEC.md` mentions "a Brazilian e-commerce retailer"
   only when retiring an older claim. Magazine Luiza being an e-commerce
   retailer is common knowledge, but it is not observable from this dossier,
   so I record it rather than assert it.
6. The PT file has no equivalent of the EN `high-volume orders` qualifier. Raw
   line 60 reads `Processei pedidos, notificações e integrações com 26% mais
   capacidade`, with no volume claim. The PT wording is the more defensible of
   the two.
7. Lippaus location, item 1 of the defect list. Recorded here as well because
   it is a factual conflict, not only a formatting one.
