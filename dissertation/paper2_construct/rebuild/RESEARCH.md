# Paper 2 — Stage 1 research synthesis (fact-checked, neutral)

Deep-research run wf_f9001618-95a. 29 primary sources fetched, 123 claims extracted, 25
adversarially verified (25 confirmed, 0 killed), 10 load-bearing findings. The brief was neutral:
test whether Φ/IIT is the right instrument, do not assume it. **Verdict: qualified yes — the
borrowing is defensible, but the strongest objection survives and Φ must earn its keep on a specific
residual class of cases (which the prior exhibit already targets).**

## The borrowing is a disciplined, established mode — under explicit standards
- Organization theory routinely imports formal models from other fields; the methods literature sets
  a clear bar (Whetten, Felin & King 2009, *J. Management* 35(3); Oswick, Fleming & Hanlon 2011, *AMR*
  36(2); Ketokivi, Mantere & Cornelissen 2017, *AMR* 42(4)). The single most applicable standard
  (Ketokivi et al.): an analogy may *express* an idea or *do explanatory-argumentative work*; when it
  reasons, **it must be critically evaluated AS an argument**, not invoked as evocative ornament.
  Oswick: one-way borrowing should be disciplined by **disanalogy and counterfactual** reasoning.
- Canonical exemplars: Hannan & Freeman (1977, *AJS* 82) imported population biology via an **explicit
  analogy-mapping step** AND an explicit warning against literal application ("A literal application…
  may miss a phenomenon of central interest"). Rivkin (2000, *Mgmt Sci* 46(6)) imported Kauffman's NK
  landscape, parametrizing complexity as elements + interactions.
- **Watch the wording:** H&F say "analogue," not "homology." Org ecology is functional **analogy**, not
  homology (shared causal origin). Paper 2 must say analogy, not homology — a reviewer will catch it.

## Φ measures exactly the right thing, and is separable from consciousness
- IIT 4.0 (Albantakis et al. 2023, *PLOS Comp Biol*; arXiv:2212.14787): φ "measures how much the
  partition reduces the probability with which a system specifies its cause-effect state," evaluated
  over the **minimum-information partition (MIP)**. φ_s = 0 **iff** the system is reducible. Definitional
  match to the moderated-dyad (reducible) / mediated-triad (irreducible) construct.
- The consciousness identity is a **postulate layered on top** of the measure ("experience is identical
  to the cause-effect structure…"; big Φ = "quantity of consciousness"). The measure is genuinely
  separable. BUT two consequences for Paper 2:
  1. Detaching the measure means the paper **cannot lean on IIT's authority** to justify the measure's
     *organizational* meaning. Construct validity must be **re-earned independently**.
  2. The exclusion/maximization machinery (φ*, finding the maximal substrate) and the axioms are
     **surplus** to a binary reducible/irreducible classifier. Use the MIP irreducibility measure; drop
     the rest.
- The IIT critiques (the 2023 "pseudoscience" letter; unfalsifiability) target the **theory**, not the
  **measure**. Paper 2's disavowal of the consciousness claim is well-founded.

## The strongest objection (survives verification, sourced from the IIT authors themselves)
- **A cheaper test detects the reducible/dyad case for free.** Mayner et al. (2018, PyPhi, *PLOS Comp
  Biol*; arXiv:1712.09644): "if the subsystem is not strongly connected then Φ is necessarily zero"
  (a unidirectional cut removing no edges leaves the structure unchanged). So **connectivity is a
  SUFFICIENT detector of reducibility, but not necessary** — not-strongly-connected ⟹ Φ=0, but
  strongly-connected does NOT imply Φ>0.
- **Consequence (the whole game):** a connectivity / conditional-independence / factorization test
  handles the easy reducible cases for free. Φ's added value, IF ANY, lives only on
  **strongly-connected structures where the cheap test is silent** but the form still reduces. Paper 2
  must show its hard triad/dyad cases live in that residual zone, or the borrowing is ornamental.
- **This is precisely what the prior exhibit does** (`W′=NOR(S,C), S′=¬W∧C, C′=NAND(W,S)`: all six
  edges, strongly connected, no constants, yet exact Φ=0 at every reachable state — every
  connectivity/CI test calls it triadic; the MIP machinery reduces it). The research independently
  confirms the exhibit is the right battleground and the load-bearing "why Φ" answer. Re-derive it,
  feature it, and frame the whole "why Φ" argument around the strongly-connected-yet-reducible zone.

## Honest limits / the three weakest links a methods reviewer attacks first
1. **Cheaper sufficient tests** (above) — answered only by the exhibit, on the residual class.
2. **Exponential exact Φ:** O(n^5·3^n), ~10–12 nodes max; exhaustive MIP search exponential (drops to
   polynomial via Queyranne's algorithm when Φ is submodular). At **N=3 (W,S,C) the bound is
   non-binding** — make this explicit as the escape hatch.
3. **Markov / conditional-independence validity:** PyPhi is "only meaningfully valid for systems that
   are Markovian and satisfy conditional independence," and the authors warn TPMs from **observed time
   series are NOT guaranteed** to satisfy this — "should be carefully checked." For Paper 2 the formal
   instrument builds the TPM from the **specified application-layer mechanism** (Boolean update
   functions), so Markov/CI hold **by construction**; the hazard binds the **empirical extension**
   (inferring a TPM from real interaction logs → Paper 3), where the check is a precondition, not
   optional. State this division cleanly.

## State-individuation = the entire empirical commitment
Φ is not invariant to how the application-layer states are carved. The individuation rule must be
**pre-registered** before any computation, with sensitivity analysis. This is the measurement-
dependence problem and the place a methods reviewer will press hardest after the cheap-test objection.

## Open questions the research did NOT close (carry into outline/draft)
1. **The alternative-measures comparison is unfilled.** None of Φ*, geometric Φ (Oizumi), stochastic
   interaction (Ay), causal emergence / effective information (Hoel, Albantakis), partial information
   decomposition (Williams & Beer), Granger/transfer-entropy, or Simon's near-decomposability survived
   as a confirmed claim. The "why Φ, not a cheaper measure" question cannot be answered *conclusively*
   until the strongest substitute is named and shown not to dominate Φ on cost. **Decision needed:**
   a focused follow-up research pass on the alternatives, or scope the comparator to the two a reviewer
   actually proposes (connectivity-separability + conditional-independence/factorization), which the
   prior `phi_vs_separability.py` / `dynamical_comparator.py` already implement.
2. **ORM-specific construct-validity standards** for a formal instrument not validated against outcomes
   (operationalization-as-contribution) — uncited; the methods-venue bar needs filling.
3. **Precedents for building valid TPMs from application-layer interaction logs** (beyond the PyPhi
   Markov warning) — unconfirmed. Christin's "Algorithms at Work" (in sources) covers opacity in
   algorithmic management.

## Key verified sources
- Whetten, Felin & King (2009), *J. Management* 35(3):537–563. https://journals.sagepub.com/doi/10.1177/0149206308330556
- Oswick, Fleming & Hanlon (2011), *AMR* 36(2):318–337. https://journals.aom.org/doi/10.5465/amr.2009.0155
- Ketokivi, Mantere & Cornelissen (2017), *AMR* 42(4):637–658. https://journals.aom.org/doi/10.5465/amr.2015.0322
- Hannan & Freeman (1977), *AJS* 82:929–964.
- Rivkin (2000), *Mgmt Sci* 46(6):824–844. https://pubsonline.informs.org/doi/10.1287/mnsc.46.6.824.11940
- Albantakis et al. (2023), *PLOS Comp Biol* (IIT 4.0); arXiv:2212.14787.
- Mayner et al. (2018), PyPhi, *PLOS Comp Biol*; arXiv:1712.09644.
- Kitazono, Kanai & Oizumi (2018), *Entropy* 20(3):173 (MIP search / Queyranne).
- Christin, "Algorithms at Work" (opacity in algorithmic management).

*Citations to be re-verified against Crossref before any enter the draft bibliography.*
