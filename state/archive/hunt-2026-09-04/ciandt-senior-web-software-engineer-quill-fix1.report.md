# Quill task result, fix round 1: ciandt-senior-web-software-engineer

Role: Resume Architect. Wrote and rebuilt. Did not grade.
Date: 2026-09-04
Hunt: 2026-09-04
Application: CI&T, Senior Web Software Engineer, Brazil
Input: `state/ciandt-senior-web-software-engineer-sieve.report.md`

## Files edited

- `resumes/hunts/2026-09-04/ciandt-senior-web-software-engineer/Lucas-Queiroz-Resume-en.tex`
- `resumes/hunts/2026-09-04/ciandt-senior-web-software-engineer/Lucas-Queiroz-Resume-en.pdf` (rebuilt)
- `reports/ciandt-senior-web-software-engineer-draft.md` (appended fix round 1 section, corrected the English gap statement and the token table)
- this report

No other file was touched. No subagent was spawned. No Maestri message was sent.

## Fixes applied

1. DexCare date range: `Jan 2026 - Present` changed to `Mar 2026 - Present`. Source: DOSSIER.md LinkedIn ground truth, captured 2026-09-04.
2. Luizalabs date range: `Jan 2024 - Jan 2026` changed to `Jan 2024 - Mar 2026`. Same source.
3. `English` placed twice. Skills line renamed `AI tooling and communication`, now ends with `Advanced English (C1)`. First DexCare bullet now ends with `working daily in English with US teams`. Source: DOSSIER.md Identity, "Advanced / C1. Daily English-only work with US teams at DexCare." The bullet does not say "remotely from Brazil"; the banned sentence from DOSSIER.md is not used.
4. `clean code` placed twice. Skills line `Engineering practices` now starts with `clean code`. DexCare maintainability bullet now reads `lint and complexity limits for clean code`. The agentic-workflows bullet keeps `code quality`, which the posting also uses. Source: DOSSIER.md AI at DexCare entry.
5. Requirements-analysis bullet restored in the Lippaus Mid-level block, third bullet: `Turned customer requirements into delivered solutions by leading project scoping and stakeholder communication and by analyzing requirements to guide technical implementation decisions.` Past tense, subject omitted, XYZ with no metric, as the dossier records no number for this bullet. `requirements analysis` also added to Skills so the practice token has a Skills placement. The bullet does not claim `functional and non-functional requirements`; the dossier records scoping and stakeholder communication only.
6. DexCare bullets reordered. New order: scheduling APIs; maintainability and clean code; agentic workflows with AI coding assistants; Epic EMR integrations, 15%; Auth0 multi-tenant endpoints, 25%. All five metrics unchanged.
7. Role-boundary spacing restored to the tractian shape. `\resumeSubheading` now uses `\\[-2pt]` on all three line breaks, no `\small`, and `\vspace{2pt}`. `\resumeRoleGap` is `\vspace{2pt}`. `grep -c '^$'` on the raw extraction returns 9, up from 6. Each role boundary now carries one blank line.

## Not applied, by instruction

Sieve items 8 to 11 stay open for Lucas. The CV carries zero occurrences of `Next.js`, `CMS`, `content model`, `PHP`, `document`, and `data flow`. No unsupported term, metric, or experience was added.

## Verification

- `tectonic Lucas-Queiroz-Resume-en.tex`: exit 0. Warnings only for Roboto font shape substitution, same as the prior build.
- `pdfinfo`: 1 page, 612 x 792 pts, letter.
- `pdftotext` raw and `pdftotext -layout` both ran on the rebuilt PDF. Contact line intact with `Vitória, ES, Brazil`, phone, email, LinkedIn, GitHub. Section headers Summary, Skills, Experience, Education present in source order. Four employment blocks and the education block each extract as one block with company, title, location, dates in that order.
- Dates in raw extraction, character for character: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. ASCII hyphen throughout.
- Titles unchanged: `Senior Software Engineer`, `Mid-level Software Engineer`, `Mid-level Software Engineer`, `Entry-level Fullstack Software Engineer`. Degree `Bachelor's degree, Information Systems`, FAESA.
- `grep -ic 'ruby\|rails'` on source, raw, and layout: 0, 0, 0.
- Ligature check: `workflow` extracts 4 times, no ligature glyphs.
- Raw term counts: English 2, clean code 2, JavaScript 3, TypeScript 3, React 3, APIs 3, integrations 3, testing 2, debugging 2, maintainability 2, AI coding assistants 3, agentic workflows 3, requirements 3. No term exceeds the cap of 3.
- Zero UTC, GMT, or time-zone overlap text.
- Rendered page image inspected at 80 dpi: no clipping, no overlap, Education block fully on page one with free space below.

## Observation for the Maestro

The raw extraction prints section headers in uppercase (`SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`) because the template's `\titleformat` applies `\scshape` with `\MakeLowercase`. This was already so in the build Sieve graded 8/8 on Gate 0, so it was left as is. Not changed in this round.
