---
citekey: guerrero2023systematic
title: A systematic review of integrated information theory: a perspective from artificial intelligence and the cognitive sciences
authors: Guerrero, Luz Enith and Castillo, Luis Fernando and Arango-L\'opez, Jeferson and Moreira, Fernando
year: 2023
doi: 10.1007/s00521-023-08328-z
arxiv: null
journal: Neural Computing and Applications
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: doi-landing
source_url: https://ceur-ws.org/Vol-2287/paper20.pdf
sha256: a3c456dd999cd2c98dc4e3b523bc33aaed1ae4dc6f0b0b49a8ab874f99a70da1
pdf_path: literature/pdfs/guerrero2023systematic.pdf
verified: true
generated_run: 2026-06-25
---

> METADATA/CONTENT MISMATCH (flagged, not invented): The frontmatter above describes the Guerrero et al. 2023 systematic review in *Neural Computing and Applications* (doi 10.1007/s00521-023-08328-z). The PDF actually stored at `pdf_path` is a different paper: **"Using Tononi Phi to Measure Consciousness of a Cognitive System While Reading and Conversing"** by Matthew Iklé, Ben Goertzel, Misgana Bayetta, George Sellman, Comfort Cover, Jennifer Allgeier, Robert Smith, Morris Sowards, Dylan Schuldberg, Man Hin Leung, Amen Belayneh, Gina Smith, and David Hanson — a CEUR-WS proceedings paper (Vol-2287, paper20.pdf; the `source_url` points to this CEUR file, not the Springer DOI). The frontmatter is preserved verbatim per task instructions, but **all sections below are authored strictly from the actual PDF contents** (the Iklé/Goertzel paper). Treat the bibliographic fields as unverified pending reconciliation of the citekey with the correct PDF.

## Summary
This short proceedings paper reports computational experiments estimating Giulio Tononi's Phi (a candidate measure of integrated information / "level of consciousness" from Integrated Information Theory) inside the OpenCog cognitive architecture during two practical tasks: (1) reading and semantically analyzing short documents, and (2) controlling the Sophia humanoid robot through a dialogue-based guided meditation. The data fed into the Phi computation are time-series of Short-Term Importance (STI) values for Atoms (nodes/links) in OpenCog's Attentional Focus, managed by the Economic Attention Networks (ECAN) module. Because the Attentional Focus exports a large number of sparse time series — ill-suited to the available Phi toolbox, which works best on a few dense series — the authors introduce a novel pipeline of first applying Independent Component Analysis (ICA) to reduce dimensionality and then computing Phi (specifically Phi 3.0, with Queyranne's Algorithm to approximate the Minimum Information Partition). Results are qualitative and explicitly preliminary: in Experiment 1, Phi jumped when the concept "insecticide" first became important during reading about insects then poisons; in Experiment 2, Phi was higher soon after more intense verbal interaction and lower while Sophia passively watched the subject meditate. The authors frame these correspondences between behavior and Phi as preliminary validation of the "ICA plus Phi" methodology rather than a claim about machine consciousness.

## Key facts it relies on
- The study runs **two experiments** in OpenCog: (1) reading/parsing short documents about insects and poison, and (2) using OpenCog plus the Ghost dialogue-control framework of the Hanson AI system to drive the Sophia robot through part of a guided meditation session.
- Phi is computed from **time-series of STI (Short-Term Importance) values** of Atoms in OpenCog's **Attentional Focus**; ECAN weights each Atom with two numbers, STI (short-term importance) and LTI (long-term importance).
- The authors implement **Phi 3.0** (rather than the approximate Φ*, both introduced by Oizumi), computing probability distributions per Krohn & Ostwald [8], and use **Queyranne's Algorithm** to approximate the Minimum Information Partition (MIP) in O(N³) time; their Python code is based on the Matlab "Practical PHI Toolbox" of Kitazono & Oizumi.
- They cite Tegmark's point that there are **at least 420 choices** one can make in calculating the Phi measure, and note that both the MIP determination and the required probability-distribution vector size grow **super-exponentially** with the number of nodes.
- The **novel methodological contribution** is an "ICA plus Phi" pipeline: apply Independent Component Analysis to reduce many sparse STI time series to a few dense ones before computing Phi; the optimal number of dimensions is chosen by minimizing the total **sum of squared residuals (SSR)**.
- In **Experiment 2** they found "thousands of Atoms" passing through the Attentional Focus and used an **optimal embedding dimension of 3** for the ICA reduction.
- **Experiment 1 result:** Phi values were calculated on the ConceptNodes "insect," "poison," and "insecticide"; there was a jump in Phi when "insecticide" first became important, interpreted as correlated with increased complexity of attentional spreading in the Atomspace (Figures 2, 3).
- **Experiment 2 result:** comparing system logs with the Phi time series, Phi was higher soon after the start of more intense verbal interaction and lower while Sophia was watching the subject meditate or breathe deeply (Figure 4).
- Experiment 1 was built on a prior OpenCog language-comprehension setup, seeding the Atomspace with Wordnet/ConceptNet4 relations and SimilarityLinks weighted via the Adagram neural network; IIT is attributed to Tononi (2004).
- Initial research was conducted in **Summer 2018** at Adams State University and supported by **Army Research Office grant W911NF-15-1-0514**; the Figure-1 "Loving AI" robot-meditation trial was conducted in California in 2018.

## Critical notes from the literature
- The authors repeatedly stress the work is **qualitative and preliminary**: they claim only "correspondences" between Phi changes and system behavior as "preliminary validation," not quantitative or statistical confirmation.
- The paper itself flags **foundational interpretive uncertainty about Phi**: it notes Tononi posits Phi as a fundamental measure of level of consciousness, while one of the authors (Goertzel [5]) holds the more cautious view that Phi estimates only one among many properties of consciousness in roughly human-like systems; they sidestep this by treating Phi merely as a useful measure of holistic information integration.
- The **ICA-plus-Phi dimension-selection step is acknowledged as immature** — the authors say choosing the number of independent dimensions via minimum SSR "will merit from further experimentation and refinement."
- Computing exact Phi is **intractable at scale** (super-exponential MIP and probability-vector growth; ~420 measure-definition choices per Tegmark), so the reported values depend heavily on approximation choices (Phi 3.0, Queyranne's MIP approximation, ICA reduction) whose effect on the results is not validated.
- The experiments use **only a handful of selected ConceptNodes / a single embedding dimension (3)** and small, illustrative tasks; no baselines, controls, or significance tests are reported, limiting generalizability of any "behavior tracks Phi" claim.

## Key topics covered
Integrated Information Theory (IIT); Tononi's Phi / Phi 3.0; Φ* approximate measure; Minimum Information Partition (MIP); Queyranne's Algorithm; OpenCog cognitive (AGI) architecture; Atomspace and Atoms (neural-symbolic hypergraph); Economic Attention Networks (ECAN); Attentional Focus; Short-Term / Long-Term Importance (STI/LTI); Independent Component Analysis (ICA) dimensionality reduction; sum of squared residuals (SSR) model selection; Practical PHI Toolbox (Kitazono & Oizumi); machine consciousness; humanoid robotics / Sophia; Hanson AI Ghost dialogue framework; guided-meditation dialogue; OpenCog reading/NLP comprehension; Wordnet/ConceptNet4 and Adagram similarity seeding; neural correlate of consciousness.
