# LinkedIn sourcing runner

`linkedin_source.py` runs at most three isolated portal workers in parallel.
It uses `maestri portal` commands and Python standard-library modules only.

Validate the query allocation:

```sh
python3 scripts/linkedin_source.py \
  --config scripts/linkedin-source.example.json plan
```

Run the complete query set:

```sh
python3 scripts/linkedin_source.py \
  --config scripts/linkedin-source.example.json run \
  --output-dir state/source-<hunt-id>
```

Use `--recency week` only after the past-24-hour run has no viable candidate.

Use `--query-limit 1 --cards-per-query 1` for a live smoke test.
The output directory must be new or empty.

The runner writes `events.jsonl`, a live `preflight.jsonl` triage queue, one
evidence file per candidate, and atomic `run.complete.json` when all workers
stop. Start triage when the first line reaches `preflight.jsonl`. Do not wait
for `run.complete.json`.
Candidate status has one of these values:

- `rejected`: a deterministic hard filter matched.
- `review`: location or contract wording needs human review.
- `preflight`: the candidate can enter the dossier requirement check.

The runner never logs in, reads credentials, submits an application, or sends
a recruiter message. It stops a worker when LinkedIn shows an authentication
or verification wall. Other portal workers continue.

Cache the LinkedIn identity once per hunt:

```sh
python3 scripts/cache_linkedin_identity.py \
  --portal "Profile Check" \
  --output state/<hunt-id>-linkedin-identity.json
```

Before Sieve, create the deterministic gate report and reduced review packet:

```sh
python3 scripts/resume_gate.py \
  --base resumes/base-en.tex \
  --tailored resumes/hunts/<hunt-id>/<application>/Lucas-Queiroz-Resume-en.tex \
  --pdf resumes/hunts/<hunt-id>/<application>/Lucas-Queiroz-Resume-en.pdf \
  --posting jobs/<application>.md \
  --manifest state/<application>-manifest.json \
  --identity-cache state/<hunt-id>-linkedin-identity.json \
  --claim-allowlist claim-allowlist.json \
  --report state/<application>-deterministic-gate.json \
  --review-packet state/<application>-review-packet.md \
  --sentinel state/<application>-deterministic-gate.complete.json
```

The application manifest is JSON with `application_id`, `language`,
`required_tokens`, and `preferred_tokens`. Quill and Sieve write their own
atomic sentinels with `worker_sentinel.py` after all required artifacts exist.
