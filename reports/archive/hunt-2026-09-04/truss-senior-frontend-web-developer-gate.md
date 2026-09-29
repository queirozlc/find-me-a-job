# ATS Analysis — resumes/hunts/2026-09-04/truss-senior-frontend-web-developer/Lucas-Queiroz-Resume-en.pdf vs truss-senior-frontend-web-developer
Segment: not observable (jobs/truss-senior-frontend-web-developer.md records `Segment: not observable`)   Date: 2026-09-04

## Verdict
BLOCKED at Gate 1

Gate 0 passes all 8 checks. Gate 1 fails on required-skill presence: `Redux` /
`Redux Toolkit` and `React Router` are absent from the resume. Neither term is
established by `DOSSIER.md`, so the Architect cannot place them. This is a
candidate-fact gap, not a document defect. Gate 2 and Gate 3 are reported
below for completeness.

Extraction used for every judgement:
```
pdftotext -layout Lucas-Queiroz-Resume-en.pdf  (54 content lines)
pdftotext         Lucas-Queiroz-Resume-en.pdf  (54 content lines)
```
Gate 0 and Gate 2 judged on the raw file.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 54 lines of clean text from raw extraction. `Producer: xdvipdfmx (0.1)`, `Pages: 1` |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes, 0 `?` characters, 0 U+FB01/U+FB02 codepoints. `office` present 2x (`back-office`, raw lines 36, 47), `workflow(s)` present 5x. `fontspec` + `Ligatures=NoCommon` in the source is working |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. Source uses a `center` block inside `document` with `\pagestyle{empty}`, so no header or footer is involved |
| 0.4 | Section headers present verbatim | PASS | Standalone raw lines 5 `SUMMARY`, 10 `SKILLS`, 16 `EXPERIENCE`, 49 `EDUCATION`. Source strings are `Summary`, `Skills`, `Experience`, `Education`; uppercase is `\scshape` rendering only, allowed by 0.4 |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks in the raw stream, none merged, none split: lines 17-28 DexCare, 29-36 Luizalabs, 37-42 Lippaus Distribuidora (Mid-level), 43-47 Lippaus Distribuidora (Entry-level). The two Lippaus roles stay distinct, each with its own title and date line |
| 0.6 | Date parseability | PASS | Every role carries `Mon YYYY - Mon YYYY` with an ASCII hyphen inside its own 4-line header: `Mar 2026 - Present` (20), `Jan 2024 - Mar 2026` (32), `Jan 2023 - Jan 2024` (40), `Mar 2021 - Jan 2023` (46), `Feb 2022 - Dec 2025` (53). Observation, not a defect: the location line sits between the title and the date line (17 `DexCare`, 18 `Senior Software Engineer`, 19 `Remote`, 20 `Mar 2026 - Present`). `CV-SPEC.md` section 2 prescribes exactly this consecutive company/title/location/dates order, and no bullet or other role separates them, so date-to-role attribution stays unambiguous |
| 0.7 | Reading order | PASS | Raw and layout extraction agree line for line across all 54 lines. Only leading indentation differs |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` returns zero images. No table, text box, contact icon or photo. Fonts are 4 embedded subsets with Unicode maps: `Roboto-Bold`, `Roboto-Regular`, `Roboto-Italic`, `CMSY9` |

## Gate 1 — Knockouts

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | posting | not stated |
| Location or time-zone overlap | posting states `Format: full-time remote, with overlap 17:00/18:00-21:00/22:00 GMT+4` | Location PASS — the posting sets no mandatory location and the resume prints `Vitória, ES, Brazil` (raw line 3). Overlap: not observable. The resume cannot answer it, because `CLAUDE.md` section 3 forbids a UTC offset or overlap statement on the CV, and `DOSSIER.md` does not record Lucas's answer. Mechanical fact: GMT+4 17:00-22:00 equals GMT-3 10:00-15:00, inside a normal Brazilian business day. Route to screening answers |
| Minimum years of experience | posting requires `5+ years of professional frontend web development experience` | PASS with a note. The dated history spans Mar 2021 to Present, which is 5 years 6 months at 2026-09-04, and the Summary states `5+ years building production web applications` (raw line 6). Front-end evidence exists at both ends of that span: raw line 47 `back-office dashboards in JavaScript` from Mar 2021, and raw line 23 `reusable React components with CSS` in the current role. The resume never states 5+ years of *front-end* work specifically |
| English proficiency requirement | posting | not stated |
| Degree requirement | posting | not stated |
| Required skill: React | posting | PASS — raw lines 6, 12, 23 |
| Required skill: JavaScript | posting | PASS — raw lines 11, 36, 47 |
| Required skill: TypeScript | posting | PASS — raw lines 6, 11, 22 |
| Required skill: Redux / Redux Toolkit | posting | **FAIL** — 0 occurrences of `Redux` or `Redux Toolkit` in the raw text. Not established by `DOSSIER.md` |
| Required skill: React Router | posting | **FAIL** — 0 occurrences of `React Router` in the raw text. Not established by `DOSSIER.md` |
| Required skill: API-driven state management | posting | PASS with a note — `API-driven state` present in Skills (raw line 12) and in an Experience bullet (raw line 22). The word `management` is absent; the phrase `state management` has 0 occurrences |
| Required skill: styling, `MUI, Emotion, SASS/SCSS, or similar` | posting | PASS — this is an alternative set with an open member (`or similar`). `CSS` is present in Skills (raw line 12) and in an Experience bullet (raw line 23). None of `MUI`, `Emotion`, `SASS`, `SCSS` appears; none is established by `DOSSIER.md` |
| Required skill: testing, `Jest, React Testing Library, or similar` | posting | PASS — alternative set with an open member. `Jest` present in Skills (raw line 13) and in an Experience bullet (raw line 26). `React Testing Library` has 0 occurrences and is not established by `DOSSIER.md` |

**Gate 1 result: FAIL.** Two cumulative required skills are absent.

## Gate 2 — Retrieval coverage: 53/100, FAIL

Requirements taken from the posting's own `We're looking for:` list. Soft
phrasing discarded. `Ember` is background context in the role description, not
a listed requirement, so it is not scored. Alternative sets are scored once, on
their best-placed member, because the posting writes `or similar`.

| Token | Class | Weight | Placement | Points |
|---|---|---|---|---|
| React | required | 3 | Skills (raw 12) + Experience (raw 23) | 3 |
| JavaScript | required | 3 | Skills (raw 11) + Experience (raw 36, 47) | 3 |
| TypeScript | required | 3 | Skills (raw 11) + Experience (raw 22) | 3 |
| Redux / Redux Toolkit | required | 3 | absent entirely | 0 |
| React Router | required | 3 | absent entirely | 0 |
| API-driven state management | required | 3 | Skills (raw 12) + Experience (raw 22), as `API-driven state`; the word `management` absent | 3 |
| Styling: MUI \| Emotion \| SASS/SCSS \| or similar | required, alternative | 3 | satisfied by `CSS`: Skills (raw 12) + Experience (raw 23). Named members all absent | 3 |
| Testing: Jest \| React Testing Library \| or similar | required, alternative | 3 | satisfied by `Jest`: Skills (raw 13) + Experience (raw 26). `React Testing Library` absent | 3 |
| frontend | required | 3 | Skills only — the category label `Frontend:` on raw line 12. No Experience bullet carries the word. `front-end` has 0 occurrences | 1 |
| Storybook | preferred | 1 | absent entirely | 0 |
| GraphQL | preferred | 1 | absent entirely | 0 |
| Cypress | preferred | 1 | absent entirely | 0 |
| Playwright | preferred | 1 | absent entirely | 0 |
| billing | preferred | 1 | absent entirely | 0 |
| invoicing | preferred | 1 | Experience only (raw 33). Not in Skills | 2 |
| payments | preferred | 1 | absent entirely | 0 |

Arithmetic:
```
required   sum(points) = 3+3+3+0+0+3+3+3+1 = 19    numerator 3*19 = 57   denominator 3*3*9  = 81
preferred  sum(points) = 0+0+0+0+0+2+0     =  2    numerator 1* 2 =  2   denominator 3*1*7  = 21
coverage = 100 * (57 + 2) / (81 + 21) = 100 * 59 / 102 = 57.8 -> 58
stuffing penalty: -5
final = 53
```

Stuffing penalty detail: `workflow`/`workflows` appears 5 times, at raw lines
8, 14, 21, 28 and 47. That crosses the 4-occurrence threshold in RUBRIC Gate 2
Step 5. It is a human-reaction penalty, applied as written. No requirement
token reaches 4 occurrences: React 3, JavaScript 3, TypeScript 3, Jest 2,
CSS 2, `API-driven state` 2.

Required tokens without Skills and Experience placement:
`Redux / Redux Toolkit` (0), `React Router` (0), `frontend` (1, Skills only).

## Gate 3 — Human scan: 87/100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 8 / 15 | Top 15% of 54 content lines is lines 1-8. `Senior Software Engineer` sits at raw line 6, so the seniority anchor is in place. The posting's function words, `Front-End` and `frontend`, do not appear anywhere in lines 1-8. Half credit |
| 3.2 | The 3 most relevant bullets first, in the most recent role | 14 / 20 | DexCare bullets 1 and 2 are the front-end ones and they lead: raw 21-22 `web interfaces with API-driven state`, raw 23 `reusable React components with CSS`. The third slot goes to an EMR integration bullet (raw 24), which is back-end. The `Jest` testing bullet, a stated posting requirement, sits fifth at raw 26 |
| 3.3 | Past-tense action verb plus an outcome, every bullet | 15 / 15 | All 12 bullets lead with a past-tense verb, subject omitted: Delivered, Improved, Reduced, Reduced, Improved, Improved, Delivered, Improved, Cut, Supported, Increased, Supported. No present tense, no `Responsible for`, no third person. Every bullet carries an outcome in XYZ shape |
| 3.4 | At least 3 bullets carry a real number | 15 / 15 | Five numbers, all traceable to the `DOSSIER.md` metric list: 15% (D2, raw 24), 25% (D3, raw 25), 20% (L2, raw 35), 18% (L3, raw 36), 26% (P2, raw 42) |
| 3.5 | One page under 10 years experience | 10 / 10 | `pdfinfo` reports `Pages: 1` |
| 3.6 | No unsupported buzzwords | 10 / 10 | No `team player`, `results-driven`, or `passionate`. Every claim in the text carries a mechanism |
| 3.7 | Skills grouped by category | 10 / 10 | Four labelled groups: `Languages`, `Frontend`, `Testing`, `Backend and AI tooling` (raw 11-14). See defect 5 for the bare `testing` entry inside the Testing group |
| 3.8 | Scannable | 5 / 5 | Blank lines separate all four sections, role headers are consistent 4-line blocks, company names are bold and titles italic, spacing is even in the layout extraction |

## Defects, ranked by cost

1. **`Redux` and `Redux Toolkit` absent — Gate 1 knockout, Gate 2 required token at 0/3.**
   The posting states `experience with Redux/Redux Toolkit, React Router, and
   API-driven state management`. The `and` makes those three cumulative. Zero
   occurrences of `Redux` in the raw text.
   **This is not an Architect fix.** `DOSSIER.md` does not establish Redux for
   any role. Placing it would invent a fact, which `CLAUDE.md` section 4
   forbids. Fix path: ask Lucas whether he used Redux or Redux Toolkit in
   production, record the answer and the role in `DOSSIER.md` first, then the
   Architect places the exact posting token in `Skills` and in one relevant
   `Experience` bullet. If the answer is no, this application is a partial
   match and the gap stands.

2. **`React Router` absent — Gate 1 knockout, Gate 2 required token at 0/3.**
   Zero occurrences. Same fix path as defect 1, and the same prohibition: not
   established by `DOSSIER.md`, so the Architect must not add it.

3. **`frontend` reaches Skills only — Gate 2, 1/3.**
   Present once, as the category label `Frontend:` on raw line 12. No
   `Experience` bullet carries the word, and the hyphenated form `front-end`,
   which the posting uses in its own title, has zero occurrences.
   Exact fix, and it invents nothing: carry the posting's term into the
   DexCare front-end bullet. Change
   `Improved shared UI consistency across scheduling surfaces by developing reusable React components with CSS.`
   so the bullet names front-end work explicitly, keeping the same claim,
   the same metric position and the same XYZ shape.

4. **Posting title function words missing from the top 15% — Gate 3.1, 7 points lost.**
   Lines 1-8 carry `Senior Software Engineer` but never `Front-End` or
   `frontend`. The job title itself must not change: `CLAUDE.md` section 1
   binds it to LinkedIn, verified below. The Summary is free text and can carry
   the function word. Change
   `I am a Senior Software Engineer with 5+ years building production web applications with TypeScript, Node.js, React, and Go.`
   so the front-end focus appears in the first eight lines, without touching
   any job title.

5. **`workflow`/`workflows` repeated 5 times — Gate 2 stuffing penalty, 5 points.**
   Raw lines 8, 14, 21, 28, 47. `CV-SPEC.md` caps any term at 3 appearances.
   Exact fix: cut two of them. Raw line 21 `across healthcare scheduling
   workflows` and raw line 47 `Supported operational and administrative
   workflows` are the two where the word carries the least weight for this
   posting.

6. **`state management` absent as a phrase — Gate 2, retrieval risk on a required token.**
   The token scores 3 on the `API-driven state` head, but a recruiter boolean
   on `state management` returns nothing. Exact fix, and it invents nothing:
   in `Frontend: React | API-driven state | CSS` and in the bullet
   `building web interfaces with API-driven state backed by TypeScript services`,
   complete the phrase to the posting's own wording, `API-driven state management`.

7. **Bare `testing` token inside the Testing skills group — Gate 3, human reaction.**
   Raw line 13 reads `Testing: Jest | Vitest | testing`. The third entry
   repeats the group label and reads as filler to a human reviewer. Exact fix:
   drop the standalone `testing` entry from the group. It adds no retrieval
   value that the `Testing:` label and `Jest` do not already carry.

8. **`invoicing` reaches Experience only — Gate 2 preferred token, 2/3.**
   Present at raw line 33, absent from `Skills`. Non-blocking. This is the one
   preferred token the dossier supports, so placing it in `Skills` recovers the
   last available preferred point.

## Match limits

Preferred tokens not placed, none of them established by `DOSSIER.md`, so none
is an Architect defect: `Storybook`, `GraphQL`, `Cypress`, `Playwright`,
`billing`, `payments`.

Required-set members not placed, where the posting's `or similar` wording keeps
the requirement satisfied by another term: `MUI`, `Emotion`, `SASS`, `SCSS`
(covered by `CSS`), and `React Testing Library` (covered by `Jest`). None of
the five is established by `DOSSIER.md`. A recruiter running a literal boolean
on `MUI` or `SCSS` or `React Testing Library` will not retrieve this document.
That is a real retrieval limit and it is not fixable without a new candidate
fact.

Screening question, kept off the CV by `CLAUDE.md` section 3: the posting
requires overlap `17:00/18:00-21:00/22:00 GMT+4`, which is 10:00-15:00 in
Lucas's GMT-3. `DOSSIER.md` does not record whether Lucas accepts it. The apply
note must answer it; the resume must not.

## Identity verification

Read read-only from the live LinkedIn profile through the `Profile Check`
portal on 2026-09-04, at
`https://www.linkedin.com/in/queiroz-lucas/details/experience/` and
`https://www.linkedin.com/in/queiroz-lucas/details/education/`. No edit was
made. Old PDFs under `~/Documents/Resumes/` were not consulted.

| Field | LinkedIn, read live | Resume raw extraction | Result |
|---|---|---|---|
| Employer 1 | `DexCare · Full-time` | `DexCare` (17) | match |
| Title 1 | `Senior Software Engineer` | `Senior Software Engineer` (18) | match |
| Dates 1 | `Mar 2026 - Present · 7 mos` | `Mar 2026 - Present` (20) | match |
| Location 1 | `Seattle, Washington, United States · Remote` | `Remote` (19) | matches `CLAUDE.md` section 3, employer city never printed |
| Employer 2 | `Luizalabs · Full-time` | `Luizalabs` (29) | match, spelling included |
| Title 2 | `Mid-level Software Engineer` | `Mid-level Software Engineer` (30) | match |
| Dates 2 | `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | `Jan 2024 - Mar 2026` (32) | match |
| Location 2 | `São Paulo, Brazil · Remote` | `Remote` (31) | matches `CLAUDE.md` section 3 |
| Employer 3 | `Lippaus Distribuidora`, `Full-time · 2 yrs 11 mos` | `Lippaus Distribuidora` (37, 43) | match, both roles kept |
| Title 3a | `Mid-level Software Engineer` | `Mid-level Software Engineer` (38) | match |
| Dates 3a | `Jan 2023 - Jan 2024 · 1 yr 1 mo` | `Jan 2023 - Jan 2024` (40) | match |
| Title 3b | `Entry-level Fullstack Software Engineer` | `Entry-level Fullstack Software Engineer` (44) | match |
| Dates 3b | `Mar 2021 - Jan 2023 · 1 yr 11 mos` | `Mar 2021 - Jan 2023` (46) | match |
| Location 3 | `Vitória, Espírito Santo, Brazil · On-site` | `Vitória, ES, Brazil` (39, 45) | matches `CLAUDE.md` section 3 |
| School | `FAESA` | `FAESA` (50) | match |
| Degree | `Bachelor's degree , Information Systems` | `Bachelor's degree, Information Systems` (51) | match on substance; the resume drops the stray space before the comma, which `CV-SPEC.md` allows |
| Education dates | `Feb 2022 – Dec 2025` | `Feb 2022 - Dec 2025` (53) | match. The months are identical; the ASCII hyphen follows `CV-SPEC.md`, as `CLAUDE.md` section 1 clarifies |

Metrics checked against the `DOSSIER.md` bullet-metric list: 15% (D2), 25%
(D3), 20% (L2), 18% (L3), 26% (P2). All five match. No metric on the document
is unsourced.

Policy scans on the raw extraction:
- Forbidden stack tokens `ruby`, `rails`, `sidekiq`, `activerecord`,
  `activejob`, `rspec`, `devise`, `pundit`, `hotwire`: 0 occurrences. PASS.
- UTC offset, `GMT`, or time-zone overlap statement: 0 occurrences. PASS,
  per `CLAUDE.md` section 3.
- Language: English only, one file, matching the posting language recorded as
  `en`. PASS, per `CLAUDE.md` section 11.
