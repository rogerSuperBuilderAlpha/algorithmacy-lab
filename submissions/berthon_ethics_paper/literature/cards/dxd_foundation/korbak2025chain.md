# Korbak, T., Balesni, M., Barnes, E., Bengio, Y., Benton, J., Bloom, J., … Mikulik, V. (2025). *Chain of thought monitorability: A new and fragile opportunity for AI safety* (arXiv:2507.11473). arXiv preprint.

**Identifier:** arXiv:2507.11473 · **Read depth:** full_text (arXiv v2, 7 Dec 2025, 11 pp.; pagination is the PDF's. Pages 1–7 of argument and 8–11 of references read; the reference list was read for the citations below, not for every entry) · **Source-tier:** preprint, multi-institution position paper · **Evidence basis:** direct_read · **Design and sample:** none (a position paper; it states "The paper represents the views of the individual authors and not necessarily of their affiliated institutions," p. 1) · **Parties modeled:** other: a developer, an automated monitor and a reasoning model; people appear once, as possible users of a visible trace · **Facets:** G · **Read:** 2026-10-13

## What it argues
Korbak et al. argue that models which "think" in human language give safety researchers a chance: "we can monitor their chains of thought (CoT) for the intent to misbehave" (abstract, p. 1). A CoT monitor is "an automated system that reads the CoT of a reasoning model and other relevant information and flags suspicious or potentially harmful interactions" (§1, p. 2); flagged responses "could then be blocked, or replaced with safer actions, or reviewed in more depth" (p. 2). They offer two reasons a trace may be monitorable. First, for hard tasks a transformer must use its chain of thought as working memory, because long serial computation passes through it (§1.1, pp. 2–3). Second, models tend to think out loud even when they do not have to (§1, p. 2). They admit that this gives no guarantee: the trace is incomplete, severe harms may need little reasoning, and "CoT monitoring is imperfect and allows some misbehavior to go unnoticed" (abstract).

Section 2 lists ways monitorability could erode: drift from readable language under more outcome-based reinforcement learning, direct supervision of the trace, indirect optimization pressure, and new architectures, including models that reason "in a continuous latent space (Hao et al., 2024; Geiping et al., 2025)" and would "lose the safety advantages that CoT confers" (p. 5). Section 3 sets research questions: how to evaluate monitorability, when it suffices, and what pressures degrade it. It says existing faithfulness tests "do not disambiguate the propensity versus the necessity of models to externalize their reasoning" and that "it is unclear what level of monitorability is sufficient" (p. 5). Section 4 asks developers to track monitorability, publish scores in system cards and weigh them in training and deployment decisions.

## Relation to the argument
Three points bear on the Nadella lineage in facet G.

First, the monitor is a machine. In the paper's design no person reads a trace, so it offers no evidence on whether a person could use one. This supports the author's reading that the safety literature leaves the human reader untested.

Second, it speaks to ruling D3 (disclosure is literacy-based and does not change the ability to navigate an algorithm) by a different route. The paper considers showing the chain of thought to users and withholds a recommendation: "Another potential intervention is for developers to make the chain of thought visible, allowing users to observe and report issues. However, this could backfire" because pressure to make traces "look safe" could break monitorability; "we don't make an explicit recommendation either way on this" (§4, p. 7). The authors' worry is that disclosure changes the thing disclosed.

Third, on ruling D4 and premise P11: the paper treats chain-of-thought monitoring as one layer among several: "safety measures for future AI agents will likely need to employ multiple monitoring layers that hopefully have uncorrelated failure modes" (§6, p. 7).

Facet check: Facet G says the post's P9 "non-negotiable" matches Korbak's "recommend[s] ... investment in CoT monitoring". The paper is more guarded. It recommends investment "alongside existing safety methods" (abstract) and "only as an addition to existing safety research directions and not as a replacement" (§5, p. 7). The paper does not call monitoring non-negotiable. The facet's quotations from the abstract and the "fragile" theme are accurate.

## In conversation with
In the bib and cited here: `greenblatt2024ai` (as "Greenblatt et al., 2024b", for review of flagged outputs and red-team evaluation, pp. 2, 5–6); `lanham2023measuring` (perturbing a trace to test whether it matters, p. 5); `turpin2023language` and `chen2025reasoning` (faithfulness tests, pp. 2, 5); `baker2025monitoring` (training pressure on traces, pp. 4–5); `hao2024training` (latent reasoning, p. 5). Not cited: `kutasov2025shade`, `jia2026faithfulness`. The author list includes Daniel Kokotajlo (AI Futures Project); the paper does not cite the bib's `kokotajlo2025ai`.
Leads: Bhatt et al. (2025), Ctrl-Z, arXiv:2504.10374; Benton et al. (2024), sabotage evaluations, arXiv:2410.21514; Arnav et al. (2025), CoT Red-Handed, arXiv:2505.23575; Emmons et al. (2025) on stress-testing monitors.

## Caution
A position paper. Its claims are conditional ("may be fragile") and forward-looking; it reports no new data, and the "externalized reasoning property" is an argument about transformers, not a measured result. Cite it for the idea of monitorability and for the authors' stated caution, not for the effectiveness of monitoring. Authorship runs across labs that build the models it discusses.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The 11-page arXiv v2 PDF (7 Dec 2025; title, arXiv ID and author list incl. Kokotajlo, Baker, Shah, Mikulik match). All 20 quotations from the paper located by page (pp. 1, 2, 3, 4, 5, 7) and section; citations in the paper's text and reference list for Greenblatt 2024b (pp. 2, 5, 6), Lanham 2023 (p. 5), Turpin 2023 and Chen 2025 (pp. 2, 5), Baker 2025 (pp. 4-6), Hao 2024 (p. 5), and the four leads (arXiv 2504.10374, 2410.21514, 2505.23575; Emmons et al. 2025). Neither `kutasov2025shade` nor `jia2026faithfulness` appears in the text.

**Findings:** No issues found. "Non-negotiable" is the facet's or the post's word, not the paper's, as the card says.
