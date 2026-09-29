#!/bin/zsh
# Tailors 4 approved postings with Quill, one at a time, /new reset between.
cd ~/career
wait_idle(){ for i in $(seq 1 30); do maestri check "$1" 2>/dev/null | grep -q "Ask Codex" && return; sleep 5; done; }
run(){ slug=$1; company=$2; corpus=$3; lang=$4
  echo "- $(date +%H:%M) Quill dispatched: tailor from base. Output state/$slug-quill.out" >> state/app-$slug.md
  sed -i '' "s/^Phase: .*/Phase: 2-tailor/" state/app-$slug.md
  maestri ask Quill "You are the Resume Architect. You write, you never grade. Read first: ~/career/CLAUDE.md, ~/career/CV-SPEC.md, ~/career/DOSSIER.md, ~/career/RUBRIC.md, ~/career/keywords/$corpus.md, and the posting with the Maestro brief at ~/career/jobs/$slug.md.

Task: tailor the base CV for $company. Start from ~/career/resumes/base-en.tex and ~/career/resumes/base-pt.tex, never from scratch. Write ~/career/resumes/$slug-en.tex and ~/career/resumes/$slug-pt.tex. Same facts, same structure, same dates in both. Keep every title and date exactly as in the base files. Keep the CV title Senior Software Engineer. Keep one page each. No Ruby or Rails token anywhere. Keep the two-column role header and the spacing rules of CV-SPEC.

Tailoring rules: reorder and reword bullets and the Skills groups so the posting's required tokens appear verbatim where the DOSSIER supports them. Use the exact spelling the posting uses. Every bullet keeps the XYZ format with a bare leading verb and its figure. Every fact stays traceable to DOSSIER.md. Anything not in DOSSIER.md ships marked [UNVERIFIED] inline. Never invent a tool, a number, or a domain. Respect the Gaps line of the Maestro brief: do not claim those tokens.

Build both with tectonic, then run pdftotext and pdftotext -layout on both PDFs into $slug-<lang>.raw.txt and .layout.txt next to them. Confirm page count 1 and that the contact block, section headers and all four employment blocks extract. Report the results.

Also write ~/career/reports/$slug-message.md with: (1) a recruiter or application message in $lang, ready to paste, under 150 words, that names two matching facts from the CV and asks for the next step; (2) prepared screening answers: time-zone overlap (Vitoria, Brazil, GMT-3, state overlap with US hours in prose), English level (Advanced/C1, daily work with a US team), contract type (all of PJ with own CNPJ, US contractor W-8BEN, CLT, EOR acceptable; pick the one the posting implies and say the others are fine), years of experience (from DOSSIER dates), notice period (write: not in DOSSIER, ask Lucas), plus any question the posting itself asks.

Write ~/career/reports/$slug-draft.md with: files written, list of changed bullets versus base, every [UNVERIFIED] marker with its reason, posting tokens you could not place and why. Reply with a short summary of the same. Do not ask questions mid-task; mark and move on." > state/$slug-quill.out 2>&1
  if [ ! -f reports/$slug-draft.md ]; then
    echo "- $(date +%H:%M) Quill ask returned with no draft, sending Enter to submit the typed prompt" >> state/app-$slug.md
    maestri ask Quill --raw "\n" >/dev/null 2>&1
    for i in $(seq 1 180); do [ -f reports/$slug-draft.md ] && maestri check Quill 2>/dev/null | grep -q "Ask Codex" && break; sleep 10; done
    maestri check Quill > state/$slug-quill.out 2>&1
  fi
  echo "- $(date +%H:%M) Quill reported. See state/$slug-quill.out and reports/$slug-draft.md" >> state/app-$slug.md
  sed -i '' "s|^CV: .*|CV: resumes/$slug-en.tex, resumes/$slug-pt.tex|" state/app-$slug.md
}
run lawnstarter-staff-product-engineer LawnStarter us-direct English
run charterup-senior-fullstack CharterUP us-direct English
run jobgether-backend-core-apis "the Jobgether partner company (Backend Engineer, Core APIs)" us-direct English
run brivia-fullstack-remoto Brivia agency Portuguese
echo CHAIN_DONE
