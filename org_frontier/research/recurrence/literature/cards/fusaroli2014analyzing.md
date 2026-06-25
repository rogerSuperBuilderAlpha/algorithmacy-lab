---
citekey: fusaroli2014analyzing
title: Analyzing Social Interactions: The Promises and Challenges of Using Cross Recurrence Quantification Analysis
authors: Fusaroli, Riccardo and Konvalinka, Ivana and Wallot, Sebastian
year: 2014
doi: 10.1007/978-3-319-09531-8_9
arxiv: null
journal: 
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:?
source_url: https://pure.au.dk/ws/files/89938143/2014_springer_maths_and_stats_analyzing_social_interactions.pdf
sha256: 719ef05f20e7d4a64f8287f64820eb3de27e635767585593b657cc6858b218e5
pdf_path: literature/pdfs/fusaroli2014analyzing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This chapter reviews the use of Cross Recurrence Quantification Analysis (CRQA) for studying social interactions, asking whether and how the method can grasp the non-linear, non-stationary, multi-timescale dynamics that interacting agents produce. The authors frame CRQA as a non-linear analogue of cross-correlation: by reconstructing the state spaces of two time-series and finding moments when both systems visit similar states, it quantifies the strength, form, and complexity of their shared dynamics, without assuming stationarity. They systematically survey applications spanning physiological coordination (heart rate in fire-walking rituals and Lego tasks), motor coordination (interpersonal precision tasks, postural sway, pendulum swinging, pedestrians, infants), gaze and head movement, turn-taking, prosody, and even symbolic and conceptual aspects of conversation. The dominant finding across studies is that interactions show higher amount and structure of recurrence than baseline controls, though some studies (notably Wallot et al. and Fusaroli et al.) find recurrence negatively related to, or a worse predictor of, effective performance, undermining the assumption that "more recurrence = better coordination." The authors then lay out seven challenges and a set of recommendations to mature the field, emphasizing theory-driven studies, consistent reporting of all indexes and effect sizes, handling of complementarity and routines, multiple timescales, and interactions with more than two agents.

## Key facts it relies on
- The literature review searched "cross recurrence" and "crqa" on PubMed, Google Scholar, and Web of Science (October 1st 2013), then manually selected social-interaction articles; the resulting list counts 41 articles (34 reporting empirical studies, the rest reviews/method papers), plus 6 submitted-but-unpublished papers.
- CRQA was introduced by Zbilut et al. [26] as an extension of Recurrence Quantification Analysis (RQA); RQA is described as a non-linear equivalent of auto-correlation and CRQA as a non-linear equivalent of cross-correlation.
- Defined recurrence indexes include: Cross Recurrence Rate (RR, raw amount of similarity); determinism (DET, recurrence points forming diagonal lines); average diagonal line length (L, time systems stay attuned); longest diagonal line (LMAX, indicator of stability of coordination); entropy (ENTR, complexity/regularity of attunement); diagonal recurrence profile (DiagProfile, the delay maximizing recurrence, indicating leading/asymmetry); laminarity (LAM, vertical-line recurrence); and trapping time (TT, average vertical line length, time trajectories stay in the same region).
- Konvalinka et al. [38] studied a fire-walking ritual in Spain, showing firewalkers' heart rhythms more closely matched those of related/friend spectators than non-related spectators (higher RR, DET, LMAX, ENTR and LAM), despite differing behavior.
- Fusaroli et al. [39] studied groups of five participants building Lego models of abstract notions ("trust", "safety") individually and collectively; heart rate coordination (RR, L, ENTR) was significant against shuffled baseline in all groups, but a surrogate-pairs contrast showed no difference in individual trials and higher coordination in collective trials, which grew over time.
- Wallot et al. [44] found that pairs building Lego cars showed significant behavioral and physiological coordinative structures (DET) that were negatively correlated with the effectiveness (functionality and aesthetic appeal) of the resulting cars.
- Richardson, Dale et al. found gaze highly coordinated (RR) between describer and listener especially at a 2 s lag, with coordination correlating with comprehension [54]; in active discussion the delay disappeared (lag 0) [55]; more shared knowledge produced higher eye-movement coordination [56].
- Reddy et al. [43] showed via a pressure mat that infants' legs and arms are significantly coordinated (higher RR) with the mother already at 2 months of age, with full-bodied coordination appearing later; prosodic (fundamental frequency) coordination appears from 3 months [66] and turn-taking coordination from at least 1 year of age [63].
- Of the reviewed empirical work, 11 of 35 report case studies and 18 of 35 use statistically relevant samples; the most basic indexes (RR, DiagProfile, LMAX) are sensitive to gender, age, dominance, familiarity, modality, and difficulty, while DET, L, ENTR, TT, and LAM are more sparsely used.
- Fusaroli et al. [61] found that RQA of the whole conversation (turn-taking, prosody, morphemes pooled) consistently provided better predictors of performance than CRQA, with each aspect contributing non-overlapping information; CRQA failed to capture complementary dynamics that RQA captured.

## Critical notes from the literature
- The paper itself stresses that CRQA indexes must be compared to appropriate baselines (shuffled data, surrogate/mismatched pairs, or within-pair contrasts); surrogate pairs are problematic for turn-taking with variable-length production and for sparse nominal data (e.g. coded nodding), where shuffled data are shown to be more conservative [36].
- The authors explicitly question the common assumption that higher amount/structure of recurrence equals more successful coordination: complementarity, differential roles, and routines can mean effective coordination involves decreased diagonal recurrence (illustrated by table-moving and tablet-marble complementarity examples and by Wallot et al. [44] and Fusaroli et al. [61]).
- They note CRQA is a powerful but complex tool with a steep learning curve and articulated, hard-to-interpret output; for predominantly linear time-series simple correlation may suffice, and for certain periodic signals phase analysis may be sufficient — CRQA "gives its best on more complex and noisy data."
- The authors flag weak reporting practice: effect sizes and statistical power are missing from the large majority of reviewed studies, and several indexes are used too inconsistently to establish their meaning.
- Open challenges acknowledged: CRQA's ability to address complementarity in tightly coupled continuous motor interaction remains an open question; multi-scale recurrence methods are only recently developed; and extending analysis beyond dyads (most studies split groups into dyads; one uses aggregative measures [2]) requires joint recurrence, network theory, or probabilistic graphical models.

## Key topics covered
Cross Recurrence Quantification Analysis (CRQA); RQA; recurrence plots; recurrence indexes (RR, DET, L, LMAX, ENTR, LAM, TT, DiagProfile); interpersonal coordination; physiological synchronization (heart rate); motor coordination; postural sway; gaze and joint attention; turn-taking; prosody; linguistic and conceptual coordination; nominal/categorical recurrence; shuffled and surrogate-pair baselines; complementarity vs. alignment; leader-follower dynamics; multiple timescales; multi-agent (more-than-two) interaction; theory-driven vs. exploratory research; reproducibility, effect size and statistical power; non-stationarity and non-linear dynamics.
