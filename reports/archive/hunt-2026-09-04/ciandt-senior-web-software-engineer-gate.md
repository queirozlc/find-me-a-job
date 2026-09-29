# ATS Analysis — resumes/hunts/2026-09-04/ciandt-senior-web-software-engineer/Lucas-Queiroz-Resume-en.pdf vs ciandt-senior-web-software-engineer
Segment: agency (the posting file records `Segment: agency`; company origin international, 25+ countries)   Date: 2026-09-04

## Verdict
BLOCKED at Gate 1.

Gate 2 also fails on required-token placement. One more blocker sits outside the gate rows:
two role date ranges contradict both the live LinkedIn profile and the refreshed `DOSSIER.md`.

Gate 0 is fully PASS, with one parse-robustness regression recorded under 0.5 that does not
trip the rubric's FAIL condition.

## Sources actually read
- `~/career/AGENTS.md`, `~/career/RUBRIC.md`, `~/career/ATS-KNOWLEDGE.md`, `~/career/CV-SPEC.md`,
  `~/career/DOSSIER.md` (re-read today, after the 2026-09-04 refresh).
- `~/career/jobs/ciandt-senior-web-software-engineer.md` (posting text plus Maestro brief).
- The CV source `.tex` and the compiled PDF, plus both extractions.
- `Profile Check` portal, read-only, no edit action sent:
  - https://www.linkedin.com/in/queiroz-lucas/details/experience/
  - https://www.linkedin.com/in/queiroz-lucas/details/education/
- The posting URL https://www.linkedin.com/jobs/view/4454020765/ was **not** re-opened. Posting
  text is quoted from the local job file only.
- The four PDFs under `~/Documents/Resumes/` were not opened. They are invalid sources.
- The sibling build `resumes/hunts/2026-09-04/tractian-senior-backend-engineer/` was used once,
  as a controlled comparison for the Gate 0.5 note. No claim about the CI&T CV rests on it.

## Extraction step (mandatory, performed first)
```
pdftotext -layout Lucas-Queiroz-Resume-en.pdf - > extracted-layout.txt
pdftotext         Lucas-Queiroz-Resume-en.pdf - > extracted-raw.txt
```
Gate 0 and Gate 2 are judged on the raw file. 55 lines. 1 page.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 55 clean lines. `pdfimages -list` returns zero images, so the page is not a scan. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00-U+FB06. Zero `\x00`, zero U+FFFD. Probe words extract intact: `workflows` (lines 7, 14, 27, 47), `office` (lines 36, 47), `fiscal` (line 36). The `fontspec` + `Ligatures=NoCommon` fix in the source works. |
| 0.3 | Contact block recoverable, in the body | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. Source has `\pagestyle{empty}` and the block sits inside `\begin{center}` in the body, not a header or footer. |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 10, 16, 49 carry `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION` as standalone lines. Source strings are `Summary`, `Skills`, `Experience`, `Education`. Uppercase rendering is allowed by the rubric. |
| 0.5 | Employment-block segmentation | PASS, **with a recorded regression** | Four separate blocks, none merged and none split: DexCare (17-28), Luizalabs (29-36), Lippaus Distribuidora Mid-level (37-42), Lippaus Distribuidora Entry-level (43-47). Each block prints Company / Title / Location / Dates on four consecutive lines, and each Lippaus role repeats its own company line, so the promotion cannot collapse. **The regression:** unlike the sibling build in this same hunt, no blank line separates the last bullet of one role from the next company name. Raw lines 27-29 read `...enforcing code / quality. / Luizalabs`. Same at 36-37 and 42-43. See the note below the table. |
| 0.6 | Date parseability | PASS **on parseability only** | Each role carries `Mon YYYY - Mon YYYY` on its own line adjacent to the title: lines 20, 32, 40, 46, 53. ASCII hyphen throughout, no EN DASH. **Two of the values are wrong. See Factual integrity.** |
| 0.7 | Reading order | PASS | Raw and layout agree on every adjacent block: name, contact, Summary, Skills, the four roles in the same order, Education. |
| 0.8 | No forbidden constructs | PASS | Source uses `itemize` only. No `tabular`, no `tabular*`, no `tcolorbox`, no `minipage`. `pdfimages -list` is empty, so no photo and no icon. |

### Note on 0.5, the blank-line regression

The rubric's FAIL condition for 0.5 is "Any two roles merged into one block, or one role split
into two, in the raw stream." Neither happens here, so the row is a PASS and I do not inflate it
into a failure. But the strongest segmentation signal in the stream is weaker than it was
yesterday, and `ATS-KNOWLEDGE.md` section 2 records that employment-block segmentation is the
only real failure mode the Textkernel template test found, 5 of 36 templates.

Controlled comparison, same hunt, same day, same content shape:

| Build | Blank lines in raw extraction | Blank line at each role boundary |
|---|---|---|
| `tractian-senior-backend-engineer` | 9 | yes, at all three boundaries |
| `ciandt-senior-web-software-engineer` | 6 | no, at none of the three |

The three missing blanks are exactly the three role boundaries. Two macro edits differ between
the builds and are the candidates: `\resumeSubheading` gained `\small` on the location and date
lines and tightened `\\[-2pt]` to `\\[-1pt]`, while `\resumeRoleGap` grew from `\vspace{2pt}` to
`\vspace{4pt}`. **I did not isolate which edit removed the blank line, and I do not assert a
cause.** The visual gap is larger, not smaller, which is why the result is counter-intuitive and
worth a rebuild test rather than a guess.

## Gate 1 — Knockouts

The posting has one requirement block, "Required Skills & Experience". It has no bonus or
preferred section, so every listed item is required.

| Check | Source | Result | Evidence |
|---|---|---|---|
| Work authorization / entity type | posting | not stated | The posting names no authorization or entity type. Employment type shows `Full-time`, location `Brazil`, workplace `Remote`. |
| Location or time-zone overlap | posting | not stated | No overlap window stated. CV prints `Vitória, ES, Brazil` and prints no UTC offset, as CLAUDE.md rule 3 demands. |
| Minimum years of experience | posting | not stated | The posting says "Senior" and "experienced" but names no number. CV Summary claims `5+ years`; LinkedIn gives Mar 2021 to Sep 2026, 5 yrs 6 mos. |
| Degree requirement | posting | not stated | No degree is required. CV carries `Bachelor's degree, Information Systems`, FAESA, anyway. |
| Modern web application development | posting | PASS | "Strong hands-on experience with modern web application development." Evidence: Summary line 6 "building web applications", DexCare bullet 1 (React with TypeScript services), Lippaus bullet "multi-tenant web and mobile platform". |
| JavaScript **and** TypeScript | posting | PASS | Cumulative, both named. `JavaScript` Skills line 11, Experience lines 36 and 47. `TypeScript` Skills line 11, Experience line 22. |
| **React and Next.js, or directly comparable modern web frameworks** | posting | **FAIL** | `React` is fully placed: Skills line 12, Experience line 21. **`Next.js` has 0 occurrences** and `DOSSIER.md` records no Next.js fact. The posting's escape clause is "or directly comparable modern web frameworks"; the CV names no framework offered in that place. React is one of the two terms the posting already asked for, not a comparable substitute for the other, and React is the library Next.js is built on rather than a peer of it. I will not convert that into a pass. RUBRIC Gate 1: absent resume evidence is a FAIL. This preserves the uncertainty the Maestro brief asked me to preserve. |
| Software engineering principles, programming logic, **clean code**, testing, debugging, maintainability | posting | PASS on substance, one token gap | `testing`, `debugging`, `maintainability` each in Skills line 13 and Experience line 25. `clean code` has 0 occurrences; the CV writes `code quality` instead (lines 26, 28). "Software engineering principles" and "programming logic" are discarded as buzzwords per RUBRIC Step 1. |
| **CMS concepts, content modeling, APIs, integrations, modern CMS architectures** | posting | **FAIL** | `APIs` and `integrations` are fully placed. **`CMS` has 0 occurrences and `content model` has 0 occurrences.** `DOSSIER.md` records no CMS fact anywhere. The Maestro brief lists this correctly as unsupported. This is the posting's central initiative, named in the role summary as "a CMS modernization and migration initiative". |
| **Familiarity with PHP-based applications** | posting | **FAIL** | **`PHP` has 0 occurrences.** `DOSSIER.md` records no PHP fact. The posting asks only for reading, debugging and navigating an existing PHP codebase, and says "Deep PHP specialization is not required", so this is a low bar, but the CV supplies no evidence at all and I will not invent one. |
| **Analyzing functional and non-functional requirements, contributing to technical implementation decisions** | posting | **FAIL, and fixable from DOSSIER.md** | `requirements` has 0 occurrences. No bullet describes requirements analysis or a technical decision. Unlike CMS and PHP, this **is** supported: `DOSSIER.md` records, under bullets approved by Lucas, "project scoping and stakeholder communication" and "customer-facing features end to end" for Lippaus. The Architect dropped that bullet from this build. |
| Practical experience using AI coding assistants or AI-enabled development tools in the SDLC | posting | PASS | `AI coding assistants` Skills line 14, Experience line 27. `agentic workflows` Skills line 14, Experience line 27. Also Summary line 7. Traced to `DOSSIER.md` "AI at DexCare". |
| **Ability to design and document technical solutions, integrations, application workflows, and data flows** | posting | **FAIL** | `integrations` is placed; `workflows` appears at lines 7, 14, 27, 47. But `document` and `documentation` have 0 occurrences, and `data flow` has 0 occurrences. No bullet describes designing or documenting a technical solution. `DOSSIER.md` records no documentation fact, so this is not fixable from local sources today. See the escalation note below. |
| **Advanced English communication skills** | posting | **FAIL, and fixable from DOSSIER.md** | **`English` has 0 occurrences in this CV.** It is a stated required item here, not a bonus. `DOSSIER.md` Identity records it plainly: "English proficiency: Advanced / C1. Daily English-only work with US teams at DexCare." **The Maestro brief is wrong on this row.** It lists "Advanced English" under "Required tokens or facts not supported by DOSSIER.md". It is supported, verbatim, and the sibling `tractian` build in this same hunt carried `Advanced English (C1)` on its Skills line. This build dropped it, on the posting where it is required rather than a bonus. |

## Gate 2 — Retrieval coverage: 67/100, FAIL

Scoring convention, stated so the run is reproducible and identical to the convention used on
the `tractian` report:
- An **alternative set** in the posting is scored once, on the best-placed member that
  `DOSSIER.md` actually supports.
- Hard requirements that can never occupy `Skills` or `Experience` (a degree, a years count, a
  capability narrative such as "analyzing functional and non-functional requirements") live in
  Gate 1 only and are excluded from the denominator here. Scoring them would force an
  artificial 0 that says nothing about retrieval.
- Placement points: absent 0, `Skills` only 1, `Experience` only 2, both 3.
- The posting has **no preferred tier**. Every item sits under "Required Skills & Experience",
  so the preferred set is empty and weight 3 applies throughout.

| # | Requirement, posting wording | Token scored | Skills | Experience | Points |
|---|---|---|---|---|---|
| R1 | "Strong experience with JavaScript and TypeScript" | `JavaScript` | line 11 | lines 36, 47 | 3 |
| R2 | same, cumulative second half | `TypeScript` | line 11 | line 22 | 3 |
| R3 | "Hands-on experience with React and Next.js" | `React` | line 12 | line 21 | 3 |
| **R4** | same requirement, second named framework | `Next.js` | **absent** | **absent** | **0** |
| **R5** | "clean code" | `clean code` | **absent** (`code quality` instead) | **absent** | **0** |
| R6 | "testing" | `testing` | line 13 | line 25 | 3 |
| R7 | "debugging" | `debugging` | line 13 | line 25 | 3 |
| R8 | "maintainability" | `maintainability` | line 13 | line 25 | 3 |
| **R9** | "Experience with CMS concepts, including content modeling ... and modern CMS architectures" | `CMS`, `content modeling` | **absent** | **absent** | **0** |
| **R10** | "Familiarity with PHP-based applications" | `PHP` | **absent** | **absent** | **0** |
| R11 | "APIs" | `APIs` | line 12 | lines 21, 24 | 3 |
| R12 | "integrations" | `integrations` | line 12 | line 23 | 3 |
| R13 | "AI coding assistants or AI-enabled development tools" | `AI coding assistants` | line 14 | line 27 | 3 |
| R14 | "agentic workflows" (role summary and responsibilities) | `agentic workflows` | line 14 | line 27 | 3 |
| **R15** | "Advanced English communication skills" | `English` | **absent** | **absent** | **0** |

Held in Gate 1 only, not scored here: modern web application development; analyzing functional
and non-functional requirements; ability to design and document technical solutions and data
flows. None is a retrieval token a recruiter would type into a boolean query.

### Arithmetic
```
required points = 3+3+3+0+0+3+3+3+0+0+3+3+3+3+0 = 30, over 15 requirements
coverage = 100 * (30 * 3) / (3 * 3 * 15) = 100 * 90 / 135 = 67
preferred set: empty, the posting states no bonus tier
```

### Step 5, stuffing penalty
No token reaches 4 occurrences. Highest counts are 3: `JavaScript`, `TypeScript`, `React`,
`APIs`, `integration`, `AI coding assistants`, `agentic workflows`, `Node.js`, `Go`. This
respects the CV-SPEC cap of 3. **Penalty: 0.** This is a real improvement over the `tractian`
build, which lost 10 points here.

**Gate 2 final: 67/100.**

**Required tokens without both `Skills` and `Experience` placement:**
`Next.js` (0), `clean code` (0), `CMS` and `content modeling` (0), `PHP` (0), `English` (0).

Two of those five are **placement defects on supported facts** and cost nothing but an edit:
`English` and `clean code`. Three are **genuine gaps** that no local source supports:
`Next.js`, `CMS`, `PHP`.

## Gate 3 — Human scan: 86/100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 10 / 15 | Top 15% of 55 lines is lines 1-8. Line 6 carries `Senior Software Engineer` and, in the same sentence, `building web applications`. The literal posting title `Senior Web Software Engineer` appears nowhere. 5 points deducted for the absent literal string. **The deduction is not recoverable:** CLAUDE.md rule 1 and `DOSSIER.md` fix the CV title at `Senior Software Engineer` and forbid adjusting a title to fit a posting. Do not "fix" this. |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | 12 / 20 | The DexCare block is correct, but the ordering is not. The posting's own emphasis is modern web with JavaScript, TypeScript, React and Next.js, a CMS migration, and AI-assisted development across the SDLC. Bullet 1 (React with TypeScript) is correctly first. Bullets 4 (testing, debugging, maintainability) and 5 (AI coding assistants, agentic workflows) map directly to two more required items and sit at positions 4 and 5. Bullets 2 and 3 (Epic EMR, Auth0 JWT) are healthcare-domain and rank below all three for this posting, yet they occupy positions 2 and 3. Two of the three highest-value bullets fall outside the first three lines. |
| 3.3 | Every bullet starts with a past-tense action verb and describes an outcome | 15 / 15 | All 11 bullets: Built, Reduced, Reduced, Improved, Built, Delivered, Improved, Cut, Supported, Increased, Supported. Zero present-tense openers, zero "Responsible for", zero third person, no bullet opens with `I`. Matches CLAUDE.md section 9 and CV-SPEC. Summary uses `I` three times, as required. |
| 3.4 | At least 3 bullets carry a real, defensible number | 15 / 15 | Five numbers, all traced to `DOSSIER.md` "Bullet metrics supplied by Lucas 2026-09-01": 15% wrong bookings (D2), 25% authentication friction (D3), 20% invoice throughput (L2), 18% support tickets (L3), 26% processing capacity (P2). No number is invented and none is rounded off the dossier value. |
| 3.5 | Length: 1 page under 10 years of experience | 10 / 10 | `pdfinfo` reports `Pages: 1`, letter size. Roughly 22% of the page is unused at the bottom, so there is room for every fix below. |
| 3.6 | No unsupported buzzwords | 10 / 10 | Grep for team player, results-driven, passionate, self-starter, rockstar, ninja, synergy, detail-oriented, hard-working: zero hits. |
| 3.7 | Skills grouped by category | 10 / 10 | Four labelled groups: Languages, Web engineering, Engineering practices, AI tooling. Tightly aimed at this posting and not a wall. |
| 3.8 | Scannable: consistent spacing, bold titles, adequate white space | 4 / 5 | Company bold, title italic, location and dates plain, consistent across all four roles. The rendered page reads cleanly and the role gaps are visually adequate. Deduct 1 for the extraction-level regression recorded under Gate 0.5: the parser stream no longer carries a blank line at any role boundary. |

**Total: 86/100.**

## Factual integrity — LinkedIn ground truth, checked 2026-09-04

Read read-only through the `Profile Check` portal. No edit action was sent to LinkedIn.
`DOSSIER.md` was refreshed on 2026-09-04 and **now matches the live profile on every row.**
The CV does not.

| Field | CV prints | LinkedIn shows | Refreshed DOSSIER.md | Result |
|---|---|---|---|---|
| DexCare employer | `DexCare` | `DexCare · Full-time` | `DexCare · Full-time` | match |
| DexCare title | `Senior Software Engineer` | `Senior Software Engineer` | same | match |
| **DexCare dates** | **`Jan 2026 - Present`** | **`Mar 2026 - Present · 7 mos`** | **`Mar 2026 - Present · 7 mos`** | **MISMATCH** |
| Luizalabs employer | `Luizalabs` | `Luizalabs · Full-time` | same | match, spelling included |
| Luizalabs title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | same | match |
| **Luizalabs dates** | **`Jan 2024 - Jan 2026`** | **`Jan 2024 - Mar 2026 · 2 yrs 3 mos`** | **`Jan 2024 - Mar 2026`** | **MISMATCH** |
| Lippaus employer, both roles | `Lippaus Distribuidora` | `Lippaus Distribuidora` | same | match |
| Lippaus senior title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | same | match |
| Lippaus senior dates | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024 · 1 yr 1 mo` | same | match |
| Lippaus first title | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | same | match |
| Lippaus first dates | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023 · 1 yr 11 mos` | same | match |
| Education | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | same | match. LinkedIn renders an EN DASH; the CV's ASCII hyphen is what CLAUDE.md rule 1 and CV-SPEC section 5 require |
| Role locations | DexCare `Remote`, Luizalabs `Remote`, Lippaus `Vitória, ES, Brazil` | DexCare `Seattle, Washington, United States · Remote`, Luizalabs `São Paulo, Brazil · Remote`, Lippaus `Vitória, Espírito Santo, Brazil · On-site` | — | correct per `DOSSIER.md` "Role locations": employer cities never print |

**This is a repeat of the same two errors found on the `tractian` build earlier today, and the
excuse that applied then does not apply now.** On that build, `DOSSIER.md` was stale and the
Architect had no correct local source. `DOSSIER.md` has since been refreshed and carries
`Mar 2026 - Present` and `Jan 2024 - Mar 2026` verbatim. This build was produced against a
correct source and still prints the old values.

The Summary claim `5+ years` survives the correction. Mar 2021 to Sep 2026 is 5 yrs 6 mos.

## Metric trace

| CV number | `DOSSIER.md` entry | Result |
|---|---|---|
| wrong bookings -15% | D2, "reduced wrong bookings by 15%" | traced |
| authentication friction -25% | D3, "reduced authentication friction by 25%" | traced |
| invoice throughput +20% | L2, "20% improvement in invoice processing throughput" | traced |
| support tickets -18% | L3, "18% fewer support tickets" | traced |
| processing capacity +26% | P2, "26% more processing capacity" | traced |
| `5+ years` | not a dossier string; arithmetic on the LinkedIn dates | derived, not invented. Stated as derived. |

No number on the CV lacks a source. No `[UNVERIFIED]` marker appears, and CLAUDE.md section 4
forbids verification markers for framework, data, cloud and tool tokens.

## Policy checks

| Rule | Result |
|---|---|
| CLAUDE.md 2, no Ruby or Rails token anywhere | PASS. Grep for ruby, rails, sidekiq, activerecord, rspec, devise, pundit, hotwire: zero hits. |
| CLAUDE.md 2, positioning as TypeScript, Node.js, React, Go | PASS. Skills line 11 leads with the four. |
| CLAUDE.md 3, degree Information Systems, FAESA | PASS. |
| CLAUDE.md 3, location `Vitória, ES, Brazil`, nothing more | PASS. |
| CLAUDE.md 3, never print a UTC offset or overlap statement | PASS. Grep for GMT, UTC, timezone, overlap: zero hits. |
| CLAUDE.md 3, Lippaus prints `Vitória, ES, Brazil`; DexCare and Luizalabs print `Remote` | PASS. |
| CLAUDE.md 3, contract detail never printed | PASS. No CLT, PJ, or Fullstack Labs token. |
| CLAUDE.md 9, bullet voice and Summary voice | PASS. See Gate 3.3. |
| CLAUDE.md 11, one language per tailored CV | PASS. English only. Posting language is `en`, company origin international. No `-pt` sibling in the application folder. |
| CV-SPEC, canonical headers in the source | PASS. `\section{Summary}`, `{Skills}`, `{Experience}`, `{Education}`. |
| CV-SPEC, ASCII hyphen in every date | PASS. Zero EN DASH in the extraction. |
| CV-SPEC, cap any term at 3 appearances | PASS. Nothing exceeds 3. |
| CV-SPEC, AI or LLM mention in Summary and in Experience | PASS. Summary line 7, DexCare bullet 5. |
| CV-SPEC, every load-bearing technology in Skills and in an Experience bullet | PASS for this posting's tokens. `Go` sits in Summary, Skills and Experience line 34. `Node.js` in Summary, Skills and line 34. |
| Maestro brief, do not convert unsupported gaps into facts | PASS. Zero occurrences of `Next.js`, `CMS`, `content model`, `PHP`. The Architect correctly refused to invent them. |

## Defects, ranked by cost

1. **DexCare start month is wrong. Factual integrity, CLAUDE.md rule 1. Blocking.**
   `Lucas-Queiroz-Resume-en.tex` line 65 reads `{DexCare}{Jan 2026 - Present}`.
   Both LinkedIn and the refreshed `DOSSIER.md` read `Mar 2026 - Present`.
   Change `Jan 2026` to `Mar 2026`.

2. **Luizalabs end month is wrong. Factual integrity, CLAUDE.md rule 1. Blocking.**
   `Lucas-Queiroz-Resume-en.tex` line 76 reads `{Luizalabs}{Jan 2024 - Jan 2026}`.
   Both LinkedIn and the refreshed `DOSSIER.md` read `Jan 2024 - Mar 2026`.
   Change `Jan 2026` to `Mar 2026`.
   Defects 1 and 2 were reported on the `tractian` build earlier today. `DOSSIER.md` is now
   correct, so this build had a correct source available and did not use it.

3. **`English` is absent. Gate 1 FAIL and Gate 2 required token at 0. Blocking, and free to fix.**
   The posting lists "Advanced English communication skills for technical discussions,
   collaboration, and documentation" under Required Skills & Experience. The CV has zero
   English tokens. The fact is supported verbatim in `DOSSIER.md` Identity: "English
   proficiency: Advanced / C1. Daily English-only work with US teams at DexCare." The sibling
   `tractian` build carried `Advanced English (C1)` on its Skills line and this build dropped it.
   Place it in Skills, source line 58 or 59, and in one Experience bullet, since a required
   token needs both placements. The DexCare block is the honest host: `DOSSIER.md` ties the
   daily English-only work to DexCare specifically.
   **Correction to the Maestro brief:** it lists "Advanced English" under "Required tokens or
   facts not supported by DOSSIER.md". That is wrong. It is supported.

4. **`clean code` is absent. Gate 2 required token at 0. Blocking, and nearly free to fix.**
   Posting: "Solid understanding of software engineering principles, programming logic, clean
   code, testing, debugging, and maintainability." The CV writes `code quality` twice instead,
   at source lines 71 and 72. `ATS-KNOWLEDGE.md` section 4.1 is explicit: preserve the posting's
   exact spelling and never rely on alias expansion. The supporting fact already exists in
   `DOSSIER.md` ("shared rules, codebase enforcement (lint, cyclomatic complexity limits,
   testing)"), so this is a wording change plus a Skills placement, not a new claim.

5. **Requirements analysis has no evidence. Gate 1 FAIL. Blocking, and fixable from DOSSIER.md.**
   Posting: "Experience analyzing functional and non-functional requirements and contributing to
   technical implementation decisions." No CV bullet covers it. `DOSSIER.md` records, among the
   Lippaus and Luizalabs bullets approved by Lucas, "project scoping and stakeholder
   communication" and "customer-facing features end to end". The Architect dropped that approved
   bullet from this build. Restore it in the Lippaus Mid-level block, source lines 87-90, in XYZ
   form and past tense. This needs no new fact from Lucas.

6. **`CMS` and `content modeling` are absent. Gate 1 FAIL, Gate 2 required token at 0. Blocking, NOT fixable locally.**
   This is the posting's central initiative: "a CMS modernization and migration initiative",
   and the required item reads "Experience with CMS concepts, including content modeling, APIs,
   integrations, and modern CMS architectures." `DOSSIER.md` records no CMS fact of any kind.
   **Escalate to Lucas.** Ask whether he has worked with a CMS, headless or traditional, and
   with content modeling. If yes, record it in `DOSSIER.md` first, then place the exact tokens.
   If no, this is a genuine gap and the application ships with it declared. Do not invent it.

7. **`PHP` is absent. Gate 1 FAIL, Gate 2 required token at 0. Blocking, NOT fixable locally.**
   Posting: "Familiarity with PHP-based applications and the ability to read, understand, debug,
   and navigate an existing PHP codebase. Deep PHP specialization is not required."
   `DOSSIER.md` records no PHP fact. **Escalate to Lucas.** The bar is low, reading and
   navigating rather than building, so a real answer may well exist. If it does, record it in
   `DOSSIER.md` first. Note for the Maestro, not for the Architect: placing a PHP token is
   consistent with CLAUDE.md section 4, which states that frameworks and tools do not decide
   primary-stack eligibility, and this posting's primary stack is JavaScript and TypeScript.

8. **`Next.js` is absent and no comparable framework is offered. Gate 1 FAIL, Gate 2 required token at 0. Blocking, NOT fixable locally.**
   Posting: "Hands-on experience with React and Next.js, or directly comparable modern web
   frameworks." `DOSSIER.md` records React but no Next.js and no other web framework.
   **Escalate to Lucas.** Ask directly whether he has shipped Next.js, or another framework that
   sits in the same place, for example Remix, Nuxt or Astro. If yes, record it in `DOSSIER.md`
   first, then place it in Skills and in one Experience bullet. If no, the honest position is
   that React alone is offered against a requirement naming two things, and Lucas decides
   whether to apply anyway.

9. **Design and documentation of technical solutions has no evidence. Gate 1 FAIL. Blocking, NOT fixable locally today.**
   Posting: "Ability to design and document technical solutions, integrations, application
   workflows, and data flows." `document`, `documentation` and `data flow` each have 0
   occurrences. `DOSSIER.md` records no documentation fact, so nothing can be placed today.
   **Escalate to Lucas.** One observation that may shorten that conversation, offered as a
   pointer and not as evidence I am rewarding: the DexCare entry on his own LinkedIn profile
   contains the line "Authored a Product Design Review for the Customer Information and
   Configuration experience". I read that text while verifying titles and dates. It is profile
   prose, not a listed local source, so I did not score it. If Lucas confirms it, the Maestro
   should record it in `DOSSIER.md` and the Architect can then place a design-and-document bullet
   from a proper source.

10. **Bullet ordering in the DexCare block. Gate 3.2, -8. Non-blocking.**
    Bullets 4 and 5 (source lines 71 and 72) carry `testing`, `debugging`, `maintainability`,
    `AI coding assistants` and `agentic workflows`, five required tokens between them, and sit
    below bullets 2 and 3, which carry healthcare-domain work this posting never asks for.
    Moving the AI bullet and the engineering-practices bullet up to positions 2 and 3 costs
    nothing factual and recovers 8 Gate 3 points.

11. **The raw extraction lost its role-boundary blank lines. Gate 0.5 note, Gate 3.8 -1. Non-blocking, worth a rebuild test.**
    See the note under Gate 0.5. The sibling build in this same hunt produces a blank line at
    every role boundary; this one produces none. Segmentation still passes, but this is the
    single most valuable parse property in `ATS-KNOWLEDGE.md` and it should not drift by
    accident. Revert the `\resumeSubheading` and `\resumeRoleGap` macros to the `tractian`
    build's spacing, rebuild, and confirm `grep -c '^$'` on the raw extraction returns 9.

## Match limits

The posting states no bonus or preferred tier, so there are no preferred tokens to place and
none to report as missed.

Three required items cannot be satisfied from any local source and are true gaps, not defects
of the writing: `Next.js`, `CMS` with `content modeling`, and `PHP`. A fourth, the
design-and-document capability, is unsupported today but may be recoverable if Lucas confirms
the Product Design Review work.

If the two fixable Gate 2 defects are applied (`English` and `clean code`, each reaching 3
points) and Lucas supplies nothing new, required points go from 30 to 36 of 45 and Gate 2 rises
to `100 * (36*3) / 135` = **80/100. Still FAIL**, because `Next.js`, `CMS` and `PHP` stay at 0.
Gate 1 also still fails on those three plus design-and-document. **The fixable edits alone do
not clear this application.** That is a real limit of the match, not a writing problem,
and it belongs to Lucas to weigh.

## What is not observable
- Work authorization and time-zone requirements. The posting states neither.
- Whether CI&T treats the "or directly comparable modern web frameworks" clause as satisfied by
  React alone. That is a human recruiter's judgement and no document discloses it.
- Which ATS CI&T runs, and therefore which parser handles this file. No public source names an
  engine for this employer. Nothing in this report is a vendor score. These are our four gates,
  defined in `RUBRIC.md`, and nothing else.
