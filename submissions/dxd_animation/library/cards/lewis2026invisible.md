---
key: lewis2026invisible
apa: "Lewis, C., Collins, S., Hanson, A., Smith, J., & Williams, T. (2026). *Invisible strings: Deriving puppetry principles and their hidden connections to robot behavior design* (arXiv:2607.03289). arXiv. https://doi.org/10.48550/arxiv.2607.03289"
authors: "Lewis, Claire; Collins, Sawyer; Hanson, Alyssa; Smith, Johanna; Williams, Tom"
year: 2026
title: "Invisible Strings: Deriving Puppetry Principles and their Hidden Connections to Robot Behavior Design"
venue: "arXiv (cs.RO; cs.HC)"
volume: ""
issue: ""
pages: ""
doi: "10.48550/arxiv.2607.03289"
url: "https://arxiv.org/abs/2607.03289"
type: preprint
facets: [F12, F11, G2]
claims: [m1, m2, m3, m4, m5, m6, m7]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "version: arXiv v1, p. 1 stamped 'arXiv:2607.03289v1 [cs.RO] 3 Jul 2026', 22 PDF pages; no published version found on 2026-11-11 (the arXiv API record lists v1 only, with no journal reference or DOI; the DataCite record for the arXiv DOI lists no related identifier; a Crossref title search returns no match); place: ~/iit-playground/dxd_animation_local/pdfs/lewis2026invisible/lewis2026invisible.pdf (+ .txt, .readorder.txt), fetched with curl from https://arxiv.org/pdf/2607.03289 (provenance.txt); date: 2026-11-11; sha256: 62a2668cb406b53c36e6c744ac4aa4ff9f82180f443230e6ed43017377985d93; metadata from arxiv.xml (sha256 a07421bbe987bff7fe07084616a5ae6e72e90904d7dd827bfeebf85885e7654d) and datacite.json (sha256 2d32acd3c7a2bbde3ac838adcf981fb5f62c727a4e25f66b5fc771439d9edb2b), both fetched 2026-11-11"
verified: pending
verified_against: ""
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Claire Lewis, Sawyer Collins, Alyssa Hanson, Johanna Smith and Tom Williams argue that roboticists who borrow from the arts have borrowed from art forms that fit robots badly, and that puppetry fills the gap. In their survey, theater says little about specific motions, dance assumes a human body, and Disney's twelve animation principles (Thomas and Johnston, their ref. [115]) work at the level of "low level animation mechanics" (p. 1). Most of those principles also "intentionally leverage the fact that 2D drawings need not adhere to laws of physics" (pp. 3–4): squash and stretch and exaggeration, for example, suit only highly flexible robots unless someone modifies them for rigid bodies (p. 4). Puppetry, by contrast, designs motion for physically embodied, not fully human characters under gravity, and puppeteers reason about morphology and about the interaction between puppet and audience and between puppet and puppeteer (pp. 1–2). The authors want "intermediate knowledge", in Cila's and Höök and Löwgren's sense, that sits between theory and single cases (p. 4).

Their method is a reading of puppetry manuals checked by puppeteers (pp. 4–5). The team was five people: one puppeteer, two HRI researchers and two undergraduates. Over a year the lead undergraduate analysed five books, two suggested by the team's puppeteer (Down 2022; Latshaw 2000) and three by "the director of a major puppetry organization" (Handspring Puppet Company 2009; Millar 2018; C. Williams 2022), and recorded recurring themes grounded in quotations. The first two books yielded thirteen principles, which the team's puppeteer reviewed and revised. A focus group of three professional puppeteers, with over 30 years of experience between them, then merged or dropped principles, leaving eight. The undergraduate drew an illustration for each principle and wrote its translation to robots. The authors built no robot and tested no users.

The eight principles, each followed by the puppeteers' review, a robot design guideline and links to the HRI literature (§§4.1–4.8, pp. 5–17):

1. If the puppet/robot is alive, it is breathing; a breath before an action can cue a human partner (pp. 5–6).
2. The audience fills the gaps: audiences assume emotion, follow attention cues such as a clear silhouette and "passing the ball", and imagine what is not there (pp. 6–9).
3. Use movement and stillness carefully: small constant movement of one or two body parts at a time, so that stillness reads as focus or a change in thought (pp. 9–10).
4. The puppet/robot must focus on something; focus shows interest and what comes next (pp. 10–11).
5. When the puppet/robot talks, it moves accordingly (pp. 11–12).
6. The puppet/robot responds truthfully to its given circumstances (pp. 13–14).
7. Control the puppet's/robot's weight; weight can convey emotion (pp. 14–15).
8. There is an economy of movement; avoid overemphasizing details (pp. 15–17).

In the discussion they place puppetry between theater, which supplies interaction scripts, and dance and animation, which supply "concrete heuristics and parameters" for moment-to-moment motion; animation keeps a low-level role (p. 17). They list three limits: the texts concern live puppetry, most concern Bunraku-style humanoid puppets, and some designers may want to avoid lifelike behaviour altogether (p. 17).

**Deception, over-attribution and ethics, as the text has them.** The paper has no ethics section. Its one ethical phrase asks designers to sense stimuli "with sensitivity to privacy and other ethical considerations" (p. 14). It treats anthropomorphism as a fact to manage, citing Heider and Simmel (p. 8), and it recommends designed illusions without comment: a hand that appears elsewhere in the room so that the user imagines "an invisible arm" (p. 9), and puppeteers who help a puppet "without shattering the illusion" (p. 16). It links unresponsiveness to "distrust" (p. 14). The only counter-note is the limitation that some designers may wish to "avoid lifelike behaviors" (p. 17).

## What the paper uses it for

- **m4 (support for the warrant, and a contrast in kind).** The authors argue that animation principles do not carry over to robots as a list, because the principles assume a medium free of physics and work at too low a level (pp. 1, 3–4). That supports m4's claim that principles do not transfer as lists. Their warrant, though, is the medium (physics, morphology, level of abstraction), not the receiver. Principle 2, "The audience fills the gaps", is a performer's account of audience inference, not of what a receiver needs in order to decide. And their remedy is another list, eight principles "validated" by three puppeteers (p. 17), not an account of the receiver. The paper can cite them for the failure of list-transfer and set its own receiver-based warrant against their medium-based one.
- **m1 (supports the techniques; a warning about the competency).** Several principles are staging by another name: keep a clear silhouette, let one puppet hold attention while the others look at it, move one or two body parts at a time, and keep an economy of movement so that "what people’s eyes are drawn to is what we want it drawn to" (pp. 7, 9–10, 16). Their calibration example is the opaque problem in miniature: a robot that is calibrating may look as if it shrugs in apathy, because "an observer may not understand the reasons for its movements" (p. 8). Their fix cuts against m1. They tell designers to use "consistent affective displays" aligned with the states designers "want audiences to interpret" (p. 8). That gives a stable reading, but one the designer chose, and here a false one, since the robot was calibrating, not feeling. m1 must tie an idempotent reading to the output's cause, not only to a consistent display.
- **m3 (support for anticipation).** A breath before an action signals "that the robot is about to act" so that people "can coordinate" (p. 6); a puppet's focus and intention "can communicate what the puppet will be doing next" (p. 10); and stillness may mark "a change in thought process" (p. 10). This is anticipation and change-marking used for coordination. It concerns the robot's own next move, not a change in the rules a third party applies.
- **m5 (supports the concern; the authors do not share it).** Life-likeness is the aim throughout: nonverbal cues together "create a lifelike embodied character" (p. 1), and breath is the source of the "life" within the puppet (p. 5). The authors tie that craft to trust: a robot that fails to respond to an expected cue risks "distrust and decreased perceptions of competence, intelligence, and animacy" (p. 14). Craft for animacy doubles as craft for trust, with no check on whether the trust is earned. That is the dissociation m5 warns about, stated here as a design goal. No decision appears anywhere in the paper.
- **m6 (a triad without binding).** Puppetry is triadic: puppet, puppeteer and audience. One puppeteer says the audience erases the operator: "the puppeteer completely disappears, even though they’re right there" (p. 8). The image fits the paper's concern that a performing character hides the party behind it, but the puppeteer operates the character and binds no counterpart. The authors treat the erasure as a craft resource, not a risk.
- **m2 (cuts against an easy citation).** The authors read Straight Ahead and Pose to Pose as a low-level way of "controlling an animated character’s movement" (p. 3), and their gloss does not distinguish the two methods clearly. They do not treat pose-to-pose as a division of labour between a key animator and an in-betweener. The paper should take that reading from Lasseter (`lasseter1987principles`), not from this source.
- **m7 and G2 (near miss; the gap stands for this source).** The authors turn a sister craft into design guidelines for robots and argue against carrying animation over, but they select principles by the art form's fit to the medium, not by any user competency, and they never mention decisions, LLMs or an intermediary.

## Loci

Matched against both text layers (`lewis2026invisible.txt`, `.readorder.txt`). Pages are the printed page numbers, which equal PDF page numbers. Locus 1 is found exactly in the layout layer; in the reading-order layer the arXiv side stamp splits it. Locus 3 runs across the page break from p. 3 to p. 4, where the running head "4 Lewis et al." intervenes; each half is found exactly. Locus 8 is a puppeteer's spoken words, quoted without the paper's enclosing double quotation marks. Locus 2 keeps the source's quotation marks around ’key frames’ as printed.

1. "Yet, while these principles bear key insights into the design of like-life characters, their application to robot design is inherently limited, in part because animation is not constrained by real-world physics, and in part because animation principles focus on low level animation mechanics and not high-level design considerations for physically embodied, interactive characters." Abstract, p. 1 ("like-life" sic).
2. "Meanwhile, the principle Straight Ahead and Pose to Pose represent two different ways of controlling an animated character’s movement, using either intermediate ’key frames’ for a character to hit before continuing the movement, or designing an animated character’s movement as moving between pairs of poses." §2.2.3 Animation, p. 3.
3. "However, most animation principles are less readily applicable in robotics because they intentionally leverage the fact that 2D drawings need not adhere to laws of physics — a degree of flexibility not afforded to most robots." §2.2.3 Animation, pp. 3–4.
4. "Our research team consisted of one puppeteer, two human robot interaction (HRI) researchers and two undergraduate students." §3 Method, p. 4.
5. "Following the creation of these original thirteen principles, a focus group was conducted with three professional puppeteers, who discussed and evaluated the principles further as they related to their practice." §3 Method, p. 5.
6. "A breath inward before an action (e.g., before picking up a box) can signal to human counterparts that the robot is about to act, so that they can coordinate and synchronize their movements." §4.1.2, p. 6.
7. "For example, if a robot is calibrating, an observer may not understand the reasons for its movements. Although its actions may be more aligned with stretching or fidgeting, observers might interpret its motion as a shrug of apathy." §4.2.2, p. 8.
8. "Your imagination fills in the gaps, but it also erases things it doesn’t need to see, in the sense of when you’re on stage with a puppet, the audience will notice you for 30 seconds, and then the puppeteer completely disappears, even though they’re right there in front of them." §4.2.1 Puppeteers’ Review (Puppeteer 1), p. 8.
9. "To prevent possible misconceptions about robots’ emotional states, roboticists should intentionally attend to the emotional states that they want audiences to interpret, and use consistent affective displays aligned with those states." §4.2.2, p. 8.
10. "Similarly, a robot designer might design a robot that, when it reaches behind the desk, a hand appears elsewhere in the room and grab something, prompting the user to imagine an invisible arm stretching out (behind the walls) to link robot hand and torso." §4.2.2, p. 9.
11. "If a robot does not respond to a cue (e.g., a siren, being touched, etc.) in the way expected by its audience, this may lead to distrust and decreased perceptions of competence, intelligence, and animacy." §4.6.2, p. 14.
12. "you want the audience to all understand that it picked up a glass, not that it used its thumb with its fingers to create strength." §4.8.1 Puppeteers’ Review (Puppeteer 2), p. 16.
13. "These insights are backed up and validated by the perspectives of the professional puppeteers (most of whom are also actors and improvisers) who served in our focus group." §5 Discussion, p. 17.
14. "Finally, in some cases, roboticists may wish to intentionally avoid lifelike behaviors, in order to reinforce robot-likeness." §5 Discussion, p. 17.

## Caution

- **Preprint.** arXiv v1 of 3 Jul 2026 is the only version found (arXiv record, DataCite record, Crossref title search, all 2026-11-11). The card cites it as a preprint; if a published version appears, its wording and pages may differ. Run-1 triage (`triage/F9-F10.md`, R7; `triage/G.md`) gave the DOI and authors; this card takes them from the arXiv and DataCite records instead.
- **Thin validation.** "Validated" (p. 17) means a single focus group of three puppeteers reviewing principles that one undergraduate drew from five books (pp. 4–5). The paper reports no coding procedure, no reliability check and no test with robots or users. The principles are practitioner consensus, not findings about receivers.
- **How they characterise animation.** The authors know animation through Thomas and Johnston's twelve principles and a few HRI applications (pp. 1, 3–4); they quote no animator's text, and this run did not check their reading against Thomas and Johnston. Their gloss on Straight Ahead and Pose to Pose (locus 2) does not separate the two methods clearly; do not cite it for what pose-to-pose means.
- **Facet F11.** The craft principles the paper states are puppetry's, not animation's. The card files them under F11 as a sister craft; the author may prefer to keep F11 for animation alone.
- **Text errors in the source.** The abstract says "like-life" (p. 1), the affiliation line reads "California Sate University San Bernadino" (p. 1), and the abstract repeats "knowledge knowledge" (p. 1). Loci keep the source's wording.
- **Co-author and source.** The reference list includes Johanna Smith (2019), *Puppetry in Theater and Arts Education* (ref. [108]); the paper does not say whether that author is the co-author or the team's puppeteer, and this card does not assume it.
- Neither `../SOURCE.md` nor `../OUTLINE.md` cites the work, so status is candidate.
