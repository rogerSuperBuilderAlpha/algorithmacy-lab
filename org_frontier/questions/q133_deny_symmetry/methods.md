# Q133 — methods

The Q132 setup with the deny agenda (a = 0). At level k the mediator imposes denial on the k states where
the parties least warrant it (highest warrant-for-1 first), committing the faithful baseline (AND, OR, XNOR,
XOR) elsewhere; W' = S, C' = S. Value is the Shapley value of subsystem Φ read at the verdict's max-Φ state
(Q132's verdict-aligned convention, since the all-ones background is degenerate off AND). The control is the
faithful AND mediator (total Φ = 2.0, mediator share two-thirds). A baseline shows extraction when some
interested level raises Φ above the faithful value with mediator share above 0.6.

Caveats carried from Q111/Q122: all-ones-free background, unproven Φ-to-money bridge; "value/share/rent" name
Shapley allocations of Φ.

Reproduce: `python -m org_frontier.questions.q133_deny_symmetry.probe_deny_symmetry`
(output in [`results/output.txt`](results/output.txt)).
