#!/bin/zsh
# Hunt 2026-09-02-b. Tailors 10 approved postings with Quill, one per dispatch, two-call /new reset between.
cd ~/career
H=state/hunt-2026-09-02-b.md
idle(){ for i in $(seq 1 120); do s=$(maestri check "$1" 2>/dev/null); if echo "$s" | grep -q "Ask Codex" && ! echo "$s" | grep -q "esc to interrupt"; then return 0; fi; sleep 5; done; return 1; }
reset_quill(){ idle Quill; maestri ask Quill --raw "/new" >/dev/null 2>&1; sleep 1; maestri ask Quill --raw "\x0d" >/dev/null 2>&1; sleep 8; idle Quill; }
run(){ slug=$1; lang=$2; corpus=$3
  L=state/app-$slug.md
  case $lang in pt) LANGNAME=Portuguese; VERBS='Construí, Projetei, Reduzi, Ajudei a construir';; *) LANGNAME=English; VERBS='Built, Designed, Reduced, Helped build';; esac
  echo "- $(date +%H:%M) Quill dispatched: tailor from base-$lang.tex. Output state/$slug-quill.out" >> $L
  sed -i '' "s/^Phase: .*/Phase: 2-tailor/" $L
  echo "- $(date +%H:%M) Quill dispatched: $slug" >> $H
  maestri ask Quill "You are Quill, the Resume Architect. You write, you never grade. Hunt 2026-09-02-b, one posting: $slug.

Read first, in full: ~/career/CLAUDE.md, ~/career/CV-SPEC.md, ~/career/DOSSIER.md, ~/career/keywords/$corpus.md, and the posting with the Maestro brief at ~/career/jobs/$slug.md.

Task: tailor the base CV for this posting in $LANGNAME only. Copy ~/career/resumes/base-$lang.tex to ~/career/resumes/$slug-$lang.tex and tailor the copy. Never start from scratch. Never edit base-$lang.tex. Never build the other language. Keep every title, date, company, and location exactly as in the base. Keep the CV title Senior Software Engineer. Keep one page. Keep the two-column role header and the spacing of CV-SPEC. No Ruby or Rails token anywhere.

Voice (Lucas, 2026-09-02): bullets first person, past tense, subject omitted, leading verb such as $VERBS. Never present tense, never 'Responsible for', never third person, no bullet starts with I. Summary in first person with the subject (I / Eu). Every bullet is XYZ: accomplished X, measured by Y, by doing Z, with the technologies named.

Tailoring: reorder and reword bullets and the Skills groups so the posting's required tokens appear verbatim where DOSSIER.md supports them, using the posting's exact spelling once. Every fact stays traceable to DOSSIER.md. Anything not in DOSSIER.md ships marked [UNVERIFIED] inline. Never invent a tool, a number, or a domain. Respect the Gaps line of the Maestro brief: do not claim those tokens. Cap any term at 3 appearances.

Build: tectonic ~/career/resumes/$slug-$lang.tex, then pdftotext and pdftotext -layout into $slug-$lang.raw.txt and $slug-$lang.layout.txt next to the PDF. Confirm 1 page, contact block, four section headers, and all five employment blocks extract. grep -n UNVERIFIED and grep -in 'ruby\|rails' on the .tex and report the hits.

Also write ~/career/reports/$slug-message.md, in $LANGNAME, with: (1) a message to the recruiter or application form, ready to paste, under 150 words, first person, naming two matching facts from the CV and asking for the next step; (2) prepared screening answers: time-zone overlap (Vitória, Brazil, GMT-3; state overlap with US hours in prose, never as an offset on the CV), English level (Advanced/C1, daily work with a US team), contract type (PJ with own CNPJ, US contractor W-8BEN, CLT, EOR all acceptable; name the one the posting implies), years of experience (from DOSSIER dates), notice period (write: not in DOSSIER, ask Lucas), plus every question the posting itself asks, answered from DOSSIER only.

Write ~/career/reports/$slug-draft.md with: files written, changed bullets versus base, every [UNVERIFIED] marker with its reason, posting tokens you could not place and why.

Do the work in this session. Do not spawn subagents, do not ask Sieve, do not report through maestri ask, do not touch any other file. Append one log line to ~/career/state/app-$slug.md when done, format '- HH:MM <what happened>' from date +%H:%M, never rewrite existing lines. Reply with a short summary of the draft report." > state/$slug-quill.out 2>&1
  echo "EXIT $?" >> state/$slug-quill.out
  echo "- $(date +%H:%M) Quill reported. See state/$slug-quill.out and reports/$slug-draft.md" >> $L
  sed -i '' "s|^CV: .*|CV: resumes/$slug-$lang.tex and .pdf|" $L
  sed -i '' "s|^Next: .*|Next: Sieve gates resumes/$slug-$lang.pdf against jobs/$slug.md.|" $L
  echo "- $(date +%H:%M) Quill reported: $slug. Draft reports/$slug-draft.md" >> $H
  reset_quill
}
reset_quill
run goodway-global-fullstack en us-direct
run brivia-fullstack-pj pt br-pj
run conta-simples-engenheira-software-senior pt br-pj
run diana-neves-fullstack-314-26 pt br-pj
run techmunity-senior-fullstack-ai en agency
run kotai-backend-nodejs-nestjs pt us-direct
run brasil-em-dobro-backend-senior pt br-pj
run ciandt-senior-fullstack en agency
run indi-node-developer en agency
run micro1-frontend-specialist en agency
echo "- $(date +%H:%M) Quill chain finished all 10 postings" >> $H
echo QUILL_CHAIN_DONE
