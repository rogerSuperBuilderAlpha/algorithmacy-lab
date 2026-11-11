---
key: thomas2001applying
apa: "Thomas, B. H., & Calder, P. (2001). Applying cartoon animation techniques to graphical user interfaces. *ACM Transactions on Computer-Human Interaction*, *8*(3), 198–222. https://doi.org/10.1145/502907.502909"
authors: "Thomas, Bruce H.; Calder, Paul"
year: 2001
title: "Applying cartoon animation techniques to graphical user interfaces"
venue: "ACM Transactions on Computer-Human Interaction"
volume: "8"
issue: "3"
pages: "198–222"
doi: "10.1145/502907.502909"
url: ""
type: article
facets: [F9, F12]
claims: [c8, m1, m2, m4, m5]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "PDF of the TOCHI article (25 pp., printed pp. 198–222), from the ACM Digital Library (dl.acm.org/doi/pdf/10.1145/502907.502909), opened in Chrome's PDF viewer and saved 2026-11-11 through the author's browser session; ~/iit-playground/dxd_animation_local/pdfs/thomas2001applying/thomas2001applying.pdf; sha256 2632c1ed9c86a76835d9087f15c0a8bcc7f3300134084348fc87083ad26c2ee7; read in full (text and tables; the electronic appendix of movies was not seen); Crossref record crossref.json, sha256 368a21c6e926876840acfb8b7d48eb5a4ae5f7a08c684124e3d1cd810d2feebc"
verified: pending
verified_against: ""
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Bruce Thomas and Paul Calder extend cartoon animation techniques, following Chang and Ungar (1993), to direct-manipulation interfaces. They built animation support into the InterViews toolkit and a drawing editor, *adraw*, and ran two experiments with it.

They frame animation as smoothing changes so that "the interpretation of the change" shifts to "the user's perception system" (p. 200), and they add four principles of their own for direct manipulation (p. 203): **attachment** (the manipulated object stays attached to the pointer), **reluctance** (objects seem reluctant to change, which suggests substance), **smoothness** (continuous change reduces cognitive load), and **anticipation**, which "states that the result of a user's action must be obvious at all times". Their anticipation is a preview of outcome, not a cartoon wind-up: a pinned object stretches toward the pointer but keeps its base fixed, showing that the move "will not succeed" (p. 207); a snapping object stretches until it lets go, showing "what will happen if the object is released at any time" (p. 208).

Two passages bear directly on the model. For **indirect manipulation**, where "the user's attention is focused elsewhere and the change is instantaneous", the change confuses, and "if the initial and final state of the screen are similar, it may not be obvious just what has changed or how the change came about" (pp. 208–209). Their remedy shows an indirect change as if the user had dragged the object, and the distortion conveys "the impression that the action, although indirect, is still under the control of the user" (p. 209). For **trial operations** they show an operation "while it is being considered": the object sits where it will go if the change is committed, with a "telltale corner stretched back to its original position", so that one display carries both the committed and the cancelled outcome (p. 210).

The experiments separate liking from performance. In Experiment 1 (N = 17, a snap-to-grid rearrangement task, four feedback conditions, 200 trials each), an ANOVA "showed no significant difference in execution time between the four feedback conditions", while participants preferred the three feedback conditions to none (p < .001) (pp. 214–215). The authors suggest the task was simple and participants "quickly learned to ignore the feedback (or lack of it)" (p. 215). In Experiment 2 (N = 13, three drawing tasks with an animation-level slider), all but one participant chose a non-zero level; they rated the animation "fun to use" (mean 6.3) and "intuitive to use" (5.5) on a 7-point scale but "were ambivalent about whether it improved productivity (mean = 4.3, sd = 2.0)" (pp. 217–219). Several said shape distortion "made placing objects slightly more difficult" (p. 220).

They conclude that animation "must be used to direct or focus the user's attention to key activities", and that "inappropriate use of animation will merely distract the user by drawing attention to the animation itself rather than the task at hand" (p. 220).

## What the paper uses it for

- **m1 (anchor).** The indirect-manipulation passage is the closest read statement of idempotent interpretation in the interface literature: a change the user did not make directly, with before and after states that look alike, leaves the user unable to tell "how the change came about" (p. 209). Their setting is a single-user editor; the change comes from the user's own indirect command, not from a second party or an intermediary with its own rule.
- **m2 (anchor).** The telltale preview is a read design for intent specification at the point of commitment: show the result of a trial operation while keeping the prior state visibly attached until the user commits or cancels (p. 210). It fits the model's move of showing what lies between the person's commitments as provisional. The authors cite a further study for its effect on recall (Thomas and Demczuk 2000), which this card has not read.
- **m5 (anchor, against the craft).** Both experiments dissociate preference from performance: users liked the animated feedback and found it "fun", yet completion times did not differ and productivity ratings were ambivalent (pp. 215, 219). The paper can cite this as early evidence that craft raises liking without raising task performance. A second passage cuts the same way: animation of an indirect change is designed to give "the impression that the action ... is still under the control of the user" (p. 209), an impression of control the paper's algorithmacy lens would treat with suspicion when another party drives the change.
- **m4 (support).** The authors add four principles derived for direct manipulation rather than carrying the cartoon list over unchanged (p. 203), and they warn that misapplied animation distracts (p. 220). Both support a selection rule. Their criterion is the interaction style, not the user's competencies.
- **c8.** HCI prior art carrying cartoon principles into interfaces, with measured results.

## Loci

Matched against the reading-order text layer (`thomas2001applying.readorder.txt`) and the PDF; page numbers are the printed TOCHI 8(3) pages (PDF p. 1 = p. 198). Inner double quotation marks are changed to single quotation marks; the authors' curly apostrophes are rendered straight.

1. "This article explores how techniques borrowed from cartoons [Thomas and Johnston 1984] and computer animation can enhance the experience of interacting with a computer." §1, p. 199.
2. "Laurel suggests the use of dramatic techniques to encourage users to suspend their disbelief." §1, p. 199.
3. "a smooth change, even it if occurs rapidly, shifts the interpretation of the change to the user's perception system" §2, p. 200 ("even it if" [sic]).
4. "The principle of anticipation states that the result of a user's action must be obvious at all times, which reduces cognitive load by supplying additional visual information and minimizing the use of short-term memory." §3, p. 203.
5. "for changes caused by indirect manipulation, where the user's attention is focused elsewhere and the change is instantaneous, the effect can be confusing." §4.3, p. 208.
6. "if the initial and final state of the screen are similar, it may not be obvious just what has changed or how the change came about." §4.3, p. 209.
7. "the distortion helps convey the impression that the action, although indirect, is still under the control of the user." §4.3, p. 209.
8. "the effect of an operation while it is being considered; the animation suggests both what would happen if the operation is committed and what would happen if it is cancelled." §4.3, p. 210 (the sentence opens on p. 209 with "Instead, we use animation to show").
9. "the object is shown in the position it will adopt if the change is committed, but with a telltale corner stretched back to its original position, as if it were attached by an elastic string." §4.3, p. 210.
10. "The experiment was completed by 17 participants" §5.1.1, p. 214.
11. "showed no significant difference in execution time between the four feedback conditions." §5.1.2, p. 215.
12. "Perhaps participants quickly learned to ignore the feedback (or lack of it) through performing the same task many times." §5.1.2, p. 215.
13. "Data was collected during the experiment from 13 different participants" §5.2.1, p. 217.
14. "participants rated it as 'fun to use' (mean = 6.3, sd = 0.9) and 'intuitive to use' (mean = 5.5, sd = 0.9)." §5.2.2, p. 219.
15. "They were ambivalent about whether it improved productivity (mean = 4.3, sd = 2.0)" §5.2.2, p. 219.
16. "inappropriate use of animation will merely distract the user by drawing attention to the animation itself rather than the task at hand." §6, p. 220.

## Caution

- **Thomas and Johnston's date.** Thomas and Calder cite "THOMAS, F. AND JOHNSTON, O. 1984. Disney Animation: The Illustion [sic] of Life. Abbeville Press" (references). Lasseter (1987) and Chang and Ungar (1993) cite 1981, Abbeville. The run-1 card `thomas1981illusion` and the sibling library's edition record use 1981. The paper should cite one edition and not take the year from Thomas and Calder.
- **Small, student samples.** Both experiments used self-selected computer-science students (17 and 13), simple editing tasks, and Silicon Graphics workstations. The null on completion time may reflect the simple task, as the authors say. The results are weak evidence either way.
- **Anticipation means something different here.** In the cartoon sense (Lasseter; Chang and Ungar), anticipation is a preparatory movement before an action. Thomas and Calder's "principle of anticipation" is that the result of an action is always obvious, a preview of outcome. The paper should say which sense it uses.
- **Single user.** Every case is one user acting on their own objects. No second party, intermediary or evaluation appears.
- **Not read.** The electronic appendix (movies) and the cited follow-up study (Thomas and Demczuk 2000) were not seen.
