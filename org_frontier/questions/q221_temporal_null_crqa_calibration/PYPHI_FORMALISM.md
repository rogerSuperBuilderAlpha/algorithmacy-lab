# PyPhi formalism and environment record

**PyPhi build.**
- Branch `feature/iit-4.0`, commit `b78d0e342d37175cbd55cf35a6d52ae035b4c50f`.
- Installed in the isolated venv `/workspace/algorithmacy-827-venv`, which was not upgraded.
- `pyphi.config.IIT_VERSION` = 4.0.
- Distance: GENERALIZED_INTRINSIC_DIFFERENCE. PARALLEL off. PROGRESS_BARS off.

**Other software.** Python 3.12.15, numpy 2.5.4, scipy 1.18.1.

**Quantity.**
- The **system** integrated information φ_s (`new_big_phi.sia(...).phi`).
- The major complex comes from `new_big_phi.maximal_complex`.
- No Φ-structure (big Φ of distinctions and relations) is used.

**TPM.**
- Deterministic: `org_frontier.classifier.classifier.tpm_from_rules`. The 8% noise TPM is never used for Φ
  (rule 8).
- State-by-node format, little-endian: state index s = X + 2Y + 4H.
- Node order (X, Y, H) = indices (0, 1, 2).
- The connectivity matrix comes from rule dependence (`cm_from_rules`).

**States and subsystems.**
- States: every state reachable under the deterministic dynamics (`foundations.proxy_audit.exact_phi.reachable_states`).
- The major complex is maximised over those states.
- Subsystems that are unreachable from a given state are skipped (`StateUnreachableError`).

**Leave-one-out.**
- q161 freezes the node's rule to the constant 0 and keeps it in the network (`TARGET_AUDIT.md`).
- The own replication also uses freeze-to-1.
- The background-condition alternative is in `identifiability/target_variants.py`.

**Ties.**
- q161 uses `TOL` = 1e-6 for B.
- The q221 core tie gap is the difference between the best and second-best complex Φ. It is 1.0 for every
  survivor.

**Precision.** Exhaustive computation, no approximations. Φ values are exact small rationals (0, 1, 2), stored
as floats.

**Determinism.** The `rep_verify` reruns are byte-identical. The CI check `q221-lead-pair-exact-phi` pins the
printed values.
