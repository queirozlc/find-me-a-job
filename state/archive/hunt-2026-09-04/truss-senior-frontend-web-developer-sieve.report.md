# Sieve task result — truss-senior-frontend-web-developer

Role: ATS Analyzer. Graded only. No CV file was edited.
Date: 2026-09-04
Gate report: `reports/truss-senior-frontend-web-developer-gate.md`

## Artifacts under test

- Posting and brief: `jobs/truss-senior-frontend-web-developer.md`
- CV source: `resumes/hunts/2026-09-04/truss-senior-frontend-web-developer/Lucas-Queiroz-Resume-en.tex`
- CV PDF: `resumes/hunts/2026-09-04/truss-senior-frontend-web-developer/Lucas-Queiroz-Resume-en.pdf`

Both extractions were produced before any judgement, per `RUBRIC.md`:
`pdftotext` raw and `pdftotext -layout`, 54 content lines each. Gate 0 and
Gate 2 were judged on the raw file.

## Verdict

**BLOCKED at Gate 1.**

| Gate | Result |
|---|---|
| Gate 0, parse integrity | PASS, 8 of 8 |
| Gate 1, knockouts | **FAIL** |
| Gate 2, retrieval coverage | 53/100, **FAIL** |
| Gate 3, human scan | 87/100 |

Gate 1 fails on one row: required-skill presence. The posting states
`experience with Redux/Redux Toolkit, React Router, and API-driven state
management`. The `and` makes those three cumulative. `Redux`, `Redux Toolkit`
and `React Router` have zero occurrences in the raw extraction.

Neither term is established by `DOSSIER.md`. The block is therefore a
candidate-fact gap, not an Architect defect. It cannot be cleared by editing
the document.

Gate 2 arithmetic: required tokens score 19 of 27 placement points across 9
rows, preferred tokens score 2 of 21 across 7 rows, giving
`100 * 59 / 102 = 58`. A 5-point stuffing penalty applies, because
`workflow`/`workflows` appears 5 times, above the 4-occurrence threshold.
Final 53. Three required tokens sit below 3 placement points:
`Redux / Redux Toolkit` at 0, `React Router` at 0, `frontend` at 1.

## Fix list

Ranked by cost. Items 1 and 2 are not Architect fixes.

1. `Redux` / `Redux Toolkit` absent. Gate 1 knockout and Gate 2 required token
   at 0/3. **Do not add it.** `DOSSIER.md` does not establish Redux for any
   role, and `CLAUDE.md` section 4 forbids inventing a fact to improve a match.
   Fix path: ask Lucas whether he used Redux or Redux Toolkit in production,
   record the answer and the role in `DOSSIER.md`, then place the exact posting
   token in `Skills` and in one relevant `Experience` bullet. If the answer is
   no, the gap stands and this is a partial match.
2. `React Router` absent. Gate 1 knockout and Gate 2 required token at 0/3.
   Same prohibition and the same fix path as item 1.
3. `frontend` reaches `Skills` only, 1/3. It appears once, as the category
   label `Frontend:` on raw line 12. The hyphenated `front-end` that the
   posting uses in its own title has zero occurrences. Fix: carry the posting's
   term into the DexCare front-end bullet, currently
   `Improved shared UI consistency across scheduling surfaces by developing
   reusable React components with CSS.` Keep the claim, the metric position and
   the XYZ shape. This invents nothing.
4. Posting title function words missing from the top 15%, Gate 3.1, 7 points.
   Lines 1 to 8 carry `Senior Software Engineer` but never `Front-End` or
   `frontend`. The job title must not change; `CLAUDE.md` section 1 binds it to
   LinkedIn. Fix in the Summary instead, currently
   `I am a Senior Software Engineer with 5+ years building production web
   applications with TypeScript, Node.js, React, and Go.`
5. `workflow`/`workflows` repeated 5 times, at raw lines 8, 14, 21, 28, 47.
   `CV-SPEC.md` caps any term at 3. Fix: cut two. Raw line 21
   `across healthcare scheduling workflows` and raw line 47
   `Supported operational and administrative workflows` carry it least.
6. `state management` absent as a phrase. The token scores 3 on the
   `API-driven state` head, but a boolean on `state management` misses. Fix:
   complete the phrase to the posting's wording, `API-driven state management`,
   in `Frontend: React | API-driven state | CSS` and in the bullet
   `building web interfaces with API-driven state backed by TypeScript
   services`.
7. Bare `testing` entry in `Testing: Jest | Vitest | testing`, raw line 13. It
   repeats the group label and reads as filler. Fix: drop it.
8. `invoicing` reaches `Experience` only, 2/3, raw line 33. Preferred and
   non-blocking. It is the one preferred token the dossier supports, so adding
   it to `Skills` recovers the last available preferred point.

## Verified facts

Titles, employers and dates were read read-only from the live LinkedIn profile
through the `Profile Check` portal on 2026-09-04, at
`https://www.linkedin.com/in/queiroz-lucas/details/experience/` and
`https://www.linkedin.com/in/queiroz-lucas/details/education/`. No edit was
made to the profile. The old PDFs under `~/Documents/Resumes/` were not used.

All 17 identity fields match: DexCare `Senior Software Engineer`
`Mar 2026 - Present`; Luizalabs `Mid-level Software Engineer`
`Jan 2024 - Mar 2026`; Lippaus Distribuidora `Mid-level Software Engineer`
`Jan 2023 - Jan 2024` and `Entry-level Fullstack Software Engineer`
`Mar 2021 - Jan 2023`; FAESA `Bachelor's degree, Information Systems`
`Feb 2022 - Dec 2025`. Both Lippaus roles are kept separate on the document,
so the promotion signal survives. Role locations follow `CLAUDE.md` section 3:
`Remote` for DexCare and Luizalabs, `Vitória, ES, Brazil` for both Lippaus
roles. The full field-by-field table is in the gate report.

Every metric on the document traces to the `DOSSIER.md` bullet-metric list:
15% (D2), 25% (D3), 20% (L2), 18% (L3), 26% (P2). No metric is unsourced. No
invented fact was found anywhere on the document.

Policy scans on the raw extraction, all clean:
- Forbidden stack tokens `ruby`, `rails`, `sidekiq`, `activerecord`,
  `activejob`, `rspec`, `devise`, `pundit`, `hotwire`: 0 occurrences.
- UTC offset, `GMT`, or any time-zone overlap statement: 0 occurrences, as
  `CLAUDE.md` section 3 requires.
- One language only, English, matching the posting language `en`.
- One page. `pdfinfo` reports `Pages: 1`. No images. Four embedded font
  subsets with Unicode maps. No NUL byte, no `?`, no ligature codepoint.

## Screening question for the apply note

The posting states `Format: full-time remote, with overlap
17:00/18:00-21:00/22:00 GMT+4`. Converted, that is 10:00 to 15:00 in Lucas's
GMT-3, inside a normal Brazilian business day. `DOSSIER.md` does not record
whether Lucas accepts the window, so his answer is not observable here. The
apply note must answer it. `CLAUDE.md` section 3 keeps it off the CV, and the
CV correctly carries no offset and no overlap sentence.

## Not observable

- Segment. `jobs/truss-senior-frontend-web-developer.md` records
  `Segment: not observable`, so no segment-specific judgement was made.
- Company origin, work authorization requirement, English proficiency
  requirement and degree requirement. The posting states none of them, so all
  four are recorded as `not stated`, never as `pass`.
- Lucas's Redux, Redux Toolkit, React Router, MUI, Emotion, SASS/SCSS, React
  Testing Library, Storybook, GraphQL, Cypress, Playwright, billing and
  payments experience. None is recorded in `DOSSIER.md`.

## Scope

Graded the resume against the posting and the rubric only. No CV file, profile
or cover letter was edited. Only the two report files were written. No subagent
was spawned. No Maestri message was sent.
