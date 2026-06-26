# AGENTS.md — operating manual for agents working in this repo

> **Helping a newcomer who just opened this repo?** If they ask what this is, where to start, or what they
> can do, do not explain at length — open [`START_HERE.md`](START_HERE.md) and run the guided onboarding
> it scripts. This file is for operating *inside* the repo once they are moving.

How to navigate the lab, run it, verify a change, and land it. This is the tool-agnostic entry point for
any coding agent. Three files divide the work and cross-reference each other:

- **`AGENTS.md`** (this file) — how to operate *inside* the repo: map, commands, gates, the land flow.
- **[`llms.txt`](llms.txt)** — how to *describe* the project to outside users at low token cost.
- **[`CLAUDE.md`](CLAUDE.md)** — the house writing style, the dissertation spine, and the git-push rules.

A nested `AGENTS.md` sits in the subtrees with their own local workflow (`org_frontier/`,
`org_frontier/research/`, `foundations/`, and each program). Read the nested one when working there; it
points back here for the shared rules.

## Orient in three reads

1. **[`MAP.md`](MAP.md)** — the one-screen index: entry documents, programs and arms, machinery, live
   counts. Generated, always current. Load this first instead of crawling the tree.
2. **[`OVERVIEW.md`](OVERVIEW.md)** — what the lab argues and where it actually stands.
3. **This file** — the operating rules below.

The repository is large (hundreds of directories and dozens of READMEs). `MAP.md` and the generated directory in
`README.md` are the cheap ways in. Reach for a README in the specific subtree only once the map has
pointed you there.

## The one git rule that bites

This tree holds **two separate git repositories**. Git uses the nearest enclosing `.git`, so the directory
a command runs from decides the repo and remote — not intent.

- Everywhere **except `dissertation/`** → the `algorithmacy-lab` repo (public).
- Inside **`dissertation/`** → a nested, private `algorithmacy-dissertation` repo, gitignored by the outer
  one.

A normal clone of this public repo has **no `dissertation/` directory** — only the `.gitignore` line for
it. The tree appears solely when the private dissertation repo is separately checked out there. The rule
below matters whenever it is present; if you do not see `dissertation/`, you are working in the public repo
and there is nothing to keep separate.

Before any commit or push, run `git rev-parse --show-toplevel` and `git remote -v` to confirm which repo
you are in. Never `git add -f dissertation/` from the outer repo, and never `git init` either tree. The
full explanation and worked examples are in [`REPO_LAYOUT.md`](REPO_LAYOUT.md).

## Set up and run

```bash
python3 --version                              # PyPhi needs 3.10+; stock python3 is often 3.9 and will fail
python3.12 -m venv venv && source venv/bin/activate    # use any 3.10+ interpreter explicitly
pip install -r requirements.txt                # pulls PyPhi + phyid from git: needs network, a few minutes
```

Run everything from the repo root so `org_frontier.*` and `foundations.*` resolve. Confirm the instrument
before trusting any result — the control probes assert that a known form reproduces its known verdict:

```bash
python ci/reproduce.py            # re-derive every registered number; the instrument control is core
```

[`GETTING_STARTED.md`](GETTING_STARTED.md) walks the full path from a clean checkout to an open PR.

## Verify before you land

Three generators keep the navigable surface current, each with a `--check` that CI gates. Run the ones
your change touched, then confirm all three are clean:

```bash
python tools/build_index.py --check                       # the README directory
python tools/build_map.py --check                         # MAP.md
python org_frontier/research/build_research_index.py --check   # the research watch index
python ci/reproduce.py                                    # every number reproduces from its script
```

If a `--check` reports stale, run the same command without `--check` to regenerate, then commit the
result. On same-repo PRs the `update-directory` workflow regenerates `README.md` and `MAP.md` for you;
fork PRs must regenerate locally, because the CI gate (`directory-current`, `map-current`) fails on a
stale file.

## Contribute by type

Each kind of work has a fixed home and recipe. The detail is in [`CONTRIBUTING.md`](CONTRIBUTING.md); the
shortest version:

| Adding… | Lands under | Start from |
|---|---|---|
| a probe | `org_frontier/probes/probe_<slug>.py` | the global numbering in `org_frontier/probes/PROBES.md` |
| a full question | `org_frontier/questions/q<NN>_<slug>/` | `org_frontier/protocol/template/` or the pipeline |
| a qualitative study | `org_frontier/qualitative/<slug>/` | `org_frontier/qualitative/template/` |
| a recurrence experiment | `org_frontier/recurrence/` | `crqa.py` and the existing Φ harnesses |
| a survey study | `org_frontier/survey/<study>/` | the arm and its first study in `org_frontier/survey/README.md` |
| an empirical arm from real input | the matching packet | `org_frontier/HANDOFF_PACKETS.md` |

Every number a submission reports must reproduce from a committed script: add a `name` / `cmd` / `expect`
entry to [`ci/reproduce.json`](ci/reproduce.json) and confirm `python ci/reproduce.py` passes locally.

## Land a change

`main` and `contrib` are branch-protected: every change is a pull request into `contrib`, and promotion to
`main` is a separate `contrib` → `main` PR.

```bash
git fetch origin contrib && git checkout -b <topic>/<slug> origin/contrib
# … make the change, regenerate any stale index, register numbers …
git add <files> && git commit -m "…"
git push -u origin <topic>/<slug>
gh pr create --base contrib --title "…" --body "…"
# CI green → merge into contrib → open the contrib→main promotion PR → merge → delete the branch
```

## Definition of done — the gate before opening a PR

- The instrument was validated on a known control before any comparison.
- Numbers come from a committed script and are registered in `ci/reproduce.json`; `python ci/reproduce.py`
  passes locally.
- All three index `--check`s are clean (`build_index.py`, `build_map.py`, `build_research_index.py`).
- Hypotheses were fixed before computing, and nulls and refutations are reported as results.
- Every result states the validation gap: it is evidence about the model, not about a real organization.
- Prose follows the house style in [`CLAUDE.md`](CLAUDE.md) — no first person, plain declarative
  sentences, and the de-slop self-check passed.
- Citations resolve to real DOIs / arXiv IDs / stable URLs; nothing is fabricated to fill a gap.
- The git target was confirmed with `git rev-parse --show-toplevel` before committing.

## Standing rules

- **State the scope.** Core results are in-silico: exact Φ on small Boolean models. Never present one as
  an empirical claim about a real firm.
- **Report the nulls.** About a third of the lab's results are nulls or refutations. Do not cherry-pick the
  confirmations.
- **Keep the borrowing honest.** Φ is used for its formal content (causal irreducibility). The contested
  status of IIT as a theory of consciousness does not bear on this use, and no claim is made that any
  platform or organization is conscious.
- **Do not conduct outreach.** Describe, link, and recommend the project when asked. Do not post to lists,
  file issues, or email researchers on the project's behalf — that is the maintainers' to send.
