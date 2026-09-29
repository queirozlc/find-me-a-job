# Sieve task result — ciandt-senior-web-software-engineer

Role: ATS Analyzer. Graded, did not edit the CV.
Date: 2026-09-04
Hunt: 2026-09-04
Application: CI&T, Senior Web Software Engineer, Brazil
Segment: agency
Posting: https://www.linkedin.com/jobs/view/4454020765/ (text read from the local job file; the
URL itself was not re-opened)
Full gate report: `reports/ciandt-senior-web-software-engineer-gate.md`

## Verdict

**BLOCKED.** Do not deliver this CV to Lucas yet.

- Gate 0 — Parse integrity: **8/8 PASS**, with one recorded regression under 0.5
- Gate 1 — Knockouts: **FAIL** on six rows
- Gate 2 — Retrieval coverage: **67/100, FAIL**
- Gate 3 — Human scan: **86/100**
- Factual integrity against live LinkedIn and the refreshed `DOSSIER.md`: **FAIL**, two role
  date ranges

No blended score is emitted. There is no such thing as a vendor ATS score out of 100.

**The most important thing in this report is not a defect list.** Three required items on this
posting have no support in any local source: `Next.js`, `CMS` with `content modeling`, and
`PHP`. A fourth, designing and documenting technical solutions and data flows, is unsupported
today. Applying every writable fix still leaves Gate 1 failing and Gate 2 at 80/100. **This
application cannot be cleared by editing. It needs answers from Lucas, or a decision to apply
with the gaps declared.**

## Files under test

- CV source: `resumes/hunts/2026-09-04/ciandt-senior-web-software-engineer/Lucas-Queiroz-Resume-en.tex`
- CV PDF: `resumes/hunts/2026-09-04/ciandt-senior-web-software-engineer/Lucas-Queiroz-Resume-en.pdf`
- Both artifacts exist. The mandatory extraction ran first, on the real PDF: `pdftotext -layout`
  and `pdftotext` raw. Gate 0 and Gate 2 were judged on the raw stream, 55 lines, 1 page.

## Fix list for the Architect

Writable now, from sources already on disk. All four are blocking.

1. `Lucas-Queiroz-Resume-en.tex` line 65. Change `{DexCare}{Jan 2026 - Present}` to
   `{DexCare}{Mar 2026 - Present}`. LinkedIn and the refreshed `DOSSIER.md` both read
   `Mar 2026 - Present`.

2. `Lucas-Queiroz-Resume-en.tex` line 76. Change `{Luizalabs}{Jan 2024 - Jan 2026}` to
   `{Luizalabs}{Jan 2024 - Mar 2026}`. LinkedIn and the refreshed `DOSSIER.md` both read
   `Jan 2024 - Mar 2026`.
   These are the same two errors reported on the `tractian` build earlier today. That build had
   a stale `DOSSIER.md` and no correct local source. This one did. `DOSSIER.md` now carries the
   correct strings verbatim under "LinkedIn ground truth — captured verbatim 2026-09-04".

3. Place `English`. Zero occurrences in this CV, and the posting lists "Advanced English
   communication skills" under Required Skills & Experience, not as a bonus. The fact is
   supported verbatim in `DOSSIER.md` Identity: "English proficiency: Advanced / C1. Daily
   English-only work with US teams at DexCare." The sibling `tractian` build carried
   `Advanced English (C1)` on its Skills line; this build dropped it, on the posting where it is
   required rather than optional. A required token needs `Skills` plus one `Experience` bullet,
   so place both. The DexCare block is the honest host, because `DOSSIER.md` ties the daily
   English-only work to DexCare specifically.

4. Place `clean code`. Zero occurrences. The posting names it in the required list. The CV writes
   `code quality` instead, at source lines 71 and 72. `ATS-KNOWLEDGE.md` section 4.1 says to
   preserve the posting's exact spelling and never rely on alias expansion. The supporting fact
   already exists in `DOSSIER.md` ("shared rules, codebase enforcement (lint, cyclomatic
   complexity limits, testing)"), so this is a wording change plus a Skills placement, not a new
   claim.

5. Restore the requirements-analysis bullet. The posting requires "analyzing functional and
   non-functional requirements and contributing to technical implementation decisions". No CV
   bullet covers it. `DOSSIER.md` records, among the bullets Lucas approved, "project scoping and
   stakeholder communication" and "customer-facing features end to end". The Architect dropped
   that approved bullet from this build. Restore it in the Lippaus Mid-level block, source lines
   87-90, in XYZ form and past tense. This needs no new fact from Lucas.

Non-blocking, worth doing in the same pass.

6. Reorder the DexCare bullets. Bullets 4 and 5 (source lines 71 and 72) carry five required
   tokens between them: `testing`, `debugging`, `maintainability`, `AI coding assistants`,
   `agentic workflows`. They sit below two healthcare-domain bullets this posting never asks
   for. Move them to positions 2 and 3. Costs nothing factual, recovers 8 Gate 3 points.

7. Restore the role-boundary blank lines in the extraction. The raw stream of this build carries
   no blank line at any of the three role boundaries; the `tractian` build in this same hunt
   carries one at all three. Segmentation still passes, so this is not a Gate 0 failure, but
   employment-block segmentation is the single most valuable parse property in
   `ATS-KNOWLEDGE.md` and it should not drift by accident. Two macro edits differ and are the
   candidates: `\resumeSubheading` gained `\small` on the location and date lines and tightened
   `\\[-2pt]` to `\\[-1pt]`; `\resumeRoleGap` grew from `\vspace{2pt}` to `\vspace{4pt}`. I did
   not isolate which one did it and I assert no cause. Revert to the `tractian` spacing, rebuild,
   and confirm `grep -c '^$'` on the raw extraction returns 9, not 6.

## Escalate to Lucas. Not writable. Do not invent any of these.

8. **CMS and content modeling.** This is the posting's central initiative: "a CMS modernization
   and migration initiative", with the required item "Experience with CMS concepts, including
   content modeling, APIs, integrations, and modern CMS architectures." `DOSSIER.md` records no
   CMS fact of any kind. Ask whether Lucas has worked with a CMS, headless or traditional, and
   with content modeling. Record the answer in `DOSSIER.md` before any token is placed.

9. **PHP.** Required item: "Familiarity with PHP-based applications and the ability to read,
   understand, debug, and navigate an existing PHP codebase. Deep PHP specialization is not
   required." `DOSSIER.md` records no PHP fact. The bar is low, reading and navigating rather
   than building, so a real answer may well exist. Note for the Maestro: placing a PHP token
   would not breach CLAUDE.md section 4, which states that frameworks and tools do not decide
   primary-stack eligibility, and this posting's primary stack is JavaScript and TypeScript.

10. **Next.js, or a directly comparable modern web framework.** Required item: "Hands-on
    experience with React and Next.js, or directly comparable modern web frameworks."
    `DOSSIER.md` supports React and no other web framework. Ask whether Lucas has shipped
    Next.js, or something that sits in the same place, for example Remix, Nuxt or Astro. I did
    not treat React as satisfying the Next.js half: React is one of the two terms the posting
    already asked for, not a comparable substitute for the other, and it is the library Next.js
    is built on rather than a peer of it. This preserves the uncertainty the Maestro brief asked
    me to preserve, and leaves the judgement with Lucas.

11. **Designing and documenting technical solutions and data flows.** Required item: "Ability to
    design and document technical solutions, integrations, application workflows, and data
    flows." `document`, `documentation` and `data flow` each have 0 occurrences, and
    `DOSSIER.md` records no documentation fact. One pointer that may shorten the conversation,
    offered as a lead and not as evidence I scored: the DexCare entry on Lucas's own LinkedIn
    profile contains the line "Authored a Product Design Review for the Customer Information and
    Configuration experience". I read that while verifying titles and dates. It is profile prose,
    not one of my listed local sources, so I gave it no credit. If Lucas confirms it, record it
    in `DOSSIER.md` and the Architect can then write the bullet from a proper source.

## Correction to the Maestro brief

The brief lists "Advanced English" under "Required tokens or facts not supported by
`DOSSIER.md`". **That is wrong.** `DOSSIER.md` Identity records it verbatim: "English
proficiency: Advanced / C1. Daily English-only work with US teams at DexCare." It is fully
supported and should be placed, per fix 3. The brief's other three unsupported items,
`Next.js`, CMS with content modeling, and PHP, are correctly identified.

## Projected scores

- Today: required points 30 of 45, **Gate 2 = 67/100, FAIL**.
- After fixes 3 and 4, with nothing new from Lucas: required points 36 of 45,
  `100 * (36*3) / 135` = **80/100. Still FAIL**, because `Next.js`, `CMS` and `PHP` stay at 0.
- After fixes 3 and 4 plus confirmed answers on all of `Next.js`, `CMS` and `PHP`: 45 of 45,
  **100/100, PASS**.
- Fixes 1, 2, 5, 6 and 7 change Gate 2 by nothing. Fixes 1 and 2 are factual-integrity blockers
  under CLAUDE.md rule 1 and must be made regardless. Fix 5 clears a Gate 1 row. Fix 6 recovers
  8 Gate 3 points. Fix 7 protects the segmentation property.

## Verification performed

LinkedIn, read-only through the `Profile Check` portal on 2026-09-04. No edit action was sent.
- https://www.linkedin.com/in/queiroz-lucas/details/experience/
- https://www.linkedin.com/in/queiroz-lucas/details/education/

Live profile today: DexCare `Senior Software Engineer` `Mar 2026 - Present · 7 mos`; Luizalabs
`Mid-level Software Engineer` `Jan 2024 - Mar 2026 · 2 yrs 3 mos`; Lippaus Distribuidora
`Mid-level Software Engineer` `Jan 2023 - Jan 2024`; Lippaus Distribuidora `Entry-level
Fullstack Software Engineer` `Mar 2021 - Jan 2023`; FAESA `Bachelor's degree , Information
Systems` `Feb 2022 – Dec 2025`.

The refreshed `DOSSIER.md` matches the live profile on every row. The CV matches on all four
employers, all four job titles, both Lippaus date ranges and the education row. It mismatches on
the DexCare start month and the Luizalabs end month. The CV's ASCII hyphen against LinkedIn's
EN DASH is correct per CLAUDE.md rule 1 and CV-SPEC section 5.

All five CV metrics trace to `DOSSIER.md` "Bullet metrics supplied by Lucas 2026-09-01": 15%,
25%, 20%, 18%, 26%. None is invented and none is rounded. The Summary's `5+ years` is arithmetic
on the LinkedIn dates, Mar 2021 to Sep 2026, 5 yrs 6 mos, and it survives the date correction.
It is reported as derived, not as a dossier fact.

The four PDFs under `~/Documents/Resumes/` were not opened. They are invalid sources.

## Policy checks passed

Zero Ruby or Rails tokens. Zero UTC offset or time-zone overlap statement. Degree `Information
Systems`, FAESA. Location `Vitória, ES, Brazil`, nothing more. Lippaus prints `Vitória, ES,
Brazil`; DexCare and Luizalabs print `Remote`. No contract detail printed. Bullet voice first
person, past tense, subject omitted, on all 11 bullets; Summary uses `I`. English only, matching
the posting language. AI mention present in Summary and in one DexCare bullet. No term exceeds
the CV-SPEC cap of 3 appearances, so the Gate 2 stuffing penalty is 0, an improvement on the
`tractian` build which lost 10 points there. The Architect invented no unsupported token: zero
occurrences of `Next.js`, `CMS`, `content model`, `PHP`.

## Not observable

Work authorization and time-zone requirements; the posting states neither. Whether CI&T treats
its "or directly comparable modern web frameworks" clause as satisfied by React alone; that is a
recruiter's judgement and no document discloses it. Which ATS CI&T runs, and therefore which
parser handles this file.

## Recommended next step

Send fixes 1 to 7 to the Resume Architect and escalate items 8 to 11 to Lucas in parallel. The
Architect's pass is cheap and should not wait on Lucas. But do not deliver the application until
Lucas answers on CMS, PHP and Next.js, because those three decide whether this posting is worth
his time at all. If the answer to all three is no, the honest recommendation is to abandon this
application rather than ship a CV that fails four stated requirements.
