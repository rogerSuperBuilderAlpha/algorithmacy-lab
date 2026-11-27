> **First contact with a newcomer.** If someone is just opening this repo and asks what it is, where to
> start, or what they can do, do **not** reply with a long explanation, an architecture tour, or a
> directory dump. Open [`START_HERE.md`](START_HERE.md) and run the guided onboarding it scripts — three
> sentences, then one question, then get them computing. That file is the authority for the greeting.
>
> To set up and compute the first verdict, run `python3 tools/start.py`. An assistant that cannot run code
> follows the "No shell" section of `START_HERE.md`.
>
> For how to navigate, run, verify, and land a change, read [`NOW.md`](NOW.md), [`AGENTS.md`](AGENTS.md),
> and [`MAP.md`](MAP.md). Writing arms live under [`submissions/`](submissions/). This file is the writing
> style, the dissertation spine, and the git-push rules.

# Writing style (applies to all prose in this repo)

**Authority:** [sciwrite](https://github.com/labarba/sciwrite) (Lorena A. Barba, CC BY 4.0), which
encodes Kristin Sainani's *Writing in the Sciences* course. The maintainer's adapted copy is the
`writing-in-house-style` skill; contributors without it can install upstream with
`/plugin install sciwrite --marketplace labarba/sciwrite`. This replaces the earlier section built on
*Academy of Management Annals* 20(2) (ruling of 27 Nov 2026); that reading stays in
`dissertation/current/paper1/exemplars/annals_20_2/FLOW_AND_COHESION.md` as background, not as rules.

Write to, and review against, six passes:

1. **Clutter.** Cut dead-weight phrases ("due to the fact that" → "because", "in order to" → "to"),
   throat-clearing ("It is worth noting that"), redundancies ("completely eliminate"), empty openers
   ("There are several studies that…"), and negatives a single word can replace.
2. **Voice and verbs.** Name who did what: active voice, "I" for solo work, "we" for coauthored work.
   Resurrect smothered verbs ("performed an analysis of" → "analyzed"). Passive is fine when the actor
   is unknown or irrelevant.
3. **Sentence and paragraph architecture.** No more than about 12 words between subject and verb;
   split sentences carrying three or more independent ideas; fix dangling modifiers; give a bare
   "This" its noun. Each paragraph has one main idea and, in argument sections, a topic sentence; each
   sentence links to the one before; transitions match the logic. Sections do their job: the
   Introduction states the gap and what the paper does; the Discussion opens with the answer and
   states limitations.
4. **Terminology.** The Banana Rule: once a term is defined, hold its name fixed everywhere. Define
   each acronym at first use in the abstract and in the body; cut acronyms made for convenience.
5. **Numbers and citations.** Numbers agree between text, tables and figures. A statistic cited only
   to a review is traced to its primary source. Every citation is verified against its source.
6. **Abstract structure.** Field → background → problem → result ("Here I show") → what it changes →
   context, within the venue's word limit.

Never change the strength of a claim or invent a number or citation; leave `[citation]` or
`[NEEDS: …]`. Leave a clear sentence alone even if a rule could be stretched to cover it. Reviews
report findings tagged CRITICAL / MAJOR / MINOR, each with its location, the original and a concrete
revision.


---

# Dissertation guiding structure (the spine — do not drift from this)

The three-paper dissertation makes ONE affirmative argument, and every edit serves it:

- **Paper 1 — a literature review that finds space for algorithmacy.** It reviews the existing
  constructs, shows they do not reach the mediated triad, and names the construct that fills the gap.
- **Paper 2 — argues that integrated information (Φ / IIT) is a great tool for exploring the mediated
  triad.** This is an affirmative case FOR the tool: Φ is a principled, powerful lens on whether and how
  a coordination form is irreducible.
- **Paper 3 — walks through a bunch of experiments** with that tool: major-complex membership, the
  design operations, the worked case models.

**Make the argument. Do NOT demote IIT.** Φ/IIT are never to be called decorative, hollow, unnecessary,
or "a calculator," and "demote the apparatus" is NOT an option on the table. That a cheap factorization
test reaches the same verdict on some field cases does not mean Φ does no work — the contribution is the
principled exploration IIT enables, not a claim that Φ is necessary or beats cheap tests. Committee or
reviewer pushback toward demoting the apparatus is adversarial stress-testing to ANSWER by making the
affirmative case better, not a mandate to gut the thesis.

**Altitude.** Be modest about what is *proven* (no worker is measured; irreducibility is *explored*, not
established as necessary) and confident about the *thesis* (algorithmacy fills a real gap; IIT is a great
tool for exploring it; the experiments are worth running). Modest ≠ self-defeating. Never trade the
tool's value away to look humble.

---

# Repository layout & git pushes (IMPORTANT — applies every session)

This tree holds **two separate git repositories**. See `REPO_LAYOUT.md` for the full
explanation. The short version, which must be respected on every git operation:

- **`dissertation/`** is its own **nested, private** repo (`dissertation/.git`) whose
  remote is `github.com/rogerSuperBuilderAlpha/algorithmacy-dissertation` (PRIVATE).
  It is gitignored by the outer repo.
- **Everything else** belongs to the outer repo `algorithmacy-lab`, remote
  `github.com/rogerSuperBuilderAlpha/algorithmacy-lab`.

Git uses the nearest enclosing `.git`, so **the directory a command runs from decides
the repo and remote** — not intent. Before any commit or push:

1. Run `git rev-parse --show-toplevel` and `git remote -v` to confirm which repo/remote.
2. Dissertation work pushes to `algorithmacy-dissertation`; PyPhi/code work pushes to
   `algorithmacy-lab`. Never mix them.
3. State the target remote to the user before pushing.
4. Never `git add -f dissertation/` in the outer repo, and never re-`git init` either tree.
5. `algorithmacy-lab`'s `main` and `contrib` branches are protected: direct pushes are rejected, so
   land changes through a pull request into `contrib`. One approving review is required; the owner can
   merge as admin while there is one maintainer. The nested `dissertation/` repo is not protected and
   still takes direct pushes. See `PUBLISHING.md`.

## Remote visibility — every session, before the first edit

Work that sits only in a local tree is invisible to the other agents and researchers in this repo.
Three rules apply to every session, in both git repositories. The full command block is in
[`AGENTS.md`](AGENTS.md) under **Remote visibility**.

1. **Branch and push before substantive work.** `git fetch --all --prune`, create a branch off
   `contrib`, and `git push -u origin <branch>` before editing. Open a draft pull request into
   `contrib` with the first commit.
2. **Commit and push after every meaningful step.** A probe, an artifact, a protocol stage, a
   checkpoint, a paragraph: commit it and `git push`. Remote state is the recoverable state.
3. **Read the other open branches and pull requests before starting, and again while working.**
   `git branch -r --sort=-committerdate`, recent commits across those branches, and `gh pr list`.
   Repeat the check before a long computation and before updating the pull request. When another
   branch or open pull request already covers the question, join it or stop.

The push target in `algorithmacy-lab` is the working branch. Confirm
`git rev-parse --show-toplevel` before every commit so dissertation work and lab work cannot cross.
