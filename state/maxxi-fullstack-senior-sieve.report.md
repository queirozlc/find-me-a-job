# ATS Analysis — resumes/hunts/2026-09-04-g/maxxi-fullstack-senior/Lucas-Queiroz-Resume-pt.pdf vs maxxi-fullstack-senior
Segment: agency   Date: 2026-09-04
Task: maxxi-fullstack-senior-sieve. Analyzer: Sieve. Hunt 2026-09-04-g.
Scope set by Maestro: semantic truth, Role Eligibility Check, full
required and preferred token table, recruiter readability, application-note
inspection. Deterministic gate PASS
(state/maxxi-fullstack-senior-deterministic-gate.json, 2026-09-04T21:22:14+00:00)
is reused as evidence and not re-run. Cached identity only. No portal. No CV
edit. No delegation. No sourcing.

## Verdict
READY

## Decision Explanation
No blocking reason.

Two items stay open before submission. Both are screening answers, not CV
defects. Neither blocks the CV. Silence in the dossier is not a mismatch.

| Item | Posting text | Evidence checked | Evidence found | Classification | Next action |
|---|---|---|---|---|---|
| Temporary and/or on-demand engagement | `Posição estratégica na área de Desenvolvimento de Software, para atuação em projetos de forma temporária e/ou sob demanda, de acordo com as necessidades dos projetos.` and title `Contrato Temporário` | DOSSIER.md Identity and Open questions; application-note.md screening answers | DOSSIER.md records contract types (`PJ with own CNPJ ... All are acceptable`) and `Notice period: Not recorded`. It does not record availability for a temporary or on-demand engagement. application-note.md already prints: `Disponibilidade de Lucas para atuação temporária ou sob demanda: não registrada no dossiê. Lucas confirma antes de enviar.` | Before-submission screening answer. LUCAS CONFIRMATION. Not a CV FIX, not a ROLE MISMATCH. | Lucas confirms availability for temporary or on-demand work before he sends the Recrutei form. No CV change. |
| PJ rate, start date or notice | Posting: `Regime De Contratação Pessoa Jurídica`. No rate, duration, or start date stated | DOSSIER.md Identity; application-note.md | `Notice period: Not recorded`. Note prints both as `não registrada no dossiê. Lucas responde.` | Before-submission screening answer. LUCAS CONFIRMATION. | Lucas answers on the form if asked. No CV change. |

## Inputs read
- ATS-KNOWLEDGE.md, RUBRIC.md, CV-SPEC.md, DOSSIER.md, CLAUDE.md (career
  root), in full.
- state/maxxi-fullstack-senior-review-packet.md (posting, manifest, delta,
  claim manifest, deterministic gate).
- jobs/maxxi-fullstack-senior.md (identical to the packet posting text, diff
  shows only two blank lines).
- state/hunt-2026-09-04-g-linkedin-identity.json (captured
  2026-09-04T20:01:30+00:00, file sha256 10d857f4...8523).
- state/maxxi-fullstack-senior-quill.report.md (Architect claims, checked,
  not trusted).
- state/app-maxxi-fullstack-senior.md (segment and phase only).
- resumes/hunts/2026-09-04-g/maxxi-fullstack-senior/Lucas-Queiroz-Resume-pt.tex,
  Lucas-Queiroz-Resume-pt.pdf, application-note.md.
- resumes/base-pt.tex, diffed against the tailored .tex.
- Extraction, run by me on the tailored PDF:
  `pdftotext <pdf> -` (raw, 76 lines, 2 form feeds) and
  `pdftotext -layout <pdf> -` (layout). All File Readability and Resume
  Evidence judgements are on the raw file.

## File Readability Check

Deterministic gate rows `pdf_extraction`, `sections`, `contact`, `layout`,
`roles` are PASS. Rows below cite my own extraction as the evidence.

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction 76 lines, 2 pages, producer xdvipdfmx, Roboto CID fonts embedded with ToUnicode (`pdffonts` uni=yes on all 4 fonts) |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes, 0 `?`, 0 code points in U+FB00-FB06. `workflow` 2 hits, `office` 2 hits (`backoffice`), `fluxo` 3 hits, all intact. `profile`, `efficient`, `conflict` absent from the text, not testable. Tex line 16 `\defaultfontfeatures{Ligatures=NoCommon}` |
| 0.3 | Contact block recoverable | PASS | Raw line 3, body text: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc` |
| 0.4 | Section headers verbatim | PASS | Standalone raw lines 5 `RESUMO`, 11 `HABILIDADES`, 21 `IDIOMAS`, 24 `EXPERIÊNCIA`, 71 `FORMAÇÃO`. PT allowlist |
| 0.5 | Employment-block segmentation | PASS | 4 role blocks, each company / title / dates / location on 4 consecutive raw lines (25-28, 42-45, 54-57, 64-67), then its bullets, 7 / 4 / 3 / 2. No merge, no split. Form feed falls at raw line 64 `Lippaus Distribuidora`; page 2 opens with the full Entry-level header, both bullets, then Formação |
| 0.6 | Date parseability | PASS | `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`, ASCII hyphen, each on the line directly after its title. 0 EN DASH characters in raw |
| 0.7 | Reading order | PASS | Raw and layout extraction, form feeds removed and whitespace normalized, are line-for-line identical (`diff` empty) |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` empty. Tex has 0 hits for `tabular`, `minipage`, `parbox`, `includegraphics`, `fancyhdr`, `multicol`, `tcolorbox`, icon fonts |

## Semantic truth

### Titles, dates, employers, locations against the LinkedIn cache

Each string searched verbatim in the cached snapshot text and in the raw
extraction.

| Company (CV raw) | Title (CV raw) | Dates (CV raw) | Location (CV raw) | In cache |
|---|---|---|---|---|
| DexCare | Senior Software Engineer | Mar 2026 - Present | Remoto | yes (`Remote`, city not printed per DOSSIER) |
| Luizalabs | Mid-level Software Engineer | Jan 2024 - Mar 2026 | Remoto | yes |
| Lippaus Distribuidora | Mid-level Software Engineer | Jan 2023 - Jan 2024 | Vitória, ES, Brazil | yes (`Vitória`, On-site) |
| Lippaus Distribuidora | Entry-level Fullstack Software Engineer | Mar 2021 - Jan 2023 | Vitória, ES, Brazil | yes |

Education: the cache does not contain `FAESA` or `Information Systems`.
Checked against DOSSIER.md LinkedIn ground truth: `FAESA`,
`Information Systems`, `Feb 2022 – Dec 2025`. CV prints `FAESA` /
`Bacharelado em Sistemas de Informação` / `Feb 2022 - Dec 2025` /
`Vitória, ES, Brazil`. Months identical, ASCII hyphen per CLAUDE.md rule 1
clarification. Deterministic gate `linkedin_identity` PASS agrees.

### Metrics
Raw extraction, in order: 15%, 25%, 7%, 33%, 20%, 18%, 26%. Seven, each
once. Match DOSSIER.md D2, D3, D5, D7, L2, L3, P2. Other numbers:
`mais de 5 anos` (Mar 2021 to Sep 2026 is 5 years 6 months) and
`AWS SDK v3`. Tex diff against resumes/base-pt.tex shows every metric
unchanged.

### Content delta against the base, fact by fact
Tex diff: 9 hunks, all rewording or token insertion. 16 bullets in base and
tailored (raw count 7 + 4 + 3 + 2). No bullet removed. No metric changed.

| Change | Source of the underlying fact | Judgement |
|---|---|---|
| Resumo adds `JavaScript` | DOSSIER: JavaScript at Lippaus (approved bullets) | True |
| Skills Backend adds `NestJS (Nest.js)` | DOSSIER does not name NestJS at any employer. Match policy weight 3, exact posting term | Allowed by policy. See defect 1 |
| Skills `Frontend` to `Frontend e mobile: React \| React Native` | DOSSIER: Lippaus stack `PostgreSQL / BullMQ / JavaScript / React Native` | True |
| Skills `AWS` to `AWS (S3)`; adds `docker-compose`, `Git` | DOSSIER: S3 via AWS SDK v3 at DexCare. `docker-compose` and `Git` not named at any employer. Weight 2 tools, exact posting terms | `AWS (S3)` true. `docker-compose`, `Git` allowed by policy. See defect 1 |
| Skills new line `Práticas: Agile (Scrum, Kanban)` | DOSSIER does not name Agile, Scrum, or Kanban. Weight 1 practice, exact posting terms | Allowed by policy. See defect 1 |
| Skills adds `prompt engineering` | DOSSIER: built Claude Code and Codex agent environments with shared rules | Supported in substance. Literal term not in DOSSIER. Low risk |
| DexCare bullet 5 `Datadog RUM` to `DataDog RUM` | Posting spelling. Vendor and DOSSIER spell `Datadog`. Skills keeps `Datadog` | True. Two spellings on one CV. See defect 4 |
| DexCare bullet 6 adds `prompt engineering` | Same as Skills row | Supported in substance |
| Luizalabs bullet 1 `Node.js` to `Node.js (Nest.js)` | DOSSIER: `Stack: Node, Java, and others`. LinkedIn cache: Node.js and Java. `Nest.js` not named | Allowed by match policy weight 3. See defect 1 |
| Luizalabs bullet 4 adds `docker-compose`, `versionados em Git`, rewords to `mantidos confiáveis` | DOSSIER: Docker, Kubernetes, GCP, ArgoCD at Luizalabs. `docker-compose` and `Git` not named | Allowed by policy weight 2. See defect 1 |
| Lippaus Mid bullet 1 adds `em React Native` | DOSSIER: Lippaus stack includes React Native; `multi-tenant web and mobile platform` approved | True |
| Lippaus Mid bullet 3 adds `em ciclos Agile (Scrum e Kanban)` | DOSSIER: project scoping and stakeholder communication approved. Agile, Scrum, Kanban not named | Allowed by policy weight 1. See defect 1 |

Stack and banned content: 0 hits in raw for `ruby`, `rails`, `sidekiq`,
`rspec`, `UTC`, `GMT`, `fuso`, `code review`, `Brasil`, `Responsáv`.
Deterministic gate `forbidden_terms` and `claim_allowlist` PASS agree.
`RabbitMQ` and `AMQP` appear in Skills only, as DOSSIER prescribes.

Carried over from the approved base, unchanged, already recorded in
state/hunt-2026-09-04-g-base-sieve.report.md: Summary clause
`para uma empresa dos EUA` and `Present` in the PT date line (LinkedIn
verbatim). No new finding.

### Application note (resumes/hunts/2026-09-04-g/maxxi-fullstack-senior/application-note.md)
Draft, not a sent message. Read in full.

- No false submission. Status line: `RASCUNHO. Lucas envia. Nenhum agente
  envia. Nenhuma candidatura foi enviada.` Message body: `pretendo me
  candidatar pela página da Recrutei`. No sentence states that a submission
  occurred. Correct.
- Personal claims traced to DOSSIER.md: Senior Software Engineer, more than
  5 years (Mar 2021 to today); PJ with own CNPJ, CLT and EOR acceptable
  (Identity); 100% remote from Vitória, ES, Brazil; `Fuso GMT-3` in
  screening answers only, not on the CV (CLAUDE.md 3); English
  `Fluente (C1)`; 33% SPI (D7); 20% SEFAZ (L2); 26% Lippaus (P2); 7% feature
  flags (D5); React with Datadog RUM, Auth0 JWT, OpenAPI/Swagger, PostgreSQL
  with Sequelize and Drizzle ORM, DynamoDB, Redis, S3 and RDS (seeded DexCare
  data); React Native at Lippaus; Claude Code and Codex daily use.
- Unknowns printed as unknown, not answered: temporary or on-demand
  availability, start date or notice, PJ rate, Recrutei form questions,
  GitHub Copilot, nine unplaced preferred tokens, code review. Correct.
- Three screening-answer claims go past what DOSSIER.md records. None is on
  the CV. Lucas should confirm each before he types it into the form:
  `Node.js também ... na Lippaus` (DOSSIER records BullMQ and JavaScript at
  Lippaus, not the literal `Node.js`); `TypeScript e JavaScript na Luizalabs
  e na Lippaus` (DOSSIER records `Node, Java, and others` at Luizalabs and
  JavaScript at Lippaus, not TypeScript at either); `código versionado em
  Git em todos os empregadores` (DOSSIER does not name Git). See defect 3.
- Same `Nest.js` at Luizalabs and `Agile (Scrum e Kanban)` at Lippaus
  wording as the CV. Defect 1 applies to the note too.

## Role Eligibility Check

| Check | Source (posting text) | Result |
|---|---|---|
| Work authorization / entity type | `Regime De Contratação Pessoa Jurídica` | PASS. DOSSIER.md Identity: `PJ with own CNPJ ... All are acceptable`. Note states PJ with own CNPJ |
| Location or time-zone overlap | Header `Brazil` and `Remote`. No city or time zone stated | PASS. Candidate in Vitória, ES, Brazil, remote. Time-zone overlap: not stated |
| Engagement type | `atuação em projetos de forma temporária e/ou sob demanda` | Open, screening answer. Not a CV field. DOSSIER silent on availability. LUCAS CONFIRMATION before submission. Not FAIL, not ROLE MISMATCH. See Decision Explanation |
| Minimum years of experience | `sólida experiência`, `Sênior`. No number stated | not stated |
| English proficiency requirement | not stated | not stated |
| Degree requirement | not stated | not stated |
| Each required skill | `Requisitos e qualificações` list | See Resume Evidence Check. All 13 manifest tokens present verbatim in Skills and Experience. `Experiência com banco de dados relacional` is met by `PostgreSQL` in Skills (Dados) and in DexCare bullet 4 and Lippaus Mid bullet 1; the literal word `relacional` is absent, see Match limits |

No FAIL row.

## Resume Evidence Check: 84/100, PASS

Required set is the manifest's 13 tokens from `Requisitos e qualificações`,
weight 3. Preferred set is the manifest's 16 tokens from `Diferenciais`,
weight 1. Posting phrases that are categories or soft descriptions
(`banco de dados relacional`, `arquitetura`, `segurança`, `performance`,
`debugging`, `caching`, `unit testing`, `GitHub Copilot` as one of three
examples) are not scored; see Match limits.

Counts are word-boundary matches on the raw extraction, case-insensitive.
Sections by header line.

| Token | Weight | Skills | Experience (bullet) | Resumo | Total count | Placement | Points |
|---|---|---|---|---|---|---|---|
| React | required 3 | Frontend e mobile | DexCare bullet 5 `monitoração React no DataDog RUM` | 1 | 3 standalone (5 counting `React Native`) | Skills + Experience | 3 |
| Node.js | required 3 | Linguagens | Luizalabs bullet 1 `microsserviços fiscais distribuídos em Node.js (Nest.js)` | 1 | 3 | Skills + Experience | 3 |
| Nest.js | required 3 | Backend `NestJS (Nest.js)` | Luizalabs bullet 1 | 0 | 2 (`NestJS` 1 more) | Skills + Experience | 3 |
| JavaScript | required 3 | Linguagens | Lippaus Entry bullet 1 `dashboards internos de backoffice em JavaScript` | 1 | 3 | Skills + Experience | 3 |
| TypeScript | required 3 | Linguagens | DexCare bullet 1 `serviços TypeScript orientados a eventos` | 1 | 3 | Skills + Experience | 3 |
| React Native | required 3 | Frontend e mobile | Lippaus Mid bullet 1 `plataforma multi-tenant web e mobile em React Native` | 0 | 2 | Skills + Experience | 3 |
| Docker | required 3 | Cloud e operação | Luizalabs bullet 4 `Implantei serviços com Docker, docker-compose e Kubernetes` | 0 | 2 | Skills + Experience | 3 |
| docker-compose | required 3 | Cloud e operação | Luizalabs bullet 4 | 0 | 2 | Skills + Experience | 3 |
| Git | required 3 | Cloud e operação | Luizalabs bullet 4 `versionados em Git` | 0 | 2 | Skills + Experience | 3 |
| Agile | required 3 | Práticas | Lippaus Mid bullet 3 `em ciclos Agile (Scrum e Kanban)` | 0 | 2 | Skills + Experience | 3 |
| Scrum | required 3 | Práticas | Lippaus Mid bullet 3 | 0 | 2 | Skills + Experience | 3 |
| Kanban | required 3 | Práticas | Lippaus Mid bullet 3 | 0 | 2 | Skills + Experience | 3 |
| prompt engineering | required 3 | Testes e ferramentas de IA | DexCare bullet 6 `regras compartilhadas, prompt engineering, lint` | 0 | 2 | Skills + Experience | 3 |
| Redux | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| PostgreSQL | preferred 1 | Dados | DexCare bullet 4; Lippaus Mid bullet 1 | 0 | 3 | Skills + Experience | 3 |
| Metabase | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| DataDog | preferred 1 | Cloud e operação (`Datadog`) | DexCare bullet 5 (`DataDog RUM`) | 0 | 2 | Skills + Experience | 3 |
| WatermelonDB | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| SQLite | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| AWS | preferred 1 | Cloud e operação `AWS (S3)` | DexCare bullet 4 `via AWS SDK v3` | 1 | 3 | Skills + Experience | 3 |
| S3 | preferred 1 | Cloud e operação | DexCare bullet 4 `ligados a S3 e RDS` | 0 | 2 | Skills + Experience | 3 |
| SQS | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| GitHub Actions | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| CI/CD | preferred 1 | Cloud e operação | Luizalabs bullet 4 `gate do CI/CD` | 0 | 2 | Skills + Experience | 3 |
| Clean Architecture | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| TDD | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| DDD | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| Claude Code | preferred 1 | Testes e ferramentas de IA | DexCare bullet 6 | 0 | 2 | Skills + Experience | 3 |
| Codex | preferred 1 | Testes e ferramentas de IA | DexCare bullet 6 | 0 | 2 | Skills + Experience | 3 |

Required: 13 tokens × 3 points × weight 3 = 117 of 117.
Preferred: 7 tokens × 3 points = 21 of 48 (16 tokens × 3).
coverage = 100 × (117 + 21) / (117 + 48) = 83.6, reported 84.

Stuffing penalty: 0. Highest standalone count of any token is 3 (React,
Node.js, JavaScript, TypeScript, PostgreSQL, AWS, Go, BullMQ, multi-tenant).
Judgement call, stated openly: the word `React` occurs 5 times when the two
`React Native` occurrences are included. The penalty models a human
reaction, and a reader sees `React Native` as a distinct product, so I count
standalone `React` (3) and apply no penalty. If the Maestro prefers the
strict count, subtract 5 (score 79) and the fix is to drop `React` from the
Resumo only, as Quill's report also proposes. Deterministic gate
`required_token_placement` PASS agrees with the placement table.

Required tokens without Skills and Experience placement: none.

## Recruiter Readability Score: 89/100

Target title is the posting title `Desenvolvedor(a) Full Stack Sênior
(Node.js + React)`. Relevance for 3.2 is judged against the
`Requisitos e qualificações` list.

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in top 15% | 10/15 | Raw line 6 of 76 (8%) carries `Senior Software Engineer` and `sistemas backend e fullstack`. The posting phrase `Full Stack` (two words) and `Desenvolvedor` do not appear. Job titles are LinkedIn-locked (CLAUDE.md rule 1), so only the Summary could carry it. Partial credit |
| 3.2 | 3 most relevant bullets first in most recent role | 16/20 | DexCare bullets 1-3: TypeScript event-driven services on Express and Koa, Epic EMR integration 15%, REST APIs multi-tenant with Auth0 JWT 25%. Bullet 1 maps to `Node.js` and `JavaScript / TypeScript`; bullets 2-3 map to the posting's `arquitetura de software, segurança, performance` line. The posting's first requirement is `React`; the React bullet is 5th and the `prompt engineering` bullet is 6th. A reorder, no content change, would put React or the AI bullet in the first 3 |
| 3.3 | Past-tense action verb and outcome | 13/15 | All 16 bullets open with a first-person past-tense verb, subject omitted: Construí ×7, Integrei, Modelei, Reduzi, Ajudei a implementar, Migrei, Implantei, Processei, Liderei, Desenvolvi. 0 hits for `Responsável`, present-tense duty lists, third person. Two bullets state no outcome: D4 `Modelei leituras e escritas ... via AWS SDK v3` and E2 `Construí funcionalidades para clientes de ponta a ponta ...`. Same as the base finding; DOSSIER says leave as is |
| 3.4 | At least 3 bullets with a real number | 15/15 | 7 bullets, all numbers traced to DOSSIER.md |
| 3.5 | Experience completeness | 10/10 | 4 roles, 16 bullets, 7 metrics, identical set to base-pt.tex (tex diff shows rewording and token insertion only). 2 pages; page 2 holds the whole Lippaus Entry-level block and Formação, no split block |
| 3.6 | No unsupported buzzwords | 10/10 | 0 hits for team player, results-driven, passionate, apaixonado, proativo, senso de dono, dinâmico, sinergia |
| 3.7 | Skills grouped by category | 10/10 | 7 labelled groups: Linguagens, Backend, Dados, Frontend e mobile, Cloud e operação, Práticas, Testes e ferramentas de IA |
| 3.8 | Scannable | 5/5 | Bold company, italic title and location, consistent role gap, single column, clean page break before a full role header |

## Defects, ranked by cost
No blocking defect. Non-blocking, in order:

1. Posting-derived tokens not recorded in DOSSIER.md at the employer where
   they are placed — semantic truth — `Nest.js` at Luizalabs (bullet 1 and
   Skills), `docker-compose` and `Git` at Luizalabs (bullet 4 and Skills),
   `Agile (Scrum e Kanban)` at Lippaus (Mid bullet 3 and Skills). All are
   allowed by the DOSSIER match policy (framework weight 3, tool weight 2,
   practice weight 1, exact posting terms) and CLAUDE.md rule 4, so no fix is
   required. Recorded so Lucas sees them before he sends. If Lucas vetoes any
   term, the Architect removes it from both placements and the Maestro
   reclassifies that token, because each is required in the manifest and its
   removal would fail the Resume Evidence Check as written. Quill's report
   already lists the same veto option.
2. React bullet is 5th and AI bullet is 6th in DexCare — Recruiter
   Readability 3.2 — move DexCare bullet 5 (`Reduzi o risco de releases em
   7% ... monitoração React no DataDog RUM.`) or bullet 6 (`Construí
   ambientes Claude Code e Codex ...`) into the first 3. Reorder only, no
   text change. Optional.
3. Three screening answers in application-note.md go past the dossier —
   application note, not CV — `Node.js também ... na Lippaus`, `TypeScript e
   JavaScript na Luizalabs e na Lippaus`, `código versionado em Git em todos
   os empregadores`. Lucas confirms each fact before he types it into the
   Recrutei form, or the Architect trims the answer to what DOSSIER.md
   records: Node.js at DexCare and Luizalabs; TypeScript at DexCare,
   JavaScript at Lippaus; Git at Luizalabs (as on the CV). LUCAS
   CONFIRMATION. No CV change.
4. Two spellings of one vendor on one CV — Recruiter Readability, cosmetic —
   Skills prints `Datadog`, DexCare bullet 5 prints `DataDog RUM`. Both
   satisfy the token check case-insensitively. Optional: choose one
   spelling. If the posting spelling is kept, change Skills `Datadog` to
   `DataDog`; if the vendor spelling is kept, change the bullet back to
   `Datadog RUM`. Lucas decision.
5. Target title phrase absent from the Summary — Recruiter Readability 3.1 —
   Summary line 6 says `sistemas backend e fullstack`. The posting also asks
   for mobile, which the Summary does not mention although DOSSIER records
   React Native at Lippaus. Optional Architect wording: `Eu sou Senior
   Software Engineer e desenvolvedor full stack com mais de 5 anos
   construindo sistemas backend, fullstack e mobile em ...`. No title,
   date, or metric touched. Lucas decision.
6. D4 and E2 carry no outcome — Recruiter Readability 3.3 — inherited from
   the base; DOSSIER says leave as is. No action.

## Before submission (not CV defects)
- Temporary or on-demand availability: Lucas confirms. DOSSIER and note are
  silent; the note already flags it. See Decision Explanation.
- PJ rate, start date or notice: not recorded, Lucas answers, as the note
  states.
- Defect 3 screening answers: Lucas confirms before typing.

## Match limits
- `Redux`, `Metabase`, `WatermelonDB`, `SQLite`, `SQS`, `GitHub Actions`,
  `Clean Architecture`, `TDD`, `DDD`: not placed. DOSSIER does not record
  them. Note lists them as not claimed. Correct.
- `banco de dados relacional` / `relacional`: literal word absent. The
  requirement is met by `PostgreSQL` in Skills and two Experience bullets.
  Optional weight-1 wording, as the P7 CV did: Skills label
  `Dados (relacionais)`. Not required.
- `arquitetura`, `segurança`, `performance`, `testes` (as a noun),
  `debugging`, `caching`, `unit testing`: literal words absent or Skills
  only (`Testes` label, `testes` in DexCare bullet 6). Related evidence
  exists (multi-tenant SPI, Auth0 JWT, Vitest and Jest gate, Datadog
  monitoring) but not the posting's words. Weight 1 practice terms.
- `GitHub Copilot`: not placed. DOSSIER records Claude Code and Codex only.
  Note says so.
- `mobile`: Skills label and Lippaus Mid bullet 1. Absent from the Summary.
  See defect 5.

## Not done
- No CV edit, no note edit, no delegation, no portal, no sourcing, no re-run
  of the deterministic gate.
