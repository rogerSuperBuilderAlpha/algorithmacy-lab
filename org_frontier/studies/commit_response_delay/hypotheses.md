# commit_response_delay — hypotheses (fixed before computing)

**Question (agenda #10).** Does a fixed delay between the commit and
the parties' response move the verdict, or only its magnitude?

**Already known (cited, not reopened).**
- #9 `timescale_separation/` — **FACTORS_LIKE_62** under hold-for-k
  (pointer only; slowed clock ≠ transport delay).
- #62 sequential factorization.
- Q10 prior (`questions/q10_commit_delay/`).
- Estimation / construct / omit / ladder closed.

**Encoding (candid; two constructions).**
1. **buffer pipeline (primary).** d pass-through buffer nodes B1…Bd
   carry S's commit to the parties; n=3+d; no B_i→B_i self-edge
   (transport, not sticky memory).
2. **lagged read (construction check).** Same lag on the 3-node map
   with no buffer nodes (composed/strided TPM).

d ∈ {0,1,2,3}. d=0 = synchronous baseline.

**Forms (designed; candid N).**
1. **conjunctive** — W'=S, S'=W∧C, C'=S (n=3 at d=0).
2. **parity_hub** — S'=P1⊕P2, Pi'=S (n=3 at d=0).

**Measures.** Φ_MIP, structure, major-complex membership (full labels).

## H1 — delay flips the verdict

On the **buffer pipeline**, some d∈{1,2,3} reads dyadic on the
conjunctive form (parity reported).

Null: buffer stays triadic at every d.

## H2 — only Φ magnitude

On buffer, verdict stays triadic at every d for both forms, and the
major-complex label set (as a set of node names) is unchanged from
d=0 at every d (only Φ moves).

Null: core membership changes, or a verdict flip occurs.

## H3 — core changes without verdict flip

On buffer for some form: structure stays triadic at every d, but the
major-complex membership (set of labels) differs from d=0 at some
d∈{1,2,3}.

Null: no such core shift, or a verdict flip co-occurs.

**Primary verdict word (buffer pipeline).**
- H1 → `DELAY_FLIPS`
- else H3 → `DELAY_CORE_SHIFT`
- else H2 → `MAGNITUDE_ONLY`
- else → `DELAY_MIXED`

Lagged-read disagreement is reported as a construction witness, not an
H gate.
