# Base apply round, hunt 2026-09-04-g

Task: hunt-2026-09-04-g-base-apply. Writer: Quill, Resume Architect.
Status: complete. Not graded. Approved by Lucas.

## What was applied

`state/hunt-2026-09-04-g-base-preview.patch` applied to
`resumes/base-en.tex` and `resumes/base-pt.tex` with `patch -p0`
(no `apply_patch` binary exists on this machine). Dry run passed first.
Both hunks applied without offset or fuzz. After the apply, each base is
byte-identical to its preview in `resumes/hunts/2026-09-04-g/base-preview/`.

Changes now in the shared bases:

1. `\resumeSubheading` prints company, title, dates, location as four
   consecutive lines in one paragraph. No `tabular*`.
2. `\samepage` and `\newline` in the header, `\nopagebreak` after it,
   `beginpenalty=10000` on `\resumeSubHeadingList`, and
   `\clubpenalty=10000`, `\widowpenalty=10000` in the preamble. A role
   header and its first bullet never split across pages.
3. PT base: `Vit\'oria, ES, Brasil` replaced by `Vit\'oria, ES, Brazil` in
   the contact block, both Lippaus roles and FAESA, per CLAUDE.md section 3.

Nothing else changed. CLAUDE.md, CV-SPEC.md, AGENTS.md, RUBRIC.md,
application files and previews untouched. CLAUDE.md and CV-SPEC.md were
read this session and predate this round.

## Build and verification

Commands: `tectonic`, `pdftotext <pdf> -`, `pdftotext -layout <pdf> -`.

| File | Pages | Bullets raw | Bullets layout | Ruby or Rails | `tabular` | `workflow` hits |
|------|-------|-------------|----------------|---------------|-----------|-----------------|
| resumes/base-en.pdf | 2 | 16 | 16 | 0 | 0 | 5 |
| resumes/base-pt.pdf | 2 | 16 | 16 | 0 | 0 | 2 |

Contact block, both: `Vitória, ES, Brazil | +55 (27) 99203-0170 |
sepulchrolucas@gmail.com | linkedin.com/in/queiroz-lucas |
github.com/queirozlc`. No UTC offset, no overlap statement.

Section headers, raw extraction. EN: Summary, Skills, Language, Experience,
Education. PT: Resumo, Habilidades, Idiomas, Experiência, Formação.

Role blocks, raw and layout, both languages, each one block with dates
directly after the title:

- DexCare, Senior Software Engineer, Mar 2026 - Present, Remote / Remoto
- Luizalabs, Mid-level Software Engineer, Jan 2024 - Mar 2026, Remote / Remoto
- Lippaus Distribuidora, Mid-level Software Engineer, Jan 2023 - Jan 2024, Vitória, ES, Brazil
- Lippaus Distribuidora, Entry-level Fullstack Software Engineer, Mar 2021 - Jan 2023, Vitória, ES, Brazil
- FAESA, Bachelor's degree, Information Systems / Bacharelado em Sistemas de Informação, Feb 2022 - Dec 2025, Vitória, ES, Brazil

Metrics present in both, unchanged: 15%, 25%, 7%, 33%, 20%, 18%, 26%.

Page break: page 2 starts with the Entry-level Lippaus header, then its two
bullets and Education. No header or bullet split.

## Not done

- No grading. The ATS Analyzer grades.
- No application tailoring. Existing tailored files keep the old header.
- No delegation, no maestri ask.
