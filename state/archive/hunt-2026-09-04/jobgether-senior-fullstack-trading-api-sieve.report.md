# Sieve task result — jobgether-senior-fullstack-trading-api

Role: ATS Analyzer. Date: 2026-09-04. Segment: agency.
Full gate report: `reports/jobgether-senior-fullstack-trading-api-gate.md`.

## Verdict

**BLOCKED at Gate 1.** Three required posting skills are absent verbatim from
the raw PDF extraction: `Golang`, `HTML`, and a modern CSS framework such as
`TailwindCSS`.

| Gate | Result |
|---|---|
| Gate 0 — Parse integrity | **PASS**, all 8 checks |
| Gate 1 — Knockouts | **FAIL**, required-skill row only |
| Gate 2 — Retrieval coverage | **58/100, FAIL**. 3 required tokens at 0 placement points |
| Gate 3 — Human scan | **88/100** |

Gate 0 is clean, so the document itself is sound. The block is content, not
format.

## Artifacts graded

- PDF: `resumes/hunts/2026-09-04/jobgether-senior-fullstack-trading-api/Lucas-Queiroz-Resume-en.pdf`, 26027 bytes, 1 page, letter.
- Source: `Lucas-Queiroz-Resume-en.tex`, same directory.
- Raw extraction: `pdftotext` with no flags. Judged Gate 0 and Gate 2 on it.
- Layout extraction: `pdftotext -layout`. Used for the Gate 0.7 order check.
- Posting: `jobs/jobgether-senior-fullstack-trading-api.md`, LinkedIn job 4461922727.

## Verification performed

### LinkedIn, read live through the `Profile Check` portal, read-only

Read on 2026-09-04 from `linkedin.com/in/queiroz-lucas/details/experience/`
and `/details/education/`. Nothing was edited. Every title and every start and
end month on the PDF matches the live profile exactly.

| Live LinkedIn | On the CV | Match |
|---|---|---|
| `Senior Software Engineer`, `DexCare · Full-time`, `Mar 2026 - Present` | `DexCare`, `Senior Software Engineer`, `Mar 2026 - Present` | YES |
| `Mid-level Software Engineer`, `Luizalabs · Full-time`, `Jan 2024 - Mar 2026` | `Luizalabs`, `Mid-level Software Engineer`, `Jan 2024 - Mar 2026` | YES |
| `Lippaus Distribuidora`, `Mid-level Software Engineer`, `Jan 2023 - Jan 2024` | `Lippaus Distribuidora`, `Mid-level Software Engineer`, `Jan 2023 - Jan 2024` | YES |
| `Lippaus Distribuidora`, `Entry-level Fullstack Software Engineer`, `Mar 2021 - Jan 2023` | same | YES |
| `FAESA`, `Bachelor's degree , Information Systems`, `Feb 2022 – Dec 2025` | `FAESA`, `Bachelor's degree, Information Systems`, `Feb 2022 - Dec 2025` | YES. The separator is the ASCII hyphen required by CV-SPEC; the months are identical. CLAUDE.md rule 1 governs the period, not the glyph. |

The two Lippaus roles stay separate on the CV, so the promotion is preserved.

### Identity facts against the local sources

| Fact | Printed | Source | Result |
|---|---|---|---|
| Degree | `Bachelor's degree, Information Systems`, `FAESA` | DOSSIER.md, live LinkedIn | OK |
| Location | `Vitória, ES, Brazil` | CLAUDE.md rule 3 | OK, nothing more printed |
| UTC offset / time-zone overlap | absent | CLAUDE.md rule 3 | OK |
| Role locations | DexCare `Remote`, Luizalabs `Remote`, both Lippaus roles `Vitória, ES, Brazil` | CLAUDE.md rule 3 | OK |
| Contract detail | absent from the CV | CLAUDE.md rule 3, context only | OK |
| Employer cities Seattle and São Paulo | absent | DOSSIER.md role-locations rule | OK |

### Metrics, each traced to a DOSSIER.md entry

| Number on the CV | DOSSIER id | Result |
|---|---|---|
| 15% fewer wrong bookings | D2 | matches |
| 25% less authentication friction | D3 | matches |
| 7% lower release risk | D5 | matches |
| 20% better invoice throughput | L2 | matches |
| 26% more processing capacity | P2 | matches |

No number appears on the CV that DOSSIER.md does not record. Nothing rounded,
nothing inflated.

### Forbidden-token rule, CLAUDE.md rule 2

0 occurrences of `Ruby`, `Rails`, `Sidekiq`, `ActiveRecord`, or `RSpec` in the
raw extraction, case sensitive and case insensitive. The Rails-world
substitutions are applied correctly: `BullMQ` carries the queue work at
Luizalabs and Lippaus, `Drizzle ORM` carries the data-mapping work at DexCare.

### One-page PDF extraction check

`pdfinfo` reports `Pages: 1`, `612 x 792 pts (letter)`. The raw extraction is
57 non-empty lines and reads cleanly top to bottom. Raw and layout order agree
on every adjacent block. `pdfimages -list` returns an empty table, so there is
no image of text and no icon. Ligature probe passes: `back-office` and
`workflows` both survive extraction, which the four retired PDFs in
`~/Documents/Resumes/` do not do. Those four were treated as invalid and were
not opened.

## What blocks the application

Three required posting skills, each worth 9 weighted Gate 2 points.

1. **`Golang`.** A spelling defect, not a missing fact. The posting writes
   `Golang` three times and never writes `Go` alone. The CV writes `Go` in
   `Skills` and in the Luizalabs bullet. The capability is evidenced, including
   a `Go (Programming Language)` skill tag on the live Luizalabs entry. Per
   ATS-KNOWLEDGE 4.2, alias expansion may never be relied on, so `Go` does not
   answer a `Golang` query. **The Architect can fix this now with no new fact.**

2. **`HTML`.** A missing fact. `DOSSIER.md` records no HTML claim. **Escalate
   to Lucas.** Do not add it on inference from React.

3. **A modern CSS framework, `TailwindCSS` or comparable.** A missing fact.
   `DOSSIER.md` records no CSS framework. The CV's bare `CSS` is the language,
   not a framework. **Escalate to Lucas.** This is an alternatives requirement,
   so one confirmed framework closes it.

Gate 1 cannot reach PASS on defect 1 alone. Defects 2 and 3 need an answer
from Lucas before any re-gate.

## Exact fix list for the Resume Architect

Blocking, in priority order.

1. Put the token `Golang` in `Skills` under `Languages`, and in the Luizalabs
   bullet that currently reads `by building distributed tax microservices in
   Node.js and Go.` Keep the Go/Golang family at 3 occurrences or fewer.
2. Hold for Lucas: `HTML`. If confirmed, place it in `Skills` under `Frontend`
   and in one Experience bullet.
3. Hold for Lucas: one modern CSS framework. If confirmed, place it in `Skills`
   under `Frontend` and in one Experience bullet.

Non-blocking, cheap, do them in the same pass.

4. Spell `Google Cloud Platform` out once, keeping `GCP`. Worth 3 weighted
   Gate 2 points, costs no line.
5. Swap DexCare bullets 2 and 4, so the `SQL` and `PostgreSQL` bullet reaches
   the first three lines of the current role and the Epic EMR bullet moves
   down. Worth up to 7 Gate 3 points. Order only, no text change.
6. Hold for Lucas: the word `startup` in the Lippaus bullet. His own live
   LinkedIn text calls Lippaus a "Fast-growing startup", so the evidence is
   candidate-authored, but `DOSSIER.md` does not record it.

There is white space at the foot of the page. Every fix above fits without a
second page.

## Match limits that no edit can close

- Knowledge of financial markets: no support.
- Fintech experience: no support.
- Algorithmic trading: no support.
- Golang **depth**. The posting asks for "Strong professional experience with
  Golang". The evidenced use is a single Luizalabs bullet. Fixing the spelling
  fixes the token, not the depth.

The Luizalabs SEFAZ and electronic-invoicing domain is tax and e-commerce
compliance. It is not trading, market data, or fintech, and it must not be
presented as any of them.

## Scope note

No file was edited except this report and
`reports/jobgether-senior-fullstack-trading-api-gate.md`. The CV was not
touched. No subagent was spawned. No Maestri message was sent. The LinkedIn
portal was used read-only.
