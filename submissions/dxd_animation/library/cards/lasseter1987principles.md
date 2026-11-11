---
key: lasseter1987principles
apa: "Lasseter, J. (1987). Principles of traditional animation applied to 3D computer animation. In *Proceedings of the 14th Annual Conference on Computer Graphics and Interactive Techniques* (pp. 35–44). ACM. https://doi.org/10.1145/37401.37407"
authors: "Lasseter, John"
year: 1987
title: "Principles of traditional animation applied to 3D computer animation"
venue: "SIGGRAPH '87"
volume: ""
issue: ""
pages: "35–44"
doi: "10.1145/37401.37407"
url: ""
type: proceedings
facets: [F1, F9, F11]
claims: [c5, c8, m1, m2, m3, m4, m5]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "PDF of the SIGGRAPH '87 paper as printed in Computer Graphics 21(4), July 1987, pp. 35–44 (10 pp.), from the ACM Digital Library (dl.acm.org/doi/pdf/10.1145/37401.37407, page marked FREE ACCESS), obtained 2026-11-11 through the author's Chrome session; ~/iit-playground/dxd_animation_local/pdfs/lasseter1987principles/lasseter1987principles.pdf; sha256 b99cde55f501ee7588e78142443605f82d6ab7b14e8011d7274037bd0c40a730; read in full from the PDF and its reading-order text layer"
verified: corrected
verified_against: "19/19 loci in the reading-order and layout text layers of the ACM DL PDF (sha256 b99cde55...), PDF pp. 5–6 on page images; crossref.json (10.1145/37401.37407); Crossref record 10.1145/37402.37407; first page"
prior_cards: [lasseter1987principles (dxd_animator)]
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11b
---

## What it argues

John Lasseter, writing from Pixar in 1987, argues that the principles of hand-drawn character animation developed at the Disney studio apply to 3D keyframe computer animation, and that the new commercial keyframe systems "will also enable people to produce more bad computer animation" because their users do not know those principles (p. 35). He addresses system designers as well as animators (p. 35).

He tells how the principles arose: Disney's drawing classes under Don Graham turned the analysis of action into named procedures, which "were isolated and named, analyzed and perfected" and taught "as rules of the trade" (p. 36). He then lists **eleven** numbered principles — squash and stretch; timing; anticipation; staging; follow through and overlapping action; straight ahead action and pose-to-pose action; slow in and out; arcs; exaggeration; secondary action; appeal (p. 36) — and treats each in its own subsection (§§2.1–2.11, pp. 36–42). A closing section on personality says personality "is not a principle unto itself, but the intelligent application of all of the principles" (p. 43). The paper lists no principle called "solid drawing" and does not say "twelve".

He sorts the principles by medium. Timing, anticipation, staging, follow through, overlap, exaggeration and secondary action "apply in the same way" in drawn and computer animation; squash and stretch, slow in and out, arcs, appeal, straight-ahead and pose-to-pose keep their meaning but change their application (p. 36). In 3D, "Motion is achieved by setting keyframe poses and having the computer generate the inbetween frames" (p. 36).

Four arguments matter for the paper.
- **Timing lives between the poses.** The effect of weight "depend[s] entirely on the spacing of the poses and not on the poses themselves" (p. 37). Quoting Thomas and Johnston, he shows that the same two extreme drawings of a head read as a blow, a twitch, an order or an appraisal depending on how many in-betweens lie between them (p. 37–38).
- **Anticipation and staging direct the viewer.** Anticipation prepares the audience and tells them *what* a character will do even when it does not show *why* (p. 38). Staging presents "an idea so it is completely and unmistakably clear", one idea at a time (p. 38).
- **Pose-to-pose with in-betweens made by other hands.** The animator plans the poses, and a "timing chart" drawn beside the drawing tells "his assistant who will be doing the inbetweens later" where to place them (p. 40). In computer animation the machine is the in-betweener, and it misbehaves: spline in-betweens overshoot so that "the value will shoot in the wrong direction", and Lasseter fixes this by adding extra extremes that "locked" the spline (pp. 40–41). He concludes that keyframe animation cannot be approached "exactly as one would pose-to-pose hand drawn animation" (p. 40).
- **Where a change goes.** A facial change during a major body move "will go unnoticed"; "The change must come before, or after, the move" (p. 42).

He ends by saying "the first goal of the animator is to entertain" (p. 43).

## What the paper uses it for

- **m2 (anchor).** Lasseter is the read source for the division of labour the intent-specification row needs: a key animator fixes the extreme poses and hands the in-betweens to another hand, with a written timing chart as the instruction (p. 40). In 3D keyframing the computer is that other hand, and its in-betweens go wrong in ways the animator must constrain by adding keys (pp. 40–41). The move to a person fixing a few commitments and an LLM or agent generating what lies between is the paper's, not Lasseter's.
- **m3 (anchor).** Two loci carry the tracking row. Anticipation leads the audience "to expect it before it actually occurs" and settles *what* happens next without explaining *why* (p. 38), which fits a cue that does not explain the rule. A change made in the middle of a major move "will go unnoticed" (p. 42). Lasseter writes about a character's face during a body move; reading this onto a rule change during a task is the paper's step.
- **m1 (support).** Staging, one idea at a time and in silhouette (pp. 38–39; [Verifier, S6: corrected from "p. 38"; the silhouette passage is on p. 39]), is the craft the opaque row draws on. The in-between table (pp. 37–38) shows that identical extreme poses carry different meanings according to what lies between them. [Lead, hand-check S7: narrowed after the verifier's note.] A film viewer sees those in-betweens, so the visible motion differs; the paper's use is that a user who sees only the extremes (what was asked and what came back) cannot tell which in-betweens produced them. That is an analogy to idempotent interpretation, not an instance of it. The table is Lasseter quoting Thomas and Johnston.
- **c5 (support).** "depend entirely on the spacing of the poses and not on the poses themselves" (p. 37) is a read, citable statement that what happens between frames carries the meaning, close to the claim Pass 2 attributes to McLaren. It does not replace a McLaren source (CHECK F1); it is Lasseter's own claim, citing Whitaker and Halas [30].
- **m4 (support, and a caution).** Lasseter addresses system designers (p. 35) and sorts principles into those that carry over unchanged and those whose application changes with the medium (p. 36). That is a precedent for the selection rule. He moves between two animation media, not from animation to interfaces.
- **m5 (cuts against the craft).** The principles serve entertainment ("the first goal of the animator is to entertain", p. 43) and the illusion that a character thinks ("Without a thought process, the actions of a character are just a series of unrelated motions", p. 43). A designer who applies them to an AI interface may build exactly the thinking character that L. Stark and Maeda and L. Stark warn about. The paper must say which principles serve the decision and which serve the character.
- **c8.** The run-1 claim that DXD should apply the animator's methods now has a read source for the methods themselves.

## Loci

Matched against the reading-order text layer (`lasseter1987principles.readorder.txt`) and the PDF; page numbers are the printed *Computer Graphics* 21(4) page numbers (PDF p. 1 = p. 35). Inner double quotation marks are changed to single quotation marks.

1. "Understanding these principles of traditional animation is essential to producing good computer animation. Such an understanding should also be important to the designers of the systems used by these animators." §1, p. 35.
2. "Gradually, procedures were isolated and named, analyzed and perfected, and new artists were taught these practices as rules of the trade." §2, p. 36.
3. "Timing, anticipation, staging, follow through, overlap, exaggeration, and secondary action apply in the same way for both types of animation." §2, p. 36.
4. "Motion is achieved by setting keyframe poses and having the computer generate the inbetween frames." §2, p. 36.
5. "The way an object behaves on the screen, the effect of weight that it gives, depend entirely on the spacing of the poses and not on the poses themselves." §2.2, p. 37 (Lasseter cites [30], Whitaker and Halas).
6. "Each inbetween drawing added between these two 'extremes' gives a new meaning to the action." §2.2, p. 37 (Lasseter quoting Thomas and Johnston [26]; the table that follows runs to p. 38).
7. "Proper timing is critical to making ideas readable." §2.2, p. 37.
8. "Anticipation is also a device to catch the audience's eye, to prepare them for the next movement and lead them to expect it before it actually occurs." §2.3, p. 38.
9. "The anticipatory moves may not show why he is doing something, but there is no question about what he is going to do next." §2.3, p. 38 (the words "why" and "what" are letter-spaced in the text layer, which marks emphasis in the print; Lasseter cites [26]).
10. "Staging is the presentation of an idea so it is completely and unmistakably clear" §2.4, p. 38.
11. "It is important, when staging an action, that only one idea be seen by the audience at a time." §2.4, p. 38.
12. "Here the animator plans his actions, figures out just what drawings will be needed to animate the business, makes the drawings concentrating on the poses, relates them to each other in size and action, and then draws the inbetweens." §2.6, p. 40.
13. "The animator indicates the placement of the inbetweens, the slow in or slow out, with a 'timing chart' drawn on the side of the drawing. This tells himself, or his assistant who will be doing the inbetweens later, how he wanted the timing to be and where he wanted the inbetween drawings placed." §2.7, p. 40.
14. "The difficulty in controlling the inbetweens makes it incorrect to approach keyframe computer animation exactly as one would pose-to-pose hand drawn animation." §2.6, p. 40.
15. "the value will shoot in the wrong direction just before (or just after) the large change in value." §2.7, p. 41.
16. "A change in the middle of a major move will go unnoticed, and value intended will be lost." §2.10, p. 42.
17. "The change must come before, or after, the move." §2.10, p. 42.
18. "Without a thought process, the actions of a character are just a series of unrelated motions." §3, p. 43.
19. "Whether it is generated by hand or by computer, the first goal of the animator is to entertain." §4, p. 43.

## Caution

- **Run 1 card superseded.** Run 1 carded this work at abstract depth from the Crossref and OpenAlex records; its S6 verification and S7 hand-check covered those records only and are removed from this file (git history keeps them). The full text now held supersedes it.
- **Eleven, not twelve.** Lasseter numbers eleven principles (p. 36) and treats personality as their application, not a twelfth principle (p. 43). The list on the dxd_animator card (`../../dxd_animator/literature/library/cards/lasseter1987principles.md`) and any draft that says "twelve principles" should not cite Lasseter for the number. "Solid drawing" is not among his principles.
- **Much of the craft content is Thomas and Johnston at second hand.** Lasseter cites Thomas and Johnston (1981) as [26] for staging, anticipation, squash and stretch, secondary action and appeal, and Whitaker and Halas (1981) as [30] for timing. Where the paper uses those passages it should cite them as Thomas and Johnston (1981), as cited in Lasseter (1987), until the book itself is read (`BROWSER_LIST.md` row 24).
- **Practitioner claims about the eye.** Lasseter's statements about perception ("the eye smooths the motion out", p. 37; strobing) are a practitioner's, cited to no perception study. They do not settle the apparent-motion question (CHECK F12).
- **OCR.** The text layer has OCR errors ("key/tame" for "keyframe", "fight" for "right", "pol3q3eA" for "popped"). The loci above were chosen from clean lines; each was found in the text layer.
- **Section order.** In the text layer, the heading "2.7 SLOW IN AND OUT" precedes "2.6 STRAIGHT AHEAD ACTION AND POSE-TO-POSE ACTION" because of column order; the pose-to-pose passage (loci 12, 14) belongs to §2.6 and the timing-chart passage (locus 13) to §2.7, both on p. 40.
- **DOI.** As the run-1 card recorded, a second record, 10.1145/37402.37407 (the *Computer Graphics* 21(4) printing), exists for the same paper. This card keeps 10.1145/37401.37407, the proceedings record the PDF was served under.
- **Personal names and gender.** Lasseter writes "he" for the animator and the assistant throughout; the paper should not carry that over.

## Verification

2026-11-11 · S6 verifier, batch A (Opus 5.5; not the writer) · verdict: corrected · checked: 19/19 loci found (text layer; the PDF p. 6 page image confirms loci 12 and 14 in the left-column §2.6 and locus 13 in the right-column §2.7, and the p. 5 image places the silhouette passage on p. 39), every locator correct (PDF p. N = p. 34 + N), section labels correct; frontmatter vs crossref.json (Lasseter, 1987, proceedings of the 14th annual conference, pp. 35–44, 10.1145/37401.37407), the first page prints *Computer Graphics* 21(4), July 1987, and Crossref returns 10.1145/37402.37407 as the *ACM SIGGRAPH Computer Graphics* 21(4) record, pp. 35–44; sha256 recomputed and matches; full_text honest (10 pp. read); quotations and facts in the body: eleven numbered principles, no "solid drawing", "solid" or "twelve" anywhere in the text, [26] = Thomas and Johnston 1981 Abbeville, [30] = Whitaker and Halas 1981 Focal, the in-between table (none to ten in-betweens, pp. 37–38), "locked" (p. 41), "the eye smooths the motion out" and strobing (p. 37), the OCR examples; claim uses · changed: m1 bullet locator "(p. 38)" to "(pp. 38–39)" · for the lead: (1) m1 stretches the table. Viewers of the in-between table see different in-betweens between the same two extremes, so the readings differ because the visible motion differs; m1 concerns an output that looks the same whatever produced it, so the table fits m1 only if the two extremes alone count as the output. (2) c5: the "depend entirely" sentence, like each paragraph of §2.2 around it, ends on [30]; cite it as Lasseter drawing on Whitaker and Halas, as the Caution already advises for [26]. Loci 8–11 and 16–17 also end on [26]. (3) Takayama, Dooley and Ju (2011) quote this paper ([15]) for the "thinking character" and a mouse-trap passage; neither occurs in this PDF (see takayama2011expressing, Verification), so the paper must not cite Lasseter (1987) for them. (4) The dxd_animator card also lists eleven items, but it splits follow through from overlapping action and omits straight ahead and pose-to-pose; it does not say "twelve" or "solid drawing".

## Hand-check

- 2026-11-11, Claude (Opus 5.5, lead; S7). Verdict: **index**. Writer: the lead; independent check: S6 verifier, batch A. Checked: the verifier's locator fix (silhouette on p. 39) against the PDF text; all 19 loci re-found by the lead when writing (scratchpad check). Changed: the m1 bullet narrowed to an analogy (the in-betweens a film viewer sees are what an agent's user does not see). For the author: Lasseter lists eleven principles, not twelve.
