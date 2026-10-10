# R5 — Prose and voice reader

Manuscript: `manuscript/REVISION_2026-10-09.md` (body read whole, reference list skimmed).
Calibration: introductions and one middle section each of Stark & Vanden Broeck (2024) and Hinds & von Krogh (2024), both *Organization Theory*.
Protocol: `~/.claude/commands/peer-review.md` Step 0, short Part 1, full Parts 2 and 3. House style: `~/.claude/writing-style.md` and the writing-style section of the project `CLAUDE.md`.

Paragraph numbers below (P1–P49) count body paragraphs from the first paragraph of the Introduction, skipping headings, the block quote, Table 1 and the figure caption. Section is given with every flag.

---

## Verdict line

**Minor revisions on prose.** The lexical slop is gone; what remains is structural uniformity. The single most important fix: break the "announce a count, then walk it" paragraph architecture, which governs about a third of the body (24 sentences announce "two/three/four Xs"; 16 of 49 paragraphs are built on one), and lengthen or subordinate the staccato stretches so the sentence-length profile moves toward the venue's.

---

## Step 0 — Register and bar

**Register identified.** A solo-authored Theory Article for *Organization Theory*. First person marks the author's moves ("I define," "I sort," "I searched," "I leave open"); claims are stated impersonally; vocabulary is plain and the author has ruled against cuteness, filler, aphoristic closers and modal padding. The paper's own signature move is the plain definitional sentence ("Interpreting is working out whether…") and the concrete two-person example (host and guest, John and Sally).

**Bar I hold it to.** The house style and the eight cohesion mechanisms in `CLAUDE.md`, calibrated against the two published OT pieces. Those two run long: Stark & Vanden Broeck average 25.2 words a sentence (32% of sentences at 30 words or more, 13% at 10 or fewer); Hinds & von Krogh average 28.1 (38.5% at 30+, 3.5% at ≤10). Both use em-dashes freely (Stark 4.0 per 1,000 words; Hinds 1.2). The house file sets ~3 per 1,000 as the floor for gloss-welding. Plainness is the author's rule and I do not trade it for venue mimicry; but "plain" and "short" are different things, and the venue shows that plain prose can run long.

**Cardinal rule, stated back.** No replacement below is more nominalized, more passive or more jargon-laden than what it replaces, and none adds a claim or a citation. Where I could not find a plainer form I say so and leave the sentence.

**Off-limits.** Quoted material from Simmel, Stark & Vanden Broeck, Selznick, Hinds & von Krogh and others; the three definitional openers of the three parts (a sustained analytic parallel, not a tic); the `[AUTHOR: …]` flags.

---

## Part 1 (short) — Buried leads and paragraph logic

1. **P6, Introduction — says three, lists four.** "The claim is limited in three ways." Then: (1) no data; (2) parts not all new; (3) "I searched Consensus, OpenAlex…"; (4) "Finally, triads with a third that judges both parties are older than software." The search sentence is not a limit, it is the novelty warrant for (2), but it stands as its own sentence between (2) and "Finally," so the reader counts four. Either drop the number or fold the search into (2). Replacement in Part 3, item 2.

2. **P15, Three Forms — the claim is buried under three disclaimers.** The paragraph's claim ("organizations first relied on people who could talk, then also on people who could handle text, and are now beginning to rely on people who can work in a triad") arrives as sentence 8 of 8, a 62-word sentence, after "The inference is mine and not Yates's. Nor do I claim that one form replaced another or that the words arrived in this order; Wilkinson coined…". Put the claim first; keep one disclaimer. Replacement in Part 3, item 3.

3. **P11, Simmel — three jobs in one paragraph.** Fourteen sentences do (a) whether the third must be a person, (b) who the party is, and (c) the three working terms *participant / counterpart / intermediary*, then (d) the two operator cases. The glossary in (c) is the most-used apparatus in the paper and it is buried at sentence 9. Split after "…a visibility she gains or loses." so the terms open their own paragraph.

4. **P42–P43, Discussion — the point arrives last.** P42 announces "two dimensions: how many parties the construct covers, and whether it describes an ability or a response," then walks five constructs without ever labelling which dimension each fails on; the reader does the sorting. The paper's addition is stated only at the end of P43. Front-load the addition or tag each construct with its dimension. Replacement in Part 3, item 6.

5. **P12, Three Forms — one justification sentence.** "Sorting forms is familiar in organization theory, which sets hierarchy, market, and network side by side (Powell, 1990) and treats a form of organizing as a set of solutions to problems that every organization has to solve (Puranam et al., 2014)." This defends the author's organizing choice (CLAUDE.md rule 4). It is venue-ordinary positioning and the author may want it; I flag it, I do not insist.

6. **P1 scene-first opener** (three examples before the question) is legitimate, not a buried lead. **P36** (two-sentence roadmap) is fine. **P17** ends on a pure forward hook ("The next section says what separates these two cases."); mechanism 6 wants exactly this, so I leave it.

Paragraph logic is otherwise sound. Tail-head linkage is unusually good across section joins: P4 ends "leaves the person's part undescribed" and P5 opens "I describe the person's part"; P17 ends on the court and P18 opens on it; P25 ends on the three lost conditions and P26 opens "The three parts of algorithmacy answer these three losses."

---

## Part 2 — The AI-slop audit, with counts

### 2.1 The numbers

| Measure | Manuscript body | Stark & VB 2024 | Hinds & vK 2024 |
|---|---|---|---|
| Body words | ~6,550 | ~13,000 | ~7,500 |
| Sentences | 301 | 344 | 231 |
| Mean words/sentence | 20.6 | 25.2 | 28.1 |
| Median | 19 | 23 | 27 |
| SD | 11.4 | 14.7 | 11.7 |
| Share ≤10 words | **23.6%** | 13.1% | 3.5% |
| Share ≥30 words | 20.9% | 32.0% | 38.5% |
| Em-dashes per 1,000 words | **0.3** (2 in body) | 4.0 | 1.2 |
| Semicolons | 44 | — | — |
| Paragraphs ending on ≤9-word sentence | 4 / 49 | — | — |
| Paragraphs ending on ≤12-word sentence | 9 / 49 | — | — |
| Sentences of ≤6 words | 22 (7.3%) | — | — |
| Sentences ending on a citation parenthesis, followed by another sentence | 15 | — | — |
| Antithesis constructions (`, not` / `and not` / `rather than` / `instead of` / `neither`) | 12 | — | — |
| "N things" announcer sentences ("two pictures," "three ways," "three points"…) | **24** | — | — |
| Paragraphs built as announce-count → ordinal walk → close | **~16 / 49** | — | — |
| Ordinal walks (The first… The second… / First,… Second,…) | 5 (P3, P8–9, P10, P19, P47) | — | — |
| Agentless passives in the subject slot | 0 (the "has been shown" tic is absent) | — | — |
| Emphasis markers (Crucially, Importantly, Notably, Note that) | 0 | — | — |
| Inflation words (tapestry, delve, nuance, foster, landscape, navigate as filler) | 0 (one "navigate" inside a quotation) | — | — |

### 2.2 What is not wrong (so the author does not fix it)

- **The landing-line drumbeat is gone.** Only 4 of 49 paragraphs exit on a sentence of nine words or fewer, and three of the four are honest: "I take the cases in order of fit." (P36, a roadmap), "The buyer and the reviewer do not." (P38, a real short after a dense build), "The next section says what separates these two cases." (P17, a forward hook). The fourth, "No one has measured it." (P34), is addressed below.
- **The agentless passive is gone.** The `has been / have been + -ed` scan returns three hits in 6,550 words ("have been named before," P6; "has been tried," P39; "are taken into account," P48), none in a subject-slot throat-clear.
- **Em-dashes are not over-used.** The one pair in the body (P24) is a textbook gloss weld. The problem runs the other way (2.5 below).
- **The three definitional openers** ("Interpreting is working out…", "Specifying intent is making…", "Keeping track is noticing…") are a sustained analytic parallel. Keep them.
- **First person** sits at the right junctures (sorting, defining, searching, leaving open) and never carries a claim. Good.
- **Antithesis** at 12 in 6,550 words is within venue usage. The issue is not the count but that five of them share one hedge shape (2.4 below).

### 2.3 Uniformity tell #1 — the counted-inventory paragraph

This is the main finding. The paper's dominant paragraph shape is: a short sentence announcing a number of items, an ordinal or parallel walk through them, and a medium closing sentence. Twenty-four sentences announce a count:

> "Existing answers start from one of two pictures." (P2) · "I describe the person's part in two steps." (P5) · "The claim is limited in three ways." (P6) · "Simmel described three positions a third can take." (P8) · "I take three points from this account." (P10) · "I therefore use three terms." (P11) · "The comparison helps the argument in two ways." (P18) · "The three parts of algorithmacy answer these three losses." (P26) · "A person can fail at this part in two directions." (P30) · "The three parts depend on one another…" (P33) · "The two ways of failing at the ability correspond to the two pictures…" (P35) · "The upshot is a limit and a prediction." (P41) · "…the differences can be stated on two dimensions…" (P42) · "An organization that places such a system between its people has three courses…" (P46) · "The first is whether… The second concerns the operator." (P47) · "Other questions are empirical." (P48) · plus eight more inside paragraphs.

Any one of these is fine, and the venue uses them (Stark & VB: "We see three limitations"). Sixteen paragraphs in a row of 49 built the same way is what the author means by "uniformity of optimization." The reader learns the drill by P8 and starts skimming for the numbers. The cure is not to delete the counts but to vary how a list enters: let the first item open the paragraph and the count arrive mid-stream (as P19 half-does); subordinate a two-item walk into one sentence; let one walk run without ordinals. Specific rewrites: Part 3 items 2, 4, 6, 8.

Related: **14 of 49 paragraphs open on a sentence of ≤8 words**, and in 11 of those the short opener is a count announcer. Short opener + walk is the signature.

### 2.4 Uniformity tell #2 — the candor formula

The paper hedges honestly, which the house style wants. But the hedge comes in one shape, repeated:

> "and I say which is which" (P6) · "I do not claim otherwise." (P6) · "The sorting is mine." (P12) · "The inference is mine and not Yates's. Nor do I claim that…" (P15) · "I accept all of this." (P16) · "and the account can be wrong" (P22) · "A construct needs stated limits, and a single clear exception counts heavily against one (Suddaby, 2010)." (P22) · "This is an expectation. No one has measured it." (P34) · "…a question I leave open." (P33) · "The account also carries a risk that should be stated." (P45) · "I offer this as a possibility that follows from the account and not as a finding." (P45) · "…so it establishes the arrangement and not the ability." (P37) · "…in dyads and not in triads." (P28)

Thirteen self-disclosures, five of them on the "X and not Y" template. Sort them:

- **Honest flat hedges — keep:** "The sorting is mine." "The inference is mine and not Yates's." "…a question I leave open." "so it establishes the arrangement and not the ability." "though it shows it in dyads and not in triads" (needs a pronoun fix, 2.7). These state scope. The house style asks for exactly this.
- **Performance — cut or flatten:**
  - "I do not claim otherwise." (P6) ranks its own candor. The next sentence already says what is claimed. Cut.
  - "I accept all of this." (P16) is concession theatre before the turn. Replace with the turn itself.
  - "A construct needs stated limits, and a single clear exception counts heavily against one (Suddaby, 2010)." (P22) is a sentence about the paper's own warrant for the paragraph that follows — the one thing CLAUDE.md rule 4 bans outright. Cut; the scope conditions that follow are the content. (Suddaby can stay in the reference list only if cited elsewhere; it is not. Dropping a citation is allowed; adding one is not.)
  - "and the account can be wrong" (P22) is a second ranking of candor in the same sentence. Cut.
  - "This is an expectation. No one has measured it." (P34): the content is honest; the two-beat staccato (4 words, 5 words) after two 33-word sentences is the performance. One flat sentence.
  - "The account also carries a risk that should be stated." (P45): agentless passive plus self-commentary. State the risk.
  - "I offer this as a possibility that follows from the account and not as a finding." (P45): the fifth "and not" hedge in the same shape; by now the reader hears the template. Flatten.

Rewrites in Part 3, items 2, 5, 7, 9.

### 2.5 Uniformity tell #3 — choppiness, and where it clusters

The manuscript's share of sentences at ten words or fewer (23.6%) is nearly double Stark & Vanden Broeck's and seven times Hinds & von Krogh's; its share at thirty or more (20.9%) is two-thirds of Stark's and half of Hinds'. Spread (SD 11.4) is adequate; the problem is the floor. The venue's plain prose runs long because it subordinates. The manuscript often does not.

The short sentences also **cluster** rather than puncture. The house style wants a short sentence to land after a dense run. Here are the runs where three or more short sentences sit together:

- **P3, Introduction, opening:** 8 / 6 / 7 / 6 words — "Each picture drops something the arrangements above contain. The first has no second person. The second has no system that decides. Several accounts come closer than either." Four shorts before any long sentence. (Also "The first has no second person" trips the ear on read-aloud: first/second/second.)
- **P10, Simmel, opening:** 7 / 18 / 11 / 7 / 15 / 10 — six sentences averaging 11 words before the 41-word Simmel quotation.
- **P15, Three Forms, middle:** "That pair of abilities is literacy. Organizations came to depend on it." (6 / 6).
- **P34, How the Parts Fit, close:** "This is an expectation. No one has measured it." (4 / 5).
- **P33:** "Without specifying intent, interpreting is a private diagnosis that changes nothing. Without interpreting, specifying intent is formatting. Without keeping track, the other two run on an understanding that has expired." (11 / 6 / 13) — the triad for cadence (2.6).

Elsewhere the variation works: P24 (6 / 18 / 21 / 24 / 11 / 32 / 33) and P14 (11 / 10 / 19 / 20 / 25 / 10) read as a human wrote them.

### 2.6 Cute, aphoristic, or auditioning

Six sentences. Ranked by how much they would be quoted in a seminar and therefore by how much they stand out from the plain voice around them:

1. **"Without interpreting, specifying intent is formatting."** (P33, How the Parts Fit.) The one true epigram in the paper. It also under-explains: a non-specialist does not know what "formatting" is doing. Replacement in Part 3, item 1.
2. **"Participants on a platform carry the responsibility without the seat."** (P20, What Sets the Algorithmic Third Apart.) Compresses Selznick's "responsibility for power rather than power itself" into a metaphor. It earns itself because the Selznick quotation is two sentences earlier and "seat" paraphrases "leadership or policy-determining structure." Borderline; keep unless the read-aloud catches it. If it goes: "Participants on a platform share the responsibility and not the power."
3. **"In each case one corner of the triad stands in for the whole."** (P35.) An epigram closer on a three-sentence paragraph that then hands nothing to the next section. Part 3, item 10.
4. **"Organization theory has the triad."** (P4, opening.) Five words, cute, and it follows P3's own epigram closer ("The observations in this literature are triadic and the constructs are dyadic."), so two quotables sit back to back across the paragraph break. P3's closer is the gap statement and earns its place. P4's opener can carry content: "Organization theorists have already drawn the triad."
5. **"I define it."** (Abstract.) Three words placed for effect in a 200-word abstract. The venue's abstracts do not do this. "I define that ability here." — or merge into the next sentence: "I define it as the ability to do interdependent work…"
6. **"Installing a system is none of these:"** (P46.) Earned; the colon delivers Christin's finding. Keep.

The final sentence of the paper — "Where they do not, they are relying on an ability that they have neither named nor checked that their people have." — is not cute, but the parallel breaks ("neither named [it] nor checked that their people have [it]") and a reader stumbles on the last line. Part 3, item 4.

### 2.7 Unclear to a non-specialist (read twice, or term before gloss)

1. **"oracy"** is used in P5 (Introduction: "oracy belongs to direct dyads") and in the abstract before Wilkinson glosses it in P14. Most readers of *OT* will not know the word. Add a four-word gloss at first use: "oracy, the ability to speak and listen, belongs to direct dyads…" (gloss carried from P14; no new claim).
2. **P15, "Nor do I claim that one form replaced another or that the words arrived in this order; Wilkinson coined 'oracy' in 1965 by analogy with the older 'literacy.'"** — "this order" has no referent the reader can find on first pass (the order is oracy → literacy → algorithmacy, which has not yet been stated as an order in this paragraph). Part 3, item 3.
3. **P21, "I name the ability for algorithmic systems for the reason that literacy is named for letters though it applies to any text: that is where the form has become general."** — read three times. "that" has no clear antecedent. Part 3, item 8.
4. **P28, "Research on communication shows that this kind of attribution is not automatic, though it shows it in dyads and not in triads."** — "it shows it": two pronouns, two referents. Replacement: "Research on communication shows that this kind of attribution is not automatic, though the studies are of dyads, not triads."
5. **P22, "the accounts built on the first picture cover it."** — "the first picture" was introduced 2,400 words earlier. Name it: "the accounts that pair one person with one machine cover it."
6. **P40, "The finding bears on what an expert who stands between a system and other people can do, and I use it below for that."** — "for that" is vague. "…and I return to it when I come to what organizations can do."
7. **P46, "Or the organization can see that its people acquire the ability"** — "see that" in the sense of "ensure" reads as "perceive" to a non-native or hurried reader. "Or the organization can make sure its people acquire the ability."
8. **P47, "the conditions under which an employer's system counts as a party need stating."** — nominalization plus agentless. "and I have not said when an employer's system counts as a party."
9. **P11, "The *intermediary* is what stands between them, which is the rule as applied, with its operator behind it."** — the "which is" clause hangs; this is what the em-dash gloss weld is for. Part 3, item 7.
10. **P3, "The first has no second person."** — first/second clash (2.5). "The first picture has no other person in it."
11. **P25, "Each feature of the intermediary undoes one."** — "one" = one condition; fine on a second read, but "undoes one of them" costs nothing.
12. **P39, "They report no data, and I use their case as they do."** — "as they do" = as a thought experiment. "…and I use their case as they do, as a thought experiment." (The phrase appears two sentences earlier in their quoted words, so this adds nothing new.)

### 2.8 Semicolon-chained literature inventories

Forty-four semicolons. The ones that read as an inventory — one scholar per clause, chained, no handle for the next sentence:

- **P2:** "Guzman and Lewis (2020) propose…; Long and Magerko (2020) list…; studies of professionals record…; and theories of how people and AI coordinate take…" (60 words). Then the same shape again for the second picture.
- **P4:** "Kornberger et al. (2017) show…; Curchod et al. (2020) describe…; Cameron (2024) draws…; Chan (2022) writes…; and Cameron and Rahman (2022) show…" (65 words).
- **P16:** "Cooren (2004) has shown…; Kuhn (2008) builds…; and Lehtinen and Pälli (2021) show…" (44 words).
- **P19:** the "Third" feature: three quotations chained with commas (53 words).
- **P31:** "Users form folk theories…; DeVito (2021) followed 25…; and Meng (2026) writes…" (50 words).
- **P44:** "Orlikowski and Scott (2008, 2023) argue…, Faraj and Pachidi (2021) argue…, Glaser et al. (2021) treat…, and Alaimo and Kallinikos (2021) show…" (55 words).
- **P28:** not semicolons but three consecutive "X (year) found…" sentences (21 / 28 / 29 words), then a fourth that regroups them.

The venue does this too (Stark & VB's "digital Taylorism" paragraph is exactly such a chain), so I do not flag P2 and P4 as faults: in an introduction a chain is how one shows the territory. P16, P31 and P44 are in argument sections, where mechanism 8 applies: group under a handle or subordinate. P28 is the clearest case, because its fourth sentence already supplies the grouping ("People in these studies assigned credit, blame, and trust between a person and a machine in patterned ways"); move that sentence first and the three findings become its evidence. Part 3, item 6.

### 2.9 Em-dashes

Two in the body, both in one pair (P24): "a specific source of equivocality—a third whose part in a result cannot be separated from the counterpart's part—and the absence of anyone to ask." A gloss weld; correct. One pair in the abstract, also a weld. No crutches.

The under-use is a tell in its own right. Glosses that the venue would weld with a dash are being carried by stand-alone "By X I mean…" sentences (P12 "By 'moderated' I mean only…"; P23 "By *ability* I mean…") and by trailing "which is" clauses (P11). Both are plain and both are fine once; the paper does them four times. Three places where a dash is plainer than the current form: P11 (item 7), P23 ("By *ability* I mean what a person can reliably do…" can stay — it is a definition, not a gloss), P42 ("Reactivity (Espeland & Sauder, 2007; Rahman, 2021) describes how people respond to being measured and does not say what they are able to do" — fine as is). Net: add one, in P11. Do not chase the venue's 3 per 1,000.

### 2.10 Filler, signalling, nominalization

None of the banned emphasis markers. No inflation vocabulary. "therefore" four times, all doing logical work. Nominalization stacks: none of the "effects a coordination" kind. Two mild ones: "the production of valuations reconfiguring the everyday practices of the hotels being evaluated" (P31 — but this paraphrases Orlikowski & Scott's own abstract and is defensible); "need stating" (P47, 2.7 item 8). "The upshot is a limit and a prediction." (P41) announces two things and then delivers two descriptions; neither is phrased as a prediction. "The upshot" is fine; drop "and a prediction" or phrase the second sentence as one: "…and I expect the demand for algorithmacy to fall on one side of the relation."

### 2.11 Per-paragraph six-question check

Questions: (1) tail-head break doing no work; (2) citation-tail where the next sentence needs a handle; (3) six consecutive new subjects; (4) epigram closer; (5) term before gloss; (6) self-commentary. "—" means clean.

| P | Section | Flags |
|---|---|---|
| 1 | Intro | (2) ends on a four-author parenthesis; next sentence "This paper asks" recovers. Minor. |
| 2 | Intro | (3) inventory; venue-ordinary in an intro. |
| 3 | Intro | (4) closer is the gap statement — earned; opening staccato (2.5). |
| 4 | Intro | (2) "(Fuller & Smith… Lopez, 2010). Students of platforms have redrawn it" — "it" reaches back over the parenthesis; works. Cute opener (2.6). |
| 5 | Intro | (5) "oracy" before gloss. |
| 6 | Intro | count mismatch (Part 1); (6) "I do not claim otherwise." |
| 7 | Simmel | — |
| 8 | Simmel | — |
| 9 | Simmel | — (two sentences; could join P8) |
| 10 | Simmel | opening staccato (2.5); otherwise the best-varied paragraph in the Simmel section. |
| 11 | Simmel | three jobs (Part 1); (5) glossary buried; "which is" clause (2.7). |
| 12 | Three Forms | (6) the Powell/Puranam justification (optional); 10 sentences doing four jobs; "The sorting is mine." mid-paragraph. |
| 13 | Three Forms | — |
| 14 | Three Forms | — (model paragraph) |
| 15 | Three Forms | claim buried (Part 1); "this order" (2.7); 62-word closer. |
| 16 | Three Forms | (6) "I accept all of this."; inventory (2.8). |
| 17 | Three Forms | forward-hook closer; fine. |
| 18 | Algorithmic Third | — |
| 19 | Algorithmic Third | inventory in the "Third" feature (2.8). |
| 20 | Algorithmic Third | (4) "without the seat" — borderline (2.6). |
| 21 | Algorithmic Third | literacy-for-letters sentence (2.7). |
| 22 | Algorithmic Third | (6) Suddaby sentence; "and the account can be wrong"; "the first picture" (2.7). |
| 23 | Algorithmacy | — |
| 24 | Participant's Position | — (best paragraph; see closing note) |
| 25 | Participant's Position | — ("undoes one", trivial) |
| 26 | Participant's Position | — |
| 27 | Interpreting | — |
| 28 | Interpreting | (3) three "X found" sentences; "it shows it". |
| 29 | Specifying Intent | — |
| 30 | Specifying Intent | — (second-best; the invented case is plain and concrete) |
| 31 | Keeping Track | inventory (2.8); 50-word chain. |
| 32 | Keeping Track | — |
| 33 | Parts Fit | (4) "is formatting"; triad for cadence. |
| 34 | Parts Fit | "This is an expectation. No one has measured it." |
| 35 | Parts Fit | (4) epigram closer, no hook. |
| 36 | Where Applies | — (roadmap, fine) |
| 37 | Where Applies | — |
| 38 | Where Applies | — (short antithetical closer earns itself) |
| 39 | Where Applies | "as they do" (2.7); "has been tried" passive, mild. |
| 40 | Where Applies | "for that" (2.7). |
| 41 | Where Applies | "a limit and a prediction" (2.10). |
| 42 | Discussion/Adds | (3) inventory; dimensions announced, not used (Part 1). |
| 43 | Discussion/Adds | (2) two citation-tails in a row; the point lands last. |
| 44 | Intermediary as Party | inventory (2.8); otherwise clean. |
| 45 | Intermediary as Party | (6) "a risk that should be stated"; "and not as a finding". |
| 46 | Three Courses | "see that" (2.7). |
| 47 | Agenda | "need stating" (2.7). |
| 48 | Agenda | — |
| 49 | Conclusion | last sentence's broken parallel (2.6). |

---

## Part 3 — Line-level rewrites, ranked by value

Each gives section, original, failure, replacement. Replacements add no claims and no citations; where a citation is dropped I say so.

**1. P33, How the Parts Fit Together — the epigram.**
Original: "Without specifying intent, interpreting is a private diagnosis that changes nothing. Without interpreting, specifying intent is formatting. Without keeping track, the other two run on an understanding that has expired."
Failure: a triad for cadence with a quotable middle that under-explains ("formatting").
Replacement: "Without specifying intent, interpreting is a private diagnosis that changes nothing. Without interpreting, there is nothing to specify, and the participant is only changing the wording of what she sends. Without keeping track, both run on an understanding of the rule that has expired."

**2. P6, Introduction — the count that does not match, and the candor line.**
Original: "The claim is limited in three ways. The paper reports no data; its cases come from published studies and from one thought experiment, and I say which is which. The parts of the ability are not all new, since two of the three have been named before; what I add is the definition over the triad and the tie between each part and a feature of the intermediary. I searched Consensus, OpenAlex, Crossref, and the 2022–2026 contents of *Administrative Science Quarterly*, *Organization Science*, *Organization Studies*, and *Organization Theory*, and found no work that names this ability or defines it in this way. [AUTHOR: …] Finally, triads with a third that judges both parties are older than software, and I do not claim otherwise. I claim that algorithmic systems have made a demanding version of that triad an ordinary condition of work."
Failure: announces three limits, reads as four; "I do not claim otherwise" ranks its own candor; "and I say which is which" is a promise about the paper's care.
Replacement: "The claim is limited. The paper reports no data; its cases come from published studies and from one thought experiment. Two of the ability's three parts have been named before, and what I add is the definition over the triad and the tie between each part and a feature of the intermediary: I searched Consensus, OpenAlex, Crossref, and the 2022–2026 contents of *Administrative Science Quarterly*, *Organization Science*, *Organization Studies*, and *Organization Theory*, and found no work that names this ability or defines it in this way. [AUTHOR: …] Triads with a third that judges both parties are older than software. What algorithmic systems have done is make a demanding version of that triad an ordinary condition of work."

**3. P15, Three Forms — claim first, one disclaimer.**
Original (last four sentences): "Yates (1989) describes American firms between about 1850 and 1920 coming to be managed through memos, reports, forms, and files, and I infer that a firm managed in this way assumes its people can read and write. The inference is mine and not Yates's. Nor do I claim that one form replaced another or that the words arrived in this order; Wilkinson coined "oracy" in 1965 by analogy with the older "literacy." The claim is that organizations first relied on people who could talk, then also on people who could handle text, and are now beginning to rely on people who can work in a triad."
Failure: three disclaimers before the claim; "this order" has no visible referent; 62-word closer.
Replacement: "Organizations first relied on people who could talk, then also on people who could handle text, and are now beginning to rely on people who can work in a triad. Yates (1989) describes American firms between about 1850 and 1920 coming to be managed through memos, reports, forms, and files; that a firm managed this way assumes its people can read and write is my inference, not hers. The sequence is one of reliance, not replacement, and the words themselves came in a different order: Wilkinson coined "oracy" in 1965 by analogy with the older "literacy.""

**4. P49, Conclusion — the last sentence.**
Original: "Where organizations remove those features, the need falls. Where they do not, they are relying on an ability that they have neither named nor checked that their people have."
Failure: broken parallel on the paper's last line.
Replacement: "Where organizations remove those features, the need falls. Where they do not, they depend on an ability they have not named, and they have not checked whether their people have it."

**5. P34, How the Parts Fit — the staccato hedge.**
Original: "I therefore expect people in the same formal position to differ in algorithmacy, by the turns they have had, by what a mistake would cost them, and by whether someone interprets for them. This is an expectation. No one has measured it."
Failure: two four-and-five-word beats performing flatness after two 33-word sentences; cluster of shorts at a paragraph close.
Replacement: "I therefore expect people in the same formal position to differ in algorithmacy, by the turns they have had, by what a mistake would cost them, and by whether someone interprets for them. No one has measured this."

**6. P28, Interpreting — group the three findings under the sentence that already groups them.**
Original: "Research on communication shows that this kind of attribution is not automatic, though it shows it in dyads and not in triads. Sundar and Nass (2000) found that people rated the same content differently according to the source they were told it came from. Hohenstein and Jung (2020) found that suggested replies raised people's trust in their chat partner and, when a conversation went badly, moved blame from the partner to the system. Sundar and Kim (2019) found that people told a chat agent was a machine reported more willingness to give it a credit-card number than people told it was a human. People in these studies assigned credit, blame, and trust between a person and a machine in patterned ways that the content alone does not explain, and Heiland (2025) reports workers forming false theories of an algorithm because they could not see it."
Failure: "it shows it"; three consecutive "X (year) found" sentences (a list with periods), with the grouping sentence arriving fourth.
Replacement: "Research on communication shows that this kind of attribution is not automatic, though the studies are of dyads, not triads. In them, people assigned credit, blame, and trust between a person and a machine in ways the content alone does not explain: Sundar and Nass (2000) found that people rated the same content differently according to the source they were told it came from; Hohenstein and Jung (2020) found that suggested replies raised people's trust in their chat partner and, when a conversation went badly, moved blame from the partner to the system; and Sundar and Kim (2019) found that people told a chat agent was a machine were more willing to give it a credit-card number than people told it was a human. Heiland (2025) reports workers forming false theories of an algorithm because they could not see it."
(Yes, this converts periods to semicolons; the gain is that the grouping handle comes first and the three findings read as its evidence rather than as three claims in a row. Same semicolon count as P16 and P44, which stay.)

**7. P45, The Intermediary as a Party — state the risk.**
Original: "The account also carries a risk that should be stated. Elish (2019) describes how a person placed beside an automated system "bears the brunt of the moral and legal responsibility" (p. 40) when it fails. Algorithmacy may work as a private repair for a public defect. The better participants become at interpreting, addressing, and keeping track, the less the opacity of the rule shows in results, and the less pressure there may be to change it. I offer this as a possibility that follows from the account and not as a finding."
Failure: agentless passive plus self-commentary in the opener; the fifth "X and not Y" hedge in the closer.
Replacement: "The account also carries a risk. Elish (2019) describes how a person placed beside an automated system "bears the brunt of the moral and legal responsibility" (p. 40) when it fails, and algorithmacy may work the same way, as a private repair for a public defect. The better participants become at interpreting, addressing, and keeping track, the less the opacity of the rule shows in results, and the less pressure there may be to change it. This follows from the account; it is not a finding."

**8. P21, What Sets the Algorithmic Third Apart — the sentence read three times.**
Original: "I name the ability for algorithmic systems for the reason that literacy is named for letters though it applies to any text: that is where the form has become general."
Failure: "that" has no antecedent; two "for"s pulling in different directions.
Replacement: "Literacy is named for letters though it applies to any text. I name this ability for algorithmic systems on the same ground: they are where the form has become general."

**9. P16 and P22, two candor lines to cut.**
P16 original: "I accept all of this. The line I draw is about who holds the verdict."
Replacement: "None of this touches the line I draw, which is about who holds the verdict."
P22 original: "A construct needs stated limits, and a single clear exception counts heavily against one (Suddaby, 2010). Because the features vary independently, the need for the ability varies with them, and the account can be wrong. Where the rule is published…"
Replacement: "Because the features vary independently, the need for the ability varies with them. Where the rule is published…"
(Drops the Suddaby citation; it is cited nowhere else, so the reference entry goes with it. Author's call.)

**10. P35, How the Parts Fit — epigram closer to hook.**
Original: "A participant who treats it as a moderated dyad reads the intermediary's verdict as the counterpart's opinion. In each case one corner of the triad stands in for the whole."
Replacement: "A participant who treats it as a moderated dyad reads the intermediary's verdict as the counterpart's opinion. Both mistake a triad for a dyad, and the next section asks which arrangements are triads at all."

### Further rewrites, lower value, ready to paste

11. **P3, Intro:** "The first has no second person. The second has no system that decides." → "The first picture has no other person in it. The second has no system that decides."
12. **P4, Intro, opener:** "Organization theory has the triad." → "Organization theorists have already drawn the triad."
13. **P5, Intro:** "On this sorting, oracy belongs to direct dyads and chains of them," → "On this sorting, oracy, the ability to speak and listen, belongs to direct dyads and chains of them,"
14. **P11, Simmel:** "The *intermediary* is what stands between them, which is the rule as applied, with its operator behind it." → "The *intermediary* is what stands between them—the rule as applied, with its operator behind it." And split the paragraph before "I therefore use three terms."
15. **P22:** "and the accounts built on the first picture cover it." → "and the accounts that pair one person with one machine cover it."
16. **P39:** "They report no data, and I use their case as they do." → "They report no data, and I use their case as they do, as a thought experiment."
17. **P40:** "and I use it below for that." → "and I return to it when I come to what organizations can do."
18. **P41:** "The upshot is a limit and a prediction. An intermediary that binds both parties equally is less common in the published record than one that binds a single side. The usual case is the lopsided triad, and in it the demand for algorithmacy falls on one side of the relation." → "The upshot is a limit. An intermediary that binds both parties equally is less common in the published record than one that binds a single side; the usual case is the lopsided triad, and there I expect the demand for algorithmacy to fall on one side of the relation."
19. **P42, Discussion:** tag the constructs with the dimensions the paragraph announces. "Algorithmic competency (Jarrahi & Sutherland, 2019), measured by Zhou, Lei, Liu, et al. (2025) as workers' "…" (p. 2), is an ability defined over two parties (see also Hong et al., 2026)." → "Algorithmic competency is an ability, but one defined over two parties: Zhou, Lei, Liu, et al. (2025) measure it as workers' "understanding of platform algorithms that assign and evaluate their work and their ability to adapt to and navigate those algorithms" (p. 2; see also Hong et al., 2026; Jarrahi & Sutherland, 2019)." Then: "AI literacy and algorithmic literacy (…) are knowledge about a system rather than an ability to work through one; …" and "Reactivity (…) is a response, not an ability: it describes how people respond to being measured and does not say what they are able to do."
20. **P46:** "Or the organization can see that its people acquire the ability," → "Or the organization can make sure its people acquire the ability,"
21. **P47:** "and the conditions under which an employer's system counts as a party need stating." → "and I have not said when an employer's system counts as a party."
22. **Abstract:** "…but no account names the ability it asks of them or defines that ability over all three parties. I define it. Algorithmacy is the ability…" → "…but no account names the ability it asks of them or defines that ability over all three parties. I define it as the ability…" (delete the following "Algorithmacy is the ability" and let the sentence run; the term "algorithmacy" is already in the title and the first clause of the next sentence can read "I call this ability algorithmacy and define it as…" if the author wants the name stated in the abstract body).

---

## Worst and best paragraphs

**Worst, in order:**
1. **P6 (Introduction, "The claim is limited in three ways")** — count mismatch, two candor performances, the one paragraph a hostile reader would quote back.
2. **P15 (Three Forms, Yates/Wilkinson)** — claim last, three disclaimers first, a referent-less "this order," a 62-word closer.
3. **P11 (Simmel, "Two questions about this borrowing")** — fourteen sentences, three jobs, the paper's working glossary buried at sentence 9.
4. **P42 (Discussion, "Several constructs lie close")** — an inventory with periods whose organizing dimensions are announced and never applied.
5. **P33 (How the Parts Fit)** — the cadence triad and the paper's one epigram.

**Best:**
1. **P24 (The Participant's Position).** Opens on a claim ("The participant does not lack information."), welds the Daft & Lengel distinction into the next sentence, lands a real short ("More data cures the first and does not cure the second."), uses the paper's only em-dash pair exactly as the house style describes, and ends on the content the next paragraph picks up. Nothing to change.
2. **P30 (Specifying Intent, the invented case).** Two failures, two employees, plain words, then one published case. This is the voice the author asked for.
3. **P14 (direct dyad, "I tell John and John tells Sally").** Concrete, short, varied.
4. **P10 (Simmel's three points),** once the opening run of shorts is loosened: "The mediator has no stake. A platform does:" is a real puncture after the Simmel quotation.

---

## Does it still read as machine-written?

Less than the author's earlier verdicts would predict, and for a different reason. The lexical tells are gone: zero subject-slot agentless passives, zero emphasis markers, zero inflation words, two em-dashes (both gloss welds), a landing line on only 4 of 49 paragraphs, antithesis at 12 in 6,550 words. What remains is architectural, and it is the thing the author warned about: a repair pass that left every paragraph the same shape.

- **Twenty-four "N things" announcer sentences and about sixteen paragraphs built as announce-a-count → walk it → close.** This is the signature a reader now learns by the second section.
- **A sentence-length floor too low for the venue:** 23.6% of sentences at ten words or fewer against 13.1% (Stark & VB) and 3.5% (Hinds & vK); 20.9% at thirty or more against 32% and 38.5%. The shorts also cluster in four stretches (P3, P10, P15, P34) instead of puncturing dense runs.
- **One hedge shape repeated thirteen times,** five of them "X and not Y," plus two sentences that comment on the paper's own warrant (P22) and candor (P6).
- **Six semicolon or period inventories** in argument sections (P16, P19, P28, P31, P42, P44) where a handle would group them.
- **Five or six quotables** in a voice that is otherwise plain, which makes them stand out more, not less.

None of this is a rewrite. All of it is a pass the author can do by ear, and most of it is listed above with the replacement text.

---

## Closing note

**Biggest genuine strength.** The cohesion. Section joins hand off cleanly (P4→P5, P17→P18, P25→P26), the three-term glossary is used consistently once introduced, and the working examples (host and guest, the seller whose standing drops, the two employees and the self-assessment, John and Sally) keep every abstraction on the ground. P24 and P30 are the paper's own voice; the revision should move the rest toward them, not toward the venue's density for its own sake.

**What only the author's read-aloud can settle.**
1. Whether "Participants on a platform carry the responsibility without the seat." (P20) is earned by the Selznick quotation two sentences above it or is a line reaching for a seminar. I lean keep; the ear decides.
2. Whether the three definitional openers of the parts (P27, P29, P31) read as a sustained analytic parallel or as a template by the third one. I lean keep.
3. Whether "The buyer and the reviewer do not." (P38) lands as a real short after a dense build or as one more antithetical beat. I lean keep.
4. Which of the sixteen count-and-walk paragraphs to loosen. Loosening all sixteen would produce a new uniformity. The four I would leave as they are: P8 (Simmel's three positions — the walk is Simmel's, not the author's), P19 (the four features — the italics carry the structure and the reader needs the numbers later), P26 (three parts answer three losses — the table follows), P46 (three courses — the venue would write it the same way).
