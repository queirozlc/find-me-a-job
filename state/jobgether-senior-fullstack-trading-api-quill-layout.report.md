# Quill layout round, Jobgether Senior Full-Stack Engineer - Trading API

Task: jobgether-senior-fullstack-trading-api-quill-layout. Hunt 2026-09-04-g. Language: en.
Date: 2026-09-04. Writer only. No grading, no delegation, no outward action, no base edit.

## What changed

- Replaced the tailored preamble (everything before `\begin{document}`) with the corrected `resumes/base-en.tex` preamble, byte for byte.
- The body (everything from `\begin{document}`) is unchanged. `diff` of old body versus new body is empty.
- `scripts/resume_gate.py` `layout_hash` of the tailored file equals the base hash. Verified in this session.

Layout effects of the base preamble:
- `\resumeSubheading` is single column. Company, title, dates, location print on consecutive lines. No `tabular*` remains (0 hits). This is the Sieve root cause, File Readability 0.8 with 0.6 and 0.7 consequences.
- `\samepage` and `\nopagebreak` keep each header with its first bullet. `beginpenalty=10000` on lists. `\clubpenalty` and `\widowpenalty` set.

## Artifacts

- Tex: resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.tex
- PDF: resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf
- Note: resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/application-note.md (unchanged, already complete)
- Report: state/jobgether-senior-fullstack-trading-api-quill-layout.report.md

## Build and extraction checks

| Check | Result |
|---|---|
| tectonic build | OK. One font warning (Roboto-Italic request), same as base builds. |
| Pages | 2. The corrected base also builds to 2 pages. Break falls between the two Lippaus roles; page 2 opens with the Entry-level header and its bullets together. CLAUDE.md 9.1 allows two pages when complete content does not fit. |
| Experience bullets | 16 in tex, 16 in raw extraction. |
| Metrics | 15%, 25%, 7%, 33%, 20%, 18%, 26% all present in raw extraction. |
| Titles, dates, locations | Unchanged from prior round. DexCare Senior Software Engineer Mar 2026 - Present Remote; Luizalabs Mid-level Software Engineer Jan 2024 - Mar 2026 Remote; Lippaus Distribuidora Mid-level Software Engineer Jan 2023 - Jan 2024 Vitória, ES, Brazil; Lippaus Distribuidora Entry-level Fullstack Software Engineer Mar 2021 - Jan 2023 Vitória, ES, Brazil; FAESA Bachelor's degree, Information Systems Feb 2022 - Dec 2025. Match DOSSIER.md LinkedIn ground truth. |
| Raw versus layout order | Identical. Every role reads Company / Title / Dates / Location then bullets in both streams. Dates sit on the line directly after the title. |
| Section headers | Summary, Skills, Language, Experience, Education present as standalone lines. |
| Contact block | Body line 3. No UTC offset, no overlap sentence. |
| Ligatures | `workflow` probe 5 hits in raw extraction. |
| Ruby or Rails tokens | 0. |
| Forbidden constructs | 0 `tabular`, no text box, no images. |

## Token placements, unchanged from the fix-1 round

Required (manifest): Golang in Skills and Luizalabs bullet 1. TypeScript in Skills and DexCare bullet 1. React in Skills and DexCare bullet 5. HTML in Skills and Lippaus entry-level bullet 1. TailwindCSS in Skills and DexCare bullet 5. SQL in Skills and DexCare bullet 4. REST APIs in Skills and DexCare bullet 3.
Preferred (manifest): PostgreSQL in Skills and DexCare bullet 4. Google Cloud Platform in Skills only, bullet prints GCP. Docker and Kubernetes in Skills and Luizalabs bullet 4.

## Not done, by instruction

- Sieve non-blocking defects 2 to 5 (bullet reorder, Google Cloud Platform in the Luizalabs bullet, `workflows` repetition, role gap) were not applied. The dispatch said no semantic rewrites unless needed for a confirmed defect, and `\resumeRoleGap` lives in the preamble that must match the base. Maestro decides whether to dispatch those as a fix list.
- Application note untouched. Recruiter message and screening answers were complete. Unknowns (notice period, salary, fintech, algorithmic trading, mentoring, C#) remain marked as not recorded. No availability invented.

## Next

Send the rebuilt PDF to Sieve.
