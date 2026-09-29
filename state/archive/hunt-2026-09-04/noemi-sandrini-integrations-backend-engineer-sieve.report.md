# Sieve task result — noemi-sandrini-integrations-backend-engineer

Seat: ATS Analyzer. Date: 2026-09-04.
Artifact: `resumes/hunts/2026-09-04/noemi-sandrini-integrations-backend-engineer/Lucas-Queiroz-Resume-en.pdf`
Posting: `jobs/noemi-sandrini-integrations-backend-engineer.md`. Segment: us-direct.
Full report with all tables: `reports/noemi-sandrini-integrations-backend-engineer-gate.md`.

No file was edited except this file and the gate report. No CV was changed. No subagent
was spawned. No Maestri message was sent. No outward action was taken.

## Verdict

**BLOCKED at Gate 1.** Do not ship this CV yet.

| Gate | Result |
|---|---|
| Gate 0, parse integrity | **PASS**, all 8 rows |
| Gate 1, knockouts | **FAIL**, 11 required rows with zero resume evidence |
| Gate 2, retrieval coverage | **FAIL**, 48/100 |
| Gate 3, human scan | 91/100 |
| Factual integrity vs live LinkedIn | **PASS**, all 12 rows match |
| Forbidden Ruby and Rails tokens | **PASS**, zero hits in source, raw, and layout |
| One-page PDF extraction | **PASS**, 1 page, clean text layer, no ligature damage |

## What is already right

- Gate 0 is fully clean. Four employment blocks segment correctly, both Lippaus roles stay
  separate, raw and layout reading order are identical, contact block is in the body, and
  the `fontspec` ligature fix works.
- Every employer, title, and date matches the live LinkedIn profile, read read-only through
  the `Profile Check` portal on 2026-09-04. The date drift that blocked the tractian
  application is not present here.
- Every one of the 21 Skills tokens also has an Experience placement. No orphan token.
- Every number traces to `DOSSIER.md`. Nothing is invented.
- The Architect refused every unsupported token in the Maestro brief. That was correct.

## Why it is blocked

Eleven stated posting requirements have zero resume evidence:
`Back-end` development, third-party API integrations, `OAuth 2.0`/`OIDC`, `Webhooks`,
`debugging`, `code review`, validation of AI-generated code, `OOP`, `SOLID`, software
design principles, and direct client communication.

The two most costly are the two halves of the role's own title. `Backend` and
`integrations` appear once each, and only inside the Skills category label
`Backend and integrations:`. A category label is not a listed token and neither word
reaches any Experience bullet.

## Fix list, Tier A — the Architect can do these now

Each is closable from `DOSSIER.md` alone. No new fact is created.

1. Place `Back-end` as a listed Skills token and in one DexCare Experience bullet. Use the
   posting's hyphenated spelling.
2. Add one DexCare bullet naming third-party API integration work. `DOSSIER.md` and
   `CV-SPEC.md` both record `Epic EMR integration` as observed fact read from the DexCare
   repos, and the CV omits it entirely. Also list `third-party API integrations` in Skills.
   This is the highest-value single change in the report.
3. Rewrite the DexCare AI bullet so it names validation of AI-generated code in the
   posting's wording. The activity is already described. Only the wording changes.
4. Cut `workflows` from 5 occurrences to 3. Change the ordinary-English uses in the DexCare
   first bullet and the Lippaus entry-level bullet. Keep all three `agentic workflows`.
   This removes a 5-point Gate 2 penalty and a CV-SPEC breach.
5. Work `back-end` and `integrations` into the Summary. **Do not touch the title.**
   `Senior Software Engineer` is fixed by CLAUDE.md rule 1 and rule 4.
6. Attach at least two unused approved metrics to existing bullets. D7, 33% less friction
   piloting new clients, fits this posting best. Only 3 of 11 bullets carry a measured Y,
   which breaches the CV-SPEC XYZ rule.
7. Vary the bullet verbs. `Supported` opens 4 of the 11 bullets.
8. Raise `\resumeRoleGap` above `\vspace{4pt}`. About 25% of the page is unused.

Tier A alone will not clear Gate 1. It closes 3 of the 11 failing rows and lifts Gate 2.

## Fix list, Tier B — blocked on Lucas

Nine Gate 1 rows have no support in `DOSSIER.md`. Writing them would be invention.
Each needs a yes or no from Lucas, then a `DOSSIER.md` entry. This seat does not edit
`DOSSIER.md`.

1. `OAuth 2.0` / `OIDC`. Did he implement these flows, or only consume Auth0? The dossier
   records `Auth0` and `multi-tenant JWT`, which is not the same claim.
2. `Webhooks`. Built or consumed?
3. `code review`. **Cheapest of the nine.** His own live LinkedIn profile already states
   it under Luizalabs: "Improved code review quality by introducing structured review
   practices and clearer pull-request documentation, reducing average review cycles from
   3-4 rounds to 1-2." The dossier does not carry it. Confirm it into the dossier.
4. `debugging`. Confirm with one concrete instance.
5. `OOP`. Confirm.
6. `SOLID`. Confirm.
7. Software design principles. Confirm.
8. Direct client communication. External clients, or internal stakeholders only? The live
   LinkedIn Lippaus entry says "working directly with stakeholders". The dossier records
   "stakeholder communication". Stakeholders are not stated to be external clients, and the
   distinction decides this row.
9. `AWS SQS`. Has he used it? Not blocking, because the posting writes "como", meaning
   "such as", so SQS is an example of the queues requirement, not a separate one. Still the
   strongest single lift available on that requirement.

## Notes for the Maestro

- Language. The posting text is pt-BR and the recruiter is Brazilian, but the posting says
  "empresa americana", the apply destination is `onstrider.com`, and the segment is
  us-direct. CV-SPEC gives `-en` to an international company, so the English build is
  defensible. The call is yours, not this seat's. The residual risk is a Portuguese
  first-pass screen.
- Six of the seven preferred requirements score zero: `SAML`, `Microsoft Entra ID`,
  `Microsoft Graph`, `Google Workspace APIs`, startup experience, and `ERP`/`CRM`. All are
  correctly refused as unsupported. This posting has a weak preferred-token ceiling for
  this candidate even after Tier A and Tier B are closed.
- `NestJS` absent is correct, not a defect. The posting writes "Express.js/NestJS" as an
  alternative and `Express` satisfies it.
- `DOSSIER.md` "LinkedIn ground truth" is current as of 2026-09-04 and agrees with the live
  profile on every row. No refresh is needed.
