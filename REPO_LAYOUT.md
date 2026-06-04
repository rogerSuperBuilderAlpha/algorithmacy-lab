# Repository layout & git push rules — READ BEFORE PUSHING

This working tree contains **two separate git repositories**. Pushing the wrong
work to the wrong remote is easy if you don't know this. The rule is simple, but
read it once.

## The two repositories

| If you are working in… | Git repo | Remote (`origin`) | Visibility |
|---|---|---|---|
| anything **except** `dissertation/` (PyPhi experiments, `org_frontier/`, code, etc.) | `iit-experiments` (this repo) | `github.com/rogerSuperBuilderAlpha/iit-experiments` | as-is |
| **`dissertation/`** (the three-paper dissertation) | `algorithmacy-dissertation` (a **nested, separate** repo at `dissertation/.git`) | `github.com/rogerSuperBuilderAlpha/algorithmacy-dissertation` | **PRIVATE** |

`dissertation/` is listed in this repo's `.gitignore`, so the outer
`iit-experiments` repo **cannot see or track** anything inside it. The dissertation
is versioned only by its own nested repo.

## The one rule

**Git always uses the nearest enclosing `.git` directory.** So *where you run the
command from decides which repo and which remote you touch* — not what you intend.

- Run git from **inside `dissertation/`** → you are in the **dissertation** repo →
  commits/pushes go to **`algorithmacy-dissertation`** (private).
- Run git from **anywhere else** in the tree → you are in **`iit-experiments`** →
  commits/pushes go to **`iit-experiments`**, and the dissertation is invisible
  (gitignored), so it can never be swept in by a stray `git add -A`.

## Check before you push (always)

```bash
git rev-parse --show-toplevel   # which repo am I in?
git remote -v                   # which remote will this push to?
git status                      # what would I be committing?
```

If `--show-toplevel` ends in `…/dissertation` you are pushing the **dissertation**;
otherwise you are pushing **iit-experiments**.

## Worked examples

**Pushing PyPhi / code work (→ iit-experiments):**
```bash
cd ~/iit-playground/pyphi-experiments        # outer repo (NOT dissertation/)
git add <files> && git commit -m "..."
git push origin main
```

**Pushing dissertation work (→ algorithmacy-dissertation, private):**
```bash
cd ~/iit-playground/pyphi-experiments/dissertation   # nested repo
git add <files> && git commit -m "..."
git push origin main
```

## Cautions

- **`cd` matters, not intent.** If you are sitting in `dissertation/` and run a
  commit meaning to save code, you will commit to the dissertation repo. Always
  check `git rev-parse --show-toplevel` first.
- **The two repos do not sync.** A push from `dissertation/` updates only the
  dissertation remote; a push from the outer tree updates only `iit-experiments`.
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
