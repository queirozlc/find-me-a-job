# Quill report — AHU Technologies, Senior Full Stack Developer (React.js, Node.js / .NET Core) LATAM

Date: 2026-09-04. Hunt: 2026-09-04-b. Language: English. Base: `resumes/base-en.tex`.

## Deliverables

- `resumes/hunts/2026-09-04-b/ahu-senior-full-stack/Lucas-Queiroz-Resume-en.tex`
- `resumes/hunts/2026-09-04-b/ahu-senior-full-stack/Lucas-Queiroz-Resume-en.pdf` (1 page)
- `resumes/hunts/2026-09-04-b/ahu-senior-full-stack/application-message.md`
- this report

## Build and extraction

- `tectonic` build: OK. One warning about Roboto-Italic font request at 9pt, no error.
- `pdfinfo`: 1 page. First build was 2 pages with only Education on page 2. Fixed by
  removing 1pt line gaps in the role header and adding 0.2in to `\textheight`.
- `pdftotext` raw and `-layout`: contact block intact (Vitória, ES, Brazil, phone,
  email, LinkedIn, GitHub). Headers extracted as SUMMARY, SKILLS, LANGUAGE,
  EXPERIENCE, EDUCATION (source strings are canonical; `\scshape` uppercases the
  render). All four employment blocks present in order: DexCare, Luizalabs,
  Lippaus Distribuidora (Mid-level), Lippaus Distribuidora (Entry-level). Titles,
  dates, and locations match DOSSIER.md LinkedIn ground truth character for
  character. All 16 base bullets present. Metrics 15%, 25%, 7%, 33%, 20%, 18%,
  26% present.
- `grep -in 'ruby\|rails'`: 0 hits.
- PDF inspected as PNG: single column, no overflow, no clipped text.

## Changes from base

1. Role header macro rewritten from `tabular*` to single-column consecutive lines
   (company, title, `location | dates`), per CV-SPEC item 2 and the Resume
   Architect role instructions. The base still carries `tabular*`; the base was
   not edited.
2. Skills Backend: `REST APIs` -> `RESTful APIs` (posting spelling). Added
   `JWT authentication`.
3. Skills Frontend: `React` -> `React.js` (posting spelling).
4. DexCare bullet 3: `with Auth0 JWT and OpenAPI/Swagger validation` ->
   `with JWT authentication through the third-party auth provider Auth0 and
   OpenAPI/Swagger validation`. Same facts, adds posting tokens `JWT
   authentication` and bonus phrase `third-party auth provider`.
5. DexCare bullet 5: `monitoring React with Datadog RUM` -> `monitoring React.js
   with Datadog RUM`.
6. `\textheight` +1.0in -> +1.2in, header line gaps 1pt -> 0pt, header trailing
   space 3pt -> 1pt. Layout only.

No employer, title, date, location, degree, metric, or language proficiency
changed. Summary unchanged; it mentions AI once.

## Required token placement

| Token | Skills | Experience bullet | Status |
|---|---|---|---|
| React.js | Frontend | DexCare, Datadog RUM bullet | placed |
| JavaScript | Languages | Lippaus Entry-level, dashboards bullet | placed |
| TypeScript | Languages | DexCare, Express/Koa bullet | placed |
| Node.js | Languages | Luizalabs, tax microservices bullet | placed |
| PostgreSQL | Data | DexCare, Sequelize/Drizzle bullet; Lippaus Mid-level | placed |
| AWS | Cloud and operations | DexCare, `AWS SDK v3` bullet | placed |
| RESTful APIs | Backend | DexCare, multi-tenant APIs bullet | placed |
| JWT authentication | Backend | DexCare, multi-tenant APIs bullet | placed |
| Next.js | - | - | unsupported, not added |
| HTML | - | - | unsupported, not added |
| CSS | - | - | unsupported, not added |
| Node 18 | - | - | unsupported, not added |
| design patterns | - | - | unsupported, not added |
| front-end pipelines | - | - | unsupported, not added |

Also not added, per dispatch instruction and no dossier support: Babel, Webpack,
NPM, Git, SVN, debugging, Agile, Waterfall.

Preferred tokens: `third-party auth provider` placed in DexCare bullet 3
(Auth0 is dossier fact). `Unit testing`, `MoQ`, `NUnit`, `complex web
architectures` not placed; MoQ and NUnit are .NET, the other two have no
dossier phrasing.

Term caps: React/React.js 3 (Summary, Skills, bullet). TypeScript 3. Node.js 3.
AWS 3. PostgreSQL 3. JWT 2.

## Message

English email draft to tahreem@ahutechnologies.com, ready to paste. States
Node.js path and explicitly no .NET Core. Screening answers only where
DOSSIER.md supports them. Nothing sent.

## Escalations for the Maestro

- Six required tokens have no claim source: Next.js, HTML, CSS, Node 18, design
  patterns, front-end pipelines. Gate 2 will show them missing. If Lucas can
  confirm any of them as fact, add the fact to DOSSIER.md and dispatch a fix
  round.
- `Open for Qualified Candidates (Local)` boundary is not observable. Lucas
  should confirm with the recruiter before sending.
- Base `base-en.tex` still uses a `tabular*` role header, which CV-SPEC item 2
  and the Architect role instructions forbid. Not edited here; needs a base
  round decision.
