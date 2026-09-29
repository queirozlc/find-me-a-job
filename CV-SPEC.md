# CV specification

Authoritative format spec. The Resume Architect builds to this; the ATS
Analyzer gates against it. Source of the template: Lucas's Overleaf document,
supplied 2026-09-01. Every change below is traceable to a File Readability
Check failure Sieve found in the four existing PDFs, or to `CLAUDE.md`.

## Toolchain

- Source: LaTeX, `article`, `letterpaper`, `10pt`. Roboto via `sfdefault`.
- Compiler: **tectonic**. One binary, no TeX Live.
- Build: `tectonic ~/career/resumes/<name>.tex`
- **Every build is followed by an extraction check.** A PDF nobody extracted is
  a PDF nobody has tested:
  ```
  pdftotext          <name>.pdf - > raw.txt      # what a parser sees
  pdftotext -layout  <name>.pdf - > layout.txt   # what a human sees
  ```
- Overleaf is for Lucas's own visual review, not part of the gate. The `.tex`
  lives in `~/career/resumes/` and he opens it there when he wants to look.

## Languages

**The bases ship as a pair**, `base-en.tex` and `base-pt.tex`. Same facts,
same structure, same dates.

**A tailored CV ships in one language only, the language of the posting**
(Lucas, 2026-09-02). Maestro decides the language at intake from the posting
text and the company origin: a Brazilian company posting in Portuguese gets
`<slug>-pt`; an international company or an English posting gets `<slug>-en`;
a Spanish posting gets `<slug>-es`, built from `base-en.tex`. Never build the
other language for the same posting.

Set `\usepackage[english]{babel}` or `[brazilian]{babel}` per language.

## Mandatory fixes to the current template

Each one is a confirmed defect, not a preference.

### 1. Ligatures — File Readability Check 0.2, failed in all four existing PDFs

The template already has `\input{glyphtounicode}` and `\pdfgentounicode=1`.
**That is not enough.** It maps the ToUnicode CMap correctly, but a ligature
glyph still maps to U+FB01, not to `f`+`i`. Confirmed: grepping the extracted
text of all four PDFs for `office`, `workflow`, `efficient`, `profile` returns
**zero hits**; the words are stored as `backofﬁce`, `workﬂows`, `ﬁscal`.

Tectonic runs XeTeX. `microtype` `\DisableLigatures` is pdfTeX-only and fails
the build (verified by Quill, 2026-09-01). `glyphtounicode` and
`\pdfgentounicode` are also pdfTeX-only; remove them. Use fontspec instead,
loaded before `roboto`:

```latex
\usepackage{fontspec}
\defaultfontfeatures{Ligatures=NoCommon}
```

Then verify: `pdftotext out.pdf - | grep -c workflow` must be non-zero when the
word is present.

### 2. Employment-block segmentation, File Readability Check 0.5

Use a single-column role header. Do not use `tabular*`, a table, or a text box.
Print company, title, location, and dates as consecutive text lines in a
consistent order. Raw and layout extraction must keep each role as one block.

Leave clear vertical space between the role header and its first bullet. Leave
clear vertical space between the last bullet and the next role. Prefer one
page, but use two pages when the complete content does not fit.

### 3. Contact block — File Readability Check 0.3, failed in all four

Add the city. It is absent today, and its absence fails the Role Eligibility
Check for any posting that requires this location.

```
Vitória, ES, Brazil | +55 (27) 99203-0170 | sepulchrolucas@gmail.com
linkedin.com/in/queiroz-lucas | github.com/queirozlc
```

**Never print a UTC offset and never print a time-zone overlap statement**
(Lucas, 2026-09-02). Overlap lives in the apply note's screening answers.

### 4. Section headers — File Readability Check 0.4

The text layer must carry the canonical strings. `\scshape` changes only the
rendering, not the extracted text, so the source string is what counts.

Required, verbatim. EN: `Summary`, `Skills`, `Experience`, `Education`,
`Language`. PT files: `Resumo`, `Habilidades`, `Experiência`, `Formação`,
`Idiomas` (Lucas, 2026-09-04; allowlisted in the RUBRIC File Readability Check, item 0.4).
Optional: `Projects`, `Certifications`.

Replace `professional summary` with `Summary`, `technical skills` with
`Skills`, `work experience` with `Experience`. Drop `\section*` in favour of
`\section` so every header is a real heading.

### 5. Dates — File Readability Check 0.6

`Mon YYYY - Mon YYYY`, ASCII hyphen, everywhere. The current template mixes an
ASCII hyphen with EN DASH U+2013 (`May 2021 -- Jan 2024`). One separator only.

## Content rules

The Summary must mention AI or LLM work once the dossier records it (Lucas, 2026-09-01).

### Titles and dates

**Strictly from LinkedIn**, per `CLAUDE.md` rule 1. The verbatim strings are in
`DOSSIER.md` under **LinkedIn ground truth**. The current template is wrong on
every one of them:

- Luizalabs ended **Jan 2026**, it is not `Present`.
- **DexCare is missing entirely.** It is the current role.
- Lippaus Distribuidora is **two roles, not one**. Entry-level Fullstack
  Software Engineer `Mar 2021 - Jan 2023`, then Mid-level Software Engineer
  `Jan 2023 - Jan 2024`. **Keep both.** The promotion is a seniority signal the
  old resumes flattened away.

### Stack

No Ruby or Rails token anywhere. Substitute the JS/TS equivalent: Sidekiq to
**BullMQ**, ActiveRecord to **Drizzle**, ActiveJob to **BullMQ**, RSpec to
**Vitest**/**Jest**, Hotwire to the actual frontend in use.

ATS match is the first content objective for an accepted posting. The primary
language or runtime must be JavaScript, TypeScript, Node.js, or Go. Triage
drops postings with another primary stack before tailoring. For an accepted
posting, place each exact required framework, library, data, messaging, cloud,
tool, or practice token in `Skills` and in one relevant `Experience` bullet.
Do not add claim-status markers.

DexCare stack is observed fact, read from the repos, safe to use: TypeScript,
Node.js, Express, Koa, PostgreSQL, Sequelize, Drizzle ORM, DynamoDB, Redis,
AWS SDK v3, LaunchDarkly, OpenFeature, OpenAPI/Swagger, Datadog, Auth0,
multi-tenant JWT, React, Epic EMR integration.

Every load-bearing technology appears in `Skills` **and** in context inside an
`Experience` bullet. Cap any term at 3 appearances.

### Bullets

Voice set by Lucas 2026-09-02, replacing the 2026-09-01 rule. **First person,
past tense, subject omitted.** Every bullet must read as something Lucas did,
not as a duty. Lead with a past-tense verb: `Built`, `Designed`, `Reduced`,
`Helped build`. Never present tense (`Deliver`, `Keep`), never `Responsible
for`, never third person. Do not write `I` at the start of a bullet; the
Summary carries the `I`. Every bullet follows the XYZ format: accomplished X,
measured by Y, by doing Z. Name the technologies in the bullet. Carry a real
number whenever the dossier has one. Mention AI or LLM work in Experience
where the dossier supports it.

PT files follow the same rule: past tense, first person, subject omitted
(`Construí`, `Reduzi`, `Ajudei a construir`).

Never trim Experience for tailoring. Copy every verified Experience role,
bullet, and metric from the selected base. Reword and reorder when required,
but do not delete content to save space or improve match.

### Language section

Spoken-language proficiency is not a technical skill. Keep it out of `Skills`
and `Habilidades`. Use a separate section after Skills:

- EN header: `Language`. Content: `Portuguese: Native | English: Fluent (C1)`.
- PT header: `Idiomas`. Content: `Português: Nativo | Inglês: Fluente (C1)`.

### Summary

Voice set by Lucas 2026-09-02: **first person with the subject**, `I build`,
`I have`, `I integrate`. Present tense for what Lucas does today, past tense
for what he did. Not a headline in third person.

Rewrite entirely. The current one says "specializing in Ruby on Rails, React,
and Node.js", claims Rails core contribution, and says the current focus is
fiscal systems for a Brazilian e-commerce retailer. All three are wrong as of
Jan 2026.

### Open-source section

**Decision made, not yet applied. Do not act on this until Lucas says so.**
Drop the `projects` / "Ruby on Rails Framework Ecosystem" block from the CV and
move it to the LinkedIn About section. Reason: it puts Ruby and Elixir tokens
in prime real estate on a document whose retrieval target is Node, TypeScript,
React and Go, and the Resume Evidence Check penalizes tokens with no supporting evidence
elsewhere in the document.

### Length

Prefer one page when every verified Experience bullet fits. Never remove a
verified Experience bullet or metric to meet a page limit. Use two pages when
the complete tailored content does not fit on one page.

## Definition of done

A CV is ready only when all of these hold:

1. A base round builds both `-en` and `-pt`. A tailored application builds
   only the posting language.
2. File Readability Check: all 8 checks PASS on the raw extraction.
3. Role Eligibility Check: no FAIL against the target posting.
4. Resume Evidence Check: every required token appears in `Skills` and in one relevant
   `Experience` bullet.
5. Every title and date matches `DOSSIER.md` **LinkedIn ground truth**
   character for character.
