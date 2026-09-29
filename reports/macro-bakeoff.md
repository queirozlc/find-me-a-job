# Employment-block macro bake-off

Task: settle CV-SPEC.md "Mandatory fixes" item 2 by test, not by assertion.
Judged against RUBRIC.md Gate 0.5, 0.6, 0.7 and Gate 0.2.
Date: 2026-09-01. Analyst: ATS Analyzer. No CV was edited.

## Method

Test documents: `~/career/reports/bakeoff/shape-{a,b,c}.tex`.
Preamble: copied from `~/career/resumes/template-rails-original.tex`, with two
changes forced by the toolchain. See "Preamble deviations" below.
Body: identical in all three. Two fake roles, two bullets each. Every bullet
carries `efficient` and `workflow` for the Gate 0.2 check.

Build: `tectonic shape-<x>.tex` (Tectonic 0.17.0)
Extract: `pdftotext shape-<x>.pdf -` and `pdftotext -layout shape-<x>.pdf -`
(poppler 26.08.0)

Pass criteria, per RUBRIC Gate 0:

- 0.5 one unbroken block per role, no blank line inside a role
- 0.6 `Mon YYYY - Mon YYYY` on the same line as, or adjacent to, the title
- 0.7 raw and layout extraction agree on the order of adjacent blocks
- 0.2 `efficient` and `workflow` recoverable, no U+FB01 / U+FB02

## Preamble deviations, and why

Both are defects in the current template. They are not preferences. They block
any tectonic build, so the bake-off could not run without them.

**1. `\input{glyphtounicode}` and `\pdfgentounicode=1` are pdfTeX primitives.**
Under tectonic (XeTeX) the build dies:

```
! Undefined control sequence.
l.7 \pdfglyphtounicode
                      {A}{0041}
```

Guarded in the test preamble with `\ifdefined\pdfgentounicode ... \fi`.

**2. CV-SPEC item 1's `\DisableLigatures` does not work under tectonic.**
microtype refuses it:

```
! Package microtype Error: Disabling ligatures of a font is only possible
(microtype)                with pdftex version 1.30 or newer.
(microtype)                Ignoring \DisableLigatures.
```

The line was removed from the test preamble. `\usepackage{microtype}` stays.

**It is also not needed.** Control probe, template font, no fix at all:

```latex
\documentclass[letterpaper,10pt]{article}
\usepackage[sfdefault]{roboto}
\begin{document}
efficient workflow office profile conflict flag
\end{document}
```

`pdftotext probe.pdf - | xxd`:

```
00000000: 6566 6669 6369 656e 7420 776f 726b 666c  efficient workfl
00000010: 6f77 206f 6666 6963 6520 7072 6f66 696c  ow office profil
00000020: 6520 636f 6e66 6c69 6374 2066 6c61 670a  e conflict flag.
```

Plain ASCII `66 66 69` for `ffi`, `66 6c` for `fl`. Zero U+FB01 / U+FB02.
Under tectonic the `roboto` package loads through `fontspec`, and XeTeX writes
the ToUnicode map from the OpenType font. The ligature loss the spec observed
in the four Overleaf PDFs does not reproduce here.

This is a finding about CV-SPEC item 1, not about the macro shapes. It is
recorded under "Questions for Lucas" below. I did not change the spec.

## Shape A: one source line per role header

Macro under test:

```latex
\newcommand{\resumeSubheading}[4]{
\vspace{-1pt}\item
  \textbf{#1} \textbar{} #3 \textbar{} #2 \textbar{} #4
  \vspace{-7pt}
}
```

`\textbar{}` extracts as ASCII `|`. CV-SPEC item 2 draws this shape with an em
dash. An em dash puts U+2014 in the text layer, so it was rejected. An ASCII
hyphen was also rejected: it collides with the date separator that Gate 0.6
looks for.

### Raw extraction, verbatim (`pdftotext shape-a.pdf -`)

```
EXPERIENCE
Company X | Senior Software Engineer | Jan 2020 - Feb 2021 | Vitoria, ES
Built an efficient billing pipeline that cut invoice workflow latency.
Owned the deployment workflow and made the release process efficient.

Company Y | Senior Software Engineer | Mar 2021 - Present | Vitoria, ES
Designed an efficient multi-tenant API and its onboarding workflow.
Automated the review workflow, making incident response efficient.
```

### Layout extraction, verbatim (`pdftotext -layout shape-a.pdf -`)

```
EXPERIENCE
 Company X | Senior Software Engineer | Jan 2020 - Feb 2021 | Vitoria, ES
   Built an efficient billing pipeline that cut invoice workflow latency.
   Owned the deployment workflow and made the release process efficient.

 Company Y | Senior Software Engineer | Mar 2021 - Present | Vitoria, ES
   Designed an efficient multi-tenant API and its onboarding workflow.
   Automated the review workflow, making incident response efficient.
```

### Verdict: PASS

| Check | Result | Evidence |
|---|---|---|
| 0.5 segmentation | PASS | One block per role. The only blank line is the one that separates the two roles. |
| 0.6 date parseability | PASS | `Jan 2020 - Feb 2021` sits on the same line as `Senior Software Engineer`. |
| 0.7 reading order | PASS | Raw and layout agree line for line after whitespace normalisation. |
| 0.2 ligatures | PASS | `efficient` 4 hits, `workflow` 4 hits, U+FB01/FB02 count 0. |

### Stress test, long header

`shape-a-stress.tex` replaces the second role header with a long one. Raw
extraction:

```
Company X | Senior Software Engineer | Jan 2020 - Feb 2021 | Vitoria, ES
Built an efficient billing pipeline that cut invoice workflow latency.
Owned the deployment workflow and made the release process efficient.

Magazine Luiza LuizaLabs via Fullstack Labs | Senior Backend Software Engineer, Platform | Mar 2021 - Present | Vitoria,
ES, Brazil
Designed an efficient multi-tenant API and its onboarding workflow.
Automated the review workflow, making incident response efficient.
```

The header wraps to a second line. No blank line appears inside the role, and
the date stays on the same line as the title. Gate 0.5 and 0.6 still PASS.
Order the fields Company, Title, Dates, Location. A wrap can then only split
the Location, which is the lowest-value field of the four.

## Shape B: two adjacent lines, `\hfill` inside `\makebox`, no `tabular*`

Macro under test:

```latex
\newcommand{\resumeSubheading}[4]{
\vspace{-1pt}\item
  \makebox[0.97\textwidth][l]{\textbf{#1}\hfill #2}\\
  \makebox[0.97\textwidth][l]{\textit{#3}\hfill \textit{#4}}
  \vspace{-7pt}
}
```

### Raw extraction, verbatim (`pdftotext shape-b.pdf -`)

```
EXPERIENCE
Company X
Senior Software Engineer

Jan 2020 - Feb 2021
Vitoria, ES

Built an efficient billing pipeline that cut invoice workflow latency.
Owned the deployment workflow and made the release process efficient.

Company Y
Senior Software Engineer
Designed an efficient multi-tenant API and its onboarding workflow.
Automated the review workflow, making incident response efficient.

Mar 2021 - Present
Vitoria, ES
```

### Layout extraction, verbatim (`pdftotext -layout shape-b.pdf -`)

```
EXPERIENCE
 Company X                                                                  Jan 2020 - Feb 2021
 Senior Software Engineer                                                            Vitoria, ES
   Built an efficient billing pipeline that cut invoice workflow latency.
   Owned the deployment workflow and made the release process efficient.

 Company Y                                                                   Mar 2021 - Present
 Senior Software Engineer                                                           Vitoria, ES
   Designed an efficient multi-tenant API and its onboarding workflow.
   Automated the review workflow, making incident response efficient.
```

### Verdict: FAIL

| Check | Result | Evidence |
|---|---|---|
| 0.5 segmentation | **FAIL** | Company X becomes three blocks. `Company X / Senior Software Engineer`, blank, `Jan 2020 - Feb 2021 / Vitoria, ES`, blank, the bullets. |
| 0.6 date parseability | **FAIL** | `Mar 2021 - Present` appears after both of Company Y's bullets, behind a blank line. It is neither on the title line nor adjacent to it. |
| 0.7 reading order | **FAIL** | Raw and layout disagree. Layout order: title, date, bullets. Raw order: title, bullets, date. |
| 0.2 ligatures | PASS | `efficient` 4 hits, `workflow` 4 hits, U+FB01/FB02 count 0. |

`\hfill` inside `\makebox` produces the same defect as `tabular*`. The right
field is a separate positioned text run, and poppler emits it out of order.
`tabular*` was not the cause. Horizontal separation was.

## Shape C: current `tabular*` macro, control

Macro under test, copied verbatim from `template-rails-original.tex:44-50`:

```latex
\newcommand{\resumeSubheading}[4]{
\vspace{-1pt}\item
  \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
    \textbf{#1} & #2 \\
    \textit{#3} & \textit{#4} \\
  \end{tabular*}\vspace{-7pt}
}
```

### Raw extraction, verbatim (`pdftotext shape-c.pdf -`)

```
EXPERIENCE
Company X
Senior Software Engineer

Jan 2020 - Feb 2021
Vitoria, ES

Built an efficient billing pipeline that cut invoice workflow latency.
Owned the deployment workflow and made the release process efficient.

Company Y
Senior Software Engineer
Designed an efficient multi-tenant API and its onboarding workflow.
Automated the review workflow, making incident response efficient.

Mar 2021 - Present
Vitoria, ES
```

### Layout extraction, verbatim (`pdftotext -layout shape-c.pdf -`)

```
EXPERIENCE
 Company X                                                                  Jan 2020 - Feb 2021
 Senior Software Engineer                                                            Vitoria, ES
   Built an efficient billing pipeline that cut invoice workflow latency.
   Owned the deployment workflow and made the release process efficient.

 Company Y                                                                   Mar 2021 - Present
 Senior Software Engineer                                                           Vitoria, ES
   Designed an efficient multi-tenant API and its onboarding workflow.
   Automated the review workflow, making incident response efficient.
```

### Verdict: FAIL

| Check | Result | Evidence |
|---|---|---|
| 0.5 segmentation | **FAIL** | Same split as B. Three blocks per role. |
| 0.6 date parseability | **FAIL** | Same as B. `Mar 2021 - Present` lands after the bullets. |
| 0.7 reading order | **FAIL** | Same as B. |
| 0.2 ligatures | PASS | `efficient` 4 hits, `workflow` 4 hits, U+FB01/FB02 count 0. |

`diff shape-b-raw.txt shape-c-raw.txt` returns no difference. B and C produce
the same raw extraction.

## Result

| Shape | 0.5 | 0.6 | 0.7 | 0.2 | Verdict |
|---|---|---|---|---|---|
| A, one source line | PASS | PASS | PASS | PASS | **WINNER** |
| B, `\makebox` + `\hfill` | FAIL | FAIL | FAIL | PASS | rejected |
| C, `tabular*` control | FAIL | FAIL | FAIL | PASS | rejected |

The damage in B and C is worse than a split block. For the most recent role the
date range is emitted after the bullets. A parser that reads the stream in
order attaches `Mar 2021 - Present` to whatever follows, or drops it. That
corrupts tenure and current-role inference at the same time. This is the
failure CV-SPEC item 2 predicted.

The test also corrects the spec's stated cause. `tabular*` is not the culprit.
Shape B removes `tabular*` and keeps the horizontal split, and it fails
identically. The cause is the horizontal split itself.

## Macro to adopt

Replace `template-rails-original.tex:44-50` with this. The argument order is
unchanged, so no call site needs editing.

```latex
% #1 Company  #2 Dates  #3 Title  #4 Location
% One source line. Everything a parser needs for one role lands on one line,
% in one text run, in reading order. Bake-off: reports/macro-bakeoff.md
\newcommand{\resumeSubheading}[4]{
\vspace{-1pt}\item
  \textbf{#1} \textbar{} #3 \textbar{} #2 \textbar{} #4
  \vspace{-7pt}
}
```

Rendered order is Company, Title, Dates, Location. Keep that order. A long
header wraps only after the Dates field, so a wrap can never separate the date
from the title.

Two more preamble changes the build proved necessary. They belong to the Resume
Architect, not to me:

```latex
% pdfTeX primitives. tectonic runs XeTeX and dies on the bare form.
\ifdefined\pdfgentounicode\input{glyphtounicode}\fi
\ifdefined\pdfgentounicode\pdfgentounicode=1\fi
```

And drop `\DisableLigatures[f,q]{encoding = *, family = *}`. It aborts the
tectonic build. `\usepackage{microtype}` on its own is safe and loads clean.

## Questions for Lucas, recorded not asked

1. CV-SPEC item 1 may be solved by the toolchain change alone. The ligature
   loss is real in the four Overleaf PDFs. It does not reproduce under tectonic
   with the same `roboto` font. Do you want item 1 rewritten to "no fix needed
   under tectonic, verify with grep after every build", or kept as written in
   case a build ever falls back to pdfLaTeX?
2. The `|` separator would then appear in three places on a finished CV: the
   contact block, the Skills list, and every role header. A parser reads it
   without ambiguity. A human may read it as busy, which is Gate 3.8. Do you
   want a different visual treatment for the header, for example a bold company
   name plus a thin rule? Any such change must be re-tested here before it
   ships.
3. Shape A drops the right-aligned dates that the current template renders.
   That is a deliberate trade: Gate 0.5, 0.6 and 0.7 over Gate 3.8. Confirm you
   accept it.

## Claims I could not verify

None. This report makes no claim about Lucas's history. `Company X` and
`Company Y` are fabricated test fixtures. The strings in the stress test are
format probes for line wrapping, not assertions about employment.
