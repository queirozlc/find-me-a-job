#!/bin/zsh
# Hunt 2026-09-02-b. Gates each tailored CV with Sieve as soon as Quill's draft lands. Two-call /clear reset between.
cd ~/career
H=state/hunt-2026-09-02-b.md
idle(){ for i in $(seq 1 120); do s=$(maestri check "$1" 2>/dev/null); if ! echo "$s" | grep -q "esc to interrupt"; then return 0; fi; sleep 5; done; return 1; }
reset_sieve(){ idle Sieve; maestri ask Sieve --raw "/clear" >/dev/null 2>&1; sleep 1; maestri ask Sieve --raw "\x0d" >/dev/null 2>&1; sleep 6; idle Sieve; }
gate(){ slug=$1; lang=$2
  L=state/app-$slug.md
  for i in $(seq 1 720); do grep -q "^EXIT" state/$slug-quill.out 2>/dev/null && break; sleep 10; done
  if [ ! -f resumes/$slug-$lang.pdf ]; then echo "- $(date +%H:%M) Sieve skipped: no PDF at resumes/$slug-$lang.pdf" >> $L; echo "- $(date +%H:%M) Sieve skipped $slug: no PDF" >> $H; return; fi
  reset_sieve
  sed -i '' "s/^Phase: .*/Phase: 3-gate/" $L
  echo "- $(date +%H:%M) Sieve dispatched: gate round 1. Output state/$slug-sieve.out" >> $L
  echo "- $(date +%H:%M) Sieve dispatched: $slug gate round 1" >> $H
  maestri ask Sieve "You are Sieve, the ATS Analyzer. You grade, you never edit a CV. Hunt 2026-09-02-b, one posting: $slug.

Read in full: ~/career/CLAUDE.md, ~/career/RUBRIC.md, ~/career/CV-SPEC.md, ~/career/DOSSIER.md, and the posting with the Maestro brief at ~/career/jobs/$slug.md.

File under test: ~/career/resumes/$slug-$lang.pdf (source ~/career/resumes/$slug-$lang.tex). Also read ~/career/reports/$slug-draft.md for the Architect's own list of [UNVERIFIED] markers.

Run the mandatory extraction step, then all four gates against the posting: Gate 0 parse integrity, Gate 1 knockouts, Gate 2 retrieval coverage, Gate 3 human scan. Apply the accepted tabular* exception from RUBRIC.md. In Gate 3 check the voice rule (CV-SPEC.md, CLAUDE.md section 9): every bullet first person, past tense, subject omitted; no bullet starts with I or Eu; Summary uses I or Eu. Check every title and date against DOSSIER.md LinkedIn ground truth character for character. Check zero Ruby or Rails tokens. List every [UNVERIFIED] marker and every number that does not trace to DOSSIER.md.

Write the report in the RUBRIC.md format to ~/career/reports/$slug-gate.md. End it with a section '## Fix list for the Architect' holding only the defects that block (Gate 0 not fully PASS, any Gate 1 FAIL) as numbered, concrete edits, or the line 'none'.

Do not edit any file under ~/career/resumes/. Do not spawn subagents. Do not report through maestri ask. Append one log line to ~/career/state/app-$slug.md when done, format '- HH:MM <what happened>' from date +%H:%M, never rewrite existing lines. Reply with: Gate 0 PASS/FAIL, Gate 1 PASS/FAIL with the failing items, Gate 2 score, Gate 3 score, the fix list." > state/$slug-sieve.out 2>&1
  echo "EXIT $?" >> state/$slug-sieve.out
  echo "- $(date +%H:%M) Sieve reported: gate round 1. See state/$slug-sieve.out and reports/$slug-gate.md" >> $L
  sed -i '' "s|^Next: .*|Next: Maestro reads reports/$slug-gate.md; fix round if blocked, else package.|" $L
  echo "- $(date +%H:%M) Sieve reported: $slug gate round 1. reports/$slug-gate.md" >> $H
}
gate goodway-global-fullstack en
gate brivia-fullstack-pj pt
gate conta-simples-engenheira-software-senior pt
gate diana-neves-fullstack-314-26 pt
gate techmunity-senior-fullstack-ai en
gate kotai-backend-nodejs-nestjs pt
gate brasil-em-dobro-backend-senior pt
gate ciandt-senior-fullstack en
gate indi-node-developer en
gate micro1-frontend-specialist en
echo "- $(date +%H:%M) Sieve chain finished all 10 gate rounds" >> $H
echo SIEVE_CHAIN_DONE
