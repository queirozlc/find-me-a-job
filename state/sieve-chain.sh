#!/bin/zsh
# Gates each tailored CV with Sieve as soon as Quill's report for it exists.
cd ~/career
run(){ slug=$1
  for i in $(seq 1 720); do grep -q "Quill reported" state/app-$slug.md 2>/dev/null && [ -f reports/$slug-draft.md ] && break; sleep 10; done
  [ -f reports/$slug-draft.md ] || { echo "TIMEOUT waiting for $slug draft"; return; }
  maestri ask Sieve --raw "/clear\n" >/dev/null 2>&1; sleep 10
  echo "- $(date +%H:%M) Sieve dispatched: gate. Output state/$slug-sieve.out" >> state/app-$slug.md
  sed -i '' "s/^Phase: .*/Phase: 3-gate/" state/app-$slug.md
  maestri ask Sieve "You are the ATS Analyzer. You grade, you never edit a CV. Read first: ~/career/CLAUDE.md, ~/career/RUBRIC.md, ~/career/ATS-KNOWLEDGE.md, ~/career/CV-SPEC.md, ~/career/DOSSIER.md (the LinkedIn ground truth section is the source for titles and dates), the posting and Maestro brief at ~/career/jobs/$slug.md, and the Architect's draft report at ~/career/reports/$slug-draft.md.

Grade ~/career/resumes/$slug-en.pdf and ~/career/resumes/$slug-pt.pdf (sources $slug-en.tex, $slug-pt.tex; extractions $slug-<lang>.raw.txt and .layout.txt exist next to them, regenerate if missing) against the posting. Run all four gates of the rubric. Gate 0 with the two-column header exception recorded in CV-SPEC and RUBRIC. Gate 1 knockouts from the posting text only. Gate 2 retrieval coverage: list every required token from the posting and whether it is present verbatim, a synonym, or absent. Gate 3 human scan. Check every title, company name and date against the DOSSIER LinkedIn ground truth block; any mismatch is a Gate 0 FAIL. Grep both .tex files for Ruby, Rails, UNVERIFIED and report every hit. Confirm one page each.

Write ~/career/reports/$slug-gate0.md: verdict per gate, Gate 2 and Gate 3 scores out of 100, a numbered fix list for the Architect (file, line, defect, what would pass), and the list of required tokens not covered. Reply with the verdicts, the two scores, the fix list count and the report path. Do not edit any file under resumes/." > state/$slug-sieve.out 2>&1
  echo "- $(date +%H:%M) Sieve reported. See state/$slug-sieve.out and reports/$slug-gate0.md" >> state/app-$slug.md
}
run lawnstarter-staff-product-engineer
run charterup-senior-fullstack
run jobgether-backend-core-apis
run brivia-fullstack-remoto
echo CHAIN_DONE
