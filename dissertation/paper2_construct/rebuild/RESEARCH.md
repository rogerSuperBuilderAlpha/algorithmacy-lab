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

---

# Stage 1b — alternative-measures comparison (the "why Φ, not X" gap, now filled)

Follow-up run wf_6da1f4bc-a7a. 25 primary sources, 25 claims verified (23 confirmed, 2 killed).
**Verdict: among the assessed measures, NONE dominates Φ on the load-bearing task** — correctly
calling a strongly-connected-yet-reducible structure *reducible*. Φ (MIP-irreducibility) is
effectively unique in doing so, firmly established against the closest competitor and by the
connectivity argument; honest gaps remain on a few measures (below).

## What the MIP step buys (the load-bearing operation)
- Φ=0 iff the cause-effect structure factors over *some* partition (the MIP makes the least
  difference). This is a within-scale partition-minimization — distinct from any connectivity or
  coarse-graining test. Unanimous across IIT 3.0/4.0 + PyPhi sources.
- **A canonical citable instance of the hard case:** PyPhi's Rule 110 "magic cut" — a fully
  connected 3-node automaton whose ABC component has φ=0 "because knowing two elements are OFF is
  enough to know the third must also be OFF." Conditional dependence makes a strongly-connected
  component reducible. This independently corroborates our exhibit with an IIT-native example, and
  is a clean teaching case for the paper.

## The alternatives, on the hard case
- **Effective Information / causal emergence (Hoel, Albantakis & Tononi 2013; Comolatti & Hoel)** —
  the closest IIT-lineage competitor, and it **provably OVER-CALLS** the hard case. EI is
  partition-free: EI = log₂(n)·[determinism − degeneracy], no partition term; causal emergence is a
  cross-scale (macro-vs-micro) coarse-graining comparison, not a same-scale factorization test. Since
  Φ in IIT is EI evaluated *at the MIP*, standalone EI is "EI minus the MIP step that detects
  factorizability." A strongly-connected, deterministic, low-degeneracy structure registers high EI
  regardless of whether it factors. So EI behaves like the cheap connectivity test and is NOT a
  substitute. (This is the single strongest verified result of the follow-up.)
- **Network modularity / community detection** — by the connectivity argument (feed-forward Φ=0;
  Rule 110), any structural proxy keyed on edge presence detects only the disconnected/sparse case
  and over-calls strongly-connected-reducible structures. Not a substitute. (Medium confidence — by
  entailment, not a modularity-specific source.)
- **Cost is moot at N=3.** Exact Φ is exponential O(n⁵·3ⁿ), but at n=3 (W,S,C) it is trivially cheap
  in absolute terms. The cost objection only bites at scale, so no "cheaper measure" gains anything
  on the paper's actual 3-party problem. This neutralizes the cost-based case for substitution.

## Honest gaps (carry as limitations or address by computation in the draft)
- **The Φ-family alternatives draw the SAME line.** Geometric Φ (Oizumi, Tsuchiya & Amari 2016), Φ*
  (Barrett & Seth 2011), stochastic interaction (Ay 2015) are *partition-based* irreducibility
  measures (unlike EI). They were NOT verified against the hard case here, but conceptually they draw
  the same MIP-style reducible/irreducible line. So choosing IIT-4.0 Φ over geometric Φ is a
  WITHIN-FAMILY pragmatic choice (canonical, exact, PyPhi-implemented), NOT a "wrong kind of measure"
  substitution that would flip dyad/triad verdicts. State this honestly — it is a strength, not a
  weakness: the verdict is robust across the partition-minimizing family.
- **PID / Integrated Information Decomposition (ΦID) synergy** (Williams & Beer 2010; Mediano, Rosas
  et al.) is the one genuinely open competitor and the most likely reviewer-proposed substitute. Not
  verified whether synergy performs a MIP-equivalent partition-minimization or merely correlates with
  Φ>0 and over-calls the hard case. **Decision for the draft:** either compute a synergy measure on
  the exhibit and report whether it over-calls (the strongest move), or flag it as the one open
  comparison and a limitation.
- **Simon's near-decomposability** and Granger/transfer-entropy were not adjudicated by primary
  sources; their verdicts rest on conceptual argument. Near-decomposability keys on interaction
  strength / block structure, so it most likely over-calls a strongly-connected uniform-strength
  structure that factors under a MIP — but flag as conceptual.

## Net for "why Φ"
The argument the paper makes: (1) cheap connectivity/CI tests catch the disconnected dyad for free
but over-call the hard case; (2) the closest cross-family alternative, EI/causal emergence, provably
over-calls it too; (3) cost is not an issue at N=3; (4) the partition-minimizing family (geometric Φ,
Φ*) draws the same line, so the verdict is robust and the IIT-4.0 Φ choice is pragmatic; (5) the one
open competitor (PID synergy) is addressed by computation or flagged. The load-bearing demonstration
is the exhibit (strongly-connected-yet-reducible), now backed by both the prior computation and the
Rule 110 magic-cut.

## Added verified sources
- Albantakis et al. (2023) IIT 4.0; Mayner et al. (2018) PyPhi (both above).
- Hoel, Albantakis & Tononi (2013), *PNAS* 110 — quantifying causal emergence / effective information.
- Comolatti & Hoel (2022/2025) — EI as generic causal strength, distinct from irreducibility.
- PyPhi docs, Rule 110 "magic cut" example (strongly-connected-yet-reducible, canonical instance).
- Oizumi, Tsuchiya & Amari (2016), *PNAS* 113 — geometric Φ (Φ-family alternative).
- Barrett & Seth (2011), *PLOS Comp Biol* — Φ* / practical integrated-information measures.
