# Quill report: P7 Group, Desenvolvedor(a) Full Stack

Date: 2026-09-04
Hunt: 2026-09-04-g. Segment: br-pj. Language: Portuguese only.
Posting: jobs/p7-group-fullstack.md (LinkedIn feed post, age 3 h, applicant count not observable). Apply form: https://forms.gle/jKppKShQBUXurieu7
Manifest: state/p7-group-fullstack-manifest.json. Required tokens: JavaScript, TypeScript, Node.js, NestJS, React, APIs REST, webhooks, LLMs, RAG. Preferred: none.
Status: written, PDF built, two pages. Not graded. Not submitted. No delegation, no maestri ask.

## Files

- /Users/lucasqueiroz/career/resumes/hunts/2026-09-04-g/p7-group-fullstack/Lucas-Queiroz-Resume-pt.tex
- /Users/lucasqueiroz/career/resumes/hunts/2026-09-04-g/p7-group-fullstack/Lucas-Queiroz-Resume-pt.pdf
- /Users/lucasqueiroz/career/resumes/hunts/2026-09-04-g/p7-group-fullstack/application-note.md
- /Users/lucasqueiroz/career/state/p7-group-fullstack-quill.report.md (this file)
- /Users/lucasqueiroz/career/state/p7-group-fullstack-quill.complete.json (sentinel)

Base resumes/base-pt.tex not touched. Preamble (lines 1-52) and every resumeSubheading block identical to the base, confirmed with diff.

## Edits to the base copy, eleven in total

1. Resumo: `TypeScript, Node.js, React e Go` to `TypeScript, JavaScript, Node.js, React e Go`.
2. Resumo: `fluxos agênticos com IA` to `fluxos agênticos com IA e LLMs`.
3. Habilidades Backend: label `Backend e mensageria`; added `NestJS`, `webhooks`; `REST APIs` to posting spelling `APIs REST`.
4. Habilidades Dados: label `Dados (relacionais e não relacionais)`. Tokens unchanged.
5. Habilidades Cloud: label `Cloud, deploy e observabilidade`. Tokens unchanged.
6. Habilidades Testes: label `Testes e IA aplicada`; added `LLMs`, `RAG`, `integrações com modelos`.
7. DexCare bullet 3: `REST APIs multi-tenant` to `APIs REST multi-tenant`. Metric 25% unchanged.
8. DexCare bullet 4: added `em bancos relacionais e não relacionais,` before the PostgreSQL/DynamoDB/Redis list. No metric in this bullet.
9. DexCare AI bullet: `Claude Code e Codex com regras compartilhadas` to `Claude Code e Codex, com LLMs e contexto RAG sobre regras compartilhadas`. Same agent-workflow context, same outcome. No RAG product, no new result.
10. Luizalabs bullet 1: `em Node.js, Java e Go` to `em Node.js (NestJS), Java e Go`. Outcome unchanged.
11. Luizalabs bullet 2: `para filas BullMQ assíncronas` to `para mensageria e processamento assíncrono em filas BullMQ`. Metric 20% unchanged.
12. Lippaus bullet 2: `integrações com 26%` to `integrações com terceiros via webhooks com 26%`. Metric unchanged.

Ecosystem tokens NestJS, webhooks, LLMs, RAG placed under AGENTS.md section 4 and the DOSSIER.md match policy. No claim-status marker. Next.js and Vite not added; React covers the posting's `React, Next.js ou Vite` line. No code-review claim. No fintech, nutraceutical, or direct-response claim. No new number.

## Build and checks

```
tectonic Lucas-Queiroz-Resume-pt.tex
pdfinfo  -> Pages: 2
pdftotext Lucas-Queiroz-Resume-pt.pdf -
pdftotext -layout Lucas-Queiroz-Resume-pt.pdf -
```

- Page count 2. Only the Formação block (FAESA) falls on page 2. Brief allows two pages and says not to force one.
- Headers RESUMO, HABILIDADES, IDIOMAS, EXPERIÊNCIA, FORMAÇÃO present in the raw extraction. Each employment block survives as one block: company, title, dates, location.
- Bullets 16 of 16. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% all present.
- `grep -ic 'ruby\|rails'` on .tex and raw text: 0.
- `grep -ic 'utc\|gmt\|code review'` on raw text: 0.
- `grep -c workflow` on raw text: 2, ligatures disabled.
- Titles, dates, companies, locations identical to base-pt.tex and to state/hunt-2026-09-04-g-linkedin-identity.json: DexCare Senior Software Engineer Mar 2026 - Present; Luizalabs Mid-level Software Engineer Jan 2024 - Mar 2026; Lippaus Distribuidora Mid-level Software Engineer Jan 2023 - Jan 2024; Lippaus Distribuidora Entry-level Fullstack Software Engineer Mar 2021 - Jan 2023; FAESA Feb 2022 - Dec 2025.

## Token placement (raw text, word-boundary counts)

| Token | Skills | Experience bullet | Count |
| --- | --- | --- | --- |
| JavaScript | Linguagens | Lippaus entry-level bullet 1; Resumo | 3 |
| TypeScript | Linguagens | DexCare bullet 1; Resumo | 3 |
| Node.js | Linguagens | Luizalabs bullet 1; Resumo | 3 |
| NestJS | Backend e mensageria | Luizalabs bullet 1 | 2 |
| React | Frontend | DexCare bullet 5; Resumo | 3 |
| APIs REST | Backend e mensageria | DexCare bullet 3 | 2 |
| webhooks | Backend e mensageria | Lippaus mid-level bullet 2 | 2 |
| LLMs | Testes e IA aplicada | DexCare AI bullet; Resumo | 3 |
| RAG | Testes e IA aplicada | DexCare AI bullet | 2 |
| Go, BullMQ, PostgreSQL | | | 3 each, at cap |

Posting practice phrases mirrored once each: `relacionais e não relacionais` (Skills label and DexCare bullet 4), `mensageria e processamento assíncrono` (Skills label and Luizalabs bullet 2), `deploy e observabilidade` (Skills label), `IA aplicada` (Skills label), `integrações com modelos` (Skills). No term exceeds 3 appearances.

## Application note

Portuguese message, apply link, and screening answers written. Facts not in the dossier (salary, start date, Next.js, Vite, own RAG product) are marked as not recorded; Lucas answers them. Form questions are not observable from the post.
