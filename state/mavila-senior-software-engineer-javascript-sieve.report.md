# ATS Analysis — resumes/hunts/2026-09-04-c/mavila-senior-software-engineer-javascript/Lucas-Queiroz-Resume-en.pdf vs mavila-senior-software-engineer-javascript
Segment: agency (Mavila Consulting, contractor assignment)   Date: 2026-09-04

Analyst: Sieve, ATS Analyzer. No file was edited. No subagent was spawned.

Extraction commands, run in the package directory:

```
pdftotext         Lucas-Queiroz-Resume-en.pdf - > raw.txt
pdftotext -layout Lucas-Queiroz-Resume-en.pdf - > layout.txt
```

Gate 0 and Gate 2 are judged on `raw.txt`.

## Verdict

**BLOCKED at Gate 1.** Two posting requirements have no evidence on the CV and
no support in `DOSSIER.md`. Neither is an Architect defect. Neither can be
fixed by editing the document.

- Gate 0 — Parse integrity: **PASS**, 8 of 8.
- Gate 1 — Knockouts: **FAIL**, 2 blockers.
- Gate 2 — Retrieval coverage: **57 / 100, FAIL**. Two required tokens score 0.
- Gate 3 — Human scan: **85 / 100**.

---

## Gate 0 — Parse integrity

`pdfinfo`: 1 page, 612 x 792 pts, PDF 1.5, 27563 bytes. `pdfimages -list`
returns zero images.

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction is 56 non-empty lines of complete prose. Contact block, five section headers, four Experience blocks, one Education block |
| 0.2 | Glyph integrity | PASS | Measured by codepoint. Zero `U+0000`, zero `U+FB00-FB06` ligature codepoints, zero `?`, zero `U+FFFD`. The only codepoint above `U+00FF` is `U+2022 BULLET`. Ligature-bearing words intact: `workflow` 5 hits (`workflows`), `office` 2 hits (`back-office`). `profile`, `efficient` and `conflict` do not occur in this document, so those arms are not exercised |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, not a header or footer: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email and LinkedIn URL all present. No UTC offset and no time-zone overlap sentence, per `CLAUDE.md` section 3 |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 11, 20, 23, 62: `SUMMARY`, `SKILLS`, `LANGUAGE`, `EXPERIENCE`, `EDUCATION`, each a standalone line. Source strings are `\section{Summary}`, `{Skills}`, `{Language}`, `{Experience}`, `{Education}`. Uppercase is `\scshape` rendering, which the gate allows |
| 0.5 | Employment-block segmentation | PASS | Four employment blocks, each a contiguous run: `Company \| Dates` on one line, `Title \| Location` on the next, then its bullets. No two roles merge. No role splits. Both Lippaus entries repeat the company name, so the promotion segments unambiguously. The tailored file replaced the base `tabular*` role header with two consecutive text lines, per `CV-SPEC.md` item 2. This removes the header-only 0.5-0.8 finding carried by every earlier `tabular*` build |
| 0.6 | Date parseability | PASS | Every role carries `Mon YYYY - Mon YYYY` on the same line as its company, one line above its title: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Separator verified by Unicode category `Pd`: the only dash character in the whole document is `U+002D HYPHEN-MINUS` |
| 0.7 | Reading order | PASS | Raw and layout are identical after whitespace normalization. Zero content blocks reorder |
| 0.8 | No forbidden constructs | PASS | No `tabular`, no `tabular*`, no text box. `pdfimages -list` returns an empty table, so no image of text, no contact icon and no photo |

**Gate 0 verdict: PASS.**

### Profile Check — LinkedIn verification

Read live in the `Profile Check` portal on 2026-09-04:
`https://www.linkedin.com/in/queiroz-lucas/details/experience/` and
`https://www.linkedin.com/in/queiroz-lucas/details/education/`.

| Block | Resume text | LinkedIn, read live | Match |
|---|---|---|---|
| 1 | `DexCare` / `Senior Software Engineer` / `Mar 2026 - Present` / `Remote` | `Senior Software Engineer` · `DexCare · Full-time` · `Mar 2026 - Present · 7 mos` | YES |
| 2 | `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Mar 2026` / `Remote` | `Mid-level Software Engineer` · `Luizalabs · Full-time` · `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | YES |
| 3 | `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` / `Vitória, ES, Brazil` | `Lippaus Distribuidora` · `Mid-level Software Engineer` · `Jan 2023 - Jan 2024 · 1 yr 1 mo` | YES |
| 4 | `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` / `Vitória, ES, Brazil` | `Lippaus Distribuidora` · `Entry-level Fullstack Software Engineer` · `Mar 2021 - Jan 2023 · 1 yr 11 mos` | YES |
| Education | `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA` · `Bachelor's degree , Information Systems` · `Feb 2022 – Dec 2025` | YES — start and end months identical. ASCII hyphen per `CV-SPEC.md` item 5 |

Every employer, title, start month and end month matches. Company spelling
`Luizalabs` correct. Both Lippaus roles present and separate. Role locations
correct per `CLAUDE.md` section 3: `Remote` for DexCare and Luizalabs,
`Vitória, ES, Brazil` for both Lippaus roles. Degree is Information Systems at
FAESA. The profile was not edited.

**Stale-document note, not a CV defect.** `CV-SPEC.md` still says "Luizalabs
ended **Jan 2026**", and `reports/maxxi-full-stack-senior-gate.md` records
`Jan 2024 - Jan 2026`. The `DOSSIER.md` LinkedIn ground truth captured
2026-09-04 and the live profile both say `Mar 2026`. The tailored CV follows
the live profile and is correct. `CV-SPEC.md` is out of date on this line.

### Forbidden-token grep

```
grep -inE 'ruby|rails|sidekiq|activerecord|activejob|rspec|devise|pundit|hotwire'
```

Zero hits on `Lucas-Queiroz-Resume-en.tex` and zero on the raw extraction.

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | `Employment type: Contractor assignment`; `Location: Bangladesh, Brazil, Colombia, Egypt, Ghana, India, Indonesia, Turkey, Vietnam` | PASS. CV prints `Vitória, ES, Brazil`. Brazil is on the accepted list. Contract type is not on the CV, correctly; the apply note records PJ and W-8BEN acceptance, which `DOSSIER.md` supports |
| Location or time-zone overlap | `Remote`; `4 hrs/day overlap with PST` | PASS on location. Overlap is not printed on the CV, per `CLAUDE.md` section 3, and is answered in the apply note screening answers |
| Minimum years of experience | no number stated | not stated |
| **Seniority level** | `We are looking for experienced software engineers (tech lead level)` | **FAIL.** The CV carries no tech lead title and no team-leadership evidence. Titles are Senior, Mid-level, Mid-level, Entry-level. `Led project scoping and stakeholder communication` is scoping and stakeholder work, not technical team leadership. `DOSSIER.md` records no lead role. Do not infer one |
| **Public repository experience** | `familiar with high-quality public GitHub repositories`; `You should have experience working with well-maintained, widely-used repos with 5000+ stars` | **FAIL.** No evidence on the CV. `DOSSIER.md` records none, and it explicitly excludes the old unsourced open-source contribution claim. `GitHub` appears once, in the contact-block URL only |
| English proficiency requirement | not stated | not stated. The CV prints `English: Fluent (C1)` in the `Language` section regardless |
| Required skill — `Strong experience with JavaScript` | posting | PASS. Skills `Languages: JavaScript`; Lippaus 2021 bullet `back-office dashboards in JavaScript` |
| Required skill — `Git` | posting | PASS. Skills `Cloud and operations: Git`; DexCare bullet `versioned in Git` |
| Required skill — `Docker` | posting | PASS. Skills `Cloud and operations: Docker`; Luizalabs bullet `deploying services with Docker and Kubernetes on GCP` |
| Required skill — `basic software pipeline setup` | posting | PASS. Skills `Pipeline setup`; Luizalabs bullet `gating the CI/CD pipeline setup` |
| Required skill — `understand and navigate complex codebases` | posting | PASS. Skills `Complex codebases`; DexCare SPI bullet `across complex codebases spanning multiple services` |
| Required skill — `running, modifying, and testing real-world projects locally` | posting | PASS with a note. The claim sits in the Summary only: `I run, modify, and test complex codebases locally with Git and Docker`. No Experience bullet states local execution. See defect 3 |
| Degree requirement | not stated | not stated |

**Gate 1 verdict: FAIL.** Two blockers, both candidate-fact gaps. The Resume
Architect cannot close either one without a new fact from Lucas. This is a
Maestro decision: obtain the facts from Lucas, or drop the posting.

---

## Gate 2 — Retrieval coverage: 57 / 100, FAIL

Token rule used, stated so the result is reproducible: a token matches when it
appears in the raw extraction as a word or as a word prefix of the posting's
term, for example `Unit testing` matches `unit test`. A multi-word term needs
its words adjacent, so `agent environments` does not match `automation
agents`.

Weights per `RUBRIC.md`: required = 3, preferred = 1.

### Required tokens, weight 3

| # | Token, posting words | Skills | Experience | Placement | Points |
|---|---|---|---|---|---|
| R1 | `JavaScript` | YES, `Languages` | YES, Lippaus 2021, `back-office dashboards in JavaScript` | Skills + Experience | 3 |
| R2 | `Git` | YES, `Cloud and operations` | YES, DexCare, `versioned in Git` | Skills + Experience | 3 |
| R3 | `Docker` | YES, `Cloud and operations` | YES, Luizalabs, `deploying services with Docker and Kubernetes` | Skills + Experience | 3 |
| R4 | `pipeline setup` | YES, `Testing and practices` | YES, Luizalabs, `gating the CI/CD pipeline setup` | Skills + Experience | 3 |
| R5 | `complex codebases` | YES, `Testing and practices` | YES, DexCare, `across complex codebases spanning multiple services` | Skills + Experience | 3 |
| R6 | `GitHub` | NO | NO | Contact-block URL only, `github.com/queirozlc` | **0** |
| R7 | `repos with 5000+ stars` | NO | NO | Absent entirely | **0** |

Required subtotal: 15 points of 21. Weighted: 45 of 63.

### Preferred tokens, weight 1

| # | Token, posting words | Skills | Experience | Placement | Points |
|---|---|---|---|---|---|
| P1 | `open-source` | NO | NO | Absent | 0 |
| P2 | `LLM` | NO | NO | Absent. The three case-insensitive hits are the substring inside `BullMQ`, not the token | 0 |
| P3 | `developer tools` | NO | YES, DexCare, `a developer tooling layer` | Experience only | 2 |
| P4 | `automation agents` | NO | NO | Absent. `agent environments` and `agentic workflows` are different terms | 0 |
| P5 | `unit test` | YES, `Unit testing` | YES, Luizalabs, `Vitest and Jest unit testing` | Skills + Experience | 3 |
| P6 | `environment setup` | YES, `Environment setup` | NO. `agent environments` and `per-customer environments` are not the term | Skills only | 1 |
| P7 | `Dockerization` | NO | NO | Absent. `Docker` is present, the derived noun is not | 0 |
| P8 | `triage` / `triaging` | NO | NO | Absent | 0 |
| P9 | `test coverage` | NO | NO | Absent | 0 |

Preferred subtotal: 6 points of 27. Weighted: 6 of 27.

### Score

```
coverage = 100 * (45 + 6) / (63 + 27) = 100 * 51 / 90 = 56.7 -> 57
```

Stuffing penalty: **0**. No token reaches 4 appearances. Counted in the raw
text: `JavaScript` 3, `TypeScript` 3, `Node.js` 3, `React` 3, `Go` 3,
`Git` 3 as a word plus 1 inside the `github.com` URL, `Docker` 3,
`PostgreSQL` 3, `Kubernetes` 2, `CI/CD` 2.

**Gate 2 result: 57 / 100, FAIL.**

Required tokens without Skills and Experience placement: **`GitHub`,
`repos with 5000+ stars`**.

Neither is fixable by an edit. `GitHub` could be written into Skills, but a
Skills entry with no supporting Experience bullet earns 1 point, not 3, and
would still fail the gate. The underlying requirement is an experience claim
that `DOSSIER.md` does not record.

---

## Gate 3 — Human scan: 85 / 100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15 / 15 | `Senior Software Engineer` appears on raw line 6, the first Summary line, and again as the DexCare title. The document is 56 non-empty lines, so the top 15% ends near line 8 |
| 3.2 | The 3 most relevant bullets in the most recent role, first 3 lines | 7 / 20 | The three bullets that answer this posting are DexCare bullet 1 (`versioned in Git`), bullet 6 (`agent environments, a developer tooling layer`) and bullet 7 (`across complex codebases`). Only bullet 1 is inside the first three lines. Bullets 2 to 5 are Epic EMR, Auth0, data modelling and feature flags, none of which this posting asks for. The `Docker` and `unit testing` evidence is further down still, in the Luizalabs block |
| 3.3 | Past-tense action verb, outcome, no duty list | 15 / 15 | All 16 bullets open with a past-tense verb, subject omitted: `Built` x7, `Integrated`, `Modeled`, `Reduced`, `Helped implement`, `Moved`, `Kept`, `Processed`, `Led`, `Developed`. No present tense. No `Responsible for`. No third person |
| 3.4 | At least 3 bullets with a real number | 15 / 15 | Seven: 15%, 25%, 7%, 33%, 20%, 18%, 26% |
| 3.5 | Experience completeness | 10 / 10 | Diffed `resumeItem` lines against `resumes/base-en.tex`. Every base Experience role, bullet and metric is present. Four bullets are reworded, none deleted, no metric dropped. The one line-count difference is the Skills section splitting `Testing and AI tooling` into `Testing and practices` plus `AI tooling`. One page |
| 3.6 | No unsupported buzzwords | 10 / 10 | No `team player`, `results-driven`, `passionate`, `synergy`, `rockstar`, `ninja` |
| 3.7 | Skills grouped by category | 10 / 10 | Seven labelled groups: `Languages`, `Backend`, `Data`, `Frontend`, `Cloud and operations`, `Testing and practices`, `AI tooling` |
| 3.8 | Scannable | 3 / 5 | One page, bold company names, italic titles, consistent `Company \| Dates` then `Title \| Location` order. Deducted 2: the tailored file tightened the top margin from -0.5in to -0.6in, text height from +1.0in to +1.2in, the section gap from 3pt to 2pt, and it separates one role block from the next with only `\vspace{3pt}`. `CV-SPEC.md` item 2 asks for clear vertical space between the last bullet of a role and the next role header. Extraction still segments every block correctly, so this is a human-scan cost, not a parse risk |

**Gate 3 total: 85 / 100.**

---

## Claim audit against DOSSIER.md and the job-file Git evidence

`DOSSIER.md` and the `Preflight evidence` block in
`jobs/mavila-senior-software-engineer-javascript.md` are the only claim sources
used here.

### Correctly not claimed

Each of these is a posting term with no dossier support, and the CV does not
assert any of them. This is correct behaviour, recorded for the Maestro.

| Posting term | On the CV? |
|---|---|
| Contributing to or evaluating open-source projects | Not claimed |
| Public repositories with 5000+ stars | Not claimed |
| LLM research or evaluation projects | Not claimed. The CV says `AI-driven agentic workflows` and `Claude Code and Codex agent environments`, both dossier facts |
| Triaging GitHub issues | Not claimed |
| Evaluating unit test coverage and quality | Not claimed. `Vitest and Jest unit testing gating the CI/CD pipeline setup` is the dossier's testing fact, not a coverage-evaluation claim |
| Dockerization as a task | Not claimed. `Docker` appears only as the Luizalabs deployment fact |
| Leading a team of junior engineers | Not claimed. `Led project scoping and stakeholder communication` is the dossier-approved Lippaus bullet about scoping and stakeholders |

### Claims to review

| Claim | Source status |
|---|---|
| Summary: `I run, modify, and test complex codebases locally with Git and Docker` | Composite. The job file records local Git commit evidence in `~/dexcare/IntegratedScheduling`. `DOSSIER.md` records Docker at Luizalabs as a deployment tool. Neither source records Lucas running codebases locally under Docker. The two halves are supported separately, the joined sentence is an inference. See defect 3 |
| DexCare bullet: `a developer tooling layer` | Wording. `DOSSIER.md` records `Built the agent environments: shared rules, codebase enforcement (lint, cyclomatic complexity limits, testing)`. `developer tooling layer` is a fair characterization of that same fact, added to reach the nice-to-have term. Low severity |
| Summary: `5+ years` | Supported. Mar 2021 to Sep 2026 is 5 years 6 months against the verified LinkedIn dates |
| Luizalabs bullet: `Node.js, Java, and Go` | Supported. `DOSSIER.md`: `Stack: Node, Java, and others`, and Go at Luizalabs is in the approved bullet list |
| Summary: `Magazine Luiza's electronic-invoicing microservices` | Supported. `DOSSIER.md` fiscal / NF-e / SEFAZ entry |
| Skills: `Complex codebases`, `Environment setup`, `Pipeline setup` | Not fabricated facts. They are posting phrases placed in a skills list. See defect 4 |

### Application message

`application-message.md` is a draft, marked `Lucas sends it`, with no agent
send action. Screening answers correctly defer the four unknown items to Lucas:
5000+ star repositories, open-source contribution, LLM evaluation projects and
leading junior engineers. Overlap with PST is answered in the note and not on
the CV, per `CLAUDE.md`. No credential appears. Nothing to correct.

---

## Defects, ranked by cost

1. **`repos with 5000+ stars` and public GitHub repository familiarity have no
   evidence** — Gate 1 FAIL, Gate 2 R6 and R7 at 0 points. Posting text:
   `You should have experience working with well-maintained, widely-used repos
   with 5000+ stars`. `DOSSIER.md` records nothing, and it explicitly excludes
   the old unsourced Rails gem contribution claim. **No document fix exists.**
   Lucas must supply the fact, or the Maestro drops the posting. Do not write
   `GitHub` or `open-source` into the CV without a source.

2. **`tech lead level` has no evidence** — Gate 1 FAIL. Posting text:
   `We are looking for experienced software engineers (tech lead level)`.
   Verified titles are Senior, Mid-level, Mid-level, Entry-level. The dossier
   records no lead role and no junior-engineer leadership. **No document fix
   exists.** Do not adjust a title, per `CLAUDE.md` rule 1.

3. **The local-execution claim is a composite inference, and it lives in the
   Summary only** — Gate 1 note, Gate 3.2. Text to review:
   `I run, modify, and test complex codebases locally with Git and Docker`.
   Git is sourced from the job file's local commit evidence. Docker is sourced
   from the Luizalabs deployment fact. The joined statement is neither source.
   Either narrow it to what the sources carry, or have Lucas confirm it. The
   posting's `Comfortable running, modifying, and testing real-world projects
   locally` also has no Experience bullet behind it.

4. **Three posting phrases sit in `Skills` as if they were technologies** —
   Gate 3 human-scan risk, no points deducted. Text:
   `Testing and practices: Unit testing | Vitest | Jest | Complex codebases |
   Environment setup | Pipeline setup`. `Complex codebases`, `Environment
   setup` and `Pipeline setup` are activities, not skills. They read to a human
   as keyword placement. They do earn real Gate 2 points, so this is a
   trade-off for the Architect and the Maestro to weigh, not an automatic fix.

5. **The three most posting-relevant DexCare bullets are not the first three**
   — Gate 3.2, 13 points lost. `versioned in Git` is bullet 1, but
   `agent environments, a developer tooling layer` is bullet 6 and
   `across complex codebases` is bullet 7. Reordering the DexCare bullets is
   allowed by `CLAUDE.md` section 9.1 and costs no fact. Deleting is not.

6. **Role separation is thin** — Gate 3.8, 2 points lost. `\resumeRoleGap` is
   `\vspace{3pt}` and the section gap dropped to 2pt. `CV-SPEC.md` item 2 asks
   for clear vertical space between the last bullet and the next role.
   Extraction is unaffected.

7. **`developer tooling layer` reaches for a nice-to-have term** — wording,
   low severity. The dossier fact is `agent environments` with shared rules,
   lint enforcement, cyclomatic complexity limits and tests. The added phrase
   describes the same work. Keep or drop, either is defensible.

8. **`CV-SPEC.md` is stale on the Luizalabs end month** — workspace defect, not
   a CV defect. It says `Luizalabs ended Jan 2026`. The live LinkedIn profile
   and the `DOSSIER.md` ground truth captured 2026-09-04 both say `Mar 2026`.
   The CV is right. The spec needs the correction. Not mine to make.

## Match limits

Preferred tokens not placed: `open-source`, `LLM`, `automation agents`,
`Dockerization`, `triage`, `test coverage`. `developer tools` reaches
Experience only. `environment setup` reaches Skills only.

Six of the nine preferred tokens describe the LLM-evaluation and open-source
core of this role. Their absence is the same candidate-fact gap that blocks
Gate 1, seen from the retrieval side. This posting asks for a body of
experience the verified record does not contain. The document is not the
limit here.
