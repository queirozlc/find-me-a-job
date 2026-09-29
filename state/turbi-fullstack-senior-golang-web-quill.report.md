# Quill report: turbi-fullstack-senior-golang-web

Task: turbi-fullstack-senior-golang-web-quill. Hunt 2026-09-04-g. Language: pt. Status: draft complete, one screening question unanswered.

## Artifacts

- resumes/hunts/2026-09-04-g/turbi-fullstack-senior-golang-web/Lucas-Queiroz-Resume-pt.tex
- resumes/hunts/2026-09-04-g/turbi-fullstack-senior-golang-web/Lucas-Queiroz-Resume-pt.pdf
- resumes/hunts/2026-09-04-g/turbi-fullstack-senior-golang-web/application-note.md
- state/turbi-fullstack-senior-golang-web-quill.complete.json

## Source and method

- Started from resumes/base-pt.tex. Preamble unchanged byte for byte. Role headers unchanged: same companies, titles, dates, and locations as the base (`Remoto` for DexCare and Luizalabs, `Vitória, ES, Brazil` for Lippaus).
- No base edit. No grading. No delegation. No outward action.
- Built with tectonic. Extracted with pdftotext raw and layout.

## Verification

- Pages: 2. Same as resumes/base-pt.pdf and the Maxxi PT CV in this hunt. Only Formação falls on page 2.
- Experience bullets: 16 of 16. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% all present.
- Contact block, section headers Resumo, Habilidades, Idiomas, Experiência, Formação present in raw extraction. Each role is one block in raw and layout extraction.
- `grep -in 'ruby\|rails'` on the tex: zero hits.
- Required tokens, count in raw extraction (Skills and one Experience bullet each): GoLang 3, React 4, microsserviços 4, sistemas distribuídos 2, Kubernetes 2, Git 3, Linux/Unix 2, OAuth 2.0 2, HTTP 3, CSS 2, JavaScript 3, Swagger 2.
- No UTC offset or overlap statement on the CV.

## Edits versus base-pt (all reword, no deletion)

- Summary: added JavaScript; wrote `Go (GoLang)` to mirror the posting spelling once.
- Skills: Linguagens now `Go (GoLang) | TypeScript | JavaScript | Node.js`. Backend gained `HTTP`, `OAuth 2.0`, `Auth0` (moved from Cloud line). New Arquitetura line: `microsserviços | sistemas distribuídos | multi-tenant | orientação a eventos`. Frontend gained `React Native | CSS`. Cloud gained `Linux/Unix | Git`.
- DexCare bullet 3: `REST APIs HTTP multi-tenant com autenticação OAuth 2.0 via Auth0 JWT, documentadas com OpenAPI/Swagger`.
- Luizalabs bullet 1: `microsserviços fiscais como sistemas distribuídos em Node.js, Java e Go (GoLang)`.
- Luizalabs bullet 4: `Docker e Kubernetes (containers Linux/Unix) no GCP via ArgoCD, versionados em Git`.
- Lippaus 2023 bullet 1: `plataforma multi-tenant web e mobile em React Native` (dossier: Lippaus stack includes React Native).
- Lippaus 2021 bullet 1: `dashboards internos de backoffice em JavaScript, HTTP e CSS`.

## Token derivations the Maestro should know

These tokens are not literal dossier strings. Each rests on a dossier fact. Reject any of them and I reword.

- `OAuth 2.0`: derived from the verified Auth0 JWT authentication at DexCare. Auth0 issues tokens through OAuth 2.0. Nothing else claimed.
- `HTTP`: derived from REST APIs at DexCare and web dashboards at Lippaus.
- `CSS`: derived from the dossier fact "back-office dashboards in JavaScript" at Lippaus. A web dashboard uses CSS. No design or CSS specialization claimed.
- `Linux/Unix`: derived from Docker and Kubernetes deployments on GCP at Luizalabs. Containers run Linux.
- `sistemas distribuídos`: the base already says "microsserviços fiscais distribuídos". Reworded to the posting token.

## Not claimed

- IoT experience. The posting names IoT backend work. The dossier has no IoT fact. Absent from CV and note; listed as unanswered in the screening answers.
- Weekend support scale, one weekend per month. Not accepted, not declined. Recorded as an unanswered before-submission screening question in the note.
- Vue.js, Angular, formal security certification, formal on-call rotation. Not in the dossier, not claimed.
- Code review (protected claim, unverified). Not introduced.

## Open for Lucas

1. Confirm or decline the one-weekend-per-month support scale.
2. Start date or notice period, and PJ salary expectation, if the Inhire form asks.
