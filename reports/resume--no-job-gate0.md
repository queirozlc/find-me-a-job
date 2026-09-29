# ATS Analysis — resume.pdf vs (no job description)
Segment: not supplied   Date: 2026-09-01

Scope: Gate 0 only. No job description was supplied, so Gates 1, 2 and 3 do not
apply and were not run. Gate 0 FAILs are blocking in any case.

## Extraction commands run
```
pdftotext -layout ~/Documents/Resumes/resume.pdf extracted-layout.txt
pdftotext          ~/Documents/Resumes/resume.pdf extracted-raw.txt
```
Second extractor, for cross-check: pypdf 6.4.0 `extract_text()`.
File metadata: Creator `TeX`, Producer `pdfTeX-1.40.16`, **2 pages**,
595.276 x 841.89 pt (A4). No embedded images.

**`pdffonts` reports `uni=no` for all seven embedded fonts.** No font in this
file carries a ToUnicode CMap. That is the documented root cause of pypdf issue
#1351, Apache PDFBox JIRA and Mozilla Bugzilla #1810914, recorded in
`~/career/ATS-KNOWLEDGE.md` section 3.

## Verdict
BLOCKED at Gate 0. 5 of 8 checks FAIL.

## The finding that matters most in this file

**This file's extraction is parser-dependent.** The two extractors disagree, and
the disagreement runs in both directions:

- `pdftotext` (poppler) returns clean ASCII: `backoffice`, `fiscal`, `workflows`,
  `notifications`, `define`. Grep finds `office` twice and `workflow` three times.
- **pypdf returns ligature codepoints for the same words**: `backoﬃce` and
  `back-oﬃce` (U+FB03, the `ffi` ligature), `Conﬁguration`, `conﬁgurations`,
  `ﬂag`, `workﬂow`, `workﬂows`, `ﬁscal`, `notiﬁcations`, `deﬁne`. Grep for the
  ASCII strings `office`, `profile`, `efficient`, `workflow`, `conflict` in the
  pypdf output returns **zero hits**.

Poppler recovers the text with its own font heuristics. A parser that trusts the
ToUnicode CMap has nothing to trust, because there is none. The knowledge base
verification method, select-all-copy, uses a poppler-class path and therefore
reports this file as clean. **It is not clean.** This is worse than a consistent
failure, because it hides under the recommended check.

I did not test any commercial ATS parser. Which behaviour a given vendor shows is
**not observable** from here. What is observed: the CMap is absent, and two real
extractors disagree.

## Gate 0 — Parse integrity

| # | Check | Result | Offending text from the extraction |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 3843 bytes of raw text recovered. No nulls, no U+FFFD, in either extractor. |
| 0.2 | Glyph integrity | **FAIL** | Not under `pdftotext`, which returns clean ASCII. **Under pypdf**: `backoﬃce`, `back-oﬃce`, `Conﬁguration`, `conﬁgurations`, `ﬂag`, `workﬂow`, `workﬂows`, `ﬁscal` (x3), `notiﬁcations`, `deﬁne`. Root cause observed in the file itself: `pdffonts` reports `uni=no` on all seven embedded fonts (`QPJUZA+SFCC2488`, `HXLOOB+SFRM1000`, `CKUQXN+CMSY10`, `ITHGCQ+SFCC1000`, `TVWWRR+SFBX1000`, `HLWMZW+SFTI1000`). |
| 0.3 | Contact block recoverable | PASS | Line 3 of the raw stream: `Espirito Santo, Brazil · sepulchrolucas@gmail.com · +55 27 992030170 ·` followed by `https://www.linkedin.com/in/queiroz-lucas`. Email, phone, city and LinkedIn URL all present, in the body, not repeated on page 2, so not a page-header object. Two notes, neither a Gate 0 FAIL: `Espirito` is missing its accent while the body writes `Espírito`, and no UTC offset is stated. The missing offset is a Gate 1 risk in LatAm-remote postings. **This is the only file of the four that recovers a city.** |
| 0.4 | Section headers verbatim | **FAIL** | `Education` and `Skills` are verbatim and correct. `Work Experiences` is not verbatim, the rubric requires `Experience`. **There is no Summary section at all.** `Language` should be `Languages`. |
| 0.5 | Employment-block segmentation | **FAIL** | Two problems, and this is the highest-value check in the rubric. (a) **No blank line separates the end of one role from the next employer.** Raw lines 35-36 read `implementation` then immediately `LuizaLabs`. Raw lines 50-51 read `resilient production environments` then immediately `Lippaus`. The layout extraction does have a blank line at both boundaries; the raw stream does not. The employer name is glued to the previous role's last bullet. (b) Each role header is still split from its dates by a blank line: `DexCare` / `Senior Software Engineer` / *(blank line)* / `Remote` / `Jan 2026 - Present`. Three roles, three occurrences. |
| 0.6 | Date parseability | PASS | All four ranges use the required `Mon YYYY - Mon YYYY` shape with a consistent ASCII hyphen: `Feb 2022 - Dec 2025`, `Jan 2026 - Present`, `Jan 2024 - Jan 2026`, `May 2021 - Jan 2024`. No date sits on the same line as its title, but each is adjacent to it within the block, which the rubric permits. **This is the only file of the four that passes 0.6.** |
| 0.7 | Reading order | **FAIL** | Severe, and the worst of the four. (a) **The Skills section is a two-column table and the raw stream drains the label column first, then the value column.** Raw lines 70-80: `Back-end:` / `Front-end:` / `DevOps & Infrastructure:` / `Feature Management & Observability:` / `AI-Assisted Development:` / *(blank)* / `Ruby on Rails, PostgreSQL, Redis, ActiveRecord, REST APIs, RSpec` / `Hotwire, React.js, JavaScript, HTML5, CSS3, Tailwind CSS` / `AWS, Kubernetes, ArgoCD, Docker, GitHub Actions, CI/CD` / `LaunchDarkly, Datadog, Feature Flags, Dark Launches, A/B Testing` / `Claude Code, Cursor, Copilot, Automated Test Authoring`. Every category label is detached from its skills. The layout extraction pairs them correctly, so raw and layout disagree. pypdf pairs them correctly too, which makes this defect parser-dependent as well. (b) `Senior Software Engineer` precedes `Remote` and `Jan 2026 - Present` in raw, while the layout renders company and location on one visual line. |
| 0.8 | No forbidden constructs | **FAIL** | No photo, no icons, no images at all (`pdfimages -list` returns zero rows). But there are **two** table constructs: the company/location/date band, and the Skills two-column table that produced the 0.7 failure. Bullets are `•` U+2022, which is allowed. Additionally the page break falls immediately before `Skills`, so the entire Skills section sits alone on page 2. |

## Gate 1 — Knockouts
Not run. No job description supplied.

## Gate 2 — Retrieval coverage
Not run. No job description supplied. Two Gate 0 findings carry into Gate 2
regardless of the posting: under a pypdf-class parser no query containing the
literal string `workflow` or `office` matches, and under a poppler-class parser
every Skills category label is detached from its skill list.

## Gate 3 — Human scan
Not run. Gate 0 is blocking.

## Defects, ranked by cost
1. **Skills table splits labels from values in the raw stream** — Gate 0.7 / 0.8 —
   Replace the two-column table with single-column lines, for example
   `Back-end: Ruby on Rails, PostgreSQL, Redis, ActiveRecord, REST APIs, RSpec`
   as one run of text.
2. **No ToUnicode CMap on any embedded font** — Gate 0.2 — Re-export from a
   toolchain that emits one. The three LaTeX Roboto files on disk do emit one
   (`uni=yes`), so this is a font and driver choice, not a LaTeX limitation.
   Then confirm with a second extractor, not only select-all-copy.
3. **Employer name glued to the previous role's last bullet** — Gate 0.5 — Force
   a blank line before `LuizaLabs` and before `Lippaus` in the extracted stream.
   Currently: `implementation` / `LuizaLabs`.
4. **Role header split from its dates by a blank line** — Gate 0.5 — Put the date
   on the same line as the employer or the title.
5. **No Summary section** — Gate 0.4 — Add a `Summary` header and block. A
   recruiter scan and the retrieval placement score both depend on it.
6. **Non-verbatim headers** — Gate 0.4 — `Work Experiences` → `Experience`,
   `Language` → `Languages`.
7. **Two pages for a Skills section alone** — Gate 0.8 — The page break lands
   right before `Skills`. Under 10 years of experience the knowledge base
   defaults to one page.
8. **Company/location/date two-column band** — Gate 0.8 / 0.7 — Remove the
   right-aligned column.
9. **Accent inconsistency in the contact line** — Gate 0.3, cosmetic —
   `Espirito Santo, Brazil` in the contact line, `Espírito Santo, Brazil` in the
   body. Pick one.

## Claims I could not verify
`~/career/DOSSIER.md` is an unfilled template. Every `[FACT]` field is empty.
**No claim in this resume is traceable to the dossier.** Beyond that:

- **`The result was an elimination of 34% redundant support tickets.`** A precise
  number with no stated measurement window, baseline, or source. This is the only
  quantified outcome in any of the four files. It needs a defensible basis in the
  dossier before it goes in front of an interviewer.
- **`DexCare` / `Senior Software Engineer` / `Jan 2026 - Present`.** Present only
  in this file. `Lucas_Node_Resume.pdf`, `Lucas_Resume.pdf` and
  `Lucas_ResumeV2.pdf` all state `LuizaLabs` / `Jan 2024 - Present` as the current
  role. Today is 2026-09-01. The files cannot both be right.
- **Degree.** This file: `Bachelor's Computer Science`. The other three:
  `Bachelor’s Degree in Information Systems`.
- **Lippaus job processing.** This file: `ActiveJob and SideKiq`. The other three:
  `BullMQ`. Same employer, same period.
- **`Contributed to the Scheduling Team's infrastructure dev environment
  migration`** and **`This migration is critical to retiring legacy v1
  infrastructure`.** Scope and criticality asserted, not evidenced.

Lucas decides what to do with these. I did not delete or defend any of them.
