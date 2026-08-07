# Dissertation review — required local pass

The nested private dissertation at `dissertation/` is **not** part of the public
`algorithmacy-lab` clone. A normal checkout has only the `.gitignore` line. This hospitality arm
still depends on that library for construct genealogy (especially Papers 1–2). **Complete this
review on a machine where the private repo is present before freezing
[`CONSTRUCTS.md`](CONSTRUCTS.md) and [`BRIDGE.md`](BRIDGE.md).**

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

- [ ] Where does Paper 1 say existing constructs fail to reach the **mediated triad**?
- [ ] Which neighbor constructs are distinguished from algorithmacy (HMC, algorithmic literacy,
      sensemaking, etc.)?
- [ ] What exact definition of algorithmacy should hospitality algorithmacy inherit?
- [ ] Which Paper 1 claims are hospitality-relevant without modification? Which need domain rewrite?

### Paper 2 — mediation lens

- [ ] How does Paper 2 argue Φ/IIT is a **principled tool** for exploring triadic coordination?
- [ ] What can be said in *Hospitality & Society* without leading on Φ mathematics?
- [ ] Which Paper 2 limitations must travel with any soft borrow (no worker measured; exploration
      not necessity proof)?
- [ ] Confirm the hospitality paper will **not** demote the apparatus even if it stays conceptual.

### Paper 3 — illustrative motifs only

- [ ] List any design operations or membership results that clarify augmentative vs substitutive
      mediation as metaphors — not as hotel findings.
- [ ] Explicitly mark each as **non-empirical for hospitality**.

### Sovereignty and agency overlap

- [ ] Cross-check dissertation language against
      [`../coordinative_sovereignty/`](../coordinative_sovereignty/) for consistency on standing,
      voice, bypass, and contestation.
- [ ] Note any dissertation-only nuance that should enter [`BRIDGE.md`](BRIDGE.md).

### Style and citation hygiene

- [ ] List claims that may be cited publicly (published or public-lab) vs claims that must be
      paraphrased without pointing at private files.
- [ ] Confirm no private verbatim blocks were pasted into this arm.

---

## 3. Review log (fill in locally)

| date | reviewer | dissertation commit / branch | notes |
|---|---|---|---|
| _YYYY-MM-DD_ | _name_ | _hash or branch_ | _one-line outcome_ |

### Load-bearing claims to carry into the hospitality paper

1. _claim — source path — paraphrase plan_
2. _
3. _

### Claims that do **not** transfer

1. _claim — reason_
2. _

### Updates required after this review

- [ ] Revise [`CONSTRUCTS.md`](CONSTRUCTS.md)
- [ ] Revise [`BRIDGE.md`](BRIDGE.md)
- [ ] Add verified citations to [`literature/references.bib`](literature/references.bib)
- [ ] Adjust [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md) section emphasis

### Blockers

_None yet / describe._

---

## 4. Agent instructions (cloud or local)

If `dissertation/` is **absent** (as in a typical cloud agent checkout of `algorithmacy-lab`):

1. Do **not** invent dissertation contents.
2. Build and edit the public baseline library from lab sources only.
3. Leave this checklist open.
4. Tell the user that construct freeze waits on a local dissertation pass.
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
