# Quill fix report 1: MFS Talento Humano, React Developer

Date: 2026-09-04
Task: mfs-react-developer-quill-fix1. Hunt: 2026-09-04-g. Language: Spanish only.
Previous report: state/mfs-react-developer-quill.report.md.
Gate defects reported by the Maestro: layout, role locations.
Status: fixed and rebuilt. Not graded. Not submitted. No base edit, no script edit, no delegation, no outward action.

## Files

- resumes/hunts/2026-09-04-g/mfs-react-developer/Lucas-Queiroz-Resume-es.tex (rewritten in place)
- resumes/hunts/2026-09-04-g/mfs-react-developer/Lucas-Queiroz-Resume-es.pdf (rebuilt)
- resumes/hunts/2026-09-04-g/mfs-react-developer/application-note.md (unchanged)
- state/mfs-react-developer-quill-fix1.report.md (this file)
- state/mfs-react-developer-quill-fix1.complete.json (sentinel)

## Changes (2)

1. Preamble: replaced with the base-en.tex preamble byte for byte, through `\begin{document}`. English babel is back. The Spanish `\%` override and the `spanish,es-noshorthands,es-nolists` babel line are gone. Verified: `diff` of the first 60 lines against base-en.tex is empty.
2. Role locations: DexCare and Luizalabs now print `Remote`, as base-en and CLAUDE.md rule 3 require. Lippaus still prints `Vitória, ES, Brazil`. `Remoto` count in the tex: 0.

Unchanged: Spanish body, headings Resumen, Habilidades, Idiomas, Experiencia, Educación, all 16 bullets, all 7 metrics, titles, dates, employers, degree, contact block, token placement.

## Build and checks

```
tectonic Lucas-Queiroz-Resume-es.tex   -> exit 0 (font warnings only)
pdfinfo                                -> Pages: 2
pdftotext         <pdf> -              -> raw
pdftotext -layout <pdf> -              -> layout
```

- Spanish accents survive raw extraction with English babel: `Construí`, `Portugués`, `EDUCACIÓN`, `fricción`, `asíncronas` present. Accents are input as TeX escapes, so babel language does not affect them.
- Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% each print once with no space before `%`. English babel does not touch `\%`, so the override was not needed.
- Headers RESUMEN, HABILIDADES, IDIOMAS, EXPERIENCIA, EDUCACIÓN present in raw.
- Bullets: 16 of 16.
- Locations in raw: `Remote`, `Remote`, `Vitória, ES, Brazil`, `Vitória, ES, Brazil`, FAESA `Vitória, ES, Brazil`.
- Titles and dates verbatim: Mar 2026 - Present; Jan 2024 - Mar 2026; Jan 2023 - Jan 2024; Mar 2021 - Jan 2023; Feb 2022 - Dec 2025.
- Every employment block survives in raw and layout as company, title, dates, location on consecutive lines, then bullets. Page break falls before the Lippaus entry-level block; page 2 holds that block and Educación whole.
- `grep -ic 'ruby\|rails'` tex: 0. `grep -ic 'ruby\|rails\|utc\|gmt\|\.net\|moq\|nunit'` raw: 0. `grep -c workflow` raw: 3.

## Token counts (raw, word-boundary), unchanged from the first report

React.js 2, JavaScript 3, TypeScript 3, Node.js 18 2, Next.js 2, APIs RESTful 2, JSON Web Token (JWT) 2, PostgreSQL 3, Agile 2, Git 2, AWS 3, HTML 2, CSS 2, Babel 2, Webpack 2, NPM 2, Unit Testing 2. At cap (3): React, JavaScript, TypeScript, Node.js, PostgreSQL, AWS, Go, BullMQ.

## Open for the Maestro

- Judgment calls 1 to 3 of the first report still stand (posting-derived tokens, design patterns, Spanish level).
- Not graded here. Gate re-run is the Maestro's next step.
