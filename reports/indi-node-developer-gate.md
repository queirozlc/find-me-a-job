# ATS Analysis — resumes/indi-node-developer-en.pdf vs indi-node-developer
Segment: agency   Date: 2026-09-02

Posting: INDI Staffing Services, Node Developer - Remote Work.
Source read: `~/career/jobs/indi-node-developer.md` (verbatim capture by Kestrel).
Posting URL as recorded in that file: https://www.linkedin.com/jobs/view/4462406496/
I did not open that URL. I graded against the quoted text in the job file.

Extraction performed before any judgement:
```
pdftotext -layout indi-node-developer-en.pdf - > extracted-layout.txt
pdftotext         indi-node-developer-en.pdf - > extracted-raw.txt
```
Raw extraction: 3794 bytes, 1 page. Gate 0 and Gate 2 judged on the raw file.

## Verdict

PASSES ALL GATES.

Gate 0 carries four failures. All four come only from the two-column
`tabular*` role header. Under the accepted exception in `RUBRIC.md`
(Lucas, 2026-09-01) they are reported, not blocking. No other cause was found.
Gate 1 has no FAIL.

## Gate 0 — Parse integrity

| # | Check | Result | Offending text |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 3794 bytes of clean text recovered |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes, 0 `?` characters, 0 U+FB01/FB02/FB00 ligature glyphs. `workflow` found 3 times, `office` 2 times, both intact. Non-ASCII inventory: `•` x13, `ó` x4, form feed x1 |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc` |
| 0.4 | Section headers present verbatim | PASS | Standalone raw lines 5, 10, 20, 73: `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`. Uppercase rendering allowed |
| 0.5 | Employment-block segmentation | FAIL, header only, not blocking | Every role splits into three raw blocks. Example, raw lines 21-25: `DexCare` / `Senior Software Engineer` / (blank) / `Jan 2026 - Present` / `Remote` |
| 0.6 | Date parseability | FAIL, header only, not blocking | No date sits on the title line. `Senior Software Engineer` is raw line 22, `Jan 2026 - Present` is raw line 24, one blank line between them. Same shape for all four roles and for FAESA. Format itself is correct: `Mon YYYY - Mon YYYY`, ASCII hyphen, all five date strings |
| 0.7 | Reading order | FAIL, header only, not blocking | Raw order is company, title, dates, location. Layout order is company + dates on one line, then title + location. The two extractions disagree on the order of the title block and the date block |
| 0.8 | No forbidden constructs | FAIL, header only, not blocking | `\resumeSubheading` wraps the header in `\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}`, source line 40. No image of text, no text box, no contact icon, no photo anywhere |

Cause check: I looked for any second cause of 0.5, 0.6, 0.7 or 0.8. There is
none. Bullets wrap as plain text. Skills is a plain list. Education uses the
same header macro. Every failure traces to the one accepted construct.

## Gate 1 — Knockouts

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | posting silent on authorization and on contract shape | not stated |
| Location or time-zone overlap | posting: `Location as shown: Brazil`, `Workplace type as shown: Remote` | PASS. Contact block city is `Vitória, ES, Brazil`. Graded on the contact block only, per RUBRIC |
| Minimum years of experience | posting: `Node.js Experience: 5+ years of experience in Node development` | PASS on the document. Summary states `5+ years of experience in Node development`. See "Claims I could not verify" for the trace problem behind this string |
| English proficiency requirement | posting: `Language Skills: Advanced English level` | PASS. Summary states `I have an Advanced English level: Advanced / C1 from daily work with a US team`. DOSSIER records Advanced / C1 and daily English-only work with US teams at DexCare as [FACT, Lucas 2026-09-01] |
| Degree requirement | posting states none | not stated |

Each required skill, present verbatim in the raw extraction:

| Required skill, posting words | Verbatim in resume |
|---|---|
| `5+ years of experience in Node development` | yes |
| `SQL and NoSQL databases` | yes |
| `microservices and cloud platforms` | yes |
| `Advanced algorithm knowledge` | **no** |
| `IT infrastructure knowledge` | **no** |
| `Intermediate agile methodologies management` | yes |
| `SOLID principles` | yes |
| `clean code` | yes |
| `scalable solutions` | yes |
| `software design patterns` | yes |
| `developing entire applications from scratch` | yes |
| `automated tests and CI/CD pipelines` | yes |
| `version control systems` | yes |
| `Advanced English level` | yes |

The two absent skills are scored as Gate 2 losses, not as Gate 1 knockouts.
The Maestro brief classifies algorithm depth and IT-infrastructure depth as
gaps and instructs that they must not be invented. Absent is the correct
state. Gate 1 result stands at PASS.

## Gate 2 — Retrieval coverage: 61/100

The posting has one requirement list and no preferred list. Every token below
is `required`, weight 3. Soft skills and benefits text are discarded.

Placement ladder. The RUBRIC ladder gives four rungs. Two tokens on this
document sit outside those rungs, so I decomposed the ladder into the additive
form that reproduces every published rung exactly, and used it for all tokens:
Skills = 1, Experience in context = 2, Summary or job title = 1, cap 4.
Absent = 0. This reproduces 0, 1, 3 and 4 without change.

| # | Token, posting words | Skills | Experience | Summary/title | Points |
|---|---|---|---|---|---|
| 1 | Node.js | yes | yes, DexCare | yes | 4 |
| 2 | 5+ years of experience in Node development | no | no | yes | 1 |
| 3 | SQL | yes | yes, DexCare | no | 3 |
| 4 | NoSQL | yes | yes, DexCare | no | 3 |
| 5 | microservices | yes | yes, DexCare | no | 3 |
| 6 | cloud platforms | yes | yes, DexCare | no | 3 |
| 7 | Advanced algorithm knowledge | no | no | no | 0 |
| 8 | IT infrastructure knowledge | no | no | no | 0 |
| 9 | agile methodologies | yes | yes, Lippaus mid-level | no | 3 |
| 10 | SOLID principles | yes | yes, DexCare | no | 3 |
| 11 | clean code | yes | yes, DexCare | no | 3 |
| 12 | scalable solutions | yes | yes, DexCare | no | 3 |
| 13 | software design patterns | yes | yes, DexCare | no | 3 |
| 14 | developing entire applications from scratch | no | yes, Lippaus mid-level | no | 2 |
| 15 | automated tests | yes | yes, DexCare and Luizalabs | no | 3 |
| 16 | CI/CD pipelines | yes | yes, Luizalabs | no | 3 |
| 17 | version control systems | yes | yes, DexCare | no | 3 |
| 18 | Advanced English level | no | no | yes | 1 |

Sum of points: 44. Denominator: 18 tokens x 4 x weight 3, reduced by the
uniform weight to 18 x 4 = 72.
coverage = 100 x 44 / 72 = 61.1 → **61**

Stuffing penalty: 0.
- No posting token reaches 4 or more exact occurrences. Highest exact counts
  are `Node.js` 3, `automated tests` 3.
- No posting token sits in Skills without supporting evidence in Experience.

Missing required tokens: `Advanced algorithm knowledge`, `IT infrastructure
knowledge`.

Partial-placement tokens, worth raising with the Architect because the cost is
cheap to recover:
- `Advanced English level` and `5+ years of experience in Node development`
  score 1 each. Both sit in Summary alone. Neither is in Skills.
- `developing entire applications from scratch` scores 2. It sits in a Lippaus
  bullet alone. It is not in Skills.

## Gate 3 — Human scan: 93/100

| # | Check | Points | Note |
|---|---|---|---|
| 3.1 | Target title in the top 15% of the document | 10 / 15 | The posting title `Node Developer` does not appear anywhere on the CV. At ~4.6% of the raw text the Summary carries `Senior Software Engineer`, and at ~5.7% it carries `Node development`. Title equivalence is present in the right place. The verbatim posting title is not. Partial award, and I state the reason rather than round it either way |
| 3.2 | The 3 most relevant bullets in the most recent role, in its first 3 lines | 20 / 20 | DexCare bullets 1, 2 and 3 are the backend/microservices bullet, the SQL and NoSQL bullet, and the REST API / scalable solutions bullet. Those are the three most relevant to this posting and they lead the role |
| 3.3 | Bullet voice | 15 / 15 | See the voice audit below. All 13 bullets pass |
| 3.4 | At least 3 bullets carry a real, defensible number | 15 / 15 | Six numbered bullets: 15%, 25%, 7%, 20%, 18%, 26%. Every one traces to the DOSSIER metric list |
| 3.5 | Length: 1 page | 10 / 10 | `pdfinfo` reports Pages: 1, letter |
| 3.6 | No unsupported buzzwords | 10 / 10 | No `team player`, `results-driven`, `passionate`, `world-class`, `ninja`, `rockstar`. The 17 printed `[UNVERIFIED]` markers are claims under the truth policy, not buzzwords, and are graded below instead |
| 3.7 | Skills grouped by category | 10 / 10 | Eight labelled groups: Languages and runtimes, Backend and architecture, Data and messaging, Practices, Delivery and testing, Methods, Cloud and operations, Frontend and AI tooling |
| 3.8 | Scannable: consistent spacing, bold titles, adequate white space | 3 / 5 | Two defects. DexCare bullet 4 is a six-item comma chain that runs three full lines and reads as a list, not as an accomplishment. DexCare leads three of its five bullets with `Reduced`, which flattens the left edge a recruiter scans down |

Total: 10 + 20 + 15 + 15 + 10 + 10 + 10 + 3 = **93 / 100**

### Voice audit, CV-SPEC and CLAUDE.md section 9

Leading word of every bullet, in document order:

DexCare: Built, Reduced, Reduced, Improved, Reduced.
Luizalabs: Built, Improved, Cut, Kept.
Lippaus Distribuidora, Mid-level: Supported, Increased, Delivered.
Lippaus Distribuidora, Entry-level: Built.

- All 13 are past tense. PASS.
- All 13 omit the subject. PASS.
- No bullet begins with `I` or `Eu`. PASS.
- No `Responsible for`, no present tense, no third person. PASS.
- Summary uses `I` four times: `I am`, `I build`, `I have`, `I integrate`. PASS.

### Titles and dates, checked character for character against DOSSIER LinkedIn ground truth

| Field | LinkedIn ground truth | On the CV | Result |
|---|---|---|---|
| DexCare title | `Senior Software Engineer` | `Senior Software Engineer` | match |
| DexCare dates | `Jan 2026 - Present` | `Jan 2026 - Present` | match |
| DexCare location | `Remote` per CLAUDE.md section 3 | `Remote` | match |
| Luizalabs company | `Luizalabs` | `Luizalabs` | match |
| Luizalabs title | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Luizalabs dates | `Jan 2024 - Jan 2026` | `Jan 2024 - Jan 2026` | match |
| Luizalabs location | `Remote` per CLAUDE.md section 3 | `Remote` | match |
| Lippaus company | `Lippaus Distribuidora` | `Lippaus Distribuidora` | match |
| Lippaus title 1 | `Mid-level Software Engineer` | `Mid-level Software Engineer` | match |
| Lippaus dates 1 | `Jan 2023 - Jan 2024` | `Jan 2023 - Jan 2024` | match |
| Lippaus title 2 | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` | match |
| Lippaus dates 2 | `Mar 2021 - Jan 2023` | `Mar 2021 - Jan 2023` | match |
| Lippaus location | `Vitória, ES, Brazil` per CLAUDE.md section 3 | `Vitória, ES, Brazil` | match |
| FAESA dates | `Feb 2022 – Dec 2025` | `Feb 2022 - Dec 2025` | match on the period. The glyph is the ASCII hyphen that CV-SPEC item 5 requires, which CLAUDE.md rule 1 permits |
| FAESA degree | `Bachelor's degree , Information Systems` | `Bachelor's degree, Information Systems` | the CV drops one space before the comma. CLAUDE.md rule 1 binds titles and dates, not the degree string. Reported only |

Both promotion roles are kept. The promotion signal is preserved.

### Ruby and Rails token scan

`grep -in 'ruby\|rails'` on `resumes/indi-node-developer-en.tex`, on
`extracted-raw.txt`, and on `extracted-layout.txt`: zero hits in all three.
PASS.

## Defects, ranked by cost

1. **`Advanced algorithm knowledge` and `IT infrastructure knowledge` are
   absent** — Gate 2, 6 points of the 39 lost. Both are stated requirements.
   The Maestro brief calls them gaps and forbids invention, so this is a
   correct loss, not an error. No fix unless Lucas supplies a fact. If he can
   defend either one, the cheapest recovery is one Skills entry plus one
   DexCare or Luizalabs bullet clause carrying the posting's own phrase.

2. **`Advanced English level` scores 1 of 4** — Gate 2. The phrase sits in the
   Summary alone. Adding an English entry to a Skills group, for example a
   `Languages` line reading `English: Advanced / C1 | Portuguese: native`,
   raises the token from 1 to 2 and gives a recruiter a fixed place to look.

3. **`5+ years of experience in Node development` scores 1 of 4** — Gate 2.
   Same cause. It is in the Summary alone. This one is harder to place
   honestly: see item 1 of "Claims I could not verify" before moving it.

4. **DexCare bullet 4 is not an XYZ bullet** — Gate 3.8 and CV-SPEC Bullets.
   Current text: `Improved daily delivery quality by applying SOLID principles
   [UNVERIFIED], clean code [UNVERIFIED], software design patterns
   [UNVERIFIED], version control systems [UNVERIFIED], Git [UNVERIFIED], and
   automated tests in Claude Code and Codex environments.` It has X and Z but
   no Y. `daily delivery quality` is not a measure. It also stacks five
   markers in one sentence, which is the least readable line on the page.
   CV-SPEC requires every bullet to be XYZ.

5. **Left-edge verb monotony at DexCare** — Gate 3.8. `Built, Reduced,
   Reduced, Improved, Reduced`. Three of five bullets open with the same verb,
   in the block a recruiter reads first.

6. **`developing entire applications from scratch` scores 2 of 4** — Gate 2.
   It is in a Lippaus bullet with no Skills placement. A Skills entry raises
   it to 3.

7. **`Agentic workflows` sits in Skills with no Experience bullet carrying the
   token** — CV-SPEC content rule, "every load-bearing technology appears in
   Skills **and** in context inside an Experience bullet". The Summary carries
   `AI-driven agentic workflows`; no Experience bullet does. The DexCare AI
   bullet names Claude Code and Codex but not the phrase. This did not trigger
   the Gate 2 stuffing penalty, because `Agentic workflows` is not a posting
   token.

8. **`RabbitMQ` and `AMQP` appear inside a DexCare Experience bullet** —
   DOSSIER records them as `Skills token only (RabbitMQ, AMQP), no service
   names on the CV` [FACT, Lucas 2026-09-01]. The bullet reads `...with
   PostgreSQL, DynamoDB, Redis, RabbitMQ, and AMQP.` This is a deviation from
   the recorded instruction. I do not know whether Lucas meant to restrict the
   placement or only to forbid internal service names. Not observable from the
   dossier text. Ask Lucas.

9. **The word `Node` reads four times** — CV-SPEC, "cap any term at 3
   appearances". `Node.js` appears 3 times and `Node development` once. As
   exact tokens neither reaches 4, so Gate 2 applies no penalty. As a human
   reading, the stem shows four times. Reported, no action recommended.

10. **`Bachelor's degree, Information Systems` drops the space before the
    comma** that LinkedIn renders. Outside CLAUDE.md rule 1, which binds
    titles and dates. Reported, no action recommended.

11. **Four Gate 0 header failures** — 0.5, 0.6, 0.7, 0.8, all from the
    accepted `tabular*` role header. Reported under the RUBRIC exception, not
    blocking, and not to be fixed. `reports/macro-bakeoff.md` holds shape A as
    the fallback if a posting is known to route through a strict parser. This
    posting applies through `www.linkedin.com`, which is not such a case on
    anything I can observe.

## Claims I could not verify

### Unmarked claims that do not trace to DOSSIER.md

1. **`5+ years of experience in Node development`**, Summary. This is the one
   I would raise first. The LinkedIn span `Mar 2021` to today is 5 years
   6 months of software engineering. The dossier does not record 5+ years of
   **Node** work. It records TypeScript on Node at DexCare [FACT-OBSERVED],
   `Node, Java, and others` at Luizalabs [FACT], and `PostgreSQL / BullMQ /
   JavaScript / React Native` at Lippaus [FACT]. Node across the whole span is
   plausible from those three entries. It is not stated. The string is a
   verbatim lift of the posting requirement and it ships with no
   `[UNVERIFIED]` marker, so the truth policy's "correct after" step cannot
   catch it mechanically. Lucas confirms or the Architect marks it.

2. **`scalable solutions`**, Skills and DexCare bullet 3, unmarked. It comes
   from the same posting requirement line as `SOLID principles` and `clean
   code`, both of which do carry the marker. The dossier does not record it.
   The treatment is inconsistent within one sentence of the posting.

3. **`Supported nationwide retailer expansion`**, Lippaus mid-level bullet 1.
   The dossier confirms the multi-tenant web and mobile platform on PostgreSQL
   [FACT]. It does not record nationwide expansion or the retailer's reach.

4. **`real-time`** in `real-time visit booking and provider availability`,
   DexCare bullet 1. The dossier records the `visit-booking` and
   `forq-availability` services and event-driven booking [FACT-OBSERVED]. It
   does not state real-time.

5. **`Magazine Luiza's e-commerce operation`**, Luizalabs bullet 1. The
   dossier records the employer and the fiscal / NF-e / SEFAZ domain [FACT].
   It does not describe the operation as e-commerce. Note that CV-SPEC
   explicitly retired the old summary sentence that framed Lucas's focus as
   fiscal systems for a Brazilian e-commerce retailer.

6. **`balancing business requirements with technical constraints`**, Lippaus
   entry-level bullet. The dossier confirms customer-facing features end to
   end and back-office dashboards in JavaScript [FACT]. This phrase is not
   recorded.

### Marked [UNVERIFIED] claims

17 marker occurrences on 9 source lines: 67, 68, 69, 71, 82, 83, 85, 103, 105.
This matches the Architect's own count in
`reports/indi-node-developer-draft.md`. All 17 print on the visible page and
in both extractions.

| Claim | Placements | Why it is not a fact |
|---|---|---|
| `microservices and cloud platforms` | Skills, DexCare bullet 1 | AWS and event-driven booking are facts. The dossier does not label the DexCare work microservices |
| `SQL and NoSQL databases` | Skills, DexCare bullet 2 | PostgreSQL and DynamoDB are facts. The broader NoSQL claim is not recorded |
| `SOLID principles` | Skills, DexCare bullet 4 | Not in the dossier |
| `clean code` | Skills, DexCare bullet 4 | Not in the dossier |
| `software design patterns` | Skills, DexCare bullet 4 | Not in the dossier |
| `version control systems` | Skills, DexCare bullet 4 | Not in the dossier |
| `Git` | Skills, DexCare bullet 4 | Not in the dossier |
| `Intermediate agile methodologies management` | Skills, Lippaus mid-level bullet 3 | Project scoping and stakeholder communication are facts. Agile methodology use and a management level are not recorded |
| `developing entire applications from scratch` | Lippaus mid-level bullet 1 | The dossier states Lucas built the platform. It does not state he started it from scratch |

Every one of the nine is an ecosystem token or a generic engineering practice
under CLAUDE.md section 4, so claiming it and marking it is the correct
handling. Lucas confirms or strikes each before applying.

### Numbers, traced

| Number on the CV | DOSSIER entry | Result |
|---|---|---|
| wrong bookings reduced 15% | D2, `reduced wrong bookings by 15%` | traces |
| authentication friction reduced 25% | D3, `reduced authentication friction by 25%` | traces |
| release risk reduced 7% | D5, `release risk reduced by 7%` | traces |
| invoice processing throughput +20% | L2, `20% improvement in invoice processing throughput` | traces |
| support tickets cut 18% | L3, `18% fewer support tickets` | traces |
| processing capacity +26% | P2, `26% more processing capacity` | traces |
| `5+ years` | none | **does not trace.** See claim 1 above |

No fabricated number was found. The only numeric claim without a dossier entry
is the years-of-experience string.

### Not observable

- Whether INDI Staffing Services gates on work authorization, entity type,
  contract shape, or a degree. The quoted posting text is silent on all four.
  I wrote `not stated`, not `pass`.
- Whether the `RabbitMQ` and `AMQP` restriction in the dossier was about
  placement or only about internal service names. The dossier sentence carries
  both readings.
- Whether this posting routes through a strict-parsing ATS. The apply
  destination host is `www.linkedin.com`. Nothing further is observable.

## Fix list for the Architect

none

Gate 0 has no blocking failure. Its four failures are the accepted `tabular*`
header exception and must not be fixed. Gate 1 has no FAIL. Nothing on this
document blocks.

The Gate 2 and Gate 3 items in "Defects, ranked by cost" are improvements, not
blockers, and the claims in the section above it are Lucas's call, not the
Architect's.
