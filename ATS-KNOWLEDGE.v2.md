# ATS Knowledge Base v2

Draft 2026-09-29. It replaces `ATS-KNOWLEDGE.md` only after Lucas approves it.
Raw research with full citations: `~/career/research/` and the source list at
the end of this file.

This file is a procedure, not an essay. Read section 0, then only the sections
that the procedure names.

---

## 0. Procedure for one application

1. **Detect the ATS** from the apply URL (section 3). Write `ats_profile` into
   `state/<application>-manifest.json`. If no pattern matches, use `generic`.
2. **Extract requirements by posting section.** Required tokens come from the
   requirements or qualifications section. Preferred tokens come from the
   nice-to-have section. Tokens in the company description or responsibilities
   are context, not criteria (U5).
3. **Resolve every token against the Skills policy** in `DOSSIER.md` with
   the claim policy (section 2). Each token gets one result: `CLAIM` or
   `GAP`. Ask Lucas only for gray-zone tokens.
4. **Tailor** with the universal rules (section 1) plus the adjustments of the
   detected profile (section 4).
5. **Prepare the form pack.** For profiles where forms or profile fields are
   scored (Gupy, LinkedIn, Workable, Workday), list the exact answers and
   field contents for Lucas. The agent never submits.
6. **Gate** with `RUBRIC.md`. A `GAP` is a match limit, never a CV defect.

---

## 1. Universal rules

Every rule has an ID, a tier, and a test. The Analyzer cites the ID.

Tiers: **[DOC]** vendor documentation or source code. **[ENG]** paper or
engineering blog by the company that built the system. **[REG]** regulatory
filing or audit. **[SIM]** vendor test without published method. **[FOLK]**
no traceable source; never optimize for it. **[INF]** our inference from
documented behavior; label it when used.

### Parse

| ID | Rule | Tier | Test |
|---|---|---|---|
| P1 | Text-layer PDF, no image of text, no scan. | DOC (Textkernel, SAP, Greenhouse) | `pdftotext` output is complete |
| P2 | Single column. No table, text box, icon, photo, graphic. | DOC (Greenhouse parse-failure list, OpenResume) | raw and layout extraction have the same block order |
| P3 | Contact block in the body, never in header or footer. | DOC (Greenhouse; OpenCATS reads only `word/document.xml`) | email, phone, city, LinkedIn in raw text |
| P4 | Canonical section headers. | DOC (OpenResume heading rules) | headers are standalone lines |
| P5 | Each role is one clean block: company, title, dates, location, bullets. | DOC-adjacent (Resumap Textkernel test: 5/36 templates merged roles) | no merged or split roles in raw text |
| P6 | Dates `Mon YYYY - Mon YYYY`. | DOC | regex on every role |
| P7 | No ligature glyphs in extracted text. | DOC (pypdf #1351, PDFBox, Bugzilla 1810914) | grep `workflow`, `office`, `profile` |
| P8 | File under 2.5 MB. | DOC (Greenhouse will not parse above 2.5 MB) | `ls -l` |

### Retrieval and match

| ID | Rule | Tier | Test |
|---|---|---|---|
| U1 | Every `CLAIM` token appears literally, in the posting's spelling. Recruiter search is boolean and literal. | DOC (Greenhouse, Lever, LinkedIn Recruiter boolean help) | grep raw text |
| U2 | Write acronym and long form once: `Amazon Web Services (AWS)`, `Continuous Integration (CI/CD)`. | DOC (Lever search does not expand abbreviations) [P-snip] | both forms present |
| U3 | Every `CLAIM` token is in `Skills` and in one Experience bullet of its anchored role (section 2.3). Semantic engines weight skills with context. | ENG (LinkedIn Skills Graph), DOC (Eightfold) | placement table in RUBRIC |
| U4 | Put the strongest tokens in the most recent role. Eightfold scores recent skills separately. | DOC (Eightfold eng blog) | token present in current role |
| U5 | Weight posting sections: requirements and qualifications first, then nice-to-have. A skill in the qualifications section is more important than one in the company description. | ENG (LinkedIn Skills Graph) | manifest splits required and preferred |
| U6 | Target title in the top of the document and in the LinkedIn headline. Title is a structured field in every ranker we can read. | ENG (LinkedIn Galene), DOC (Greenhouse, HiredScore, Eightfold) | title in first 15% |
| U7 | State seniority explicitly: `Senior` in the title, `5+ years` in the Summary. Seniority is a ranking feature. | ENG (Ha-Thuc 2015) | both present |
| U8 | Canonical skill names (`Node.js`, `PostgreSQL`, `Amazon Web Services (AWS)`). Engines normalize to taxonomies (ESCO, LinkedIn 39K skills). | DOC (SmartRecruiters ESCO), ENG (LinkedIn) | no custom names |
| U9 | No term more than 3 times. Hidden or white text is visible in the ATS plain-text view. | DOC (plain-text view), FOLK (penalty size) | count per token |
| U10 | Screening questions are the main automatic rejection point. Answer them exactly and truthfully. | DOC (LinkedIn must-have, Workable auto-disqualify, Taleo, Gupy eliminatórias, Recruitee, JazzHR) | form pack reviewed by Lucas |
| U11 | An unexplained gap over 6 months is a common filter. | DOC (HBS Hidden Workers 2021) | no gap today |

---

## 2. Claim policy

Set by Lucas 2026-09-29. The objective is to match the posting as closely as
the ATS can measure, inside the technologies Lucas knows. The posting decides
what enters the CV. Lucas decides only the gray zone.

### 2.1 Sources

The **Skills policy** in `DOSSIER.md`:

- **Attested umbrella.** Families of technologies Lucas attests he knows.
  Added automatically.
- **Blacklist.** Blocked categories and tokens (2.4). Never added.
- **Gray zone.** Undefined or unclear: in no umbrella family and not
  blacklisted. Ask Lucas once.
- **Whitelist.** Gray-zone tokens Lucas approved. Never ask twice.

### 2.2 Token results

| Result | Condition | Action |
|---|---|---|
| `CLAIM` | Token is in the umbrella or on the whitelist. | Add it automatically: `Skills` plus one bullet in its anchored role (2.3). No confirmation. |
| `GAP` | Token is blacklisted, or is gray zone and Lucas has not answered. | Never write it. Ask Lucas once for a gray-zone token and record the answer in the whitelist or blacklist. It lowers coverage and never blocks as a CV defect. |

### 2.3 Placement and relations

- **Anchored placement.** A `CLAIM` token goes into one bullet of the role
  whose domain fits it best: fiscal and invoicing at Luizalabs, healthcare
  scheduling at DexCare, orders and distribution at Lippaus. Write it as part
  of that role's work. Example: SQS goes into a fiscal or invoicing flow at
  Luizalabs. Interview defense is Lucas's responsibility; agents never filter
  a token for interview risk.
- **Only what the posting asks.** An umbrella token that the posting does not
  ask for stays out, except base CV content and stack-depth blocks.
- **Stack depth: requested token plus its building blocks.** When the posting
  asks for a higher-level token (framework, platform, managed service), add
  the lower-level umbrella tokens it is built on or competes with. Put them
  in `Skills`, grouped next to the requested token. Examples: posting asks NestJS, add `Express`, `Fastify`. Posting asks
  Next.js, add `React`, `Node.js`. Posting asks Prisma, add `PostgreSQL`,
  `Drizzle ORM`. Posting asks Kubernetes, add `Docker`, `Helm`.
  Why it helps: boolean searches often use OR groups (`NestJS OR Express OR
  Fastify`), embedding engines score in-domain tokens as closer to the posting
  [INF], and the human reads depth under the framework. It costs one line.
  The reverse direction adds little: a posting for Express or Fastify gains
  almost nothing from `NestJS`. Keep it in `Skills` only if it is already
  there, never add a bullet for it.
- **Extra sibling tokens.** No vendor documents a penalty for skills that the
  posting did not ask for. Criteria engines (Ashby, Workable, HiredScore,
  Teamtailor, Recruitee, Pinpoint) grade each criterion and ignore the rest.
  Embedding engines (Eightfold, Gupy, LinkedIn two-tower) may lose some
  similarity from off-target text [INF]. Rule: an unrequested sibling may stay
  in `Skills`. It does not get a bullet.
- **Patterns.** CQRS, event sourcing, DDD, idempotency, retry with DLQ, saga:
  the bullet names what the mechanism separated or protected. A pattern word
  without a mechanism reads as a buzzword to the human reader.

### 2.4 Blacklist: blocked

Never added for a posting (Lucas, 2026-09-29). They move embedding similarity
and recruiter perception toward a job family Lucas does not want. The
exception column is the only way a related token enters.

| Category | Examples | Exception |
|---|---|---|
| IT support and helpdesk | Zendesk, Freshdesk, ServiceNow, Jira Service Management as an agent, "ticket handling", "user support" | Built an integration with the product's API: write it as an integration, for example `Zendesk API integration`. |
| Manual QA | test case execution, manual regression | Automated tests are engineering: keep Vitest, Jest, Playwright. |
| Sysadmin and ops-only | server administration, on-call as the main duty | On-call as part of owning a service is fine. |
| BI and data analyst | Power BI, Tableau, Excel reporting | Building a data pipeline is engineering. |
| CRM and platform admin | Salesforce admin, HubSpot admin | API integration, as above. |
| Primary languages outside the target stack | Java, Python, Ruby, Elixir, PHP, C# | A true fact may stay inside the bullet of the role (Java at Luizalabs). Never in `Skills`, never in the Summary. |
| Management titles and duties that exceed the target level | "managed a team of 8" when it did not happen, "Engineering Manager" | Mentoring and leading a project are fine when true. |

### 2.5 Never

- A credential, certification, degree, or regulated-domain qualification that
  Lucas does not hold. His real degree (Information Systems, FAESA) always
  stays.
- A yes on a screening question when the true answer is no. Screening answers
  are attestations, and they are the main automatic rejection point (U10).
- A years-of-experience number that the dates do not support.
- A metric that is not in the DOSSIER.
- A change to title, date, employer, location, or language level.

---

## 3. ATS detection

Match the apply URL, after redirects. First match wins.

| Pattern | Profile | Tier |
|---|---|---|
| `linkedin.com/jobs/view/...` with Easy Apply | `linkedin-easy-apply` | DOC |
| `*.gupy.io/jobs/<id>`, `portal.gupy.io` | `gupy` | verified live 2026-09-29 |
| `jobs.ashbyhq.com/<board>/<id>` | `ashby` | DOC, verified live 2026-09-29 |
| `*.myworkdayjobs.com/...` | `workday` | P-snip |
| `boards.greenhouse.io/...`, `job-boards.greenhouse.io/...` | `greenhouse` | P-snip |
| `jobs.lever.co/...`, `jobs.eu.lever.co/...` | `lever` | DOC |
| `apply.workable.com/...` | `workable` | P-snip |
| `careers-*.icims.com/...` | `icims` | P-snip |
| `jobs.smartrecruiters.com/...` | `smartrecruiters` | S |
| `*.teamtailor.com/jobs/...` | `teamtailor` | P-snip |
| `*.recruitee.com/...` | `recruitee` | S |
| `*.pinpointhq.com/...` | `pinpoint` | S |
| `*.breezy.hr/...` | `breezy` | S |
| `*.applytojob.com/...` | `jazzhr` | P-snip |
| `*.bamboohr.com/careers/...` | `generic` (no AI ranking found) | S |
| `jobs.deel.com/...` | `deel` | P-snip |
| `*.inhire.app/...`, `form-app.inhire.app/...` | `inhire` | P-snip |
| `*.vagas.solides.com.br/...` | `solides` | P-snip |
| email, WhatsApp, Google Form, custom page | `generic` | — |

A custom career domain can hide the ATS. Check the apply form's page source
for the vendor host before falling back to `generic`.

---

## 4. ATS profiles

Each profile lists what the scorer reads, how it ranks, where it rejects,
and the tailoring adjustments on top of section 1. **No vendor publishes
weights.** Everything below is inputs and output format.

### `gupy` (Brazil)

- **Scorer:** Gaia, aderência 0 to 100, highest first. "Mathematical
  similarity" between posting, candidate profile, and candidate answers.
  Company sets mandatory and desirable requirements, seniority, competencies.
  [DOC, gupy.io blog]
- **Reads:** the Gupy profile fields **Habilidades** and **Experiências**.
  The CV file is parsed into those fields. **The company sees the structured
  profile, not the file.** Older Gupy posts say tests and the fit cultural
  test also feed the ranking; newer pages mention only the profile fields.
  Current state: not observable. [DOC]
- **Rejects:** only on eliminatory additional questions. Missing requirements
  lower the rank. [DOC]
- **Adjust:**
  - Portuguese. The profile is the CV. The master profile holds, in
    Habilidades, the umbrella tokens most requested across the saved postings
    in `jobs/`, and each Experiência names tokens by anchored placement. The form pack per posting holds only the
    additional-question answers.
  - Gupy prefers DOCX upload for parsing. Lucas reviews every parsed field.
  - Complete every test. Treat them as ranked until shown otherwise.
- **One profile for all postings.** A Gupy profile is usually not changed per
  posting. Tailoring happens once, on a master Gupy profile built from the
  DOSSIER Skills policy. Per posting, only the additional questions and tests
  change. A `GAP` cannot be closed per posting, so the apply decision uses
  required coverage (RUBRIC) against the master profile.

### `linkedin-easy-apply`

- **Scorer:** Skills Match: explicit profile skills, implicit skills from
  profile text (headline, About, titles, position descriptions), and
  same-country location. "Top applicant" means top 50% by current role,
  experience, and skills. Hiring Assistant (paid) ranks against recruiter
  criteria and reads profile and resume. [DOC]
- **Reads:** the **profile first**. The resume is attached, but only Hiring
  Assistant and the human read it.
- **Rejects:** a screening question marked "must-have qualification"
  auto-archives and sends a rejection email. [DOC]
- **Adjust:**
  - The LinkedIn profile is the scored document. Profile Skills must hold the
    posting's `CLAIM` tokens and be linked to the role where used.
  - Same-country location lowers Skills Match for a US posting [INF from the
    documented location input]. Nothing to fix; know it.
  - Form pack: every screening answer, with the numeric years per skill that
    the dates support.

### `ashby`

- **Scorer:** recruiter defines up to 50 criteria. AI marks each as meets,
  does not meet, or undecided, with citations. Recruiters sort by percentage
  met. [DOC]
- **Reads:** resume, and whether long-form answers are substantive.
- **Rejects:** no automatic rejection documented.
- **Adjust:** one explicit, quotable sentence per posting requirement, so the
  AI can cite it. Undecided is the loss case: avoid indirect evidence. Answer
  long-form questions fully.

### `workday` (HiredScore)

- **Scorer:** grade A to D. B = all basic qualifications. A = all basic, most
  preferred, and an average match above a threshold. [DOC]
- **Reads:** resume vs job description skills and qualifications; title,
  location, minimum years, education level, and major. [DOC, P-snip]
- **Rejects:** knockout questionnaire answers [S].
- **Adjust:** cover every basic qualification literally first (B), then
  preferred (A). State total years explicitly. Workday forms re-ask work
  history: the form pack copies titles and dates from LinkedIn ground truth.

### `greenhouse`

- **Scorer:** Talent Matching buckets Strong, Good, Partial, Limited, Needs
  manual review, against a calibration of skills, experience, titles, and
  industry, each weighted. Several terms map to one calibrated skill. [DOC]
- **Reads:** the resume: skills, years, titles, dates, company names, derived
  industry.
- **Rejects:** "does not auto-reject or auto-advance". [DOC]
- **Adjust:** industry is derived from company names. Put the domain in the
  role line or first bullet (`healthcare scheduling`, `e-commerce fiscal`).
  "Rare formatting" goes to manual review: keep the base layout.

### `lever`

- **Scorer:** Talent Fit, binary fit with strengths and considerations, off
  by default. [P-snip]
- **Reads:** resume, application answers, job requirements.
- **Adjust:** U2 matters most here: search does not expand abbreviations.

### `workable`

- **Scorer:** must-have = 2 points, nice-to-have = 1, partial = half,
  normalized to 100%. Reads "completeness of candidate input". [DOC]
- **Rejects:** **yes**. "Auto-disqualify" removes applicants who miss a
  criterion marked "Disqualify if not met". [DOC]
- **Adjust:** fill every optional form field. Every must-have `CLAIM` gets an
  explicit sentence. A must-have `GAP` is a likely auto-disqualify: report it
  to Lucas before he applies.

### `teamtailor`, `recruitee`, `pinpoint`, `deel`

- **Scorer:** per-criterion checklists (met / not met / unknown, or X of Y).
  [DOC]
- **Reads:** resume, cover letter (Teamtailor, Recruitee), application
  answers, custom fields.
- **Rejects:** Recruitee knockout questions can disqualify [P-snip].
  Teamtailor can auto-advance, not reject.
- **Adjust:** when a cover letter field exists, write one line per required
  criterion with its evidence. It is read by the scorer.

### `icims`, `smartrecruiters`

- **Scorer:** iCIMS Role Fit (skills and experience) [S]. SmartRecruiters
  Winston Match, stars with Skills, Experience, Education subscores [P-snip],
  skills normalized to ESCO [DOC].
- **Adjust:** U8 canonical names. Education line complete.

### `breezy`, `jazzhr`

- Breezy: match 0 to 10, computed once at apply time, never recomputed [DOC].
  Apply with the final CV only. JazzHR: knockout questions can remove the
  applicant [P-snip].

### `inhire`, `solides`, `abler` (Brazil)

- Rank by aderência. **Salary expectation is a ranking input** (InHire, Abler).
  Sólides and Abler use behavioural tests (Profiler, DISC). [P, P-snip]
- **Adjust:** the form pack flags the salary field for Lucas. Complete the
  tests.

### `generic` (fallback)

Use when no pattern matches, or for email and WhatsApp applications. Apply
section 1 fully. Assume a human reads first and a boolean search runs later
on the stored text. Keep the full-width base layout. No profile-specific
adjustment.

---

## 5. LinkedIn Recruiter (sourcing, not applying)

Recruiter search ranks the profile when nobody applied.

- Query: canonical titles, skills, company, location, plus boolean keywords.
  Stop words ignored. [ENG, DOC]
- Ranker trained on **InMail accepted**, not on relevance. Answer every
  InMail, including a polite no. [ENG]
- Features: title match, fraction of the query's skills held, seniority from
  title qualifiers, location, shared connections, companies, and schools,
  profile views, how often recruiters contact the member. [ENG]
- Keyword fields highlighted: headline, About, Experience title and
  description, Skills. [DOC]
- Remote workplace filter returns only Open to Work members and ignores
  location. Open to Work: recruiters only, Remote. [DOC]
- Fairness re-ranking by gender runs on all Recruiter searches. [ENG]

---

## 6. Myths. Never optimize for these.

| Claim | Status |
|---|---|
| "75% of resumes are auto-rejected" | FOLK. Preptel sales claim, 2012, no method. |
| "The ATS rejects a resume below score N" | Mostly false. Current vendor docs rank, they do not reject. Automatic rejection comes from knockout questions and Workable criteria. A 0 to 100 score does exist in Gupy and Workable, but it orders the queue. |
| "Match rate must be 75-80%" | FOLK. Jobscan's own metric, formula unpublished. |
| White-text keywords | False. Visible in the ATS plain-text view. |
| "+40% callbacks from numbers", "2x from tailoring" | FOLK. |

---

## 7. Not observable

- Score weights for every vendor, including under NYC Local Law 144 audits.
- Whether Gupy tests still feed the ranking.
- Workday parser behavior and PDF vs DOCX preference.
- Whether Open to Work changes Recruiter ranking, beyond the filter.
- Whether endorsements or skill pin order change ranking.

---

## Sources

Gupy: gupy.io/blog/gaia-inteligencia-artificial-gupy · gupy.io/inteligencia-artificial · gupy.io/blog/algoritmos-de-ordenacao · gupy.io/blog-do-emprego/como-funciona-a-ordenacao-da-gupy · gupy.io/blog-do-emprego/preenchimento-de-curriculo
LinkedIn: linkedin.com/help/recruiter/answer/a593591 (Skills Match) · a7109476 (Hiring Assistant) · linkedin.com/help/linkedin/answer/a519651 (must-have) · a512348 (Easy Apply) · a415295 (Recruiter search) · arXiv 1809.06481, 1809.06473, 1602.04572, 1905.01989 · linkedin.com/blog/engineering/skills-graph/extracting-skills-from-content
Workday: doc.workday.com/hiredscore/.../reference--candidate-grades.html · workday.com/en-us/legal/responsible-ai-and-bias-mitigation.html
Greenhouse: support.greenhouse.io articles 41131886674075, 200989175, 202360199
Ashby: docs.ashbyhq.com/ai-assisted-application-review
Workable: help.workable.com/hc/en-us/articles/38381544828695
Lever: lever.co/blog/levers-ai-innovations-are-here · help.lever.co article 28081525270685
Teamtailor: support.teamtailor.com/en/articles/10209597 · Recruitee: support.recruitee.com/en/articles/12984798 · Pinpoint: help.pinpoint.support/en/articles/13574273 · Breezy: help.breezy.hr/en/articles/6389729 · Deel: deel.com/solutions/hire/ats
Eightfold: eightfold.ai/engineering-blog/ai-powered-talent-matching-the-tech-behind-smarter-and-fairer-hiring · SmartRecruiters AI whitepaper · Oracle: docs.oracle.com/.../evaluate-candidate-applications-using-ai-matching-ratings.html
Abler: blog.abler.com.br/como-funciona-o-ranking-de-triagem-da-abler · InHire: inhire.com.br/ia · Sólides: solides.com.br/blog/solides-matcher-compare-perfis-e-cargos
Parsing: developer.textkernel.com · github.com/opencats/OpenCATS lib/DocumentToText.php · github.com/xitanggg/open-resume
Filters: HBS/Accenture "Hidden Workers" 2021 · Taleo prescreening docs
