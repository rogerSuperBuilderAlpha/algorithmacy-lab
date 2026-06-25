---
citekey: albantakis2014animats
title: Evolution of Integrated Causal Structures in Animats Exposed to Environments of Increasing Complexity
authors: Albantakis, Larissa and Hintze, Arend and Koch, Christof and Adami, Christoph and Tononi, Giulio
year: 2014
doi: 10.1371/journal.pcbi.1003966
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1003966&type=printable
sha256: dddab0e9f87af7f6151ea4eb5bf9eb29a6ce153edc15390ede326047fd6f7bad
pdf_path: literature/pdfs/albantakis2014animats.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper asks whether adaptation to environments of increasing causal complexity drives the evolution of more numerous and more integrated "concepts" in the brains of simple artificial organisms ("animats"). The authors evolved small logic-gate networks (8 binary elements: 2 sensors, 4 hidden elements, 2 motors) via a genetic algorithm over 60,000 generations to solve "Active Categorical Perception" tasks — a Tetris-like game where animats must catch or avoid falling blocks of different sizes. They analyzed the evolved brains using Integrated Information Theory (IIT 3.0) measures: the number of concepts, summed integrated information of concepts (Σφ^Max), and the integrated conceptual information (Φ^Max) of the main complex. Across four tasks of increasing difficulty (requiring increasing sequential memory) the number of concepts grew, integrated conceptual information increased, and this increase scaled with the memory demands of the environment. Restricting the animats' sensor or motor capacities — forcing greater reliance on internal memory in the same task — likewise selected for more concepts and higher integration. The authors conclude that capturing the causal structure of a rich environment, given limited sensors and internal elements, is a driving force toward highly integrated "brains," and, since IIT links integration to consciousness, this offers a rationale for why integrated/conscious structures might be evolutionarily favored.

## Key facts it relies on
- Each animat brain has a fixed architecture of 8 binary Markov elements: 2 sensors, 4 hidden elements, and 2 motors (left/right); sensor and motor elements by design cannot be part of concepts/complexes, so the maximal number of concepts is 2^4 − 1 = 15 (power set of the 4 hidden elements, excluding the empty set).
- Animats were evolved with a genetic algorithm for 60,000 generations, starting from an initial population of 100 animats with no connections between brain elements (generation zero); fitness used roulette-wheel selection with exponential measure S = 1.02^(F*128); 50 independent lines of descent (LODs) were obtained per task condition.
- Fitness is the fraction of successfully caught or avoided blocks over 128 test trials (all 16 initial positions × left/right × different block sizes); the world is 16×36 units with periodic boundaries, and blocks fall in 36 time steps.
- Four tasks of increasing memory demand were used: Task 1 (catch size 1 / avoid size 3), Task 2 (catch 1 / avoid 2), Task 3 (catch 1+4 / avoid 2+3), Task 4 (catch 3+6 / avoid 4+5); in Task 1 the momentary sensor state S1S2=11 alone distinguishes the blocks (modular solution possible), while Tasks 2–4 require integrating sensor inputs over multiple time steps.
- Average final fitness decreased with task difficulty: Task 1 ≈ 94.2±0.7%, Task 2 ≈ 94.0±1.2%, Task 3 ≈ 82.9±1.0% (83%), Task 4 ≈ 79.5±1.4% (80%) at generation 59,904.
- Spearman rank correlations of fitness with the number of concepts (Table 1) rose across tasks: <R> = 0.38 (Task 1), 0.55 (Task 2), 0.47 (Task 3), 0.71 (Task 4); correlations with Φ^Max rose from 0.11 (Task 1) to 0.50 (Task 4).
- The overall highest values found for a single animat state in these simulations were Σφ^Max = 3.11 and Φ^Max = 4.125; the fittest Task 4 animat had a main complex with average <Φ^Max> = 1.13.
- IIT 3.0 measures (concepts, Σφ^Max, Φ^Max of the main complex) were computed via transition probability matrices generated every 512 generations along each LOD and averaged over the 128 test-trial states, weighted by each state's probability of occurrence.
- In Task 1, perfect categorization can be achieved either by a purely modular network (no main complex, Φ^Max=0) or by an integrated network (Φ^Max>0); the two solution types arose with roughly equal probability across LODs, and integrated solutions showed higher degeneracy (341 different TPMs / 332 wiring diagrams for Φ^Max>0 animats vs. 60 TPMs / 44 wiring diagrams for Φ^Max=0).
- Restricting Task 1 animats to a single sensor lowered average fitness to 82.8±1.4% but selected for more concepts, higher Σφ^Max and more integration; similar effects occurred with one motor only and with 1% sensor noise, confirming that greater reliance on memory favors integration.

## Critical notes from the literature
- The authors explicitly note that any task could in principle be solved by a purely modular brain with Φ=0 given an arbitrary number of elements and time-steps; integration is favored only under constraints on the number of elements/connections (they cannot rule out that Task 4 is solvable in a non-integrated manner, but find evolution strongly prefers integrated brains there).
- The architecture is severely constrained: at most 4 hidden Markov elements and at most 4-in/4-out connections per gate, so results about the growth of concepts and Φ apply within this small, bounded substrate rather than to large networks.
- Causal measures are interrelated and tend to correlate, but the paper documents dissociations: e.g., in a Task 1 LOD Φ^Max decreased while other measures increased; main-complex (MC) measures correlated with fitness in far fewer LODs (e.g., 12/50 in Task 1) than whole-brain concept counts, because both modular and integrated brains can raise fitness.
- The link from these results to consciousness is conditional ("to the extent IIT is correct") and interpretive; the evolutionary advantage of high-Φ structures is offered as a possible rationale for why consciousness evolved, not a demonstration.
- The sensor-noise simulation showed that across all 50 LODs noise did not clearly raise integration (average final fitness in noise-free Task 1 was lower for noise-adapted animats, 88.1±1.0% vs 94.2±0.7%); only a subset of 20 best-performing noisy LODs developed more concepts and larger main complexes, indicating the compensation effect is partial and limited within 60,000 generations.

## Key topics covered
Integrated Information Theory (IIT 3.0); integrated conceptual information (Φ, Φ^Max, "big phi"); integrated information of mechanisms (φ, φ^Max, "small phi"); concepts and conceptual structures; main complex (MC) and causal exclusion; cause-effect repertoires and minimum information partition (MIP); animats / artificial life; Markov Brains and hidden Markov gates (HMGs); genetic algorithm evolution and lines of descent (LOD); Active Categorical Perception (Tetris-like catch/avoid task); sequential memory and environmental complexity; modular vs. integrated network architectures; degeneracy and robustness; sensor/motor restriction and sensor noise; earth-mover's distance (EMD); evolution of consciousness.
