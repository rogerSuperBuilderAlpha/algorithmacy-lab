---
key: wang2024survey
apa: "Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science*, 18(6), Article 186345. https://doi.org/10.1007/s11704-024-40231-1"
authors: "Wang, Lei; Ma, Chen; Feng, Xueyang; Zhang, Zeyu; Yang, Hao; Zhang, Jingsen; Chen, Zhiyuan; Tang, Jiakai; Chen, Xu; Lin, Yankai; Zhao, Wayne Xin; Wei, Zhewei; Wen, Jirong"
year: 2024
title: "A survey on large language model based autonomous agents"
venue: "Frontiers of Computer Science"
volume: "18"
issue: "6"
pages: "Article 186345"
doi: "10.1007/s11704-024-40231-1"
url: ""
type: article
facets: [F8]
claims: [c1]
role: support
load: load-bearing
read_depth: partial
object_read: "Publisher PDF (Springer, open access, CC BY 4.0 per its own licence block; 26 pp. with references) and its text layer wang2024survey.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/wang2024survey/; fetched from link.springer.com (FETCH_LOG.tsv); read 2026-11-08; PARTS READ: PDF pp. 1-9 (abstract, §1, §2.1 profiling, memory, planning and the action module as far as external tools) and pp. 19-20 (§6.2-§6.6, §7); NOT READ: p. 10 (end of §2.1.4), §2.2 (pp. 10-11), §3 applications (pp. 12-15), §4 evaluation (pp. 16-18), §5, §6.1, the reference list; sha256 7bc39a036655ab7523cd56963738a0c0e8eab7790ef43318ff8706c36dc67b8a (PDF, from sha256.txt; recomputed with shasum -a 256, matches)"
verified: corrected
verified_against: "crossref.json (13 authors, title, venue, 18(6), article 186345, DOI, journal-article, dates); sha256 recomputed; text layer and per-page pdftotext, 12 quotations traced"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# L. Wang et al. (2024), A survey on large language model based autonomous agents

## What it argues

Lei Wang and twelve co-authors at Renmin University of China survey the field of agents built on large
language models. They organise it under three heads: how to construct such an agent, where agents are
applied, and how to evaluate them. The construction half carries the part this paper needs. The authors
propose "a unified framework" for agent architecture with four modules: profiling (the agent's role,
"usually written into the prompt"), memory (short-term memory is the context window; long-term memory is
an external vector store), planning (with or without feedback; some agents hand planning to an external
planner), and action (the module that calls tools and APIs and touches the environment). They compare the
split to ordinary machine learning: designing the architecture is like choosing the network structure, and
acquiring capability is like learning the parameters. Their closing list of open problems names
role-playing, alignment, prompt robustness, hallucination, the "knowledge boundary" of the LLM, and the
speed of inference.

The survey is descriptive. It sorts roughly a year of agent papers into a taxonomy and does not argue about
what an AI is. Its own framing treats the LLM as the centre: the authors say research "employs LLMs as
central controllers", and the modules are things that "equip" the LLM. That is a model-centred vocabulary
wrapped around a non-model-centred system.

## What the paper uses it for

- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): the use fits for the "harnesses"
  third of the claim. Wang et al. show, in a peer-reviewed survey, that the field already builds agents as
  an LLM with a profile prompt, a memory store, a planner and a tool layer around it, and that the modules
  depend on one another. Three stretches. First, the survey never uses "harness" as a noun (the only hit in
  the text layer is the verb in "harness their respective benefits"), so "harness" is the paper's word for
  their modules, not theirs. Second, it says nothing about virtual machines. In the pages read, efficiency
  appears as a property of memory storage and retrieval and, in §6.6, as slow inference, never as part of
  what makes the AI (the unread §4 also lists "efficiency metrics" for evaluation). Third, the authors do not say the modules are
  part of the AI rather than add-ons; their wording leans the other way (LLM as "central controller"). The
  paper has to make that step itself. The survey supplies the anatomy, not the argument.
- No use for c2 (model-centrism misplaces the intelligence). A reader could cite the survey on either side,
  and the card does not claim it as a witness against model-centrism.

## Loci

Locators: the held copy prints a running header "Front. Comput. Sci., 2024, 18(6): 186345" and page
numbers 1-26 (article, licence block, references and author biographies), so PDF page n = printed
page n. I matched every quotation against
`pdftotext` output for that single PDF page of the held PDF (sha256 above), because the `.txt` layer
interleaves the two columns. Where the source has inner double quotation marks the card would give single
quotes; no quotation below needed that.

- "employs LLMs as central controllers to construct autonomous agents" — PDF p. 1, §1; matched against page text of wang2024survey.pdf
- "the key idea is to equip LLMs with crucial human capabilities like memory and planning to make them behave like humans and complete various tasks effectively." — PDF p. 1, §1; matched against page text of wang2024survey.pdf
- "building autonomous agents is far from QA, since they need to fulfill specific roles and autonomously perceive and learn from the environment to evolve themselves like humans." — PDF p. 2, §2.1; matched against page text of wang2024survey.pdf
- "the overall structure of our framework is illustrated Fig. 2, which is composed of a profiling module, a memory module, a planning module, and an action module." — PDF p. 2, §2.1; matched against page text of wang2024survey.pdf
- "designing the agent architecture is analogous to determining the network structure, while the agent capability acquisition is similar to learning the network parameters." — PDF p. 2, §2; matched against page text of wang2024survey.pdf
- "The profile module serves as the foundation for agent design, exerting significant influence on the agent memorization, planning, and action procedures." — PDF p. 3, §2.1.1; matched against page text of wang2024survey.pdf
- "short-term memory is analogous to the input information within the context window constrained by the transformer architecture. Long-term memory resembles the external vector storage that agents can rapidly query and retrieve from as needed." — PDF p. 4, §2.1.2; matched against page text of wang2024survey.pdf
- "A significant distinction between traditional LLMs and the agents is that the latter must possess the capability to learn and complete tasks in dynamic environments." — PDF p. 6, §2.1.2; matched against page text of wang2024survey.pdf
- "This module is located at the most downstream position and directly interacts with the environment." — PDF p. 8, §2.1.4; matched against page text of wang2024survey.pdf
- "the agents are empowered with the capability to call external tools for executing action." — PDF p. 9, §2.1.4; matched against page text of wang2024survey.pdf
- "they encompass not a single prompt but a prompt framework that considers all modules, wherein the prompt for one module has the potential to influence others." — PDF p. 20, §6.3; matched against page text of wang2024survey.pdf
- "the efficiency of agent actions is greatly affected by the speed of LLM inference." — PDF p. 20, §6.6; matched against page text of wang2024survey.pdf

## Caution

- **Read depth.** `partial`. I read the abstract, the introduction, the architecture framework through the
  action module's tool list, and the challenges and conclusion. I did not read the capability-acquisition
  section, the applications, the evaluation section or the reference list. The paper must not cite the
  survey for anything in those parts without a further read.
- **Author list.** DECISIONS and the F5-F9 triage printout stopped at twelve names and flagged the last as
  unconfirmed. Crossref gives thirteen, in this order: Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao
  Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Jirong
  Wen. The PDF's first page shows the same thirteen. The APA string above carries all thirteen ("Zhao, W.
  X."; "Wen, J.").
- **Dates and version.** The PDF states "Received March 5, 2024; accepted March 10, 2024". Crossref gives
  online 2024-03-22 and a print date of December 2024 for volume 18, issue 6. The year 2024 holds on every
  count, so no `registered_year`. This is the publisher's open-access version, not a preprint.
- **Pagination.** Crossref has an article number (186345) and no page range. The card uses the article number
  and PDF pages.
- **Homonyms.** "Wang, L." is a very common name. This is Lei Wang of Renmin University of China (Gaoling
  School of Artificial Intelligence), with Xu Chen and Yankai Lin as corresponding authors.
- **Dated coverage.** The survey's Fig. 1 counts papers from January 2021 to August 2023. It predates the
  harness-engineering literature the paper may also cite (for example `zhou2026externalization`).
- **What the paper may not claim from it:** that the authors treat the surrounding modules as part of the
  AI, that they discuss virtual machines, or that they argue against model-centrism.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 3
- verdict: corrected. Frontmatter matches Crossref; all 12 quotations are verbatim on the stated PDF pages; read_depth partial is honest; the c1 stretches are named.
- checked: frontmatter against crossref.json; sha256 of the PDF; each quotation by per-page pdftotext with whitespace and hyphenation normalised; section numbers (§6.1-§6.6 headings, §6.6 Efficiency); "harness" occurrences (verb on p. 5 and a reference title only); "central controllers", "usually written into the prompt", "unified framework", "external planner", received/accepted dates, Renmin affiliation, corresponding-author marks, Fig. 1 date range; PDF page count (26) and printed page numbers.
- changed: (1) c1 bullet: "efficiency appears only as slow inference (§6.6)" was too strong; the pages read also use efficiency for memory storage and retrieval, and the unread §4 lists "Efficiency metrics". Reworded. (2) Loci note said printed page numbers run 1-20 on the article pages; the held PDF numbers all 26 pages 1-26. Reworded; locators unchanged.
