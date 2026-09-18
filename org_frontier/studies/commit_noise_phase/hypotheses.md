# commit_noise_phase — hypotheses (fixed before computing)

**Question (agenda #6).** Is there a Φ phase transition as a
probabilistic commit's noise rises, or only the smooth decay the
reliability sweeps showed (#27, #38)?

**Already known (cited, not reopened).**
- Probe #27: mediator reliability r; Φ 2.0→0, triadic until r=0.5.
- Probe #38: asymmetric counterpart read; same pattern.
- Q6 (`questions/q6_noise_phase_transition/`): fine grid on the
  mediated AND triad — smooth Φ, no susceptibility peak, verdict
  flips only at p=0.5. Estimation / construct / omit / ladder closed.

**Noise model (fixed).** Commit flip-noise on the mediator/hub column
of the state-by-node TPM:
`P(out=1) = (1−p)·clean + p·(1−clean)`. Reliability = 1−p.
p ∈ {0.00, 0.01, …, 0.50}. Noise is in the mechanism TPM (not
initial-state injection). Exact binary IIT-4.0 Φ.

**Forms (designed; candid N).**
1. **conjunctive_hub** n=3 — S′ = P1∧P2, Pi′=S (single AND hub; = #27
   mediated triad up to label order). Clean Φ=2.0.
2. **parity_hub** n=3 — S′ = P1⊕P2, Pi′=S. Clean Φ=0.5 (contrast
   family; small clean Φ).

**Measures at each p.** Φ_MIP (max over reachable), binary structure
(triadic/dyadic), n_core = |major complex|.

## H1 — sharp phase transition

There exists an interior p* ∈ (0, 0.5) where either family (a) flips
verdict to dyadic, or (b) drops Φ by ≥ **25%** of that family's total
fall Φ(0)−Φ(0.5) in a single grid step.

Null: no interior verdict flip and no such Φ step on either family.

## H2 — only smooth decay

On **both** families: Φ is monotone non-increasing (tol 1e-6); no
single step carries ≥25% of total fall; verdict stays triadic for all
p < 0.5 and is dyadic only at p=0.5.

Null: some family violates monotonicity, carries a ≥25% step, or flips
verdict interiorly.

## H3 — core / Φ decoupling (interior)

On some family, an **interior** adjacent grid step (left endpoint p < 0.5)
shows either (a) n_core changes while |ΔΦ| < **0.05·Φ(0)** (core
transition without Φ jump), or (b) |ΔΦ| ≥ **0.25·(Φ(0)−Φ(0.5))** while
n_core is unchanged (Φ jump without core change). The degenerate
endpoint step into p=0.5 is excluded — that is the verdict collapse,
not a mid-curve decoupling.

Null: no interior core/Φ decoupling of either kind.

**Primary verdict word.**
- H1 → `PHASE_TRANSITION`
- else H2 and not H3 → `SMOOTH_DECAY`
- else H3 and not H1 → `CORE_DECOUPLE`
- else → `NOISE_MIXED`
