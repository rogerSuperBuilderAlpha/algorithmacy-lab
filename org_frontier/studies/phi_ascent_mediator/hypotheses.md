# phi_ascent_mediator — hypotheses (fixed before computing)

**Question (agenda #14).** Does an adaptive mediator that learns
toward higher Φ (not toward dropping a party, #79) converge to the
conjunctive hub, the pool, or somewhere else?

**Already known (cited, not reopened).**
- Probe #79: mediator that degrades reliance on the counterpart
  (r: 1→0) walks Φ 2.0→0 and flips dyadic at the endpoint — learning
  *away* from a party.
- Zoo landmarks (#104, #115, #116, #132): conjunctive hub Φ=n−1;
  pool Φ=n(n−1) (6 at n=3, 12 at n=4); parity decays; chain flat at 2.
- `STOCH_TEMPORAL_ARC.md` / #5–#13 — pointers only.
- Estimation / construct / omit / ladder closed.

**Learning rule (fixed; candid).** Exact binary IIT-4.0 Φ_MIP
(whole-form max over reachable). Two panels, both greedy ascent
(move only to a strictly higher-Φ neighbor; stop at local max).

**Panel A — mechanism ascent (n=3).** Parties fixed: W′=S, C′=S.
Mediator rule S′ ranges over all 256 Boolean functions of (W,S,C)
(truth-table mask). Neighborhood = single-bit flip of the table.
From every start mask, greedy-ascend; record terminal mask, Φ, and
whether the terminal is the conjunctive hub (S′=W∧C), the OR hub
(S′=W∨C), or another Φ-maximizer. Pool wiring is *not* in this panel
(parties stay read-S).

**Panel B — topology ascent (n=3 and n=4).** Catalog of designed
forms: chain, conjunctive hub (single_hub), two_hub, all-required
pool, ring, parity_hub. Neighborhood = the full catalog (any other
form). Greedy-ascend from each catalog member; record the terminal.
This is the panel that can reach the pool.

**#79 contrast.** Re-run the drop-a-party reliability path
(r∈{1,0.75,0.5,0.25,0}); confirm Φ falls and flips dyadic at r=0.

**Candid N.** n=3 for mechanism panel (exhaustive 256); n∈{3,4} for
topology panel (6 forms). No continuous weight learning; no
stochastic policy gradient — discrete greedy Φ-ascent only.

## H1 — converges to the conjunctive hub

On Panel A, a majority (>50%) of the 256 starts terminate at the AND
hub mask, **or** on Panel B a majority of starts terminate at the
conjunctive hub rather than pool/chain/other.

Null: neither panel majority-terminates at the conjunctive hub.

## H2 — converges to the pool (catalog Φ-maximum)

On Panel B: the all-required pool is a Φ-maximum of the catalog at
both n=3 and n=4; at n=4 every greedy trajectory terminates at the
pool (unique max); at n=3 every trajectory terminates at some catalog
Φ-maximum (pool may tie, e.g. with ring).

Null: pool is not maximal, or some n=4 start terminates off-pool, or
some n=3 start terminates below the catalog max.

## H3 — somewhere else

On Panel A, the ascent terminates on a **Φ plateau** with more than
one maximizer (n_max>1 at Φ\*=max), and the AND hub is not the unique
or majority terminal — mechanism learning under fixed party reads
does not select the conjunctive hub. (Topology-panel pool success is
compatible with H3 on the mechanism panel; primary word then names
both.)

Null: Panel A majority-terminates at a single named form (AND or OR).

**Primary verdict word.**
- H2 and H3 and not H1 → `PLATEAU_ELSE_POOL`
- H2 and not H1 and not H3 → `TO_POOL`
- H1 and not H2 → `TO_HUB`
- H3 and not H2 → `ELSEWHERE`
- else → `ASCENT_MIXED`

**Instrument gate.** #79 path: Φ(1)=2.0 triadic, Φ(0)=0 dyadic.
Panel B: pool Φ > hub Φ at n=3 and n=4. Faithful triad control.
