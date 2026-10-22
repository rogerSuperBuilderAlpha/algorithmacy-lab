# Debate map: the 17 pasted citations, checked

Checked 2026-10-20 against Crossref, OpenAlex, Semantic Scholar and Consensus. Records and abstracts: `records.md`. Searches: `../search-log.md` rows 44–48.

**Reading status (updated 2026-10-20, second pass).** Roger downloaded 17 PDFs. I read Gegoff, Tatasciore, Disley & Khan, Forshaw, Yang and Lamb in full or in their substantive sections. For the other six debate papers, I read the method, results and discussion. Notes are in `NOTES_FULLTEXT.md`. Still abstract only: Najjar & Nasir, Khan et al., Kula & Avcı. Gill has no abstract and is unread. Zhang et al. has no abstract and is unread. The verdicts in Section 2 below were first made from abstracts. Reading the full texts confirmed every one, with the additions marked "Full text:".

## 1. Citation errors in the pasted list

| # | As pasted | Correct record | Error |
|---|---|---|---|
| 1 | Tatasciore et al. (2026), DOI …251312345 | Human Factors 68(1), 5–27. https://doi.org/10.1177/00187208251349269 | DOI wrong |
| 2 | Gegoff et al. (2025), DOI …251318921 | Human Factors 67(8), 776–794. https://doi.org/10.1177/00187208251318465 | DOI wrong; it is now in an issue |
| 3 | Khan et al. (2026), DOI …2026.2312456 | TIES 27(5), 419–436. https://doi.org/10.1080/1463922X.2026.2622027 | DOI wrong |
| 4 | Kula & Avcı (2026), DOI …2026.2325812 | TIES 27(5), 487–503. https://doi.org/10.1080/1463922X.2026.2644279 | DOI wrong |
| 5 | Gill, A. (2026), DOI …2026.2319087 | Gill, Astha. TIES 27(5), 437–454. https://doi.org/10.1080/1463922X.2026.2623130 | DOI wrong |
| 6 | No authors; "…Support Dynamic AI Teaming?", DOI …261465892 | Lamb, S. C., Byrne, M., Norman, T. J., Ramchurn, S. D., & Naiseh, M. (2026). What's informing trust and adoption? Can current cognitive models support expert adoption of AI? JCEDM 20(2), 158–175. https://doi.org/10.1177/15553434261430550 | Authors missing; title and DOI wrong |
| 7 | No authors; "…Prior Beliefs in Automated Decision Aids", 20(1), 1–39 | Haghighi, B. T., & Wong, B. L. W. (2026). Susceptibility to misinformation: Exploring persuasion and prior orientation in recognition-primed decision pathways. JCEDM, online first. https://doi.org/10.1177/15553434261472960 | Authors missing; title, volume and pages wrong (DOI right) |
| 8 | Disley, M., et al. 41(6), 445–472 | Disley, M., & Khan, M. (2026). HCI, online first, 1–42. https://doi.org/10.1080/07370024.2026.2708617 | Volume, pages, DOI invented |
| 9 | Najjar, M. S., et al. 41(6), 473–501 | Najjar, M. S., & Nasir, M. (2026). HCI, online first, 1–31. https://doi.org/10.1080/07370024.2026.2717534 | Volume, pages, DOI invented |
| 10 | Forshaw, T., et al. 41(6), 345–370 | Forshaw, T., Hale, J., & Longmire, M. (2026). HCI, online first, 1–26. https://doi.org/10.1080/07370024.2026.2744236 | Volume, pages, DOI invented |
| 11 | Dunham, J., Wang, Y., Chamberlain, A., & Papangelis, K. (2025) | Xu, J., Luna, S. M., Tigwell, G. W., Lalone, N., Saker, M., Laato, S., Dunham, J., Wang, Y., Chamberlain, A., & Papangelis, K. (2025). TOCHI 32(6), 1–24. https://doi.org/10.1145/3749841 | First six authors dropped |
| 12 | No authors; "…Building: Scaffolding Autonomy in Cognitive Work", DOI 10.1145/3771924 | Kot et al. (2026). Exploring the role of generative AI in dementia resilience building activities: Uncovering opportunities and challenges. TOCHI 33(1), 1–45. https://doi.org/10.1145/3773029 | Authors missing; subtitle invented; the DOI points to another paper |
| 13 | Cetinkaya & Krämer (2026) | BIT 45(5), 840–854. https://doi.org/10.1080/0144929X.2025.2533358 | Correct |
| 14 | Horvers, A., et al., 45(2), DOI …2026.2410214 | BIT, online first. https://doi.org/10.1080/0144929X.2026.2740744 | Volume and DOI invented |
| 15 | Tafesse & Mamo, DOI …2025.2361092 | BIT 45(2), 314–331. https://doi.org/10.1080/0144929X.2025.2517215 | DOI wrong |
| 16 | Yang et al., Article 103901 | IJHCS 217, Article 103920. https://doi.org/10.1016/j.ijhcs.2026.103920 | Article number and DOI wrong |
| 17 | No authors; "Meditation Needs Prompts Too? More Control May Not Mean More Calm…" | The DOI given (…103928) resolves to Zhang, K., Xu, J.-P., Wang, Y.-M., Zhang, K.-W., & Yim, J.-H. From control to authorship: Exploring how user agency relates to generative presence and therapeutic self-attribution in AI-driven VR mindfulness. IJHCS 218. | Pasted title not found anywhere; probable match, unconfirmed |

Thirteen of seventeen DOIs were wrong or pointed to other papers. The three "41(6)" HCI entries have invented volume and page numbers. The tool that produced this list should not be trusted for citations.

## 2. Does each paper say what the pasted "connection" claims?

| # | Pasted claim (short) | What the abstract reports | Verdict |
|---|---|---|---|
| 1 Tatasciore | user control over information layers prevents overload | Letting operators choose the transparency level did not improve automation use; high transparency chosen on 41% of missions, more often when the mission felt hard | **Use**, but the finding is a null. It argues for system-placed decision spaces, not user-summoned ones |
| 2 Gegoff | recommendations vs raw information alter vigilance | Recommendations made decisions more accurate and faster but reduced discrimination of system-information accuracy; people scrutinized information more without recommendations | **Use.** Closest debate paper to your Consequence paragraph. Full text: the discrimination drop is small (.93 vs .94, ηp² = .05). |
| 3 Khan | opaque pacing depletes working memory | Survey of ride-hailing drivers; algorithmic dehumanisation → ego depletion → lower safety compliance. No pacing, no working-memory measure | Claim overstated. Skip |
| 4 Kula & Avcı | conversational breakdowns, cognitive friction | Usability study of Copilot, 20 students | Weak. Skip |
| 5 Gill | revises HF models for software agents | Adds self-consciousness to the SHELL model; conceptual | Weak. Precedent only for a theory paper |
| 6 Lamb | classical trust models vs real-time generative systems | Longitudinal naturalistic study of defence analysts adopting a machine-vision overlay; supports interdependence over task allocation. Not generative, not real-time | Claim overstated. Possible in Section 7 (algorithmacy as interdependence). Full text: analysts watch live video with an AI overlay and say they need to learn the tool's "boundary conditions"; this is a candidate for Section 7. |
| 7 Haghighi & Wong | fluent automated text bypasses verification | Six participants judged misinformation narratives; no automated aid, no fluency manipulation | Claim wrong. Skip |
| 8 Disley & Khan | injecting friction to force reflection | Weight-level concept suppression in Llama3.2:3b; N = 37 within-subjects; workload–ownership trade-off | **Use** for the cost side (RQ3). Full text: §2.3 cites Cox et al.'s (2016) "microboundaries", an interface-level friction close to decision spaces. |
| 9 Najjar & Nasir | temporal dynamics of turns dictate intervention frequency | N = 244, four interaction structures; iterative critique gave higher task-appropriate creativity than AI-led proposal. No timing or intervention measure | Claim overstated. **Use** only for "structure changes outcomes" |
| 10 Forshaw | perceptual thresholds for reflection vs dismissal | Eight managers welcomed probing questions from a human coach and resisted the same questions from an AI coach ("Reflection Penalty") | Claim wrong (nothing perceptual). **Use** as a risk to decision spaces. Full text: the coached behaviours appeared after both formats despite the stated dislike. |
| 11 Xu (listed as Dunham) | overlays redirect attention; oculomotor parallels | Shared-AR game, 22 participants, observation and interviews; no eye tracking | Claim wrong. Skip |
| 12 Kot | unsegmented generation induces passive reliance | Qualitative study of generative AI in dementia resilience activities | Claim wrong. Skip |
| 13 Cetinkaya & Krämer | layout and transparency indicators shape attention | Conjoint analysis; two user clusters with opposing preferences (explainability/certification vs fairness/reliability). No layout or attention measure | Claim overstated. Skip |
| 14 Horvers | pacing must match working-memory limits | Four educational cases; automation-augmentation paradox; complementation arises when teachers "interpret, validate and enact AI-generated output." No pacing or load data | Claim wrong. Skip. Full text: teachers interpreted AI output more critically in planning and reflection than during lesson execution (§3.2.3). |
| 15 Tafesse & Mamo | chatbots narrow visual search space | MTurk N = 191 perception survey; no visual-search data | Claim wrong. Skip |
| 16 Yang | dynamic cues guide saccadic targeting | N = 30 CAVE study; AR shortened fixation durations; authors note this "may also indicate overreliance"; earlier crossing with AR | **Use**, for the point that less looking can mean more trust, not better perception. No saccade-targeting result in the abstract |
| 17 Zhang (probable) | waiting delays alter workload and agency | No abstract found | Cannot assess. Skip |

## 3. Where the paper sits in the debate (five papers worth citing)

- **Recommendations lower scrutiny.** Gegoff et al. (2025) separate the recommendation from the information. A streamed answer is a recommendation delivered while it forms, so your Consequence paragraph gains a Human Factors anchor that is not about LLMs.
- **Choice of transparency did not help.** Tatasciore et al. (2026) gave operators control over transparency and found no gain. Decision spaces put the boundary in the display, so the user does not have to ask for it.
- **Friction costs something.** Disley and Khan (2026) and Forshaw et al. (2026) show the price: lower ease, or resistance when an AI asks the user to do the work. RQ3 tests that price.
- **Structure changes outcomes.** Najjar and Nasir (2026) show that interaction structure changes what people produce.
- **Gaze is ambiguous.** Yang et al. (2026) read shorter fixations as possible overreliance. Your design already pairs gaze with error detection; this paper gives the reason in a 2026 IJHCS study.

I found no paper in these 17 that studies the visual presentation of streamed LLM text. The gap stated in round 1 stands for this set.
