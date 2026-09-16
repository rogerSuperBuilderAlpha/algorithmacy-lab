# Stoch–temporal arc — working picture

Short synthesis of the stochastic and temporal lane on
`RESEARCH_AGENDA_50_V2` for PR #739. Exact binary IIT-4.0 Φ;
in-silico. Estimation / construct / omit / ladder stay closed.
Sibling arcs:
[`CONSTRUCT_LADDER_ARC.md`](CONSTRUCT_LADDER_ARC.md),
[`OMIT_ATOM_ARC.md`](OMIT_ATOM_ARC.md),
[`ESTIMATION_ARC.md`](ESTIMATION_ARC.md).

## Verdict in one line

**Flip-noise collapses only at p\*=0.5 with smooth Φ; construction
(hold-k / delay encoding) decides temporal factoring; oscillatory
rot_ring has its own flat Φ=2 law; correlated SBS collapses to the CI
projection under IIT-4.0; genuine triadic/dyadic coexistence exists
beyond sticky hysteresis; CT embedding softens but does not erase
#112’s grain/schedule dependence; Φ-ascent goes to pool/plateau, not
the hub.**

## Arc

| # | study | verdict | claim |
|---|---|---|---|
| 6 | [`studies/commit_noise_phase/`](studies/commit_noise_phase/) | **SMOOTH_DECAY** | Hub flip-noise: monotone Φ glide; verdict flips only at p=0.5; no interior phase |
| 7 | [`studies/party_vs_mediator_noise/`](studies/party_vs_mediator_noise/) | **SAME_THRESHOLD_DIFF_CURVE** | Party vs mediator share p\*=0.5; seat still shapes Φ / n_core |
| 8 | [`studies/parity_vs_conjunctive_noise/`](studies/parity_vs_conjunctive_noise/) | **SAME_P_STAR** | Parity and conjunctive share p\*=0.5 at n=3,4; conjunctive sheds more Φ̂ |
| 9 | [`studies/timescale_separation/`](studies/timescale_separation/) | **FACTORS_LIKE_62** | hold-for-k flips dyadic at k\*=2 (core→{S}); prob 1/k stays triadic |
| 10 | [`studies/commit_response_delay/`](studies/commit_response_delay/) | **DELAY_CORE_SHIFT** | Buffer stays triadic with shifting core; lagged read flips at d=2 |
| 11 | [`studies/oscillatory_scaling/`](studies/oscillatory_scaling/) | **DIFFERENT_LAW** | rot_ring Φ=2 constant (period=n); separable from #132 fixed-point zoo |
| 5 | [`studies/correlated_output_noise/`](studies/correlated_output_noise/) | **CORE_SHIFT_NO_FLIP** | Non-CI shared-coin SBS; Φ only sees CI projection (= indep dual-party flip) |
| 13 | [`studies/genuine_bistability/`](studies/genuine_bistability/) | **GENUINE_COEXISTENCE** | Triadic+dyadic attractors coexist; #109 sticky is MULTI_SAME + hysteresis |
| 14 | [`studies/phi_ascent_mediator/`](studies/phi_ascent_mediator/) | **PLATEAU_ELSE_POOL** | S′ ascent → Φ=2 plateau; topology ascent → pool (unique at n=4) |
| 12 | [`studies/continuous_time_invariance/`](studies/continuous_time_invariance/) | **STILL_DEPENDENT** | CTMC embed softens #112 (200/216 tri) but seq-like rates still flip 8/24 |

Pointers only for the middle of the noise lane (#6–#10 detail lives in
those FINDINGS).

## Working picture

1. **Noise is soft on the verdict.** Across hub, party, and family
   seats (#6–#8), flip-noise drives smooth Φ decay. The binary verdict
   holds to the coin-flip endpoint p\*=0.5. Seat and family still shape
   magnitude and sometimes n_core; they do not move the collapse
   threshold on these panels.

2. **Temporal factoring is construction-bound.** Slowing the mediator
   by hold-for-k factors like sequential update (#9 / #62); a
   probabilistic 1/k commit does not. Transport delay (#10) is not the
   same object: buffer depth shifts core and Φ without the sticky-{S}
   factorization, while a lagged-read encoding can flip. Grain,
   schedule, hold, and delay are distinct axes (#112 catalogue).

3. **Oscillation adds a law, not a verdict split.** A rotating-update
   ring keeps Φ=2 with period=n (#11), separable from and_ring caps and
   hub/parity landmarks. Dynamics can mint a fifth scaling shape
   without leaving the triadic side.

4. **Correlated output noise is an instrument limit.** A shared-coin
   SBS that state-by-node cannot express is genuinely non-CI (#5), but
   exact IIT-4.0 / PyPhi evaluate only the CI projection — identical to
   independent dual-party flip. No interior verdict flip beyond #61's
   static shared input; one-point n_core dip on the projection.

5. **Bistability is real — and not #109.** At fixed coupling, ordinary
   forms (memoryless triad, xor-memory, …) host coexisting triadic and
   dyadic attractors (#13). The sticky mediator's activity hysteresis
   (#109) is same-verdict multistability (both attractors dyadic) plus
   path-dependent mean activity — a different phenomenon.

6. **Φ-ascent does not select the hub.** Learning toward higher Φ
   (#14), opposite #79’s drop-a-party path, lands on a multi-form Φ=2
   plateau under fixed party reads and on the all-required pool when
   topology can open (pool/ring tie at n=3; pool unique at n=4).

7. **Continuous time does not buy invariance.** Native CT Φ is absent
   from the PyPhi pin. A CTMC→expm embedding (#12) keeps equal-rate
   cells triadic where discrete grain-2/seq wipe the panel, but extreme
   rate asymmetry still flips a third of forms — #112’s lesson
   survives under the proxy.

## Scope

Exact binary IIT-4.0; designed n≤5 Boolean / stochastic TPMs; CT
proxy via embedded discrete observation; in-silico. No organization
measured. No reopen of estimation, construct, omit, or ladder arms.

## Best next

**Arc closable.** Prefer agenda **#15+** (hierarchy / topology) or
empirical / survey packets. Native continuous-time IIT would reopen
#12 only if a new pin lands. Do not reopen estimation / construct /
omit / ladder.
