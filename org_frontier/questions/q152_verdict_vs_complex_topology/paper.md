# q152 — The whole-system verdict and the major complex are not interchangeable diagnostics

## Question

The program reads two things off a coordination form. The whole-system **verdict** says
whether the form is triadic (irreducible integration, Φ > 0 over the minimum-information
partition) or dyadic. The **major complex** says which nodes carry that integration — the
maximal-Φ subsystem, its core membership. These are often treated as one reading: a
triadic verdict is taken to mean the parties are bound together. This study asks whether
the two readings can come apart on the topologies already built in studies 1-9, at matched
n = 5, 6.

## Approach

Every studied topology — chain, ring, pool, single-hub, two-hub, symmetric multihub swept
over its mediator count, and hub-chain hierarchies — is instantiated at n = 5, 6. For each,
the verdict, the major-complex core, and the per-party Shapley values of subsystem Φ are
read from the existing machinery. A topology is flagged as a disagreement when the verdict
is triadic but the core excludes at least one node. The worker-system-counterpart triad is
the control: verdict triadic, core full.

## Result

Disagreement is real and common. Chain topologies are triadic at the whole-system level yet
their major complex collapses onto a small terminal subsystem, excluding the upstream
parties the form nominally strings together. Symmetric multihubs at large mediator count
are triadic yet drop one or more parties from the core. The whole-system verdict and core
membership are therefore not interchangeable: a triadic verdict does not certify that every
party is inside the integrated core. H1 is supported.

The zero-Shapley marker does not track the disagreement. Topologies disagree while carrying
no exactly-zero Shapley party (negative or small-positive marginal contributions are enough
to leave a node outside the core), so the biconditional `disagree <=> has-zero-Shapley`
fails. H2 is not supported: a zero Shapley value is neither necessary nor a clean marker for
exclusion from the core.

The verbatim run, including the per-topology table and the H1/H2 verdict lines, is in
`results/output.txt`.

## Scope

Exact IIT-4.0 Φ on synthetic Boolean coordination forms — a pre-disclosed prior catalog of
topologies used as baselines. This is an in-silico comparison of two diagnostics; it makes
no claim about any empirical organization, and the validation gap to field data is open.
