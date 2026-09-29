# Quill report — Mindshaker Talent, Programador React (Pleno)

Date: 2026-09-04. Language: Portuguese. Base: `resumes/base-pt.tex`.
Status: complete. Not graded. Nothing sent or submitted.

## Files written

- `resumes/hunts/2026-09-04-b/mindshaker-react-pleno/Lucas-Queiroz-Resume-pt.tex`
- `resumes/hunts/2026-09-04-b/mindshaker-react-pleno/Lucas-Queiroz-Resume-pt.pdf` (1 page)
- `resumes/hunts/2026-09-04-b/mindshaker-react-pleno/application-message.md`
- `state/mindshaker-react-pleno-quill.report.md` (this file)

No base CV, ledger, or note was edited. No other tailored or archived resume was read.

## Required token placement

| Token | Weight | Habilidades | Experiência bullet | Support |
|---|---|---|---|---|
| React | 3 | Frontend line | DexCare, LaunchDarkly/OpenFeature bullet | Dossier: DexCare frontend React |
| TypeScript | 4 | Linguagens line | Resumo (first sentence). Not in a bullet, see note 1 | Dossier: DexCare TypeScript on Node.js |
| React Query ou SWR | 3 | not placed | not placed | Unsupported. No dossier fact. Not inferred from React. |
| Testing Library | 3 | not placed | not placed | Unsupported. No dossier fact. Not inferred from Vitest or Jest. |
| APIs REST | 2 | Backend line (posting spelling, replaces `REST APIs`) | DexCare, Auth0 JWT bullet | Base bullet |
| GraphQL | 2 | not placed | not placed | Unsupported. No dossier fact. |
| hooks | 1 | Frontend line | DexCare React bullet | Practice-level. Dossier support is React only; see note 2 |
| composição de componentes | 1 | Frontend line | DexCare React bullet | Practice-level. Same as hooks; see note 2 |
| gestão de estado | 1 | Frontend line | DexCare React bullet | Practice-level. Same as hooks; see note 2 |
| ponta a ponta / entrega em produção | 1 | none | Lippaus 2021 bullet: `de ponta a ponta, até a produção` | Base bullet, reworded |
| Inglês B2 ou superior | knockout | Idiomas: `Inglês: Fluente (C1)` | Resumo: `em inglês com equipes internacionais` | Dossier: C1, daily English at DexCare |
| 100% remoto, PJ (B2B) | knockout | not on CV | not on CV | Dossier: PJ with own CNPJ. Stated in the email only |

Note 1. `TypeScript` appears twice (Resumo, Habilidades). I removed it from the
DexCare Express/Koa bullet and did not add it to the React bullet to hold the
term under the cap of 3 while keeping `React` at 3. The Frontend skills line
carries `tipagem de componentes e props` to mirror `TypeScript aplicado a
componentes e props` without a fourth `TypeScript`. If the Analyzer requires
`TypeScript` inside a bullet, the fix is to restore `serviços TypeScript` in the
Express/Koa bullet and drop it from the Resumo first sentence.

Note 2. The dossier records `Frontend: React` at DexCare and nothing more
specific. `hooks`, `composição de componentes`, and `gestão de estado` are
weight-1 practice terms placed under the match policy "when they fit the role
history". They are not dossier facts. If the Maestro treats them as
unsupported, remove them from the Frontend line and from the DexCare React
bullet; the bullet then reads as in the base.

## Preferred tokens

Not placed, no dossier support: Design systems, componentes acessíveis,
acessibilidade, Next.js, Playwright, Cypress, performance de renderização,
revisões de código.

## Content changes from base-pt.tex

Facts unchanged: employers, titles, dates, locations, degree, all seven
metrics (7%, 25%, 15%, 33%, 20%, 18%, 26%), Idiomas line. All 16 base bullets
kept (7 DexCare, 4 Luizalabs, 3 Lippaus 2023, 2 Lippaus 2021).

- Resumo: `construindo sistemas` to `em sistemas`; added `em inglês com equipes
  internacionais`; `APIs multi-tenant na AWS` kept; `interfaces` clause reads
  `o frontend web`; `Antes, eu construí microsserviços fiscais de notas
  eletrônicas` (dropped `os` and `da emissão de`).
- Habilidades: new `Frontend` line `React | hooks | composição de componentes |
  gestão de estado | tipagem de componentes e props`, moved above Backend.
  `REST APIs` to `APIs REST`.
- DexCare: React bullet moved to first position and reworded to name `hooks,
  composição de componentes e gestão de estado`. `REST APIs` to `APIs REST`.
  Express/Koa bullet dropped the word `TypeScript` (cap) and shortened `para
  uma plataforma de agendamento em saúde` to `no agendamento em saúde`.
- Luizalabs: dashboards bullet reworded to `sobre os microsserviços fiscais,
  dando visibilidade e reduzindo chamados de suporte em 18%`. Deploy bullet
  `mantendo a produção confiável com suítes Vitest e Jest como gate do CI/CD`
  to `protegendo a produção com Vitest e Jest no gate do CI/CD`.
- Lippaus 2021: bullets reordered; end-to-end bullet gained `até a produção`.

Rewordings were made to keep one page. No bullet or metric was removed.

## Build and verification

- `tectonic Lucas-Queiroz-Resume-pt.tex`: OK. Font warnings only.
- `pdfinfo`: 1 page.
- `pdftotext` raw and `-layout`: contact line present with Vitória, ES, Brasil,
  phone, email, LinkedIn, GitHub. Headers RESUMO, HABILIDADES, IDIOMAS,
  EXPERIÊNCIA, FORMAÇÃO present. Four employment blocks present with company,
  title, dates, location each. FAESA block present. 16 bullets. 7 metrics.
- Ligatures: `fiscais`, `fluxos`, `flags` extract intact.
- `grep -in 'ruby\|rails'` on .tex and extracted text: zero hits.
- No UTC or GMT string.
- Term counts in extracted text: React 3, TypeScript 2, Node.js 3, BullMQ 3,
  PostgreSQL 3, hooks 2, composição de componentes 2, gestão de estado 2,
  APIs REST 2.
- Visual check of the rendered page: layout intact, no overflow.
- Header macro: kept the base `\resumeSubheading` unchanged, including its
  `tabular*` two-column header, because the base ships with it. Raw
  extraction keeps each role as one block.

## Email

`application-message.md` carries a Portuguese email with the exact subject
`Programador React · Pleno`. It claims only dossier facts, states remote, PJ
with own CNPJ, and English C1, and does not mention React Query, SWR, Testing
Library, GraphQL, or any preferred token. It does not say that anything was
sent.

## Escalations for the Maestro

1. Two mandatory tokens are unsupported: React Query or SWR, and Testing
   Library. Gate 2 will not fully pass on required-token placement.
2. GraphQL (responsibilities) is unsupported.
3. Decide on note 1 (TypeScript in a bullet) and note 2 (practice terms).
