# ATS Analysis — jobgether-backend-core-apis-en.pdf / -pt.pdf vs jobgether-backend-core-apis
Segment: agency   Date: 2026-09-01

Posting: Backend Engineer, Core APIs — Jobgether (on behalf of a partner).
https://www.linkedin.com/jobs/view/4460256096/
Captured verbatim in `jobs/jobgether-backend-core-apis.md`. Every requirement
below is quoted from that file. Nothing is inferred.

## Verdict

| Gate | EN | PT |
|---|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, accepted exception) | **PASS** (same) |
| Gate 1 — Knockouts | **PASS** — no FAIL | **PASS** — no FAIL |
| Gate 2 — Retrieval coverage | **9 / 100** | **5 / 100** |
| Gate 3 — Human scan | **90 / 100** | **90 / 100** |

Not blocked. Both documents parse, both are one page, both match LinkedIn
character for character. The problem is Gate 2, and the penalty term is doing
most of the damage. Read the Gate 2 section before reacting to the number.

---

## Gate 0 — Parse integrity

Both PDFs confirmed **1 page** (`pdfinfo`). `pdfimages -list` returns zero
images in both. Zero NUL bytes and zero U+FFFD in either raw extraction.

| # | Check | EN | PT | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | PASS | Raw extraction is complete prose, 74 lines EN / 75 PT |
| 0.2 | Glyph integrity | PASS | PASS | `grep -oic workflow` EN = 4, PT = 3. `office` EN = 2, PT = 2 (`back-office` / `backoffice`). Zero `U+FB00-FB06`, zero `\x00` in either raw file. `\defaultfontfeatures{Ligatures=NoCommon}` at `en.tex:16` / `pt.tex:16` |
| 0.3 | Contact block recoverable | PASS | PASS | Line 3 of raw, in the body, not a header: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email, LinkedIn all present. No UTC offset printed |
| 0.4 | Section headers verbatim | PASS | PASS | EN raw: `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`. PT raw: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`. Uppercase rendering allowed by Gate 0.4 |
| 0.5 | Employment-block segmentation | FAIL — header only | FAIL — header only | Raw splits each role header into 4 lines: `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` / `Remote`. **No two roles merge. No role splits into two employment entries.** Cause is the `tabular*` at `en.tex:41` / `pt.tex:41` |
| 0.6 | Date parseability | FAIL — header only | FAIL — header only | Dates sit one line below the title in the raw stream, not on it. Format `Mon YYYY - Mon YYYY` with ASCII hyphen is correct in all five blocks |
| 0.7 | Reading order | FAIL — header only | FAIL — header only | `diff` of normalized raw vs layout returns **5 hunks in each language, all five are the role or education header**. Zero content blocks reorder |
| 0.8 | No forbidden constructs | FAIL — header only | FAIL — header only | `tabular*` role header. No table elsewhere, no text box, no image of text, no icon, no photo. `pdfimages -list` returns zero rows |

**All four FAILs trace only to the two-column role header.** That is the
accepted exception recorded in `CV-SPEC.md` item 2 and in `RUBRIC.md`
"Accepted exception, set by Lucas 2026-09-01". Reported, not blocking.
No other cause of 0.5-0.8 exists in either document.

### LinkedIn ground-truth cross-check — PASS

Every company, title and date, character for character against the
`DOSSIER.md` **LinkedIn ground truth** block.

| Block | Resume text (EN and PT identical) | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` | identical | YES |
| 3 | `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | identical | YES |
| 4 | `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | identical | YES |
| Education | `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — periods identical; ASCII hyphen per CV-SPEC item 5 |

Both Lippaus roles are present and separate. The promotion is preserved.
**No Gate 0 FAIL from the ground-truth check.**

Two observations outside the title/company/date scope, neither a FAIL:

- The PT file keeps the English date word `Present` (`pt.tex:77`). That is
  correct under CLAUDE.md rule 1: dates must be identical to LinkedIn.
- The PT file translates the degree to `Bacharelado em Sistemas de Informação`
  (`pt.tex:122`). The titles rule binds job titles. The PT translation policy
  covers this. Not a defect.
- Both Lippaus roles print `Remote`. LinkedIn records Lippaus as `On-site`.
  See fix 18; it is Lucas's to resolve, not the Architect's.

### Forbidden-token grep

```
grep -rniE 'ruby|rails|unverified' jobgether-backend-core-apis-en.tex jobgether-backend-core-apis-pt.tex
```
**Zero hits in either `.tex`** (grep exit status 1). Zero hits across all four
extraction files. No `[UNVERIFIED]` marker ships in this package.

### Page count

`pdfinfo` reports `Pages: 1` for `jobgether-backend-core-apis-en.pdf` and
`Pages: 1` for `jobgether-backend-core-apis-pt.pdf`. **Confirmed, one page each.**

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source (verbatim) | Result |
|---|---|---|
| Work authorization / entity type | "Candidates must be authorized to work from their home location; visa sponsorship is not provided." Location label: "Brazil (Remote)" | **PASS** — resume states `Vitória, ES, Brazil` as the home location. Note: the resume nowhere states work authorization in words; it is carried by the location line alone |
| Location | "Our partner is looking for a Backend Engineer, Core APIs based in Brazil." | **PASS** — `Vitória, ES, Brazil` |
| Time-zone overlap | Not stated. The posting says "globally distributed", "highly asynchronous environment". The capture file records "no overlap window stated" | **not stated** — resume states `US-hours overlap` anyway. See fix 16 |
| Minimum years of experience | "2+ years of professional backend software development experience" | **PASS** — Mar 2021 to Sep 2026 = 5 yr 6 mo from the LinkedIn dates. Summary states `5+ years` |
| English proficiency | "Strong communication skills in English, with the ability to collaborate effectively across a globally distributed and asynchronous team." | **PASS** — EN Summary states `Advanced/C1 English`; PT Summary states `inglês Advanced/C1`. Backed by `DOSSIER.md` [FACT] |
| Degree requirement | Not stated in the posting | **not stated** |

Required-skill presence, verbatim in the raw extraction (EN):

| Required skill (posting's words) | Present verbatim? |
|---|---|
| `Go and/or Node.js` | **YES, both.** `Go` 2 occurrences, `Node.js` 3 |
| `scalable backend systems` | **YES**, Summary, verbatim phrase |
| `APIs`, `microservices` | **YES**, both |
| `real-time data-processing services` | **PARTIAL.** `real-time` YES. `data processing` **absent** |
| `SQL` | **YES**, 3 occurrences |
| `DynamoDB, Redis, or Elasticsearch` | **YES.** DynamoDB and Redis present; Elasticsearch absent. The OR is satisfied |
| `Git` | **NO.** The only `git` string is inside `github.com/queirozlc` |
| `IDEs` | **NO** |
| `shell scripting` | **NO** |
| `CI/CD workflows` | **YES**, 2 occurrences |
| `performance tuning`, `debugging` | **NO**, neither |
| `testing`, `reliability improvements` | `testing` via `Testing and AI tooling`, `Vitest`, `Jest`. `reliability` only as the stem `reliable` |

**Gate 1 verdict: PASS. No knockout FAIL in either language.**

---

## Gate 2 — Retrieval coverage: EN 9 / 100, PT 5 / 100

### Conventions used, stated so this is reproducible

1. `required` = the posting's **Requirements** section. `preferred` = every
   item the posting marks "is a plus", "is beneficial", "is preferred", "is an
   advantage", or "highly valued".
2. Soft skills are discarded per RUBRIC Gate 2 Step 1. Discarded here:
   independent investigation, root-cause analysis, hypothesis development,
   experimentation, constructive collaboration, distributed-team working style.
3. `Elasticsearch` is **not scored**. The posting writes "data stores such as
   DynamoDB, Redis, or Elasticsearch"; DynamoDB and Redis satisfy that OR.
   Scoring the unfulfilled alternative would penalize a met requirement.
4. `on-call rotation`, `mentoring` and `cross-functional` appear in
   **Accountabilities**, not in **Requirements**. The Maestro brief classifies
   them as required. I score them at Gate 3, not Gate 2, and list them below as
   uncovered. Both readings are visible; Lucas can pick.
5. Tier convention for placements the rubric table does not name: a token in an
   Experience bullet in context but absent from Skills scores 3; a token in the
   Summary only scores 4. Both are stated per row.

### Scale of the number

The rubric's formula uses an **unweighted numerator over a weighted
denominator**. With 21 required and 17 preferred tokens, a document that
scored the maximum 4 on every token would compute
`100 * (84 + 68) / (252 + 68) = 47.5`, not 100. **47.5 is the ceiling of this
gate for this posting**, before penalties. Read 9/100 against 47.5, not
against 100. This is a rubric arithmetic defect, not a document defect. I
apply the formula as written for consistency with
`reports/charterup-senior-fullstack-gate0.md`, and I flag it here rather than
change it unilaterally.

### English — required tokens (weight 3)

| # | Token | Placement | Points |
|---|---|---|---|
| 1 | `Go` | Skills `Languages`, Experience Luizalabs b1. **Not in Summary** | 3 |
| 2 | `Node.js` | Skills, Experience DexCare b1, Summary | 4 |
| 3 | `backend` | Skills group label, Experience DexCare b1, Summary `scalable backend systems` | 4 |
| 4 | `APIs` | Skills, Experience DexCare b1 and b2, Summary | 4 |
| 5 | `microservices` | Skills `Microservices`, Experience Luizalabs b1, Summary | 4 |
| 6 | `real-time` | Experience DexCare b1, Summary. Not in Skills | 4 |
| 7 | `data processing` | **Absent.** Nearest: `processing capacity` (Lippaus b1), `event-driven` | 0 |
| 8 | `SQL` | Skills, Experience DexCare b3, Summary | 4 |
| 9 | `DynamoDB` | Skills, Experience DexCare b3 (`DynamoDB Streams`), Summary | 4 |
| 10 | `Redis` | Skills, Experience DexCare b3, Summary | 4 |
| 11 | `Git` | **Absent.** Only inside `github.com/queirozlc` | 0 |
| 12 | `IDEs` | **Absent** | 0 |
| 13 | `shell scripting` | **Absent** | 0 |
| 14 | `CI/CD` | Skills, Experience Luizalabs b3 | 3 |
| 15 | `English` proficiency | Summary `Advanced/C1 English` | 4 |
| 16 | `2+ years` backend | Summary `5+ years` | 4 |
| 17 | `performance tuning` | **Absent** | 0 |
| 18 | `debugging` | **Absent** | 0 |
| 19 | `testing` | Skills `Testing and AI tooling`, `Vitest`, `Jest`; Experience DexCare b6 `tests`, Luizalabs b3 | 3 |
| 20 | `reliability` | Experience Luizalabs b3, stem `reliable`. Not in Skills, not in Summary | 3 |
| 21 | `production-grade` | Experience Luizalabs b3, stem `production`. Full token absent | 3 |

Required subtotal: **55**. Required denominator: `4 * 3 * 21 = 252`.

### English — preferred tokens (weight 1)

| # | Token | Placement | Points |
|---|---|---|---|
| 1 | `Terraform` | **Absent** | 0 |
| 2 | `AWS CloudFormation` | **Absent** | 0 |
| 3 | `TypeScript` | Skills, Experience DexCare b1, Summary | 4 |
| 4 | `Express` | Skills, Experience DexCare b1 | 3 |
| 5 | `ClickHouse` | **Absent** | 0 |
| 6 | `dbt` | **Absent** | 0 |
| 7 | `Snowflake` | **Absent** | 0 |
| 8 | `BigQuery` | **Absent** | 0 |
| 9 | `Redshift` | **Absent** | 0 |
| 10 | `Databricks` | **Absent** | 0 |
| 11 | `Datadog` | Skills, Experience DexCare b4 | 3 |
| 12 | `logging` | Experience DexCare b4 `browser logging`. Not in Skills | 3 |
| 13 | `telemetry` | **Absent** | 0 |
| 14 | `Docker` | Skills, Experience Luizalabs b3 | 3 |
| 15 | `Kubernetes` | Skills, Experience Luizalabs b3 | 3 |
| 16 | both `Go` and `Node.js` in a backend context | Both present, but in **different roles**: Node.js at DexCare, Go at Luizalabs beside Java | 3 |
| 17 | `security` / `privacy` mechanisms | Neither word appears. Synonyms only: `Auth0 JWT`, `isolate tenants`, `secrets` | 1 |

Preferred subtotal: **23**. Preferred denominator: `4 * 1 * 17 = 68`.

```
coverage_en = 100 * (55 + 23) / (252 + 68) = 100 * 78 / 320 = 24.375 -> 24
```

### Stuffing penalty — English

| Trigger | Token | Penalty |
|---|---|---|
| Appears 4 or more times | `APIs` — 4 occurrences: Summary `core APIs`, Skills `Core APIs`, DexCare b1 `Core APIs`, DexCare b2 `multi-tenant APIs`. Also breaches CV-SPEC "cap any term at 3 appearances" | -5 |
| In Skills, no supporting evidence anywhere in Experience | `RabbitMQ` (`en.tex:67`) | -5 |
| In Skills, no supporting evidence anywhere in Experience | `AMQP` (`en.tex:67`) | -5 |

I checked all 33 Skills tokens against the Experience section. Only `RabbitMQ`
and `AMQP` lack support. Every other Skills token appears in at least one
bullet. No other token reaches 4 occurrences: `Core APIs` 3, `TypeScript` 3,
`Node.js` 3, `SQL` 3, `Redis` 3, `DynamoDB` 3, `PostgreSQL` 3, `React` 3,
`BullMQ` 3, `backend` 3, `microservices` 3, `Go` 2, `real-time` 2.

```
Gate 2 EN = 24 - 15 = 9 / 100
```

**The RabbitMQ / AMQP penalty is Lucas's instruction colliding with the
rubric.** `DOSSIER.md` records: "DexCare messaging: RabbitMQ / AMQP used on
services. **Skills token only**, no service names on the CV. [FACT, Lucas
2026-09-01]". The Architect must not silently remove them. See fix 3.

### Portuguese — 5 / 100

Same token list, same posting, scored on `jobgether-backend-core-apis-pt.raw.txt`.
The posting is written in English, so the English token is what retrieval
matches. Seven rows differ:

| Token | EN | PT | Cause |
|---|---|---|---|
| `real-time` | 4 | **0** | PT writes `em tempo real`. `real-time` occurs 0 times |
| `microservices` | 4 | **3** | Skills keeps `Microservices` verbatim; Summary and Experience use `microsserviços`. Verbatim count drops 3 to 1 |
| `testing` | 3 | **1** | PT writes `Testes`, `testes`. `Vitest` and `Jest` carry the Skills placement alone |
| `reliability` | 3 | **0** | PT writes `confiáveis` |
| `production-grade` | 3 | **0** | PT writes `produção` |
| `English` | 4 | **3** | PT writes `inglês Advanced/C1`. The token `English` is absent; `Advanced/C1` carries it |
| `2+ years` | 4 | **3** | PT writes `mais de 5 anos`. `5+ years` absent |

Preferred subtotal is unchanged at 23; every preferred token that scored is an
untranslated proper name.

```
coverage_pt = 100 * (40 + 23) / 320 = 100 * 63 / 320 = 19.7 -> 20
Gate 2 PT  = 20 - 15 = 5 / 100
```

Same three penalties. `APIs` also reaches 4 occurrences in PT.

### Required tokens not covered

Absent from both documents:

1. `data processing` — required. `real-time data-processing services` is a
   named requirement; only `real-time` lands.
2. `Git` — required. Present only as a substring of `github.com`.
3. `IDEs` — required.
4. `shell scripting` — required.
5. `performance tuning` — required.
6. `debugging` — required.

Present only as a stem or synonym, not verbatim:

7. `reliability` — only `reliable` (EN); nothing in PT.
8. `production-grade` — only `production` (EN); nothing in PT.

Preferred tokens not covered:

9. `Terraform`, `AWS CloudFormation`, `ClickHouse`, `dbt`, `Snowflake`,
   `BigQuery`, `Redshift`, `Databricks`, `telemetry` — none appears in
   `DOSSIER.md`. The Maestro brief already names most as gaps.
10. `security`, `privacy` — neither word appears, though Auth0 JWT and tenant
    isolation are recorded facts.

Accountability tokens not covered, not scored at Gate 2 (see convention 4):

11. `on-call` — absent from both documents. No on-call evidence in `DOSSIER.md`.
12. `mentor` / `mentoring` — absent from both. No mentoring evidence.
13. `cross-functional` — absent from both.

Requirement satisfied by an alternative, no action needed:

14. `Elasticsearch` — absent, but the posting's OR is met by DynamoDB and Redis.

---

## Gate 3 — Human scan: 90 / 100 (EN and PT)

| # | Check | Points | Basis |
|---|---|---|---|
| 3.1 | Target title in the top 15% | **12** / 15 | `Core APIs` lands in the Summary, line 6 of a 74-line one-page document, well inside the top 15%. Docked 3: the posting's title noun `Backend Engineer` never appears as a phrase, and the Summary writes `core APIs` in lower case while the posting and the Skills line write `Core APIs` |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | **16** / 20 | DexCare b1 (Core APIs, TypeScript, Node.js, Express, Koa), b2 (Auth0 JWT, OpenAPI, multi-tenant), b3 (SQL, PostgreSQL, DynamoDB, Redis, AWS) are exactly the three the posting weights highest, and they are first. Docked 4: **no bullet anywhere carries mentoring, on-call, or cross-functional signal**, and all three are named Accountabilities. `Go` is also absent from the current role |
| 3.3 | Every bullet leads with an outcome or action verb | **15** / 15 | All 16 bullets lead with a bare verb: Deliver, Reduce, Serve, Enable, Delivered, Improved, Kept, Cut, Increased, Supported, Turned. Zero "Responsible for". Present tense for the current role, past for prior roles |
| 3.4 | At least 3 bullets carry a real number | **15** / 15 | Seven do: 25%, 7%, 15%, 33%, 20%, 18%, 26%. All trace to the `DOSSIER.md` metric list, IDs D2, D3, D5, D7, L2, L3, P2 |
| 3.5 | Length: 1 page under 10 years | **10** / 10 | `pdfinfo` confirms `Pages: 1` for both |
| 3.6 | No unsupported buzzwords | **10** / 10 | No "team player", "results-driven", "passionate". Nothing comparable found |
| 3.7 | Skills grouped by category | **8** / 10 | Six labeled groups, ordered Languages, Backend, Data, Frontend, Cloud, Testing/AI. Good order for this posting. Docked 2: `Frontend: React` is a one-item group, and `Testing and AI tooling` fuses two unrelated concepts under one label |
| 3.8 | Scannable | **4** / 5 | Clean one-page render, ruled headers, bold companies, adequate role spacing per CV-SPEC item 2. Docked 1: wrapped bullets have no hanging indent, so continuation lines start flush under the bullet glyph. Five bullets wrap in EN, six in PT |

PT scores identically. Same structure, same defects, one extra wrapped bullet.

Not scored by the rubric but worth stating: **four of seven DexCare bullets
open with "Reduce"** (b2, b4, b5, b7). The repetition is visible on a fast scan.

---

## Defects, ranked by cost — fix list for the Resume Architect

19 items. Items 15 to 19 are Lucas's decisions, not the Architect's.

| # | File and line | Defect | What would pass |
|---|---|---|---|
| 1 | `en.tex:67`, `pt.tex:67` | `APIs` reaches 4 occurrences. Breaches CV-SPEC "cap any term at 3 appearances" and costs -5 at Gate 2. The fourth is `multi-tenant APIs` at `en.tex:81` / `pt.tex:81` | Change `multi-tenant APIs` to `multi-tenant services` at `en.tex:81` and `pt.tex:81`. `Core APIs` stays at 3 occurrences and the penalty clears |
| 2 | `en.tex:70`, `pt.tex:70` | Required token `Git` absent. The only `git` string is inside the GitHub URL. This is a Requirements-section item, weight 3, currently scoring 0 | Add `Git` to the `Cloud and operations` group, next to `CI/CD`. It is a defensible everyday tool, and one Experience bullet already implies it. Confirm with Lucas that he wants it named |
| 3 | `en.tex:67`, `pt.tex:67` | `RabbitMQ` and `AMQP` sit in Skills with zero Experience support. -10 at Gate 2, the largest single penalty | **Do not remove them.** `DOSSIER.md` records them as Skills-token-only by Lucas's own instruction. Either get Lucas to approve one supporting DexCare bullet naming RabbitMQ, or accept the -10 and note it in the application package. Escalate |
| 4 | `en.tex:80`, `pt.tex:80` | Required phrase `data processing` absent. The posting names "real-time data-processing services" twice | `DOSSIER.md` records DynamoDB Streams and event-driven booking as FACT-OBSERVED. Rewrite DexCare b1 to name real-time data processing over those streams, for example "...event-driven TypeScript and Node.js services that process real-time booking data through DynamoDB Streams...". No new claim is introduced |
| 5 | `en.tex:62`, `pt.tex:62` | `Go` never reaches the Summary. The posting weights Go equally with Node.js and calls experience in both "highly valued". Go scores 3 instead of 4, and the preferred "both Go and Node.js" row scores 3 | Name `Go` in the Summary beside TypeScript and Node.js, scoped as recorded usage, not as primary depth. `DOSSIER.md` confirms Go at Luizalabs [FACT] and records no depth |
| 6 | `en.tex:80-86`, `pt.tex:80-86` | `Go` appears in no DexCare bullet. A backend-Go requisition scans the current role first and finds none | **Do not invent one.** `DOSSIER.md` records no Go at DexCare. Ask Lucas whether he uses Go at DexCare. If not, fix 5 is the only available move |
| 7 | `en.tex:70`, `pt.tex:70` | Required tokens `performance tuning` and `debugging` absent. The posting requires "Conduct performance tuning, debugging, testing, and reliability improvements" | No `DOSSIER.md` evidence exists for either. Escalate to Lucas before any bullet is written. Do not add the words to Skills without an Experience bullet behind them; that trades a 0 for a -5 stuffing penalty |
| 8 | `en.tex:70`, `pt.tex:70` | Required token `shell scripting` absent | Add `Shell scripting` only if Lucas confirms it, and only with a supporting bullet. Same stuffing trap as fix 7 |
| 9 | `en.tex:95`, `pt.tex:95` | `reliability` and `production-grade` appear only as the stems `reliable` and `production`. Both are Requirements-section language | Rewrite Luizalabs b3 to carry `reliability` and `production-grade` as words, for example "Improved production-grade service reliability by deploying Docker and Kubernetes on GCP through ArgoCD". Same facts, exact tokens |
| 10 | `en.tex:67` and `:70`, `pt.tex` same | Preferred item "Internet security and privacy mechanisms" scores 1. Neither `security` nor `privacy` appears, though Auth0 JWT, multi-tenant JWT, tenant isolation and secrets are all recorded facts | Rename the `Backend` or `Cloud and operations` group to carry `Multi-tenant security` or `Authentication and authorization`, supported by `en.tex:81` and `en.tex:86` |
| 11 | `en.tex:69`, `pt.tex:69` | Gate 3.7, -2. `Frontend: React` is a one-item group | Add `React Native`, confirmed at Lippaus in `DOSSIER.md` and already used at `en.tex:104`. The group becomes `Frontend: React \| React Native` |
| 12 | `en.tex:71`, `pt.tex:71` | Gate 3.7. `Testing and AI tooling` fuses two unrelated concepts under one label | Split into `Testing: Vitest \| Jest` and `AI tooling: Claude Code \| Codex \| Agentic workflows`. Costs one line; the one-page constraint has room |
| 13 | `en.tex:36`, `pt.tex:36` | Gate 3.8, -1. `\resumeItem` gives wrapped bullets no hanging indent. Five bullets wrap in EN, six in PT; each continuation line starts flush under the bullet glyph | Give `\resumeItem` a hanging indent so continuation lines align under the bullet text. This is a macro change, not a content change, and does not touch the accepted header exception |
| 14 | `en.tex:62`, `pt.tex:62` | Gate 3.1, -3. The Summary writes `core APIs` in lower case; the posting title and the Skills line write `Core APIs` | Capitalize to `Core APIs` in both Summaries. One-character change, aligns the highest-weight field with the posting's exact title token |
| 15 | `en.tex:81`, `:83`, `:84`, `:86`, PT same | Gate 3, unscored. Four of seven DexCare bullets open with `Reduce` | Vary two openers without changing the facts, for example `Cut` or `Isolated`. Cosmetic, cheap, visible on a fast scan |
| 16 | `en.tex:62`, `pt.tex:62` | `US-hours overlap` is not recorded in `DOSSIER.md`. The posting states **no** overlap window; it asks for asynchronous work | **Escalate to Lucas.** The claim buys nothing at Gate 1 for this posting and is unverified. Either Lucas confirms it as a fact, or the clause goes |
| 17 | `en.tex:104`, `pt.tex:104` | "Supported nationwide expansion" is not in `DOSSIER.md`. The multi-tenant platform and the stack are confirmed; a national rollout is not | Confirm with Lucas or remove. It carries no posting token, so removal costs nothing at Gate 2 |
| 18 | `en.tex:101` and `:110`, `pt.tex` same | Both Lippaus roles print `Remote`. LinkedIn records `Lippaus Distribuidora` as `On-site`, Vitória. The DOSSIER rule "Role locations print `Remote` only" justifies itself against the DexCare and Luizalabs employer cities and does not address the Lippaus On-site record | **Escalate to Lucas.** This is a conflict between two of his own instructions. Outside the title, company and date scope, so it is not a Gate 0 FAIL. I do not resolve it. Carried forward unchanged from `reports/charterup-senior-fullstack-gate0.md` fix 13 |
| 19 | `pt.raw.txt` throughout | PT Gate 2 is 4 points below EN because seven English retrieval tokens are translated away: `real-time`, `microservices`, `testing`, `reliability`, `production`, `English`, `5+ years` | The posting is written in English, so **submit the EN document**. If the PT file is used anywhere, keep the English proper term beside the Portuguese phrase where it is an established technical term, for example `em tempo real (real-time)`. Architect's call, low priority for this posting |

---

## Claims I could not verify

Listed for Lucas. Not deleted, not defended.

1. **"US-hours overlap"** — `en.tex:62`, `pt.tex:62`. Not in `DOSSIER.md`. See fix 16.
2. **"Supported nationwide expansion"** — `en.tex:104`, `pt.tex:104`. A Lippaus national rollout is not recorded. See fix 17.
3. **"for a beverage distribution startup"** — `en.tex:112`, `pt.tex:112`. Lippaus's industry and company stage are not recorded in `DOSSIER.md`.
4. **"gated by Vitest and Jest in CI/CD"** — `en.tex:95`, `pt.tex:95`. The DOSSIER confirms Vitest and Jest as tools used at Luizalabs and Lippaus. It does not record that they gated a CI/CD pipeline.
5. **"provider availability"** — `en.tex:80`, `pt.tex:80`. `DOSSIER.md` lists a `forq-availability` service and event-driven booking as FACT-OBSERVED. The phrase is a reasonable reading of that, but "provider availability" as a delivered outcome is not recorded in those words.
6. **Go depth** — `en.tex:66`, `en.tex:93`. `DOSSIER.md` confirms Go at Luizalabs [FACT] and records no depth. The bullet is correctly scoped and claims nothing more. Flagged only because this posting weights Go equally with Node.js, so Lucas needs to know exactly how thin this is before he applies.
7. **Java depth at Luizalabs** — `en.tex:93`. `DOSSIER.md` records "Node, Java, and others" with no depth. Correctly scoped, flagged for the same reason.
8. **Lippaus location "Remote"** — conflicts with the LinkedIn "On-site" record. See fix 18.

Verified and clear, checked and needing no action: every company, title and
date against the LinkedIn ground-truth block; all seven percentage figures
(DOSSIER metric IDs D2, D3, D5, D7, L2, L3, P2); the DexCare stack tokens
(FACT-OBSERVED from the repos on disk); the SPI description and its 33%;
`RabbitMQ` and `AMQP` as Skills-only tokens by Lucas's instruction;
`Claude Code`, `Codex` and `Agentic workflows`; `React Native` at Lippaus;
the Magazine Luiza / SEFAZ fiscal domain; `Advanced/C1` English; the
Information Systems degree at FAESA; `Vitória, ES, Brazil` on the contact
line with no UTC offset printed.

---

## Analyzer's read, in one paragraph

The build is sound. Both documents parse, both are one page, every title and
date matches LinkedIn character for character, both Lippaus roles survive as
separate blocks, no Ruby or Rails token appears, and no `[UNVERIFIED]` marker
ships. Gate 1 has no FAIL: Brazil location, 5+ years against a 2+ requirement,
and stated Advanced/C1 English all clear. Gate 3 at 90 is strong. Gate 2 at 9
is the story, and it splits in two. Fifteen of the 24 raw points lost are
recoverable inside the DOSSIER: fixes 1, 2, 4, 5, 9, 10 and 14 cost nothing in
truth and are worth roughly 12 points. The other loss is structural. The
posting asks for Git, IDEs, shell scripting, performance tuning and debugging,
and `DOSSIER.md` records none of them, so those five zeros are honest. The
`RabbitMQ` / `AMQP` -10 is not an Architect error at all; it is Lucas's own
Skills-only instruction meeting the rubric's stuffing rule, and only Lucas can
release it. Fixes 3, 6, 7, 8, 16, 17 and 18 are questions for him. His answers,
not the Architect's next edit, decide whether this application is worth sending.
