---
citekey: hosaka2025graph
title: Graph neural networks for integrated information and major complex estimation
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
pdf_path: literature/pdfs/hosaka2025graph.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Exact computation of integrated information (Phi) and the major complex in IIT 3.0 is computationally prohibitive beyond roughly 10 nodes because it requires evaluating all possible partitions within nested combinatorial optimizations. To bypass this, the paper proposes a graph neural network (GNN) using transformer convolutions with multi-head attention that learns the input-output mapping from system structure to Phi and major-complex membership directly from exact IIT 3.0 solutions, rather than modeling the IIT computation itself. The GNN is trained on small random systems (N = 5, 6, 7) whose exact solutions are obtained with the PyPhi library, in both a non-extrapolative setting (train and test on mixed N = 5,6,7) and an extrapolative setting (train on N = 5,6, test on N = 7). In the non-extrapolative setting the model achieves a correlation of 0.7446 between estimated and true Phi and a node-wise major-complex classification accuracy of 0.8574, outperforming standard GraphConv/GAT convolutions. The model then scales to much larger systems (N up to 100), where it cannot estimate Phi values accurately but preserves the qualitative topology-dependent trends (tree-like, fully connected, loop-containing) seen in exact small-N computations. Applied to a 100-node split-brain-like system of two weakly coupled 50-node subsystems, the model shows local integration at near-zero inter-subsystem coupling that gives way to global integration as coupling probability p_e increases. The author frames this as a practical, IIT 4.0-compatible approach for qualitative analysis of integrated information in large systems.

## Key facts it relies on
- The architecture uses four consecutive transformer convolutional layers (multi-head attention, 4 heads): 1st conv 50 output channels, 2nd and 3rd conv 150 output channels, then a final one-head transformer convolution with 50 output channels; batch normalization, ReLU, and dropout (drop rate 0.3) follow each of the first three layers. The network then splits into two branches: Branch 1 does global max pooling -> dropout -> fully connected -> linear activation to output Phi; Branch 2 subtracts the global max-pooled vector r from each node feature, then dropout -> fully connected -> softmax for binary "included"/"not included" major-complex classification.
- Each node has a 6-dimensional feature vector: (1) max{p_i(1|S), p_i(-1|S)}, (2) parameter T (shared across nodes), (3) node degree, (4) closeness centrality, (5) betweenness centrality, (6) clustering coefficient; edge features are a single dimension equal to edge weight J_ij. The node state S_i is deliberately NOT used as a feature, to preserve theoretical invariance under state inversion (p(S*|S) = p(-S*|-S)).
- Random systems: nodes take states +1/-1; undirected edges added with probability p = 0.4; edge weights J_ij drawn from a standard normal distribution; next-state conditional probability follows a Boltzmann distribution p_i(s|S) = 1/(1+exp(-2*tau_i*s/T)) with tau_i = sum over neighbors of J_ij*S_j; sharpness parameter T sampled uniformly from [0.1, 3.0] per system. Exact Phi and major complex computed with the PyPhi library (Mayner et al.).
- Non-extrapolative experiment 1: dataset of 3000 graphs (1000 each for N = 5, 6, 7), shuffled, 90% train / 10% test, averaged over 100 repetitions. Proposed method: Phi MSE 0.4611, Phi correlation 0.7446, node-wise major-complex accuracy 0.8574, graph-wise accuracy 0.5779 (graph-wise exceeds the value expected from raising node-wise accuracy to the power 5, 6, or 7).
- Extrapolative experiment 2 (train N = 5,6 on 1500 graphs total, test on 1000 graphs of N = 7, averaged over 100 trials): proposed method Phi MSE 0.8543, Phi correlation 0.6815, node-wise accuracy 0.8229, graph-wise accuracy 0.4686; the model tends to underestimate Phi in the high-value range not covered by training.
- Substituting transformer convolution with GraphConv or GAT degrades performance substantially (e.g., non-extrapolative graph-wise accuracy drops to 0.4650 for GraphConv and 0.4168 for GAT vs 0.5779 proposed). The LION optimizer gives a clear efficiency advantage (average convergence 94.2 epochs vs 166.2 for Adam, 185.4 for RAdam, 160.8 for AdamW) with no significant accuracy loss.
- Training settings: optimizer LION, learning rate 0.0001, mini-batch size 128; total loss = MSE for Phi + 5x cross-entropy for major-complex classification (weighting factor of five); penalty factor 1.8 applied to label "out" to address class imbalance; data augmentation adds disconnected-subsystem instances amounting to 5% of training data; k-means oversampling into seven bins; early stopping after 50 epochs of no validation improvement.
- Computational efficiency: training on 3000 graphs (N = 5,6) completed in 2-3 minutes; inference of Phi and major complex for 1000 graphs of N = 7 took under 2 seconds total, whereas exact IIT 3.0 computation for a single N = 7 graph required more than 30 minutes on average; the cut-one approximation reduced computation by less than 10% on average.
- Scaling analysis used three topologies (tree-like with N-1 edges, fully connected, loop-containing with ~40% of fully-connected edges), 10 random instances per N-topology pair, exact for N up to 7 (or up to 10 for tree-like). With 100 GNN models ensembled (node included if >=60% of models predict inclusion), qualitative trends were preserved for N = 10,20,...,100: tree-like keep low Phi and small major complexes; fully connected and loop-containing show Phi increasing with N and major complexes spanning most/all nodes, though estimated Phi values are lower than exact-implied values.
- Split-brain-like system: 100 nodes split into two 50-node subsystems (intra-subsystem edge probabilities 0.6 and 0.4), with inter-subsystem edge probability p_e from 0 to 0.4, 50 test systems per p_e. At p_e = 0 the major complex is the first 50 nodes (local integration, ratio 0.5); as p_e rises to ~0.01-0.02 local integration disappears rapidly; the major-complex ratio eventually reaches ~0.93 and estimated Phi remains roughly constant for small p_e (p_e <~ 0.02) then rises, reflecting a transition toward global integration.

## Critical notes from the literature
- The author states the method cannot accurately estimate Phi values for large N; it is useful only for comparing systems or identifying topology-dependent trends qualitatively, and Phi is underestimated in the high-value range beyond the training distribution (confirmed in both the extrapolative experiment and large-N scaling, where fully connected and loop-containing estimates fall below exact-implied values).
- The multi-task approach yielded only limited improvement over single-task models; the author acknowledges the model does not fully exploit the theoretical relationship between integrated information and the major complex, and calls this a key challenge for future work.
- The author explicitly reports that the learned attention patterns showed no general or consistent correspondence to information integration as defined in IIT (Fig 4 visualization), cautioning against over-interpreting the attention weights as mechanistically meaningful.
- The approach is purely data-driven imitation of input-output IIT solutions and does not model the nested optimization of IIT 3.0; the author notes further validation across different datasets and scenarios is required, and the split-brain system (100 nodes) is far smaller than an actual brain.
- Per-node uneven distribution of Phi values (most systems have Phi below 1) limits accuracy in the higher-Phi regions; oversampling did not sufficiently reproduce diverse graph/feature characteristics in sparse regions, so a more balanced set of real samples is suggested for robustness.

## Key topics covered
- Integrated information theory (IIT) 3.0; integrated information Phi; major complex; minimum information partition; mechanism-level integrated information (small phi)
- Computational intractability of exact IIT; PyPhi library; cut-one approximation
- Graph neural networks; transformer convolution; multi-head attention; message passing; Weisfeiler-Lehman expressiveness; GraphConv; graph attention networks (GAT); Graph Isomorphism Network
- Multi-task learning; global max pooling; max-pooled-vector subtraction for major-complex classification; isomorphism invariance; state-inversion invariance
- Node features (centrality measures, Boltzmann transition probability, parameter T); edge weights; random Boltzmann-dynamics systems
- LION optimizer vs Adam/RAdam/AdamW; data augmentation; k-means oversampling; class-imbalance penalty; early stopping
- Non-extrapolative vs extrapolative evaluation; scaling behavior across tree-like, fully connected, and loop-containing topologies; ensemble prediction for large N
- Split-brain scenario; local vs global integration; inter-subsystem connectivity p_e
- IIT 4.0 compatibility; relations and heterogeneous graphs; contrastive learning; connectome-level brain networks as future testbeds
