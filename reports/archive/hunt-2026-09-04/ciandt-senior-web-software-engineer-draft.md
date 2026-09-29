# CI&T Senior Web Software Engineer Resume Draft

## Scope

- Language: English.
- Base: `resumes/base-en.tex`.
- Positioning: TypeScript, Node.js, React, and Go.
- Output: one tailored source and one PDF.

## Supported posting tokens

The resume places each supported required token in Skills and Experience.

| Token | Experience evidence |
| --- | --- |
| JavaScript | Luizalabs and Lippaus dashboard delivery |
| TypeScript | DexCare scheduling services |
| React | DexCare scheduling interfaces |
| APIs | DexCare scheduling APIs |
| integrations | Epic EMR integrations |
| testing | DexCare Vitest and Jest controls |
| debugging | DexCare Datadog workflow |
| maintainability | DexCare service quality controls |
| AI coding assistants | DexCare Claude Code and Codex workflow |
| agentic workflows | DexCare daily delivery workflow |
| clean code | DexCare lint and complexity limits (fix round 1) |
| English | DexCare daily English work with US teams (fix round 1) |
| requirements analysis | Lippaus Mid-level scoping and implementation decisions (fix round 1) |

## Gaps for Sieve

- Next.js is not supported by the dossier and does not appear in the resume.
- CMS concepts and content modeling are not supported by the dossier and do not appear in the resume.
- Familiarity with PHP-based applications is not supported by the dossier and does not appear in the resume.
- Advanced English was listed as a gap in the Maestro brief. Sieve corrected this: DOSSIER.md Identity supports it. Fix round 1 placed `Advanced English (C1)` in Skills and `English` in one DexCare bullet.
- The posting permits a comparable modern web framework, but the brief does not confirm that React satisfies this option.

No gap was converted into a claim. No `[UNVERIFIED]` marker was required or added.

## Content changes

- Replaced the general summary with a web-engineering summary for this posting.
- Focused DexCare bullets on React, TypeScript, APIs, integrations, engineering practices, and AI-assisted delivery.
- Kept dossier metrics for wrong bookings, authentication friction, invoice throughput, support tickets, and processing capacity.
- Preserved the exact employers, titles, date periods, locations, education, and contact data from the verified base and dossier.
- Changed the copied role-header macro to the required single-column format.

## Mechanical verification

- `tectonic` completed with exit code 0. It emitted Roboto font request warnings and created the PDF.
- `pdfinfo` reported one letter-size page.
- Raw and layout extraction retained all contact fields, four section headers, four employment blocks, and the education block.
- Source, raw text, and layout text each contained zero Ruby or Rails tokens.
- The resume contained zero Next.js, CMS, content modeling, PHP, or `[UNVERIFIED]` tokens.
- The rendered page showed no clipping, overlap, or missing content.


## Fix round 1, 2026-09-04

Applied Sieve fixes 1 to 7. Items 8 to 11 stay open for Lucas. No Next.js, CMS, content modeling, PHP, or documentation claim was added.

- Fix 1: DexCare dates changed to `Mar 2026 - Present`, per DOSSIER.md LinkedIn ground truth.
- Fix 2: Luizalabs dates changed to `Jan 2024 - Mar 2026`, per DOSSIER.md LinkedIn ground truth.
- Fix 3: `Advanced English (C1)` added to the Skills line `AI tooling and communication`. The first DexCare bullet now ends with `working daily in English with US teams`, from the DOSSIER.md Identity fact.
- Fix 4: `clean code` added to the Skills line `Engineering practices`. The DexCare maintainability bullet now reads `lint and complexity limits for clean code`. The agentic-workflows bullet keeps `code quality`.
- Fix 5: Restored the approved scoping bullet in the Lippaus Mid-level block in XYZ form: `Turned customer requirements into delivered solutions by leading project scoping and stakeholder communication and by analyzing requirements to guide technical implementation decisions.` Added `requirements analysis` to Skills so the practice token has a Skills placement too. The bullet uses `requirements`, not `functional and non-functional requirements`, because the dossier records scoping and stakeholder communication only.
- Fix 6: DexCare bullets reordered. Order now: scheduling APIs, maintainability and clean code, agentic workflows, Epic EMR integrations, Auth0 endpoints.
- Fix 7: Role header macro reverted to the tractian spacing: no `\small`, `\\[-2pt]`, `\vspace{2pt}`; `\resumeRoleGap` reverted to `\vspace{2pt}`. Raw extraction now carries 9 blank lines, with one blank line at each role boundary.

Verification after fix round 1:

- `tectonic` exit 0, one letter page.
- Raw and layout extraction keep the contact line, four section headers, four employment blocks, and the education block.
- Dates in the raw stream: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`.
- Zero Ruby or Rails tokens in source, raw, and layout.
- Term counts in the raw stream: English 2, clean code 2, JavaScript 3, TypeScript 3, React 3, APIs 3, integrations 3, AI coding assistants 3, agentic workflows 3, requirements 3. No term exceeds 3.
- Zero Next.js, CMS, content model, PHP, document, UTC, GMT tokens.
