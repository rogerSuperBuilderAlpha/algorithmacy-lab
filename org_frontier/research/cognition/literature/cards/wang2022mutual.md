---
citekey: wang2022mutual
title: Mutual Theory of Mind for Human-AI Communication
authors: Wang, Qiaosi and Goel, Ashok K.
year: 2022
doi: null
arxiv: 2210.03842
journal: arXiv
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2210.03842
sha256: c9776eec758bcbb1d53270929cdfa400f62aab348325ec2d2a762f7786137ddf
pdf_path: literature/pdfs/wang2022mutual.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how the HCI community can systematically study an emerging human-AI interaction (HAI) paradigm in which both humans and AI systems continually build interpretations of each other's minds. Drawing on the human cognitive ability of Theory of Mind (ToM)—the ability to make conjectures about one's own and others' mental states—the authors propose a Mutual Theory of Mind (MToM) framework as a conceptual (process and content) account of human-AI communication. The framework specifies three elements (interpretation, feedback, and mutuality) that iteratively shape communication across three stages: AI's construction of its ToM, user's recognition of AI's ToM, and AI's revision of its ToM. The authors emphasize the recursive, second-level ToM idea ("I can think about what you think about my mind") and demonstrate the framework's utility with two prior empirical studies set in online-learning contexts. Study 1 shows that linguistic cues in student questions can be used to predict student perceptions of an AI teaching assistant (the construction stage); Study 2 shows how users react to and perceive AI misrepresentations of their personality (the recognition stage), finding that users' AI knowledge (AI literacy) moderates trust changes. The paper closes by mapping research opportunities across the three stages. (Note: the PDF is the May 2024 version presented at the ToMinHAI at CHI 2024 workshop.)

## Key facts it relies on
- MToM framework defines three core elements—interpretation, feedback, and mutuality—operating across three stages: AI's construction of its ToM, user's recognition of AI's ToM, and AI's revision of its ToM.
- ToM is defined as the ability to make conjectures about ourselves and others' mental states (e.g., emotions, intentions); interpretations can be recursive (second-level ToM: "my interpretation of your interpretation of my mind"), which is the focus of the empirical work.
- The framework synthesizes three communication perspectives: the Shannon-Weaver communication-studies model (encoding/decoding of messages), the cognitive-science perspective (ToM/behavioral cues), and Goffman's social-science perspective of impression management (expression given vs. expression given off).
- Study 1 (construction stage): an AI agent acting as a virtual teaching assistant answered students' logistics questions in an online class discussion forum for 10 weeks with about 376 students enrolled; bi-weekly perceptions (anthropomorphism, intelligence, likeability) and student questions were collected.
- Study 1 result: using linear regression models with linguistic features (readability, sentiment, linguistic diversity, adaptability) as predictors, verbosity negatively associated with student perceptions, while readability, sentiment, diversity, and adaptability positively associated with anthropomorphism, intelligence, and likeability (details in the authors' CHI 2021 paper).
- Study 2 (recognition stage): semi-structured interviews with 20 college students plus a survey experiment with 198 students on Prolific, using a Wizard-of-Oz approach to fabricate intentionally accurate/inaccurate AI-generated personality inferences from participants' personality ground truth.
- Study 2 result: participants who saw AI (mis)representations adopted rationales that "AI works like a machine, human, and/or magic"; linear regression/moderation analysis showed people's existing AI knowledge (AI literacy) significantly moderates changes in their trust of the AI after encountering AI misrepresentations.
- A proposed mitigation: if a user adopts the "magic" rationale, the AI could provide explanations to nudge them toward the "machine" rationale to reduce overreliance.

## Critical notes from the literature
- This is a position/framework paper (a CHI 2024 workshop submission), not a single new experiment; the two empirical studies are summaries of the authors' prior work used to illustrate the framework rather than new validations of MToM as a whole.
- The authors note their empirical work so far has examined only the first two of the three MToM stages (construction and recognition)—the revision stage is presented only as future research opportunities, so the full iterative loop is not empirically demonstrated.
- The paper acknowledges an underlying open problem of operationalization: how to operationalize ToM given the huge variation of human minds across contexts and individuals.
- The authors situate their work against prior findings that people tend to over-trust and view AI as an authority, and warn that these reactions can persist or even be exacerbated when AI misrepresents users—motivating customized repair strategies.
- Scope is largely online-learning contexts with student populations (e.g., a virtual TA, AI social facilitators); generalization to other domains is asserted conceptually rather than tested.

## Key topics covered
Mutual Theory of Mind (MToM); Theory of Mind (ToM); second-level/recursive ToM; human-AI interaction (HAI) vs. human-computer interaction (HCI); interpretation–feedback–mutuality; construction/recognition/revision stages; Shannon-Weaver communication model; Goffman impression management; conversational agents (CAs) and the expectation-experience "gulf"; linguistic cues (readability, sentiment, diversity, adaptability, verbosity); user perceptions (anthropomorphism, intelligence, likeability); AI misrepresentations; AI literacy and trust; Wizard-of-Oz method; machine/human/magic rationales; overreliance and repair strategies.
