---
citekey: sun2025multiagent
title: Multi-Agent Coordination across Diverse Applications: A Survey
authors: Sun, Lijun and Yang, Yijun and Duan, Qiqi and Shi, Yuhui and Lyu, Chao and Chang, Yu-Cheng and Lin, Chin-Teng and Shen, Yang
year: 2025
doi: 10.48550/arXiv.2502.14743
arxiv: null
journal: arXiv preprint
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2502.14743
sha256: de8fbdff90b586fdd478ef5009e7584a5a1e7d37fd3c15eeab5d66fd495aab8e
pdf_path: literature/pdfs/sun2025multiagent.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This survey reviews the state of multi-agent coordination research across diverse applications, organizing it around four fundamental coordination questions: (1) what is coordination, (2) why coordination, (3) who to coordinate with, and (4) how to coordinate. The authors propose a unified framework in which coordination in sequential decision-making is an iterative process of three components: evaluating system-level performance, deciding "who to coordinate with" (interdependency/clustering), and deciding "how to coordinate" (update decisions). They first analyze three general coordination tasks common to almost all MAS — coordinated learning, communication and cooperation, and conflict-of-interest resolution — then survey six application domains: search and rescue, warehouse automation and logistics, transportation systems, humanoid and anthropomorphic robots, satellite systems, and LLM-based multi-agent systems. The survey builds on Malone et al.'s definition of coordination as "managing dependencies between activities" and frames clustering of agents as the answer to "who to coordinate with." It identifies three promising future directions: hybridization of hierarchical and decentralized coordination, human-MAS coordination, and LLM-based MAS, addressing three open performance concerns — scalability, heterogeneity, and learning mechanisms.

## Key facts it relies on
- The survey is structured around four fundamental coordination questions: what is coordination, why coordination, who to coordinate with, and how to coordinate (stated in the abstract and Introduction).
- Based on Web of Science records (Fig. 1), the MAS topic covers 148 of a total of 252 research areas; the top 15 areas include Computer Science, Mathematics, Engineering, Automation Control Systems, Robotics, and Telecommunications.
- The paper adopts Malone et al.'s [92] definition that "coordination is managing dependencies between activities (tasks) of actors (agents)," and a definition consistent with Wooldridge [149] for the multi-agent system.
- Definition 2 defines multi-agent coordination as agents interacting and making decisions for overall system-level performance, including resolving conflicted interests, via two essential decisions: who to coordinate with and how to coordinate.
- The unified framework casts coordination as an iterative three-component process: evaluate system-level performance, social choice on who to coordinate with, and how to coordinate (Fig. 3).
- Three general MAS coordination tasks are surveyed: coordinated learning (CL), communication and cooperation, and conflict-of-interest resolution (Section 3, Table 1).
- Centralized training and decentralized execution (CTDE) is identified as a typical coordinated learning paradigm, with examples MAPPO [153], VDN [134], QMIX [115]; credit assignment addressed by MADDPG [87], COMA [47], IC3Net [128]; and learnable inter-agent communication via DIAL [46], BiCNet [108], SchedNet [66].
- Six MAS application domains are surveyed: search and rescue, warehouse automation and logistics, transportation systems, humanoid and anthropomorphic robots, satellite systems, and LLM-based multi-agent systems (Section 4, Table 2).
- For satellite swarms, the paper cites concrete examples: the constellation of 4 hierarchical swarms of total 28 small satellites in the Magnetic Nano-Probe Swarm mission [88], the swarm of 36 cubesats in the QB50 project [110], and the swarm of 50 nano-satellites in the radio telescope project OLFAR [39].
- For LLM-based social interaction simulation, Gao et al. [49] construct large-scale social networks comprising 8,563 and 17,945 LLM agents; the CAMEL framework [72] enables autonomous cooperation via role-playing and inception prompting.
- The paper identifies three promising future directions: hybridization of hierarchical and decentralized coordination, human-MAS coordination, and LLM-based MAS, mapped to three open performance concerns of scalability, heterogeneity, and learning mechanism.

## Critical notes from the literature
- The authors acknowledge that few prior surveys explicitly unify interdisciplinary coordination research from the "who to coordinate with" and "how to coordinate" perspective; most classify coordination algorithms by techniques/tasks or summarize specific algorithmic techniques (Introduction).
- On conflict-of-interest resolution, the paper concludes that guaranteed safety faces "the curse of dimensionality for centralized solvers, the imperfection of rule-based distributed solutions, and the immaturity of distributed learning-based methods" (Section 3.3); rule-based solutions are hard to provide optimal solutions for all cases and are often designed case-by-case.
- The paper notes that work in satellite swarms "is still limited, and more researches are expected to empower the swarm and demonstrate the swarm's advantageous properties in more scenarios" (Section 4.5).
- The authors flag that LLMs, like other machine learning techniques, can suffer from poor generalization (e.g., hallucination) if the training dataset or joint state space cannot cover the cases of interest, and that LLM training is often expensive in economic and labor costs (Section 5.3).
- Section 4 is explicitly described as a "non-exhaustive list of MAS applications," and the applications were chosen largely from topic areas of MAS surveys in the last five years rather than as a systematic enumeration.

## Key topics covered
Multi-agent systems (MAS); multi-agent coordination; unified coordination framework; who-to-coordinate-with vs. how-to-coordinate; coordinated/social learning; centralized training decentralized execution (CTDE); credit assignment; inter-agent communication (event-triggered, stigmergy, attention); conflict-of-interest resolution; multi-agent path finding (MAPF); swarm intelligence; coordination graphs and clustering; search and rescue; warehouse automation and logistics; traffic signal control; autonomous driving; humanoid and anthropomorphic robots (dual-arm, dexterous hand); satellite constellations, swarms, and communications; LLM-based multi-agent systems (decision-making and behavior simulation); hierarchical vs. decentralized hybridization; human-MAS coordination and human-swarm interaction; nBCI; computational trust modeling; scalability, heterogeneity, learning mechanisms.
