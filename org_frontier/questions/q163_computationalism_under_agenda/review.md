# q163 — review

## What was run

Probe 317 extends battery_computationalism's channel/actor forms by replacing the faithful S = W ∧ C
gate with Q126's mediator(agenda, k). The shared module
`org_frontier/cognition/interested_mediator_forms.py` holds the actor and channel builders for the
interested-mediator line. The instrument control reproduces the faithful actor (triadic, Φ = 2.0) and
the matched channel (Φ = 0). Output is byte-identical across three runs.

## Reuse and integrity

Φ and the major complex come from `org_frontier/probes/lib.py`; the verdict from the classifier; the
mediator and parties_read_by_S from the Q126 probe. No Φ is reimplemented. No RNG enters the
computation; a seeded generator is fixed for hygiene. Every number in FINDINGS comes from the captured
run in `results/output.txt`.

## Verdicts and honesty

H1 is supported, and the support is one-sided: only the approve agenda shows the non-monotone bump
(0.417 at k=2 rising to 0.500 at k=3); deny is monotone. The probe reports H1 as the disjunction over
agendas and prints which agenda carries it, so the asymmetry is visible. H2 is refuted, reported as a
null: the flip-test shows S still reading both parties while Φ has already collapsed.

## Threats

- The non-monotone bump depends on the order-averaged reading. On the strictly ordered ladder the
  approve surplus is monotone (2.0, 0.5, 0, 0, 0). The two readings answer different questions and both
  are printed; H1 is evaluated on the order-averaged surplus, the order-independent one.
- parties_read_by_S is a binary connectivity flip-test. It cannot see a graded loss of dependence on a
  party, so the H2 null may be an artifact of coarseness. A graded read measure is the natural follow-up
  and is named in the paper.
- The channel caps at k=2 (two W-states) while the actor runs to k=4. The channel is Φ = 0 throughout,
  so the cap does not affect the surplus, but the asymmetry is worth noting.

## Scope

Exact Φ on a 3-node Boolean model; synthetic forms; no measured worker. The contribution is a Φ
signature that separates an interested actor from a degrading channel, and a clean null on whether
agenda-reading substitutes for party-reading.
