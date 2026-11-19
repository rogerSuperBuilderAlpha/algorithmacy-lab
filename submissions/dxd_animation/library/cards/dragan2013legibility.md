---
key: dragan2013legibility
apa: "Dragan, A. D., Lee, K. C. T., & Srinivasa, S. S. (2013). Legibility and predictability of robot motion. In *2013 8th ACM/IEEE International Conference on Human-Robot Interaction (HRI)* (pp. 301–308). IEEE. https://doi.org/10.1109/hri.2013.6483603"
authors: "Dragan, Anca D.; Lee, Kenton C. T.; Srinivasa, Siddhartha S."
year: 2013
title: "Legibility and predictability of robot motion"
venue: "HRI '13"
volume: ""
issue: ""
pages: "301–308"
doi: "10.1109/hri.2013.6483603"
url: "https://dl.acm.org/doi/abs/10.5555/2447556.2447672"
type: proceedings
facets: [F12]
claims: [m1, m3, m7]
role: contrast
load: load-bearing
read_depth: abstract
object_read: "version: the abstract as displayed on the ACM DL landing page of the HRI '13 proceedings copy (dl.acm.org/doi/abs/10.5555/2447556.2447672, pp. 301–308), read 2026-11-12 in the author's Chrome session and saved verbatim as ~/iit-playground/dxd_animation_local/pdfs/dragan2013legibility/abstract_acm_page.txt (provenance.txt); sha256 of that file: d47bae43fe259b2469a22dc330106fccae116e8ba4c6f6e5efb2d2cf307e508f; I read the saved file, not the page, on 2026-11-12; full text behind 'Get Access', not opened; Crossref record for the IEEE DOI in crossref.json, sha256 7944ce1ddcb830b62a6c908f464d5852f6bc340b07efd82e0d55f5ea555086d5"
verified: corrected
verified_against: "abstract_acm_page.txt (sha256 d47bae43…, recomputed) and crossref.json (sha256 7944ce1d…, recomputed); 2026-11-12, S6 verifier batch D"
prior_cards: []
status: candidate
added: 2026-11-12
run: dxda-lib-2026-11b
---

## What it argues

This is an abstract card. Everything below comes from the abstract shown on the ACM DL page and saved verbatim; I have not read the paper.

Anca Dragan, Kenton Lee and Siddhartha Srinivasa start from collaboration: "A key requirement for seamless human-robot collaboration is for the robot to make its intentions clear to its human collaborator." They define their term in the next sentence: "A collaborative robot's motion must be legible, or intent-expressive." Their target is a conflation in the field: "Legibility is often described in the literature as and effect of predictable, unsurprising, or expected motion" (the source's "as and effect", for "as an effect"). Against it they set their "central insight", that "predictability and legibility are fundamentally different and often contradictory properties of motion." They formalise the two "based on inferences between trajectories and goals in opposing directions, drawing the analogy to action interpretation in psychology", and they model those inferences "based on optimizing cost, drawing the analogy to the principle of rational action." They report that "Our experiments validate our formalism's prediction that predictability and legibility can contradict, and provide support for our models", and conclude that robots "must change the way they plan their motion." The abstract does not say which inference runs in which direction, and it gives no design, sample size or effect for the experiments.

## What the paper uses it for

- **m7 and m1 (contrast: the label).** This is the source of "legibility" as human–robot interaction uses it: a robot's motion that expresses its intent to the human watching it, "legible, or intent-expressive". The word is a homonym of the legibility the author's ruling rejects, "Algorithmacy is not legibility … not for a user who reads the algorithm more skilfully" (`../MODEL.md` §3). In Dragan et al. the robot's motion carries its goal to the watcher; the watcher reads no planner, rule or model. That sense sits nearer the model's own move, building the reading into what the person sees, than to the reading of the algorithm the ruling sets aside. The paper should gloss the homonym wherever it cites robot-motion work, and must not cite this paper as an example of the legibility it rejects. For m7, the abstract shows a mature literature on making intent readable through motion; it says nothing about decisions, intermediaries or animation, so it does not touch the gap as `../MODEL.md` §2.3 words it.
- **m1 (the card's reading).** The abstract's split between predictable and legible motion matches two jobs a display can do: confirm what the person already expected, or tell them something they did not know. Row 1's labelled staging does the second. The abstract's claim that the two "can contradict" warns that a display tuned to look expected may tell the person less. This is my extension; the abstract concerns robot trajectories only.
- **m3 (the card's reading).** The same tension bears on row 3's cue before a rule change: a cue that announces something new may look unexpected. The abstract gives no data on how observers weigh the two.

## Loci

None. This is an abstract card; the quotations above come from the abstract only.

## Caution

- **Abstract only.** The full text is paywalled on the ACM DL and I did not see it. The formalism's directions, the experiments, their N and their results are unknown to this card. Any claim about what the paper shows beyond the abstract needs the full text first (`BROWSER_LIST.md` if it cannot be reached).
- **Two records, one paper.** Crossref holds the IEEE record: DOI 10.1109/hri.2013.6483603, "2013 8th ACM/IEEE International Conference on Human-Robot Interaction (HRI)", Tokyo, 3–6 March 2013, pp. 301–308, IEEE. The ACM DL page that carried the abstract is 10.5555/2447556.2447672, with pp. 301–308 as recorded in the header of `abstract_acm_page.txt`. The card cites the IEEE DOI.
- **The source's typo.** "as and effect of" is as printed on the ACM page.
- **How others in this run gloss it (not checked against this paper).** Szafir, Mutlu and Fong (2014) describe its distinction as legible motion "allowing users to correctly infer the robot’s goal" and predictable motion "matching the expectations of an observer who knew the goal a priori", and report that its legibility-optimised trajectories were arced and let observers better predict an end target (szafir2014communication, locus 3; §2.1, p. 359). Dragan, Holladay and Srinivasa (2014) build their deception model on its observer model (dragan2014analysis, §III, p. 3). Schulz, Torresen and Herstad (2019) introduce the work as "Citing an inspiration from animation, but not necessarily using animation techniques" (p. 12:4; checked this run against the Schulz text layer). These are other authors' readings; the abstract confirms none of the directions they give.
- **Facet.** The abstract never mentions animation. The F12 placement rests on Schulz et al.'s remark above and on Szafir et al.'s use of the paper for arced, intent-expressive motion, not on this abstract.
- **Registry.** No card for this work exists in the registry (searched by key, DOI and title, 2026-11-12). It was an uncarded lead in `RUN_REPORT.md` and in schulz2019animation.

## Verification

2026-11-12 · S6 verifier, batch D (Opus 5.5; not the writer) · verdict: corrected · checked: 0/0 loci (Loci None, as an abstract card requires); frontmatter vs crossref.json (Dragan, Lee, Srinivasa; 2013 8th ACM/IEEE HRI, Tokyo, 3–6 March 2013; IEEE; pp. 301-308; 10.1109/hri.2013.6483603); sha256 recomputed for abstract_acm_page.txt (d47bae43…) and crossref.json (7944ce1d…), both match sha256.txt and object_read; read_depth abstract honest: the folder holds no PDF, and every body quotation is in the saved abstract (11 found, incl. "as and effect of"); the Caution's glosses by others: Szafir et al.'s two phrases (Szafir p. 359), Dragan et al. 2014's observer model "[11]" (§III, PDF p. 3), and Schulz et al.'s sentence (Schulz text layer, PDF p. 4 = p. 12:4) all found; registry.tsv holds no card for this work (its one "dragan" row is a co-author of hadfield2017offswitch); claim uses · changed: one quotation, "…and provide support for our models," → "…for our models",: the source ends that sentence with a full stop, so the comma moves outside the quotation marks · for the lead: the m7/m1 bullet calls this paper "the source of 'legibility' as human–robot interaction uses it". The abstract itself says "Legibility is often described in the literature as…", so the term predates the paper. Szafir et al. cite it together with Lichtenthaler et al. (2012, [26]), and Dragan et al. (2014) list earlier titles that use the word (Beetz et al. 2010, [3]; Mainprice et al. 2010, [22]). The paper may cite it as the standard source of the legible/predictable distinction, not as the origin of the term. The m1 and m3 readings are labelled as the card's own and stay so.

## Hand-check

- 2026-11-12, Claude (Opus 5.5, lead; S7). Verdict: **index**. Writer: subagent; check: S6 verifier, batch D (corrected). Checked: the 'intent-expressive' sentence against abstract_acm_page.txt (the lead copied the abstract from the ACM page). Changed: nothing further. For the author: cite for the legible/predictable distinction, not as the origin of the word; abstract only.
