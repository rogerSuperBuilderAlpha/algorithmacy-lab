# Style specification and sentence gate — Algorithmacy and Sovereignty — 2026-08-23

The models, as selected. Argument and cadence: Aytac (2024), Digital domination, *Political Studies* 72(1), profiled from the full text this session. Register and vocabulary: Cutolo and Kenney (2021), *AMP* 35(4), profiled this session. Structure: Rawls per the `rawlsian-prose` skill, already governing OUTLINE_v2. Contrast-vocabulary source for §4: Stark and Vanden Broeck (2024), whose 5,689-word licensed corpus sits at `style_candidates/stark2024.txt`.

Precedence when the models disagree: house bars first, the Rawls skill second, Aytac's mechanics third, Cutolo and Kenney's register fourth. Every conflict between them is resolved below; a drafter should never have to adjudicate one.

## 1. What is taken from each model

**From Aytac, the argumentation.** Thesis stated in full by the second paragraph, after one paragraph of dated, named, real-world scene-setting. The central concept coined in a single stipulation sentence ("an instance of domination is quasi-public if it amounts to...") and immediately tested on a paradigm case. Enumeration announced and delivered in order (two mechanisms, three objections), embedded in prose. Objections voiced in the objector's own indicative mood at full strength, then answered by diagnosis ("The first problem with this objection is that it fails to acknowledge...") or by concede-then-contain ("Even if we acknowledge that..., this does not..."). Hedges live only in the objector's voice; the author's own claims are unmodalized. Paragraphs close by returning to the normative payoff. Citations sentence-end parenthetical by default, author-led with page pins only for load-bearing definitional borrowings.

**From Cutolo and Kenney, the register.** Management-venue accessibility: concrete actors as grammatical subjects (the seller, the platform, the regulator), technical terms glossed at first use in apposition, mid-length declaratives alternating with occasional short pivots, empirical anchors named (companies, cases, figures) rather than gestured at. Their measured profile: sentences mean 18–20 words with deliberate alternation between 8–12-word topic sentences and 40-word subordinate builds; claim-first paragraph openings dominant; citations mid-sentence or terminal, never load-bearing as subjects.

**From Rawls, the structure.** Already fixed in OUTLINE_v2: main idea first, rival's best case before its failure, device, principles with priority rule, institutions, ends. Paragraph shape: claim, elaboration, reason, one-sentence concession, return.

**From Stark and Vanden Broeck, one thing only.** The compact contrast construction for coordination forms ("whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted") as the §4 template for parallel-clause definition work. Their heavy "we," their paired dashes, and their 28-word mean do not carry.

## 2. Resolved conflicts

First person. Aytac's "I argue" and Rawls's "I shall maintain" are both overridden: zero first person, singular or plural (house bar; three authors; double anonymization). Commitment carries through claim-first declaratives; where Aytac writes "I contend that platforms dominate in two ways," this chapter writes "Platforms bind the coordinated actor in two ways."

Roadmap and metadiscourse. Aytac closes his introduction with "The article proceeds as follows" and opens paragraphs with "Let me now." Overridden: no roadmap paragraph, no self-narration, no "as argued above," no "this section shows" (house bar; the 2026-08-02 style pass already stripped these once). The Rawlsian alternative stands: the order of sections is the roadmap.

Rhetorical questions. Aytac uses them as paragraph hinges, answered in the next sentence. Permitted at most twice in the chapter, only as a hinge before the answer, never as an opener of a section. The existing §5.2 direct question ("ask what the mediator still does") is one of the two.

Enumeration against the rule-of-three ban. Aytac enumerates relentlessly; the house bans rule-of-three climaxes. The line: enumeration of substantively distinct items, announced by count and delivered in order, is argument and stays ("Five features block the literate model, each at a different point"). Triplets assembled for rhythm ("clear, direct, and uncompromising") are decoration and go.

Sentence length. Aytac runs mean ≈23 sd ≈7; Cutolo and Kenney mean ≈18–20 with wide alternation; the project's own QA benchmarked published models at sd ≥14. Targets: mean 21–26 per section, sd ≥12, at least one sub-10-word sentence per ~500 words doing real work (a clarifying denial, an imperative introducing a case, a verdict), no more than one sentence over 45 words per section.

Hedging. Zero hedges on the chapter's own claims (no "seems," "might," "perhaps," "arguably," "may well" in authorial voice). Modals appear only inside a voiced objection or a reported position, and empirical uncertainty is stated as fact about the evidence ("the evidence on X is not yet in"), never as authorial diffidence.

Passive voice. House bar is active voice; the models run 20–32% passive. Resolution: passives only where the agent is unknown or irrelevant, capped at 10% of finite clauses per section, and never in a sentence that advances the argument. "The seller is read by the system" fails; "the system reads the seller" passes.

## 3. The sentence gate

Every drafted sentence must pass all applicable checks. The gate runs per section, before any section is declared done.

G1. Opens the paragraph with a claim or a defined term, if it is a paragraph opener; framing openers are allowed only in expository passages (§1 history, literature positioning), never in §§2, 5, 6.
G2. No first person, singular or plural.
G3. No em-dash. Commas, semicolons, colons, parentheses only.
G4. Active voice unless the agent is genuinely unknown or irrelevant; never passive in an argumentative sentence.
G5. No hedge in authorial voice; modals only inside voiced objections or reported positions.
G6. No metadiscourse: no "this section," "as noted above," "we now turn," "it is worth noting," "importantly."
G7. Citations at sentence end in parentheses; author-led only for a definitional borrowing carrying a page pin; never a citation as the grammatical subject doing the arguing.
G8. No X-not-Y construction; state what the thing is in one sentence, why the rival fails in another.
G9. No rule-of-three climax; enumerations carry announced counts and substantively distinct items.
G10. Concrete grammatical subject where one exists: the seller, the platform, the court, the directive, the system; abstractions as subjects only for defined constructs.
G11. Every technical term either already defined in the chapter or glossed in apposition at first use; no decorative jargon (no "always-already," "performative," "imbricated," "problematize," scare quotes on ordinary words).
G12. Length discipline: over 45 words, split unless the logical structure is strictly sequential; under 10 words, only if it earns the emphasis.
G13. Concession discipline: at most one concession per move; "of course" clears the table, "yet" or "still" returns; the concession never becomes the paragraph.
G14. Banned strings, hard: em-dash character; "computable"; "genuinely"; "the argument" as a self-reference; "practised" (US spelling throughout); first-person tokens; "In this section"; "as we will see."
G15. Verbatim-refrain check: no sentence pattern repeated more than twice in the chapter (the antithesis machine and metronomic short openers the panels named).
G16. Every factual or attributive claim carries its support per the evidence audit; a sentence that asserts without a source either cites, or is a definitional or argumentative move that needs none.

## 4. QA protocol

The gate is enforced in three passes per section, in order. First, mechanical: a grep pass over the drafted section for G2, G3, G14, first-person tokens, hedge lexicon, metadiscourse strings, sentence-length statistics against the targets; anything flagged is fixed before reading. Second, sentence read: every sentence checked against G1–G16 by a reviewer who did not draft it, with failures listed by line, no silent fixes. Third, cadence read: the section read against one page of Aytac (argument sections) or Cutolo and Kenney (applied sections) for rhythm, and against the section's word budget from OUTLINE_v2. A section passes when the mechanical pass is clean, the sentence read lists zero open failures, and the cadence read raises nothing the drafter cannot cite a spec line to refuse. The author's read-aloud of §2 and §5 (the definition and the device) remains owed at the end, as with the previous draft.

## 5. Calibration exemplars

Aytac, argument moves (short quotes within fair use): thesis form, "I argue that social media companies' power to regulate communication in the public sphere illustrates a novel type of domination" (this chapter's equivalent, without the first person: "The chapter's claim is that..." becomes simply the claim, asserted). Coinage form: "an instance of domination is quasi-public if it amounts to a private actor dominating others qua citizens," then the paradigm case; the chapter's coinages follow the same genus-differentia stipulation, as the Key Terms already do. Objection form: "One might object..."; return form: "The first problem with this objection is that it fails to acknowledge the role of discretion."

House-conform rewrites of the three Stark and Vanden Broeck representative sentences, as drafting calibration: their "But the analysis... must, we contend, not be a sub-field of labor studies" becomes "The analysis of algorithmic management is not a sub-field of labor studies"; their Möbius sentence keeps its parallel clauses and loses nothing; their "our task in this essay is to develop" becomes the developed thing stated outright.

## 6. Division of labor across the chapter

Argument sections (§§2, 3, 5, 9 of OUTLINE_v2): Aytac mechanics at full strength; densest objection craft in §3 (the rival) and §5 (the device against its neighbors). Applied sections (§§6, 7, 8): Cutolo and Kenney register leads; shorter mean, named cases, figures carried in prose. Expository passages (§1 history, §4 positioning): citation-led openings permitted, Rawlsian compression enforced. Key Terms: stipulation form throughout, already conformant. Abstract: third person, unmodalized, 150-word cap, written last.
