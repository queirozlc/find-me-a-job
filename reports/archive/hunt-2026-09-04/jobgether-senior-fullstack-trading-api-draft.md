# Jobgether Senior Full-Stack Engineer - Trading API Resume Draft

## Scope

- Created one English resume from `resumes/base-en.tex`.
- Preserved the verified contact data, employers, titles, locations, dates, and education.
- Left the base resume unchanged.

## Source basis

- Used `DOSSIER.md` as the source for all candidate facts.
- Used `jobs/jobgether-senior-fullstack-trading-api.md` for posting requirements.
- Used `keywords/agency.md` for the agency keyword corpus.

## Tailoring decisions

- Positioned Lucas as a TypeScript, Node.js, React, and Go engineer.
- Added each supported posting token to Skills and a relevant Experience bullet: Go, TypeScript, React, CSS, SQL, PostgreSQL, REST APIs, API design, testing, deployment, GCP, Docker, Kubernetes, and remote work.
- Prioritized full-stack product delivery, API work, relational data, cloud deployment, and remote collaboration.
- Kept all four employment blocks and used first-person, past-tense, subject-omitted bullets.
- Omitted the DexCare SPI achievement with its 33% metric and the Luizalabs fiscal-dashboard achievement with its 18% metric to keep the resume focused and on one page.
- Kept all Lippaus bullets from the base resume.

## Exclusions

- Did not claim strong Golang depth, HTML, TailwindCSS, another CSS framework, financial markets, fintech, algorithmic trading, or startup experience.
- Did not add credentials, contract facts, work authorization, regulated-domain qualifications, or new metrics.
- Did not print a time-zone statement.

## Verification result

- Tectonic built the PDF successfully. It emitted `roboto.sty` font-request warnings and created the requested PDF.
- `pdfinfo` reported one page.
- Raw and layout extraction preserved the contact block, Summary, Skills, Experience, Education, all four employment blocks, and Education.
- Source and PDF extraction contained zero forbidden stack tokens.
- The source used `fontspec`, `Ligatures=NoCommon`, Roboto, single-column role headers, and no tables.
- Visual inspection found no clipping, overlap, missing content, or second page.

## Fix round 1, 2026-09-04

Input: `state/jobgether-senior-fullstack-trading-api-sieve.report.md`. Applied supported fixes 1, 4, and 5 only.

- Fix 1: `Golang` now appears in Skills under Languages and in the Luizalabs distributed tax microservices bullet. The Summary keeps `Go`. The Go and Golang family totals three occurrences.
- Fix 4: Skills now reads `Google Cloud Platform (GCP)`. The Luizalabs deployment bullet keeps `GCP`.
- Fix 5: DexCare bullets 2 and 4 swapped. The SQL and PostgreSQL bullet is now second. The Epic EMR bullet is now fourth. No bullet text changed.
- Held for Lucas: HTML, TailwindCSS or another CSS framework, and the word `startup`. Not added.
- Still excluded: strong Golang depth, financial markets, fintech, algorithmic trading. Not added.

Verification after the rebuild: tectonic exit 0, one letter page, raw and layout extraction intact, all five date ranges exact, zero Ruby or Rails tokens in source and both extractions.
