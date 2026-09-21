# noise_composed_carriers — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #12).** Does party-vs-mediator noise
(V2 #7 `SAME_THRESHOLD_DIFF_CURVE`) still share p*=0.5 when the carrier
is a **composed necklace** or **multi-hub span** rather than a single
hub?

**Already known (cited, not reopened).**
- V2 #7 `party_vs_mediator_noise/` — **SAME_THRESHOLD_DIFF_CURVE**:
  p*=0.5 on both seats for conjunctive and parity hubs; Φ curves and
  (on conjunctive) n_core still differ by locus.
- V2 #6 `commit_noise_phase/` — SMOOTH_DECAY under hub commit noise.
- V3 #4 `local_triad_necklace/` — AND necklace = ring landmark Φ=4.
- V3 #6 `shared_mediator_k/` — shared-S AND merge Φ=2k.

**Noise model (fixed).** Same flip-noise as V2 #7:
`P(out=1)=(1−p)·clean+p·(1−clean)` on selected TPM column(s).
Exact binary IIT-4.0 Φ via `classify`.

**Carriers.**
1. **hub3** — conjunctive hub control (V2 #7 seat).
2. **shared_k2** — two local triads sharing mediator S (n=5);
   multi-unit / multi-hub span via shared mediator.
3. **necklace** — closed AND local-triad necklace (n=6; V3 #4).

**Loci.**
- **mediator** — hub column (S / S / H0).
- **party** — one party column (P1 / W1 / P0).

**Collapse threshold p*.** First grid p with structure=`dyadic`
(Φ ≤ PHI_EPS). Grid includes 0.49 and 0.50 so a shared coin-flip
endpoint is identifiable.

## H1 — hub control reproduces V2 #7

On hub3, p*_party = p*_mediator = 0.50. Null: control drifts.

## H2 — composed carriers share party/mediator p*

On shared_k2 and necklace, |p*_party − p*_mediator| < 0.02.
Null: some composed carrier splits seats by ≥0.02.

## H3 — composed p* stays at 0.5

On every composed carrier, both loci collapse at p*=0.50.
Null: some composed locus leaves 0.50 (shift under composition).

## H4 — panel closed

Instrument control passes and H1–H3 resolve to a panel verdict.

## Reading keys

- **SAME_PSTAR_COMPOSED:** H1 ∧ H2 ∧ H3 — coin-flip p* survives
  necklace and shared-mediator span for both seats.
- **COMPOSE_SPLITS_PSTAR:** H1 ∧ ¬H2 — composition separates party vs
  mediator thresholds.
- **COMPOSE_SHIFTS_PSTAR:** H1 ∧ H2 ∧ ¬H3 — seats still match but leave
  0.5 under composition.
- **CONTROLS_FAIL:** H1 fails.
