# q168 — findings

Probe 322. H(out|W) with C hidden and uniform, output drawn from Q126's mediator(agenda, k). The faithful
floor is 0.50 bits (PP1, k=0). The W-probing limit is the residual that survives the worker probing W.

## Residual surprise across interestedness k

| k | H(out\|W) approve | H(out\|W) deny | after probing W | probing removes |
|---|-------------------|----------------|-----------------|-----------------|
| 0 | 0.50 (= floor)    | 0.50 (= floor) | unchanged       | 0.00            |
| 1 | 1.00 (> floor)    | 0.00           | unchanged       | 0.00            |
| 2 | 0.50 (= floor)    | 0.00           | unchanged       | 0.00            |
| 3 | 0.00              | 0.00           | unchanged       | 0.00            |
| 4 | 0.00              | 0.00           | unchanged       | 0.00            |

Under the approve agenda at k=1 the residual is 1.00 bits, twice the faithful floor. Overriding the
least-warrant state (W=0, C=0) toward approve aliases C-driven variance into W=0, a value the faithful gate
left determinate at 0. Both W-values then carry a full bit of C-aliased surprise. The deny agenda only
collapses output variance, so its residual falls from the floor and never rises. Probing W removes 0.00 bits
of the residual at every k under both agendas.

## Verdicts

- H1 SUPPORTED. The interested residual reaches 1.00 bits at approve k=1, above the 0.50-bit faithful floor.
  An agenda imposed where the parties least warrant it can add irreducible surprise the worker can neither
  set nor see, beyond what a merely hidden counterpart sets. The null (interest equals the floor) is false.
- H2 CONFIRMED. Probing W leaves H(out|W) unchanged at every k. The surplus is C-aliased: setting and
  observing W learns P(out|W) exactly yet removes none of the C-driven part. The agenda's contribution sits
  on the opacity floor, not in the channel the worker controls. The null (probing drives it toward 0) is
  false.

## Scope

Closed-form information theory on a 3-variable Boolean model. Evidence about the instrument and the
construct. The empirical reading is on synthetic forms. Output is deterministic and byte-identical across
runs.
