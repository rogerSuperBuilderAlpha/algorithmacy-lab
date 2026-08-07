# Dissertation review — timeboxed local pass

The nested private dissertation at `dissertation/` is **not** part of the public
`algorithmacy-lab` clone. A normal checkout has only the `.gitignore` line. This hospitality arm
draws on that library for construct genealogy (especially Papers 1–2).

> **Scope change (2026-08-07).** This pass no longer gates the construct freeze. With 28 days to
> the submission window, a gate that only one machine can open is a schedule risk, and it is not
> load-bearing: [`CONSTRUCTS.md`](CONSTRUCTS.md) is already fully specified from the locked abstract
> and the public lab. Freeze the constructs, then run this pass **inside a one-day box, in parallel
> with drafting**, to sharpen the Paper 1 gap argument and fix citation genealogy. If it contradicts
> a frozen definition, amend the definition — that is cheap. A stalled draft is not. See
> [`PLAN.md`](PLAN.md) §5.A.

Do not copy private chapter prose into this public tree. Log paths, claims, and paraphrase notes
here. See [`../../REPO_LAYOUT.md`](../../REPO_LAYOUT.md).

---

## 0. Mount the dissertation (local)

From the algorithmacy-lab root on a machine with access to the private remote:

```bash
# Confirm you are in the public lab root
git rev-parse --show-toplevel
git remote -v
# expect: …/algorithmacy-lab

# If dissertation/ is missing, clone the private repo into the ignored path
git clone git@github.com:rogerSuperBuilderAlpha/algorithmacy-dissertation.git dissertation

# Confirm the nested repo (separate .git)
cd dissertation
git rev-parse --show-toplevel
git remote -v
# expect: …/algorithmacy-dissertation
cd ..
```

If the dissertation already lives elsewhere, symlink or copy is fine so long as
`/path/to/algorithmacy-lab/dissertation/` resolves and remains gitignored by the outer repo.

**Never** run `git add -f dissertation/` from the outer tree.

---

## 1. Orient (read before extracting)

Typical targets (adjust if the private tree uses different names — record actual paths in the log):

| focus | look for |
|---|---|
| Spine / overview | top-level README, overview, or three-paper map |
| Paper 1 | literature review; construct gap; algorithmacy named against neighbors |
| Paper 2 | affirmative case for integrated information / Φ as a lens on mediated coordination |
| Paper 3 | experiments, design operations, worked cases — motifs only for this H&S paper |
| Shared glossary | any constructs file that defines algorithmacy, triad, literacy |

Also re-read the public spine rules in [`../../CLAUDE.md`](../../CLAUDE.md): one affirmative
argument; do not demote IIT; modest about proof; confident about the thesis.

---

## 2. Checklist — extract for hospitality

Work through each item. Mark `[x]` only when the log row below is filled.

### Paper 1 — construct space

- [x] Where does Paper 1 say existing constructs fail to reach the **mediated triad**? Paper 1 sets
      the mediated triad against the *moderated dyad*, where a third element shapes a channel the two
      parties still own. The dyadic constructs describe a party relating to a system; none reaches a
      counterpart one must coordinate *through* a constitutive third party.
- [x] Which neighbor constructs are distinguished? CMC competence, human-machine communication,
      AI-mediated communication, the literacies, algorithm sensemaking, algorithmic competency —
      and, as the nearest structural rival, boundary organizations, which confer voice. The platform
      variant is distinguished by withholding voice, not by absence of membership.
- [x] What exact definition should hospitality algorithmacy inherit? The definition lives in Paper 2,
      not Paper 1 (see below), and it is now recorded in [`CONSTRUCTS.md`](CONSTRUCTS.md).
- [x] Which claims are hospitality-relevant without modification? The **standing series** — every
      settled coordination form specifies what flows back to the coordinated party, and the platform
      form is the only one stated without a return. Hospitality has always specified a return, which
      makes the borrow sharp. Needs domain rewrite: the six-question template and the grading matrix,
      which are review apparatus and should not enter an H&S article.

### Paper 2 — the competency derivation

Paper 2 is *The Competency a Form Demands: Algorithmacy and the Co-optation Column*. The checklist
below was written for a Φ-based Paper 2 that is no longer current; it is answered as the paper stands.

- [x] Where does the competency come from? Derived, not asserted: a coordination form owes its
      parties accountability, predictability, and common understanding; a facet is what a party does
      in the absence of a withheld condition. Three facets admit — asymmetric interpretation, intent
      specification, temporal tracking.
- [x] What is the main result? The individual/institutional division. Understanding and
      predictability can be supplied privately; accountability cannot, because it is a relation
      between parties rather than a state a party can be in. **This is the hospitality paper's
      reason for holding two constructs.**
- [x] Which limitations must travel with any borrow? Rival explanations named and not defeated
      (prior expertise, task mix, hours, general self-efficacy); the facets are a derivation, not a
      finding; nothing measures a person; the account is scoped to arrangements where all three
      withholdings hold together.
- [x] Does the borrow demote the lab thesis? No. Paper 2 carries no Φ, so the hospitality article's
      conceptual register is continuous with its genealogy rather than a retreat from it.

### Paper 3 — designed, unfielded

- [x] Paper 3 is a qualitative study: protocol, pre-committed coding scheme, three instruments, and
      an IRB package. **Status: designed, unfiled, unfielded. No data exists and no participant has
      been approached.**
- [x] Marked non-empirical for hospitality. The only legitimate use is §8 future research — the
      empirical arm for the construct is already designed. Never imply a finding.

### Sovereignty and agency overlap

- [x] Cross-checked. The dissertation's individual/institutional division gives coordinative
      sovereignty a derivation rather than a definition: standing is the thing competence
      structurally cannot reach. Voice is the operative term in both trees.
- [x] Dissertation-only nuance now in [`BRIDGE.md`](BRIDGE.md): the standing series, the
      boundary-organization rival, the three integrating conditions, the facet derivation, and the
      scope boundary that becomes the augmentative/substitutive condition.

### Style and citation hygiene

- [x] Everything carried across is paraphrased argument plus published sources. Dissertation-internal
      objects (the grading matrix, the six-question template, the seventh row, the standing series'
      interior order) are described, not quoted, and flagged as the dissertation's own proposals
      where they are not settled.
- [x] No private verbatim blocks in this arm. Checked on the 2026-08-07 pass.

### Discrepancy found on the dissertation side — reported, not touched

`current/spine/` (one-pager, front matter, narrative, conclusion) describes Paper 2 as a Φ formal-model
paper and Paper 3 as a population study over the 4,096-form family. The manuscripts in
`current/paper2/` and `current/paper3/` are a competency derivation and a qualitative design. The
spine files were last modified by a directory reorganization on 2026-07-28 and none names Paper 2's
actual title. The spine appears to describe a superseded plan. **This arm does not edit the
dissertation repo — flagging only.**

---

## 3. Review log

| date | reviewer | dissertation commit / branch | notes |
|---|---|---|---|
| 2026-08-07 | Roger Hunt (with Claude) | `main` @ `9abb3ea` | Library pass complete (1,766 cards) |
| 2026-08-07 | Roger Hunt (with Claude) | `main` @ `9abb3ea` | Chapter pass complete (Papers 1–3, spine). One conflict with the locked abstract; one dissertation-side discrepancy reported |

**Scope.** Two passes, both on 2026-08-07. The **library pass** read `research/library/` (1,766
reference cards) and produced [`literature/FOUNDATION.md`](literature/FOUNDATION.md) Part 1 plus 33
sourced additions to [`literature/references.bib`](literature/references.bib). The **chapter pass**
read `current/paper1/PAPER.md`, `current/paper2/PAPER.md`, `current/paper3/`, and `current/spine/`,
and produced FOUNDATION.md Part 2 plus corrections to [`BRIDGE.md`](BRIDGE.md),
[`CONSTRUCTS.md`](CONSTRUCTS.md), and [`design_principles.md`](design_principles.md).

**The one thing that needs a decision.** Paper 2 derives that contestation cannot be a facet of the
competency, because accountability is a relation between parties rather than a state a party can be
in. [`ABSTRACT.md`](ABSTRACT.md) puts "contest" inside the competence definition. The abstract is
locked, so the resolution is the maintainer's — see FOUNDATION.md Part 2.

### Load-bearing claims carried into the hospitality paper

1. **The host is the co-opted party.** The library's Airbnb cluster documents a platform capturing
   the listing, calendar, and guest relationship, steering the host through pricing and ranking, and
   conferring no standing. Paraphrase plan: this is *Who Hosts the Guest?* answered from the host's
   side, and it is the paper's best-evidenced claim. Cite the public sources (Cheng and Foley 2019;
   Roelofsen and Minca 2018; Bosma 2022; Leick et al. 2024), never the private cards.
2. **Control runs through measurement rather than command.** Rahman (2021) and the platform-labor
   cluster establish that steering works precisely because it must not look like instruction.
   Paraphrase plan: this is the mechanism behind substitutive hospitality — the guest and employee
   are directed without anyone issuing a direction.
3. **Competence without standing is the recurring shape.** Hosts reverse-engineer, professionalize,
   and comply, and none of it converts into authority over the rules. Paraphrase plan: this is
   exactly why hospitality algorithmacy (competence) needs coordinative sovereignty (standing) as a
   separate construct — the library shows competence alone does not deliver influence.

### Claims that do **not** transfer

1. **Anything Φ-shaped.** The library's formal apparatus grades models of coordination. The
   hospitality article stays conceptual, per [`PLAN.md`](PLAN.md) §9.
2. **The dissertation's Lipsky verdict.** The dissertation logs Street-Level Bureaucracy as
   orthogonal because its platform worker maps onto Lipsky's client rather than the discretion-
   holder. In a hotel that mapping reverses and Lipsky applies natively — do not carry the
   orthogonality finding across. See [`literature/FOUNDATION.md`](literature/FOUNDATION.md)
   finding 5.
3. **Paper 1's fourth-form adjudication.** The cell structure, the co-optation naming contest, and
   the rival-carving argument are dissertation-internal machinery. The hospitality paper takes the
   structure and leaves the adjudication.

### Updates required after this review

- [x] Add sourced citations to [`literature/references.bib`](literature/references.bib) — 33 added
- [x] Adjust [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md) section emphasis — §2 gains platform
      hospitality, §5 gains the folk-theory evidence base, §6 gains the three published nulls,
      §7 leads on Folger and on infrastructure invisibility
- [x] Revise [`CONSTRUCTS.md`](CONSTRUCTS.md) — inherited definition, three facets, and the open
      contestation decision recorded
- [x] Revise [`BRIDGE.md`](BRIDGE.md) — transfer table rebuilt against the actual Papers 1–3

### Blockers

None on the review. One decision is owed on the abstract's contestation clause before
[`CONSTRUCTS.md`](CONSTRUCTS.md) can be frozen cleanly.

---

## 4. Agent instructions (cloud or local)

If `dissertation/` is **absent** (as in a typical cloud agent checkout of `algorithmacy-lab`):

1. Do **not** invent dissertation contents.
2. Build and edit the public baseline library from lab sources only.
3. Leave this checklist open and keep drafting — the freeze does not wait on it.
4. Tell the user that the genealogy pass is still owed and which claims would benefit from it.
5. Optionally prepare a patch list of questions for the human reviewer to answer in the log above.

If `dissertation/` **is** present:

1. Run `git rev-parse --show-toplevel` inside `dissertation/` and confirm the private remote.
2. Complete sections 2–3 of this file in the **public** arm (this file is tracked by
   `algorithmacy-lab`).
3. Commit review-log updates from the outer repo only.
4. Push dissertation-side edits (if any) only from inside `dissertation/`, to the private remote,
   as a separate operation with the target remote stated first.

---

## 5. Done criterion for this file

This review is complete when every Paper 1–2 checkbox is marked, the log has at least three
load-bearing claims with paraphrase plans, and [`BRIDGE.md`](BRIDGE.md) has been updated in the
same PR or a follow-up PR.
