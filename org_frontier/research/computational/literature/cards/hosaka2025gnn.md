---
citekey: hosaka2025gnn
title: Graph Neural Networks for Integrated Information and Major Complex Estimation
authors: Hosaka, Tadaaki
year: 2025
doi: 10.1371/journal.pone.0335966
arxiv: null
journal: PLOS ONE
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: plos-template
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0335966&type=printable
sha256: caf6b1e40988534b75e62339c952bec34cfc69187ec5ea35be8ddb3877fbe234
pdf_path: literature/pdfs/hosaka2025gnn.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether graph neural networks (GNNs) can approximate the system-level integrated information Φ and the "major complex" of integrated information theory (IIT) 3.0, quantities whose exact computation grows exponentially with node count and is therefore restricted to systems with fewer than ~10 nodes. The author trains a GNN built from four transformer-convolution layers with multi-head attention, plus a two-branch head that jointly regresses Φ (graph-wise) and classifies major-complex membership (node-wise), using exact PyPhi solutions for randomly generated systems of N = 5, 6, 7 nodes as ground truth. In a non-extrapolative test (mixed N = 5,6,7), the model reaches a Φ correlation of 0.7446 and node-wise major-complex accuracy of 0.8574; in an extrapolative test (train on N = 5,6; test on N = 7) it tends to underestimate Φ in the high-value range but preserves qualitative patterns. Applied to much larger systems (N up to 100) across tree-like, fully-connected, and loop-containing topologies, the GNN reproduces qualitative topology-dependent trends even though absolute Φ is underestimated. A qualitative case study of a 100-node "split-brain-like" system of two 50-node subsystems shows that as inter-subsystem edge probability p_e rises, "local integration" disappears (around p_e ≈ 0.01–0.02) and the major complex expands toward "global integration," with the node ratio climbing to about 0.93. The author concludes the GNN is a practical tool for qualitative analysis of Φ and major complexes in large systems where exact IIT 3.0 is infeasible.

## Key facts it relies on
- The model uses four consecutive transformer convolutional layers with multi-head attention (first conv 50 output channels with 4 heads; 2nd/3rd convs 150 output channels; a final one-head conv with 50 output channels), then splits into two branches: Branch 1 (global max pooling → fully connected → linear) estimates Φ, and Branch 2 (global max pooling difference, node features minus the pooled vector r → fully connected → softmax) classifies major-complex membership.
- Node feature vectors are six-dimensional: (1) max{p_i(1|S), p_i(−1|S)}, (2) parameter T, (3) node degree, (4) closeness centrality, (5) betweenness centrality, (6) clustering coefficient; edge features are one-dimensional (edge weight J_ij). The node state S_i is deliberately not used as a feature to preserve invariance under state inversion (p(S*|S) = p(−S*|−S)).
- Systems are randomly generated with binary node states (+1/−1), undirected edges with connection probability p = 0.4, edge weights J_ij drawn from a standard normal distribution, and transition probabilities from a Boltzmann distribution p_i(s|S) = 1/(1 + exp(−2τ_i s / T)) with τ_i = Σ J_ij S_j; T is sampled uniformly from [0.1, 3.0] per system.
- Ground-truth Φ and major complexes were computed exactly with the PyPhi library (Mayner et al., ref 14) for N = 5, 6, 7.
- Non-extrapolative experiment (Table 1, 3000 graphs, 1000 each for N = 5,6,7; 90/10 train/test; averaged over 100 repetitions): proposed method Φ MSE = 0.4611, Φ correlation = 0.7446, node-wise major-complex accuracy = 0.8574, graph-wise accuracy = 0.5779.
- Extrapolative experiment (Table 2, train/validate on N = 5,6 with 1500 graphs; test on 1000 graphs of N = 7): proposed method Φ MSE = 0.8543, Φ correlation = 0.6815, node-wise accuracy = 0.8229, graph-wise accuracy = 0.4686.
- The LION optimizer (learning rate 0.0001, mini-batch 128) converged in an average of 94.2 epochs versus 166.2 (Adam), 185.4 (RAdam), and 160.8 (AdamW); training used a multi-task loss of MSE for Φ plus five times the cross-entropy for classification, with a penalty factor of 1.8 on label "out," data augmentation (5% added disconnected-subsystem examples), and k-means oversampling into seven bins.
- Computational advantage: training on 3000 graphs (N = 5,6) typically finished in 2–3 minutes and inference on 1000 graphs (N = 7) took under 2 seconds, whereas exact IIT 3.0 computation for a single N = 7 graph required more than 30 minutes on average; the cut-one approximation (ref 14) reduced exact computation time by less than 10%.
- Split-brain-like case study (100 nodes = two 50-node subsystems with internal edge probabilities 0.6 and 0.4): at p_e = 0 the major complex is the first 50 nodes (ratio 0.5); as p_e rises the "local integration" proportion drops sharply around p_e ≈ 0.01–0.02 (Fig 11), and the major-complex node ratio eventually reaches about 0.93 (Fig 12) while estimated Φ stays roughly constant for p_e ≲ 0.02 then increases.

## Critical notes from the literature
- The author states the method cannot accurately estimate absolute Φ for large N; for fully-connected and loop-containing systems the estimated Φ values are lower than exact values, so usefulness is limited to comparing systems or identifying topology-dependent trends, not precise Φ values.
- In the extrapolative setting the model systematically underestimates Φ in the high-value range not covered by training data; the author notes confidence in Φ estimates may decrease for graphs larger than N = 7.
- The multi-task approach yielded only limited improvement over single-task models, which the author flags as a failure to fully capture the deeper interconnection between Φ and the major complex, and names as a key challenge for future work.
- Visualizations of learned attention weights showed no general or consistent correspondence to information integration as defined in IIT; the author explicitly reports finding no clear relationship between attention patterns and the IIT framework.
- The work adopts IIT 3.0 only; the author argues compatibility with IIT 4.0 (both share the objective of computing Φ and identifying the complex), but the split-brain analysis and large-N claims are qualitative and the author states further validation across different datasets and scenarios is required.

## Key topics covered
Integrated information theory (IIT 3.0); integrated information Φ; major complex; minimum information partition; graph neural networks; transformer convolution; multi-head attention; message passing and 1-WL expressiveness; multi-task learning (regression + node classification); PyPhi; Boltzmann transition dynamics; node centrality features; LION optimizer; data augmentation and oversampling; extrapolation to larger systems; tree-like / fully-connected / loop-containing topologies; split-brain model; local vs global integration; computational complexity of IIT; ensemble prediction.
