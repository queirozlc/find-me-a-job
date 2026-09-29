# Quill report: Kake, Senior Fullstack Engineer (React + Golang)

Date: 2026-09-04
Language: English only
Segment: agency
Base: resumes/base-en.tex, copied. Base not edited.
Status: package written, PDF built, one page. Not graded.

## Files written or changed

- resumes/hunts/2026-09-04-e/kake-senior-fullstack-engineer-react-golang/Lucas-Queiroz-Resume-en.tex
- resumes/hunts/2026-09-04-e/kake-senior-fullstack-engineer-react-golang/Lucas-Queiroz-Resume-en.pdf
- resumes/hunts/2026-09-04-e/kake-senior-fullstack-engineer-react-golang/application-message.md (draft, not sent)
- resumes/hunts/2026-09-04-e/README.md (Kake row status changed from `tailoring` to `review`)
- state/kake-senior-fullstack-engineer-react-golang-quill.report.md (this file)

No other file was changed.

## Build

```
tectonic Lucas-Queiroz-Resume-en.tex
pdfinfo Lucas-Queiroz-Resume-en.pdf
pdftotext Lucas-Queiroz-Resume-en.pdf -
pdftotext -layout Lucas-Queiroz-Resume-en.pdf -
pdftoppm -r 70 -png Lucas-Queiroz-Resume-en.pdf page
```

Build succeeded. Only fontspec font-loading notices, same as the base. Page count: 1, confirmed with pdfinfo. Rendered PNG inspected: no clipping, no overlap, no missing glyph.

## Extraction checks on the raw text

- Contact block on one line: city, phone, email, LinkedIn, GitHub. No UTC offset, no time-zone statement.
- Headers extract as SUMMARY, SKILLS, LANGUAGE, EXPERIENCE, EDUCATION. Small caps render upper case in pdftotext, same as the base.
- Four employment blocks plus Education each extract as one block: `Company | Dates` then `Title | Location`, then bullets. Single-column header, no tabular.
- `grep -c workflow` returns 5 and `office` returns 2, so ligatures are disabled.
- `grep -in 'ruby\|rails'` on the .tex and the extracted text returns nothing.
- Titles, dates, and locations: every `{Company}{Dates}` and `{Title}{Location}` pair is identical to base-en.tex, checked with diff.

## Preserved content

- Roles: 4 of 4 (DexCare, Luizalabs, Lippaus Mid-level, Lippaus Entry-level). Education preserved.
- Bullets: 16 of 16. Same count as the base.
- Metrics: 15%, 25%, 7%, 33%, 20%, 18%, 26%. All 7 present.
- Rewording for fit, facts unchanged: "e-commerce operation" to "e-commerce"; "SEFAZ communication" to "SEFAZ calls"; "improving" to "raising"; "visibility into fiscal workflows" to "fiscal workflow visibility"; "through ArgoCD" to "via ArgoCD"; "Jest testing" to "Jest tests". Luizalabs language order became "Go, Node.js, and Java".
- Layout: same margins as the 2026-09-04-c tailored copy (top margin -0.6in, text height +1.2in).

## Term placement

| Term | Skills | Experience bullet | Count |
| --- | --- | --- | --- |
| Go | Languages | Luizalabs, tax microservices in Go | 3 |
| Golang | Languages, `Go (Golang)` | none, mirrored once | 1 |
| React | Frontend | DexCare, observability to React with Datadog RUM | 3 |
| TypeScript, Node.js | Languages | DexCare bullet 1, Luizalabs bullet 1 | 3 each |
| Backend services | Backend | DexCare bullet 1 | 3 |
| Service-oriented architecture | Backend | DexCare bullet 1 | 2 |
| Sync and async workloads | Messaging and workloads | DexCare bullet 1 | 2 |
| AWS | Cloud and operations | DexCare, AWS SDK v3 | 3 |
| Docker, Kubernetes | Cloud and operations | Luizalabs deploy bullet | 2 each |
| REST APIs (gRPC equivalent) | Backend | DexCare Auth0 bullet | 2 |
| RabbitMQ, AMQP, BullMQ (Kafka equivalent) | Messaging and workloads | BullMQ in Luizalabs and Lippaus bullets | 1, 1, 3 |
| Relational and NoSQL databases | Data | DexCare data bullet | 2 |
| PostgreSQL, DynamoDB, Redis | Data | DexCare data bullet, Lippaus platform bullet | 3, 2, 2 |
| Testing | Testing and AI tooling | DexCare AI bullet, Luizalabs deploy bullet | 2 |
| Observability, metrics, logging, Datadog | Observability and practices | DexCare flags bullet | 3, 2, 2, 2 |
| Feature flags | Cloud and operations | DexCare flags bullet | 2 |
| Performance | Observability and practices | Lippaus BullMQ bullet | 2 |
| Reliability | Observability and practices | Luizalabs SEFAZ bullet | 2 |
| Scalability | Observability and practices | DexCare SPI bullet | 2 |
| Code reviews | Observability and practices | DexCare AI bullet | 2 |
| 5+ years | Summary | | 1 |

No term exceeds 3 appearances. Practice terms (performance, reliability, scalability, code reviews) are placed on role-history fit under weight 1. The dossier has no explicit code-review entry; the AI bullet ties it to the codebase-enforcement fact.

## Unsupported tokens left absent

gRPC, Kafka, A/B testing, experimentation platforms, tracing, incident response, fintech, high compliance, crypto, Web3, GraphQL, Next.js, and any traffic volume. Verified with grep on the extracted text: zero hits for gRPC, Kafka, A/B, fintech, crypto, Web3. The screening answers mark these as not recorded in the dossier.

## Message

application-message.md holds the English message to Sharon M. plus screening answers. Time zone is stated in the message and screening answers only, never on the CV.
