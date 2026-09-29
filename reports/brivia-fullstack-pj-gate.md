# ATS Analysis — brivia-fullstack-pj-pt.pdf vs brivia-fullstack-pj
Segment: br-pj   Date: 2026-09-02

Judged on extractions the analyzer regenerated from the PDF under test:
`pdftotext -layout` and `pdftotext` on `resumes/brivia-fullstack-pj-pt.pdf`
(28716 bytes, built 2026-09-02 19:19, producer `xdvipdfmx (0.1)`).
Source cross-read: `resumes/brivia-fullstack-pj-pt.tex`.
Posting text: `jobs/brivia-fullstack-pj.md` (LinkedIn post `dfRZ_hDY`, captured
by Kestrel, hunt 2026-09-02-b).
Titles, companies and dates checked against `DOSSIER.md` **LinkedIn ground truth**.
Architect's own marker list read: `reports/brivia-fullstack-pj-draft.md`.

Rule versions applied: `CLAUDE.md` and `RUBRIC.md` as of 2026-09-02, including
the 2026-09-02 changes that (a) forbid a time-zone overlap statement on the CV
and make its absence `not stated`, never a FAIL, and (b) set the Lippaus role
location to `Vitória, ES, Brazil`.

This is our rubric. It is not a vendor score. No ATS emits these numbers.

## Verdict

**BLOCKED at Gate 1.**

| Gate | Result |
|---|---|
| Gate 0 — Parse integrity | **PASS** (4 header-only FAILs, reported not blocking) |
| Gate 1 — Knockouts | **FAIL** — entity type: the posting contracts in `regime PJ`, the document states no PJ or CNPJ |
| Gate 2 — Retrieval coverage | **22 / 100** |
| Gate 3 — Human scan | **88 / 100** |

The document parses cleanly and its voice, numbers and LinkedIn fidelity are
correct. It blocks on one omission that `DOSSIER.md` can fix today. Gate 2 at
22 is low, and most of the gap is not a missing fact: the Architect declined
to claim five ecosystem tokens the Maestro brief explicitly authorised under
`CLAUDE.md` section 4. See defect 2.

---

## Gate 0 — Parse integrity

`pdfinfo` reports **1 page**, letter. `pdfimages -list` returns **zero images**.
`pdffonts` shows four embedded subsets, all with ToUnicode maps
(`Roboto-Bold`, `Roboto-Regular`, `Roboto-Italic`, `CMSY9`).

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction is complete prose, 79 content lines plus one form feed. Every section present |
| 0.2 | Glyph integrity | PASS | Zero `\x00`, zero `U+FFFD`, zero `?`, zero `U+FB00-FB04` ligature codepoints. Measured by codepoint in Python, not by shell grep. The **only** character above U+00FF in the whole extraction is `U+2022 BULLET`. Ligature-bearing words are intact: `fiscais` 4, `fluxos` 3, `flags` 1, `notificações` 1, `configurações` 1, `funcionalidades` 2, `oficinas`-class words none present |
| 0.3 | Contact block recoverable | PASS | Raw line 3, in the body, not a header or footer: `Vitória, ES, Brasil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. City, phone, email and LinkedIn URL all present. No UTC offset, no time-zone overlap sentence, per `CLAUDE.md` section 3 as amended 2026-09-02 |
| 0.4 | Section headers verbatim | PASS | Raw lines 5, 10, 19, 73: `RESUMO`, `HABILIDADES`, `EXPERIÊNCIA`, `FORMAÇÃO`, each a standalone line. The PT allowlist in Gate 0.4. Uppercase rendering allowed. `\section`, not `\section*` |
| 0.5 | Employment-block segmentation | FAIL — header only | Raw splits each role header into `DexCare` / `Senior Software Engineer` / blank / `Jan 2026 - Present` / `Remoto`. **No two roles merge. No role splits into two employment entries.** Four Experience blocks and one Education block, all intact and in the right order. Cause is the `tabular*` at `brivia-fullstack-pj-pt.tex:41` |
| 0.6 | Date parseability | FAIL — header only | Every date sits one blank line below its title, not on it. Format correct in all five blocks: `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. Separator verified by codepoint: the only dash character in the document is `U+002D HYPHEN-MINUS`. No EN DASH anywhere |
| 0.7 | Reading order | FAIL — header only | Whitespace-normalized `difflib` comparison of raw against layout returns **exactly 5 hunks, and all five are a role or education header**. Raw: company, title, dates, location. Layout: company+dates, title+location. **Zero content blocks reorder.** Bullet order is identical in both extractions |
| 0.8 | No forbidden constructs | FAIL — header only | The `tabular*` role header, `tex:41-44`. No table elsewhere, no text box, no image of text, no icon, no photo. `pdfimages -list` is empty |

**All four FAILs trace only to the two-column role header.** That is the
accepted exception in `CV-SPEC.md` item 2 and in `RUBRIC.md` "Accepted
exception, set by Lucas 2026-09-01". Reported, not blocking. I searched for any
other cause of 0.5-0.8 and found none: the source carries exactly one
`tabular*`, inside `\resumeSubheading`, and nothing else on the forbidden list.

**Gate 0 verdict: PASS.**

### LinkedIn ground-truth cross-check — PASS

Character for character against the `DOSSIER.md` LinkedIn block.

| Block | Resume text (raw lines) | LinkedIn ground truth | Match |
|---|---|---|---|
| 1 | `DexCare` (20) / `Senior Software Engineer` (21) / `Jan 2026 - Present` (23) | `Senior Software Engineer` / `DexCare` / `Jan 2026 - Present` | YES |
| 2 | `Luizalabs` (39) / `Mid-level Software Engineer` (40) / `Jan 2024 - Jan 2026` (42) | identical | YES |
| 3 | `Lippaus Distribuidora` (52) / `Mid-level Software Engineer` (53) / `Jan 2023 - Jan 2024` (55) | identical | YES |
| 4 | `Lippaus Distribuidora` (63) / `Entry-level Fullstack Software Engineer` (64) / `Mar 2021 - Jan 2023` (66) | identical | YES |
| Education | `FAESA` (74) / `Bacharelado em Sistemas de Informação` (75) / `Feb 2022 - Dec 2025` (77) | `FAESA` / `Bachelor's degree , Information Systems` / `Feb 2022 – Dec 2025` | YES — start and end months identical; ASCII hyphen per `CV-SPEC.md` item 5 and the `CLAUDE.md` 2026-09-01 clarification. The degree name is translated, which is correct for a `-pt` file and matches `base-pt` |

Company spelling `Luizalabs` is correct. Both Lippaus roles are present and
separate; the promotion is preserved. Job titles stay in English, which is
required by `CLAUDE.md` rule 1 and matches `base-pt`.

Role locations match the amended rule: `Remoto` for DexCare and Luizalabs,
`Vitória, ES, Brasil` for both Lippaus roles. **The location conflict raised in
`reports/goodway-global-fullstack-gate.md` defect 8 is settled and this
document is on the correct side of it.**

`Jan 2026 - Present` keeps the English word `Present` on a Portuguese
document. `base-pt.raw.txt:23` does the same. Rule 1 binds the date string, so
this is reported, not a defect.

### Forbidden-token grep

```
grep -inE 'ruby|rails|sidekiq|activerecord|activejob|rspec|devise|pundit|hotwire'
```
**Zero hits** in `brivia-fullstack-pj-pt.tex` and zero in both extractions.

```
grep -rn UNVERIFIED resumes/brivia-fullstack-pj-pt.tex
```
**Zero hits.** Independently confirmed. The Architect's draft claims "Nenhum"
and that claim is factually correct. Whether zero markers is the *right*
outcome is a separate question, and the answer is no. See defect 3.

---

## Gate 1 — Knockouts

Extracted from the posting text only. Nothing inferred.

| Check | Posting source | Result |
|---|---|---|
| Work authorization / entity type | `➡️ Contratação: PJ` and `está contratando Desenvolvedor(a) Fullstack em regime PJ` | **FAIL** — the posting makes PJ the contracting model. The document states no entity type: `PJ` 0 hits, `CNPJ` 0 hits in the raw extraction. `DOSSIER.md` Identity records `Contract types available: PJ with own CNPJ ... [FACT, Lucas 2026-09-01]`, so the document is silent on a fact it already holds. Same failure the earlier Brivia package took in `reports/brivia-fullstack-remoto-gate0.md` |
| Location | `📍 Modelo: 100% Remoto` and `A Brivia ... está contratando`; workplace type Remote | **PASS** — graded on the contact-block city, per the `RUBRIC.md` amendment of 2026-09-02. Contact line reads `Vitória, ES, Brasil`. Two roles print `Remoto` |
| Time-zone overlap | Not stated in the posting | **not stated** — and never a FAIL. `CLAUDE.md` section 3 and `RUBRIC.md` Gate 1, both amended 2026-09-02: overlap is never printed on the CV and is answered in the apply note's screening answers |
| Minimum years of experience | Not stated. The posting states `❗ Senioridade: Pleno / Sênior` | **not stated** for years. Seniority **PASS** — the document carries `Senior Software Engineer` as the current LinkedIn title and `mais de 5 anos de experiência profissional` in the Summary |
| English proficiency | **Not stated in the posting.** The posting is written in Portuguese by a Brazilian employer, contracts in BRL benefits (`Vale Refeição`, `Bradesco`, `Metlife`, `ABRADI`), and offers a `Programa de Desenvolvimento de Idiomas` as a **benefit**, not a requirement | **not stated** — the LatAm-remote hard-gate rule does not fire on a Brazil-domestic Portuguese posting. Same reading as `reports/brivia-fullstack-remoto-gate0.md`. For the record, the document states no English level: `ingl` 0 hits, `English` 0, `C1` 0, `fluen` 0 |
| Degree requirement | `⭐ Diferenciais: Formação superior completa em TI, Engenharia de Software ou áreas correlatas` — a differential, not a requirement | **PASS as a differential** — `Bacharelado em Sistemas de Informação`, FAESA, is one of the named fields |
| Own equipment | `❗ Exigência: Equipamento próprio para atuação` | **not stated on the document** (`equipament` 0 hits, `notebook` 0 hits). `DOSSIER.md` records no fact either way. **Not a rubric row**, recorded because the posting states it as a hard condition. This belongs in the apply note's screening answers, not on the CV, and it needs an answer from Lucas |

Required-skill presence, verbatim in the raw extraction:

| Requirement (posting's words) | Present verbatim? |
|---|---|
| `React` | YES — Summary, Skills, and one Experience bullet, but only inside `React Native` (raw 70). See defect 4 |
| `TypeScript` | YES |
| `Node.js` | YES |
| `desenvolvimento web` | YES — Skills group label only |
| `APIs` | YES |
| `arquitetura BFF` / `BFF` | **NO** — 0 hits |
| `PostgreSQL` | YES |
| `bancos de dados relacionais` | YES — Skills group label only |
| `integrações` | YES |
| `processamento assíncrono/mensageria` | YES as the exact slashed pair in Skills. In Experience only as `filas assíncronas` and `jobs assíncronos`. `mensageria` 1 hit total, Skills only |
| `código testável` | YES — Skills group label. Supported in Experience by `testes`, `Vitest`, `Jest` |
| `boas práticas de engenharia` | **NO** — 0 hits |
| `code review` | **NO** — 0 hits |
| `esteiras de CI/CD` | YES — `esteiras de CI/CD` verbatim at raw 50 |
| `times multidisciplinares` / `Produto` / `UX` / `Dados` / `QA` | **NO** — 0 hits for all five |

**Gate 1 verdict: FAIL on one row.** Entity type. Every other stated gate
passes or is `not stated`. The absent required tokens above are Gate 2 losses
and ranked defects, not knockouts.

---

## Gate 2 — Retrieval coverage: 22 / 100

### Scoring conventions used, stated so this is reproducible

Carried forward from `reports/goodway-global-fullstack-gate.md`.

1. Where the posting joins two terms with a slash
   (`processamento assíncrono/mensageria`), the pair scores **once**, at its
   best-covered member, because the document can carry the pair as one string.
2. The rubric ladder assumes a token can sit in `Skills`. For a token whose
   only home is `Education` (`Formação superior completa em TI`), the ladder
   has no rung. I score it **2** and mark the row. My convention, not the
   rubric's text.
3. A `Skills` **group label** counts as a `Skills` placement. `desenvolvimento
   web`, `bancos de dados relacionais` and `código testável` are all group
   labels the Architect tuned to the posting's words. That is sound practice
   and it earns rung 1. It does not earn rung 3, because rung 3 needs the token
   inside an Experience bullet and none of the three appears there.
4. Inflections count for rung 3 where the stem is the posting's stem
   (`assíncronas`/`assíncronos` for `assíncrono`, `testes` for `testável`).
   Marked on each row.
5. `required` and `preferred` are taken from the posting's own headings:
   `Estão procurando devs com` is required, `⭐ Diferenciais` is preferred.
   The posting draws that line itself, so I did not invent one.
6. `Atuação colaborativa com times multidisciplinares` is kept as a token, not
   discarded as a soft skill, because it names four concrete functions
   (Produto, UX, Dados, QA) that recruiters do search on. Marked as a judgement.

### Required tokens — weight 3, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| R1 | `React` | yes (11) | yes (70) | **yes** (7) | 4 | Full ladder on the token. The Experience hit is `React Native`, in the 2021-2023 role. See defect 4 |
| R2 | `TypeScript` | yes (11) | yes (26) | **yes** (7) | 4 | Full ladder |
| R3 | `desenvolvimento web` | yes (11, group label) | **no** | no | 1 | Convention 3 |
| R4 | `Node.js` | yes (11) | yes (45) | **yes** (7) | 4 | Full ladder |
| R5 | `APIs` | yes (12, `REST APIs`) | yes (29) | **yes** (7, `Eu construo APIs`) | 4 | Full ladder |
| R6 | `arquitetura BFF` / `BFF` | no | no | no | **0** | Absent. The Maestro brief authorised this as a claimable ecosystem token. See defect 2 |
| R7 | `PostgreSQL` | yes (13) | yes (31, 58) | no | 3 | Absent from the Summary |
| R8 | `bancos de dados relacionais` | yes (13, group label) | **no** | no | 1 | Convention 3 |
| R9 | `integrações` | yes (14, group label) | yes (59) | **yes** (7) | 4 | Full ladder |
| R10 | `processamento assíncrono/mensageria` | yes (14, exact pair) | yes (47, 59, inflected) | no | 3 | Convention 4. `mensageria` itself never reaches Experience, and `RabbitMQ`/`AMQP` are absent from the whole document. See defect 5 |
| R11 | `código testável` | yes (17, group label) | yes (35 `testes`, 50 `Vitest`/`Jest`) | no | 3 | Convention 4 |
| R12 | `boas práticas de engenharia` | no | no | no | **0** | Absent. Generic engineering practice, claimable under `CLAUDE.md` section 4. See defect 2 |
| R13 | `code review` | no | no | no | **0** | Absent. Named explicitly in `CLAUDE.md` section 4 as a claimable practice, and listed in the Maestro brief. See defect 2 |
| R14 | `esteiras de CI/CD` | yes (15, `CI/CD`) | yes (50, `esteiras de CI/CD` verbatim) | no | 3 | The Experience bullet carries the posting's own noun `esteiras` |
| R15 | `times multidisciplinares` (Produto, UX, Dados, QA) | no | no | no | **0** | Absent. Convention 6 |

Required points earned: **34**. Required denominator: 15 x 3 x 4 = **180**.

### Preferred tokens — weight 1, max 4 points each

| # | Token (posting's words) | Skills | Experience | Summary / title | Points | Note |
|---|---|---|---|---|---|---|
| P1 | `Formação superior completa em TI` | — | — | — | 2 | Convention 2. `FAESA` / `Bacharelado em Sistemas de Informação`, raw 74-75 |
| P2 | `integração de aplicações com modelos de IA/ML` | no | no | no | **0** | `ML` 0 hits, `modelos de IA` 0 hits. The Maestro brief authorised this as a claimable ecosystem token. See defect 2 |
| P3 | `uso de ferramentas de IA no desenvolvimento` | yes (17, group label carries the posting's phrase verbatim) | yes (34) | **yes** (8) | 4 | Full ladder. The strongest single placement in the document |
| P4 | `soluções orientadas a dados` (indicadores, scores, recomendações, modelos preditivos) | no | no | no | **0** | All five absent. No dossier fact behind any of them |
| P5 | `microsserviços` | yes (15) | yes (45, 48) | no | 3 | Absent from the Summary |
| P6 | `processamento distribuído` | yes (15) | yes (45) | no | 3 | Absent from the Summary |
| P7 | `certificações em Cloud/DevOps` | no | no | no | **0** | Absent. Named as a gap in the Maestro brief. `DOSSIER.md` records no certification. **Never claim this one** |

Preferred points earned: **12**. Preferred denominator: 7 x 1 x 4 = **28**.

### Step 3

```
coverage = 100 * (34 + 12) / (180 + 28) = 100 * 46 / 208 = 22.12 -> 22
```

### Step 4 stuffing penalty: 0

Whole-word counts, word-boundary regex, not substring grep: `React` 3,
`TypeScript` 3, `Node.js` 3, `JavaScript` 3, `Go` 3, `PostgreSQL` 3, `APIs` 3,
`integrações` 3, `microsserviços` 3, `IA` 3, `BullMQ` 3, `Java` 2,
`processamento distribuído` 2, `CI/CD` 2, `Express` 2, `Koa` 2, `Auth0` 2,
`AWS` 2, `Docker` 2, `Kubernetes` 2, `mensageria` 1. **No token reaches 4.**
The `CV-SPEC.md` 3-appearance cap holds exactly, on every term.

One `Skills` token has no Experience evidence: `Agentic workflows` (raw 17).
Its substance is in the Summary as `fluxos agênticos` and in the DexCare AI
bullet, and it is a `DOSSIER.md` FACT token set that Lucas fixed himself. It is
not a token this posting asks for, so **no penalty is applied**, per the same
treatment in `reports/goodway-global-fullstack-gate.md` defect 7.

**Gate 2 final: 22 / 100.**

### Missing required tokens

1. `BFF` / `arquitetura BFF`
2. `boas práticas de engenharia`
3. `code review`
4. `times multidisciplinares`, `Produto`, `UX`, `Dados`, `QA`
5. `mensageria` in an Experience bullet (present in Skills only)
6. `desenvolvimento web` in an Experience bullet (Skills label only)
7. `bancos de dados relacionais` in an Experience bullet (Skills label only)

Missing preferred: `modelos de IA/ML`, `soluções orientadas a dados`,
`indicadores`, `scores`, `recomendações`, `modelos preditivos`,
`certificações em Cloud/DevOps`.

### Ceiling, stated honestly

Only **one** token on this posting is a true dossier gap: P7, Cloud/DevOps
certifications. Everything else that scores 0 scores 0 by a choice, not by
absence of fact.

- Placing R6, R12, R13 and R15 at rung 3, and P2 at rung 3, lifts coverage
  from **22 to 29**.
- Also lifting R3 and R8 from rung 1 to rung 3, by putting `desenvolvimento
  web` and `bancos de dados relacionais` inside an existing bullet, reaches
  **31**.
- Adding `RabbitMQ` and `AMQP` to the messaging Skills group, and `mensageria`
  to the Luizalabs SEFAZ bullet, does not move R10 past 3 but removes the
  thinnest group on the document. See defect 5.

22 is not a build defect and it is not laziness. It is the cost of routing
around five tokens the ecosystem rule told the Architect to claim.

---

## Gate 3 — Human scan: 88 / 100

| # | Check | Points | Basis |
|---|---|---|---|
| 3.1 | Target title in the top 15% | **13** / 15 | Top 15% of a 79-line raw extraction is lines 1-11. Line 6 opens `Eu sou Senior Software Engineer`; line 7 carries `fullstack com React, TypeScript, Node.js e Go`; line 11 repeats React, TypeScript and Node.js in Skills. Three of the four technologies in the posting's own title sit inside the window. Docked 2: `PostgreSQL`, the fourth title technology, first appears at line 13, just outside; and the posting's title noun `Desenvolvedor(a) Fullstack` never appears as a title, only as the adjective `fullstack` on `sistemas` |
| 3.2 | 3 most relevant bullets in the most recent role, first 3 lines | **13** / 20 | The three most posting-relevant DexCare bullets are b1 (`TypeScript`, `Express`, `Koa`, backend, event-driven), b3 (`REST APIs`, `Auth0 JWT`, `OpenAPI/Swagger`, contratos de API, 25%) and b4 (`PostgreSQL`, `Sequelize`, `Drizzle ORM`, `DynamoDB`, `Redis`). They sit at positions **1, 3 and 4**. Position 2 is the Epic EMR bullet, which carries no posting token at all. Docked 3 for that. Docked 4 more: **`React` appears nowhere in the DexCare block**, and nowhere in Experience except inside `React Native` in the 2021-2023 role, while `React` is the first technology in the posting's title |
| 3.3 | Voice rule (`CV-SPEC.md`, `CLAUDE.md` section 9) | **15** / 15 | All 16 bullets checked one by one. Openers in document order: `Construí`, `Integrei`, `Construí`, `Conectei`, `Reduzi`, `Construí`, `Ajudei`, `Construí`, `Melhorei`, `Reduzi`, `Mantive`, `Construí`, `Aumentei`, `Entreguei`, `Construí`, `Construí`. **Every one is pretérito perfeito, first person singular, subject omitted. Zero start with `Eu`. Zero present tense. Zero `Responsável por`. Zero third person.** The Summary uses `Eu` three times: `Eu sou`, `Eu construo`, `Eu integro`, with present tense, which `CV-SPEC.md` requires |
| 3.4 | At least 3 bullets carry a real, defensible number | **15** / 15 | Seven do: 15%, 25%, 7%, 33%, 20%, 18%, 26%. **All seven trace to the `DOSSIER.md` bullet-metrics list**, IDs D2, D3, D5, D7, L2, L3, P2, each attached to the same method the dossier attaches it to. No number on this document fails to trace |
| 3.5 | Length: 1 page under 10 years | **10** / 10 | `pdfinfo` reports `Pages: 1` |
| 3.6 | No unsupported buzzwords | **10** / 10 | No `team player`, `results-driven`, `passionate`, `proativo`, `dinâmico`, `apaixonado`. `código de alta qualidade` is a `DOSSIER.md` FACT phrase, not a buzzword |
| 3.7 | Skills grouped by category | **8** / 10 | Six labelled groups, all meaningful, and the labels are tuned to the posting's own phrases, which is good practice and earns Gate 2 points. Docked 2: **`Integrações e processamento assíncrono/mensageria: BullMQ` holds one single tool** (`tex:75`). It is the group that answers a required posting line, and `RabbitMQ` and `AMQP`, both `DOSSIER.md` FACT Skills tokens, are missing from it. A one-item group under a two-concept label reads thin to a human and leaves `mensageria` unsupported |
| 3.8 | Scannable | **4** / 5 | One clean page, ruled headers, bold companies, role gaps per `CV-SPEC.md` item 2, consistent spacing. Docked 1: wrapped bullets have no hanging indent, so nine continuation lines start flush under the bullet glyph, for example raw 27 `uma plataforma de agendamento em saúde.`, raw 49 `fluxos fiscais.`, raw 71 `restrições técnicas.` |

Total: **88 / 100**. The highest Gate 3 this team has produced for a tailored
document.

---

## Defects, ranked by cost

| # | File and line | Defect | What would pass |
|---|---|---|---|
| **1** | `brivia-fullstack-pj-pt.tex:66` (Summary) or the contact block, `tex:57-62` | **Gate 1 blocker. The document states no entity type.** The posting contracts `em regime PJ` and puts `Contratação: PJ` in its second line. Raw extraction: `PJ` 0 hits, `CNPJ` 0 hits | **Fixable today, from the dossier, no new fact needed.** `DOSSIER.md` Identity: `Contract types available: PJ with own CNPJ, US contractor (W-8BEN), CLT, EOR/Deel-style employment. All acceptable. [FACT, Lucas 2026-09-01]`. Put `PJ` and `CNPJ` into the raw text, in the contact line or in one Summary clause. This clears the only Gate 1 FAIL |
| **2** | `tex:69-76` (Skills) and the DexCare and Luizalabs blocks | **Five ecosystem tokens the Maestro brief authorised were routed around instead of claimed.** The brief's `Claim marked [UNVERIFIED]:` line names `BFF`, `processamento assíncrono/mensageria`, `integração com modelos de IA/ML`, `microsserviços`, `code review`. Only `microsserviços` and the async half were placed. The draft report at `reports/brivia-fullstack-pj-draft.md` states "O Maestro brief identifica BFF como lacuna", which no longer matches the brief on disk, whose `Gaps:` line holds only Cloud/DevOps certifications. **Not an Architect error:** `state/app-brivia-fullstack-pj.md` records at 19:21 that the brief's `Gaps` line was rewritten after the draft was already tailored. The document was built against the older brief. `CLAUDE.md` section 4 is explicit that a routed-around ecosystem token is a lost match for nothing. Costs R6, R12, R13, R15 and P2, worth **7 coverage points** | Claim `BFF`, `code review`, `boas práticas de engenharia` and `modelos de IA/ML` in Skills and in one existing bullet each, **each marked `[UNVERIFIED]` inline** as section 4 requires. Lucas confirms or strikes each before the package is sent. `certificações em Cloud/DevOps` stays out: it is the one real gap |
| 3 | `tex:78-113` (Experience) | **Six claims not traceable to `DOSSIER.md` ship with no `[UNVERIFIED]` marker.** `CLAUDE.md` section 4: "Any claim not in `DOSSIER.md` ships marked `[UNVERIFIED]` inline." The draft reports zero markers as a clean result; the rule makes zero markers wrong here, not right. Full list under "Claims I could not verify" | Mark all six inline, or drop the unsupported clause. None of the six carries a posting token, so removing any of them costs **zero** Gate 2 points. This is the cheapest fix on the list |
| 4 | `tex:78-90` (DexCare block) | **`React` appears in Experience only as `React Native`, in the 2021-2023 role.** It is the first technology in the posting's title and its first required bullet. The DexCare block, which a recruiter reads first, has none. Costs Gate 3.2 (-4) and holds the document's strongest section off the posting's strongest signal | `DOSSIER.md` records `React` in the DexCare stack as `[FACT-OBSERVED]`, read from the repos. The D5 bullet already says `monitoração de frontend no Datadog RUM`; the Architect used `frontend` there specifically to respect the 3-appearance cap. Naming React there instead would make it 4 appearances and trip the cap, so the cap is what must give, or another appearance must be freed. **This one is a real trade-off, not an oversight.** Raise it with Maestro rather than silently breaking the cap |
| 5 | `tex:75` (Skills) and `tex:96` (Luizalabs SEFAZ bullet) | **`RabbitMQ` and `AMQP` are absent from the whole document**, both 0 hits, though `DOSSIER.md` records them as FACT Skills tokens and the posting requires `mensageria`. The messaging group therefore carries one tool, `BullMQ`, under a two-concept label. Costs Gate 3.7 (-2) and leaves `mensageria` with Skills-only support | Add `RabbitMQ` and `AMQP` to the `Integrações e processamento assíncrono/mensageria` group. They are FACTs, they need no marker, Lucas's own instruction is "Skills token only, no service names on the CV", and that is exactly the placement. Zero risk, immediate Gate 3.7 recovery |
| 6 | `tex:71` and `tex:73` (Skills group labels) | `desenvolvimento web` and `bancos de dados relacionais` sit in `Skills` group labels and in **no** Experience bullet. Holds R3 and R8 at 1 of 4 each | Both phrases can be placed with **no new claim**. Raw 58 already reads `plataforma multi-tenant web e mobile sobre PostgreSQL`; raw 31 already models reads and writes in PostgreSQL. Rewording those two bullets to carry the posting's exact nouns is worth **+4** raw Gate 2 points |
| 7 | `tex:78-113` | `times multidisciplinares`, `Produto`, `UX`, `Dados` and `QA` are absent, all 0 hits. The nearest evidence is raw 60-61, `liderar o escopo de projetos e a comunicação com stakeholders`, a `DOSSIER.md` FACT | **Escalate to Lucas, one question.** The dossier confirms stakeholder communication at Lippaus but names no function. If Lucas confirms he worked with Produto, UX, Dados or QA, the token is placeable; if not, it stays out. Do not infer the functions from `stakeholders` |
| 8 | `tex:78-113` | Nine wrapped bullet continuation lines have no hanging indent. Gate 3.8, -1. Same defect as `reports/goodway-global-fullstack-gate.md` fix 11, still unfixed | A hanging-indent macro on `\resumeItem`. **Verify the result in the extraction, not in the source**: a source macro that looks right can still extract wrong. `memory: source-hanging-indent-macros-must-be-verified-in-pdf-extraction` |
| 9 | Apply note, not the CV | The posting states `❗ Exigência: Equipamento próprio para atuação`. `DOSSIER.md` records no fact. The draft report flagged this as an open question and it is still open | **Ask Lucas.** It belongs in the apply note's screening answers, never on the CV. Not a rubric row and not blocking, but the form will ask |
| 10 | `tex:79, 81, 84, 86` and `:93, 105, 110, 111` | Verb monotony. `Construí` opens **6 of 16** bullets and 3 of the 7 DexCare bullets. Reads as one template applied six times | Vary two or three openers. Outcomes, numbers and tokens stay identical. Not a rubric line item; it costs on the human scan |

---

## Claims I could not verify

Listed for Lucas. Not deleted, not defended. None carries an `[UNVERIFIED]`
marker today; see defect 3.

1. **`mais de 5 anos de experiência profissional em software`** — raw 6. Not a
   stated dossier number. It is arithmetic on the LinkedIn ground-truth dates,
   Mar 2021 to Sep 2026 = 5 yr 6 mo. Defensible. Listed so the derivation is on
   the record.
2. **`reservas orientadas a eventos em tempo real`** — raw 26. The dossier
   records `event-driven booking` and `healthcare scheduling at scale`.
   **`tempo real` / real-time is not recorded.**
3. **`que isolaram dados, garantiram contratos de API`** — raw 29. The dossier
   records multi-tenant JWT (SCH-343), Auth0, and OpenAPI/Swagger validators.
   These two outcome clauses are consistent with that; neither is recorded as
   an outcome.
4. **`Mantive implantações confiáveis`** and **`bloquear esteiras de CI/CD com
   Vitest e Jest`** — raw 50. Docker, Kubernetes, GCP, ArgoCD, Vitest and Jest
   are confirmed tools at Luizalabs. The reliability outcome and the CI/CD
   gating role are not recorded. **Do not remove blindly:** this bullet is the
   only Experience placement of `esteiras de CI/CD`, required token R14.
5. **`que apoiou a expansão nacional de varejistas`** — raw 58. The dossier
   confirms the multi-tenant web and mobile platform on PostgreSQL at Lippaus.
   It records no national rollout.
6. **`de uma startup de distribuição de bebidas`** — raw 69. Lippaus's industry
   and company stage are recorded nowhere in the dossier.
7. **`que deram visibilidade aos fluxos fiscais`** — raw 48. The dossier
   confirms fiscal back-office dashboards and the 18% figure. The visibility
   outcome is a phrasing, not a recorded fact. Weakest item on this list.

Verified and needing no action: every title, company and date against the
LinkedIn block, character for character; all seven percentages against the
dossier metric list (D2, D3, D5, D7, L2, L3, P2); the SPI description and its
33%, with no internal customer name printed, as instructed; every DexCare stack
token (FACT-OBSERVED from the repos); `Node.js`, `Java` and `Go` at Luizalabs;
the fiscal / NF-e / SEFAZ domain for Magazine Luiza; BullMQ, Docker,
Kubernetes, GCP, ArgoCD, Vitest and Jest as tools used; `React Native` at
Lippaus; Claude Code, Codex and agentic workflows; the Information Systems
degree at FAESA; `Vitória, ES, Brasil` on the contact line with no UTC offset
and no time-zone sentence; `Remoto` for DexCare and Luizalabs and
`Vitória, ES, Brasil` for both Lippaus roles, per the 2026-09-02 correction;
zero Ruby or Rails tokens; zero `[UNVERIFIED]` markers present.

---

## Analyzer's read, in one paragraph

This is the best-built document the team has shipped. Gate 0 is clean apart
from the accepted header exception, every title and date matches LinkedIn
character for character, all sixteen bullets hold the voice rule with no
exception, all seven numbers trace to the dossier, the 3-appearance cap holds
on every term, no Ruby or Rails token appears, and the Lippaus location now
follows the 2026-09-02 correction. It blocks on one line the document does not
say: that Lucas contracts as PJ with his own CNPJ, on a posting whose second
line is `Contratação: PJ`. That is one clause from a dossier FACT. The larger
cost is Gate 2 at 22, and that number is a timing accident, not sloppiness:
the Maestro brief's `Gaps` line was rewritten at 19:21, after the document was
already tailored, so five ecosystem tokens the current brief authorises were
routed around against the older brief. Under `CLAUDE.md` section 4 those are
lost matches for nothing. Fixing defects 1, 2,
5 and 6 costs no new facts from Lucas and takes the document from BLOCKED at
22 to passing Gate 1 at about 31, with a Gate 3 near 90.

---

## Fix list for the Architect

Blocking only. Gate 0 is PASS under the accepted `tabular*` exception, so
nothing from Gate 0 appears here. One item, the single Gate 1 FAIL.

1. **`resumes/brivia-fullstack-pj-pt.tex`, contact block (`tex:57-62`) or the
   Summary (`tex:66`) — state the entity type.** The posting contracts
   `em regime PJ`; the document contains zero occurrences of `PJ` and zero of
   `CNPJ`. Source the fact verbatim from `DOSSIER.md` Identity:
   `Contract types available: PJ with own CNPJ, US contractor (W-8BEN), CLT,
   EOR/Deel-style employment. All acceptable. [FACT, Lucas 2026-09-01]`.
   It is a FACT, so it ships with **no** `[UNVERIFIED]` marker. Add the tokens
   `PJ` and `CNPJ` so both reach the raw text. Never print a UTC offset and
   never print a time-zone overlap sentence (`CLAUDE.md` section 3, amended
   2026-09-02). Rebuild with tectonic, keep the document to one page, then
   confirm with:
   ```
   pdftotext resumes/brivia-fullstack-pj-pt.pdf - | grep -E 'PJ|CNPJ'
   ```
   This clears the only Gate 1 FAIL and unblocks the package.
