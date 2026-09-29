# ATS Analyzer Rubric v3

Owned by the ATS Analyzer. Deterministic, reproducible, and honest about what
it is: **our rubric, not a simulation of any vendor's proprietary score.**
Never present these numbers as coming from an ATS.

Read `~/career/ATS-KNOWLEDGE.md` first. Every rule here traces to it.

---

## Inputs

1. The resume file, as a file on disk. Not pasted text. The file is the
   artifact under test.
2. The job description, as raw text, saved to `~/career/jobs/<slug>.md`.
3. The target segment: `us-direct`, `br-pj`, or `agency`.

## Mandatory extraction step

Do this before any judgement. Reasoning over the source document instead of
the extracted text is the single way this analysis becomes worthless.

```
pdftotext -layout resume.pdf - > extracted-layout.txt   # human reading order
pdftotext          resume.pdf - > extracted-raw.txt     # parser reading order
```

`extracted-raw.txt` is the closest available approximation of what a parser
receives after text extraction. **Judge the File Readability Check and Resume
Evidence Check on the raw file.**
If the two files disagree about ordering, the layout is unsafe.

For DOCX use `python-docx`, or unzip and read `word/document.xml`.

---

## File Readability Check (binary, blocking)

Any FAIL here stops the analysis. Report it and nothing else. There is no
point scoring a document that does not survive extraction.

| # | Check | FAIL condition |
|---|---|---|
| 0.1 | Text layer exists | Raw extraction is empty or garbage |
| 0.2 | Glyph integrity | Any `\x00`, `?`, or missing fi/fl/ff. Grep the raw text for `office`, `profile`, `efficient`, `workflow`, `conflict` and confirm they are intact |
| 0.3 | Contact block recoverable | Email, phone, city, LinkedIn URL all present in raw text, in the body, not a header or footer |
| 0.4 | Section headers present verbatim | EN: `Summary`, `Skills`, `Language`, `Experience`, `Education`. PT (`-pt` files): `Resumo`, `Habilidades`, `Idiomas`, `Experiência`, `Formação`. Recoverable as standalone lines, case-insensitive (uppercase rendering is allowed) |
| 0.5 | **Employment-block segmentation** | Any two roles merged into one block, or one role split into two, in the raw stream. Highest-value check in this rubric |
| 0.6 | Date parseability | Every role has `Mon YYYY - Mon YYYY` on the same line as, or adjacent to, its title |
| 0.7 | Reading order | Raw and layout extraction disagree on the order of any two adjacent content blocks |
| 0.8 | No forbidden constructs | Table, text box, image of text, contact icon, photo |

Output: a table of 8 rows, PASS or FAIL, and for each FAIL the exact offending
text from the extraction.

---

## Role Eligibility Check (binary, blocking)

Extract these from the job description. Do not infer them. If the posting is
silent, mark `not stated`, never `pass`.

| Check | Source | Result |
|---|---|---|
| Work authorization / entity type | posting | PASS / FAIL / not stated |
| Location or time-zone overlap | posting | PASS / FAIL / not stated |
| Minimum years of experience | posting | PASS / FAIL / not stated |
| English proficiency requirement | posting | PASS / FAIL / not stated |
| Each required skill | posting | present verbatim in resume? |
| Degree requirement | posting | PASS / FAIL / not stated |

For every explicit posting requirement, absent resume evidence is a FAIL.
Do not infer evidence from an unrelated title, employer, or location.

A failed status is not a sufficient result. Report one row for each failed
requirement:

| Field | Required content |
|---|---|
| Requirement | Short literal name of the mandatory requirement |
| Posting text | The exact posting sentence that creates the requirement |
| Evidence checked | Exact files, profile fields, or other approved sources checked |
| Evidence found | Matching evidence, conflicting evidence, or `none found` |
| Why it failed | One direct sentence that connects the requirement to the evidence gap |
| Fix type | `CV FIX`, `LUCAS CONFIRMATION`, or `ROLE MISMATCH` |
| Next action | The one action needed to continue, or `abandon this posting` |

Use `CV FIX` only when an approved source already contains the fact. Use
`LUCAS CONFIRMATION` when the approved sources are silent. Use `ROLE MISMATCH`
when verified facts contradict the requirement or Lucas confirms that he does
not meet it. Never convert silence into a claim that Lucas lacks experience.

---

## Resume Evidence Check (required-token blocking, preferred coverage scored 0-100)

Exact-token matching. This models the lexical floor, which is what most real
recruiter search still is.

**Step 1.** Extract every hard requirement from the posting. Classify each as
`required` or `preferred` using the posting's own words. Discard soft skills
and buzzwords. They are not retrieval tokens.

**Step 2.** For each token, search the raw extracted text:

| Placement | Points |
|---|---|
| Absent entirely | 0 |
| In `Skills` only | 1 |
| In `Experience` only | 2 |
| In `Skills` and in one `Experience` bullet, in context | 3 |

**Step 3.**

```
coverage = 100 * sum(points * requirement_weight)
                 / sum(3 * requirement_weight)
requirement_weight: required = 3, preferred = 1
```

**Step 4, hard result.** The Resume Evidence Check FAILS when any required token earns fewer than
3 placement points. Send every missing placement back to the Architect and
re-run the check. Preferred tokens affect the score but do not block.

For each required token below 3 points, state exactly which placement is
missing, quote the available evidence, and assign the same fix type used by
the Role Eligibility Check. If the same underlying fact fails both checks,
list it once in the Decision Explanation and cross-reference it here. Do not
present one fact gap as two independent reasons.

**Step 5, stuffing penalty.** Subtract 5 points per token that appears 4 or
more times. This is a human-reaction penalty, not a machine one.

**Report, always:** the full token table with placement and points. The number
alone is useless. The table is the deliverable.

---

## Recruiter Readability Score (reported, not blocking, scored 0-100)

Recruiters scan fast, non-linearly, anchored on headers. The one peer-reviewed
eye-tracking result found time on **Experience** and **Education** the
strongest predictors of approval.

| # | Check | Points |
|---|---|---|
| 3.1 | Target title appears in the top 15% of the document | 15 |
| 3.2 | The 3 most relevant bullets are in the most recent role, in its first 3 lines | 20 |
| 3.3 | Every bullet starts with a clear past-tense action verb and describes an outcome. No present-tense duty lists and no "Responsible for" phrasing | 15 |
| 3.4 | At least 3 bullets carry a real, defensible number | 15 |
| 3.5 | Experience completeness: no verified role, bullet, or metric from the selected base was removed. Prefer 1 page; allow 2 when complete content does not fit | 10 |
| 3.6 | No unsupported buzzwords ("team player", "results-driven", "passionate") | 10 |
| 3.7 | Skills grouped by category, not one undifferentiated wall | 10 |
| 3.8 | Scannable: consistent spacing, bold titles, adequate white space | 5 |

---

## Report format

Emit exactly this. No preamble.

```
# ATS Analysis — <resume file> vs <job slug>
Segment: <us-direct | br-pj | agency>   Date: <YYYY-MM-DD>

## Verdict
<READY | BLOCKED: <clear check name>>

## Decision Explanation
<For READY: `No blocking reason.`>
<For BLOCKED: one table with these columns: Check, Requirement, Posting text,
Evidence checked, Evidence found, Why it failed, Fix type, Next action.>
<List each root cause once. A status or score without this table is invalid.>

## File Readability Check
<8-row table, PASS/FAIL, offending text quoted for each FAIL>

## Role Eligibility Check
<table>

## Resume Evidence Check: NN/100, <PASS | FAIL>
<full token table with requirement weight, placement and points>
Required tokens without Skills and Experience placement: <list>

## Recruiter Readability Score: NN/100
<8-row table>

## Defects, ranked by cost
1. <defect> — <check> — <exact fix, quoting the text to change>
2. ...

## Match limits
<preferred tokens not placed, or none>
```

## Prohibitions

- Never edit the resume. Report defects, hand them to the Resume Architect.
- Never write only `FAIL`, `BLOCKED`, or a score. Always give the exact reason
  and next action in the Decision Explanation.
- Never emit a single blended "ATS score". The checks are separate on purpose.
- Never claim a vendor produces these numbers.
- Never guess a job requirement the posting did not state.
