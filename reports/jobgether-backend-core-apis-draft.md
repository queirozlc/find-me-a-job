# Backend Engineer, Core APIs — draft report

## Files written

- `resumes/jobgether-backend-core-apis-en.tex`
- `resumes/jobgether-backend-core-apis-en.pdf`
- `resumes/jobgether-backend-core-apis-en.raw.txt`
- `resumes/jobgether-backend-core-apis-en.layout.txt`
- `resumes/jobgether-backend-core-apis-pt.tex`
- `resumes/jobgether-backend-core-apis-pt.pdf`
- `resumes/jobgether-backend-core-apis-pt.raw.txt`
- `resumes/jobgether-backend-core-apis-pt.layout.txt`
- `reports/jobgether-backend-core-apis-message.md`
- `reports/jobgether-backend-core-apis-draft.md`

## Changed bullets versus base

The Portuguese CV mirrors the same factual changes in Portuguese.

### DexCare

- Kept the real-time booking bullet in position 1 and reworded it around the posting's exact `Core APIs`, `TypeScript`, `Node.js`, `backend services`, `Express`, and `Koa` terms.
- Moved the 25% authentication-friction bullet from position 3 to position 2 and retained Auth0 JWT, OpenAPI/Swagger, multi-tenant APIs, and tenant isolation.
- Moved the data-modeling bullet from position 4 to position 3 and added supported `SQL`, PostgreSQL, DynamoDB, Redis, and AWS context.
- Moved the 7% release-risk bullet from position 5 to position 4 and added supported Datadog browser logging alongside RUM and feature flags.
- Moved the 15% wrong-booking bullet from position 2 to position 5 and tightened its Epic EMR wording.
- Kept the AI-environment bullet in position 6 and shortened it without changing the Claude Code, Codex, shared rules, lint, complexity-limit, or testing facts.
- Kept the 33% SPI bullet in position 7 and shortened it around shared services and tenant isolation.

### Luizalabs

- Kept the electronic-invoice bullet first and foregrounded supported distributed microservices, Java, and Go; omitted Node.js here to keep the posting's primary Node.js token within the appearance cap.
- Kept the 20% invoice-throughput bullet in position 2 without changing its facts.
- Moved the production deployment/testing bullet from position 4 to position 3 to foreground Docker, Kubernetes, and CI/CD.
- Moved the 18% support-ticket bullet from position 3 to position 4 and rewrote it to lead with the measured outcome.

### Lippaus Distribuidora — Mid-level Software Engineer

- Moved the 26% processing-capacity bullet from position 2 to position 1 to foreground asynchronous backend jobs.
- Kept the platform bullet in position 2 and added the dossier-supported React Native detail.
- Kept project scoping and stakeholder communication in position 3.

### Lippaus Distribuidora — Entry-level Fullstack Software Engineer

- Kept the JavaScript back-office bullet first and shortened it without changing its facts.
- Kept customer-facing end-to-end delivery second without changing its facts.

## Other source changes

- Rewrote the Summary around `5+ years`, `scalable backend systems`, `Core APIs`, microservices, `TypeScript`, `Node.js`, real-time scheduling, `SQL`, DynamoDB, Redis, AI-driven agentic workflows, Advanced/C1 English, and US-hours overlap.
- Reordered Skills to prioritize Languages, Backend, Data, then supporting Frontend, Cloud/operations, and testing/AI tooling.
- Added supported `SQL`, `Core APIs`, microservices, browser logging, Docker, Kubernetes, CI/CD, and Datadog wording.
- Kept `Go` as recorded usage only and did not imply primary-stack depth.
- Changed every role location to the dossier-confirmed remote fact while preserving all base titles and dates exactly.
- Preserved the two-column role header and every CV-SPEC spacing macro.

## `[UNVERIFIED]` markers

None. Every shipped claim is traceable to `DOSSIER.md`.

## Posting tokens not placed

- `Elasticsearch`, `Terraform`, `AWS CloudFormation`, `ClickHouse`, `dbt`, `Snowflake`, `BigQuery`, `Redshift`, and `Databricks`: absent from the DOSSIER; several are named gaps in the Maestro brief.
- Strong hands-on Go depth: Go usage at Luizalabs is confirmed, but depth is not recorded; the CV states use only.
- `Git`, IDEs, and shell scripting: no explicit DOSSIER evidence. Supported `CI/CD` was placed.
- Generic `real-time data-processing services`: real-time healthcare scheduling and event-driven services are supported, but the broader data-processing characterization is not.
- Independent investigation, root-cause analysis, hypothesis development, experimentation, and performance tuning: no experience-level evidence in the DOSSIER.
- Shared on-call rotation: no on-call evidence in the DOSSIER.
- Mentoring junior developers: no mentoring evidence in the DOSSIER.
- Globally distributed and asynchronous team experience: daily work with a US team is supported; the broader team shape is not recorded.
- Modern telemetry practices: Datadog RUM and browser logging are supported; telemetry practice ownership is not.
- Internet security and privacy mechanisms: Auth0 JWT and tenant isolation are supported; the broader characterization is not recorded.

## Build and extraction results

- English: tectonic PASS; 1 page; raw and layout extraction files written.
- Portuguese: tectonic PASS; 1 page; raw and layout extraction files written.
- Contact block: extracted in both languages with city, phone, email, LinkedIn, and GitHub.
- Section headers: English `Summary`, `Skills`, `Experience`, `Education`; Portuguese `Resumo`, `Habilidades`, `Experiência`, `Formação`; all extracted.
- Employment blocks: DexCare, Luizalabs, and both Lippaus Distribuidora roles extracted in both languages with their titles and dates.
- Raw/layout order: content order matches. The accepted two-column header split documented in CV-SPEC remains and introduces no additional loss.
- Visual render: PASS for both one-page PDFs; no clipping, overlap, broken glyphs, or spacing defects observed.
- Forbidden-token scan: PASS for both CV sources and extractions.
- `[UNVERIFIED]`: none in either CV source or extraction.

## Maestri analyzer handoff

Not run: `maestri list` showed only the connected `Recruiter` agent and no ATS Analyzer. No grading was performed by the Resume Architect.

## Fix round 1

1. Capped `APIs` at three appearances by changing the DexCare authentication bullet from `multi-tenant APIs` to `multi-tenant services` in both languages.
4. Rewrote DexCare bullet 1 to name `real-time data processing` over `DynamoDB Streams` in the existing event-driven TypeScript and Node.js services context.
5. Added `Go` to both Summaries, explicitly scoped to recorded use at Luizalabs rather than DexCare or primary-stack depth.
9. Rewrote the Luizalabs deployment bullet to carry the exact terms `reliability` and `production-grade` alongside Docker, Kubernetes, GCP, ArgoCD, Vitest, Jest, and CI/CD.
10. Renamed the Backend Skills group to carry `Multi-tenant security`, supported by the existing Auth0 JWT and tenant-isolation bullet.
11. Expanded the Frontend group to `React | React Native`.
12. Split the combined testing/AI line into separate `Testing` and `AI tooling` Skills groups.
13. Added a 1 em hanging indent to the `resumeItem` macro so wrapped lines align under bullet text.
14. Capitalized `Core APIs` in both Summaries.
15. Varied the DexCare opening verbs. English now uses `Deliver`, `Cut`, `Serve`, `Lower`, `Reduce`, `Enable`, and `Decrease`; Portuguese uses `Entrega`, `Corta`, `Atende`, `Diminui`, `Reduz`, `Habilita`, and `Mitiga`.

Additional corrections:

- Removed the US-hours overlap clause from both Summaries while retaining Advanced/C1 English.
- Removed the unsupported nationwide scope from the Lippaus mid-level platform bullet.
- Removed the unsupported industry and company-stage wording from the Lippaus entry-level dashboard bullet.
- Kept the relevant English retrieval terms beside Portuguese wording: `5+ years`, `microservices`, `real-time data processing`, `Testing`, `reliability`, `production-grade`, and `English`.
- Rebuilt both PDFs with `tectonic`, regenerated raw and layout extractions, and confirmed both remain one page.
