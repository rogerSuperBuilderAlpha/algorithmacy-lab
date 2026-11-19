---
key: dragicevic2011temporal
apa: "Dragicevic, P., Bezerianos, A., Javed, W., Elmqvist, N., & Fekete, J.-D. (2011). Temporal distortion for animated transitions. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '11)* (pp. 2009–2018). ACM. https://doi.org/10.1145/1978942.1979233"
authors: "Dragicevic, Pierre; Bezerianos, Anastasia; Javed, Waqas; Elmqvist, Niklas; Fekete, Jean-Daniel"
year: 2011
title: "Temporal Distortion for Animated Transitions"
venue: "CHI '11"
volume: ""
issue: ""
pages: "2009–2018"
doi: "10.1145/1978942.1979233"
url: "https://inria.hal.science/inria-00556177"
type: proceedings
facets: [F9]
claims: [c8, c5]
role: support
load: load-bearing
read_depth: full_text
object_read: "version: HAL author copy inria-00556177v2 (submitted 4 Jun 2012), 11 PDF pages, HAL cover page then the CHI '11 article; place: ~/iit-playground/dxd_animation_local/pdfs/dragicevic2011temporal/ (PDF + .txt), fetched from https://inria.hal.science/inria-00556177/document; date: 2026-11-05; sha256: b6a7c995774f5d197e3cde1fa0763874f33faabce7f6b5a0cbc392fddc0eb893"
verified: corrected
verified_against: "10/10 loci in pdftotext re-extraction of the HAL PDF (sha256 b6a7c995...); Crossref + OpenAlex records; title page"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Dragicevic, Bezerianos, Javed, Elmqvist and Fekete test a rule that interface designers had borrowed from cartoon animation: slow-in/slow-out pacing, where an animated transition starts slowly, speeds up and ends slowly. Designers adopted the rule by informal guideline, and the authors say nobody had tested it. They compared four pacing strategies in an object-tracking experiment: constant speed, slow-in/slow-out (SI/SO), fast-in/fast-out (FI/FO) and an adaptive strategy that slows down around the visually busiest frames. Twelve students tracked one point among identical points (200 in the generated data, 1,038 in the real camera data) that moved for one second, and the authors measured how far the point they chose lay from the true target. SI/SO gave the lowest error on the generated data and on a real camera dataset. The adaptive strategy matched SI/SO only when the busy frames fell at the start or end of the move, and otherwise did worse than constant speed. The authors explain this by predictability: a gradual start and stop help the eye begin and end smooth pursuit. They conclude that the endpoints matter more than the complex middle, and they say their study does not address whether to animate at all.

## What the paper uses it for

- **c8.** It shows that one animator's principle (slow-in/slow-out, which the authors trace to cartoon animators, citing Chang and Ungar and Johnston and Thomas) was carried into interfaces and then measured. That is a worked case of "apply the animator's methods", and it supports the `../OUTLINE.md` §5 move of turning timing into pacing. The source also cuts against a naive version of that move. The authors end by saying interface work "has largely been dominated by design principles from general animation that may not necessarily transfer to interaction design", and their pacing rule that follows the viewer's load (the adaptive strategy) lost to the plain animator's rule. The paper should not cite it as showing that the animator's rules transfer without test.
- **c5.** Thin. The study concerns how a viewer follows motion that is present; it does not deal with missing frames. The nearest link is that the authors allocate a fixed "frame budget" and say that slowing one stretch means speeding another. The paper can use that as an analogy for pacing a stream to load (`../OUTLINE.md` §4.1), but the authors tested one-second point-cloud moves, not text streams or decisions.

## Loci

Page locators are PDF pages counted by form feeds in the HAL copy (cover page = p. 1; the article starts on PDF p. 2, which is CHI p. 2009 on the title page). The HAL copy prints no ACM page numbers. The text layer interleaves the two columns, so each quotation was matched against one column read on its own. Inner double quotes are rendered as single quotes in locus 3.

1. "One informal design guideline for creating effective animated transitions has long been the use of slow-in/slow-out pacing, but no empirical data exist to support this practice." Abstract, PDF p. 2.
2. "Slow-in/slow-out outperformed other techniques, but we saw technique differences depending on the type of visual transition." Abstract, PDF p. 2.
3. "cartoon animators sometimes use a ‘slow in’ or ‘slow out’ effect [8, 18]" Introduction, PDF p. 2.
4. "However, no perceptual studies have been performed to confirm this informal design rule." Introduction, PDF p. 2.
5. "SI/SO was significantly more accurate than C and FI/FO, with no significant difference between SI/SO and A." Results, Real Dataset, PDF p. 7.
6. "Constant speed motion is better than adaptive speed and FI/FO for all other distractor profiles (dm and do), second only to SI/SO." Discussion, PDF p. 8.
7. "In other words, easing in and out of an animation seems much more important than slowing down and speeding up around frames of high visual complexity." Discussion, PDF p. 8.
8. "Another potential limitation is that our study only measured tracking of a single object" Limitations, PDF p. 9.
9. "our work has not addressed the question whether or not to use animation in the first place, but rather which pacing methodology should be chosen if animation is adopted in an interactive application." Generalizations, PDF p. 9.
10. "an area that so far has largely been dominated by design principles from general animation that may not necessarily transfer to interaction design." Conclusion, PDF p. 10.

## Caution

- `../CHECK.md` and the triage table list the authors correctly as Dragicevic, Bezerianos, Javed, Elmqvist, Fekete (title page, Crossref, OpenAlex agree). FACETS F9 lists "Chevalier" in place of Elmqvist; that is wrong. This card leaves FACETS alone.
- The triage note (F9) credits the slow-in/slow-out principle to Lasseter. The text of this paper attributes it to cartoon animators, citing [8, 18] (PDF p. 2). [Verifier, S6: corrected] In a pdftotext re-extraction the reference list reads cleanly: [8] is Chang and Ungar, "Animation: From cartoons to the user interface", and [18] is Johnston and Thomas, *The Illusion of Life*. Lasseter is [24], "Principles of traditional animation applied to 3D computer animation"; the authors cite him for the transfer of the animation principles to computer animation (PDF p. 3) and for non-straight paths, not for slow-in/slow-out itself. The card does not name Lasseter as the source of slow-in/slow-out.
- Scope limits the authors state: identical grey squares, one tracked point, straight paths, one-second transitions, 12 participants, the participant starting each trial by pressing the space bar. Locus 8 records the single-object limit.
- Locus 5 reports the real-dataset result. On the generated dataset the authors report mean selection error of 0.28 for SI/SO against 0.49 for constant, 0.63 for adaptive and 0.65 for FI/FO (PDF p. 7).
- I read the whole text layer, including the appendix on point-cloud generation (equations) and the reference list.

## Verification

2026-11-05 · S6 verifier, batch b06 (opus; not the writer) · verdict: corrected · checked: loci 10/10 found on the stated PDF pages (locus 2 across the line-end hyphen "slow-/out"); metadata vs crossref.json and openalex.json (five authors with Elmqvist, 2011, CHI '11, pp. 2009–2018, DOI) and the HAL cover; sha256 recomputed and matches; depth full_text consistent with the 11-page PDF; summary facts (12 paid students, n = 200 generated points, 1,038 camera objects, 1-second transitions, errors 0.28/0.49/0.63/0.65, Space bar, frame budget, smooth pursuit) found in the text · changed: [8, 18] attributed correctly (Chang and Ungar; Johnston and Thomas) in the c8 bullet and Caution; Lasseter located as ref [24] and his actual use recorded in Caution

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 10/10 loci found in a fresh pdftotext extraction of the HAL PDF (sha256 b6a7c99… unchanged); PDF pages by form feed (cover = p. 1): all ten locators correct (locus 2 across "slow-/out", locus 3 with the double quotes converted, locus 6 as a bullet item); [8] = Chang and Ungar, [18] = Johnston and Thomas, [24] = Lasseter, 12 participants, 1,038 objects and the 0.28/0.49/0.63/0.65 errors confirmed; frontmatter vs crossref.json and openalex.json (five authors with Elmqvist, CHI '11, 2009–2018, DOI); claim uses: c8 is a fair worked case with its counter-reading stated; c5 is marked thin.
- Changed: nothing.
- For the author: FACETS F9 lists "Chevalier" in place of Elmqvist among the authors; FACETS is outside the cards and was left alone.
