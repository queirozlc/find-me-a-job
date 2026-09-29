# ATS Analysis — lawnstarter-staff-product-engineer-{en,pt}.pdf vs lawnstarter-staff-product-engineer
Segment: us-direct   Date: 2026-09-01
Posting: https://www.linkedin.com/jobs/view/4459567512/ (captured verbatim in `jobs/lawnstarter-staff-product-engineer.md`)

## Verdict

| Gate | EN | PT |
|---|---|---|
| Gate 0 — Parse integrity | PASS (4 accepted header exceptions) | PASS (4 accepted header exceptions) |
| Gate 1 — Knockouts | PASS (no knockout stated in the posting) | PASS |
| Gate 2 — Retrieval coverage | **38 / 100** | **36 / 100** |
| Gate 3 — Human scan | **91 / 100** | **91 / 100** |

Not blocked. Gate 2 is the failure surface. The posting is dense in
staff-level process tokens (`evals`, `prompts`, `guardrails`, `rollout`,
`rollback`, `runbooks`, `architecture`, `metric`, `marketplace`,
`documented`) and the CV carries almost none of them.

### Extraction basis

Both PDFs re-extracted with `pdftotext` and `pdftotext -layout` before any
judgement. The regenerated raw files are byte-identical to the committed
`*.raw.txt` files. Gate 0 and Gate 2 are judged on the raw extraction.

---

## Gate 0 — Parse integrity

| # | Check | EN | PT | Evidence |
|---|---|---|---|---|
| 0.1 | Text layer exists | PASS | PASS | Full raw extraction recovered, 1 page each |
| 0.2 | Glyph integrity | PASS | PASS | EN: `workflows` x4, `office` x2, `configuration`, `flags`, `isolated` all intact. PT: `workflows` x2, `backoffice` x2, `fiscais` x3, `notificações` intact. No U+FB00-FB06, no NUL |
| 0.3 | Contact block recoverable | PASS | PASS | Line 3 of raw, in the body (`\pagestyle{empty}`, `\begin{center}`): city, phone, email, LinkedIn, GitHub |
| 0.4 | Section headers verbatim | PASS | PASS | EN `SUMMARY` / `SKILLS` / `EXPERIENCE` / `EDUCATION`; PT `RESUMO` / `HABILIDADES` / `EXPERIÊNCIA` / `FORMAÇÃO`. Standalone lines, uppercase rendering, allowed case-insensitive |
| 0.5 | Employment-block segmentation | FAIL — **accepted, not blocking** | FAIL — **accepted, not blocking** | Raw splits every role header into `Company` / `Title` / blank / `Dates` / `Remote`. Sole cause is the `tabular*` role header. CV-SPEC item 2 + RUBRIC exception, Lucas 2026-09-01. All four roles remain individually recoverable with correct title and dates |
| 0.6 | Date parseability | FAIL — **accepted, not blocking** | FAIL — **accepted, not blocking** | Dates are separated from the title by a blank line in raw, same `tabular*` cause. Every date string is itself well formed `Mon YYYY - Mon YYYY`, ASCII hyphen |
| 0.7 | Reading order | FAIL — **accepted, not blocking** | FAIL — **accepted, not blocking** | Raw and layout disagree only inside the role header (raw: Company, Title, Dates, Location; layout: Company+Dates, Title+Location). Section order and role order agree exactly |
| 0.8 | No forbidden constructs | FAIL — **accepted, not blocking** | FAIL — **accepted, not blocking** | `tabular*` at `.tex:41`, role header only. No text box, no image of text, no icon, no photo |

**No other cause of 0.5-0.8 exists.** Under the CV-SPEC item 2 / RUBRIC
exception these four are reported, not blocking.

### LinkedIn ground-truth check (any mismatch would be a Gate 0 FAIL)

| DOSSIER LinkedIn ground truth | EN PDF | PT PDF | Result |
|---|---|---|---|
| `Senior Software Engineer` · `DexCare` · `Jan 2026 - Present` | identical | identical | MATCH |
| `Mid-level Software Engineer` · `Luizalabs` · `Jan 2024 - Jan 2026` | identical | identical | MATCH |
| `Mid-level Software Engineer` · `Lippaus Distribuidora` · `Jan 2023 - Jan 2024` | identical | identical | MATCH |
| `Entry-level Fullstack Software Engineer` · `Lippaus Distribuidora` · `Mar 2021 - Jan 2023` | identical | identical | MATCH |
| `FAESA` · Information Systems · `Feb 2022 – Dec 2025` | `Feb 2022 - Dec 2025` | `Feb 2022 - Dec 2025` | MATCH (ASCII hyphen per CV-SPEC item 5; the LinkedIn EN DASH is a glyph difference, not a period difference) |

Company spelling `Luizalabs` correct. Both Lippaus roles kept separate. The PT
CV keeps all four job titles in English and keeps `Present` in English, which
is what CLAUDE.md rule 1 requires. **No Gate 0 FAIL from titles or dates.**

### Forbidden-token grep

`grep -rniE 'ruby|rails|unverified'` on `lawnstarter-staff-product-engineer-en.tex`,
`lawnstarter-staff-product-engineer-pt.tex` and both raw extractions:
**zero hits in all four files.**

### Page count

`pdfinfo`: EN 1 page, PT 1 page. Confirmed.

### Source-to-artifact drift (defect, outside the 8 checks)

The shipped PDFs cannot be reproduced from the `.tex` files. Both Summaries
differ:

- `en.tex:62` reads `measurable product outcomes`; the EN PDF reads
  `measurable production outcomes`.
- `pt.tex:62` reads `resultados de produto mensuráveis`; the PT PDF reads
  `resultados mensuráveis em produção`.

Every bullet and every role-header field matches the PDF exactly; only the
Summary drifts. Consequence: the token `product` is absent from both shipped
PDFs, and `product` is the word in the posting title.

---

## Gate 1 — Knockouts

Extracted from the posting text only.

| Check | Posting says | Result |
|---|---|---|
| Work authorization / entity type | Nothing. "Work from anywhere" | not stated |
| Location or time-zone overlap | Location label `Belo Horizonte, Minas Gerais, Brazil (Remote)`; benefit line "Work from anywhere". No overlap window stated | not stated |
| Minimum years of experience | Nothing | not stated |
| English proficiency | Nothing | not stated |
| Degree requirement | Nothing | not stated |
| Required skills | "You need deep skill in at least one of our stacks plus credible production experience with AI coding agents" | see below |

| Required skill | Present verbatim in raw? |
|---|---|
| Deep skill in at least one stack: `TypeScript` / `React` / `React Native` (or `PHP`/`Laravel`) | PASS — `TypeScript`, `React`, `React Native` all verbatim, all in Experience in context |
| Credible production experience with AI coding agents | PASS — `AI coding agents`, `Claude Code`, `Codex`, "daily production work", DexCare bullet 1 |
| AI-native, agents used daily on production work | PASS — Summary and DexCare bullet 1 |
| Operating at a lead level ("whatever your current title") | WEAK — only `leading` inside "leading project scoping" (Lippaus, Jan 2023 - Jan 2024). No lead-level evidence in the current role. Not a FAIL, because the posting states no title requirement |

**Gate 1 verdict: PASS.** The posting states no knockout. Time-zone overlap
and English are not gated by this posting, so their presence in the Summary is
optional here, not required.

---

## Gate 2 — Retrieval coverage: EN 38 / 100, PT 36 / 100

### Scoring notes, stated so the number is reproducible

1. The RUBRIC formula `100 * sum(points_earned) / sum(4 * weight)` cannot reach
   100 if the numerator is unweighted. It is read here as
   `100 * sum(points * weight) / sum(4 * weight)`. Required weight 3,
   preferred weight 1.
2. The RUBRIC placement ladder is anchored on the `Skills` section, which
   models technology tokens only. This posting's required tokens are mostly
   concept tokens (`rollout`, `runbooks`, `metric`) that no resume puts in
   `Skills`. Those are scored on a stated parallel ladder:
   absent 0, synonym or substring only 1, verbatim in an Experience bullet in
   context 3, also in Summary 4. **This is my interpretation, not a RUBRIC
   rule.** The RUBRIC does not cover concept tokens.
3. `Cursor` and `PHP/Laravel` are classified `preferred`, not `required`,
   because the posting writes "Claude Code, Cursor, Codex, **or equivalent**"
   and "at least one of our stacks". The alternates are satisfied.

### Required tokens, weight 3 (EN)

| # | Token | Skills | Experience | Summary | Points |
|---|---|---|---|---|---|
| 1 | `Claude Code` | yes | yes, DexCare b1 | yes | 4 |
| 2 | `Codex` | yes | yes, DexCare b1 | yes | 4 |
| 3 | `AI coding agents` | `AI agents` label | yes, verbatim, DexCare b1 | `AI-native` only | 3 |
| 4 | `TypeScript` | yes | yes, DexCare b4 | yes | 4 |
| 5 | `React` | substring of `React Native` only | yes, verbatim, DexCare b3 | no | 3 |
| 6 | `React Native` | yes | yes, Lippaus mid b2 | no | 3 |
| 7 | `production` | n/a | yes, "daily production work", "production-ready" | yes, "production outcomes" | 4 |
| 8 | `agent workflows` | `Agentic workflows` | yes, verbatim, DexCare b1 | no | 3 |
| 9 | `evals` | no | no | no | **0** |
| 10 | `prompts` | no | no | no | **0** |
| 11 | `guardrails` | no | paraphrase: lint, cyclomatic complexity limits, tests | no | 1 |
| 12 | `tests` | `Vitest`, `Jest` | yes, verbatim, DexCare b1 | no | 3 |
| 13 | `observability` | yes, group label | yes, DexCare b3 | no | 3 |
| 14 | `architecture` | no | paraphrase: "event-driven", "distributed tax microservices" | no | 1 |
| 15 | `data model` | no | "modeling data in PostgreSQL", not the token | no | 1 |
| 16 | `rollout` | no | flags behind LaunchDarkly/OpenFeature | no | 1 |
| 17 | `rollback` | no | no | no | **0** |
| 18 | `security` | no | Auth0 JWT, tenant isolation, secrets | no | 1 |
| 19 | `performance` | no | "throughput", "processing capacity" | no | 1 |
| 20 | `runbooks` | no | "reusable ... agent workflows" | no | 1 |
| 21 | `metric` | no | no | "measurable ... outcomes" | 1 |
| 22 | `documented` / `documentation` | no | no | no | **0** |
| 23 | `marketplace` | no | `e-commerce` only | no | **0** |
| 24 | `staff` / `lead` | no | `leading`, substring, 3rd role | no | 1 |
| 25 | PM / designer partnership | no | "stakeholder communication" | no | 1 |
| 26 | post-launch review | no | no | no | **0** |

Required points earned: **44** of a possible 104.

### Preferred tokens, weight 1 (EN)

| Token | Points | Note |
|---|---|---|
| `AWS` | 4 | Skills, DexCare b6, Summary |
| `Datadog` | 3 | Skills, DexCare b3 |
| `Cursor` | 0 | not in DOSSIER |
| `PHP` / `Laravel` | 0 | documented gap |
| `MCP servers` | 0 | not in DOSSIER |
| `Redshift` | 0 | documented gap |
| `dbt` | 0 | documented gap |
| `Segment` | 0 | not in DOSSIER |
| `Airflow` | 0 | documented gap |
| `Sentry` | 0 | documented gap |
| `GitHub Actions` | 0 | CV has generic `CI/CD` only |
| `Confluence` | 0 | not in DOSSIER |
| `Jira` | 0 | not in DOSSIER |

Preferred points earned: **7** of a possible 52.

### Calculation

```
numerator   = 3 * 44 + 1 * 7 = 139
denominator = 4 * (3 * 26) + 4 * (1 * 13) = 312 + 52 = 364
coverage    = 100 * 139 / 364 = 38.2  ->  38 / 100
```

Stuffing penalty: **0**. No token appears 4 or more times. Every `Skills`
technology token has supporting evidence in an `Experience` bullet, including
`Go` (Luizalabs), `JavaScript` (Lippaus entry), `Vitest` and `Jest`
(Luizalabs), `Express` and `Koa` (DexCare b4).

### PT differences

Same table, two rows lower, because the PT prose translates the words:

| Token | EN | PT | Cause |
|---|---|---|---|
| `production` | 4 | 3 | PT Summary says `em produção`; only `production-ready` in the bullet carries the English token |
| `tests` | 3 | 1 | PT says `testes` |

```
PT numerator = 3 * 41 + 1 * 7 = 130
PT coverage  = 100 * 130 / 364 = 35.7  ->  36 / 100
```

### Required tokens not covered

Zero points, verbatim absent from both PDFs:

1. `evals`
2. `prompts`
3. `rollback`
4. `documented` / `documentation`
5. `marketplace`
6. post-launch review / "did it work" review

Scored 1, term absent, substance present:

7. `guardrails`
8. `architecture` / `architectural`
9. `data model`
10. `rollout`
11. `security`
12. `performance`
13. `runbooks`
14. `metric`
15. `staff` / lead-level operation
16. PM and designer partnership

Preferred tokens not covered: `Cursor`, `PHP`, `Laravel`, `MCP servers`,
`Redshift`, `dbt`, `Segment`, `Airflow`, `Sentry`, `GitHub Actions`,
`Confluence`, `Jira`.

Also absent and worth naming separately: **`product`**. The posting title is
`Staff Software Engineer, Product`; the posting says "Product Engineer", "true
product partner", "a product-engineering role". The EN PDF contains only
`production` and `production-ready`. The `.tex` already says
`product outcomes`; a rebuild recovers this token.

---

## Gate 3 — Human scan: EN 91 / 100, PT 91 / 100

| # | Check | Points | Result |
|---|---|---|---|
| 3.1 | Target title in the top 15% | 8 / 15 | `Senior Software Engineer` sits at raw line 6, inside the top 15%. The target title `Staff Software Engineer, Product` does not appear, and `Product` does not appear at all. The title itself is fixed by DOSSIER (Lucas 2026-09-01: CV title stays `Senior Software Engineer`), so only the `Product` half is fixable |
| 3.2 | 3 most relevant bullets first, in the most recent role | 20 / 20 | DexCare b1 AI agents / Claude Code / Codex, b2 15% wrong bookings, b3 7% release risk with React, observability and Datadog. Correct ordering for this posting |
| 3.3 | Every bullet leads with an outcome or action verb | 13 / 15 | All 16 bullets lead with a bare action verb. No "Responsible for". Deduction: four of the seven DexCare bullets lead with `Reduce`, which reads as a template on a fast scan |
| 3.4 | At least 3 bullets carry a real number | 15 / 15 | Seven: 15%, 7%, 25%, 33%, 20%, 18%, 26%. All traced to DOSSIER metrics D2, D5, D3, D7, L2, L3, P2 |
| 3.5 | Length: 1 page under 10 years | 10 / 10 | `pdfinfo` confirms 1 page, both languages |
| 3.6 | No unsupported buzzwords | 10 / 10 | `AI-native` and `outcome-driven` both appear, both are the posting's own words, and both are supported by evidence in Experience. No "team player", "results-driven", "passionate" |
| 3.7 | Skills grouped by category | 10 / 10 | Four labelled groups: AI agents and quality, Languages and frontend, Backend and data, Cloud and observability |
| 3.8 | Scannable | 5 / 5 | Consistent role headers, bold company, italic title, uniform inter-role gap, one page |

PT scores identically. The PT DexCare block repeats `Reduz` four times, the
same 3.3 deduction.

---

## Fix list for the Resume Architect

19 items. `[DOSSIER-OK]` means the fix is a rewording over facts already in
`DOSSIER.md`. `[BLOCKED]` means it needs a new fact from Lucas and must not be
written until he supplies it.

| # | File | Line | Defect | What would pass |
|---|---|---|---|---|
| 1 | `lawnstarter-staff-product-engineer-en.tex` `-pt.tex` | 62 | Shipped PDFs do not match their source. EN PDF says `production outcomes`, `.tex` says `product outcomes`. PT PDF says `resultados mensuráveis em produção`, `.tex` says `resultados de produto mensuráveis` | Rebuild both with tectonic and re-extract. Re-run every Gate 0 check on the new extraction. `[DOSSIER-OK]` |
| 2 | `-en.tex` | 62 | Token `product` absent from the shipped PDF. Posting title is `Staff Software Engineer, Product` | Item 1 alone recovers `product outcomes`. Stronger: name `product engineering` once in the Summary. `[DOSSIER-OK]` |
| 3 | `-en.tex` `-pt.tex` | 67 | `React` is only a substring of `React Native` in `Skills`. A recruiter boolean on `"React"` still hits, but the canonical token is not listed | List `React` as its own token beside `React Native`. React at DexCare is a DOSSIER observed fact. `[DOSSIER-OK]` |
| 4 | `-en.tex` `-pt.tex` | 81 | `architecture` absent. Bullet describes event-driven services without naming the architecture | Reword to name `event-driven architecture`. No new claim. `[DOSSIER-OK]` |
| 5 | `-en.tex` `-pt.tex` | 83 | `data model` absent. Bullet says "modeling data in PostgreSQL" | Reword to `data model` / `data modeling`. `[DOSSIER-OK]` |
| 6 | `-en.tex` `-pt.tex` | 80 | `rollout` absent. Bullet describes flag-gated releases | Reword to name a `controlled rollout` behind LaunchDarkly/OpenFeature flags. `[DOSSIER-OK]` |
| 7 | `-en.tex` `-pt.tex` | 82 | `security` absent. Bullet carries Auth0 JWT, tenant isolation, secrets | Name `security` once in that bullet. `[DOSSIER-OK]` |
| 8 | `-en.tex` `-pt.tex` | 92 or 103 | `performance` absent. Bullets carry 20% throughput and 26% capacity | Name `performance` once. `[DOSSIER-OK]` |
| 9 | `-en.tex` `-pt.tex` | 78 | `guardrails` absent. Bullet already lists shared rules, lint, cyclomatic complexity limits, tests | Call that set `guardrails`. Naming choice over existing facts. `[DOSSIER-OK]` |
| 10 | `-en.tex` `-pt.tex` | 62 | `metric` absent. Summary says "measurable ... outcomes" | Use `metric` once in the Summary. `[DOSSIER-OK]` |
| 11 | `-en.tex` `-pt.tex` | 78 | `evals` absent. This is the posting's single most-repeated craft token ("evals that catch issues before merge") | **`[BLOCKED]`** DOSSIER records shared rules, lint, complexity limits and tests, not evals. Ask Lucas whether he built agent evals at DexCare |
| 12 | `-en.tex` `-pt.tex` | 78 | `prompts` absent. Posting: "prompts that encode our conventions" | **`[BLOCKED]`** DOSSIER says "shared rules", not prompts. Ask Lucas whether he authored agent prompts or Claude Code skills |
| 13 | `-en.tex` `-pt.tex` | 78 | `runbooks` absent | **`[BLOCKED]`** No DOSSIER fact. Ask Lucas |
| 14 | `-en.tex` `-pt.tex` | 80 | `rollback` absent. Feature flags imply reversibility but a rollback strategy is a separate claim | **`[BLOCKED]`** Ask Lucas whether he owned rollback strategy |
| 15 | `-en.tex` `-pt.tex` | 62 | `documented` / `documentation` absent. Posting: "Decisive and documented" | **`[BLOCKED]`** No DOSSIER fact on written architecture decisions |
| 16 | `-en.tex` `-pt.tex` | 78 or 84 | No lead-level evidence in the current role. Only `leading` in the Lippaus 2023-2024 bullet. Posting requires "operating at a lead level" | **`[BLOCKED]`** Ask Lucas for a defensible lead-level fact at DexCare, for example whether he led SPI or the agent-environment work rather than helped |
| 17 | `-en.tex` `-pt.tex` | 62, 101 | PM and designer partnership absent. Posting requires "a strong horizontal partner" | **`[BLOCKED]`** DOSSIER has "stakeholder communication" at Lippaus only. Ask Lucas about PM and designer partnership at DexCare |
| 18 | `-en.tex` `-pt.tex` | 78-84 | Four of seven DexCare bullets lead with `Reduce` / `Reduz`. Gate 3.3 deduction | Vary the leading verbs while keeping the outcome first. `[DOSSIER-OK]` |
| 19 | `-pt.tex` | 78, 94 | PT Gate 2 is 2 points below EN because `tests` becomes `testes` and `production` becomes `produção` | Accept as correct Portuguese. Report only, no change recommended, unless Lucas wants the PT CV to carry English retrieval tokens |

Not fixable at all, and not defects: `Cursor`, `MCP servers`, `GitHub Actions`,
`Segment`, `Confluence`, `Jira`, `PHP`, `Laravel`, `Redshift`, `dbt`,
`Airflow`, `Sentry`. No DOSSIER fact supports any of them. Do not write them.

---

## Claims I could not verify

Two shipped claims do not trace to `DOSSIER.md`, and neither carries an inline
`[UNVERIFIED]` marker, which CLAUDE.md rule 4 requires. Lucas decides.

1. **"beverage distribution startup"** — `en.tex:111`, `pt.tex:111`
   ("startup de distribuição de bebidas"). DOSSIER names the employer
   `Lippaus Distribuidora` and its stack, and records no industry. Beverages
   are not stated anywhere in DOSSIER.
2. **"Supported nationwide retailer expansion"** — `en.tex:102`, `pt.tex:102`.
   DOSSIER confirms "multi-tenant web and mobile platform on PostgreSQL". It
   records no nationwide scope and no retailer customer base.

Weaker, flagged for completeness:

3. **"real-time"** in the DexCare booking bullet, `en.tex:81`, `pt.tex:81`.
   DOSSIER records "event-driven booking, healthcare scheduling at scale" and
   the `visit-booking` and `forq-availability` services. It does not record a
   real-time latency claim.
4. **"US teams and US-hours overlap"** in the Summary, `en.tex:62`,
   `pt.tex:62`. The English and US-team facts are in DOSSIER
   ("Daily English-only work with US teams at DexCare"). The hours-overlap
   claim is an inference from GMT-3, not a DOSSIER fact. Separately, DOSSIER
   carries a style rule: "Do not print 'Works remotely from Brazil with US-based
   teams' or any equivalent sentence." Whether this Summary clause is an
   equivalent sentence is Lucas's call, not mine. The posting does not gate on
   time zone, so removing the clause would cost nothing at Gate 1.

`grep -rn UNVERIFIED` on both `.tex` files and both raw extractions: zero hits.
