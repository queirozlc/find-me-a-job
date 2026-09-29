# ATS Analysis — Lucas_ResumeV2.pdf vs (no job description)
Segment: not supplied   Date: 2026-09-01

Scope: Gate 0 only. No job description was supplied, so Gates 1, 2 and 3 do not
apply and were not run. Gate 0 FAILs are blocking in any case.

## Extraction commands run
```
pdftotext -layout ~/Documents/Resumes/Lucas_ResumeV2.pdf extracted-layout.txt
pdftotext          ~/Documents/Resumes/Lucas_ResumeV2.pdf extracted-raw.txt
```
Second extractor, for cross-check: pypdf 6.4.0 `extract_text()`.
File metadata: Creator `LaTeX with hyperref`, Producer `pdfTeX-1.40.25`,
1 page, 612 x 792 pt (US Letter). No embedded images. All embedded fonts carry
a ToUnicode CMap (`pdffonts` uni=yes).

This file is `Lucas_Resume.pdf` plus one extra Lippaus line. Its defects are the
same, plus one.

## Verdict
BLOCKED at Gate 0. 6 of 8 checks FAIL.

## Gate 0 — Parse integrity

| # | Check | Result | Offending text from the extraction |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 2930 bytes of raw text recovered. No nulls, no U+FFFD. |
| 0.2 | Glyph integrity | **FAIL** | The ASCII strings `office`, `profile`, `efficient`, `workflow`, `conflict` return **zero** grep hits. Present as ligature codepoints instead: `workﬂows` (x3), `ﬁscal` (x4), `backofﬁce`, `back-ofﬁce`, `notiﬁcations`, `deﬁne`. `ﬁ` is U+FB01, `ﬂ` is U+FB02. Both extractors agree. This file has the highest ligature count of the four, 11 occurrences. |
| 0.3 | Contact block recoverable | **FAIL** | Contact line is `+55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc`. Email, phone and LinkedIn present. **City is absent.** The only location string is `Vitória, ES`, which belongs to the FAESA education entry. |
| 0.4 | Section headers verbatim | **FAIL** | Raw text has `PROFESSIONAL SUMMARY`, `TECHNICAL SKILLS`, `WORK EXPERIENCE`. Rubric requires `Summary`, `Skills`, `Experience`. `PROJECTS` and `EDUCATION` are acceptable. All are standalone lines, so heading detection should still fire. Low cost. |
| 0.5 | Employment-block segmentation | **FAIL** | Two problems. (a) Each role is split in two by a blank line: `LuizaLabs` / `Mid-Level Software Engineer` / *(blank line)* / `Jan 2024 - Present` / `Brazil`, and the same shape for Lippaus. (b) Inside the Lippaus block one body line carries no bullet marker while its neighbours do: `Development and maintenance of internal back-ofﬁce and dashboard interactive control applications using Ruby on Rails, supporting operational workﬂows and administrative processes.` sits between the unbulleted intro line and the `•` list. A parser using bullet markers to delimit list items reads this line as free text, not as an achievement. The two employers do not merge with each other. |
| 0.6 | Date parseability | **FAIL** | Inconsistent separator. `Jan 2024 - Present` uses an ASCII hyphen. `May 2021 – Jan 2024` and `Feb 2022 – Dec 2025` use EN DASH U+2013. No date sits on the same line as its title. |
| 0.7 | Reading order | **FAIL** | In every role, `Mid-Level Software Engineer` precedes `Jan 2024 - Present` in the raw stream, while the layout extraction renders company and date on one visual line. Raw and layout disagree on the order of two adjacent blocks. The education block is not reordered in this file. |
| 0.8 | No forbidden constructs | **FAIL** | No photo, no icons, no images at all (`pdfimages -list` returns zero rows). But the company/date band is a two-column construct, and the 0.7 disagreement is its direct symptom. Bullets are `•` U+2022, which is allowed. |

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
   and U+FB02 with plain ASCII letters. Affected: `workﬂows` → `workflows`,
   `ﬁscal` → `fiscal`, `backofﬁce` → `backoffice`, `back-ofﬁce` → `back-office`,
   `notiﬁcations` → `notifications`, `deﬁne` → `define`.
2. **Role header split from its dates by a blank line** — Gate 0.5 — Put the
   date on the same line as the employer or the title. Target shape:
   `LuizaLabs — Mid-Level Software Engineer — Jan 2024 - Present — Brazil`,
   with no blank line inside the block.
3. **Unbulleted body line inside the Lippaus bullet list** — Gate 0.5 — Add a
   `•` to `Development and maintenance of internal back-ofﬁce and dashboard
   interactive control applications using Ruby on Rails...`, or delete it.
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
**No claim in this resume is traceable to the dossier.** Beyond that, these are
direct contradictions against the other resume files on disk:

- **Current employer.** This file: `LuizaLabs` / `Jan 2024 - Present`.
  `resume.pdf`: `LuizaLabs` / `Jan 2024 - Jan 2026` plus `DexCare` /
  `Senior Software Engineer` / `Jan 2026 - Present`. Today is 2026-09-01.
- **Degree.** This file: `Bachelor’s Degree in Information Systems`.
  `resume.pdf`: `Bachelor's Computer Science`.
- **LuizaLabs stack.** This file: `Ruby on Rails, React, and Golang` and
  `Sidekiq`. `Lucas_Node_Resume.pdf` describes the same role and period as
  `Express, Nest js, React, and Golang` and `BullMQ and RabbitMQ`.
- **Seniority.** This file: `Mid-Level Software Engineer` as the current title.
  `resume.pdf`: `Senior Software Engineer`.
- **Rails core contribution.** `Proven track record of contributing to the Ruby
  on Rails core framework and community gems`. Not traceable to the dossier, and
  not evidenced by any commit link, PR link or gem name in the document. The
  summary word `core` is stronger than the Projects line, which says only
  `framework and associated gems`.
- **`Expert in architecting microservices and scalable systems`.** Self-rating,
  no evidence in the document.
- **Lippaus job processing.** This file: `BullMQ`. `resume.pdf`:
  `ActiveJob and SideKiq`.

Lucas decides what to do with these. I did not delete or defend any of them.
