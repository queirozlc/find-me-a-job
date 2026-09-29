# Quill report — Etho IT Solutions, Full Stack Software Engineer (Agentic Development & MCP Integrations)

Date: 2026-09-04. Hunt: 2026-09-04-b. Language: English. Base: `resumes/base-en.tex`.

## Deliverables

- `resumes/hunts/2026-09-04-b/etho-it-agentic-full-stack/Lucas-Queiroz-Resume-en.tex`
- `resumes/hunts/2026-09-04-b/etho-it-agentic-full-stack/Lucas-Queiroz-Resume-en.pdf` (1 page, 26.7 KiB)
- `resumes/hunts/2026-09-04-b/etho-it-agentic-full-stack/application-message.md`

Base CVs untouched. No ledger or Maestri note edited. Nothing sent, nothing submitted.

## Build and verification

- `tectonic` build: success. Font warnings only.
- `pdfinfo`: Pages 1. All 16 Experience bullets fit with clear spacing. Rendered page inspected visually.
- `pdftotext` raw and `-layout`: contact block intact (`Vitória, ES, Brazil | +55 (27) 99203-0170 | sepulchrolucas@gmail.com | linkedin.com/in/queiroz-lucas | github.com/queirozlc`). No UTC offset.
- Section headers in the text layer: Summary, Skills, Language, Experience, Education. Rendered as small caps; source strings are canonical.
- Employment blocks: DexCare, Luizalabs, Lippaus Distribuidora (Jan 2023 - Jan 2024), Lippaus Distribuidora (Mar 2021 - Jan 2023). Each block extracts as `Company | Title` then `Location | Dates` then bullets. Education block extracts the same way.
- `grep -in 'ruby\|rails\|unverified'` on the .tex and on the raw extraction: zero hits. Note: a first draft used the word `guardrails`, which matched the `rails` grep. Replaced with `enforcement`.
- Ligature check: `grep -c workflow` on raw extraction is 5, non-zero.
- Base comparison: 16 bullets in base, 16 in tailored. Metrics 15%, 25%, 7%, 33%, 20%, 18%, 26% all present. Titles and dates match base and DOSSIER LinkedIn ground truth character for character: 9 of 9 strings present.

## Format change from base

The base `\resumeSubheading` uses `tabular*`. CV-SPEC item 2 and the Resume Architect role file forbid `tabular*`. The tailored file prints the role header as two consecutive left-aligned text lines: `Company | Title`, then `Location | Dates`. Content is identical. Raw extraction now keeps each role as one block with no blank line between title and dates. The Maestro may want to carry this header into the next base round; I did not edit the base.

## Changes from base content

Summary
- `TypeScript, Node.js, React, and Go systems` to `TypeScript/Node, React, and Go systems with production ownership`. Mirrors the posting spelling `TypeScript/Node` once and places `production ownership`.
- `I integrate AI-driven agentic workflows into daily delivery` to `I integrate Claude Code and Codex agentic workflows into daily delivery`. Places `Claude` and `Claude Code` in the Summary.

Skills
- Cloud and operations: added `Containers`.
- New line `Testing and security practices: Test automation | Vitest | Jest | Input validation | Secrets handling`.
- New line `AI tooling: Claude Code | Codex | Agentic workflows | Agent rules and enforcement`. Vitest and Jest moved out of the former combined line. No token removed.

Experience, DexCare
- AI bullet moved to first position and reworded: `Built Claude Code and Codex agent environments with shared agent rules and enforcement (lint, cyclomatic complexity limits, and tests) that enabled agentic workflows to produce high-quality code in daily delivery.` Same facts as the base and the dossier.
- Auth0 bullet: `OpenAPI/Swagger validation` to `OpenAPI/Swagger input validation`. Supported by `express-openapi-validator` in the dossier.
- Data bullet: `wired to S3 and RDS through AWS SDK v3` to `wired to S3, RDS, and Secrets Manager through AWS SDK v3 for storage and secrets handling`. Supported by the dossier AWS SDK v3 list (S3, STS, Secrets Manager, RDS Signer).
- All other DexCare bullets unchanged.

Experience, Luizalabs
- Deployment bullet: `Deployed services with Docker and Kubernetes on GCP through ArgoCD, keeping production reliable with Vitest and Jest suites gating CI/CD` to `Deployed services as containers with Docker and Kubernetes on GCP through ArgoCD, keeping production reliable with Vitest and Jest test automation gating CI/CD`. Places `containers` and `test automation`. Phrase kept on one extracted line.
- Other Luizalabs bullets unchanged.

Experience, Lippaus (both roles) and Education: unchanged.

## Required token placement

| Token | Skills | Experience bullet | Status |
|---|---|---|---|
| TypeScript | Languages | DexCare services bullet | placed (3 total) |
| Node | Node.js in Languages | Luizalabs Node.js bullet; `TypeScript/Node` in Summary | placed |
| React | Frontend | DexCare Datadog RUM bullet | placed (3 total) |
| Claude | inside `Claude Code` | inside `Claude Code` | placed as substring of Claude Code only |
| Claude Code | AI tooling | DexCare AI bullet | placed (3 total with Summary) |
| AWS | Cloud and operations | DexCare data bullet | placed (3 total) |
| GCP | Cloud and operations | Luizalabs deployment bullet | placed |
| containers | Cloud and operations | Luizalabs deployment bullet | placed |
| CI/CD | Cloud and operations | Luizalabs deployment bullet | placed |
| test automation | Testing and security practices | Luizalabs deployment bullet | placed |
| input validation | Testing and security practices | DexCare Auth0 bullet | placed |
| secrets handling | Testing and security practices | DexCare data bullet | placed |
| production ownership | not a Skills token | Summary only | placed in Summary |

## Required tokens not placed (unsupported by DOSSIER.md and base)

- Anthropic Messages API. No dossier fact. Not inferred from Claude Code use, per dispatch.
- MCP, MCP servers, tools, resources. No dossier fact. Not inferred.
- tool use, function calling. No dossier fact.
- prompt engineering, skill engineering. The dossier records "shared rules" for agent environments. I printed `shared agent rules`, not the posting phrases, because the dossier does not use them.
- code review. No dossier fact.
- OWASP. No dossier fact.
- Azure. No dossier fact.
- IaC. No dossier fact. ArgoCD is GitOps deployment, not IaC tooling. Not claimed as IaC.

## Preferred tokens not placed

Multi-agent, planner, executor, critic, human-in-the-loop, LLM evaluation, evals, golden datasets, regression testing, token management, cost management, Jira, Confluence, spec-first. None supported by the dossier as a Lucas claim.

## Knockout coverage

- Remote: role locations print Remote for DexCare and Luizalabs.
- Fluent English: `English: Fluent (C1)` in the Language section.
- Brazil location: contact block prints Vitória, ES, Brazil.
- 6+ years: CV states 5+ years. LinkedIn history starts Mar 2021. Not changed. Flagged in the screening answers.

## Escalations for the Maestro

1. The posting's core requirements (MCP servers, Anthropic Messages API, tool use) have no dossier support. The CV is honest and the recruiter message states the gap. Gate 2 required-token coverage will not be full. This is a dossier gap, not a writing defect. Lucas can add facts to DOSSIER.md if he has them.
2. The 6+ years requirement versus 5+ years on the CV. Not adjusted.
3. Header layout changed from `tabular*` to consecutive lines to satisfy CV-SPEC item 2. Consider a base round if the Maestro wants the bases aligned.
