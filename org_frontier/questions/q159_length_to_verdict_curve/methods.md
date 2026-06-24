# q159 — methods

## Forms

The pool is the 3-node forms_library, a random 3-node ensemble (`rand_form`, 120 draws, seed 0), and
a random 4-node ensemble (`rand_form4`, 120 draws, seed 1). Each form carries an exact-Φ verdict from
its major-complex core size: triadic for a core of three or more nodes, dyadic for a core of two.
Sub-dyadic cores are dropped. The surviving pool holds 95 forms (18 triadic, 77 dyadic).

## The CRQA-implied verdict

The behavioral verdict at trajectory length L thresholds one feature: the prominence spread, the
count of prominent pairwise lead-lag links read by the coupling matrix above a fixed prominence
floor. Coupling breadth grows with the number of coordinated parties, so a triadic form carries more
prominent links than a dyadic one. A form reads triadic when its spread clears a single threshold.

The threshold is fit once, at the reference length of 2400 steps, as the spread split that maximizes
balanced accuracy against the exact-Φ labels. It is then held fixed and applied at every swept
length. Fixing the boundary isolates one effect: how trajectory length alone moves the spread
feature. A boundary re-fit at each length would chase the feature and hide the convergence.

## Length sweep and convergence

Lengths sweep over 150, 300, 600, 1200, and 2400 steps. Each form's trajectory is seeded by a fixed
per-form seed, so every spread reading reproduces byte-for-byte. The convergence length of a form is
the smallest swept length at which its CRQA verdict equals its reference (2400-step) verdict and
stays equal at every longer swept length.

H1 reads the share of forms converged by 600 steps and compares agreement with the exact-Φ verdict at
600, 1200, and 2400 steps. H1 is supported when over 80% of forms have converged by 600 steps and
agreement does not rise from 1200 to 2400.

H2 bins forms by exact-Φ tertile and compares the mean convergence length of the top tertile against
the bottom. The Φ distribution piles up at the ceiling: many forms share Φ = 2.0, so a value-quantile
cut leaves bins empty. The tertiles are cut by rank with ties broken by ascending Φ then form index,
giving three near-equal bins. H2 is supported when the high-Φ tertile has the smaller mean
convergence length.

## Instrument control

The control is the worker-system-counterpart triad `[x[1], x[0]&x[2], x[1]]` with labels (W, S, C):
verdict triadic, max_phi 2.0, major-complex Φ 2.0, full 3-node core. The control also confirms the
length-parameterized spread feature returns a finite, nonnegative value at every swept length.

## Determinism

All ensemble draws and all trajectory samples are seeded with fixed seeds. Exact Φ is deterministic.
The probe output is byte-identical across repeated runs.

## Scope

Every number is exact IIT-4.0 Φ on synthetic Boolean coordination forms. This is an in-silico study
of the CRQA-to-Φ bridge. No field organization is measured, and the bridge from a coded organization
to a transition matrix is not yet validated against observed data.
