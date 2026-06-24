# Q133 — review of prior work

Q133 completes Q132 ([`q132_value_baselines`](../q132_value_baselines/paper.md)), which ran the value sweep
under the approve agenda only and noted that under deny the re-integrating baseline is the other balanced
rule, citing Q127 ([`q127_interest_baselines`](../q127_interest_baselines/paper.md)) for the agenda symmetry.
Q133 computes that case so the mirror reproduces from a script rather than resting on inference. It reuses
the Q131/Q132 value function (Shapley of subsystem Φ at the integrating state) and adds nothing new to the
method; the contribution is closing the agenda symmetry with a registered number.
