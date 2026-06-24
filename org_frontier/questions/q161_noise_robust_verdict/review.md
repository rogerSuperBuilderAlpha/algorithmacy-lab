# q161 — Review notes

## What the probe shows

On sixteen synthetic Boolean forms, the bottleneck-node verdict is the most robust to flip-rate
misspecification (best-minus-worst 0.091 across flip, agreement 0.75 to 0.84), the membership
verdict is intermediate (spread 0.117), and the triadic/dyadic verdict is the most fragile (spread
0.162, correct at every flip for only 5 of 16 forms). Both pre-registered hypotheses fail: H1
predicted the reverse ranking, and H2's entropy-tracking correlation is -0.148.

## Anticipated pushback and answers

Threshold choice drives the triadic/dyadic fragility. The spread threshold is calibrated once at
the natural flip, so the verdict is built to be best there and to drift as flip moves. A reviewer
could call the fragility an artifact of single-flip calibration. The answer is that this is the
point: a verdict read through a fixed threshold inherits the calibration's flip. The bottleneck
argmax needs no threshold to inherit. The contrast between the two decodings is the finding here.

The corpus is small (16 forms) and the Spearman for H2 is computed on 16 points. A correlation of
-0.148 on 16 points is indistinguishable from zero, which is why H2 is reported as not supported.
The probe makes the weaker claim that entropy fails to explain the optimum's variation, and stops
there.

Bottleneck recovery rising with flip looks odd. More noise sharpens the rank separation between the
articulation node and the rest by keeping the run exploring, so the argmax is read more cleanly. At
very low flip the run collapses toward a short cycle and the centralities flatten. The probe sweeps
to 0.30 and the trend is monotone in that band; it is not claimed to hold for arbitrarily large
flip.

## Scope and validity

Exact IIT-4.0 Phi ground truth; CRQA readings on synthetic trajectories; seeded and byte-identical
across reruns. No field organization is measured. The result is a property of CRQA decoding under
update-noise misspecification, useful as a baseline for which read-outs to trust when the noise
regime is uncertain.

## Does it serve the thesis

Yes, modestly. The exact-Phi major complex is the fixed ground truth every CRQA verdict is scored
against, so the apparatus is doing the work of saying what "correct" means here. The contribution
is the principled comparison IIT enables across three different read-outs, not a claim that any
cheap CRQA statistic recovers Phi.
