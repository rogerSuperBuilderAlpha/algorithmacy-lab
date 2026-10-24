# Margono, S., & Shneiderman, B. (1987). A study of file manipulation by novices using commands vs. direct manipulation (Technical Report CAR-TR-264). University of Maryland.

**Identifier:** https://www.cs.umd.edu/users/ben/papers/Margono1987Study.pdf · **Read depth:** full_text (14-page author-hosted PDF from the UMD page; the text carries no printed page numbers, so locators are section numbers; Table 1 did not survive text extraction, so its standard deviations were not read) · **Source-tier:** technical report · **Evidence basis:** direct_read · **Design and sample:** within-subject comparison, N = 30 novices (18 from a psychology subject pool, 12 by personal contact); each used both an Apple Macintosh and an IBM PC with MS-DOS; file tasks create, copy, rename, erase · **Parties modeled:** person–system · **Facets:** F · **Read:** 2026-10-13

## What it argues
The authors test whether a direct-manipulation interface suits novices better than a command interface. Section 1.1 lists the four properties they take from Shneiderman (1983): continuous representation of the objects of interest; physical actions in place of syntax; "rapid, incremental, reversible actions"; and layered learning. They add Norman's two aspects of directness, distance and engagement, and say the goal is that "the user should learn the task domain instead of the computer system" (§1.1).

Procedure (§2.4): a demo, two practice rounds (maximum 20 minutes per machine), then four tasks performed without the instruction sheet (maximum 20 minutes), then a questionnaire. Each subject used both machines; the report says two subjects shared each one-hour session, one starting on each machine. An eight-subject pilot preceded the 30 (§2.4.1). Satisfaction is an "ad hoc scale" built from two six-point questions plus one point for the preferred machine (§2.4.2).

Results (§3): mean test time 5.77 min on the PC against 4.80 min on the Macintosh, "statistically significant by t-test at the p < 0.10 level"; mean errors 2.03 against 0.80 (p < 0.01); satisfaction 3.80 against 5.37 "out of a 7 point scale" (p < 0.01). Practice means were 9.37 and 8.2 min (first round) and 5.1 and 4.8 min (second). Eighteen subjects preferred the Macintosh, ten the PC, one was undecided, one liked both. Discussion (§4): "almost all" struggled with the mouse at first, more than twenty mastered it in nine to ten minutes, and five struggled throughout; on the PC, subjects forgot punctuation, added spaces and omitted parameters. The authors conclude the study gave "some support" for the Macintosh being more user-friendly, and warn that "this experiment dealt only with novices in a learning situation" and that frequent and expert users "often prefer and may work more rapidly with command language strategies" (§5).

## Relation to the argument
Supports the claim in facet F that a re-representation of a task (visible objects, pointing in place of recalled syntax) lowers the cost of a first encounter, with the weakest-supported parallel to word separation: the work of recalling and typing syntax moves into the artefact. It bears on D10 (the history is a guide, and the novice/expert claim is open): the authors themselves limit the result to novices and say experts may prefer commands. That caveat is the one the paper should carry.

Facet check: the facet's figures (30 novices, 5.77 and 4.80 min at p < 0.10, errors p < 0.01, 18 against 10 preferring the Macintosh) match the text. The facet's caveat that the comparison confounds interface style with machine is correct and the source never addresses it: the Macintosh and PC differ in screen, keyboard and mouse as well (§1.3). The satisfaction figure rests on an ad hoc composite, and the time difference is significant only at p < 0.10. The test time is under five minutes in both conditions.

## In conversation with
- `shneiderman1983direct`: the source of the four-property definition of direct manipulation the report adopts.
- `hutchins1985direct`: the report cites "Hitchins, Hollan, and Norman" (User Centered System Design, 1986), a misspelling of Hutchins; that book is the same group's work on directness (distance and engagement), but the bib entry is the 1985 article, so treat the link as the shared authors and idea.
- Leads not in the bib: Norman (1984), "Stages and levels in human-machine interaction"; Rubinstein and Hersh (1984), *The Human Factor*; Burns and Veint (1985), PC Magazine comparison.

## Caution
A small, unreplicated, two-machine comparison with a lenient significance level on the time measure, one hour per subject, and a self-built satisfaction scale. It shows nothing about long-run or expert performance, and nothing about coordination through a third party.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the author-hosted UMD PDF named in the card (title, authors, report text match). Checked 6 quotations and about 25 numbers or procedural claims (N = 30 and its 18/12 split, pilot of 8, practice and test means, errors, satisfaction scale, preference counts, section numbers, cited works) against the extracted text.

**Findings:** No issues found. The citation to 'Hitchins, Hollan, and Norman' is in the reference list as the card says.
