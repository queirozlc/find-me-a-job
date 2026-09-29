# Master Career Dossier, Lucas Queiroz

This file is the candidate-authorized source for resume content and match
policy.

**Status: ACTIVE.** This file does not use claim-status markers.

## Match policy

ATS match is the first objective after eligibility and primary-stack triage.
Use this weight order:

1. **Primary language or runtime, weight 4.** Accept JavaScript, TypeScript,
   Node.js, and Go. Drop a posting when its primary requirement is Ruby or
   Rails, Java, Python, PHP, C# or .NET, or another outside stack. Never change
   the CV to a different primary language for that posting.
2. **Frameworks and libraries, weight 3.** Match the posting's exact terms in
   `Skills` and in one relevant `Experience` bullet. Express, Fastify, NestJS,
   React, Next.js, Angular, Vite, and similar terms do not decide eligibility.
3. **Data, messaging, cloud, and tools, weight 2.** Match exact required terms
   in `Skills` and in one relevant `Experience` bullet.
4. **Practices and adjacent terms, weight 1.** Match exact posting terms when
   they fit the role history.

Do not change titles, dates, employers, degree, location, metrics, contract
status, work authorization, or language proficiency to improve a match. Do
not invent a posting, recruiter, primary programming language, credential, or
regulated-domain qualification.

---

## Identity
- Name: Lucas Queiroz
- Location: Vitória, ES, Brazil
- Portuguese proficiency: Native.
- English proficiency: Fluent (C1). Daily English-only work with US teams at
  DexCare.
- Contract types available: PJ with own CNPJ, US contractor with W-8BEN, CLT,
  and EOR or Deel-style employment. All are acceptable.
- Notice period: Not recorded.

## Open questions for Lucas
Agents append missing screening facts here. Do not infer an answer.

Appended 2026-09-01 by Maestro after the base CV draft:
1. Resolved 2026-09-01: see bullet metrics above.
2. Resolved 2026-09-01: see bullet metrics above.
3. Resolved 2026-09-01: see the DexCare AI entry below.
4. Resolved 2026-09-04: English is Fluent (C1). Portuguese is Native.
5. Contract types available: PJ, CLT, W-8BEN contractor, own CNPJ.
6. Notice period.
7. Resolved 2026-09-01: both full-time, Luizalabs direct CLT.

---

## Seeded career data, read from repos on disk 2026-09-01

Read directly from `~/dexcare/*/package.json` and `tsconfig` presence by
Maestro. This is observation, not a claim from an old resume. Safe to use.

### DexCare, current role
**Language: TypeScript on Node.js across every service. No Ruby exists at
DexCare.**

Services on disk: `intelligence-engine`, `visit-booking`,
`IntegratedScheduling`, `scheduling-apis`, `forq-availability`, `common`,
`Vanir`. All carry a `tsconfig`. None carries a `Gemfile`.

- Web: **Express**, **Koa**
- Data: **PostgreSQL** (`pg`), **Sequelize**, **Drizzle ORM**, **DynamoDB**
  and DynamoDB Streams, **Redis**
- Cloud: **AWS SDK v3** — S3, STS, Secrets Manager, RDS Signer
- Flags: **LaunchDarkly**, **OpenFeature**
- API contracts: **OpenAPI / Swagger** (`swagger-parser`,
  `express-openapi-validator`)
- Observability: **Datadog** RUM and browser logs
- Auth: **Auth0**, multi-tenant JWT (SCH-343)
- Frontend: **React**, `date-fns`
- Domain: **Epic EMR integration** (`emr-epic-interconnect`, `emr-time-slot`),
  event-driven booking, healthcare scheduling at scale

Still needed from Lucas: scale numbers (RPS, patient volume, latency, team
size) and which of these he personally owned versus used.

### Magazine Luiza / LuizaLabs, previous
- **Direct CLT employee, full-time.** Corrected by Lucas 2026-09-01. The earlier "through Fullstack Labs" entry was wrong. Context only, not printed on the CV.
- Stack: **Node, Java, and others**. **Not Rails.**
- Everything else previously recorded for this employer (fiscal/NF-e/SEFAZ
  domain, Sidekiq, PostgreSQL tuning, GCP, ArgoCD) came from the retired
  Rails-framed resume and is not a source for this dossier.

### Existing artifacts are not sources
`~/Documents/Resumes/`: `Lucas_Node_Resume.pdf`, `Lucas_ResumeV2.pdf`,
`Lucas_Resume.pdf`, `resume.pdf`, `recruiter_message_en.md`,
`recruiter_message_pt.md`.
These were written under the retired Rails positioning. Do not copy claims
from them.

### Bullet voice, resolved 2026-09-02
Lucas decided: first person, past tense, subject omitted in bullets
(`Built X, measured by Y, by doing Z`). Summary uses `I` explicitly. The
2026-09-01 "bare verb, never first person" rule is retired. `CV-SPEC.md`
Bullets and Summary sections and `RUBRIC.md` 3.3 carry the rule.

---

## Career data supplied by Lucas on 2026-09-01

- Degree: **Information Systems** (FAESA).
- Location on documents: **Vitória, ES, Brazil**.
  **Never print a UTC offset on the resume.** It is GMT-3; state time-zone
  overlap in prose when a posting gates on it.
- Luizalabs / Magazine Luiza: **Mid-level Software Engineer**, direct CLT,
  full-time. Corrected 2026-09-01.
- **Titles and dates come from LinkedIn, strictly.** Never from an old resume,
  never reconstructed, never adjusted to fit a posting. See `CLAUDE.md` rule 1.
  Verbatim strings captured 2026-09-01, see **LinkedIn ground truth** below.
- **Stack substitution rule.** Drop every Rails-world component and use its
  JS/TS equivalent: Sidekiq to **BullMQ**, ActiveRecord to **Drizzle**,
  ActiveJob to **BullMQ**, RSpec to **Vitest**/**Jest**, and the same rule for
  any tool not listed.
  Note: this is consistent with Lucas's own account that LuizaLabs was Node
  and Java, not Rails. The Rails entries in the old resumes were the
  fabrication; the substitution moves toward the truth, not away from it.
  Exact framework and tool terms from an accepted posting can be used under
  the weight policy above.

### Additional career data supplied on 2026-09-01

- **Luizalabs domain was fiscal / NF-e / SEFAZ.** Distributed tax microservices, electronic invoice issuing, state tax authority integration, fiscal back-office dashboards.
- **Tools used at Luizalabs and Lippaus:** BullMQ, Docker, Kubernetes, GCP, ArgoCD, Vitest, Jest.
- **Bullet voice:** first person, past tense, subject omitted (`Built`, `Reduced`, `Helped build`). Summary uses `I`. Superseded the bare-verb rule on 2026-09-02. Format every bullet as XYZ: accomplished X, measured by Y, by doing Z. Name the tech stack in the bullet.
- **Portuguese CV headers are translated:** `Resumo`, `Habilidades`, `Experiência`, `Formação`, `Idiomas`. The RUBRIC File Readability Check, item 0.4, carries the allowlist.
- **AI mention required** in Experience bullets and in Summary.
- **AI tools used: Claude Code, Codex.** Agentic workflows integrated into development. Skills token set: `Claude Code | Codex | Agentic workflows`. Summary claim: "Integrates AI-driven agentic workflows to accelerate development cycles."
- **Lippaus and Luizalabs bullets approved by Lucas:** multi-tenant web and mobile platform on PostgreSQL, BullMQ job processing, project scoping and stakeholder communication, back-office dashboards in JavaScript, customer-facing features end to end, Go at Luizalabs, Lippaus stack PostgreSQL / BullMQ / JavaScript / React Native.
- **AI at DexCare:** uses Claude Code and Codex in daily delivery. Built the agent environments: shared rules, codebase enforcement (lint, cyclomatic complexity limits, testing) so agentic workflows produce high-quality code. One DexCare Experience bullet in XYZ format carries this. **No AI bullet for Luizalabs**; Claude Code barely existed when Lucas left.
- **Company spelling: `Luizalabs`**, as on LinkedIn. Final.
- **Bullet metrics supplied by Lucas 2026-09-01.** IDs refer to the bullet list in `reports/base-cv-draft.md` order at round 5:
  - D1 (booking services): no number. Leave as is (Lucas, final).
  - D2 (Epic EMR time-slot sync): reduced wrong bookings by 15%.
  - D3 (Auth0 JWT multi-tenant APIs): reduced authentication friction by 25%.
  - D5 (feature flags): release risk reduced by 7%.
  - L2 (SEFAZ async BullMQ): 20% improvement in invoice processing throughput.
  - L3 (fiscal dashboards): 18% fewer support tickets.
  - P2 (Lippaus BullMQ jobs): 26% more processing capacity.
  - D1, D4, D6, L1, L4, P1, P3, E1, E2: no number. Leave as is.
  - New DexCare bullet D7: helped implement the SPI environment, which isolates clients into multi-tenant environments, reducing friction for piloting new clients by 33%. SPI = Shared Platform Initiative (read from DexCare Confluence 2026-09-01: https://dexcare.atlassian.net/wiki/spaces/SPI/pages/20029833239/Shared+Platform+Initiative and .../20305412099/SPI+Multi-Tenant+Architecture+Overview). Concept: move from single-tenant deployments, one AWS environment per customer, to a shared multi-tenant platform where clients share deployed service instances with isolated configuration, secrets and data stores. Describe conceptually on the CV, no technical depth. Do not print internal customer names.
- **DexCare messaging: RabbitMQ / AMQP** used on services. Skills token only (`RabbitMQ`, `AMQP`), no service names on the CV.
- **Role locations.** DexCare and Luizalabs print `Remote`; Seattle and São Paulo are employer cities and never appear. Lippaus prints `Vitória, ES, Brazil`, matching LinkedIn (On-site, Vitória).
- **Time-zone overlap is never printed on the CV.** It is answered in the apply note screening answers only.
- **Headline.** Lucas will change the LinkedIn headline from `Senior Full-Stack Software Engineer` to `Senior Software Engineer` himself. Agents never edit the profile. CV title stays `Senior Software Engineer`.
- **Do not print** "Works remotely from Brazil with US-based teams" or any equivalent sentence. Lucas sees no value in it.

### Excluded content

- **Rails core / community gem contribution.** Claimed in `Lucas_Resume.pdf`
  and `Lucas_ResumeV2.pdf` with no commit, PR, or gem named. Not answered yet.
  Do not use it unless Lucas adds the source details.
- **CV format specification.** Lucas has existing formats tied to ATS parsing.
  Being defined.

---

## LinkedIn ground truth — captured verbatim 2026-09-04

Read off the English primary profile. **This is the only source for titles and
dates.** Do not normalize, translate, or tidy. Company spelling included.

### Experience

```
Senior Software Engineer
DexCare · Full-time
Mar 2026 - Present · 7 mos
Seattle, Washington, United States · Remote

Mid-level Software Engineer
Luizalabs · Full-time
Jan 2024 - Mar 2026 · 2 yrs 3 mos
São Paulo, Brazil · Remote

Lippaus Distribuidora
Full-time · 2 yrs 11 mos
Vitória, Espírito Santo, Brazil · On-site

    Mid-level Software Engineer
    Jan 2023 - Jan 2024 · 1 yr 1 mo

    Entry-level Fullstack Software Engineer
    Mar 2021 - Jan 2023 · 1 yr 11 mos
```

### Education

```
FAESA
Bachelor's degree , Information Systems
Feb 2022 – Dec 2025
```

### What this corrects in the Overleaf template

The template is wrong on every one of these. Fix before any build.

| Template says | LinkedIn says |
| --- | --- |
| `LuizaLabs` `Jan 2024 - Present` | `Luizalabs` `Jan 2024 - Mar 2026` — **the role ended** |
| DexCare absent entirely | `Senior Software Engineer` `DexCare` `Mar 2026 - Present` — **the current role is missing** |
| `Lippaus` one entry, `May 2021 -- Jan 2024` | `Lippaus Distribuidora`, **two roles**: `Entry-level Fullstack Software Engineer` `Mar 2021 - Jan 2023`, then `Mid-level Software Engineer` `Jan 2023 - Jan 2024` |
| — | The Lippaus **promotion** is a real seniority signal the old resumes flattened away. Keep both roles. |

### Discrepancy resolved 2026-09-01

LinkedIn shows both DexCare and Luizalabs as `Full-time`. Lucas supplied this
employment detail:
both are full-time, Luizalabs was direct CLT. The earlier "through Fullstack
Labs" note was an error. No LinkedIn change needed.
