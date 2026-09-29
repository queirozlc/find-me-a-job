# ATS Analysis — resumes/base-en.pdf and resumes/base-pt.pdf vs (no posting, base round)
Segment: n/a (shared base pair)   Date: 2026-09-04
Task: hunt-2026-09-04-g-base-sieve. Analyzer: Sieve. Scope set by Maestro:
File Readability Check (8 checks) and Recruiter Readability Score only. No
Role Eligibility Check and no Resume Evidence Check, because there is no
posting. Both CVs untouched.

## Verdict
READY (base round). Both bases pass all 8 File Readability checks. No
identity, date, or metric defect found.

## Decision Explanation
No blocking reason.

## Inputs read
- ATS-KNOWLEDGE.md, RUBRIC.md, CV-SPEC.md, CLAUDE.md (career root),
  DOSSIER.md, state/hunt-2026-09-04-g-linkedin-identity.json,
  state/hunt-2026-09-04-g-base-apply.report.md.
- resumes/base-en.tex, resumes/base-pt.tex, resumes/base-en.pdf,
  resumes/base-pt.pdf.
- Extraction: `pdftotext <pdf> -` (raw) and `pdftotext -layout <pdf> -`
  (layout) for both PDFs. All Gate 0 judgements below are on the raw file.
- Cross-check: both `.tex` files are byte-identical to
  `resumes/hunts/2026-09-04-g/base-preview/`. Both `.tex` files were rebuilt
  with tectonic in a scratch directory. The rebuilt raw extraction is
  byte-identical to the shipped PDF extraction for EN and for PT. The shipped
  PDFs are the current sources.

## File Readability Check

### resumes/base-en.pdf

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 72 raw lines, 2 pages, Roboto CID fonts embedded with ToUnicode (`pdffonts` uni=yes), producer xdvipdfmx |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes (`tr -cd '\000'`), 0 `?`, 0 glyphs in U+FB00-FB06. `workflow` 5 hits, `office` 2 hits (`back-office`), all intact. `profile`, `efficient`, `conflict` absent from the text, so not testable |
| 0.3 | Contact block recoverable | PASS | Line 3 of raw, body text, `\pagestyle{empty}`: `Vitória, ES, Brazil \| +55 (27) 99203-0170 \| sepulchrolucas@gmail.com \| linkedin.com/in/queiroz-lucas \| github.com/queirozlc` |
| 0.4 | Section headers verbatim | PASS | Standalone lines `SUMMARY`, `SKILLS`, `LANGUAGE`, `EXPERIENCE`, `EDUCATION` (uppercase rendering, source strings canonical) |
| 0.5 | Employment-block segmentation | PASS | 4 role blocks, each company / title / dates / location on 4 consecutive lines, then its bullets. Bullets per role 7 / 4 / 3 / 2. No merge, no split. Page break falls between Lippaus Mid-level and Lippaus Entry-level; page 2 opens with the full 4-line header and both bullets |
| 0.6 | Date parseability | PASS | Every role has `Mon YYYY - Mon YYYY` (ASCII hyphen) on the line directly after the title. 0 EN DASH characters |
| 0.7 | Reading order | PASS | Raw and layout extraction, whitespace-normalized, are line-for-line identical |
| 0.8 | No forbidden constructs | PASS | `pdfimages -list` empty. `.tex` has no `tabular`, `minipage`, `parbox`, `includegraphics`, `fancyhdr`, icon font |

### resumes/base-pt.pdf

| # | Check | Result | Evidence |
|---|---|---|---|
| 0.1 | Text layer exists | PASS | 72 raw lines, 2 pages, same font set and producer as EN |
| 0.2 | Glyph integrity | PASS | 0 NUL bytes, 0 `?`, 0 glyphs in U+FB00-FB06. `workflow` 2 hits, `office` 2 hits (`backoffice`), `fluxo` 3 hits, all intact. All accented characters (ç ã í ó ê ...) extract as single code points |
| 0.3 | Contact block recoverable | PASS | Same body-text contact line as EN, `Brazil` spelling per CLAUDE.md section 3 |
| 0.4 | Section headers verbatim | PASS | Standalone lines `RESUMO`, `HABILIDADES`, `IDIOMAS`, `EXPERIÊNCIA`, `FORMAÇÃO` |
| 0.5 | Employment-block segmentation | PASS | Same 4 blocks, 7 / 4 / 3 / 2 bullets. Page break at the same position as EN, header and both bullets intact on page 2 |
| 0.6 | Date parseability | PASS | Same 5 date lines as EN, ASCII hyphen, adjacent to title |
| 0.7 | Reading order | PASS | Raw and layout identical after whitespace normalization |
| 0.8 | No forbidden constructs | PASS | No images, no tables, no text boxes |

Note on method: a first NUL scan with `grep -c $'\x00'` returned 73 on both
files. That is a shell artifact, the pattern becomes empty and matches every
line. The byte-level count `tr -cd '\000' | wc -c` is 0 on both files.

## Identity verification against LinkedIn cache

Source: `state/hunt-2026-09-04-g-linkedin-identity.json`, captured
2026-09-04T20:01:30+00:00 from
https://www.linkedin.com/in/queiroz-lucas/details/experience/. Each string
below was searched verbatim in the cached profile text and in both raw
extractions.

| Company (CV) | Title (CV) | Dates (CV) | In cache | EN raw | PT raw |
|---|---|---|---|---|---|
| DexCare | Senior Software Engineer | Mar 2026 - Present | yes | yes | yes |
| Luizalabs | Mid-level Software Engineer | Jan 2024 - Mar 2026 | yes | yes | yes |
| Lippaus Distribuidora | Mid-level Software Engineer | Jan 2023 - Jan 2024 | yes | yes | yes |
| Lippaus Distribuidora | Entry-level Fullstack Software Engineer | Mar 2021 - Jan 2023 | yes | yes | yes |

Locations: DexCare and Luizalabs print `Remote` (EN) / `Remoto` (PT). Both
Lippaus roles print `Vitória, ES, Brazil`. Matches CLAUDE.md section 3.

Education: the identity cache covers the Experience details page only and
does not contain `FAESA`. Education was checked against DOSSIER.md
"LinkedIn ground truth": `FAESA`, `Bachelor's degree , Information Systems`,
`Feb 2022 – Dec 2025`. CV prints `FAESA` / `Bachelor's degree, Information
Systems` (EN) or `Bacharelado em Sistemas de Informação` (PT) /
`Feb 2022 - Dec 2025`. Months identical. Separator is the ASCII hyphen per
CLAUDE.md rule 1 clarification. The degree string is not a job title. The PT
degree wording is not observable against the Portuguese LinkedIn profile;
the cache read the English profile.

Metrics, both files, raw extraction, in order: 15%, 25%, 7%, 33%, 20%, 18%,
26%. Seven metrics. Each one matches DOSSIER.md bullet metrics D2, D3, D5,
D7, L2, L3, P2. No other number appears except `5+` years / `mais de 5 anos`
in Summary and `AWS SDK v3`.

Stack: 0 hits for `ruby`, `rails`, `sidekiq`, `activerecord`, `rspec` in
both files. 0 hits for `UTC`, `GMT`, `overlap`, `fuso`. Every counted
technology token appears at most 3 times (CV-SPEC cap): TypeScript 3,
Node.js 3, Go 3, React 3, BullMQ 3, PostgreSQL 3, AWS 3, multi-tenant 3.

## Sixteen Experience bullets, verified

Both files: 16 bullets in raw and in layout extraction, 7 DexCare, 4
Luizalabs, 3 Lippaus Mid-level, 2 Lippaus Entry-level. Count and order match
`state/hunt-2026-09-04-g-base-apply.report.md` and the `.tex` sources.

| # | Role | EN opening verb | PT opening verb | Metric |
|---|---|---|---|---|
| D1 | DexCare | Built | Construí | none (dossier: leave as is) |
| D2 | DexCare | Integrated | Integrei | 15% |
| D3 | DexCare | Built | Construí | 25% |
| D4 | DexCare | Modeled | Modelei | none |
| D5 | DexCare | Reduced | Reduzi | 7% |
| D6 | DexCare | Built | Construí | none |
| D7 | DexCare | Helped implement | Ajudei a implementar | 33% |
| L1 | Luizalabs | Built | Construí | none |
| L2 | Luizalabs | Moved | Migrei | 20% |
| L3 | Luizalabs | Built | Construí | 18% |
| L4 | Luizalabs | Deployed | Implantei | none |
| P1 | Lippaus Mid | Built | Construí | none |
| P2 | Lippaus Mid | Processed | Processei | 26% |
| P3 | Lippaus Mid | Led | Liderei | none |
| E1 | Lippaus Entry | Developed | Desenvolvi | none |
| E2 | Lippaus Entry | Built | Construí | none |

All 16 start with a past-tense verb, subject omitted. 0 hits for
`Responsible for`, present-tense duty verbs, or third person. Summary uses
`I` (EN) and `Eu` (PT).

## Role Eligibility Check
Not run. No posting in scope for a base round.

## Resume Evidence Check
Not run. No posting in scope for a base round.

## Recruiter Readability Score: 98/100 (EN), 98/100 (PT)

Target title for a base round is the CV title `Senior Software Engineer`
(DOSSIER.md). Relevance for 3.2 is judged against the positioning
TypeScript, Node.js, React, Go, since there is no posting.

| # | Check | EN | PT | Evidence |
|---|---|---|---|---|
| 3.1 | Target title in top 15% | 15/15 | 15/15 | `Senior Software Engineer` on raw line 6 of 72 (8%), first Summary sentence, and again as the DexCare title |
| 3.2 | 3 most relevant bullets first in most recent role | 20/20 | 20/20 | DexCare bullets 1-3: TypeScript/Express/Koa event-driven services, Epic EMR 15%, multi-tenant REST APIs with Auth0 and OpenAPI 25% |
| 3.3 | Past-tense action verb and outcome in every bullet | 13/15 | 13/15 | All 16 verbs pass. Two bullets state no outcome: D4 `Modeled booking reads and writes ... wired to S3 and RDS through AWS SDK v3` and E2 `Built customer-facing features end to end by balancing business requirements with technical constraints` |
| 3.4 | At least 3 bullets with a real number | 15/15 | 15/15 | 7 bullets, all numbers traced to DOSSIER.md |
| 3.5 | Experience completeness | 10/10 | 10/10 | 4 roles, 16 bullets, 7 metrics, nothing removed. 2 pages; page 2 carries the Entry-level role and Education. Whether tighter spacing fits one page was not tested |
| 3.6 | No unsupported buzzwords | 10/10 | 10/10 | 0 hits for team player, results-driven, passionate, self-starter, synergy, dynamic |
| 3.7 | Skills grouped by category | 10/10 | 10/10 | 6 labelled groups: Languages, Backend, Data, Frontend, Cloud and operations, Testing and AI tooling |
| 3.8 | Scannable | 5/5 | 5/5 | Bold company, italic title and location, consistent 3pt role gap, single column, no orphaned header |

## Defects, ranked by cost
No blocking defect. Non-blocking items for the Architect and Maestro:

1. D4 and E2 carry no outcome — Recruiter Readability 3.3 — DOSSIER.md
   records "no number, leave as is" for D4 and E2, so this is a wording
   observation only. A qualitative outcome clause is possible without a
   metric. Lucas decision, not a CV FIX.
2. PT Summary prints `para uma empresa dos EUA` — content parity — the EN
   Summary has no employer-origin clause. CV-SPEC says the bases carry the
   same facts. DOSSIER.md bans "Works remotely from Brazil with US-based
   teams or any equivalent sentence". This clause names the employer's
   country, not Lucas's remote position, so it is not a clear match for the
   ban. Lucas decision. Lucas approved this preview, so it stands unless he
   says otherwise.
3. PT prints `Present` in `Mar 2026 - Present` — consistency — matches
   LinkedIn verbatim as CLAUDE.md rule 1 requires. A Portuguese recruiter
   sees one English word in the date line. No action unless Lucas changes
   the rule.
4. Page 2 carries 6 content lines plus Education — Recruiter Readability
   3.5 — allowed by the rubric. If the Architect wants one page, it must
   come from spacing only, never from removing a bullet.

## Match limits
Not applicable. No posting.

## Not done
- No CV edit, no delegation, no portal use.
- No Role Eligibility Check, no Resume Evidence Check, per task scope.
