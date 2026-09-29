# ATS Analysis — resumes/hunts/2026-09-04/tractian-senior-backend-engineer/Lucas-Queiroz-Resume-en.pdf vs tractian-senior-backend-engineer
Segment: not observable (the posting file records `Segment: not observable`; company origin not stated)   Date: 2026-09-04

## Verdict
BLOCKED at Gate 1.

Two more blockers stand outside the Gate 1 row set and must be fixed in the same pass:
- **Factual integrity, CLAUDE.md rule 1.** Two role date ranges do not match the live
  LinkedIn profile. Read read-only through the `Profile Check` portal on 2026-09-04.
- **Gate 2 required-token placement.** The non-relational database requirement holds
  `Skills` placement only.

Gate 0 is fully PASS.

## Sources actually read
- `~/career/AGENTS.md`, `~/career/CLAUDE.md`, `~/career/RUBRIC.md`, `~/career/ATS-KNOWLEDGE.md`,
  `~/career/CV-SPEC.md`, `~/career/DOSSIER.md`.
- `~/career/jobs/tractian-senior-backend-engineer.md` (posting text plus Maestro brief).
- The CV source `.tex` and the compiled PDF, plus both extractions.
- `Profile Check` portal, read-only, no edit action sent:
  - https://www.linkedin.com/in/queiroz-lucas/details/experience/
  - https://www.linkedin.com/in/queiroz-lucas/details/education/
- Original posting URL https://www.linkedin.com/jobs/view/4443416703/ was **not** re-opened.
  Posting text is quoted from the local job file only.
- The four PDFs under `~/Documents/Resumes/` were not opened. They are invalid sources.

## Extraction step (mandatory, performed first)
```
pdftotext -layout Lucas-Queiroz-Resume-en.pdf - > extracted-layout.txt
pdftotext         Lucas-Queiroz-Resume-en.pdf - > extracted-raw.txt
```
Gate 0 and Gate 2 are judged on the raw file. 64 content lines. 1 page.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 64 clean lines. `pdfimages -list` returns zero images, so the page is not a scan. |
| 0.2 | Glyph integrity | PASS | Zero codepoints in U+FB00-U+FB06. Zero `\x00` and zero U+FFFD. Probe words extract intact: `workflows` (lines 8, 16, 56), `office` (lines 42, 56), `fiscal` (line 42), `workflow` (line 42). The `fontspec` + `Ligatures=NoCommon` fix in the source works. |
| 0.3 | Contact block recoverable, in the body | PASS | Raw line 3: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. Source has `\pagestyle{empty}` and the block sits inside `\begin{center}` in the body, not a header or footer. |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 10, 18, 59 carry `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION` as standalone lines. Source strings are `Summary`, `Skills`, `Experience`, `Education`. Uppercase rendering is allowed by the rubric. |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks in the raw stream, none merged and none split: DexCare (19-33), Luizalabs (35-42), Lippaus Distribuidora Mid-level (44-50), Lippaus Distribuidora Entry-level (52-57). Each block prints Company / Title / Location / Dates as consecutive lines, and a blank line closes it. The two Lippaus roles each repeat the company line, so the promotion cannot collapse. |
| 0.6 | Date parseability | PASS **on parseability only** | Each role carries `Mon YYYY - Mon YYYY` on its own line adjacent to the title: lines 22, 38, 47, 55, 63. ASCII hyphen throughout, no EN DASH. **The values themselves are wrong on two roles. See the Factual integrity section.** |
| 0.7 | Reading order | PASS | Raw and layout agree on every adjacent block: name, contact, Summary, Skills, the four roles in the same order, Education. |
| 0.8 | No forbidden constructs | PASS | Source uses `itemize` only. No `tabular`, no `tabular*`, no `tcolorbox`, no `minipage`. `pdfimages -list` is empty, so no photo and no icon. Fonts are four embedded subsets with `uni` mapping. |

## Gate 1 — Knockouts

| Check | Source | Result | Evidence |
|---|---|---|---|
| Work authorization / entity type | posting | not stated | The Requirements block names no authorization or entity type. Employment type shows `Full-time`. |
| Location or time-zone overlap | posting | not stated | Location shows `São Paulo, São Paulo, Brazil`, workplace type `Remote`. No overlap window is stated in the text. CV prints `Vitória, ES, Brazil` and prints no UTC offset, as CLAUDE.md rule 3 demands. |
| Minimum years of experience | posting | PASS | Posting: "5+ years of backend development experience". CV Summary line 6: "5+ years of backend development". LinkedIn dates give Mar 2021 to Sep 2026, 5 yrs 6 mos. The claim survives the date correction below. |
| English proficiency requirement | posting | PASS (bonus only) | English is under "Bonus points", not Requirements. CV Skills line 16: `Advanced English (C1)`. |
| **Portuguese proficiency requirement** | posting | **FAIL** | Posting Requirements, verbatim: "Fluency in Portuguese." No Portuguese token appears anywhere in the raw extraction (0 occurrences). The Brazilian location, `Lippaus Distribuidora`, `Magazine Luiza` and `SEFAZ` are employer and location facts. RUBRIC Gate 1 states directly: "Do not infer evidence from an unrelated title, employer, or location." Absent resume evidence is a FAIL. |
| Degree requirement | posting | PASS | Posting: "Bachelor's degree in Computer Science, Engineering, or a related technical field." CV Education lines 60-63: `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025`. Information Systems is a computing degree and reads as the posting's own "related technical field". |
| Runtime requirement | posting | PASS | Posting: "Strong programming skills in Go, Python, Node.js, and/or Rust." This is an alternative set. `Node.js` and `Go` both carry Skills and Experience placement. |
| Messaging requirement | posting | PASS | Posting: "event-driven applications using messaging technologies like Kafka, RabbitMQ, BullMQ or similar." Alternative set. `RabbitMQ` and `BullMQ` both carry Skills and Experience placement. |
| Microservices and distributed system design | posting | PASS | Cumulative. Both halves carry Skills and Experience placement. |
| Relational **and** non-relational databases | posting | PASS on presence, FAILS Gate 2 on placement | Cumulative requirement. Relational: `PostgreSQL` present. Non-relational: `DynamoDB` and `Redis` present verbatim, but in `Skills` only. Gate 1 asks presence, so PASS here; the placement failure blocks in Gate 2. |
| Mission-critical backend services in high-growth, product-driven environments | posting | PASS | Not a retrieval token; discarded from Gate 2 per RUBRIC Step 1 as buzzword-heavy. Narrative evidence carried by the DexCare healthcare scheduling bullets and the Luizalabs e-commerce invoice bullet. |

## Gate 2 — Retrieval coverage: 67/100, FAIL

Scoring convention, stated so the run is reproducible:
- An **alternative set** in the posting ("and/or", "like X, Y, Z or similar", "e.g.") is scored
  once, as one requirement, on the best-placed member that DOSSIER.md actually supports.
- The **degree** and the **years-of-experience** requirements are hard requirements but never
  occupy `Skills` or `Experience`. Scoring them would force an artificial 0. They live in
  Gate 1 only, and are excluded from the denominator here.
- Placement points: absent 0, `Skills` only 1, `Experience` only 2, both 3.

### Required requirements, weight 3

| # | Requirement, posting wording | Token scored | Skills | Experience | Points |
|---|---|---|---|---|---|
| R1 | "Strong programming skills in Go, Python, Node.js, and/or Rust" | `Node.js` | line 11 | line 39 "distributed tax services in Node.js and" | 3 |
| R1b | same alternative set | `Go` | line 11 | lines 39-40 "Node.js and / Go." | 3 |
| R2 | "messaging technologies like Kafka, RabbitMQ, BullMQ or similar" | `RabbitMQ` | line 12 | line 23 "with RabbitMQ / messaging" | 3 |
| R2b | same alternative set | `BullMQ` | line 12 | lines 41, 49 | 3 |
| R3 | "event-driven architecture" / "event-driven applications" | `event-driven` | line 12 | line 23 "event-driven TypeScript APIs" | 3 |
| R4 | "Deep understanding of microservices architecture" | `microservices` | line 12 | line 32 "shared multi-tenant microservices" | 3 |
| R5 | "distributed system design" | `distributed systems` | line 12 | line 25 "across distributed systems" | 3 |
| R6 | "relational (e.g., PostgreSQL, ClickHouse)" | `PostgreSQL` | line 13 | lines 25, 50 | 3 |
| **R7** | **"non-relational databases (e.g., ScyllaDB, Cassandra,, MongoDB)"** | `DynamoDB` | line 13 | **absent** | **1** |
| R7b | same requirement, second supported candidate | `Redis` | line 13 | **absent** | 1 |
| R8 | "resilient APIs", "Develop and maintain APIs" | `APIs` | line 12 | lines 23, 27 | 3 |
| **R9** | **"Fluency in Portuguese."** | `Portuguese` | **absent** | **absent** | **0** |

R1/R1b, R2/R2b and R7/R7b are alternative or candidate pairs inside one requirement. Each pair
counts once. Requirement scores used: R1=3, R2=3, R3=3, R4=3, R5=3, R6=3, R7=1, R8=3, R9=0.

### Preferred requirements, weight 1

| # | Requirement | Token | Skills | Experience | Points |
|---|---|---|---|---|---|
| P1 | "Fluency in English" (Bonus points) | `English` | line 16 `Advanced English (C1)` | absent, Summary line 7 only, and Summary is not Experience | 1 |
| P2 | "Contributions to open-source or personal projects" | `open-source` | absent | absent. Only the bare `github.com/queirozlc` URL on line 3 | 0 |

### Arithmetic
```
required:  sum(points * 3) = (3+3+3+3+3+3+1+3+0) * 3 = 22 * 3 = 66
           denominator      = 3 * 3 * 9                        = 81
preferred: sum(points * 1) = (1 + 0) * 1                       =  1
           denominator      = 3 * 1 * 2                        =  6
coverage = 100 * (66 + 1) / (81 + 6) = 100 * 67/87 = 77
```

### Step 5, stuffing penalty
Literal-string counts in the raw extraction, 4 or more occurrences:

| Token | Count | Where |
|---|---|---|
| `React` | 5 | line 6 Summary, line 14 twice (`React \| React Native`), line 28 DexCare, line 50 Lippaus |
| `multi-tenant` | 4 | line 7 Summary, lines 27, 32 DexCare, line 50 Lippaus |

Penalty: -5 each, -10 total. This is the rubric's human-reaction penalty, not a machine one.
Note for the Architect: two of the five `React` hits come from the string `React Native`, which
is a different technology. The rubric rule is a literal-string rule, so the penalty applies as
written. Judge the readability cost yourself before cutting anything.

**Gate 2 final: 77 - 10 = 67/100.**

**Required tokens without both `Skills` and `Experience` placement:**
`Portuguese` (0 points, absent entirely), and the non-relational database requirement, where
`DynamoDB` and `Redis` both hold 1 point, `Skills` only.

## Gate 3 — Human scan: 93/100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 10 / 15 | Top 15% of 64 lines is lines 1-10. Line 6 carries `Senior Software Engineer` and, in the same sentence, `backend development`. The literal posting title `Senior Backend Engineer` appears nowhere. 5 points deducted for the absent literal string. **The deduction is not recoverable:** CLAUDE.md rule 1 and DOSSIER.md fix the CV title at `Senior Software Engineer` and forbid adjusting a title to fit a posting. Do not "fix" this. |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | 20 / 20 | DexCare bullets 1-3 are the three that carry this posting's core tokens: event-driven APIs plus RabbitMQ, distributed systems plus PostgreSQL, multi-tenant REST APIs. Correct ordering for this posting. |
| 3.3 | Every bullet starts with a past-tense action verb and describes an outcome | 15 / 15 | All 12 bullets: Supported, Reduced, Reduced, Reduced, Improved, Reduced, Delivered, Improved, Reduced, Increased, Supported, Supported. Zero present-tense openers, zero "Responsible for", zero third person, no bullet opens with `I`. Matches CLAUDE.md section 9 and CV-SPEC. Summary uses `I` explicitly, as required. |
| 3.4 | At least 3 bullets carry a real, defensible number | 15 / 15 | Seven numbers, and every one traces to DOSSIER.md "Bullet metrics supplied by Lucas 2026-09-01": 15% wrong bookings (D2), 25% authentication friction (D3), 7% release risk (D5), 33% pilot friction (D7), 20% invoice throughput (L2), 18% support tickets (L3), 26% processing capacity (P2). No number is invented and no number is rounded off the dossier value. |
| 3.5 | Length: 1 page under 10 years of experience | 10 / 10 | `pdfinfo` reports `Pages: 1`, letter size. |
| 3.6 | No unsupported buzzwords | 10 / 10 | Grep for team player, results-driven, passionate, self-starter, rockstar, ninja, synergy, go-getter, detail-oriented, hard-working: zero hits. |
| 3.7 | Skills grouped by category | 10 / 10 | Six labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing AI and communication. Not a wall. |
| 3.8 | Scannable: consistent spacing, bold titles, adequate white space | 3 / 5 | Company bold, title italic, location and dates plain, consistent across all four roles. Deduct 2: `\resumeRoleGap` is only `\vspace{2pt}`, so in the layout extraction the last bullet of one role sits on the line directly above the next company name (layout lines 33-34, 41-42, 48-49). CV-SPEC section 2 asks for clear vertical space between the last bullet and the next role. Parse safety is unharmed, Gate 0.5 passes; this is a human-eye cost only. Roughly 15% of the page is unused at the bottom, so the space is available. |

**Total: 93/100.**

## Factual integrity — LinkedIn ground truth, checked 2026-09-04

Read read-only through the `Profile Check` portal. No edit action was sent to LinkedIn.

| Field | CV prints | LinkedIn shows today | Result |
|---|---|---|---|
| DexCare employer | `DexCare` | `DexCare · Full-time` | match |
| DexCare title | `Senior Software Engineer` | `Senior Software Engineer` | match |
| **DexCare dates** | **`Jan 2026 - Present`** | **`Mar 2026 - Present · 7 mos`** | **MISMATCH** |
| Luizalabs employer | `Luizalabs` | `Luizalabs · Full-time` | match, spelling included |
| Luizalabs title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| **Luizalabs dates** | **`Jan 2024 - Jan 2026`** | **`Jan 2024 - Mar 2026 · 2 yrs 3 mos`** | **MISMATCH** |
| Lippaus employer, both roles | `Lippaus Distribuidora` | `Lippaus Distribuidora` | match |
| Lippaus senior title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Lippaus senior dates | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024 · 1 yr 1 mo` | match |
| Lippaus first title | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | match |
| Lippaus first dates | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023 · 1 yr 11 mos` | match |
| Education | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | match. LinkedIn renders an EN DASH; the CV uses the ASCII hyphen, which is what CLAUDE.md rule 1 and CV-SPEC section 5 require |
| Role locations | DexCare `Remote`, Luizalabs `Remote`, Lippaus `Vitória, ES, Brazil` | DexCare `Seattle, Washington, United States · Remote`, Luizalabs `São Paulo, Brazil · Remote`, Lippaus `Vitória, Espírito Santo, Brazil · On-site` | correct per DOSSIER.md "Role locations": employer cities never print |

**The two date mismatches are not the Architect's arithmetic error.** LinkedIn's own duration
labels are self-consistent with today's date, 2026-09-04: Mar 2026 to Sep 2026 is 7 months, and
Jan 2024 to Mar 2026 is 2 yrs 3 mos. The profile was changed after the DOSSIER.md ground-truth
block was captured on 2026-09-01. **`DOSSIER.md` is therefore stale on these two rows.** I do
not edit `DOSSIER.md`; refreshing it belongs to the Maestro or to Lucas.

The Summary claim `5+ years of backend development` survives the correction. Mar 2021 to
Sep 2026 is 5 yrs 6 mos.

## Metric trace

Every number on the CV, checked against `DOSSIER.md`, not against any old PDF.

| CV number | DOSSIER.md entry | Result |
|---|---|---|
| wrong bookings -15% | D2, "reduced wrong bookings by 15%" | traced |
| authentication friction -25% | D3, "reduced authentication friction by 25%" | traced |
| release risk -7% | D5, "release risk reduced by 7%" | traced |
| pilot friction -33% | D7, "reducing friction for piloting new clients by 33%" | traced |
| invoice throughput +20% | L2, "20% improvement in invoice processing throughput" | traced |
| support tickets -18% | L3, "18% fewer support tickets" | traced |
| processing capacity +26% | P2, "26% more processing capacity" | traced |
| `5+ years` | not a dossier string; arithmetic on the LinkedIn dates | derived, not invented. Stated as derived. |

No number on the CV lacks a source. No `[UNVERIFIED]` marker appears in the document, and
CLAUDE.md section 4 forbids verification markers for framework, data, cloud and tool tokens.

## Policy checks

| Rule | Result |
|---|---|
| CLAUDE.md 2, no Ruby or Rails token anywhere | PASS. Grep for ruby, rails, sidekiq, activerecord, rspec, devise, pundit, hotwire: zero hits. |
| CLAUDE.md 3, degree Information Systems, FAESA | PASS. |
| CLAUDE.md 3, location `Vitória, ES, Brazil`, nothing more | PASS. |
| CLAUDE.md 3, never print a UTC offset or overlap statement | PASS. Grep for GMT, UTC, timezone, overlap: zero hits. |
| CLAUDE.md 3, Lippaus prints `Vitória, ES, Brazil`; DexCare and Luizalabs print `Remote` | PASS. |
| CLAUDE.md 3, contract detail never printed | PASS. No CLT, PJ, or Fullstack Labs token. |
| CLAUDE.md 9, bullet voice and Summary voice | PASS. See Gate 3.3. |
| CLAUDE.md 11, one language per tailored CV | PASS. English only. Posting language is `en`. No `-pt` sibling in the application folder. |
| CV-SPEC, canonical headers in the source | PASS. `\section{Summary}`, `{Skills}`, `{Experience}`, `{Education}`. |
| CV-SPEC, ASCII hyphen in every date | PASS. Zero EN DASH in the extraction. |
| CV-SPEC, every load-bearing technology in Skills and in an Experience bullet | PARTIAL. `AWS` sits in the Summary (line 7) and in Skills (line 15) with no Experience bullet. Non-blocking for this posting: AWS is not a posting requirement. |
| CV-SPEC, cap any term at 3 appearances | FAIL, minor. `React` 5, `multi-tenant` 4. Already charged as the Gate 2 stuffing penalty. |
| CV-SPEC, AI or LLM mention in Summary and in Experience | PASS. Summary line 8, DexCare bullet 5 (`Claude Code and Codex environments`). |
| Maestro brief, do not claim unsupported alternatives | PASS. Zero occurrences of Kafka, Python, Rust, ClickHouse, ScyllaDB, Cassandra, MongoDB. The Architect correctly refused to invent them. |

## Defects, ranked by cost

1. **DexCare start month is wrong. Factual integrity, CLAUDE.md rule 1. Blocking.**
   `Lucas-Queiroz-Resume-en.tex` line 70 reads `{DexCare}{Jan 2026 - Present}`.
   LinkedIn shows `Mar 2026 - Present`. Change `Jan 2026` to `Mar 2026`.

2. **Luizalabs end month is wrong. Factual integrity, CLAUDE.md rule 1. Blocking.**
   `Lucas-Queiroz-Resume-en.tex` line 82 reads `{Luizalabs}{Jan 2024 - Jan 2026}`.
   LinkedIn shows `Jan 2024 - Mar 2026`. Change `Jan 2026` to `Mar 2026`.
   Related, and not the Architect's task: `DOSSIER.md` "LinkedIn ground truth" still carries the
   2026-09-01 values and is now stale on both rows. The Maestro or Lucas must refresh it, or the
   next tailoring run will reintroduce the same two errors.

3. **Portuguese fluency is a stated posting requirement with no resume evidence. Gate 1 FAIL. Blocking.**
   Posting Requirements, verbatim: "Fluency in Portuguese." Zero Portuguese tokens in the CV.
   **This fix cannot be made from the current sources.** `DOSSIER.md` records only
   "English proficiency: Advanced / C1" and states no Portuguese level. Escalate to Lucas for
   his Portuguese proficiency level, record it in `DOSSIER.md`, and only then place the exact
   token. Target placement once recorded: the Skills line 16 group
   `Testing, AI, and communication: ... | Advanced English (C1)`, plus one Experience bullet
   context that already sits in a Brazilian-language setting, for example the Luizalabs SEFAZ
   bullet on line 86 of the source. Do not assert a proficiency level that Lucas has not given.

4. **The non-relational database requirement holds `Skills` placement only. Gate 2 FAIL. Blocking.**
   Posting Requirements: "Proficiency in both relational (e.g., PostgreSQL, ClickHouse) and
   non-relational databases (e.g., ScyllaDB, Cassandra,, MongoDB), with a focus on performance
   and scalability." The relational half is fully placed. The non-relational half is not:
   `DynamoDB` and `Redis` appear only on Skills line 13,
   `Data: PostgreSQL | DynamoDB | Redis | Drizzle ORM | Sequelize`.
   Place `DynamoDB` in one DexCare Experience bullet. `DynamoDB` and `DynamoDB Streams` are
   observed DexCare stack in `DOSSIER.md` and in `CV-SPEC.md`, so this needs no new fact.
   The natural host is source line 73, which already carries the real-time booking and
   availability work: `Supported real-time booking and provider availability by building
   event-driven TypeScript APIs on Express and Koa with RabbitMQ messaging.`
   Do not claim ScyllaDB, Cassandra, MongoDB or ClickHouse. None is supported.

5. **Stuffing penalty, -10 on Gate 2. Non-blocking.**
   `React` appears 5 times and `multi-tenant` 4 times. CV-SPEC caps any term at 3.
   Cutting one `React` and one `multi-tenant` recovers 10 Gate 2 points. Lowest-value
   occurrences to consider: the Summary `React` on line 55 of the source, whose Languages
   and Frontend Skills groups already carry the token, and one of the two DexCare
   `multi-tenant` uses on source lines 75 and 78.

6. **`AWS` has no Experience placement. CV-SPEC content rule. Non-blocking here.**
   `AWS` appears in the Summary and in Skills only. It is not a TRACTIAN requirement, so it
   costs nothing on this posting, but it breaks the CV-SPEC rule that every load-bearing
   technology appears in `Skills` and in context inside an `Experience` bullet.

7. **Role separation is visually tight. Gate 3.8, -2. Non-blocking.**
   `\resumeRoleGap` is `\vspace{2pt}`. In the layout extraction the last bullet of each role
   sits directly above the next company name. CV-SPEC section 2 asks for clear vertical space
   between the last bullet and the next role. About 15% of the page is unused, so the space is
   there. Parse safety is unaffected.

## Match limits

Preferred tokens not placed:
- `open-source`, 0 points. Posting bonus: "Contributions to open-source or personal projects
  demonstrating backend architecture or data processing expertise." The CV carries the bare
  `github.com/queirozlc` URL and no open-source claim. `DOSSIER.md` "Excluded content" holds the
  Rails core / gem contribution claim as unsourced and unusable, and the open-source section
  decision is recorded as "Decision made, not yet applied. Do not act on this until Lucas says
  so." **No open-source claim can be added from current sources.** It needs a named repository,
  PR, or commit from Lucas.
- `English`, 1 point, `Skills` only. Preferred, so it does not block. Adding it to an Experience
  bullet would recover a small amount of Gate 2 score.

Required posting alternatives correctly left unclaimed, because `DOSSIER.md` supports none of
them: `Kafka`, `Python`, `Rust`, `ClickHouse`, `ScyllaDB`, `Cassandra`, `MongoDB`.
Each is a member of an alternative set that a supported token already satisfies, except the
non-relational examples, which is why defect 4 exists.

`ETL` appears in the posting's team description and in "What you'll do" ("scalable ETL
pipelines"), but not in the Requirements block. It is not scored as a required token. It is
absent from the CV, and no ETL fact appears in `DOSSIER.md`, so it cannot be added.

One reading ambiguity, reported and not resolved by me: `DOSSIER.md` records
"**DexCare messaging: RabbitMQ / AMQP** used on services. Skills token only (`RabbitMQ`,
`AMQP`), no service names on the CV." The restriction that sentence names is service names, and
the CV names no DexCare service, so the current DexCare RabbitMQ bullet complies on that
reading. A stricter reading of "Skills token only" would forbid the Experience placement
altogether, which would put it in direct conflict with the Maestro brief, which lists RabbitMQ
as a required token, and with RUBRIC Gate 2, which demands both placements. Lucas or the
Maestro should settle the wording in `DOSSIER.md`. I did not guess it either way.

## What is not observable
- The segment. The posting file records `Segment: not observable` and `Company origin: not
  stated`. I did not classify it.
- Work authorization and time-zone requirements. The posting text states neither.
- Which ATS TRACTIAN runs, and therefore which parser handles this file. No public source names
  an engine for this employer. Nothing in this report is a vendor score. These are our four
  gates, defined in `RUBRIC.md`, and nothing else.
