# continuous_time_invariance — hypotheses (fixed before computing)

**Question (agenda #12).** Computed in continuous time rather than by
discrete update, is the verdict grain-and-schedule invariant after all
(#112 found no discrete invariant)?

**Already known (cited, not reopened).**
- Probe #112: of 24 canonically triadic forms, grain-1 sync keeps
  24/24; grain-2 sync keeps 0/24; sequential keeps 0/24; across-
  condition majority keeps 0/24. No modeling-free discrete invariant.
- `STOCH_TEMPORAL_ARC.md` — discrete stoch–temporal lane otherwise
  closed (#5–#11, #13–#14). Estimation / construct / omit / ladder
  closed.
- Methodology note: exact Φ questions that need native continuous
  time fall outside what the discrete IIT-4.0 / PyPhi pin answers
  cleanly (`protocol/methodology_review.md`).

**Instrument fact (fixed before computing).** PyPhi’s IIT-4.0 pin has
no continuous-time Φ primitive. `timescale.py` only raises a discrete
TPM to an integer power. Native CT IIT is therefore unavailable here.

**Defensible proxy (fixed; candid).** Async continuous-time Boolean
network: each node i updates by its Boolean rule at exponential rate
r_i (competing clocks → rate matrix Q). Observation at grain Δt is the
embedded TPM P(Δt)=expm(Q·Δt). Exact binary IIT-4.0 Φ is computed on
the CI-projected state-by-node form of P(Δt) — the same projection
limit as agenda #5 (embedded SBS is not conditionally independent for
Δt>0). This asks whether *CT-generated dynamics observed at Δt under
rate schedule r* restore verdict invariance, not whether a native
continuous-time Φ exists.

**Panel (candid N).**
- Forms: the 24 canonically triadic n=3 corpus forms of #112
  (`enumerate_family` filter).
- Discrete controls (re-#112): grain-1 sync, grain-2 sync, sequential.
- CT grid: Δt ∈ {0.1, 1.0, 5.0}; rate schedules
  `equal=(1,1,1)`, `slow_S=(1,0.1,1)`, `seq_like=(100,10,1)`.

**Measures.** Per cell: structure (triadic/dyadic), Φ_MIP. Aggregate:
fraction of forms still triadic under each discrete condition; fraction
of CT cells triadic; number of forms that flip on any CT cell.

## H1 — continuous-time restores invariance

On the CT grid, **every** cell (all 24 forms × all Δt × all three
schedules) remains triadic — grain and schedule no longer flip the
verdict under the embedding proxy.

Null: at least one CT cell is dyadic.

## H2 — still schedule/grain dependent

At least one CT cell is dyadic (some form × Δt × schedule flips), so
the embedding proxy does not restore a modeling-free invariant.
(Discrete #112 wipeout may still be softened — report the contrast.)

Null: no CT cell flips (H1).

## H3 — NOT_TESTABLE under current IIT-4.0 PyPhi pin

The study cannot run a defensible Φ comparison at all (embedding
rejected / numerically unusable / no runnable path), and only the
instrument gap is reported.

Null: the embedding proxy runs and yields H1 or H2.

**Primary verdict word.**
- H1 → `CT_INVARIANT`
- H2 → `STILL_DEPENDENT`
- H3 → `NOT_TESTABLE`
- else → `CT_MIXED`

**Instrument gate.** #112-style discrete: grain-1 = 24/24 triadic;
grain-2 = 0/24; sequential = 0/24. Faithful triad sync Φ=2.0.
Embedded P(Δt) row-stochastic after clip/renorm.
