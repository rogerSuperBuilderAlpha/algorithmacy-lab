---
key: ribeiro2012illusion
apa: "Ribeiro, T., & Paiva, A. (2012). The illusion of robotic life: Principles and practices of animation for robots. In *Proceedings of the Seventh Annual ACM/IEEE International Conference on Human-Robot Interaction (HRI '12)* (pp. 383–390). ACM. https://doi.org/10.1145/2157689.2157814"
authors: "Ribeiro, Tiago; Paiva, Ana"
year: 2012
title: "The Illusion of Robotic Life: Principles and Practices of Animation for Robots"
venue: "HRI '12"
volume: ""
issue: ""
pages: "383–390"
doi: "10.1145/2157689.2157814"
url: ""
type: proceedings
facets: [F12, F11]
claims: [m5, m4, m1, m3, m2, m7]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "version: ACM DL publisher PDF of the HRI '12 paper, printed pp. 383–390, 8 PDF pages; place: ~/iit-playground/dxd_animation_local/pdfs/ribeiro2012illusion/ (PDF + .txt + .readorder.txt + crossref.json), obtained from dl.acm.org/doi/pdf/10.1145/2157689.2157814 via the author's browser (provenance.txt); date: 2026-11-11; sha256: d61a837d9bbeb088b951f0f47979903a272763eb0282f6c9f48e7d7fa6023af9"
verified: pending
verified_against: ""
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Ribeiro and Paiva borrow from animators to make EMYS, a robot head with eleven degrees of freedom, no lower eyelids and a mouth that only opens and closes, show six basic emotions. They restate the twelve Disney principles one at a time, crediting the list to "Johnston and Thomas [46]", and say how each might apply to a robot. They also draw on the heavier exaggeration of Warner Bros. and MGM and on Jim Henson's puppets, which, like robots, have few moving parts. They built the expressions in Autodesk 3ds Max on a virtual model kept in sync with the physical robot. In phase 1 they reduced FACS and MPEG-4 facial features to nine robot features. A preliminary test, reported elsewhere (their [39]), found that people recognised Anger and Sadness but confused Disgust with Anger and confused the other three with each other. In phase 2 they revised the expressions by hand, using exaggeration, timing, solid drawing (asymmetry), staging, arcs, slow in/slow out and follow-through. They then ran an online video survey: 61 participants from seven countries watched 18 four-second clips (six emotions at intensities 1, 3 and 5) and chose an emotion from a forced-choice list that included "Don't Know". For Anger, Fear and Sadness, over 90% of participants named at least two of the three intensities correctly. Over 60% did so for Surprise and Joy, and 44.3% for Disgust (prose on p. 389; Table 2, p. 388). The authors conclude that animation principles help people understand a robot's emotions and that expressing emotion in a robot is "equivalent to creating the illusion of life". They call the method an artistic process, worked out for one embodiment.

## What the paper uses it for

- **m5.** This is a clear case of craft spent on the character. The authors state the goal as making people believe the robot "actually has a persona and feelings" (locus 14), and their only outcome is whether viewers can name the emotion the robot displays. They measure no decision, task or reliance. The paper can cite it as an instance of robot animation aimed at life-likeness. It cannot cite it for the second half of m5, that such craft raises reliance or attribution without helping a decision, because the study measures neither.
- **m4.** It supports the weaker form of the claim. The authors say the principles must be worked out separately for each embodiment (loci 10–11), that squash and stretch hardly applies to rigid robots (locus 5), and that the method is "currently an artistic process". Their account of the receiver is thin. They tie appeal to understanding (locus 9) and cite Hess on the encoder "who would like to be understood" and the decoder "who strives to understand" (§3.1, p. 386), but their evaluation is a recognition test with no model of the viewer. The source supports the claim that principles do not transfer as a list better than the claim that they transfer through an account of the receiver.
- **m1.** Partly. The authors gloss staging as "making sure that the expressive intention is clear to the viewer" (locus 7) and use it in the revisions, but what the viewer must read is an emotion label, collected as one forced choice per clip. They do not test whether a reading holds on a second look, and they let participants play each clip "any number of times" (§6.2, p. 388). One result shows a display that does not settle a reading: at intensity 1, more viewers chose "Don't Know" than Disgust (locus 13).
- **m3.** The source states this and does not test it. The authors write that anticipation "helps viewers and users to understand what a character is going to do" (locus 6) and that follow-through helps "to mark that an action has ended" (§2.1.1, p. 384). Neither is tested. Their phase 2 revisions name exaggeration, timing, solid drawing, staging, arcs, slow in/slow out and follow-through, but not anticipation (§6.1, p. 388).
- **m2.** Thin, and it cuts against the model's reading of key poses. The authors map pose-to-pose to "pre-designed animation, which can be synced and blended with other kinds of behaviours", and they map straight-ahead to procedural animation (locus 8). In their mapping the generated motion is the straight-ahead kind, not the in-betweens of a key-pose plan. They do not treat key poses as instructions to other hands.
- **m7.** It supports the gap claim as a near neighbour. The authors choose principles to make an emotion recognisable to a viewer, not to support any decision competence.

## Loci

Page locators are the ACM page numbers printed in the object read (383–390; PDF p. N = p. 382 + N). In both text layers the abstract column is interleaved with the introduction, so I matched loci 1–2 against the abstract column cut from the layout `.txt` and read on its own. I matched the rest against the reading-order layer (`.readorder.txt`). The PDF prints a superscript "TM" after "Disney"; loci 1 and 3 omit it. No inner quotation marks needed changing.

1. "We adapted principles and practices of animation from Disney and other animators for robots, and applied them on the development of emotional expressions for the EMYS robot." Abstract, p. 383.
2. "Our work shows that applying animation principles to robots is beneficial for human understanding of the robots’ emotions." Abstract, p. 383.
3. "Most professional animators follow a set of twelve principles that result of more than 60 years of Disney productions. These were compiled in a book by Johnston and Thomas [46], the last two of the Nine Old Men" §2.1, p. 383.
4. "Van Breemen [47] has already proposed to apply the Principles of Animation to robots, claiming user-interface robots to have the same problem of early day’s animations: they miss the illusion of life." §2.1.1, p. 384.
5. "This principle is hard to apply to robots, because robots are generally composed of rigid parts." §2.1.1, Squash and Stretch, p. 384.
6. "Anticipating movements and actions helps viewers and users to understand what a character is going to do." §2.1.1, Anticipation, p. 384.
7. "Staging is related to the general set-up in which the character expresses itself. This principle is related to making sure that the expressive intention is clear to the viewer." §2.1.1, Staging, p. 384.
8. "We can regard this as having a robot to produce interactive, procedural animation (straight-ahead), or pre-designed animation, which can be synced and blended with other kinds of behaviours (Pose-to-Pose)." §2.1.1, Straight Ahead and Pose-to-Pose, p. 384.
9. "Motion and behaviours of robots should also be easy to understand, because if the users don’t understand what they see, their appeal for the robot will fall." §2.1.1, Appeal, p. 385.
10. "Applying principles and practices of animation to robots is currently an artistic process." §6.1, p. 387.
11. "Therefore we must first explore the ground before we can draw conclusions on how to generalize them, because each robotic embodiment will function and express itself in different ways." §6.1, p. 387.
12. "The results for all the expressions yielded significant values." §6.4, p. 388.
13. "Intensity 1 of Disgust had slightly more participants selecting Don’t Know (47.5%) than Disgust (45.9%)." §6.4, p. 389.
14. "Expressing emotions in robots is thus equivalent to creating the illusion of life in robots: making people think and feel that the mechanical being they see in front of them actually has a persona and feelings." §7, p. 389.

## Caution

- **Attribution of the principles.** The running text credits the twelve principles to "Johnston and Thomas [46]" (locus 3). Reference [46] reads "F. Thomas and O. Johnston. The Illusion of Life: Disney Animation. Disney Editions, 1995." (p. 390). So the authors cite a 1995 edition, not the 1981 one, and reverse the author order in the running text. They do not cite Lasseter (1987). They credit van Breemen [47] (a CHI '04 workshop paper, dated 2003 in their list) with first proposing the principles for robots, and they report that van Breemen "called this Merging Logic" (slow in/slow out) in the iCat [48] (p. 384).
- **Strength of the evidence.** Phase 2 has no control condition. The phase 1 results come from a separate study ([39], IVA '11), which this paper reports in one sentence without numbers or a sample size. Locus 12 claims "significant values" but reports no test, statistic or chance level. The claim that the principles are "beneficial" (locus 2) therefore rests on comparing two separate samples, and the authors changed several principles at once for each emotion, so they cannot isolate the effect of any one principle. Participants could replay clips without limit (§6.2, p. 388), and 73.8% said they "appreciate Animation Movies" (§6.3, p. 388).
- **Ethics.** The authors make no statement about deception, over-attribution or ethical risk. They present making people "think and feel" that the robot has feelings as the goal (locus 14), not as a risk.
- **Not this paper.** Schulz, Torresen and Herstad (2019, p. 12:2) quote a definition of robot animation, "expressing identity, emotion and intention", and attribute it to "Ribeiro and Paiva [67]" with the locator "[67, p. 388]". Their [67] is Ribeiro and Paiva's 2017 ICMI paper on the Adelino robot, not this one. The phrase does not occur in this text (I searched the text layer for "identity"). Schulz et al. left this 2012 paper (their [68]) out of their review because its metadata did not mention an evaluation (p. 12:6). Do not attribute that definition to ribeiro2012illusion.
- **Metadata.** Crossref splits the title into title and subtitle ("The illusion of robotic life" / "principles and practices of animation for robots"). The card joins them, as the title page does. The `triage/DECISIONS.md` Tier 2 list names this work correctly as "Ribeiro & Paiva 2012".
- **What I read.** The whole text: abstract, §§1–7, Tables 1–2 and the reference list. The text layer garbles Table 2, so I read it from the PDF page image (p. 388). Each emotion there has a second row that merges the None Correct and One Correct columns, and the Two Correct and All Correct columns. The merged two-or-all figures are: Anger 91.8%, Disgust 44.3%, Fear 91.8%, Joy 60.7%, Sadness 93.4%, Surprise 73.8%).
