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
facets: [F9]
claims: [c8, c5]
role: support
load: load-bearing
read_depth: partial
object_read: "version: White Rose eprint 470, deposited copy of the journal article with the HCI page numbers 325–372 printed, 49 PDF pages; place: ~/iit-playground/dxd_animation_local/pdfs/may2003using/ (PDF + .txt), fetched from https://eprints.whiterose.ac.uk/id/eprint/470/1/mayj3.pdf; date: 2026-11-05; sha256: ea3bd9adf162cfbcc6284c2fc139c6d27a0f3c0889237e765521db05345d948c"
verified: corrected
verified_against: "12/12 loci in the eprint text layer and a pdftotext re-extraction (sha256 ea3bd9ad...); Crossref + OpenAlex records; eprint cover and typeset title page"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

May, Dean and Barnard argue that interface designers can borrow from film editors, who guide a viewer through a story despite frequent cuts between shots, but that the borrowing needs a psychological model in between, because film craft books are written for film. Their model, an extension of May and Barnard's 1995 account, predicts that editors place the object the viewer should look at next close to where the viewer was just looking, a practice the authors call collocation. They test whether editors really do this by recording where viewers looked in the 40-millisecond intervals after each of 1,916 cuts (the sum of the three counts they report) in one commercially released film, sorted into 10 classes of cut. The eye-movement pattern fits the collocation predictions broadly but not fully: six classes behaved as predicted (69 percent of cuts), three did not and one was ambiguous. The authors then apply the model to interface design: keep the detail the user is working on in the same screen position when a view changes, prefer a cut to a close-up over a continuous zoom where the user just wants detail, and treat a jump cut as a tool that can interrupt the user on purpose. They run no interface experiment.

## What the paper uses it for

- **c8.** It is the precedent for the paper's move in §5: a craft that handles discontinuity (film editing) is mapped onto interface design through an explicit account of the viewer, and the authors test that the craft works before they transfer it. The authors also note that every interface event is designed, "in the same way that every frame of a film has been constructed by the film's makers", which backs the paper's view that the interface has an animator. The source does not support the full §5 move. It concerns where the eye lands after a cut, not pacing, staging or key poses, and its transfer is argued from theory plus one film, not tested on interfaces.
- **c5.** Partly. The authors treat discontinuity as something craft manages, not a defect, which fits the paper's reading of missing frames. But a film cut is a jump between shots, not a missing in-between frame, so the match is by analogy. One finding cuts the other way: the authors suspect that editors in some cases time the cut after the viewer's eye has already moved, "following their change in gaze rather than driving it" (locus 9). That weakens any use of the source for the claim that the craft steers the viewer.

## Loci

Page locators are the journal page numbers printed in the object read (HCI 18(4), 325–372). Each quotation was matched against the .txt text layer of that object. No inner quotation marks needed changing.

1. "It has been suggested that computer interfaces could be made more usable if their designers utilized cinematography techniques, which have evolved to guide the viewer through a narrative despite frequent discontinuities in the presented scene (i.e., cuts between shots)." Abstract, p. 325.
2. "People rarely emerge from cinemas baffled by film cutting, complaining that they did not know where to look or that they missed crucial elements of the narrative because they were trying to work out what the new shot meant." §1, p. 327.
3. "However, it must be emphasized that an interface event is never directly caused by the user but is always a result of a design decision." §1, p. 328.
4. "Every single interface event has been designed—and needs to be designed well—in the same way that every frame of a film has been constructed by the film’s makers." §1, p. 328.
5. "Filmmakers have learned through one century of experimentation what forms of dynamic scenes are easily comprehended by their viewers and which are not." §2, p. 331.
6. "However, these books are all situated within the domain of film, and it is not at all clear how the knowledge that they contain can be transferred to interface design." §2, p. 331.
7. "May and Barnard (1995) argued that to transfer the craft knowledge from cinematography to interface design economically, an intermediate psychological account was needed" §2, p. 332.
8. "The peak amount of eye movement occurs between 120 and 200 msec after the cut for conversation and previous cuts; between 120 and 280 msec for over-the-shoulder, subjective, and topic cuts; between 200 and 280 msec for end-of-scene cuts; and between 280 and 440 msec for result cuts." §6.2, p. 360.
9. "It may be that in choosing when to cut a shot, in these cases the editor has determined the frame by which the viewer is likely to have moved their gaze, and placed the cut there, effectively following their change in gaze rather than driving it." §6.3, p. 362.
10. "Six of the 10 cuts behaved as we expected (accounting for 1,327 cuts in the entire film, or 69%), three did not (503 cuts), and one was ambiguous (86 cuts)." §6.3, p. 361.
11. "Where the user just wants to get more detail about a particular element, our model suggests that a simple cut to a close-up view would be sufficient" §7, p. 365.
12. "which is generally regarded as unfilmic because of its propositional consequences for the narrative, but which for the same reasons may be valuable in a computer interface because it serves to interrupt processing and attract the user’s attention to the incongruous element of the display." §8, p. 369.

## Caution

- Partial read. I read PDF pp. 1–11 (cover, abstract, §§1–2 and the start of §3; HCI pp. 325–334) and PDF pp. 36–47 (the end of §6.2, §6.3, §7, §8 and the notes; HCI pp. 359–370). I did not read the rest of §3, §§4–5 (the Interacting Cognitive Subsystems model of film watching) or §6.1 and most of §6.2 (method and results; HCI pp. 334–359), nor the reference list. Every claim above about the model and the eye-tracking results rests on the abstract, §6.3 and §§7–8 only.
- The abstract says "Peaks in eye movements between 160 and 280 msec after the cut were detected for 6 of the 10 classes". Locus 8, from §6.2, lists peaks for seven classes (conversation, previous, over-the-shoulder, subjective, topic, end-of-scene, result) between 120 and 440 msec. I did not find a reconciliation in the parts I read. Cite the figures from §6.2 and §6.3, not the abstract, until someone checks the results section.
- The eprint header on PDF p. 1 gives the title "Using film cutting in interface design" and the author order "May, J., Barnard, P. and Dean, M." The typeset article (PDF p. 2) and Crossref give "Using Film Cutting Techniques in Interface Design" and the order May, Dean, Barnard. This card follows the typeset article and Crossref.
- [Verifier, S6] I read the §6.2 results passage (PDF pp. 36–37, HCI pp. 359–360) and the opening of §6.3. Both name peaks for seven classes and none for detail, following and novel cuts; neither explains the abstract's "6 of the 10". The discrepancy stands in the object read.
- Crossref gives the issue date as December 2003 and the volume as 18, issue 4, pages 325–372; the eprint header gives no issue number.
- The eye-movement data come from one film, and the authors say that a test of the rules would need material "produced explicitly for the investigation" with professional filmmakers (§8, p. 370).
- The authors compare film and interface honestly: they write that a film viewer is "passive" while the HCI is "largely under the control of the user" (§1, pp. 327–328). The paper's c6 reading, that the user is also an animator, finds no support in this source; May et al. place the designer, not the user, behind each interface event (locus 3).

## Verification

2026-11-05 · S6 verifier, batch b06 (opus; not the writer) · verdict: corrected · checked: loci 12/12 found, and each PDF page maps to the printed HCI page (PDF n = HCI 323 + n; printed numbers 360, 361, 365, 369, 370 confirmed); metadata vs crossref.json and openalex.json (May, Dean, Barnard; 2003; HCI 18(4), 325–372; DOI) and the eprint cover (Barnard–Dean order, short title); sha256 recomputed and matches; depth partial honest, and the unread sections are listed; summary facts (40-msec intervals, 10 classes, 1,327 + 503 + 86 = 1,916 cuts, "passive" and "under the control of the user" on HCI p. 328, "produced explicitly" on p. 370) found · changed: PDF page count 50 → 49 (pdfinfo); added a Caution note that §6.2–6.3 do not reconcile the abstract's "6 of the 10"

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 12/12 loci found in may2003using.txt; the p. 328 loci sit between the printed running heads 327 and 329; frontmatter vs crossref.json (May, Dean, Barnard; 2003; HCI 18(4), 325–372; DOI) and the eprint cover; sha256 recomputed; partial depth honest, unread sections listed; c8/c5 uses follow the source with their limits stated.
- Changed: nothing.
- For the author: the abstract's "6 of the 10 classes" and §6.2's seven classes with peaks do not reconcile in the parts read (Caution). Quote the §6.2–6.3 figures, not the abstract's, until someone reads §6.1–6.2 whole.
