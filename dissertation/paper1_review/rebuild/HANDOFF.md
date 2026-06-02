# Rebuild handoff (state for the next context window)

## Immediate next task
Restyle Paper 1's draft to genuinely match the Nagel voice. The current draft passes the
mechanical CLAUDE.md checks but reads as **plain academic, not Nagel-plain**. Fix the voice.

### The style diagnosis (what is wrong, concretely)
The prose avoids the banned tics but commits a different sin: abstraction-stacking and clever
parallelism in place of blunt concreteness. Symptoms to hunt and kill:
- Abstract nominalizations as subjects: "the context facet is a parameter on what passes...",
  "each terminates in the counterpart", "the integrative architecture survives the shift".
  Nagel uses concrete subjects and active verbs.
- "The X is the Y" definitional cadence repeated for rhythm.
- Clever antithetical pairs ("a parameter on an exchange cannot hold a producer of one").
- Long clear sentences where a short blunt one would land harder.
- Latinate vocabulary (constitute, parameterize, terminate, instantiate) over plain words.

### What Nagel actually does (the target)
Read /Users/ludwitt/Downloads/Nagel-What-is-it-like-to-be-a-bat.pdf. Short blunt opening
claims ("Consciousness is what makes the mind-body problem really intractable"). Mostly short
declaratives. Concrete words. Contrast by repetition ("Without consciousness... With it..."),
not ornament. The difficulty is in the idea, not the sentence. NOTE: Nagel uses first person
heavily; the user FORBIDS it here (CLAUDE.md rule 4) — keep the subject the paper/construct/
the thing, but otherwise match Nagel.

### How to run the style pass (recommendation)
Do it yourself, section by section, NOT via parallel agents — the agents produced this
plain-academic register and will likely reproduce it. Rewrite each paragraph: shorten, swap
abstract subjects for concrete ones, cut the clever pairs, lead blunt. Preserve every
citation, number, and claim (style-only). Verify with the same checks (0 first person; em-dash
count; citation resolution unchanged).

---

## Project state
**Goal:** rebuild the whole dissertation from scratch, paper by paper, staged
(research → outline → draft → review), per the user. Optimize for clean writing + sourcing.

**Branch:** `rebuild/paper-by-paper` (off `main`). Repo: `/Users/ludwitt/iit-playground/pyphi-experiments`.
Python venv: `~/iit-playground/venv-4.0/bin/python` (for Papers 2-3 computational work later).

**Other branches:** `main` (canonical, has the OLD revised dissertation); `style/plain-prose`
(a plain-prose rewrite of the OLD Paper 1-3 + framing, unmerged — reference only).

**CLAUDE.md** at repo root holds the writing rules (Nagel plain style, no first person).

### Locked decisions for the rebuild
- **Full blank slate**, but findings/contributions largely carry over; craft + sourcing upgrade.
- **Variance puzzle is CUT** everywhere. Do not motivate through "equivalently-positioned
  workers get divergent outcomes."
- **Paper 1 is framing-light:** it carries the CONCEPTUAL distinction only. NO IIT, NO Φ, NO
  formal model, NO game theory, NO "five structural properties" set — those are Paper 2.
- **The spine:** oracy → literacy → algorithmacy. Existing constructs = MODERATED DYAD
  (a medium shapes a two-party exchange; reduces to the pair). The phenomenon = MEDIATED TRIAD
  (a third party constitutes the coordination, commits binding determinations, holds its own
  authored interest, keeps the parties apart). Algorithmacy = the mediated-triad competency.
- **The open question that divides the papers:** is a given network's coordination protocol a
  moderated dyad or a mediated triad? Inspection can't settle it. Paper 2 builds a model that
  catalogs it (the IIT/Φ classifier: factors → moderated dyad; irreducible → mediated triad).
  Paper 3 runs experiments with the model.

### Paper 1 status
- Stage 1 (deep research): DONE. Run wf_89edb916-27e. Findings: the phenomenon + construct gap
  are solid; the broader framing was NOT adjudicated (user chose framing-light).
- Stage 2 (outline): DONE, approved. `rebuild/OUTLINE.md`.
- Stage 3 (draft): DONE, expanded to ~14k words. `rebuild/DRAFT.md`. Built from the user's
  conversation-mining extraction (`/Users/ludwitt/Downloads/Paper_1_Conversation_Mining_Extraction.md`),
  assembled from four parallel section agents (working files in `rebuild/expand/`).
- **Outstanding on Paper 1:**
  1. THE STYLE PASS (above) — the immediate task.
  2. Citation-integrity pass: 18 bibliography entries flagged `**[verify]**` need exact
     volume/pages/DOI confirmed (esp. Carolus 2023, Koch 2024, Karizat 2021, Stelmaszak 2025,
     Curchod 2020, Larsen & Bong 2016, Podsakoff 2016, Anthony/Bailey/Etzrodt).
  3. Four content gaps (from the extraction's own gap list): an applied criterion for a
     coordination shift "in kind"; a second non-platform worked example (court or market-maker
     through all three conditions); named seriality dissenters; an operationalized sensemaking
     measure for the discriminant strategy.
- Construct name is **algorithmacy** (completes the oracy/literacy series). Three formative
  dimensions: inferential (signal asymmetry), translational (intent compression), temporal-
  tracking (opaque mediation). Discriminant axis: the relational/coordinative target separates
  it from algorithm sensemaking (interpreting the system) and Zhou et al.'s algorithmic
  competency (navigating the system). Zhou cite corrected: APJHR 63(2), e70004,
  10.1111/1744-7941.70004.

### Then: Papers 2 and 3
Same staged process. Paper 2 = construct + the formal model that catalogs moderated-dyad vs
mediated-triad (the existing IIT/Φ instrument and committed results on `main` are reusable
ground truth: `paper2_construct/` and `paper3_baseline/` scripts under the venv). Paper 3 =
experiments with the model. The corrected exhibit for Paper 2 is `S'=¬W∧C` (Φ=0); the
comparator claim rests on the verified exhibit, not "strictly stronger."
