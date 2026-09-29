# ATS Rubric v4

Two parts, in pipeline order (Lucas, 2026-09-29):

1. **Posting Analysis**, before the build. Sieve reads the posting and writes
   the spec. The go/no-go decision happens here, so no CV is built for a
   posting that fails.
2. **CV Verification**, after the build. `scripts/resume_gate.py` checks the
   CV against the base CV and the spec. No LLM review runs after the build.

This is **our rubric, not a simulation of any vendor's proprietary score.**
Never present these numbers as coming from an ATS. Rules trace to
`ATS-KNOWLEDGE.v2.md`.

---

# Part 1. Posting Analysis (Sieve, before the build)

## Inputs

1. The posting, as raw text, saved to `~/career/jobs/<slug>.md`.
2. The `ats_profile` detected at intake (`ATS-KNOWLEDGE.v2.md` section 3).
   `generic` when no pattern matched.
3. The **Skills policy** in `DOSSIER.md`: attested umbrella, blacklist, gray
   zone, whitelist.
4. The base CV for the posting language, `resumes/base-<lang>.tex`, and the
   role domains in `CLAUDE.md` section 4.1.

## Step 1. Role Eligibility (blocking)

Extract these from the posting. Do not infer them. If the posting is silent,
mark `not stated`, never `pass`.

| Check | Result |
|---|---|
| Work authorization / entity type | PASS / FAIL / not stated |
| Location or time-zone overlap | PASS / FAIL / not stated |
| Minimum years of experience | PASS / FAIL / not stated |
| English proficiency requirement | PASS / FAIL / not stated |
| Degree requirement | PASS / FAIL / not stated |

Judge against `DOSSIER.md`. Technical tokens are not judged here. For each
FAIL, give the exact posting sentence, the evidence checked, and the fix type:
`LUCAS CONFIRMATION` when the DOSSIER is silent, `ROLE MISMATCH` when verified
facts contradict the requirement. Never convert silence into a claim that
Lucas lacks experience.

## Step 2. Tokens

Extract every hard requirement. Classify it as `required` or `preferred`
from the posting's own words. Discard soft skills and buzzwords.

Resolve each token with the Skills policy (`CLAUDE.md` section 4.1):

| Result | Source | Goes to |
|---|---|---|
| `CLAIM` | umbrella or whitelist | `required_tokens` / `preferred_tokens` |
| `GAP` | blacklist | `gap_tokens` / `preferred_gap_tokens` |
| `ASK` | gray zone, no whitelist entry | `ask_tokens` and the gap lists: a question for Lucas, `GAP` until he answers |

## Step 3. Spec

For each `CLAIM` token, write:

- **Anchor.** The role whose domain fits best (fiscal and invoicing at
  Luizalabs, healthcare scheduling at DexCare, orders and distribution at
  Lippaus). Use the company name exactly as the base CV prints it. Skip the
  anchor when the base CV already has the token in an Experience bullet.
- **Stack depth.** Umbrella building blocks that go in Skills next to a
  high-level token (NestJS: Express, Fastify). Only for tokens the posting
  asks.

## Step 4. Projected coverage

Quill places every `CLAIM` token in Skills and in one bullet, so each earns 3
points. Coverage is known before the build:

```
required_coverage = 100 * required_CLAIM / (required_CLAIM + required_GAP)
```

`ASK` tokens count as `GAP` until Lucas answers.

## Step 5. ATS profile and form pack

Apply the adjustments of the detected profile (`ATS-KNOWLEDGE.v2.md`
section 4) as build instructions:

| Profile | Instruction to Quill |
|---|---|
| `ashby`, `workday`, `workable`, criteria profiles | One explicit sentence per required `CLAIM` token that a model can quote |
| `greenhouse` | Domain or industry word in each role line or first bullet |
| `workday` | Total years stated and supported by dates |
| `linkedin-easy-apply` | List required `CLAIM` tokens missing from the cached LinkedIn Skills. Lucas edits the profile; agents never do |
| `gupy` | No build. Coverage against the master Gupy profile, then the form pack |

Write the form pack: every screening question the posting or form shows, with
a true answer from the DOSSIER, or `LUCAS CONFIRMATION`.

## Step 6. Verdict

| Verdict | Condition | Next action |
|---|---|---|
| `NO-GO` | Role Eligibility `ROLE MISMATCH`, or projected coverage below 70 with no `ASK` that could lift it | Abandon. No build |
| `NO-GO` | `workable` and a must-have required token is `GAP` | Report to Lucas. No build |
| `ASK` | An `ASK` token or `LUCAS CONFIRMATION` decides the verdict | Maestro asks Lucas, in one batch per hunt |
| `GO` | Everything else | Build |

## Outputs

1. `state/<application>-manifest.json`, the spec:

```json
{
  "application_id": "<slug>",
  "language": "en",
  "ats_profile": "ashby",
  "required_tokens": ["NestJS", "SQS"],
  "preferred_tokens": ["GraphQL"],
  "gap_tokens": [],
  "preferred_gap_tokens": [],
  "ask_tokens": [],
  "anchors": {"NestJS": "Luizalabs", "SQS": "Luizalabs"},
  "stack_depth_tokens": ["Express", "Fastify"],
  "build_instructions": ["One quotable sentence per required token"],
  "projected_required_coverage": 100,
  "verdict": "GO"
}
```

2. `reports/<application>-analysis.md`: the verdict, the Role Eligibility
   table, the token table (token, required or preferred, result, policy line,
   anchor), projected coverage, and the form pack. No preamble.

---

# Part 2. CV Verification (script, after the build)

`scripts/resume_gate.py` runs on the built CV. Exit `0` PASS, `1` FAIL, `2`
could not run. A FAIL goes back to Quill with the failure list. Two rounds
maximum, then escalate to Lucas.

| Check | FAIL condition |
|---|---|
| `pdf_extraction` | PDF text is empty |
| `sections` | A section header of the CV language is missing |
| `contact` | Email, city, LinkedIn, or GitHub missing from the PDF text |
| `layout` | Preamble differs from the base CV |
| `roles` | Company, title, dates, or location differ from the base CV |
| `linkedin_identity` | A role field is not in the cached LinkedIn snapshot |
| `experience_completeness` | A base bullet or metric was removed |
| `forbidden_terms` | Ruby, Rails, or a time-zone statement |
| `claim_allowlist` | A protected claim introduced without approval |
| `required_token_placement` | A required `CLAIM` token is not in Skills and in Experience |
| `spec_placement` | An anchored token is not in its role, or a stack-depth token is not in Skills |
| `blacklist` | A DOSSIER blacklist token was added |
| `gap_tokens_written` | A `GAP` token was written |
| `required_coverage` | Below 70 |

File Readability items that the script does not test (segmentation, reading
order, glyphs, forbidden constructs) are properties of the base layout. The
`layout` and `roles` checks lock them, so they are verified once per base CV
change, in the base round.

## Base round (only when a base CV changes)

Sieve runs the full File Readability Check on the base PDF:

```
pdftotext -layout base.pdf - > extracted-layout.txt
pdftotext          base.pdf - > extracted-raw.txt
```

| # | Check | FAIL condition |
|---|---|---|
| 0.1 | Text layer exists | Raw extraction is empty or garbage |
| 0.2 | Glyph integrity | `\x00`, `?`, or broken fi/fl/ff in `office`, `profile`, `efficient`, `workflow`, `conflict` |
| 0.3 | Contact block recoverable | Email, phone, city, LinkedIn in the body, not a header or footer |
| 0.4 | Section headers verbatim | EN `Summary`, `Skills`, `Language`, `Experience`, `Education`; PT `Resumo`, `Habilidades`, `Idiomas`, `Experiência`, `Formação` |
| 0.5 | Employment-block segmentation | Two roles merged, or one role split, in the raw stream |
| 0.6 | Date parseability | Each role has `Mon YYYY - Mon YYYY` next to its title |
| 0.7 | Reading order | Raw and layout extraction disagree on two adjacent blocks |
| 0.8 | No forbidden constructs | Table, text box, image of text, contact icon, photo |

Recruiter readability is a build rule for Quill (`CV-SPEC.md`): target title
near the top, the three most relevant bullets first in the most recent role,
past-tense XYZ bullets, at least 3 real numbers, no buzzwords, grouped Skills.

## Prohibitions

- Sieve never edits a CV. Quill never grades.
- Never guess a requirement the posting did not state.
- Never put a blacklisted or unanswered gray-zone token in the spec.
- Never claim a vendor produces these numbers.
- Never drop, move, or soften a token for interview risk.
