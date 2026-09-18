# shared_mediator_k — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #6).** Across **k>2** local conjunctive triads
sharing a single mediator, does merge Φ scale as **k**, as **2k**, or
**saturate** — and does OR bridging still refuse merge?

**Already known (cited, not reopened).**
- **V2 #16 / `two_triad_shared_member`:** shared mediator + AND merges two
  triads into one five-node core at **Φ=4.0**; shared leaves do not; OR
  does not merge.
- **V3 #4 / #5:** composed topologies pick landmarks / factor / collapse;
  no new hybrid ring–hub law.
- Single triad: Φ=2.0. Ternary / residual-cascade / M3 noted only.

**Gap.** #16 fixes k=2. The lift to k≥3 — scaling of merge Φ, and whether
OR still refuses — is open.

**Universe.** Binary exact IIT-4.0. Construction: for each i=1..k, parties
(W_i, C_i) copy S; S′ = bridge_i (W_i ∧ C_i). Bridge ∈ {AND, OR}.
n = 2k+1. Primary: k∈{1,2,3} (n∈{3,5,7}).

**Merge** = full-core (all 2k+1 nodes) triadic. **Refuse** = not full-core
merge (local cores / collapse).

**Scale as k:** merge Φ ≈ c·k for AND across k=1,2,3 (affine in k).
**Scale as 2k:** merge Φ ≈ 2k (k=1→2, k=2→4, k=3→6).
**Saturate:** AND merge Φ at k=3 equals k=2 (Φ=4), not larger.

## H1 — instrument + k=2 replicate

Faithful triad Φ=2.0. k=2 AND: full five-node merge, core Φ=4.0 (V2 #16).
k=2 OR: does **not** full-merge.

## H2 — OR refuses at k=3

k=3 OR does not full-merge (extends #16 OR refuse).

## H3 — AND merge Φ scaling

Among {scale_k, scale_2k, saturate}, exactly one describes AND merge Φ at
k=1,2,3 (using k=1 triad Φ=2 as the k=1 point). Decision rule:
- **scale_2k** if Φ(k) = 2k within eps for k=1,2,3;
- **scale_k** if Φ(k) = k within eps (will fail k=1,2 given known 2 and 4);
- **saturate** if Φ(3)=Φ(2)=4 and Φ(2)=4 > Φ(1)=2;
- else **OTHER_SCALE** (report the triple).

## H4 — panel verdict

H1–H2 hold, and H3 picks one named scale → token among
`SCALE_2K_OR_REFUSES` / `SCALE_K_OR_REFUSES` / `SATURATE_OR_REFUSES` /
`OTHER_SCALE_OR_REFUSES` (OR refuse is part of every positive token).
