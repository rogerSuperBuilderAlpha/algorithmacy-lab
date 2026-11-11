---
key: gonzalez1996does
apa: "Gonzalez, C. (1996). Does animation in user interfaces improve decision making? In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems: Common Ground (CHI '96)* (pp. 27–34). ACM Press. https://doi.org/10.1145/238386.238396"
authors: "Gonzalez, Cleotilde"
year: 1996
title: "Does animation in user interfaces improve decision making?"
venue: "CHI '96"
volume: ""
issue: ""
pages: "27–34"
doi: "10.1145/238386.238396"
url: ""
type: proceedings
facets: [F9, F12, G2]
claims: [m1, m4, m5, m6, m7, c8, c9]
role: support
load: load-bearing
read_depth: full_text
object_read: "version: ACM Digital Library PDF of the CHI '96 paper, 8 pp., a scan of printed proceedings pages 27–34 with an OCR text layer (PDF creation date 19 Nov 2002); place: ~/iit-playground/dxd_animation_local/pdfs/gonzalez1996does/gonzalez1996does.pdf (+ .txt, .readorder.txt), obtained from dl.acm.org/doi/pdf/10.1145/238386.238396 through the author's Chrome session (provenance.txt); date: 2026-11-11; sha256: 5c914fb5b02381a04af474072fd8cfc08c9a405e5746b3743f56916b4fc7b6f5; metadata from crossref.json re-fetched 2026-11-11 (sha256 734734d752295c838283c17fa4fb89218368590d42d048372603ec06d94b9eef)"
verified: pending
verified_against: ""
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Cleotilde Gonzalez asks how animated interfaces should be designed to improve decision making, and she answers with a laboratory experiment. She defines animation in HCI by what it does for the user, not by movement alone: varying images, driven by the user's actions, that help the user see continuous change and build "a more appropriate mental model of the task" (p. 27). She adds that computer animation "seems to be quite different from classical animation" (p. 27, citing Chang and Ungar). The study tests propositions of her Animation User Interface Design (AUID) framework, which predicts that task domain and structure, individual differences (visual ability, experience) and interface features (image realism, transition continuity, interactivity style) together shape decision performance (p. 28). The framework itself is in her 1995 Texas Tech dissertation, reference [7], which this run did not read.

Eighty-nine undergraduates took part for course credit and a $5 incentive tied to accuracy and time (p. 28). Each received one of eight interface treatments, crossing realistic or abstract images, gradual or abrupt transitions, and parallel or sequential interactivity, and each did two choice tasks in balanced random order (pp. 28, 31). In "Home Directory" the subject chose, from twenty rental places described on eleven attributes, the one closest to a stated ideal; in "Bolt in the Boat" the subject chose, from five animated scenarios, the water level that best predicted what happens when a bolt carried in a floating boat is sunk (p. 28). Gradual transitions used a dissolve and changed one element per frame, so that in Home Directory the places appeared one at a time; abrupt transitions showed every place meeting an attribute in a single frame, or the bolt's fall in three screens (pp. 29–30). Parallel interactivity let the user play any segment in any order; sequential interactivity gave play, step and stop buttons (p. 30). Gonzalez measured decision time, decision accuracy (closeness to the single correct answer) and rated ease of use and enjoyability, with visual imagery and computer experience as covariates (pp. 28, 31–32).

The results, as printed: gradual transitions produced more accurate decisions than abrupt ones across both tasks, F(1,78) = 5.84, p < .05. They made no significant difference to decision time, an interaction with task order blocked any claim about ease of use, and subjects' greater enjoyment of gradual transitions did not reach significance (p. 32). Realistic images improved accuracy, time, ease of use and enjoyability, and parallel interactivity improved accuracy and enjoyability (p. 32). Gonzalez reads the transition effect as task-dependent: it mattered more in the physics task, where objects moved, than in Home Directory, where objects appeared and disappeared (p. 33). She concludes that decision-support animation "must be smooth, simple, interactive" and must fit the user's mental model (p. 33). She reports only significance at .05 and Table 2's pattern of significant effects; the text gives no means or effect sizes.

## What the paper uses it for

- **m1 (support, within limits).** The gradual condition is a measured case of "one idea at a time": each frame changed one element, and the rental places entered one by one (pp. 29–30). It raised decision accuracy across both tasks (p. 32), which makes this the clearest read evidence in the library that a staging-like rule moves a decision outcome. The source cuts against the opaque row in three ways. Its tasks were transparent: every attribute was given, and "Only one correct answer existed" (p. 28), so accuracy here means nearness to a known answer, not a reading that survives a second look at an output with many possible causes. The effect sat mainly in the physics task, where motion carried the information (p. 33), so it does not show that pacing helps anyone read a static or textual output. And smooth transitions did not speed decisions (p. 32). The paper can cite it for the finding that changing one element at a time improved accuracy on a transparent choice task, not for idempotent interpretation.
- **m4 (support).** Gonzalez separates computer animation from classical animation (p. 27) and ties each recommendation to the task and the user's mental model: designers should "define transition effects according to the task structure" (p. 33). That is a task-and-receiver warrant for transfer, close to m4. She does not take her smoothness rule from animators. She cites it to Stasko [17], an HCI chapter, as "a basic principle of animation design" (p. 33). The source shows a warrant built from the task, not from the animator's craft.
- **m5 (cuts against a strong reading).** No character appears. The features that raised enjoyment (realistic images, parallel interactivity) also raised accuracy (p. 32), so this study shows affect and accuracy moving together, not the dissociation m5 describes. The one partial split runs the other way: gradual transitions raised accuracy while their effect on enjoyment did not reach significance (p. 32). The paper may use that as a case of craft spent on the decision without a measured affective gain. It should not cite Gonzalez as evidence that affective craft harms decisions.
- **m6 (outside the boundary).** One user, one decision-support display and one correct answer make the study dyadic and transparent. It stands for the dyadic case the model sets aside.
- **m7 (narrows the claim).** The AUID framework is an earlier model that selects animation features by their effect on decision performance, with task and user characteristics as moderators (p. 28). Its "animation" is the computer animation of data displays, not the animator's craft, and it treats the user's visual ability and experience as covariates (pp. 32–33), not as competencies that choose techniques. m7 holds only if it says "animation craft" and "decision competencies" and names Gonzalez as the nearest earlier model.
- **c8 (run-1 tag).** A read precedent for carrying an animation rule into decision support and measuring the result.
- **c9 (run-1 tag).** Not a prior statement of the gap: no LLM, no character, no interface framed as animation in the animator's sense.

## Loci

Matched against the reading-order text layer (`gonzalez1996does.readorder.txt`); the layout layer (`.txt`) interleaves the two columns. Pages are the printed proceedings pages (PDF p. N = p. 26 + N, checked against the page images of PDF pp. 1, 6 and 7). No locus contains inner quotation marks.

1. "Subjects were more accurate with smooth rather than abrupt animation." Abstract, p. 27.
2. "a series of varying images presented dynamically according to user actions in ways that help the user to perceive a continuous change over time and develop a more appropriate mental model of the task [7]." Introduction, p. 27 (italic in print).
3. "However, computer animation seems to be quite different from classical animation [5]." Introduction, p. 27.
4. "In summary, little or no work has been done to study the effect of animation on decision making." Literature review of empirical research of animation interface design, p. 28.
5. "The AUID framework predicts that the task domain and structure, individual differences such as visual abilities and experience, and characteristics of the animated interface such as image realism, continuity of the transitions, and correspondence between the interactivity style and the form of presentation affect decision making performance." Empirical approach, p. 28.
6. "These prototypes created eight treatment conditions (Table 1) that were administered to eighty nine undergraduate students that participated voluntarily in the experiment." Empirical approach, p. 28.
7. "Decision accuracy was the closeness between the user's response and the objective. Only one correct answer existed for a given task." Empirical approach, p. 28.
8. "Besides transition effects, gradual transitions involved the change of only one element in each display frame of the animation." Design of transitions, p. 29.
9. "Observations of accuracy data indicated that animation with gradual transitions produced more accurate responses than animation with abrupt transitions. These observations were statistically significant across tasks (F(1,78)=5.84, p<.05)." Data analysis and results, Interface main effects, p. 32.
10. "Observations of the enjoyability data indicated that gradual transitions caused subjects to enjoy the animation more than abrupt transitions; however, these observations were not statistically significant at the .05 level." Data analysis and results, Interface main effects, p. 32.
11. "Although smoothness is considered a basic principle of animation design [17], the effects of smooth presentations have not always shown to be effective." Discussion of the results, Interface effects, p. 33 (the OCR layer reads "riot" for "not"; the word was read on the page image).
12. "It seems that when the visualization of the movement of the objects is critical to understand the task, gradual transitions are more important to ensure accurate responses than in situations that do not require the objects' movement." Discussion of the results, Interface effects, p. 33.
13. "This research supports the idea that to be an effective decision support tool, animation must be smooth, simple, interactive and explicitly account for the appropriateness of the user's mental model of the task." Conclusions, p. 33.
14. "Finally, the use of animation in more realistic and complex environments is required to support the external validity of these findings." Conclusions, p. 34.

## Caution

- **Run-1 card superseded.** The run-1 card (added 2026-11-05) was a metadata card built from the Crossref record alone, with Loci = None. Its S6 Verification and S7 Hand-check sections covered that record only; they are dropped from this file, and git history keeps them. The smooth-versus-abrupt result, which run 1 held only from a triage note, is now read in the source (locus 1; locus 9).
- **Surname.** The title page prints "Cleotilde Gonzalez" with no accent (p. 27), and Crossref agrees. The run-2 brief and `triage/G.md` write "González". The APA string follows the byline. The OCR layer misreads the byline as "Cleotflde Gonzaiez".
- **Two names for one manipulation.** The abstract says "smooth" and "abrupt animation"; the method and results say "gradual" and "abrupt" transitions. They are the same factor.
- **OCR.** The PDF is a scan. Besides locus 11, the text layer has "perforated" for "performed" and "flame" for "frame" in places; the loci were chosen from clean lines or checked on the page image.
- **Design label.** Gonzalez calls the design a "mixed four-factor within-subjects design" (p. 28), yet the researcher entered one treatment number per subject (p. 31), so the three interface factors vary between subjects and only the task varies within. The paper should describe it as eight interface treatments with two tasks each, not as a within-subjects comparison of transitions.
- **Thin statistics.** Every effect is reported as p < .05 with an F value; the text gives no means, standard deviations or effect sizes, and no per-task accuracy for the transition factor, although the discussion says the effect was stronger in the physics task (p. 33). The subjects were mostly novices and good visualizers (p. 33).
- **Journal version not read.** `triage/F9-F10.md` (R4) lists González and Kasper (1997) in *Decision Sciences* as a fuller version; that record is unchecked this run.
- **Crossref record.** The record re-fetched on 2026-11-11 differs from the 2026-11-05 copy only in its index date and citation count; the earlier copy is kept beside it as `crossref.2026-11-05.json` (sha256 cfe427ba…).
- Neither `../SOURCE.md` nor `../OUTLINE.md` cites the work, so status stays candidate.
