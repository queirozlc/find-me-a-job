# micro1 Frontend Engineer Specialist draft report

## Files written

- `resumes/micro1-frontend-specialist-en.tex`
- `resumes/micro1-frontend-specialist-en.pdf`
- `resumes/micro1-frontend-specialist-en.raw.txt`
- `resumes/micro1-frontend-specialist-en.layout.txt`
- `reports/micro1-frontend-specialist-message.md`
- `reports/micro1-frontend-specialist-draft.md`
- `state/app-micro1-frontend-specialist.md`, one appended log line only

## Changed bullets versus base

### DexCare

- Reworded the booking-services bullet around TypeScript, Node.js, Express, Koa, AWS, real-time booking, and provider availability.
- Replaced the base release-risk bullet with one marked frontend-depth bullet. It keeps the supported React, 7%, LaunchDarkly/OpenFeature, and Datadog RUM facts. It contains all eight marked posting claims.
- Reworded the AI-environment bullet around Claude Code, Codex, agentic workflows, shared rules, lint, complexity limits, and tests.
- Kept the 25% authentication-friction result and shortened the bullet around REST APIs, Auth0 JWT, and OpenAPI/Swagger.
- Removed three lower-priority base bullets to keep one page and avoid unsupported frontend depth outside the one marked bullet.

### Luizalabs

- Reworded the tax-services bullet around Java, Go, and electronic invoice issuing.
- Reworded the BullMQ and SEFAZ bullet to lead with the 20% throughput result.
- Reworded the deployment bullet around Docker, Kubernetes, GCP, ArgoCD, CI/CD, Vitest, and Jest.
- Removed the dashboard bullet to prioritize the posting's frontend terms while keeping the term cap.

### Lippaus Distribuidora, Mid-level Software Engineer

- Kept the PostgreSQL platform and nationwide-expansion facts with shorter wording.
- Reworded the BullMQ bullet to lead with the 26% processing-capacity result.
- Reworded the scoping bullet around stakeholder requirements and PostgreSQL platform work.

### Lippaus Distribuidora, Entry-level Fullstack Software Engineer

- Kept one JavaScript back-office dashboard bullet for the posting's frontend evidence.
- Removed the customer-feature bullet to keep one page.

## Other changes

- Rewrote the Summary around JavaScript, TypeScript, React, Node.js, Go, healthcare interfaces, back-office products, Advanced / C1 English, and AI-driven agentic workflows.
- Used the posting spellings `Javascript` and `Typescript` once in Skills.
- Reordered Skills around frontend architecture, quality, technical communication, backend data, cloud delivery, testing, and AI tooling.
- Preserved every base company, title, date, and location.
- Preserved the two-column role header and CV-SPEC spacing.
- Did not edit `resumes/base-en.tex`. Its SHA-256 remained `34902052e97bcfe8e6c99f8255e4a5c2a4cb5a2ba969a65543874bfd3564a8a7`.

## UNVERIFIED markers

The source has 16 marker occurrences on four grep lines. Skills contains eight markers. One DexCare bullet contains the matching eight markers.

- `Component architecture [UNVERIFIED]`, twice. The dossier does not record component-architecture work.
- `State management patterns [UNVERIFIED]`, twice. The dossier does not record state-management work.
- `SSR/CSR/SSG [UNVERIFIED]`, twice. The dossier does not record these rendering strategies.
- `frontend performance optimization [UNVERIFIED]`, twice. The dossier records Datadog RUM and a 7% release-risk result, but it does not record frontend-performance optimization.
- `accessibility/A11y [UNVERIFIED]`, twice. The dossier does not record accessibility work.
- `Technical writing [UNVERIFIED]`, twice. The dossier does not record technical-writing work.
- `RFCs/ADRs [UNVERIFIED]`, twice. The dossier does not record RFC or ADR authorship.
- `Code review feedback [UNVERIFIED]`, twice. The dossier does not record code-review work.

`grep -n UNVERIFIED` returned lines 67, 68, 69, and 82.

## Posting tokens not placed

- `3+ years of professional experience in frontend engineering`: The DOSSIER dates show 5 years and 6 months of software engineering. They do not quantify frontend-only tenure.
- `modern HTML/CSS practices`: The dossier does not record HTML or CSS work, and the Maestro brief does not authorize this token as a marked claim.
- `technically rigorous documentation`: The dossier does not record documentation quality. The narrower authorized `Technical writing` claim is present with a marker.
- `AI model` training: The dossier records AI-assisted development with Claude Code and Codex. It does not record training AI models.
- `Ally`: The posting's first list uses `Ally`, while its scope and Maestro brief use accessibility and `A11y`. The CV uses the brief token and does not claim a separate `Ally` skill.

The Maestro brief lists no gaps. The items above stay out because the dossier does not support them and the claim line does not authorize them.

## Build and extraction results

- `tectonic`: PASS. It reported only Roboto font-request warnings.
- Page count: 1.
- Raw and layout extraction files: written.
- Contact block: extracted with city, phone, email, LinkedIn, and GitHub.
- Section headers: `Summary`, `Skills`, `Experience`, and `Education` extracted.
- Blocks: DexCare, Luizalabs, both Lippaus roles, and FAESA extracted with titles and dates.
- Visual review: PASS. No clipping, overlap, broken glyph, or spacing defect was visible.
- Required phrase extraction: PASS for all placed phrases, including `Advanced / C1`.
- Exact term cap: PASS. JavaScript, TypeScript, Node.js, React, Go, frontend, PostgreSQL, and BullMQ each appear no more than three times.
- `grep -in 'ruby\|rails'` on the source: zero hits.
- The same forbidden scan on both extraction files: zero hits.
