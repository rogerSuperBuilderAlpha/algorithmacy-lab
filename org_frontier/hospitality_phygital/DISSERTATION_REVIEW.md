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

## 3. Review log

| date | reviewer | dissertation commit / branch | notes |
|---|---|---|---|
| 2026-08-07 | Roger Hunt (with Claude) | `main` @ `9abb3ea` | First pass. Library pass complete (1,766 cards); Paper 1–3 chapter pass still owed |

**Scope of the 2026-08-07 pass.** The pass read `research/library/` — the dissertation's reference
corpus — against the CFP and the locked abstract, and it produced
[`literature/FOUNDATION.md`](literature/FOUNDATION.md) plus 33 sourced additions to
[`literature/references.bib`](literature/references.bib). It did **not** yet read the Paper 1–3
manuscripts in `current/`, so the Paper 1 construct-gap argument and the Paper 2 affirmative case
remain unextracted. Section 2's checkboxes stay open for that reason.

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
- [ ] Revise [`CONSTRUCTS.md`](CONSTRUCTS.md) — pending the Paper 1 chapter pass
- [ ] Revise [`BRIDGE.md`](BRIDGE.md) — pending the same

### Blockers

None. The remaining work is the Paper 1–3 chapter pass, which is scheduled, not blocked.

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
