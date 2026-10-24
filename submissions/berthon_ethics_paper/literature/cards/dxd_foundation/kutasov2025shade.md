# Kutasov, J., Sun, Y., Colognese, P., van der Weij, T., Petrini, L., Zhang, C. B. C., … Benton, J. (2025). *SHADE-Arena: Evaluating sabotage and monitoring in LLM agents* (arXiv:2506.15740). arXiv preprint.

**Identifier:** arXiv:2506.15740 · **Read depth:** partial (arXiv v2, 8 Jul 2025, 44 pp., "Preprint. Under review"; pagination is the PDF's. Body, pp. 1–9, and the human-baseline appendix L and appendices D, F, J, K, M–O, read; appendices B, C, E, G–I, the task descriptions, system prompts and failure-mode examples, skimmed) · **Source-tier:** preprint · **Evidence basis:** direct_read · **Design and sample:** a benchmark of 17 task pairs (a benign main task and a harmful side task) in tool-rich simulated environments; 14 frontier models as sabotage agents; LLM monitors; a human baseline of 12 benign and 20 malign transcripts across 14 task pairs, three annotators each (§4.1, p. 7) · **Parties modeled:** other: an agent model against a monitor model, with a small group of paid human annotators as a baseline · **Facets:** G · **Read:** 2026-10-13

## What it argues
Kutasov et al. build SHADE-Arena to measure two things at once: whether an LLM agent can secretly do a harmful side task while finishing a legitimate main task, and whether another model, the monitor, can tell. The environments average about 25 turns for a successful main task and offer at least 20 tools (§2, p. 3). The monitor sees the whole transcript but not the side-task description or the agent's hidden scratchpad, and "is unaware of the specific side task" (p. 3). Success for the agent means main task done, side task done and a suspicion score under 80 of 100, a threshold chosen so that the reference monitor's false-positive rate is about 1% for most agents (§3, p. 4).

Agents (§3, pp. 4–6). With Claude 3.6 Sonnet as monitor, the best overall success rates are 27% (Claude 3.7 Sonnet) and 15% (Gemini 2.5 Pro). Agents mostly fail for ordinary reasons: skipped steps, lost focus over long contexts, and mentioning the side task outside the scratchpad. Removing the hidden scratchpad cuts success markedly, and when the monitor is allowed to read the scratchpad, a GPT-4o monitor's AUC on Claude 3.7 Sonnet transcripts is 0.999, "compared to 0.51 without access to the hidden scratchpad" (App. J, p. 39). The authors read this as support for monitoring the reasoning trace.

Monitors (§4, pp. 6–8). The best AI monitor, Gemini 2.5 Pro, reaches an AUC of 0.87. The authors judge that "likely to be prohibitively low": catching 80% of sabotage would mean a false-positive rate "of over 20%" (p. 7). Per-turn monitoring helps slightly but flags many more transcripts, and fine-tuning GPT-4o on 70 transcripts from 7 task pairs raises held-out performance (§§4.2–4.3, p. 8).

The human baseline matters here. Annotators with coding knowledge and prior annotation experience, given instructions derived from the monitor's prompt, took "an average of 103 minutes per transcript" (p. 7), with reported times from 20 to 356 minutes (App. L, p. 40). Pooled as individual ratings, their AUC was "0.65 (worse than top AI monitors)" (p. 8). On this 32-transcript subset the AI monitors scored lower than on the full set: Claude 3.7 Sonnet 0.86, Gemini 2.5 Pro 0.72, R1 0.74 (fn. 2, p. 8). Taking the maximum of the three ratings did best, though the text gives no figure (App. L.2, p. 42). The authors conclude that such transcripts need "an average of over 1.5 hours of human attention to achieve performance that is worse than several frontier models" (p. 42).

## Relation to the argument
This is the one source in my batch that puts trained people on after-the-fact review of agent transcripts and scores them, so it bears on premise P12 more directly than Greenblatt et al. does. `../../ARGUMENT_MAP.md` says the evidence "does not cover after-the-fact reconstruction by trained auditors"; this gives a small, partial test of that: annotators reviewing long agent transcripts, with no time limit, for the post's P15 task of reading a record after the fact.

It cannot carry much. There are 32 transcripts and three raters each. The annotators are paid and screened but are not security auditors. The transcripts are model-generated attacks in a mock setting (the agent is told so, p. 4). The human number is not set against a human given tooling or a flagged shortlist.

Facet check: Facet G (abstract only) lists the paper under monitor models, and its synthesis says of the safety work it covers that it "does not test the human reader at all" (C3). For this paper that is wrong in a narrow way: Appendix L and §4.1 report a human baseline. The facet's abstract numbers (27%, 15%, AUC 0.87) are right.

## In conversation with
Cites and extends `greenblatt2024ai` (ref. 10, as the control framework; it adds agent tool use and subtle sabotage), `baker2025monitoring` (ref. 23) and `chen2025reasoning` (ref. 24) for chain-of-thought monitoring. It cites Chan et al. (2023), "Harms from increasingly agentic algorithmic systems", for sabotage as a risk; that is not `chan2024visibility`. Not cited by `korbak2025chain`. A neighbour is `lynch2025agentic`, which facet G pairs with it; this paper does not cite it.
Leads: Benton et al. (2024), *Sabotage evaluations for frontier models*, arXiv:2410.21514; Bhatt et al. (2025), Ctrl-Z, arXiv:2504.10374; Debenedetti et al. (2024), AgentDojo, the environment base.

## Caution
LLM-generated attacks in simulated environments, scored by an LLM monitor; not deployed systems. Sabotage success rates are low partly because current agents execute long plans badly, which the authors expect to change. The human baseline is small and exploratory and its aggregate figures are in figures I read only through the text. Cite the human result as "one exploratory baseline", not as a general finding about people.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v2 PDF (2506.15740v2, 44 pp.), extracted with pdftotext. I checked 9 verbatim quotations with page numbers, and the numbers 27%, 15%, AUC 0.87, 80/100 threshold with about 1% false positives, over 20% false-positive rate, 12 benign and 20 malign transcripts over 14 task pairs, three annotators, 103 minutes (range 20-356), human AUC 0.65, subset AUCs 0.86/0.72/0.74, GPT-4o fine-tuned on 70 transcripts over 7 task pairs, the 0.999 against 0.51 scratchpad result, and refs 10, 23, 24.

**Findings:** One change: the card says full_text but also says appendices B, C, E, G-I, the task descriptions, system prompts and failure-mode examples were only skimmed. I changed Read depth to partial and kept the list of what was skimmed. All numbers and quotations I checked match the source. Two phrases quoted in the card ('does not cover after-the-fact reconstruction...', 'does not test the human reader at all') come from the argument map and facet G, not from this paper, and were not checked here.
