# Quill report: Maxxi, Desenvolvedor(a) Full Stack Sênior (Node.js + React) | Contrato Temporário

Date: 2026-09-04
Task: maxxi-fullstack-senior-quill. Hunt: 2026-09-04-g. Segment: agency. Language: Portuguese only.
Posting: jobs/maxxi-fullstack-senior.md. Manifest: state/maxxi-fullstack-senior-manifest.json.
Base: resumes/base-pt.tex (corrected single-column header, Brazil spelling). Preamble and layout copied unchanged.
Status: written. Not graded. Not submitted. No base edit, no delegation, no outward action.

## Files

- resumes/hunts/2026-09-04-g/maxxi-fullstack-senior/Lucas-Queiroz-Resume-pt.tex
- resumes/hunts/2026-09-04-g/maxxi-fullstack-senior/Lucas-Queiroz-Resume-pt.pdf
- resumes/hunts/2026-09-04-g/maxxi-fullstack-senior/application-note.md
- state/maxxi-fullstack-senior-quill.report.md (this file)
- state/maxxi-fullstack-senior-quill.complete.json (sentinel)

## Changes to the base copy (11 exact-string edits, each matched once)

1. Resumo: `TypeScript, Node.js, React e Go` to `TypeScript, JavaScript, Node.js, React e Go`.
2. Habilidades Backend: added `NestJS (Nest.js)`. Canonical token plus the posting spelling.
3. Habilidades Frontend renamed `Frontend e mobile`: `React | React Native`.
4. Habilidades Cloud e operação: `AWS` to `AWS (S3)`; added `docker-compose` and `Git`.
5. Habilidades: new line `Práticas: Agile (Scrum, Kanban)`.
6. Habilidades Testes e ferramentas de IA: added `prompt engineering`.
7. DexCare bullet 5: `Datadog RUM` to `DataDog RUM`, mirrors the posting spelling once. Skills keeps `Datadog`.
8. DexCare bullet 6: `regras compartilhadas, lint,` to `regras compartilhadas, prompt engineering, lint,`.
9. Luizalabs bullet 1: `Node.js, Java e Go` to `Node.js (Nest.js), Java e Go`. Same placement the P7 application used with `NestJS`.
10. Luizalabs bullet 4: `Docker e Kubernetes` to `Docker, docker-compose e Kubernetes`; added `versionados em Git`. Metric-free bullet, facts otherwise unchanged.
11. Lippaus mid-level bullet 1: `web e mobile sobre PostgreSQL` to `web e mobile em React Native sobre PostgreSQL`. Dossier records Lippaus stack as PostgreSQL / BullMQ / JavaScript / React Native.
12. Lippaus mid-level bullet 3: added `em ciclos Agile (Scrum e Kanban)`.

Untouched: contact block, all titles, dates, company names, locations, degree, Idiomas, all 16 bullets kept, all 7 metrics kept. No protected claim added: `code review` appears nowhere in the tex or note.

## Build and checks

```
tectonic Lucas-Queiroz-Resume-pt.tex    -> exit 0
pdfinfo                                  -> Pages: 2
pdftotext          <pdf> -               -> raw
pdftotext -layout  <pdf> -               -> layout
```

- Raw contact line: `Vitória, ES, Brazil | +55 (27) 99203-0170 | sepulchrolucas@gmail.com | linkedin.com/in/queiroz-lucas | github.com/queirozlc`.
- Headers RESUMO, HABILIDADES, IDIOMAS, EXPERIÊNCIA, FORMAÇÃO present in raw.
- Every employment block survives in raw and layout as company, title, dates, location on consecutive lines, then its bullets.
- Page break falls before the Lippaus entry-level block. Page 2 holds that whole block and the whole Formação block. No block splits.
- Bullets: 16 of 16. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% each present once.
- Titles and dates: DexCare Senior Software Engineer Mar 2026 - Present; Luizalabs Mid-level Software Engineer Jan 2024 - Mar 2026; Lippaus Distribuidora Mid-level Software Engineer Jan 2023 - Jan 2024; Lippaus Distribuidora Entry-level Fullstack Software Engineer Mar 2021 - Jan 2023; FAESA Feb 2022 - Dec 2025. Locations Remoto, Remoto, Vitória, ES, Brazil, Vitória, ES, Brazil.
- `grep -in 'ruby\|rails'` on tex: 0. `grep -ic 'ruby\|rails\|utc\|gmt\|brasil'` on raw: 0. `grep -c workflow` on raw: 2, ligatures disabled.

## Token placement (raw text, word-boundary counts)

Required:

| Token | Habilidades | Experience bullet | Count |
| --- | --- | --- | --- |
| React | Frontend e mobile | DexCare bullet 5; Resumo | 3 standalone (5 with `React Native`) |
| Node.js | Linguagens | Luizalabs bullet 1; Resumo | 3 |
| Nest.js | Backend, as `NestJS (Nest.js)` | Luizalabs bullet 1 | 2 (NestJS 1) |
| JavaScript | Linguagens | Lippaus entry-level bullet 1; Resumo | 3 |
| TypeScript | Linguagens | DexCare bullet 1; Resumo | 3 |
| React Native | Frontend e mobile | Lippaus mid-level bullet 1 | 2 |
| Docker | Cloud e operação | Luizalabs bullet 4 | 2 |
| docker-compose | Cloud e operação | Luizalabs bullet 4 | 2 |
| Git | Cloud e operação | Luizalabs bullet 4 | 2 |
| Agile | Práticas | Lippaus mid-level bullet 3 | 2 |
| Scrum | Práticas | Lippaus mid-level bullet 3 | 2 |
| Kanban | Práticas | Lippaus mid-level bullet 3 | 2 |
| prompt engineering | Testes e ferramentas de IA | DexCare bullet 6 | 2 |

Preferred, placed (dossier-supported): PostgreSQL 3, DataDog 1 + Datadog 1, AWS 3, S3 2, CI/CD 2, Claude Code 2, Codex 2.

Preferred, not placed, no dossier fact: Redux, Metabase, WatermelonDB, SQLite, SQS, GitHub Actions, Clean Architecture, TDD, DDD. Zero occurrences. Listed in the note as not claimed.

At cap (3): React, Node.js, JavaScript, TypeScript, PostgreSQL, AWS, Go, BullMQ.

## Judgment calls for the Maestro

1. `React Native` adds two `React` word hits. Standalone `React` stays at 3. If the Analyzer counts `React Native` toward the `React` cap, the fix is to drop `React` from the Resumo, not from Skills or the DexCare bullet.
2. `Agile`, `Scrum`, `Kanban`, `docker-compose`, and `Git` are posting-derived practice and tool tokens placed under the weight-1 and weight-2 rule. The dossier does not name them. They fit the Lippaus project-scoping bullet and the Luizalabs deploy bullet. Lucas can veto any of them.
3. `Nest.js` follows the P7 precedent (`NestJS` in the Luizalabs Node.js bullet). The dossier records Luizalabs as `Node, Java, and others`.
4. Two pages. All 16 bullets kept; the added Práticas line pushed nothing new across the break beyond what the base already sends to page 2.

## Application note

Full Portuguese recruiter message, Recrutei apply URL as observed, recruiter not observable, screening answers per posting item, explicit unknowns: notice period, PJ rate, availability for temporary or on-demand work, GitHub Copilot, and the nine unplaced preferred tokens. Wording is intent (`pretendo me candidatar`). No submission claimed. Code review is stated as not claimed.

## Open for the Maestro

- Availability for a temporary or on-demand contract, notice period, and PJ rate are not recorded. Lucas answers before sending.
- Not graded here. Deterministic gate and Sieve review are the Maestro's next step.
