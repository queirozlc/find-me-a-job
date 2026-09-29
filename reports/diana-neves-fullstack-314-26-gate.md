# ATS Analysis — diana-neves-fullstack-314-26-pt.pdf vs diana-neves-fullstack-314-26
Segment: br-pj   Date: 2026-09-02

Judged on extractions the analyzer regenerated from the PDF under test:
`pdftotext -layout` and `pdftotext` on
`resumes/diana-neves-fullstack-314-26-pt.pdf` (28783 bytes, built 2026-09-02
19:30, 1 page, letter). Source cross-read:
`resumes/diana-neves-fullstack-314-26-pt.tex`.
Posting text: `jobs/diana-neves-fullstack-314-26.md` (LinkedIn post
`https://lnkd.in/p/di4pYA8t`, recruiter Diana Neves, code `314-26`, captured by
Kestrel, hunt 2026-09-02-b). Company not stated in the post.
Titles, companies and dates checked against `DOSSIER.md` **LinkedIn ground truth**.
Architect's own marker list read: `reports/diana-neves-fullstack-314-26-draft.md`.

Rule versions applied: `CLAUDE.md` and `RUBRIC.md` as of 2026-09-02.

This is our rubric. It is not a vendor score. No ATS emits these numbers.

## Verdict

**BLOCKED at Gate 1.**

| Gate | Result |
|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, reported not blocking) |
| Gate 1 — Knockouts | **FAIL** — entity type: the post contracts `PJ \| Contrato Indeterminado`, the document states no PJ and no CNPJ |
| Gate 2 — Retrieval coverage | **6 / 100** (26 before a −20 stuffing penalty) |
| Gate 3 — Human scan | **95 / 100** |

This is the best-covered tailoring of the hunt so far. Twenty-three of the
twenty-six required tokens sit in `Skills` **and** in an Experience bullet,
which is exactly what `CLAUDE.md` section 4 asks for and what the Conta
Simples package failed to do. It blocks on one omission that `DOSSIER.md` can
fix today, the same omission the Brivia package took.

Two things need Lucas before this ships, neither of them the Architect's
error to fix alone:

- **`Certificação GCP ou similares` is a stated requirement and Lucas holds
  none.** The document correctly does not claim it. This is a real gap, not a
  document defect, and it needs a screening answer.
- **33 `[UNVERIFIED]` markers print on the page.** That is the process working
  as designed, and it also means the PDF as built is not the PDF that gets
  sent. Lucas confirms or strikes each one first.

---

## Gate 0 — Parse integrity

`pdfinfo` reports **1 page**, letter. Raw extraction is 76 lines.

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Complete prose. Contact block, four sections, four Experience blocks and one Education block all present |
| 0.2 | Glyph integrity | PASS | Measured by codepoint in Python, not by shell grep. Zero `\x00`, zero `U+FB00-FB04` ligature codepoints, zero `U+FFFD`, zero stray `?`. The only character above U+00FF is `U+2022 BULLET`. Ligature-bearing words intact: `fiscais` 1, `fluxos` 1, `funcionalidades` 1, `integrações` 3, `confiáveis` 1, `Distribuidora` 2 |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, not a header or footer: `Vitória, ES, Brasil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email and LinkedIn URL all present. No UTC offset, no time-zone overlap sentence |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 11, 21, 69: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, each a standalone line. PT allowlist, Gate 0.4. Uppercase rendering allowed |
| 0.5 | Employment-block segmentation | FAIL — header only | Raw splits each role header into `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remoto`. **No two roles merge. No role splits into two employment entries.** Four Experience blocks and one Education block, intact and in order. Both Lippaus entries repeat the company name, so the promotion segments unambiguously. Cause is the `tabular*` in `\resumeSubheading` |
| 0.6 | Date parseability | FAIL — header only | Every date sits one blank line below its title. Format correct in all five blocks: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Separator verified by Unicode category `Pd`: the only dash in the document is `U+002D HYPHEN-MINUS` |
| 0.7 | Reading order | FAIL — header only | Raw order per role header: company, title, dates, location. Layout: company+dates, title+location. **Zero content blocks reorder.** The new name block (name, title, contact) reads in the same order in both extractions |
| 0.8 | No forbidden constructs | FAIL — header only | The `tabular*` role header. No table elsewhere, no text box, no image of text, no icon, no photo |

**All four FAILs trace only to the two-column role header**, the accepted
exception in `CV-SPEC.md` item 2 and `RUBRIC.md`. Reported, not blocking. I
searched for any other cause of 0.5-0.8 and found none.

**Gate 0 verdict: PASS.**

### New element versus `base-pt`

Raw line 2 carries `Senior Software Engineer` as a headline directly under the
name. `base-pt` has no such line. It is **not a defect**: `DOSSIER.md` records
"CV title stays `Senior Software Engineer`. [FACT]" and the string matches
LinkedIn exactly. It also puts the target title at line 2 of 76, which is why
Gate 3.1 is full marks. Recorded as a deviation from the base so Lucas can
decide whether it becomes the base too.

### LinkedIn ground-truth cross-check — PASS

Character for character against the `DOSSIER.md` LinkedIn block.

| Block | Resume text (raw lines) | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` (22) / `Senior Software Engineer` (23) / `Jan 2026 - Present` (25) | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | `Luizalabs` (39) / `Mid-level Software Engineer` (40) / `Jan 2024 - Jan 2026` (42) | identical | YES |
| 3 | `Lippaus Distribuidora` (51) / `Mid-level Software Engineer` (52) / `Jan 2023 - Jan 2024` (54) | identical | YES |
| 4 | `Lippaus Distribuidora` (60) / `Entry-level Fullstack Software Engineer` (61) / `Mar 2021 - Jan 2023` (63) | identical | YES |
| Education | `FAESA` (70) / `Bacharelado em Sistemas de Informação` (71) / `Feb 2022 - Dec 2025` (73) | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — start and end months identical; ASCII hyphen per `CV-SPEC.md` item 5 |

Company spelling `Luizalabs` correct. Both Lippaus roles present and separate.
Role locations correct: `Remoto` for DexCare and Luizalabs, `Vitória, ES,
Brasil` for both Lippaus roles.

### Forbidden-token grep

```
grep -inE 'ruby|rails|sidekiq|activerecord|activejob|rspec|devise|pundit|hotwire'
```
**Zero hits** in the `.tex` and zero in both extractions. **Zero Ruby or Rails
tokens confirmed.**

```
grep -o UNVERIFIED resumes/diana-neves-fullstack-314-26-pt.tex | wc -l
```
**33.** The raw extraction carries the same 33. The Architect's draft states
33. That count is factually correct. Full list below under "Claims I could not
verify".

---

## Gate 1 — Knockouts

Extracted from the post text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | `💼 PJ \| Contrato Indeterminado` | **FAIL** — the post names PJ as the contracting model. The document states no entity type: `PJ` 0 hits, `CNPJ` 0 hits in the raw extraction. `DOSSIER.md` Identity records `Contract types available: PJ with own CNPJ ... [FACT, Lucas 2026-09-01]`, so the document is silent on a fact it already holds. Identical to `reports/brivia-fullstack-pj-gate.md` |
| Location | `📍 Home Office`, workplace type Remote | **PASS** — graded on the contact-block city per the `RUBRIC.md` 2026-09-02 amendment. Contact line reads `Vitória, ES, Brasil`. Two roles print `Remoto` |
| Time-zone overlap | Not stated in the post | **not stated** — and never a FAIL |
| Minimum years of experience | Not stated. The post states no seniority level at all | **not stated.** The document carries `Senior Software Engineer` at raw 2 and 23, and `mais de 5 anos` at raw 6 |
| English proficiency | **Not stated in the post.** Written in Portuguese, PJ contract, domestic benefits (`TotalPass`, `StarBem`) | **not stated** — the LatAm-remote hard-gate rule does not fire on a Brazil-domestic Portuguese post. The document states it anyway: `Eu tenho Inglês Advanced/C1 e trabalho diariamente com um time dos EUA` (raw 8), which is a `DOSSIER.md` [FACT]. Covered either way |
| Degree requirement | Not stated in the post | **not stated.** The document carries `Bacharelado em Sistemas de Informação`, FAESA |
| **Certificação GCP ou similares** | `• Certificação GCP ou similares;` under `🔎 Requisitos` | **Not held.** `Certifica` 0 hits in the document, `Certificação` 0. `DOSSIER.md` records no certification of any kind. **Not a rubric row and not a document defect** — the CV is correct to stay silent, because claiming it would be fabrication. Recorded here because the post states it as a requirement. It needs an answer from Lucas in the screening answers of the apply note. Same treatment as the "own equipment" row in `reports/brivia-fullstack-pj-gate.md` |

Required-skill presence, verbatim in the raw extraction. Required is taken
from the post's own heading `🔎 Requisitos`.

| Requirement (post's words) | Present verbatim? |
|---|---|
| `TypeScript` | YES — Summary, Skills, Experience |
| `microsserviços` | YES — Skills (13), Experience (28) |
| `Hooks` | YES — Skills (16), Experience (34) |
| `Context API` | YES — Skills (16), Experience (34) |
| `GCP` | YES — Skills (17), Experience (47) |
| `Cloud Run` | YES — Skills (17), Experience (47) |
| `Pub/Sub` | YES — Skills (15), Experience (46) |
| `Cloud Functions` | YES — Skills (17), Experience (47) |
| `Vite/Webpack` | YES — Skills (16), Experience (35) |
| `Jest` | YES — Skills (19), Experience (49) |
| `RTL` | YES — Skills (16), Experience (35) |
| `Git` | YES — Skills (19), Experience (36) |
| `GitLab` | YES — Skills (19), Experience (36) |
| `SOLID` | YES — Skills (13), Experience (36) |
| `Clean Code` | YES — Skills (14), Experience (36) |
| `padrões de projeto` | YES — **Skills only** (14). Absent from every bullet |
| `mensageria` | YES — Skills group label `Mensageria e dados` (15), Experience (30) |
| `RabbitMQ` | YES — Skills (15), Experience (30) |
| `Kafka` | YES — Skills (15), Experience (30) |
| `Docker` | YES — Skills (17), Experience (47) |
| `Docker Compose` | YES — Skills (17), Experience (47) |
| `Kubernetes` | YES — Skills (18), Experience (48) |
| `integrações de alta complexidade` | YES — Experience only (31) |
| `ambientes de grande escala` | YES — Experience only (29) |
| `decisões arquiteturais estratégicas` | YES — Experience only (37) |
| `Certificação GCP ou similares` | **NO** — 0 hits, correctly |

**Gate 1 verdict: FAIL on one row.** Entity type. Every other stated gate
passes or is `not stated`.

---

## Gate 2 — Retrieval coverage: 6 / 100

### Scoring conventions used, stated so this is reproducible

Carried forward from `reports/goodway-global-fullstack-gate.md`,
`reports/brivia-fullstack-pj-gate.md` and
`reports/conta-simples-engenheira-software-senior-gate.md`.

1. `required` comes from the post's own heading `🔎 Requisitos`. The post lists
   no `diferenciais`, so `preferred` is taken from the technology tokens named
   under `🧩Atividades principais` and nowhere else. Those are duties, not
   stated requirements, so they carry weight 1. This follows the Maestro
   brief's own split into `Required` and `Activities name`.
2. A `Skills` **group label** counts as a `Skills` placement, rung 1. Rung 3
   needs the token inside an Experience bullet.
3. Inflections count for rung 3 where the stem is the post's stem.
4. The rubric ladder assumes a token can sit in `Skills`. For a token whose
   only placement is an Experience bullet, the ladder has no rung: rung 3
   requires `Skills` beneath it. I score it **2** and mark the row. Same
   convention as the Summary-only and Education-only rungs in the two earlier
   reports.
5. The numerator is the unweighted sum of points and the denominator is
   `count × weight × 4`, exactly as the rubric's Step 3 formula is literally
   written and as the three earlier reports in this hunt computed it.
6. Step 4 frequency is measured with a whole-word, Unicode-aware regex, and a
   compound that contains a shorter token (`Docker Compose` contains `Docker`,
   `REST APIs` contains `APIs`) counts toward the shorter token's total. This
   is the literal reading of `CV-SPEC.md` "cap any term at 3 appearances" and
   it matches the earlier reports. Where a breach is an artifact of that
   overlap, the defect text says so.

### Required tokens — weight 3, max 4 points each

| # | Token (post's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| R1 | `TypeScript` | yes (12) | yes (28) | **yes** (6) | 4 | Full ladder |
| R2 | `microsserviços` | yes (13) | yes (28) | no | 3 | |
| R3 | `Hooks` | yes (16) | yes (34) | no | 3 | |
| R4 | `Context API` | yes (16) | yes (34) | no | 3 | |
| R5 | `GCP` | yes (17) | yes (47) | no | 3 | |
| R6 | `Cloud Run` | yes (17) | yes (47) | no | 3 | |
| R7 | `Pub/Sub` | yes (15) | yes (46) | no | 3 | |
| R8 | `Cloud Functions` | yes (17) | yes (47) | no | 3 | |
| R9 | `Vite/Webpack` | yes (16) | yes (35) | no | 3 | |
| R10 | `Jest` | yes (19) | yes (49) | no | 3 | |
| R11 | `RTL` | yes (16) | yes (35) | no | 3 | |
| R12 | `Git` | yes (19) | yes (36) | no | 3 | |
| R13 | `GitLab` | yes (19) | yes (36) | no | 3 | |
| R14 | `SOLID` | yes (13) | yes (36) | no | 3 | |
| R15 | `Clean Code` | yes (14) | yes (36) | no | 3 | |
| R16 | `padrões de projeto` | yes (14) | **no** | no | 1 | The only required token left in `Skills` with no bullet. Stuffing penalty applies. See defect 2 |
| R17 | `mensageria` | yes (15, group label `Mensageria e dados`) | yes (30) | no | 3 | Convention 2 plus a real bullet hit |
| R18 | `RabbitMQ` | yes (15) | yes (30) | no | 3 | See defect 3, a `DOSSIER.md` placement instruction |
| R19 | `Kafka` | yes (15) | yes (30) | no | 3 | |
| R20 | `Docker` | yes (17) | yes (47) | no | 3 | |
| R21 | `Docker Compose` | yes (17) | yes (47) | no | 3 | |
| R22 | `Kubernetes` | yes (18) | yes (48) | no | 3 | |
| R23 | `integrações de alta complexidade` | no | yes (31) | no | 2 | Convention 4 |
| R24 | `ambientes de grande escala` | no | yes (29) | no | 2 | Convention 4 |
| R25 | `decisões arquiteturais estratégicas` | no | yes (37) | no | 2 | Convention 4 |
| R26 | `Certificação GCP ou similares` | no | no | no | **0** | **A real gap. Never claim it.** `DOSSIER.md` records no certification |

Required points earned: **71**. Required denominator: 26 × 3 × 4 = **312**.

### Preferred tokens — weight 1, max 4 points each

Technology tokens named only under `🧩Atividades principais`.

| # | Token (post's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| P1 | `Node.js/NestJS` | yes (13) | yes (28) | `Node.js` yes (6), `NestJS` no | 3 | The compound is not in the Summary; `Node.js` alone is |
| P2 | `React.js` | yes (16) | yes (34) | no | 3 | |
| P3 | `Swagger` | yes (13, `OpenAPI/Swagger`) | yes (32) | no | 3 | |
| P4 | `testes unitários e de integração` | yes (19, verbatim) | yes (49, verbatim) | no | 3 | The post's exact phrase in both fields |
| P5 | `CI/CD` | yes (18) | yes (48) | no | 3 | |
| P6 | `DevOps` | yes (17, group label `Cloud e DevOps`) | yes (48) | no | 3 | Convention 2 |

Preferred points earned: **18**. Preferred denominator: 6 × 1 × 4 = **24**.

### Step 3

```
coverage = 100 * (71 + 18) / (312 + 24) = 100 * 89 / 336 = 26.49 -> 26
```

### Step 4 — stuffing penalty: −20

**(a) Tokens in `Skills` with no supporting evidence anywhere in Experience,
−5 each.**

| Token | Any Experience evidence? | Penalty |
|---|---|---|
| `padrões de projeto` | none. No bullet names a pattern. `SOLID` and `Clean Code` are adjacent practices, not the token | −5 |
| `AMQP` (15) | none, but **this post does not ask for it** | 0 |
| `DynamoDB` (15), `Redis` (15) | none. The DexCare data-modelling bullet was cut for length. **Not asked by this post** | 0 |
| `AWS` (17) | Summary only (raw 7). **Not asked by this post** | 0 |
| `Claude Code`, `Codex` (19) | yes (36) | 0 |

`AMQP`, `DynamoDB`, `Redis` and `AWS` take no penalty under the same treatment
applied in `reports/brivia-fullstack-pj-gate.md`: the penalty prices a human
reaction to padding against **this** posting's asks. They are still four
`Skills` entries with no supporting bullet, and they are recorded in defect 6.

Subtotal: **−5**.

**(b) Frequency, −5 each at 4 or more appearances.** Whole-word counts,
Unicode-aware boundaries, convention 6:

`Docker` **4**, `JavaScript` **4**, `APIs` **4**, then `TypeScript` 3,
`Node.js` 3, `Go` 3, `BullMQ` 3, `multi-tenant` 3, `integrações` 3, and every
other measured term at 2 or 1.

- `JavaScript` **4** is a genuine breach with no compound artifact: raw 12,
  45, 57, 66.
- `Docker` **4** is an artifact of `Docker Compose`: `Docker` standalone
  twice (17, 47) plus `Docker Compose` twice (17, 47).
- `APIs` **4** is an artifact of `REST APIs`: bare `APIs` twice (7, 28) plus
  `REST APIs` twice (13, 32).

Subtotal: **−15**.

Total penalty: **−20**.

```
26 - 20 = 6
```

**Gate 2 final: 6 / 100.** Twenty-six before penalty.

### Missing required tokens

1. `Certificação GCP ou similares` — 0 hits. The only true dossier gap on this
   posting, and the CV is right not to claim it.
2. `padrões de projeto` — `Skills` only, absent from every bullet.
3. `integrações de alta complexidade`, `ambientes de grande escala`,
   `decisões arquiteturais estratégicas` — Experience only, absent from
   `Skills`.

Missing preferred: none. All six are at rung 3.

### Ceiling, stated honestly

- Moving `padrões de projeto` into the DexCare architecture bullet lifts R16
  from 1 to 3 and removes −5. Coverage goes to **13**.
- Adding `integrações de alta complexidade`, `ambientes de grande escala` and
  `decisões arquiteturais estratégicas` to a `Skills` group lifts R23, R24 and
  R25 from 2 to 3. Coverage goes to **14**.
- Cutting one `JavaScript`, one bare `APIs` and one `Docker` occurrence
  removes the remaining −15. Coverage reaches **29**.
- Placing `TypeScript`-class tokens in the Summary is the only route past 30,
  and the Summary is already full. **29 is the realistic ceiling** while
  `Certificação GCP` stays honestly absent, which it must.

The gap between 6 and 29 is entirely frequency discipline and three
placements. No new claim is needed for any of it.

---

## Gate 3 — Human scan: 95 / 100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15/15 | `Senior Software Engineer` at raw line **2 of 76** = 2.6%, as a headline under the name, and again in the Summary at raw 6 and as the DexCare title at raw 23. The post's own title is `Desenvolvedor Fullstack (Node.js / React)`; `CLAUDE.md` rule 1 binds the CV to the LinkedIn English string, so the English title is correct |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20/20 | DexCare bullet 1: `microsserviços`, `APIs de alta performance`, `TypeScript`, `Node.js/NestJS`, `ambientes de grande escala`. Bullet 2: `mensageria`, `RabbitMQ`, `Kafka`, 15%, `integrações de alta complexidade`. Bullet 3: `REST APIs`, `Auth0`, `OpenAPI/Swagger`, 25%. All three land on the post's own requirement list. Best 3.2 result of the hunt |
| 3.3 | Voice rule | 15/15 | 13 of 13 bullets pass. Full table below |
| 3.4 | At least 3 bullets with a real, defensible number | 15/15 | Six: 15% (raw 30), 25% (32), 7% (34), 20% (46), 18% (49), 26% (58). **All six trace to `DOSSIER.md`** bullet metrics D2, D3, D5, L2, L3, P2 |
| 3.5 | Length | 10/10 | `pdfinfo` reports 1 page, letter |
| 3.6 | No unsupported buzzwords | 10/10 | Zero hits for `proativo`, `apaixonado`, `dinâmico`, `comunicativo`, and for the EN list `team player`, `results-driven`, `passionate`, `hands-on`. `decisões arquiteturais estratégicas` is an unsupported qualifier, but it is a claim carrying its own marker, not a buzzword this check names. Reported under "Claims I could not verify" |
| 3.7 | Skills grouped by category | 9/10 | Six labelled groups (raw 12-19), every one a real technology category tuned to the post's own vocabulary: `Linguagens`, `Backend e arquitetura`, `Mensageria e dados`, `Frontend`, `Cloud e DevOps`, `Qualidade e colaboração`. **Minus 1:** the fifth group's label is `Cloud e DevOps [UNVERIFIED]`, which puts the marker on the **label**, so it reads as marking `AWS`, `GCP`, `Docker`, `Kubernetes`, `ArgoCD` and `CI/CD` as unverified. Those six are `DOSSIER.md` facts. See defect 4 |
| 3.8 | Scannable | 1/5 | Consistent 5pt inter-role gap, bold company, italic title, one column, full width, and a headline title that anchors the top of the page. **Minus 3: 33 `[UNVERIFIED]` markers** on a one-page document, roughly one every two lines, four of them inside a single Skills line (16) and five inside a single bullet (36-37). As built, the page reads as an annotated draft, not a resume. **Minus 1: verb monotony.** `Construí` opens 6 of 13 bullets (raw 28, 32, 36, 45, 57, 67) |

**Gate 3 total: 95/100.**

The 3.8 deduction is against the document **as built**. It is not a criticism
of the marker policy: `CLAUDE.md` section 4 requires the markers, and they
disappear the moment Lucas confirms or strikes each claim. It is recorded so
nobody sends this PDF unedited.

## Voice check (explicit, per `CLAUDE.md` section 9 and `CV-SPEC.md`)

Leading token of every Experience bullet, read from the raw extraction:

| Raw line | Leading verb | Verdict |
|---|---|---|
| 28 | Construí | 1st person past, subject omitted, OK |
| 30 | Integrei | OK |
| 32 | Construí | OK |
| 34 | Reduzi | OK |
| 36 | Construí | OK |
| 45 | Construí | OK |
| 46 | Migrei | OK |
| 47 | Implantei | OK |
| 49 | Reduzi | OK |
| 57 | Construí | OK |
| 58 | Aumentei | OK |
| 66 | Desenvolvi | OK |
| 67 | Construí | OK |

- Bullets that break the rule: **none**. 13 of 13 pass.
- Bullets starting with `Eu`: **none**.
- Present tense in a bullet: **none**.
- `Responsável por` or third person: **none**.
- Summary uses `Eu`: **yes**, four times — `Eu sou`, `Eu desenvolvo`,
  `Eu tenho`, `Eu integro` (raw 6-8).
- Every bullet carries a technology name. Six of thirteen carry a number.

**Voice: PASS.**

---

## Defects, ranked by cost

1. **No entity type on the document** — Gate 1 FAIL, blocking. The post reads
   `💼 PJ | Contrato Indeterminado`. `PJ` and `CNPJ` both return 0 hits.
   `DOSSIER.md` already records `PJ with own CNPJ` as a [FACT]. Fix in the
   fix list below.
2. **`padrões de projeto` sits in `Skills` with no bullet** — Gate 2 R16, worth
   2 points plus the −5 penalty, so 7 points of the 20-point gap. It is the
   only required token that broke the section 4 rule ("Skills **and** one
   bullet"). The DexCare bullet at raw 36 already carries `SOLID` and
   `Clean Code` and is the natural home.
3. **`RabbitMQ` placed in an Experience bullet** — truth handling, needs
   Lucas. `DOSSIER.md`: "DexCare messaging: RabbitMQ / AMQP used on services.
   **Skills token only** (`RabbitMQ`, `AMQP`), no service names on the CV.
   [FACT, Lucas 2026-09-01]". Raw 30 puts `RabbitMQ` inside the EMR Epic
   bullet, attaching it to a named integration. The technology is a fact and
   no DexCare service is named, so this is a placement question, not a
   fabrication. It is unmarked. Lucas rules.
4. **The marker on a Skills group label** — Gate 3.7, minus 1. Raw 17 reads
   `Cloud e DevOps [UNVERIFIED]:`, which reads as marking the whole group.
   `AWS`, `GCP`, `Docker`, `Kubernetes`, `ArgoCD` and `CI/CD` are all
   `DOSSIER.md` facts. Only `DevOps` as an experience claim needs the marker.
5. **Three post phrases claimed without a marker** — truth handling.
   `APIs de alta performance` (28), `ambientes de grande escala` (29) and
   `integrações de alta complexidade` (31) are the post's own words applied to
   DexCare. None appears in `DOSSIER.md`. The nearest recorded fact is
   "healthcare scheduling at scale" [FACT-OBSERVED]. `decisões arquiteturais
   estratégicas` in the same document **is** marked, so the marking is
   internally inconsistent.
6. **Four `Skills` entries with no bullet anywhere** — `AMQP`, `DynamoDB`,
   `Redis`, `AWS`. No Gate 2 penalty, because this post does not ask for them,
   but they are padding a document that already has 33 markers to defend. They
   became orphans when the DexCare data-modelling bullet was cut.
7. **`JavaScript` appears 4 times** — Gate 2 Step 4, −5, and a `CV-SPEC.md`
   3-appearance cap breach. Raw 12, 45, 57, 66. Not an artifact; one of the
   three bullet mentions can go.
8. **`Docker` and `APIs` each reach 4** — Gate 2 Step 4, −5 each. Both are
   overlap artifacts (`Docker Compose`, `REST APIs`). Cheapest fix: drop the
   bare `Docker` from the `Cloud e DevOps` Skills line, which already carries
   `Docker Compose`, and drop one bare `APIs`.
9. **The 33% SPI metric was cut** — content loss, no rubric deduction. The
   DexCare SPI bullet (`DOSSIER.md` D7) and the data-modelling bullet were
   dropped to hold one page. That is a defensible trade for this posting, and
   it costs the strongest number in the dossier. Recorded so the choice is
   visible.
10. **Verb monotony** — Gate 3.8, part of the minus 1. `Construí` opens 6 of
    13 bullets.
11. **`tabular*` role header, four Gate 0 findings** — reported, not blocking,
    by Lucas's 2026-09-01 decision. No action.
12. **`Present` and English month abbreviations in a Portuguese document** —
    observation only. Rule 1 outranks language consistency.

---

## Claims I could not verify

Traced against `DOSSIER.md`. I do not delete these and I do not defend them.
Lucas decides.

### The 33 `[UNVERIFIED]` markers, all 17 distinct claims

Counted in both the `.tex` and the raw extraction. Each token is marked in
`Skills` and again in its Experience bullet, which is why 17 claims produce 33
markers (`DevOps` is marked once in a group label covering both).

| # | Claim | Raw lines | Architect's stated reason |
|---|---|---|---|
| 1 | `NestJS` | 13, 28 | `DOSSIER.md` confirms Node.js, Express and Koa, not NestJS |
| 2 | `microsserviços` at DexCare | 13, 28 | Confirmed at Luizalabs, not at DexCare |
| 3 | `SOLID` | 13, 36 | Not recorded as a fact |
| 4 | `Clean Code` | 14, 36 | Not recorded as a fact |
| 5 | `Pub/Sub` | 15, 46 | BullMQ and messaging confirmed, Pub/Sub not |
| 6 | `Kafka` | 15, 30 | RabbitMQ and AMQP confirmed, Kafka not |
| 7 | `Hooks` | 16, 34 | React confirmed, Hooks not |
| 8 | `Context API` | 16, 34 | React confirmed, Context API not |
| 9 | `Vite/Webpack` | 16, 35 | React confirmed, the bundler not |
| 10 | `RTL` | 16, 35 | Jest and Vitest confirmed, React Testing Library not |
| 11 | `DevOps` | 17, 48 | Tools confirmed, the term as experience not |
| 12 | `Cloud Run` | 17, 47 | GCP confirmed at Luizalabs, Cloud Run not |
| 13 | `Cloud Functions` | 17, 47 | GCP confirmed at Luizalabs, Cloud Functions not |
| 14 | `Docker Compose` | 17, 47 | Docker confirmed, Compose not |
| 15 | `Git` | 19, 36 | Not recorded as a fact |
| 16 | `GitLab` | 19, 36 | Not recorded as a fact |
| 17 | `decisões arquiteturais estratégicas` | 37 | Agent environments confirmed, the decisions are not qualified as strategic |

All 17 need Lucas's yes or no before this package is sent. Fifteen of them are
ecosystem tokens `CLAUDE.md` section 4 explicitly authorises claiming.

### Numbers

Every number on the document traces to `DOSSIER.md`:

| Number | Raw line | Dossier id |
|---|---|---|
| 15% wrong bookings | 30 | D2 |
| 25% authentication friction | 32 | D3 |
| 7% release risk | 34 | D5 |
| 20% invoice throughput | 46 | L2 |
| 18% support tickets | 49 | L3 |
| 26% order and integration capacity | 58 | P2 |

**No number on the document fails to trace to `DOSSIER.md`.**

One quantity is derived rather than recorded:

- `mais de 5 anos` (Summary, raw 6). Not stated in `DOSSIER.md`.
  Arithmetically consistent with the LinkedIn ground truth: `Mar 2021` to
  2026-09-02 is 5 years 6 months. Consistent, not a recorded fact.

### Prose claims not traceable to the dossier, and unmarked

1. `APIs de alta performance` (DexCare, raw 28). The post's own phrase.
   `DOSSIER.md` records no performance claim. Unmarked.
2. `ambientes de grande escala` (DexCare, raw 29). The post's own phrase. The
   nearest fact is "healthcare scheduling at scale" [FACT-OBSERVED], which is
   adjacent but not the same claim. Unmarked.
3. `integrações de alta complexidade` (DexCare, raw 31). The post's own
   phrase. `DOSSIER.md` records the Epic EMR integration without a complexity
   qualifier. Unmarked.
4. `padrões de projeto` (Skills, raw 14). Same class as `SOLID` and
   `Clean Code`, both of which are marked. This one is not. Unmarked.
5. `apoiando a expansão nacional de varejistas` (Lippaus Mid-level, raw 57).
   Inherited from `base-pt`. `DOSSIER.md` confirms the multi-tenant platform,
   nothing about nationwide scope.
6. `startup de distribuição de bebidas` (Lippaus Entry-level, raw 66).
   Inherited from `base-pt`. Not in `DOSSIER.md` in any form.

### Claims that are facts and correctly unmarked

Recorded so the marking can be audited both ways: `React Native` (raw 57) is
`DOSSIER.md` [FACT] for the Lippaus stack; `Inglês Advanced/C1` and the daily
US-team work (raw 8) are [FACT, Lucas 2026-09-01]; `GCP`, `Docker`,
`Kubernetes`, `ArgoCD`, `BullMQ`, `Vitest`, `Jest` at Luizalabs are [FACT];
`RabbitMQ`, `AMQP` at DexCare are [FACT] as tokens, see defect 3 for the
placement question.

---

## Fix list for the Architect

1. **Add the entity type to the document.** Gate 1 FAIL, the only blocking
   defect. The post states `💼 PJ | Contrato Indeterminado` and the raw
   extraction returns `PJ` 0 hits, `CNPJ` 0 hits. `DOSSIER.md` Identity
   records `Contract types available: PJ with own CNPJ, US contractor
   (W-8BEN), CLT, EOR/Deel-style employment. All acceptable. [FACT, Lucas
   2026-09-01]`, so no new claim is needed. Put the token where it is
   retrievable and where `CV-SPEC.md` item 3 already allows text: append
   `PJ (CNPJ próprio)` to the contact line at raw 3, or add one clause to the
   Summary. Do not print a UTC offset or a time-zone overlap sentence while
   editing that block; `CLAUDE.md` section 3 forbids both.
