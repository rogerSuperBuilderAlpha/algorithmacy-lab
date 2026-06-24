# q187 methods

## Construct

The bridge module `org_frontier.qualitative.disagreement_phi` scores two party accounts of one
coordination as a Phi spread. Each account is a Boolean rule set over the same labelled nodes.
The module runs each account through the exact-Phi classifier and reports verdict agreement, the
Phi gap, and the core Jaccard overlap of the two major-complex cores. This study adds two
extensions to the module: `signed_phi_gap`, the difference of the two whole-system max Phi
values with sign, and `core_node_divergence`, a per-node attribution that names which parties
the two accounts place differently in the integrated core.

## Encoding

Three parties over the little-endian state tuple x: x[0] is the poster P, x[1] is the automated
system S, x[2] is the policy team T. The poster reads the system, P <- S. The system is the hub
and reads the poster and the policy team, S <- P & T. This wiring is shared by both accounts.

The two accounts differ only in the policy team's update rule.

- Spectator (poster's account): T <- P. The policy team watches the poster, does not read the
  system back, and stays outside the core. This is the oversight prior's observing-principal
  case, a team read once and then absent.
- Oversight (system's account): T <- S. The policy team reads the system back, closing the
  loop, and folds into the top of the core. This is the oversight prior's coupled-principal
  case, a team that is part of the decision as it happens.

The system carries the mediator-with-memory and oversight priors: it is the hub the other two
route through, and the policy team sits above it.

## Matched control

The control holds the policy team external in both accounts. Both control rules keep the policy
team out of the core, drawn from the set of T rules that yield core {P,S} at triadic structure
with max Phi 2.0. Control A uses T <- P; control B uses a distinct T-external truth table. With
the policy team external in both, the cores agree and the per-node attribution names no node.

## Verdict logic

H1 is supported when the treatment has a nonzero core Jaccard gap, the disputed set is exactly
{T}, and the matched control has an empty disputed set with full core agreement. H2 is supported
when the signed phi_gap, oversight minus spectator, exceeds zero; otherwise the H2-null is
recorded, distinguishing equal Phi from a spectator account that integrates at least as much.

## Determinism

The probe seeds NumPy with `default_rng(0)`. The construct is exact, with no Monte Carlo, so the
seed guards any downstream stochastic helper. Three runs produce byte-identical output. An
instrument control validates the machinery on the faithful triad, which reads triadic with max
Phi 2.0.

## Scope

The accounts are coder-supplied rule sets, not measured worker states. The empirical arm is on
synthetic data. The construct scored is divergence between two stated accounts, validated on the
control. The result is an in-silico baseline at one seed, not a measurement of a real moderation
coordination. The validation gap from rule set to lived practice is open.
