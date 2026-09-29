# Goodway Group draft report

## Files written

- `resumes/goodway-global-fullstack-en.tex`
- `resumes/goodway-global-fullstack-en.pdf`
- `resumes/goodway-global-fullstack-en.raw.txt`
- `resumes/goodway-global-fullstack-en.layout.txt`
- `reports/goodway-global-fullstack-message.md`
- `reports/goodway-global-fullstack-draft.md`
- `state/app-goodway-global-fullstack.md`, one appended log line only

## Changed bullets versus base

- DexCare D1: Reframed the event-driven services as scheduling workflows. Kept TypeScript, Express, Koa, booking, and availability.
- DexCare D4: Reframed the data stack as SQL-backed booking flows. Kept PostgreSQL, Sequelize, Drizzle ORM, DynamoDB Streams, Redis, and AWS SDK v3.
- DexCare D6: Reframed the Claude Code and Codex work as supported AI-assisted delivery. Kept the documented quality controls.
- Luizalabs L2: Led with the supported 20% throughput result and BullMQ method.
- Luizalabs L3: Led with the supported 18% support-ticket result and dashboard method.
- Luizalabs L4: Led with reliable deployment delivery. Kept Docker, Kubernetes, GCP, ArgoCD, CI/CD, Vitest, and Jest.
- Lippaus P2: Led with the supported 26% capacity result and BullMQ method.
- Lippaus P3: Reframed the supported scoping and stakeholder work around customer-facing JavaScript features.
- Lippaus E1: Changed the leading verb from `Developed` to `Built` and kept the supported JavaScript dashboard fact.
- Lippaus E2: Removed the general customer-facing feature bullet because P3 now carries that supported fact with a named technology.

## UNVERIFIED markers

None.

## Verification

- `tectonic` built the PDF. It emitted Roboto font request warnings and no build error.
- `pdfinfo` reported one page.
- Raw and layout extraction contain the full contact block and the four required section headers.
- The base contains four Experience blocks and one Education block. All five `resumeSubheading` blocks extract with their company or school, title, date, and location.
- Visual inspection found no clipping, overlap, broken glyph, or unreadable text.
- `grep -n UNVERIFIED` returned no hits.
- The required forbidden-term grep returned no hits.
- React, TypeScript, JavaScript, Node.js, Go, AWS, REST APIs, dashboards, and AI each appear no more than three times as whole terms in the CV source.

## Posting tokens not placed

- `Git`: DOSSIER.md does not record Git.
- `4+ years`: The CV uses the accurate dossier-derived value `5+ years`.
- `strong experience`: DOSSIER.md does not assign this depth label.
- `modern web applications`: The dossier supports web applications, but it does not support the qualifier `modern`.
- `software design`: DOSSIER.md does not record this exact claim.
- `debugging`: DOSSIER.md does not record this claim.
- `cross-functional teams`: The dossier supports stakeholder communication, but it does not identify the teams as cross-functional.
- `remote environment`: The role headers show the base locations. The dossier does not support this exact phrase in a CV claim.
- `data-driven applications`: The dossier supports back-office dashboards, but it does not use this broader claim.
- `data visualization`: The Maestro brief identifies this as a gap.
- `Python`: The Maestro brief identifies this as a gap.
- `data engineering workflows`: The Maestro brief identifies this as a gap.
- `automation`: The dossier supports AI-driven agentic workflows, but it does not use this broader token.
- `modern CI/CD practices`: The dossier supports CI/CD, but it does not support the qualifier `modern`.
