#!/bin/zsh
cd ~/career; S=lawnstarter-staff-product-engineer
while pgrep -f "state/quill-chain.sh" >/dev/null; do sleep 15; done
echo "- $(date +%H:%M) Quill dispatched: fix round 1. Output state/$S-quill-fix1.out" >> state/app-$S.md
maestri ask Quill "You are the Resume Architect. Fix round 1 for LawnStarter. Read ~/career/reports/$S-gate0.md (the Analyzer's report), ~/career/DOSSIER.md, ~/career/CV-SPEC.md, ~/career/jobs/$S.md. Edit ~/career/resumes/$S-en.tex and $S-pt.tex only.

Apply fix list items 1 to 10 and 18 (all marked DOSSIER-OK): rebuild so the PDFs match the .tex; put 'product' and 'product engineering' once in the Summary; list 'React' as its own Skills token beside 'React Native'; name 'event-driven architecture', 'data model', 'controlled rollout', 'security', 'performance', 'guardrails' and 'metric' once each inside the bullets that already carry the supporting fact; vary the leading verbs so no more than two DexCare bullets start with the same verb. Same edits in Portuguese.

Do NOT write evals, prompts, runbooks, rollback, documented, lead-level or PM/designer claims. Those are BLOCKED until Lucas answers.

Two claims lack DOSSIER support: 'beverage distribution startup' (line 111) and 'Supported nationwide retailer expansion' (line 102). Remove the industry word and the nationwide scope, or keep them with an inline [UNVERIFIED] marker. Also remove the 'US-hours overlap' clause from the Summary; DOSSIER forbids that sentence and this posting does not gate on time zone. Keep 'Advanced/C1 English' only if it fits on one page.

Then: tectonic both, pdftotext and pdftotext -layout into the .raw.txt and .layout.txt, confirm 1 page each, confirm the Summary in the PDF matches the .tex. Update ~/career/reports/$S-draft.md with a 'Fix round 1' section listing each change. Reply with a short summary. Do not ask questions mid-task." > state/$S-quill-fix1.out 2>&1
echo "- $(date +%H:%M) Quill fix round 1 reported. See state/$S-quill-fix1.out" >> state/app-$S.md
echo "- $(date +%H:%M) Sieve dispatched: re-gate r1. Output state/$S-sieve-r1.out" >> state/app-$S.md
maestri ask Sieve --raw "/clear\n" >/dev/null 2>&1; sleep 10
maestri ask Sieve "You are the ATS Analyzer. You grade, you never edit. Re-gate LawnStarter after fix round 1. Read ~/career/RUBRIC.md, ~/career/CV-SPEC.md, ~/career/DOSSIER.md, ~/career/jobs/$S.md, your previous report ~/career/reports/$S-gate0.md and the Architect's ~/career/reports/$S-draft.md. Regenerate the extractions of ~/career/resumes/$S-en.pdf and $S-pt.pdf with pdftotext and pdftotext -layout. Run all four gates again with the same scoring method as your previous report so scores are comparable. Check titles and dates against the DOSSIER LinkedIn block. Grep both .tex for Ruby, Rails, UNVERIFIED. Confirm 1 page each. Write ~/career/reports/$S-gate0-r1.md with verdicts, Gate 2 and Gate 3 scores, which of the 19 fixes are resolved, and any new defect. Reply with verdicts, scores, remaining fix count, report path." > state/$S-sieve-r1.out 2>&1
echo "- $(date +%H:%M) Sieve re-gate r1 reported. See state/$S-sieve-r1.out and reports/$S-gate0-r1.md" >> state/app-$S.md
