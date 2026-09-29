# CharterUP Senior Full Stack — draft report

## Files written

- `resumes/charterup-senior-fullstack-en.tex`
- `resumes/charterup-senior-fullstack-en.pdf`
- `resumes/charterup-senior-fullstack-en.raw.txt`
- `resumes/charterup-senior-fullstack-en.layout.txt`
- `resumes/charterup-senior-fullstack-pt.tex`
- `resumes/charterup-senior-fullstack-pt.pdf`
- `resumes/charterup-senior-fullstack-pt.raw.txt`
- `resumes/charterup-senior-fullstack-pt.layout.txt`
- `reports/charterup-senior-fullstack-message.md`
- `reports/charterup-senior-fullstack-draft.md`

## Changed bullets versus base

The Portuguese CV mirrors the same factual changes in Portuguese.

### DexCare

- Moved the AI-environment bullet from position 6 to position 1 and aligned it with `AI-assisted development`, daily Claude Code and Codex use, shared rules, lint, complexity limits, and tests.
- Moved the 7% release-risk bullet from position 5 to position 2 and added supported `React`, `AWS`, and Datadog context.
- Kept the 25% authentication-friction bullet in position 3 and reworded it around the posting's exact `REST API Services` token.
- Moved the booking-services bullet from position 1 to position 4 and added supported `Node.js` beside `TypeScript`.
- Moved the 15% wrong-booking bullet from position 2 to position 5 and tightened its Epic EMR wording.
- Moved the data-modeling bullet from position 4 to position 6 and shortened it without changing the supported PostgreSQL, Sequelize, Drizzle ORM, DynamoDB, and Redis facts.
- Kept the 33% SPI bullet in position 7 and shortened it around shared services and tenant isolation.

### Luizalabs

- Kept the electronic-invoice bullet first and retained the dossier-supported `Node.js`, `Java`, and `Go` statement without claiming Java depth.
- Moved the production deployment/testing bullet from position 4 to position 2 to foreground supported DevOps exposure.
- Moved the 20% invoice-throughput bullet from position 2 to position 3 without changing its facts.
- Moved the 18% support-ticket bullet from position 3 to position 4 and rewrote it to lead with the measured outcome.

### Lippaus Distribuidora — Mid-level Software Engineer

- Moved the project-scoping and stakeholder-communication bullet from position 3 to position 1 to surface supported leadership evidence.
- Moved the platform bullet from position 1 to position 2 and added supported `React Native` for Mobile Apps exposure.
- Moved the 26% processing-capacity bullet from position 2 to position 3 and rewrote it to lead with the figure.

### Lippaus Distribuidora — Entry-level Fullstack Software Engineer

- Moved the customer-facing delivery bullet from position 2 to position 1 and mirrored the posting's `end-to-end` spelling.
- Moved the JavaScript back-office bullet from position 1 to position 2 and shortened it without changing its facts.

## Other source changes

- Rewrote the Summary around `5+ years`, `full stack`, `TypeScript`, customer-facing and back-office systems, `REST API Services`, `AWS`, daily Claude Code and Codex use, `AI-assisted development`, Advanced/C1 English, and US-hours overlap.
- Reordered Skills into Languages, Frontend and Mobile Apps, Backend, Data, Cloud and DevOps, and AI-assisted development.
- Added dossier-supported `Java` to Skills while keeping its Experience evidence limited to the recorded Luizalabs use.
- Changed every role location to the dossier-confirmed remote fact while preserving all base titles and dates exactly.
- Preserved the two-column role header and every CV-SPEC spacing macro.

## `[UNVERIFIED]` markers

None. Every shipped claim is traceable to `DOSSIER.md`.

## Posting tokens not placed

- `Vue`: explicitly absent from the DOSSIER and named as a gap in the Maestro brief.
- `JVM-based` depth and the posting's stronger proven-backend characterization: the DOSSIER records Java use at Luizalabs but no depth; only the supported Java fact was placed.
- Mentoring junior engineers: no mentoring evidence in the DOSSIER.
- The exact combined claim `hands-on leadership of end-to-end projects`: project-scoping leadership and end-to-end customer-facing delivery are separately supported, but the DOSSIER does not tie them into one claim.
- `cross-functional` collaboration: stakeholder communication is supported, but the DOSSIER does not identify the functions involved.
- `Data Engineering`: no supported experience-level fact in the DOSSIER.
- `AI-based deployment tools`: daily AI-assisted development is supported; AI deployment tooling is not.
- `Angular`, `Kotlin`, and `C#`: no DOSSIER evidence; they were not needed because supported alternatives React and Java were placed.

## Build and extraction results

- English: tectonic PASS; 1 page; raw and layout extraction files written.
- Portuguese: tectonic PASS after wording compression; 1 page; raw and layout extraction files written.
- Contact block: extracted in both languages with city, phone, email, LinkedIn, and GitHub.
- Section headers: English `Summary`, `Skills`, `Experience`, `Education`; Portuguese `Resumo`, `Habilidades`, `Experiência`, `Formação`; all extracted.
- Employment blocks: DexCare, Luizalabs, and both Lippaus Distribuidora roles extracted in both languages with their titles and dates.
- Raw/layout order: content order matches. The accepted two-column header split documented in CV-SPEC remains and introduces no additional loss.
- Visual render: PASS for both one-page PDFs; no clipping, overlap, broken glyphs, or spacing defects observed.
- Forbidden-token scan: PASS for both CV sources and extractions.
- `[UNVERIFIED]`: none in either CV source or extraction.

## Maestri analyzer handoff

Not run: `maestri list` showed only the connected `Recruiter` agent and no ATS Analyzer. No grading was performed by the Resume Architect.
