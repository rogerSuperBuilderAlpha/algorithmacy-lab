"""Assemble the causal-emergence corpus from the ToolSearch results.

Curated union of on-topic Scholar Gateway + Consensus hits, screened against the boundary rule in
methods.md. Off-topic hits (molecular-dynamics coarse-graining, generic time-series causal discovery,
systems medicine) are dropped. Writes literature/corpus.jsonl, seeds.json, literature/references.bib.

Abstracts for the Scholar-sourced supplement are pulled from the parsed scholar_recs.json (real
abstracts + DOIs). CE-core / philosophy entries carry abstracts transcribed from the Consensus tool
results. DOIs are set only where verified; otherwise null and the seed harvests by title.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = "/private/tmp/claude-501/-Users-ludwitt-iit-playground-pyphi-experiments-dissertation/b841b09d-f057-4d42-a757-2878fe2fee4c/scratchpad/scholar_recs.json"

# --- Scholar supplement: (slug, doi) -> abstract+title+year pulled from scholar_recs.json ---
scholar = {r["doi"]: r for r in json.load(open(SCRATCH)) if r.get("doi")}

# entries: slug, title, year, doi (None if unverified), abstract, is_preprint, venue
E = []
def add(slug, title, year, doi, abstract, venue="", preprint=False):
    E.append(dict(slug=slug, title=title, year=year, doi=doi,
                  abstract=abstract.strip(), venue=venue, preprint=preprint))

def add_scholar(slug, doi, venue=""):
    r = scholar[doi]
    add(slug, r["title"], r["year"], doi, r["abstract"], venue)

# ===== Causal-emergence information-theoretic core (Hoel lineage + measure development) =====
add("hoel2013macrobeatmicro", "Quantifying causal emergence shows that macro can beat micro", 2013,
    "10.1073/pnas.1314922110",
    "It is widely assumed that, once a micro level is fixed, macro levels are fixed too (supervenience), and that only the micro level is causally complete. Using a measure, effective information (EI), that depends on both the effectiveness of a system's mechanisms and the size of its state space, we measure EI at micro and macro levels in simple systems whose micro mechanisms are fixed. For certain causal architectures EI can peak at a macro level, when coarse-grained macro mechanisms are more deterministic and/or less degenerate than the underlying micro mechanisms to an extent that overcomes the smaller state space. Thus the macro can supersede the micro causally, leading to genuine causal emergence.",
    "PNAS")
add("hoel2017mapterritory", "When the Map Is Better Than the Territory", 2016,
    "10.3390/e19050188",
    "The causal structure of a system can be analyzed at multiple scales. Recent research applying information theory to causal analysis shows the causal structure of some systems comes into focus and is more informative at a macroscale: a macroscale description (a map) can be more informative than a fully detailed microscale description (the territory), called causal emergence. This paper grounds the phenomenon in Shannon's channel capacity, arguing systems have a causal capacity that different descriptions use to various degrees, via the same mathematical principles as error-correcting codes. For some systems only macroscale descriptions use the full causal capacity.",
    "Entropy")
add("hoel2016macromicroIIT", "Can the macro beat the micro? Integrated information across spatiotemporal scales", 2016,
    "10.1093/nc/niw012",
    "Beyond effective information we consider additional requirements of a proper measure of causal power from the intrinsic perspective of a system: composition, state-dependency, integration (causal irreducibility of the whole to its parts), and exclusion. A measure satisfying these, Phi-max, was developed in integrated information theory. Evaluating Phi-max at micro and macro levels in simplified neuronal-like systems, we show that for systems with indeterminism and/or degeneracy Phi can peak at a macro level, when coarse-graining micro elements produces macro mechanisms with high irreducible causal selectivity. Macro causal emergence and micro causal exclusion hold when causal power is assessed in full from the intrinsic perspective.",
    "Neuroscience of Consciousness")
add("comolatti2022widespread", "Causal emergence is widespread across measures of causation", 2022,
    None,
    "Causal emergence is the theory that macroscales can reduce the noise in causal relationships, leading to stronger causes at the macroscale. First identified using effective information and later integrated information, it has been analyzed in real data across the sciences. Is it a quirk of these measures? We examined over a dozen popular measures of causation from philosophy, statistics, psychology, and genetics; all showed cases of causal emergence, because measures of causation are based on a small set of related causal primitives. This consilience shows macroscale causation is a general fact about causal relationships, scientifically detectable, and not a quirk of any particular measure.",
    "arXiv", True)
add("comolatti2025consilience", "Consilience in Causation: Causal Emergence Is Found Across Measures of Causation", 2025,
    None,
    "We examine over a dozen popular measures of causation from different fields and identify a high degree of consilience: measures are often very similar or rediscovered, because they are based on a small set of related causal primitives (sufficiency and necessity, or determinism and degeneracy). Using a simple model system we demonstrate how the consilience of causation guarantees that causal emergence is commonly found across causal measures, identifying instances across all measures analyzed. This sets the mathematical understanding of emergence on firmer ground and opens the door for detecting natural scales of causal interaction.",
    "Entropy")
add("hoel2025ce2", "Causal Emergence 2.0: Quantifying emergent complexity", 2025,
    None,
    "There is debate about what the macroscales of systems can add beyond mere compression. Here a new theory of emergence is introduced wherein different scales of a system are treated like slices of a higher-dimensional object. The theory distinguishes which scales possess unique causal contributions and which are not causally relevant. Constructed from an axiomatic notion of causation, it is applied in coarse-grains of Markov chains, identifying all cases of macroscale causation: instances where reduction to a microscale is possible yet lossy about causation. It posits a causal apportioning schema and a novel measure of emergent complexity.",
    "arXiv", True)
add("yuan2024survey", "Emergence and Causality in Complex Systems: A Survey of Causal Emergence and Related Quantitative Studies", 2024,
    "10.3390/e26020108",
    "Emergence and causality are two fundamental concepts for understanding complex systems, and they are interconnected. Causal emergence (CE) theory aims to bridge these two concepts and employs measures of causality to quantify emergence. This paper provides a comprehensive review of recent advancements in quantitative theories and applications of CE, focusing on two challenges: quantifying CE and identifying it from data. The latter requires integrating machine learning and neural network techniques, linking causal emergence and machine learning, with effective information (EI) as the central measure. It surveys applications and future perspectives.",
    "Entropy")
add("yang2023findingemergence", "Finding emergence in data by maximizing effective information", 2023,
    None,
    "Quantifying emergence and modeling emergent dynamics data-drivenly for complex dynamical systems is challenging because emergent behaviors cannot be directly captured by micro-level observational data. Inspired by causal emergence theory, this paper introduces a machine learning framework to learn macro-dynamics in an emergent latent space and quantify the degree of CE by maximizing effective information. On simulated and real data it quantifies degrees of CE and reveals influences of noise types. It learns a one-dimensional coarse-grained macro-state from fMRI data representing complex neural activities during movie-clip viewing.",
    "National Science Review")
add("zhang2022nis", "Neural Information Squeezer for Causal Emergence", 2022,
    None,
    "Stronger causality can be obtained at the macro-level than the micro-level of the same Markovian dynamical systems if an appropriate coarse-graining strategy is applied. Identifying this emergent causality from data is difficult because the appropriate strategy is hard to find. This paper proposes a machine learning framework, Neural Information Squeezer, to automatically extract the effective coarse-graining strategy and macro-level dynamics and identify causal emergence directly from time-series data, using an invertible neural network to decompose any coarse-graining into information conversion and information discarding. It extracts coarse-graining functions and dynamics on different levels and identifies CE on several example systems.",
    "Entropy")
add("zhang2024svdreversibility", "Dynamical reversibility and a new theory of causal emergence based on SVD", 2024,
    None,
    "The theory of causal emergence with effective information posits that complex systems can exhibit CE where macro-dynamics show stronger causal effects than micro-dynamics; a key challenge is dependence on the coarse-graining method. We introduce approximate dynamical reversibility from the singular value decomposition of the Markov chain and establish a framework for CE based on it. CE lies in redundancy: irreversible and correlated information pathways within the Markov dynamics. CE is quantified as the potential maximal efficiency increase for dynamical reversibility. We show a strong correlation between reversibility and EI, establishing equivalence between SVD and EI-maximization frameworks, independent of coarse-graining technique.",
    "npj Complexity")
add("liu2024exactlinear", "An Exact Theory of Causal Emergence for Linear Stochastic Iteration Systems", 2024,
    None,
    "After coarse-graining a complex system, the macro-state dynamics may exhibit more pronounced causal effects than the micro-state, known as causal emergence, quantified by effective information. Two challenges are the absence of frameworks in continuous stochastic dynamical systems and reliance on coarse-graining. We introduce an exact theoretic framework for CE within linear stochastic iteration systems with continuous state spaces and Gaussian noise, derive an analytical expression for EI, and identify optimal linear coarse-graining strategies maximizing CE. Maximal CE and optimal coarse-graining are determined by the principal eigenvalues and eigenvectors of the dynamic system's parameter matrix.",
    "Entropy")
add("liu2025svdgaussian", "Singular-value-decomposition-based causal emergence for Gaussian iterative systems", 2025,
    None,
    "Causal emergence based on effective information demonstrates that macrostates can exhibit stronger causal effects than microstates. Identification of CE and maximization of EI rely on coarse-graining strategies, a key challenge. A recently proposed CE framework based on approximate dynamical reversibility using SVD is independent of coarse-graining but limited to discrete-state transition matrices. This article proposes a CE quantification framework for Gaussian iterative systems based on approximate dynamical reversibility from the SVD of inverse covariance matrices in forward and backward dynamics, applicable to any continuous-state Gaussian-noise dynamical system.",
    "Physical Review E")
add("chvykov2020causalgeometry", "Causal Geometry", 2020,
    None,
    "Information geometry studies the efficacy of scientific models by quantifying the impact of model parameters on predicted effects. Here we introduce causal geometry, formalizing how outcomes are impacted by parameters and how parameters can be intervened upon, and a geometric version of effective information. We show it is given by the matching between the space of effects and the space of interventions. This is a consequence of causal emergence, wherein macroscopic causal relationships may carry more information than fundamental microscopic ones; a coarse-grained model may be more informative than the microscopic one, especially when it better matches the scale of accessible interventions.",
    "Entropy")
add("chen2025mesoscalelaw", "A Law of Emergence: Maximum Causal Power at the Mesoscale", 2025,
    None,
    "Complex systems universally exhibit emergence, but a predictive law has been absent. We define a system's causal power at spatial scale l as its effective information EI_l, measured by mutual information between a maximum-entropy intervention and its outcome, and prove a Middle-Scale Peak Theorem: for a broad class of systems with local interactions, EI_l is not monotonic but exhibits a strict maximum at a mesoscopic scale, a necessary consequence of a trade-off between noise-averaging at small scales and locality-limited response at large scales. We provide reproducible evidence in a 2D Ising model near criticality and agent-based collective behavior.",
    "arXiv", True)
add("luo2025emcausal", "Emergence-Inspired Multi-Granularity Causal Learning", 2025,
    None,
    "Existing causal learning algorithms focus on micro-level causal discovery and struggle to identify the influence of macro systems composed of micro-level variables, because macro causal relationships are mediated through micro-level interactions. We propose the Emergence-inspired Multi-granularity Causal learning (EMCausal) method, introducing a progressive mapping encoder to simulate aggregation of micro variables into macro representations and a causal consistency constraint to reconstruct micro variables from macro representations, learning a multi-granular causal structure. It identifies causal graphs under the influence of causal emergence on synthetic and real datasets.",
    "unknown")
add("rosas2020reconciling", "Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data", 2020,
    "10.1371/journal.pcbi.1008289",
    "Few quantitative theories of what constitutes emergent phenomena have been proposed. This article introduces a formal theory of causal emergence in multivariate systems, studying the relationship between the dynamics of parts of a system and macroscopic features of interest. It provides a quantitative definition of downward causation and introduces a complementary modality, causal decoupling. The theory yields practical criteria efficiently calculable in large systems. It is illustrated on Conway's Game of Life, Reynolds' flocking model, and neural activity measured by electrocorticography.",
    "PLoS Computational Biology")
add("mediano2021greaterthanparts", "Greater than the parts: a review of the information decomposition approach to causal emergence", 2021,
    None,
    "The study of emergence has suffered from a lack of formalisms. Here we summarize, elaborate, and extend a formal theory of causal emergence based on information decomposition, quantifiable and amenable to empirical testing. The theory relates emergence with information about a system's temporal evolution that cannot be obtained from the parts of the system separately. The article provides an accessible but rigorous introduction, discussing merits in various scenarios and addressing interpretation issues and potential misunderstandings.",
    "Philosophical Transactions A")
add("mcsharry2024learningemergent", "Learning diverse causally emergent representations from time series data", 2024,
    None,
    "Cognitive processes take place at a macroscopic scale in systems with emergent properties. Recent proposals provide information-theoretic metrics to detect emergence in time series, but identifying relevant macroscopic variables a priori is non-trivial. We put forward a data-driven method using representation learning and differentiable information estimators to find variables with emergent properties, successfully detecting emergent variables and recovering ground-truth emergence values in synthetic data, extending to multiple independent features. The method scales to real experimental brain-activity datasets, uncovering the emergent structure of cognitive representations.",
    "NeurIPS")

# ===== Deflationary / critique of causal-emergence measures =====
add_scholar("dewhurst2021neither", "10.1002/tht3.489", "Thought")
add("dewhurst2020realpatterns", "Causal Emergence and Real Patterns", 2020,
    None,
    "Erik Hoel and colleagues propose a model of causal emergence based on an information-theoretic measure of causation, effective information: certain complex systems are structured so that an intervention at the macro-level is more informative than at the micro-level. I assess the extent to which this is genuinely causal and/or emergent, and argue that its interventionist approach to causation supports only an epistemic form of emergence. The best way to make sense of the proposal is via Ladyman and Ross's information-theoretic gloss on Dennettian real patterns, clarifying the sense in which emergence can be both causal and epistemic.",
    "unknown")
add("eberhardt2022distortions", "Causal Emergence: When Distortions in a Map Obscure the Territory", 2022,
    "10.3390/philosophies7020030",
    "We provide a critical assessment of the account of causal emergence in Erik Hoel's When the map is better than the territory. We show that the causal macro variables implied by the account result in interventions with significant ambiguity, and that the operations of marginalization and abstraction do not commute; both are desiderata any account of multi-scale causal analysis should respect. The problems derive from averaging steps and the introduction of a maximum-entropy distribution extraneous to the system under investigation.",
    "Philosophies")

# ===== Dynamical-systems accounts of emergent macro-variables =====
add("barnett2021dynamicalindependence", "Dynamical independence: Discovering emergent macroscopic processes in complex dynamical systems", 2021,
    None,
    "We introduce a notion of emergence for macroscopic variables associated with highly multivariate microscopic dynamical processes. Dynamical independence instantiates the intuition of an emergent macroscopic process as one possessing the characteristics of a dynamical system in its own right, with its own dynamical laws distinct from those of the underlying microscopic dynamics. We quantify departure from dynamical independence by a transformation-invariant Shannon-information-based measure of dynamical dependence, emphasizing data-driven discovery of dynamically independent macroscopic variables, with application to neural systems from neurophysiological time series.",
    "Physical Review E")
add("milinkovic2024emergentneural", "Capturing the emergent dynamical structure in biophysical neural models", 2024,
    None,
    "Complex neural systems can display structured emergent dynamics. Using information theory, we apply Dynamical Independence to uncover emergent dynamical structure in a minimal 5-node biophysical neural model shaped by integration and segregation. DI defines a dimensionally-reduced macroscopic variable as emergent to the extent it behaves as an independent dynamical process, distinct from micro-level dynamics, measured by minimizing transfer entropy from micro to macro variables. The degree of emergence is minimized at balanced points of integration and segregation and maximized at the extremes.",
    "PLoS Computational Biology")
add("schulman2001coarsegrains", "Coarse Grains: The Emergence of Space and Order", 2001,
    None,
    "The emergence of macroscopic variables can be effected through coarse graining. Despite practical and fundamental benefits, the apparently subjective nature of selecting coarse grains has been considered problematic. We provide objective selection methods deriving from the existence of relatively slow dynamical time scales, and show the emergence of both spatial variables and order parameters within a framework for nonequilibrium statistical mechanics. Although significant objective criteria are introduced, we do not provide a unique prescription: the grains, and by implication entropy, are defined only modulo a characteristic time scale of observation.",
    "Foundations of Physics")
add("morita2023finegrained", "A fine-grained distinction of coarse graining", 2023,
    None,
    "This paper distinguishes two main types of coarse graining and reveals the relationship between coarse graining and emergence. In physics some forms of coarse graining seem indispensable to show a physical property, while others merely change our descriptions. Investigating the renormalization group method, irreversibility, and the rigid body in classical mechanics, the case studies reveal a distinction between substantial and mere coarse-graining, clarifying the relationships between coarse graining and emergence and providing implications for the issues about emergence.",
    "European Journal for Philosophy of Science")
add_scholar("gongjing2014renormalizationca", "10.1002/cplx.21557", "Complexity")

# ===== Downward / top-down causation: philosophy of the reality question =====
add("emmeche2000levels", "Levels, Emergence and Three Versions of Downward Causation", 2000,
    None,
    "The idea of a higher-level phenomenon having a downward causal influence on a lower-level process has taken various forms. Based on ontological theses about inter-level relations, types of causation, and the possibility of reduction, three versions of downward causation are distinguished. The strong form is held to conflict with contemporary science; the medium version may describe thoughts constraining neurophysiological states; the weak form is physically acceptable but may not in practice be a feasible description. All forms have specific problems, but the medium and weak versions seem most promising.",
    "unknown")
add("bitbol2012withoutfoundations", "Downward causation without foundations", 2012,
    None,
    "Emergence is interpreted in a non-dualist framework. No metaphysical distinction between higher and basic levels is supposed, only a duality of modes of access, which are construed as constitutive of the patterns of organization in Kant's sense. The emergent levels of organization and the inter-level causations are neither illusory nor ontologically real: they are objective in the sense of transcendental epistemology. This neo-Kantian approach defuses several paradoxes associated with downward causation and makes good sense of it independently of any prejudice about the existence of a hierarchy of levels of being.",
    "Synthese")
add("campbell2011physicalism", "Physicalism, Emergence and Downward Causation", 2011,
    None,
    "The development of a defensible notion of emergence has been dogged by threshold issues highlighted by Jaegwon Kim. We argue that physicalist assumptions confuse and vitiate the project: Kim's contention that emergence entails supervenience is contradicted by his own argument that microstructure belongs to the whole object, and his argument against downward causation is question-begging. We argue for rejecting the assumption that what basically exists are things; our best physics tells us there are only fields in process. We need an ontology that gives priority to organization, which is inherently relational.",
    "Axiomathes")
add("santos2014relational", "Upward and Downward Causation from a Relational-Horizontal Ontological Perspective", 2014,
    None,
    "Downward causation exercised by emergent properties of wholes upon their lower-level constituents has been accused of conceptual and metaphysical incoherence. This paper criticizes and refuses the traditional hierarchical-vertical way of conceiving both types of causation while preserving their ontological significance, and the atomistic-combinatorial view of the entities constituting the emergence base. It proposes an alternative relational ontological view with a horizontal, intra-level way of representing putative cross-level causation, arguing that Kim's causal-closure principle and overdetermination objection can be surpassed.",
    "Axiomathes")
add("zhong2020takingemergentism", "Taking Emergentism Seriously", 2020,
    None,
    "The Exclusion Argument has afflicted non-reductionists for decades. This article argues that emergentism, the view that mental entities can downwardly cause physical entities in a non-overdetermining way, is the most plausible approach to solving the exclusion problem. The emergentist approach is largely absent in contemporary philosophy of mind because it rejects the Causal Closure of Physics; the article challenges the consensus on causal closure and defends a physicalist version of emergentism, arguing competing approaches involve ad hoc postulations of mental causation.",
    "Australasian Journal of Philosophy")
add("heil2021emergencedc", "Emergence and Downward Causation", 2021,
    None,
    "Emergence and downward causation are best understood in light of one another. Downward causation would occur when a whole, which includes various parts, influences the behavior of those parts; a whole is emergent when capable of exercising downward causation, one way to distinguish weak or explanatory emergence from robust ontological emergence. The intelligibility of emergence in this sense is questioned, and proponents of emergence appear committed ill-advisedly to a corpuscularian universe. The Aristotelian picture of objects interacting could turn out to be best suited to the manifest image.",
    "Appearance in Reality")
add("wong2020withoutvertical", "Ontological Emergence Without Vertical Causation", 2020,
    None,
    "This essay addresses two related problems faced by ontological emergence and proposes a solution. It outlines the concept of emergence, the ontological/epistemological distinction, and the synchronic/diachronic distinction, focusing on synchronic ontological emergence; discusses the two related problems of configurational forces and downward causation; and presents a solution that affirms ontological emergence but denies vertical causation, addressing objections to that view.",
    "Axiomathes")
add("paoletti2017opinionated", "Downward Causation: An Opinionated Introduction", 2017,
    None,
    "This introduction presents key concepts on the prospects for downward causation in metaphysics and the philosophy of science, across three parts: downward causation and the metaphysics of causation; scientific examples of downward causation; and downward causation, mind and agency. Beside Kim's exclusion argument, philosophers of mind need to consider explanatory practices in the neurosciences, and empirical concerns about the irreducibility of downward causation. Downward causation is commonly linked to emergence: an entity acting as a downward cause is an emergent entity, and vice versa.",
    "unknown")
add("decaro2017threeviews", "Three Views on Mental Downward Causation", 2017,
    None,
    "This chapter evaluates three proposals: Anomalous Monism, Ontological Emergentism, and the Intentional Causation View. Not all forms of downward causation are Cartesian or antinaturalistic. Anomalous Monism seems to imply mental properties are causally inert, amounting to epiphenomenalism. An account based on ontological emergence and downward causation is taken as compatible with the scientific view. A way of accounting for mental downward causation is a form of causal pluralism based on causation as an intentional context-relative notion, interdependent with explanation.",
    "unknown")
add("ellis2021physicallogicalmental", "Physical, Logical, and Mental Top-Down Effects", 2021,
    None,
    "We explore the architecture of downward causation through three cases. The universe is not causally closed because of irreducible randomness at the quantum level, and contextual effects occur where higher levels modify lower-level elements by changing their context. There are important logical downward causes: abstract objects such as logical principles, numbers, algorithms and plans have measurable effects on lower levels. We sketch a model for mind-body interaction in which the levels of a human organism together enable mental top-down effects, arguing downward causation is a widespread natural phenomenon.",
    "unknown")
add("sanchezcanizares2017ellisreview", "Review of How can physics underlie the mind? Top-down causation in the human context, by G. Ellis", 2017,
    None,
    "This review of George Ellis's book on top-down causation and strong emergence in nature recognizes the plausibility of his arguments that the reductive stance is wanting for complex systems, but argues that Ellis does not unambiguously demonstrate the occurrence of downward causation in physics: many ontological claims are a non-sequitur from the premises, due to circularity or flaws in the proof. It discusses the odd kind of supervenience Ellis defends, the role of quantum indetermination and boundary conditions, and questions his fivefold classification of top-down causation.",
    "Contemporary Physics")
add_scholar("tabaczek2013formalcause", "10.1111/zygo.12012", "Zygon")
add("fornal2024topdowncompleteness", "Is Top-Down Causation Reconcilable with the Principle of the Completeness of Physics?", 2024,
    None,
    "This article examines downward causation in the context of the debate on emergence and the causal exclusion argument. It critically analyzes Stephen Yablo's proportionality argument and trope theory, highlighting their limitations in explaining mental causation, and argues that the powers-based approach, particularly in its creative and selective variants, provides the most convincing defense of downward causation, allowing real emergent properties and avoiding causal overdetermination.",
    "Philosophical Discourses")
add_scholar("navarrete2024contextualemergence", "10.1111/jtsb.12414", "Journal for the Theory of Social Behaviour")
add("brisset2016institutions", "Institutions as Emergent Phenomena: Redefining Downward Causation", 2016,
    None,
    "The concept of emergence is frequently used to characterize social institutions, though philosophy of mind argues it encompasses the dubious notion of downward causation. This work shows that although problematic in some fields, emergence is an ontological feature of the social world. Defining an institution as an exogenous device, it shows the relationship between institution and individual actions is not only causal but also intersubjective and constitutive.",
    "unknown")
add("sawyer2012emergencesociology", "Response to Emergence in Sociology", 2012,
    None,
    "This response defends nonreductive individualism and an account of downward causation against Kim's critique of Fodor by analogy. The original paper already addressed Kim's critique by drawing on philosophers of mind to make an argument for downward causation based on wild disjunction. As empirical examples of irreducible emergent group properties, the author cites studies of improvisational theater dialogues and social networks, and argues the autonomy of the social level is not distinct from the autonomy of the mental level.",
    "Philosophy of the Social Sciences")
add("murphy2008mentalcausation", "Emergence and Mental Causation", 2008,
    None,
    "This chapter deals with how emergent mental events or properties can have downward causal efficacy without violating the causal closure of the physical world. Emergence needs to be defined in terms of the denial of causal reductionism; causal antireductionism amounts to the affirmation of top-down or downward causation. Downward causation is defined in terms of the selection among lower-level causal processes on the basis of their higher-level properties: mental properties have an irreducible role, since it is only by virtue of supervenient mental properties that neural processes become subject to selective pressures.",
    "unknown")
add("leidenhag2016panpsychism", "From Emergence Theory to Panpsychism: A Philosophical Evaluation of Nancey Murphy's Non-reductive Physicalism", 2016,
    None,
    "This article critically evaluates non-reductive physicalism as defended by Nancey Murphy, arguing that the examples given do not illustrate robust emergence and the philosophical idea of downward causation; that the thesis of multiple realizability is ontologically neutral and cannot support the causal efficacy of higher-level properties; and that supervenience is incompatible with strong emergence. It also argues for a relationship between emergence theory and panpsychism regarding the origin and nature of mind.",
    "Sophia")

# ===== Ontological-emergence / critical-realism philosophy (Scholar supplement, real DOIs) =====
add_scholar("silberstein2003searchontological", "10.1111/1467-9213.00136", "Philosophical Quarterly")
add_scholar("wilson2009emergencephysics", "10.1111/j.1747-9991.2009.00239.x", "Philosophy Compass")
add_scholar("humphreys2017formulating", "10.1111/rati.12160", "Ratio")
add_scholar("gillett2014naturalpiety", "10.1111/1746-8361.12056", "Dialectica")
add_scholar("elderVass2007forEmergence", "10.1111/j.1468-5914.2007.00325.x", "Journal for the Theory of Social Behaviour")
add_scholar("elderVass2013criticalrealismprocess", "10.1111/jtsb.12017", "Journal for the Theory of Social Behaviour")
add_scholar("lawson2020cambridgeontology", "10.1111/jtsb.12251", "Journal for the Theory of Social Behaviour")
add_scholar("morgan2024realismcomplexity", "10.1111/jtsb.12409", "Journal for the Theory of Social Behaviour")
add_scholar("fryer2024contextcriticalrealism", "10.1111/jtsb.12439", "Journal for the Theory of Social Behaviour")
add_scholar("wan2011irreducibility", "10.1002/cplx.20377", "Complexity")
add_scholar("mcgivern2010almostanywhere", "10.1002/cplx.20307", "Complexity")

# ===== Statistical / interventionist causation and information-emergence measures (Scholar supplement) =====
add_scholar("hitchcock2002transitionchances", "10.1111/1468-0114.00033", "Nous")
add_scholar("baumgartner2009interdefining", "10.1111/j.1746-8361.2009.01191.x", "Dialectica")
add_scholar("fernandez2012complexityinformation", "10.1002/cplx.21424", "Complexity")
add_scholar("sole2009informationaggregation", "10.1111/j.1756-8765.2009.01047.x", "Topics in Cognitive Science")
add_scholar("squazzoni2012computationalsociology", "10.1111/jtsb.12004", "Journal for the Theory of Social Behaviour")

# ---- write corpus.jsonl ----
seen = set()
corpus = []
for e in E:
    if e["slug"] in seen:
        raise SystemExit("dup slug: " + e["slug"])
    seen.add(e["slug"])
    corpus.append({"slug": e["slug"], "title": e["title"], "abstract": e["abstract"],
                   "year": e["year"], "doi": e["doi"]})

with open(os.path.join(HERE, "literature", "corpus.jsonl"), "w") as f:
    for c in corpus:
        f.write(json.dumps(c) + "\n")

# ---- seeds.json (list for harvest) ----
seeds = [{"slug": e["slug"], **({"doi": e["doi"]} if e["doi"] else {"title": e["title"]})} for e in E]
json.dump(seeds, open(os.path.join(HERE, "seeds.json"), "w"), indent=1)

# ---- references.bib ----
def bibkey(slug):
    return slug
def esc(s):
    return s.replace("&", "\\&")
lines = ["% Causal-emergence corpus + method papers. DOIs given where verified; preprints flagged.\n"]
for e in E:
    typ = "@misc" if e["preprint"] else "@article"
    lines.append(f"{typ}{{{bibkey(e['slug'])},")
    lines.append(f"  title = {{{esc(e['title'])}}},")
    lines.append(f"  year = {{{e['year']}}},")
    if e["venue"]:
        field = "howpublished" if e["preprint"] else "journal"
        lines.append(f"  {field} = {{{esc(e['venue'])}}},")
    if e["doi"]:
        lines.append(f"  doi = {{{e['doi']}}},")
    if e["preprint"]:
        lines.append("  note = {preprint},")
    lines.append("}\n")
# method papers
lines.append("""@article{simsek2023systematicity,
  title = {Systematicity in Organizational Research Literature Reviews: A Framework and Assessment},
  author = {Simsek, Zeki and Fox, Brian C. and Heavey, Ciaran},
  journal = {Organizational Research Methods},
  volume = {26}, number = {2}, pages = {292--321}, year = {2023},
  doi = {10.1177/10944281211008652},
}

@article{simsek2022compelling,
  title = {Compelling Questions in Research: Seeing What Everybody Has Seen and Thinking What Nobody Has Thought},
  author = {Simsek, Zeki and Heavey, Ciaran and Fox, Brian C. and Yu, Tieying},
  journal = {Journal of Management}, year = {2022},
  doi = {10.1177/01492063211073068},
}
""")
open(os.path.join(HERE, "literature", "references.bib"), "w").write("\n".join(lines))

print(f"corpus: {len(corpus)} sources")
print(f"seeds: {len(seeds)} ({sum(1 for s in seeds if 'doi' in s)} by DOI, {sum(1 for s in seeds if 'title' in s)} by title)")
print(f"with abstract>80 chars: {sum(1 for c in corpus if len(c['abstract'])>80)}")
print(f"verified DOIs: {sum(1 for e in E if e['doi'])}")
