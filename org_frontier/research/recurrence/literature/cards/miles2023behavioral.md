---
citekey: miles2023behavioral
title: Behavioral dynamics of conversation, (mis)communication and coordination in noisy environments
authors: Miles, Kelly and Weisser, Adam and Kallen, Rachel W. and Varlet, Manuel and Richardson, Michael J. and Buchholz, J{\"o}rg M.
year: 2023
doi: 10.1038/s41598-023-47396-y
arxiv: null
journal: Scientific Reports
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41598-023-47396-y.pdf
sha256: c8c97b13375c2a5ac7af4ca1575dc747ac48d63936aed54d464a40d187548510
pdf_path: literature/pdfs/miles2023behavioral.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper asks how conversational partners reciprocally coordinate verbal (speech level) and nonverbal (interpersonal distance, body/head movement) behavior to hear and be heard as background noise degrades the signal-to-noise ratio. Twenty-two pairs of typical-hearing adults held two-minute free conversations while standing or seated around a table, with seven realistic binaural background-noise scenes (53–92 dB SPL) presented over acoustically transparent headphones, and motion-tracking plus close-talk microphones recorded behavior. The authors identify three phases of adaptive behavior: a transient phase (rapid initial reductions in interpersonal distance and increases in speech level proportional to noise and talker configuration), a sustaining phase (ongoing reciprocal speech and movement coordination, quantified via Cross-Recurrence Quantification Analysis, that strengthens with noise), and a resetting phase (intermittent moving closer and/or talking louder to restore communication after breakdowns). Communication breakdowns (other-initiated repairs) stayed low and stable below about 78 dB SPL but rose steeply above it, identifying ~78 dB SPL as a critical threshold where behavioral compensation became insufficient. Movement-based coordination was greater when seated (where the table constrained distance changes), whereas distance resetting was used more when standing.

## Key facts it relies on
- Sample: 44 participants in 22 pairs (friends 14 pairs, couples 6, siblings 2); all pure-tone thresholds better than 20 dB HL; average age 22.2 years for female participants (n=32) and 24.4 for male participants (n=12).
- Seven background noise scenes (ARTE database plus two party scenes) at long-term average levels: Library 53.0, Living Room 63.3, Cafe 71.7, Train Station 77.1, Food Court 79.6, No Music Party 85.0, Music Party 92.0 dB SPL; each conversation and noise lasted two minutes; standing pairs started 2.5 m apart, seated pairs sat across a round table 0.76 cm in diameter.
- Interpersonal distance change increased linearly with noise: 0.70 cm (SE 0.20; CI 0.30–1.09) per 1 dB when seated and 2.0 cm (SE 0.20; CI 1.61–2.40) when standing; significant noise×configuration interaction F(1,283)=21.08, p<0.001, η²=0.07.
- Speech level rose by a mean of 0.32 dB (SE 0.10; CI 0.26–0.38) per 1 dB increase in noise (main effect of noise F(1,277)=123.18, p<0.001, η²=0.31), with no credible effect of talker configuration (F(1,277)=0.418, p=0.59).
- CRQA metrics: %REC = movement similarity, %DET = structural organization, MAXLINE = coordination stability; embedding dimension 6, T-lag 23 samples, recurrence radius 20% of mean distance; movement similarity rose 0.016% (SE 0.006) and structural organization 0.45% (CI 0.30–0.62) per 1 dB noise increase.
- Coordination was greater when seated: movement similarity 1.65% (SE 0.15) seated vs 0.84% (SE 0.15) standing; structural organization 53.3% vs 43.0%; coordination stability (MAXLINE) increased 0.99% (CI 0.64–1.34) per 1 dB only when seated.
- Above 78 dB SPL communication breakdowns rose ~0.15 (SE 0.024; CI 0.107–0.203) per 1 dB (significant main effect F(1,151)=40.65, p<0.001, η²=0.21), i.e. one extra breakdown per ~7 dB, averaging 1.2 breakdowns/min; below 78 dB SPL breakdowns rose only ~0.02 per dB (~0.3/min).
- Following a breakdown, pairs reduced interpersonal distance (F(1,791)=8.095, p=0.005) and raised speech levels (F(1,787)=71.29, p<0.001, η²=0.08), moving on average 5 cm closer and increasing speech by 3.2 dB; receiver-related SNR still decreased by ~21.2 dB (seated) / ~16.0 dB (standing) over the 39 dB noise range.
- Speech-level fluctuations tracked the noise envelope with a delay of ~2 s; correlation between noise and speech envelopes peaked in the highly fluctuating train station environment (Fig. 3F).

## Critical notes from the literature
- Generalizability is limited by the degree to which the unnatural acoustic/technical setup and being observed by experimenters resemble realistic settings; differences in how conversation was elicited and observed may be perceived by participants (authors' own caveat).
- Communication breakdowns were captured only through overt verbal signaling of other-initiated repairs; the authors note many breakdowns are handled nonverbally (e.g., "freeze look", head/body gestures) or via "let it pass" and so are not counted, and some breakdowns may arise from turn-taking mismanagement or topic shifts rather than SNR.
- The 78 dB SPL "critical threshold" is specific to young, typical-hearing adults; the authors frame it as a candidate real-world threshold for difficult conversations, consistent with but not established beyond this population.
- Authors stress communicating in noise is not purely an SNR problem: physical barriers (table), physiological limits, and psychological/cultural conventions (power dynamics, comfort with proximity and loudness) also constrain compensatory behavior.
- The dataset and test methods are largely reported in the authors' prior paper (Weisser et al. 2019, ref. 30); transcripts and audio are not shared due to identifiable content.

## Key topics covered
Conversational coordination; interpersonal synergies / reciprocal compensation; Lombard effect; signal-to-noise ratio; interpersonal distance adaptation; speech level adaptation; Cross-Recurrence Quantification Analysis (%REC, %DET, MAXLINE); interpersonal motor/postural coordination; communication breakdowns and other-initiated repairs; noise envelope tracking and speech co-modulation; transient/sustaining/resetting behavioral phases; 78 dB SPL critical threshold; standing vs seated configuration; motion capture; ARTE / binaural noise scenes.
