# ATS Analysis — brasil-em-dobro-backend-senior-pt.pdf vs brasil-em-dobro-backend-senior
Segment: br-pj   Date: 2026-09-02

Judged on extractions the analyzer regenerated from the PDF under test:
`pdftotext -layout` and `pdftotext` on
`resumes/brasil-em-dobro-backend-senior-pt.pdf` (1 page, letter). Source
cross-read: `resumes/brasil-em-dobro-backend-senior-pt.tex`.
Posting text: `jobs/brasil-em-dobro-backend-senior.md` (LinkedIn job
`4459998340`, Brasil em Dobro, captured by Kestrel, hunt 2026-09-02-b).
Titles, companies and dates checked against `DOSSIER.md` **LinkedIn ground truth**.
Architect's own marker list read: `reports/brasil-em-dobro-backend-senior-draft.md`.

Rule versions applied: `CLAUDE.md`, `RUBRIC.md` and `CV-SPEC.md` as of 2026-09-02.

This is our rubric. It is not a vendor score. No ATS emits these numbers.

## Verdict

**PASSES ALL GATES.** No blocking gate fails.

| Gate | Result |
|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, reported not blocking) |
| Gate 1 — Knockouts | **PASS** — no FAIL row |
| Gate 2 — Retrieval coverage | **24 / 100** (stuffing penalty 0) |
| Gate 3 — Human scan | **92 / 100** |

Every required knowledge token the posting names is present verbatim:
`Typescript`, `Fastify`, `Docker`, `Mysql`, `SQL`, `Git`. The `Diferencial`
token `AWS` is present too. Gate 2 sits at 24 because the posting's
requirement list is short and the document carries a large amount of material
this posting never asks for, which is a denominator effect, not a miss.

Two conditions need Lucas before this is sent, and neither is a document
defect. The posting says **"Esperamos que você trabalhe somente para o Brasil
em Dobro, ou seja, não fará nenhum tipo de trabalho freelancer"** and **"Você
precisa ter o seu computador próprio para começar a trabalhar"**. Neither is
observable from `DOSSIER.md`, and neither belongs on a CV. They belong in the
apply note's screening answers.

---

## Gate 0 — Parse integrity

`pdfinfo` reports **1 page**. Raw extraction is 74 lines, layout 53.

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Complete prose. Contact block, four sections, four Experience blocks and one Education block all present |
| 0.2 | Glyph integrity | PASS | Measured by codepoint in Python, not by shell grep. Zero `\x00`, zero `U+FB00-FB06` ligature codepoints, zero `U+FFFD`, zero `?`. The only character above `U+00FF` is `U+2022 BULLET`, 12 of them. Ligature-bearing words intact: `fiscais` 3, `fluxos` 3, `funcionalidades` 1, `configurações` 1, `Distribuidora` 2. The document contains no `ff` word, so that arm of 0.2 is not exercised |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, not a header or footer: `Vitória, ES, Brasil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email and LinkedIn URL all present. No UTC offset, no time-zone overlap sentence |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 11, 19, 67: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, each a standalone line. PT allowlist, Gate 0.4. Source strings are `\section{Resumo}`, `{Habilidades}`, `{Experi\^encia}`, `{Forma\c{c}\~ao}`; the uppercase is `\scshape` rendering, which the gate allows |
| 0.5 | Employment-block segmentation | FAIL — header only | Raw splits each role header into `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remoto`. **No two roles merge. No role splits into two employment entries.** Four Experience blocks and one Education block, intact and in order. Both Lippaus entries repeat the company name, so the promotion segments unambiguously. Cause is the `tabular*` in `\resumeSubheading` |
| 0.6 | Date parseability | FAIL — header only | Every date sits one blank line below its title, not on the same line. Format correct in all five blocks: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Separator verified by Unicode category `Pd`: the only dash in the whole document is `U+002D HYPHEN-MINUS` |
| 0.7 | Reading order | FAIL — header only | Raw order per role header: company, title, dates, location. Layout: company+dates, title+location. **Zero content blocks reorder.** The name block reads in the same order in both extractions |
| 0.8 | No forbidden constructs | FAIL — header only | The `tabular*` role header. No table elsewhere, no text box, no image of text, no icon, no photo |

**All four FAILs trace only to the two-column role header**, the accepted
exception in `CV-SPEC.md` item 2 and `RUBRIC.md`. Reported, not blocking. I
searched for any other cause of 0.5-0.8 and found none.

**Gate 0 verdict: PASS.**

### LinkedIn ground-truth cross-check — PASS

Character for character against the `DOSSIER.md` LinkedIn block.

| Block | Resume text (raw lines) | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` (20) / `Senior Software Engineer` (21) / `Jan 2026 - Present` (23) | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | `Luizalabs` (38) / `Mid-level Software Engineer` (39) / `Jan 2024 - Jan 2026` (41) | identical | YES |
| 3 | `Lippaus Distribuidora` (49) / `Mid-level Software Engineer` (50) / `Jan 2023 - Jan 2024` (52) | identical | YES |
| 4 | `Lippaus Distribuidora` (58) / `Entry-level Fullstack Software Engineer` (59) / `Mar 2021 - Jan 2023` (61) | identical | YES |
| Education | `FAESA` (68) / `Bacharelado em Sistemas de Informação` (69) / `Feb 2022 - Dec 2025` (71) | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — start and end months identical; ASCII hyphen per `CV-SPEC.md` item 5 |

Company spelling `Luizalabs` correct. Both Lippaus roles present and separate.
Role locations correct per `CLAUDE.md` section 3: `Remoto` for DexCare and
Luizalabs, `Vitória, ES, Brasil` for both Lippaus roles. Degree is
Information Systems at FAESA.

### Forbidden-token grep

```
grep -inE 'ruby|rails|sidekiq|activerecord|activejob|rspec|devise|pundit|hotwire'
```
**Zero hits** in the `.tex` and zero in both extractions. **Zero Ruby or Rails
tokens confirmed.**

```
grep -o UNVERIFIED resumes/brasil-em-dobro-backend-senior-pt.tex | wc -l
```
**9 markers**, covering **5 distinct claims**: `Fastify`, `MySQL`, `Mysql`,
`SQL`, `Git`. The raw extraction carries the same 9. The Architect's draft
lists exactly those 5. That claim is factually correct. This is the lowest
marker count of the hunt so far.

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | **Not stated.** The posting names no contract shape. LinkedIn shows `Full-time`. Apply destination is a `forms.gle` form | **not stated** — the document is silent on contract shape, correctly. `DOSSIER.md` records `PJ with own CNPJ, US contractor (W-8BEN), CLT, EOR/Deel-style employment. All acceptable. [FACT]`, so any shape is available if asked |
| Location | Location as shown: `Brazil`. Workplace type as shown: `Remote`. The posting text names no city and no mandatory location | **PASS** — contact line reads `Vitória, ES, Brasil` (raw 3), and `Brasil` appears three more times as a role and education location |
| Time-zone overlap | Not stated in the posting | **not stated** — and never a FAIL (`CLAUDE.md` section 3, `RUBRIC.md` Gate 1) |
| Minimum years of experience | **Not stated.** The title says `Senior`; the knowledge bar reads `Conhecimento (intermediário)` | **not stated.** The document carries `Senior Software Engineer` at raw 2 and 21, and `mais de 5 anos` at raw 6 |
| English proficiency | `Inglês Intermediário`, listed under `Qualificações` | **PASS** — raw 7-9: `Eu tenho Inglês Avançado/C1, acima do requisito de Inglês Intermediário, e trabalho diariamente em inglês com uma equipe dos EUA`. `DOSSIER.md` records `Advanced / C1. Daily English-only work with US teams at DexCare. [FACT, Lucas 2026-09-01]`. Stated explicitly, so no absence FAIL |
| Degree requirement | Not stated in the posting | **not stated.** The document carries `Bacharelado em Sistemas de Informação`, FAESA |
| **Exclusividade** | `Esperamos que você trabalhe somente para o Brasil em Dobro, ou seja, não fará nenhum tipo de trabalho freelancer` | **Not observable. Needs Lucas.** `exclusiv` 0 hits and `freelanc` 0 hits in the document, correctly: no CV can assert this, and `CLAUDE.md` rule 1 requires DexCare to print as `Jan 2026 - Present`. `DOSSIER.md` leaves `Notice period:` empty. **Not a FAIL and not a document defect.** It belongs in the apply note's screening answers |
| **Computador próprio** | `Você precisa ter o seu computador próprio para começar a trabalhar` | **Not observable. Needs Lucas.** Not a CV field. **Not a FAIL.** Screening answer |

Required-skill presence, verbatim in the raw extraction. Required is taken
from the posting's own line `Conhecimento (intermediário)`.

| Requirement (posting's words) | Present verbatim? |
|---|---|
| `Typescript` | YES — Skills raw 13 in the posting's own spelling `Typescript`; `TypeScript` in Summary (6) and in DexCare bullet 1 (26) |
| `Fastify` | YES — Skills (12), DexCare bullet 1 (26). Marked `[UNVERIFIED]` in both |
| `Docker` | YES — Skills (15), Luizalabs bullet 3 (47) |
| `Mysql (SQL)` | YES — both spellings. `MySQL` Skills (14) and DexCare bullet 4 (31); `Mysql` Skills (14); `SQL` Skills (14) and bullet 4 (31). All marked `[UNVERIFIED]` |
| `Git` | YES — Skills (15), DexCare bullet 5 (33). Marked `[UNVERIFIED]` in both |
| `Inglês Intermediário` | YES — Summary (7-9), exceeded |
| `Comunicação via texto clara e rápida` | Soft skill, discarded from Gate 2 per Step 1. Nearest document evidence: `Liderei o escopo de projetos e a comunicação com stakeholders` (56). The **texto** and **rápida** qualifiers are not claimed, correctly |
| `Consegue trabalhar de forma independente` | Soft skill, discarded. Not claimed |
| `Curiosidade profunda`, `Aprendizado rápido, por conta própria` | Soft skills, discarded. Not claimed |
| `trabalhe somente para o Brasil em Dobro` | **NO**, correctly. See the Gate 1 row |
| `computador próprio` | **NO**, correctly. See the Gate 1 row |
| `familiaridade com serviços da AWS` (Diferencial) | YES — Skills (15), DexCare bullet 4 (32) as `AWS SDK v3` |

**Gate 1 verdict: PASS.** No FAIL row.

---

## Gate 2 — Retrieval coverage: 24 / 100

### Scoring conventions used, stated so this is reproducible

Carried forward from `reports/goodway-global-fullstack-gate.md`,
`reports/brivia-fullstack-pj-gate.md`,
`reports/conta-simples-engenheira-software-senior-gate.md`,
`reports/diana-neves-fullstack-314-26-gate.md` and
`reports/kotai-backend-nodejs-nestjs-gate.md`.

1. **The posting draws its own line.** `required` comes from the job title,
   the role description sentence, and the line `Conhecimento (intermediário)`.
   `preferred` comes from the line `Diferencial` and from the technical nouns
   inside `Responsabilidades`, which the posting labels as decision areas, not
   as knowledge requirements.
2. A `Skills` **group label** counts as a `Skills` placement, rung 1. Rung 3
   needs the token inside an Experience bullet.
3. Inflections count for rung 3 where the stem is the posting's stem.
4. Where the posting lists alternates in one clause (`Mysql (SQL)`), the
   clause scores **once**, at its best-covered member.
5. For a token with no available `Skills` rung, or with `Skills` plus
   `Summary` but no bullet, the ladder has no rung. I score it **2** and mark
   the row.
6. Soft skills are discarded per Step 1: `Comunicação via texto clara e
   rápida`, `Consegue trabalhar de forma independente`, `Curiosidade
   profunda`, `Aprendizado rápido, por conta própria`. They are not retrieval
   tokens. `Inglês Intermediário`, `exclusividade` and `computador próprio`
   are graded at Gate 1 only, not double-counted here.
7. The numerator is the unweighted sum of points and the denominator is
   `count × weight × 4`, exactly as the rubric's Step 3 formula is literally
   written and as the earlier reports computed it.
8. Step 4 frequency is measured with a whole-word, Unicode-aware regex, and a
   compound containing a shorter token counts toward the shorter token's
   total.

### Required tokens — weight 3, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| R1 | `Typescript` | yes (13, the posting's exact spelling) | yes (26) | **yes** (6) | 4 | Full ladder. Both spellings present |
| R2 | `Node.js` (job title) | yes (12) | yes (26) | **yes** (6) | 4 | Full ladder |
| R3 | `Fastify` | yes (12) | yes (26) | no | 3 | Marked `[UNVERIFIED]` in both places. The posting also misspells it `Fasftify` once in `Responsabilidades`; the Architect correctly used the title's spelling |
| R4 | `Docker` | yes (15) | yes (47) | no | 3 | Luizalabs bullet. `DOSSIER.md` [FACT] |
| R5 | `Mysql (SQL)` | yes (14, all three spellings) | yes (31) | no | 3 | Convention 4, scored once. `PostgreSQL` is the `DOSSIER.md` fact carrying the clause; `MySQL`, `Mysql` and `SQL` are marked |
| R6 | `Git` | yes (15) | yes (33) | no | 3 | Marked in both places |
| R7 | `back-end` / `backend` (job title, `aplicações back-end`) | yes (12, the `Backend:` group label) | **no** | **yes** (6, `aplicações backend`) | 2 | Convention 5. **No bullet carries the word.** See defect 1 |
| R8 | `APIs` (`integração das APIs`) | yes (12, `REST APIs`) | yes (29, `REST APIs multi-tenant`) | **yes** (7, `APIs`) | 4 | Full ladder |
| R9 | `testes` (`integração das APIs e testes`) | **no** (the group label is `Mensageria e qualidade`; `Vitest` and `Jest` are tools, not the token) | yes (33) | no | 2 | Convention 5. See defect 2 |

Required points earned: **28**. Required denominator: 9 × 3 × 4 = **108**.

### Preferred tokens — weight 1, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| P1 | `serviços da AWS` (Diferencial) | yes (15) | yes (32, `AWS SDK v3`) | no | 3 | `DOSSIER.md` [FACT-OBSERVED] |
| P2 | `arquitetura` | no | no | no | **0** | `arquitet` 0 hits in the whole document. **Recoverable without any new claim.** See defect 3 |
| P3 | `frameworks` | no | no | no | **0** | The word is absent. Express, Koa and Fastify are named, the category word is not |
| P4 | `usabilidade` | no | no | no | **0** | 0 hits. `DOSSIER.md` records no usability work. Correctly not claimed |
| P5 | `acessibilidade` | no | no | no | **0** | 0 hits. `DOSSIER.md` records no accessibility work. Correctly not claimed |

Preferred points earned: **3**. Preferred denominator: 5 × 1 × 4 = **20**.

### Step 3

```
coverage = 100 * (28 + 3) / (108 + 20) = 100 * 31 / 128 = 24.22 -> 24
```

### Step 4 — stuffing penalty: 0

**(a) Posting tokens in `Skills` with no supporting evidence in Experience.**
None. Every one of `Typescript`, `Fastify`, `Docker`, `MySQL`, `SQL`, `Git`
and `AWS` also appears inside an Experience bullet, which is exactly what
`CLAUDE.md` section 4 requires of a claimed ecosystem token. **Penalty 0.**

Five `Skills` entries have no bullet behind them anywhere:

| Token | Raw line | Asked for by this posting? | Penalty |
|---|---|---|---|
| `Redis` | 14 | no | 0 |
| `RabbitMQ` | 16 | no | 0 |
| `AMQP` | 16 | no | 0 |
| `Datadog` | 16 | no | 0 |
| `Agentic workflows` | 17 | no | 0 |

No penalty under the treatment applied in
`reports/brivia-fullstack-pj-gate.md` and
`reports/kotai-backend-nodejs-nestjs-gate.md`: the penalty prices a human
reaction to padding against **this** posting's asks, and this posting asks for
none of the five. They are still five unsupported entries, recorded in
defect 5.

**(b) Frequency, −5 each at 4 or more appearances.** Whole-word counts,
Unicode-aware boundaries, convention 8:

`Typescript` 3, `Node.js` 3, `React` 3, `Go` 3, `APIs` 3, `BullMQ` 3,
`MySQL`+`Mysql` 3 combined, `Inglês` 3, and every other measured term at 2
or 1. **No term reaches 4.** The `CV-SPEC.md` 3-appearance cap holds exactly,
on every term.

Total penalty: **0**.

**Gate 2 final: 24 / 100.**

### Missing required tokens

1. `back-end` / `backend` in an Experience bullet — `Skills` label and
   `Summary` only.
2. `testes` in `Skills` — one Experience bullet only.

Missing preferred: `arquitetura`, `frameworks`, `usabilidade`,
`acessibilidade`.

### Ceiling, stated honestly

- Putting `backend` inside the first DexCare bullet lifts R7 from 2 to 3.
- Adding `Testes` as a `Skills` group label, or the word `testes` beside
  `Vitest | Jest`, lifts R9 from 2 to 3.
- `arquitetura` is the single largest free gain and needs **no new claim**:
  `DOSSIER.md` records `Distributed tax microservices` at Luizalabs as [FACT]
  and `event-driven booking` at DexCare as [FACT-OBSERVED]. Naming the word in
  `Skills` and in one bullet takes P2 from 0 to 3.
- With all three: `coverage = 100 * (30 + 6) / 128 = 28`.
- `usabilidade` and `acessibilidade` must stay at 0. `DOSSIER.md` records
  neither, and the Architect's draft says so explicitly. **Do not claim them.**
  `frameworks` as a bare category word is not worth a line.

**28 is the honest ceiling on this posting**, and 24 is already above the
hunt's Conta Simples (0), Diana Neves (6) and Brivia (22) results. The score is
held down by a short requirement list against a document carrying a lot of
material this posting never asks for. That is a denominator effect, not a
retrieval miss: **every token the posting actually names is present.**

---

## Gate 3 — Human scan: 92 / 100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15/15 | `Senior Software Engineer` at raw line **2 of 74** = 2.7%, as a headline under the name, again in the Summary (6) and as the DexCare title (21). The posting's title is `Desenvolvedor Backend Senior - Node.js / Typescript`; `CLAUDE.md` rule 1 binds the CV to the LinkedIn English string, and the Summary carries `backend`, `TypeScript` and `Node.js` on the same line |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 15/20 | DexCare bullet 1 (26) carries `TypeScript`, `Node.js`, `Fastify` — the posting's three core tokens in one line, the strongest possible opening. Bullet 3 (29) carries `REST APIs` and 25%. **Minus 5: bullet 2 (28) is the Epic EMR time-slot bullet and carries no posting token at all.** `MySQL`/`SQL` sit at bullet 4 (31), `Git` at bullet 5 (33), `Docker` down in Luizalabs (47). A recruiter scanning three lines sees two of the five knowledge tokens |
| 3.3 | Voice rule | 15/15 | 12 of 12 bullets pass. Full table below |
| 3.4 | At least 3 bullets with a real, defensible number | 15/15 | Five: 15% (28), 25% (29), 33% (35), 20% (46), 26% (55). **All five trace to `DOSSIER.md`** bullet metrics D2, D3, D7, L2, P2. This document keeps the 33% SPI figure, the strongest in the dossier, which the Kotai tailoring dropped |
| 3.5 | Length | 10/10 | `pdfinfo` reports 1 page |
| 3.6 | No unsupported buzzwords | 10/10 | Zero hits for `proativo`, `apaixonado`, `dinâmico`, `comunicativo`, `autodidata`, `resiliente`, `protagonista`, and for the EN list `team player`, `results-driven`, `passionate`, `hands-on`. The posting's soft block (`Curiosidade profunda`, `Aprendizado rápido`, `forma independente`) was correctly **not** mirrored into prose |
| 3.7 | Skills grouped by category | 10/10 | Six labelled groups (raw 12-17): `Backend`, `Linguagens e frontend`, `Dados`, `Cloud e entrega`, `Mensageria e qualidade`, `Ferramentas de IA`. Every label is a real technology category. No `keywords` dump label anywhere |
| 3.8 | Scannable | 2/5 | Consistent inter-role spacing, bold company, italic title, one column, full width, headline title anchoring the top. **Minus 1: 9 `[UNVERIFIED]` markers**, three of them inside a single `Dados` line (14) which then wraps. **Minus 1: `MySQL [UNVERIFIED] \| Mysql [UNVERIFIED] \| SQL [UNVERIFIED]` are three near-identical adjacent entries in one `Skills` line.** A machine reads three tokens; a human reads keyword padding. This is the most visible cosmetic defect on the page. **Minus 1: verb monotony plus a thin tail.** `Construí` opens 4 of 12 bullets (26, 31, 33, 64), and the Lippaus Entry-level role carries a **single** bullet for a 22-month period while DexCare carries six |

**Gate 3 total: 92/100.**

The 3.8 deduction is against the document **as built**. `CLAUDE.md` section 4
requires the markers, and they disappear once Lucas confirms or strikes each
claim. It is recorded so nobody sends this PDF unedited.

## Voice check (explicit, per `CLAUDE.md` section 9 and `CV-SPEC.md`)

Leading token of every Experience bullet, read from the raw extraction:

| Raw line | Leading verb | Verdict |
|---|---|---|
| 26 | Construí | 1st person past, subject omitted, OK |
| 28 | Integrei | OK |
| 29 | Construí | OK |
| 31 | Modelei | OK |
| 33 | Construí | OK |
| 35 | Ajudei | OK |
| 44 | Construí | OK |
| 46 | Migrei | OK |
| 47 | Implantei | OK |
| 55 | Processei | OK |
| 56 | Liderei | OK |
| 64 | Construí | OK |

- Bullets that break the rule: **none**. 12 of 12 pass.
- Bullets starting with `Eu` or `I`: **none**. All four `Eu` occurrences are in
  the Summary.
- Present tense in a bullet: **none**.
- `Responsável por` or third person: **none**.
- Summary uses `Eu`: **yes**, four times — `Eu sou`, `Eu desenvolvo`,
  `Eu tenho`, `Eu integro` (raw 6-9).
- Every bullet names a technology or a delivery outcome. Five of twelve carry
  a number.

**Voice: PASS.**

---

## Defects, ranked by cost

1. **`backend` never reaches a bullet** — Gate 2 R7, worth 1 point on a
   required token, and it is the posting's own job-title noun. It is in the
   `Backend:` `Skills` label (12) and in the Summary (6). The first DexCare
   bullet already says `Construí serviços TypeScript sobre Node.js, Fastify,
   Express e Koa`; `serviços backend` costs one word.
2. **`arquitetura` is absent from the whole document** — Gate 2 P2, 0 of 4,
   and the **largest free gain on this posting**. It needs no new claim:
   `DOSSIER.md` records `Distributed tax microservices` at Luizalabs [FACT]
   and `event-driven booking` at DexCare [FACT-OBSERVED]. The Luizalabs
   bullet at raw 44 (`microsserviços fiscais distribuídos`) is the natural
   home for the posting's own word.
3. **`MySQL [UNVERIFIED] | Mysql [UNVERIFIED] | SQL [UNVERIFIED]` in one
   `Skills` line** — Gate 3.8, part of the minus 3, raw 14. The Architect
   added the second spelling to preserve the posting's exact glyph run. It
   buys nothing a case-insensitive parser does not already give, and it costs
   a human reader. Recommend dropping `Mysql [UNVERIFIED]` and keeping
   `MySQL [UNVERIFIED] | SQL [UNVERIFIED]`. Gate 2 is unaffected: R5 scores
   once by convention 4.
4. **`testes` reaches no `Skills` rung** — Gate 2 R9, worth 1 point. The group
   label is `Mensageria e qualidade`; `Vitest` and `Jest` are tools, not the
   posting's token. Renaming the group, or adding the bare word, fixes it.
5. **Five `Skills` entries with no bullet anywhere** — `Redis` (14),
   `RabbitMQ` (16), `AMQP` (16), `Datadog` (16), `Agentic workflows` (17). No
   Gate 2 penalty, because this posting asks for none of them, but they are
   five unsupported entries on a document that already carries 9 markers. On a
   posting this short, they are also the cheapest source of the line space
   defects 1, 2 and 4 need.
6. **Bullet 2 of the current role carries no posting token** — Gate 3.2, the
   minus 5. The Epic EMR time-slot bullet (28) is a strong bullet and a real
   15% number, but it occupies the second of the three lines a recruiter
   actually reads on a Fastify/MySQL/Docker/Git posting. Swapping it below
   the `MySQL`/`SQL` bullet would put three posting tokens in the first three
   lines.
7. **Three numbers were cut to hold one page** — content loss, no rubric
   deduction. The Luizalabs fiscal dashboards bullet (`DOSSIER.md` **L3,
   18%**), the Lippaus multi-tenant platform bullet (P1) and the Lippaus
   internal dashboards bullet (E1) are gone, and the DexCare feature-flag
   bullet (D5, 7%) with them. The document keeps five numbers including the
   33% SPI figure. Defensible, and worth Lucas seeing.
8. **The Lippaus Entry-level role carries one bullet** — Gate 3.8, part of the
   minus 3. A 22-month role rendered as a single line next to a six-bullet
   DexCare block makes the page bottom-thin.
9. **Verb monotony** — Gate 3.8, part of the minus 3. `Construí` opens 4 of 12
   bullets (26, 31, 33, 64).
10. **`e-commerce do Magazine Luiza`** — truth handling, raw 45. `DOSSIER.md`
    confirms the fiscal / NF-e / SEFAZ domain as [FACT] and does not carry the
    word `e-commerce`. Unmarked. Same finding as the base and the other
    tailorings of this hunt.
11. **`entregando reservas de consultas em tempo real`** — truth handling, raw
    26-27. `DOSSIER.md` records `event-driven booking, healthcare scheduling
    at scale` [FACT-OBSERVED]. It records no real-time latency claim.
    Unmarked.
12. **`acima do requisito de Inglês Intermediário` in the Summary** — raw 8.
    The sentence quotes this posting's own requirement text back at the
    reader, which reads as a document written for one ad. The underlying fact
    (`Inglês Avançado/C1`) is a `DOSSIER.md` [FACT] and carries Gate 1 on its
    own. Observation for Lucas, not a rubric deduction.
13. **`tabular*` role header, four Gate 0 findings** — reported, not blocking,
    by Lucas's 2026-09-01 decision. No action.
14. **`Present` and English month abbreviations in a Portuguese document** —
    observation only. `CLAUDE.md` rule 1 outranks language consistency.

---

## Claims I could not verify

Traced against `DOSSIER.md`. I do not delete these and I do not defend them.
Lucas decides.

### The 9 `[UNVERIFIED]` markers, all 5 distinct claims

Counted in both the `.tex` and the raw extraction. Each claim is marked in
`Skills` and again in its Experience bullet, except `Mysql`, which is a
`Skills`-only spelling variant.

| # | Claim | Raw lines | Architect's stated reason |
|---|---|---|---|
| 1 | `Fastify` | 12, 26 | `DOSSIER.md` confirms Node.js, Express and Koa at DexCare, not Fastify |
| 2 | `MySQL` | 14, 31 | `DOSSIER.md` confirms PostgreSQL, DynamoDB and Redis, not MySQL |
| 3 | `Mysql` | 14 | Spelling variant kept to mirror the posting's glyph run. Same unconfirmed claim as 2 |
| 4 | `SQL` | 14, 31 | PostgreSQL is a fact; the bare `SQL` token is not separately recorded |
| 5 | `Git` | 15, 33 | The dossier records the agent environments, lint and testing, not Git by name |

All 5 need Lucas's yes or no before this package is sent. Every one is an
ecosystem token `CLAUDE.md` section 4 explicitly authorises claiming, and each
is placed in `Skills` **and** in one bullet, exactly as section 4 requires.
The Maestro brief lists `Fastify`, `MySQL` and `Git` under
`Claim marked [UNVERIFIED]:` and names no gaps. The Architect added `Mysql`
and `SQL` beyond the brief, which is consistent with the same rule.

### Numbers

Every number on the document traces to `DOSSIER.md`:

| Number | Raw line | Dossier id |
|---|---|---|
| 15% wrong bookings | 28 | D2 |
| 25% authentication friction | 29 | D3 |
| 33% new-client friction (Shared Platform Initiative) | 35 | D7 |
| 20% invoice throughput | 46 | L2 |
| 26% order and integration capacity | 55 | P2 |

**No number on the document fails to trace to `DOSSIER.md`.**

One quantity is derived rather than recorded:

- `mais de 5 anos` (Summary, raw 6). Not stated in `DOSSIER.md`.
  Arithmetically consistent with the LinkedIn ground truth: `Mar 2021` to
  2026-09-02 is 5 years 6 months. Consistent, not a recorded fact.

### Prose claims not traceable to the dossier, and unmarked

1. `entregando reservas de consultas em tempo real` (DexCare, raw 26-27).
   `DOSSIER.md` records `event-driven booking` and `healthcare scheduling at
   scale` as [FACT-OBSERVED], and no real-time claim.
2. `e-commerce do Magazine Luiza` (Luizalabs, raw 45). `DOSSIER.md` confirms
   the fiscal / NF-e / SEFAZ domain as [FACT] and does not carry the word
   `e-commerce`. Magazine Luiza being an e-commerce retailer is common
   knowledge; it is not observable from this dossier, so I record it rather
   than assert it.
3. `sustentando leituras e escritas ligadas a S3 e RDS via AWS SDK v3`
   (DexCare, raw 31-32). `S3`, `RDS Signer` and `AWS SDK v3` are all
   [FACT-OBSERVED]. **Supported.** Recorded only because `sustentando` is a
   qualifier the dossier does not phrase.
4. `permitindo entregas diárias de código de alta qualidade` (DexCare, raw
   33-34). `DOSSIER.md` records the agent environments and the quality
   enforcement as [FACT, Lucas 2026-09-01], and `daily delivery` is the
   dossier's own framing. **Supported.** Recorded only because `alta
   qualidade` is a qualifier.

### Claims that are facts and correctly unmarked

Recorded so the marking can be audited both ways: `Inglês Avançado/C1` and the
daily English work with a US team (raw 7-9) are [FACT, Lucas 2026-09-01];
`Express`, `Koa`, `PostgreSQL`, `Redis`, `Sequelize`, `Drizzle ORM`, `Auth0`,
`Datadog`, `OpenAPI/Swagger`, `AWS SDK v3`, `Epic EMR`, `RabbitMQ` and `AMQP`
at DexCare are [FACT-OBSERVED]; the Shared Platform Initiative bullet is
[FACT, D7]; `Go` and `JavaScript` at Luizalabs, the SEFAZ / NF-e domain,
`BullMQ`, `Docker`, `Kubernetes`, `GCP`, `ArgoCD`, `Vitest`, `Jest` are
[FACT]; `React Native` and the stakeholder-communication bullet at Lippaus are
[FACT]; `Claude Code`, `Codex` and `Agentic workflows` are [FACT].

### Not observable, and needing Lucas before applying

- **Exclusividade.** `Esperamos que você trabalhe somente para o Brasil em
  Dobro, ou seja, não fará nenhum tipo de trabalho freelancer`. Lucas holds a
  current full-time role at DexCare, which the CV must print as
  `Jan 2026 - Present` under `CLAUDE.md` rule 1. `DOSSIER.md` has an empty
  `Notice period:` field. Not a CV question. It belongs in the apply note's
  screening answers.
- **Computador próprio.** `Você precisa ter o seu computador próprio para
  começar a trabalhar`. Not observable from `DOSSIER.md`. Screening answer.
- **Contract shape.** The posting names none, and the apply destination is a
  `forms.gle` form. `DOSSIER.md` records PJ, CLT, W-8BEN and EOR as all
  acceptable [FACT], so no shape is a blocker.

---

## Fix list for the Architect

none
