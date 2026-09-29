# Quill report: Mavila Consulting, Senior Software Engineer – JavaScript

Date: 2026-09-04
Language: English only
Base: resumes/base-en.tex, copied. Base not edited.
Status: package written, PDF built, one page. Not graded.

## Files written

- resumes/hunts/2026-09-04-c/mavila-senior-software-engineer-javascript/Lucas-Queiroz-Resume-en.tex
- resumes/hunts/2026-09-04-c/mavila-senior-software-engineer-javascript/Lucas-Queiroz-Resume-en.pdf
- resumes/hunts/2026-09-04-c/mavila-senior-software-engineer-javascript/application-message.md (draft, not sent)
- state/mavila-senior-software-engineer-javascript-quill.report.md (this file)

No other file was changed. No dependency was added.

## Build

Command, run in the package directory:

```
tectonic Lucas-Queiroz-Resume-en.tex
pdftotext Lucas-Queiroz-Resume-en.pdf -
pdftotext -layout Lucas-Queiroz-Resume-en.pdf -
pdftoppm -r 80 -png Lucas-Queiroz-Resume-en.pdf page
```

Result: build succeeded. Output 26.9 KiB. The only warnings are fontspec font-loading notices for Roboto italic and Computer Modern math faces. They are the same notices the base emits. No missing glyph.

Rendered page count: 1. Confirmed with `pdfinfo`.

Rendered inspection of the PNG: no clipping, no overlap, no missing glyph. Contact block, five section headers, four employment blocks, and Education are all present. Every base Experience role, bullet, and metric is present.

Extraction checks on the raw text:
- Contact block extracted on one line with city, phone, email, LinkedIn, GitHub.
- Headers extract as SUMMARY, SKILLS, LANGUAGE, EXPERIENCE, EDUCATION. The base renders headers in small caps, and pdftotext returns them in upper case. Same behavior as the base.
- Each role extracts as one block: company and dates on one line, title and location on the next, then bullets.
- `grep -c workflow` returns 5 and `office` returns 2, so ligatures are disabled.
- `grep -in 'ruby\|rails'` on the .tex and on the extracted text returns nothing.
- Titles and dates: every `{Company}{Dates}` and `{Title}{Location}` pair is identical to base-en.tex, checked with diff.

## Format change from the base

The base defines the role header with `tabular*`. The role instructions and CV-SPEC item 2 forbid `tabular*`. The tailored copy prints the header as two consecutive text lines: `Company | Dates` then `Title | Location`. Titles, dates, and locations are unchanged.

To keep one page after the added Summary sentence and Skills tokens, the top margin moved from -0.5in to -0.6in, text height from +1.0in to +1.2in, and the header gap from 3pt to 2pt. No bullet was removed or shortened.

## Mandatory term placement

| Term | Skills | Experience bullet | Total on page |
| --- | --- | --- | --- |
| JavaScript | Languages | Lippaus 2021, back-office dashboards in JavaScript | 3 (Summary, Skills, bullet) |
| Git | Cloud and operations | DexCare, services versioned in Git | 3 (Summary, Skills, bullet), plus the GitHub URL in the contact block |
| Docker | Cloud and operations | Luizalabs, deployed with Docker and Kubernetes | 3 (Summary, Skills, bullet) |
| CI/CD | Cloud and operations | Luizalabs, unit testing gating the CI/CD pipeline setup | 2 |
| Unit testing | Testing and practices | Luizalabs, Vitest and Jest unit testing | 2 |
| Complex codebases | Testing and practices | DexCare SPI bullet, across complex codebases spanning multiple services | 3 (Summary, Skills, bullet) |
| Node.js | Languages | Luizalabs, tax microservices in Node.js | 3 (Summary, Skills, bullet) |

Adjacent posting terms placed with source support:
- `Pipeline setup` (posting: basic software pipeline setup): Skills, and the Luizalabs CI/CD bullet. Supported by the dossier's ArgoCD and CI/CD facts.
- `Environment setup`: Skills. Supported by the DexCare agent environments and SPI environment facts.
- `run, modify, and test complex codebases locally with Git and Docker` in the Summary mirrors the posting's "running, modifying, and testing real-world projects locally". Supported by Git repository evidence and Docker use at Luizalabs.
- `developer tooling layer` and `agent environments` in the DexCare AI bullet address the nice-to-have "building or testing developer tools or automation agents". Supported by the dossier's DexCare AI entry.

Git evidence: the job context records direct local commit evidence. The commit count was not used as a metric.

Cap check: no technology term exceeds 3 appearances. TypeScript 3, React 3, Node.js 3, JavaScript 3, Git 3, Docker 3.

## Unsupported terms omitted

- Open-source contribution or evaluation: not in the dossier. The dossier excludes the old Rails gem contribution claim. Not claimed.
- LLM research or evaluation projects: not in the dossier. Not claimed. The CV mentions agentic workflows and agent environments only, per the dossier.
- 5000+ star repositories: not in the dossier. Not claimed.
- Issue triaging, test coverage evaluation, Dockerization as a task: not in the dossier as things Lucas did. Not claimed as bullets. Docker appears only as a deployment fact.
- Leading a team of junior engineers: not in the dossier. Not claimed.
- 4 hrs/day overlap with PST: not printed on the CV per CLAUDE.md. Answered in the screening answers of the message draft.

## Application message

Draft in English addressed to Juliana Verissimo, with screening answers. Four screening items are marked for Lucas to answer himself because the dossier does not record them: 5000+ star repository experience, open-source contribution, LLM evaluation projects, and leading junior engineers.

## Open for the Maestro

- Confirm the single-column header change is the accepted form for the hunt. The base still carries `tabular*`.
- The Summary now carries a fourth sentence. If the Analyzer flags Summary length, the sentence "I run, modify, and test complex codebases locally with Git and Docker" can move into the DexCare SPI bullet.
