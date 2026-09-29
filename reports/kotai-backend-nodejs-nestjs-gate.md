# ATS Analysis — kotai-backend-nodejs-nestjs-pt.pdf vs kotai-backend-nodejs-nestjs
Segment: us-direct   Date: 2026-09-02

Judged on extractions the analyzer regenerated from the PDF under test:
`pdftotext -layout` and `pdftotext` on
`resumes/kotai-backend-nodejs-nestjs-pt.pdf` (1 page, letter). Source
cross-read: `resumes/kotai-backend-nodejs-nestjs-pt.tex`.
Posting text: `jobs/kotai-backend-nodejs-nestjs.md` (LinkedIn job `4459981590`,
Kotai Project, captured by Kestrel, hunt 2026-09-02-b).
Titles, companies and dates checked against `DOSSIER.md` **LinkedIn ground truth**.
Architect's own marker list read: `reports/kotai-backend-nodejs-nestjs-draft.md`.

Rule versions applied: `CLAUDE.md` and `RUBRIC.md` as of 2026-09-02.

This is our rubric. It is not a vendor score. No ATS emits these numbers.

## Verdict

**PASSES ALL GATES.** No blocking gate fails.

| Gate | Result |
|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, reported not blocking) |
| Gate 1 — Knockouts | **PASS** — no FAIL row |
| Gate 2 — Retrieval coverage | **31 / 100** (no stuffing penalty; the first clean Step 4 of the hunt) |
| Gate 3 — Human scan | **98 / 100** |

**The strongest package of hunt 2026-09-02-b on every measure.** Gate 2 at 31
beats Brivia (22), Conta Simples (0) and Diana Neves (6), and it is the only
one of the four to take **zero** stuffing penalty: every posting token in
`Skills` also appears in an Experience bullet, no term breaks the
`CV-SPEC.md` 3-appearance cap, and the marker count is 16 rather than 33.

One condition needs Lucas before this is sent, and it is not a document
defect: the posting demands **`dedicação integral e exclusiva`**, "sem vínculo
simultâneo com outro emprego ou contrato ativo", and says the condition
"poderá ser verificada durante o processo seletivo". Lucas holds a current
full-time role. Whether he accepts that condition is not observable from
`DOSSIER.md`. It belongs in the apply note's screening answers.

---

## Gate 0 — Parse integrity

`pdfinfo` reports **1 page**, letter. Raw extraction is 76 lines.

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Complete prose. Contact block, four sections, four Experience blocks and one Education block all present |
| 0.2 | Glyph integrity | PASS | Measured by codepoint in Python, not by shell grep. Zero `\x00`, zero `U+FB00-FB04` ligature codepoints, zero `U+FFFD`, zero stray `?`. The only character above U+00FF is `U+2022 BULLET`. Ligature-bearing words intact: `fiscais` 2, `fluxos` 1, `funcionalidades` 1, `confiabilidade` 1, `flags` 1, `Distribuidora` 2 |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, not a header or footer: `Vitória, ES, Brasil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email and LinkedIn URL all present. No UTC offset, no time-zone overlap sentence |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 11, 22, 69: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, each a standalone line. PT allowlist, Gate 0.4 |
| 0.5 | Employment-block segmentation | FAIL — header only | Raw splits each role header into `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remoto`. **No two roles merge. No role splits into two employment entries.** Four Experience blocks and one Education block, intact and in order. Both Lippaus entries repeat the company name, so the promotion segments unambiguously. Cause is the `tabular*` in `\resumeSubheading` |
| 0.6 | Date parseability | FAIL — header only | Every date sits one blank line below its title. Format correct in all five blocks: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Separator verified by Unicode category `Pd`: the only dash in the document is `U+002D HYPHEN-MINUS` |
| 0.7 | Reading order | FAIL — header only | Raw order per role header: company, title, dates, location. Layout: company+dates, title+location. **Zero content blocks reorder.** The name block (name, title, contact) reads in the same order in both extractions |
| 0.8 | No forbidden constructs | FAIL — header only | The `tabular*` role header. No table elsewhere, no text box, no image of text, no icon, no photo |

**All four FAILs trace only to the two-column role header**, the accepted
exception in `CV-SPEC.md` item 2 and `RUBRIC.md`. Reported, not blocking. I
searched for any other cause of 0.5-0.8 and found none.

**Gate 0 verdict: PASS.**

### One extraction artifact worth recording

The Summary phrase `arquitetura de software` wraps across raw lines 6 and 7 as
`arquitetura de` / `software`. A naive exact-string search over the raw stream
would miss it there. **This is a `pdftotext` line-wrap artifact, not a defect
in the PDF**: the words are contiguous in the page's text stream, and the same
phrase appears unbroken in `Skills` at raw 15. Recorded because Gate 2 is
scored on the raw file and the row is affected. The same applies to
`tratamento de erros em` / `APIs REST` across raw 12-13.

### New element versus `base-pt`

Raw line 2 carries `Senior Software Engineer` as a headline under the name, as
`diana-neves-fullstack-314-26-pt` also does. `base-pt` has no such line. **Not
a defect**: `DOSSIER.md` records "CV title stays `Senior Software Engineer`.
[FACT]" and the string matches LinkedIn exactly. Two of this hunt's tailorings
now carry it; the base does not. Lucas may want to settle that.

### LinkedIn ground-truth cross-check — PASS

Character for character against the `DOSSIER.md` LinkedIn block.

| Block | Resume text (raw lines) | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` (23) / `Senior Software Engineer` (24) / `Jan 2026 - Present` (26) | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
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
grep -o UNVERIFIED resumes/kotai-backend-nodejs-nestjs-pt.tex | wc -l
```
**16**, covering **8 distinct claims**, each marked once in `Skills` and once
in its Experience bullet. The raw extraction carries the same 16. The
Architect's draft lists exactly those 8. That claim is factually correct.

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | `Modelo de contratação: Empresa internacional; Prestação de serviço; **Não é necessário ter PJ ativa no momento da candidatura**` | **PASS** — the posting removes the PJ requirement at application. The document is silent (`PJ` 0 hits, `CNPJ` 0), and silence costs nothing here. `DOSSIER.md` records `PJ with own CNPJ, US contractor (W-8BEN), CLT, EOR/Deel-style employment. All acceptable. [FACT]`, so the contractor shape is available if asked later. **This is why the same silence that fails Brivia and Diana Neves does not fail here** |
| Location | `Residir no Brasil` under `Requisitos`; `Trabalho 100% remoto` | **PASS** — contact line reads `Vitória, ES, Brasil`, and `Brasil` appears twice more as a Lippaus role location. The requirement is met verbatim in the highest-prominence field on the page |
| Time-zone overlap | Not stated in the posting | **not stated** — and never a FAIL |
| Minimum years of experience | Not stated. The posting labels no seniority level | **not stated.** The document carries `Senior Software Engineer` at raw 2 and 24, and `mais de 5 anos` at raw 6 |
| English proficiency | **Not stated in the posting.** Written in Portuguese, though the company is described as `Empresa internacional` | **not stated** — I do not infer an English gate from "empresa internacional". The document states it anyway: `Eu tenho Inglês Avançado/C1 e trabalho diariamente em inglês com uma equipe dos EUA` (raw 8-9), which is a `DOSSIER.md` [FACT, Lucas 2026-09-01]. Covered either way |
| Degree requirement | Not stated in the posting | **not stated.** The document carries `Bacharelado em Sistemas de Informação`, FAESA |
| **Dedicação integral e exclusiva** | `Disponibilidade para dedicação integral e exclusiva` under `Requisitos`, and under `Modelo de contratação`: `A posição exige atuação exclusiva, sem vínculo simultâneo com outro emprego ou contrato ativo` / `Essa condição poderá ser verificada durante o processo seletivo` | **Not observable. Needs Lucas.** `exclusiv` 0 hits and `dedicação` 0 hits in the document, correctly: no CV can assert this, and `CLAUDE.md` rule 1 requires DexCare to print as `Jan 2026 - Present`. `DOSSIER.md` records no notice period and no availability date; the `Notice period:` field is still an empty `[FACT]` slot. **Not a FAIL and not a document defect.** It is a real condition Lucas must accept or decline, and it belongs in the apply note's screening answers |

Required-skill presence, verbatim in the raw extraction. Required is taken
from the posting's own heading `## Requisitos`.

| Requirement (posting's words) | Present verbatim? |
|---|---|
| `Residir no Brasil` | YES — `Brasil` at raw 3, 55, 64 |
| `desenvolvimento backend em Node.js` | YES — `desenvolvimento backend` Summary (6), `Node.js` Skills (12), Experience (29), Summary (7) |
| `NestJS` | YES — Skills (12), Experience (29) |
| `TypeScript` | YES — Skills (14), Experience (29), Summary (7) |
| `APIs REST` | YES — Skills (13), Experience (30) |
| `modelagem de dados` | YES — Summary (6), Skills (15), Experience (31) |
| `arquitetura de software` | YES — Summary (6-7, line-wrapped), Skills (15). **Absent from every bullet** |
| `PostgreSQL` | YES — Skills (15), Experience (31) |
| `ORMs`, `Prisma`, `TypeORM` | YES — all three in Skills (15-16) and Experience (31-32) |
| `validação, segurança e tratamento de erros em APIs` | YES — the full triple in Skills (12-13) and again in Experience (29-30) |
| `Boa comunicação e capacidade de trabalhar de forma remota` | Soft skill, discarded from Gate 2 per Step 1. Document evidence: `Remoto` twice as a role location, `Liderei o escopo de projetos e a comunicação com stakeholders` (58) |
| `Disponibilidade para dedicação integral e exclusiva` | **NO**, correctly. See the Gate 1 row above |

**Gate 1 verdict: PASS.** No FAIL row.

---

## Gate 2 — Retrieval coverage: 31 / 100

### Scoring conventions used, stated so this is reproducible

Carried forward from `reports/goodway-global-fullstack-gate.md`,
`reports/brivia-fullstack-pj-gate.md`,
`reports/conta-simples-engenheira-software-senior-gate.md` and
`reports/diana-neves-fullstack-314-26-gate.md`.

1. `required` comes from the posting's heading `## Requisitos`, `preferred`
   from `## Diferenciais`. The posting draws that line itself.
2. A `Skills` **group label** counts as a `Skills` placement, rung 1. Rung 3
   needs the token inside an Experience bullet.
3. Inflections count for rung 3 where the stem is the posting's stem.
4. Where the posting lists alternates in one clause (`Prisma, TypeORM ou
   equivalentes`; `Redis, BullMQ, RabbitMQ ou similares`), the clause scores
   **once**, at its best-covered member.
5. For a token with no available `Skills` rung, or with `Skills` plus
   `Summary` but no bullet, the ladder has no rung. I score it **2** and mark
   the row. Same convention as the Summary-only, Education-only and
   Experience-only rungs in the earlier reports.
6. Soft skills are discarded per Step 1: `Boa comunicação`, and every line
   under `## Perfil que buscamos` (`autonomia`, `perfil analítico`,
   `maturidade profissional`). They are not retrieval tokens. Recorded as a
   judgement.
7. `Disponibilidade para dedicação integral e exclusiva` is an availability
   condition, not a retrieval token. Scored in Gate 1 only.
8. The numerator is the unweighted sum of points and the denominator is
   `count × weight × 4`, exactly as the rubric's Step 3 formula is literally
   written and as the earlier reports computed it.
9. Step 4 frequency is measured with a whole-word, Unicode-aware regex, and a
   compound containing a shorter token counts toward the shorter token's
   total.

### Required tokens — weight 3, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title / contact | Points | Note |
|---|---|---|---|---|---|---|
| R1 | `Residir no Brasil` | no | yes (55, 64) | **yes** (3, contact block) | 3 | Convention 5. A location token has no sensible `Skills` rung; contact block plus two Experience fields is the strongest placement available |
| R2 | `desenvolvimento backend em Node.js` | yes (12) | yes (29) | **yes** (6-7) | 4 | Full ladder. `desenvolvimento backend` is verbatim in the Summary |
| R3 | `NestJS` | yes (12) | yes (29) | no | 3 | Marked `[UNVERIFIED]` in both places |
| R4 | `TypeScript` | yes (14) | yes (29) | **yes** (7) | 4 | Full ladder |
| R5 | `APIs REST` | yes (13) | yes (30) | no | 3 | The Summary carries `APIs multi-tenant`, not `APIs REST` |
| R6 | `modelagem de dados` | yes (15) | yes (31) | **yes** (6) | 4 | Full ladder. The posting's exact phrase in all three fields |
| R7 | `arquitetura de software` | yes (15) | **no** | **yes** (6-7) | 2 | Convention 5. No bullet carries it; `arquiteturas distribuídas` (45) is a different token. See defect 1 |
| R8 | `PostgreSQL` | yes (15) | yes (31) | no | 3 | |
| R9 | `ORMs` (`Prisma`, `TypeORM` ou equivalentes) | yes (15-16) | yes (31-32) | no | 3 | Convention 4. `Sequelize` and `Drizzle ORM` are `DOSSIER.md` facts and carry the clause; `Prisma` and `TypeORM` are the posting's names, marked |
| R10 | `validação, segurança e tratamento de erros em APIs` | yes (12-13) | yes (29-30) | no | 3 | The full triple, verbatim, in both fields |

Required points earned: **32**. Required denominator: 10 × 3 × 4 = **120**.

### Preferred tokens — weight 1, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| P1 | `filas e workers` (`Redis`, `BullMQ`, `RabbitMQ` ou similares) | yes (17, the phrase verbatim) | yes (47, the phrase verbatim) | no | 3 | Convention 4. `BullMQ`, `RabbitMQ` and `Redis` are all in both fields |
| P2 | `microservices` ou `arquiteturas distribuídas` | yes (17, both) | yes (45, both) | no | 3 | The posting's English spelling `microservices` is mirrored, not translated. Correct |
| P3 | `Docker` e ambiente `Linux` | yes (18) | yes (48) | no | 3 | `Linux` marked `[UNVERIFIED]` |
| P4 | `Web3`, `blockchain`, `dApps`, `wallets`, redes `EVM` | no | no | no | **0** | All five at 0 hits. **A real gap. Never claim it.** The Maestro brief names it a gap and the Architect obeyed |
| P5 | `alta complexidade`, `alta disponibilidade`, `operações sensíveis` | no | no | no | **0** | All three at 0 hits. `DOSSIER.md` records the healthcare and fiscal domains as facts but carries none of these qualifiers. The Architect declined to claim them, and said so in the draft |
| P6 | `observabilidade`, `performance` e `confiabilidade` | yes (19, all three) | yes (33 `observabilidade`, 48 `confiabilidade`) | no | 3 | Convention 4, scored at `observabilidade`. `performance` reaches `Skills` only |

Preferred points earned: **12**. Preferred denominator: 6 × 1 × 4 = **24**.

### Step 3

```
coverage = 100 * (32 + 12) / (120 + 24) = 100 * 44 / 144 = 30.56 -> 31
```

### Step 4 — stuffing penalty: 0

**(a) Tokens in `Skills` with no supporting evidence in Experience.** Every
posting token in `Skills` has a bullet behind it. The four `Skills` entries
without their own bullet are:

| Token | Supporting evidence | Penalty |
|---|---|---|
| `arquitetura de software` (15) | `arquiteturas distribuídas` and `microservices fiscais` (45) are architecture work in a bullet | 0 |
| `performance` (19) | the 20% throughput (47) and 26% capacity (57) bullets are performance outcomes | 0 |
| `AMQP` (17) | none, and **this posting does not ask for it** | 0 |
| `AWS` (18) | none in Experience, and **this posting does not ask for it** | 0 |

`AMQP` and `AWS` take no penalty under the same treatment applied in
`reports/brivia-fullstack-pj-gate.md`: the penalty prices a human reaction to
padding against **this** posting's asks. They are still two `Skills` entries
with no supporting bullet, recorded in defect 4.

**(b) Frequency, −5 each at 4 or more appearances.** Whole-word counts,
Unicode-aware boundaries, convention 9:

`Node.js` 3, `TypeScript` 3, `APIs` 3, `BullMQ` 3, `Go` 3, `React` 3,
`JavaScript` 3, `modelagem de dados` 3, and every other measured term at 2 or
1. **No term reaches 4.** The `CV-SPEC.md` 3-appearance cap holds exactly, on
every term.

Total penalty: **0**.

**Gate 2 final: 31 / 100.** The first clean Step 4 of the hunt.

### Missing required tokens

1. `arquitetura de software` in an Experience bullet — `Skills` and `Summary`
   only.
2. `Disponibilidade para dedicação integral e exclusiva` — absent, correctly.
   Not a retrieval loss; see the Gate 1 row.

Missing preferred: `Web3`, `blockchain`, `dApps`, `wallets`, `EVM`,
`alta complexidade`, `alta disponibilidade`, `operações sensíveis`.

### Ceiling, stated honestly

- Putting `arquitetura de software` inside the DexCare or Luizalabs
  architecture bullet lifts R7 from 2 to 3. Coverage goes to **32**.
- `performance` in an Experience bullet does not move P6, which is already at
  its best member.
- `Web3` and the availability qualifiers are the only remaining zeros, and
  **all of them must stay zero.** P4 is a domain Lucas never worked in, which
  `CLAUDE.md` section 4 defines as a gap to route around, not a claim. P5's
  three qualifiers have no dossier fact behind them.

**32 is the honest ceiling on this posting.** The 8 preferred points locked
behind Web3 are unreachable without fabrication. Unlike the other three
tailorings in this hunt, there is almost nothing left on the table here.

---

## Gate 3 — Human scan: 98 / 100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15/15 | `Senior Software Engineer` at raw line **2 of 76** = 2.6%, as a headline under the name, again in the Summary at raw 6 and as the DexCare title at raw 24. The posting's title is `Desenvolvedor(a) Backend (Node.js / NestJS)`; `CLAUDE.md` rule 1 binds the CV to the LinkedIn English string |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 20/20 | DexCare bullet 1 carries `TypeScript`, `Node.js`, `NestJS`, `Auth0 JWT`, `validação`, `segurança`, `tratamento de erros em APIs REST` and 25% — six required tokens in one line. Bullet 2 carries `modelagem de dados`, `PostgreSQL`, `Redis` and the four ORMs. Bullet 3 carries `observabilidade`, `Datadog` and 7%. The posting's `Requisitos` list is answered in order, in the first three lines of the current role |
| 3.3 | Voice rule | 15/15 | 11 of 11 bullets pass. Full table below |
| 3.4 | At least 3 bullets with a real, defensible number | 15/15 | Five: 25% (raw 30), 7% (33), 15% (35), 20% (47), 26% (57). **All five trace to `DOSSIER.md`** bullet metrics D3, D5, D2, L2, P2 |
| 3.5 | Length | 10/10 | `pdfinfo` reports 1 page, letter |
| 3.6 | No unsupported buzzwords | 10/10 | Zero hits for `proativo`, `apaixonado`, `dinâmico`, `comunicativo`, and for the EN list `team player`, `results-driven`, `passionate`, `hands-on`. The posting's `Perfil que buscamos` block (`autonomia`, `perfil analítico`, `maturidade profissional`) was correctly **not** mirrored into prose |
| 3.7 | Skills grouped by category | 10/10 | Seven labelled groups (raw 12-20), every one a real technology category tuned to the posting's own vocabulary: `Backend`, `Linguagens e frontend`, `Dados e arquitetura`, `Filas e serviços`, `Cloud e operação`, `Confiabilidade`, `Testes e IA`. No `keywords` dump label anywhere. Best Skills block of the hunt |
| 3.8 | Scannable | 3/5 | Consistent 5pt inter-role gap, bold company, italic title, one column, full width, headline title anchoring the top. **Minus 1: 16 `[UNVERIFIED]` markers**, four of them inside the first DexCare bullet (29-30) and four inside the `Backend` Skills line (12-13), which wrap awkwardly (`tratamento de erros em` / `APIs REST [UNVERIFIED]`). Half the density of `diana-neves`, still a visible annotation layer. **Minus 1: verb monotony plus a thin tail.** `Construí` opens 4 of 11 bullets (29, 36, 45, 66), and the Lippaus Entry-level role carries a **single** bullet for a 22-month period while DexCare carries five. The bottom third of the page reads thin |

**Gate 3 total: 98/100.**

The 3.8 deduction is against the document **as built**. `CLAUDE.md` section 4
requires the markers, and they disappear once Lucas confirms or strikes each
claim. It is recorded so nobody sends this PDF unedited.

## Voice check (explicit, per `CLAUDE.md` section 9 and `CV-SPEC.md`)

Leading token of every Experience bullet, read from the raw extraction:

| Raw line | Leading verb | Verdict |
|---|---|---|
| 29 | Construí | 1st person past, subject omitted, OK |
| 31 | Apliquei | OK |
| 33 | Reduzi | OK |
| 35 | Integrei | OK |
| 36 | Construí | OK |
| 45 | Construí | OK |
| 47 | Migrei | OK |
| 48 | Implantei | OK |
| 57 | Processei | OK |
| 58 | Liderei | OK |
| 66 | Construí | OK |

- Bullets that break the rule: **none**. 11 of 11 pass.
- Bullets starting with `Eu`: **none**. All four `Eu` occurrences are in the
  Summary.
- Present tense in a bullet: **none**.
- `Responsável por` or third person: **none**.
- Summary uses `Eu`: **yes**, four times — `Eu sou`, `Eu construo`, `Eu tenho`,
  `Eu integro` (raw 6-9).
- Every bullet names a technology. Five of eleven carry a number.

**Voice: PASS.**

---

## Defects, ranked by cost

1. **`arquitetura de software` never reaches a bullet** — Gate 2 R7, worth 1
   point and the only required token below rung 3. It is in `Skills` (15) and
   in the Summary (6-7). The Luizalabs bullet at raw 45 already says
   `microservices fiscais e arquiteturas distribuídas`, which is the natural
   home for the posting's own phrase.
2. **Four numbers were cut to hold one page** — content loss, no rubric
   deduction. The DexCare SPI bullet (`DOSSIER.md` D7, **33%**), the Luizalabs
   fiscal dashboards bullet (**L3, 18%**), the Lippaus multi-tenant platform
   bullet (P1) and the Lippaus internal dashboards bullet (E1) are all gone.
   The document keeps five numbers and drops the two largest. Defensible for a
   backend-only posting, and worth Lucas seeing: 33% is the strongest figure
   in the dossier.
3. **The Lippaus Entry-level role carries one bullet** — Gate 3.8, part of the
   minus 1. A 22-month role rendered as a single line next to a five-bullet
   DexCare block makes the page bottom-heavy in the wrong direction. Freed
   space from cutting one DexCare bullet would balance it.
4. **Two `Skills` entries with no bullet anywhere** — `AMQP` (17) and `AWS`
   (18). No Gate 2 penalty, because this posting asks for neither, but they
   are unsupported entries on a document that already carries 16 markers.
   `AWS` in particular lost its bullet when the DexCare data-modelling bullet
   was rewritten around ORMs.
5. **`e-commerce do Magazine Luiza`** — truth handling, raw 46. `DOSSIER.md`
   confirms the fiscal / NF-e / SEFAZ domain as [FACT] and does not carry the
   word `e-commerce`. Unmarked. Same finding as the base and the other
   tailorings.
6. **`sustentando leituras e escritas de reservas com consistência`** — truth
   handling, raw 32. `DOSSIER.md` confirms the DexCare data stack as
   [FACT-OBSERVED]. It records no consistency claim. Unmarked.
7. **Verb monotony** — Gate 3.8, part of the minus 1. `Construí` opens 4 of 11
   bullets. Mildest case in the hunt.
8. **`tabular*` role header, four Gate 0 findings** — reported, not blocking,
   by Lucas's 2026-09-01 decision. No action.
9. **`Present` and English month abbreviations in a Portuguese document** —
   observation only. Rule 1 outranks language consistency.
10. **`Inglês Avançado/C1` here, `Inglês Advanced/C1` in
    `diana-neves-fullstack-314-26-pt`** — cosmetic inconsistency across two
    documents in the same hunt. `DOSSIER.md` records `Advanced / C1`. Both are
    faithful; only one can be the convention. Lucas picks.

---

## Claims I could not verify

Traced against `DOSSIER.md`. I do not delete these and I do not defend them.
Lucas decides.

### The 16 `[UNVERIFIED]` markers, all 8 distinct claims

Counted in both the `.tex` and the raw extraction. Each claim is marked in
`Skills` and again in its Experience bullet, so 8 claims produce 16 markers.

| # | Claim | Raw lines | Architect's stated reason |
|---|---|---|---|
| 1 | `NestJS` | 12, 29 | `DOSSIER.md` confirms Node.js, Express and Koa, not NestJS |
| 2 | `validação` | 12, 29 | Auth0 and OpenAPI make it plausible; the specific practice is not recorded |
| 3 | `segurança` | 12, 30 | Auth0 and JWT make it plausible; the specific practice is not recorded |
| 4 | `tratamento de erros em APIs REST` | 13, 30 | The specific practice is not recorded |
| 5 | `Prisma` | 15-16, 31 | Sequelize and Drizzle ORM are facts; Prisma is not |
| 6 | `TypeORM` | 16, 31-32 | Sequelize and Drizzle ORM are facts; TypeORM is not |
| 7 | `Linux` | 18, 48 | Docker, Kubernetes, GCP and ArgoCD are facts; Linux is not recorded |
| 8 | `observabilidade` | 19, 33 | Datadog RUM is a fact; the brief requires the token to stay marked |

All 8 need Lucas's yes or no before this package is sent. Every one is an
ecosystem token `CLAUDE.md` section 4 explicitly authorises claiming, and each
is placed in `Skills` **and** in one bullet, exactly as section 4 requires.

### Numbers

Every number on the document traces to `DOSSIER.md`:

| Number | Raw line | Dossier id |
|---|---|---|
| 25% authentication friction | 30 | D3 |
| 7% release risk | 33 | D5 |
| 15% wrong bookings | 35 | D2 |
| 20% invoice throughput | 47 | L2 |
| 26% order and integration capacity | 57 | P2 |

**No number on the document fails to trace to `DOSSIER.md`.**

One quantity is derived rather than recorded:

- `mais de 5 anos` (Summary, raw 6). Not stated in `DOSSIER.md`.
  Arithmetically consistent with the LinkedIn ground truth: `Mar 2021` to
  2026-09-02 is 5 years 6 months. Consistent, not a recorded fact.

### Prose claims not traceable to the dossier, and unmarked

1. `sustentando leituras e escritas de reservas com consistência` (DexCare,
   raw 32). `DOSSIER.md` records PostgreSQL, Redis, Sequelize and Drizzle ORM
   as [FACT-OBSERVED], and no consistency claim.
2. `e-commerce do Magazine Luiza` (Luizalabs, raw 46). `DOSSIER.md` confirms
   the fiscal / NF-e / SEFAZ domain as [FACT] and does not carry the word
   `e-commerce`. Magazine Luiza being an e-commerce retailer is common
   knowledge; it is not observable from this dossier, so I record it rather
   than assert it.
3. `permitindo entregas diárias de código de alta qualidade` (DexCare, raw
   36-37). `DOSSIER.md` records the agent environments and the quality
   enforcement as [FACT, Lucas 2026-09-01]; `entregas diárias` is the
   dossier's own framing ("uses Claude Code and Codex in daily delivery"), so
   this one is **supported**. Recorded only because `alta qualidade` is a
   qualifier.

### Claims that are facts and correctly unmarked

Recorded so the marking can be audited both ways: `Inglês Avançado/C1` and the
daily English work with a US team (raw 8-9) are [FACT, Lucas 2026-09-01];
`Express`, `Koa`, `Sequelize`, `Drizzle ORM`, `PostgreSQL`, `Redis`, `Auth0`,
`Datadog`, `LaunchDarkly`, `OpenFeature`, `RabbitMQ` at DexCare are
[FACT-OBSERVED]; `microservices` and `arquiteturas distribuídas` at Luizalabs
are [FACT] ("Distributed tax microservices"); `BullMQ`, `Docker`,
`Kubernetes`, `GCP`, `ArgoCD`, `Vitest`, `Jest` are [FACT]; `Agentic
workflows`, `Claude Code` and `Codex` are [FACT].

### Not observable, and needing Lucas before applying

- **`dedicação integral e exclusiva`.** The posting requires it and says it
  may be verified during the process. `DOSSIER.md` has an empty
  `Notice period:` field and records no availability date. Not a CV question.
  It belongs in the apply note's screening answers.
- **`Contratação imediata`.** The posting headline says it. Same open field.

---

## Fix list for the Architect

none
