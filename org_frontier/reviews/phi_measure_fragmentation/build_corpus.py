"""Build the corpus for the phi_measure_fragmentation review.

The corpus is assembled from the academic semantic-search connectors (Scholar Gateway and Consensus)
over the measure vocabulary — "measures of integrated information", "practical approximations to
integrated information", "integrated information decomposition / synergy", "causal emergence measure",
"neural complexity integration / segregation", "total correlation / multi-information" — and screened
against the boundary rule: the source's central object is a quantitative measure of integrated
information, integration, complexity, or synergy (its definition, computation, approximation,
comparison, or critique). Pure applications that use a fixed off-the-shelf measure without engaging the
measure itself, pure statistical dependence coefficients (Pearson, MIC), quantum-correlation measures,
and ML representation-learning uses are out of boundary and were dropped in screening.

Each record carries a stable slug, the verbatim title, a short abstract sufficient for coding, the
year, and a DOI where one is confidently known (else null; harvest resolves those by title). Writes:

  literature/corpus.jsonl   — one screened in-boundary source per line {slug,title,abstract,year,doi}
  seeds.json                — [{slug, doi}] or [{slug, title}] for lib/harvest.py

    python -m org_frontier.reviews.phi_measure_fragmentation.build_corpus

Standard library only. No model tokens. Deterministic.
"""

import json
import os
import re

HERE = os.path.dirname(__file__)

# (title, year, doi_or_None, abstract). doi only where the canonical value is confidently known;
# otherwise None and harvest resolves the seed by title.
CORPUS = [
    # --- origin / exact IIT phi and practical proxies ---
    ("Measuring information integration", 2003, "10.1186/1471-2202-4-31",
     "The capacity to integrate information, Phi, is given by the minimum amount of effective "
     "information that can be exchanged between two complementary parts of a subset; it is used to "
     "identify the complexes of a neural system and is applied to idealized neural architectures."),
    ("Integrated Information in Discrete Dynamical Systems: Motivation and Theoretical Framework", 2008,
     "10.1371/journal.pcbi.1000091",
     "Introduces a time- and state-dependent measure of integrated information, phi, capturing the "
     "causal states available to a system as a whole above and beyond its parts, and analyzes it on "
     "discrete networks and Hopfield attractors."),
    ("A measure for brain complexity: relating functional segregation and integration in the nervous "
     "system", 1994, "10.1073/pnas.91.11.5033",
     "Introduces neural complexity (CN), a measure capturing the interplay between functional "
     "segregation and integration, obtained from the average deviation from statistical independence "
     "for subsets of increasing size, demonstrated in cortical simulations."),
    ("Characterising the complexity of neuronal interactions", 1995, None,
     "Applies the Tononi-Sporns-Edelman neural complexity measure to real neurophysiological "
     "processes, expressing complexity via the profile of entropies of different-sized regions and "
     "relating it to the average mutual information between regions and the whole."),
    ("Connectivity and complexity: the relationship between neuroanatomy and brain dynamics", 2000, None,
     "Uses the neural complexity measure to quantify how a pattern of functional connectivity combines "
     "functional segregation and integration, finding specific neuroanatomical motifs uniquely "
     "associated with high complexity in cortical models."),
    ("Neural complexity and structural connectivity", 2009, None,
     "Develops a Gaussian approximation of the Tononi neural complexity measure that is computationally "
     "cheap and scales polynomially, elucidating the relationship between a neural system's complexity "
     "and its structural connectivity."),
    ("Neural complexity: a graph theoretic interpretation", 2011, None,
     "Derives an approximation of the Tononi-Sporns-Edelman neural complexity measure in terms of "
     "graph motifs and the moments of a weight distribution, establishing how neural complexity depends "
     "on network topology such as cyclic motifs."),
    ("Practical Measures of Integrated Information for Time-Series Data", 2011,
     "10.1371/journal.pcbi.1001052",
     "Describes two new measures, Phi_E and Phi_AR, that overcome the limitations of discrete-Markov "
     "phi and are easy to apply to time-series data, demonstrated in simulations."),
    ("Measuring Integrated Information from the Decoding Perspective", 2016,
     "10.1371/journal.pcbi.1004654",
     "Derives the practical measure Phi* using mismatched decoding from information theory, shows other "
     "practical measures fail the required lower and upper bounds, and gives an analytical Gaussian "
     "expression applicable to experimental data."),
    ("Improved Measures of Integrated Information", 2016, "10.1371/journal.pcbi.1005123",
     "Presents a taxonomy of Phi-measures characterized by choice of factorization, distributions, and "
     "comparison measure, requiring attractive properties to reduce hundreds of options to a handful, "
     "and derives exact and approximate formulas for real data."),
    ("A Principled Infotheoretic phi-like Measure", 2014, None,
     "Pinpoints three concerns about phi purely as a measure of irreducibility and proposes a revised "
     "measure psi, grounded in Partial Information Decomposition and faster to compute than phi."),
    ("A Compression-Complexity Measure of Integrated Information", 2016, None,
     "Proposes Phi^C, a measure of integrated information from a lossless-compression complexity "
     "perspective, that is well bounded and faster to compute, and shows in simulations it has similar "
     "hierarchy to phi across networks."),
    ("Simulation Study of Two Measures of Integrated Information", 2017, None,
     "Measures the compression-complexity Phi^C on simulated neuronal-motif and random networks and "
     "compares it against Tononi's integrated information phi, highlighting where the two measures "
     "diverge in how they capture integration."),
    ("Estimating the Integrated Information Measure Phi from High-Density Electroencephalography during "
     "States of Consciousness in Humans", 2018, None,
     "Introduces a practical method to estimate an approximation of Phi from 128-channel EEG and relates "
     "it to EEG connectivity across anesthetic states, finding the approximation alone insufficient but "
     "useful in a multi-dimensional parameter space."),
    ("Evaluating Approximations and Heuristic Measures of Integrated Information", 2019,
     "10.3390/e21050525",
     "Tests whether several proposed heuristic measures and computational approximations correlate with "
     "exact phi on simulated 3-6 node binary networks where the ground truth can be established, finding "
     "some approximate phi closely and others predict only low-phi systems."),
    ("Integrated Information, a Complexity Measure for optimal partitions", 2023, None,
     "Calculates analytically the geometric integrated information index phi_G and its maximum over "
     "partitions for Ising-spin systems using the information-geometry formulation of integrated "
     "information theory."),
    ("Unified framework for information integration based on information geometry", 2015, None,
     "Proposes a measure of integrated information derived from information geometry, interpreted as the "
     "divergence between a system's actual distribution and one where causal influences are "
     "disconnected, unifying mutual information, transfer entropy, and stochastic interaction."),
    ("Optimizing Integrated Information with a Prior Guided Random Search Algorithm", 2022, None,
     "Provides a random-search algorithm to optimize the IIT measure Phi computed from a transition "
     "probability matrix, investigating the structure of graphs with higher Phi as node count grows."),
    ("The Phi measure of integrated information is not well-defined for general physical systems", 2019,
     None,
     "Argues that the measure Phi of integrated information, in its current formulation, fails to be "
     "well-defined for general physical systems, presenting three ways it is ambiguous or ill-defined."),
    ("Integrated information theory: the good, the bad and the misunderstood", 2026, None,
     "Reviews integrated information theory and argues that a high value of the measure Phi is not "
     "synonymous with more consciousness, that Phi is not well-defined for real physical systems, and "
     "that only proxies for IIT measures have so far been computed."),
    ("Integrated information as a metric for group interaction", 2017, "10.1371/journal.pone.0188049",
     "Applies the integrated information measure phi as a metric for group interaction, computing it on "
     "work groups, Wikipedia editor groups, and Internet communication as a measure of interactional "
     "complexity that sometimes predicts group performance."),

    # --- integrated information decomposition / PID / synergy ---
    ("Nonnegative Decomposition of Multivariate Information", 2010, None,
     "Reconsiders from first principles the information a set of sources provides about a variable, "
     "defines redundancy as a minimum over sources, and proposes the partial information decomposition "
     "into nonnegative redundant, unique, and synergistic atoms over a redundancy lattice."),
    ("Measuring multivariate redundant information with pointwise common change in surprisal", 2016,
     None,
     "Presents a new redundancy measure (Iccs) based on the common change in surprisal shared between "
     "variables at the pointwise level, used within the partial information decomposition to split "
     "multivariate mutual information into redundant, unique, and synergistic contributions."),
    ("The Partial Entropy Decomposition: Decomposing multivariate entropy and mutual information via "
     "pointwise common surprisal", 2017, None,
     "Applies the partial information decomposition formalism to multivariate entropy with a pointwise "
     "common-surprisal redundancy measure, revealing dyadic versus triadic generative structure "
     "invisible to classical Shannon measures."),
    ("Pointwise Partial Information Decomposition Using the Specificity and Ambiguity Lattices", 2018,
     None,
     "Derives a partial information decomposition by applying the redundancy lattice separately to the "
     "specificity and ambiguity components of pointwise mutual information, defining measures of "
     "redundant specificity and ambiguity that recombine into a multivariate decomposition."),
    ("A Novel Approach to the Partial Information Decomposition", 2019, None,
     "Proposes a general framework for multivariate PID defined by an analogy with set-theoretic "
     "intersection and union plus an informativeness ordering, and defines a PID via the Blackwell "
     "order with an operational interpretation."),
    ("Synergy and Redundancy in Dual Decompositions of Mutual Information Gain and Information Loss",
     2016, None,
     "Extends the Williams-Beer information-gain lattice, introduces dual information-loss lattices with "
     "reversed roles of redundancy and synergy, and proposes procedures to construct multivariate "
     "decompositions from measures of synergy or unique information."),
    ("Exact Partial Information Decompositions for Gaussian Systems Based on Dependency Constraints",
     2018, None,
     "Derives closed-form partial information decompositions (I_dep) for univariate and multivariate "
     "Gaussian systems using maximum-entropy models under marginal dependency constraints, comparing "
     "against the minimum-mutual-information decomposition."),
    ("Introducing a differentiable measure of pointwise shared information", 2021, None,
     "Presents a partial-information-decomposition redundancy measure that is differentiable with "
     "respect to the probability mass function, emerges from information-theoretic principles, and has "
     "the form of a local mutual information with an operational interpretation."),
    ("Invariant Components of Synergy, Redundancy, and Unique Information among Three Variables", 2017,
     None,
     "Extends the partial information decomposition to describe trivariate dependencies without a "
     "target/source split, revealing seven nonnegative invariant subatoms and splitting redundancy into "
     "source and non-source components."),
    ("Generalized decomposition of multivariate information", 2023, None,
     "Introduces a generalized information decomposition based on the Kullback-Leibler divergence that "
     "relaxes the source/target distinction, decomposing total correlation, negentropy, and mutual "
     "information, and relating synergistic information to Tononi-Sporns-Edelman complexity."),
    ("Decomposing past and future: Integrated information decomposition based on shared probability "
     "mass exclusions", 2022, None,
     "Proposes an integrated information decomposition measure of temporal dependency based on local "
     "probability-mass exclusions, applied to spiking activity from cortical cultures to resolve modes "
     "of information storage, transfer, and modification."),
    ("A Measure of Synergy Based on Union Information", 2024, None,
     "Introduces a new measure of union information from a communication-channel perspective, from which "
     "a synergy measure stems, and critically reviews existing characterizations of union information "
     "and synergy in the partial information decomposition literature."),
    ("Gaussian Partial Information Decomposition: Bias Correction and Application to High-dimensional "
     "Data", 2023, None,
     "Proposes an efficient method for computing a partial information decomposition on multivariate "
     "Gaussians that recovers the ground truth in canonical examples at high dimensionality, and "
     "introduces a finite-sample bias correction, applied to mouse-brain recordings."),
    ("Multivariate Partial Information Decomposition: Constructions, Inconsistencies, and Alternative "
     "Measures", 2025, None,
     "Provides closed-form two-source PID atoms satisfying the axioms, proves an impossibility theorem "
     "that no lattice-based decomposition is consistent for more than three sources, and presents "
     "alternative multivariate unique and synergistic information measures validated on the Ising "
     "model."),
    ("Decomposing Multivariate Information Rates in Networks of Random Processes", 2025, None,
     "Extends the partial information decomposition to random processes with temporal correlations "
     "(partial information rate decomposition), decomposing shared dynamic information into unique, "
     "redundant, and synergistic contributions, validated on Gaussian benchmarks and physiological "
     "networks."),
    ("Non-Negative Decomposition of Multivariate Information: From Minimum to Blackwell-Specific "
     "Information", 2024, None,
     "Proposes a non-negative partial information decomposition satisfying an inclusion-exclusion "
     "relation for any f-information measure, constructed from a pointwise Blackwell-order perspective "
     "and proven to satisfy the desired axioms."),
    ("A Partial Information Decomposition for Multivariate Gaussian Systems Based on Information "
     "Geometry", 2024, None,
     "Extends an information-geometry partial information decomposition to multivariate Gaussian systems "
     "with vector inputs and outputs, deriving explicit expressions and proving non-negativity, "
     "symmetry, and monotonicity, compared against other Gaussian decompositions."),
    ("Partial Information Decomposition via Deficiency for Multivariate Gaussians", 2021, None,
     "Shows that closed-form Gaussian PID does not extend to vector messages in general and proposes a "
     "convex-optimization framework, based on statistical deficiency, to approximately compute a "
     "bivariate PID for high-dimensional multivariate Gaussians."),
    ("Towards an extended taxonomy of information dynamics via Integrated Information Decomposition",
     2021, None,
     "Combines Information Decomposition and Integrated Information into Integrated Information "
     "Decomposition (PhiID), a framework to quantify higher-order dynamical interactions and express "
     "measures of information transfer and dynamical complexity as aggregates of information modes."),
    ("Beyond integrated information: A taxonomy of information dynamics phenomena", 2019, None,
     "Combines partial information decomposition and integrated information into Integrated Information "
     "Decomposition (PhiID), revealing that what is typically called integration is an aggregate of "
     "heterogeneous phenomena and formulating new tailored measures of integrated information."),
    ("Evolving higher-order synergies reveals a trade-off between stability and information integration "
     "capacity in complex systems", 2024, None,
     "Evolves Boolean networks with high synergy, redundancy, or Tononi-Sporns-Edelman complexity and "
     "measures their capacity to integrate information, finding high-synergy systems chaotic with high "
     "integration capacity and TSE-complex systems balancing the trade-off."),

    # --- causal emergence / effective information ---
    ("Quantifying causal emergence shows that macro can beat micro", 2013, "10.1073/pnas.1314922110",
     "Uses effective information (EI), which depends on the effectiveness of a system's mechanisms and "
     "its state-space size, to show that for certain causal architectures EI peaks at a macro level, "
     "yielding genuine causal emergence."),
    ("Can the macro beat the micro? Integrated information across spatiotemporal scales", 2016, None,
     "Goes beyond effective information to a measure Phi_Max satisfying composition, state-dependency, "
     "integration, and exclusion, and evaluates it at micro and macro levels of simplified neuronal "
     "systems, showing integrated information can peak at a macro scale."),
    ("When the Map Is Better Than the Territory", 2016, None,
     "Grounds causal emergence in Shannon's channel capacity, arguing systems have a causal capacity "
     "that different macroscale descriptions exploit to varying degrees via error-correcting-code-like "
     "principles, so a macroscale can be more informative than the microscale."),
    ("The Emergence of Informative Higher Scales in Complex Networks", 2019, None,
     "Derives effective information for networks from first principles, shows how grouping nodes into "
     "macronodes can increase a network's effective information (causal emergence), and finds "
     "informative higher scales common across simulated and real networks."),
    ("Uncertainty and causal emergence in complex networks", 2019, None,
     "Derives effective information as a measure of the uncertainty in paths along a network and shows "
     "that grouping nodes into macronodes can increase effective information, a phenomenon of causal "
     "emergence common across biological, social, and technological networks."),
    ("Reconciling emergences: An information-theoretic approach to identify causal emergence in "
     "multivariate data", 2020, "10.1371/journal.pcbi.1008289",
     "Introduces a formal theory of causal emergence in multivariate systems giving a quantitative "
     "definition of downward causation and causal decoupling, with practical criteria efficiently "
     "computable in large systems and illustrated on the Game of Life and neural data."),
    ("Emergence as the conversion of information: a unifying theory", 2021, None,
     "Provides an umbrella framework for emergence based on information conversion, using partial "
     "information decomposition to show that coarse-graining can convert mutual information into "
     "synergistic information, so synergy can increase at macroscales."),
    ("Causal emergence is widespread across measures of causation", 2022, None,
     "Examines over a dozen independently developed measures of causation and shows all exhibit causal "
     "emergence, proving they are based on a small set of causal primitives, so macroscale causation is "
     "not a quirk of effective information or integrated information."),
    ("Consilience in Causation: Causal Emergence Is Found Across Measures of Causation", 2025, None,
     "Shows a high degree of consilience among a dozen measures of causation reducible to causal "
     "primitives of sufficiency and necessity (or determinism and degeneracy), demonstrating that "
     "causal emergence is commonly found across all measures analyzed."),
    ("Emergence and Causality in Complex Systems: A Survey of Causal Emergence and Related Quantitative "
     "Studies", 2024, None,
     "Reviews quantitative theories and applications of causal emergence, focusing on quantifying it and "
     "identifying it from data, and emphasizing effective information as the central measure of causal "
     "emergence."),
    ("Dynamical reversibility and a new theory of causal emergence based on SVD", 2024, None,
     "Introduces approximate dynamical reversibility from the singular value decomposition of a Markov "
     "chain as a new causal-emergence framework independent of coarse-graining, establishing an "
     "equivalence with effective-information maximization on Boolean networks and cellular automata."),
    ("Finding emergence in data by maximizing effective information", 2023, None,
     "Introduces a machine-learning framework that learns macro-dynamics in a latent space by "
     "maximizing effective information and quantifies the degree of causal emergence, validated on "
     "simulated and fMRI data."),
    ("Causal Geometry", 2020, None,
     "Introduces causal geometry, a geometric version of effective information formalizing how model "
     "parameters can be intervened upon, showing that a coarse-grained model can carry more information "
     "when it better matches the scale of accessible interventions (causal emergence)."),
    ("Causal Emergence 2.0: Quantifying emergent complexity", 2025, None,
     "Introduces a new theory of emergence treating a system's scales as slices of a higher-dimensional "
     "object, apportioning the causal contribution of each scale and defining a new measure of emergent "
     "complexity as how widely a system's causal workings are distributed across scales."),
    ("Causal emergence from effective information: Neither causal nor emergent?", 2021, None,
     "Introduces the effective-information measure of causal emergence and assesses whether it is "
     "genuinely causal or emergent, arguing it supports only an epistemic form of causal emergence."),
    ("An Exact Theory of Causal Emergence for Linear Stochastic Iteration Systems", 2024, None,
     "Introduces an exact theoretic framework for causal emergence in linear stochastic iteration "
     "systems with continuous state spaces and Gaussian noise, deriving an analytical expression for "
     "effective information and optimal coarse-graining strategies."),
    ("A Law of Emergence: Maximum Causal Power at the Mesoscale", 2025, None,
     "Defines a system's causal power at a spatial scale via effective information and proves a "
     "middle-scale peak theorem that effective information is maximized at a mesoscopic scale, with "
     "evidence from an Ising model and agent-based collective behavior."),

    # --- total correlation / multi-information as integration measures ---
    ("Measuring Dependence with Matrix-based Entropy Functional", 2021, None,
     "Proposes matrix-based normalized total correlation and dual total correlation to quantify the "
     "dependence of multiple variables without estimating the underlying distributions, shown to be "
     "differentiable and statistically more powerful than prevalent measures."),
    ("Maximizing Multivariate Information With Error-Correcting Codes", 2018, None,
     "Shows that total correlation and dual total correlation admit a spectrum of measures with varying "
     "sensitivity to intermediate orders of dependence, relating them to error-correcting codes and "
     "deriving the class of global maximizers."),
    ("Functional connectivity via total correlation: Analytical results in visual areas", 2022, None,
     "Presents analytical results proving advantages of multivariate total correlation over mutual "
     "information as a measure of functional connectivity in early-vision neural networks, and uses the "
     "analytical setting to check empirical total-correlation estimators."),
    ("Total/dual correlation/coherence, redundancy/synergy, complexity, and O-information for real and "
     "complex valued multivariate data", 2025, None,
     "Presents Gaussian equations for total correlation, dual total correlation, O-information, "
     "Tononi-Sporns-Edelman complexity, and a redundancy-synergy index, and generalizes them to "
     "structured groups of variables and to the contribution of individual connections."),
    ("Estimating Total Correlation with Mutual Information Estimators", 2020, None,
     "Introduces a framework to estimate total correlation, a measure of statistical dependency among "
     "multiple variables, with sample-based mutual information estimators by decomposing it into mutual "
     "information terms, with consistency analysis and experiments."),
    ("Estimating Total Correlation with Mutual Information Bounds", 2020, None,
     "Introduces sample-based variational total-correlation estimators by connecting total correlation "
     "to mutual information and decomposing it into mutual information terms, evaluated in simulation "
     "against true total-correlation values."),

    # --- clustering / balance measures in the integration lineage ---
    ("The Effect of Electroencephalogram (EEG) Reference Choice on Information-Theoretic Measures of "
     "the Complexity and Integration of EEG Signals", 2017, None,
     "Studies two information-theoretic measures of functional brain segregation and integration, "
     "interaction complexity CI(X) and integration I(X), applied to EEG, and how choice of reference "
     "affects them, with dipole-source validation of the scalp-level estimates."),
    ("Regions, systems, and the brain: Hierarchical measures of functional integration in fMRI", 2008,
     None,
     "Shows that the information-theoretic measure integration, derived from mutual information, can be "
     "applied hierarchically to quantify functional interactions between compound brain systems, "
     "applied to glioma-patient fMRI to detect lesional reorganization."),
    ("Measuring the dynamic balance of integration and segregation underlying consciousness, "
     "anesthesia, and sleep in humans", 2024, None,
     "Proposes an fMRI-based metric, the integration-segregation difference (ISD), capturing network "
     "efficiency and clustering, used to quantify brain-state transitions across anesthesia and sleep "
     "and to differentiate conscious from unconscious states."),
]


def slugify(title, year, taken):
    base = re.sub(r"[^a-z0-9]+", "", (title or "").lower())[:24] or "src"
    slug = f"{base}{year or ''}"
    n, out = 1, slug
    while out in taken:
        n += 1
        out = f"{slug}_{n}"
    taken.add(out)
    return out


def main():
    taken = set()
    recs = []
    for title, year, doi, ab in CORPUS:
        title = re.sub(r"\s+", " ", title).strip()
        recs.append({"slug": slugify(title, year, taken), "title": title,
                     "abstract": ab, "year": year, "doi": doi})
    recs.sort(key=lambda r: (r["year"], r["title"]))

    os.makedirs(os.path.join(HERE, "literature"), exist_ok=True)
    with open(os.path.join(HERE, "literature", "corpus.jsonl"), "w") as fh:
        for r in recs:
            fh.write(json.dumps(r) + "\n")
    seeds = [{"slug": r["slug"], "doi": r["doi"]} if r["doi"]
             else {"slug": r["slug"], "title": r["title"]} for r in recs]
    json.dump(seeds, open(os.path.join(HERE, "seeds.json"), "w"), indent=1)
    with_doi = sum(1 for r in recs if r["doi"])
    print(f"corpus: {len(recs)} in-boundary sources  |  with DOI: {with_doi}  |  "
          f"title-resolved seeds: {len(recs) - with_doi}")
    print(f"wrote literature/corpus.jsonl, seeds.json ({len(seeds)})")


if __name__ == "__main__":
    main()
