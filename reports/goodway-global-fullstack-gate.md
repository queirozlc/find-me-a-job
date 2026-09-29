# ATS Analysis — goodway-global-fullstack-en.pdf vs goodway-global-fullstack
Segment: us-direct   Date: 2026-09-02

Judged on extractions the analyzer regenerated from the PDF under test:
`pdftotext -layout` and `pdftotext` on `resumes/goodway-global-fullstack-en.pdf`.
Source cross-read: `resumes/goodway-global-fullstack-en.tex`.
Posting text: `jobs/goodway-global-fullstack.md` (LinkedIn 4462451164, captured
by Kestrel, hunt 2026-09-02-b).
Titles, companies and dates checked against `DOSSIER.md` **LinkedIn ground truth**.
Architect's own marker list read: `reports/goodway-global-fullstack-draft.md`.

This is our rubric. It is not a vendor score. No ATS emits these numbers.

## Verdict

**BLOCKED at Gate 1.**

| Gate | Result |
|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, reported not blocking) |
| Gate 1 — Knockouts | **FAIL** — English proficiency absent, time-zone overlap absent |
| Gate 2 — Retrieval coverage | **19 / 100** |
| Gate 3 — Human scan | **86 / 100** |

The document parses. It fails Gate 1 on the two LatAm-remote hard gates that
`RUBRIC.md` names explicitly: neither English proficiency nor time-zone
overlap appears anywhere in the document. One of the two is fixable from
`DOSSIER.md` today. The other is not, and it collides with `CLAUDE.md`
section 3. See the fix list.

---

## Gate 0 — Parse integrity

`pdfinfo` reports **1 page**. `pdfimages -list` returns **zero images**.
`pdffonts` shows four embedded subsets, all with ToUnicode maps
(`Roboto-Bold`, `Roboto-Regular`, `Roboto-Italic`, `CMSY9`).

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction is complete prose, 79 lines, every section present |
| 0.2 | Glyph integrity | PASS | Zero `\x00` bytes, zero `U+FFFD`, zero `U+FB00-FB04` ligature codepoints (byte-level count in Python, not a shell grep). `workflow` 4 hits, `office` 3 hits, `fiscal` 1 hit, `friction` 2 hits, `flags` 1 hit, `Auth0` 2 hits, all intact. The only non-ASCII characters in the whole extraction are `ó` and `•` |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, not a header or footer: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email, LinkedIn URL all present. No UTC offset printed, per `CLAUDE.md` section 3 |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 10, 18, 72: `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, each a standalone line. Uppercase rendering allowed by Gate 0.4. `\section` not `\section*`, per CV-SPEC item 4 |
| 0.5 | Employment-block segmentation | FAIL — header only | Raw splits each role header into `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remote`. **No two roles merge. No role splits into two employment entries.** Four Experience blocks and one Education block, all intact and correctly ordered. Cause is the `tabular*` at `goodway-global-fullstack-en.tex:39` |
| 0.6 | Date parseability | FAIL — header only | Every date sits one blank line below its title, not on it. Format is correct in all five blocks: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Separator is an **ASCII hyphen** in all five, verified by `repr()`, per CV-SPEC item 5 |
| 0.7 | Reading order | FAIL — header only | Whitespace-normalized `diff` of raw against layout returns **exactly 5 hunks, all five the role or education header**. Raw: company, title, dates, location. Layout: company+dates, title+location. **Zero content blocks reorder.** Bullet order is identical in both extractions |
| 0.8 | No forbidden constructs | FAIL — header only | The `tabular*` role header. No table elsewhere, no text box, no image of text, no icon, no photo. `pdfimages -list` is empty |

**All four FAILs trace only to the two-column role header.** That is the
accepted exception recorded in `CV-SPEC.md` item 2 and in `RUBRIC.md`
"Accepted exception, set by Lucas 2026-09-01". Reported, not blocking.
I looked for any other cause of 0.5-0.8 and found none.

**Gate 0 verdict: PASS.**

### LinkedIn ground-truth cross-check — PASS

Character for character against the `DOSSIER.md` LinkedIn block.

| Block | Resume text | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` | identical | YES |
| 3 | `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | identical | YES |
| 4 | `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | identical | YES |
| Education | `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — start and end months identical; ASCII hyphen per CV-SPEC item 5 and the `CLAUDE.md` 2026-09-01 clarification. The LinkedIn space before the comma is a source typo, not a period |

Company spelling `Luizalabs` is correct. Both Lippaus roles are present and
separate; the promotion is preserved. **No Gate 0 FAIL from this check.**

One location conflict, outside the title, company and date scope: see defect 8.

### Forbidden-token grep

```
grep -in 'ruby|rails|sidekiq|activerecord|activejob|rspec|devise|pundit|hotwire'
```
**Zero hits** in `goodway-global-fullstack-en.tex` and zero in both extraction
files.

```
grep -rn UNVERIFIED resumes/goodway-global-fullstack-en.tex
```
**Zero hits.** Independently confirmed. The Architect's draft report claims
"None" and that claim is correct. **No `[UNVERIFIED]` marker ships in this
package.**

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | "We are targeting individuals that live in Brazil, Colombia, and Mexico for this role. We are not currently accepting candidates from the United States." No work-authorization or entity-type requirement is stated. Contract type is not stated; LinkedIn shows `Full-time` | **not stated** |
| Location | Residency in Brazil, Colombia or Mexico, quoted above. `Location as shown: Brazil`, `Workplace type: Remote` | **PASS** — resume states `Vitória, ES, Brazil` on the contact line |
| Time-zone overlap | **Not stated in the posting.** The capture and the Maestro brief both record this | **FAIL** — the resume states no overlap anywhere. `RUBRIC.md` Gate 1: "Time-zone overlap and English fluency are standard hard gates in LatAm-remote postings. If the resume does not state them explicitly, that is a FAIL, not a neutral." This is a LatAm-remote posting. See defect 2 for the conflict this creates |
| Minimum years of experience | "4+ years of professional software engineering experience" | **PASS** — Mar 2021 to Sep 2026 = 5 yr 6 mo from the LinkedIn dates. Summary states `5+ years of professional software engineering experience`, the posting's own phrasing |
| English proficiency | **Not stated in the posting.** The posting is written in English and the interview is a live English-language coding session, but no proficiency level is required in the text | **FAIL** — the resume states no English level anywhere. Grep for `english`, `C1`, `fluen`, `advanced` returns zero hits in the raw extraction. Same rubric rule as above. `DOSSIER.md` carries the fact: "Advanced / C1. Daily English-only work with US teams at DexCare. [FACT, Lucas 2026-09-01]" |
| Degree requirement | Not stated in the posting | **not stated** — resume carries `Bachelor's degree, Information Systems`, FAESA |

Required-skill presence, verbatim in the raw extraction:

| Requirement (posting's words) | Present verbatim? |
|---|---|
| `React` | YES |
| `JavaScript/TypeScript` | YES — exact slashed pair in Skills |
| `Node.js` | YES |
| `REST APIs` | YES |
| `modern web applications` | Partial. `Web applications` YES, `modern` NO |
| `AWS` cloud services | YES |
| `Git` | **NO** — the only hit is the `github.com` URL, a substring, not the token |
| `CI/CD` practices | YES. `modern` NO |
| `software design` | **NO** |
| testing | YES — `Testing` in Skills, `tests` in a DexCare bullet, `Vitest`/`Jest` in a Luizalabs bullet |
| `debugging` | **NO** |
| `cross-functional` teams | **NO** |
| `remote environment` | Partial. `Remote` YES as two role locations. The phrase NO |
| data-driven applications or `dashboards` | `dashboards` YES. `data-driven` NO |
| `SQL` | YES |
| `data visualization` | **NO** |
| `Docker` or `Kubernetes` | YES, both |
| `Python` or data engineering workflows | **NO**, neither |
| `AI` or `automation` | `AI` YES. `automation` NO |

**Gate 1 verdict: FAIL.** The two stated gates the posting does impose,
residency and years, both pass. The failure is on the two rubric-mandated
LatAm-remote gates, and both come from what the document omits, not from
anything it claims. The absent required-skill tokens above are Gate 2 losses
and ranked defects, not knockouts.

---

## Gate 2 — Retrieval coverage: 19 / 100

### Scoring conventions used, stated so this is reproducible

Carried forward unchanged from `reports/charterup-senior-fullstack-gate0.md`,
plus one extension forced by this document.

1. Where the posting offers alternatives ("Docker **or** Kubernetes",
   "Python **or** data engineering workflows", "AI **or** automation",
   "data-driven applications **or** dashboards"), the group scores **once**,
   at its best-covered member. Scoring each alternative separately would
   double-penalize an OR.
2. The rubric ladder assumes a token can sit in `Skills`. For phrase tokens
   that cannot (`4+ years of professional software engineering experience`),
   and for skill tokens found in `Experience` but **not** in `Skills`, the
   ladder has no rung. I score those **2** and mark the row. This is my
   convention, not the rubric's text.
3. **Extension, new here.** `web applications` sits in `Skills` **and** in the
   `Summary` but in **no** `Experience` bullet. The rubric's rung 4 reads
   "**Also** in Summary or a job title", which chains to rung 3, and rung 3
   fails. I score it **2** and mark the row.
4. The Step 4 stuffing penalty is applied only to tokens in this table.
   Unsupported `Skills` tokens outside this table are reported as defect 7.
5. **The posting declares no preferred tier.** "What You Bring" is a single
   undivided block. `RUBRIC.md` Step 1 says to classify using the posting's
   own words, and the posting's own words draw no line. Every token below
   therefore carries **weight 3**. I did not invent a preferred tier to
   soften the denominator. The consequence is stated under "Ceiling" below.

### Tokens — weight 3, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| R1 | `4+ years of professional software engineering experience` | — | no | **yes** | 2 | Summary line 6, as `5+ years of professional software engineering experience`. Convention 2 |
| R2 | `React` | yes (L12) | yes (L32) | **yes** (L7) | 4 | Full ladder |
| R3 | `TypeScript` | yes (L11) | yes (L26) | **yes** (L7) | 4 | Full ladder |
| R4 | `JavaScript` | yes (L11) | yes (L60, L69) | no | 3 | Absent from the Summary |
| R5 | `Node.js` | yes (L11) | yes (L44) | **yes** (L7) | 4 | Full ladder |
| R6 | `REST APIs` | yes (L13) | yes (L28) | **yes** (L7) | 4 | Full ladder |
| R7 | `modern web applications` → `web applications` | yes (L12) | **no** | **yes** (L7) | 2 | Convention 3. No Experience bullet carries the token. `modern` absent |
| R8 | `AWS` cloud services | yes (L14) | yes (L31) | **yes** (L7, `AWS cloud services` verbatim) | 4 | Full ladder |
| R9 | `Git` | no | no | no | **0** | Absent. `github.com` on the contact line is a substring, not the token |
| R10 | `modern CI/CD practices` → `CI/CD` | yes (L14) | yes (L49) | no | 3 | `modern` absent |
| R11 | `software design` | no | no | no | **0** | Absent |
| R12 | testing | yes (L16, `Testing`) | yes (L34 `tests`, L50 `Vitest`/`Jest`) | no | 3 | The Skills label carries `Testing`; the bullet carries the inflection `tests` |
| R13 | `debugging` | no | no | no | **0** | Absent |
| R14 | `cross-functional` teams | no | no | no | **0** | Absent |
| R15 | `remote environment` → `Remote` | no | yes (L23, L42, role locations) | no | 2 | Convention 2. The phrase itself is absent |
| R16 | data-driven applications **or** `dashboards` (OR) | yes (L12, `Back-office dashboards`) | yes (L47, L69) | no | 3 | Scored at `dashboards`. `data-driven` absent everywhere |
| R17 | `SQL` | yes (L15) | yes (L30, `SQL-backed`) | no | 3 | Standalone `SQL` twice; `PostgreSQL` counted separately |
| R18 | `data visualization` | no | no | no | **0** | Absent. Maestro brief names it a gap |
| R19 | `Docker` **or** `Kubernetes` (OR) | yes (L14, both) | yes (L49, both) | no | 3 | Scored once at best member |
| R20 | `Python` **or** data engineering workflows (OR) | no | no | no | **0** | Both absent. Maestro brief names both as gaps |
| R21 | `AI` **or** `automation` (OR) | yes (L16) | yes (L33) | **yes** (L8) | 4 | Scored at `AI`. `automation` absent |

Points earned: **48**. Denominator: 21 tokens x 3 x 4 = **252**.

```
coverage = 100 * 48 / 252 = 19.05 -> 19
```

### Step 4 stuffing penalty: 0

No token in the table reaches 4 appearances. Whole-word counts, measured with
word-boundary regex and not substring grep: `React` 3, `TypeScript` 3,
`JavaScript` 3, `Node.js` 3, `AWS` 3, `REST APIs` 3, `PostgreSQL` 3,
`dashboards` 3, `AI` 3, `Go` 3, `Docker` 2, `Kubernetes` 2, `CI/CD` 2,
`SQL` standalone 2. The CV-SPEC 3-appearance cap holds exactly.

`web applications` (R7) sits in `Skills` with no Experience **token**, but it
does have Experience **evidence** in substance: "multi-tenant web and mobile
platform" (L58) and "back-office dashboards in JavaScript" (L69). Step 4 asks
for supporting evidence, not for the exact string. **No penalty applied.**
The lost point is already taken at R7.

### Missing tokens

Absent verbatim from the document:

1. `Git`
2. `software design`
3. `debugging`
4. `cross-functional`
5. `data visualization`
6. `Python`
7. `data engineering` / data engineering workflows
8. `automation`
9. `data-driven`
10. `modern` (as the qualifier on `web applications` and on `CI/CD practices`)
11. `scalable` / `scalability` — "scalable backend services" in "Who You Are",
    "balance scalability" in "What You Will Do"
12. `collaborate` / `collaboration`
13. `maintainable` — "reliable, maintainable" in "Who You Are"

### Ceiling, stated honestly

19 is not a build defect. Six of the 21 tokens (R9, R11, R13, R14, R18, R20)
score 0 because **`DOSSIER.md` records no fact behind them**. The Architect
was right to leave every one of them out; the draft report lists that
reasoning and it is sound. If those six stay at 0, the maximum this document
can reach is 180 of 252, or **71**. The distance from 19 to 71 is recoverable
work. The distance from 71 to 100 needs new facts from Lucas.

The undivided "What You Bring" block is what makes the denominator harsh:
`Python` and `data visualization` carry the same weight 3 as `React`. I did
not reweight them, because the posting states no preferred tier and
`RUBRIC.md` forbids guessing a requirement the posting did not state.

---

## Gate 3 — Human scan: 86 / 100

| # | Check | Points | Basis |
|---|---|---|---|
| 3.1 | Target title in the top 15% | **12** / 15 | Top 15% of a 79-line raw extraction is lines 1-12. Line 6 opens `I am a Senior Software Engineer` and line 6 also carries `full stack`. Docked 3: the posting's title is `Global Full Stack Software Engineer` and **the string `Full Stack Software Engineer` appears nowhere in the document**. `full stack` appears once, as an adjective on `systems`, not as a title |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | **12** / 20 | The three most posting-relevant DexCare bullets are b3 (`REST APIs`, `Auth0`, `OpenAPI/Swagger`, 25%), b4 (`SQL`, `PostgreSQL`, `AWS SDK v3`) and b5 (`React`, `Datadog`). They sit at positions **3, 4 and 5**. Positions 1 and 2 lead with healthcare scheduling and Epic EMR, which carry **no posting token at all**. Docked 8: **`React` is the posting's first-named technology and it appears exactly once in the whole Experience section, at DexCare bullet 5** |
| 3.3 | Voice rule (CV-SPEC, `CLAUDE.md` section 9) | **15** / 15 | All 15 bullets checked one by one. Openers: `Built`, `Integrated`, `Built`, `Built`, `Reduced`, `Built`, `Helped implement`, `Built`, `Improved`, `Reduced`, `Kept`, `Built`, `Increased`, `Delivered`, `Built`. **Every one is past tense, first person, subject omitted. No bullet starts with `I`. No present tense. No `Responsible for`. No third person.** Summary uses `I` three times: `I am`, `I build`, `I integrate`; present tense in the Summary is correct per CV-SPEC |
| 3.4 | At least 3 bullets carry a real, defensible number | **15** / 15 | Seven do: 15%, 25%, 7%, 33%, 20%, 18%, 26%. **All seven trace to the `DOSSIER.md` metric list**, IDs D2, D3, D5, D7, L2, L3, P2, each attached to the same method the dossier attaches it to |
| 3.5 | Length: 1 page under 10 years | **10** / 10 | `pdfinfo` reports `Pages: 1` |
| 3.6 | No unsupported buzzwords | **10** / 10 | No `team player`, `results-driven`, `passionate`, or anything comparable. `high-quality code` is a `DOSSIER.md` FACT phrase, not a buzzword |
| 3.7 | Skills grouped by category | **8** / 10 | Six labeled groups, all meaningful: Languages and runtimes, Frontend and applications, Backend and APIs, Cloud and delivery, Data, Testing and AI. Docked 2: **`Auth0` sits in `Testing and AI`** (`en.tex:71`). Auth0 is neither a testing tool nor an AI tool. A recruiter reading that line reads a category error |
| 3.8 | Scannable | **4** / 5 | One clean page, ruled headers, bold companies, role gaps per CV-SPEC item 2. Docked 1: wrapped bullets have no hanging indent, so ten continuation lines start flush under the bullet glyph, for example `TypeScript services on Express and Koa.` and `distribution startup.` |

Total: **86 / 100**.

Not a rubric line item, worth stating: **`Built` opens 7 of the 15 bullets,
and 4 of the 7 DexCare bullets.** See defect 9.

---

## Defects, ranked by cost

Defects 1 and 2 are the Gate 1 blockers. They come first because Gate 1
outranks everything below it.

| # | File and line | Defect | What would pass |
|---|---|---|---|
| **1** | `goodway-global-fullstack-en.tex:62` (Summary) | **English proficiency is stated nowhere in the document.** Zero hits for `english`, `C1`, `fluen`, `advanced` in the raw extraction. `RUBRIC.md` Gate 1 makes this a hard FAIL on a LatAm-remote posting, and this posting targets Brazil, Colombia and Mexico for a US and UK company, with a live English-language coding interview | **Fixable today, from the dossier.** `DOSSIER.md` Identity: "English proficiency: Advanced / C1. Daily English-only work with US teams at DexCare. [FACT, Lucas 2026-09-01]". Add one Summary clause carrying `Advanced English (C1)` and the daily-use evidence. It is a FACT, it needs no `[UNVERIFIED]` marker, and it clears the blocker outright |
| **2** | `goodway-global-fullstack-en.tex:62` (Summary) | **Time-zone overlap is stated nowhere.** Same rubric rule, same FAIL | **Not the Architect's to fix, and I do not recommend an edit.** Two of Lucas's own instructions collide here. `CLAUDE.md` section 3 says to state overlap in prose "when a posting gates on it" — **this posting does not gate on it**. And `DOSSIER.md` records no time-zone-overlap fact at all; the previous package's `US-hours overlap` claim was flagged as untraceable in `reports/charterup-senior-fullstack-gate0.md` fix 14. **Escalate to Lucas.** He either supplies the overlap as a fact and lifts the section 3 restriction for this posting, or he accepts the rubric FAIL as a rubric artifact and ships. I do not resolve it and I do not invent the fact |
| 3 | `en.tex:62` (Summary), `en.tex:67` (Skills) | **`Full Stack Software Engineer` appears nowhere.** The posting's title is `Global Full Stack Software Engineer`. Costs Gate 3.1 (-3) and weakens every title-similarity signal a recruiter search leans on | `full stack` is already in the Summary as an adjective. Recasting the Summary opener so the phrase reads as a title, without touching the LinkedIn-bound role titles in the Experience blocks, places it. The Experience titles must not change: they are LinkedIn ground truth |
| 4 | `en.tex:75-87` (DexCare block) | **`React` appears once in the whole Experience section, at bullet 5.** It is the posting's first-named technology, in both "What You Will Do" and "What You Bring". Costs Gate 3.2 (-8) and holds R2 at its current placement | Move the React evidence higher in the DexCare block, or add React to the SQL-backed or REST APIs bullet where `DOSSIER.md` already records React as DexCare stack (FACT-OBSERVED). Reordering costs nothing at Gate 2 and recovers Gate 3.2 points |
| 5 | `en.tex:64-71` (Skills), Summary | **Six required tokens are absent and none can be added from `DOSSIER.md`:** `Git`, `software design`, `debugging`, `cross-functional`, `data visualization`, `Python` / data engineering workflows. Together they cap Gate 2 at 71 | **Escalate to Lucas, one question each.** `Git` is the cheapest and most likely: every repo in `~/dexcare` is a git repo, but `DOSSIER.md` does not record it and I do not promote an inference to a fact. `cross-functional` is the second cheapest: the dossier confirms "project scoping and stakeholder communication" at Lippaus but does not name the functions. `Python`, `data visualization` and data engineering are named gaps in the Maestro brief; do not add them on inference. Worth up to 52 Gate 2 points if Lucas confirms all six |
| 6 | `en.tex:67`, `en.tex:62` | **`web applications` sits in `Skills` and `Summary` but in no Experience bullet.** Held R7 at 2 of 4 | The Lippaus mid-level bullet (`en.tex:102`) already says "multi-tenant web and mobile platform". Changing `platform` to `web application` places the token with **no new claim**, since the dossier FACT is "multi-tenant web and mobile platform". Worth +2 raw Gate 2 points |
| 7 | `en.tex:68` and `:71` | **Three `Skills` tokens have no supporting evidence anywhere in `Experience`:** `RabbitMQ`, `AMQP`, `Agentic workflows`. `RUBRIC.md` Gate 2 Step 4 names this a real human-reaction penalty | **Not a fabrication and not an Architect error.** All three are `DOSSIER.md` FACTs, and Lucas explicitly directed RabbitMQ and AMQP to be "Skills token only, no service names on the CV". Reported so Lucas knows the cost. His instruction stands unless he changes it. No penalty applied at Gate 2, because none of the three is a token this posting asks for |
| 8 | `en.tex:100` and `:109` | **Both Lippaus roles print `Vitória, ES, Brazil` as the role location.** `DOSSIER.md` states: "Role locations print `Remote` only. Seattle and São Paulo are employer cities; Lucas worked every role remotely. **No employer city on the CV.** [FACT, Lucas 2026-09-01]". LinkedIn separately records Lippaus as `On-site`, Vitória, Espírito Santo, Brazil | **Escalate to Lucas.** This is the same conflict `reports/charterup-senior-fullstack-gate0.md` fix 13 raised, now resolved the other way: that package printed `Remote` for Lippaus and was flagged against LinkedIn; this one prints the city and is flagged against the dossier rule. Lucas's two instructions disagree and only he settles it. It is outside the title, company and date scope, so it is **not** a Gate 0 FAIL |
| 9 | `en.tex:76, 78, 79, 81` and `:90, 102, 111` | **Verb monotony.** `Built` opens 7 of 15 bullets and 4 of the 7 DexCare bullets. Reads as one template applied seven times, and it blunts the strongest section of the document | Vary the openers on two or three of them. The outcomes, numbers and tokens stay identical. Not a rubric line item; it costs on the human scan |
| 10 | `en.tex:71` | `Auth0` sits in the `Testing and AI` Skills group. Gate 3.7, -2 | Move `Auth0` to `Backend and APIs` or `Cloud and delivery`. Zero Gate 2 cost, the token stays in `Skills` |
| 11 | `en.tex:76-86` and elsewhere | Ten wrapped bullet continuation lines have no hanging indent. Gate 3.8, -1 | A hanging-indent macro on `\resumeItem`. Verify the result **in the extraction**, not in the source; a source macro that looks right can still extract wrong |
| 12 | `en.tex:102` | "supported nationwide retailer expansion" is not in `DOSSIER.md` | Confirm with Lucas or remove. Carries no posting token, so removal costs nothing at Gate 2. See "Claims I could not verify" |
| 13 | `en.tex:111` | "for a beverage distribution startup" is not in `DOSSIER.md` | Same. Lippaus's industry and stage are recorded nowhere |
| 14 | `en.tex:95` | "gating CI/CD with Vitest and Jest" — the dossier confirms Vitest and Jest as **tools used** at Luizalabs and Lippaus. It does not record that they gated a CI/CD pipeline | Confirm with Lucas. **Do not remove blindly:** `CI/CD` is required token R10 and this bullet is its only Experience placement |

---

## Claims I could not verify

Listed for Lucas. Not deleted, not defended.

1. **"supported nationwide retailer expansion"** — `en.tex:102`. `DOSSIER.md`
   confirms the multi-tenant web and mobile platform on PostgreSQL at Lippaus.
   It records no national rollout.
2. **"for a beverage distribution startup"** — `en.tex:111`. Lippaus's
   industry and company stage are recorded nowhere in the dossier.
3. **"gating CI/CD with Vitest and Jest"** — `en.tex:95`. Tools confirmed,
   the CI/CD gating role is not.
4. **"Kept production deployments reliable"** — `en.tex:95`. Docker,
   Kubernetes, GCP and ArgoCD are confirmed tools at Luizalabs. The
   reliability outcome is not recorded and carries no number.
5. **"real-time booking and provider availability"** — `en.tex:76`. The
   dossier records event-driven booking, healthcare scheduling at scale, and
   a `forq-availability` service. **`real-time` is not recorded.**
6. **"isolated tenant data, enforced API contracts"** — `en.tex:79`. The
   dossier records multi-tenant JWT (SCH-343), Auth0, and OpenAPI/Swagger
   validators. These two outcome clauses are consistent with that, but
   neither is recorded as an outcome.
7. **"Magazine Luiza's e-commerce operation"** — `en.tex:90`. The dossier
   records the Luizalabs domain as fiscal / NF-e / SEFAZ for Magazine Luiza.
   It does not describe the operation as e-commerce.
8. **Lippaus location `Vitória, ES, Brazil`** — `en.tex:100`, `:109`.
   Contradicts the dossier FACT "Role locations print `Remote` only. No
   employer city on the CV." See defect 8.
9. **`5+ years`** — `en.tex:62`. Not a stated dossier number. It is arithmetic
   on the LinkedIn ground-truth dates, Mar 2021 to Sep 2026 = 5 yr 6 mo.
   Defensible, and correct against the posting's `4+ years`. Listed only so
   the derivation is on the record.

Verified and needing no action: every title, company and date against the
LinkedIn block; all seven percentages against the dossier metric list (D2, D3,
D5, D7, L2, L3, P2); the SPI description and its 33%, including the
instruction not to print internal customer names, which is obeyed; every
DexCare stack token (FACT-OBSERVED from the repos); `Go` and `Java` at
Luizalabs; BullMQ, Docker, Kubernetes, GCP, ArgoCD, Vitest and Jest as tools
used; Claude Code, Codex and agentic workflows; the Information Systems degree
at FAESA; `Vitória, ES, Brazil` on the contact line with no UTC offset;
zero Ruby or Rails tokens; zero `[UNVERIFIED]` markers.

---

## Analyzer's read, in one paragraph

Mechanically this is the cleanest tailored document this team has produced.
It parses, the employment blocks segment correctly apart from the accepted
header exception, every title and date matches LinkedIn character for
character, the voice rule holds on all 15 bullets with no exception, all seven
numbers trace to the dossier, no Ruby or Rails token appears, and no
`[UNVERIFIED]` marker ships. It still blocks, and it blocks on an omission:
the document never says Lucas speaks English, on a posting that hires across
Brazil, Colombia and Mexico and interviews live in English. That fix is one
sentence and the fact is already in the dossier. The time-zone FAIL beside it
is a genuine collision between the rubric and `CLAUDE.md` section 3, and it is
Lucas's to settle, not the Architect's. Gate 2 at 19 is honest distance, not
sloppiness: six of the 21 required tokens need facts that do not exist yet,
and the posting's undivided requirement block gives `Python` the same weight
as `React`. Fixes 3, 4, 6 and 10 are free and recover real points. Fix 5 is a
short list of questions for Lucas, and his answers decide whether this
application is worth sending.

---

## Fix list for the Architect

Blocking only. Gate 0 is PASS under the accepted `tabular*` exception, so
nothing from Gate 0 appears here. Both items below are Gate 1 FAILs.

1. **`resumes/goodway-global-fullstack-en.tex:62`, Summary.** Add an English
   proficiency statement. Source it verbatim from `DOSSIER.md` Identity:
   "Advanced / C1. Daily English-only work with US teams at DexCare. [FACT,
   Lucas 2026-09-01]". The token `English` and the level `C1` must both reach
   the raw extraction. Rebuild with tectonic, then confirm with
   `pdftotext goodway-global-fullstack-en.pdf - | grep -i 'english\|C1'`.
   Keep the document to one page. This clears the Gate 1 English FAIL.
2. **`resumes/goodway-global-fullstack-en.tex:62`, Summary — do not edit yet.**
   The time-zone overlap FAIL cannot be fixed from `DOSSIER.md`: no
   overlap fact is recorded there, and `CLAUDE.md` section 3 restricts
   printing overlap to postings that gate on it, which this posting does not.
   **Ask Maestro to put it to Lucas.** If Lucas supplies an overlap fact and
   authorizes printing it, add one prose clause stating the overlap, never a
   UTC offset, and rebuild. If he declines, this FAIL stands as a rubric
   artifact and he ships knowing it. Do not invent the fact and do not print
   an offset.
