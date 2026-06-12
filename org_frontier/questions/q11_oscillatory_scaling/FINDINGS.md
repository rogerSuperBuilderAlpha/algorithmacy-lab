# Q11: oscillatory Φ scaling law findings

Forms (discrete TPMs, grain 1, n=3,4,5,6):
- rot_ring(n): rotating update x_k' = x_{k−1} (traveling wave, synchronous period = n).
- commit_ring(n,p): conjunctive hub at node 0 committed every p micro-steps (hold_k_tpm, s_idx=0, k=p), composed.
- flip_ring(n): distributed parity x_k' = ¬x_{k−1}.
- Baselines: and_ring(n) (#132), conjunctive hub Φ=n−1, parity hub Φ=2^(2−n) (#115/#120).
Measure: Φ_MIP, verdict, MIP, major complex (`pyphi.compute.major_complex()`), attractor period. PHI_EPS=1e-9, TOL=1e-6.
Instrument controls (passed across probes): strict-mediation triad triadic Φ=2.0 {W,SC}; and_ring(3)=6.0, and_ring(4)=4.0; parity_hub(5)=0.125 full core.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 rotating ring is a fifth law distinct from capped Φ=4 | confirmed | rot_ring Φ_MIP=[2,2,2,2] over n=3..6 (constant, triadic, full core, period=n); and_ring=4.0 at n=4,5,6; gap Φ_rot−Φ_and = −2.0 at every matched n; both decision clauses fire |
| H2 cycle period is a term in the law | confirmed | commit_ring Φ at p=1 = n−1 (2,3,4,5), at p=2,3 = 0; Δ_p Φ = −2,−3,−4,−5 at n=3,4,5,6; rot_ring corroborant flat Φ=2 (no corroboration, decision rests on commit sweep) |
| H3 distributed flip breaks the parity decay | confirmed | flip_ring Φ=[2,2,2,2] full core vs hub floor 2^(2−n)=[0.5,0.25,0.125,0.0625]; gaps widen [1.5,1.75,1.875,1.9375]; step ratios=1.0, no halving; measured periods 6,4,10,6 (honest, off nominal 2n at even n) |
| H4 both cyclers triadic + full core across n | refuted | rot_ring triadic Φ=2 full core (n=3,4,5); commit_ring(n,2) DYADIC Φ=0, core shed to {x0} at n=3,4,5 (collapses to copy-x0 map, CM `[[1,1,1],[0,0,0],[0,0,0]]` at n=3); dyadic at n=3 already |
| H5 grain band widens with period | refuted | g*(n) (smallest grain reading dyadic) = [3,2,5,2] for n=3,4,5,6; not non-decreasing, g*(6)=2 < g*(3)=3; odd n flip at g=p, even n at g=2 (parity-of-n, not period-scaling); grain-1 baseline triadic Φ=2 |

**Through-line.** An oscillatory attractor adds a Φ(n) law beyond the four the fixed-point zoo held, and period is a variable in it, while triadicity and a period-scaled grain band both fail to follow from cycling alone. The rotating ring is a fifth shape, constant Φ=2 across n, separable from the capped Φ=4 ring at every matched size (H1). Period enters as a term: the periodic-commit form moves Φ from n−1 to 0 when only the commit cadence changes (H2). Distributing the parity flip drops the parity hub's decay, so the decay belongs to the shared XOR commit and clears once the flip spreads around the loop (H3). The two refutations bound the claim: a built-to-cycle form can still factor to dyadic (commit_ring at p=2, H4), and the grain band tracks the parity of n while ignoring the period (H5). The flat Φ=2 rotation that makes H1 clean is also why the period term has to come from the mediated commit form and the grain band stays fixed as p grows.

**Caveats.** Sizes n=3..6, cadence p=1,2,3; verdict is grain- and schedule-relative (H5); Φ magnitude is ordinal. The period term is shown for the mediated commit form (cadence set independently of n); the rotating ring is flat in both n and p. Laws are properties of these constructions and stay local to them; arbitrary cyclers are untested. No measured worker.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q11_oscillatory_scaling.probe_probe_q11_rotating_law` (and `_period_term`, `_flip_ring_decay`, `_triadic_persistence`, `_grain_band`)
