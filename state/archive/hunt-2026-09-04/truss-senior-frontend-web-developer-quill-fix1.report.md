# Quill fix round 1 result — truss-senior-frontend-web-developer

Role: Resume Architect. Edited only. No grading. No subagent spawned. No Maestri message sent.
Date: 2026-09-04
Input: `state/truss-senior-frontend-web-developer-sieve.report.md`

## Files edited

- `resumes/hunts/2026-09-04/truss-senior-frontend-web-developer/Lucas-Queiroz-Resume-en.tex`
- `resumes/hunts/2026-09-04/truss-senior-frontend-web-developer/Lucas-Queiroz-Resume-en.pdf` (rebuilt)
- `reports/truss-senior-frontend-web-developer-draft.md`
- this file

## Fixes applied

| Sieve item | Change | Location |
| --- | --- | --- |
| 3 | `reusable React components with CSS` became `reusable front-end React components with CSS` | DexCare bullet 2 |
| 4 | `production web applications` became `production front-end web applications` | Summary |
| 5 | `across healthcare scheduling workflows` became `for healthcare scheduling`; `administrative workflows` became `administrative processes` | DexCare bullet 1; Lippaus entry-level bullet |
| 6 | `API-driven state` became `API-driven state management` | Frontend Skills line; DexCare bullet 1 |
| 7 | Dropped bare `testing` entry | Testing Skills line, now `Jest | Vitest` |
| 8 | Added `Domain: Electronic invoicing | Healthcare scheduling` | New Skills line |

Fix 6 note: the DexCare bullet wrapped between `state` and `management` in the raw extraction on the first rebuild. A LaTeX non-breaking space now holds the phrase on one line. Raw and layout extraction both contain `state management` twice.

Fix 8 note: `Electronic invoicing` traces to the DOSSIER.md Luizalabs fiscal, NF-e, and SEFAZ domain. `Healthcare scheduling` traces to the DOSSIER.md DexCare domain entry. The bullet wording `for healthcare scheduling` in DexCare bullet 1 keeps that phrase at 3 occurrences.

## Fixes not applied

- Sieve items 1 and 2, `Redux`, `Redux Toolkit`, `React Router`: not added. DOSSIER.md does not establish them. Lucas has not confirmed them. The Gate 1 gap stands and needs a candidate fact from Lucas.
- No MUI, Emotion, SASS/SCSS, React Testing Library, Storybook, GraphQL, Cypress, Playwright, billing, or payments token was added.
- No GMT+4, UTC offset, or overlap statement was added.

## Unchanged facts

Titles, employers, dates, locations, degree, contact block, and all five metrics (15%, 25%, 20%, 18%, 26%) are unchanged.

## Verification

- `tectonic Lucas-Queiroz-Resume-en.tex`: exit code 0. Roboto font warnings only.
- `pdfinfo`: Pages 1.
- `pdftotext` raw and `pdftotext -layout`: contact block, `Summary`, `Skills`, `Experience`, `Education`, four employment blocks, education block all present.
- Dates in extraction: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. All match DOSSIER.md LinkedIn ground truth.
- `grep -ci 'ruby\|rails'` on source, raw text, and layout text: 0, 0, 0.
- `grep -ci 'redux\|router\|gmt\|utc\|overlap'` on source, raw text, and layout text: 0, 0, 0.
- Raw extraction term counts: workflow/workflows 3, front-end 2, frontend 1, API-driven 3, state management 2, testing 2 (one label, one bullet), invoicing 2, healthcare scheduling 3, multi-tenant 3, React 3, TypeScript 3, JavaScript 3, Node.js 3, Jest 2, Vitest 2, CSS 2. No term exceeds 3.
- Non-ASCII characters in raw text: accented `ó` and `í` in `Vitória`, the bullet glyph, and the apostrophe. No ligature codepoint.
