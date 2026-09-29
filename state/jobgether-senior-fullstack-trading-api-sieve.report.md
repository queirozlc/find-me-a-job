# ATS Analysis — resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf vs jobgether-senior-fullstack-trading-api
Segment: agency   Date: 2026-09-04

Artifacts graded (all present on disk):
- PDF: `resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf` (1 page, xdvipdfmx, 0 embedded images, 27,614 bytes, built 17:08 local)
- Source: same directory, `Lucas-Queiroz-Resume-en.tex`
- Raw extraction: `pdftotext Lucas-Queiroz-Resume-en.pdf -` (82 lines)
- Layout extraction: `pdftotext -layout Lucas-Queiroz-Resume-en.pdf -` (59 lines)
- Posting: `jobs/jobgether-senior-fullstack-trading-api.md`, captured 2026-09-04 17:01 America/Sao_Paulo from `https://www.linkedin.com/jobs/view/4461922727/`. 14 applicants. Not labeled Reposted.
- Identity source: `state/hunt-2026-09-04-g-linkedin-identity.json`, Profile Check snapshot of `https://www.linkedin.com/in/queiroz-lucas/details/experience/` captured 2026-09-04T20:01:30+00:00, sha256 `ea38bc6f…50b2a`. The portal was not opened live in this review. Education is verified against the `LinkedIn ground truth — captured verbatim 2026-09-04` block of `DOSSIER.md`, because the cached snapshot covers the experience page only.
- Deterministic gate: `state/jobgether-senior-fullstack-trading-api-deterministic-gate.json`, status PASS, 10 of 10 checks, generated 2026-09-04T20:09:30+00:00.

## Verdict
BLOCKED: File Readability Check

## Decision Explanation

| Check | Requirement | Posting text | Evidence checked | Evidence found | Why it failed | Fix type | Next action |
|---|---|---|---|---|---|---|---|
| File Readability Check 0.8 (0.6 and 0.7 share this cause) | Single-column role header. No table, text box, image of text, icon, or photo. | n/a. The requirement comes from `RUBRIC.md` File Readability Check 0.8 ("Table, text box, image of text, contact icon, photo") and `CV-SPEC.md` item 2 ("Use a single-column role header. Do not use `tabular*`, a table, or a text box."). | `Lucas-Queiroz-Resume-en.tex` lines 39-45; raw extraction lines 22-26, 42-46, 56-60, 66-70, 77-81; layout extraction lines 19-20, 37-38, 46-47, 51-52, 58-59; `pdfimages -list`; `RUBRIC.md` and `CV-SPEC.md` in full; `resumes/base-en.tex`; `reports/jobgether-backend-core-apis-gate0-r1.md`; the Kake and Mavila tailored `.tex` files. | The role header macro is a table: `\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}` … `\end{tabular*}` (`.tex` lines 41-44). Effect in the raw stream: `DexCare` / `Senior Software Engineer` / blank / `Mar 2026 - Present` / `Remote`. Effect in the layout stream: `DexCare … Mar 2026 - Present` then `Senior Software Engineer … Remote`. Every role and the education block show the same pattern. No two roles merge and no role splits. `pdfimages -list` returns no rows. `resumes/base-en.tex` carries the same macro (2 `tabular` hits). The Kake tailored `.tex` (`2026-09-04-e`) already replaced it with two consecutive text lines and passed all 8 checks. | The rubric lists a table as a forbidden construct and the CV spec forbids `tabular*` by name. Earlier reports (for example `reports/jobgether-backend-core-apis-gate0-r1.md`) treated this header as an "accepted exception, set by Lucas 2026-09-01" recorded in `RUBRIC.md`. That text is not in `RUBRIC.md` v3 or in `CV-SPEC.md` today (`grep -i exception` returns nothing), so the exception is not observable and this review cannot apply it. The dates also sit one blank line below the title instead of on or adjacent to it (0.6), and raw and layout disagree on title-versus-date order inside every header (0.7). | CV FIX | The Architect replaces `\resumeSubheading` with the single-column header used in `resumes/hunts/2026-09-04-e/kake-senior-fullstack-engineer-react-golang/Lucas-Queiroz-Resume-en.tex` lines 39-43 (`\textbf{#1} \textbar{} #2 \\[0pt]` then `\textit{#3} \textbar{} \textit{#4}`), rebuilds, re-extracts, then re-runs this review. Note for the Maestro: `scripts/resume_gate.py` `layout` compares the preamble hash against `resumes/base-en.tex`, which still carries `tabular*`, so the header fix will fail that deterministic check until the base is fixed or the check is adjusted. If Lucas confirms the header exception still stands, record it in `RUBRIC.md` and this verdict becomes READY with no other change; every other check below already passes. |

One root cause only. Everything else in this document passes. The rubric
says a File Readability FAIL stops the analysis. The dispatch asked for the
complete rubric report, so the remaining checks are reported below on the
current extraction. The header fix changes only the five header blocks, not
the Summary, Skills, bullets, or metrics, so those results carry over.

## File Readability Check

Judged on the raw extraction.

| # | Check | Result | Offending text |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 82 lines of clean text. |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes (`tr -d -c '\000' \| wc -c` = 0), 0 `?`, 0 characters in U+FB00-U+FB06. Only non-ASCII characters are `•` (16) and `ó` (4). Ligature probe words present in the document extract intact: `back-office` x2, `workflows` x5. `profile`, `efficient`, `conflict` are not in this document, so 0 hits is correct. |
| 0.3 | Contact block recoverable | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. In the body, not a header or footer. No UTC offset, no time-zone sentence. |
| 0.4 | Section headers present verbatim | PASS | Standalone lines `SUMMARY` (5), `SKILLS` (10), `LANGUAGE` (18), `EXPERIENCE` (21), `EDUCATION` (76). Uppercase is `\scshape` rendering; the source strings are `Summary`, `Skills`, `Language`, `Experience`, `Education`. |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks in the raw stream at lines 22, 42, 56, 66, each `Company` / `Title` / `Dates` / `Location` then its bullets, blank line between blocks. Both Lippaus roles repeat the company name, so the promotion segments unambiguously. No merge, no split. |
| 0.6 | Date parseability | FAIL, header only | Every date is `Mon YYYY - Mon YYYY` with an ASCII hyphen: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Each sits one blank line below its title in the raw stream (lines 23/25, 43/45, 57/59, 67/69, 78/80), not on the title line or adjacent to it. Cause: the `tabular*` header. |
| 0.7 | Reading order | FAIL, header only | Raw: `DexCare` / `Senior Software Engineer` / `Mar 2026 - Present` / `Remote`. Layout: `DexCare … Mar 2026 - Present` / `Senior Software Engineer … Remote`. Title and dates swap order inside all five header blocks. Section order, role order, and bullet order are identical in both extractions. Cause: the `tabular*` header. |
| 0.8 | No forbidden constructs | FAIL | `tabular*` role header, `.tex` lines 41-44. No other table, no text box, no image of text, no contact icon, no photo. `pdfimages -list` returns zero rows. |

## Role Eligibility Check

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | Posting: "This position is listed on behalf of a partner company, who manages all applications and next steps. Our partner is looking for a Senior Full-Stack Engineer - Trading API based in Brazil." No authorization, contract, or entity requirement stated. | not stated. `DOSSIER.md` records PJ, CLT, W-8BEN contractor, and EOR as acceptable. |
| Location or time-zone overlap | Posting: "based in Brazil"; card: "Brazil (Remote)"; benefits: "Fully remote working environment." | PASS. CV prints `Vitória, ES, Brazil`. No UTC offset and no overlap sentence on the CV, as `CLAUDE.md` 3 requires. |
| Minimum years of experience | "5+ years of professional full-stack software development experience." | PASS. Summary states "5+ years of full-stack development". Cached LinkedIn span Mar 2021 to Present is 5 yrs 6 mos. The first role title is `Entry-level Fullstack Software Engineer`; React, TypeScript, and Node.js appear across all four roles. |
| English proficiency requirement | Posting is silent. Posting language is English. | not stated. CV prints `English: Fluent (C1)` in the `Language` section. |
| Degree requirement | Posting is silent. | not stated. CV prints `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025`. |
| Required skill: Golang | "Strong professional experience with Golang and TypeScript/React"; "Proficiency in at least one modern systems programming language such as Golang or C#." | Present verbatim. `Go (Golang)` in Skills and in the Luizalabs bullet. The alternative `C#` is correctly absent; it is in no approved source. |
| Required skill: TypeScript | "Proficiency in TypeScript and React" | Present verbatim in Skills and in DexCare bullet 1. |
| Required skill: React | "Proficiency in TypeScript and React, including experience creating intuitive, responsive, and performant user interfaces." | Present verbatim in Skills and in DexCare bullet 5. |
| Required skill: HTML | "Strong knowledge of HTML and modern CSS frameworks" | Present verbatim in Skills and in the Lippaus entry-level bullet. |
| Required skill: TailwindCSS or comparable | "…modern CSS frameworks, particularly TailwindCSS or comparable technologies." | Present verbatim. `TailwindCSS` in Skills and in DexCare bullet 5. `CSS` also in Skills and the Lippaus bullet. Source note under Match limits. |
| Required skill: SQL and relational databases | "Solid experience with SQL and relational databases, preferably PostgreSQL." | Present verbatim. `SQL` and `PostgreSQL` in Skills; DexCare bullet 4 "Modeled booking reads and writes in SQL on PostgreSQL". |
| Required skill: REST APIs and API design | "Strong understanding of REST APIs and API design best practices." | Present verbatim. `REST APIs` and `API design` in Skills; DexCare bullet 3 "Built multi-tenant REST APIs … owning API design and contracts". |
| Requirement: stakeholder requirements into features | "Demonstrated ability to gather, clarify, and translate stakeholder requirements into well-designed, fully implemented features." | Not a retrieval token. Evidence present: Lippaus mid-level bullet "Led project scoping and stakeholder communication that turned stakeholder requirements into production-ready features." Reword of the dossier-approved scoping bullet; facts unchanged. |
| Communication, attention to detail, ownership | "Excellent communication and collaboration skills…"; "Strong attention to detail…"; "Ability to take ownership of complex projects…" | Soft skills, not graded, not tokens. |

Role Eligibility Check: no FAIL.

### LinkedIn field verification, cached snapshot of 2026-09-04T20:01:30+00:00

| CV field | CV prints | Snapshot shows | Result |
|---|---|---|---|
| Role 1 employer / title | `DexCare` / `Senior Software Engineer` | `Senior Software Engineer`, `DexCare · Full-time` | MATCH |
| Role 1 dates | `Mar 2026 - Present` | `Mar 2026 - Present · 7 mos` | MATCH |
| Role 1 location | `Remote` | `Seattle, Washington, United States · Remote` | MATCH per `CLAUDE.md` 3 |
| Role 2 employer / title | `Luizalabs` / `Mid-level Software Engineer` | `Mid-level Software Engineer`, `Luizalabs · Full-time` | MATCH, spelling included |
| Role 2 dates | `Jan 2024 - Mar 2026` | `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | MATCH |
| Role 2 location | `Remote` | `São Paulo, Brazil · Remote` | MATCH per `CLAUDE.md` 3 |
| Role 3 employer / title | `Lippaus Distribuidora` / `Mid-level Software Engineer` | `Lippaus Distribuidora`, `Mid-level Software Engineer` | MATCH |
| Role 3 dates | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024 · 1 yr 1 mo` | MATCH |
| Role 3 location | `Vitória, ES, Brazil` | `Vitória, Espírito Santo, Brazil · On-site` | MATCH per `CLAUDE.md` 3 |
| Role 4 title | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | MATCH |
| Role 4 dates | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023 · 1 yr 11 mos` | MATCH |
| Education | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | `DOSSIER.md` ground truth 2026-09-04: `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | MATCH (ASCII hyphen per `CV-SPEC.md`) |

Both Lippaus roles are kept as separate entries. The Luizalabs role in the
snapshot carries the `Go (Programming Language)` skill tag and lists
"Node.js and Java" in its bullet text; `DOSSIER.md` records "Go at Luizalabs"
among the bullets Lucas approved. The `Go (Golang)` claim is sourced.

## Resume Evidence Check: 90/100, PASS

Required weight 3, preferred weight 1. Placement: absent 0, Skills only 1,
Experience only 2, Skills and one Experience bullet in context 3. Counts are
word-boundary counts on the raw extraction.

### Required tokens

| # | Token | Weight | Skills placement | Experience placement | Points |
|---|---|---|---|---|---|
| 1 | Golang | 3 | `Languages: … Go (Golang)` | Luizalabs: "Built distributed tax microservices in **Go (Golang)**, Node.js, and Java that delivered electronic invoice issuing…" | 3 |
| 2 | TypeScript | 3 | `Languages: TypeScript` | DexCare 1: "Built event-driven **TypeScript** services on Express and Koa that delivered real-time visit booking…" | 3 |
| 3 | React | 3 | `Frontend: React` | DexCare 5: "…monitoring **React** and TailwindCSS interfaces with Datadog RUM." | 3 |
| 4 | HTML | 3 | `Frontend: … HTML` | Lippaus entry-level: "Developed internal back-office dashboards in JavaScript, **HTML**, and CSS…" | 3 |
| 5 | TailwindCSS (or comparable CSS framework) | 3 | `Frontend: … CSS \| TailwindCSS` | DexCare 5: "…monitoring React and **TailwindCSS** interfaces with Datadog RUM." | 3 |
| 6 | SQL / relational databases | 3 | `Languages: … SQL`; `Data: PostgreSQL` | DexCare 4: "Modeled booking reads and writes in **SQL** on **PostgreSQL** with Sequelize and Drizzle ORM…" | 3 |
| 7 | REST APIs | 3 | `Backend: … REST APIs` | DexCare 3: "Built multi-tenant **REST APIs** with Auth0 JWT and OpenAPI/Swagger validation…" | 3 |
| 8 | API design | 3 | `Backend: … API design` | DexCare 3: "…owning **API design** and contracts, that isolated tenant data…" | 3 |
| 9 | 5+ years full-stack | 3 | n/a, eligibility statement | Summary: "**5+ years of full-stack development** in TypeScript, React, Node.js, and Go." Verified span 5 yrs 6 mos. | 3 |

Required subtotal: 9 tokens at 3 points. `sum(points * 3) = 81`, `max = 9 * 3 * 3 = 81`.

### Preferred tokens

| # | Token | Weight | Skills placement | Experience placement | Points |
|---|---|---|---|---|---|
| 1 | PostgreSQL | 1 | `Data: PostgreSQL` | DexCare 4 and Lippaus mid-level 1 ("multi-tenant web and mobile platform on **PostgreSQL**") | 3 |
| 2 | Google Cloud Platform | 1 | `Cloud and operations: … Google Cloud Platform (GCP)` | Luizalabs 4 prints "on **GCP**", not the exact posting token. The Skills line binds the alias, but the rubric scores exact tokens and does not rely on alias expansion. | 1 |
| 3 | Docker | 1 | `Cloud and operations: … Docker` | Luizalabs 4: "Deployed services with **Docker** and Kubernetes on GCP through ArgoCD…" | 3 |
| 4 | Kubernetes | 1 | `Cloud and operations: … Kubernetes` | Luizalabs 4 | 3 |
| 5 | financial markets / fintech | 1 | absent | absent | 0 |
| 6 | algorithmic trading | 1 | absent | absent | 0 |
| 7 | startup | 1 | n/a | Lippaus entry-level: "…workflows of a beverage distribution **startup**." | 2 |
| 8 | fully remote environment | 1 | n/a | `Remote` as the location line of the DexCare and Luizalabs roles | 2 |

Preferred subtotal: `sum(points * 1) = 14`, `max = 8 * 3 * 1 = 24`.

### Score

```
coverage = 100 * (81 + 14) / (81 + 24) = 100 * 95 / 105 = 90.5 -> 90
```

Stuffing penalty: 0. No token appears 4 or more times on a word-boundary
count. Highest counts: `TypeScript` 3, `React` 3, `REST APIs` 3,
`PostgreSQL` 3, `Go` 3. `SQL` standalone 2, `CSS` standalone 2, `Golang` 2,
`TailwindCSS` 2, `HTML` 2, `API design` 2, `Docker` 2, `Kubernetes` 2.
`workflows` appears 5 times; it is not a posting token and is not penalized
here, see defect 4.

**Required tokens without Skills and Experience placement:** none.

### Absences that are correct, not defects

`C#`, `fintech`, `financial`, `trading`, `mentor`, `code review`, `pull
request` all return 0 hits in the raw extraction. The posting offers `Golang
or C#`, and Golang is placed. No domain, mentoring, or protected claim was
invented. The protected claim `code-review` in `claim-allowlist.json` is
absent from the CV, as its `unverified` status requires.

### Prohibition sweep on the raw extraction

| Term | Hits | Result |
|---|---|---|
| Ruby, Rails | 0, 0 | PASS |
| UTC, GMT, time zone, timezone, overlap | 0 | PASS |
| Sidekiq, ActiveRecord, RSpec | 0 | PASS |

Spoken-language proficiency appears only under `LANGUAGE` (raw line 19:
`Portuguese: Native | English: Fluent (C1)`). It is not in Skills. PASS.

### Experience completeness against `resumes/base-en.tex`

The deterministic gate `experience_completeness` PASS records 16 base
bullets and 16 tailored bullets. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26%
are all present. Six bullets were reworded; each stays inside the recorded
facts:

| Tailored wording | Base wording | Judgement |
|---|---|---|
| "…owning API design and contracts, that isolated tenant data…" | "…that isolated tenant data, enforced API contracts…" | Practice token added on a bullet that already carries OpenAPI/Swagger contract validation. Fits the role history. |
| "…in SQL on PostgreSQL with Sequelize and Drizzle ORM, plus DynamoDB Streams…" | "…in PostgreSQL with Sequelize and Drizzle ORM, DynamoDB Streams…" | `SQL` is implied by PostgreSQL. No new fact. |
| "…monitoring React and TailwindCSS interfaces with Datadog RUM." | "…monitoring React with Datadog RUM." | Ecosystem token on the React frontend at DexCare. Authorized by the match policy the dispatch cites. Not in the `DOSSIER.md` DexCare stack list, see Match limits. |
| "…in Go (Golang), Node.js, and Java…" | "…in Node.js, Java, and Go…" | Reorder plus the posting's spelling in parentheses. Sourced, see above. |
| "…turned stakeholder requirements into production-ready features." | "…turned customer requirements into delivered solutions." | Mirrors the posting's phrase. Same fact. |
| "…dashboards in JavaScript, HTML, and CSS…" | "…dashboards in JavaScript…" | Ecosystem tokens implied by JavaScript dashboards. No new fact. |

## Recruiter Readability Score: 91/100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 15/15 | `Senior Software Engineer` and `full-stack` are on raw line 6 of 82 (7%). The posting title is `Senior Full-Stack Engineer - Trading API`; the CV keeps the LinkedIn-true title, which `CLAUDE.md` 1 requires. Not a deduction. |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | 12/20 | DexCare bullets 1 (TypeScript backend services) and 3 (REST APIs, API design) carry posting tokens. Bullet 2 (Epic EMR) carries none. The posting's frontend emphasis (React, TailwindCSS) sits at bullet 5 and the SQL/PostgreSQL proof at bullet 4. Golang evidence is in the second role only, which the facts require. |
| 3.3 | Every bullet starts with a past-tense action verb and describes an outcome | 15/15 | All 16 bullets: Built, Integrated, Built, Modeled, Reduced, Built, Helped implement, Built, Moved, Built, Deployed, Built, Processed, Led, Developed, Built. No present tense, no "Responsible for", no third person. Summary uses `I`. |
| 3.4 | At least 3 bullets carry a real, defensible number | 15/15 | Seven bullets: 15%, 25%, 7%, 33%, 20%, 18%, 26%. Every one traces to the metric list in `DOSSIER.md`. |
| 3.5 | Experience completeness, page count | 10/10 | Nothing removed, 16 of 16 bullets. One page. |
| 3.6 | No unsupported buzzwords | 10/10 | No "team player", "results-driven", or "passionate". "high-quality code" is the dossier's own wording. |
| 3.7 | Skills grouped by category | 10/10 | Six labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing, observability, and AI tooling. |
| 3.8 | Scannable spacing and white space | 4/5 | Role headers are bold and consistent. In the layout extraction the last bullet of a role and the next role header sit on adjacent lines (layout lines 36-37, 45-46, 50-51). `\resumeRoleGap` is 3pt. `CV-SPEC.md` item 2 asks for clear vertical space between the last bullet and the next role. |

## Defects, ranked by cost

1. **`tabular*` role header** — File Readability Check 0.8, with 0.6 and 0.7 as consequences — blocking. Replace `.tex` lines 39-45 with the single-column macro from the Kake tailored file: `\textbf{#1} \textbar{} #2 \\[0pt]` then `\textit{#3} \textbar{} \textit{#4}`. Rebuild and re-extract. Fix type CV FIX. See the Decision Explanation for the base-parity note on `scripts/resume_gate.py`.
2. **Frontend proof is fifth in the DexCare block** — Recruiter Readability 3.2 — not blocking. Move "Reduced release risk by 7% by shipping behind LaunchDarkly/OpenFeature flags and monitoring React and TailwindCSS interfaces with Datadog RUM." to position 2 or 3, ahead of "Integrated Epic EMR time-slot flows…". Reorder only, no text change.
3. **`Google Cloud Platform` has Skills placement only** — Resume Evidence Check, preferred, not blocking. In the Luizalabs deploy bullet, print "on Google Cloud Platform (GCP)" once in place of "on GCP". Raises the preferred token from 1 to 3 points and the coverage from 90 to 92. Keeps the term at 2 appearances.
4. **`workflows` appears 5 times** — human-scan repetition, not blocking, not a rubric penalty. Occurrences: Skills `Agentic workflows`, Summary "agentic workflows", DexCare 6 "agentic workflows", Luizalabs 3 "fiscal workflows", Lippaus entry-level "workflows of a beverage distribution startup". Optional: reword one of the last two, for example "fiscal operations".
5. **No blank line between the last bullet of a role and the next header in the layout stream** — Recruiter Readability 3.8 — not blocking. Raise `\resumeRoleGap` if the page still holds one page after the header fix.

## Match limits

- Preferred tokens not placed: `financial markets` / `fintech` (0), `algorithmic trading` (0). No approved source records trading, market data, or fintech work. The Luizalabs domain is fiscal invoicing, which is not the same thing and was correctly not relabeled. Do not add these without Lucas.
- `Google Cloud Platform` at 1 point, see defect 3.
- `TailwindCSS` is placed on the DexCare React frontend under the match policy for ecosystem tokens. `DOSSIER.md` lists the DexCare frontend as React and `date-fns` and does not name a CSS framework. This review does not reject the token. It records that the source is policy, not a dossier entry, so Lucas can confirm it in the screening answer where the application note already states it.
- Posting title `Senior Full-Stack Engineer` is not printed; the CV prints the LinkedIn title `Senior Software Engineer` with "full-stack development" in the Summary line, as the title rule requires.
