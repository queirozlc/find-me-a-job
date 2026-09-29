# ATS Analysis — resumes/hunts/2026-09-04-g/p7-group-fullstack/Lucas-Queiroz-Resume-pt.pdf vs p7-group-fullstack
Segment: br-pj   Date: 2026-09-04
Task: p7-group-fullstack-sieve. Analyzer: Sieve. Hunt 2026-09-04-g.
Scope set by Maestro: semantic truth, Role Eligibility Check, required-token
evidence, recruiter readability. Deterministic gate PASS
(state/p7-group-fullstack-deterministic-gate.json, 2026-09-04T21:18:27+00:00)
and base File Readability PASS (state/hunt-2026-09-04-g-base-sieve.report.md)
are reused as evidence. Cached identity only. No portal. No CV edit. No
delegation.

## Verdict
READY

## Decision Explanation
No blocking reason.

One item stays open before submission. It is a screening answer, not a CV
defect, and it does not block the CV:

| Item | Posting text | Evidence checked | Evidence found | Classification | Next action |
|---|---|---|---|---|---|
| Full-time availability | `⏱️ Atuação full-time` | DOSSIER.md Identity and Open questions; application-note.md screening answers | DOSSIER.md records contract types (`PJ with own CNPJ ... All are acceptable`) and `Notice period: Not recorded`. It does not record full-time availability for a new engagement. application-note.md already prints: `Disponibilidade full-time de Lucas: não registrada no dossiê. Lucas confirma antes de enviar.` | Before-submission screening answer. LUCAS CONFIRMATION. Not a CV FIX, not a ROLE MISMATCH. Silence is not a mismatch. | Lucas confirms full-time availability before he sends the form. No CV change. |

## Inputs read
- ATS-KNOWLEDGE.md, RUBRIC.md, CV-SPEC.md, DOSSIER.md, CLAUDE.md (career root).
- state/p7-group-fullstack-review-packet.md (posting, manifest, delta, claim
  manifest, deterministic gate).
- jobs/p7-group-fullstack.md (identical to the packet posting text, diff
  shows only a trailing blank line).
- state/hunt-2026-09-04-g-base-sieve.report.md (base File Readability PASS).
- state/hunt-2026-09-04-g-linkedin-identity.json (captured
  2026-09-04T20:01:30+00:00, sha256 ea38bc6f...50b2a).
- state/p7-group-fullstack-quill.report.md and
  state/p7-group-fullstack-quill-layout.report.md (Architect claims, checked,
  not trusted).
- resumes/hunts/2026-09-04-g/p7-group-fullstack/Lucas-Queiroz-Resume-pt.tex,
  Lucas-Queiroz-Resume-pt.pdf, application-note.md.
- resumes/base-pt.tex, diffed against the tailored .tex.
- Extraction, run by me on the tailored PDF:
  `pdftotext <pdf> -` (raw, 75 lines) and `pdftotext -layout <pdf> -`
  (layout). All File Readability and Resume Evidence judgements are on the
  raw file.

## File Readability Check

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | Raw extraction 75 lines, 2 pages, producer xdvipdfmx, Roboto CID fonts embedded with ToUnicode (`pdffonts` uni=yes for all 4 fonts). Deterministic gate `pdf_extraction` PASS. Same toolchain as the base PASS |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes (`tr -cd '\000' \| wc -c`), 0 `?`, 0 code points in U+FB00-FB06. `workflow` 2 hits, `office` 2 hits (`backoffice`), `fluxo` 3 hits, all intact. `profile`, `efficient`, `conflict` absent from the text, not testable. Preamble is byte-identical to the base preamble (`Ligatures=NoCommon`), per tex diff |
| 0.3 | Contact block recoverable | PASS | Raw line 3, body text, `\pagestyle{empty}`: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. Deterministic gate `contact` PASS |
| 0.4 | Section headers verbatim | PASS | Standalone raw lines 5 `RESUMO`, 11 `HABILIDADES`, 19 `IDIOMAS`, 22 `EXPERIÊNCIA`, 69 `FORMAÇÃO`. Source strings canonical PT allowlist. Deterministic gate `sections` PASS |
| 0.5 | Employment-block segmentation | PASS | 4 role blocks, each company / title / dates / location on 4 consecutive raw lines (23-26, 40-43, 53-56, 62-65), then its bullets, 7 / 4 / 3 / 2. No merge, no split. Page break (form feed) falls before raw line 62 `Lippaus Distribuidora`; page 2 opens with the full 4-line Entry-level header and both bullets, then Formação. Deterministic gate `roles` and `layout` PASS |
| 0.6 | Date parseability | PASS | `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`, ASCII hyphen, each on the line directly after its title. 0 EN DASH characters in tex or raw |
| 0.7 | Reading order | PASS | Raw and layout extraction, form feeds removed and whitespace normalized, are line-for-line identical (`diff` empty) |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` empty. Tex has 0 hits for `tabular`, `minipage`, `parbox`, `includegraphics`, `fancyhdr`, `multicol`, `tcolorbox`, icon fonts. The prior `tabular*` header was removed by the layout fix; the current preamble is the approved base preamble |

## Semantic truth

### Titles, dates, employers, locations against the LinkedIn cache

Each string searched verbatim in the cached profile text and in the raw
extraction.

| Company (CV raw) | Title (CV raw) | Dates (CV raw) | Location (CV raw) | In cache |
|---|---|---|---|---|
| DexCare | Senior Software Engineer | Mar 2026 - Present | Remoto | yes (`Seattle ... · Remote`, city not printed per DOSSIER) |
| Luizalabs | Mid-level Software Engineer | Jan 2024 - Mar 2026 | Remoto | yes |
| Lippaus Distribuidora | Mid-level Software Engineer | Jan 2023 - Jan 2024 | Vitória, ES, Brazil | yes (`Vitória, Espírito Santo, Brazil · On-site`) |
| Lippaus Distribuidora | Entry-level Fullstack Software Engineer | Mar 2021 - Jan 2023 | Vitória, ES, Brazil | yes |

Education: cache covers the Experience page only. Checked against DOSSIER.md
LinkedIn ground truth: `FAESA`, `Information Systems`, `Feb 2022 – Dec 2025`.
CV prints `FAESA` / `Bacharelado em Sistemas de Informação` /
`Feb 2022 - Dec 2025` / `Vitória, ES, Brazil`. Months identical, ASCII
hyphen per CLAUDE.md rule 1 clarification. Deterministic gate
`linkedin_identity` PASS agrees.

### Metrics
Raw extraction, in order: 15%, 25%, 7%, 33%, 20%, 18%, 26%. Seven, each once.
Match DOSSIER.md D2, D3, D5, D7, L2, L3, P2. No other number except
`mais de 5 anos` (Mar 2021 to Sep 2026 is 5 years 6 months) and `AWS SDK v3`.
Tex diff against resumes/base-pt.tex shows every metric unchanged.

### Content delta against the base, fact by fact
Tex diff: 12 changed lines, all rewording or token insertion. 16 bullets in
base and tailored. No bullet removed. No metric changed.

| Change | Source of the underlying fact | Judgement |
|---|---|---|
| Resumo adds `JavaScript` and `e LLMs` | DOSSIER: JavaScript at Lippaus and Luizalabs; AI mention required; Claude Code and Codex are LLM tools | True |
| Skills labels renamed to posting phrases (`Backend e mensageria`, `Dados (relacionais e não relacionais)`, `Cloud, deploy e observabilidade`, `Testes e IA aplicada`) | Labels only, tokens under them unchanged except additions below | True, cosmetic |
| Skills adds `NestJS`, `webhooks`, `APIs REST` (spelling), `LLMs`, `RAG`, `integrações com modelos` | DOSSIER match policy weight 2 and 3: exact posting terms allowed; CLAUDE.md rule 4: no verification markers for frameworks and tools | Allowed by policy |
| DexCare bullet 3 `REST APIs` to `APIs REST` | Spelling to posting | True |
| DexCare bullet 4 adds `em bancos relacionais e não relacionais,` | DOSSIER seeded data: PostgreSQL, DynamoDB, Redis observed in repos | True |
| DexCare AI bullet adds `com LLMs e contexto RAG sobre regras compartilhadas` | DOSSIER: built agent environments with shared rules, lint, complexity limits, testing. `RAG` not named in DOSSIER. Quill report: `No RAG product, no new result` | Wording stretch, see defect 1. Not a fabricated credential |
| Luizalabs bullet 1 `Node.js` to `Node.js (NestJS)` | DOSSIER: `Stack: Node, Java, and others`; LinkedIn cache: `Node.js and Java`. `NestJS` not named in either | Allowed by match policy weight 3. See defect 2 |
| Luizalabs bullet 2 adds `mensageria e processamento assíncrono` | DOSSIER: BullMQ at Luizalabs, SEFAZ async migration, approved | True |
| Lippaus bullet 2 adds `com terceiros via webhooks` | LinkedIn cache Lippaus: `third-party integrations`. `webhooks` not named | `integrações com terceiros` true. `webhooks` allowed by policy weight 2. See defect 2 |

Stack and banned content: 0 hits in raw for `ruby`, `rails`, `sidekiq`,
`activerecord`, `rspec`, `UTC`, `GMT`, `overlap`, `fuso`, `code review`,
`Brasil`. Deterministic gate `forbidden_terms` and `claim_allowlist` PASS
agree. `RabbitMQ` and `AMQP` appear in Skills only, as DOSSIER prescribes.

Carried over from the approved base, unchanged, already recorded in the base
sieve report: Summary clause `para uma empresa dos EUA` (Lucas approved the
base preview) and `Present` in the PT date line (LinkedIn verbatim). No new
finding.

### Application note (resumes/hunts/2026-09-04-g/p7-group-fullstack/application-note.md)
Draft, not a sent message. Read in full.

- Status line: `RASCUNHO. Lucas envia. Nenhum agente envia.` Message body:
  `pretendo me candidatar pelo formulário indicado`. No statement that a
  submission occurred. Correct.
- Personal claims, each traced: PJ with own CNPJ, CLT and EOR acceptable
  (DOSSIER Identity); 100% remote from Vitória, ES, Brazil (DOSSIER);
  `Fuso GMT-3` in screening answers only, not on the CV (CLAUDE.md 3,
  CV-SPEC); English `Fluente (C1)`, daily English work with US teams
  (DOSSIER Identity); 33% SPI (DOSSIER D7); 20% SEFAZ (L2); 26% Lippaus (P2);
  React with Datadog RUM, RabbitMQ/AMQP at DexCare (DOSSIER seeded data);
  Claude Code and Codex daily use (DOSSIER). No unsourced personal claim
  found.
- Unknowns are printed as unknown, not answered: salary, start date or
  notice, Next.js, Vite, own RAG product, form questions.
- Full-time availability: handled as a screening answer with
  `Lucas confirma antes de enviar`. Correct classification.
- Same `contexto RAG` wording as the CV. Defect 1 applies to the note too.

## Role Eligibility Check

| Check | Source (posting text) | Result |
|---|---|---|
| Work authorization / entity type | `📄 Contratação PJ` | PASS. DOSSIER.md Identity: `PJ with own CNPJ ... All are acceptable`. Application note states PJ with own CNPJ |
| Location or time-zone overlap | `📍 Trabalho remoto`. No country, city, or time-zone stated | PASS for remote. Time-zone overlap: not stated |
| Dedication | `⏱️ Atuação full-time` | Open, screening answer. Not a CV field. DOSSIER silent on availability. LUCAS CONFIRMATION before submission. Not FAIL, not ROLE MISMATCH. See Decision Explanation |
| Minimum years of experience | not stated | not stated |
| English proficiency requirement | not stated | not stated |
| Degree requirement | not stated | not stated |
| Each required skill | `Principais conhecimentos` list | See Resume Evidence Check. All 9 manifest tokens present verbatim in Skills and Experience |

No FAIL row.

## Resume Evidence Check: 87/100, PASS

The posting labels its list `Principais conhecimentos` and does not separate
required from preferred. The manifest (Maestro intake) sets 9 required tokens
and 0 preferred. I grade those 9 as required, weight 3. The remaining posting
knowledge phrases are graded as preferred, weight 1, so that the score
reflects them without inventing a requirement level the posting did not
state. `Next.js` and `Vite` are alternatives to `React` (`React, Next.js ou
Vite`); React satisfies the line, so they are excluded from the score and
listed under Match limits.

Counts are word-boundary matches on the raw extraction, case-insensitive.
Sections by header line.

| Token | Weight | Skills | Experience (bullet) | Resumo | Total count | Placement | Points |
|---|---|---|---|---|---|---|---|
| JavaScript | required 3 | Linguagens | Lippaus Entry bullet 1 `dashboards internos de backoffice em JavaScript` | 1 | 3 | Skills + Experience | 3 |
| TypeScript | required 3 | Linguagens | DexCare bullet 1 `serviços TypeScript orientados a eventos` | 1 | 3 | Skills + Experience | 3 |
| Node.js | required 3 | Linguagens | Luizalabs bullet 1 `microsserviços fiscais distribuídos em Node.js (NestJS)` | 1 | 3 | Skills + Experience | 3 |
| NestJS | required 3 | Backend e mensageria | Luizalabs bullet 1 | 0 | 2 | Skills + Experience | 3 |
| React | required 3 | Frontend | DexCare bullet 5 `monitoração React no Datadog RUM` | 1 | 3 | Skills + Experience | 3 |
| APIs REST | required 3 | Backend e mensageria | DexCare bullet 3 `APIs REST multi-tenant com Auth0 JWT` | 0 | 2 | Skills + Experience | 3 |
| webhooks | required 3 | Backend e mensageria | Lippaus Mid bullet 2 `integrações com terceiros via webhooks` | 0 | 2 | Skills + Experience | 3 |
| LLMs | required 3 | Testes e IA aplicada | DexCare bullet 6 `com LLMs e contexto RAG` | 1 | 3 | Skills + Experience | 3 |
| RAG | required 3 | Testes e IA aplicada | DexCare bullet 6 | 0 | 2 | Skills + Experience | 3 |
| relacionais e não relacionais | preferred 1 | Dados label | DexCare bullet 4 | 0 | 2 | Skills + Experience | 3 |
| integrações | preferred 1 | `integrações com modelos` | Lippaus Mid bullet 2 | 0 | 2 | Skills + Experience | 3 |
| mensageria | preferred 1 | Backend label | Luizalabs bullet 2 | 0 | 2 | Skills + Experience | 3 |
| processamento assíncrono | preferred 1 | absent | Luizalabs bullet 2 | 0 | 1 | Experience only | 2 |
| testes | preferred 1 | Testes label | DexCare bullet 6 `e testes` | 0 | 2 | Skills + Experience | 3 |
| deploy | preferred 1 | Cloud label | absent | 0 | 1 | Skills only | 1 |
| observabilidade | preferred 1 | Cloud label | absent | 0 | 1 | Skills only | 1 |
| IA aplicada | preferred 1 | Testes label | absent | 0 | 1 | Skills only | 1 |
| integrações com modelos | preferred 1 | Testes e IA aplicada | absent | 0 | 1 | Skills only | 1 |
| arquitetura | preferred 1 | absent | absent | 0 | 0 | absent | 0 |
| segurança | preferred 1 | absent | absent | 0 | 0 | absent | 0 |

Required: 9 tokens × 3 points × weight 3 = 81 of 81.
Preferred: 18 points of 33 (11 tokens × 3).
coverage = 100 × (81 + 18) / (81 + 33) = 86.8, reported 87.
Stuffing penalty: 0. Highest count of any token is 3 (JavaScript,
TypeScript, Node.js, React, LLMs, Go, PostgreSQL, BullMQ, multi-tenant).
Deterministic gate `required_token_placement` PASS agrees.

Required tokens without Skills and Experience placement: none.

## Recruiter Readability Score: 90/100

Target title is the posting title `Desenvolvedor(a) Full Stack`. Relevance
for 3.2 is judged against the posting list.

| # | Check | Points | Evidence |
|---|---|---|---|
| 3.1 | Target title in top 15% | 10/15 | Raw line 6 of 75 (8%) carries `Senior Software Engineer` and `sistemas backend e fullstack`. The posting phrase `Desenvolvedor Full Stack` does not appear. Job titles are LinkedIn-locked (CLAUDE.md rule 1), so only the Summary could carry it. Partial credit |
| 3.2 | 3 most relevant bullets first in most recent role | 17/20 | DexCare bullets 1-3: TypeScript event-driven services, Epic EMR integration 15%, APIs REST multi-tenant 25%. All three map to posting lines (JavaScript e TypeScript, integrações, APIs REST). The AI bullet (`LLMs`, `RAG`, posting line 8) is 6th and the React bullet is 5th. A reorder, no content change, would put a posting-named area in the first 3 |
| 3.3 | Past-tense action verb and outcome | 13/15 | All 16 bullets open with a first-person past-tense verb, subject omitted: Construí ×7, Integrei, Modelei, Reduzi, Ajudei a implementar, Migrei, Implantei, Processei, Liderei, Desenvolvi. 0 hits for `Responsável`, present-tense duty lists, third person. Two bullets state no outcome: D4 `Modelei leituras e escritas ... via AWS SDK v3` and E2 `Construí funcionalidades para clientes de ponta a ponta ...`. Same as the base finding; DOSSIER says leave as is |
| 3.4 | At least 3 bullets with a real number | 15/15 | 7 bullets, all numbers traced to DOSSIER.md |
| 3.5 | Experience completeness | 10/10 | 4 roles, 16 bullets, 7 metrics, identical set to base-pt.tex (tex diff shows rewording only). 2 pages; page 2 holds the whole Lippaus Entry-level block and Formação, no split block |
| 3.6 | No unsupported buzzwords | 10/10 | 0 hits for team player, results-driven, passionate, apaixonado, proativo, senso de dono, dinâmico, sinergia |
| 3.7 | Skills grouped by category | 10/10 | 6 labelled groups: Linguagens, Backend e mensageria, Dados, Frontend, Cloud, Testes e IA aplicada |
| 3.8 | Scannable | 5/5 | Bold company, italic title and location, consistent 3pt role gap, single column, clean page break before a full role header |

## Defects, ranked by cost
No blocking defect. Non-blocking, in order:

1. `contexto RAG sobre regras compartilhadas` (DexCare bullet 6, and the same
   sentence in application-note.md) — semantic truth — DOSSIER.md records
   agent environments with shared rules, lint, complexity limits and tests.
   It does not record RAG. Quill's own report says `No RAG product`. The
   sentence describes rule files loaded as context, which is a stretch of
   the term. Lucas decision: keep it only if he will defend `RAG` in an
   interview. If not, the Architect changes the bullet to
   `Construí ambientes Claude Code e Codex, com LLMs sobre regras
   compartilhadas, lint, ...` and moves `RAG` out of Experience. That would
   drop `RAG` to Skills only (1 point) and the required-token check would
   FAIL under the manifest as written, so the Maestro would also have to
   reclassify `RAG` as preferred. Cross-reference: application note says
   `Produto próprio de RAG: não registrado no dossiê`, which is the honest
   screening answer.
2. `NestJS` at Luizalabs (bullet 1) and `webhooks` at Lippaus (bullet 2) —
   semantic truth — neither term is named in DOSSIER.md or in the LinkedIn
   cache for those employers. Both placements are allowed by the DOSSIER
   match policy (framework weight 3, tool weight 2, exact posting terms) and
   CLAUDE.md rule 4. Recorded so Lucas sees them before he sends. No action
   unless Lucas rejects either term.
3. Target title phrase absent from the Summary — Recruiter Readability 3.1 —
   Summary line 6 says `sistemas backend e fullstack`. Titles cannot change.
   Optional Architect wording: `Eu sou Senior Software Engineer e
   desenvolvedor full stack com mais de 5 anos ...`. Lucas decision, no
   metric or title touched.
4. AI bullet is 6th in DexCare — Recruiter Readability 3.2 — move DexCare
   bullet 6 (`Construí ambientes Claude Code e Codex ...`) to position 3 or
   4. Reorder only, no text change. Optional.
5. D4 and E2 carry no outcome — Recruiter Readability 3.3 — inherited from
   the base; DOSSIER says leave as is. No action.

## Before submission (not CV defects)
- Full-time availability: Lucas confirms. DOSSIER and note are silent; the
  note already flags it. See Decision Explanation.
- Salary or PJ rate, start date or notice: not recorded, Lucas answers, as
  the note states.

## Match limits
- `Next.js`, `Vite`: not placed. Alternatives to `React` in the posting;
  React is placed. DOSSIER does not record them, note says so.
- `arquitetura`, `segurança`: literal words absent. Related evidence exists
  (multi-tenant SPI, Auth0 JWT, `segredos e dados isolados`) but not the
  posting's words. Weight 1 practice terms.
- `deploy`, `observabilidade`, `IA aplicada`, `integrações com modelos`:
  Skills only.
- `processamento assíncrono`: Experience only.

## Not done
- No CV edit, no note edit, no delegation, no portal, no re-run of the
  deterministic gate or the base sieve.
