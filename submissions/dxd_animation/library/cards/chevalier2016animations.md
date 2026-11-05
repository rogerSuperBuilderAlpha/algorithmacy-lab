---
key: chevalier2016animations
apa: "Chevalier, F., Henry Riche, N., Plaisant, C., Chalbi, A., & Hurter, C. (2016). Animations 25 years later: New roles and opportunities. In *Proceedings of the International Working Conference on Advanced Visual Interfaces (AVI '16)* (pp. 280–287). ACM. https://doi.org/10.1145/2909132.2909255"
authors: "Chevalier, Fanny; Henry Riche, Nathalie; Plaisant, Catherine; Chalbi, Amira; Hurter, Christophe"
year: 2016
title: "Animations 25 Years Later: New Roles and Opportunities"
venue: "AVI '16"
volume: ""
issue: ""
pages: "280–287"
doi: "10.1145/2909132.2909255"
url: "https://enac.hal.science/hal-01322962"
type: proceedings
facets: [F9]
claims: [c8]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "version: HAL author copy hal-01322962v1 (submitted 29 May 2016), 9 PDF pages, HAL cover page then the AVI '16 article; place: ~/iit-playground/dxd_animation_local/pdfs/chevalier2016animations/ (PDF + .txt), fetched from https://enac.hal.science/hal-01322962/document; date: 2026-11-05; sha256: bec93627de462aa519291af4ed807ad2c1f3006742cf066d8f697e1254de4cd0"
verified: verified
verified_against: "12/12 loci in pdftotext re-extraction of the HAL PDF (sha256 bec93627...); Crossref + OpenAlex records; title page"
prior_cards: []
status: cited
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Chevalier and four co-authors revisit Baecker and Small's 1990 account of what animation does in a user interface. They reviewed academic papers and commercial systems, collected over 200 examples, and interviewed 20 practitioners and researchers. From this they build a taxonomy of 23 roles in five categories: keeping in context, teaching aid, user experience, data encoding and visual discourse (Table 1, PDF p. 3). For each role they give a definition and examples, and for each category they suggest evaluation methods and research opportunities. They define animation broadly, following Betrancourt and Tversky, as a series of frames in which each frame alters the one before and "the sequence of frames is determined either by the designer or the user". The paper is about animation in interfaces. It does not discuss how a character animator works, apart from one quotation about motion and life (Role 19). Its main claim is that animation does many more jobs than navigation aid and teaching device, including hooking, engaging, persuading and encoding emotion, and that the research community should study those jobs.

## What the paper uses it for

- **c8** (anchor). `../SOURCE.md` cites it with Silvio and Stark for the sentence "researchers and designers must learn and apply the core methodologies of the animator". The source supports a narrower point: interface animation is an established design practice with a catalogue of roles, a set of evaluation methods and a list of known abuses. It does not describe the animator's methods. The use therefore stretches the source, and `../CHECK.md` F11 already says so. The paper can cite it for "interface designers already use animation for many jobs"; for "the animator's method" it needs Thomas and Johnston or an equivalent. The source also cuts against a quiet assumption in c8. Chevalier et al. treat animation as something a designer adds to an interface (Role 13 even lists it as "a distractor to fight boredom when the system is busy"), which is close to the "hide the frames" option the paper argues against.

## Loci

Page locators are PDF pages counted by form feeds in the HAL copy (the cover page is p. 1; the article runs PDF pp. 2–8, which are AVI pp. 280–287 on the title page). The HAL copy prints no ACM page numbers. Each quotation was matched against the .txt text layer of the object read. The inner quotation marks in locus 2 are single quotes in place of the original double quotes.

1. "We revisit Baecker and Small’s pioneering work Animation at the Interface, 25 years later." Abstract, PDF p. 2.
2. "We use the broad definition of animation by Betrancourt and Tversky [7]: ‘computer animation refers to any application which generates a series of frames, so that each frame appears as an alteration of the previous one, and where the sequence of frames is determined either by the designer or the user.’" §2, PDF p. 2.
3. "The contributions of this paper are i) a taxonomy of 23 roles, organized in 5 categories" §1, PDF p. 2.
4. "Animation is now considered a core component of UI design." §2.2.3, PDF p. 5.
5. "Animation is used as a visual feedback to track progress, and a distractor to fight boredom when the system is busy." Role 13, PDF p. 6.
6. "Because animations attract a viewer’s attention, it can be used to keep user engaged (or get their attention back) when an activity require a substantial attention time." Role 11, PDF p. 5.
7. "Animation can be used to make a particular point across with the intent to persuade or convince its viewer." Role 23, PDF p. 7.
8. "Like every other technology animation can be misused to fill a nefarious role." §2.2.5 Opportunities, PDF p. 7.
9. "instead of attracting users’ attention to a new or important item it can be used to distract (focusing attention on the wrong thing as a strategy)." §2.2.5 Opportunities, PDF p. 7.
10. "because of its strong perceptual draw [4], animation might prevent users from perceiving other elements of the display." Role 20 Opportunities, PDF p. 7.
11. "The fact that motion is a good proxy for emotion has been known for long in traditional cartoon animation" Role 19, PDF p. 7.
12. "Our corpus did not cover examples of animation beyond GUIs such as tangible interfaces (e.g. physical visualizations) or augmented reality interfaces." §4.1, PDF p. 8.

## Caution

- The title page of the object read gives "Animations 25 Years Later: New Roles and Opportunities" (HAL copy and article header). Crossref's title field is the short form "Animations 25 Years Later" with the subtitle "New Roles and Opportunities" held separately.
- The AVI page range 280–287 comes from the HAL title page ("pp.280-287") and Crossref. I did not see ACM-printed page numbers.
- `../CHECK.md` F11 is right: the paper reviews interface animation, not the character animator's craft. `../SOURCE.md` (Pass 2) still cites it for "the core methodologies of the animator"; this card leaves that sentence alone.
- The authors say they "opted not to report on the results of published evaluations" (§2.1, PDF p. 3), so the taxonomy does not tell the paper which animation roles work.
- Not an approved tag, but possible: the misuse passage (loci 8, 9) could serve c3 (an animation can steer attention to the wrong thing). The authors say so briefly and cite Pandey et al. on deceptive visualisations; they offer no study of it.
- [Verifier, S6] Crossref splits the second author as given "Nathalie Henry", family "Riche"; the title page and OpenAlex give "Nathalie Henry Riche". The card's "Henry Riche, N." follows the title page; a BibTeX export from Crossref would print "Riche, N. H.", so check the reference list by hand.
- The HAL copy is an author version, "Copyright - All rights reserved". I read the whole text layer, including the reference list.

## Verification

2026-11-05 · S6 verifier, batch b06 (opus; not the writer) · verdict: verified · checked: loci 12/12 found on the stated PDF pages (matched against a fresh pdftotext extraction because the stored .txt interleaves columns); metadata vs crossref.json and openalex.json (authors, year, title/subtitle, AVI '16, pp. 280–287, DOI) and the HAL title page; sha256 recomputed and matches; depth full_text consistent with the 9-page PDF; summary facts (over 200 examples, 20 interviewees, five categories, Table 1 on PDF p. 3, §2.1 evaluation remark on PDF p. 3) found in the text · changed: added one Caution note on the Crossref split of "Henry Riche"
