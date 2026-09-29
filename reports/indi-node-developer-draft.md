# INDI Staffing Services Node Developer draft report

## Files written

- `resumes/indi-node-developer-en.tex`
- `resumes/indi-node-developer-en.pdf`
- `resumes/indi-node-developer-en.raw.txt`
- `resumes/indi-node-developer-en.layout.txt`
- `reports/indi-node-developer-message.md`
- `reports/indi-node-developer-draft.md`
- `state/app-indi-node-developer.md`, one appended log line only

## Changed bullets versus base

### DexCare

- Replaced the booking-services bullet with a posting-focused bullet for TypeScript, Node.js, Express, Koa, AWS, and `microservices and cloud platforms [UNVERIFIED]`.
- Reworded the 15% wrong-booking bullet around Epic EMR, PostgreSQL, DynamoDB, Redis, RabbitMQ, AMQP, and `SQL and NoSQL databases [UNVERIFIED]`.
- Reworded the 25% authentication-friction bullet around REST APIs, scalable solutions, Auth0 JWT, and OpenAPI/Swagger.
- Replaced the base data-modeling and AI bullets with one delivery-quality bullet. It includes Claude Code, Codex, automated tests, and the marked practices from the brief.
- Kept the 7% release-risk result and reworded it around React, LaunchDarkly/OpenFeature, and Datadog RUM.
- Removed the SPI bullet to keep one page and prioritize the posting requirements.

### Luizalabs

- Reworded the distributed-tax-services bullet around Java, Go, and electronic invoice issuing.
- Reworded the BullMQ and SEFAZ bullet to lead with the 20% throughput result.
- Reworded the dashboard bullet to lead with the 18% support-ticket result.
- Reworded the deployment bullet around Docker, Kubernetes, GCP, ArgoCD, Vitest, Jest, automated tests, and CI/CD pipelines.

### Lippaus Distribuidora, Mid-level Software Engineer

- Reworded the platform bullet around nationwide expansion, PostgreSQL, and the marked `developing entire applications from scratch` phrase.
- Reworded the BullMQ bullet to lead with the 26% processing-capacity result.
- Reworded the scoping bullet around the marked agile-methodology phrase and supported stakeholder communication.

### Lippaus Distribuidora, Entry-level Fullstack Software Engineer

- Combined the two base bullets into one bullet for customer-facing and back-office JavaScript features. This kept the supported operational-workflow and technical-constraint facts.

## Other changes

- Rewrote the Summary with the exact `5+ years of experience in Node development`, `Advanced English level`, and `Advanced / C1` phrases.
- Reordered Skills around backend architecture, data, engineering practices, delivery, cloud operations, and AI tooling.
- Preserved every base company, title, date, and location.
- Preserved the two-column role header and CV-SPEC spacing.
- Did not edit `resumes/base-en.tex`. Its SHA-256 remained `34902052e97bcfe8e6c99f8255e4a5c2a4cb5a2ba969a65543874bfd3564a8a7`.

## UNVERIFIED markers

The source has 17 marker occurrences on nine grep lines.

- `microservices and cloud platforms [UNVERIFIED]`, twice in Skills and DexCare. The brief requires the `microservices` marker. The dossier supports AWS and event-driven services, but it does not assign the microservices label to Lucas's DexCare work.
- `SQL and NoSQL databases [UNVERIFIED]`, twice in Skills and DexCare. PostgreSQL and DynamoDB are facts. The brief still requires the broader `NoSQL` claim to carry the marker.
- `SOLID principles [UNVERIFIED]`, twice in Skills and DexCare. SOLID is not in the dossier.
- `clean code [UNVERIFIED]`, twice in Skills and DexCare. Clean code is not in the dossier.
- `software design patterns [UNVERIFIED]`, twice in Skills and DexCare. Design patterns are not in the dossier.
- `version control systems [UNVERIFIED]`, twice in Skills and DexCare. Version-control use is not in the dossier.
- `Git [UNVERIFIED]`, twice in Skills and DexCare. Git is not in the dossier.
- `Intermediate agile methodologies management [UNVERIFIED]`, twice in Skills and Lippaus. The dossier supports project scoping and stakeholder communication. It does not state agile-methodology use or a management level.
- `developing entire applications from scratch [UNVERIFIED]`, once in Lippaus. The dossier states that Lucas built the platform. It does not state that he started the applications from scratch.

`grep -n UNVERIFIED` returned lines 67, 68, 69, 71, 82, 83, 85, 103, and 105.

## Posting tokens not placed

- `Advanced algorithm knowledge`: The Maestro brief identifies algorithm depth as a gap.
- `IT infrastructure knowledge`: The Maestro brief identifies IT-infrastructure depth as a gap.
- `architecting backend systems`: The dossier does not state architecture ownership.
- `code reviews`: The dossier does not record code-review work.
- `analytics`: Datadog RUM is a fact, but the dossier does not record analytics work.
- `automation and tool development`: The dossier supports agent environments. It does not state tool-development ownership or an engineering-productivity result.
- `defining engineering processes for product launches and releases`: The dossier supports a 7% release-risk result. It does not state process ownership.
- `technical interviews`: The dossier does not record interview work.

## Build and extraction results

- `tectonic`: PASS. It reported only Roboto font-request warnings.
- Page count: 1.
- Raw and layout extraction files: written.
- Contact block: extracted with city, phone, email, LinkedIn, and GitHub.
- Section headers: `Summary`, `Skills`, `Experience`, and `Education` extracted.
- Blocks: DexCare, Luizalabs, both Lippaus roles, and FAESA extracted with titles and dates.
- Visual review: PASS. No clipping, overlap, broken glyph, or spacing defect was visible.
- Required phrase extraction: PASS for all placed phrases, including `Advanced / C1`.
- Exact high-weight term cap: PASS. TypeScript, Node.js, React, Go, JavaScript, BullMQ, and PostgreSQL each appear no more than three times.
- `grep -in 'ruby\|rails'` on the source: zero hits.
- The same forbidden scan on both extraction files: zero hits.
