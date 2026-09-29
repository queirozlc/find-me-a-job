# Quill report — Paola Gesé, SeniorFrontendDeveloper (Remote Contract)

Date: 2026-09-04
Hunt: 2026-09-04-b
Language: English
Base: resumes/base-en.tex

## Outputs

- resumes/hunts/2026-09-04-b/paola-senior-frontend-svelte/Lucas-Queiroz-Resume-en.tex
- resumes/hunts/2026-09-04-b/paola-senior-frontend-svelte/Lucas-Queiroz-Resume-en.pdf
- resumes/hunts/2026-09-04-b/paola-senior-frontend-svelte/application-message.md
- state/paola-senior-frontend-svelte-quill.report.md (this file)

## Build and verification

- Built with tectonic. Zero errors. Font warnings only (Roboto italic at 9pt, cosmetic).
- Pages: 1.
- Raw and layout pdftotext extraction run. Contact block present in the body: Vitória, ES, Brazil, phone, email, LinkedIn, GitHub. No UTC offset.
- Section headers in the text layer: Summary, Skills, Language, Experience, Education.
- Four employment blocks present and separate: DexCare, Luizalabs, Lippaus Distribuidora (Mid-level), Lippaus Distribuidora (Entry-level). FAESA education block present.
- Titles and dates match DOSSIER.md LinkedIn ground truth character for character.
- Ligature check: `workflow` extracts 5 times.
- `grep -in 'ruby\|rails'` on the .tex: zero hits.
- All 16 base Experience bullets and all 7 metrics (15%, 25%, 7%, 33%, 20%, 18%, 26%) preserved. No role, bullet, or metric removed.
- PDF rendered and inspected visually.

## Format change from the base

The base uses a `tabular*` two-column role header. CV-SPEC item 2 and the Architect role file require a single-column header without `tabular*`. This tailored file uses a single-column header: company on one line, then `Title | Location | Dates` on the next line. Raw and layout extraction keep each role as one block. The base was not edited.

## Required token placement

| Token | Weight | Skills | Experience bullet | Status |
|---|---|---|---|---|
| JavaScript | 4 | Languages | Lippaus Entry-level: back-office dashboards in JavaScript | placed |
| TypeScript | 4 | Languages | DexCare: event-driven TypeScript services | placed |
| Svelte | 3 | not placed | not placed | UNSUPPORTED, see below |

## Preferred token placement

| Token | Skills | Experience bullet | Status |
|---|---|---|---|
| Node.js | Languages | Luizalabs: tax microservices in Node.js | placed |
| AWS Lambda | not placed | not placed | UNSUPPORTED, see below |

`AWS` alone is in Skills and in the DexCare AWS SDK v3 bullet.

## Practice tokens

| Posting term | Placement |
|---|---|
| clean code | Skills Frontend line; DexCare agentic-workflow bullet ("produce clean code") |
| agile teams | Skills Practices line; Luizalabs deploy bullet ("in agile teams") |
| UX | Summary; Skills Frontend line; DexCare release bullet ("the React UX") |
| communication | Skills Practices line ("Stakeholder communication"); Lippaus Mid-level bullet |
| cross-functional remote teams | Skills Practices line; DexCare first bullet; Summary ("fast-paced remote teams") |

## Unsupported required tokens, not added

1. **Svelte** (must-have, weight 3). DOSSIER.md has no Svelte fact. The base has none. The frontend evidence is React at DexCare and JavaScript dashboards at Lippaus. Svelte was not inferred from React or TypeScript. It does not appear on the CV. The DM states this openly.
2. **AWS Lambda** (nice-to-have). DOSSIER.md records AWS SDK v3 for S3, STS, Secrets Manager, and RDS Signer. No Lambda fact. Not added.

Expected gate result: Gate 2 required-token placement cannot fully PASS because Svelte is absent. This is an escalation to the Maestro, not a defect I can fix without a new dossier fact from Lucas.

## Term appearance counts (cap 3)

TypeScript 3, JavaScript 3, Node.js 3, React 3, AWS 3. A first draft placed `React Native` in the Lippaus mobile bullet, which pushed React to 4; reverted to the base wording.

## Content edits versus the base

- Summary: added JavaScript, "products in fast-paced remote teams", and "customer-facing web and mobile UX". Kept the AI mention. First person with I.
- Skills: added `Frontend: React | UX | Clean code` as the second line and a `Practices` line. Other lines unchanged.
- DexCare bullet 1: appended "working in a cross-functional remote team".
- DexCare bullet 5: "monitoring React with Datadog RUM" became "monitoring the React UX with Datadog RUM".
- DexCare bullet 6: "high-quality code" became "clean code".
- Luizalabs bullet 4: added "in agile teams".
- All other bullets verbatim from the base.

## Knockouts from the posting

- 5+ years of frontend experience: Mar 2021 to Sep 2026 is 5 years 6 months of fullstack work, stated as "5+ years" in the Summary.
- Remote contract, Latin America: Lucas is in Vitória, ES, Brazil. Contract types per dossier: PJ with CNPJ, W-8BEN US contractor, EOR. USD contract is acceptable.
- English: Fluent (C1), in the Language section.

## DM

application-message.md holds a ready-to-paste English LinkedIn DM. It states the Svelte gap plainly, claims only React, TypeScript, JavaScript, Node.js, and AWS work, and does not say an application was submitted. Nothing was sent.
