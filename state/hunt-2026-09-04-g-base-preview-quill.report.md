# Base-layout preview round, hunt 2026-09-04-g

Task: hunt-2026-09-04-g-base-preview-quill, fix1 applied
(hunt-2026-09-04-g-base-preview-quill-fix1). Writer: Quill, Resume Architect.
Status: complete. Not graded. Shared bases untouched. Approval pending.

## Fix1, 2026-09-04

Maestro correction: RUBRIC check 0.6 requires dates on the title line or
adjacent to it. The header order changed from company, title, location,
dates to company, title, dates, location. Only the preview `.tex` files, the
patch and this report changed. Both PDFs rebuilt.

Adjacency verified in raw and layout extraction, both languages: in every
role (DexCare, Luizalabs, Lippaus twice, FAESA) the dates line is the line
directly after the title line. Bullets: 16 raw, 16 layout, both languages.
Pages: 2 each. Ruby or Rails tokens: 0. Page break unchanged: page 2 starts
with the Entry-level Lippaus header, no header or bullet split.

## Files

- resumes/hunts/2026-09-04-g/base-preview/base-en.tex
- resumes/hunts/2026-09-04-g/base-preview/base-en.pdf
- resumes/hunts/2026-09-04-g/base-preview/base-pt.tex
- resumes/hunts/2026-09-04-g/base-preview/base-pt.pdf
- state/hunt-2026-09-04-g-base-preview.patch (unified diff, previews against resumes/base-en.tex and resumes/base-pt.tex)

## Changes in the previews only

1. `\resumeSubheading` no longer uses `tabular*`. It prints company, title,
   dates and location as four consecutive lines in one paragraph. Company is
   bold, title and location italic, dates plain. Same order in every role and
   in Education.
2. The header paragraph is wrapped in `\samepage` and uses `\newline`, not
   `\\`. Reason: `\raggedright` redefines `\\` as a paragraph end, so a page
   break could land between header lines. `\newline` keeps the four lines in
   one paragraph and `\samepage` forbids a break inside it.
3. `\nopagebreak` after the header and `beginpenalty=10000` on
   `\resumeSubHeadingList`. Reason: without them the break landed between the
   header and its first bullet.
4. `\clubpenalty=10000` and `\widowpenalty=10000` in the preamble. Reason:
   without them the break split the first bullet of the last Lippaus role
   across pages.
5. PT preview: four occurrences of `Vit\'oria, ES, Brasil` replaced by
   `Vit\'oria, ES, Brazil` (contact block, two Lippaus roles, FAESA), per
   AGENTS.md section 3.

Unchanged: all content, 16 Experience bullets, metrics, titles, dates,
margins, font sizes, section headers, Skills, Language and Idiomas sections.
The `\vspace{3pt}` after the header and `\resumeRoleGap` are unchanged.

## Build and verification

| File | Pages | Bullets raw | Bullets layout | Ruby or Rails tokens | `workflow` hits |
|------|-------|-------------|----------------|----------------------|-----------------|
| base-en.pdf | 2 | 16 | 16 | 0 | 5 |
| base-pt.pdf | 2 | 16 | 16 | 0 | 2 |

Commands: `tectonic`, `pdftotext <pdf> -`, `pdftotext -layout <pdf> -`.

Raw and layout extraction order, both languages: contact block, Summary or
Resumo, Skills or Habilidades, Language or Idiomas, Experience or
Experiência, Education or Formação. Every role reads as one block:
company, title, location, dates, then its bullets. Order verified in both
extractions for DexCare, Luizalabs, Lippaus (two roles) and FAESA.
Order inside each block after fix1: company, title, dates, location.

Page break: page 1 ends after the third Lippaus bullet of the Mid-level role.
Page 2 starts with the Entry-level Lippaus header and holds its two bullets
and Education. No header and no bullet is split across pages, in either
language.

The `\resumeSubheading` comment that referenced the accepted parser cost in
RUBRIC.md was replaced by a comment describing the single-column header.
RUBRIC.md itself was not edited.

## Not done

- No grading. The ATS Analyzer grades.
- No edit to resumes/base-en.tex, resumes/base-pt.tex, existing application
  files, CV-SPEC.md, AGENTS.md, RUBRIC.md.
- No delegation, no maestri ask.

## Open point for the Maestro

The one-page target of the old template is lost with the four-line header.
Both previews are two pages. CV-SPEC.md item 2 permits two pages when the
complete content does not fit. Lucas decides whether the parser gain is
worth the second page before the patch is applied to the shared bases.
