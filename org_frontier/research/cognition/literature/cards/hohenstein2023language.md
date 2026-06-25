---
citekey: hohenstein2023language
title: Artificial intelligence in communication impacts language and social relationships
authors: Hohenstein, Jess and Kizilcec, Ren\'e F. and DiFranzo, Dominic and Aghajari, Zhila and Mieczkowski, Hannah and Levy, Karen and Naaman, Mor and Hancock, Jeffrey and Jung, Malte F.
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
pdf_path: literature/pdfs/hohenstein2023language.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks what social consequences follow from using AI-generated reply suggestions ("smart replies") in interpersonal text communication. The authors built a custom web messaging tool (Moshi) and ran two randomized experiments in which pairs of Mechanical Turk crowdworkers discussed a policy issue while smart-reply availability was experimentally manipulated. Using an instrumental-variable design (smart-reply availability as the instrument for actual use), Study 1 found that smart replies were used readily, sped up communication (10.2% more messages per minute), made the self's messages more positive in sentiment, and—through actual partner use—improved the self's ratings of the partner's cooperation and affiliation. However, the more a participant believed (perceived) their partner used smart replies, the less cooperative, less affiliative, and more dominant they rated that partner, even controlling for actual use. Study 2 manipulated smart-reply sentiment (Google, positive, negative, or none) and showed that negative smart replies produced more negative conversation sentiment than positive or Google replies, demonstrating that AI-suggested sentiment shifts the emotional content of human conversation. The central tension: AI can speed communication and improve interpersonal perceptions, but the prevailing anti-social connotations of AI undermine these benefits when AI use is suspected or overt.

## Key facts it relies on
- Study 1 randomly assigned 219 pairs of participants ("self" and "partner") independently to have Google Reply API smart replies available or not, yielding four conditions; 438 MTurk crowdworkers recruited, 424 retained for use analyses, N=361 (124 women, 235 men, 1 other; age 18-68, M=34.07, SD=10.1) for survey analyses.
- Availability strongly encouraged use (first-stage t(211)=13.8, P<0.0001); smart replies accounted for 14.3% of sent messages on average; availability raised communication speed by 10.2% more messages per minute (intent-to-treat t(198)=2.173, P=0.0309).
- Perceived partner smart-reply use correlated only weakly with actual use (Pearson's r=0.22, t(97)=3.62, P=0.0005); higher perceived use predicted lower rated cooperation (t(92)=-9.89, P<0.0001), lower affiliation (t(92)=-6.90, P<0.0001), and higher dominance (t(92)=2.27, P=0.0256), controlling for actual use.
- IV estimates: increased actual partner smart-reply use improved the self's ratings of partner cooperation (b=15.66, t(189)=2.39, P=0.018) and affiliation (b=21.79, t(189)=2.75, P=0.007) but not dominance (b=-0.53, P=0.90), and led the self to send more positive-sentiment messages (b=0.178, t(205)=2.02, P=0.045; b=0.208 with smart-reply messages excluded).
- Study 2 used a between-subjects design with 291 pairs (582 crowdworkers) in four conditions (Google, positive-sentiment, negative-sentiment, or no smart replies); conversations lasted 6.33 min on average (SD=2.67) and used about 20 messages.
- Sentiment measured with VADER (compound score -1 to +1); negative smart replies caused more negative conversation sentiment than positive smart replies (t(127)=2.75, P=0.007, d=.352) and than Google smart replies (t(127)=2.40, P=0.018, d=.323), highlighting the positive-sentiment bias of commercial smart replies.
- Omitting smart-reply messages from the corpus removed the between-condition sentiment differences (F(3,277)=0.360, P=0.782), indicating shifts are driven by use of smart replies rather than mere exposure.
- LIWC Affect (0-100, sum of Positive and Negative Emotion) confirmed smart replies introduced affective language: positive/Google replies raised affect vs. control (t(124)=2.95, P<0.001, d=0.272); negative replies lowered it (t(123)=-3.50, P<0.001, d=0.454).
- Background statistic cited: as of 2017 algorithmic responses constituted 12% of all Gmail messages (~6.7 billion AI-written emails per day).

## Critical notes from the literature
- The negative interpersonal effects of perceived smart-reply use are correlational only; the authors explicitly state this finding "does not show causally how attitudes shift in response to actual smart reply use," whereas the positive effects of actual use are causal (IV-based).
- The IV identification rests on the exclusion restriction holding because participants are blind to their partner's smart-reply availability and to whether any message is a smart reply; validity depends on that design assumption rather than direct testing.
- Scope is limited: short single-session conversations among MTurk crowdworkers on assigned policy/work-rejection topics, using one specific commercial system (Google Reply API). The authors call for longitudinal research and raise the open concern of language homogenization over time.
- Effect sizes for the language/sentiment manipulations are small-to-moderate (Cohen's d roughly 0.27-0.45), and Google smart replies did not significantly increase sentiment relative to no smart replies (t(137)=0.55, P=0.58).
- Self-reported perceived use was elicited only after a post-hoc definition of smart replies was provided, and raw conversation data were kept confidential (not shared) for privacy reasons, limiting external replication of the text-level analyses.

## Key topics covered
AI-mediated communication; smart replies / algorithmic response suggestions; Google Reply API; randomized experiments; instrumental variable estimation; first-stage/intent-to-treat/IV effects; cluster-robust standard errors; VADER sentiment analysis; LIWC affect dictionary; Revised Interpersonal Adjective Scales (IAS-R, affiliation and dominance); cooperative communication scale; perceived vs. actual AI use; communication speed; emotional/sentiment contagion in language; interpersonal perception and trust; Mechanical Turk crowdworkers; Moshi messaging research platform.
