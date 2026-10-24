# Langer, M., Baum, K., & Schlicker, N. (2025). Effective human oversight of AI-based systems: A signal detection perspective on the detection of inaccurate and unfair outputs. *Minds and Machines, 35*, Article 1. https://doi.org/10.1007/s11023-024-09701-0

**Identifier:** doi:10.1007/s11023-024-09701-0 · **Read depth:** full_text (publisher PDF, open access; accepted 10 Oct 2024, online 5 Nov 2024, issue year 2025; pagination is the journal's "Page N of 30" counter, 30 pp. Body, pp. 1–23, read in full; references, pp. 24–30, scanned for the citations named below) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** none (a conceptual article; the authors say "The current paper reflects conceptual work," p. 22) · **Parties modeled:** person–system (an overseer and an AI system's outputs); affected people appear only as the subject of unfairness · **Facets:** G · **Read:** 2026-10-13

## What it argues
Langer, Baum and Schlicker argue that a person can oversee an AI system only as well as the person can detect its errors, and that the detection of errors is best studied with signal detection theory (SDT). They define the claim: "effective human oversight equals effective error detection in combination with an effective intervention in response to this detection" (§2, p. 4). Errors cover inaccurate and unfair outputs (p. 2). Oversight at "runtime or inspection time" is their focus, either during operation or after the fact (p. 2).

SDT separates two things that a hit rate runs together (§3.1, pp. 6–10). Sensitivity (d′) is how well an overseer tells erroneous outputs from normal ones. Response bias (c) is how much evidence the overseer needs before calling an output erroneous. A cautious overseer and a perceptive one can show the same hit rate. The authors add an extension: for unfairness there is no ready ground truth, so researchers must choose a standard (the 80% adverse-impact rule, group-fairness definitions, justice rules, or a consensus among raters), and the choice changes the measures (§3.2.2, pp. 12–15).

§3.3 (pp. 15–22) offers hypotheses, in a table of task, system and person factors with a predicted direction (Table 2, p. 16). Examples: time pressure lowers sensitivity; high levels of automation "can remove people from the decision-making situation, making it harder to find evidence of unfairness" (p. 18); low system reliability can raise sensitivity, so "Optimizing the system alone may render it unoverseeable" and it "may even be a (possibly controversial) option to deliberately use a less sophisticated system" (p. 18). Oversight aids may help, but "whereas such aids may enhance sensitivity, they also come with all the challenges associated with automated decision aids such as automation bias or deskilling" (p. 19). On transparency: "to date there is limited evidence that explanations can actually benefit unfairness detection" (p. 19). They know of no study applying SDT to unfairness detection in AI outputs (p. 22).

## Relation to the argument
It supplies the vocabulary for premise P12 and a clean test for it. The post asks a person to read evidence and to halt; Langer et al. say the question to ask is the person's sensitivity and bias on a defined error, measured against a chosen standard. It also names a limit that bears on the argument: nobody has measured this for unfair outputs, and for inaccurate outputs they cite one SDT study, Gentile et al. (2023), as showing that recent work has begun (p. 6).

It bears on ruling D7 (understanding by deciding): the passage on automation removing the person from the decision, with its hiring example, where overseers who "analyzed information from applicants" themselves do better than those shown only a score (p. 18, citing Langer, König et al., 2021), is a stated hypothesis consistent with the author's pilots point. It is a hypothesis from one cited study, not a test.

It bears on D3 only indirectly: the authors list transparency as having uncertain effect on sensitivity and response bias (Table 2, p. 16).

Facet check: Facet G (abstract only) summarizes it as "a signal-detection framework for error detection by overseers". That is right, and it should be cited as a framework paper; there are no data in it.

## In conversation with
In the bib and cited here: `bainbridge1983ironies` (p. 18, the "irony of automation" and its p. 777 quotation); `green2022flaws` (the case that oversight policies rest on weak evidence, pp. 2, 18, 23); `sterz2024quest` (effective oversight reduces risk, p. 2); `parasuraman2010complacency` (complacency, automation bias, pp. 4, 18); `bucinca2021trust` (forced reflection time improves detection of flawed recommendations, p. 17); `gigerenzer1995improve` (natural frequencies in stimulus design, fn. 5, p. 12). Cites the 2015 algorithm-aversion paper, a different work from `dietvorst2018overcoming`, and Colquitt (2001), a different Colquitt paper from `colquitt2001justice`. The bib's `laux2024institutionalised` is not cited.
Leads: McBride et al. (2014), the error-management model (detect, explain, correct, integrate); Sheridan (2021) on supervisory control; Zerilli et al. (2019) on the control problem; Alexander (2022), the dissertation on adverse-impact judgments.

## Caution
Conceptual; the predictions in Table 2 are the authors' hypotheses, not findings. It treats one overseer and one output at a time, and it does not cover an overseer of a system that adapts to the overseer. Its examples come from hiring and medicine, not mediated platforms. Cite pages by the journal's "Page N of 30" counter.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The publisher PDF (Minds and Machines 35:1, 30 pp., same authors and title), extracted with pdftotext; page numbers are the PDF pages, which match the 'Page N of 30' counter. I checked 11 verbatim quotations with their pages, Table 2 on p. 16, the 80% rule discussion, the Colquitt, Dietvorst, Alexander, Gentile, Bainbridge, Gigerenzer, Bucinca, Green and Sterz references, and that Laux is not cited.

**Findings:** One overstatement fixed: the card said that for inaccurate outputs the authors 'cite only a few SDT studies (Gentile et al., 2023, p. 6)'. On p. 6 they cite a single study, Gentile et al. (2023), as showing that 'recent work has begun' to use SDT on inaccurate outputs. Everything else matches. The facet quotation 'a signal-detection framework for error detection by overseers' is the facet's wording and was not checked against the paper.
