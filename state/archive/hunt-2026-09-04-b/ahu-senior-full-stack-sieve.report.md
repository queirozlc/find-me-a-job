# ATS Analysis — resumes/hunts/2026-09-04-b/ahu-senior-full-stack/Lucas-Queiroz-Resume-en.pdf vs ahu-senior-full-stack
Segment: not stated in `jobs/ahu-senior-full-stack.md`. Company origin recorded there as not observable. Not inferred.   Date: 2026-09-04

Analyzer: Sieve, ATS Analyzer. Graded against `RUBRIC.md` v2 and `ATS-KNOWLEDGE.md`.
These numbers are this team's rubric. No vendor produces them.

## Extraction

```
pdftotext -layout Lucas-Queiroz-Resume-en.pdf  -> layout.txt   (64 lines)
pdftotext         Lucas-Queiroz-Resume-en.pdf  -> raw.txt      (65 lines)
```

Gate 0 and Gate 2 judged on the raw file. `pdfinfo`: 1 page, letter, PDF 1.5.
`pdfimages -list`: no images. `pdffonts`: 4 embedded subset fonts, all with
Unicode maps.

## Verdict

**BLOCKED at Gate 1 and Gate 2.** Gate 0 also carries one FAIL.

- Gate 0: FAIL (0.5 employment-block segmentation).
- Gate 1: FAIL (required-skill presence). Other knockouts PASS or not stated.
- Gate 2: 52/100, **FAIL**. Six required tokens score 0 placement points.
- Gate 3: 70/100.

## Profile Check — LinkedIn verification

Read from the live profile through the `Profile Check` portal on 2026-09-04.
URLs read:
`https://www.linkedin.com/in/queiroz-lucas/details/experience/` and
`https://www.linkedin.com/in/queiroz-lucas/details/education/`.
Nothing on the profile was changed.

| CV prints | LinkedIn shows | Result |
|---|---|---|
| `DexCare` / `Senior Software Engineer` / `Mar 2026 - Present` | `Senior Software Engineer`, `DexCare · Full-time`, `Mar 2026 - Present · 7 mos` | match |
| `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Mar 2026` | `Mid-level Software Engineer`, `Luizalabs · Full-time`, `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | match |
| `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | `Lippaus Distribuidora`, `Mid-level Software Engineer`, `Jan 2023 - Jan 2024 · 1 yr 1 mo` | match |
| `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | `Lippaus Distribuidora`, `Entry-level Fullstack Software Engineer`, `Mar 2021 - Jan 2023 · 1 yr 11 mos` | match |
| `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | match |

Every employer, title, start month and end month is identical to LinkedIn.
Separator glyph is the ASCII hyphen on the CV where LinkedIn renders an EN
DASH. That follows `CLAUDE.md` rule 1 as clarified on 2026-09-01 and
`CV-SPEC.md` item 5. Not a defect.

Role locations: CV prints `Remote` for DexCare and Luizalabs, and
`Vitória, ES, Brazil` for both Lippaus roles. This follows `CLAUDE.md` section 3.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 65 raw lines extracted, all content recoverable |
| 0.2 | Glyph integrity | PASS | `office` 2 hits (`back-office`), `workflow` 5 hits. No U+FB01/FB02/FB00 codepoints. No NUL. Only non-ASCII bytes present are U+2022 bullet, U+000C form feed, `ó` |
| 0.3 | Contact block recoverable | PASS | Raw line 3: `Vitória, ES, Brazil | +55 (27) 99203-0170 | sepulchrolucas@gmail.com | linkedin.com/in/queiroz-lucas | github.com/queirozlc`. In the body, `\pagestyle{empty}`, no header or footer |
| 0.4 | Section headers verbatim | PASS | Standalone raw lines `SUMMARY`, `SKILLS`, `LANGUAGE`, `EXPERIENCE`, `EDUCATION`. Source strings are the canonical mixed case; `\scshape` changes only the render. Case-insensitive match allowed by the rubric |
| 0.5 | **Employment-block segmentation** | **FAIL** | See below |
| 0.6 | Date parseability | PASS | All five blocks carry `Mon YYYY - Mon YYYY` with an ASCII hyphen on the line following the title. Adjacency defect for DexCare is charged to 0.5, not double-counted here |
| 0.7 | Reading order | PASS | Raw and layout agree on the order of every adjacent block |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` empty. Source uses `itemize` only, no `tabular`, no text box, no icon, no photo |

### 0.5 FAIL, exact evidence

The raw stream carries exactly one blank line inside the `Experience` section,
and it falls **inside** the DexCare role header, between the title and its
dates:

```
[EXPERIENCE]
[DexCare]
[Senior Software Engineer]
[]                                  <- blank line splits the header
[Remote | Mar 2026 - Present]
[• Built event-driven TypeScript services on Express and Koa ...]
```

No blank line separates any two roles. The DexCare block ends and Luizalabs
starts with no break at all:

```
[environments with shared service instances and isolated configuration, secrets, and data stores.]
[Luizalabs]
[Mid-level Software Engineer]
[Remote | Jan 2024 - Mar 2026]
```

Measured line geometry from `pdftotext -bbox-layout`:

| Gap | Points |
|---|---|
| Bullet to bullet inside a role | 10.96 |
| Last bullet of a role to the next company name | 13.95 |
| DexCare title to its date line | 9.91 |

The role boundary carries only 2.99 pt more vertical space than an ordinary
line break. The only paragraph break in the whole section falls in the middle
of the current role's header. The whitespace signal that a segmenter reads is
inverted: it marks a split where there is none, and marks nothing where the
real role boundaries are.

`CV-SPEC.md` item 2 requires: "Leave clear vertical space between the role
header and its first bullet. Leave clear vertical space between the last
bullet and the next role." Neither holds. `ATS-KNOWLEDGE.md` section 2 records
that employment-block segmentation was the only real failure mode across the
36-template Textkernel test, and `RUBRIC.md` names 0.5 the highest-value check
in the rubric. The current role is the one at risk.

The rest of Gate 0 is clean. The ligature fix from `CV-SPEC.md` item 1 works:
`fontspec` with `Ligatures=NoCommon` is present in the source and `workflow`
and `back-office` both extract intact, which the four legacy PDFs failed.

## Gate 1 — Knockouts

Requirements taken verbatim from the `Required:` block of the posting text in
`jobs/ahu-senior-full-stack.md`. Nothing inferred.

| Check | Posting text | Result |
|---|---|---|
| Work authorization / entity type | silent | not stated |
| Location or time-zone overlap | `📍 Location: Open for Qualified Candidates (Local)`, title wording `LATAM` | **not stated** — see below |
| Minimum years of experience | `Experience: 5+ years of professional software development experience.` | PASS |
| English proficiency | `Language Proficiency: Minimum B1/B2 English proficiency (strong written & verbal communication).` | PASS |
| Each required skill present verbatim | `React.js, Next.js, JavaScript, TypeScript, HTML, and CSS`; `Node.js (Node 18) and/or .NET Core`; `PostgreSQL`, `AWS`; `RESTful APIs, JWT authentication, design patterns, and front-end pipelines` | **FAIL** |
| Degree requirement | silent | not stated |

### Years of experience, PASS

Earliest LinkedIn start is `Mar 2021` (Lippaus Distribuidora, Entry-level
Fullstack Software Engineer). Continuous to `Present` as of 2026-09-04. That is
5 years 6 months. The posting asks 5+. The CV Summary prints `5+ years`, which
matches the LinkedIn range and is not a rounded-up claim.

### English proficiency, PASS

The `Language` section prints `Portuguese: Native | English: Fluent (C1)`.
C1 clears a B1/B2 minimum. Source: `DOSSIER.md` Identity, resolved 2026-09-04.

### Location, not stated

The posting says `Open for Qualified Candidates (Local)`. It never defines what
`Local` bounds. The posting title wording says `LATAM`, which would include
Brazil, but the post body never repeats it as an eligibility rule and never
names a country, city, or radius. The two wordings are not reconciled anywhere
in the posting text.

**The boundary of `Local` is not observable.** I do not infer one. This is not
a resume defect and the Architect cannot fix it. It is a question for the
recruiter, and per `CLAUDE.md` section 7 only Lucas contacts them.

The CV prints `Vitória, ES, Brazil` in the contact block, so whatever boundary
the recruiter applies, the reviewer can apply it without guessing.

### Required-skill presence, FAIL

Six tokens from the posting's own `Required:` block are absent from the resume
entirely:

`Next.js`, `HTML`, `CSS`, `Node 18`, `design patterns`, `front-end pipelines`.

Confirmed by case-insensitive fixed-string search of the raw extraction:
0 hits each. `.NET Core` is also absent, but the posting writes
`Node.js (Node 18) and/or .NET Core`, so the Node.js path satisfies that
clause and .NET Core is not charged as a miss.

`RUBRIC.md` Gate 1: "For every explicit posting requirement, absent resume
evidence is a FAIL. Do not infer evidence from an unrelated title, employer, or
location." I add nothing on their behalf. `DOSSIER.md` records no Next.js, no
HTML, no CSS, no Node version, no design-patterns claim, and no front-end
pipeline claim. The Architect was correct not to write them.

## Gate 2 — Retrieval coverage: 52/100, **FAIL**

Tokens classified by the posting's own words. The `Required:` heading gives the
required set. The `Bonus Points / A Plus:` heading gives the preferred set.
Tokens that appear only under `Key Responsibilities` (Babel, Webpack, NPM, Git,
SVN, debugging, Agile, Waterfall) are duties, not stated requirements, so they
are not scored. They are listed under Match limits.

Placement scale: 0 absent, 1 Skills only, 2 Experience only, 3 both.

### Required tokens, weight 3

| Token | Skills | Experience bullet | Pts |
|---|---|---|---|
| `React.js` | `Frontend: React.js` | DexCare: "monitoring React.js with Datadog RUM" | 3 |
| `Next.js` | absent | absent | **0** |
| `JavaScript` | `Languages` | Lippaus Entry-level: "Developed internal back-office dashboards in JavaScript" | 3 |
| `TypeScript` | `Languages` | DexCare: "Built event-driven TypeScript services on Express and Koa" | 3 |
| `HTML` | absent | absent | **0** |
| `CSS` | absent | absent | **0** |
| `Node.js` | `Languages` | Luizalabs: "Built distributed tax microservices in Node.js, Java, and Go" | 3 |
| `Node 18` | absent | absent | **0** |
| `PostgreSQL` | `Data` | DexCare: "Modeled booking reads and writes in PostgreSQL with Sequelize and Drizzle ORM"; Lippaus Mid-level: "multi-tenant web and mobile platform on PostgreSQL" | 3 |
| `AWS` | `Cloud and operations` | DexCare: "wired to S3 and RDS through AWS SDK v3" | 3 |
| `RESTful APIs` | `Backend` | DexCare: "Built multi-tenant RESTful APIs with JWT authentication..." | 3 |
| `JWT authentication` | `Backend` | DexCare: "with JWT authentication through the third-party auth provider Auth0" | 3 |
| `design patterns` | absent | absent | **0** |
| `front-end pipelines` | absent | absent | **0** |

Required subtotal: 24 points of a possible 42.

### Preferred tokens, weight 1

| Token | Skills | Experience bullet | Pts |
|---|---|---|---|
| `Unit testing` | absent as that string. `Vitest`, `Jest` are present but are not the posting token | Luizalabs bullet names `Vitest and Jest suites`, again not the posting token | 0 |
| `MoQ` | absent | absent | 0 |
| `NUnit` | absent | absent | 0 |
| `third-party auth providers` | absent | DexCare: "through the third-party auth provider Auth0". Singular, the posting writes the plural | 2 |
| `complex web architectures` | absent | absent | 0 |

Preferred subtotal: 2 points of a possible 15.

### Score

```
coverage = 100 * (24*3 + 2*1) / (3*3*14 + 3*1*5)
         = 100 * (72 + 2) / (126 + 15)
         = 100 * 74 / 141
         = 52.48  ->  52
```

Stuffing penalty: 0. Highest repeat count in the raw text is 3
(`React`/`React.js`, `TypeScript`, `Node.js`, `PostgreSQL`, `AWS`, `Go`,
`BullMQ`, `multi-tenant`). Nothing reaches 4. The `CV-SPEC.md` cap of 3 holds.

**Gate 2 score: 52/100. FAIL.**

Required tokens without both Skills and Experience placement:
`Next.js`, `HTML`, `CSS`, `Node 18`, `design patterns`, `front-end pipelines`.

**These six cannot be fixed by writing.** `DOSSIER.md` is the only claim source
and it records none of them. Adding them would invent a credential, which
`CLAUDE.md` section 4 forbids. The gate stays FAIL until Lucas confirms a fact
that supports a token, at which point the fact goes into `DOSSIER.md` first.
This is a match ceiling on the posting, not a defect in the Architect's work.

## Gate 3 — Human scan: 70/100

| # | Check | Pts | Note |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 0 / 15 | The posting's title is `Senior Full Stack Developer`. `Full Stack Developer` appears nowhere in the resume, 0 hits. `Senior Software Engineer` does appear at raw line 6, inside the top 15%. `CLAUDE.md` rule 1 and `DOSSIER.md` lock the CV title to `Senior Software Engineer`. **Do not fix this.** Recorded as a scan cost the title rule accepts |
| 3.2 | 3 most relevant bullets in the first 3 of the most recent role | 10 / 20 | DexCare bullets 1 and 3 are on-posting: TypeScript on Express and Koa; RESTful APIs with JWT authentication. Bullet 2 is Epic EMR domain work, not a posting token. The two remaining high-value bullets sit lower: PostgreSQL at position 4, React.js at position 5. Two of three, half credit |
| 3.3 | Past-tense action verb and an outcome, no duty lists | 12 / 15 | All 16 bullets open with a past-tense verb, subject omitted: Built, Integrated, Modeled, Reduced, Helped, Moved, Deployed, Processed, Led, Developed. No present tense, no "Responsible for", no third person. Two bullets carry no outcome clause, so they are not full XYZ: DexCare bullet 4 ("Modeled booking reads and writes in PostgreSQL ... wired to S3 and RDS through AWS SDK v3") and Lippaus Entry-level bullet 2 ("Built customer-facing features end to end by balancing business requirements with technical constraints") |
| 3.4 | At least 3 bullets carry a real number | 15 / 15 | Seven do: 15%, 25%, 7%, 33%, 20%, 18%, 26%. All trace to the metrics Lucas supplied on 2026-09-01 in `DOSSIER.md` |
| 3.5 | Experience completeness | 10 / 10 | `base-en.tex` carries 16 bullets, the tailored file carries 16. Diff shows two rewordings and zero deletions: `REST APIs` to `RESTful APIs` plus `JWT authentication` phrasing in DexCare bullet 3, and `React` to `React.js` in DexCare bullet 5. No role, bullet, or metric removed. One page |
| 3.6 | No unsupported buzzwords | 10 / 10 | No "team player", "results-driven", "passionate", or equivalent |
| 3.7 | Skills grouped by category | 10 / 10 | Six labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing and AI tooling |
| 3.8 | Scannable | 3 / 5 | Single column, bold company, italic title, consistent bullet glyph. Marked down for the spacing defect measured in Gate 0.5: a 13.95 pt role boundary against a 10.96 pt line gap gives a reader almost no visual break between employers, and the `Frontend:` group holds a single token |

## Defects, ranked by cost

1. **Employment-block segmentation, Gate 0.5, blocking.** The single blank line
   in `Experience` falls between `Senior Software Engineer` and
   `Remote | Mar 2026 - Present`, splitting the current role's header, while no
   blank line separates any two roles. Measured: role boundary 13.95 pt,
   intra-role line gap 10.96 pt, DexCare title-to-date gap 9.91 pt. Fix in
   `\resumeSubheading` and `\resumeRoleGap`: remove whatever produces the break
   inside the DexCare header, and raise the between-role space so the boundary
   gap is clearly larger than a line gap. Re-extract and confirm the raw stream
   shows a blank line before each of `DexCare`, `Luizalabs`, and both
   `Lippaus Distribuidora` lines, and none inside any header.

2. **Six required tokens absent, Gate 1 and Gate 2, blocking, not writable.**
   `Next.js`, `HTML`, `CSS`, `Node 18`, `design patterns`,
   `front-end pipelines`. No `DOSSIER.md` support. Do not add them. Escalate to
   Lucas: if he confirms any as fact, the fact enters `DOSSIER.md` first, then
   the Architect places the token in `Skills` and in one Experience bullet.

3. **Two bullets are not full XYZ, Gate 3.3.** DexCare bullet 4 and Lippaus
   Entry-level bullet 2 name the technology and the action but no measured
   outcome. `CV-SPEC.md` Bullets requires "accomplished X, measured by Y, by
   doing Z". `DOSSIER.md` records D4 and P3 as "no number. Leave as is", so the
   fix is an outcome clause in words, not an invented number.

4. **Highest-value posting bullets sit below the fold of the current role,
   Gate 3.2.** The PostgreSQL bullet is 4th and the React.js bullet is 5th in
   DexCare. Reordering inside the role is allowed by `CLAUDE.md` section 9.1.
   No content change needed.

5. **Preferred token is singular against the posting's plural, Gate 2.** The CV
   reads `the third-party auth provider Auth0`; the posting reads
   `third-party auth providers`. Costs 1 placement point. Low value. Only worth
   changing if the sentence still reads truthfully, and Auth0 is the one
   provider `DOSSIER.md` records, so the singular is the honest form. Leaving
   it is defensible.

## Match limits

Preferred tokens not placed: `Unit testing`, `MoQ`, `NUnit`,
`complex web architectures`. `MoQ` and `NUnit` are .NET unit-test libraries and
the resume takes the Node.js path the posting allows, so they are out of reach
by design.

Responsibility-block tokens not placed and not scored: `Babel`, `Webpack`,
`NPM`, `Git`, `SVN`, `debugging`, `Agile`, `Waterfall`. None appears in the
posting's `Required:` block, and none has a `DOSSIER.md` claim source. Not
inferred, not charged.

Open question for Lucas, not a resume defect: the boundary of
`Open for Qualified Candidates (Local)` against the `LATAM` title wording is
not observable from the posting text.
