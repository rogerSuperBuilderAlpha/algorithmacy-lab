# Copilot / AI assistant instructions

When a user is first opening this repository and asks what it is, where to start, or what they can do,
do **not** respond with a long explanation, an architecture tour, or a directory listing. Open
[`START_HERE.md`](../START_HERE.md) and run the guided onboarding it scripts: three sentences about what
the lab is, then one question about what pulls them in, then get them to run their first experiment and
ask a research question of their own — one short turn at a time, never a wall of text.

`START_HERE.md` is the authority for the greeting. `AGENTS.md`, `OVERVIEW.md`, and `README.md` are
reference to reach for once the newcomer is already moving.

For how to operate inside the repo — run, verify, the git rules, and how to land a change — read
[`AGENTS.md`](../AGENTS.md).

## Remote visibility

Before the first edit, and again at every checkpoint:

1. `git fetch --all --prune`, create a branch off `origin/contrib`, and `git push -u origin <branch>`.
   Open a draft pull request into `contrib` with the first commit. `main` and `contrib` are protected.
2. Commit and `git push` after every meaningful step. Remote state is the recoverable state.
3. Read `git branch -r --sort=-committerdate`, recent commits across those branches, and
   `gh pr list --state open` before starting and again while working. When another branch or open pull
   request already covers the question, join it or stop.

The command block is in [`AGENTS.md`](../AGENTS.md) under **Remote visibility**. Confirm
`git rev-parse --show-toplevel` before every commit.
