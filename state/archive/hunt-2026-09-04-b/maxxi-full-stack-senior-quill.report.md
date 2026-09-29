# Quill task result: maxxi-full-stack-senior

Role: Resume Architect. Wrote and built. Did not grade.
Date: 2026-09-04
Hunt: 2026-09-04-b
Application: Maxxi, Desenvolvedor(a) Full Stack Sênior (Node.js + React), Contrato Temporário, Brazil, Remote, Pessoa Jurídica
Posting: `jobs/maxxi-full-stack-senior.md`, https://www.linkedin.com/jobs/view/4463149985/
Language: Portuguese. Base: `resumes/base-pt.tex`, not edited.

## Files written

- `resumes/hunts/2026-09-04-b/maxxi-full-stack-senior/Lucas-Queiroz-Resume-pt.tex`
- `resumes/hunts/2026-09-04-b/maxxi-full-stack-senior/Lucas-Queiroz-Resume-pt.pdf`
- `resumes/hunts/2026-09-04-b/maxxi-full-stack-senior/application-message.md`
- this report

No other file was touched. No base CV was edited. No subagent was spawned. No Maestri message was sent. No ledger or note was edited. No application was submitted.

## Changes from base-pt.tex

Structure:
1. Role header changed from the base `tabular*` two-column macro to a single-column macro: company, title, then `Location | Dates` on consecutive lines. Reason: the Resume Architect role file and CV-SPEC item 2 forbid `tabular*`. Raw extraction shows each role as one block.
2. Spacing tightened to fit one page with all content: `\titlespacing` 2pt/1pt, header `\vspace{1pt}`, role gap 1pt, `\topmargin` -0.65in, `\textheight` +1.3in. Top and bottom margins are about 0.35in. Rendered page inspected: no clipping, no overlap.

Summary (first person with `Eu`):
- `sistemas backend e fullstack` changed to `produtos web e mobile`, mirroring the posting's `produtos web e mobile`.
- Added `com arquitetura de software, segurança, performance e testes` after the DexCare clause. All four are posting terms. Supported by DOSSIER: event-driven booking design, SPI multi-tenant architecture, Auth0 multi-tenant JWT isolation, throughput and release metrics, Vitest and Jest suites.
- Dropped `para uma empresa dos EUA` and shortened the AI sentence to `Eu integro fluxos agênticos com IA no desenvolvimento diário.` to fit one page. The AI mention stays.

Skills (Habilidades):
- `Dados`: added `banco de dados relacional` before `PostgreSQL`.
- `Frontend` renamed `Frontend e mobile`: `React | React Native`.
- `Cloud e operação`: added `S3`, `Git`; `Datadog` spelled `DataDog` here to mirror the posting once. Bullet keeps canonical `Datadog`.
- New `Práticas` line: `arquitetura de software | segurança | performance | testes unitários (unit testing) | Vitest | Jest`.
- `Testes e ferramentas de IA` renamed `Ferramentas de IA`: `Claude Code | Codex | Agentic workflows | prompt engineering`.

Experience, all roles, bullets, and metrics preserved (7 DexCare, 4 Luizalabs, 3 Lippaus Mid, 2 Lippaus Entry). Reworded bullets, facts unchanged:
- DexCare Auth0 bullet: `isolaram dados` changed to `isolaram dados com segurança`. Metric 25% unchanged.
- DexCare data bullet: `em PostgreSQL` changed to `no banco de dados relacional PostgreSQL`.
- DexCare flags bullet: `monitoração React no Datadog RUM` changed to `monitoração de performance do frontend React no Datadog RUM`. Metric 7% unchanged.
- DexCare AI bullet: `com regras compartilhadas` changed to `com prompt engineering de regras compartilhadas`. Basis: DOSSIER AI at DexCare entry, shared rules for Claude Code and Codex agents.
- Luizalabs deploy bullet: `Implantei serviços com Docker` changed to `Implantei serviços versionados em Git com Docker`; `suítes Vitest e Jest` changed to `suítes de testes unitários Vitest e Jest`.
- Lippaus Mid platform bullet: `plataforma multi-tenant web e mobile sobre PostgreSQL` changed to `plataforma multi-tenant web e mobile em React Native sobre PostgreSQL`. Basis: DOSSIER Lippaus stack `PostgreSQL / BullMQ / JavaScript / React Native`, approved bullet `multi-tenant web and mobile platform on PostgreSQL`.

## Required posting tokens

| Token | Skills | Experience bullet | Basis |
|---|---|---|---|
| React | yes | DexCare flags bullet | DOSSIER DexCare frontend |
| Node.js | yes | Luizalabs microservices bullet | DOSSIER |
| Nest.js | no | no | Not in DOSSIER. DexCare web frameworks are Express and Koa. Reported, not added. |
| JavaScript | yes | Lippaus Entry dashboards bullet | DOSSIER |
| TypeScript | yes | DexCare services bullet | DOSSIER |
| React Native | yes | Lippaus Mid platform bullet | DOSSIER Lippaus stack |
| Docker | yes | Luizalabs deploy bullet | DOSSIER tools |
| docker-compose | no | no | Not in DOSSIER. Reported, not added. |
| Git | yes | Luizalabs deploy bullet | Weak basis: DOSSIER records no `Git` token. Support is the GitHub profile in the base contact block and DexCare repos on disk carrying `.git`. Maestro may strike it. |
| banco de dados relacional | yes | DexCare data bullet | DOSSIER PostgreSQL |
| Agile, Scrum, Kanban | no | no | Not in DOSSIER. Reported, not added. |
| prompt engineering | yes | DexCare AI bullet | DOSSIER: built agent environments with shared rules for Claude Code and Codex. Maestro may judge this a stretch. |
| arquitetura de software | yes | Summary only | No bullet placement. Supported conceptually by DOSSIER event-driven and SPI work. |
| segurança | yes | DexCare Auth0 bullet | DOSSIER Auth0 multi-tenant JWT |
| performance | yes | DexCare flags bullet | DOSSIER metrics |
| testes | yes | Luizalabs deploy bullet, DexCare AI bullet | DOSSIER Vitest, Jest |
| code review | no | no | Not in DOSSIER. Reported, not added. |

## Preferred posting tokens

Placed: PostgreSQL, DataDog/Datadog, AWS, S3, CI/CD, unit testing (as `testes unitários (unit testing)`), Claude Code, Codex.
Not placed, not in DOSSIER: Redux, Metabase, WatermelonDB, SQLite, SQS, GitHub Actions, Clean Architecture, TDD, DDD, debugging, caching, GitHub Copilot. `AWS Cloud` phrase not mirrored; canonical `AWS` used.

## Verification

- `tectonic Lucas-Queiroz-Resume-pt.tex`: exit 0. Warnings only for Roboto italic font shape, same as base.
- `pdfinfo`: 1 page.
- `pdftotext` raw and `pdftotext -layout` run. Contact line intact: `Vitória, ES, Brasil`, phone, email, LinkedIn, GitHub, in the body. Headers extract as `RESUMO`, `HABILIDADES`, `IDIOMAS`, `EXPERIÊNCIA`, `FORMAÇÃO` in source order (uppercase from `\scshape`, same as base). Raw and layout agree on block order. Four employment blocks and one education block, each one block with company, title, location, dates. 10 blank lines in raw, one at each block boundary.
- Titles character for character from DOSSIER LinkedIn ground truth: `Senior Software Engineer`, `Mid-level Software Engineer`, `Mid-level Software Engineer`, `Entry-level Fullstack Software Engineer`.
- Dates in raw: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. ASCII hyphen.
- Locations: DexCare and Luizalabs `Remoto`; Lippaus and FAESA `Vitória, ES, Brasil`, as in base-pt.
- Metrics present: 15%, 25%, 7%, 33%, 20%, 18%, 26%. No bullet deleted.
- `grep -ic 'ruby\|rails'` on tex, raw, layout: 0, 0, 0. `UNVERIFIED`: 0. UTC, GMT, fuso: 0.
- Ligatures: `workflow` extracts 2 times, no fi/fl glyphs.
- Raw term counts: TypeScript 3, Node.js 3, JavaScript 2, React (exact word) 3, React Native 2, React substring total 5, Docker 2, Git 2 (plus `github` in contact), PostgreSQL 3, banco de dados relacional 2, prompt engineering 2, CI/CD 2, Datadog/DataDog 2, Claude Code 2, Codex 2, AWS 3, S3 2, arquitetura de software 2, segurança 3, performance 3, testes 4, unit testing 1, agentic workflows 2, Vitest 2, Jest 2, BullMQ 3.
- Two counts exceed 3 only under substring counting: `React` (5, of which 2 are inside `React Native`) and the common word `testes` (4). Exact-term counts are within the cap. Flagged for the Analyzer.

## Open for the Maestro

1. `Git` and `prompt engineering` are the two placements with the thinnest DOSSIER basis. Strike either on request; the page still fits.
2. Unsupported required tokens: Nest.js, docker-compose, Agile, Scrum, Kanban, code review. Not added. Lucas can confirm them for a fix round.
3. The message and screening answers state PJ with own CNPJ, remote from Vitória, Portuguese native, English C1. Notice period and salary expectation are not in the dossier and are left for Lucas.
