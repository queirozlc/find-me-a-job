# Quill report: MFS Talento Humano, React Developer

Date: 2026-09-04
Task: mfs-react-developer-quill. Hunt: 2026-09-04-g. Segment: agency. Language: Spanish only.
Posting: jobs/mfs-react-developer.md. Manifest: state/mfs-react-developer-manifest.json.
Base: resumes/base-en.tex (corrected single-column header). Preamble and layout copied unchanged except babel and one percent-sign fix (below).
Status: written. Not graded. Not submitted. No base edit, no delegation, no outward action.

## Files

- resumes/hunts/2026-09-04-g/mfs-react-developer/Lucas-Queiroz-Resume-es.tex
- resumes/hunts/2026-09-04-g/mfs-react-developer/Lucas-Queiroz-Resume-es.pdf
- resumes/hunts/2026-09-04-g/mfs-react-developer/application-note.md
- state/mfs-react-developer-quill.report.md (this file)
- state/mfs-react-developer-quill.complete.json (sentinel)

## Preamble changes (2)

1. `\usepackage[english]{babel}` to `\usepackage[spanish,es-noshorthands,es-nolists]{babel}`.
2. Added `\AtBeginDocument{\renewcommand{\%}{\char37\relax}}`. Spanish babel prints `15 %` with a thin space. The override restores `15%` so every metric extracts as one token. Verified in raw text.

## Content changes to the base copy

- Body translated to Spanish. Headings: Resumen, Habilidades, Idiomas, Experiencia, Educación.
- Literal, untranslated: every company name, every job title, every date string including `Present`, the contact block, `Vitória, ES, Brazil`. DexCare and Luizalabs location prints `Remoto` (same word in Spanish and Portuguese, mirrors base-pt).
- Idiomas: `Portugués: Nativo | Inglés: Fluido (C1)`. No Spanish proficiency printed; the dossier does not record one.
- Educación: `Licenciatura en Sistemas de Información (Information Systems)`, FAESA, `Feb 2022 - Dec 2025`.
- Resumen: first person (`Soy`, `Construyo`, `Integro`), adds `JavaScript` to the stack list, keeps the AI mention once.
- Habilidades edits: `Node.js` to `Node.js 18`; added `HTML | CSS` to Lenguajes; `REST APIs` to `APIs RESTful`; Frontend `React` to `React.js | Next.js | Babel | Webpack | NPM`; added `Git` to Nube y operaciones; new line `Seguridad: Auth0 | JSON Web Token (JWT)` (Auth0 moved out of the cloud line); testing line adds `Unit Testing | Agile`.
- DexCare bullet 3: `Auth0 JWT` to `Auth0 y JSON Web Token (JWT)`; `REST APIs` to `APIs RESTful`.
- DexCare bullet 5: `React` to `React.js y Next.js`.
- Luizalabs bullet 1: `Node.js` to `Node.js 18`.
- Luizalabs bullet 4: added `versionados en Git` and `pruebas unitarias (Unit Testing)` around the Vitest and Jest suites.
- Lippaus mid-level bullet 3: added `en ciclos Agile`.
- Lippaus entry-level bullet 1: `JavaScript` to `JavaScript, HTML y CSS`.
- Lippaus entry-level bullet 2: added `con pipelines de build front-end en Babel, Webpack y NPM`.

Untouched: all 16 bullets kept, all 7 metrics kept, all titles, dates, employers, degree, locations. No `.NET`, `MoQ`, `NUnit` token anywhere. No protected claim: `code review` appears nowhere in the tex or note. No design-pattern personal claim on the CV.

## Build and checks

```
tectonic Lucas-Queiroz-Resume-es.tex   -> exit 0 (font warnings only)
pdfinfo                                -> Pages: 2
pdftotext         <pdf> -              -> raw
pdftotext -layout <pdf> -              -> layout
```

- Raw contact line: `Vitória, ES, Brazil | +55 (27) 99203-0170 | sepulchrolucas@gmail.com | linkedin.com/in/queiroz-lucas | github.com/queirozlc`.
- Headers RESUMEN, HABILIDADES, IDIOMAS, EXPERIENCIA, EDUCACIÓN present in raw.
- Every employment block survives in raw and layout as company, title, dates, location on consecutive lines, then its bullets.
- Page break falls before the Lippaus entry-level block. Page 2 holds that whole block and the whole Educación block. No block splits.
- Bullets: 16 of 16. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% each present once, no space before `%`.
- Titles and dates verbatim: DexCare Senior Software Engineer Mar 2026 - Present; Luizalabs Mid-level Software Engineer Jan 2024 - Mar 2026; Lippaus Distribuidora Mid-level Software Engineer Jan 2023 - Jan 2024; Lippaus Distribuidora Entry-level Fullstack Software Engineer Mar 2021 - Jan 2023; FAESA Feb 2022 - Dec 2025.
- `grep -in 'ruby\|rails'` on tex: 0. `grep -ic 'ruby\|rails\|utc\|gmt\|\.net\|moq\|nunit'` on raw: 0. `grep -c workflow` on raw: 3, ligatures disabled.

## Token placement (raw text, word-boundary counts)

Required:

| Token | Habilidades | Experience bullet | Count |
| --- | --- | --- | --- |
| React.js | Frontend | DexCare bullet 5 | 2 (React total 3, with Resumen) |
| JavaScript | Lenguajes | Lippaus entry-level bullet 1; Resumen | 3 |
| TypeScript | Lenguajes | DexCare bullet 1; Resumen | 3 |
| Node.js 18 | Lenguajes | Luizalabs bullet 1 | 2 (Node.js total 3, with Resumen) |
| Next.js | Frontend | DexCare bullet 5 | 2 |
| APIs RESTful | Backend | DexCare bullet 3 | 2 |
| JSON Web Token (JWT) | Seguridad | DexCare bullet 3 | 2 |
| PostgreSQL | Datos | DexCare bullet 4; Lippaus mid-level bullet 1 | 3 |
| Agile | Pruebas, prácticas y herramientas de IA | Lippaus mid-level bullet 3 | 2 |
| Git | Nube y operaciones | Luizalabs bullet 4 | 2 |
| AWS | Nube y operaciones | DexCare bullet 4; Resumen | 3 |
| HTML | Lenguajes | Lippaus entry-level bullet 1 | 2 |
| CSS | Lenguajes | Lippaus entry-level bullet 1 | 2 |
| Babel | Frontend | Lippaus entry-level bullet 2 | 2 |
| Webpack | Frontend | Lippaus entry-level bullet 2 | 2 |
| NPM | Frontend | Lippaus entry-level bullet 2 | 2 |

Preferred: `Unit Testing` placed (Habilidades, Luizalabs bullet 4), 2. `MoQ`, `NUnit` not placed, .NET tools, zero occurrences.

At cap (3): React, JavaScript, TypeScript, Node.js, PostgreSQL, AWS, Go, BullMQ.

## Judgment calls for the Maestro

1. Posting-derived tokens with no dossier fact, placed under the 2026-09-04 match policy: `Next.js` (DexCare bullet 5), `Node.js 18` (Luizalabs bullet 1, version not recorded), `Babel`, `Webpack`, `NPM` (Lippaus entry-level bullet 2), `HTML`, `CSS` (Lippaus entry-level bullet 1), `Git`, `Agile`. Same rule the Maxxi application used for Nest.js, docker-compose, Git, Agile. Each is flagged in the note for Lucas to confirm or veto. Next.js is the weakest: the dossier records React at DexCare, not Next.js.
2. Design patterns: the CV makes no claim. The note offers a suggested three-pattern answer mapped to dossier facts (Observer/pub-sub, Repository, Strategy) for Lucas to confirm in his own words.
3. Spanish proficiency is not recorded. The message is in Spanish because the posting is. The note says so and asks Lucas to confirm before sending. Nothing about Spanish on the CV.
4. Two pages, same break point as the Maxxi PT application. All 16 bullets kept.
5. `Present` and `Remoto`: the date string stays literal per the brief; the location word follows base-pt.

## Application note

Full Spanish recruiter message addressed to María Fernanda Spirito, Google Form URL as observed, recruiter profile not observable, screening answers per posting item, explicit unknowns: Spanish level, Node.js 18, Next.js, Babel/Webpack/NPM, Waterfall, SVN/Mercurial, .NET Core, MoQ/NUnit, salary expectation in USD, start date or notice, contract type. Wording is intent (`pienso postularme`). No submission claimed.

## Open for the Maestro

- Lucas confirms or vetoes the posting-derived tokens in judgment call 1 before sending.
- Salary expectation, availability, and Spanish level are not recorded. Lucas answers before sending.
- Not graded here. Deterministic gate and Sieve review are the Maestro's next step.
