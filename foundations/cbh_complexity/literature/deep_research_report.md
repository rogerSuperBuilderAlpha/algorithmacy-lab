# Deep-research report: literature for the Complex Brain Hypothesis instantiation

Output of the deep-research harness (run wf_0f9c41db-3e6, 111 agents, 28 sources fetched, top claims
adversarially verified 2/3). Synthesised for the `cbh_complexity` project. OA = open access.

## Bottom line (the open gap, verified)

The Complex Brain Hypothesis (Mago et al. 2026) is a **purely theoretical/conceptual** proposal. No
surveyed source, including the CBH paper itself, computationally instantiates it on exactly-computable
systems (Ising, small Boolean/Markov networks) with exact, side-by-side entropy, TSE neural complexity,
Aaronson apparent complexity, and **exact IIT Φ**. The entropy-vs-complexity dissociation has not been
demonstrated on exactly-computable systems with exact Φ. **Caveat:** a companion whole-brain modelling
paper exists — Vohryzek et al. (2025), *Whole-Brain Models of Minimal Phenomenal Experience: Approaching
Criticality through Jhana Meditation* (bioRxiv 2025.09.25.678574) — but it works on fitted whole-brain
models, not exactly-computable systems with exact Φ, so it does not close the gap. Our contribution (the
exact-systems instantiation) is therefore novel, but it must position itself relative to Vohryzek et al.

## Verified findings

1. **CBH (Mago et al. 2026, arXiv:2605.16146, OA).** Richness is better indexed by complexity than
   entropy; complexity is grain/scale-dependent (fine-grained → rich HCPE; coarse-grained → contentless
   MPE); both regimes show elevated entropy but diverge in complexity and perturbational signature.
2. **The open gap (above).** High confidence; the CBH frames "MPEs as a test case for computational
   theories," signalling the computation is future work.
3. **Entropic Brain Hypothesis (Carhart-Harris et al. 2014, Front. Hum. Neurosci. 8:20, OA; revisited
   2018, Neuropharmacology 142:167–178).** Quality of a conscious state is a function of the entropy of
   spontaneous brain activity, within bounds; psychedelics = high-entropy "primary states."
4. **Empirical signal-diversity rises in psychedelics.** Schartner et al. 2017 (Sci Rep 7:46421, OA):
   spontaneous MEG signal diversity (LZc, coalition entropy) reliably higher under psilocybin, ketamine,
   LSD than waking rest, even controlling for spectral power. Tagliazucchi et al. 2014 (Hum Brain Mapp
   35(11):5442–56, OA): wider repertoire of dynamical connectivity states under psilocybin.
5. **TSE neural complexity (Tononi, Sporns & Edelman 1994, PNAS 91:5033–5037, OA).** Average deviation
   from statistical independence over subset sizes; HIGH only when segregation and integration coexist,
   LOW at both extremes (fully independent / high-entropy → low; fully dependent → low relative to the
   peak). Formal dissociation of complexity from entropy — the conceptual core of the CBH. *Our exact
   computation refines this: the fully-dependent (ordered redundant) extreme is $(N-1)/2$, below the peak
   but not near zero, so $C_N$ does not cleanly mark the ordered state as low-richness.*
6. **Perturbational Complexity Index (Casali et al. 2013, Sci Transl Med 5:198ra105; validated Casarotto
   et al. 2016).** TMS perturbation + Lempel-Ziv compression of the source-space response = a complexity
   (integration + differentiation) index, not raw entropy; discriminates graded conscious level across
   wakefulness, sleep, sedation, and disorders of consciousness.
7. **Complexity tracks conscious LEVEL.** Schartner et al. 2015 (PLOS ONE 10:e0133532, OA): LZc/ACE/SCE
   fall under propofol (single threshold separates wakeful rest from LOC). Schartner et al. 2017
   (Neurosci. Conscious. 2017(1):niw022, OA): the same measures fall in NREM sleep.
8. **The cleanest empirical wedge — Farnes et al. 2020 (PLOS ONE 15:e0242056, OA).** Under sub-anaesthetic
   ketamine, spontaneous EEG diversity (LZc, ACE, SCE) increased significantly, but TMS-evoked PCI did
   *not* differ from normal wakefulness. The authors read this as PCI/integration indexing the brain's
   *capacity* to sustain consciousness, while spontaneous diversity indexes the complexity of conscious
   *content*. This is the real-brain analogue of our entropy-vs-Φ dissociation: a diversity measure and a
   complexity/integration measure come apart in the same state.

## How this informs the paper

- **Positioning:** cite Vohryzek et al. (2025) as the companion whole-brain effort and state precisely
  what we add (exactness + IIT Φ on small systems), preserving the novelty claim honestly.
- **Empirical grounding (§2.1, §5.3):** Farnes 2020 is the empirical dissociation our toy systems model;
  Schartner 2017 and Tagliazucchi 2014 are the EBH evidence; Schartner 2015/2017 and Casali 2013 show
  complexity tracking conscious level. These replace the previous hand-waving with a real evidence base.
- **TSE nuance (§5.2):** the literature's "low at both extremes" is qualitative; our exact $(N-1)/2$
  value sharpens it and supports the claim that $C_N$ does not cleanly separate the ordered low-richness
  state.
