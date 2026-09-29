# ATS Analysis — resumes/hunts/2026-09-04/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf vs jobgether-senior-fullstack-trading-api
Segment: agency   Date: 2026-09-04

## Verdict
BLOCKED at Gate 1

Gate 0 PASSES on all 8 checks. Gate 1 FAILS on the required-skill row: the
posting states `Golang`, `HTML`, and a modern CSS framework such as
`TailwindCSS`. None of the three is present verbatim in the raw extraction.
Gate 2 is 58/100 and FAILS on the same three required tokens.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | `pdftotext` returns 57 non-empty lines of clean text. No image XObjects: `pdfimages -list` returns an empty table. |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes. 0 characters in U+FB00-FB06. 0 replacement characters. Only two non-ASCII code points in the whole file: `ó` (U+00F3) and `•` (U+2022). Ligature probe: `back-office` extracts intact (1 hit for `office`), `workflows` extracts intact (3 hits). `\defaultfontfeatures{Ligatures=NoCommon}` is doing its job. |
| 0.3 | Contact block recoverable | PASS | Line 3 of the raw stream, in the body, not a header or footer: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc` |
| 0.4 | Section headers present verbatim | PASS | `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION` recover as standalone lines. Uppercase rendering is allowed by the rubric. |
| 0.5 | Employment-block segmentation | PASS | Four distinct blocks in the raw stream, none merged, none split. Each opens with a company line and carries four consecutive header lines before its first bullet: `DexCare / Senior Software Engineer / Remote / Mar 2026 - Present`, `Luizalabs / Mid-level Software Engineer / Remote / Jan 2024 - Mar 2026`, `Lippaus Distribuidora / Mid-level Software Engineer / Vitória, ES, Brazil / Jan 2023 - Jan 2024`, `Lippaus Distribuidora / Entry-level Fullstack Software Engineer / Vitória, ES, Brazil / Mar 2021 - Jan 2023`. The two Lippaus roles stay separate, which keeps the promotion visible. |
| 0.6 | Date parseability | PASS | Every role carries `Mon YYYY - Mon YYYY` inside its own header block, two lines below the title, with no bullet between. ASCII hyphen throughout; the non-ASCII scan proves no EN DASH survives anywhere in the document. |
| 0.7 | Reading order | PASS | Raw and `-layout` extraction agree on the order of every adjacent content block. Single column, full width. |
| 0.8 | No forbidden constructs | PASS | No `tabular`, no text box, no image, no icon, no photo. `pdfimages -list` is empty. Fonts are four embedded subsets with Identity-H and a `uni` map. |

## Gate 1 — Knockouts

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | posting | not stated. The posting says only "based in Brazil" and "Full-time". It names no visa, entity, or contract requirement. |
| Location or time-zone overlap | posting | PASS. Posting: "looking for a Senior Full-Stack Engineer - Trading API based in Brazil", workplace type Remote. Resume prints `Vitória, ES, Brazil` in the contact block. No UTC offset printed, per CLAUDE.md rule 3. |
| Minimum years of experience | posting | PASS. Posting: "5+ years of professional full-stack software development experience." Resume Summary: "with 5+ years". Dated history runs `Mar 2021` to `Present`, 5 yrs 6 mos, verified against LinkedIn. |
| English proficiency requirement | posting | not stated. The posting asks for "Excellent communication and collaboration skills" but names no language or level. |
| Each required skill | posting | **FAIL.** See the table below. |
| Degree requirement | posting | not stated. The posting names no degree. |

### Required-skill presence, verbatim in the raw extraction

| Required skill, in the posting's own words | Verbatim in resume? |
|---|---|
| `TypeScript` — "Proficiency in TypeScript and React" | YES |
| `React` — "Proficiency in TypeScript and React" | YES |
| `SQL` — "Solid experience with SQL and relational databases" | YES |
| `REST APIs` — "Strong understanding of REST APIs" | YES |
| `API design` — "API design best practices" | YES |
| `Golang` — "Strong professional experience with Golang and TypeScript/React" | **NO.** The resume spells it `Go`, 3 occurrences. The posting spells it `Golang`, 3 occurrences. 0 hits for `Golang` in the extraction. |
| `HTML` — "Strong knowledge of HTML and modern CSS frameworks" | **NO.** 0 hits. |
| `TailwindCSS` or a comparable modern CSS framework — "particularly TailwindCSS or comparable technologies" | **NO.** 0 hits for `TailwindCSS` and 0 for `Tailwind`. The resume carries bare `CSS`, which is the language, not a framework. |

Note on `Golang`. This is a spelling defect, not a missing fact. The capability
is evidenced: `Go` sits in `Skills` under `Languages` and inside the Luizalabs
bullet "building distributed tax microservices in Node.js and Go", and the live
LinkedIn profile tags `Go (Programming Language)` on the Luizalabs role.
ATS-KNOWLEDGE 4.2 is explicit that alias expansion must never be relied on, so
`Go` does not satisfy a `Golang` query.

Note on `HTML` and `TailwindCSS`. These are missing facts, not spelling
defects. `DOSSIER.md` records no HTML claim and no CSS framework of any kind.
The Maestro brief lists both under "Required tokens or facts not fully
established by DOSSIER.md". Neither may be added until Lucas confirms it.

## Gate 2 — Retrieval coverage: 58/100, FAIL

`Skills` = the `SKILLS` block. `Experience` = a bullet inside the `EXPERIENCE`
block. Placement scored on the raw extraction.

### Required tokens, weight 3

| Token | Posting wording | Placement | Points |
|---|---|---|---|
| `TypeScript` | "Proficiency in TypeScript and React" | Skills (`Languages: TypeScript`) + DexCare bullet 1 ("building TypeScript and React scheduling interfaces") | 3 |
| `React` | "Proficiency in TypeScript and React" | Skills (`Frontend: React`) + DexCare bullet 1 | 3 |
| `SQL` | "Solid experience with SQL and relational databases" | Skills (`SQL`) + DexCare bullet 4 ("consistent across SQL stores") | 3 |
| `REST APIs` | "Strong understanding of REST APIs" | Skills (`REST APIs`) + DexCare bullet 3 ("building multi-tenant REST APIs with Auth0 JWT") | 3 |
| `API design` | "API design best practices" | Skills (`API design`) + DexCare bullet 3 ("Improved API design, as measured by a 25% reduction") | 3 |
| `Golang` | "Strong professional experience with Golang"; also satisfies "at least one modern systems programming language such as Golang or C#" | **Absent.** Only `Go` appears. | **0** |
| `HTML` | "Strong knowledge of HTML" | **Absent.** | **0** |
| `TailwindCSS` or comparable CSS framework | "modern CSS frameworks, particularly TailwindCSS or comparable technologies" | **Absent.** Bare `CSS` is in Skills and in DexCare bullet 1, but no framework token. | **0** |

Required subtotal: 15 of 24 placement points, weighted 45 of 72.

### Preferred tokens, weight 1

| Token | Posting wording | Placement | Points |
|---|---|---|---|
| `PostgreSQL` | "preferably PostgreSQL" | Skills + DexCare bullet 4 + Lippaus bullet 1 | 3 |
| `Docker` | "Experience with Docker and Kubernetes is advantageous" | Skills + Luizalabs bullet 3 | 3 |
| `Kubernetes` | same | Skills + Luizalabs bullet 3 | 3 |
| remote working | "Experience working effectively in a fully remote environment is beneficial" | Skills (`remote work`) + DexCare bullet 6 ("Improved daily delivery quality in remote work") | 3 |
| `Google Cloud Platform` | "cloud platforms, preferably Google Cloud Platform" | **Absent as spelled.** The resume uses the abbreviation `GCP`, in Skills and in the Luizalabs bullet. The posting's own spelling never appears. | **0** |
| financial markets | "Knowledge of financial markets ... is a strong plus" | Absent. `financial` scores 0 hits. | 0 |
| fintech | "experience in fintech is a strong plus" | Absent. | 0 |
| algorithmic trading | "Experience with algorithmic trading ... is advantageous" | Absent. `trading` and `algorithmic` both score 0 hits. | 0 |
| startup environment | "Previous experience in a startup or rapidly growing technology environment is a plus" | Absent from the resume. | 0 |

Preferred subtotal: 12 of 27 placement points, weighted 12 of 27.

### Score

```
coverage = 100 * (45 + 12) / (72 + 27) = 100 * 57 / 99 = 57.6 -> 58
```

Stuffing penalty: 0. No token reaches 4 occurrences. The highest counts are
`Go`, `TypeScript`, `React`, `Node.js`, `PostgreSQL`, `testing` and
`multi-tenant` at 3 each, which is the CV-SPEC cap.

Required tokens without Skills and Experience placement: `Golang`, `HTML`,
`TailwindCSS` or a comparable modern CSS framework.

## Gate 3 — Human scan: 88/100

| # | Check | Result | Points |
|---|---|---|---|
| 3.1 | Target title in the top 15% | Partial. The posting's title is `Senior Full-Stack Engineer - Trading API`. The resume opens with `Senior Software Engineer` in Summary line 1 and `full-stack` in Summary line 2, both inside the top 15% of the document. The exact posting title is absent, and it must stay absent: CLAUDE.md rule 4 forbids changing a title to improve a match, and `Senior Software Engineer` is the LinkedIn title. Credit for the near title, deduction for the missing `Trading API` and `Full-Stack Engineer` retrieval strings. | 10 / 15 |
| 3.2 | The 3 most relevant bullets in the most recent role, in its first 3 lines | Partial. DexCare bullet 1 (TypeScript, React, CSS) and bullet 3 (API design, REST APIs) are on target. Bullet 2 is `Epic EMR time-slot flows with hospital records`, a healthcare-domain bullet with no purchase on a trading-API posting, and it occupies line 2. Bullet 4 (`SQL`, `PostgreSQL`) is more relevant to this posting and sits below the fold of the first three. | 13 / 20 |
| 3.3 | Past-tense action verb plus an outcome on every bullet | PASS. All 14 bullets open with `Delivered`, `Reduced`, `Improved`, `Kept`, `Supported`, `Increased`, or `Turned`. No present tense. No "Responsible for". No third person. Every bullet carries an outcome clause. | 15 / 15 |
| 3.4 | At least 3 bullets carry a real, defensible number | PASS, 5 bullets. 15% wrong bookings, 25% authentication friction, 7% release risk, 20% invoice throughput, 26% processing capacity. All five trace to the metrics Lucas supplied in `DOSSIER.md` (D2, D3, D5, L2, P2). No invented number. | 15 / 15 |
| 3.5 | One page under 10 years experience | PASS. `pdfinfo` reports `Pages: 1`, letter. | 10 / 10 |
| 3.6 | No unsupported buzzwords | PASS. No "team player", "results-driven", or "passionate". Every adjective is attached to a named technology or a number. | 10 / 10 |
| 3.7 | Skills grouped by category | PASS. Five labelled groups: `Languages`, `Frontend`, `Backend and data`, `Cloud and operations`, `Practices and AI tooling`. | 10 / 10 |
| 3.8 | Scannable | PASS. Consistent role header order across all four blocks: bold company, italic title, italic location, plain dates. Consistent bullet indent. Section rules separate the four sections. White space remains at the foot of the page, so the fixes below can land without a second page. | 5 / 5 |

## Defects, ranked by cost

1. **`Golang` never appears; the resume says `Go`** — Gate 1 required-skill FAIL, Gate 2 required-token FAIL, 9 weighted points.
   The posting spells it `Golang` three times and never writes `Go` alone.
   Fix, in two places, with no new fact:
   - `Skills`, change `\resumeItem{\textbf{Languages:} TypeScript \textbar{} JavaScript \textbar{} Node.js \textbar{} Go}` so the token `Golang` is present.
   - Luizalabs bullet 1, change `by building distributed tax microservices in Node.js and Go.` so the token `Golang` is present in the bullet.
   Keep the total occurrences of the Go/Golang family at or under 3, per the CV-SPEC cap.

2. **`HTML` absent** — Gate 1 required-skill FAIL, Gate 2 required-token FAIL, 9 weighted points.
   Posting: "Strong knowledge of HTML and modern CSS frameworks".
   `DOSSIER.md` records no HTML claim. **Do not add it as a fact.** Escalate to
   Lucas: does he claim HTML, and against which role? Once he confirms, it goes
   in `Skills` under `Frontend` and in one DexCare or Lippaus bullet. Until
   then this stays a gap and Gate 1 stays FAIL.

3. **No modern CSS framework token; `TailwindCSS` absent** — Gate 1 required-skill FAIL, Gate 2 required-token FAIL, 9 weighted points.
   Posting: "modern CSS frameworks, particularly TailwindCSS or comparable
   technologies". The resume's bare `CSS` in `Frontend: React \textbar{} CSS`
   and in DexCare bullet 1 does not answer this. `DOSSIER.md` records no CSS
   framework at all. **Do not invent one.** Escalate to Lucas: which CSS
   framework did he use, and where. This is an alternatives requirement, so any
   one confirmed framework closes it.

4. **`Google Cloud Platform` absent as spelled** — Gate 2 preferred token, 3 weighted points, non-blocking.
   The resume writes `GCP` in `Cloud and operations:` and in the Luizalabs
   bullet "running Docker and Kubernetes on GCP with CI/CD". The posting writes
   "preferably Google Cloud Platform". Fix: spell it out once and keep the
   abbreviation, for example `Google Cloud Platform (GCP)` in `Skills`. Costs
   no line.

5. **DexCare bullet order buries the most relevant evidence** — Gate 3.2, 7 points.
   `Reduced wrong bookings by 15% by integrating Epic EMR time-slot flows with
   hospital records.` is line 2 of the current role and carries no token this
   posting asks for. `Kept booking data consistent across SQL stores by
   modeling reads and writes in PostgreSQL with Sequelize and Drizzle ORM.`
   carries `SQL` and `PostgreSQL` and sits at line 4. Swap the two. No text
   changes, only order.

6. **No `startup` token, although the evidence exists and is candidate-authored** — Gate 2 preferred, 3 weighted points, non-blocking.
   The posting rewards "Previous experience in a startup or rapidly growing
   technology environment". Lucas's own live LinkedIn description of the
   Lippaus role reads "Fast-growing startup powering Heineken's beverage
   distribution network across Brazil", read from the profile on 2026-09-04.
   The Lippaus bullet "Supported nationwide retailer expansion by building a
   multi-tenant web and mobile platform on PostgreSQL." can carry the word
   without any new claim. `DOSSIER.md` does not record it, so confirm with
   Lucas before printing.

## Match limits

Four preferred requirements have no support anywhere in `DOSSIER.md`, in the
verified LinkedIn profile, or in the DexCare repo observations, and none of
them may be manufactured:

- Knowledge of financial markets.
- Experience in fintech.
- Experience with algorithmic trading, professional or personal.
- Golang **depth**, as distinct from the `Golang` spelling. The posting asks
  for "Strong professional experience with Golang". The evidenced use is one
  Luizalabs bullet. Fixing defect 1 fixes the token, not the depth. This is a
  real match limit and it survives every fix above.

The Luizalabs electronic-invoicing and SEFAZ domain is tax and e-commerce
compliance. It is not trading, not market data, and not fintech, and it must
not be presented as any of them.
