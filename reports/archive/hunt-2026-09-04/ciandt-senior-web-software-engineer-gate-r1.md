# ATS Analysis — resumes/hunts/2026-09-04/ciandt-senior-web-software-engineer/Lucas-Queiroz-Resume-en.pdf vs ciandt-senior-web-software-engineer
Segment: agency (the posting file records `Segment: agency`; company origin international, 25+ countries)   Date: 2026-09-04

Round: **fix round 1 re-grade.** Baseline: `reports/ciandt-senior-web-software-engineer-gate.md`
and `state/ciandt-senior-web-software-engineer-sieve.report.md`. Architect input:
`state/ciandt-senior-web-software-engineer-quill-fix1.report.md`.

## Verdict
BLOCKED at Gate 1.

Gate 2 also fails on required-token placement. The two factual-integrity blockers from round 0
are cleared. Gate 0 is fully PASS and the round-0 segmentation regression is gone. Gate 3 rose
from 86 to 95.

**Every supported fix landed. Every remaining failure is an unsupported requirement.** No
further edit can clear this application. It needs answers from Lucas, or a decision to apply
with the gaps declared.

## Sources actually read

- `AGENTS.md`, `RUBRIC.md`, `ATS-KNOWLEDGE.md`, `CV-SPEC.md`, `DOSSIER.md`, all in full.
- `jobs/ciandt-senior-web-software-engineer.md`, the posting text and the Maestro brief.
- `state/ciandt-senior-web-software-engineer-sieve.report.md` (round 0 result).
- `state/ciandt-senior-web-software-engineer-quill-fix1.report.md` (Architect fix round 1).
- `reports/ciandt-senior-web-software-engineer-gate.md` (round 0 gate report).
- The CV source `.tex` and the CV `.pdf` under test, both dated 2026-09-04 11:17.
- LinkedIn, live, read-only through the `Profile Check` portal. No edit action was sent.
  - https://www.linkedin.com/in/queiroz-lucas/details/experience/
  - https://www.linkedin.com/in/queiroz-lucas/details/education/
- The posting URL https://www.linkedin.com/jobs/view/4454020765/ was **not** re-opened. The
  posting text was read from the local job file only.
- The four PDFs under `~/Documents/Resumes/` were not opened. They are invalid sources.

## Mandatory extraction, run first

```
pdftotext -layout Lucas-Queiroz-Resume-en.pdf  -> extracted-layout.txt   56 lines
pdftotext         Lucas-Queiroz-Resume-en.pdf  -> extracted-raw.txt      60 lines
```

Gate 0 and Gate 2 are judged on the raw file. Every line number below is a raw-extraction line
number unless it says `source`.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 60 lines of clean text. `pdfimages -list` returns zero rows, so the page carries no raster layer and is not a scan. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00-U+FB06. Zero NUL bytes, zero U+FFFD, zero literal `?`. The only non-ASCII codepoints in the whole stream are U+00F3 `ó` and U+2022 `•`. Probe words extract intact: `workflow` 4 times (lines 7, 14, 25, 52), `office` 2 times (lines 37, 52). `profile`, `efficient` and `conflict` do not occur in the document, so they cannot be probed. The `fontspec` + `Ligatures=NoCommon` fix at source lines 11-12 works. All four fonts embed with a unicode map (`pdffonts`: uni = yes on every row). |
| 0.3 | Contact block recoverable, in the body | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email and LinkedIn URL all present. Source has `\pagestyle{empty}` and the block sits inside `\begin{center}` in the body, not a header or footer. |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 10, 16, 54 carry `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION` as standalone lines. Source strings are `Summary`, `Skills`, `Experience`, `Education` (source lines 51, 54, 62, 102). Uppercase rendering is allowed by the rubric, case-insensitive. |
| 0.5 | Employment-block segmentation | PASS, **regression cleared** | Four separate blocks, none merged and none split: DexCare (17-28), Luizalabs (30-37), Lippaus Distribuidora Mid-level (39-46), Lippaus Distribuidora Entry-level (48-52). Each prints Company / Title / Location / Dates on four consecutive lines, and each Lippaus role repeats its own company line, so the promotion cannot collapse. **The round-0 regression is fixed.** A blank line now separates every role boundary: raw blanks sit at lines 2, 4, 9, 15, **29, 38, 47, 53**, 59. `grep -c '^$'` returns **9**, up from 6, matching the `tractian` shape. |
| 0.6 | Date parseability | PASS | Each role carries `Mon YYYY - Mon YYYY` on its own line inside its block: lines 20, 33, 42, 51, 58. ASCII hyphen throughout; `grep -c '–'` on the raw text returns 0. The date line sits two lines below its title, with the location line between; the block is contiguous and unambiguous either way. **The two wrong values from round 0 are corrected. See Factual integrity.** |
| 0.7 | Reading order | PASS | Raw and layout agree on every adjacent block: name, contact, Summary, Skills, the four roles in the same order, Education. No pair is transposed. |
| 0.8 | No forbidden constructs | PASS | Source uses `itemize` only. `grep` for `tabular`, `fbox`, `parbox`, `minipage`, `includegraphics`, `multicol` returns zero hits. `pdfimages -list` is empty, so no photo, no icon, no image of text. |

**Gate 0: 8/8 PASS, with no recorded regression.** This is a clean improvement over round 0,
which passed 8/8 but carried a segmentation-robustness regression under 0.5.

## Gate 1 — Knockouts

The posting has one requirement block, "Required Skills & Experience". It has no bonus or
preferred section, so every listed item is required.

| Check | Source | Result | Evidence |
|---|---|---|---|
| Work authorization / entity type | posting | not stated | The posting names no authorization or entity type. Employment type shows `Full-time`, location `Brazil`, workplace `Remote`. |
| Location or time-zone overlap | posting | not stated | No overlap window stated. The posting's location is `Brazil` and the CV prints `Vitória, ES, Brazil`, so no location knockout can fire. The CV prints no UTC offset and no overlap sentence, as CLAUDE.md rule 3 demands. |
| Minimum years of experience | posting | not stated | The posting says "Senior" and "experienced" but names no number. CV Summary claims `5+ years`; LinkedIn gives Mar 2021 to Sep 2026, 5 yrs 6 mos. |
| Degree requirement | posting | not stated | No degree is required. CV carries `Bachelor's degree, Information Systems`, FAESA, anyway. |
| Modern web application development | posting | PASS | "Strong hands-on experience with modern web application development." Evidence: Summary line 6 `building web applications with TypeScript, Node.js, React, and Go`; DexCare bullet 1 (React with TypeScript services on Express and Koa); Lippaus bullet line 43 (multi-tenant web and mobile platform). |
| JavaScript **and** TypeScript | posting | PASS | Cumulative, both named. `JavaScript` Skills line 11, Experience lines 37 and 52. `TypeScript` Skills line 11, Experience line 22, Summary line 6. |
| **React and Next.js, or directly comparable modern web frameworks** | posting | **FAIL** | `React` is fully placed: Skills line 12, Experience line 21, Summary line 6. **`Next.js` has 0 occurrences** and `DOSSIER.md` records no Next.js fact. The posting's escape clause is "or directly comparable modern web frameworks"; the CV names no framework offered in that place. React is one of the two terms the posting already asked for, not a comparable substitute for the other, and React is the library Next.js is built on rather than a peer of it. I will not convert that into a pass. RUBRIC Gate 1: absent resume evidence is a FAIL. This preserves the uncertainty the Maestro brief asked me to preserve. **Unchanged from round 0.** |
| Software engineering principles, programming logic, **clean code**, testing, debugging, maintainability | posting | **PASS, round-0 gap closed** | `clean code` now placed: Skills line 13, Experience line 24 (`lint and complexity limits for clean code`). `testing`, `debugging`, `maintainability` each Skills line 13 and Experience line 23. "Software engineering principles" and "programming logic" are discarded as buzzwords per RUBRIC Step 1. |
| **CMS concepts, content modeling, APIs, integrations, modern CMS architectures** | posting | **FAIL** | `APIs` and `integrations` are fully placed. **`CMS` has 0 occurrences and `content model` has 0 occurrences.** `DOSSIER.md` was re-read in full today and records no CMS fact anywhere; its only `CMS`-adjacent strings are policy text, not candidate facts. This is the posting's central initiative, named in the role summary as "a CMS modernization and migration initiative". **Unchanged from round 0.** |
| **Familiarity with PHP-based applications** | posting | **FAIL** | **`PHP` has 0 occurrences.** `DOSSIER.md` records no PHP fact; its two `PHP` hits are the triage-knockout policy list at lines 15 and 19, not candidate history. The posting asks only for reading, debugging and navigating an existing PHP codebase, and says "Deep PHP specialization is not required", so this is a low bar, but the CV supplies no evidence at all and I will not invent one. **Unchanged from round 0.** |
| Analyzing functional and non-functional requirements, contributing to technical implementation decisions | posting | **PASS on evidence, round-0 gap closed, one qualifier missing** | The restored Lippaus bullet, lines 45-46: `Turned customer requirements into delivered solutions by leading project scoping and stakeholder communication and by analyzing requirements to guide technical implementation decisions.` `requirements` now occurs 3 times: Skills line 13 (`requirements analysis`), Experience lines 45 and 46. The rubric's FAIL condition is absent resume evidence; evidence is now present, so the row passes. **The qualifier `functional and non-functional` is absent and `DOSSIER.md` does not support it.** The Architect correctly refused to write it. See defect 4 for the wording caveat. |
| Practical experience using AI coding assistants or AI-enabled development tools in the SDLC | posting | PASS | `AI coding assistants` Skills line 14, Experience line 25, Summary line 7. `agentic workflows` Skills line 14, Experience line 25, Summary line 7. Traced to `DOSSIER.md` "AI at DexCare". |
| **Ability to design and document technical solutions, integrations, application workflows, and data flows** | posting | **FAIL** | `integrations` is placed and `workflows` appears at lines 7, 14, 25, 52. But **`document` and `documentation` have 0 occurrences, and `data flow` has 0 occurrences.** No bullet describes designing or documenting a technical solution. `DOSSIER.md` records no documentation fact, so this is still not fixable from local sources. **Unchanged from round 0.** Escalation item, see below. |
| **Advanced English communication skills** | posting | **PASS, round-0 gap closed** | `English` now placed twice: Skills line 14 (`Advanced English (C1)`) and Experience line 22 (`working daily in English with US teams`). Both trace to `DOSSIER.md` Identity, "English proficiency: Advanced / C1. Daily English-only work with US teams at DexCare." The DexCare host is the honest one, because the dossier ties the daily English-only work to DexCare specifically. |

**Gate 1: FAIL on four rows, down from six.** The two closed rows, `Advanced English` and
`analyzing requirements`, were both supported facts the Architect placed from `DOSSIER.md`. The
four open rows, `Next.js`, `CMS`/`content modeling`, `PHP`, and `design and document technical
solutions and data flows`, have no support in any local source and stay at zero, as instructed.

## Gate 2 — Retrieval coverage: 80/100, FAIL

Scoring convention, identical to round 0 so the two runs are comparable:
- An **alternative set** in the posting is scored once, on the best-placed member that
  `DOSSIER.md` actually supports.
- Hard requirements that can never occupy `Skills` or `Experience` (a degree, a years count, a
  capability narrative) live in Gate 1 only and are excluded from the denominator here.
- Placement points: absent 0, `Skills` only 1, `Experience` only 2, both 3.
- The posting has **no preferred tier**. Every item sits under "Required Skills & Experience",
  so the preferred set is empty and weight 3 applies throughout.

| # | Requirement, posting wording | Token scored | Skills | Experience | Points | vs r0 |
|---|---|---|---|---|---|---|
| R1 | "Strong experience with JavaScript and TypeScript" | `JavaScript` | line 11 | lines 37, 52 | 3 | = |
| R2 | same, cumulative second half | `TypeScript` | line 11 | line 22 | 3 | = |
| R3 | "Hands-on experience with React and Next.js" | `React` | line 12 | line 21 | 3 | = |
| **R4** | same requirement, second named framework | `Next.js` | **absent** | **absent** | **0** | = |
| R5 | "clean code" | `clean code` | line 13 | line 24 | **3** | **0 → 3** |
| R6 | "testing" | `testing` | line 13 | line 23 | 3 | = |
| R7 | "debugging" | `debugging` | line 13 | line 23 | 3 | = |
| R8 | "maintainability" | `maintainability` | line 13 | line 23 | 3 | = |
| **R9** | "Experience with CMS concepts, including content modeling ... and modern CMS architectures" | `CMS`, `content modeling` | **absent** | **absent** | **0** | = |
| **R10** | "Familiarity with PHP-based applications" | `PHP` | **absent** | **absent** | **0** | = |
| R11 | "APIs" | `APIs` | line 12 | line 21 | 3 | = |
| R12 | "integrations" | `integrations` | line 12 | line 27 | 3 | = |
| R13 | "AI coding assistants or AI-enabled development tools" | `AI coding assistants` | line 14 | line 25 | 3 | = |
| R14 | "agentic workflows" (role summary and responsibilities) | `agentic workflows` | line 14 | line 25 | 3 | = |
| R15 | "Advanced English communication skills" | `English` | line 14 | line 22 | **3** | **0 → 3** |

Held in Gate 1 only, not scored here: modern web application development; analyzing functional
and non-functional requirements; ability to design and document technical solutions and data
flows. None is a retrieval token a recruiter would type into a boolean query.

### Arithmetic
```
required points = 3+3+3+0+3+3+3+3+0+0+3+3+3+3+3 = 36, over 15 requirements
coverage = 100 * (36 * 3) / (3 * 3 * 15) = 100 * 108 / 135 = 80
preferred set: empty, the posting states no bonus tier
```

This lands exactly on the round-0 projection of 80/100.

### Step 5, stuffing penalty

No scored token reaches 4 occurrences. Highest counts are 3: `JavaScript`, `TypeScript`,
`React`, `APIs`, `integration`, `AI coding assistants`, `agentic workflows`, `Node.js`, `Go`,
`requirements`. **Penalty: 0.**

One observation that is not a penalty. The bare word `workflows` occurs 4 times, at lines 7, 14,
25 and 52. Three are the scored token `agentic workflows`, which sits at the CV-SPEC cap of 3.
The fourth is `administrative workflows` at line 52, a different sense in a different role. The
rubric's penalty applies to the tokens in the table above, and `workflows` alone is not one, so
I do not deduct. Recorded so the count does not drift upward unnoticed in a later round.

**Gate 2 final: 80/100, FAIL.**

**Required tokens without both `Skills` and `Experience` placement:**
`Next.js` (0), `CMS` and `content modeling` (0), `PHP` (0).

All three are genuine gaps that no local source supports. The two placement defects on supported
facts, `English` and `clean code`, are both closed. **There is no writable Gate 2 fix left.**

## Gate 3 — Human scan: 95/100

| # | Check | Points | Evidence | vs r0 |
|---|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 10 / 15 | Top 15% of 59 content lines is lines 1-9. Line 6 carries `Senior Software Engineer` and, in the same sentence, `building web applications`. The literal posting title `Senior Web Software Engineer` appears nowhere. 5 points deducted for the absent literal string. **The deduction is not recoverable:** CLAUDE.md rule 1 and `DOSSIER.md` fix the CV title at `Senior Software Engineer` and forbid adjusting a title to fit a posting. Do not "fix" this. | = |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | **20 / 20** | The reorder landed. DexCare bullet 1, lines 21-22: React with TypeScript on Express and Koa, plus daily English. Bullet 2, lines 23-24: maintainability, testing, debugging, clean code. Bullet 3, lines 25-26: agentic workflows and AI coding assistants. Those three carry every one of the posting's supported required tokens. The healthcare-domain bullets, Epic EMR and Auth0 JWT, now sit at positions 4 and 5 where this posting values them. | **12 → 20** |
| 3.3 | Every bullet starts with a past-tense action verb and describes an outcome | 15 / 15 | All 12 bullets: Built, Improved, Built, Reduced, Reduced, Delivered, Improved, Cut, Supported, Increased, Turned, Supported. Zero present-tense openers, zero "Responsible for", zero third person, no bullet opens with `I`. Matches CLAUDE.md section 9 and CV-SPEC. Summary uses `I` three times, as required. | = |
| 3.4 | At least 3 bullets carry a real, defensible number | 15 / 15 | Five numbers, all traced to `DOSSIER.md` "Bullet metrics supplied by Lucas 2026-09-01": 15% wrong bookings (D2), 25% authentication friction (D3), 20% invoice throughput (L2), 18% support tickets (L3), 26% processing capacity (P2). No number is invented and none is rounded off the dossier value. The restored requirements bullet correctly carries no number, because the dossier records none for it. | = |
| 3.5 | Length: 1 page under 10 years of experience | 10 / 10 | `pdfinfo` reports `Pages: 1`, 612 x 792 pts, letter. The rendered page at 110 dpi shows roughly 15% of the page unused at the bottom. No clipping, no overlap, the Education block sits fully on page one. | = |
| 3.6 | No unsupported buzzwords | 10 / 10 | Grep for team player, results-driven, passionate, self-starter, rockstar, ninja, synergy, detail-oriented, hard-working, go-getter: zero hits. | = |
| 3.7 | Skills grouped by category | 10 / 10 | Four labelled groups: `Languages`, `Web engineering`, `Engineering practices`, `AI tooling and communication`. The fourth was renamed this round to host `Advanced English (C1)` honestly rather than filing a language under tooling alone. Tightly aimed at this posting and not a wall. | = |
| 3.8 | Scannable: consistent spacing, bold titles, adequate white space | **5 / 5** | Company bold, title italic, location and dates plain, consistent across all four roles. The round-0 deduction was for the extraction-level blank-line regression under Gate 0.5. That regression is cleared: the parser stream now carries a blank line at all three role boundaries and before Education. | **4 → 5** |

**Total: 95/100.** Up from 86.

## Factual integrity — LinkedIn ground truth, checked live 2026-09-04

Read read-only through the `Profile Check` portal. No edit action was sent to LinkedIn. The
experience and education detail pages were opened and read as rendered.

| Field | CV prints | LinkedIn shows, live today | Result |
|---|---|---|---|
| DexCare employer | `DexCare` | `DexCare · Full-time` | match |
| DexCare title | `Senior Software Engineer` | `Senior Software Engineer` | match |
| **DexCare dates** | `Mar 2026 - Present` | `Mar 2026 - Present · 7 mos` | **MISMATCH CLEARED** |
| Luizalabs employer | `Luizalabs` | `Luizalabs · Full-time` | match, spelling included |
| Luizalabs title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| **Luizalabs dates** | `Jan 2024 - Mar 2026` | `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | **MISMATCH CLEARED** |
| Lippaus employer, both roles | `Lippaus Distribuidora` | `Lippaus Distribuidora` | match |
| Lippaus senior title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Lippaus senior dates | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024 · 1 yr 1 mo` | match |
| Lippaus first title | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | match |
| Lippaus first dates | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023 · 1 yr 11 mos` | match |
| Education | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | match. LinkedIn renders an EN DASH; the CV's ASCII hyphen is what CLAUDE.md rule 1 and CV-SPEC section 5 require |
| Role locations | DexCare `Remote`, Luizalabs `Remote`, both Lippaus roles `Vitória, ES, Brazil` | DexCare `Seattle, Washington, United States · Remote`, Luizalabs `São Paulo, Brazil · Remote`, Lippaus `Vitória, Espírito Santo, Brazil · On-site` | correct per `DOSSIER.md` "Role locations": employer cities never print |

**Both round-0 date errors are corrected.** Every title, employer and date on the CV now matches
the live profile character for character, allowing the CV-SPEC hyphen rule.

The Summary claim `5+ years` survives. Mar 2021 to Sep 2026 is 5 yrs 6 mos. Reported as derived
arithmetic on the LinkedIn dates, not as a dossier string.

## Metric trace

| CV number | `DOSSIER.md` entry | Result |
|---|---|---|
| wrong bookings -15% | D2, "reduced wrong bookings by 15%" | traced |
| authentication friction -25% | D3, "reduced authentication friction by 25%" | traced |
| invoice throughput +20% | L2, "20% improvement in invoice processing throughput" | traced |
| support tickets -18% | L3, "18% fewer support tickets" | traced |
| processing capacity +26% | P2, "26% more processing capacity" | traced |
| `5+ years` | not a dossier string; arithmetic on the LinkedIn dates | derived, stated as derived |

No number on the CV lacks a source. No verification marker appears, and CLAUDE.md section 4
forbids them for framework, data, cloud and tool tokens.

## Policy checks

| Rule | Result |
|---|---|
| CLAUDE.md 2, no Ruby or Rails token anywhere | PASS. Grep of source, raw and layout for ruby, rails, sidekiq, activerecord, activejob, rspec, devise, pundit, hotwire: **0, 0, 0**. |
| CLAUDE.md 2, positioning as TypeScript, Node.js, React, Go | PASS. Skills line 11 leads with the four. |
| CLAUDE.md 3, degree Information Systems, FAESA | PASS, line 56. |
| CLAUDE.md 3, location `Vitória, ES, Brazil`, nothing more | PASS, line 3. |
| CLAUDE.md 3, never print a UTC offset or overlap statement | PASS. Grep of source, raw and layout for UTC, GMT, time zone, timezone, overlap: **0, 0, 0**. |
| CLAUDE.md 3, Lippaus prints `Vitória, ES, Brazil`; DexCare and Luizalabs print `Remote` | PASS, lines 19, 32, 41, 50. |
| CLAUDE.md 3, contract detail never printed | PASS. No CLT, PJ, EOR or Fullstack Labs token. |
| CLAUDE.md 9, bullet voice and Summary voice | PASS. See Gate 3.3. |
| CLAUDE.md 11, one language per tailored CV | PASS. English only. Posting language is `en`, company origin international. No `-pt` sibling in the application folder; the directory holds exactly two files, the `.tex` and the `.pdf`. |
| CV-SPEC, canonical headers in the source | PASS. `\section{Summary}`, `{Skills}`, `{Experience}`, `{Education}` at source lines 51, 54, 62, 102. |
| CV-SPEC, ASCII hyphen in every date | PASS. Zero EN DASH in the extraction. |
| CV-SPEC, cap any term at 3 appearances | PASS for every scored token. See the `workflows` note under Gate 2 Step 5. |
| CV-SPEC, AI or LLM mention in Summary and in Experience | PASS. Summary line 7, DexCare bullet 3 at line 25. |
| CV-SPEC, every load-bearing technology in Skills and in an Experience bullet | PASS for this posting's tokens. `Go` sits in Summary, Skills and Experience line 35. `Node.js` in Summary, Skills and line 35. |
| Maestro brief, do not convert unsupported gaps into facts | PASS. Zero occurrences of `Next.js`, `CMS`, `content model`, `PHP`, `document`, `data flow`. The Architect held the line under a second round of pressure. |

## Prior-fix verification, one row per round-0 item

| # | Round-0 fix | Applied? | Evidence |
|---|---|---|---|
| 1 | DexCare `Jan 2026` → `Mar 2026` | **yes** | Source line 65, raw line 20. Matches live LinkedIn. |
| 2 | Luizalabs `Jan 2026` → `Mar 2026` end | **yes** | Source line 76, raw line 33. Matches live LinkedIn. |
| 3 | Place `English` in Skills and one Experience bullet | **yes** | Skills line 14, Experience line 22. Traced to `DOSSIER.md` Identity. The banned sentence "Works remotely from Brazil with US-based teams" is not used. |
| 4 | Place `clean code` in Skills and one Experience bullet | **yes** | Skills line 13, Experience line 24. The agentic bullet keeps `code quality`, which the posting also uses, so both spellings are present without stuffing. |
| 5 | Restore the requirements-analysis bullet | **yes** | Lippaus Mid-level, raw lines 45-46. Past tense, subject omitted, XYZ with no metric. Does not claim `functional and non-functional`. |
| 6 | Reorder the DexCare bullets | **yes** | New order at lines 21-28. Gate 3.2 recovers the full 20 points. |
| 7 | Restore the role-boundary blank lines | **yes** | `grep -c '^$'` on the raw extraction returns **9**, and blanks sit at lines 29, 38, 47, 53, which are exactly the three role boundaries plus the Education boundary. Gate 3.8 recovers its point and the Gate 0.5 regression note is withdrawn. |
| 8-11 | CMS, PHP, Next.js, design-and-document | **correctly not applied** | Zero occurrences of every token. No unsupported fact was invented under a second round of pressure. |

**All seven writable fixes landed. All four escalations stayed unwritten.**

## Defects, ranked by cost

1. **`Next.js` absent — Gate 1 and Gate 2 R4 — not writable.** The posting requires "Hands-on
   experience with React and Next.js, or directly comparable modern web frameworks."
   `DOSSIER.md` supports React and no other web framework. Whether CI&T reads the escape clause
   as satisfied by React alone is a recruiter's judgement that no document discloses. **Escalate
   to Lucas:** has he shipped Next.js, or something that sits in the same place, for example
   Remix, Nuxt or Astro? Record the answer in `DOSSIER.md` before any token is placed.

2. **`CMS` and `content modeling` absent — Gate 1 and Gate 2 R9 — not writable.** This is the
   posting's central initiative: "a CMS modernization and migration initiative", with the
   required item "Experience with CMS concepts, including content modeling, APIs, integrations,
   and modern CMS architectures." `DOSSIER.md` records no CMS fact of any kind. **Escalate to
   Lucas:** has he worked with a CMS, headless or traditional, and with content modeling?

3. **`PHP` absent — Gate 1 and Gate 2 R10 — not writable.** Required item: "Familiarity with
   PHP-based applications and the ability to read, understand, debug, and navigate an existing
   PHP codebase. Deep PHP specialization is not required." `DOSSIER.md` records no PHP fact. The
   bar is low, reading and navigating rather than building, so a real answer may well exist.
   Note for the Maestro: placing a PHP token would not breach CLAUDE.md section 4, which states
   that frameworks and tools do not decide primary-stack eligibility, and this posting's primary
   stack is JavaScript and TypeScript.

4. **Designing and documenting technical solutions and data flows absent — Gate 1 — not
   writable.** Required item: "Ability to design and document technical solutions, integrations,
   application workflows, and data flows." `document`, `documentation` and `data flow` each have
   0 occurrences, and `DOSSIER.md` records no documentation fact. One pointer, offered as a lead
   and not as evidence I scored: the DexCare entry on Lucas's own LinkedIn profile carries the
   line "Authored a Product Design Review for the Customer Information and Configuration
   experience, identifying hidden null values and limited in-place editing as causes of
   duplicate support requests." I read that today while verifying titles and dates. It is
   profile prose, not one of my listed local sources, so I gave it no credit. If Lucas confirms
   it, record it in `DOSSIER.md` and the Architect can then write the bullet from a proper
   source. That single confirmation would clear this row.

5. **`Vitest` and `Jest` are attributed to DexCare, and `DOSSIER.md` scopes them to Luizalabs
   and Lippaus — factual integrity, writable — new this round.** Raw line 23 reads `Improved
   maintainability across services by using Vitest and Jest for testing, Datadog for debugging,
   and lint and complexity limits for clean code.` That bullet sits in the DexCare block.
   `DOSSIER.md` line 130 reads "**Tools used at Luizalabs and Lippaus:** BullMQ, Docker,
   Kubernetes, GCP, ArgoCD, Vitest, Jest." The DexCare seeded stack, read from the repos on disk
   and listed at `DOSSIER.md` lines 66-82, names no test framework at all; the DexCare AI entry
   names "testing" as part of codebase enforcement but no tool. `Datadog` in the same bullet
   **is** supported for DexCare, at `DOSSIER.md` line 75. So the sentence mixes one sourced tool
   with two tools sourced to different employers. The `testing` token itself stays supported at
   DexCare, so Gate 2 R6 does not change. **Fix by either** moving `Vitest` and `Jest` out of the
   DexCare bullet and naming them in a Luizalabs or Lippaus bullet, **or** asking Lucas to
   confirm the DexCare test framework and recording it in `DOSSIER.md` first. Do not simply
   delete the testing evidence: the posting requires the `testing` token and the AI-at-DexCare
   dossier entry supports it without a tool name.

6. **`analyzing requirements` is one inferential step past the dossier wording — low severity,
   worth a confirmation, not a rewrite.** `DOSSIER.md` records, among the bullets Lucas
   approved, "project scoping and stakeholder communication" and "customer-facing features end
   to end". The bullet at lines 45-46 renders that as `leading project scoping and stakeholder
   communication and by analyzing requirements to guide technical implementation decisions`.
   Analyzing requirements is a fair reading of project scoping and round 0 sanctioned this
   wording explicitly, so I am not calling it invented. But it is a paraphrase, not a quotation,
   and the posting's own qualifier `functional and non-functional` is correctly absent. Ask
   Lucas to confirm the phrasing when he answers items 1 to 4, and the row closes cleanly.

7. **Literal posting title absent — Gate 3.1, 5 points — deliberately not fixable.** The CV
   carries `Senior Software Engineer`; the posting title is `Senior Web Software Engineer`.
   CLAUDE.md rule 1 forbids adjusting a title to fit a posting. Recorded so no later round
   "fixes" it.

## Match limits

The posting states no preferred or bonus tier, so there are no unplaced preferred tokens. Every
unplaced token is a required one, and all three are listed as defects 1 to 3.

## Not observable

- Work authorization and time-zone requirements. The posting states neither.
- Whether CI&T treats its "or directly comparable modern web frameworks" clause as satisfied by
  React alone. That is a recruiter's judgement and no document discloses it.
- Which ATS CI&T runs, and therefore which parser handles this file. `ATS-KNOWLEDGE.md` section
  2 names an engine for six vendors and records "not observable" for the rest.
- Whether Lucas has CMS, PHP, Next.js or technical-documentation experience. `DOSSIER.md` is
  silent on all four and I did not ask him.

## Projected scores

- Today, after fix round 1: Gate 0 **8/8 PASS**, Gate 1 **FAIL on 4 rows**, Gate 2 **80/100
  FAIL**, Gate 3 **95/100**.
- Defect 5 is the only writable item left, and it changes no gate score. It is a factual
  attribution fix, not a retrieval fix.
- With a confirmed answer on `Next.js`, `CMS` and `PHP`, and those tokens placed in `Skills`
  plus one `Experience` bullet each: required points 45 of 45, Gate 2 **100/100 PASS**. Defect 4
  would additionally need the documentation confirmation to clear Gate 1 in full.
- With no answer from Lucas, this application cannot pass Gate 1 or Gate 2 by any edit.

No blended score is emitted. There is no such thing as a vendor ATS score out of 100; see the
myth table in `ATS-KNOWLEDGE.md` section 1.
