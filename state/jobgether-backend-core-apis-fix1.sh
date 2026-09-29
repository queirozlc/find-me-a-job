#!/bin/zsh
cd ~/career; S=jobgether-backend-core-apis
while pgrep -f "state/quill-chain.sh|lawnstarter-staff-product-engineer-fix1.sh" >/dev/null; do sleep 15; done
echo "- $(date +%H:%M) Quill dispatched: fix round 1. Output state/$S-quill-fix1.out" >> state/app-$S.md
maestri ask Quill "You are the Resume Architect. Fix round 1 for the Jobgether partner posting (Backend Engineer, Core APIs). Read ~/career/reports/$S-gate0.md, ~/career/DOSSIER.md, ~/career/CV-SPEC.md, ~/career/jobs/$S.md. Edit ~/career/resumes/$S-en.tex and $S-pt.tex only.

Apply fix list items 1, 4, 5, 9, 10, 11, 12, 13, 14, 15 exactly as the report describes: cap 'APIs' at 3; name real-time data processing over DynamoDB Streams in DexCare b1; put Go in the Summary scoped as recorded usage; carry 'reliability' and 'production-grade' in the Luizalabs deploy bullet; a Skills group label carrying 'Multi-tenant security' or 'Authentication and authorization'; 'Frontend: React | React Native'; split Testing and AI tooling into two groups; hanging indent in the resumeItem macro; 'Core APIs' capitalized in the Summary; vary the DexCare openers. Same edits in Portuguese, keeping English technical terms beside the Portuguese phrase where the report's item 19 suggests.

Do NOT add Git, shell scripting, performance tuning, debugging, a RabbitMQ bullet, or Go at DexCare. Those wait for Lucas.

Remove the 'US-hours overlap' clause from both Summaries; DOSSIER forbids that sentence. For 'Supported nationwide expansion' and 'beverage distribution startup': remove the unsupported words or keep them with an inline [UNVERIFIED] marker.

Then: tectonic both, pdftotext and pdftotext -layout into the .raw.txt and .layout.txt, confirm 1 page each. Append a 'Fix round 1' section to ~/career/reports/$S-draft.md listing each change. Reply with a short summary. Do not ask questions mid-task." > state/$S-quill-fix1.out 2>&1
echo "- $(date +%H:%M) Quill fix round 1 reported. See state/$S-quill-fix1.out" >> state/app-$S.md
echo "- $(date +%H:%M) Sieve dispatched: re-gate r1. Output state/$S-sieve-r1.out" >> state/app-$S.md
while pgrep -f "maestri ask Sieve" >/dev/null; do sleep 15; done
maestri ask Sieve --raw "/clear\n" >/dev/null 2>&1; sleep 10
maestri ask Sieve "You are the ATS Analyzer. You grade, you never edit. Re-gate the Jobgether partner posting after fix round 1. Read ~/career/RUBRIC.md, ~/career/CV-SPEC.md, ~/career/DOSSIER.md, ~/career/jobs/$S.md, your previous report ~/career/reports/$S-gate0.md and ~/career/reports/$S-draft.md. Regenerate extractions of ~/career/resumes/$S-en.pdf and $S-pt.pdf with pdftotext and pdftotext -layout. Run all four gates with the same scoring method as before so scores are comparable. Check titles and dates against the DOSSIER LinkedIn block. Grep both .tex for Ruby, Rails, UNVERIFIED. Confirm 1 page each. Write ~/career/reports/$S-gate0-r1.md with verdicts, scores, which of the 19 fixes are resolved, any new defect. Reply with verdicts, scores, remaining fix count, report path." > state/$S-sieve-r1.out 2>&1
echo "- $(date +%H:%M) Sieve re-gate r1 reported. See state/$S-sieve-r1.out and reports/$S-gate0-r1.md" >> state/app-$S.md
