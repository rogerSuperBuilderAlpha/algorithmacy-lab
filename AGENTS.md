# AGENTS.md — operating manual for agents working in this repo

> **Helping a newcomer who just opened this repo?** If they ask what this is, where to start, or what they
> can do, do not explain at length — open [`START_HERE.md`](START_HERE.md) and run the guided onboarding
> it scripts. This file is for operating *inside* the repo once they are moving.

How to navigate the lab, run it, verify a change, and land it. This is the tool-agnostic entry point for
any coding agent. Three files divide the work and cross-reference each other:

- **`AGENTS.md`** (this file) — how to operate *inside* the repo: remote visibility first, then map,
  commands, gates, and the land flow.
- **[`llms.txt`](llms.txt)** — how to *describe* the project to outside users at low token cost.
- **[`CLAUDE.md`](CLAUDE.md)** — the house writing style, the dissertation spine, and the git-push rules.

A nested `AGENTS.md` sits in the subtrees with their own local workflow (`org_frontier/`,
`org_frontier/research/`, `foundations/`, [`submissions/slacker_thirds/`](submissions/slacker_thirds/AGENTS.md),
and each program). Read the nested one when working there; it
points back here for the shared rules.

## Orient in three reads

1. **[`NOW.md`](NOW.md)** — this week's live deadlines and canonical drafts. Writing arms live under
   [`submissions/`](submissions/). Do not crawl `org_frontier/` looking for IGI, hospitality, or Lima.
2. **[`MAP.md`](MAP.md)** — the one-screen index: instrument, computational lab, empirical arms,
   submissions, machinery, live counts. Generated, always current.
3. **[`OVERVIEW.md`](OVERVIEW.md)** — what the lab argues and where it actually stands. Then this file
   for the operating rules. **[`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md)** is the registry of open threads,
   and `python tools/build_catalog.py --find "<keywords>"` places a question against everything already
   asked.

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

## Remote visibility — branch, push, and read the other work

A change that exists only in a local working tree is invisible to every other agent and researcher.
Three rules bind every session in this repo, before the first edit and again at every checkpoint.
`main` and `contrib` are protected: the push target is the working branch.

**1. Create the branch and push it before substantive work.** Fetch, read what is already in flight
(rule 3), then create the branch off `contrib` and push it immediately:

```bash
git fetch --all --prune
git checkout -b <topic>/<slug> origin/contrib
git push -u origin <topic>/<slug>
```

From a fork, `origin` is the fork and `upstream` is this repository: branch off `upstream/contrib` and
`git push -u origin <topic>/<slug>`. Open a draft pull request into `contrib` with the first commit so
the work is visible while it is still in progress. A session whose environment requires a particular
branch-name template uses that template; the base is still `contrib`, and the push is still immediate.

**2. Commit and push after every meaningful step.** A probe, an artifact, a protocol stage, a
checkpoint, a doc edit: commit it and `git push`. Remote state is the recoverable state. Do not leave
hours of work unpushed in the local tree.

**3. Read the other open branches and pull requests before starting, and again while working.**

```bash
git fetch --all --prune
git branch -r --sort=-committerdate
git for-each-ref --sort=-committerdate --format='%(committerdate:short) %(refname:short) %(subject)' refs/remotes | head -30
gh pr list --state open --limit 40
```

From a fork, list this repository's pull requests with
`gh pr list --repo rogerSuperBuilderAlpha/algorithmacy-lab --state open`. Repeat the check before a
long computation and before updating the pull request. When another branch or open pull request already
covers the question, join it or stop. Parallel sessions stay aligned by reading each other's remote
state, not by assuming the local tree is the only one.

The same three rules apply inside the nested `dissertation/` repo, against that repo's own remote.
Confirm the toplevel before every commit so a push cannot land in the wrong repository.

## Set up and run

```bash
python3 --version                              # PyPhi needs 3.10+; stock python3 is often 3.9 and will fail
python3.12 -m venv venv && source venv/bin/activate    # use any 3.10+ interpreter explicitly
pip install -r requirements.txt                # pulls PyPhi + phyid from git: needs network, a few minutes
```

Run everything from the repo root so `org_frontier.*` and `foundations.*` resolve. Confirm the instrument
before trusting any result — the controls assert that a known form reproduces its known verdict:

```bash
python -m org_frontier.classifier.validate     # must print "Instrument validated" (about two seconds)
python ci/reproduce.py instrument-controls     # the same gate as CI runs it
```

`python ci/reproduce.py` with no arguments is the full manifest (hundreds of checks, some of them
minutes each); that is the nightly job, not the confirm step.

For large cheap-feature panels, the lab-default **margin cascade** screens with a Probe-131 RF and
calls exact Φ only on the top **B=10%** most uncertain forms (OOF `|p−0.5|`, recomputed per panel):

```bash
python -m org_frontier.cascade.run --panel path/to/panel.csv          # B=0.10 default
python -m org_frontier.cascade.run --panel …/residual_panel_n4_unconstrained.csv --smoke
```

See [`org_frontier/cascade/README.md`](org_frontier/cascade/README.md). Do not freeze τ across sizes.

[`GETTING_STARTED.md`](GETTING_STARTED.md) walks the full path from a clean checkout to an open PR.

## Verify before you land

Four generators keep the navigable surface current, each with a `--check` that CI gates. Run the ones
your change touched, then confirm all four are clean:

```bash
python tools/build_index.py --check                       # the README directory
python tools/build_map.py --check                         # MAP.md
python tools/build_catalog.py --check                     # catalog.json, the searchable index
python org_frontier/research/build_research_index.py --check   # the research watch index
python ci/reproduce.py <check-name> …                     # the numbers your change registered
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
| a full question | `org_frontier/questions/q<NN>_<slug>/` | `python tools/build_catalog.py --find …`, then `python -m org_frontier.protocol.new_question` |
| an open thread | wherever its row in `OPEN_QUESTIONS.md` points | set the row to `claimed` in the same PR |
| a qualitative study | `org_frontier/qualitative/<slug>/` | `org_frontier/qualitative/template/` |
| a recurrence experiment | `org_frontier/recurrence/` | `crqa.py` and the existing Φ harnesses |
| a survey study | `org_frontier/survey/<study>/` | the arm and its first study in `org_frontier/survey/README.md` |
| an empirical arm from real input | the matching packet | `org_frontier/HANDOFF_PACKETS.md` |

Every number a submission reports must reproduce from a committed script: add a `name` / `cmd` / `expect`
entry to [`ci/reproduce.json`](ci/reproduce.json) and confirm `python ci/reproduce.py` passes locally.

## Land a change

The branch already exists on the remote before this point (**Remote visibility**, above). `main` and
`contrib` stay protected: every change is a pull request into `contrib`, and promotion to `main` is a
separate `contrib` → `main` PR.

```bash
# already done before the first edit, and again after every meaningful step:
git add <files> && git commit -m "…"
git push
gh pr create --base contrib --draft --title "…" --body "…"   # with the first commit, not at the end
# keep committing and pushing; mark the PR ready when the definition of done below is met
# CI green → merge into contrib → open the contrib→main promotion PR → merge → delete the branch
```

From a fork, `origin` is the fork: add this repository as `upstream`, branch off `upstream/contrib`,
and open the PR with `--repo rogerSuperBuilderAlpha/algorithmacy-lab` (the recipe is in
[`GETTING_STARTED.md`](GETTING_STARTED.md#8-open-a-pull-request)). The `update-directory` job cannot push
to a fork, so regenerate the indexes locally before pushing.

## Definition of done — the gate before opening a PR

- The instrument was validated on a known control before any comparison.
- Numbers come from a committed script and are registered in `ci/reproduce.json`; `python ci/reproduce.py`
  passes locally.
- All four index `--check`s are clean (`build_index.py`, `build_map.py`, `build_catalog.py`,
  `build_research_index.py`).
- Hypotheses were fixed before computing (`python ci/precommit_audit.py origin/contrib..HEAD` shows the
  order), and nulls and refutations are reported as results.
- Every result states the validation gap: it is evidence about the model, not about a real organization.
- Prose follows the house style in [`CLAUDE.md`](CLAUDE.md), its current rules: claim-first paragraphs,
  named agents in active voice, first person only for authorial labor, no emphasis-marker openers, and
  the flow self-check passed.
- Citations resolve to real DOIs / arXiv IDs / stable URLs; nothing is fabricated to fill a gap.
- The git target was confirmed with `git rev-parse --show-toplevel` before committing.
- The working branch was pushed before the first substantive edit and again after every meaningful step.
- Open remote branches and open pull requests were read before starting and again before the pull
  request was updated. The work does not duplicate a branch or pull request already in flight.

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
