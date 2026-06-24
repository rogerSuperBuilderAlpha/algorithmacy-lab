# q192 — review

## What was run

Study 1 of the reconciliation-cost line within the qualitative disagreement program. The probe
defines an account as a triple of per-node rules over a fixed six-rule catalog, adds a `reconcile`
routine that runs breadth-first single-rule edits from account A to the first account matching
account B's `(structure, core)` signature, and tests two fixed hypotheses on a panel against the
faithful triad. It imports the q183 bridge `org_frontier.qualitative.disagreement_phi.spread` for
the Φ spread and `verdict()` / `major_complex()` from `org_frontier.probes.lib` for the signatures.
Φ is not reimplemented.

## What holds

- Instrument control passes: the faithful triad reads triadic with max Φ_MIP = 2.0.
- Reconcile controls pass: identity pair at distance 0, one-rule-apart pair at distance 1.
- The signature map covers all 216 accounts in the catalog space.
- Edit distance and spread magnitude are strongly rank-correlated (Spearman 0.8355); zero-spread
  pairs sit at distance 0.
- Path-order invariance holds: every pair at distance ≥ 1 has a single shortest-path length equal
  to its distance.
- Output is byte-identical across three runs (deterministic, seeded).

## What failed, and why it is a real finding

- H1 refuted. Edit distance is not a monotone function of the spread. Three panel accounts share a
  spread of 2.6667 and reconcile at distances 1, 2, and 3. The Φ spread fixes the verdict-and-core
  gap, not the number of catalog edits that bridge it. The correlation is strong but the strict
  monotone claim fails.
- H2 not supported. Reconciliation is path-order-invariant but not symmetric. The directed distance
  from an account to B's signature class differs from the reverse, because signature classes differ
  in size and reachability. A symmetric metric is the standard for a well-defined distance, so the
  combined H2 fails.

## Limits and open points

- The reconciliation cost is defined over a single hand-built catalog of six rules. A different
  catalog changes the neighbour graph and the distances. The catalog dependence is not measured
  here.
- The panel pairs all accounts against one target (the faithful triad). The asymmetry and the
  monotonicity break are read against this one endpoint; a later study should vary the endpoint.
- The match target is B's signature class, not B's exact rule set. This is what creates the
  asymmetry. A variant that reconciles to the exact rules would be symmetric by construction but
  would no longer measure verdict-and-core reconciliation.
- The accounts are synthetic. The probe scores edit distance between coded rule sets, not a real
  coordination. The catalog-to-observation gap is not addressed.

## Verdict

Both hypotheses refuted on synthetic accounts, and the refutations are informative. The reconcile
routine is well-anchored and deterministic; reconciliation cost is a directed quasi-distance,
strongly rank-correlated with the Φ spread but neither a monotone function of it nor a symmetric
metric.
