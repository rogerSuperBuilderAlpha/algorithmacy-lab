# Structural model for the decision-spaces theory paper: Cutting & Deterding (2022)

**Citation:** Cutting, J., & Deterding, S. (2022). The task-attention theory of game learning: A theory and research agenda. *Human–Computer Interaction, 39*(5–6), 257–287. https://doi.org/10.1080/07370024.2022.2047971

**Copy read:** CC-BY published version, White Rose Research Online, 33 pages. I read §§1–4.0.2, §5 opening, §5.1–5.1.3, §5.4 and §6 in full, and skimmed §§4.1–5.3.

## Why this paper

### How I found it
I searched OpenAlex for *HCI* journal articles from 2019 on with "theory", "framework", "conceptual" or "theoretical" in the title or abstract. I then excluded any whose abstract reported participants, interviews or experiments. The candidates were:

| Paper | Why it was considered | Why I passed over it |
|---|---|---|
| Cutting & Deterding (2022) | Cognitive theory with propositions | **Chosen** |
| Rapp (2021), "Wearable technologies as extensions: a postphenomenological framework and its design implications" | Theory-only paper | Philosophical register |
| Strohmann et al. (2022), "Toward a design theory for virtual companionship" | Theory-only paper | Design-science register |
| Tractinsky (2019), "The usability construct" | Theory-only paper | A commentary, and closed access |

### Why it was chosen
- **No data.** It is a theory-only *HCI* article with no new study. Its formal predictions "have not been directly empirically tested" (§5.1).
- **Same register as your paper.** It builds a cognitive theory of attention from psychology for an HCI audience, which is your register.
- **Same contribution type as yours:** a named construct, mechanisms, numbered propositions, testable predictions, and implications for research and design.
- **Overlapping content, by chance.** It treats eye tracking as a measure of overt attention only (§3.1), cites inattentional blindness, and closes with a section on reflection and breaking attentional absorption (§5.4).

## Its structure, section by section

| § | Section (their heading) | What it does | Length (approx.) |
|---|---|---|---|
| — | Front matter | Title, keywords, article history. **The published version has no abstract on its first page**; it opens straight into §1. OpenAlex's "abstract" is just the first lines of the introduction. *HCI*'s style guide still asks for one, so write one. | — |
| 1 | Introduction | (a) An empirical puzzle: game-learning evidence is "mixed and contradictory". (b) A claim in one sentence: "we propose that task-based attention is ... [a] moderator". (c) The two bases of evidence for the claim. (d) **Scope bracketing:** "not ... the sole or primary mechanism ... we analytically bracket such other aspects." (e) What prior accounts miss. (f) **The whole theory as six numbered points.** (g) A roadmap naming each subsection. | ~1,300 words |
| 2 | A brief introduction to attention | A primer on the base science for an HCI reader: key terms, then the two mechanisms the theory rests on. | ~970 |
| 3 | Attention in current HCI, media effects, and learning theories | A **mini-review of competing theories**, one subsection per field. Each ends by naming what that field omits. A summary paragraph then states the gap. | ~1,830 |
| 4 | How task-based attention moderates game learning | **The theory.** It opens by restating the gap and naming the theory, including why the name was chosen. **Figure 1** is a "nomological network": a diagram of the constructs (A–E) and the arrows between them. Next come six propositions, (i)–(vi), each given as a bold line plus a short paragraph. **Table 1** lists 12 formal predictions, each tied to an arrow in Figure 1 (e.g., "1→C"). Subsections then take each construct in turn: current evidence, how it shows up in games, how games differ from non-interactive media, and a closing "Formally, ... predicts ...". | ~6,700 |
| 5 | Discussion: implications and future work | Opens by stating the three ways the theory extends prior theories. Then implications by audience: 5.1 research (first item: "severe testing of task-attention theory itself"), 5.2 design, 5.3 the wider field. **5.4 takes on the strongest counterpoint** (that breadth, disattention and reflection also matter for learning) rather than a generic limitations list. | ~3,800 |
| 6 | Conclusion | Synthesis in three paragraphs, ending on an inversion: "We have studied what players are looking at for a long time; task-attention theory may help us understand what they have been seeing." | ~250 |

**No separate Limitations section.** Limits appear in three places instead: the scope bracketing in §1, caveats in the "future work" subsections (e.g., §5.1.2, "these findings may not generalize to games"), and the counterpoint section, §5.4.

## Moves to copy

1. **Open on a puzzle in the evidence, not on the importance of the technology.** For you, the evidence on streaming is mixed: perceived trust rises (Bhat, 2025), but perceived effectiveness does not.
2. **State the theory in one sentence, then bracket what it does not explain.** For you: decision spaces address *perceptual* support for supervision, not model accuracy, explanation design or user training.
3. **Give the whole theory as numbered points in the introduction**, before any evidence.
4. **Write a primer section** on the base science for HCI readers. For you: reading and eye movements.
5. **Write a mini-review of competing accounts**, each ending on what it omits. For you: LLM streaming work, automation-trust models, and LLM friction and overreliance work.
6. **Name the theory, and say why it has that name.**
7. **Draw a Figure 1 network of constructs and arrows**, and tie every formal prediction to an arrow.
8. **Use a uniform pattern for each construct:** evidence, how it shows up in this medium, how this medium differs, then "Formally, ... predicts ...".
9. **Make testing the theory the first item of future work**, and say plainly that the predictions are untested.
10. **Replace a limitations list with the strongest counterpoint**, argued.
11. **End on a short inversion** that restates the paper's contribution.

## How your outline would change if you follow it

| Current outline (`paper/FINAL_OUTLINE_HCI.md`) | Following Cutting & Deterding |
|---|---|
| §1 Introduction | Keep it, and add: a puzzle in the evidence, a one-sentence claim, scope bracketing, **the theory as numbered points**, and a roadmap that names subsections. |
| §2 Scriptio continua | Keep it as the historical argument. Cutting & Deterding have no history section, so this is your distinctive move. It could also fold into §1 as the motivating analogy. |
| §3 Three mechanisms | Becomes the **primer** (their §2): reading, attention and events, kept short. |
| *(none)* | **New section: how current accounts treat streaming** (their §3). Covers LLM streaming and pacing work (Liu et al., 2024; Xiao & Yang, 2025; Zhu et al., 2026, CHI EA), automation-trust models (Parasuraman & Manzey, 2010; Lee & See, 2004; Tatasciore et al., 2026; Gegoff et al., 2025), and LLM friction and overreliance work (Buçinca et al., 2021; Collins et al., 2024; Cox et al., 2016; Disley & Khan, 2026). Each ends on what it omits: *where* in the stream the boundaries fall. |
| §4 Decision spaces + §5 Propositions | **Merge them into one theory section** (their §4): a named account; a Figure 1 network running from stream features through onset capture, segmentation and look-back availability to fixation, regression and detection; propositions; a table of formal predictions tied to arrows; then a subsection per function using the uniform pattern. |
| §6 Design space | Becomes **Discussion 5.2, design implications**. |
| §7 Algorithmacy | Becomes **Discussion 5.3, implications for the wider field**. |
| §8 Limits | Becomes **Discussion 5.4, the strongest counterpoint**: friction is disliked and pauses may only work by slowing things down (Forshaw et al., 2026; Buçinca et al., 2021; Arun et al., 2026). Scope limits move to the introduction's bracketing. |
| §9 Conclusion | Keep it, and end on an inversion. |

**Scale (counted from the text):** the theory section is about 6,700 of about 14,900 words of body text (45%). The 19,566-word total includes references. That suggests your merged theory section should be the longest in the paper.
