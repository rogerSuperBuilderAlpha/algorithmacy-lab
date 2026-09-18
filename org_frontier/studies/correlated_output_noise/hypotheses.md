# correlated_output_noise — hypotheses (fixed before computing)

**Question (agenda #5).** Does true correlated output noise — a
state-by-state TPM the state-by-node form cannot express — change the
verdict, where a static shared input did not (#61)?

**Already known (cited, not reopened).**
- Probe #61: static shared exogenous input N that both parties read
  leaves major complex {W,S,C} at Φ=2.0; N stays out. Modeling flag:
  true correlated *output* noise needs a non-factorable SBS TPM.
- `commit_noise_phase/` (#6 SMOOTH_DECAY): hub-column flip-noise —
  monotone Φ; verdict flips only at p=0.5.
- `party_vs_mediator_noise/` (#7 SAME_THRESHOLD_DIFF_CURVE):
  single-party vs mediator flip-noise share p*=0.5; locus shapes Φ /
  n_core. Pointers only for #6–#11 otherwise.
- Estimation / construct / omit / ladder closed.

**Honest noise model (fixed).** Clean form: conjunctive mediated triad
n=3, labels (W, S, C), rules W′=S, S′=W∧C, C′=S (clean Φ_MIP=2.0).

**Correlated SBS (shared-coin party flip).** From each present state,
with probability 1−p emit the clean next state; with probability p flip
*both* party outputs together (W′ and C′ XOR 1; S′ stays clean). Joint
P(W′,C′∣x) is not a product for p∈(0,0.5] — the TPM is not
conditionally independent and has no faithful state-by-node form.

**What exact IIT-4.0 Φ can see.** IIT-4.0 / PyPhi assume conditional
independence of units given the present (Albantakis et al. 2023).
`Network` converts any SBS input to multidimensional state-by-node,
silently projecting away non-CI structure. The CI projection of this
shared-coin model is exactly independent flip-noise of rate p on
columns (W, C) — the joint-party SBN construction. Exact Φ is therefore
reported on that projection, with the non-CI residual and
projection≡indep identity recorded as instrument witnesses. Candid N:
one designed n=3 form; one shared-coin parameterization; grid
p=0.00…0.50 step 0.01.

**Baselines at the same form.**
1. Independent dual-party SBN flip (cols W,C) — must match the
   projection.
2. Single-party and mediator SBN flip — node-noise baselines (#6/#7).
3. Probe #61 `no_shock` / `shared_shock` / `shock_in_commit` — static
   shared input (whole-system + major-complex reading).

**Measures.** Non-CI residual max|SBS − roundtrip(SBS)|; projection
identity max|SBN_proj − SBN_indep_WC|; Φ_MIP, structure, n_core on the
CI projection vs p.

## H1 — correlated SBS flips the verdict where node noise / #61 did not

On the CI projection that exact Φ evaluates, there exists an interior
p* ∈ (0, 0.5) at which the structure flips to dyadic — a verdict change
#61's static shared input did not produce, and that state-by-node
mediator / single-party / dual-party flip-noise do not produce below
p=0.5.

Null: no interior dyadic flip; first dyadic only at p=0.5 (or never),
matching the node-noise / #61 “no verdict change” reading.

## H2 — same smooth decay as node-flip

On the CI projection: Φ is monotone non-increasing (tol 1e-6); no
single grid step carries ≥ **25%** of total fall Φ(0)−Φ(0.5); verdict
stays triadic for all p < 0.5 and is dyadic only at p=0.5 — the same
SMOOTH_DECAY template as #6 hub noise and #7 dual-party SBN noise.
Additionally, max|Φ_proj(p) − Φ_indep_WC(p)| < 1e-9 on the full grid
(projection identity on the Φ curve).

Null: monotonicity fails, a ≥25% interior step appears, an interior
verdict flip appears, or Φ_proj diverges from Φ_indep_WC.

## H3 — core shift without verdict flip

On the CI projection, some interior p ∈ (0, 0.5) has n_core ≠ 3 while
structure stays triadic — a core membership change without a verdict
flip, distinguishing the projection from #61's fixed n_core=3 at Φ=2.

Null: n_core=3 at every interior p with triadic structure (core stable
through the smooth decay).

**Primary verdict word.**
- H1 → `VERDICT_FLIP`
- else H2 and not H3 → `NO_EXTRA_EFFECT`
- else H3 and not H1 → `CORE_SHIFT_NO_FLIP`
- else → `CORRELATED_MIXED`

Instrument gate (required before scoring): at every tested p>0 the SBS
is not CI (residual > 1e-9); at every p the projection equals
independent dual-party SBN (max abs diff < 1e-9); p=0 recovers clean
triadic Φ=2.0; #61 `shared_shock` major complex stays {W,S,C} Φ=2.0.
