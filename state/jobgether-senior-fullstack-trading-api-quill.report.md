# Quill report: Jobgether, Senior Full-Stack Engineer - Trading API

Date: 2026-09-04
Hunt: 2026-09-04-g
Language: English only
Segment: agency
Base: resumes/base-en.tex, copied. Base not edited. Preamble and layout unchanged, confirmed with diff on lines 1-52.
Status: package written, PDF built, one page. Not graded. Not submitted.

## Files written

- /Users/lucasqueiroz/career/resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.tex
- /Users/lucasqueiroz/career/resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf
- /Users/lucasqueiroz/career/resumes/hunts/2026-09-04-g/jobgether-senior-fullstack-trading-api/application-note.md (draft, not sent)
- /Users/lucasqueiroz/career/state/jobgether-senior-fullstack-trading-api-quill.report.md (this file)
- /Users/lucasqueiroz/career/state/jobgether-senior-fullstack-trading-api-quill.complete.json (sentinel)

No other file was changed. The app ledger and hunt README were not touched; the Maestro owns them.

## Inputs read

AGENTS.md, CV-SPEC.md, DOSSIER.md, ATS-KNOWLEDGE.md, claim-allowlist.json, jobs/jobgether-senior-fullstack-trading-api.md, state/jobgether-senior-fullstack-trading-api-manifest.json, state/hunt-2026-09-04-g-linkedin-identity.json, resumes/base-en.tex, keywords/agency.md.

## Build

```
tectonic Lucas-Queiroz-Resume-en.tex
pdfinfo Lucas-Queiroz-Resume-en.pdf        # Pages: 1
pdftotext Lucas-Queiroz-Resume-en.pdf -
pdftotext -layout Lucas-Queiroz-Resume-en.pdf -
```

Build succeeded. Only fontspec font-loading notices, same as the base. First build overflowed to two pages by the Education block; I shortened my own additions (not base facts) until the complete content fit on one page. No base bullet was removed.

## Extraction checks on the raw text

- Contact block on one line: city, phone, email, LinkedIn, GitHub. No UTC offset, no time-zone statement.
- Headers extract as SUMMARY, SKILLS, LANGUAGE, EXPERIENCE, EDUCATION.
- Four employment blocks plus Education each extract as one block: company, title, dates, location, then bullets. Role header macro is the base's, unchanged per the dispatch.
- `grep -c workflow` returns 5 and `office` returns 2, so ligatures are disabled.
- `grep -in 'ruby\|rails'` on the .tex and on the extracted text returns 0.
- `grep -ic 'utc\|gmt\|fintech\|trading\|tailwind\|code review'` on the extracted text returns 0.

## Titles and dates

Every `{Company}{Dates}` and `{Title}{Location}` pair is identical to base-en.tex (diff on the resumeSubheading lines). Each title and period string was also found verbatim in state/hunt-2026-09-04-g-linkedin-identity.json: `Senior Software Engineer` / `Mar 2026 - Present`, `Mid-level Software Engineer` / `Jan 2024 - Mar 2026`, `Mid-level Software Engineer` / `Jan 2023 - Jan 2024`, `Entry-level Fullstack Software Engineer` / `Mar 2021 - Jan 2023`. Company strings `DexCare`, `Luizalabs`, `Lippaus Distribuidora` match.

## Preserved content

- Roles: 4 of 4. Education preserved.
- Bullets: 16 of 16 (raw text count of `•` is 16).
- Metrics: 15%, 25%, 7%, 33%, 20%, 18%, 26%. All 7 present.
- Language section separate: `Portuguese: Native | English: Fluent (C1)`.
- Summary: first person with `I`, mentions AI once, mentions `full-stack development` and `REST APIs`.

## Edits against the base, facts unchanged

- Summary: `5+ years building TypeScript, Node.js, React, and Go systems` to `5+ years of full-stack development in TypeScript, React, Node.js, and Go`; `multi-tenant APIs` to `multi-tenant REST APIs`.
- Skills Languages: added `(Golang)` after `Go`, added `SQL`.
- Skills Backend: added `API design`; moved `Auth0` here from Cloud (line-fit).
- Skills Frontend: added `HTML | CSS`.
- Skills Cloud: `GCP` to `Google Cloud Platform (GCP)`; `Datadog` moved to the last line, renamed `Testing, observability, and AI tooling`.
- DexCare Auth0 bullet: `that isolated tenant data, enforced API contracts, and reduced` to `, owning API design and contracts, that isolated tenant data and reduced`.
- DexCare data bullet: `in PostgreSQL with` to `in SQL on PostgreSQL with`; `, DynamoDB Streams, and Redis` to `, plus DynamoDB Streams and Redis`.
- Luizalabs bullet 1: language order `Node.js, Java, and Go` to `Go, Node.js, and Java`.
- Lippaus mid bullet 3: `turned customer requirements into delivered solutions` to `turned stakeholder requirements into production-ready features`. Dossier-approved fact: project scoping and stakeholder communication.
- Lippaus entry bullet 1: `in JavaScript` to `in JavaScript, HTML, and CSS`. Inference: a JavaScript back-office web dashboard is HTML and CSS. Flag if the Analyzer treats this as unsupported.

## Term placement (raw text, word-boundary counts)

| Token | Manifest | Skills | Experience bullet | Count |
| --- | --- | --- | --- | --- |
| Golang | required | Languages, `Go (Golang)` | none, mirrored once; `Go` in Luizalabs bullet 1 | 1 (Go: 3) |
| TypeScript | required | Languages | DexCare bullet 1 | 3 |
| React | required | Frontend | DexCare flags bullet | 3 |
| HTML | required | Frontend | Lippaus entry bullet 1 | 2 |
| TailwindCSS | required | absent | absent | 0 |
| SQL | required | Languages | DexCare data bullet | 2 |
| REST APIs | required | Backend | DexCare Auth0 bullet | 3 |
| PostgreSQL | preferred | Data | DexCare data bullet, Lippaus platform bullet | 3 |
| Google Cloud Platform | preferred | Cloud, `Google Cloud Platform (GCP)` | Luizalabs deploy bullet as `GCP` | 1 (GCP: 2) |
| Docker | preferred | Cloud | Luizalabs deploy bullet | 2 |
| Kubernetes | preferred | Cloud | Luizalabs deploy bullet | 2 |
| API design | practice | Backend | DexCare Auth0 bullet | 2 |
| CSS | practice | Frontend | Lippaus entry bullet 1 | 2 |
| full-stack | practice | Summary | | 1 |
| stakeholder requirements | practice | | Lippaus mid bullet 3 | 1 |

No term exceeds 3 appearances. Node.js 3, AWS 3, BullMQ 3, all at the cap.

## Escalation: TailwindCSS absent

`TailwindCSS` is a required token in the manifest. DOSSIER.md records no CSS framework of any kind, so I did not place it. Placing it would be an invented tool claim. The screening answer marks it `not recorded`. If Lucas confirms Tailwind use at any employer, add `TailwindCSS` to Skills Frontend and to the matching bullet in a fix round. `C#`, `mentor`, `fintech`, `trading`, `algorithmic trading`, and `financial markets` were also left absent; none is supported by the dossier, and the dispatch forbids implying fintech or trading experience. `code review` is on the claim allowlist as unverified and was not added.

## Note

application-note.md holds the English recruiter message and screening answers. No recruiter name is observable on the posting, so the message addresses the Jobgether team. Time zone appears in the screening answers only, never on the CV. Unavailable facts (TailwindCSS, C#, fintech, algorithmic trading, mentoring, salary, notice period) are marked `not recorded`.

## Fix round 1, 2026-09-04

Superseded on two points by state/jobgether-senior-fullstack-trading-api-quill-fix1.report.md: `TailwindCSS` is now placed in Skills Frontend and in the DexCare flags bullet, and `Golang` is now placed in the Luizalabs bullet 1 as `Go (Golang)`. The TailwindCSS escalation above is closed by the Maestro's ruling under AGENTS.md section 4.
