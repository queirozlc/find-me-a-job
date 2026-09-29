# ATS Analysis — resumes/hunts/2026-09-04-e/kake-senior-fullstack-engineer-react-golang/Lucas-Queiroz-Resume-en.pdf vs kake-senior-fullstack-engineer-react-golang
Segment: us-direct   Date: 2026-09-04

Artifacts graded (all present on disk):
- PDF: `resumes/hunts/2026-09-04-e/kake-senior-fullstack-engineer-react-golang/Lucas-Queiroz-Resume-en.pdf` (1 page, xdvipdfmx, 0 embedded images)
- Source: same directory, `Lucas-Queiroz-Resume-en.tex`
- Raw extraction: `pdftotext Lucas-Queiroz-Resume-en.pdf -` (66 lines)
- Layout extraction: `pdftotext -layout Lucas-Queiroz-Resume-en.pdf -` (62 lines)

LinkedIn verification: read live through the Profile Check portal on
2026-09-04, read-only. Pages read:
`https://www.linkedin.com/in/queiroz-lucas/details/experience/` and
`https://www.linkedin.com/in/queiroz-lucas/details/education/`.

## Verdict
BLOCKED: Resume Evidence Check

## Decision Explanation

| Check | Requirement | Posting text | Evidence checked | Evidence found | Why it failed | Fix type | Next action |
|---|---|---|---|---|---|---|---|
| Resume Evidence Check (required token `code reviews`) | Participation in code reviews | "Participate in code reviews and help uphold strong engineering standards" | `DOSSIER.md` in full; `resumes/base-en.tex` in full; `state/` is not a claim source | None found. The dossier's DexCare AI entry records only "shared rules, codebase enforcement (lint, cyclomatic complexity limits, testing)". Base CV bullet reads "...cyclomatic complexity limits, and tests that enabled agentic workflows to produce high-quality code in daily delivery." Neither text contains code review, pull request, or review. | The tailored DexCare bullet adds "upheld engineering standards in code reviews". No approved source records Lucas performing or participating in code reviews. The required token has mechanical Skills + Experience placement, but the Experience placement rests on a claim with no traceable source, so the token cannot be credited. | LUCAS CONFIRMATION | Ask Lucas whether he participates in code reviews and where, then have the Architect rewrite the bullet on his answer. Do not delete the token before he answers; the approved sources are silent, which is not the same as absent experience. |

One root cause only. It is cross-referenced in the token table below.

## File Readability Check

Judged on the raw extraction.

| # | Check | Result | Offending text |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 66 lines of clean text. |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes, 0 `?`, 0 characters in U+FB00-U+FB06. Only non-ASCII characters are `ó` and `•`. Ligature probe words present in the document extract intact: `back-office` x2, `workflow(s)` x5. `profile`, `efficient`, `conflict` are not in this document, so 0 hits is correct, not a defect. |
| 0.3 | Contact block recoverable | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. In the body, not a header or footer. |
| 0.4 | Section headers present verbatim | PASS | Standalone lines `SUMMARY` (5), `SKILLS` (11), `LANGUAGE` (21), `EXPERIENCE` (24), `EDUCATION` (63). Uppercase rendering allowed; the source strings are `Summary`, `Skills`, `Language`, `Experience`, `Education`. |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks in the raw stream, each `Company \| Dates` then `Title \| Location` then bullets, with a blank line between blocks at raw lines 40, 49, 56. No merge, no split. The tailored `.tex` replaced the base `tabular*` role header with a single-column header, which is what produces this result. |
| 0.6 | Date parseability | PASS | `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. All `Mon YYYY - Mon YYYY`, ASCII hyphen, on the line immediately above the title line. |
| 0.7 | Reading order | PASS | Raw and layout extraction carry the same block order and the same sentence order. Only leading whitespace and blank-line placement differ. |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` returns zero images. No table, text box, image of text, contact icon, or photo. |

## Role Eligibility Check

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | Posting states "🌎 Remote \| LATAM" and "💰 Paid in USD". It states no work authorization or entity requirement. | not stated |
| Location or time-zone overlap | "🌎 Remote \| LATAM". The job file records "The Kake listing shows GMT-3 for this specific role." | PASS. CV prints `Vitória, ES, Brazil`, inside LATAM. The CV prints no UTC offset and no time-zone sentence, as required. Overlap is answered in the apply note only. |
| Minimum years of experience | "5+ years of professional software engineering experience" | PASS. Summary states "5+ years". LinkedIn-verified span Mar 2021 to Present is 5 yrs 6 mos. |
| English proficiency requirement | Posting is silent. | not stated. CV prints `English: Fluent (C1)` in the `Language` section. |
| Degree requirement | Posting is silent. | not stated. CV prints `FAESA \| Feb 2022 - Dec 2025`, `Bachelor's degree, Information Systems`. |
| Required skill: Go/Golang | "Strong Golang experience" | Present verbatim. `Go (Golang)` in Skills, `Go` in the Luizalabs bullet. Depth is a match limit, see below. |
| Required skill: React | "Comfortable being backend-heavy while still contributing to React when needed" | Present verbatim in Skills and in the DexCare Datadog bullet. |
| Required skill: service-oriented architecture | "solid service-oriented architecture skills" | Present verbatim in Skills and in the first DexCare bullet. |
| Required skill: cloud infrastructure (AWS) | "Production experience with cloud infrastructure (ideally AWS)" | Present verbatim. `AWS` in Skills; `AWS SDK v3` in the DexCare data bullet. |
| Required skill: Docker, Kubernetes | "Hands-on with modern backend tooling such as Docker, Kubernetes..." | Present verbatim in Skills and in the Luizalabs deployment bullet. |
| Required skill: gRPC (or equivalent) | "...gRPC, Kafka (or equivalent)" | PASS on the alternative. `REST APIs` and `OpenAPI/Swagger` in Skills and in the DexCare multi-tenant API bullet. `gRPC` is correctly absent; it is not in any approved source and was not invented. |
| Required skill: Kafka (or equivalent) | "...gRPC, Kafka (or equivalent)" | PASS on the alternative. `BullMQ` in Skills and in two Experience bullets. `RabbitMQ` and `AMQP` in Skills only, which is what `DOSSIER.md` instructs ("Skills token only... no service names on the CV"). `Kafka` is correctly absent. |
| Required skill: relational and/or NoSQL databases | "Experience with relational and/or NoSQL databases" | Present verbatim in Skills and in the DexCare data bullet. |
| Required skill: code reviews | "Participate in code reviews and help uphold strong engineering standards" | **FAIL.** See the Decision Explanation. Present verbatim in the CV, but with no source in `DOSSIER.md` or `base-en.tex`. |

### LinkedIn field verification, read 2026-09-04 through Profile Check

Every title, employer, date, location, and the degree on the CV matches the
live profile. Read-only; the profile was not edited.

| CV field | CV prints | LinkedIn shows | Result |
|---|---|---|---|
| Role 1 employer / title | `DexCare` / `Senior Software Engineer` | `Senior Software Engineer`, `DexCare · Full-time` | MATCH |
| Role 1 dates | `Mar 2026 - Present` | `Mar 2026 – Present · 7 mos` | MATCH (ASCII hyphen per `CV-SPEC.md`) |
| Role 1 location | `Remote` | `Seattle, Washington, United States · Remote` | MATCH per `CLAUDE.md` 3 (employer city never printed) |
| Role 2 employer / title | `Luizalabs` / `Mid-level Software Engineer` | `Mid-level Software Engineer`, `Luizalabs · Full-time` | MATCH, including the `Luizalabs` spelling |
| Role 2 dates | `Jan 2024 - Mar 2026` | `Jan 2024 – Mar 2026 · 2 yrs 3 mos` | MATCH |
| Role 2 location | `Remote` | `São Paulo, Brazil · Remote` | MATCH |
| Role 3 employer / title | `Lippaus Distribuidora` / `Mid-level Software Engineer` | `Lippaus Distribuidora`, `Mid-level Software Engineer` | MATCH |
| Role 3 dates | `Jan 2023 - Jan 2024` | `Jan 2023 – Jan 2024 · 1 yr 1 mo` | MATCH |
| Role 3 location | `Vitória, ES, Brazil` | `Vitória, Espírito Santo, Brazil · On-site` | MATCH per `CLAUDE.md` 3 |
| Role 4 title | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | MATCH |
| Role 4 dates | `Mar 2021 - Jan 2023` | `Mar 2021 – Jan 2023 · 1 yr 11 mos` | MATCH |
| Education | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | MATCH |

Both Lippaus roles are kept as separate entries. The promotion is preserved.

## Resume Evidence Check: 84/100, FAIL

Required weight 3, preferred weight 1. Placement: absent 0, Skills only 1,
Experience only 2, Skills and one Experience bullet in context 3.

### Required tokens

| # | Token | Weight | Skills placement | Experience placement | Points |
|---|---|---|---|---|---|
| 1 | Go / Golang | 3 | `Languages: Go (Golang)` | Luizalabs: "Built distributed tax microservices in **Go**, Node.js, and Java..." | 3 |
| 2 | React | 3 | `Frontend: React` | DexCare: "...adding observability to **React** with Datadog RUM metrics and browser logging." | 3 |
| 3 | backend services | 3 | `Backend: Backend services` | DexCare: "Built event-driven TypeScript **backend services** on Express and Koa..." | 3 |
| 4 | sync and async workloads | 3 | `Messaging and workloads: ... Sync and async workloads` | DexCare: "...for **sync and async workloads**, that delivered real-time visit booking..." | 3 |
| 5 | service-oriented architecture | 3 | `Backend: ... Service-oriented architecture` | DexCare: "...in a **service-oriented architecture** for sync and async workloads..." | 3 |
| 6 | AWS / cloud infrastructure | 3 | `Cloud and operations: AWS` | DexCare: "...wired to S3 and RDS through **AWS** SDK v3." | 3 |
| 7 | Docker | 3 | `Cloud and operations: ... Docker` | Luizalabs: "Deployed services with **Docker** and Kubernetes on GCP via ArgoCD..." | 3 |
| 8 | Kubernetes | 3 | `Cloud and operations: ... Kubernetes` | Luizalabs: "...Docker and **Kubernetes** on GCP via ArgoCD..." | 3 |
| 9 | gRPC or equivalent API tooling | 3 | `Backend: ... REST APIs \| OpenAPI/Swagger` | DexCare: "Built multi-tenant **REST APIs** with Auth0 JWT and **OpenAPI/Swagger** validation..." | 3 |
| 10 | Kafka or equivalent messaging | 3 | `Messaging and workloads: RabbitMQ \| AMQP \| BullMQ` | Luizalabs: "Moved SEFAZ calls to asynchronous **BullMQ** queues..."; Lippaus: "...by moving the work to asynchronous **BullMQ** jobs." | 3 |
| 11 | relational and/or NoSQL databases | 3 | `Data: Relational and NoSQL databases \| PostgreSQL \| DynamoDB \| Redis` | DexCare: "Modeled booking reads and writes across **relational and NoSQL databases**, PostgreSQL... DynamoDB Streams, and Redis..." | 3 |
| 12 | testing | 3 | `Testing and AI tooling: Vitest \| Jest` | DexCare: "...cyclomatic complexity limits, and **testing**..."; Luizalabs: "...Vitest and Jest tests gating CI/CD." | 3 |
| 13 | observability | 3 | `Observability and practices: ... Observability` | DexCare: "...adding **observability** to React with Datadog RUM metrics and browser logging." | 3 |
| 14 | performance | 3 | `Observability and practices: ... Performance` | Lippaus: "Improved processing **performance** for high-volume orders, notifications, and integrations, adding 26% more capacity..." | 3 |
| 15 | reliability | 3 | `Observability and practices: ... Reliability` | Luizalabs: "...raising invoice throughput by 20% and **reliability** through fault tolerance." | 3 |
| 16 | scalability | 3 | `Observability and practices: ... Scalability` | DexCare: "...and improving platform **scalability** by replacing per-customer environments with shared service instances..." | 3 (evidence caveat, defect 2) |
| 17 | **code reviews** | 3 | `Observability and practices: ... Code reviews` | DexCare: "...that upheld engineering standards in **code reviews**..." — **placement present, evidence not traceable to any approved source** | **0** |
| 18 | 5+ years | 3 | n/a, eligibility statement | Summary: "Senior Software Engineer with **5+ years**..." Verified span Mar 2021 to Present = 5 yrs 6 mos | 3 |

Required subtotal: 17 tokens at 3 points, 1 token at 0 points.
`sum(points * 3) = 153`, `max = 18 * 3 * 3 = 162`.

### Preferred tokens

| # | Token | Weight | Skills placement | Experience placement | Points |
|---|---|---|---|---|---|
| 1 | feature flags | 1 | `Cloud and operations: ... Feature flags \| LaunchDarkly \| OpenFeature` | DexCare: "...shipping behind LaunchDarkly/OpenFeature **feature flags**..." | 3 |
| 2 | metrics | 1 | `Observability and practices: ... Metrics` | DexCare: "...Datadog RUM **metrics** and browser logging." | 3 (evidence caveat, defect 3) |
| 3 | logging | 1 | `Observability and practices: ... Logging` | DexCare: "...and browser **logging**." | 3 |
| 4 | A/B testing / experimentation | 1 | absent | absent | 0 |
| 5 | tracing | 1 | absent | absent | 0 |
| 6 | incident response | 1 | absent | absent | 0 |
| 7 | regulated / high-compliance (literal token) | 1 | absent | absent as a literal token. The domains are present as facts: Epic EMR healthcare scheduling at DexCare, SEFAZ fiscal invoicing at Luizalabs. | 0 |
| 8 | fintech | 1 | absent | absent | 0 |
| 9 | crypto | 1 | absent | absent | 0 |
| 10 | Web3 | 1 | absent | absent | 0 |

Preferred subtotal: `sum(points * 1) = 9`, `max = 10 * 3 * 1 = 30`.

### Score

```
coverage = 100 * (153 + 9) / (162 + 30) = 100 * 162 / 192 = 84.4 -> 84
```

Stuffing penalty: 0. No requirement token appears 4 or more times on a
word-boundary count. Highest counts are `Go` 3, `React` 3, `AWS` 3,
`BullMQ` 3, `PostgreSQL` 3, `backend services` 3, `observability` 3.

**Required tokens without credited Skills and Experience placement:**
`code reviews`. The missing part is not the placement, it is the source. See
the Decision Explanation, listed there once.

### Absences that are correct, not defects

`gRPC`, `Kafka`, `A/B`, `tracing`, `incident`, `fintech`, `crypto`, `Web3` all
return 0 hits in the raw extraction. The posting writes "gRPC, Kafka (or
equivalent)", and the equivalents are placed. Nothing was invented.

### Prohibition sweep on the raw extraction

| Term | Hits | Result |
|---|---|---|
| Ruby | 0 | PASS |
| Rails | 0 | PASS |
| UTC | 0 | PASS |
| GMT | 0 | PASS |
| time zone / timezone / overlap | 0 / 0 / 0 | PASS |
| Sidekiq, ActiveRecord, RSpec | 0 | PASS |

Spoken-language proficiency appears only under the `LANGUAGE` header
(raw line 22: `Portuguese: Native \| English: Fluent (C1)`). It is not in
`Skills`. PASS.

### Experience completeness against `resumes/base-en.tex`

No verified role, bullet, or metric was removed.

| Role | Base bullets | Tailored bullets | Metrics in base | Metrics in tailored |
|---|---|---|---|---|
| DexCare | 7 | 7 | 15%, 25%, 7%, 33% | 15%, 25%, 7%, 33% |
| Luizalabs | 4 | 4 | 20%, 18% | 20%, 18% |
| Lippaus, Mid-level | 3 | 3 | 26% | 26% |
| Lippaus, Entry-level | 2 | 2 | none | none |

All rewording stays inside the facts, with two exceptions carried as defects
1 and 2 below. Reordering "Node.js, Java, and Go" to "Go, Node.js, and Java"
in the Luizalabs bullet is allowed reordering; `DOSSIER.md` records "Go at
Luizalabs" among the bullets approved by Lucas, and the live LinkedIn role
carries the `Go (Programming Language)` skill tag.

## Recruiter Readability Score: 91/100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 15/15 | `Senior Software Engineer` is on raw line 6 of 66, which is 9%. The posting title is `Senior Full-Stack Engineer`; the CV keeps the LinkedIn-true title, which `CLAUDE.md` 1 requires. Not a deduction. |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | 12/20 | DexCare bullets 1 and 3 are highly relevant (backend services, service-oriented architecture, sync and async workloads, REST APIs). Bullet 2 is Epic EMR, which carries no posting token. The single strongest posting signal, Go, is absent from the whole DexCare block; the only Go evidence sits in the second role. For a posting headlined "Strong Go/Golang backend experience", the top of the document does not lead with Go. |
| 3.3 | Every bullet starts with a past-tense action verb and describes an outcome | 15/15 | All 16 bullets: Built, Integrated, Built, Modeled, Reduced, Built, Helped, Built, Moved, Built, Deployed, Built, Improved, Led, Developed, Built. No present tense, no "Responsible for", no third person. Subject omitted. Summary uses `I`. |
| 3.4 | At least 3 bullets carry a real, defensible number | 15/15 | Seven bullets carry one: 15%, 25%, 7%, 33%, 20%, 18%, 26%. Every one traces to the metric list in `DOSSIER.md`. |
| 3.5 | Experience completeness, page count | 10/10 | Nothing removed, see the table above. One page. |
| 3.6 | No unsupported buzzwords | 10/10 | No "team player", "results-driven", or "passionate". "high-quality code" is the dossier's own wording for the DexCare agent environments. |
| 3.7 | Skills grouped by category | 10/10 | Eight labelled groups: Languages, Backend, Messaging and workloads, Data, Frontend, Cloud and operations, Observability and practices, Testing and AI tooling. |
| 3.8 | Scannable spacing and white space | 4/5 | Role headers are bold and consistent, and the raw stream carries a blank line between roles. In the layout extraction the last bullet of a role and the next role header sit on adjacent lines with no blank line. `\resumeRoleGap` is 3pt, and the page margins were widened past the base (`\topmargin -.6in`, `\textheight +1.2in`). The page is very dense. `CV-SPEC.md` item 2 asks for clear vertical space between the last bullet and the next role. |

## Defects, ranked by cost

1. **`code reviews` claim has no source** — Resume Evidence Check, blocking. The DexCare bullet reads "...and testing that **upheld engineering standards in code reviews** and enabled agentic workflows to produce high-quality code in daily delivery." `DOSSIER.md` records only "shared rules, codebase enforcement (lint, cyclomatic complexity limits, testing)"; `base-en.tex` reads "...and tests that enabled agentic workflows to produce high-quality code in daily delivery." No approved source contains code review, pull request, or review. Fix type LUCAS CONFIRMATION. Ask Lucas; do not delete the token before he answers, and do not record that he lacks the experience.

2. **`scalability` is attached to the SPI bullet as an outcome the dossier does not state** — Resume Evidence Check, not blocking. The bullet reads "...reducing new-client pilot friction by 33% **and improving platform scalability** by replacing per-customer environments with shared service instances...". `DOSSIER.md` D7 records the architecture change (single-tenant environments to shared service instances) and the 33% pilot-friction figure. It does not record a scalability result. The architecture change is real and recorded, so the word describes the recorded change rather than inventing a new one, and the 33% stays correctly attached to pilot friction. Still a characterization, not a stated fact. Fix type LUCAS CONFIRMATION. Ask Lucas to confirm the phrasing, or have the Architect anchor `scalability` on a bullet where a number already carries it.

3. **`metrics` is not the dossier's word for the Datadog evidence** — Resume Evidence Check, preferred token, not blocking. The bullet reads "Datadog RUM **metrics** and browser logging." `DOSSIER.md` records "Observability: Datadog RUM and browser logs". Fix type LUCAS CONFIRMATION. Ask Lucas whether he worked with Datadog metrics as such, or have the Architect print "Datadog RUM and browser logging", which matches the source exactly.

4. **The Summary puts Go first across a 5+ year claim** — Recruiter Readability and honesty, not blocking. It reads "Senior Software Engineer with 5+ years building **backend-heavy Go**, TypeScript, Node.js, and React systems." The approved sources record Go at Luizalabs only, `Jan 2024 - Mar 2026`, alongside Node.js and Java. `DOSSIER.md` states DexCare is "TypeScript on Node.js across every service". A reader takes the sentence to mean Go across 5+ years. Fix type CV FIX. The Architect can keep Go in the sentence and scope it to the record, for example naming the languages without implying Go spans the whole period.

5. **No Go evidence anywhere in the most recent role block** — Recruiter Readability 3.2, not blocking, and not fixable by writing. The current role is TypeScript-only in every approved source, so this is a true property of the history, not a document defect. It costs 8 points on 3.2 and it is the largest single ranking risk against a Go-first posting. Fix type ROLE MISMATCH in part; nothing can be added without inventing Go work at DexCare.

6. **Vertical space between roles is thin** — Recruiter Readability 3.8, not blocking. `\resumeRoleGap` is 3pt and the layout extraction shows a role header directly under the previous bullet. Fix type CV FIX. Increase the gap. Segmentation still passes, so this is cosmetic, not a parse risk.

## Match limits

Preferred tokens not placed: `A/B testing` / experimentation platforms,
`tracing`, `incident response`, `fintech`, `crypto`, `Web3`, and the literal
regulated / high-compliance tokens. None of these appears in an approved
source, and none was invented. The regulated-domain evidence is present as
fact rather than as the posting's token: Epic EMR healthcare scheduling at
DexCare and SEFAZ fiscal invoicing at Luizalabs.

Two further limits, both outside the CV's control:

- **Go depth is not observable.** The posting asks for "Strong Golang
  experience". The approved sources place Go at one Mid-level role among
  three languages, with no depth, ownership, or scale figure. The CV states
  what is recorded and no more. Whether that clears the bar is Kake's call.
- **Observability evidence is frontend-only.** The posting asks for
  observability as an end-to-end ownership item. The only recorded
  observability tooling is Datadog RUM and browser logs, which is React-side.
  Backend observability, tracing, and incident response are not recorded.

The `gRPC, Kafka (or equivalent)` requirement is satisfied on the alternative
and is not a limit: REST APIs with OpenAPI/Swagger contracts carry the API
tooling, BullMQ carries the messaging, and RabbitMQ with AMQP sit in Skills
exactly as `DOSSIER.md` directs.
