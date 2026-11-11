---
key: may2003using
apa: "May, J., Dean, M. P., & Barnard, P. J. (2003). Using film cutting techniques in interface design. *Human–Computer Interaction*, *18*(4), 325–372. https://doi.org/10.1207/s15327051hci1804_1"
authors: "May, Jon; Dean, Michael P.; Barnard, Philip J."
year: 2003
title: "Using Film Cutting Techniques in Interface Design"
venue: "Human–Computer Interaction"
volume: "18"
issue: "4"
pages: "325–372"
doi: "10.1207/s15327051hci1804_1"
url: "https://eprints.whiterose.ac.uk/id/eprint/470/"
type: article
facets: [F9, F12]
claims: [c8, c5, m4, m1, m5, m7]
role: support
load: load-bearing
read_depth: full_text
object_read: "version: White Rose eprint 470, a deposited copy of the typeset journal article (HCI 18, journal pages 325–372 printed) behind a one-page eprint cover, 49 PDF pages (pdfinfo); place: ~/iit-playground/dxd_animation_local/pdfs/may2003using/may2003using.pdf, with text layers may2003using.txt and may2003using.readorder.txt, fetched 2026-11-05 from https://eprints.whiterose.ac.uk/id/eprint/470/1/mayj3.pdf (FETCH_LOG.tsv); read in full 2026-11-11 (run 1 read pp. 325–334 and 359–370 on 2026-11-05); sha256 ea3bd9adf162cfbcc6284c2fc139c6d27a0f3c0889237e765521db05345d948c (recomputed this run; matches sha256.txt). Records: crossref.json sha256 cb9680b0715c673eb8348629f5ebc57f2765c33395e89fff99e891489473e33c; openalex.json sha256 ec78a2b16f83f022fb4ffb76a81e3825e91e66ea4f4d98eafe8425e1fb780853"
verified: pending
verified_against: ""
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11b
---

# May, Dean & Barnard (2003), Using film cutting techniques in interface design

## What it argues

May, Dean and Barnard argue that interface designers can borrow film editors' craft, but only through an
intermediate psychological account of why the craft works on viewers. Film textbooks are written for film, and
copying their rules case by case, they write, "lacks generalizability" (p. 332). They pick one rule to carry
over, collocation: the editor places the object the viewer should look at next where the viewer was already
looking. They pick it because it rests on "physical location rather than narrative or thematic relations"
(p. 328), which makes it the rule most directly applicable to interfaces.

The account sits in Barnard's Interacting Cognitive Subsystems (ICS) framework (§4). ICS treats cognition as a
chain of subsystems that recode information, each with its own image record of what it has processed, and the
model uses four of its levels: visual (VIS: edges, hues, contrast), object (OBJ: a scene parsed into objects
with location and depth), propositional (PROP: entities with identities and relations) and implicational
(IMPLIC: what the entities are doing and why, with its bodily feeling). Watching film runs VIS→OBJ→PROP→IMPLIC,
while IMPLIC→PROP feeds the viewer's grasp of the story back down as expectation. In this model the viewer is
focally aware of narrative meaning at the implicational level, and seeing the scene is subsidiary work (§5).
"Dynamic control", the bottleneck where processing effort gathers, normally sits at IMPLIC. A cut works when
the new shot fits the representations already active. When it does not, dynamic control moves down to repair
the scene and the viewer loses the story (loci 16–17). Collocation works because an object at the old point of
gaze becomes the new psychological subject at once, so VIS→OBJ need not search: after a collocated cut from a
smoking gun to a falling man, "the viewer sees a shot fired and then sees someone being shot" (p. 349). The
same machinery explains Kubrick's cut from a thrown bone to a space station (a deliberate carry-over of
meaning), why crossing the axis jars (it "makes them attend to the medium", locus 19), and why animation can
transform an object's colour and shape without confusing the viewer (locus 18). The authors add a notation,
transition path diagrams, for tracing each shift of the viewer's attentional subject.

From this account they predict, for ten classes of cut, whether collocation should help (Figure 8, p. 355):
yes for detail, result, following, over-the-shoulder and topical cuts; no for conversation, subjective,
previous, novel and end-of-scene cuts. A collocated cut should produce little eye movement just after it; a
non-collocated cut should produce a peak.

The test (§6) asks whether editors really do this. Five students watched the whole of *The Mask of Zorro*
(132 min, 1,916 cuts) on DVD in widescreen while an eye tracker logged gaze every 20 msec; one participant's
data were excluded, leaving four. The authors dropped 185 cuts that another cut followed within 1 sec, leaving
1,731, and for each class computed the size of the change in gaze position, ignoring direction, in 16
successive 40-msec intervals from 40 msec before to 600 msec after the cut. Seven classes showed a peak
(locus 8); detail, following and novel cuts showed none. The authors count six classes as behaving as
expected, three not, and one (result, whose peak came late) as ambiguous (locus 10). Their predictions for
topical and novel cuts were "clearly in the wrong direction" (p. 363). The fastest eye movements, after
conversation cuts, came too soon to be reactions to the new shot, so the authors suggest that the editor may
be following the viewer's gaze rather than driving it (locus 9).

§§7–8 turn the account into interface advice: keep the detail a user zooms on in the same screen position,
show the result of an operation where the operation happened, prefer a cut (or a few discrete steps) to a
continuous fly-through when the user only wants detail (locus 11), pass through an overview between two
close-ups, and use the film-breaking jump cut on purpose to interrupt the user (locus 12). The authors test
none of this. Their interface material is a design proposal for a small-screen map, a fictional interface in
*Blade Runner*, an informal modelling session with designers at a workshop, and a preference finding for the
hydra videoconferencing system that they cite from Sellen (1992). They close by proposing the test they did not
run, eye tracking "within a conventional HCI environment" (p. 370).

## What the paper uses it for

- **m4** (transfer warrant: craft carries over only through an account of the receiver). This is the clearest
  precedent the library holds. May et al. reject case-by-case borrowing (locus 6), require "an intermediate
  psychological account" that explains the craft "in terms of their consequences for the viewers’ mental
  processing" (locus 7), and call such a model "an essential intermediate stage" (locus 14). They also mark
  where the account's assumptions fail for interfaces: a film viewer already has the procedural knowledge to
  read what is shown, while interface elements are "symbolic and abstract" (locus 15). Three limits. Their
  account is perceptual (where the eye goes after a cut), and they leave narrative comprehension out of the
  model on purpose because it "is less important in HCI than in film" (p. 338); a decision is made at the
  levels they bracket. Their transfer is argued from the account plus one film and never tested on an
  interface. And their own data reversed two of the account's predictions (p. 363), so the warrant is a model
  with known misses, not a validated one.
- **m1** (opaque row; the paper's case against "showing the frames" or exposing the backend). Two passages
  support the claim that turning the receiver's attention to the medium costs them the meaning. May et al.
  report Kraft's (1986) finding that viewers could attend to the cutting or to the meaning of the scenes, "but
  not both" (locus 13), and they say that crossing the axis "makes them attend to the medium" (locus 19). In
  ICS terms, anything that pulls dynamic control away from IMPLIC loses the viewer the story (locus 17). The
  use is by analogy: May et al. write about cuts and screen layout, not about exposing a system's internals,
  and the Kraft result reaches this card second-hand.
- **m5** (dissociation: craft spent on the character versus craft spent on the decision). May et al. draw a
  parallel split for film. They set aside the editing advice aimed at "leading the viewer to infer motive and
  intention" as "not directly relevant to interface design" (p. 332), and keep the craft that serves the
  viewer's perceptual task. Their split is narrative versus perception, not character versus decision, so it
  is a precedent for the shape of m5, not for its content.
- **m7** (gap). Of the works this library holds, May et al. come nearest to a prior model that selects screen
  craft through an account of the receiver. They select film-editing craft through a model of perception and attention, not animation craft
  through decision competencies, so they bound the gap rather than close it. The gap statement should name them.
- **c8** (run 1; §5 maps the animator's methods onto interface design). The source models the move: a craft
  that handles discontinuity is mapped onto interfaces through an explicit account of the viewer, and the
  authors check that editors use the craft before transferring it. They also put a designer behind every
  interface event, "in the same way that every frame of a film has been constructed by the film’s makers"
  (locus 4). The source does not support the full §5 move: it concerns where the eye lands after a cut, not
  pacing, staging or key poses, and its interface advice is untested.
- **c5** (run 1; missing frames, the interstices are the craft). Partly. The authors treat discontinuity as
  something craft manages, not a defect, and their sentence on animation craft (locus 18) says animated objects
  can change colour and shape across frames without confusing the viewer. (Their only other mention of
  animation, on p. 364, concerns three-dimensional data displays.) But a film cut is a jump between shots,
  not a missing in-between frame, so the match is by analogy.

## Loci

Page locators are the journal page numbers printed in the object read (HCI 18, 325–372); PDF p. = HCI p. − 323,
which I checked against the running heads. I matched each quotation on the stated page against both text layers
(may2003using.txt and may2003using.readorder.txt, with line-end hyphens joined and running heads dropped), and
each occurs once. Locus 18 crosses a page break and the Figure 3 caption, so I matched its two halves
separately and read both page images (PDF pp. 21–22). No inner quotation marks needed changing. Loci 1–12 keep
run 1's numbers.

1. "It has been suggested that computer interfaces could be made more usable if their designers utilized cinematography techniques, which have evolved to guide the viewer through a narrative despite frequent discontinuities in the presented scene (i.e., cuts between shots)." Abstract, p. 325.
2. "People rarely emerge from cinemas baffled by film cutting, complaining that they did not know where to look or that they missed crucial elements of the narrative because they were trying to work out what the new shot meant." §1, p. 327.
3. "However, it must be emphasized that an interface event is never directly caused by the user but is always a result of a design decision." §1, p. 328.
4. "Every single interface event has been designed—and needs to be designed well—in the same way that every frame of a film has been constructed by the film’s makers." §1, p. 328.
5. "Filmmakers have learned through one century of experimentation what forms of dynamic scenes are easily comprehended by their viewers and which are not." §2, p. 331.
6. "However, these books are all situated within the domain of film, and it is not at all clear how the knowledge that they contain can be transferred to interface design." §2, p. 331.
7. "May and Barnard (1995) argued that to transfer the craft knowledge from cinematography to interface design economically, an intermediate psychological account was needed, which described why the craft knowledge worked in terms of their consequences for the viewers’ mental processing." §2, p. 332.
8. "The peak amount of eye movement occurs between 120 and 200 msec after the cut for conversation and previous cuts; between 120 and 280 msec for over-the-shoulder, subjective, and topic cuts; between 200 and 280 msec for end-of-scene cuts; and between 280 and 440 msec for result cuts." §6.2, p. 360.
9. "It may be that in choosing when to cut a shot, in these cases the editor has determined the frame by which the viewer is likely to have moved their gaze, and placed the cut there, effectively following their change in gaze rather than driving it." §6.3, p. 362.
10. "Six of the 10 cuts behaved as we expected (accounting for 1,327 cuts in the entire film, or 69%), three did not (503 cuts), and one was ambiguous (86 cuts)." §6.3, p. 361.
11. "Where the user just wants to get more detail about a particular element, our model suggests that a simple cut to a close-up view would be sufficient" §7, p. 365.
12. "which is generally regarded as unfilmic because of its propositional consequences for the narrative, but which for the same reasons may be valuable in a computer interface because it serves to interrupt processing and attract the user’s attention to the incongruous element of the display." §8, p. 369.
13. "Therefore, they were able to attend to the physical structure of the film cutting, or to the meaning of the scenes portrayed, but not both (Kraft, 1986)." §3, p. 335.
14. "To make a mapping from the language and technology of film to computer interface design, a model of these processes is an essential intermediate stage." §3, p. 335.
15. "For the interpretation of a film, we can assume that the procedural knowledge is all in place: that is, the images on the screen, the events portrayed, and their meanings will all be within the viewer’s body of experience; the processes would, in principle, have little difficulty carrying out transformations of what is shown. This may not be the case in the comprehension of computer interfaces where the display elements are more likely to be symbolic and abstract, and so would be a clear point of departure for the modeling of cognition." §4, p. 337.
16. "In what follows, we argue that inconsistencies between the subsidiary task and the primary task distract the viewer from comprehending the narrative, and so are generally to be avoided unless such an interruption is desired, perhaps for rhetorical effect." §5, p. 341.
17. "For clear comprehension, then, a dynamic display or a film should avoid locating dynamic control away from the IMPLIC subsystem." §5, p. 342.
18. "A similar technique is extensively used in animation, where elements can undergo spectacular transformations of color and shape quite unlike those of their real-world counterparts without producing any propositional problems for the viewers—their reaction to the bizarre incongruities in the implicational representation being amusement." §5.1, pp. 344–345 ("view-/ers" is split across the page break).
19. "Although crossing the axis can be overcome quickly by the top-down constraints of the narrative, it momentarily distracts the viewer from the message of the film and makes them attend to the medium." §5.2, p. 352.
20. "In the film’s 132 min, there were 1,916 cuts (roughly one every 4 sec)." §6, p. 354.
21. "There were five participants in this experiment, all students at the University of Sheffield." §6.1, p. 357.
22. "One hundred eighty-five cuts that were followed by another cut within 1 sec were omitted from the analysis (by proportion, mainly result, detail, or following cuts), leaving 1,731 cuts per participant." §6.2, p. 358.

## Caution

- **Run 2 rewrite.** Run 1's card (2026-11-05) was `partial`: it read HCI pp. 325–334 and 359–370 and had 12
  loci (`verified: corrected`). In this run I read the whole object, pp. 325–372 with notes and references, so
  the card is now `full_text`. I re-found all 12 loci, kept their numbers, and extended locus 7 to the end of its
  sentence; I added loci 13–22 from pp. 335–358, the parts run 1 had not read. I rewrote "What it argues"
  around the ICS account, added claims m4, m1, m5 and m7 and facet F12, and corrected two run-1 statements: the
  analysis covered 1,731 cuts, not 1,916, and it measured how far gaze moved, ignoring direction, not where
  viewers looked. I removed run 1's `## Verification` and `## Hand-check` sections, which checked the partial
  read; git history keeps them.
- **The count.** The film has 1,916 cuts (locus 20; repeated on p. 357). After dropping 185, the analysis used
  1,731 (locus 22). Figure 8 (p. 355) gives class counts of 54, 61, 276, 560, 142, 26, 149, 341, 95 and 27; I
  read them on the page image, and they sum to 1,731, so they are the analysed cuts, although the caption calls
  them the "number of each within the film". §6.3's 1,327 + 503 + 86 (locus 10) sums to 1,916, so those are
  whole-film counts: on Figure 8's numbers the same three groups hold 1,208, 462 and 61, and the differences
  (119 + 41 + 25) add up to the 185 dropped cuts. I computed these sums. Separately, the classification check
  queried "185 cases (9.7%)" (p. 355); the paper does not say whether the two 185s are related.
- **The abstract's "6 of the 10".** Partly reconciled, by my reading only. §6.2 and Figure 8 report peaks for
  seven classes; six of them end by 280 msec (120–200, 120–280 or 200–280) and the seventh, result, runs 280–440
  msec. The abstract's "Peaks in eye movements between 160 and 280 msec after the cut were detected for 6 of
  the 10 classes" fits those six, but its lower bound (160) does not match §6.2's (120), and the paper never
  states the reconciliation. The abstract's six is also not §6.3's six that "behaved as we expected", which
  include detail and following, the classes with no peak. Cite Figure 8 and §§6.2–6.3, not the abstract.
- **The abstract rounds up.** It concludes that editors "do successfully use collocation" for detail,
  following and result cuts. §6.3 calls result ambiguous (locus 10), finds a "comparatively high proportion of
  large changes made for detail cuts" (p. 361), and calls the detail data "the most noisy" (p. 363). For the
  three no-peak classes the evidence is an absence: the authors write that they "can be said not to induce eye
  movements" (p. 361), on data from four viewers.
- **Following or driving.** The authors' own caveat (locus 9) concerns the fastest cuts, "in these cases"
  conversation cuts, where the end of an utterance, prosody and glances cue the cut, and they conclude that
  "these eye movements must use information available to the viewer prior to the cut and might even have been
  initiated before the cut" (p. 362). The caveat does not touch the collocation classes directly, but it shows
  that part of what looks like the editor steering is the viewer anticipating. Do not cite May et al. for "the
  craft drives the viewer's gaze" without it.
- **No interface was tested.** The authors run no interface study. Their interface evidence is a design
  proposal (the small-screen map, Figure 11), a fictional interface (*Blade Runner*), their own informal
  modelling of an electron-microscopy package at a designers' workshop, and a finding they cite: "Sellen (1992)
  reported that people preferred this system to a single screen with multiple windows" (p. 367), which concerns
  videoconferencing, not collocation. They propose the interface test for future work (p. 370).
- **Sample and stimulus.** One film, on DVD, viewed on a widescreen television at about 22° by 9°; five
  participants, one excluded because 9.5% of their coordinates fell off the screen, four analysed (pp.
  357–358). The authors themselves say a test of the rules would need material "produced explicitly for the
  investigation" with professional filmmakers (p. 370).
- **Viewer versus user.** The authors call the film viewer "passive" because they "cannot change the film or
  alter its rate of progress" (p. 328), while the interface user drives the interaction; in their own examples
  the display is still composed by the computer (p. 367). The c6 reading, that the user is also an animator,
  finds no support here: May et al. put the designer behind every interface event (locus 3).
- **Second-hand sources.** Kraft (1986, 1987), Hochberg (1986), Richards (1992), Boorstin (1991) and Sellen
  (1992) reach this card only through May et al. Cite them only after reading them.
- **Title and author order.** The eprint cover (PDF p. 1) gives "Using film cutting in interface design" and
  the order "May, J., Barnard, P. and Dean, M." The typeset article (PDF p. 2) and Crossref give "Using Film
  Cutting Techniques in Interface Design" and the order May, Dean, Barnard. The card follows the typeset
  article and Crossref. Crossref gives print date December 2003, vol. 18, issue 4, pages 325–372; the typeset
  page header gives "HUMAN–COMPUTER INTERACTION, 2003, Volume 18, pp. 325–372" with no issue number.
