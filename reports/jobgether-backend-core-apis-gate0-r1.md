# ATS Analysis — jobgether-backend-core-apis-en.pdf / -pt.pdf vs jobgether-backend-core-apis
Segment: agency   Date: 2026-09-01   Round: fix round 1 re-gate

Posting: Backend Engineer, Core APIs — Jobgether (on behalf of a partner).
https://www.linkedin.com/jobs/view/4460256096/
Captured verbatim in `jobs/jobgether-backend-core-apis.md`. Every requirement
below is quoted from that file. Nothing is inferred.

Baseline for comparison: `reports/jobgether-backend-core-apis-gate0.md`.
Architect's change log: `reports/jobgether-backend-core-apis-draft.md`,
section "Fix round 1".

Extractions regenerated for this run:
```
pdftotext -layout jobgether-backend-core-apis-{en,pt}.pdf -> *.layout.txt
pdftotext         jobgether-backend-core-apis-{en,pt}.pdf -> *.raw.txt
```
Gate 0 and Gate 2 are judged on the raw files. The round-0 extraction files
were overwritten by this run, so I cannot diff round 0 against round 1 at the
extraction level. Every round-0 number quoted below is quoted from the round-0
report, not re-measured.

## Verdict

| Gate | EN round 0 | EN round 1 | PT round 0 | PT round 1 |
|---|---|---|---|---|
| Gate 0 — Parse integrity | PASS (4 header-only FAILs, accepted exception) | **PASS** (same 4 header-only FAILs) | PASS | **PASS** |
| Gate 1 — Knockouts | PASS | **PASS** | PASS | **PASS** |
| Gate 2 — Retrieval coverage | 9 / 100 | **11 / 100** | 5 / 100 | **10 / 100** |
| Gate 3 — Human scan | 90 / 100 | **93 / 100** | 90 / 100 | **93 / 100** |

**Not blocked.** Both documents parse, both are one page, every title and date
matches LinkedIn character for character, no Ruby or Rails token appears, no
`[UNVERIFIED]` marker ships.

Gate 2 moved 24 -> 26 raw EN and 20 -> 25 raw PT. The reported score moved less
because a **new** stuffing penalty appeared. Read the Gate 2 penalty section
before reacting to the number.

---

## Gate 0 — Parse integrity

Both PDFs confirmed **1 page** (`pdfinfo`). `pdfimages -list` returns zero rows
in both. Zero NUL bytes, zero U+FFFD, zero U+FB00-FB06 ligature glyphs, zero
literal `?` in either raw extraction (measured with Python over the raw files).

| # | Check | EN | PT | Evidence, round 1 |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | PASS | Raw extraction is complete prose, 76 lines EN / 78 PT |
| 0.2 | Glyph integrity | PASS | PASS | `grep -oic`: `workflow` EN 4 / PT 3, `office` EN 2 / PT 2. `profile`, `efficient`, `conflict` do not occur in either document, so they are untestable here, not failures. Zero ligature glyphs measured directly. `\defaultfontfeatures{Ligatures=NoCommon}` at `en.tex:16` / `pt.tex:16` |
| 0.3 | Contact block recoverable | PASS | PASS | Raw line 3, in the body, not a header. EN: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. PT identical except `Brasil`. City, phone, email, LinkedIn all present. No UTC offset in either |
| 0.4 | Section headers verbatim | PASS | PASS | EN raw: `SUMMARY` (5), `SKILLS` (10), `EXPERIENCE` (19), `EDUCATION` (69). PT raw: `RESUMO` (5), `HABILIDADES` (11), `EXPERIÊNCIA` (20), `FORMAÇÃO` (71). Uppercase rendering allowed by Gate 0.4 |
| 0.5 | Employment-block segmentation | FAIL — header only | FAIL — header only | Raw splits each role header into 4 lines, e.g. EN 20-24: `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remote`. **No two roles merge. No role splits into two employment entries.** Four employment blocks plus Education, all intact. Cause is the `tabular*` at `en.tex:41` / `pt.tex:41` |
| 0.6 | Date parseability | FAIL — header only | FAIL — header only | Dates sit two lines below the title in the raw stream, not on it. Format `Mon YYYY - Mon YYYY` with ASCII hyphen is correct in all five blocks |
| 0.7 | Reading order | FAIL — header only | FAIL — header only | Word-level `diff` of raw vs layout returns **5 hunks in EN and 5 in PT. All ten are the italic title line of a role or education header.** Zero content blocks reorder |
| 0.8 | No forbidden constructs | FAIL — header only | FAIL — header only | `tabular*` role header at `en.tex:41` / `pt.tex:41`. No table elsewhere, no text box, no image of text, no icon, no photo. `pdfimages -list` returns zero rows |

**All four FAILs trace only to the two-column role header.** That is the
accepted exception in `CV-SPEC.md` item 2 and `RUBRIC.md` "Accepted exception,
set by Lucas 2026-09-01". Reported, not blocking. No other cause of 0.5-0.8
exists in either document. Unchanged from round 0.

### LinkedIn ground-truth cross-check — PASS

Read off the round-1 raw extractions, against the `DOSSIER.md` **LinkedIn
ground truth** block.

| Block | Raw lines EN / PT | Resume text | LinkedIn ground truth | Match |
|---|---|---|---|---|
| 1 | 20-23 / 21-24 | `DexCare` / `Senior Software Engineer` / `Jan 2026 - Present` | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | 38-41 / 40-43 | `Luizalabs` / `Mid-level Software Engineer` / `Jan 2024 - Jan 2026` | identical | YES |
| 3 | 50-53 / 52-55 | `Lippaus Distribuidora` / `Mid-level Software Engineer` / `Jan 2023 - Jan 2024` | identical | YES |
| 4 | 60-63 / 62-65 | `Lippaus Distribuidora` / `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023` | identical | YES |
| Education | 70-73 / 72-75 | `FAESA` / `Bachelor's degree, Information Systems` / `Feb 2022 - Dec 2025` | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — periods identical; ASCII hyphen per CV-SPEC item 5 |

Both Lippaus roles remain present and separate. The promotion is preserved.
**No Gate 0 FAIL from the ground-truth check.** Unchanged from round 0.

The PT file keeps the English date word `Present` (`pt.tex:78`). Correct under
CLAUDE.md rule 1: dates identical to LinkedIn.

### Forbidden-token grep

```
grep -rniE 'ruby|rails|unverified' jobgether-backend-core-apis-en.tex jobgether-backend-core-apis-pt.tex
grep -rniE 'ruby|rails|unverified' jobgether-backend-core-apis-{en,pt}.{raw,layout}.txt
```
**Zero hits.** Both greps exit 1. No `[UNVERIFIED]` marker ships in this package.

### Page count

`pdfinfo` reports `Pages: 1` for both PDFs. **Confirmed, one page each.**

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred. Unchanged verdict.

| Check | Posting source (verbatim) | Result |
|---|---|---|
| Work authorization / entity type | "Candidates must be authorized to work from their home location; visa sponsorship is not provided." Location label: "Brazil (Remote)" | **PASS** — resume states `Vitória, ES, Brazil` as the home location. The resume nowhere states work authorization in words; it is carried by the location line alone |
| Location | "Our partner is looking for a Backend Engineer, Core APIs based in Brazil." | **PASS** — `Vitória, ES, Brazil` (EN), `Vitória, ES, Brasil` (PT) |
| Time-zone overlap | Not stated. The posting says "globally distributed", "highly asynchronous environment". The capture file records "no overlap window stated" | **not stated** — and, after fix 16, the resume no longer states any overlap. See the note below |
| Minimum years of experience | "2+ years of professional backend software development experience" | **PASS** — Mar 2021 to Sep 2026 = 5 yr 6 mo from the LinkedIn dates. Summary states `5+ years` |
| English proficiency | "Strong communication skills in English, with the ability to collaborate effectively across a globally distributed and asynchronous team." | **PASS** — EN Summary: `Works in Advanced/C1 English.` PT Summary: `Trabalha em inglês Advanced/C1 (English).` Backed by `DOSSIER.md` [FACT] |
| Degree requirement | Not stated in the posting | **not stated** |

Note on time-zone, stated so nobody is surprised later: RUBRIC Gate 1 says an
absent overlap statement is a FAIL **in postings that gate on overlap**. This
posting gates on the opposite; it asks for asynchronous work. So removing
`US-hours overlap` (fix 16) costs nothing here and removes an unverified claim.
It does remove the only overlap signal from the document. If the partner
company later gates on overlap, the exposure is real and it is Lucas's call.

Required-skill presence, verbatim in the round-1 EN raw extraction:

| Required skill (posting's words) | Round 0 | Round 1 |
|---|---|---|
| `Go and/or Node.js` | YES, both | **YES, both.** `Go` 3 word-boundary occurrences, `Node.js` 3 |
| `scalable backend systems` | YES | **YES**, Summary line 6, verbatim phrase |
| `APIs`, `microservices` | YES, both | **YES**, both |
| `real-time data-processing services` | PARTIAL, `data processing` absent | **YES.** Line 26: `Deliver real-time data processing over DynamoDB Streams` |
| `SQL` | YES | **YES**, 3 standalone occurrences |
| `DynamoDB, Redis, or Elasticsearch` | YES (OR satisfied) | **YES**, unchanged. Elasticsearch still absent; the OR is satisfied |
| `Git` | NO | **NO.** The only `git` string is still inside `github.com/queirozlc` |
| `IDEs` | NO | **NO** |
| `shell scripting` | NO | **NO** |
| `CI/CD workflows` | YES | **YES**, 2 occurrences |
| `performance tuning`, `debugging` | NO, neither | **NO, neither** |
| `testing`, `reliability improvements` | stems only | **`reliability` now verbatim** (line 46). `testing` still only as `Testing` in Skills |

**Gate 1 verdict: PASS. No knockout FAIL in either language.** Same as round 0.

---

## Gate 2 — Retrieval coverage: EN 11 / 100, PT 10 / 100

### Method, identical to round 0

Restated so the two rounds are comparable. All five conventions from the
round-0 report are carried forward unchanged:

1. `required` = the posting's **Requirements** section. `preferred` = every item
   marked "is a plus", "is beneficial", "is preferred", "is an advantage", or
   "highly valued".
2. Soft skills discarded per RUBRIC Gate 2 Step 1.
3. `Elasticsearch` is **not scored**; DynamoDB and Redis satisfy the posting's OR.
4. `on-call`, `mentoring`, `cross-functional` sit in **Accountabilities**, not
   Requirements. Scored at Gate 3, listed here as uncovered.
5. Tier convention for placements the rubric table does not name: a token in an
   Experience bullet in context but absent from Skills scores 3; a token in the
   Summary only scores 4.

**Ceiling, unchanged.** The rubric's formula divides an unweighted numerator by
a weighted denominator. With 21 required and 17 preferred tokens, a perfect
document computes `100 * (84 + 68) / (252 + 68) = 47.5`, not 100. **47.5 is the
ceiling of this gate for this posting**, before penalties. This is a rubric
arithmetic defect, not a document defect. I apply the formula as written for
comparability and flag it rather than change it unilaterally.

### English — required tokens (weight 3)

| # | Token | Placement, round 1 | R0 | R1 |
|---|---|---|---|---|
| 1 | `Go` | Skills 11, Exp Luizalabs b1 line 44, **Summary line 7** | 3 | **4** |
| 2 | `Node.js` | Skills 11, Exp DexCare b1 line 26, Summary 7 | 4 | 4 |
| 3 | `backend` | Skills group label 12, Exp 26 `backend services`, Summary 6 `scalable backend systems` | 4 | 4 |
| 4 | `APIs` | Skills 12, Exp 26, Summary 6 | 4 | 4 |
| 5 | `microservices` | Skills 12 `Microservices`, Exp 44, Summary 6 | 4 | 4 |
| 6 | `real-time` | Exp 26, Summary 7. Not in Skills | 4 | 4 |
| 7 | `data processing` | **Exp 26** `real-time data processing over DynamoDB Streams`. Not in Skills, not in Summary | 0 | **3** |
| 8 | `SQL` | Skills 13, Exp 30, Summary 7 | 4 | 4 |
| 9 | `DynamoDB` | Skills 13, Exp 26 `DynamoDB Streams`, Summary 7 | 4 | 4 |
| 10 | `Redis` | Skills 13, Exp 30, Summary 7 | 4 | 4 |
| 11 | `Git` | **Absent.** Only inside `github.com/queirozlc` | 0 | 0 |
| 12 | `IDEs` | **Absent** | 0 | 0 |
| 13 | `shell scripting` | **Absent** | 0 | 0 |
| 14 | `CI/CD` | Skills 15, Exp 46 | 3 | 3 |
| 15 | `English` proficiency | Summary 8 `Advanced/C1 English` | 4 | 4 |
| 16 | `2+ years` backend | Summary 6 `5+ years` | 4 | 4 |
| 17 | `performance tuning` | **Absent** | 0 | 0 |
| 18 | `debugging` | **Absent** | 0 | 0 |
| 19 | `testing` | Skills 16 `Testing: Vitest \| Jest`; Exp 35 `tests`, 46 `Vitest, Jest` | 3 | 3 |
| 20 | `reliability` | **Exp 46 verbatim**, `production-grade service reliability`. Not in Skills, not in Summary | 3 (stem) | 3 |
| 21 | `production-grade` | **Exp 46 verbatim**. Not in Skills, not in Summary | 3 (stem) | 3 |

Required subtotal: **59** (round 0: 55). Denominator `4 * 3 * 21 = 252`.

Rows 20 and 21 gained exactness, not points. The round-0 report already awarded
3 for the stems `reliable` and `production`. Fix 9 replaced the stems with the
posting's exact words, which is the correct outcome for a lexical retrieval
gate even though the tier does not move.

### English — preferred tokens (weight 1)

| # | Token | Placement, round 1 | R0 | R1 |
|---|---|---|---|---|
| 1 | `Terraform` | Absent | 0 | 0 |
| 2 | `AWS CloudFormation` | Absent | 0 | 0 |
| 3 | `TypeScript` | Skills 11, Exp 26, Summary 6 | 4 | 4 |
| 4 | `Express` | Skills 12, Exp 27 | 3 | 3 |
| 5 | `ClickHouse` | Absent | 0 | 0 |
| 6 | `dbt` | Absent | 0 | 0 |
| 7 | `Snowflake` | Absent | 0 | 0 |
| 8 | `BigQuery` | Absent | 0 | 0 |
| 9 | `Redshift` | Absent | 0 | 0 |
| 10 | `Databricks` | Absent | 0 | 0 |
| 11 | `Datadog` | Skills 15, Exp 31 | 3 | 3 |
| 12 | `logging` | Exp 32 `browser logging`. Not in Skills | 3 | 3 |
| 13 | `telemetry` | Absent | 0 | 0 |
| 14 | `Docker` | Skills 15, Exp 46 | 3 | 3 |
| 15 | `Kubernetes` | Skills 15, Exp 46 | 3 | 3 |
| 16 | both `Go` and `Node.js` in a backend context | Both now in Skills, Experience **and Summary** (line 7). Still in different roles: Node.js at DexCare, Go at Luizalabs | 3 | **4** |
| 17 | `security` / `privacy` mechanisms | `security` now verbatim in the Skills group label 12, `Backend and Multi-tenant security`. **`security` appears nowhere in Experience; `privacy` appears nowhere at all.** Skills-only tier | 1 | 1 |

Preferred subtotal: **24** (round 0: 23). Denominator `4 * 1 * 17 = 68`.

Row 17 is the one fix that did not pay. Fix 10 put the word in Skills, which is
the 1-point tier. To reach 3 the word `security` must also appear inside an
Experience bullet.

```
coverage_en = 100 * (59 + 24) / 320 = 100 * 83 / 320 = 25.94 -> 26   (round 0: 24)
```

### Stuffing penalty — English

| Trigger | Token | R0 | R1 |
|---|---|---|---|
| 4 or more occurrences | `APIs` | -5 | **0 — cleared.** 3 occurrences: Summary 6, Skills 12, Exp 26. Fix 1 works |
| In Skills, no Experience support | `RabbitMQ` (`en.tex:67`) | -5 | -5 |
| In Skills, no Experience support | `AMQP` (`en.tex:67`) | -5 | -5 |
| 4 or more occurrences | `React` | 0 | **-5 — NEW.** See below |

I re-checked all 35 Skills tokens against Experience. `RabbitMQ` and `AMQP`
remain the only two without support. `React Native`, added by fix 11, **is**
supported at line 57.

Occurrence counts, round 1 EN: `Core APIs` 3, `APIs` 3, `TypeScript` 3,
`Node.js` 3, `Go` 3, `SQL` 3, `PostgreSQL` 3, `Redis` 3, `DynamoDB` 3,
`BullMQ` 3, `backend` 3, `microservices` 3, `multi-tenant` 3,
`agentic workflows` 3, `real-time` 2, `Express` 2, `Koa` 2, `Docker` 2,
`Kubernetes` 2, `Datadog` 2, `CI/CD` 2, **`React` 4**.

```
Gate 2 EN = 26 - 15 = 11 / 100   (round 0: 9)
```

#### The new `React` penalty is a counting artifact. Read this before acting.

The round-0 report counted `React` at 3 by counting the **string** `React`,
which includes the `React` inside `React Native`. Fix 11 added `React Native`
to the Frontend Skills group, so under that same counting the string now
occurs 4 times: Skills `React` (14), Skills `React Native` (14), Exp `React`
(31), Exp `React Native` (57). That crosses the RUBRIC Step 4 threshold and
the CV-SPEC "cap any term at 3 appearances" rule.

Under **distinct-token** counting, `React` occurs twice and `React Native`
occurs twice, and no penalty applies. Then:

```
Gate 2 EN, distinct-token counting = 26 - 10 = 16 / 100
Gate 2 PT, distinct-token counting = 25 - 10 = 15 / 100
```

I report the string-counting number as the headline so the two rounds stay
comparable, and I state both. **I do not decide which is correct. That is a
rubric question for Lucas.** React is not a posting token for this requisition,
so the practical cost of either reading is small.

### Portuguese — 10 / 100

Same token list, same posting, scored on
`jobgether-backend-core-apis-pt.raw.txt`. The posting is written in English, so
the English token is what retrieval matches. Fix 19 placed an English gloss
beside the Portuguese wording. Seven rows moved:

| Token | R0 | R1 | Round-1 evidence |
|---|---|---|---|
| `real-time` | 0 | **4** | Summary 8 `em tempo real (real-time)`, Exp 27 `(real-time data processing)` |
| `microservices` | 3 | **4** | Skills 13 `Microservices`, Summary 7 `microsserviços (microservices)`. **Experience still carries only `microsserviços`** (line 46) |
| `testing` | 1 | 1 | Skills 17 `Testes (Testing)`. The English token is still Skills-only; Experience carries `testes` |
| `reliability` | 0 | **3** | Exp 48 `confiabilidade (reliability)` |
| `production-grade` | 0 | **3** | Exp 48 `serviços production-grade` |
| `English` | 3 | **4** | Summary 9 `inglês Advanced/C1 (English)` |
| `2+ years` | 3 | **4** | Summary 6 `mais de 5 anos (5+ years)` |
| `data processing` | 0 | **3** | Exp 27 `(real-time data processing)` |
| `Go` | 3 | **4** | Skills 12, Exp 46, Summary 7 |

PT required subtotal: **57** (round 0: 40). PT preferred subtotal: **24**,
identical to EN; every preferred token that scores is an untranslated proper
name, plus the `Go`+`Node.js` Summary row and the `security` Skills label.

```
coverage_pt = 100 * (57 + 24) / 320 = 100 * 81 / 320 = 25.31 -> 25   (round 0: 20)
Gate 2 PT   = 25 - 15 = 10 / 100                                     (round 0: 5)
```

Same three penalties as EN: `RabbitMQ` -5, `AMQP` -5, `React` -5. `APIs` is at
3 in PT as well and its penalty is cleared.

I award `microservices` 4 in PT on the Skills-plus-Summary placement. Note the
generosity honestly: the rubric tier that reaches 4 assumes an Experience
placement underneath, and PT Experience does not have one. Round 0 was
generous in the same direction, awarding 3 for a Skills-only placement, so the
two rounds stay comparable. If the tier is read strictly, PT loses 3 points and
lands at 9 / 100.

### Required tokens still not covered

Absent from both documents, unchanged from round 0:

1. `Git` — required. Present only as a substring of `github.com`. Fix 2 not applied.
2. `IDEs` — required.
3. `shell scripting` — required. Fix 8 not applied, escalated.
4. `performance tuning` — required. Fix 7 not applied, escalated.
5. `debugging` — required. Fix 7 not applied, escalated.

Now covered, previously missing: `data processing`, `reliability` (verbatim),
`production-grade` (verbatim), and in PT `real-time`, `English`, `5+ years`.

Preferred tokens still not covered:

6. `Terraform`, `AWS CloudFormation`, `ClickHouse`, `dbt`, `Snowflake`,
   `BigQuery`, `Redshift`, `Databricks`, `telemetry` — none appears in
   `DOSSIER.md`. The Maestro brief already names most as gaps.
7. `privacy` — absent. `security` reaches Skills only.

Accountability tokens not covered, not scored at Gate 2 (convention 4):

8. `on-call` — absent from both. No on-call evidence in `DOSSIER.md`.
9. `mentor` / `mentoring` — absent from both. No mentoring evidence.
10. `cross-functional` — absent from both.

Requirement satisfied by an alternative, no action needed:

11. `Elasticsearch` — absent, but the posting's OR is met by DynamoDB and Redis.

---

## Gate 3 — Human scan: 93 / 100 (EN and PT)

| # | Check | R0 | R1 | Basis |
|---|---|---|---|---|
| 3.1 | Target title in the top 15% | 12 / 15 | **13** / 15 | The round-0 3-point dock had two causes. **Cause b is resolved:** the Summary now writes `Core APIs` capitalized (raw line 6), matching the posting title and the Skills line. Fix 14 works. **Cause a remains:** the posting's title noun `Backend Engineer` never appears as a phrase in either document. Dock 2 |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 16 / 20 | 16 / 20 | DexCare b1 (real-time data processing, DynamoDB Streams, Core APIs, TypeScript, Node.js, Express, Koa), b2 (Auth0 JWT, OpenAPI/Swagger, multi-tenant), b3 (SQL, PostgreSQL, DynamoDB, Redis, AWS) are the three the posting weights highest, and they are first. b1 is now stronger than in round 0. **Unchanged dock of 4:** no bullet anywhere carries mentoring, on-call or cross-functional signal, all three named Accountabilities, and `Go` is still absent from the current role |
| 3.3 | Every bullet leads with an outcome or action verb | 15 / 15 | 15 / 15 | All 16 EN bullets lead with a bare verb: Deliver, Cut, Serve, Lower, Reduce, Enable, Decrease, Delivered, Improved, Improved, Cut, Increased, Built, Turned, Supported, Delivered. Zero "Responsible for". Present tense for the current role, past for prior roles |
| 3.4 | At least 3 bullets carry a real number | 15 / 15 | 15 / 15 | Seven do: 25%, 7%, 15%, 33%, 20%, 18%, 26%. All trace to the `DOSSIER.md` metric list, IDs D2, D3, D5, D7, L2, L3, P2 |
| 3.5 | Length: 1 page under 10 years | 10 / 10 | 10 / 10 | `pdfinfo` confirms `Pages: 1` for both |
| 3.6 | No unsupported buzzwords | 10 / 10 | 10 / 10 | No "team player", "results-driven", "passionate". Nothing comparable found |
| 3.7 | Skills grouped by category | 8 / 10 | **10** / 10 | Both round-0 causes resolved. Fix 11: `Frontend: React \| React Native` is no longer a one-item group. Fix 12: the fused label is split into `Testing: Vitest \| Jest` and `AI tooling: Claude Code \| Codex \| Agentic workflows`. Seven labeled groups, still one page |
| 3.8 | Scannable | 4 / 5 | 4 / 5 | **Fix 13 did not take effect. Measured, not assumed.** `pdftotext -bbox` on the EN PDF: bullet glyph `•` xMin `57.599`, first word `Deliver` xMin `62.827`, continuation word `services` on the next line xMin `57.599`. The continuation line is flush with the bullet glyph, not with the bullet text. PT is identical: `Entrega` xMin `62.827`, continuation `TypeScript` xMin `57.599`. Five bullets wrap in EN, six in PT. Dock 1 stands |

```
Gate 3 EN = 13 + 16 + 15 + 15 + 10 + 10 + 10 + 4 = 93 / 100
Gate 3 PT = same structure, same defects, one extra wrapped bullet = 93 / 100
```

Unscored, resolved: fix 15 worked. Round 0 recorded four of seven DexCare
bullets opening with `Reduce`. Round 1 EN opens with Deliver, Cut, Serve,
Lower, Reduce, Enable, Decrease; PT with Entrega, Corta, Atende, Diminui,
Reduz, Habilita, Mitiga. One repeat each.

---

## Fix round 1 — resolution of the 19 defects

**11 resolved. 1 partial. 7 not resolved. 1 new defect.**

| # | Defect | Status | Evidence |
|---|---|---|---|
| 1 | `APIs` at 4 occurrences | **RESOLVED** | `APIs` now 3 in both raw files. `multi-tenant APIs` is now `multi-tenant services` (EN raw 28-29, PT raw 29-30). -5 penalty cleared |
| 2 | `Git` absent | **NOT RESOLVED** | Only `github.com/queirozlc`. Not attempted in round 1. Required token, weight 3, still scoring 0 |
| 3 | `RabbitMQ` / `AMQP` unsupported in Skills | **NOT RESOLVED** | Still `en.tex:67` / `pt.tex:67` with no Experience bullet. -10 stands. **Lucas's decision, correctly not taken by the Architect** |
| 4 | `data processing` absent | **RESOLVED** | EN raw 26 `Deliver real-time data processing over DynamoDB Streams for Core APIs`. PT raw 27. Token 0 -> 3 in both. No new claim: DynamoDB Streams and event-driven services are FACT-OBSERVED |
| 5 | `Go` not in Summary | **RESOLVED** | EN raw 7 `with Go used at Luizalabs`, PT raw 7 `com uso de Go na Luizalabs`. Correctly scoped to recorded use, not depth. Token 3 -> 4, and the preferred `Go`+`Node.js` row 3 -> 4 |
| 6 | `Go` in no DexCare bullet | **NOT RESOLVED** | Correct. `DOSSIER.md` records no Go at DexCare. **Question for Lucas** |
| 7 | `performance tuning`, `debugging` absent | **NOT RESOLVED** | Correct. No DOSSIER evidence. **Question for Lucas** |
| 8 | `shell scripting` absent | **NOT RESOLVED** | Correct. No DOSSIER evidence. **Question for Lucas** |
| 9 | `reliability`, `production-grade` as stems only | **RESOLVED** | EN raw 46 `Improved production-grade service reliability by deploying Docker and Kubernetes on GCP through ArgoCD and using Vitest, Jest, and CI/CD.` PT raw 48. Both tokens verbatim. Tier unchanged at 3; exactness gained |
| 10 | `security` / `privacy` absent | **PARTIAL** | `security` now in the Skills group label, `Backend and Multi-tenant security` (`en.tex:67`, `pt.tex:67`). The word reaches Skills only, which is the 1-point tier. **Gate 2 row unchanged at 1.** `privacy` still absent everywhere |
| 11 | `Frontend: React` one-item group | **RESOLVED at Gate 3.7** | `Frontend: React \| React Native`, supported at EN raw 57. **Introduced new defect N1**, see below |
| 12 | `Testing and AI tooling` fused | **RESOLVED** | Split into two groups, EN raw 16-17, PT raw 17-18. Still one page |
| 13 | No hanging indent on wrapped bullets | **NOT RESOLVED** | `\hangindent=1em\hangafter=1` is present in the source at `en.tex:36` / `pt.tex:36`, but **it does not reach the rendered PDF**. Measured with `pdftotext -bbox`: continuation lines start at xMin `57.599`, identical to the bullet glyph, while bullet text starts at `62.827`. Both languages. Gate 3.8 dock of 1 stands |
| 14 | Summary wrote `core APIs` lower case | **RESOLVED** | `Core APIs` capitalized, EN raw 6, PT raw 6. Gate 3.1 +1 |
| 15 | Four DexCare bullets open with `Reduce` | **RESOLVED** | Seven distinct openers in each language. Unscored, cosmetic, done |
| 16 | `US-hours overlap` unverified | **RESOLVED by removal** | The clause is absent from both Summaries. `Advanced/C1 English` retained. Gate 1 verdict unaffected for this posting; see the time-zone note in Gate 1 |
| 17 | "Supported nationwide expansion" unverified | **RESOLVED by removal** | EN raw 57 now reads `Built a multi-tenant web and React Native mobile platform on PostgreSQL.` PT raw 59 equivalent |
| 18 | Both Lippaus roles print `Remote`, LinkedIn records `On-site` | **NOT RESOLVED** | Still `Remote` at `en.tex:102` and `en.tex:111`, `pt.tex` same. **A conflict between two of Lucas's own instructions. Correctly left for him.** I do not resolve it |
| 19 | PT translated seven English retrieval tokens away | **RESOLVED** | All seven now carry an English gloss. PT raw subtotal 40 -> 57. `testing` gained the gloss but not the tier, because PT Experience still carries only `testes` |

### New defects found in round 1

| # | File and line | Defect | What would pass |
|---|---|---|---|
| N1 | `en.tex:69`, `pt.tex:69` | **Fix 11 raised the string `React` to 4 occurrences**, which trips RUBRIC Gate 2 Step 4 and the CV-SPEC "cap any term at 3 appearances" rule under the counting the round-0 report used. Cost: -5 at Gate 2 in both languages | Two options, both cheap. **(a)** Decide that `React` and `React Native` are distinct tokens, in which case no penalty applies and Gate 2 reads EN 16 / PT 15. This is a rubric question, **Lucas's call, not the Architect's.** **(b)** If the string reading stands, drop `React Native` from the Frontend Skills group; it is already evidenced at `en.tex:105`. That reverts Gate 3.7 to 8 / 10 and trades 2 Gate 3 points for 5 Gate 2 points |
| N2 | `pt.tex:55`, `pt.tex:123` | The PT contact line and PT education location print `Vitória, ES, Brasil`. `CLAUDE.md` rule 3 and `CV-SPEC.md` item 3 both write the location as **`Vitória, ES, Brazil`**, and neither states a translation exception for the location. The EN file is correct at `en.tex:55` and `en.tex:123` | **I cannot verify whether round 1 introduced this.** The round-0 extraction files were overwritten by this run and the round-0 report quoted the contact line only once, with `Brazil`. Not a Gate 0 FAIL, since city and country are both recoverable. **Escalate to Lucas:** does the location string translate in the PT document, or is it fixed as `Brazil` in both? |

---

## Claims I could not verify

Listed for Lucas. Not deleted, not defended.

Cleared since round 0, by removal or rewrite:

- `US-hours overlap` — removed from both Summaries.
- `Supported nationwide expansion` — removed from the Lippaus mid-level bullet.
- `for a beverage distribution startup` — removed. EN raw 66 now reads
  `Supported operations by building JavaScript back-office dashboards.`
- `gated by Vitest and Jest in CI/CD` — the gating claim is gone. EN raw 46 now
  says `using Vitest, Jest, and CI/CD`, which matches the DOSSIER "tools used"
  fact exactly.
- `provider availability` — removed. EN raw 30 now reads `Serve booking data by
  modeling SQL data in PostgreSQL...`.

Still open:

1. **Go depth** — `en.tex:66`, `en.tex:94`, and now `en.tex:62` (Summary).
   `DOSSIER.md` confirms Go at Luizalabs [FACT] and records **no depth**. The
   wording is correctly scoped and claims nothing more. Flagged because this
   posting weights Go equally with Node.js and calls experience in both "highly
   valued". Lucas needs to know exactly how thin this is before he applies.
2. **Java depth at Luizalabs** — `en.tex:94`. `DOSSIER.md` records "Node, Java,
   and others" with no depth. Correctly scoped, flagged for the same reason.
3. **Lippaus location `Remote`** — conflicts with the LinkedIn `On-site`
   record. See fix 18.
4. **New in round 1: `Deliver real-time data processing over DynamoDB Streams`**
   — `en.tex:81`, `pt.tex:81`. `DOSSIER.md` records DynamoDB, DynamoDB Streams
   and event-driven booking as FACT-OBSERVED from the repos. It does **not**
   record real-time data processing as an owned delivery in those words. The
   inference is short and reasonable. Flagged, not disputed.
5. **New in round 1: `production-grade service reliability`** — `en.tex:96`,
   `pt.tex:96`. `DOSSIER.md` confirms Docker, Kubernetes, GCP, ArgoCD, Vitest
   and Jest at Luizalabs [FACT]. `production-grade` and `reliability` are
   characterizations of that work, not separately recorded facts. Flagged.
6. **PT location string `Brasil`** — see new defect N2.

Verified and needing no action: every company, title and date against the
LinkedIn ground-truth block; all seven percentage figures (DOSSIER metric IDs
D2, D3, D5, D7, L2, L3, P2); the DexCare stack tokens (FACT-OBSERVED from the
repos on disk); the SPI description and its 33%; `RabbitMQ` and `AMQP` as
Skills-only tokens by Lucas's instruction; `Claude Code`, `Codex` and
`Agentic workflows`; `React Native` at Lippaus; the Magazine Luiza / SEFAZ
fiscal domain; `Advanced/C1` English; the Information Systems degree at FAESA;
the EN contact line with no UTC offset printed.

---

## Analyzer's read, in one paragraph

Round 1 did the honest work available inside the DOSSIER. Eleven of nineteen
defects are closed, and the five that were left open are exactly the five that
should have been: `Git`, `shell scripting`, `performance tuning`, `debugging`
and Go at DexCare have no evidence, and the Architect did not invent any. Raw
Gate 2 coverage moved 24 -> 26 EN and 20 -> 25 PT, with the Portuguese document
gaining most because fix 19 stopped translating the posting's own retrieval
tokens away. Gate 3 moved 90 -> 93 on both. Two things blunt the headline
number. First, the `RabbitMQ` / `AMQP` -10 is still Lucas's own Skills-only
instruction meeting the rubric's stuffing rule; only he can release it.
Second, fix 11 tripped a -5 on `React` under the same string counting round 0
used, which is very likely a counting artifact rather than a real defect, and
resolving that one rubric question is worth 5 points in both languages for
zero edits. Fix 13 is the one claim in the change log that the PDF does not
support: the macro was edited but the hanging indent does not render, and I
measured it rather than trusted it. Everything structural is sound. The gap
between 11/100 and the 47.5 ceiling is now mostly five honest zeros and one
arithmetic question, not a document defect.
