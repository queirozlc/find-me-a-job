# ATS Analysis — charterup-senior-fullstack-en.pdf / -pt.pdf vs charterup-senior-fullstack
Segment: us-direct   Date: 2026-09-01

Judged on the raw extractions regenerated 2026-09-01 by the analyzer:
`resumes/charterup-senior-fullstack-{en,pt}.raw.txt` and `.layout.txt`.
Posting text: `jobs/charterup-senior-fullstack.md`.
Titles, companies and dates checked against `DOSSIER.md` **LinkedIn ground truth**.

This is our rubric. It is not a vendor score. No ATS emits these numbers.

## Verdict

| Gate | EN | PT |
|---|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, reported not blocking) | **PASS** (same 4) |
| Gate 1 — Knockouts | **PASS with defects** (no hard knockout; 2 required tokens absent) | same |
| Gate 2 — Retrieval coverage | **19 / 100** | **16 / 100** |
| Gate 3 — Human scan | **92 / 100** | **92 / 100** |

Not blocked. The document parses. The problem is Gate 2, and it is severe.

---

## Gate 0 — Parse integrity

Both PDFs confirmed **1 page** (`pdfinfo`). `pdfimages -list` returns zero
images in both. Fonts are embedded subsets with ToUnicode maps.

| # | Check | EN | PT | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | PASS | Raw extraction is complete prose, 54 lines EN / 53 PT |
| 0.2 | Glyph integrity | PASS | PASS | `grep -c workflow` EN = 2, PT = 1. `back-office` EN = 3, `backoffice` PT = 3. Zero `U+FB00-FB06`, zero `\x00` in either raw file |
| 0.3 | Contact block recoverable | PASS | PASS | Line 3 of raw, in the body: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email, LinkedIn all present |
| 0.4 | Section headers verbatim | PASS | PASS | EN raw: `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`. PT raw: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`. Uppercase rendering allowed by Gate 0.4 |
| 0.5 | Employment-block segmentation | FAIL — header only | FAIL — header only | Raw splits each role header into 4 lines: `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remote`. **No two roles merge. No role splits into two employment entries.** Cause is the `tabular*` at `en.tex:41` |
| 0.6 | Date parseability | FAIL — header only | FAIL — header only | Dates are one blank line below the title, not on it: `Senior Software Engineer` … `Jan 2026 - Present`. Format `Mon YYYY - Mon YYYY` with ASCII hyphen is correct in all five blocks |
| 0.7 | Reading order | FAIL — header only | FAIL — header only | `diff` of raw vs layout returns 5 hunks, **all five are the role/education header**. Raw: company, title, dates, location. Layout: company+dates, title+location. Zero content blocks reorder |
| 0.8 | No forbidden constructs | FAIL — header only | FAIL — header only | `tabular*` role header. No table elsewhere, no text box, no image of text, no icon, no photo |

**All four FAILs trace only to the two-column role header.** That is the
accepted exception recorded in `CV-SPEC.md` item 2 and in `RUBRIC.md`
"Accepted exception, set by Lucas 2026-09-01". Reported, not blocking.
No other cause of 0.5-0.8 exists in either document.

### LinkedIn ground-truth cross-check — PASS

Every title, company and date, character for character against the
`DOSSIER.md` LinkedIn block.

| Resume block | Resume text | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` | `Mid-level Software Engineer` / `Luizalabs` / `Jan 2024 - Jan 2026` | YES |
| 3 | `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | YES |
| 4 | `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | identical | YES |
| Education | `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — periods identical; ASCII hyphen per CV-SPEC item 5 |

Both Lippaus roles are present and separate. The promotion is preserved.
**No Gate 0 FAIL from the ground-truth check.**

One location conflict, outside the title/company/date scope: see fix 13.

### Forbidden-token grep

```
grep -rniE 'ruby|rails|unverified' charterup-senior-fullstack-en.tex charterup-senior-fullstack-pt.tex
```
**Zero hits in either `.tex`.** Zero hits across all four extraction files.
No `[UNVERIFIED]` marker ships in this package.

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | "We hire in the U.S. and Canada and are actively expanding our global footprint." No Brazil work-authorization requirement is stated | **not stated** |
| Location | "Location: Remote, Brazil" | **PASS** — resume states `Vitória, ES, Brazil` |
| Time-zone overlap | Not stated in the posting. The capture file records this explicitly | **not stated** — resume states `US-hours overlap` anyway |
| Minimum years of experience | "5+ years of professional experience as a full stack software engineer" | **PASS** — Mar 2021 to Sep 2026 = 5 yr 6 mo from LinkedIn dates; Summary states `5+ years` |
| English proficiency | Not stated in the posting | **not stated** — resume states `Advanced/C1` anyway |
| Degree requirement | Not stated in the posting | **not stated** |

Required-skill presence, verbatim in the raw extraction:

| Required skill (posting's words) | Present verbatim? |
|---|---|
| `full stack` | YES |
| Frontend framework `Vue`, `React` or `Angular` | **React YES.** Vue absent, Angular absent. The OR is satisfied |
| Backend `JVM-based environments (Java, Kotlin, C#)` | **Java YES** as a token. `JVM` absent. Kotlin, C# absent |
| `AWS` | YES |
| AI-based development or deployment tools | YES — `AI-assisted development` verbatim |
| `cross-functional` teams | **NO — absent from both documents** |
| Mentor junior engineers | **NO — absent from both documents** |

**Verdict: PASS with defects.** No hard knockout fails. The posting states no
work-authorization, time-zone, English or degree gate; the two gates it does
state, location and years, both pass. Two required-skill tokens are absent
verbatim. Those are Gate 2 losses and ranked defects, not knockouts.

---

## Gate 2 — Retrieval coverage: EN 19 / 100, PT 16 / 100

### Scoring conventions used, stated so this is reproducible

1. Where the posting offers alternatives ("Vue, React, **or** Angular";
   "Java, Kotlin, C#"), the group scores **once**, at its best-covered member.
   Scoring each alternative separately would triple-penalize an OR.
2. The rubric ladder assumes a token can sit in `Skills`. For phrase tokens
   that cannot (`full stack`, `5+ years`, `end-to-end`), and for skill tokens
   found in `Experience` but **not** in `Skills`, the ladder has no rung.
   I score those **2**, between "Skills only" (1) and "Skills + Experience" (3),
   and mark the row. This is my convention, not the rubric's text.
3. The Step 4 stuffing penalty is applied only to tokens in this table.
   Applying it to every `Skills` entry regardless of relevance to this posting
   would drive every document near zero. Unsupported `Skills` tokens outside
   this table are reported as fix 12 instead.

### Required tokens — weight 3, max 4 points each

| # | Token | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| R1 | `full stack` | — | no | **yes** | 2 | Summary only: "5+ years delivering full stack TypeScript systems" |
| R2 | `5+ years` | — | no | **yes** | 2 | Summary only |
| R3 | `end-to-end` | — | **yes** | no | 2 | Lippaus entry-level b1: "features end-to-end" |
| R4 | Frontend framework (`Vue`\|`React`\|`Angular`) | **NO** | yes (React) | no | 2 | React appears once, DexCare b2. **`React` is absent from the Skills block.** Vue 0 hits, Angular 0 hits |
| R5 | JVM backend (`Java`\|`Kotlin`\|`C#`) | yes | yes | no | 3 | `Java` in Languages, and once in the Luizalabs bullet among three languages. No depth evidence |
| R6 | `AWS` | yes | yes | **yes** | 4 | Cloud and DevOps; DexCare b2; Summary |
| R7 | `JavaScript` | yes | yes | no | 3 | Languages; Lippaus entry-level b2 |
| R8 | `AI-assisted development` | yes | yes | **yes** | 4 | Own Skills group; DexCare b1; Summary. Posting's exact spelling |
| R9 | `cross-functional` | no | no | no | **0** | Absent |
| R10 | Mentor / mentoring | no | no | no | **0** | Absent |

Required subtotal: **22** of 120 (10 tokens x 3 x 4).

### Preferred tokens — weight 1, max 4 points each

| # | Token | Points | Note |
|---|---|---|---|
| P1 | `Vue` | 0 | Absent. The posting names it first in both the stack line and the requirements line |
| P2 | `REST API Services` | 4 | Skills, DexCare b3, Summary. Posting's exact capitalization |
| P3 | `Web Applications` | 0 | Absent verbatim. Synonym present: "multi-tenant web ... platform" |
| P4 | `Mobile Apps` | 1 | Skills label only ("Frontend and Mobile Apps"). Experience says "React Native mobile platform", a synonym |
| P5 | `Data Engineering` | 0 | Absent |
| P6 | `DevOps` | 1 | Skills label only ("Cloud and DevOps"). Supported in substance by Docker/Kubernetes/ArgoCD/CI-CD bullets, but the token itself is not in a bullet |
| P7 | `JVM` | 0 | Absent. The posting's own qualifier for its backend requirement |
| P8 | `Kotlin` / `C#` | 0 | Absent |
| P9 | `scalable` / `scalability` | 0 | Absent. Posting: "ensuring scalability, reliability" |
| P10 | `automation` | 0 | Absent |

Preferred subtotal: **8** of 40.

```
coverage = 100 * (22 + 8) / (120 + 40) = 100 * 30 / 160 = 18.75 -> 19
```

### Step 4 stuffing penalty: 0

No token in the table above appears 4 or more times. Highest counts are
`AWS` 3, `TypeScript` 3, `Node.js` 3, `AI-assisted development` 3. The
CV-SPEC 3-appearance cap holds. No token in the table sits in `Skills`
without Experience evidence.

### Portuguese: 16 / 100

Same structure, same technology tokens, three phrase losses:

| Token | EN | PT | Cause |
|---|---|---|---|
| `5+ years` | 2 | **0** | PT reads "mais de 5 anos". The token is gone |
| `monitoring` | 2 | **0** | PT reads "monitoramento" |
| all others | — | identical | Technology tokens are untranslated in both files |

```
coverage_pt = 100 * (20 + 6) / 160 = 16.25 -> 16
```

The posting is in English and the segment is us-direct. The English document
is the retrieval artifact. The PT gap is expected and is not a defect to fix.

### Required tokens not covered

Absent verbatim from **both** documents:

1. `Vue`
2. `Angular`
3. `JVM`
4. `Kotlin`
5. `C#`
6. `cross-functional`
7. Mentor / mentoring / "junior engineers"
8. `Data Engineering`
9. `Web Applications`
10. `scalability` / `scalable`
11. `automation`

Present but **not in the `Skills` block**, which is where recruiter boolean
search lands hardest:

12. `React` — one hit, buried in a DexCare bullet

---

## Gate 3 — Human scan: 92 / 100 (EN and PT)

| # | Check | Points | Basis |
|---|---|---|---|
| 3.1 | Target title in the top 15% | **15** / 15 | "Senior Software Engineer" opens the Summary, line 5 of a 54-line one-page document. It is also the current DexCare title |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | **16** / 20 | DexCare b1-b3 are the three most posting-relevant: AI-assisted development, React on AWS, REST API Services. Docked 4: **no bullet in the whole document carries a leadership, ownership or mentoring signal**, which is what a Senior requisition scans for first |
| 3.3 | Every bullet leads with an outcome or action verb | **15** / 15 | All 16 bullets lead with a bare verb: Enable, Reduce, Deliver, Serve, Delivered, Kept, Improved, Cut, Turned, Supported, Increased. Zero "Responsible for". Present tense for the current role, past for prior roles, correctly |
| 3.4 | At least 3 bullets carry a real number | **15** / 15 | Seven do: 7%, 25%, 15%, 33%, 20%, 18%, 26%. All trace to the DOSSIER metric list |
| 3.5 | Length: 1 page under 10 years | **10** / 10 | `pdfinfo` confirms `Pages: 1` for both |
| 3.6 | No unsupported buzzwords | **10** / 10 | No "team player", "results-driven", "passionate". Nothing comparable found |
| 3.7 | Skills grouped by category | **7** / 10 | Six labeled groups, good. Docked 3: `Frontend and Mobile Apps: React Native` is a **one-item group whose label promises frontend and delivers a mobile framework**. A recruiter scanning for Vue or React reads this line and sees neither |
| 3.8 | Scannable | **4** / 5 | Clean one-page render, ruled headers, bold companies, adequate role spacing per CV-SPEC item 2. Docked 1: wrapped bullets have no hanging indent, so the continuation line ("lint, complexity limits, and tests.") starts flush under the bullet glyph. Four bullets wrap in EN |

PT scores identically. Same structure, same defects, one extra wrapped bullet.

Not scored by the rubric but worth stating: **four of seven DexCare bullets
open with "Reduce"**. See fix 7.

---

## Defects, ranked by cost — fix list for the Resume Architect

16 items. Fixes 1-5 are the ones that move Gate 2.

| # | File and line | Defect | What would pass |
|---|---|---|---|
| **1** | `charterup-senior-fullstack-en.tex:67`, `-pt.tex:67` | **`React` is absent from the `Skills` block.** The line reads `Frontend and Mobile Apps: React Native`. `React Native` is a distinct skill token; a recruiter boolean for `React` as a term does not reliably resolve it. The posting names React in both the stack line and the requirements line. This is the single highest-cost Gate 2 loss in the document | Add `React` as its own entry ahead of `React Native`. DOSSIER supports it: React is a confirmed DexCare stack fact, and DexCare b2 already ships React in context. Raises R4 from 2 to 3, +1.9 Gate 2 points, and fixes Gate 3.7 (+3) |
| **2** | Both `.tex`, Skills and Summary | **`Vue` absent entirely.** The posting's first-named frontend framework, and its actual stack ("JavaScript (Vue, React)") | Cannot be fixed from `DOSSIER.md`. Vue is recorded nowhere and the Maestro brief names it as a gap. **Escalate to Lucas: has he used Vue?** If yes, he supplies the fact and it ships. If no, it stays absent. Do not add it on inference |
| **3** | Both `.tex`, Summary line 62 / 61, or a Lippaus bullet | **`cross-functional` absent.** Stated in "What You'll Bring": "thrives in cross-functional teams", and in "What You'll Do": "Collaborate cross-functionally" | The DOSSIER confirms "project scoping and stakeholder communication" at Lippaus but does not name the functions involved. **Escalate to Lucas: which functions did he work across?** Once confirmed, the Lippaus mid-level b1 (`en.tex:102`) carries the token naturally. Worth +4 raw Gate 2 points, the largest single required-token recovery available |
| **4** | Both `.tex`, DexCare or Luizalabs bullets | **Mentoring absent.** "Mentor junior engineers, sharing best practices in both traditional and AI-enhanced development techniques" is a stated responsibility and a Senior-level scan signal | No mentoring evidence exists in `DOSSIER.md`. **Escalate to Lucas.** Note that DexCare b1 is adjacent: he "built the agent environments: shared rules, codebase enforcement" for the team. If Lucas confirms this was mentoring or enablement of other engineers, the bullet can carry the token. Worth +4 raw points and closes the Gate 3.2 leadership gap |
| **5** | `en.tex:93`, `pt.tex:93` | **JVM backend evidence is thin and the `JVM` token is absent.** The only Java evidence is `Java` named among three languages in one Luizalabs bullet. The posting asks for "**Proven** backend experience in JVM-based environments" | `DOSSIER.md` records "Stack: Node, Java, and others" at Luizalabs with **no depth**, and the Maestro brief names JVM as the main risk. Do not manufacture depth. **Escalate to Lucas: what did he build in Java at Luizalabs?** Any depth claim ships `[UNVERIFIED]` until he answers. If nothing more is available, this posting stays a stretch and Lucas should know that before applying |
| 6 | Both `.tex`, Summary | `end-to-end` and leadership are not tied together. The posting asks for "hands-on leadership of end-to-end projects". The resume has "leading project scoping" at Lippaus (`en.tex:102`) and "features end-to-end" at Lippaus entry-level (`en.tex:112`), in two different roles, four years apart | The Architect's own draft report already flagged this as unsupported as a combined claim. Correct call. Leave it unless Lucas confirms he led an end-to-end project. Do not join two separate facts into one sentence |
| 7 | `en.tex:81, 82, 84, 86`; `pt.tex` same | **Verb monotony.** Four of seven DexCare bullets open with "Reduce". Reads as one template applied seven times and blunts the strongest section of the document | Vary the openers on two of the four. The outcomes and numbers stay identical. Not a rubric line item; it costs on the human scan |
| 8 | `en.tex:67`, `pt.tex:67` | One-item Skills group labeled `Frontend and Mobile Apps`. Gate 3.7, -3 | Resolved by fix 1. Consider splitting into `Frontend:` and `Mobile:` once React is present |
| 9 | Both `.tex`, Skills | `Data Engineering` absent. Named in "About The Role" as one of five disciplines the role leads | Preferred, weight 1. No DOSSIER support for an experience-level claim. The Architect's draft correctly declined it. Leave absent unless Lucas has a fact |
| 10 | Both `.tex`, DexCare bullets | `scalability` / `scalable` and `automation` absent. Posting: "ensuring scalability, reliability, and continuous improvement through intelligent monitoring and automation" | DexCare b7 (SPI, 33%) and b4 (event-driven services) both describe scale work without using the word. A one-word substitution in an existing bullet places the token with no new claim. Check the one-page fit after |
| 11 | `pt.tex:62` | PT Summary reads "mais de 5 anos", losing the `5+ years` token; `monitoramento` at `pt.tex:81` loses `monitoring` | Low priority. The posting is English and the segment is us-direct, so the EN file is the retrieval artifact. Fix only if the PT file is submitted anywhere |
| 12 | `en.tex:68` and `:71`, `pt.tex` same | Three `Skills` tokens have no supporting evidence anywhere in `Experience`: **`RabbitMQ`**, **`AMQP`**, **`Agentic workflows`**. `RUBRIC.md` Gate 2 Step 4 calls this out as a real human-reaction penalty | **Not a fabrication.** All three are `DOSSIER.md` FACTs, and Lucas explicitly directed RabbitMQ/AMQP to be "Skills token only, no service names on the CV". Reported so Lucas knows the cost. His instruction stands unless he changes it |
| 13 | `en.tex:101` and `:110`, `pt.tex` same | **Both Lippaus roles print `Remote`. LinkedIn records `Lippaus Distribuidora` as `On-site`, Vitória, Espírito Santo, Brazil.** The DOSSIER rule "Role locations print `Remote` only" justifies itself against Seattle and São Paulo, the DexCare and Luizalabs employer cities. It does not address the Lippaus On-site record | **Escalate to Lucas.** This is a conflict between two of his own instructions, not an Architect error. It is outside the title/company/date scope, so it is not a Gate 0 FAIL. I do not resolve it |
| 14 | `en.tex:62`, `pt.tex:62` | Summary claims "US teams and **US-hours overlap**". `DOSSIER.md` confirms "Daily English-only work with US teams at DexCare" as FACT. **"US-hours overlap" is not recorded anywhere in the DOSSIER** | The posting does not state a time-zone requirement, so this sentence buys nothing at Gate 1 here. Either get Lucas to confirm the overlap as a fact, or drop the clause. Do not ship an unrecorded claim unmarked |
| 15 | `en.tex:81`, `pt.tex:81` | Attribution drift. The bullet reads "Reduce release risk by 7% by shipping **React on AWS** with LaunchDarkly/OpenFeature flags". `DOSSIER.md` D5 attributes the 7% to **feature flags**, not to React or AWS | Rephrase so the 7% attaches to the flags, and keep React and AWS as the delivery context. The tokens survive, the causal claim becomes accurate |
| 16 | `en.tex:104` and `:113`, `pt.tex` same | Two Lippaus claims are not in the DOSSIER: "Supported **nationwide expansion**" and "for a **beverage distribution startup**". The DOSSIER confirms the multi-tenant platform and the stack, but records neither Lippaus's industry, nor its stage, nor a national rollout | Confirm both with Lucas or remove them. Neither carries a posting token, so removal costs nothing at Gate 2 |

---

## Claims I could not verify

Listed for Lucas. Not deleted, not defended.

1. **"US-hours overlap"** — `en.tex:62`, `pt.tex:62`. Not in `DOSSIER.md`. See fix 14.
2. **7% attributed to React on AWS** — `en.tex:81`. DOSSIER D5 attributes it to feature flags. See fix 15.
3. **"Supported nationwide expansion"** — `en.tex:104`. Lippaus national rollout is not recorded.
4. **"for a beverage distribution startup"** — `en.tex:113`. Lippaus's industry and stage are not recorded.
5. **"gated by Vitest and Jest in CI/CD"** — `en.tex:94`. The DOSSIER confirms Vitest and Jest as tools used at Luizalabs and Lippaus. It does not record that they gated a CI/CD pipeline.
6. **Java depth at Luizalabs** — `en.tex:93`. The DOSSIER records "Node, Java, and others" with no depth. The bullet is correctly scoped and claims nothing more. Flagged only because this posting requires "proven backend experience in JVM-based environments", so Lucas needs to know exactly how thin this is before he applies. See fix 5.
7. **Lippaus location "Remote"** — conflicts with the LinkedIn "On-site" record. See fix 13.

Verified and clear, checked but needing no action: every title, company and
date (LinkedIn block); all seven percentage figures (DOSSIER metric list, IDs
D2, D3, D5, D7, L2, L3, P2); the DexCare stack tokens (FACT-OBSERVED from the
repos); `Go` at Luizalabs; the SPI description; `RabbitMQ`/`AMQP` and
`Agentic workflows` as Skills tokens; the Information Systems degree at FAESA;
`Vitória, ES, Brazil` on the contact line with no UTC offset printed.

---

## Analyzer's read, in one paragraph

The document is mechanically sound. It parses, the employment blocks segment
correctly apart from the accepted header exception, every title and date
matches LinkedIn character for character, no Ruby or Rails token appears, no
`[UNVERIFIED]` marker ships, and it scans well for a human at 92. Gate 2 at 19
is not a build defect. It is the honest distance between this candidate and
this posting: CharterUP wants Vue on the frontend and proven JVM on the
backend, and `DOSSIER.md` supports neither. Fixes 1, 3, 4 and 10 are the
recoverable points and they are worth roughly 12 Gate 2 points. Fixes 2 and 5
are not the Architect's to make. They are questions for Lucas, and his answers
decide whether this application is worth sending.
