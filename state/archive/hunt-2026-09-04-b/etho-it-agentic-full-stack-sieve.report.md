# ATS Analysis — resumes/hunts/2026-09-04-b/etho-it-agentic-full-stack/Lucas-Queiroz-Resume-en.pdf vs etho-it-agentic-full-stack
Segment: us-direct (Contract, US-based stakeholders, company origin not observable)   Date: 2026-09-04

Artifacts under test, all present and read:
- `resumes/hunts/2026-09-04-b/etho-it-agentic-full-stack/Lucas-Queiroz-Resume-en.tex`
- `resumes/hunts/2026-09-04-b/etho-it-agentic-full-stack/Lucas-Queiroz-Resume-en.pdf` (1 page, 27353 bytes, PDF 1.5, xdvipdfmx)
- Raw extraction: `pdftotext Lucas-Queiroz-Resume-en.pdf` (54 non-blank lines)
- Layout extraction: `pdftotext -layout Lucas-Queiroz-Resume-en.pdf`

Every judgement below is made on the raw extraction, not on the `.tex` and not on
pasted text.

## Verdict

**BLOCKED at Gate 1.** Gate 0 passes 8 of 8. Gate 1 fails on two stated posting
requirements: minimum years of experience, and required-skill presence. Gate 2
scores 39/100 and FAILS the required-token rule with 14 required tokens at zero
placement points. Gate 3 scores 88/100 and is reported only.

Gate 1 and Gate 2 fail for the same underlying reason: the posting's core
required qualifications (MCP, Anthropic Messages API, tool use, function
calling, prompt and skill engineering, code review, OWASP, IaC) have no support
in `DOSSIER.md`. This is a claim-source gap, not a writing defect. The Architect
cannot close it without new facts from Lucas.

## Gate 0 — Parse integrity

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction returns 54 non-blank lines of clean text. No image-only page. |
| 0.2 | Glyph integrity | PASS | Zero U+FB00-U+FB06 ligature codepoints. Zero `\x00`. Zero U+FFFD. Only two non-ASCII characters in the whole file: `•` (16) and `ó` (4). `workflow` matches 5 times, `office` 2 times (`back-office`), `fi` 5, `fl` 8, `ff` 2. `profile`, `efficient`, `conflict` do not occur in this document, so they are not testable here. |
| 0.3 | Contact block recoverable | PASS | Line 3 of the raw stream: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. In the body. No PDF header or footer object. No UTC offset and no time-zone statement, per CLAUDE.md rule 3. |
| 0.4 | Section headers present verbatim | PASS | Raw stream carries `SUMMARY`, `SKILLS`, `LANGUAGE`, `EXPERIENCE`, `EDUCATION` as standalone lines. Uppercase rendering is allowed by the rubric; the `.tex` source strings are `Summary`, `Skills`, `Language`, `Experience`, `Education`. |
| 0.5 | Employment-block segmentation | PASS | Four separate blocks in the raw stream, each `Company \| Title` then `Location \| Dates` then its bullets: `DexCare \| Senior Software Engineer`, `Luizalabs \| Mid-level Software Engineer`, `Lippaus Distribuidora \| Mid-level Software Engineer`, `Lippaus Distribuidora \| Entry-level Fullstack Software Engineer`. No merge. No split. The two Lippaus roles stay distinct. |
| 0.6 | Date parseability | PASS | Every role date line is `Mon YYYY - Mon YYYY` with an ASCII hyphen, on the line adjacent to the title line: `Remote \| Mar 2026 - Present`, `Remote \| Jan 2024 - Mar 2026`, `Vitória, ES, Brazil \| Jan 2023 - Jan 2024`, `Vitória, ES, Brazil \| Mar 2021 - Jan 2023`, `Vitória, ES, Brazil \| Feb 2022 - Dec 2025`. No EN DASH anywhere. |
| 0.7 | Reading order | PASS | Raw and layout extraction are identical line for line after stripping leading and trailing whitespace and blank lines. No adjacent block disagrees. |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` returns zero images. No table, no `tabular*`, no text box, no contact icon, no photo. Fonts are four embedded subsets with Identity-H encoding and ToUnicode present (`Roboto-Bold`, `Roboto-Regular`, `Roboto-Italic`, `CMSY9`). |

## Gate 1 — Knockouts

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | Posting text states no work-authorization requirement. LinkedIn metadata carries a `Contract` label only. | not stated |
| Location or time-zone overlap | Posting: `📍 Remote`, LinkedIn location `Brazil`, `Fluent English (US-based stakeholders)`. Resume contact line prints `Vitória, ES, Brazil`; DexCare and Luizalabs role locations print `Remote`. No overlap requirement stated. | PASS |
| Minimum years of experience | Posting: `6+ years of full stack development ... with production ownership`. LinkedIn earliest role starts `Mar 2021`. Mar 2021 to Sep 2026 is 5 years 6 months. Resume Summary states `5+ years`. | **FAIL** |
| English proficiency requirement | Posting: `Fluent English, comfortable working directly with US-based stakeholders`. Resume `LANGUAGE` section: `Portuguese: Native \| English: Fluent (C1)`. | PASS |
| Each required skill present verbatim | 12 of 26 required tokens present in the raw text. 14 absent, including the posting's own headline requirements `MCP`, `MCP servers`, `Anthropic Messages API`, `tool use`, `function calling`, `prompt engineering`, `skill engineering`, `code review`, `OWASP`, `IaC`. Rubric: for every explicit posting requirement, absent resume evidence is a FAIL. | **FAIL** |
| Degree requirement | Posting states none. | not stated |

### LinkedIn verification, Profile Check portal, read 2026-09-04

Read from `https://www.linkedin.com/in/queiroz-lucas/details/experience/` and
`https://www.linkedin.com/in/queiroz-lucas/details/education/`. The profile was
not edited.

| LinkedIn, verbatim | Resume raw extraction | Match |
|---|---|---|
| `Senior Software Engineer` / `DexCare · Full-time` / `Mar 2026 - Present · 7 mos` | `DexCare \| Senior Software Engineer` / `Remote \| Mar 2026 - Present` | exact |
| `Mid-level Software Engineer` / `Luizalabs · Full-time` / `Jan 2024 - Mar 2026 · 2 yrs 3 mos` | `Luizalabs \| Mid-level Software Engineer` / `Remote \| Jan 2024 - Mar 2026` | exact |
| `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024 · 1 yr 1 mo` | `Lippaus Distribuidora \| Mid-level Software Engineer` / `Vitória, ES, Brazil \| Jan 2023 - Jan 2024` | exact |
| `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023 · 1 yr 11 mos` | `Lippaus Distribuidora \| Entry-level Fullstack Software Engineer` / `Vitória, ES, Brazil \| Mar 2021 - Jan 2023` | exact |
| `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | `FAESA \| Bachelor's degree, Information Systems` / `Vitória, ES, Brazil \| Feb 2022 - Dec 2025` | exact on period; separator is the ASCII hyphen required by CV-SPEC item 5 |

Nine of nine employer, title and date strings verified against LinkedIn. Zero
defects. Role locations follow CLAUDE.md rule 3: DexCare and Luizalabs print
`Remote`, Lippaus prints `Vitória, ES, Brazil`.

### Years-of-experience arithmetic

Earliest LinkedIn employment start: `Mar 2021`. Today: 2026-09-04.
Mar 2021 to Mar 2026 is 5 years. Mar 2026 to Sep 2026 is 6 months.
Total: **5 years 6 months**. The posting requires **6+ years**. The gap is
6 months. The resume states `5+ years`, which is accurate and must not be
changed. The knockout is real and cannot be fixed on the document.

## Gate 2 — Retrieval coverage: 39/100, FAIL

Requirements extracted from the posting's own `Required qualifications` and
`Preferred qualifications` sections. Soft skills discarded
(`Ability to read and critique large volumes of generated code quickly`).

### Required tokens, weight 3

| # | Token | Skills | Experience bullet | Points |
|---|---|---|---|---|
| 1 | TypeScript | `Languages: TypeScript` | `Built event-driven TypeScript services on Express and Koa` | 3 |
| 2 | Node | `Node.js` | `Built distributed tax microservices in Node.js, Java, and Go` | 3 |
| 3 | React | `Frontend: React` | `monitoring React with Datadog RUM` | 3 |
| 4 | production ownership | absent | absent (Summary only: `Go systems with production ownership`) | **0** |
| 5 | Claude | inside `Claude Code` | inside `Built Claude Code and Codex agent environments` | 3 |
| 6 | Claude Code | `AI tooling: Claude Code` | `Built Claude Code and Codex agent environments` | 3 |
| 7 | Anthropic Messages API | absent | absent | **0** |
| 8 | tool use | absent | absent | **0** |
| 9 | function calling | absent | absent | **0** |
| 10 | prompt engineering | absent | absent | **0** |
| 11 | skill engineering | absent | absent | **0** |
| 12 | MCP | absent | absent | **0** |
| 13 | MCP servers | absent | absent | **0** |
| 14 | tools (MCP tool definitions) | absent | absent | **0** |
| 15 | resources (MCP resources) | absent | absent | **0** |
| 16 | test automation | `Test automation` | `Vitest and Jest test automation gating CI/CD` | 3 |
| 17 | code review | absent | absent | **0** |
| 18 | OWASP | absent | absent | **0** |
| 19 | secrets handling | `Secrets handling` | `through AWS SDK v3 for storage and secrets handling` | 3 |
| 20 | input validation | `Input validation` | `Auth0 JWT and OpenAPI/Swagger input validation` | 3 |
| 21 | AWS | `AWS` | `wired to S3, RDS, and Secrets Manager through AWS SDK v3` | 3 |
| 22 | GCP | `GCP` | `Docker and Kubernetes on GCP through ArgoCD` | 3 |
| 23 | Azure | absent | absent | **0** |
| 24 | containers | `Containers` | `Deployed services as containers with Docker and Kubernetes` | 3 |
| 25 | CI/CD | `CI/CD` | `test automation gating CI/CD` | 3 |
| 26 | IaC | absent | absent | **0** |

Required subtotal: **36 of 78** placement points. 12 tokens at 3, 14 tokens at 0.

### Preferred tokens, weight 1

| Token | Skills | Experience | Points |
|---|---|---|---|
| Multi-agent | absent | absent | 0 |
| planner | absent | absent | 0 |
| executor | absent | absent | 0 |
| critic | absent | absent | 0 |
| human-in-the-loop | absent | absent | 0 |
| LLM evaluation | absent | absent | 0 |
| evals | absent | absent | 0 |
| golden datasets | absent | absent | 0 |
| regression testing | absent | absent | 0 |
| token management | absent | absent | 0 |
| cost management | absent | absent | 0 |
| Jira | absent | absent | 0 |
| Confluence | absent | absent | 0 |
| spec-first | absent | absent | 0 |

Preferred subtotal: **0 of 42** placement points. 14 of 14 absent.

### Score

```
numerator   = (36 points x weight 3) + (0 points x weight 1)          = 108
denominator = (26 tokens x 3 x weight 3) + (14 tokens x 3 x weight 1) = 276
coverage    = 100 x 108 / 276                                         = 39
```

Stuffing penalty: **0**. No graded token appears 4 or more times. Highest graded
token frequency is 3 (`TypeScript`, `React`, `AWS`, `Claude Code`).

**Gate 2 result: 39/100, FAIL.** Step 4 of the rubric fails: 14 required tokens
earn fewer than 3 placement points.

### Required tokens without Skills and Experience placement

`production ownership`, `Anthropic Messages API`, `tool use`, `function calling`,
`prompt engineering`, `skill engineering`, `MCP`, `MCP servers`, `tools`,
`resources`, `code review`, `OWASP`, `Azure`, `IaC`.

### Placement notes, stated so the number is not read as more than it is

- **`Node` is a substring placement, not a standalone verbatim placement.**
  Skills and Experience carry `Node.js`. The bare string `Node` appears in the
  Summary only, inside `TypeScript/Node`. Scored 3 because any full-text index
  that tokenizes on non-alphanumerics emits `Node` from `Node.js`, and because
  ATS-KNOWLEDGE 4.2 records alias collapsing as a confirmed mechanism. That
  section also records that the specific `Node.js`/`Node` collapse is **not**
  confirmed. Treat this row as the least certain 3 in the table.
- **`Claude` is likewise a token inside `Claude Code`.** No standalone `Claude`
  appears in Skills or Experience.
- **`Azure` is one branch of the posting's own alternative** `AWS/GCP/Azure`.
  The document places `AWS` and `GCP` at 3 points each, so the posting's cloud
  requirement is satisfied on its own terms. The row scores 0 under the strict
  per-token rule this dispatch ordered. It is the one zero in the table that is
  not a real capability gap.
- **`tools` and `resources` are MCP terms of art in this posting**, not the
  generic English words. Neither appears in the document in any sense.

## Gate 3 — Human scan: 88/100

| # | Check | Points | Finding |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 8 / 15 | The posting's title is `Full Stack Software Engineer`. The string `full stack` appears **nowhere** in the document. What sits at non-blank line 4, inside the top 15%, is `I am a Senior Software Engineer`. `Entry-level Fullstack Software Engineer` occurs at line 54, one word and far outside the top band. Partial credit: a senior engineering title is prominent. **This is capped, not fixable.** CLAUDE.md rules 1 and 4 forbid adjusting a title to fit a posting, and `Senior Software Engineer` is the verified LinkedIn title. |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 15 / 20 | The agent bullet is correctly promoted to DexCare position 1, and the TypeScript services bullet is position 2. Position 3 is the Epic EMR bullet, which is healthcare domain and carries no posting token. The `Auth0 JWT and OpenAPI/Swagger input validation` bullet, which places two required QA tokens, sits at position 4. |
| 3.3 | Past-tense action verb and an outcome, no present tense, no `Responsible for` | 15 / 15 | All 16 bullets open with a past-tense verb, subject omitted: `Built` (x7), `Integrated`, `Modeled`, `Reduced`, `Helped`, `Moved`, `Deployed`, `Processed`, `Led`, `Developed`. Zero occurrences of `Responsible for`. Summary uses first person with `I`, per CV-SPEC. |
| 3.4 | At least 3 bullets carry a real number | 15 / 15 | Seven do: 15%, 25%, 7%, 33%, 20%, 18%, 26%. All seven trace to the metrics Lucas supplied in `DOSSIER.md` 2026-09-01. |
| 3.5 | Experience completeness against the base | 10 / 10 | `resumes/base-en.tex` carries 16 Experience bullets (DexCare 7, Luizalabs 4, Lippaus mid 3, Lippaus entry 2). The tailored file carries the same 16 in the same distribution. No bullet, role or metric removed. One page. |
| 3.6 | No unsupported buzzwords | 10 / 10 | Zero hits for `team player`, `results-driven`, `passionate`, `self-starter`, `detail-oriented`, `synerg`. |
| 3.7 | Skills grouped by category | 10 / 10 | Seven labelled groups: `Languages`, `Backend`, `Data`, `Frontend`, `Cloud and operations`, `Testing and security practices`, `AI tooling`. Not a wall. |
| 3.8 | Scannable | 5 / 5 | One page. Bold role headers in an embedded Roboto-Bold subset. Section rules. Consistent role-header shape across all four blocks. |

Total: **88 / 100**. Reported, not blocking.

## Unsupported claims found

Audited against `DOSSIER.md` as the only claim source, per this dispatch.

1. **`with production ownership` in the Summary.** Added by the tailoring; the
   base Summary reads `TypeScript, Node.js, React, and Go systems` with no
   ownership clause. `DOSSIER.md` does not record the phrase, and the DexCare
   section records the opposite state: *"Still needed from Lucas: scale numbers
   (RPS, patient volume, latency, team size) and **which of these he personally
   owned versus used**."* Ownership is an open dossier question, so the Summary
   asserts as fact something the dossier marks unresolved. Reported, not fixed.
   Lucas can close it by answering that question in `DOSSIER.md`.

No other tailored delta is unsupported. The following were checked and are
supported:

- `OpenAPI/Swagger input validation` — `DOSSIER.md` records
  `express-openapi-validator` under API contracts. Request validation against an
  OpenAPI schema is input validation.
- `S3, RDS, and Secrets Manager through AWS SDK v3 for storage and secrets
  handling` — `DOSSIER.md` records `AWS SDK v3 — S3, STS, Secrets Manager, RDS
  Signer`.
- `Deployed services as containers with Docker and Kubernetes` — `DOSSIER.md`
  records Docker and Kubernetes at Luizalabs.
- `Vitest and Jest test automation gating CI/CD` — Vitest and Jest are in the
  dossier tool list; the `gating CI/CD` phrasing is inherited unchanged from
  `base-en.tex`, not introduced by this tailoring.
- `Agent rules and enforcement` in Skills — `DOSSIER.md` records *"Built the
  agent environments: shared rules, codebase enforcement (lint, cyclomatic
  complexity limits, testing)"*.
- `Claude Code`, `Codex`, `Agentic workflows` — recorded in `DOSSIER.md` as the
  approved AI skills token set.
- `Node.js, Java, and Go` at Luizalabs — `DOSSIER.md` records `Node, Java, and
  others` plus `Go at Luizalabs`.

Confirmed absent, correctly: zero occurrences of `Ruby`, `Rails` or any
claim-status marker in the `.tex` or the extraction.

### Claims the document correctly did NOT make

The dispatch named eight areas not to infer from adjacent facts. The Architect
inferred none of them. Verified by grep on the raw extraction: `Anthropic` 0,
`Messages API` 0, `MCP` 0, `Model Context Protocol` 0, `tool use` 0, `function
calling` 0, `OWASP` 0, `Azure` 0, `IaC` 0, `code review` 0. Daily Claude Code
use was not stretched into Anthropic Messages API, MCP, tool use or prompt
engineering. ArgoCD was not relabelled as IaC. This is the correct behaviour and
it is why Gate 2 scores 39 rather than higher.

## Defects, ranked by cost

1. **Gate 1, minimum years — `6+ years` required, 5 years 6 months verified.**
   The Summary states `5+ years`. **No document fix exists and none may be
   attempted.** LinkedIn shows employment beginning `Mar 2021`; CLAUDE.md rule 4
   forbids changing dates to improve a match. This is a Maestro and Lucas
   decision: apply with a 6-month gap and address it in the screening answers,
   or drop the posting. Quill already flagged it.

2. **Gate 1 and Gate 2, the MCP and Anthropic requirement cluster is entirely
   absent** — `MCP`, `MCP servers`, `tools`, `resources`, `Anthropic Messages
   API`, `tool use`, `function calling`, `prompt engineering`, `skill
   engineering`. Nine required tokens at 0 points. The posting builds its whole
   role around these: *"designing and maintaining MCP (Model Context Protocol)
   integrations"*, *"Design, build and secure MCP servers/clients"*, *"Define
   tool schemas"*. **Do not fix by writing.** `DOSSIER.md` supports none of it.
   The only legitimate route is Lucas adding real MCP and Anthropic API facts to
   `DOSSIER.md`; if he has none, the correct outcome is that this posting does
   not match.

3. **Gate 2, `code review` absent** — 0 points. Required by the posting:
   *"code review at scale"*, and the role is *"acting as the final authority on
   code quality"*. `DOSSIER.md` records no code-review fact, so the Architect
   was right to leave it out. **Observation for Lucas, not an instruction to the
   Architect:** the LinkedIn Luizalabs entry, read today, contains *"Improved
   code review quality by introducing structured review practices and clearer
   pull-request documentation, reducing average review cycles from 3-4 rounds to
   1-2."* That is on the profile but **not in `DOSSIER.md`**, and this dispatch
   makes `DOSSIER.md` the only claim source. If Lucas confirms it into the
   dossier, `code review` becomes placeable and this defect closes. Until then
   it stays a FAIL and the Architect must not use it.

4. **Gate 2, `OWASP` absent** — 0 points. Posting: *"security-minded (OWASP,
   secrets handling, input validation)"*. The sibling tokens `secrets handling`
   and `input validation` both score 3; only `OWASP` is missing. No dossier
   support. Not fixable by writing.

5. **Gate 2, `IaC` absent** — 0 points. Posting: *"containers, CI/CD, IaC"*.
   `containers` and `CI/CD` both score 3. Quill's reasoning is correct and
   should stand: ArgoCD is GitOps continuous delivery, not infrastructure-as-code
   tooling, and claiming `IaC` from it would be an inference. Not fixable by
   writing.

6. **Gate 2, `production ownership` scores 0 and is simultaneously an
   unsupported claim.** It sits in the Summary, which earns no placement points
   under the rubric, so it buys nothing for retrieval while asserting something
   `DOSSIER.md` records as an open question. **Fix, if Lucas confirms ownership:
   answer the open dossier question, then place the token in Skills and in one
   DexCare Experience bullet where it earns 3 points. Fix, if he does not:
   delete `with production ownership` from the Summary line
   `I am a Senior Software Engineer with 5+ years building TypeScript/Node,
   React, and Go systems with production ownership.`** The Architect decides
   only after Lucas answers. This is the one Gate 2 zero the team controls.

7. **Gate 3.2, bullet ordering inside DexCare** — 15/20. **Fix: swap DexCare
   bullet 3 and bullet 4.** Move
   `Built multi-tenant REST APIs with Auth0 JWT and OpenAPI/Swagger input
   validation ...` into position 3 and
   `Integrated Epic EMR time-slot flows ...` into position 4. The QA and
   security bullet carries two required tokens and matches the posting's
   *"Quality assurance & code stability"* section; the Epic EMR bullet carries
   none. No fact changes, no bullet is removed, so CLAUDE.md 9.1 is respected.

8. **Gate 3.1, posting title absent** — 8/15. **No fix. Do not act on this.**
   Recorded so the score is explainable. Inserting `Full Stack Software
   Engineer` would violate CLAUDE.md rule 1, which binds titles to LinkedIn, and
   rule 4, which forbids adjusting a title to fit a posting.

## Match limits

Preferred tokens not placed, 14 of 14: `Multi-agent`, `planner`, `executor`,
`critic`, `human-in-the-loop`, `LLM evaluation`, `evals`, `golden datasets`,
`regression testing`, `token management`, `cost management`, `Jira`,
`Confluence`, `spec-first`. None is supported by `DOSSIER.md`.

Structural limit: this posting's required qualifications are roughly half
generic full-stack, which the document covers at 3 points per token, and half
agentic-AI platform engineering, which `DOSSIER.md` does not evidence at all.
Twelve of the fourteen missing required tokens are unreachable by any amount of
rewriting. Two are reachable: `production ownership` if Lucas answers the open
dossier question, and `code review` if he confirms the LinkedIn Luizalabs claim
into `DOSSIER.md`. Even with both closed, Gate 2 would reach only 61/100 and
would still FAIL the required-token rule, and Gate 1 would still fail on the
6-year minimum.

Not observable, recorded rather than guessed: the target ATS and its parser,
company origin, employment label, and the external apply destination. The
posting is Easy Apply with no external destination shown.
