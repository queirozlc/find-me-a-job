# ATS Analysis — resumes/ciandt-senior-fullstack-en.pdf vs ciandt-senior-fullstack
Segment: agency   Date: 2026-09-02

Extraction (mandatory step, run by Sieve before any judgement):
```
pdftotext -layout resumes/ciandt-senior-fullstack-en.pdf - > extracted-layout.txt
pdftotext         resumes/ciandt-senior-fullstack-en.pdf - > extracted-raw.txt
```
Gate 0 and Gate 2 are judged on `extracted-raw.txt`.

## Verdict
PASSES ALL GATES

Gate 0: PASS. Four rows fail, and every one of them traces only to the
two-column `tabular*` role header. That is the accepted exception set by Lucas
2026-09-01 (RUBRIC.md, CV-SPEC.md item 2): reported, not blocking. No other
cause of a Gate 0 failure is present.
Gate 1: no FAIL.

## Gate 0 — Parse integrity

| # | Check | Result | Offending text |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction is 3737 bytes of clean text |
| 0.2 | Glyph integrity | PASS | Zero U+0000, zero U+FFFD, zero U+FB00-FB06. `back-office` x2 and `workflows` x5 extract intact |
| 0.3 | Contact block recoverable | PASS | `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc` on raw line 3, in the body. `\pagestyle{empty}`, no header, no footer |
| 0.5 | Employment-block segmentation | FAIL (header only, accepted) | Each role splits into two blocks: `DexCare` / `Senior Software Engineer`, blank line, `Jan 2026 - Present` / `Remote`. Same shape on all four roles and on Education |
| 0.4 | Section headers present verbatim | PASS | `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION` are standalone raw lines. Source strings are `\section{Summary}`, `{Skills}`, `{Experience}`, `{Education}`. Uppercase rendering is allowed |
| 0.6 | Date parseability | FAIL (header only, accepted) | Dates sit on their own raw line, separated from the title by a blank line, not on the same line as the title. The format itself is correct: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`, ASCII hyphen throughout |
| 0.7 | Reading order | FAIL (header only, accepted) | Raw order is Company, Title, Dates, Location. Layout order is Company, Dates, Title, Location. The disagreement is confined to the five `tabular*` headers. Section order and bullet order agree |
| 0.8 | No forbidden constructs | FAIL (header only, accepted) | `tabular*` inside `\resumeSubheading`. `pdfimages -list` returns zero images. No photo, no icon, no text box. All four fonts embedded with Unicode maps |

Rows are printed in rubric order 0.1, 0.2, 0.3, 0.5 first because 0.5 is the
highest-value check; 0.4, 0.6, 0.7, 0.8 follow. No row failed for any cause
outside the accepted header exception, so Gate 0 does not block.

Segmentation detail worth stating plainly: no two roles are merged, and the
two Lippaus Distribuidora roles stay separate blocks. The promotion signal
survives extraction.

## Gate 1 — Knockouts

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | posting | not stated. The post names no contract type, no entity type, no authorization requirement |
| Location | posting: `based in Brazil or Colombia` | PASS. Contact block reads `Vitória, ES, Brazil` |
| Time-zone overlap | posting | not stated. Never printed on the CV (Lucas, 2026-09-02); absence is not a FAIL |
| Minimum years of experience | posting | not stated. The post says `Senior` and nothing numeric |
| English proficiency requirement | posting | not stated as a requirement. The resume states it anyway: `My English level is Advanced/C1.` Traces to DOSSIER.md [FACT, Lucas 2026-09-01]. PASS on the resume side |
| Degree requirement | posting | not stated |

Required skills, present verbatim in the raw extraction:

| Posting requirement (posting's words) | Verbatim in resume? |
|---|---|
| `Strong programming experience with JavaScript/TypeScript/Node.js` | PASS. Summary carries the exact string `strong programming experience with JavaScript/TypeScript/Node.js` |
| `focus on backend development` | PASS. Summary: `focused on backend development` |
| `designing or architecting new and existing systems` | PARTIAL. Neither `designing` nor `architecting` appears anywhere. Only `Backend and architecture` in the Skills label |
| `design patterns, reliability, and scalability` | PASS. All three present, each in Skills and in DexCare bullet 1 |
| `developing cloud-native applications and platforms using AWS` | PASS. `cloud-native on AWS` in Skills and in a DexCare bullet |
| `Experience with or a passion for Generative AI` | PASS. `Generative AI` in Skills and in a DexCare bullet |
| `Experience as a mentor, Tech Lead, or Engineering Team Lead` | PASS. This is an OR. `mentoring` and `tech-lead responsibilities` are present. `Tech Lead` and `Engineering Team Lead` are absent as exact strings |
| `based in Brazil or Colombia` | PASS. `Brazil` present in the contact block |

No Gate 1 FAIL. The `designing / architecting` row is PARTIAL, not FAIL: the
posting's own list of what that experience means, design patterns plus
reliability plus scalability, is present verbatim.

## Gate 2 — Retrieval coverage: 60/100

Scoring rules I applied, stated so the number is reproducible:

- Every token below is `required` by the posting's own words. The posting
  states no preferred requirement. Weight 3 on all of them.
- The formula is read as `points_earned = weight * placement_points`, with
  denominator `sum(4 * weight)`. That is the only reading under which a
  perfect document scores 100.
- Matching is case-insensitive. A hyphen and a space are treated as the same
  separator, so `tech-lead` matches `Tech Lead`. A different suffix on a
  shared root of six or more characters counts as present, with the variant
  quoted.
- The title words `Senior` and `Full Stack` and the location word `Brazil`
  are excluded from this table on purpose. Title placement is Gate 3.1;
  location is Gate 1. Scoring them here against a Skills-section tier table
  would produce a misleading zero.

| # | Token (posting's words) | Weight | Observed placement | Placement pts |
|---|---|---|---|---|
| 1 | JavaScript | 3 | Summary + Skills + Lippaus entry bullet | 4 |
| 2 | TypeScript | 3 | Summary + Skills + DexCare bullet 1 | 4 |
| 3 | Node.js | 3 | Summary + Skills + Luizalabs bullet 1 | 4 |
| 4 | backend development | 3 | Summary + Skills label `Backend and architecture`. No Experience bullet | 1 |
| 5 | design patterns | 3 | Skills + DexCare bullet 1 | 3 |
| 6 | reliability | 3 | Skills + DexCare bullet 1 | 3 |
| 7 | scalability | 3 | Skills + DexCare bullet 1 | 3 |
| 8 | designing / architecting | 3 | Skills label only, as `architecture`. No Experience bullet | 1 |
| 9 | cloud-native | 3 | Skills + DexCare bullet 5 | 3 |
| 10 | AWS | 3 | Summary + Skills + DexCare bullet 5 | 4 |
| 11 | Generative AI | 3 | Skills + DexCare bullet 6 | 3 |
| 12 | mentor | 3 | Skills + Lippaus mid bullet 3, as `mentoring` | 3 |
| 13 | Tech Lead | 3 | Skills + Lippaus mid bullet 3, as `tech-lead` | 3 |
| 14 | Engineering Team Lead | 3 | Absent entirely | 0 |

```
sum(placement)      = 39
sum(points_earned)  = 3 * 39 = 117
denominator         = 4 * 3 * 14 = 168
coverage before penalty = 100 * 117 / 168 = 69.6
```

Step 4, stuffing penalty. No scored token reaches 4 occurrences. Two scored
tokens sit in Skills with no supporting evidence anywhere in Experience:

- `backend` / `Backend and architecture` — in the Skills label and in the
  Summary, in no bullet. −5
- `architecture` — in the Skills label only, in no bullet. −5

```
coverage = 69.6 - 10 = 59.6  ->  60/100
```

Missing required tokens: `Engineering Team Lead` (absent). `designing` and
`architecting` (absent as words; only the noun `architecture` is present, and
only in a Skills label).

Two unscored Skills entries also carry no Experience support: `Drizzle ORM`
and `RabbitMQ`. They are not posting tokens, so they do not move the number.
They are a human-scan defect, listed below.

## Gate 3 — Human scan: 86/100

| # | Check | Result | Points |
|---|---|---|---|
| 3.1 | Target title in the top 15% | PARTIAL. The Summary's first six words are `I am a Senior Software Engineer`. The posting title is `Senior Full Stack Engineer`. `Senior` and `Engineer` land at the top; `Full Stack` appears nowhere in the Summary or Skills. The CV title is LinkedIn-locked, so the fix belongs in the Summary body, not in a title | 8 / 15 |
| 3.2 | The 3 most relevant bullets in the most recent role, first 3 lines | PARTIAL. DexCare bullet 1 is on target and carries design patterns, reliability, scalability. The other two headline posting requirements, cloud-native on AWS and Generative AI, sit at bullet 5 and bullet 6. Bullets 1 and 3 each wrap to two lines, so the literal first three lines reach only into bullet 2 | 14 / 20 |
| 3.3 | Past-tense first-person verb, subject omitted, `I` in the Summary | PASS. All 14 bullets lead with a past-tense verb: Built, Integrated, Built, Reduced, Helped build, Built, Built, Moved, Built, Kept, Built, Processed, Led, Built. No present tense. No `Responsible for`. No third person. No bullet starts with `I`. The Summary opens `I am a Senior Software Engineer` and carries `I build`, `I have shipped`, `I integrate` | 15 / 15 |
| 3.4 | At least 3 bullets carry a real, defensible number | PASS. Seven do: 15%, 25%, 7%, 33%, 20%, 18%, 26% | 15 / 15 |
| 3.5 | One page under 10 years experience | PASS. `pdfinfo` reports Pages: 1, letter | 10 / 10 |
| 3.6 | No unsupported buzzwords | PASS. No `team player`, no `results-driven`, no `passionate`. The seven `[UNVERIFIED]` claims are marked claims awaiting Lucas, not buzzwords | 10 / 10 |
| 3.7 | Skills grouped by category | PASS. Seven labelled groups: Programming, Backend and architecture, Data and messaging, Frontend, Cloud and operations, Leadership, Testing and AI tooling | 10 / 10 |
| 3.8 | Scannable | PARTIAL. Bold company, italic title, consistent 5pt role gap, one page, adequate white space. Two ragged wraps hurt the scan: the Skills line 2 orphans `scalability [UNVERIFIED]` onto its own line, and DexCare bullet 1 orphans `[UNVERIFIED] for reliability [UNVERIFIED] and scalability [UNVERIFIED].` onto a second line | 4 / 5 |

Total: 8 + 14 + 15 + 15 + 10 + 10 + 10 + 4 = **86 / 100**

### Titles and dates, checked character for character against DOSSIER.md LinkedIn ground truth

| CV string | LinkedIn ground truth | Match |
|---|---|---|
| `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` / `Remote` | `Senior Software Engineer`, `DexCare`, `Jan 2026 - Present` | exact |
| `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` / `Remote` | `Mid-level Software Engineer`, `Luizalabs`, `Jan 2024 - Jan 2026` | exact |
| `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` / `Vitória, ES, Brazil` | `Mid-level Software Engineer`, `Jan 2023 - Jan 2024` | exact |
| `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` / `Vitória, ES, Brazil` | `Entry-level Fullstack Software Engineer`, `Mar 2021 - Jan 2023` | exact |
| `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | periods exact. Separator is the ASCII hyphen, correct per CLAUDE.md rule 1 as clarified 2026-09-01 and CV-SPEC.md item 5. The degree string drops LinkedIn's stray space before the comma; that is not a title and not a date |

Locations print as CLAUDE.md section 3 requires: DexCare and Luizalabs
`Remote`, Lippaus `Vitória, ES, Brazil`. No employer city appears. No UTC
offset and no time-zone overlap statement appears anywhere on the document.

### Ruby and Rails token check

Zero hits. I grepped the raw extraction and the `.tex` source for `ruby`,
`rails`, `rspec`, `sidekiq`, `activerecord`, `activejob`, `hotwire`, `devise`,
`pundit`, `erb`, `gem`, case-insensitive. Both return nothing.

## Defects, ranked by cost

1. **`backend` appears in no Experience bullet** — Gate 2, −5 stuffing penalty
   and 1 point instead of 3 or 4 on a required token. The posting's first
   requirement is `focus on backend development`. The word lives in the
   Summary and in the Skills label `Backend and architecture`, and in no
   bullet. Highest-value single fix on this document.
2. **`designing` and `architecting` appear nowhere** — Gate 2, −5 penalty and
   1 point on a required token. The posting says `Experience designing or
   architecting new and existing systems`. Only the noun `architecture`
   exists, in a Skills label. DexCare bullet 1 says `Built event-driven
   TypeScript services`, which is the place a verb like `Designed` or
   `Architected` belongs.
3. **`Generative AI` and `cloud-native on AWS` sit at DexCare bullets 5 and 6**
   — Gate 3.2, −6. Both are named requirements in the posting. They are below
   the fold of a fast scan on the most recent role.
4. **`Full Stack` appears nowhere in the Summary or Skills** — Gate 3.1, −7.
   The posting title is `Senior Full Stack Engineer`. The only occurrence in
   the document is `Fullstack` inside the oldest role's LinkedIn-locked title.
   The CV title stays `Senior Software Engineer` per DOSSIER.md; the Summary
   is where the posting's title words can go.
5. **`Engineering Team Lead` absent** — Gate 2, 0 points on a required token.
   Optional fix: the posting requirement is an OR and the `mentor` arm is
   already satisfied. Adding this phrase without a confirmed fact would be a
   new unverified claim, so I do not recommend it unless Lucas confirms it.
6. **`Drizzle ORM` and `RabbitMQ` sit in Skills with no Experience support** —
   Gate 3, human reaction. Neither appears in any bullet. Both are DOSSIER
   facts, so this is a placement defect, not a truth defect.
7. **Two ragged wrap orphans** — Gate 3.8, −1. Skills line 2 orphans
   `scalability [UNVERIFIED]`; DexCare bullet 1 orphans `[UNVERIFIED] for
   reliability [UNVERIFIED] and scalability [UNVERIFIED].` Both resolve
   themselves when Lucas strikes or confirms the markers.
8. **Left-edge verb monotony** — Gate 3, human reaction, no rubric row. `Built`
   opens 6 of the 14 bullets, including three of the six DexCare bullets. Not
   scored, worth noting.

None of the eight is blocking.

## Claims I could not verify

### `[UNVERIFIED]` markers: 14 occurrences, 7 distinct claims

Counted with `grep -o UNVERIFIED` on the raw extraction. The count matches the
Architect's own list in `reports/ciandt-senior-fullstack-draft.md` and the
ledger's `Open:` line.

| Claim | Occurrences | Where |
|---|---|---|
| `design patterns [UNVERIFIED]` | 2 | Skills `Backend and architecture`; DexCare bullet 1 |
| `reliability [UNVERIFIED]` | 2 | Skills `Backend and architecture`; DexCare bullet 1 |
| `scalability [UNVERIFIED]` | 2 | Skills `Backend and architecture`; DexCare bullet 1 |
| `cloud-native on AWS [UNVERIFIED]` | 2 | Skills `Cloud and operations`; DexCare bullet 5 |
| `Generative AI [UNVERIFIED]` | 2 | Skills `Testing and AI tooling`; DexCare bullet 6 |
| `mentoring [UNVERIFIED]` | 2 | Skills `Leadership`; Lippaus mid-level bullet 3 |
| `tech-lead responsibilities [UNVERIFIED]` | 2 | Skills `Leadership`; Lippaus mid-level bullet 3 |

All seven are ecosystem-token claims the Maestro brief directed, under
CLAUDE.md section 4. Lucas confirms or strikes each one before applying.

### Numbers, traced against DOSSIER.md

Every percentage on the document traces to the bullet metrics Lucas supplied
2026-09-01:

| Number | Bullet | DOSSIER ID |
|---|---|---|
| 15% wrong bookings | DexCare, Epic EMR time-slot | D2 |
| 25% authentication friction | DexCare, Auth0 JWT multi-tenant | D3 |
| 7% release risk | DexCare, feature flags | D5 |
| 33% new-client pilot friction | DexCare, shared services | D7 |
| 20% invoice throughput | Luizalabs, SEFAZ async BullMQ | L2 |
| 18% support tickets | Luizalabs, fiscal dashboards | L3 |
| 26% more capacity | Lippaus, BullMQ jobs | P2 |

One number does not trace to a DOSSIER string:

- **`5+ years`** in the Summary. It is arithmetic on the LinkedIn ground
  truth: `Mar 2021` to today is 5 years 6 months. Derived, not fabricated. I
  report it because DOSSIER.md carries no such string.

### Unmarked qualifiers I could not trace to DOSSIER.md

These are not `[UNVERIFIED]`-marked and they are not in the dossier. Lucas
decides; I do not delete them and I do not defend them.

- **`nationwide retailer expansion`** — Lippaus mid-level bullet 1. DOSSIER
  confirms `multi-tenant web and mobile platform on PostgreSQL`. It says
  nothing about nationwide scope or expansion.
- **`high-volume`** in `Processed high-volume orders, notifications, and
  integrations` — Lippaus mid-level bullet 2. DOSSIER confirms the BullMQ jobs
  and the 26% figure, not the volume qualifier.
- **`Magazine Luiza's e-commerce operation`** — Luizalabs bullet 1. DOSSIER
  confirms the fiscal / NF-e / SEFAZ domain at Magazine Luiza. The
  `e-commerce operation` framing came from the retired Rails resume, which
  DOSSIER marks untrusted.
- **`real-time`** in `delivered real-time visit booking` — DexCare bullet 1.
  DOSSIER confirms `event-driven booking, healthcare scheduling at scale` and
  the `visit-booking` service. It does not state a real-time property.
- **`nationwide`, `high-volume`, `real-time`** are the qualifier class flagged
  before: an unverified qualifier is a claim, not decoration.

### Not observable

- Whether CI&T's `jobs.lever.co` destination runs a strict parsing ATS. No
  public source names Lever's parsing engine (ATS-KNOWLEDGE.md section 2:
  `Workday, Lever, Ashby — Not observable`). I did not open the apply link. If
  Lucas learns it is strict, `reports/macro-bakeoff.md` shape A is the
  recorded fallback for the role header.
- Contract type, workplace type, work authorization, years, English
  requirement and degree requirement: the post states none of them.

## Fix list for the Architect

none
