# LawnStarter Staff Product Engineer — draft report

## Files written

- `resumes/lawnstarter-staff-product-engineer-en.tex`
- `resumes/lawnstarter-staff-product-engineer-en.pdf`
- `resumes/lawnstarter-staff-product-engineer-en.raw.txt`
- `resumes/lawnstarter-staff-product-engineer-en.layout.txt`
- `resumes/lawnstarter-staff-product-engineer-pt.tex`
- `resumes/lawnstarter-staff-product-engineer-pt.pdf`
- `resumes/lawnstarter-staff-product-engineer-pt.raw.txt`
- `resumes/lawnstarter-staff-product-engineer-pt.layout.txt`
- `reports/lawnstarter-staff-product-engineer-message.md`
- `reports/lawnstarter-staff-product-engineer-draft.md`

## Changed bullets versus base

The Portuguese CV mirrors the same changes in Portuguese.

### DexCare

- Moved the agent-environment bullet from position 6 to position 1 and reworded it around `AI coding agents`, daily `production work`, reusable `agent workflows`, `Claude Code`, and `Codex`; retained the supported controls: shared rules, lint, cyclomatic-complexity limits, and tests.
- Kept the 15% wrong-booking figure in position 2 and rewrote the sentence to lead with the measured outcome.
- Moved the 7% release-risk bullet from position 5 to position 3 and added the supported exact tokens `React`, `observability`, and `Datadog`.
- Moved the booking-services bullet from position 1 to position 4 and added supported `Node.js` beside `TypeScript`.
- Moved the 25% authentication-friction bullet from position 3 to position 5 and tightened it around Auth0 JWT, OpenAPI/Swagger, and tenant isolation.
- Moved the data-modeling bullet from position 4 to position 6 without changing its facts.
- Kept the 33% Shared Platform Initiative bullet in position 7 without changing its facts.

### Luizalabs

- Kept the electronic-invoice and 20% throughput bullets unchanged.
- Reworded the 18% support-ticket bullet to lead with its measured outcome.
- Reworded the deployment/testing bullet to use the posting-aligned `production-ready` wording while retaining Docker, Kubernetes, GCP, ArgoCD, Vitest, Jest, and CI/CD.

### Lippaus Distribuidora — Mid-level Software Engineer

- Moved the project-scoping and stakeholder-communication bullet from position 3 to position 1 without changing its facts.
- Moved the platform bullet from position 1 to position 2 and added supported `React Native`.
- Moved the 26% processing-capacity bullet from position 2 to position 3 and rewrote it to lead with the figure.

### Lippaus Distribuidora — Entry-level Fullstack Software Engineer

- Reordered the two existing bullets so end-to-end customer-facing delivery appears first; wording and facts are unchanged.

## Other source changes

- Rewrote the Summary for LawnStarter's exact supported themes: `AI-native`, `outcome-driven`, `full stack`, `TypeScript`, daily `Claude Code` and `Codex`, product outcomes, `AWS`, Advanced/C1 English, and US-hours overlap.
- Reordered and compressed Skills into AI quality, languages/frontend, backend/data, and cloud/observability groups.
- Added supported `React Native`, `AI agents`, and `observability` tokens.
- Changed every role location to the dossier-confirmed remote fact while preserving the base titles and dates exactly.
- Preserved the two-column role header and the CV-SPEC spacing macros.

## `[UNVERIFIED]` markers

None. Every shipped claim is traceable to `DOSSIER.md`.

## Posting tokens not placed

- `PHP/Laravel`, `Redshift`, `dbt`, `Airflow`, and `Sentry`: explicitly listed as gaps in the Maestro brief.
- `Cursor`, `Segment`, `GitHub Actions`, `MCP servers`, `evals tooling`, `Confluence`, and `Jira`: no personal-use evidence in the DOSSIER.
- PM/designer partnership, documented architecture/data-model/rollout decisions, runbooks, post-launch reviews, marketplace metrics, and lead-level decision authority: the DOSSIER does not support these claims.
- `Staff` as the CV title: intentionally not used because the requested CV title is `Senior Software Engineer` and every employment title must remain exactly as in the base.

## Build and extraction results

- English: tectonic PASS; 1 page; raw and layout extraction files written.
- Portuguese: tectonic PASS; 1 page; raw and layout extraction files written.
- Contact block: extracted in both languages with city, phone, email, LinkedIn, and GitHub.
- Section headers: English `Summary`, `Skills`, `Experience`, `Education`; Portuguese `Resumo`, `Habilidades`, `Experiência`, `Formação`; all extracted.
- Employment blocks: DexCare, Luizalabs, and both Lippaus Distribuidora roles extracted in both languages with their titles and dates.
- Raw/layout order: content order matches. The accepted two-column header split documented in CV-SPEC remains and introduces no additional loss.
- Forbidden stack tokens: none in either CV source or extraction.
- `[UNVERIFIED]`: none in either CV source or extraction.
- Visual render: PASS for both one-page PDFs; no clipping, overlap, broken glyphs, or spacing defects observed.

## Maestri analyzer handoff

Not run: `maestri list` showed only the connected `Recruiter` agent and no ATS Analyzer. No grading was performed by the Resume Architect.

## Fix round 1

1. Rebuilt both PDFs from the current `.tex` sources and regenerated the raw and layout extractions, removing the Summary source-to-artifact drift.
2. Added `product engineering` and a separate `product` outcome reference once each in the Summary.
3. Added `React` as its own Skills token beside `React Native`.
4. Named `event-driven architecture` in the existing DexCare TypeScript and Node.js booking-services bullet.
5. Named `data model` in the existing DexCare PostgreSQL modeling bullet.
6. Named `controlled rollout` in the existing DexCare feature-flag bullet.
7. Named `security` in the existing DexCare Auth0 JWT and tenant-isolation bullet.
8. Named `performance` in the existing Luizalabs 20% invoice-throughput bullet.
9. Named the existing shared rules, lint, complexity limits, and tests as `guardrails` in the DexCare agent-environment bullet.
10. Named `metric` in the existing 15% wrong-booking bullet.
18. Varied all seven DexCare leading verbs: `Enable`, `Improve`, `Lower`, `Deliver`, `Strengthen`, `Serve`, and `Cut`; the Portuguese version mirrors them with seven distinct verbs.

Additional corrections:

- Removed the unsupported industry description from the Lippaus entry-level bullet.
- Removed the unsupported nationwide and retailer scope from the Lippaus mid-level platform bullet.
- Removed the US-hours overlap clause from both Summaries and retained only `Advanced/C1 English`.
- Mirrored every factual and structural change in Portuguese; English retrieval terms were retained in context where required.
- Confirmed both PDFs remain one page and each extracted Summary matches its `.tex` source.
