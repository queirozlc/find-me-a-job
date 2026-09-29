You are Quill, the Resume Architect. This is a base round, not a tailoring task.

Read, in this order and in full: ~/career/CLAUDE.md, ~/career/CV-SPEC.md,
~/career/DOSSIER.md. Then read ~/career/resumes/base-en.tex and
~/career/resumes/base-pt.tex.

Task: rewrite the Summary and every Experience bullet of both base files in
the voice Lucas set on 2026-09-02, in place, and rebuild both PDFs.

Voice rule:
- Bullets: first person, past tense, subject omitted. EN: "Built", "Designed",
  "Reduced", "Helped build". PT: "Construí", "Projetei", "Reduzi", "Ajudei a
  construir". Never present tense ("Deliver", "Keep", "Reduce"), never
  "Responsible for", never third person. Do not start a bullet with "I".
- Summary: first person with the subject. "I build ...", "I have ...",
  "I integrate ...". Present tense for what Lucas does today at DexCare, past
  tense for what he did before.
- Keep the XYZ shape: accomplished X, measured by Y, by doing Z. Keep every
  number that is there now; they are dossier facts. Keep every technology
  token that is there now. Do not add claims. Do not change titles, dates,
  companies, locations, Skills lines, or the layout.

Examples of the change, DexCare:
- now: "Deliver real-time visit booking and provider availability for a
  healthcare scheduling platform by building event-driven TypeScript services
  on Express and Koa."
- new: "Built event-driven TypeScript services on Express and Koa that deliver
  real-time visit booking and provider availability for a healthcare
  scheduling platform."
- now: "Reduce release risk by 7% by shipping behind LaunchDarkly/OpenFeature
  flags and monitoring React with Datadog RUM."
- new: "Reduced release risk by 7% by shipping behind LaunchDarkly/OpenFeature
  flags and monitoring React with Datadog RUM."

Build and verify each file:
  tectonic ~/career/resumes/base-en.tex
  pdftotext ~/career/resumes/base-en.pdf ~/career/resumes/base-en.raw.txt
  pdftotext -layout ~/career/resumes/base-en.pdf ~/career/resumes/base-en.layout.txt
Same for base-pt. Confirm one page each, contact block and all four section
headers present, every employment block present, zero UNVERIFIED, zero
Ruby or Rails tokens.

Do the work in this session. Do not spawn subagents, do not ask Sieve to
grade, do not report through maestri ask. Do not touch any other file.

Append one log line to ~/career/state/hunt-2026-09-02-b.md when done, format
"- HH:MM <what happened>" from `date +%H:%M`. Never rewrite existing lines.

Reply with: one page yes/no per file, the full new Summary of each file, the
count of bullets rewritten per file, and any bullet you could not convert and
why.
