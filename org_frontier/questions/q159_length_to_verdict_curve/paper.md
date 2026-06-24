# q159 — How Long a Run a Stable CRQA Verdict Needs

A CRQA reading of a sampled run places a coordination form as triadic or dyadic. The exact major
complex gives the structural ground truth from the model's transition matrix. The behavioral verdict
comes from a finite run, so a short run can read a form one way and a longer run another. The practical
question for the recurrence line is how long a run a stable reading needs, and whether the answer
depends on how irreducible the form is.

The CRQA-implied verdict here thresholds one feature, the prominence spread: the count of prominent
pairwise lead-lag links read from the coupling matrix. Coupling breadth grows with the number of
coordinated parties, so a triadic form carries more prominent links than a dyadic one. The threshold
is fit once at the longest run, 2400 steps, as the spread cut that best separates the exact-Φ labels,
then held fixed across the length sweep. Holding the boundary fixed isolates the length effect: a
boundary re-fit at each length would chase the feature and mask the convergence.

The pool is 95 synthetic forms (18 triadic, 77 dyadic) from the 3-node corpus, a random 3-node
ensemble, and a random 4-node ensemble. Lengths sweep over 150, 300, 600, 1200, and 2400 steps. A
form's convergence length is the shortest run at which its verdict matches the 2400-step reference and
stays matched at every longer run.

The verdict settles fast. By 600 steps, 92.63% of forms have reached a reading that no longer changes.
Agreement with the exact-Φ verdict reaches 0.81 at 1200 steps and does not rise at 2400. Six hundred
steps suffice for a stable verdict across nearly all forms, which supports H1.

Convergence length does not fall with Φ magnitude. The rank-tertile means rise from 159.7 steps in the
low-Φ third to 450.0 in the high-Φ third, the reverse of the prediction, which refutes H2. The corpus
gives the hypothesis little to work with: Φ piles up at the ceiling value 2.0, so the low and high
tertiles straddle the same Φ and magnitude carries almost no variance to set convergence length apart.

Two limits bound the reading. The spread cut reaches only 0.62 balanced accuracy and agreement tops
out near 0.81, so a single threshold is a coarse behavioral proxy for the structural verdict; the
convergence result is about when the reading stops moving, not whether it is right. And the whole study
is in-silico. Every Φ is exact IIT-4.0 Φ on a model transition matrix, the behavioral side is a sampled
run of that model, and the bridge from a coded field organization to a transition matrix is not yet
validated against observed data. The length figures are properties of these synthetic runs.

The usable result for the recurrence line is the length budget: 600 sampled steps give a stable CRQA
verdict for the great majority of these forms, and longer runs add no verdict accuracy. Φ magnitude
does not buy a shorter run in this corpus, so a fixed run length is the right default until a corpus
with real Φ spread can test the dependence.
