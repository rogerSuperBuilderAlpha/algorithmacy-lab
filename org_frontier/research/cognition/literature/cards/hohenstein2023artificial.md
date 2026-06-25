---
citekey: hohenstein2023artificial
title: Artificial Intelligence in Communication Impacts Language and Social Relationships
authors: Hohenstein, Jess and Kizilcec, Ren{\'e} F. and DiFranzo, Dominic and Aghajari, Zhila and Mieczkowski, Hannah and Levy, Karen and Naaman, Mor and Hancock, Jeffrey and Jung, Malte F.
year: 2023
doi: 10.1038/s41598-023-30938-9
arxiv: null
journal: Scientific Reports
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41598-023-30938-9.pdf
sha256: 7853d76e8618f4fdd436d60372202ad5beb43cdca970de6908112e021c763ac3
pdf_path: literature/pdfs/hohenstein2023artificial.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how using AI-generated "smart replies" (algorithmic response suggestions) in text-based interpersonal communication affects language and social relationships. The authors built a custom messaging app (Moshi) and ran two randomized experiments with Mechanical Turk crowdworkers who discussed a policy issue with an anonymous partner. In Study 1 (219 pairs), smart-reply availability was randomly assigned per participant, and an instrumental-variable (IV) approach estimated effects of actual smart-reply use; in Study 2 (291 pairs), pairs were assigned to Google, positive, negative, or no smart replies to isolate the effect of suggestion sentiment on conversation tone. Using smart replies increased communication speed and led to more positive emotional language, and a partner's increased actual smart-reply use raised the self's ratings of the partner's cooperation and affiliation. However, the more a participant believed their partner used smart replies, the less cooperative and affiliative and the more dominant they rated that partner, even controlling for actual use. Study 2 showed that negative smart replies made conversations more negative than positive or Google smart replies, and these language shifts were driven by use of the replies rather than mere exposure. The authors conclude AI can speed communication and improve interpersonal perceptions, but the anti-social connotations of AI undermine these benefits when its use is overt.

## Key facts it relies on
- As of 2017, algorithmic responses constituted 12% of all messages sent through Gmail, representing about 6.7 billion emails written by AI on our behalf each day (cited from prior reports).
- Study 1 randomly assigned 219 pairs of participants ("self" and "partner") independently to smart-reply availability, yielding four scenarios; smart replies were generated using the Google Reply API. 438 MTurk crowdworkers were recruited; after exclusions, 424 participants were used for smart-reply-use analyses and N = 361 for survey-based analyses.
- Availability of smart replies strongly encouraged use [first-stage: t(211) = 13.8, P < 0.0001]; smart replies accounted for 14.3% of sent messages on average, and availability produced 10.2% more messages sent per minute [intent-to-treat: t(198) = 2.173, P = 0.0309].
- Perceived smart-reply use correlated with actual use but only weakly [Pearson's r = 0.22, t(97) = 3.62, P = 0.0005]; greater perceived use predicted lower cooperation ratings [t(92) = -9.89, P < 0.0001], lower affiliation [t(92) = -6.90, P < 0.0001], and higher dominance [t(92) = 2.27, P = 0.0256], controlling for actual use.
- Increased actual partner smart-reply use improved the self's ratings of partner cooperation [IV: b = 15.66, t(189) = 2.39, P = 0.018] and affiliation [IV: b = 21.79, t(189) = 2.75, P = 0.007], but not dominance [IV: b = -0.53, t(189) = -0.13, P = 0.90].
- Increased partner smart-reply use led the self to send messages with more positive sentiment [IV: b = 0.178, t(205) = 2.02, P = 0.045], persisting when smart-reply messages were excluded [b = 0.208, t(205) = 2.17, P = 0.031].
- Study 2 randomly assigned 291 pairs (582 MTurk crowdworkers) to Google, positive, negative, or no smart replies; conversation sentiment was measured with VADER (compound score from -1 to 1). Negative smart replies caused more negative emotional content than positive smart replies [t(127) = 2.75, P = 0.007, d = .352] and than Google smart replies [t(127) = 2.40, P = 0.018, d = .323].
- Language shifts were driven by use, not exposure: with smart-reply messages omitted from the corpus, sentiment differences between conditions were minimal [F(3277) = 0.360, P = 0.782].
- A LIWC Affect-score precursor analysis confirmed positive and Google smart replies raised conversation affect vs. control [t(124) = 2.95, P < 0.001, d = 0.272] while negative smart replies lowered it [t(123) = -3.50, P < 0.001, d = 0.454].
- Methods: perceived dominance/affiliation via Revised Interpersonal Adjective Scales (IAS-R, 16 selected items, 1-7 scale); cooperative communication via a 7-item scale; IV estimation used cluster-robust (CR2) standard errors; Study 1 was pre-registered on AsPredicted; data available in a Mendeley repository.

## Critical notes from the literature
- The negative interpersonal effects of perceived smart-reply use are correlational; the authors explicitly state this "does not show causally how attitudes shift in response to actual smart reply use," whereas the positive effects of actual use are causal (IV-identified).
- Scope is narrow: a single ~6-7 minute policy-discussion task between anonymous MTurk strangers; the authors note they lack insight into real-world frequency of AI use and call for longitudinal research on long-term effects, including possible homogenization / loss of personal communication style.
- Effects depend on smart-reply availability acting as an "encouragement" to use; the authors found no main effects of mere exposure when suggestions were not used, and ratings of cooperation/affiliation were not significantly affected by availability for the self.
- The studies rely on one commercial smart-reply system (Google Reply API) plus crowdworker-rated positive/negative reply sets, and sentiment is measured with lexicon-based tools (VADER, LIWC); generalization to other AI-mediation systems (e.g., Smart Compose, LLM-based generation) is asserted in the discussion but not directly tested.

## Key topics covered
AI-mediated communication; smart replies / algorithmic response suggestions; computer-mediated communication; instrumental-variable causal estimation; randomized experiments; interpersonal perception (cooperation, affiliation, dominance); IAS-R; sentiment analysis (VADER, LIWC); communication speed; perceived vs. actual AI use; transparency and trust in AI; Mechanical Turk crowdworkers; Moshi research platform.
