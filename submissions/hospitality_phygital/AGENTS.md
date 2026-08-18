# AGENTS.md — hospitality_phygital

Operating notes for agents working in this arm. Shared lab rules live in
[`../../AGENTS.md`](../../AGENTS.md). House style and the dissertation spine live in
[`../../CLAUDE.md`](../../CLAUDE.md).

## What this arm is

A conceptual / design-theory project for the *Hospitality & Society* phygital special issue. It
reuses algorithmacy and coordinative sovereignty. It does **not** add Φ probes on the critical path.

## First actions

1. Read [`README.md`](README.md) and [`PLAN.md`](PLAN.md).
2. Read [`ABSTRACT.md`](ABSTRACT.md) — the pitch is locked unless the user asks to change it.
3. Check whether `dissertation/` exists at the repo root.
   - **Missing:** continue with public lab sources; keep
     [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md) open; do not fabricate private content.
   - **Present:** run the dissertation review checklist and fill the log before freezing constructs.

## Editing rules

- Arm documents follow [`../../CLAUDE.md`](../../CLAUDE.md): no first person; plain declarative
  sentences; cut antithesis-machine and self-honesty tics.
- **The manuscript is exempt from the no-first-person rule**, by a ruling measured from venue
  exemplars and recorded in [`manuscript/REGISTER.md`](manuscript/REGISTER.md). *Hospitality &
  Society* prose uses the first person throughout, runs 150–250-word paragraphs and makes the cited
  author the subject of the sentence. The first full draft inherited repo style instead of measuring
  the venue, and read wrong. The exemption covers `manuscript/DRAFT.md` and the submission front
  matter, and expires with this submission. Everything else in the arm keeps house style.
- Do not demote IIT/Φ in bridge notes. The hospitality article may stay conceptual; that is audience
  fit, not a retreat from the lab thesis.
- State the validation gap whenever lab computational results are mentioned.
- Never `git add -f dissertation/` from the outer repo.

## Land changes

Branch off `contrib`, commit in `algorithmacy-lab`, push, open a PR into `contrib`. Confirm
toplevel and remote before every commit:

```bash
git rev-parse --show-toplevel
git remote -v
```

After adding or renaming navigable files, regenerate the map if the arm registration changed:

```bash
python tools/build_map.py
python tools/build_map.py --check
```

## Do not

- Conduct outreach to special-issue editors or APA organizers.
- Present in-silico Φ results as findings about real hospitality organizations.
- Replace the locked abstract's core claims without an explicit user request.
