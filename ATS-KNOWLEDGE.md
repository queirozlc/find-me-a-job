# ATS Knowledge Base

Single source of truth for every career agent on this canvas.
Compiled 2026-09-01 from five parallel research passes. Raw reports with full
citations are in `~/career/research/`.

Read this file before you act. Do not repeat work already recorded here.

---

## 0. Rules of evidence

Career advice on the open web is mostly unsourced SEO content. Every claim
below carries a tier:

- **[DOC]** vendor technical documentation or a reproducible bug report.
- **[ENG]** engineering blog or peer-reviewed paper from the company that
  built the system.
- **[REG]** regulatory filing, for example an NYC Local Law 144 bias audit.
- **[SIM]** paired simulation or vendor product test, not a live field
  experiment.
- **[FOLK]** repeated widely, no traceable primary source. Treat as unknown.

If you add a claim to this file, tag it. If you cannot find a source, write
"not observable". Never invent a source.

---

## 1. Myths to never optimize for

These are load-bearing. Optimizing for them wastes effort and can hurt.

| Claim | Status |
|---|---|
| "ATS auto-rejects 75% of resumes" | **False.** Traced to a 2012 sales pitch by Preptel, a vendor that shut down in 2013. No methodology was ever published. The number drifts 70/75/88% across sites, the signature of an unsourced viral stat. |
| "The ATS gives you a score out of 100" | **False as framed.** No primary documentation from Workday, Greenhouse, SAP, Textkernel, RChilli, or Affinda describes a 0-100 gating score. That number belongs to third-party grading products, not to the employer's ATS. One open-source checker's own README disclaims its simulation as "approximations, not the actual proprietary algorithms". Enhancv's own page says "There's no such thing as an ATS score". |
| "White text keyword stuffing works" | **False, and it backfires.** Most ATS display the extracted plain text on the candidate record. Hidden text becomes visible there, and to any recruiter who select-all-copies the file. |
| "Quantifying achievements gives +40% callbacks" | **[FOLK].** No primary study exists. Quantify where you have a real number. Do not treat the statistic as fact. |
| "Tailoring gives 2x callbacks" | **[FOLK].** Same pattern. Tailoring is mechanically sensible, the percentage is invented. |
| "50+ endorsements outrank 0" / "All-Star = 40x more search appearances" | **[FOLK].** No LinkedIn primary source. The 40x figure originates around 2013-14 with no methodology. |
| "6-second recruiter scan" | **[SIM], weak.** The Ladders 2012 (6s) and 2018 (7.4s) studies never disclosed sample size, recruiter experience, or resume lengths, and were never peer reviewed. Directionally true that scanning is fast and non-linear. Do not design to the second. |

**Analyzer consequence:** never report a fake vendor score. Report
gate-by-gate results against a defined and reproducible rubric.

---

## 2. The pipeline, reconstructed

No vendor publishes a full diagram. This is assembled from documented
fragments. Stages 3 and 4 are where candidates actually lose.

1. **Ingest.** File type detection.
2. **Text extraction.** Native text layer only. **No major ATS-embedded parser
   does OCR on image-only PDFs.** SAP states directly that a scanned or
   image PDF "will not parse as expected". **[DOC]**
3. **Reading-order reconstruction.** Undocumented at every vendor. Parsers
   read a linear stream from document object order, not visual position.
   This is why columns break.
4. **Section segmentation** by heading detection.
5. **Named-entity extraction.** NLP/ML models.
6. **Taxonomy normalization.** Skills, titles, education levels map to an
   internal ontology (Textkernel taxonomy / O*NET 2019 / ISCO 2008; Workday
   Skills Cloud). **[DOC]**
7. **Structured JSON/XML output** into the candidate record.

### Who runs what

| ATS | Parser | Confidence |
|---|---|---|
| SAP SuccessFactors | Textkernel | Confirmed both sides **[DOC]** |
| SmartRecruiters | Textkernel | Confirmed by press release |
| Jobvite | Daxtra | Confirmed on Jobvite's own partner page |
| Bullhorn | Daxtra | Confirmed in Bullhorn's knowledge base |
| Greenhouse | **In-house, proprietary** | Confirmed by Greenhouse's own blog. They now layer generative AI for anonymization and "Structured Candidate Search" over in-house similarity models. |
| Oracle Taleo | Third party, vendor varies by deployment | Oracle names no vendor |
| iCIMS | Reported as Textkernel | **Third-party blogs only. Not in any iCIMS document.** |
| Workday, Lever, Ashby | **Not observable** | No public source names an engine |

### Best available parse evidence

Resumap ran 36 distinct resume templates carrying one identical fictional
candidate through Textkernel's live Tx API, the engine behind SuccessFactors
and SmartRecruiters. **[DOC-adjacent primary test]**

- All 36 parsed without crashing.
- 10/10 job-critical skills retained on 36/36.
- Median 68 distinct skills extracted, range 54-69.
- Contact and education fully extracted on 31/36.
- **The only real failures were work-history segmentation: 5/36 templates
  merged or wrongly split job entries.**

**Read that correctly.** On a modern parser, keyword loss is not the main
risk. **Employment-block segmentation is.** If two roles merge, your tenure,
your titles, and your seniority inference all corrupt at once. Design the
Experience section to be unambiguously segmentable above everything else.

---

## 3. Parse safety: hard constraints

Non-negotiable, all mechanically grounded:

- **Single column, full width.** Multi-column risks interleaving text
  mid-sentence. Jobscan's own testing reports a multi-column resume where the
  parser "picked up the work experience section but ignored everything else,
  no skills, no About section, no contact info".
- **No tables, no text boxes.**
- **No photo, no icons.** An icon is an image and carries no text. A phone
  number after a bare icon loses its semantic label. Photos also carry
  measured discrimination risk (see section 7).
- **Contact details in the body, never in a header or footer.**
- **No image-only or flattened PDF.** Confirmed hard failure. **[DOC]**
- **Beware ligatures.** `pypdf` issue #1351 is a reproducible bug where
  `extract_text()` returns nulls for fi/fl/ff glyphs; independently confirmed
  in Apache PDFBox JIRA and Mozilla Bugzilla #1810914. Cause: a missing or
  wrong `ToUnicode` CMap. **[DOC, primary]** Real words affected: office,
  profile, efficient, conflict, workflow. **Verification is mandatory:** open
  the PDF, select all, copy, paste into a plain text editor. What you see is
  what the parser sees.
- **Canva and InDesign exports** can rasterize text or emit it as vector
  outlines. Same select-all-copy test decides it.
- **Verbatim section headers.** Use exactly: `Summary`, `Skills`,
  `Experience`, `Projects`, `Education`, `Certifications`. Creative headers
  risk the whole block being dropped into an unstructured bucket.
- **Dates:** `Mon YYYY - Mon YYYY`, for example `Mar 2022 - Present`.
- **Bullets:** plain `-` or `•` only.
- **Filename:** use a descriptive ASCII-only file name.
- **Format:** text-based PDF by default. DOCX when the target ATS is old or
  unknown. Always obey what the posting asks for.

---

## 4. Retrieval and ranking

Two distinct layers. Confusing them is the most common analysis error.

### 4.1 Lexical retrieval is still the floor

OpenCATS, the open-source ATS whose schema is inspectable, confirms real ATS
search is often plain full-text keyword search over converted plain text, not
semantic matching. Recruiters type boolean queries by hand. Exact string
match still decides whether you are in the result set at all.

**Therefore: each literal target token from the posting must appear.** Preserve
the posting's spelling.

### 4.2 Taxonomy collapses aliases, sometimes

LinkedIn's skills taxonomy blog reports **39K skills, 374K aliases, 200K
edges**. **[ENG]** Alias collapsing is the documented mechanism that should
make `Node.js`, `NodeJS`, and `Node` resolve to one node. **Caveat: LinkedIn's
worked examples used different terms, not that exact triple.** So alias
collapsing is confirmed as a mechanism, not confirmed for our specific tokens.

Textkernel's Ontology API exposes Extract, Normalize, Autocomplete, and
Lookup Skills endpoints. **[DOC]** Taxonomy size not disclosed on that page.

**Operational rule:** never rely on alias expansion. Use the posting's exact
spelling and let the ontology do the rest.

Free taxonomies we can actually download:
- **O*NET** — CC BY 4.0, full database download. Cleanest option.
- **ESCO** — EUPL 1.2, API plus dumps.
- **Lightcast Open Skills** — full API access is now gated behind a paid
  contract.

### 4.3 The ML ranking layer

LinkedIn Recruiter runs on the **Galene** federated Lucene stack: a broker
distributes the query to sharded partitions, each scores with an ML model, a
federator re-ranks the merged set with near-real-time features. **[ENG]**

Ranking model evolution, all from LinkedIn Engineering: GBDT with a
**pairwise learning-to-rank** objective, then LINE-style network embeddings
for query expansion, then GLMix for per-recruiter and per-contract
personalization, plus multi-armed bandits for session exploration. **[ENG]**

**The objective function matters more than any of that.** LinkedIn's own
writeup names three ranking factors: similarity of work experience and skills
to the criteria, job posting location, and **predicted likelihood of a
positive response to recruiter outreach**. The optimization target is
explicitly **InMail Accept rate**, not keyword relevance. **[ENG]**

Consequence: looking responsive is a ranking feature, not a nicety.

### 4.4 Score composition is not observable

Searched hard for it. **No source anywhere discloses the actual weights
between skills, title, education, and tenure, for any vendor** — not even
under regulatory bias-audit disclosure. The HireVue NYC Local Law 144 audit
(DCI Consulting) was read directly: it discloses tiering methodology
(Bottom / Middle / Top) and real impact ratios by gender, race, and
intersectional group, but **not the scoring weights**. **[REG]**

Anyone who tells you the weights is guessing. We do not guess.

---

## 5. LinkedIn Recruiter specifics

### Confirmed indexed and ranked fields
Canonical titles, canonical skills, company, location. Named explicitly in
LinkedIn's Recruiter engineering post. **[ENG]**

### Spotlights, verified against the live help page
Current names, which differ from older terminology still circulating:
Open to work · Active talent · Have company connections · Interested in your
company · Rediscovered candidates · Internal candidates · Candidates saved by
· Applicants · Missed candidates · Verifications. **[DOC]**

### Location and remote
From LinkedIn's official Recruiter help. **[DOC]**

- A location selection implies a **100-mile radius**.
- Workplace type changes the behavior. **Remote: location is disregarded
  entirely and results are global.**
- **The Workplace-types filter only returns candidates who have set Open to
  Work preferences.**

**This is the lever.** A recruiter in the US filtering for Remote does not
see Brazil as a disqualifier. But they only see candidates who set Open to
Work preferences at all. Setting Open to Work with workplace type Remote,
recruiter-only visibility, is the mechanically confirmed way for a
Brazil-based profile to enter a global remote search.

Recruiter-only visibility shows a private note inside Recruiter's UI, no
public green frame. LinkedIn blocks visibility from Recruiter users at your
current employer via the "currently working here" flag but **states it cannot
guarantee complete privacy**. **[DOC]**

### Skill assessments
LinkedIn Engineering confirms passed skills feed the Galene index and Jobs
matching, and are Recruiter-filterable. LinkedIn self-reports "~30%
improvement in likelihood to hear back from a recruiter". **[ENG]** The
confirmed effect is **filterability plus response-likelihood**, not a generic
ranking boost.

### Not confirmed by any LinkedIn primary source
Endorsement counts affecting rank. Whether pinning a skill to the top 3
changes ranking weight rather than only display. The All-Star search
multiplier. SSI as a ranking input. Connection degree. Whether About,
Experience descriptions, Certifications, Featured, or Recommendations are
search-weighted, though they are plausible free-text index contributors.
**Treat all of these as unknown, not as false, and never as fact.**

---

## 6. Where the candidate actually gets filtered

Four checks, in order. Ranking never happens if a blocking check rejects.

- **File Readability Check.** Did the fields survive extraction, and did the
  employment blocks segment correctly?
- **Role Eligibility Check.** Rules-based, before any scoring. Work authorization,
  location, years of experience, required-skill presence, screening question
  answers. Binary and unforgiving.
- **Resume Evidence Check.** Do you appear in the recruiter's boolean query or
  the system's candidate set? Driven by exact tokens in indexed fields.
- **Recruiter Readability Score.** Fast, non-linear, anchored on headers. One
  peer-reviewed study (Piña & Petersheim, MDPI 2504-4990/5/3/38, read only via
  abstract, so unverified secondhand) trained a classifier on recruiter
  eye-tracking and reached **AUC 0.767**, with total viewing time and time on
  **Experience and Education** the strongest predictors.

---

## 7. Content evidence worth trusting

- **Name and race discrimination is real and large.** Bertrand &
  Mullainathan, *American Economic Review* 94(4), 2004. Correspondence audit
  with real job ads. White-sounding names got **50% more callbacks**, and
  better resume quality raised callbacks more for White names than Black
  names. A PNAS meta-analysis of 49 North American studies since 1989 found
  White applicants get 36% more callbacks than equally qualified Black
  applicants and 24% more than Latino applicants. Peer reviewed.
- **Omit the photo.** Both for parse safety and because photo effects are
  measured, interaction-dependent, and asymmetric by gender.
- **Employment gaps.** A real negative signal, not fixed in magnitude. An
  explained gap outperformed an unexplained one, 25.6% vs 23.3% callback. The
  unemployment-duration penalty shrinks in tight labor markets.
- **Length.** ResumeGo, n=482 recruiting professionals, 7,712 resumes, forced
  paired choice. Two-page chosen 5,375 times against 2,337 for the matched
  one-pager, with the gap widest above 10 years of experience. **[SIM], not a
  live callback experiment.** At ~5 years, the gap is smaller. Default to one
  page.
- **Achievement frameworks.** XYZ ("Accomplished X as measured by Y, by doing
  Z") is attributed to Laszlo Bock, ex-Google SVP People Ops, in *Work Rules!*
  (2015). STAR originates from DDI's Targeted Selection, credited to
  Dr. William C. Byham, **1974**. CAR has no traceable origin. **None of the
  three has been experimentally validated for resume outcomes.** They are
  structuring heuristics. Use them because they force specificity, not
  because they are proven.

---

## 8. Local Analyzer method

- **No open-source parser approximates a commercial ATS.** pyresparser's
  education and experience extraction is documented as inaccurate. GROBID is
  tuned for academic papers. LayoutLMv3 and Donut are document-understanding
  models, not resume parsers.
- **Therefore our Analyzer does not fake a parser.** It uses real text
  extraction (`pdftotext -layout`, `pdftotext` raw, `python-docx`) and then
  reasons over the extracted stream, which is exactly the input a real parser
  receives after stage 2. This is honest and it catches the failures that
  matter: dropped fields, garbled glyphs, merged employment blocks.
- **Free ground truth available:** O*NET download (CC BY 4.0), ESCO
  (EUPL 1.2).
- **Benchmark tools worth a sanity check, never a target:** Jobscan match
  rate, Teal, Enhancv. Each measures its own invented metric.

---
