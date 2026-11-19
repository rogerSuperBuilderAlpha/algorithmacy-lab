# Repository layout & git push rules — READ BEFORE PUSHING

This working tree contains **two separate git repositories**. Pushing the wrong
work to the wrong remote is easy if you don't know this. The rule is simple, but
read it once.

## The two repositories

| If you are working in… | Git repo | Remote (`origin`) | Visibility |
|---|---|---|---|
| anything **except** `dissertation/` (PyPhi experiments, `org_frontier/`, code, etc.) | `algorithmacy-lab` (this repo) | `github.com/rogerSuperBuilderAlpha/algorithmacy-lab` | as-is |
| **`dissertation/`** (the three-paper dissertation) | `algorithmacy-dissertation` (a **nested, separate** repo at `dissertation/.git`) | `github.com/rogerSuperBuilderAlpha/algorithmacy-dissertation` | **PRIVATE** |

`dissertation/` is listed in this repo's `.gitignore`, so the outer
`algorithmacy-lab` repo **cannot see or track** anything inside it. The dissertation
is versioned only by its own nested repo.

**A normal clone of the public repo has no `dissertation/` directory at all** — only the `.gitignore`
line for it. The tree appears solely when someone with access separately clones the private dissertation
repo into that path. If you do not see `dissertation/`, you are working purely in `algorithmacy-lab` and
the two-repo rule below has nothing to act on; it matters once the tree is present.

## The one rule

**Git always uses the nearest enclosing `.git` directory.** So *where you run the
command from decides which repo and which remote you touch* — not what you intend.

- Run git from **inside `dissertation/`** → you are in the **dissertation** repo →
  commits/pushes go to **`algorithmacy-dissertation`** (private).
- Run git from **anywhere else** in the tree → you are in **`algorithmacy-lab`** →
  commits/pushes go to **`algorithmacy-lab`**, and the dissertation is invisible
  (gitignored), so it can never be swept in by a stray `git add -A`.

## Check before you push (always)

```bash
git rev-parse --show-toplevel   # which repo am I in?
git remote -v                   # which remote will this push to?
git status                      # what would I be committing?
```

If `--show-toplevel` ends in `…/dissertation` you are pushing the **dissertation**;
otherwise you are pushing **algorithmacy-lab**.

## Worked examples

**Pushing PyPhi / code work (→ algorithmacy-lab):** `main` and `contrib` are branch-protected, so
changes go through a pull request into `contrib` (see [`PUBLISHING.md`](PUBLISHING.md) and **Remote
visibility** in [`AGENTS.md`](AGENTS.md)). Push the working branch before the first edit, and push
again after every meaningful step. Read the other remote branches and open pull requests first.

```bash
cd ~/iit-playground/pyphi-experiments        # outer repo (NOT dissertation/)
git fetch --all --prune
git branch -r --sort=-committerdate
gh pr list --state open
git checkout -b topic/my-change origin/contrib
git push -u origin topic/my-change          # immediately, before substantive edits
git add <files> && git commit -m "..."
git push                                    # again after every meaningful step
gh pr create --base contrib --draft         # with the first commit; mark ready when done
```

The owner can still merge as a repository admin while there is one maintainer. Promotion to `main` is a
separate `contrib` → `main` pull request.

**Pushing dissertation work (→ algorithmacy-dissertation, private):** the same three visibility rules
apply on this remote. The repo is not branch-protected, so a direct push to its `main` is accepted;
the default when a session is editing is still a working branch pushed before the edits and after
every meaningful step, after reading the other branches.

```bash
cd ~/iit-playground/pyphi-experiments/dissertation   # nested repo
git rev-parse --show-toplevel                # must end in dissertation
git fetch --all --prune && git branch -r --sort=-committerdate
git checkout -b topic/my-change
git push -u origin topic/my-change
git add <files> && git commit -m "..."
git push
```

## Cautions

- **`cd` matters, not intent.** If you are sitting in `dissertation/` and run a
  commit meaning to save code, you will commit to the dissertation repo. Always
  check `git rev-parse --show-toplevel` first.
- **The two repos do not sync.** A push from `dissertation/` updates only the
  dissertation remote; a push from the outer tree updates only `algorithmacy-lab`.
  If you changed both in one session, that is **two** separate commits and pushes.
- **Do not `git add dissertation/` in the outer repo.** It is gitignored on
  purpose; adding it back (e.g. with `git add -f`) would re-track the dissertation
  here and defeat the separation.
- **Never `git init` again inside either tree.** Both repos already exist
  (`./.git` and `./dissertation/.git`).

## Why it is set up this way

The dissertation needs its own private version history, separate from the public
experiments code. Nesting it under `dissertation/` (ignored by the outer repo,
tracked by its own private repo) keeps the working files in one convenient place
while routing each kind of work to the correct remote.
