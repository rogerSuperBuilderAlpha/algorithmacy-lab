# Paper 2 — execution plan (construct development + IIT formal model)

> **RECAST NOTICE (superseding).** This plan predates the formal-model recast. The authoritative artifacts
> are now `draft/DRAFT.md`, `ARGUMENT.md`, and `state_alphabet.md`. Φ is **adopted as a formal model** under
> three named modeling choices (W–S–C representation, the state-individuation rule, the party partition), not
> asserted as *identical* to triadicity; "decision procedure / verdict" below should read as "formal model /
> classification," and the "calibration anchor handed to Paper 3" is obsolete (that anchor was cut). The
> paper also now acknowledges the borrowed measure's critics (the 2023 IIT pseudoscience debate; Cerullo's
> XOR-grid result).

**Mode:** construct + formal model. The IIT model is literal here. **Status:** executed and drafted
(`draft/DRAFT.md`).

## The instrument (reuse from this repo)

Papers 2–3 reuse the repo's exact IIT-4.0 Φ oracle. No vendoring needed — sibling package import:

- `from proxy_audit import exact_phi` → `exact_big_phi(tpm_sbn, cm, state)` (exact Φ for a whole system in a
  state) and `network_phi_aggregations(tpm_sbn, cm, n, rng)` (mean/max/π-weighted over reachable states).
  Accepts **any** state-by-node TPM of shape `(2^n, n)`, values in [0,1] — including non-Boolean
  application-layer TPMs built from interaction logs.
- `pyphi.new_big_phi.evaluate_partition(cut, subsystem, system_state, ...)` tests a **specific** partition,
  i.e. the **worker–system–counterpart** partition, not only the system MIP. Use this to show Φ is
  irreducible across the W–S–C cut, which is the formal content of "triadic."
- Env: `~/iit-playground/venv-4.0/bin/python` (IIT-4.0 PyPhi). **Tractability:** Φ is super-exponential in
  state count, so the application-layer state alphabet must stay small — this *is* the §4 individuation
  discipline, not a separate limitation.

## How "our process" maps here

- **The load-bearing decision is the state-individuation rule (outline §4).** Pre-register it *before any
  computation*, exactly as we validate measures on controls before comparing: "a new application-layer state
  begins when the mediator commits a determination that alters its causal disposition toward the parties."
  Defend it against the two competing criteria (action-availability, visibility). This is the paper's single
  empirical commitment.
- **Validate the instrument on controls before the worked examples:** a factoring/independent
  application-layer TPM → Φ ≈ 0 (the W–S–C partition reduces it); a known-irreducible coupling → Φ > 0 that
  the W–S–C partition cannot reduce. Only proceed once controls pass.
- **Compute, don't assert:** the two worked examples are computed, not argued — report the actual Φ values.

## Steps (deferred to an execution session)

1. `phi_instrument.py`: wrap `proxy_audit.exact_phi` to (a) take an application-layer state-by-node TPM and
   compute exact Φ, and (b) evaluate Φ across the specified worker–system–counterpart partition via
   `evaluate_partition`. Validate on controls (factoring → ~0; irreducible coupling → >0).
2. Write `state_alphabet.md`: the pre-registered individuation rule + how an application-layer TPM is
   constructed from observable interaction logs (the §3 application-layer argument).
3. **Worked example A — dyadic limit:** chat with a language model. Build the state alphabet under the rule;
   the model commits nothing that couples a third party → the matrix factors → low Φ.
4. **Worked example B — irreducible triad:** résumé → applicant-tracking-system → hiring-manager. The system
   commits a determination neither party controls → the matrix does not factor → Φ the W–S–C partition
   cannot reduce. Report both Φ values side by side; tie back to the competency claim (one-hop inference vs
   reasoning through the whole triad).
5. Take up the **continuous-platform case** (Uber commits in a stream) as the rule's hardest test and an
   open problem handed to Paper 3's calibration.
6. Write the paper (intro → borrowing → application layer → state alphabet → worked application →
   contribution-and-limits). Concede IIT-as-consciousness-theory is contested in one sentence and return:
   only the irreducibility measure is imported. Cite the precedent for importing formalisms (fitness
   landscapes from biology; network measures from graph theory).

## Deliverable and scope

The instrument + the worked application: **Φ over the application-layer matrix is a decision procedure for
triadicity** (hence for whether a form demands algorithmacy vs literacy). **No calibration** — a Φ value is
not yet a difficulty scale until anchored to an observed outcome; that is Paper 3.

## Honest limits to state

State-alphabet dependence (named and pre-registered, not hidden) and the absence of an outcome anchor
(handed to Paper 3). Tractability as a discipline on granularity, not a defect.
