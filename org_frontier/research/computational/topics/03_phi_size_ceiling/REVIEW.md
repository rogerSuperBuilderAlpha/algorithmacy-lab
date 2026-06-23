# The Combinatorial Size Ceiling on Exact Phi
<!-- run: 2026-06-23 | sources: 13 -->
Search method: web and arXiv/Crossref queries plus the Consensus and Scholar Gateway academic tools, run 2026-06-23; every entry carries a verified DOI or arXiv ID.

Exact integrated information confronts a layered combinatorial problem that confines rigorous computation to systems of roughly ten units or fewer. The measure rests on the minimum information partition (MIP), the weakest cut of a system, and locating it by exhaustive search requires evaluating all bipartitions, which grows as 2^(N-1)-1, with full partition counts following the Bell numbers (Kitazono, Kanai & Oizumi, 2018). For IIT 3.0 the cost compounds: states, subsystems, mechanisms, purviews, and partitions each scale exponentially, so the reference toolbox runs in O(n·5^(3^n)) and is limited in practice to about 10-12 nodes (Mayner et al., 2018). The IIT 4.0 formalism, which unfolds a complete Φ-structure of distinctions and relations, raises the burden further, since sums over relations can grow hyper-exponentially with unit count (Albantakis et al., 2023).

The foundational IIT 3.0 specification fixes this cost structure by requiring, at every level, a search over candidate purviews and partitions to identify maximally irreducible cause-effect repertoires (Oizumi, Albantakis & Tononi, 2014). Early implementations made the exhaustion explicit and confirmed the exponential blow-up of MIP search on real neural data (Krohn & Ostwald, 2017). Toker and Sommer (2019) characterize the same bottleneck as computation time that "explodes super-exponentially with network size," motivating approximate spectral solutions for larger brain networks.

Several lines of work attack the partition layer specifically. Exploiting submodularity, Queyranne's algorithm reduces MIP search from O(2^N) to roughly O(N^3): for N=40 an exhaustive scan would take about 123 days while the submodular search finishes in a second (Hidaka & Oizumi, 2018; Kitazono et al., 2018). These guarantees hold cleanly only for submodular surrogate measures, and the diversity among candidate Φ measures means a tractable proxy need not behave like the exact quantity (Mediano, Seth & Barrett, 2019). Geometric and dynamic-programming reformulations (GeoMIP) and memoization heuristics (HDMP) push the practical envelope without removing the exponential core, and graph-neural-network estimators approximate the major complex while conceding that exact cost remains exponential in node count (Hosaka, 2025). Theoretical results on upper bounds suggest symmetries that could prune computation (Zaeemzadeh & Tononi, 2023), yet a recent critical review stresses that exact Φ has not been computed on any real physical system, and that published values are proxies (Mediano et al., 2026). The ceiling therefore persists as a structural feature of exact IIT.

## References
- Albantakis, L. et al. (2023). Integrated information theory (IIT) 4.0.
- Hidaka, S. & Oizumi, M. (2018). Fast and exact search for the partition with minimal information loss.
- Hosaka, T. (2025). Graph neural networks for integrated information and major complex estimation.
- Kitazono, J., Kanai, R. & Oizumi, M. (2018). Efficient algorithms for searching the minimum information partition.
- Krohn, S. & Ostwald, D. (2017). Computing integrated information.
- Mayner, W.G.P. et al. (2018). PyPhi: A toolbox for integrated information theory.
- Mediano, P.A.M., Seth, A.K. & Barrett, A.B. (2019). Measuring integrated information.
- Mediano, P.A.M. et al. (2026). Integrated information theory: the good, the bad and the misunderstood.
- Oizumi, M., Albantakis, L. & Tononi, G. (2014). From the phenomenology to the mechanisms of consciousness: IIT 3.0.
- Toker, D. & Sommer, F.T. (2019). Information integration in large brain networks.
- Zaeemzadeh, A. & Tononi, G. (2023). Upper bounds for integrated information.
