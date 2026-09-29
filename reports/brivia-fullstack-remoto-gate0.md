# ATS Analysis — brivia-fullstack-remoto-en.pdf / brivia-fullstack-remoto-pt.pdf vs brivia-fullstack-remoto
Segment: agency   Date: 2026-09-01

Extractions regenerated from the PDFs on disk with `pdftotext` (raw) and
`pdftotext -layout`. Gate 0 and Gate 2 judged on the raw stream.

## Verdict

| Gate | EN | PT |
|---|---|---|
| Gate 0 — Parse integrity | PASS (2 header-only findings, reported not blocking) | PASS (2 header-only findings, reported not blocking) |
| Gate 1 — Knockouts | FAIL — 1 knockout (PJ / CNPJ not stated on the document) | FAIL — 1 knockout (PJ / CNPJ not stated on the document) |
| Gate 2 — Retrieval coverage | 42/100 | 42/100 |
| Gate 3 — Human scan | 95/100 | 95/100 |

Overall: **BLOCKED at Gate 1.** Gate 0 is clean. The blocking defect is a
contract-eligibility statement the posting makes a hard requirement and the
document does not answer. The dossier records the fact, so the fix is additive.

---

## Gate 0 — Parse integrity

Scored against the accepted exception in `RUBRIC.md` and `CV-SPEC.md` item 2:
failures caused only by the two-column `tabular*` role header are reported,
not blocking.

| # | Check | EN | PT | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | PASS | Raw extraction is 3423 B (EN) / 3550 B (PT), full prose recovered |
| 0.2 | Glyph integrity | PASS | PASS | 0 hits for U+FB00-U+FB06 in either raw file. `workflows` x4, `back-office` x2, `fiscal` x1, `flags` x1 recovered intact in EN; `fiscais` x3, `backoffice` x2, `flags` x1 in PT |
| 0.3 | Contact block recoverable | PASS | PASS | Line 3 of raw, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email, LinkedIn all present. No header or footer used |
| 0.4 | Section headers verbatim | PASS | PASS | EN: `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION` as standalone lines. PT: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`. Uppercase rendering allowed by 0.4 |
| 0.5 | Employment-block segmentation | FAIL (header-only, non-blocking) | FAIL (header-only, non-blocking) | Each role splits into two raw blocks: `DexCare` / `Senior Software Engineer`, blank line, `Jan 2026 - Present` / `Remote`. **No two roles merge. No role splits into two roles.** Four distinct roles recover with the correct company, title, dates. Cause is the `tabular*` header alone |
| 0.6 | Date parseability | FAIL (header-only, non-blocking) | FAIL (header-only, non-blocking) | Dates are adjacent to the title but not on the same line, and a blank line separates them. Format itself is correct: `Mon YYYY - Mon YYYY`, ASCII hyphen, every role |
| 0.7 | Reading order | FAIL (header-only, non-blocking) | FAIL (header-only, non-blocking) | Layout pairs `DexCare` with `Jan 2026 - Present` on one line; raw emits both left cells, then both right cells. Disagreement is confined to the role header. Bullets, Summary, Skills and Education agree in both extractions |
| 0.8 | No forbidden constructs | FAIL (header-only, non-blocking) | FAIL (header-only, non-blocking) | `tabular*` in `\resumeSubheading` (line 39, both files). **`pdfimages -list` returns zero images in both PDFs.** No photo, no icon, no text box, no image of text |

### Titles, company names and dates vs DOSSIER LinkedIn ground truth

| Document | LinkedIn ground truth | Match |
|---|---|---|
| `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | exact |
| `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` | `Mid-level Software Engineer` / `Luizalabs` / `Jan 2024 - Jan 2026` | exact |
| `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | same | exact |
| `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | same | exact |
| `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | months exact; separator is ASCII hyphen per `CV-SPEC.md` and the Lucas clarification of 2026-09-01 |

**No Gate 0 title or date FAIL.** All four employment blocks and the education
block match LinkedIn character for character on company, title and month.

The PT file keeps the job titles in English, matching LinkedIn. It translates
only the degree line (`Bacharelado em Sistemas de Informação`). This is
consistent with rule 1, which binds titles and dates, not degree prose.

### Source grep

`grep -rniE 'ruby|rails|UNVERIFIED'` over `brivia-fullstack-remoto-en.tex` and
`brivia-fullstack-remoto-pt.tex`: **zero hits in both files.**

### Page count

`pdfinfo`: `Pages: 1` for both PDFs. Confirmed.

---

## Gate 1 — Knockouts

Extracted from the posting text only.

| Check | Posting says | Result |
|---|---|---|
| Work authorization / entity type | `Contratação no modelo PJ (CNPJ ativo necessário);` | **FAIL.** The posting makes an active CNPJ a hard requirement. Neither PDF states PJ availability or a CNPJ. `DOSSIER.md` records `PJ with own CNPJ` as [FACT], so the document is silent on a fact it holds |
| Location or time-zone overlap | `Brazil`; `Remoto`; `Disponibilidade para atuar em modelo remoto` | PASS. Contact line reads `Vitória, ES, Brazil` / `Vitória, ES, Brasil`. Every role prints `Remote` / `Remoto` |
| Minimum years of experience | not stated | not stated |
| English proficiency requirement | not stated | not stated |
| Degree requirement | `será considerada um diferencial` — differential, not required | PASS as a differential. `Information Systems` / `Sistemas de Informação` is one of the four named fields |
| Own equipment | `Equipamento próprio;` | not stated on either document. Not a rubric row; recorded because the posting states it as a condition |
| Required skills present verbatim | see Gate 2 | 4 required tokens absent, 3 more present only as a synonym |

**Gate 1 verdict: FAIL on one row.** Time-zone and English are `not stated` in
this posting, so the LatAm-remote hard-gate rule in `RUBRIC.md` does not fire
here.

---

## Gate 2 — Retrieval coverage: EN 42/100, PT 42/100

Scoring method, stated so the run is reproducible:

- Tokens are taken from `Requisitos` and `Requisitos Técnicos` (weight 3) and
  from `Diferenciais` and `Formação Acadêmica` (weight 1).
- The posting is in Portuguese. The EN document is scored on the English
  equivalent of each token, the PT document on the posting's literal
  Portuguese term.
- Placement points follow `RUBRIC.md` Step 2. For a token that is a practice or
  a phrase rather than a listed technology (integrations, asynchronous
  processing, testable code, code review, engineering best practices,
  architecture decisions), a `Skills` entry is not expected: presence in one
  Experience bullet in context scores 3, and 4 if it is also in the Summary.
  This deviation is recorded here, not applied silently.
- `earned = points * weight`, `max = 4 * weight`.

### Required tokens (weight 3)

| # | Posting token (PT / EN) | EN placement | EN pts | PT placement | PT pts |
|---|---|---|---|---|---|
| R1 | Fullstack | Summary, Skills label, job title `Entry-level Fullstack Software Engineer` | 4 | Resumo, Skills label, same job title | 4 |
| R2 | React | Summary, Skills, D6 bullet `monitoring React with Datadog RUM` | 4 | Resumo, Skills, D6 | 4 |
| R3 | TypeScript | Summary, Skills, D1 `event-driven TypeScript services` | 4 | Resumo, Skills, D1 | 4 |
| R4 | Node.js | Summary, Skills, D1 `on Node.js with Express and Koa` | 4 | Resumo, Skills, D1 | 4 |
| R5 | APIs | Summary `Delivers APIs`, Skills, D2 `multi-tenant APIs` | 4 | Resumo `Entrega APIs`, Skills, D2 | 4 |
| R6 | BFF / BFFs | **absent** | 0 | **absent** | 0 |
| R7 | integrações / integrations | Summary, D4 `through integrations between the scheduling platform and Epic EMR`, P2 | 4 | Resumo, D4, P2 | 4 |
| R8 | PostgreSQL | Skills, D3, P1 | 3 | Skills, D3, P1 | 3 |
| R9 | bancos de dados relacionais / relational databases | **absent verbatim.** Synonym present: `PostgreSQL` | 0 | **absent verbatim.** Synonym: `PostgreSQL` | 0 |
| R10 | processamento assíncrono / asynchronous processing | Summary, L2 `asynchronous BullMQ queues`, P2 `asynchronous BullMQ jobs` | 4 | Resumo, L2 `filas BullMQ assíncronas`, P2 `jobs assíncronos BullMQ` | 4 |
| R11 | mensageria / messaging | Skills group label `Data and messaging` only. No Experience bullet uses the word | 1 | Skills label `Dados e mensageria` only | 1 |
| R12 | código testável / testable code | D5 `produce testable, high-quality code` | 3 | D5 `código testável e de alta qualidade` | 3 |
| R13 | code review | **absent** | 0 | **absent** | 0 |
| R14 | CI/CD | Summary, Skills, L3 `gating CI/CD` | 4 | Resumo, Skills, L3 `gate do CI/CD` | 4 |
| R15 | Produto, UX, Dados, QA collaboration | **absent.** Nearest is `stakeholder communication`, which names none of the four functions | 0 | **absent.** Nearest is `comunicação com stakeholders` | 0 |
| R16 | remoto / remote | Role location `Remote` on all four roles | 3 | `Remoto` on all four roles | 3 |
| R17 | integração com serviços e modelos de IA/ML | **absent.** The document evidences AI tooling for engineering, not application integration with AI/ML services or models. Distinct requirement in the posting | 0 | **absent**, same reason | 0 |
| R18 | ferramentas de IA na engenharia / AI tools in engineering | Summary `AI-driven agentic workflows into daily engineering`, Skills `AI tools`, D5 `Claude Code and Codex environments` | 4 | Resumo, Skills `Ferramentas de IA`, D5 | 4 |
| R19 | testes / tests | Skills `Vitest \| Jest`, D5 `and tests`, L3 `Vitest and Jest suites` | 3 | Skills, D5 `e testes`, L3 `suítes Vitest e Jest` | 3 |
| R20 | boas práticas de engenharia / engineering best practices | **absent verbatim.** Mechanisms are present (`lint enforcement, cyclomatic complexity limits, and tests`), the token is not | 0 | **absent verbatim** | 0 |

Required subtotal: **49 points** of a possible 80, both files.

### Preferred tokens (weight 1)

| # | Posting token | EN placement | EN pts | PT pts |
|---|---|---|---|---|
| P1 | soluções orientadas a dados / data-driven | absent | 0 | 0 |
| P2 | indicadores, scores, recomendações, modelos preditivos | absent. Correctly withheld: the Maestro brief forbids the predictive-model claim and the dossier has no fact | 0 | 0 |
| P3 | microsserviços / microservices | Summary, Skills, L1 `distributed tax microservices in Java and Go` | 4 | Resumo, Skills, L1 `microsserviços fiscais distribuídos` | 4 |
| P4 | arquiteturas modernas de aplicações web | absent | 0 | 0 |
| P5 | plataformas de mensageria e processamento distribuído | absent as a token. Overlaps R11, not double counted | 0 | 0 |
| P6 | decisões de arquitetura / architecture decisions | Skills group label `Backend and architecture` only | 1 | `Backend e arquitetura` only | 1 |
| P7 | certificações Cloud / DevOps / Arquitetura / IA-ML | absent. Correctly withheld, no dossier fact | 0 | 0 |
| P8 | Sistemas de Informação / Information Systems | Education `Bachelor's degree, Information Systems` | 3 | `Bacharelado em Sistemas de Informação` | 3 |

Preferred subtotal: **8 points** of a possible 32, both files.

### Computation

```
earned = (49 * 3) + (8 * 1) = 155
max    = (80 * 3) + (32 * 1) = 272
coverage = 100 * 155 / 272 = 57.0
```

### Stuffing penalty

`RUBRIC.md` Step 4: minus 5 per token in `Skills` with no supporting evidence
anywhere in `Experience`.

| Token | Finding | Penalty |
|---|---|---|
| `RabbitMQ` | Skills line 68 only. No Experience bullet mentions it | -5 |
| `AMQP` | Skills line 68 only. No Experience bullet mentions it | -5 |
| `AWS` | Skills line 70 only. No Experience bullet mentions AWS, although the dossier records AWS SDK v3 at DexCare | -5 |

Every other Skills token has Experience support: Go (L1), DynamoDB (D3),
Redis (D3), Docker / Kubernetes / ArgoCD / GCP (L3), Datadog (D6),
LaunchDarkly / OpenFeature (D6), Auth0 (D2), Express / Koa (D1),
OpenAPI/Swagger (D2), JavaScript (E1), Vitest / Jest (L3), Claude Code /
Codex / Agentic workflows (D5), microservices (L1), APIs (D2).

No token in the table reaches 4 occurrences. Observation, outside the table:
`workflows` appears 4 times in the EN document (Summary, Skills, L4, E1). It is
not a posting token, so no penalty is applied. Flagged because a human reader
notices repetition.

```
Gate 2 EN = 57.0 - 15 = 42.0  ->  42/100
Gate 2 PT = 57.0 - 15 = 42.0  ->  42/100
```

### Required tokens not covered

Absent entirely, weight 3:

1. `BFF` / `BFFs`
2. `code review`
3. Collaboration with `Produto`, `UX`, `Dados`, `QA`
4. Integration of applications with `serviços e modelos de IA/ML`
5. `boas práticas de engenharia` / engineering best practices

Present only as a synonym, weight 3:

6. `bancos de dados relacionais` / relational databases — only `PostgreSQL`
7. `mensageria` / messaging — Skills group label only, no Experience evidence
8. `processamento distribuído` — only `distributed tax microservices`

Preferred tokens not covered: `soluções orientadas a dados`, `indicadores`,
`scores`, `recomendações`, `modelos preditivos`, `arquiteturas modernas de
aplicações web`, `plataformas de mensageria`, `certificações`.

---

## Gate 3 — Human scan: EN 95/100, PT 95/100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15/15 | Summary line 1 opens `Senior Software Engineer with 5+ years building fullstack web applications`. The posting title token `Fullstack` is in the first sentence, both languages |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | **15/20** | D1 (TypeScript, Node.js, Express, Koa), D2 (multi-tenant APIs, Auth0, OpenAPI), D3 (PostgreSQL, Sequelize, Drizzle, DynamoDB, Redis) are all on target. **React, the first technology the posting names, does not appear until DexCare bullet 6.** For a Fullstack posting that leads with `Frontend: React e TypeScript`, that is a real placement miss |
| 3.3 | Every bullet leads with an outcome or action verb | 15/15 | EN: Deliver, Reduce, Serve, Reduce, Enable, Reduce, Reduce, Deliver, Improve, Keep, Cut, Support, Increase, Turn, Support, Deliver. PT: Entrega, Reduz, Atende, Reduz, Permite, Reduz, Reduz, Entrega, Melhora, Mantém, Reduz, Apoia, Aumenta, Converte, Apoia, Entrega. No `Responsible for`, no first person |
| 3.4 | At least 3 bullets carry a real number | 15/15 | Seven: 25%, 15%, 7%, 33%, 20%, 18%, 26%. All traceable to the metrics Lucas supplied on 2026-09-01 |
| 3.5 | Length: 1 page under 10 years | 10/10 | `pdfinfo` reports 1 page for both |
| 3.6 | No unsupported buzzwords | 10/10 | No `team player`, `results-driven`, `passionate`, `rockstar`. `high-quality` and `real-time` are attached to concrete mechanisms |
| 3.7 | Skills grouped by category | 10/10 | Six labelled groups, not a wall |
| 3.8 | Scannable | 5/5 | Consistent role-header shape, bold company, four employment blocks, one page, headers with rules |

```
Gate 3 EN = 95/100
Gate 3 PT = 95/100
```

---

## Fix list for the Resume Architect

Ranked by cost. Nine fixes. Priority follows the role file: Gate 0 first, then
Gate 1 knockouts, then missing required retrieval tokens, then Gate 3.

**1. Gate 1 — PJ / CNPJ eligibility is not stated.**
File: `resumes/brivia-fullstack-remoto-en.tex` and `-pt.tex`, contact block
region, lines 52-58 (the block above `\section{Summary}` / `\section{Resumo}`).
Defect: the posting makes `Contratação no modelo PJ (CNPJ ativo necessário)` a
hard requirement. Neither document answers it. `DOSSIER.md` records
`PJ with own CNPJ` as [FACT, Lucas 2026-09-01].
What would pass: one short line stating PJ availability with an active CNPJ,
in the contact block or as the closing sentence of the Summary. PT wording
should use the posting's own term `PJ` and `CNPJ`. Do not print a UTC offset.

**2. Gate 2 — `code review` is absent (weight 3, 0/12 points).**
File: both `.tex`, DexCare bullet D5, line 83.
Defect: the bullet describes shared rules, lint enforcement, complexity limits
and tests, but never the token the posting names twice (`Vivência com code
review`, `Qualidade: testes, code review`).
What would pass: name `code review` inside D5 or a neighbouring DexCare bullet,
in context with the quality mechanisms already there. The token is identical in
both languages.

**3. Gate 2 — `BFF` / `BFFs` is absent (weight 3, 0/12 points).**
File: both `.tex`, Skills line 67 and DexCare bullet D2, line 80.
Defect: the posting lists BFF twice as a required architecture item. The
Architect's draft states the dossier holds no BFF fact, which is correct.
What would pass: nothing, unless Lucas confirms BFF work. **Do not invent it.**
Escalate to Lucas as a yes/no question. If confirmed, add `BFF` to the
`Backend and architecture` / `Backend e arquitetura` Skills line and to D2 in
context. If not confirmed, this token stays at 0 and the gap is honest.

**4. Gate 2 — application integration with AI/ML services and models is absent
(weight 3, 0/12 points).**
File: both `.tex`, Skills line 71 and DexCare bullet D5, line 83.
Defect: the posting states two separate AI requirements. The document covers
one (AI tools applied to engineering, D5, scoring 4). It does not cover the
other (`integração de aplicações com serviços e modelos de IA/ML`). D5 does not
substitute for it.
What would pass: nothing without a fact. `DOSSIER.md` records `intelligence-engine`
as a DexCare service on disk but does not say what it does. Escalate to Lucas:
did he integrate an application with an AI or ML service or model? Do not
infer it from the service name.

**5. Gate 2 — collaboration with Produto, UX, Dados and QA is absent
(weight 3, 0/12 points).**
File: both `.tex`, Lippaus mid-level bullet P3, line 104.
Defect: P3 says `leading project scoping and stakeholder communication` /
`liderando o escopo de projetos e a comunicação com stakeholders`. `stakeholders`
names none of the four functions the posting requires.
What would pass: if the dossier or Lucas supports it, name the functions
explicitly in P3 or in a DexCare bullet. The dossier does not record this
today, so escalate before writing it.

**6. Gate 2 — `mensageria` / `messaging` scores 1 of 12, and `RabbitMQ` and
`AMQP` each take a -5 stuffing penalty.**
File: both `.tex`, Skills line 68.
Defect: `RabbitMQ` and `AMQP` sit in Skills with zero Experience support. That
is -10 of the -15 total penalty, and it is the largest single lever in Gate 2.
The posting requires `Conhecimento em processamento assíncrono e mensageria`.
What would pass: name RabbitMQ or AMQP inside one DexCare bullet in context.
`DOSSIER.md` records `DexCare messaging: RabbitMQ / AMQP used on services`
as [FACT, Lucas 2026-09-01], with the constraint `Skills token only, no service
names on the CV`. Ask Lucas whether a bullet may say he used RabbitMQ/AMQP
without naming a service. If yes, this single edit recovers roughly 10 points.

**7. Gate 2 — `AWS` takes a -5 stuffing penalty.**
File: both `.tex`, Skills line 70.
Defect: `AWS` appears in Skills with no Experience bullet mentioning it, while
`DOSSIER.md` records `AWS SDK v3 — S3, STS, Secrets Manager, RDS Signer` as a
repo-observed fact at DexCare.
What would pass: name AWS in one DexCare bullet, for example inside D3 next to
DynamoDB Streams. Recovers 5 points and removes a human-reaction defect. The
posting does not require AWS, so this is penalty removal, not coverage gain.

**8. Gate 3.2 — React is buried at DexCare bullet 6 (-5 points).**
File: both `.tex`, DexCare bullets, lines 79-85.
Defect: the posting's first technical requirement is `Frontend: React e
TypeScript`. In the document React first appears in Experience at D6, line 84,
below the fold of a fast scan of the current role.
What would pass: move the React evidence into the first three DexCare bullets,
or add React to D1 if the dossier supports it (`Frontend: React` is recorded
for DexCare). Keep the 7% release-risk metric attached wherever D6 lands.

**9. Gate 2 — `bancos de dados relacionais` and `boas práticas de engenharia`
are absent verbatim.**
File: both `.tex`, Skills lines 67-69.
Defect: the posting names `bancos de dados relacionais` and `boas práticas de
engenharia` as requirements. Only `PostgreSQL` and the concrete quality
mechanisms are present. Exact-token retrieval does not expand these.
What would pass: in the PT file, relabel the Skills group to carry
`bancos de dados relacionais` alongside PostgreSQL, and use `boas práticas de
engenharia` once where the quality mechanisms are described. Mirror in EN with
`relational databases` and `engineering best practices`. This is relabelling
of existing true content, not a new claim.

Not a fix, recorded for Lucas: the posting states `Equipamento próprio`. The
document is silent and `DOSSIER.md` has no fact. The Architect already routed
this to the message file. It belongs in the application form, not on the CV.

---

## Claims I could not verify

Traced against `DOSSIER.md`. Neither `.tex` carries an `[UNVERIFIED]` marker,
so these are unmarked claims with no dossier line behind them. I do not delete
them and I do not defend them. Lucas decides.

1. **`beverage distribution startup` / `startup de distribuição de bebidas`** —
   `brivia-fullstack-remoto-en.tex` line 111, `-pt.tex` line 111.
   `DOSSIER.md` names the employer `Lippaus Distribuidora` and confirms the
   back-office dashboards in JavaScript, but records no industry and no company
   size. Beverage distribution and startup are both unsourced in the dossier.

2. **`nationwide retailer expansion` / `expansão nacional de varejistas`** —
   line 102 in both files.
   The dossier confirms `multi-tenant web and mobile platform on PostgreSQL`
   for Lippaus. It records no national scope and no retailer customer base.

3. **`real-time` in D1** — line 79 in both files.
   The dossier confirms `event-driven booking` and `healthcare scheduling at
   scale` from the repos. It records no latency figure and does not use the
   term real-time. The dossier's DexCare section still lists scale numbers as
   [OPEN].

4. **`Magazine Luiza's e-commerce operation`** — line 92 in both files.
   The dossier confirms the fiscal / NF-e / SEFAZ domain at Luizalabs and names
   Magazine Luiza as the employer group. It does not state that the invoice
   issuing served the e-commerce operation specifically.

5. **`5+ years` / `mais de 5 anos`** — Summary, line 62 region, both files.
   Not stated in the dossier as a claim, but arithmetically derivable from the
   LinkedIn ground truth block: `Mar 2021` to today is 5 years 6 months.
   Recorded for completeness, not contested.
