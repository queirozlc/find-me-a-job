# Career workspace — hard constraints

Binding on every agent that touches this directory. These are not preferences.
Ground truth lives in `ATS-KNOWLEDGE.md`, the rubric in `RUBRIC.md`, the facts
in `DOSSIER.md`, the hunt config in `find-me-a-job.md`.

## 1. Titles and dates come from LinkedIn, strictly

**Every job title and every date on any resume, profile, or message must match
the LinkedIn profile exactly.** Read them from LinkedIn. Do not copy them from
an old resume, do not reconstruct them from memory, do not adjust a title to
fit a posting, do not round a date.

Clarified by Lucas 2026-09-01: the rule is about the periods, not the glyphs.
Start and end months must be identical to LinkedIn. The separator glyph follows
`CV-SPEC.md` (ASCII hyphen), even where LinkedIn renders an EN DASH.

The four existing PDFs in `~/Documents/Resumes/` contradict each other on
current employer, dates, and degree. They are not a source. LinkedIn is.

## 2. Stack positioning

- Position as **TypeScript, Node.js, React, Go**.
- **No Ruby or Rails token appears anywhere** in a resume, headline, job
  title, summary, or skills list.
- Where the history recorded a Rails-world tool, use its JS/TS equivalent:
  Sidekiq to **BullMQ**, ActiveRecord to **Drizzle**, ActiveJob to **BullMQ**,
  RSpec to **Vitest** or **Jest**, Devise/Pundit to the actual auth in use.
  Apply the same rule to any tool not listed here.
- Rails may remain in the history as a fact if Lucas confirms it. It never
  occupies a high-weight indexed field.

## 3. Identity facts

- Degree: **Information Systems**, FAESA.
- Location on documents: **Vitória, ES, Brazil**. Nothing more.
- **Never print a UTC offset or a time-zone overlap statement on the
  resume** (Lucas, 2026-09-02). It is GMT-3. Overlap is answered only in the
  screening answers of the apply note, never on the CV.
- Lippaus role location prints **Vitória, ES, Brazil**, matching LinkedIn
  (Lucas, 2026-09-02). DexCare and Luizalabs print `Remote`.
- Luizalabs / Magazine Luiza: **Mid-level**, **direct CLT employee**,
  full-time. DexCare: full-time. Corrected by Lucas 2026-09-01; the earlier
  "through Fullstack Labs" statement was wrong. Do not print the contract
  detail on the CV; it is context only.

## 4. Match policy

ATS match is the first objective after eligibility and primary-stack triage.
Use this weight order:

1. **Primary language or runtime, weight 4.** Accept JavaScript, TypeScript,
   Node.js, and Go. Drop a posting when its primary requirement is Ruby or
   Rails, Java, Python, PHP, C# or .NET, or another outside stack.
2. **Frameworks and libraries, weight 3.** Match the posting's exact tokens in
   `Skills` and in one relevant `Experience` bullet. Examples include Express,
   Fastify, NestJS, React, Next.js, Angular, and Vite.
3. **Data, messaging, cloud, and tools, weight 2.** Match exact required tokens
   in `Skills` and in one relevant `Experience` bullet.
4. **Practices and adjacent terms, weight 1.** Match exact posting terms when
   they fit the role history.

Frameworks, libraries, databases, cloud services, and tools do not decide
primary-stack eligibility. Do not use verification markers for these tokens.
Do not change titles, dates, employers, degree, location, metrics, contract
status, work authorization, or language proficiency to improve a match.
Never invent a posting, recruiter, primary programming language, credential,
or regulated-domain qualification.

## 5. Role separation

- The Resume Architect **writes** and never grades.
- The ATS Analyzer **grades** and never edits.
- Never collapse these two seats. A writer that grades itself grades
  generously.

## 6. Worker delegation and monitoring

- The agent that sends a worker task owns the background execution. Use the
  background mechanism of the sending harness.
- The receiving worker runs the task normally. It must not detach itself,
  start a second background process, or use `maestri ask` to report back.
- Keep the background handle or output path. Poll it until the worker reaches
  a terminal result. Use `maestri check` only as a progress view.
- A timeout, an empty output file, or a successful dispatch is not completion.
  Do not resend the task. Continue polling the original task.
- Update the ledger and the visible status note at dispatch, material progress,
  completion, and blocker states.
- Do not give Lucas a final result while an authorized worker task is still
  running, unless Lucas explicitly asks to leave it running.
- A worker does not fan out. One dispatch carries one posting. The Resume
  Architect never spawns subagents to tailor several postings at once; the
  Maestro dispatches each posting and owns each handle (Lucas, 2026-09-02).

## 7. Outward actions

- Agents **never** submit an application, never send a recruiter message,
  never click a submit button. Lucas does.
- **Never** set LinkedIn Open to Work to "All members". Recruiters only,
  workplace type Remote.
- At a LinkedIn auth wall: escalate to Lucas, poll in the background, keep
  working on anything that needs no portal. One password retry maximum. Never
  solve a CAPTCHA, switch accounts, or bypass 2FA.
- Never write a credential to a file, note, log, or report.

## 8. Sourcing

- Recency cut: past 24 hours first, past week at the widest. Never widen it to
  manufacture volume.
- Drop every role labeled `Reposted`. Do not tailor or rank it.
- Drop every role that states `Over 100 applicants`, `100+ applicants`, or
  that more than 100 people clicked Apply. If LinkedIn does not show a count,
  record it as not observable and do not infer one.
- Segment weight: US-direct and Brazilian PJ are top and equal. Consultancies
  and agencies third.
- Seniority: Senior preferred, strong Mid acceptable.
- Quote real posting text. Never synthesize a job description from memory.

## 9. CV voice

Set by Lucas 2026-09-02. Bullets: first person, past tense, subject omitted
(`Built`, `Reduced`, `Helped build`). Never present tense, never "Responsible
for", never third person. Summary: first person with `I`. Every bullet is XYZ:
accomplished X, measured by Y, by doing Z. Rule lives in `CV-SPEC.md`.

## 9.1 CV completeness and language proficiency

- Never trim a tailored CV. Preserve every verified Experience role and every
  verified Experience bullet from the selected base CV. The Architect may
  reword or reorder a bullet when the facts stay exact. It must not delete a
  bullet or metric to save space or improve match.
- Page count never overrides Experience completeness. Prefer one page when the
  complete content fits. Use two pages when it does not.
- Put spoken-language proficiency only in a separate `Language` section on an
  English CV and `Idiomas` section on a Portuguese CV. Never put it in Skills.
- Print `Portuguese: Native` and `English: Fluent (C1)`.

## 10. Triage knockouts

Maestro drops these at triage, before any tailoring (Lucas, 2026-09-02):

- Any role labeled `Reposted`.
- Any role that states `Over 100 applicants`, `100+ applicants`, or more than
  100 people clicked Apply.
- Apply destination on Gupy (any `gupy.io` URL).
- Company blocklist: BairesDev.
- Hybrid or on-site anywhere. Remote only.
- Primary language or runtime outside JavaScript, TypeScript, Node.js, and Go.
  Examples include Ruby or Rails, Java-first, Python-first, PHP-first, and
  C# or .NET-first postings. Do not reject a posting only for a framework.
- Knockouts from the posting text: work authorization Lucas lacks,
  "not for freelancers" when no CLT/EOR option, mandatory location.

Triage is never skipped. The Maestro reports how many were dropped and why.

## 11. One language per tailored CV

A tailored CV ships in the posting's language only. Maestro decides at intake
from the posting text and the company origin. Bases stay a pair.

## 12. Vocabulary

One `/find-me-a-job` execution is a **hunt**. Never "cycle". The per-posting
pipeline inside a hunt is an **application**. Ledgers: `hunt-<date>.md`,
`app-<company>-<role>.md`.

## 13. Hunt summary note

At the end of every hunt, when all applications are delivered or abandoned,
the Maestro writes one note `hunt-<date>-summary` in the `Hunts` fichário:
one table row per application (role link, resume path, primary-stack result,
review results, recruiter channel, deadline) plus every cold message in full.
Lucas, 2026-09-02. Format lives in the `find-me-a-job` skill.
