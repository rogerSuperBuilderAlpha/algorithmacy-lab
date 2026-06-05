# Publishing in this project

This is an open research project, and the record it produces is meant to grow by contribution. Anyone
can publish here: an essay that argues a claim, a study that takes a question through the protocol, or
a correction to something already in the tree. Publishing means the work lands in the repository under
your name, after a public review that ends in a merge.

The review is the point, and it works differently from the usual kind. In a conventional journal two
or three anonymous readers judge a manuscript on whether its prose is persuasive, because they cannot
run it. Here every empirical claim reproduces from a committed script, so a reviewer can start by
reproducing it and only then argue about what it means. Review becomes mechanical first and editorial
second. The whole exchange happens in the open, on the pull request, signed by name, and stays in the
history as a permanent record of how the claim was checked. The aspiration is a standing group of
maintainers who sign off on submissions this way, a peer review that is reproducible by construction
and attributed rather than blind.

## What you can submit

- **An essay.** A piece of prose that argues a position about coordination, measurement, the
  literacy-or-algorithmacy thesis, or the method. It lands in [`org_frontier/essays/`](org_frontier/essays/).
  An essay that makes an empirical claim has to point at the script that backs it.
- **A study.** A research question taken through the six-stage protocol
  ([`org_frontier/protocol/RESEARCH_PROTOCOL.md`](org_frontier/protocol/RESEARCH_PROTOCOL.md)): review,
  literature, hypotheses fixed before computing, methods, a run against the exact-Φ instrument, and a
  paper. It lands under `org_frontier/questions/q<NN>_<slug>/`.
- **A probe.** A single exact-Φ experiment with a question, a pre-committed hypothesis, and a result,
  added to [`org_frontier/probes/PROBES.md`](org_frontier/probes/PROBES.md).
- **A correction.** A result that does not reproduce, a citation that does not resolve, a modeling
  choice that changes a verdict. Corrections are first-class work and are reviewed like any other
  submission.

## The standard every submission meets

Three commitments make the work reviewable. They are not style preferences. They are what lets a
stranger trust the result.

1. **Every number reproduces from a committed script.** If the essay says Φ = 2.0, a reviewer must be
   able to run a named module from the repo root and get 2.0. No number appears that cannot be traced
   to a run. A claim with no script behind it is an opinion and goes in a clearly opinion paragraph.
2. **Claims are fixed before computing, and the order is auditable.** A study commits its hypotheses
   and their nulls to git, with a decision rule for each, before the test code exists. The commit
   timestamps are the evidence that the analysis was not fit to the result after the fact. Nulls and
   refutations are reported as findings, not dropped.
3. **Scope is stated.** Results are in-silico: exact Φ on small Boolean models. They are evidence about
   the models, separated from claims about real organizations by a validation gap that computing harder
   never closes. Every submission says so where it could be mistaken for an empirical claim about firms.

Prose follows the house style in [`CLAUDE.md`](CLAUDE.md): no first person, plain declarative
sentences, citations that resolve to real sources, and a de-slop pass. The full contributor conventions
for code and probes are in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## The workflow

The repository keeps two branches that matter to contributors. `main` is the published record. `contrib`
is the integration branch where reviewed work collects before it is promoted. Contributors never push to
`main`.

1. **Fork** the repository and create a branch off `contrib`, named for the work
   (`essay/platform-as-form`, `study/q44-matrix-structure`).
2. **Write** the essay or run the study, meeting the three commitments above. Commit your hypotheses
   before your results so the history shows the order.
3. **Open a pull request into `contrib`** (not `main`). The PR description states the claim, lists the
   exact commands a reviewer runs to reproduce every number, and names the scope.
4. **Review happens on the PR**, in the open (next section). You respond to it in commits on the same
   branch.
5. **Sign-off.** A reviewer approves the PR, and it merges into `contrib`. Branch protection requires
   one approving review on every pull request.
6. **Promotion.** Periodically the owner promotes `contrib` to `main` through a pull request. A promotion
   is a publication event: the work is now part of the standing record.

This keeps `main` clean and gives every submission a staging buffer where it can be checked and revised
without disturbing the published record.

## The review

A reviewer works a submission in four passes, in order. The first two are mechanical and gate the rest.

1. **Reproduction.** Continuous integration runs this pass automatically. A submission registers each
   number it reports in [`ci/reproduce.json`](ci/reproduce.json) — a command and the output strings that
   must appear — and the `reproduce-the-numbers` workflow re-derives them on every pull request. A number
   that does not reproduce fails the check and blocks the merge until it is fixed or withdrawn. A reviewer
   can also run `python ci/reproduce.py` locally.
2. **Pre-commitment audit.** For a study, confirm the git history shows the hypotheses and decision
   rules committed before the result. Confirm nulls and refutations are reported, not buried.
3. **Argument.** Judge the claim itself: whether the model represents what it says it does, whether the
   modeling commitments are declared, whether the conclusion follows from the verdict, and whether the
   scope statement is honest about the validation gap.
4. **Prose.** Check the house style and that citations resolve.

Approval is given as a GitHub review on the PR, signed and public. Both `contrib` and `main` are
branch-protected: every change arrives as a pull request, nobody pushes to either branch directly, and a
merge needs one approving review. While the project has a single maintainer, that maintainer merges as a
repository admin, because GitHub does not let an author approve their own pull request; contributor
submissions still need the maintainer's review and approval. When a second maintainer joins, admin
exemption is turned off so every pull request, the owner's included, needs an approval, and the required
count rises as the group grows. The PR thread is the review record and is never squashed away, so anyone
can later see exactly how a published claim was checked and who vouched for it.

## Becoming a maintainer

Maintainers are contributors with a track record. Several merged submissions, careful reviews of other
people's work, and corrections filed honestly are how the role is earned. A maintainer can review and
sign off on submissions; the owner promotes `contrib` to `main` and grants the role. The intent is to
distribute sign-off authority as the group proves itself, so the review process becomes a community's
rather than one person's.

## A note on the two repositories

This working tree contains a separate, private dissertation repository nested at `dissertation/`,
gitignored and invisible here. Contributions go to the public `algorithmacy-lab` repository only. Where
you run git from decides the remote, so read [`REPO_LAYOUT.md`](REPO_LAYOUT.md) before committing, and
never `git add -f dissertation/`.
