---
key: siskind2024would
apa: "Siskind, S. R., Nichols, E., & Gomez, R. (2024). Would you be impressed: Applying principles of magic to chatbot conversations. *Frontiers in Robotics and AI*, *11*, Article 1256937. https://doi.org/10.3389/frobt.2024.1256937"
authors: "Siskind, Sarah Rose; Nichols, Eric; Gomez, Randy"
year: 2024
title: "Would you be impressed: applying principles of magic to chatbot conversations"
venue: "Frontiers in Robotics and AI"
volume: "11"
issue: ""
pages: "Article 1256937"
doi: "10.3389/frobt.2024.1256937"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11076854/"
type: article
facets: [G]
claims: [c8, c9]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "PMC HTML rendering of the published open-access article (Front. Robot. AI 2024 Apr 24;11:1256937, PMCID PMC11076854, CC BY), text layer siskind2024would.txt read in full, reference list skimmed; local folder ~/iit-playground/dxd_animation_local/pdfs/siskind2024would/; original URL https://pmc.ncbi.nlm.nih.gov/articles/PMC11076854/ (FETCH_LOG.tsv row siskind2024would); read 2026-11-05; sha256 of the .html cc392bdf7f15f9c964b0789bf7a75655359d6daca5dcbb85d2098eea8a7367f1"
verified: corrected
verified_against: "siskind2024would.txt (PMC HTML text layer; all 11 loci and section locators), crossref.json, openalex.json; sha256 of siskind2024would.html recomputed and matched"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Siskind, Nichols and Gomez argue that chatbot designers should borrow the working principles of stage magic. A magic trick and a chatbot conversation share a property: "most of their audiences do not know how they work" (Abstract). Magicians have long practice at "gracefully skirting limitations in order to engage their audience", and the authors want dialogue designers to do the same. From informal interviews with working magicians they derive ten principles: have a story, misdirection, sucker gag, playing the odds, emotional connection, driving the point home, remember the claim, forcing, multiple outs, and the kicker (§4). They state the aim as "a model of communication centered on controlling the user's attention, expectations, decisions, and memory" (Abstract).

They apply the principles to Haru, a tabletop social robot, in a short scripted first-meeting conversation (§3, §5.1). They compare a "Magical" script with a "Control" script. Thirty-four online evaluators watched one video of each and rated both on Likert scales (§5.6, §5.7). The Magical script scored higher on robot familiarity, on the perceived engagement of the human, on three personality traits and on five of nine principle items (§6.2). The rapport-expectation scale showed no significant difference (§6.2.3). The authors call the study "exploratory" and list its limits (§7). In the conclusion they tentatively propose ("Perhaps the following line should be drawn") that deceiving the user is acceptable only to improve the experience, not to manipulate users against their best interests (§8).

The magician is the authors' model for the designer. The user is the audience. The chatbot is both the performer's prop and the performer. No animator appears, and the source does not mention animation.

## What the paper uses it for

- **c8 (contrast).** The paper's c8 says DXD should use the animator's craft (surface the frames, make the interstices visible) and not hide frames or expose the backend. Siskind et al. also draw on a performing craft whose skill lies in managing what the audience sees, but they use it to hide the system's gaps. §4.4 hides missing branches ("The user hopefully overestimates Haru's abilities"), and §1 says chatbots "should be discreet about their formulaic nature". This makes the source the opposite case: a craft borrowed for concealment, not surfacing. The source does not say the two crafts are twins. That pairing is the paper's reading.
- **c9 (gap).** A prior work that takes a performing craft as the model for an LLM-era interface. It treats magic, not animation, and tests it on a scripted social robot, not an LLM interface. It supports c9 only as a near neighbour. It does not frame LLM interfaces as animation for decision design.

Stretches and cuts against the paper:
- The study is a scripted, tree-based dialogue system (§3), not a generative LLM. Any claim that it bears on LLM interfaces is an extension.
- §4.8 describes "forcing" as controlling decisions "while giving the illusion of free choice". That is close to what the paper's c3 and c6 call co-optive. The source presents it as a design tool with an ethical limit in §8, not as a critique. The paper should not cite it as evidence that magic is co-optive in the c6 sense.
- The authors' ethical line (§8) separates harmless deception from manipulation against the user's interests. If the paper wants a foil, it must say the authors draw that line themselves.

## Loci

Quotations are verbatim from the PMC HTML text layer. Inner quotation marks in the source become single quotes here. Locators are article section numbers as printed (the HTML has no page numbers). Each was matched against the siskind2024would.txt text layer read this session.

- "We formulate a model of communication centered on controlling the user's attention, expectations, decisions, and memory based on examples from the history of magic." (Abstract; matched against the .txt)
- "But magicians, unlike the designers of dialogue systems, have centuries of practice in gracefully skirting limitations in order to engage their audience and enhance a sense of awe." (Abstract; matched against the .txt)
- "Similarly, chatbots should be discreet about their formulaic nature in order to create personalized interactions." (§1 Introduction; matched against the .txt)
- "The user hopefully overestimates Haru's abilities, which is intended to increase their engagement." (§4.4 Playing the odds; matched against the .txt)
- "Forcing in magic refers to the practice of controlling the audience's decisions while giving the illusion of free choice." (§4.8 Forcing; matched against the .txt)
- "The effect, it is hoped, is the user believing they have more control of the conversation than they actually do." (§4.8 Forcing; matched against the .txt)
- "Non-magicians often think that misdirection is moving an audience's attention away from what we do not want them to see, but, in reality, it is about moving an audience's attention towards something else." (§4.2, a magician's remark reported as personal communication; matched against the .txt)
- "The magic principles were tested together rather than one at a time" (§7 Limitations; matched against the .txt)
- "our findings should be viewed as exploratory work in developing and evaluating magic principles for informing chatbot conversation design." (§7 Limitations; matched against the .txt)
- "Perhaps the following line should be drawn: it is acceptable to deceive the user purely for the purposes of enhancing the user experience, but not to manipulate users against their best interests." (§8 Conclusion; matched against the .txt)
- "Since the human participant in the video was a co-author, there may have been the incentive to appear more engaged in the magic conversation" (§7 Limitations; matched against the .txt)

## Caution

- Registry spelling. The byline in the read text is "Randy Gomez" (no accent). OpenAlex has "Gómez". The card follows the byline and Crossref.
- Evidence is thin. The study uses one pair of videos with the same participant, who is a co-author and not blind to the hypotheses (§5.2, §7). It has 34 online raters, whose most common reply on robot familiarity was "I have not seen or used a robot in my life" (§5.6). The principles came from informal interviews, not from the magic literature (§7).
- The text overstates one result. §6.2.1 and the Abstract say the human interlocutor was rated higher on four of seven engagement items, naming attention at p < 0.05. Table 1 in the same text gives Person Attention (E10) p = 0.179. Only the happiness, interest and familiarity items (E08, E09, E14) show significance in the table, so the table supports three of seven. The table caption says its p values come from paired t-tests with a Bonferroni correction; the prose does not say whether its p < 0.05 for attention is corrected, which may explain the mismatch. Quote the table, not the abstract, if the engagement result is used.
- Internal cross-references are off. §5.1 and §5.1.2 point to "the magical principles introduced in Section 2", but the principles are in §4. §1 numbers the sections differently from the body.
- Forcing and multiple outs ran the other way. §6.2.4 reports a "reverse trend" for these items, which the authors read as parts of the conversation looking outside the robot's control (single question for both, per the footnote). This cuts against the principle the paper would find most relevant to c6.
- Funding. Honda Research Institute Japan funded the work, and two authors work there (Funding Statement; Conflict of interest).
- Not in SOURCE.md or OUTLINE.md, so status is candidate. DECISIONS.md lists it as in, contrast, c8, c9, and names it the §5 foil. The author decides whether it enters the paper. DECISIONS reserves `so2026beyond` as an LLM-specific alternative.
- Supplementary tables (evaluator comments and video transcripts) were not available in the folder and were not read.

## Verification

2026-11-05 · S6 verifier, batch b07 (opus; not the writer) · verdict: corrected · checked: loci 11/11 found verbatim in siskind2024would.txt (curly quotes normalised), all section locators match the printed headings; metadata vs crossref/openalex (authors, year 2024, title, venue, vol. 11, article 1256937, DOI) match; depth full_text honest (HTML and full text layer held; supplementary tables absent, as the card says); sha256 of .html recomputed and matched; Caution points (Table 1 E10 p = 0.179, "Section 2" cross-references, reverse trend, Honda funding) confirmed in the text · changed: §8 paraphrase softened to the authors' tentative "Perhaps" (What it argues); "mostly unfamiliar with robots" replaced by the text's "most common reply" (Caution); added the Table 1 Bonferroni note (Caution)
