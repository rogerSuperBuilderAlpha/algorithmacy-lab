---
key: chang1993animation
apa: "Chang, B.-W., & Ungar, D. (1993). Animation: From cartoons to the user interface. In *Proceedings of the 6th Annual ACM Symposium on User Interface Software and Technology* (pp. 45–55). ACM. https://doi.org/10.1145/168642.168647"
authors: "Chang, Bay-Wei; Ungar, David"
year: 1993
title: "Animation: From Cartoons to the User Interface"
venue: "UIST '93"
volume: ""
issue: ""
pages: "45–55"
doi: "10.1145/168642.168647"
url: ""
type: proceedings
facets: [F9, F12]
claims: [c8, m1, m3, m4, m5, m6]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "PDF of the UIST '93 paper (11 pp., printed pp. 45–55), from the ACM Digital Library (dl.acm.org/doi/pdf/10.1145/168642.168647), opened in Chrome's PDF viewer and saved 2026-11-11 through the author's browser session; ~/iit-playground/dxd_animation_local/pdfs/chang1993animation/chang1993animation.pdf; sha256 7e7bdd5b80ec62478ca6b151e40f3ad55df47bc7f225b076b8f077d1bfd460cc; read in full from the PDF and its reading-order text layer; Crossref record re-fetched 2026-11-11 (crossref.json, sha256 cd9784985f97c9ba031e3fe2ec26db2206179636c81ddcd0d862cee7b78ed644)"
verified: pending
verified_against: ""
prior_cards: [chang1993animation (dxd_animator)]
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11b
---

## What it argues

Bay-Wei Chang and David Ungar argue that user interfaces built from static displays handle change badly, and that cartoon animation — "exceedingly successful at engaging its audience" (abstract) — offers techniques that make change on the screen easy to follow. They used the interface of the Self programming environment as a testbed.

They start from an interpretation problem. When a screen jumps from one state to another, "the causal connection between the old state of the screen and the new state of the screen is not immediately clear" (p. 45), and the user has to work out which objects are the same, which changed and which changes came from their own action. To interpret a change "efficiently and reliably", the user needs an expectation of what the screen will look like (p. 45). Animation supplies cues "before, during, and after the action" and offloads "some of the cognitive burden of interpreting the change to the perceptual system" (p. 46).

They take their principles from Thomas and Johnston's *Disney Animation: The Illusion of Life* (p. 46) and group them as **solidity** (solid drawing, motion blur, smooth arrivals and departures, dissolves), **exaggeration** (anticipation, follow through) and **reinforcement** (slow in and slow out, arcs, follow through) (pp. 46–51; summary table p. 52). Anticipation is "a way of exaggerating a preliminary action in order to give the audience a cue about the main action to follow" (p. 50); in Self, an object about to move on its own first "anticipates that move with small, quick contrary movement" (p. 50). The reinforcing effects work below awareness: "The audience is not consciously aware of these effects" (p. 50).

They explain why cartoons, not realistic animation, fit interfaces: cartoons are theatrical, they absorb the viewer so that the cartoon's mechanics "are quickly forgotten", and their medium resembles computer graphics (pp. 52–53). They then set limits (§4, p. 53). "The most important difference" is that a cartoon is passive and an interface interactive, so the user must stay in control and animation must not make the user wait. Cartoons are for diversion, interfaces for work, so the wackiness does not transfer. A cartoon can use anticipation for a surprise gag, suggesting one action and delivering another; such a surprise suits a cartoon and, they say, would disturb the user of an interface (p. 53; the text layer garbles the adjective, so it is paraphrased here). Animation "should be as fast as it can be while still preserving legibility" (p. 53).

The evidence is informal. "Some user testing" was carried out; users either noticed and enjoyed the animation or took it for granted, and glitches "can suddenly wreck the illusion" (p. 53). No measures are reported. They close by proposing the techniques for collaborative applications, where "remote users often will initiate actions" (p. 54).

## What the paper uses it for

- **m1 (anchor).** Chang and Ungar state the interface version of idempotent interpretation without the term: after a sudden change the user cannot tell how the old state led to the new one, or which changes came from their own action and which are incidental (p. 45). Their remedy — make the transition visible so perception carries the inference (p. 46) — is a design move that takes interpretive work off the person, the direction of DXD. They work on one user's own screen; the step to a second party's input passing through an intermediary is the paper's.
- **m3 (anchor).** Two loci: anticipation as a cue to the action that follows (p. 50), and their closing proposal to use anticipation, slow in and out, motion blur and follow through to inform a user "about remotely initiated actions" (p. 54). The second is the nearest read precedent for signalling changes made by another party before they land. Chang and Ungar propose it and do not test it.
- **m4 (anchor).** §4 is a transfer argument: some cartoon techniques carry over and others (surprise gags, wackiness) do not, because an interface is interactive and serves work (p. 53). This is a precedent for a selection rule. Their criterion is the medium's purpose, not the user's competencies.
- **m5 (support).** Their account of engagement is the co-optive side of the craft: the cartoon's mechanics "are quickly forgotten" and the reinforcing effects work without the audience being "consciously aware" of them (pp. 50, 52). They treat this as a benefit. Read through algorithmacy, the same property hides what the intermediary is doing. Their warning that anticipation can be used to suggest one action and deliver another (p. 53) names the deceptive use the paper must rule out.
- **m6 (support, partial).** Collaborative applications with "remote users" (p. 54) bring in a second party but no intermediary that evaluates or binds. They mark the edge of the model's scope, not its core case.
- **c8.** HCI prior art that already carries cartoon principles into interfaces, now read in full.

## Loci

Matched against the reading-order text layer (`chang1993animation.readorder.txt`) and the PDF; page numbers are the printed UIST '93 pages (PDF p. 1 = p. 45). Inner double quotation marks are changed to single quotation marks. The text layer has OCR errors; the loci were chosen from clean lines, and each was found in it.

1. "When the user cannot visually track the changes occurring in the interface, the causal connection between the old state of the screen and the new state of the screen is not immediately clear." §1, p. 45.
2. "To be able to efficiently and reliably interpret what has happened when the screen changes state, the user must be prepared with an expectation of what the screen will look like after the action." §1, p. 45.
3. "Animation provides the visual cues necessary to understand what is happening before, during, and after the action." §1, p. 46.
4. "offloading some of the cognitive burden of interpreting the change to the perceptual system" §1, p. 46.
5. "The principles of animation mentioned in this section are drawn from the excellent treatise on cartoon animation" §2, p. 46 (the sentence continues with Thomas and Johnston's title, which the text layer garbles).
6. "showing motion is not just showing a series of still pictures" §2.1.1, p. 48.
7. "is a way of exaggerating a preliminary action in order to give the audience a cue about the main action to follow." §2.2.1, p. 50 (the subject, "Anticipation", is the run-in heading).
8. "Exaggeration increases the prominence of features deemed significant by the animator" §2.2, p. 50.
9. "The audience is not consciously aware of these effects." §2.3, p. 50.
10. "The mechanics of the cartoon (brightly colored, outlined shapes in front of largely static backgrounds) are quickly forgotten, and do not reappear in the audience's awareness." §3, p. 52.
11. "The most important difference between them is that the cartoon is a passive medium, while the user interface is an interactive one." §4, p. 53.
12. "by making the anticipation suggest to the audience one action, while having a different action actually happen." §4, p. 53.
13. "Because a user interface is a tool for doing some task, animation in it should be as fast as it can be while still preserving legibility." §4, p. 53.
14. "Some user testing of the animation in the Self user interface has been carried out." §5, p. 53.
15. "inconsistencies in the animation or performance glitches can suddenly wreck the illusion of the interface and draw attention to the animation itself." §5, p. 53.
16. "remote users often will initiate actions, so the user may not even have the advantage of expecting something to happen." §6, p. 54.

## Caution

- **Run 1 card superseded.** Run 1 carded this work at metadata depth; its S6 verification and S7 hand-check covered the Crossref record only and are removed from this file (git history keeps them). Its Caution notes stay true: the Crossref record's event field reads "PRS93: Parallel Rendering Symposium" against the UIST container title, and Crossref dates the proceedings December 1993 while the paper's running footer gives the meeting as November 3–5, 1993, Atlanta.
- **No measured evidence.** The paper reports informal "user testing" (p. 53) with no N, task or measure. It can support claims about what designers proposed and why, not claims that the techniques improve comprehension.
- **Persistence of vision.** In §2.1.1 the authors explain the double image of a fast-moving object "Because of persistence of vision" (p. 47). Film scholars treat that account as a myth (CHECK F12; `anderson1993myth`, abstract). Do not cite Chang and Ungar for the perceptual mechanism.
- **"Legibility".** Chang and Ungar use "legibility" for how readable a motion is (p. 53). The author's standing ruling "Algorithmacy is not legibility" (`../../decision_experience_design/README.md`) uses the word for a user reading the algorithm. The paper should not let the two senses meet without a gloss.
- **Thomas and Johnston at second hand.** The principles are Thomas and Johnston's as Chang and Ungar read them (reference [24], dated 1981, Abbeville). Cite accordingly until the book is read.
- **OCR.** The text layer garbles many words ("confime", "faater", "distuding"); quotations outside the loci above should be checked against the PDF page before use.
- **Pronouns.** The authors alternate "he" and "her" for the user.
