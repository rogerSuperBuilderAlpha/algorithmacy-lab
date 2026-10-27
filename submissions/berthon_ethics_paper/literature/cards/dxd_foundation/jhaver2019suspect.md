# Jhaver, S., Appling, D. S., Gilbert, E., & Bruckman, A. (2019). "Did you suspect the post would be removed?": Understanding user reactions to content removals on Reddit. *Proceedings of the ACM on Human-Computer Interaction, 3*(CSCW), Article 192.

**Identifier:** doi:10.1145/3359294 · **Read depth:** full_text (published PDF, 33 pp.; journal pagination 192:1–192:33). I read the body and the reference list; of Appendix A (the 24-item questionnaire) I read only items 15–24 · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** one-shot survey of Reddit users whose posts had just been removed. The authors drew 10,000 recent submissions from randomly chosen subreddits, waited three hours, found the removed ones and messaged the authors; 1,054 people submitted and 907 remained after cleaning (8.2% of those contacted) (192:9–10). 61% US, 81% male, 55% under 25 (192:10). Linear regressions on two five-point items, plus coding of 849 open-ended answers (192:13, 19) · **Parties modeled:** two parties plus a third party (poster, volunteer moderators who hold the rule, and the platform that supplies the tools) · **Facets:** J · **Read:** 2026-10-13

## What it argues

Jhaver and colleagues ask how people react hours after a moderator removes their post, and whether community rules and removal explanations change that. Most react badly: 10.3% strongly agree and 13.6% agree the removal was fair, against 33% and 26.9% who disagree (192:13). The abstract (192:1) says 37% "did not understand why their post was removed"; the body's figure is 36.9% of the 849 open-ended answers coded "lack of clarity about why post was removed" (Table 7, 192:19).

Silence is the Reddit default. The site does not tell the author of a removal (192:4), and 41.8% (n = 379) did not notice until the survey arrived (192:15). Noticing goes with a fairer rating (β = .265). People who received an explanation (39.7%, n = 360) judged the removal fairer (β = .384, p < .001) and were somewhat more likely to say they would post again (β = .088, p < .05) (192:17). Only whether the explanation gave new information mattered for fairness (β = .200); mode (comment, message, flair) and source (human or bot) did not (192:18). Rule clarity helped on both outcomes (β = .170 and .223) (192:17).

One result runs against the abstract. Readers of the rules rated removals less fair (β = -.314), which the authors call "surprising" (192:16–17) and explain by rules that are subjective or too many to follow (192:22–23). The Discussion says "when moderated users read the rules before posting, they are less likely to consider their post removal as fair" (192:23). The abstract says the opposite: "users who read community guidelines or receive explanations for removal are more likely to perceive the removal as fair" and post again.

Fit stays low. Controls alone explain under 1% of variance; the full model reaches adjusted R² of .324 for fairness and .123 for the intention to post again, and a model with explanations alone leaves the second at .000 (192:16, 18).

## Relation to the argument

Q4 in facet J and, indirectly, ruling D3 (disclosure as a literacy-based intervention). The rule-holder here is a volunteer neighbour, not an interested owner. The paper supports the claim that reasons change how people judge a decision. It is thin on what they then do: the behavioural outcome is a stated intention, the association is small, and the authors take actual posting up elsewhere "with a larger dataset" (192:11, ref. 45). That second paper bears on D3's claim that disclosure does not affect our ability to navigate the system; this one does not settle it.

It also bears on D8. Reddit's local moderators hold the convention, and the site gives them tools but by default does not tell the poster (192:4). The text describes no appeal. With no notice, many respondents build folk theories of moderator bias (192:20–21).

Facet check: facet J quoted the abstract only. The abstract's "read community guidelines" clause is not what Table 5 shows, and its 37% rests on 849 coded answers, not 907 respondents.

## In conversation with

- `jhaver2019transparency` (ref. 45): the paper prints it as 2018, *PACM HCI* vol. 2; the bib has 2019, vol. 3, doi:10.1145/3359252. The behavioural follow-up on removal explanations.
- `eslami2016first`, `myerswest2018censored`: folk theories and users' readings of moderation (192:5–7).
- `suzor2018digital` (ref. 80) and `gillespie2019custodians` (ref. 34, printed 2018): frameworks and background (192:6).
- Not in the bib: Fiesler et al. (2018), *Reddit Rules!*; Kiesler, Kraut and Resnick (2012); Jhaver et al. (2019), the Automoderator study, *TOCHI* 26(5); Suzor, Myers West, Quodling and York (2019); Kizilcec (2016).

## Caution

Self-report within hours, on one platform, from people who answered a private message (8.2%), mostly young and male. The authors did not judge whether removals were legitimate (192:2, n. 2). Outcomes are single Likert items regressed linearly; "post again" records intention; subreddit is uncontrolled. They call the analysis "primarily exploratory" (192:12). Not evidence on algorithms or on the paper's triad.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the CSCW published PDF (34 text pages; PDF page n = article page 192:n). Searched all 8 quotations and found each; checked about 30 numbers and locators against pp. 1, 4, 9-19, 23 (10.3/13.6/33/26.9% fairness split, 36.9% vs the abstract's 37%, 41.8% n=379, 39.7% n=360, betas .265, .384, .088, .200, .170, .223, -.314, adjusted R2 .006 baseline, .324 and .123 full model, .000 with explanations, 8.2% response, 1,054 / 907 / 849, 61/81/55%, 10,000 submissions, three hours).

**Findings:** No issues found. The Read depth line honestly says Appendix A was read only in part (items 15-24); I judged that small enough to keep full_text. One nuance, not an error: the '.000' adjusted R2 is for baseline plus removal explanations, which the card words as 'explanations alone'.
