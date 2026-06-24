# q187 review

## Claim audited

Two accounts of a takedown coordination, differing only in the policy team's rule, were scored
as a Phi spread. The treatment splits on the core with the policy team as the single disputed
party; the matched control names no party. The two accounts read equal Phi.

## Checks

- Instrument control passes: the faithful triad reads triadic with max Phi 2.0.
- The two treatment accounts share the poster and system rules and differ only in the policy
  team's rule. Verified by construction in the probe.
- Treatment core Jaccard is 0.667 with disputed set {T}; control core Jaccard is 1.0 with empty
  disputed set. The control rules out an encoding artifact.
- Signed phi_gap, oversight minus spectator, is +0.0000, so H2's strict-inequality prediction is
  refuted and the H2-null is recorded.
- Three runs produce byte-identical output. The probe seeds NumPy with default_rng(0).

## Weaknesses

- The result sits at one wiring and one seed. The equal-Phi finding depends on the poster-system
  loop already integrating fully at the shared wiring; a wiring where the loop integrates less
  could let the policy team add Phi when it joins the core. The study does not sweep wirings, so
  the H2-null is a single-point result, not a general claim that coupling never raises Phi.
- Both accounts read the same structure and the same Phi here, so the spread's verdict-agreement
  and phi-gap components carry no signal in this case. The whole signal is in the core
  divergence. A harder case would split the structure or the Phi too.
- The accounts are synthetic rule sets. No worker is measured. The disputed-party claim is about
  two coded accounts, not about a real moderation team.

## Verdict

The probe supports H1 and refutes H2 on its own terms, with a matched control and deterministic
output. The contribution is the per-node attribution that names the disputed party and the clean
separation of integration level from core membership. The scope is in-silico at one seed.
