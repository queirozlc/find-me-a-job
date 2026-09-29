# Quill fix round 1 result — tractian-senior-backend-engineer

Role: Resume Architect. Edited, did not grade.
Date: 2026-09-04
Hunt: 2026-09-04
Application: TRACTIAN, Senior Backend Engineer
Input: `state/tractian-senior-backend-engineer-sieve.report.md`

## Files edited

- `resumes/hunts/2026-09-04/tractian-senior-backend-engineer/Lucas-Queiroz-Resume-en.tex`
- `resumes/hunts/2026-09-04/tractian-senior-backend-engineer/Lucas-Queiroz-Resume-en.pdf` (rebuilt)
- `reports/tractian-senior-backend-engineer-draft.md`

No other file was changed. The base pair was not touched.

## Fixes applied

| Sieve fix | Change | Source line |
| --- | --- | --- |
| 1 | `{DexCare}{Jan 2026 - Present}` to `{DexCare}{Mar 2026 - Present}` | 70 |
| 2 | `{Luizalabs}{Jan 2024 - Jan 2026}` to `{Luizalabs}{Jan 2024 - Mar 2026}` | 82 |
| 3 | DexCare booking bullet now ends `with RabbitMQ messaging and DynamoDB tables.` DynamoDB is observed DexCare stack in DOSSIER.md and CV-SPEC.md. | 73 |
| 5 | `React` removed from the Summary and from the LaunchDarkly bullet (`shipping features behind LaunchDarkly`). Count 5 to 3. Remaining: Skills `React`, Skills `React Native`, Lippaus `React Native`. | 55, 76 |
| 5 | `multi-tenant` removed from the Auth0 bullet (`building REST APIs with Auth0 JWT`). Count 4 to 3. Remaining: Summary, DexCare shared-platform bullet, Lippaus bullet. | 75 |
| 6 | `AWS` placed in the DexCare shared-platform bullet: `helping replace per-customer AWS deployments`. Supported by the DOSSIER.md SPI entry, "one AWS environment per customer". Count 3: Summary, Skills, Experience. | 78 |
| 7 | `\resumeRoleGap` widened from `\vspace{2pt}` to `\vspace{7pt}`. | 42 |

## Not applied

- Fix 4, Portuguese fluency. Not applied. DOSSIER.md records no Portuguese level. No Portuguese token was added. This stays open for Lucas.
- No unsupported term, metric, or experience was added. Zero Kafka, Python, Rust, ClickHouse, ScyllaDB, Cassandra, MongoDB.

## Verification after rebuild

- `tectonic`: exit 0.
- `pdfinfo`: Pages 1.
- `pdftotext` raw and `pdftotext -layout`: contact block, Summary, Skills, Experience, Education, all four employment blocks, and FAESA extracted in order. Each role extracts as company, title, location, dates, then bullets. Visible space now separates the last bullet of each role from the next company name in the layout extraction.
- Dates in raw extraction: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. All match DOSSIER.md LinkedIn ground truth captured 2026-09-04.
- Titles unchanged: Senior Software Engineer, Mid-level Software Engineer, Mid-level Software Engineer, Entry-level Fullstack Software Engineer.
- Locations unchanged: DexCare and Luizalabs `Remote`, Lippaus `Vitória, ES, Brazil`. No UTC offset, no overlap statement.
- `grep -in 'ruby\|rails'` on the .tex, raw, and layout text: 0 hits each.
- Term counts in raw extraction: React 3, multi-tenant 3, AWS 3, DynamoDB 2, event-driven 3, PostgreSQL 3, BullMQ 3, distributed 3, APIs 3, TypeScript 3, Node.js 3.
- Metrics unchanged: 15%, 25%, 7%, 33%, 20%, 18%, 26%.
- Voice unchanged: all bullets first person, past tense, subject omitted. Summary uses `I`.

## Open for the Maestro

- Portuguese proficiency level from Lucas, then record in DOSSIER.md before any Portuguese token enters the CV.
- Sieve noted the DOSSIER.md "LinkedIn ground truth" block. The copy I read today is dated 2026-09-04 and already carries `Mar 2026 - Present` and `Jan 2024 - Mar 2026`. The CV now matches it.

No grade was produced.
