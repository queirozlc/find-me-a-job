# ATS Analysis — resumes/hunts/2026-09-04/noemi-sandrini-integrations-backend-engineer/Lucas-Queiroz-Resume-en.pdf vs noemi-sandrini-integrations-backend-engineer
Segment: us-direct   Date: 2026-09-04

## Verdict
BLOCKED at Gate 1.

Gate 0 is fully PASS. Every parse check survives extraction.

Gate 1 fails on required-skill presence. Eleven stated posting requirements have zero
resume evidence. Nine of those eleven have no support in `DOSSIER.md` either, so the
Architect cannot close them alone. They need a decision from Lucas.

Gate 2 fails as a consequence, at 48/100.

Factual integrity is clean. Every employer, title, and date matches the live LinkedIn
profile, read read-only on 2026-09-04.

## Sources actually read
- `~/career/AGENTS.md`, `~/career/CLAUDE.md`, `~/career/RUBRIC.md`,
  `~/career/ATS-KNOWLEDGE.md`, `~/career/CV-SPEC.md`, `~/career/DOSSIER.md`.
- `~/career/jobs/noemi-sandrini-integrations-backend-engineer.md`, posting text and
  Maestro brief.
- The CV source `.tex`, the compiled PDF, and both extractions.
- `~/career/reports/noemi-sandrini-integrations-backend-engineer-draft.md`, the
  Architect note, read to check declared gaps against the artifact.
- `Profile Check` portal, read-only. No edit action was sent:
  - https://www.linkedin.com/in/queiroz-lucas/details/experience/
  - https://www.linkedin.com/in/queiroz-lucas/details/education/
- The apply link https://lnkd.in/dpNKwZBu was **not** opened. Posting text is quoted
  from the local job file only.
- The four PDFs under `~/Documents/Resumes/` were not opened. They are invalid sources.

## Extraction step, performed first
```
pdftotext -layout Lucas-Queiroz-Resume-en.pdf - > extracted-layout.txt
pdftotext         Lucas-Queiroz-Resume-en.pdf - > extracted-raw.txt
```
Gate 0 and Gate 2 are judged on the raw file. 54 content lines. 1 page, letter size.
All line numbers below refer to the raw extraction.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 54 clean lines. `pdfimages -list` returns zero images, so the page is not a scan. `pdfinfo` shows Producer `xdvipdfmx`, not encrypted. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00-U+FB06. Zero `\x00` and zero U+FFFD. The complete non-ASCII inventory of the raw file is 11 `•`, 4 `ó`, and 1 form feed page separator. Probe words extract intact: `workflows` (lines 22, 47), `office` in `back-office` (line 47), `friction` (line 24), `Fullstack` (line 44). `profile`, `efficient`, and `conflict` do not occur in this document. The `fontspec` plus `Ligatures=NoCommon` fix at source lines 11-12 works. |
| 0.3 | Contact block recoverable, in the body | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. Email, phone, city, and LinkedIn URL are all present. The source sets `\pagestyle{empty}` and puts the block inside `\begin{center}` in the body, not a header or footer. |
| 0.4 | Section headers present verbatim | PASS | Raw lines 5, 10, 17, 49 carry `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION` as standalone lines. Source strings are `\section{Summary}`, `{Skills}`, `{Experience}`, `{Education}`. Uppercase rendering is allowed by the rubric. |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks in the raw stream. None merged and none split: DexCare 18-28, Luizalabs 29-36, Lippaus Distribuidora Mid-level 37-42, Lippaus Distribuidora Entry-level 43-47. Each block prints Company / Title / Location / Dates as four consecutive lines before its bullets. Both Lippaus roles repeat the company line, so the promotion cannot collapse into one entry. |
| 0.6 | Date parseability | PASS | Every role carries `Mon YYYY - Mon YYYY` on its own line inside its block: lines 21, 32, 40, 46, and 53 for Education. ASCII hyphen throughout. Zero EN DASH and zero EM DASH in the extraction. The date line sits one line below the title, separated only by the location line, inside the same contiguous block. No role boundary intervenes, so each date binds to one title without ambiguity. |
| 0.7 | Reading order | PASS | Raw and layout extraction were compared token by token after whitespace normalisation. The token order is identical. No adjacent content block disagrees. |
| 0.8 | No forbidden constructs | PASS | The source uses `itemize` only. No `tabular`, no `tabular*`, no `tcolorbox`, no `minipage`, no `\includegraphics`. `pdfimages -list` is empty, so no photo and no contact icon. Fonts are four embedded subsets, each with a `uni` map. |

## Gate 1 — Knockouts

The posting is pt-BR. Requirement wording is quoted verbatim from the posting, then
translated in the evidence column.

| Check | Source | Result | Evidence |
|---|---|---|---|
| Work authorization / entity type | posting | not stated | The posting states "100% remoto, LATAM", "40h/semana", and "Contratação de longo prazo". It names no work authorization and no legal entity type. The Maestro brief records the same. |
| Location or time-zone overlap | posting | PASS on location, not stated on overlap | Posting: "uma posição 100% remota para profissionais da LATAM". CV line 3 prints `Vitória, ES, Brazil`, inside LATAM. No overlap window is stated in the posting. The CV prints no UTC offset and no overlap sentence, as CLAUDE.md rule 3 demands. |
| Minimum years of experience | posting | not stated | Posting: "Experiência em desenvolvimento Back-end". No number is given. |
| English proficiency requirement | posting | PASS on the proficiency half | Posting: "Inglês avançado/fluente, incluindo comunicação direta com clientes." `Advanced English` is placed in Skills line 15 and in Experience line 28. The second half of the same requirement, direct client communication, is a separate FAIL row below. |
| Degree requirement | posting | not stated | The posting names no degree. |
| Required skill: Node.js | posting | PASS | Skills line 11, Experience line 22. |
| Required skill: TypeScript | posting | PASS | Skills line 11, Experience line 22. |
| Required skill: Express.js **or** NestJS | posting | PASS | Posting writes "Express.js/NestJS", an alternative. `Express` is placed in Skills line 12 and Experience line 23. `NestJS` is absent and is not required, because the alternative is satisfied. Spelling note: the posting writes `Express.js`, the CV writes `Express`. |
| Required skill: REST | posting | PASS | `REST APIs` in Skills line 12 and Experience line 24. |
| Required skill: AWS | posting | PASS | Skills line 13, Experience line 25 `AWS SDK v3`. |
| Required skill: Docker | posting | PASS | Skills line 13, Experience line 35. |
| Required skill: PostgreSQL | posting | PASS | Skills line 13, Experience lines 25 and 41. |
| Required skill: sistemas orientados a eventos | posting | PASS | Event-driven systems. `event-driven` in Skills line 12 and Experience line 22. |
| Required skill: filas / mensageria | posting | PASS | Queues and messaging. `queues` in Skills line 12 and Experience line 34 `BullMQ queues`. The posting names `AWS SQS` with "como", meaning "such as", so SQS is an example and not a separate cumulative requirement. `AWS SQS` is absent from the CV. |
| Required skill: testes | posting | PASS | `testing` in Skills line 15 and Experience line 27. |
| Required skill: arquitetura de sistemas distribuídos | posting | PASS | `distributed systems` in Skills line 12 and Experience line 33. |
| Required skill: AI-assisted development | posting | PASS | Skills line 15, Experience line 26. |
| **Required skill: desenvolvimento Back-end** | posting | **FAIL** | Back-end development. `Back-end` with the posting hyphen: 0 occurrences. `Backend` appears once, at line 12, and only as the Skills category label `Backend and integrations:`. It is not a listed skill token and it appears in no Experience bullet. |
| **Required skill: integrações de APIs de terceiros** | posting | **FAIL** | Third-party API integrations. `third-party`: 0 occurrences. `integrations` appears once, at line 12, again only inside the category label `Backend and integrations:`. No Experience bullet names an integration with an external system. This is the head noun of the role title, `Integrations Back-end Engineer`. |
| **Required skill: OAuth 2.0 / OIDC** | posting | **FAIL** | `OAuth`: 0 occurrences. `OIDC`: 0 occurrences. Line 24 carries `Auth0 JWT`. RUBRIC Gate 1 forbids inferring evidence that the document does not state, so `Auth0` is not counted as `OAuth 2.0/OIDC`. |
| **Required skill: Webhooks** | posting | **FAIL** | 0 occurrences anywhere in the raw extraction. |
| **Required skill: debugging** | posting | **FAIL** | 0 occurrences. |
| **Required skill: code review** | posting | **FAIL** | 0 occurrences. |
| **Required skill: validação de código gerado por IA** | posting | **FAIL** | Validation of AI-generated code. No verbatim token. Lines 26-27 read "Improved daily code quality by using AI code agents in AI-assisted development and agentic workflows with Claude Code, Codex, lint rules, complexity limits, and testing". That is capability evidence for the same activity, but it carries neither `validation` nor `AI-generated code`. |
| **Required skill: OOP** | posting | **FAIL** | 0 occurrences. |
| **Required skill: SOLID** | posting | **FAIL** | 0 occurrences. |
| **Required skill: princípios de software design** | posting | **FAIL** | Software design principles. 0 occurrences of `software design` or `design principles`. |
| **Required skill: comunicação direta com clientes** | posting | **FAIL** | Direct client communication. `client`, `clients`, `customer`: 0 occurrences. Line 28 says "with US teams", which is internal, not client-facing. |

**Gate 1 result: FAIL.** Eleven required rows carry zero resume evidence. RUBRIC Gate 1
states directly: "For every explicit posting requirement, absent resume evidence is a
FAIL." Two of the eleven are closable from `DOSSIER.md` today. Nine are not, and must go
to Lucas before any token is written. See the fix list.

## Gate 2 — Retrieval coverage: 48/100, FAIL

Scoring convention, stated so the run is reproducible:
- An **alternative set** in the posting, marked by `/` or by "como" meaning "such as", is
  scored once as one requirement, on the best-placed member that `DOSSIER.md` supports.
- A list joined by "e", meaning "and", is **cumulative**. Each member is one requirement.
- Placement points: absent 0, `Skills` only 1, `Experience` only 2, both 3.
- Work authorization, location, and years of experience never occupy `Skills` or
  `Experience`. They live in Gate 1 only and are excluded from this denominator.

### Required requirements, weight 3

| # | Requirement, posting wording | Token scored | Skills | Experience | Points |
|---|---|---|---|---|---|
| R1 | "Experiência em desenvolvimento Back-end" | `Backend` | line 12, category label only | absent | 1 |
| R2 | "Node.js" | `Node.js` | line 11 | line 22 | 3 |
| R3 | "TypeScript" | `TypeScript` | line 11 | line 22 | 3 |
| R4 | "Express.js/NestJS", alternative | `Express` | line 12 | line 23 | 3 |
| R5 | "integrações de APIs de terceiros" | `integrations` | line 12, category label only | absent | 1 |
| R6 | "REST" | `REST APIs` | line 12 | line 24 | 3 |
| **R7** | **"OAuth 2.0/OIDC"** | `OAuth 2.0`, `OIDC` | **absent** | **absent** | **0** |
| **R8** | **"Webhooks"** | `Webhooks` | **absent** | **absent** | **0** |
| R9 | "Conhecimento em AWS" | `AWS` | line 13 | line 25 | 3 |
| R10 | "Docker" | `Docker` | line 13 | line 35 | 3 |
| R11 | "PostgreSQL" | `PostgreSQL` | line 13 | lines 25, 41 | 3 |
| R12 | "sistemas orientados a eventos" | `event-driven` | line 12 | line 22 | 3 |
| R13 | "filas/mensageria, como AWS SQS" | `queues` | line 12 | line 34 | 3 |
| R14 | "Experiência com testes" | `testing` | line 15 | line 27 | 3 |
| **R15** | **"debugging"** | `debugging` | **absent** | **absent** | **0** |
| **R16** | **"code review"** | `code review` | **absent** | **absent** | **0** |
| R17 | "arquitetura de sistemas distribuídos" | `distributed systems` | line 12 | line 33 | 3 |
| R18 | "AI-assisted development" | `AI-assisted development` | line 15 | line 26 | 3 |
| **R19** | **"validação de código gerado por IA"** | no exact token | **absent** | **absent** | **0** |
| **R20** | **"OOP"** | `OOP` | **absent** | **absent** | **0** |
| **R21** | **"SOLID"** | `SOLID` | **absent** | **absent** | **0** |
| **R22** | **"princípios de software design"** | `software design` | **absent** | **absent** | **0** |
| R23 | "Inglês avançado/fluente" | `Advanced English` | line 15 | line 28 | 3 |
| **R24** | **"comunicação direta com clientes"** | `client`, `customer` | **absent** | **absent** | **0** |

Required points, in order: 1, 3, 3, 3, 1, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 0, 0, 0, 0, 3, 0.
Sum = 41 over 24 requirements.

`AWS SQS` is not scored as a separate requirement. The posting introduces it with "como",
so it is an exemplar of R13. It is absent from the CV, and that is recorded as a match
limit, not as a required-token failure.

### Preferred requirements, weight 1

Taken from the "Diferenciais" block only.

| # | Requirement, posting wording | Token scored | Skills | Experience | Points |
|---|---|---|---|---|---|
| P1 | "SAML" | `SAML` | absent | absent | 0 |
| P2 | "Microsoft Entra ID" | `Entra` | absent | absent | 0 |
| P3 | "Microsoft Graph" | `Graph` | absent | absent | 0 |
| P4 | "Google Workspace APIs" | `Workspace` | absent | absent | 0 |
| P5 | "Experiência em startups" | `startup` | absent | absent | 0 |
| P6 | "ERPs, CRMs ou plataformas complexas", alternative | `ERP`, `CRM` | absent | absent | 0 |
| P7 | "criando workflows e padrões de engenharia utilizando IA" | `agentic workflows` | line 15 | line 26 | 3 |

Preferred points sum = 3 over 7 requirements.

`GCP` is placed in Skills line 13 and Experience line 35, but the posting never names GCP.
It is not scored. RUBRIC forbids guessing a requirement the posting did not state.

### Arithmetic
```
required:  sum(points * 3) = 41 * 3                = 123
           denominator     = 3 * 3 * 24            = 216
preferred: sum(points * 1) =  3 * 1                =   3
           denominator     = 3 * 1 *  7            =  21
coverage = 100 * (123 + 3) / (216 + 21) = 100 * 126 / 237 = 53
```

### Step 5, stuffing penalty
Literal-string counts in the raw extraction, 4 or more occurrences, restricted to tokens
the posting actually uses.

| Token | Count | Where |
|---|---|---|
| `workflows` | 5 | line 7 Summary `agentic workflows`, line 15 Skills `agentic workflows`, line 22 DexCare `provider-availability workflows`, line 26 DexCare `agentic workflows`, line 47 Lippaus `administrative workflows` |

Penalty: -5. This is the rubric's human-reaction penalty, not a machine one. Two of the
five hits, lines 22 and 47, are ordinary English usage and not keyword placement. The rule
is a literal-string rule, so the penalty applies as written. CV-SPEC also caps any term at
3 appearances, so the same count is a CV-SPEC breach.

No other posting token reaches 4. `TypeScript`, `Node.js`, `REST`, `AWS`, `PostgreSQL`,
`event-driven`, `distributed systems`, `agentic workflows`, `AI-assisted development`,
`BullMQ`, `React`, and `Go` each appear exactly 3 times. `Express`, `Docker`, `queues`,
`testing`, `Advanced English`, `AI code agents`, `GCP`, and `Redis` each appear twice.

**Gate 2 score: 53 - 5 = 48/100. FAIL.**

Required tokens without both `Skills` and `Experience` placement:
`Back-end` (R1), `third-party API integrations` (R5), `OAuth 2.0/OIDC` (R7),
`Webhooks` (R8), `debugging` (R15), `code review` (R16),
`validation of AI-generated code` (R19), `OOP` (R20), `SOLID` (R21),
`software design principles` (R22), `direct client communication` (R24).

## Gate 3 — Human scan: 91/100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 8 / 15 | Top 15% of 54 lines is lines 1 to 8. Line 6 carries `Senior Software Engineer`. The literal posting title `Integrations Back-end Engineer` appears nowhere, and neither `integrations` nor `back-end` appears in the Summary. Deduct 5 for the absent title string. **That 5 is not recoverable:** CLAUDE.md rule 1 and rule 4 fix the CV title at `Senior Software Engineer` and forbid adjusting a title to fit a posting. Do not "fix" it. Deduct 2 more for the absent domain words, which the Summary can carry without touching any title. |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | 20 / 20 | DexCare bullets 1 to 3 carry this posting's core tokens in the right order: event-driven TypeScript and Node.js on Express, multi-tenant REST APIs with authentication, then PostgreSQL and AWS data access. Correct ordering for an integrations back-end role. |
| 3.3 | Every bullet starts with a clear past-tense action verb and describes an outcome | 15 / 15 | All 11 bullets open with a past-tense verb and the subject is omitted: Delivered, Reduced, Supported, Improved, Supported, Delivered, Improved, Kept, Supported, Increased, Supported. Zero present-tense openers, zero "Responsible for", zero third person, and no bullet opens with `I`. The Summary uses `I` explicitly. This matches CLAUDE.md section 9 and CV-SPEC. Two separate weaknesses are real but fall outside this row and are listed in the defect list: `Supported` opens 4 of 11 bullets, and only 3 of 11 bullets carry the measured Y that CV-SPEC's XYZ rule requires. |
| 3.4 | At least 3 bullets carry a real, defensible number | 15 / 15 | Exactly three: 25% authentication friction (line 24), 20% invoice throughput (line 34), 26% processing capacity (line 42). Each traces to `DOSSIER.md`. See the metric trace. The bar is met at the minimum. Four more approved dossier metrics are unused. |
| 3.5 | Length: 1 page under 10 years of experience | 10 / 10 | `pdfinfo` reports `Pages: 1`, letter size. |
| 3.6 | No unsupported buzzwords | 10 / 10 | Grep for team player, results-driven, passionate, self-starter, rockstar, ninja, synergy, go-getter, detail-oriented, hard-working, guru, proven track record: zero hits. |
| 3.7 | Skills grouped by category | 10 / 10 | Five labelled groups: Languages, Backend and integrations, Data and cloud, Frontend, Delivery. Not one undifferentiated wall. |
| 3.8 | Scannable: consistent spacing, bold titles, adequate white space | 3 / 5 | Company bold, title italic, location and dates plain, consistent across all four roles and Education. Single column, full width. Deduct 2: `\resumeRoleGap` is `\vspace{4pt}`, so in the render the last bullet of one role sits close under the next company name at the DexCare-to-Luizalabs and Luizalabs-to-Lippaus joins. CV-SPEC section 2 asks for clear vertical space between the last bullet and the next role. Parse safety is unharmed and Gate 0.5 passes. This is a human-eye cost only, and about 25% of the page is unused at the bottom, so the space is available. |

**Total: 91/100.**

## Factual integrity — LinkedIn ground truth, checked 2026-09-04

Read read-only through the `Profile Check` portal. No edit action was sent to LinkedIn.

| Field | CV prints | LinkedIn shows today | Result |
|---|---|---|---|
| DexCare employer | `DexCare` | `DexCare · Full-time` | match |
| DexCare title | `Senior Software Engineer` | `Senior Software Engineer` | match |
| DexCare dates | `Mar 2026 - Present` | `Mar 2026 - Present · 7 mos` | match |
| Luizalabs employer | `Luizalabs` | `Luizalabs · Full-time` | match, spelling included |
| Luizalabs title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Luizalabs dates | `Jan 2024 - Mar 2026` | `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | match |
| Lippaus employer, both roles | `Lippaus Distribuidora` | `Lippaus Distribuidora` | match |
| Lippaus senior title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Lippaus senior dates | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024 · 1 yr 1 mo` | match |
| Lippaus first title | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | match |
| Lippaus first dates | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023 · 1 yr 11 mos` | match |
| Education | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | match. LinkedIn renders an EN DASH, the CV uses the ASCII hyphen, which is what CLAUDE.md rule 1 and CV-SPEC section 5 require |
| Role locations | DexCare `Remote`, Luizalabs `Remote`, Lippaus `Vitória, ES, Brazil` | DexCare `Seattle, Washington, United States · Remote`, Luizalabs `São Paulo, Brazil · Remote`, Lippaus `Vitória, Espírito Santo, Brazil · On-site` | correct per DOSSIER.md "Role locations". Employer cities never print. |

All twelve rows match. The date correction that blocked the tractian application on
2026-09-04 is applied here. `DOSSIER.md` "LinkedIn ground truth — captured verbatim
2026-09-04" agrees with the live profile on every row.

## Metric trace

Every number and every named technology on the CV, checked against `DOSSIER.md` and the
live profile, never against an old PDF.

| CV item | Source entry | Result |
|---|---|---|
| authentication friction -25% | DOSSIER D3, "reduced authentication friction by 25%" | traced |
| invoice throughput +20% | DOSSIER L2, "20% improvement in invoice processing throughput" | traced |
| processing capacity +26% | DOSSIER P2, "26% more processing capacity" | traced |
| `5+ years` in the Summary | not a dossier string. Arithmetic on the LinkedIn dates, Mar 2021 to Sep 2026 is 5 yrs 6 mos | derived, not invented. Stated as derived. |
| Express, Koa, PostgreSQL, DynamoDB, Redis, AWS SDK v3, Auth0, OpenAPI/Swagger, React, multi-tenant | DOSSIER "DexCare stack is observed fact, read from the repos" | traced |
| SEFAZ, electronic invoice issuing, Magazine Luiza e-commerce | DOSSIER "Luizalabs domain was fiscal / NF-e / SEFAZ" | traced |
| Go at Luizalabs | DOSSIER "Go at Luizalabs" | traced |
| BullMQ, Docker, Kubernetes, GCP, ArgoCD, Vitest, Jest | DOSSIER "Tools used at Luizalabs and Lippaus" | traced |
| Claude Code, Codex, lint rules, complexity limits, testing | DOSSIER "AI at DexCare" | traced |
| Lippaus multi-tenant web and mobile platform on PostgreSQL | DOSSIER "Lippaus and Luizalabs bullets approved by Lucas" | traced |
| Lippaus back-office dashboards in JavaScript | DOSSIER, same entry | traced |

No number on the CV lacks a source. No claim-status marker appears in the document, which
is correct: CLAUDE.md section 4 forbids verification markers for framework, data, cloud,
and tool tokens.

## Policy checks

| Rule | Result |
|---|---|
| CLAUDE.md 2, no Ruby or Rails token anywhere | PASS. Grep of the `.tex` source, the raw extraction, and the layout extraction for ruby, rails, sidekiq, activerecord, activejob, rspec, devise, pundit, hotwire, gemfile: zero hits in all three files. |
| CLAUDE.md 3, degree Information Systems, FAESA | PASS. Lines 50-51. |
| CLAUDE.md 3, location `Vitória, ES, Brazil`, nothing more | PASS. Line 3. |
| CLAUDE.md 3, never print a UTC offset or an overlap statement | PASS. Grep for GMT, UTC, time zone, overlap, BRT, -03:00: zero hits. |
| CLAUDE.md 3, Lippaus prints `Vitória, ES, Brazil`, DexCare and Luizalabs print `Remote` | PASS. Lines 20, 31, 39, 45. |
| CLAUDE.md 3, contract detail never printed | PASS. Grep for CLT, CNPJ, W-8BEN, Fullstack Labs, freelance: zero hits. |
| CLAUDE.md 4, no title, date, employer, degree, location, or metric changed to improve a match | PASS. See Factual integrity and Metric trace. |
| CLAUDE.md 9, bullet voice and Summary voice | PASS. See Gate 3.3. |
| CLAUDE.md 11, one language per tailored CV | PASS, with a stated residual risk. The posting text is pt-BR and the recruiter is Brazilian, but the posting states "empresa americana", the apply destination is `onstrider.com`, and the Maestro set `Segment: us-direct`. CV-SPEC gives `-en` to an international company. Only the `-en` file exists in the application folder, with no `-pt` sibling. The language call belongs to the Maestro, not to this seat. The residual risk is that first-pass screening happens in Portuguese. Recorded as a match limit. |
| CV-SPEC, canonical headers in the source | PASS. `\section{Summary}`, `{Skills}`, `{Experience}`, `{Education}`. |
| CV-SPEC, ASCII hyphen in every date | PASS. Zero EN DASH and zero EM DASH in the extraction. |
| CV-SPEC, every load-bearing technology in Skills **and** in an Experience bullet | PASS. Every one of the 21 tokens listed in Skills has an Experience placement. No orphan Skills token exists. This is a real strength of the artifact. |
| CV-SPEC, cap any term at 3 appearances | FAIL, minor. `workflows` appears 5 times. Already charged as the Gate 2 stuffing penalty. |
| CV-SPEC, AI or LLM mention in the Summary and in Experience | PASS. Summary line 7, DexCare bullet 4 at lines 26-27. |
| CV-SPEC, every bullet in XYZ format | FAIL, partial. Only 3 of 11 bullets carry a measured Y. See defect 6. |
| Maestro brief, do not convert a declared gap into a claim | PASS. Zero occurrences of NestJS, OAuth, OIDC, Webhook, SQS, OOP, SOLID, SAML, Entra, Graph, Workspace, ERP, CRM, startup, client. The Architect correctly refused to invent every one of them. |

## Defects, ranked by cost

**Tier A. The Architect can close these now from `DOSSIER.md`. No new fact is needed.**

1. **`Back-end` has no real placement** — Gate 1, Gate 2 R1, Gate 3.1 — The only hit is
   the Skills category label `Backend and integrations:` on line 12. A category label is
   not a listed token and it reaches no Experience bullet. This is half the posting's
   role title. Fix: add `back-end` as a listed token in the `Backend and integrations`
   group, and place it in one DexCare bullet. The DexCare and Luizalabs work is back-end
   work in the dossier's own words, so no new fact is created. Use the posting's
   hyphenated spelling `Back-end`, since the posting writes it that way and Gate 2 is
   exact-string.

2. **`integrations` and `third-party` have no real placement** — Gate 1, Gate 2 R5,
   Gate 3.1 — Same category-label problem, plus `third-party` is absent entirely. This is
   the other half of the role title and the whole subject of the job. `DOSSIER.md` records
   `Epic EMR integration` as observed fact read from the DexCare repos, and CV-SPEC lists
   it in the approved DexCare stack. The CV omits Epic EMR completely. Fix: add one
   DexCare bullet that names the third-party API integration work, for example an
   integration with the Epic EMR system, and list `third-party API integrations` in
   Skills. This is the single highest-value change in this report.

3. **Validation of AI-generated code is described but not named** — Gate 1, Gate 2 R19 —
   Lines 26-27 already describe the activity: `lint rules, complexity limits, and testing`
   applied to `AI code agents`. `DOSSIER.md` "AI at DexCare" states the purpose in plain
   words: "so agentic workflows produce high-quality code". Fix: rewrite that bullet so it
   carries the posting's own wording, validation of AI-generated code, and place the term
   in Skills too. No new fact is created. Only the wording changes.

4. **`workflows` appears 5 times** — Gate 2 stuffing, CV-SPEC 3-appearance cap — Costs 5
   points and breaches the cap. Fix: change the ordinary-English uses on line 22
   (`provider-availability workflows`) and line 47 (`administrative workflows`) to another
   word. Keep all three `agentic workflows` hits, which are the scored preferred token P7.

5. **The Summary carries neither domain word** — Gate 3.1, 2 recoverable points — The
   Summary names TypeScript, Node.js, React, Go, event-driven, REST APIs, distributed
   systems, and AWS, but not back-end and not integrations. Fix: work both words into the
   Summary. **Do not touch the title.** `Senior Software Engineer` is fixed by CLAUDE.md
   rule 1 and rule 4.

6. **Only 3 of 11 bullets carry a measured Y** — CV-SPEC XYZ rule, Gate 3.4 sits at the
   bare minimum — Four approved dossier metrics are unused: D2 15% fewer wrong bookings,
   D5 7% lower release risk, D7 33% less friction piloting new clients, L3 18% fewer
   support tickets. Fix: attach at least two of them to existing bullets. D7 is the best
   fit for this posting, because it describes multi-tenant client onboarding.

7. **`Supported` opens 4 of the 11 bullets** — Gate 3, human scan — Lines 25, 28, 41, 47.
   It is also the weakest verb in the set and it makes those bullets read as support work
   rather than ownership. Fix: vary the verbs. Keep past tense, subject omitted.

8. **Role gaps are tight** — Gate 3.8, 2 points — `\resumeRoleGap` is `\vspace{4pt}`. The
   last bullet of a role sits close under the next company name. About 25% of the page is
   unused, so the space exists. Fix: raise the gap.

**Tier B. Blocked on Lucas. Do not write any of these onto the CV until he confirms.**

These nine Gate 1 rows have no support in `DOSSIER.md`. The Architect was right to leave
them out. Writing them now would be invention, which CLAUDE.md rule 4 forbids. Each needs
a yes or no from Lucas, and a dossier entry if yes.

| # | Posting requirement | What to ask Lucas | What is observable today |
|---|---|---|---|
| 9 | `OAuth 2.0` / `OIDC` | Did he implement OAuth 2.0 or OIDC flows, not only consume Auth0? | `DOSSIER.md` records `Auth0` and `multi-tenant JWT` at DexCare. Auth0 is an OIDC provider, but the dossier does not say Lucas built OAuth or OIDC flows. Not observable from the CV or the dossier. |
| 10 | `Webhooks` | Has he built or consumed webhooks? | Nothing in `DOSSIER.md`. Not observable. |
| 11 | `code review` | Confirm the LinkedIn claim into the dossier. | **His own live LinkedIn profile already states it**, under Luizalabs: "Improved code review quality by introducing structured review practices and clearer pull-request documentation, reducing average review cycles from 3–4 rounds to 1–2." Read read-only 2026-09-04. `DOSSIER.md` does not carry it and the Maestro brief lists it as unsupported. This looks like the cheapest of the nine to close, but the dossier is the authorized source for CV content, not the profile text, so the Maestro or Lucas must add it first. This seat does not edit `DOSSIER.md`. |
| 12 | `debugging` | Confirm and give one concrete instance. | Nothing in `DOSSIER.md`. Not observable. |
| 13 | `OOP` | Confirm. | Nothing in `DOSSIER.md`. Not observable. |
| 14 | `SOLID` | Confirm. | Nothing in `DOSSIER.md`. Not observable. |
| 15 | `princípios de software design` | Confirm. | Nothing in `DOSSIER.md`. Not observable. |
| 16 | `comunicação direta com clientes` | Did he communicate directly with external clients, or only with internal stakeholders? | The live LinkedIn Lippaus entry says "working directly with stakeholders to translate business requirements into production software". Stakeholders are not stated to be external clients. `DOSSIER.md` records only "project scoping and stakeholder communication". The distinction decides this row, so it needs Lucas, not an inference. |
| 17 | `AWS SQS` | Has he used SQS? | Nothing in `DOSSIER.md`. `DOSSIER.md` records `RabbitMQ / AMQP` at DexCare and `BullMQ` at Luizalabs and Lippaus. Not a blocking requirement, because the posting writes "como", meaning "such as". Adding SQS would still be the strongest single lift on R13. |

## Match limits

Preferred tokens not placed, all correctly refused as unsupported:
`SAML`, `Microsoft Entra ID`, `Microsoft Graph`, `Google Workspace APIs`, startup
experience, `ERP`, `CRM`, complex platforms. Six of the seven preferred requirements score
zero. Only P7, engineering workflows and standards built with AI, is placed.

Other limits:
- `NestJS` is absent. This is correct and not a defect. The posting writes
  "Express.js/NestJS" as an alternative and `Express` satisfies it.
- `AWS SQS` is absent. Not blocking, since the posting introduces it as an example.
- The posting is written in pt-BR and the recruiter, Noemi Sandrini, is Brazilian. The CV
  is English. That call follows CV-SPEC for an American company and belongs to the
  Maestro. The residual risk is a Portuguese first-pass screen.
- `GCP` is placed in `Skills` and `Experience` but the posting never asks for it. It is
  not scored either way.
