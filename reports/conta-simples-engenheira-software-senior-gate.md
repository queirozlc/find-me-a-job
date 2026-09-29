# ATS Analysis — conta-simples-engenheira-software-senior-pt.pdf vs conta-simples-engenheira-software-senior
Segment: br-pj   Date: 2026-09-02

Judged on extractions the analyzer regenerated from the PDF under test:
`pdftotext -layout` and `pdftotext` on
`resumes/conta-simples-engenheira-software-senior-pt.pdf` (28498 bytes, built
2026-09-02 19:25). Source cross-read:
`resumes/conta-simples-engenheira-software-senior-pt.tex`.
Posting text: `jobs/conta-simples-engenheira-software-senior.md`
(LinkedIn job `4459962289`, captured by Kestrel, hunt 2026-09-02-b).
Titles, companies and dates checked against `DOSSIER.md` **LinkedIn ground truth**.
Architect's own marker list read:
`reports/conta-simples-engenheira-software-senior-draft.md`.

Rule versions applied: `CLAUDE.md` and `RUBRIC.md` as of 2026-09-02, including
the 2026-09-02 changes that (a) forbid a time-zone overlap statement on the CV
and make its absence `not stated`, never a FAIL, (b) set the Lippaus role
location to `Vitória, ES, Brazil`, and (c) `CLAUDE.md` section 4 ecosystem
tokens: claimed **in Skills and in one bullet**, marked `[UNVERIFIED]`.

This is our rubric. It is not a vendor score. No ATS emits these numbers.

## Verdict

**PASSES ALL GATES.** No blocking gate fails.

| Gate | Result |
|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, reported not blocking) |
| Gate 1 — Knockouts | **PASS** — no FAIL row. Four rows are `not stated` in the posting |
| Gate 2 — Retrieval coverage | **0 / 100** (15 before the stuffing penalty, −45 penalty, clamped at 0) |
| Gate 3 — Human scan | **90 / 100** |

The document parses cleanly, its voice is correct, every number traces to
`DOSSIER.md`, and every title and date matches LinkedIn character for
character. It blocks on nothing.

Gate 2 at 0 is the finding that matters. The cause is a single line: the
Architect put ten posting tokens into a `Skills` line labelled
`Palavras-chave da vaga` and placed **none of them in an Experience bullet**.
`CLAUDE.md` section 4 requires both halves: "placed in Skills **and in one
bullet** where the history makes it plausible". Half the rule was applied. The
rubric Step 4 penalty for a `Skills` token with no Experience evidence then
fires eight times. Two of the ten tokens did not even need an `[UNVERIFIED]`
marker: `React Native` is a `DOSSIER.md` **[FACT]** and `NoSQL` is carried by
`DynamoDB`, a **[FACT-OBSERVED]**. See defects 1 to 3.

---

## Gate 0 — Parse integrity

`pdfinfo` reports **1 page**. Raw extraction is 81 lines.

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Complete prose. Contact block, four sections, four Experience blocks and one Education block all present |
| 0.2 | Glyph integrity | PASS | Measured by codepoint in Python, not by shell grep. Zero `\x00`, zero `U+FB00-FB04` ligature codepoints, zero `U+FFFD`, zero stray `?`. The only characters above U+00FF are `U+2022 BULLET`. Ligature-bearing words intact: `fiscais` 4, `fluxo` 3, `flags` 1, `configurações` 1, `confiável` 1, `notificações` 1, `funcionalidades` 1, `Distribuidora` 2 |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, not a header or footer: `Vitória, ES, Brasil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email and LinkedIn URL all present. No UTC offset, no time-zone overlap sentence, per `CLAUDE.md` section 3 as amended 2026-09-02 |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 11, 20, 74: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, each a standalone line. PT allowlist, Gate 0.4. Uppercase rendering allowed. `\section`, not `\section*` |
| 0.5 | Employment-block segmentation | FAIL — header only | Raw splits each role header into `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remoto`. **No two roles merge. No role splits into two employment entries.** Four Experience blocks and one Education block, all intact and in the right order. Both Lippaus entries repeat the company name, so the promotion segments unambiguously. Cause is the `tabular*` in `\resumeSubheading`, `tex:41-44` |
| 0.6 | Date parseability | FAIL — header only | Every date sits one blank line below its title, not on it. Format correct in all five blocks: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Separator verified by Unicode category `Pd`: the only dash in the whole document is `U+002D HYPHEN-MINUS`. No EN DASH anywhere |
| 0.7 | Reading order | FAIL — header only | Raw order per header: company, title, dates, location. Layout order: company+dates, title+location. **Zero content blocks reorder.** Bullet order and section order are identical in both extractions |
| 0.8 | No forbidden constructs | FAIL — header only | The `tabular*` role header, `tex:41-44`. No table elsewhere, no text box, no image of text, no icon, no photo. Contact separators are `$\|$`, not icons |

**All four FAILs trace only to the two-column role header.** That is the
accepted exception in `CV-SPEC.md` item 2 and in `RUBRIC.md` "Accepted
exception, set by Lucas 2026-09-01". Reported, not blocking. I searched the
source for any other cause of 0.5-0.8 and found none: exactly one `tabular*`
exists, inside `\resumeSubheading`, and nothing else on the forbidden list.

**Gate 0 verdict: PASS.**

### LinkedIn ground-truth cross-check — PASS

Character for character against the `DOSSIER.md` LinkedIn block.

| Block | Resume text (raw lines) | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` (21) / `Senior Software Engineer` (22) / `Jan 2026 - Present` (24) | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | `Luizalabs` (40) / `Mid-level Software Engineer` (41) / `Jan 2024 - Jan 2026` (43) | identical | YES |
| 3 | `Lippaus Distribuidora` (54) / `Mid-level Software Engineer` (55) / `Jan 2023 - Jan 2024` (57) | identical | YES |
| 4 | `Lippaus Distribuidora` (64) / `Entry-level Fullstack Software Engineer` (65) / `Mar 2021 - Jan 2023` (67) | identical | YES |
| Education | `FAESA` (75) / `Bacharelado em Sistemas de Informação` (76) / `Feb 2022 - Dec 2025` (78) | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — start and end months identical; ASCII hyphen per `CV-SPEC.md` item 5 and the `CLAUDE.md` 2026-09-01 clarification. The degree name is translated, correct for a `-pt` file and matching `base-pt` |

Company spelling `Luizalabs` is correct. Both Lippaus roles are present and
separate; the promotion is preserved. Job titles stay in English, required by
`CLAUDE.md` rule 1 and matching `base-pt`.

Role locations match the amended rule: `Remoto` for DexCare and Luizalabs,
`Vitória, ES, Brasil` for both Lippaus roles.

`Jan 2026 - Present` keeps the English word `Present` on a Portuguese
document, as `base-pt` does. Rule 1 binds the date string, so this is
reported, not a defect.

### Forbidden-token grep

```
grep -inE 'ruby|rails|sidekiq|activerecord|activejob|rspec|devise|pundit|hotwire'
```
**Zero hits** in the `.tex` and zero in both extractions. **Zero Ruby or Rails
tokens confirmed.**

```
grep -rn UNVERIFIED resumes/conta-simples-engenheira-software-senior-pt.tex
```
**One hit**, `tex:71`. Full text below under "Claims I could not verify".
The Architect's draft reports one marker. That claim is factually correct.

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | The posting states no contracting model. It lists CLT-shaped benefits (`Plano de saúde`, `Licença parental estendida`, `Seguro de vida`) but **never names CLT, PJ or a contract type** | **not stated.** Reading CLT off a benefits list would be inferring a requirement the posting did not state, which `RUBRIC.md` forbids. For the record the document is silent too: `PJ` 0 hits, `CNPJ` 0 hits. `DOSSIER.md` records `PJ with own CNPJ, US contractor (W-8BEN), CLT, EOR/Deel-style employment. All acceptable. [FACT]`, so no contract shape can knock this candidate out |
| Location | `📍 Modelo de trabalho 100% remoto`; `Location as shown: Brazil`; workplace type Remote | **PASS** — graded on the contact-block city per the `RUBRIC.md` 2026-09-02 amendment. Contact line reads `Vitória, ES, Brasil`. Two roles print `Remoto` |
| Time-zone overlap | Not stated in the posting | **not stated** — and never a FAIL. `CLAUDE.md` section 3 and `RUBRIC.md` Gate 1, both amended 2026-09-02 |
| Minimum years of experience | Not stated. The posting states `Experiência sólida` and the title `Pessoa Engenheira de Software Senior` | **not stated** for years. Seniority **PASS** — the document carries `Senior Software Engineer` as the current LinkedIn title, and `mais de 5 anos` in the Summary |
| English proficiency | **Not stated in the posting.** Written end to end in Portuguese by a Brazilian employer, hiring in Brazil, with domestic benefits (`Ifood Benefícios`, `Wellhub`, `Zenklub`) | **not stated** — the LatAm-remote hard-gate rule does not fire on a Brazil-domestic Portuguese posting. Same reading as `reports/brivia-fullstack-pj-gate.md`. For the record the document states no English level: `ingl` 0 hits, `English` 0, `C1` 0, `fluen` 0. Recording it as FAIL would guess a requirement the posting did not state |
| Degree requirement | Not stated anywhere in the posting | **not stated.** The document carries `Bacharelado em Sistemas de Informação`, FAESA |

Required-skill presence, verbatim in the raw extraction. Required is taken
from the posting's own heading `O que esperamos de você`.

| Requirement (posting's words) | Present verbatim? |
|---|---|
| `desenvolvimento e arquitetura de software` | YES — Summary raw 6-7, verbatim. Nowhere else |
| `POO` | YES — Skills keyword line only (raw 17) |
| `SOLID` | YES — Skills keyword line only |
| `Design Patterns` | YES — Skills keyword line only |
| `Clean Code` | YES — Skills keyword line only |
| `Node.js` | YES — Skills, Experience, Summary |
| `TypeScript` | YES — Skills, Experience, Summary |
| `Java` / `Kotlin` / `Go` (posting's alternates) | `Go` YES in all three fields. `Java` YES in one Luizalabs bullet. `Kotlin` **NO**, 0 hits, and correctly so, it is not in `DOSSIER.md` |
| `React` | YES — Skills (raw 15 and 17), one Experience bullet (raw 34) |
| `React Native` | YES — Skills keyword line only. **Absent from Experience** |
| `testes automatizados` | YES — Skills group label (raw 16) and one Experience bullet (raw 51) |
| `Jest` | YES — Skills and Experience |
| `Mocha` | YES — Skills keyword line only |
| `Testing Library` | YES — Skills keyword line only |
| `bancos de dados SQL` | Partial — `SQL` as a standalone word appears **once**, in the Skills group label `Dados SQL e Cloud Computing`. The phrase `bancos de dados` is absent |
| `NoSQL` | YES — Skills keyword line only. `DynamoDB` carries it in Experience |
| `Cloud Computing` | YES — Skills group label only (raw 14) |
| `APIs REST` | YES — Skills, Experience, Summary |
| `protocolos de comunicação` | YES — Skills group label only (raw 13) |
| `boas práticas de integração` | **NO** — `boas prática` 0 hits. Experience has `contratos de integração`, not the posting's phrase |
| `ferramentas de IA` | YES — Summary only (raw 8). Absent from Skills and from Experience as that string |
| `Agentes de IA` | YES — Skills keyword line only |
| `Mentalidade protagonista` | **NO** — `protagonista` 0 hits, `autonomia` 0 hits. Discarded as a soft skill, see Gate 2 convention 5 |

**Gate 1 verdict: PASS.** No FAIL row. The absent tokens above are Gate 2
losses and ranked defects, not knockouts.

---

## Gate 2 — Retrieval coverage: 0 / 100

### Scoring conventions used, stated so this is reproducible

Carried forward from `reports/goodway-global-fullstack-gate.md` and
`reports/brivia-fullstack-pj-gate.md`, plus one new convention.

1. `required` and `preferred` come from the posting's own headings:
   `O que esperamos de você` is required, `Será diferencial se você tiver` is
   preferred. The posting draws the line itself, so I did not invent one.
2. A `Skills` **group label** counts as a `Skills` placement, rung 1. It does
   not earn rung 3, which needs the token inside an Experience bullet.
3. Inflections count for rung 3 where the stem is the posting's stem.
4. Where the posting offers alternates in one clause
   (`ou Java, ou Kotlin, ou Go`), the alternate set scores **once**, at its
   best-covered member. `Node.js` and `TypeScript` from the same clause are
   scored as their own rows, because each is a first-class retrieval token.
5. `Mentalidade protagonista, com autonomia para liderar iniciativas` is
   **discarded as a soft skill** under `RUBRIC.md` Gate 2 Step 1, which says
   to discard soft skills. It names no concrete function, unlike the
   multidisciplinary-team token kept in the Brivia report. Recorded as a
   judgement. The closest document evidence is `Liderei o escopo de projetos e
   a comunicação com stakeholders` (raw 62), which is not the posting's token.
6. **New convention.** The rubric ladder assumes a token can sit in `Skills`.
   For a token whose only placement is the `Summary`, the ladder has no rung:
   rung 4 requires `Skills` and `Experience` beneath it. I score it **2** and
   mark the row. My convention, not the rubric's text. It applies to
   `desenvolvimento e arquitetura de software` and `ferramentas de IA`.
7. The numerator is the unweighted sum of points and the denominator is
   `count × weight × 4`, exactly as the rubric's Step 3 formula is literally
   written and as the two earlier reports in this hunt computed it. Kept for
   comparability across the hunt.
8. Items under `Seu dia a dia na Conta Simples` are duties, not stated
   requirements. They are not scored. Recorded so the omission is visible.

### Required tokens — weight 3, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| R1 | `desenvolvimento e arquitetura de software` | no | no | **yes** (6-7, verbatim) | 2 | Convention 6 |
| R2 | `POO` | yes (17) | **no** | no | 1 | Keyword line. Stuffing penalty applies |
| R3 | `SOLID` | yes (17) | **no** | no | 1 | Keyword line. Stuffing penalty applies |
| R4 | `Design Patterns` | yes (17) | **no** | no | 1 | Keyword line. Stuffing penalty applies |
| R5 | `Clean Code` | yes (17) | **no** | no | 1 | Keyword line. Stuffing penalty applies |
| R6 | `Node.js` | yes (12) | yes (46) | **yes** (6) | 4 | Full ladder |
| R7 | `TypeScript` | yes (12) | yes (27) | **yes** (7) | 4 | Full ladder |
| R8 | `Java` / `Kotlin` / `Go` | yes (12, `Go`) | yes (46, `Java e Go`) | **yes** (7, `Go`) | 4 | Convention 4, scored at `Go`. `Kotlin` absent and correctly so |
| R9 | `React` | yes (15, 17) | yes (34) | no | 3 | Absent from the Summary |
| R10 | `React Native` | yes (17) | **no** | no | 1 | Keyword line. **`DOSSIER.md` records React Native in the Lippaus stack as [FACT]**, and the Lippaus bullet already says `web e mobile` (raw 60). Rung 3 is available today with no new claim. See defect 2 |
| R11 | `testes automatizados` | yes (16, group label) | yes (51, verbatim) | no | 3 | The Experience bullet carries the posting's exact phrase |
| R12 | `Jest` | yes (16) | yes (52) | no | 3 | Absent from the Summary |
| R13 | `Mocha` | yes (17) | **no** | no | 1 | Keyword line. Stuffing penalty applies |
| R14 | `Testing Library` | yes (17) | **no** | no | 1 | Keyword line. Stuffing penalty applies |
| R15 | `SQL` (`bancos de dados SQL`) | yes (14, group label `Dados SQL`) | **no** as a standalone word | no | 1 | Convention 2. `PostgreSQL` (3 hits) is the evidence but is not the token |
| R16 | `NoSQL` | yes (17) | **no** as the token | no | 1 | `DynamoDB` (raw 32) is supporting evidence, so **no stuffing penalty** on this one |
| R17 | `Cloud Computing` | yes (14, group label) | **no** | no | 1 | Convention 2. `AWS` 3 hits and `GCP` 2 hits are the evidence, not the token |
| R18 | `APIs REST` | yes (13) | yes (29) | **yes** (7) | 4 | Full ladder. Strongest placement in the document |
| R19 | `protocolos de comunicação` | yes (13, group label) | **no** | no | 1 | Convention 2 |
| R20 | `boas práticas de integração` | no | no | no | **0** | Absent. `boas prática` 0 hits. A generic engineering practice, claimable under `CLAUDE.md` section 4. See defect 4 |
| R21 | `ferramentas de IA` | no | no | **yes** (8) | 2 | Convention 6. The Skills group label reads `Testes automatizados e agentes`, which does not carry the posting's phrase. See defect 5 |
| R22 | `Agentes de IA` | yes (18) | **no** as the token | no | 1 | The Claude Code / Codex environments bullet (raw 35) is supporting evidence, so **no stuffing penalty** on this one |

Required points earned: **41**. Required denominator: 22 × 3 × 4 = **264**.

### Preferred tokens — weight 1, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| P1 | `AWS Serverless` | yes (17) | **no** | no | 1 | Keyword line. `AWS SDK v3`, `S3`, `RDS` are in Experience (raw 32-33), and none of them is serverless. Stuffing penalty applies |
| P2 | `Abertura de Conta em Fintech` | no | no | no | **0** | `Abertura` 0 hits, `Fintech` 0 hits. **A real dossier gap. Never claim this one.** The nearest fact is the Luizalabs fiscal / NF-e domain, which is not account opening |

Preferred points earned: **1**. Preferred denominator: 2 × 1 × 4 = **8**.

### Step 3

```
coverage = 100 * (41 + 1) / (264 + 8) = 100 * 42 / 272 = 15.44 -> 15
```

### Step 4 — stuffing penalty: −45

**(a) Tokens in `Skills` with no supporting evidence anywhere in Experience,
−5 each.** All eight sit on the single line labelled `Palavras-chave da vaga`
(raw 17-18):

| Token | Any Experience evidence? | Penalty |
|---|---|---|
| `POO` | none | −5 |
| `SOLID` | none | −5 |
| `Design Patterns` | none | −5 |
| `Clean Code` | none | −5 |
| `React Native` | none. `web e mobile` (raw 60) does not name it | −5 |
| `Mocha` | none | −5 |
| `Testing Library` | none | −5 |
| `AWS Serverless` | none. `AWS SDK v3`, `S3`, `RDS` are not serverless | −5 |
| `NoSQL` | **yes** — `DynamoDB`, raw 32 | 0 |
| `Agentes de IA` | **yes** — `Claude Code e Codex`, raw 35 | 0 |

Subtotal: **−40**.

**(b) Frequency, −5 each at 4 or more appearances.** Whole-word counts, regex
with Unicode-aware boundaries, not substring grep:

`APIs` **4**, `React` 3, `TypeScript` 3, `Node.js` 3, `Go` 3, `PostgreSQL` 3,
`AWS` 3, `BullMQ` 3, `REST` 3, `multi-tenant` 3, `DynamoDB` 2, `Jest` 2,
`Vitest` 2, `Express` 2, `Koa` 2, `Redis` 2, `GCP` 2, `JavaScript` 2,
`Claude Code` 2, `Codex` 2, `IA` 2, `Java` 1, `SQL` 1, `NoSQL` 1,
`React Native` 1, `Mocha` 1, `Testing Library` 1.

`APIs` reaches **4** (raw 7, raw 13 twice, raw 29). That breaks the
`CV-SPEC.md` 3-appearance cap, which the two earlier reports in this hunt
treat as a Step 4 input on every term. Subtotal: **−5**.

Total penalty: **−45**.

```
15 - 45 = -30
```

**Clamped to 0.** The rubric scores 0-100 and defines no floor; clamping at 0
is my convention, stated so the arithmetic stays visible.

**Gate 2 final: 0 / 100.** Fifteen before penalty.

### Missing required tokens

1. `boas práticas de integração` — 0 hits.
2. `Mentalidade protagonista` / `autonomia` — 0 hits (discarded as a soft
   skill, recorded here for completeness).
3. `Kotlin` — 0 hits, correctly, no dossier fact.
4. Eight tokens present in `Skills` but **absent from every Experience
   bullet**: `POO`, `SOLID`, `Design Patterns`, `Clean Code`, `React Native`,
   `Mocha`, `Testing Library`, `AWS Serverless`.
5. `SQL`, `Cloud Computing`, `protocolos de comunicação` — group labels only,
   never inside a bullet.
6. `ferramentas de IA` — Summary only, absent from Skills and Experience.

Missing preferred: `Abertura de Conta em Fintech`.

### Ceiling, stated honestly

Only **one** token on this posting is a true dossier gap: P2, fintech
account opening. Everything else scoring low scores low by placement, not by
absence of fact.

- Moving the eight unsupported keyword-line tokens into one plausible bullet
  each removes the whole −40 penalty and lifts each row from 1 to 3. Required
  points go 41 → 57, coverage before penalty 15 → 21, and after penalty
  **21 minus the `APIs` −5 = 16**.
- Also cutting one `APIs` occurrence removes the last −5 and lands at **21**.
- Adding `ferramentas de IA` to the Skills label and to the Claude Code bullet
  lifts R21 from 2 to 4. Adding `boas práticas de integração` to the OpenAPI
  bullet lifts R20 from 0 to 3. Coverage reaches **~23**.

The ceiling on this posting is low by construction: the posting asks for many
abstract practice tokens (`POO`, `SOLID`, `Clean Code`, `Design Patterns`,
`protocolos de comunicação`, `boas práticas de integração`) that no honest
bullet carries more than once. The realistic target is the low twenties, and
the difference between 0 and 23 is entirely placement work.

---

## Gate 3 — Human scan: 90 / 100

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 15/15 | `Senior Software Engineer` at raw line **6 of 81** = 7.4%, inside the Summary's first sentence. It repeats as the DexCare title at raw 22. The posting's own title is `Pessoa Engenheira de Software Senior`; `CLAUDE.md` rule 1 binds the CV to the LinkedIn English string, so the English title is correct and is not a defect |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | 15/20 | DexCare bullets 1 and 2 are on target: TypeScript/Express/Koa event-driven, then `APIs REST` multi-tenant with `OpenAPI/Swagger` and a 25% number. Bullet 3 is the EMR Epic sync, a healthcare-domain bullet this fintech posting does not ask for. **Minus 5:** the AI-tooling bullet (raw 35, `Claude Code e Codex`) sits sixth. The posting names AI tooling twice, in `Seu dia a dia` and again in `O que esperamos`, and treats it as a differentiator. It belongs in the top three |
| 3.3 | Voice rule | 15/15 | 16 of 16 bullets pass. Full table below |
| 3.4 | At least 3 bullets with a real, defensible number | 15/15 | Seven: 25% (raw 30), 15% (31), 7% (34), 33% (37), 20% (48), 18% (50), 26% (61). **All seven trace to `DOSSIER.md`** bullet metrics D3, D2, D5, D7, L2, L3, P2 |
| 3.5 | Length | 10/10 | `pdfinfo` reports 1 page, letter |
| 3.6 | No unsupported buzzwords | 10/10 | Zero hits for `proativo`, `apaixonado`, `dinâmico`, `comunicativo`, `protagonista`, and for the EN list `team player`, `results-driven`, `passionate`, `hands-on` |
| 3.7 | Skills grouped by category | 7/10 | Six labelled groups (raw 12-18), five of them real technology categories tuned to the posting's own words. **Minus 3:** the sixth group is labelled `Palavras-chave da vaga`, literally "keywords from the job posting". That is not a category, it is an admission. A human reader sees ten unsupported terms under a label announcing they were copied from the ad. This is the human-reaction failure `RUBRIC.md` Step 4 exists to price |
| 3.8 | Scannable | 3/5 | Consistent 5pt inter-role gap, bold company, italic title, one column, full width. **Minus 1: verb monotony.** `Construí` opens 6 of 16 bullets (raw 27, 29, 35, 46, 49, 71). A recruiter scanning the left edge sees one word repeatedly, which lowers the scan anchor's information value. **Minus 1: orphan line.** The keyword line wraps and leaves `\| Agentes de IA [UNVERIFIED]` alone on raw line 18, visible on the page as a dangling fragment that starts with a pipe |

**Gate 3 total: 90/100.**

## Voice check (explicit, per `CLAUDE.md` section 9 and `CV-SPEC.md`)

Leading token of every Experience bullet, read from the raw extraction:

| Raw line | Leading verb | Verdict |
|---|---|---|
| 27 | Construí | 1st person past, subject omitted, OK |
| 29 | Construí | OK |
| 31 | Integrei | OK |
| 32 | Modelei | OK |
| 34 | Reduzi | OK |
| 35 | Construí | OK |
| 37 | Ajudei | OK |
| 46 | Construí | OK |
| 48 | Migrei | OK |
| 49 | Construí | OK |
| 51 | Implantei | OK |
| 60 | Construí | OK |
| 61 | Processei | OK |
| 62 | Liderei | OK |
| 70 | Desenvolvi | OK |
| 71 | Construí | OK |

- Bullets that break the rule: **none**. 16 of 16 pass.
- Bullets starting with `Eu`: **none**.
- Present tense in a bullet: **none**.
- `Responsável por` or third person: **none**.
- Summary uses `Eu`: **yes**, four times — `Eu sou`, `Eu construo`,
  `eu construí`, `Eu integro` (raw 6-9).

**Voice: PASS.**

---

## Defects, ranked by cost

1. **Ten posting tokens live in `Skills` and in no bullet** — Gate 2, the
   whole −40 penalty and eight rows stuck at rung 1. `CLAUDE.md` section 4
   requires an ecosystem token to be "placed in Skills **and in one bullet**
   where the history makes it plausible". Only the Skills half was done. Fix:
   place each of `POO`, `SOLID`, `Design Patterns`, `Clean Code`,
   `React Native`, `Mocha`, `Testing Library`, `AWS Serverless` inside one
   existing bullet where the history supports it, keeping the `[UNVERIFIED]`
   marker on the claim.
2. **`React Native` is a dossier FACT and is being treated as a keyword** —
   Gate 2 R10, and a truth-handling error. `DOSSIER.md`: "Lippaus stack
   PostgreSQL / BullMQ / JavaScript / React Native. [FACT, Lucas 2026-09-01]".
   The Lippaus Mid-level bullet at raw 60 already says `web e mobile`. Naming
   React Native there is a fact, not a claim, and it moves a **required**
   posting token from 1 to 3. It should also come off the `[UNVERIFIED]` line.
3. **`NoSQL` is over-marked as `[UNVERIFIED]`** — truth handling. `DynamoDB`
   is `[FACT-OBSERVED]` in `DOSSIER.md` and is already in the DexCare bullet
   at raw 32. `NoSQL` describes it. Marking it unverified asks Lucas to
   confirm something the dossier already records.
4. **`boas práticas de integração` scores 0** — Gate 2 R20, a required token.
   A generic engineering practice, explicitly claimable under `CLAUDE.md`
   section 4. The DexCare bullet at raw 29 already carries
   `contratos de integração` and `OpenAPI/Swagger`. Fix: use the posting's own
   phrase in that bullet, marked `[UNVERIFIED]`.
5. **`ferramentas de IA` reaches only the Summary** — Gate 2 R21, worth 2 of
   4 on a token the posting names twice. The Skills label reads
   `Testes automatizados e agentes`. Fix: put the posting's phrase in the
   label and in the Claude Code / Codex bullet at raw 35.
6. **The `Palavras-chave da vaga` label** — Gate 3.7, minus 3. It tells the
   reader the line was copied from the ad. Once defect 1 is fixed the line
   mostly empties; whatever remains belongs under a real category name.
7. **`APIs` appears 4 times** — Gate 2 Step 4, −5, and a `CV-SPEC.md`
   3-appearance cap breach. Raw 7, raw 13 twice, raw 29. The Skills label
   `Protocolos de comunicação e APIs:` immediately precedes `APIs REST`, so
   one of the two is free to cut.
8. **AI bullet buried at position six** — Gate 3.2, minus 5. Move the
   `Claude Code e Codex` bullet (raw 35) into the DexCare top three.
9. **Verb monotony** — Gate 3.8, minus 1. `Construí` opens 6 of 16 bullets.
   Vary three without changing the claim.
10. **Orphan keyword fragment** — Gate 3.8, minus 1. Raw 18 renders as a line
    beginning with a pipe: `| Agentes de IA [UNVERIFIED]`.
11. **`tabular*` role header, four Gate 0 findings** — Gate 0.5, 0.6, 0.7,
    0.8. Reported, not blocking, by Lucas's 2026-09-01 decision. No action.
12. **`Present` and English month abbreviations in a Portuguese document** —
    observation only, no point deducted. Rule 1 requires the LinkedIn string
    verbatim and outranks language consistency.

---

## Claims I could not verify

Traced against `DOSSIER.md`. I do not delete these and I do not defend them.
Lucas decides.

### The one `[UNVERIFIED]` marker in the source

`resumes/conta-simples-engenheira-software-senior-pt.tex:71`, rendering at raw
17-18:

```
Palavras-chave da vaga: POO | SOLID | Design Patterns | Clean Code |
React Native | Mocha | Testing Library | AWS Serverless | NoSQL |
Agentes de IA [UNVERIFIED]
```

One marker covers ten tokens. Two of the ten do not belong under it:

- `React Native` — `DOSSIER.md` [FACT], Lippaus stack.
- `NoSQL` — carried by `DynamoDB`, `DOSSIER.md` [FACT-OBSERVED].

The remaining eight (`POO`, `SOLID`, `Design Patterns`, `Clean Code`, `Mocha`,
`Testing Library`, `AWS Serverless`, `Agentes de IA`) are genuinely
unconfirmed and need Lucas's yes or no before this package is sent.

### Numbers

Every number on the document traces to `DOSSIER.md`:

| Number | Raw line | Dossier id |
|---|---|---|
| 25% authentication friction | 30 | D3 |
| 15% wrong bookings | 31 | D2 |
| 7% release risk | 34 | D5 |
| 33% piloting friction, SPI | 37 | D7 |
| 20% invoice throughput | 48 | L2 |
| 18% support tickets | 50 | L3 |
| 26% processing capacity | 61 | P2 |

**No number on the document fails to trace to `DOSSIER.md`.**

One quantity is derived rather than recorded:

- `mais de 5 anos` (Summary, raw 6). Not stated in `DOSSIER.md`. It is
  arithmetically consistent with the LinkedIn ground truth: `Mar 2021` to
  2026-09-02 is 5 years 6 months. Consistent, not a recorded fact. Same
  finding as `reports/base-pt-gate-2026-09-02-b.md` item 1.

### Prose claims not traceable to the dossier

All four are inherited from the approved `base-pt`, not introduced by this
tailoring. Verified by reading `resumes/base-pt.raw.txt`.

1. `desenvolvimento e arquitetura de software` (Summary, raw 6-7). `DOSSIER.md`
   records DexCare systems and stack, and leaves "which of these he personally
   owned versus used" **[OPEN]**. Architecture ownership is not recorded.
   New to this tailoring; `base-pt` says `construindo sistemas backend e
   fullstack`.
2. `reservas em tempo real` (DexCare, raw 27). `DOSSIER.md` records
   "event-driven booking". `tempo real` is a qualifier it does not carry.
   Inherited from `base-pt` raw 26.
3. `apoiou a expansão nacional de varejistas` (Lippaus Mid-level, raw 60).
   `DOSSIER.md` confirms the multi-tenant web and mobile platform on
   PostgreSQL. It records nothing about nationwide scope. Inherited from
   `base-pt` raw 59.
4. `startup de distribuição de bebidas` (Lippaus Entry-level, raw 70). Not in
   `DOSSIER.md` in any form. Inherited from `base-pt` raw 69.
5. `e-commerce do Magazine Luiza` (Luizalabs, raw 46-47). `DOSSIER.md`
   confirms the fiscal / NF-e / SEFAZ domain as [FACT]. It does not carry the
   word `e-commerce`. Magazine Luiza being an e-commerce retailer is common
   knowledge; it is not observable from this dossier, so I record it rather
   than assert it.

---

## Fix list for the Architect

none
