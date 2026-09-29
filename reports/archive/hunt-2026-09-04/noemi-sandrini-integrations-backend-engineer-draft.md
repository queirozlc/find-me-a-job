# Noemi Sandrini Integrations Back-end Engineer Resume Draft

## Scope

- Language: English for an American company.
- Base: `resumes/base-en.tex`.
- Positioning: TypeScript, Node.js, React, and Go.
- Output: one tailored source and one PDF.

## Supported posting tokens

The resume places each supported required token in Skills and Experience.

| Token | Experience evidence |
| --- | --- |
| Node.js | DexCare event-driven services |
| TypeScript | DexCare event-driven services |
| Express | DexCare service delivery |
| Back-end | DexCare booking services |
| third-party API integrations | DexCare Epic EMR time-slot sync |
| REST APIs | DexCare multi-tenant authentication APIs |
| AWS | DexCare scheduling data access through AWS SDK v3 |
| Docker | Luizalabs service deployment |
| PostgreSQL | DexCare data modeling and Lippaus platform work |
| event-driven | DexCare booking services |
| queues | Luizalabs BullMQ processing |
| testing | DexCare AI delivery controls |
| distributed systems | Luizalabs tax systems |
| AI-assisted development | DexCare agent environments |
| validation of AI-generated code | DexCare agent environments |
| AI code agents | DexCare Claude Code and Codex workflow |
| Advanced English | DexCare work with US teams |

The resume also places the supported preferred tokens GCP and agentic workflows in Skills and Experience.

## Gaps for Sieve

- NestJS is not supported by the dossier. The resume uses supported Express as the posting alternative.
- OAuth 2.0/OIDC, Webhooks, and AWS SQS are not supported by the dossier.
- OOP and SOLID are not supported by the dossier.
- Direct client communication is not supported by the dossier.
- The Maestro brief does not classify debugging or code review as supported claims.
- Validation of AI-generated code is now named in the DexCare AI bullet, from the dossier agent-environment fact.
- The resume does not claim SAML, Microsoft Entra ID, Microsoft Graph, Google Workspace APIs, ERP, CRM, or startup experience.

No gap was converted into a claim. No claim-status marker was added.

## Content changes

- Replaced the general summary with an integrations and distributed-systems summary.
- Focused DexCare bullets on Express, REST APIs, AWS data systems, AI delivery, and Advanced English work with US teams.
- Focused Luizalabs bullets on distributed systems, BullMQ queues, Docker, and GCP.
- Kept dossier metrics for authentication friction, invoice throughput, and processing capacity.

### Fix round 1, 2026-09-04

Source: `state/noemi-sandrini-integrations-backend-engineer-sieve.report.md`, Tier A fixes 1 to 8.

- Placed `Back-end` in the Summary, as a listed Skills token, and in the DexCare booking bullet. Renamed the Skills category label from `Backend and integrations` to `Services` to hold the term at three appearances.
- Placed `third-party API integrations` in the Summary, in Skills, and in a new DexCare bullet on the Epic EMR time-slot sync. The bullet carries the approved 15% wrong-bookings metric.
- Added the approved Shared Platform Initiative bullet with the 33% pilot-friction metric. Written conceptually, no customer names, no `AWS` token, to keep `AWS` at three.
- Rewrote the DexCare AI bullet. It now names validation of AI-generated code, agent environments, shared rules, lint, complexity limits, and testing, per the dossier.
- Cut `workflows` from five to three. The DexCare booking bullet now says `features`. The Lippaus entry-level bullet now says `processes`. All three `agentic workflows` remain.
- Varied bullet verbs. `Supported` no longer opens any bullet. Openers: Delivered, Reduced, Cut, Helped implement, Served, Raised, Collaborated, Shipped, Improved, Kept, Enabled, Increased, Streamlined.
- Raised the role gap from 4pt to 8pt. The PDF stays on one page.
- Title, employers, dates, locations, degree, and contact block unchanged.
- Did not add OAuth 2.0, OIDC, Webhooks, code review, debugging, OOP, SOLID, software design principles, direct client communication, or AWS SQS. Tier B stays open for Lucas.
- Preserved the exact employers, titles, refreshed date periods, locations, education, and contact data.
- Changed the copied role-header macro to the required single-column format.

## Mechanical verification

- `tectonic` completed with exit code 0. It emitted Roboto font request warnings and created the PDF.
- `pdfinfo` reported one letter-size page.
- Raw and layout extraction retained all contact fields, four section headers, four employment blocks, and the education block.
- Source, raw text, and layout text each contained zero Ruby or Rails tokens.
- The resume contained zero unsupported tokens listed in the Maestro brief.
- The rendered page showed no clipping, overlap, or missing content.

