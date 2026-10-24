# Fok, R., & Weld, D. S. (2024). In search of verifiability: Explanations rarely enable complementary performance in AI-advised decision making. *AI Magazine, 45*(3), 317–332.

**Identifier:** doi:10.1002/aaai.12182 · arXiv:2305.07722 · **Read depth:** full_text (arXiv v4 of 1 Feb 2024, 12 pages, read in full; the Wiley version of record, pp. 317–332, was not opened, so the locators below are section, table and figure numbers, not journal pages) · **Source-tier:** peer-reviewed article (perspective / synthesis) · **Evidence basis:** direct_read · **Design and sample:** none; a position paper that tabulates 29 study conditions from the XAI decision-making literature (Table 1) and argues from them · **Parties modeled:** person–system; §6.4 compares one-human-one-AI teams with human groups · **Facets:** R1 · **Read:** 2026-10-14

## What it argues
Fok and Weld offer a single account of the mixed XAI results: "explanations can enable complementary performance in AI-advised decision making to the extent they allow a decision maker to verify an AI's recommendation" (§4). Their Figure 1 caption puts it as a claim: "We claim AI explanations cannot foster appropriate reliance and engender complementary performance in decision making, except in the rare instances in which they efficiently verify the AI's recommendation."

Evidence and steps:
- Table 1 lists 29 study conditions. In 24 the explanation does not enable verification; none of these shows complementary performance (21 ✗, and 3 marked ★ where the gain also appeared with confidence scores alone). In the 5 that enable verification (Quizbowl, Wikipedia QA, maze, two interactive-rationale MCQA studies), all show complementary performance.
- The maze is the model case: given a highlighted path a person can check the answer cheaply, like checking a certificate for an NP-complete problem (§4.1, Figure 4). But "our maze example is unusual — explanations in the tasks most commonly considered in XAI studies (e.g., recidivism prediction, medical applications, sentiment analysis, or deceptive review detection) do not enable verification" (§4.1).
- Verification comes in degrees: "by sufficiently lowering the cost of verification, explanations can provide enough utility to improve team performance" (§4.2).
- Where the AI is better than the person, explanations raise team accuracy by raising trust, "since they tend to make the audience trust the recommendation" (§6.3); "the mere presence of explanations can increase a decision maker's trust in the AI's recommendations" (§2).
- §5 separates outcome-graded reliance (accept when the AI turns out right) from strategy-graded reliance (accept when the AI is expected to do better) and argues for the second.
- §6.4 links verifiability to Laughlin's "demonstrability": recidivism and loan decisions are "judgmental tasks, where no demonstrable (i.e., verifiable) solution may exist."

## Relation to the argument
The paper supports P8 in the form the argument map now gives it, and it gives the author a sharper mechanism than "information overload." Explanations fail because most tasks offer nothing to check, not because the person reads badly. That is close to the author's distinction: a rationale gives the person something to read, and reading it does not decide anything.

It also complicates the "category error" framing. On Fok and Weld's account the dividing line is verifiability, not text against non-text. Several of their successes are texts: a retrieved Wikipedia passage, an interactive natural-language rationale. A text that lets the person check the answer works. So the ruling D3 ("disclosure is a literacy based intervention") should not be read as "anything to read fails"; the stronger claim is that a rule or rationale about the mediator does not verify the outcome a person needs to decide on.

For the triad (P11), §6.4's point that coordination decisions are often "judgmental" cuts both ways. It explains why disclosure of a platform's rules cannot be verified against an outcome. It also means a convention that makes outcomes checkable has no guarantee of existing.

**Use in DRAFT_v2:** Not cited in DRAFT_v2. The draft cites Bansal et al. (2021), whose second author is Fok, but not this paper. It bears on:
- Line 33 ("explanations reduce overreliance only under particular conditions, such as a hard task with an explanation that is cheap to check (Vasconcelos et al., 2023)"): **supports** and generalises it; Fok and Weld state the condition as verifiability and tabulate it (Table 1; §4.2).
- Line 168 ("explanations yielded no reliable improvement"): **supports**, with the qualification that verifiable explanations do produce complementary performance (Table 1, 5 of 5).
- Line 19 ("Where explanations or alerts do help ... they operate inside dyadic human–machine loops"): **narrows**. Fok and Weld locate the successes in verifiability, not in dyadic structure; every study in their table is dyadic, failures included, so dyad alone cannot be what separates success from failure.
- Line 31 (the "implicit cognitive model" that rendering internals yields calibrated trust): **supports**; the authors argue "explanation faithfulness is largely irrelevant" to decision performance (§3; also §6.1).

## In conversation with
- `vasconcelos2023explanations` (ref. 69): the maze study; the paradigm case of a verifying explanation (§4.1).
- `bucinca2021trust` (ref. 13): cognitive forcing, read as a way to raise engagement at a cost in load (§6.2).
- `poursabzi2021manipulating` (ref. 59): listed among studies where explanations did not enable verification (Table 1).
- `alufaisan2021explainable` (ref. 4) and `zhang2020effect` (ref. 76): both listed in Table 1 as feature-importance conditions with no verification and no complementary performance.
- Bansal et al. 2021 (ref. 7): sentiment and logical-reasoning conditions in Table 1; not in the bib.
- Leads not in the bib: Laughlin and Ellis 1986, demonstrability in group problem solving; Chen, Feng, Sharma and Tan 2023 (FAccT), machine explanations and human intuitions; Feng and Boyd-Graber 2019, Quizbowl; González et al. 2021, open-domain QA.

## Caution
A perspective piece; Table 1 is the authors' coding of other studies, with no stated coding protocol and no effect sizes. The ★ judgements are theirs. Version read is the arXiv preprint; the AI Magazine text may differ in wording and has its own pagination. It says nothing about LLM outputs in open-ended tasks, or about decisions with a counterpart party.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the arXiv v4 PDF (2305.07722v4, 1 Feb 2024, 12 pp.) and extracted it myself. I matched all seven quotations word for word and checked their section locators against the section headings (the "We claim" sentence is indeed the Figure 1 caption, §4, §4.1, §4.2, §2, §3, §6.3, §6.4). I recounted Table 1: 29 rows; 24 marked ✗ for verification, of which 21 ✗ and 3 ★ for complementary performance; 5 ✓/✓ (Quizbowl, Wikipedia ODQA, maze, two interactive-rationale MCQA). I checked refs 4, 7, 13, 59, 69, 76 and the Laughlin demonstrability passage, and the AI Magazine record (45(3), 317–332, DOI 10.1002/aaai.12182) against Crossref. I grepped every surname in DRAFT_v2.md lines 1–502 and confirmed the card's statement that the source is not cited there; I re-read each DRAFT_v2 line the card names (19, 31, 33, 35, 39, 43, 160, 168, 172, 174 as applicable) and judged the verdict against it.

**Findings:**
1. No errors found. The verdicts on lines 19, 31, 33 and 168 hold; the line-19 "narrows" verdict is fair because every Table 1 study, success or failure, is dyadic.
