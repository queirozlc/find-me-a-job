# TRACTIAN Senior Backend Engineer draft analysis

## Scope

- Created one English CV from `resumes/base-en.tex`.
- Used `jobs/tractian-senior-backend-engineer.md` and `keywords/unassigned.md`.
- Kept the segment as `not observable`.
- Did not edit the base CV.
- Did not create the other language.

## Positioning

- Positioned Lucas as TypeScript, Node.js, React, and Go. React stays in Skills and in the Lippaus bullet.
- Focused the Summary on 5+ years of backend development in TypeScript, Node.js, and Go, event-driven healthcare scheduling, multi-tenant services, AWS, English use, and AI-driven agentic workflows.
- Preserved all companies, exact LinkedIn titles, exact date periods, role locations, contact data, and education data from the verified base and dossier.
- Replaced the base table header with consecutive single-column company, title, location, and date lines.

## Required token placement

| Token | Skills | Experience evidence |
| --- | --- | --- |
| `Node.js` | Languages | Luizalabs electronic-invoice services |
| `Go` | Languages | Luizalabs electronic-invoice services |
| `event-driven` | Backend | DexCare booking and provider-availability APIs |
| `RabbitMQ` | Backend | DexCare event-driven messaging |
| `BullMQ` | Backend | Luizalabs invoice queues and Lippaus jobs |
| `microservices` | Backend | DexCare shared multi-tenant services |
| `distributed systems` | Backend | DexCare Epic EMR time-slot flows |
| `PostgreSQL` | Data | DexCare scheduling data and Lippaus platform |
| `DynamoDB` | Data | DexCare booking and provider-availability APIs |
| `APIs` | Backend | DexCare booking and authentication APIs |

The document also keeps TypeScript in Skills and in a DexCare bullet, and AWS in Summary, Skills, and the DexCare shared-platform bullet. `React`, `multi-tenant`, and `AWS` each appear exactly three times. No term appears more than three times.

## Bullet changes

- Kept every bullet in subject-omitted first-person past tense.
- Used an outcome and an implementation method in every bullet.
- Kept the dossier metrics of 15%, 25%, 7%, 33%, 20%, 18%, and 26%.
- Did not add a number where the dossier says no number is available.
- Reduced the bullet count to keep the required single-column role headers on one page while preserving all four employment blocks.

## Gaps and exclusions

- Did not add Kafka, Python, Rust, ClickHouse, ScyllaDB, Cassandra, or MongoDB because the dossier does not support them.
- Did not claim Portuguese fluency because the dossier does not record it.
- Did not claim mission-critical service experience because the dossier does not use that qualification.
- Did not claim open-source work because the dossier excludes the unsupported prior claim.
- Added no `[UNVERIFIED]` markers because the CV contains only supported claims.

## Fix round 1, 2026-09-04

Applied Sieve fixes 1, 2, 3, 5, 6, and 7. Fix 4, Portuguese fluency, was not applied. Lucas has not supplied the level.

- DexCare dates corrected to `Mar 2026 - Present`.
- Luizalabs dates corrected to `Jan 2024 - Mar 2026`.
- `DynamoDB` added to the DexCare booking and provider-availability bullet.
- `React` reduced from 5 to 3 occurrences. Removed from the Summary and from the LaunchDarkly bullet.
- `multi-tenant` reduced from 4 to 3 occurrences. Removed from the Auth0 REST APIs bullet.
- `AWS` added to the DexCare shared-platform bullet, supported by the dossier's SPI description of one AWS environment per customer.
- `\resumeRoleGap` widened from 2pt to 7pt. The PDF stays on one page.

## Verification

- `tectonic`: completed with exit code 0 after fix round 1.
- `pdfinfo`: one page.
- `pdftotext`: contact data, Summary, Skills, Experience, Education, DexCare, Luizalabs, both Lippaus Distribuidora roles, FAESA, all titles, and all dates extracted.
- `pdftotext -layout`: the same content extracted in the correct order.
- Forbidden-token scan of the source and both text extractions: zero hits.
- Unsupported-token scan of both text extractions: zero hits.
- Visual render: no clipping, overlap, broken glyphs, or split employment blocks.

No CV grade was produced.
