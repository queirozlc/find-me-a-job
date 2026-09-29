# Quill layout report: P7 Group, Desenvolvedor(a) Full Stack

Date: 2026-09-04
Task: p7-group-fullstack-quill-layout. Hunt: 2026-09-04-g. Segment: br-pj. Language: Portuguese only.
Posting: jobs/p7-group-fullstack.md. Manifest: state/p7-group-fullstack-manifest.json.
Required tokens: JavaScript, TypeScript, Node.js, NestJS, React, APIs REST, webhooks, LLMs, RAG. Preferred: none.
Status: rebuilt on the approved base preamble. Not graded. Not submitted. No base edit, no delegation, no outward action.

## Files

- resumes/hunts/2026-09-04-g/p7-group-fullstack/Lucas-Queiroz-Resume-pt.tex
- resumes/hunts/2026-09-04-g/p7-group-fullstack/Lucas-Queiroz-Resume-pt.pdf
- resumes/hunts/2026-09-04-g/p7-group-fullstack/application-note.md
- state/p7-group-fullstack-quill-layout.report.md (this file)
- state/p7-group-fullstack-quill-layout.complete.json (sentinel)

## Changes to the tailored tex

1. Preamble replaced by the approved resumes/base-pt.tex preamble, lines 1 to the line before `\begin{document}`. `diff` on that range: identical. This brings the single-column `\resumeSubheading` (company, title, dates, location as consecutive lines, `\samepage`, `\nopagebreak`), `\clubpenalty`, `\widowpenalty`, and `beginpenalty=10000` on the lists. The `tabular*` header is gone.
2. `ES, Brasil` replaced by `ES, Brazil` in the contact block, both Lippaus role locations, and the FAESA location. Four occurrences. Zero `Brasil` left in the tex.
3. Body content otherwise untouched: Resumo, Habilidades, Idiomas, all 16 Experience bullets, all 7 metrics, all titles, dates, and company names identical to the prior tailored tex.

## Build and checks

```
tectonic Lucas-Queiroz-Resume-pt.tex     -> exit 0
pdfinfo                                   -> Pages: 2
pdftotext          <pdf> -                -> raw
pdftotext -layout  <pdf> -                -> layout
```

- Raw contact line: `Vitória, ES, Brazil | +55 (27) 99203-0170 | sepulchrolucas@gmail.com | linkedin.com/in/queiroz-lucas | github.com/queirozlc`.
- Headers RESUMO, HABILIDADES, IDIOMAS, EXPERIÊNCIA, FORMAÇÃO present in raw.
- Each employment block survives in raw and layout as company, title, dates, location on consecutive lines, followed by its bullets.
- Page 2 holds the whole Lippaus entry-level block (header plus 2 bullets) and the whole Formação block. No block splits across the page break.
- Bullets 16 of 16. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% each present once.
- Titles and dates: DexCare Senior Software Engineer Mar 2026 - Present; Luizalabs Mid-level Software Engineer Jan 2024 - Mar 2026; Lippaus Distribuidora Mid-level Software Engineer Jan 2023 - Jan 2024; Lippaus Distribuidora Entry-level Fullstack Software Engineer Mar 2021 - Jan 2023; FAESA Feb 2022 - Dec 2025. Locations Remoto, Remoto, Vitória, ES, Brazil, Vitória, ES, Brazil.
- `grep -in 'ruby\|rails'` on tex: 0. `grep -ic 'ruby\|rails\|utc\|gmt'` on raw: 0. `grep -c workflow` on raw: 2, ligatures disabled.

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

## Application note

Three corrections, everything else preserved (full Portuguese message, apply link, screening answers, explicit unknowns for salary, start date, Next.js, Vite, own RAG product, form questions).

1. Message: `me candidatei pelo formulário` replaced by `pretendo me candidatar pelo formulário indicado`. Nothing was submitted.
2. Message: `e tenho disponibilidade full-time` removed. Closing line now states remote work from Vitória, ES, Brazil and PJ with own CNPJ only.
3. Screening: `Localização` now prints `Vitória, ES, Brazil`. `Dedicação` now reads: the posting asks full-time; Lucas's full-time availability is not recorded in the dossier; Lucas confirms before sending.

## Open for the Maestro

- Full-time availability is not recorded anywhere. Lucas must confirm it before the note is sent.
- Not graded here. Deterministic gate and Sieve review are the Maestro's next step.
