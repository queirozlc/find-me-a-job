# ATS Analysis — Lucas_Node_Resume.pdf vs (no job description)
Segment: not supplied   Date: 2026-09-01

Scope: Gate 0 only. No job description was supplied, so Gates 1, 2 and 3 do not
apply and were not run. Gate 0 FAILs are blocking in any case.

## Extraction commands run
```
pdftotext -layout ~/Documents/Resumes/Lucas_Node_Resume.pdf extracted-layout.txt
pdftotext          ~/Documents/Resumes/Lucas_Node_Resume.pdf extracted-raw.txt
```
Second extractor, for cross-check: pypdf 6.4.0 `extract_text()`.
File metadata: Creator `LaTeX with hyperref`, Producer `pdfTeX-1.40.27`,
1 page, 612 x 792 pt (US Letter). No embedded images. All embedded fonts carry
a ToUnicode CMap (`pdffonts` uni=yes).

## Verdict
BLOCKED at Gate 0. 6 of 8 checks FAIL.

## Gate 0 — Parse integrity

| # | Check | Result | Offending text from the extraction |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 2520 bytes of raw text recovered. No nulls, no U+FFFD. |
| 0.2 | Glyph integrity | **FAIL** | The ASCII strings `office`, `profile`, `efficient`, `workflow`, `conflict` return **zero** grep hits. The words are present as precomposed ligature codepoints: `high-trafﬁc`, `workﬂows` (x2), `ﬁscal` (x3), `backofﬁce`, `notiﬁcations`, `deﬁne`. `ﬁ` is U+FB01, `ﬂ` is U+FB02. Both extractors agree. |
| 0.3 | Contact block recoverable | **FAIL** | Contact line is `+55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. Email, phone and LinkedIn are present. **City is absent.** The only location string in the file is `Vitória, ES`, and it belongs to the FAESA education entry, not to the candidate. |
| 0.4 | Section headers verbatim | **FAIL** | Raw text has `PROFESSIONAL SUMMARY`, `TECHNICAL SKILLS`, `WORK EXPERIENCE`. The rubric requires `Summary`, `Skills`, `Experience`. `EDUCATION` is acceptable. All four are standalone lines, so heading detection should still fire. Low cost, listed for completeness. |
| 0.5 | Employment-block segmentation | **FAIL** | Each role is split in two by a blank line in the raw stream. LuizaLabs: `LuizaLabs` / `Mid-Level Software Engineer` / *(blank line)* / `Jan 2024 - Present` / `Brazil`. Lippaus: `Lippaus` / `Entry-Level Fullstack Software Engineer` / *(blank line)* / `May 2021 – Jan 2024` / `Brazil`. A parser that treats a blank line as a block boundary reads employer+title as one block and dates+location as another. The two employers do not merge with each other. |
| 0.6 | Date parseability | **FAIL** | Separator is inconsistent. `Jan 2024 - Present` uses an ASCII hyphen. `May 2021 – Jan 2024` and `Feb 2022 – Dec 2025` use EN DASH U+2013. The knowledge base format is `Mon YYYY - Mon YYYY`. Additionally no date sits on the same line as its title, and the FAESA date is not adjacent to the degree at all (see 0.7). |
| 0.7 | Reading order | **FAIL** | Two disagreements. (a) The education location and date land at the very **end** of the raw stream, after the LANGUAGES section: raw lines 51-56 read `LANGUAGES` / `Portuguese — Native` / `English — Fluent` / *(blank)* / `Vitória, ES` / `Feb 2022 – Dec 2025`. In the layout extraction they sit beside `FAESA`. The degree therefore has no date attached in the parser stream. (b) In every role, `Mid-Level Software Engineer` precedes `Jan 2024 - Present` in raw, while the layout renders company and date on one visual line. |
| 0.8 | No forbidden constructs | **FAIL** | No photo, no icons, no images at all (`pdfimages -list` returns zero rows). But the company/date band is a two-column construct, and the raw-versus-layout order disagreement in 0.7 is its direct symptom. Bullets are `•` U+2022, which is allowed. |

## Gate 1 — Knockouts
Not run. No job description supplied.

## Gate 2 — Retrieval coverage
Not run. No job description supplied. One Gate 0 finding carries into Gate 2
regardless of the posting: no boolean recruiter query containing the literal
string `workflow` or `office` can match this document.

## Gate 3 — Human scan
Not run. Gate 0 is blocking.

## Defects, ranked by cost
1. **Ligature codepoints break exact-token search** — Gate 0.2 — Replace U+FB01
   and U+FB02 with plain ASCII letters. Affected: `high-trafﬁc` → `high-traffic`,
   `workﬂows` → `workflows`, `ﬁscal` → `fiscal`, `backofﬁce` → `backoffice`,
   `notiﬁcations` → `notifications`, `deﬁne` → `define`.
2. **Education date and location detached to the end of the stream** —
   Gate 0.7 — `Vitória, ES` and `Feb 2022 – Dec 2025` must appear immediately
   after `Bachelor’s Degree in Information Systems`, not after `English — Fluent`.
3. **Role header split from its dates by a blank line** — Gate 0.5 — Put the
   date on the same line as the employer or the title. Target shape:
   `LuizaLabs — Mid-Level Software Engineer — Jan 2024 - Present — Brazil`,
   with no blank line inside the block.
4. **Two-column company/date band** — Gate 0.8 / 0.7 — Remove the right-aligned
   column. Single column, full width.
5. **No candidate city in the contact block** — Gate 0.3 — Add the city, country
   and the UTC offset to the contact line.
6. **Inconsistent date separator** — Gate 0.6 — Replace EN DASH U+2013 in
   `May 2021 – Jan 2024` and `Feb 2022 – Dec 2025` with an ASCII hyphen.
7. **Non-verbatim section headers** — Gate 0.4 — `PROFESSIONAL SUMMARY` → `Summary`,
   `TECHNICAL SKILLS` → `Skills`, `WORK EXPERIENCE` → `Experience`. Low cost.

## Claims I could not verify
`~/career/DOSSIER.md` is an unfilled template. Every `[FACT]` field is empty.
**No claim in this resume is traceable to the dossier.** Beyond that blanket
statement, these are direct contradictions against the other resume files on
disk, so at most one version can be accurate:

- **Current employer.** This file states `LuizaLabs` / `Jan 2024 - Present`.
  `resume.pdf` states `LuizaLabs` / `Jan 2024 - Jan 2026` and `DexCare` /
  `Senior Software Engineer` / `Jan 2026 - Present`. Today is 2026-09-01.
- **Degree.** This file: `Bachelor’s Degree in Information Systems`.
  `resume.pdf`: `Bachelor's Computer Science`.
- **LuizaLabs stack.** This file: `Express, Nest js, React, and Golang` and
  `BullMQ and RabbitMQ`. `Lucas_Resume.pdf` and `Lucas_ResumeV2.pdf` describe the
  same role and period as `Ruby on Rails, React, and Golang` and `Sidekiq`.
- **Seniority.** This file: `Mid-Level Software Engineer` as the current title.
  `resume.pdf`: `Senior Software Engineer`.
- **Lippaus job processing.** This file: `BullMQ`. `resume.pdf`:
  `ActiveJob and SideKiq`.

Lucas decides what to do with these. I did not delete or defend any of them.
