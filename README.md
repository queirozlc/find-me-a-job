# career

Job hunt workspace for the `/find-me-a-job` skill. The skill source lives in
`skill/find-me-a-job/`.

## Requirements

- Clone this repo to `~/career`. The skill uses that path.
- Claude Code or Codex.
- Maestri, for the canvas, notes, and worker seats.
- Python 3, for `scripts/`.

## Install the skill

Paste this prompt into Claude Code or Codex, from `~/career`:

```text
Install the find-me-a-job skill from this repo.

1. Confirm the repo is at ~/career. If not, stop and tell me.
2. Create ~/.agents/skills/ if it does not exist.
3. If ~/.agents/skills/find-me-a-job exists and is not a symlink to
   ~/career/skill/find-me-a-job, show me what is there and ask before you
   replace it.
4. Symlink ~/.agents/skills/find-me-a-job -> ~/career/skill/find-me-a-job.
5. Symlink ~/.claude/skills/find-me-a-job -> ~/.agents/skills/find-me-a-job
   (Claude Code). For Codex, do the same under ~/.codex/skills/.
6. Verify that SKILL.md resolves through each symlink.
7. Tell me to restart the agent, then run /find-me-a-job. With no
   find-me-a-job.md config, the skill runs its init flow first.
```

The symlink keeps one source. Edits to the skill are edits to this repo.
