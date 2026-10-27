# Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Wortman Vaughan, J. (2024). "I'm not sure, but...": Examining the impact of large language models' uncertainty expression on user reliance and trust. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)* (pp. 822–835). ACM.

**Identifier:** doi:10.1145/3630106.3658941 · arXiv:2405.00623 · **Read depth:** full_text (arXiv v2 of 15 May 2024, 25 pages in the FAccT layout without proceedings page numbers; main text §§1–7 read in full; appendices A–E skimmed only for the question list; locators are section and table numbers) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** pre-registered between-subjects experiment (OSF mnrp9), US MTurk workers, 656 complete responses of which 252 excluded, N = 404 (Control 104, first-person uncertainty 92, general-perspective uncertainty 94, No-AI 114); eight yes/no medical questions answered with or without responses adapted from Copilot in Bing (July 2023), correct on half · **Parties modeled:** person–system · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
The study inserts a hedge at the start of an LLM-search answer and nothing else. First-person: "I'm not {certain, sure}, but {it seems to me...}"; general: "{It's unclear...}, but it seems like" (§3.4). The information content is otherwise identical.

Results (Table 1; §§4–5):
- With AI access, participants agreed with the AI's answer 80.9% of the time (No-AI baseline 58.4%). First-person hedging cut agreement to 74.8% (significant); general hedging to 77.6% (not significant).
- Accuracy: Control 63.9%, first-person 72.8% (significant against Control), general 67.9% (not significant), No-AI 74.2%.
- Split by the AI's correctness (§5.1, exploratory): access to the AI raised accuracy when the AI was right (88.5% vs 77.9% No-AI) and cut it sharply when wrong (33.0% vs 64.7%). On individual answers, hedging raised accuracy on wrong answers from 43.6% to 52.0% (first-person) and from 32.8% to 48.0% (general), at a smaller cost on right answers.
- Abstract: "first-person expressions (e.g., "I'm not sure, but...") decrease participants' confidence in the system and tendency to agree with the system's answers, while increasing participants' accuracy."

The authors do not claim a fix: "the participants with the highest task performance were those without access to AI responses" (§6). They caution regulators against "blanket requirements on uncertainty expression" (§7).

## Relation to the argument
This is a contrary case to P8 of a specific kind. A four-word disclosure about the system's state, attached to the answer at the point of use, changed what people did and made them more accurate. It is not a rule book or a rationale. It reads like the draft's Target 3: a short signal that tells the person how far to rely, with nothing to study. The result therefore supports the draft's line 160 and cuts against reading D3 as "any disclosure fails."

It also supports the larger worry. A fluent LLM answer cut accuracy on wrong answers by about half against no AI (33.0% vs 64.7%), and the hedge recovered only part of that. People clicked the sources rarely (behavioural link clicks 2.7%–7.2% in the model estimates; raw 30.6%–34.9%) even when they said they used them (§4.3).

**Use in DRAFT_v2:** Not cited in DRAFT_v2. It bears on:
- Line 160 ("a one-line statement of a property changes what people do ... as a signal that a calculation is unnecessary"): **supports** that a one-line signal changes behaviour (§4.1, §4.5), and **narrows** the mechanism: here the signal told people a check was *necessary*, the opposite of the draft's example.
- Line 168 ("The failure of disclosure is documented across empirical human–AI interaction"): **complicates**. A minimal disclosure of uncertainty raised accuracy by 8.9 points (Table 1).
- Line 35 (LLM outputs leave the user to check after the fact): **supports**. Access to fluent answers lowered accuracy and the hedge did not restore it to the No-AI level (§5.1, §6).
- Line 33 ("explanations can raise acceptance ... whether or not it is correct"): **supports** for unhedged LLM answers (§5.1).

## In conversation with
- `zhang2020effect` (ref. 118): communicating confidence supports trust calibration (§1).
- `vasconcelos2023explanations` (ref. 102): cited for overreliance (§1) and for task performance as an outcome (§2.3). A second Vasconcelos et al. paper (ref. 101, uncertainty highlighting in code completion) is a lead not in the bib.
- Bansal et al. 2021 (ref. 7) and Chen et al. 2023 (ref. 25): cited for confidence displays and for the split-by-correctness analysis; not in the bib.
- `steyvers2025large` carries the same point with verbal confidence aligned to model confidence.
- Leads not in the bib: Mielke et al. 2022 (ref. 73), linguistic calibration of dialogue agents; Zhou, Hwang, Ren and Sap 2024 (ref. 119), LLMs' reluctance to express uncertainty; Spatharioti et al. 2023 (ref. 92, arXiv; a later version appeared at CHI 2025), LLM search and overreliance; Oba and Berger 2022 (ref. 78, SSRN), hedges and persuasion.

## Caution
Eight questions, a 50%-accurate AI, and uncertainty expressed at random rather than calibrated; the authors say these choices "may have impacted our results" (§6). One-session, US, English, MTurk Masters workers with 38.4% exclusions. The over/under-reliance split in §5.1 is exploratory. The FAccT pagination is from Crossref; the copy read is the arXiv version.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the arXiv v2 PDF (2405.00623, 25 pp.) and extracted it myself. I checked the sample (656 complete, 252 = 38.4% excluded, N = 404 split 104/92/94/114; OSF mnrp9; MTurk Masters; Copilot in Bing, July 2023; eight questions, four answered correctly), every percentage in Table 1 and §5.1 (80.9/58.4/74.8/77.6 agreement; 63.9/72.8/67.9/74.2 accuracy; 88.5 vs 77.9 and 33.0 vs 64.7; 43.6→52.0 and 32.8→48.0, with the smaller cost on correct answers, 92.2→89.2 and 94.8→83.1), the link-click figures (2.7–7.2% model estimates, 30.6–34.9% raw), and all quotations with their sections (§6 Discussion; "blanket requirements" is in §7, Ethical Considerations and Positionality). I checked refs 7, 25, 73, 78, 92, 101, 102, 118, 119 and confirmed via Crossref that Spatharioti et al. appeared at CHI 2025 (doi:10.1145/3706598.3714082). Crossref confirms FAccT '24 pp. 822–835. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. No errors found. The line-160 verdict ("supports" the behavioural effect, "narrows" the mechanism because the hedge signals that a check is necessary) is right.
