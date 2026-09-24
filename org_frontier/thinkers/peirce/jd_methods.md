# Joint determination — methods (pre-registered addendum)

Fixed 2026-09-24 with [`jd_hypotheses.md`](jd_hypotheses.md), before any probe below ran.

## Instrument

The instrument is the one the Peirce paper uses ([`methods.md`](methods.md)). The probe reads exact IIT-4.0
cause–effect structures with PyPhi's `new_big_phi.phi_structure` on the stock binary install. The
whole-system verdict is Φ over the MIP, maximised over reachable states (`org_frontier.probes.lib.verdict`).
The major complex comes from `org_frontier.probes.lib.major_complex`.

The state set is the paper's: the all-ones state plus every state reachable under the form's rules
(`foundations.proxy_audit.exact_phi.reachable_states`).

Every run starts with the paper's instrument control, `forms.run_control()`:
- the conjunctive triad A′ = M, M′ = A ∧ B, B′ = M;
- expected Φ = 2.000000, core {A, M, B}, adicity 3, and maximal distinction M → cause AB;
- a failed control stops the run with no comparison read.

## The joint-determination reader

At each state in the state set, take every distinction with φ > 0 whose mechanism is a single element X.
The element is **jointly determined** at that state when its cause purview contains two or more elements
other than X. The reader reports, for each form:

- `jd_elements`: the elements that are jointly determined at some state, each with the largest such cause
  purview and its φ;
- `jd`: true if `jd_elements` is non-empty;
- `jd_in_whole`: true if Φ_MIP > 0, and some jointly determined X is in the major complex together with at
  least two elements of its cause purview other than X.

Compound mechanisms (two or more elements) do not count. This is the difference from the paper's
cause-side adicity, which counts |mechanism ∪ cause purview| over all distinctions: a two-element mechanism
with a one-element cause purview scores 3 there, and it is not joint determination here.

## Forms

**JD1** — from `forms.py`: CONTROL, GIVING_GENUINE, SIGN_PRAGMATIC; MONADIC_DEGENERATE, DYADIC_DEGENERATE,
GIVING_DEGENERATE, SIGN_EXOGENOUS; and the one-input wirings copy_BCA and copy_CCA from `one_input_wirings(3)`.
From `../simmel/forms.py`: DYAD_MUTUAL.

**JD2** — from `../simmel/forms.py`:
- MAJORITY_TRIAD: every rule is maj(A, B, C);
- TRIAD_MUTUAL: A′ = B ∧ C, B′ = A ∧ C, C′ = A ∧ B;
- MEDIATOR: A′ = A ∧ M, M′ = A ∧ B, B′ = B ∧ M.

**JD3(a)** — the one-input wirings of `one_input_wirings(5)`, reduced to one representative per isomorphism
class.
- A wiring f (node i copies f(i) ≠ i) is relabelled by every permutation p as k ↦ p⁻¹(f(p(k))).
- The class representative is the lexicographically smallest relabelled tuple.
- There are 13 classes. Each representative is evaluated as copy wiring with the labels A–E.

**JD3(b)** — `two_input_sample(30, seed=1, n=4)` from `forms.py`, unchanged.

## Decision rules

- **JD1.** CONFIRMED if the three positive forms have `jd_in_whole` true and the eight negative forms have
  `jd` false. PARTIAL if one form misreads. REFUTED if two or more misread.
- **JD2.** CONFIRMED if MAJORITY_TRIAD has `jd` true with Φ_MIP = 0, and TRIAD_MUTUAL and MEDIATOR have
  `jd_in_whole` true. PARTIAL if the majority holds and one of the other two fails. REFUTED if the majority
  fails.
- **JD3.** (a) holds if no class has `jd` true. Among the 30 forms of (b), count:
  - forms with `jd_in_whole` true;
  - forms with `jd` true and Φ_MIP = 0.

  CONFIRMED if (a) holds and both counts are ≥ 1. PARTIAL if (a) holds and exactly one count is ≥ 1.
  REFUTED otherwise.

Anything noticed after the fact is labelled *post hoc* and does not change a verdict.

## Reproduction

```
python -m org_frontier.thinkers.peirce.probe_peirce_joint_determination            # JD1, JD2, JD3(b) prefix of 8
python -m org_frontier.thinkers.peirce.probe_peirce_joint_determination --full     # adds JD3(a) and all 30 of JD3(b)
```

The fast run prints the JD1 and JD2 verdicts and the two JD3(b) counts over its 8-form prefix. The prefix
counts are descriptive only. The JD3 verdict is printed by the full run alone.

Results go to `results/probe_peirce_joint_determination.json`, or `…_full.json` for the full run. The fast
run is registered in `ci/reproduce.json`; the full run is registered as slow and is reproduced nightly.
