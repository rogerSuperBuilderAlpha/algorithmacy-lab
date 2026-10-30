# O01: what survives, and the next test

The saved weighted-quorum results support the full-group extremes-only claim within the tested
models. They refute the stronger claim that a mixed weighted rule cannot retain a smaller core.
This note records a source review and a count of existing CSV rows on 2026-10-30. No new exact-Φ
experiment was run. The input-noise design below is a proposal, not a completed result.

## The claim and its scope

In the baseline, each party copies mediator S, and S fires when at least k parties are active.
Only OR (k=1) and AND (k=all) retain the full core. The implementation is
[`threshold_hub`](../probe_threshold_scaling.py), lines 23–29. With m parties plus S, the extreme
core has Φ=m. The atlas uses n for total nodes when it writes Φ=n−1.

The [atlas findings](../../studies/coordination_logic_atlas/FINDINGS.md), lines 11–25, also say that
interior quorums have no irreducible core. These are separate claims: a whole system can factor
while a smaller core remains irreducible. Probe 457 tests that distinction with weighted rules.

## What the existing tests show

The [saved deterministic output](results/run.txt), lines 51–60, reports 33 classes, including 21
mixed classes. Two mixed rules, weights (1,1,2,2) at quotas 2 and 5, retain {S,P3,P4} at core φ=2.
Both whole systems have Φ=0. These examples refute the no-smaller-core claim without refuting
the full-group claim.

The [noise output](results/run.txt), lines 72–126, reports stable extreme membership and falling
core φ on the tested commit-noise grid below ε=0.5. H6 reports 12 violations, but its scorer
counts existing mixed cores that survive noise. It does not require a new core to appear.
Compare [hypotheses.md](hypotheses.md), lines 151–155, with
[the scorer](probe_weighted_quorum.py), lines 426–427. The saved CSVs contain no mixed class that
acquires a core of at least two parties after starting with fewer than two.

This count can be reproduced from the repo root with standard-library Python; it reads files
and prints counts only:

```python
import csv
from pathlib import Path

root = Path("org_frontier/probes/weighted_quorum/results")
with (root / "classes.csv").open(newline="") as source:
    classes = list(csv.DictReader(source))
with (root / "noise.csv").open(newline="") as source:
    noise = list(csv.DictReader(source))
by_id = {row["class"]: row for row in classes}
mixed = [row for row in classes if row["type"] == "mixed"]
noisy_mixed = [row for row in noise
               if by_id[row["class"]]["type"] == "mixed"
               and float(row["eps"]) < 0.5]
for name, rows in (("deterministic", mixed), ("commit noise <0.5", noisy_mixed)):
    full = sum(len(row["core"].split()) == int(row["n"]) + 1 for row in rows)
    positive = sum(float(row["whole_phi"]) > 1e-9 for row in rows)
    print(name, len(rows), "full cores", full, "positive whole Phi", positive)
rescues = [row for row in noise
           if by_id[row["class"]]["type"] == "mixed"
           and float(row["eps"]) > 0
           and len(by_id[row["class"]]["core"].split()) < 3
           and len(row["core"].split()) >= 3]
print("noise-created multi-party cores", len(rescues))
```

Expected counts: 21 deterministic mixed rows, 147 mixed rows below ε=0.5, zero full cores,
zero positive whole-system readings, and zero noise-created multi-party cores.
The existing CI checks are `probe-weighted-quorum-ci` and `probe-weighted-quorum-full` in
[`ci/reproduce.json`](../../../ci/reproduce.json). The full experiment writes CSV files;
`--ci` skips both those writes and the noise arm.

## Minimal new test: input observation errors

Input noise remains outside the existing [pre-registration](hypotheses.md), lines 132–140.
Test three parties copying S, with OR, 2-of-3 majority, and AND mediator rules at error rates
η ∈ {0, 0.1, 0.5}: nine cases. Independently flip each input as observed by S. Keep actual party
states and their copying rules unchanged.

For actual party vector x and observed vector y, set
P(S′=1 | x) = Σ_y f(y) η^d(x,y) (1−η)^(3−d(x,y)), where d counts differing bits.
Sum over all eight observed vectors. Use these exact probabilities in the transition matrix;
do not estimate them from sampled trajectories.

Fix these decision rules before computing:

- At η=0, reproduce the deterministic AND, OR, and majority anchors. At η=0.5, S must be
  independent of its inputs and the system must factor. Failed controls make the test unscorable.
- At η=0.1, support the narrow extension if AND/OR retain the full core and majority has
  whole-system Φ≤1e-9. A full-group majority core or loss of an extreme full core refutes it.
- Report a smaller majority core separately: it refutes the stronger no-smaller-core claim.

Run the known instrument controls first. Report whole-system Φ, core membership and φ, and the
whole-system state profile. The classifier takes the maximum over reachable states, so one state
can decide the verdict; see [classifier.py](../../classifier/classifier.py), lines 142–158.
The core helper also chooses a maximum and keeps the first strict winner; inspect tied maxima
before claiming unique membership.

## Confounds and limits

Commit flips and input observation errors are different noise models. Keep noise location fixed
within each comparison. Also keep the copying-party wiring fixed: the older
[quorum thread](../../threads/quorum/quorum.py) samples constant, copying, and inverted party
rules, so its 3% extreme rate is not the copying-hub prediction.

The atlas's explanation that no majority voter is pivotal is too broad. A majority voter can
change the outcome when the other two votes split. A lack of full-group integration does not
imply zero Boolean influence; the weighted probe measures that influence with swing counts.

Agreement between weight bounds 0..5 and 0..6 is a saturation check, not by itself a proof that
all larger weight bounds add no functions. The tested party counts and finite noise grid also
bound the result. IIT 3.0 gives a different majority verdict, as the probe's
[scope notes](README.md#scope) report.

These are findings about small Boolean coordination models under IIT 4.0. They do not measure
real committees or organizations. The proposed input-noise test remains unrun, and O01 remains
open in the registry.
