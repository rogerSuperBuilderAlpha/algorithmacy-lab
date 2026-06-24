# q190 — Is the disagreement-Φ spread robust to elicitation noise?

Two parties give two accounts of one coordination. The disagreement-Φ bridge (q183) scores how far
apart those accounts sit: whether both read the same structure (verdict_agreement), the gap in
whole-system Φ (phi_gap), and the overlap of their integrated cores. Each account is an elicited
rule table, and elicitation is imprecise. A spread that moved whenever the rule table was jittered
would measure the analyst's precision, not the coordination. This study tests whether the spread
holds up under bounded noise in each account's rules.

## Setup

Each account is a Boolean rule list over labels (W, S, C), turned into a deterministic TPM. Noise
gates each TPM entry with probability 0.10 and pulls gated entries toward 0.5 by 0.10, so a stated
1.0 reads as 0.9 and a stated 0.0 reads as 0.1. The table stays near-deterministic. Whole-system
max Φ_MIP of the perturbed table is read by the exact IIT-4.0 oracle.

Six pairs span the dyad/triad boundary. Two put two triads together (Φ = 2.0 each); these sit far
from the boundary. Two put a triad against a clean dyad (Φ near zero); these straddle it. One puts
two clean dyads together at the boundary. One is the bridge anchor, the faithful triad against
itself. A pair is near-boundary when at least one account is a clean dyad.

## Result

Verdict_agreement moved on near-boundary pairs and nowhere else. Across 30 draws per pair, the two
triad-vs-dyad pairs flipped agreement 2 and 3 times, the two-dyad pair flipped 4 times, and the
three pairs of two triads flipped zero times. The signed phi_gap never changed sign on any pair.
The flips come from a clean dyad's Φ lifting above the classifier epsilon under jitter, the only
boundary crossing the noise can produce. A triad keeps Φ at or above about 0.65 under the same
jitter and stays triadic.

For the pairs that disagree at noise zero, the gap magnitude is measurable. Pooled over those
pairs, phi_gap had mean 1.33 and standard deviation 0.55, a signal-to-noise of 2.44. The gap is a
quantity, not jitter.

## Reading

The spread tracks a genuine verdict boundary. Where two accounts agree and sit clear of the
boundary, no amount of this jitter moves the verdict; where one account is a clean dyad at the
boundary, jitter can cross it, and that is where the analysis should expect instability. For pairs
that genuinely disagree, the gap magnitude carries signal well above the noise.

## Scope

Exact IIT-4.0 Φ on small synthetic Boolean coordination forms. The accounts are coder-supplied, so
both rates are baselines on synthetic data. "Account", "elicitation noise", and "boundary" name
rule-table-and-Φ quantities, not measured organizations. The Φ-to-organization bridge is open.
