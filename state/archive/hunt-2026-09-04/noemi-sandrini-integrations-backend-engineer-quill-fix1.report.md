# Quill fix round 1 result — noemi-sandrini-integrations-backend-engineer

Role: Resume Architect. Edited, did not grade.
Date: 2026-09-04
Hunt: 2026-09-04
Application: Noemi Sandrini, Integrations Back-end Engineer
Input: `state/noemi-sandrini-integrations-backend-engineer-sieve.report.md`, Tier A fixes 1 to 8

## Files edited

- `resumes/hunts/2026-09-04/noemi-sandrini-integrations-backend-engineer/Lucas-Queiroz-Resume-en.tex`
- `resumes/hunts/2026-09-04/noemi-sandrini-integrations-backend-engineer/Lucas-Queiroz-Resume-en.pdf` (rebuilt)
- `reports/noemi-sandrini-integrations-backend-engineer-draft.md`

No other file was changed. The base pair and DOSSIER.md were not touched. No subagent was spawned. No Maestri message was sent.

## Fixes applied

| Sieve fix | Change | Source line |
| --- | --- | --- |
| 1 | `Back-end` listed as a Skills token. DexCare booking bullet now reads `building event-driven Back-end services in TypeScript and Node.js on Express`. Skills label `Backend and integrations` renamed to `Services` so the term stays at 3. | 57, 69 |
| 2 | New DexCare bullet: `Reduced wrong bookings by 15% by building third-party API integrations with Epic EMR that kept bookable time slots synced with hospital records.` Source: DOSSIER.md observed DexCare stack, Epic EMR integration, and metric D2. `third-party API integrations` also listed in Skills. | 57, 70 |
| 3 | DexCare AI bullet rewritten: `Raised code quality in AI-assisted development by building agent environments with shared rules, lint, complexity limits, and testing for validation of AI-generated code from the AI code agents Claude Code and Codex in agentic workflows.` Source: DOSSIER.md "AI at DexCare". | 74 |
| 4 | `workflows` 5 to 3. Booking bullet `workflows` to `features`. Lippaus entry-level bullet `workflows` to `processes`. All three `agentic workflows` kept. | 69, 99 |
| 5 | Summary now reads `I build event-driven back-end REST APIs, third-party API integrations, and distributed systems on AWS.` Title untouched. | 52 |
| 6 | Two unused approved metrics attached. D2, 15% wrong bookings, in the Epic bullet. D7, 33% pilot friction, in a new Shared Platform Initiative bullet written conceptually with no customer names. Metrics with a Y: 6 of 13 bullets. | 70, 72 |
| 7 | Verbs varied. `Supported` removed from all four bullets. Openers now: Delivered, Reduced, Cut, Helped implement, Served, Raised, Collaborated, Shipped, Improved, Kept, Enabled, Increased, Streamlined. No opener repeats. | 69-99 |
| 8 | `\resumeRoleGap` raised from `\vspace{4pt}` to `\vspace{8pt}`. PDF stays on one page. Rendered page shows clear space between roles and no clipping. | 39 |

## Not applied

- Tier B rows: OAuth 2.0, OIDC, Webhooks, code review, debugging, OOP, SOLID, software design principles, direct client communication, AWS SQS. Not added. DOSSIER.md does not confirm them. They remain open for Lucas.
- The word `client` appears once, in `new-client pilot friction`, from the approved D7 metric text. It is not a client-communication claim.
- No unsupported term, metric, or experience was added.

## Verification after rebuild

- `tectonic`: PDF written, only Roboto font-request warnings.
- `pdfinfo`: Pages 1, letter.
- `pdftotext` raw and `pdftotext -layout`: contact block with city, phone, email, LinkedIn, GitHub; headers Summary, Skills, Experience, Education; four employment blocks in order DexCare, Luizalabs, Lippaus Mid-level, Lippaus Entry-level; FAESA block. Each role extracts as company, title, location, dates, then bullets. Raw and layout reading order identical.
- Dates in raw extraction: `Mar 2026 - Present`, `Jan 2024 - Mar 2026`, `Jan 2023 - Jan 2024`, `Mar 2021 - Jan 2023`, `Feb 2022 - Dec 2025`. All match DOSSIER.md LinkedIn ground truth captured 2026-09-04.
- Titles unchanged: Senior Software Engineer, Mid-level Software Engineer, Mid-level Software Engineer, Entry-level Fullstack Software Engineer.
- Locations unchanged: DexCare and Luizalabs `Remote`, Lippaus `Vitória, ES, Brazil`. No UTC offset, no overlap statement.
- `grep -ic 'ruby\|rails'` on .tex, raw text, layout text: 0, 0, 0.
- Ligature check: `workflow` and `office` extract intact.
- Term counts in raw extraction: Back-end 3, integrations 3, workflows 3, REST APIs 3, event-driven 3, TypeScript 3, Node.js 3, AWS 3, React 3, PostgreSQL 3, BullMQ 3, distributed systems 3, AI-assisted development 3, agentic workflows 3, Go 3, AI code agents 2, testing 2, Express 2, multi-tenant 2, Advanced English 2, Docker 2, queues 2, Epic 1. No term above 3.
- Metrics on the CV: 15%, 25%, 33%, 20%, 26%. All from DOSSIER.md.
- Voice: all bullets first person, past tense, subject omitted. Summary uses `I`.

## Open for the Maestro

- Tier B needs Lucas's yes or no per row, then a DOSSIER.md entry, before any of those tokens enter the CV.
- Language choice for this posting (pt-BR text, American company) remains the Maestro's call. This round kept `-en`.

No grade was produced.
