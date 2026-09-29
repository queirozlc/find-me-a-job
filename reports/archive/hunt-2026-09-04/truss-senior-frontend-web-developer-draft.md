# Truss Senior Front-End Web Developer Resume Draft

## Scope

- Language: English.
- Base: `resumes/base-en.tex`.
- Positioning: TypeScript, Node.js, React, and Go.
- Output: one tailored source and one PDF.
- Posting primary language: JavaScript and TypeScript. Accepted.

## Supported posting tokens

The resume places each supported token in Skills and in one Experience bullet.

| Token | Status | Skills line | Experience evidence |
| --- | --- | --- | --- |
| React | required | Frontend | DexCare reusable React components |
| JavaScript | required | Languages | Luizalabs fiscal dashboards; Lippaus back-office dashboards |
| TypeScript | required | Languages | DexCare TypeScript services behind web interfaces |
| API-driven state management | required | Frontend | DexCare booking and availability interfaces |
| Jest | required or similar | Testing | DexCare release confidence bullet |
| CSS | required, similar styling | Frontend | DexCare reusable React components |
| invoicing | preferred | Domain | Luizalabs electronic invoicing bullet |
| front-end | posting title term | none, Summary carries it | DexCare reusable front-end React components |

Term counts in the raw extraction after fix round 1: React 3, TypeScript 3, JavaScript 3, Node.js 3, API-driven 3, state management 2, workflow or workflows 3, front-end 2, frontend 1, healthcare scheduling 3, multi-tenant 3, Jest 2, Vitest 2, CSS 2, testing 2, invoicing 2. No term exceeds the cap of 3.

## Gaps for Sieve

- Redux and Redux Toolkit are not supported by the dossier and do not appear in the resume. The resume carries `API-driven state` as the nearest supported term.
- React Router is not supported by the dossier and does not appear in the resume.
- MUI, Emotion, and SASS/SCSS are not supported by the dossier and do not appear in the resume. The posting allows a similar styling tool. The resume carries `CSS` as the supported equivalent.
- React Testing Library is not supported by the dossier and does not appear in the resume. The posting allows a similar testing tool. The resume carries `Jest` and `Vitest` as the supported equivalents.
- Storybook, GraphQL, Cypress, Playwright, billing, and payments are not supported by the dossier and do not appear in the resume.
- Ember is not supported by the dossier and does not appear in the resume.
- The required overlap of 17:00/18:00-21:00/22:00 GMT+4 is not on the resume. Lucas's availability for it is not recorded in the dossier. It belongs to the screening answers only.

No gap was converted into a claim. No claim-status marker was added.

## Content changes

- Rewrote the Summary for a front-end posting: production web applications, API-driven user interfaces, mature multi-tenant systems, and one AI mention.
- Reduced Skills to four lines: Languages, Frontend, Testing, and Backend and AI tooling. Dropped Data and Cloud lines that carry no posting token.
- Rewrote the DexCare bullets around web interfaces, API-driven state, reusable React components with CSS, Epic EMR integrations, multi-tenant REST APIs, Jest and Vitest testing, and agentic workflows. Dropped the data-layer, feature-flag, and SPI bullets.
- Reworded the Luizalabs bullets to carry `invoicing` and `JavaScript`. Dropped Java and the deployment bullet.
- Trimmed Lippaus to three bullets total, keeping PostgreSQL, BullMQ, and JavaScript.
- Kept dossier metrics: wrong bookings 15%, authentication friction 25%, invoice throughput 20%, support tickets 18%, processing capacity 26%.
- Preserved the exact employers, titles, date periods, locations, education, and contact data from the base and the dossier.
- Changed the copied role-header macro to the single-column format required by CV-SPEC item 2.
- Final edit before the prior harness stopped: removed one `React` and one `JavaScript` and `TypeScript` mention from the first two DexCare bullets to stay within the cap of 3. The PDF was rebuilt from that source in this session.

## Mechanical verification

- `tectonic Lucas-Queiroz-Resume-en.tex` completed with exit code 0. It emitted Roboto font request warnings and wrote the PDF.
- `pdfinfo` reported one letter-size page.
- Raw and layout extraction retained all contact fields, four section headers, four employment blocks, and the education block.
- Source, raw text, and layout text each contained zero Ruby or Rails tokens.
- Raw text contained zero Redux, React Router, MUI, Emotion, SASS, SCSS, Testing Library, Storybook, GraphQL, Cypress, Playwright, billing, payment, GMT, UTC, overlap, or claim-status tokens.
- `grep -c workflow` on the raw text returned 3 after fix round 1, which confirms ligatures are disabled and the cap of 3 holds.
- The rendered page showed no clipping, overlap, or missing content.

## Fix round 1, 2026-09-04

Applied Sieve fixes 3 through 8 only. Fixes 1 and 2, Redux, Redux Toolkit, and React Router, were not applied. DOSSIER.md does not establish them, and Lucas has not confirmed them.

- Fix 3: added the posting's `front-end` term to the DexCare shared UI bullet: `reusable front-end React components with CSS`. Claim and XYZ shape unchanged.
- Fix 4: added `front-end` to the Summary: `5+ years building production front-end web applications`. No LinkedIn title changed.
- Fix 5: reduced `workflow`/`workflows` from 5 to 3. DexCare bullet 1 now reads `for healthcare scheduling`. Lippaus entry-level bullet now reads `operational and administrative processes`.
- Fix 6: completed the phrase to `API-driven state management` in the Frontend Skills line and in DexCare bullet 1. A non-breaking space keeps the phrase on one line in the raw extraction.
- Fix 7: removed the filler `testing` entry from the Testing Skills line. The line is now `Jest | Vitest`.
- Fix 8: added `Electronic invoicing` to Skills on a new `Domain` line, with `Healthcare scheduling`. Both trace to DOSSIER.md: Luizalabs fiscal and NF-e domain, DexCare healthcare scheduling domain.
- No metric, title, date, employer, location, or degree changed. No GMT, UTC, or overlap statement was added.

### Verification after fix round 1

- `tectonic` exit code 0. `pdfinfo` reports one page.
- Raw and layout extraction keep the contact block, the four section headers, the four employment blocks, and the education block.
- All five date ranges match DOSSIER.md LinkedIn ground truth character for character.
- Zero Ruby, Rails, Redux, Router, GMT, UTC, or overlap tokens in the source, raw text, and layout text.
- Raw text contains only ASCII plus the accented characters in `Vitória`, the bullet glyph, and the apostrophe. No ligature codepoint.
