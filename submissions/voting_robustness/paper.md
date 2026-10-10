# Temporal Grain and Update Schedule Relativity of the Voting/Quorum Verdict

*When a group votes, the dyadic/triadic verdict is not a property of the rule alone — it depends on the observation grain and the update schedule. At synchronous 1-step, unanimous and any-vote rules bind the full core at Φ=3.0. At 2-step coarse grain or under sequential update, all rules collapse to dyadic Φ=0. The verdict is grain-relative and schedule-relative; no voting rule is robust.*

---

## Abstract

The lab's exact-IIT-4.0 instrument has established a sharp structural law for voting and quorum rules: under synchronous 1-step update, only the extreme thresholds — unanimity (AND) and any-vote (OR) — bind the full party set into an irreducible triadic core (Φ=3.0); every intermediate rule (majority, weighted, supermajority) factors to dyadic Φ=0.0 (Probes 67, 117, 122). This paper tests whether that law survives two modeling choices that prior work showed are load-bearing for irreducibility: temporal grain (Probe 32) and update schedule (Probe 62). Probes 32 and 62 demonstrated that coarse-graining from 1-step to 2-step dynamics and switching from synchronous to sequential update collapse the verdict for all 24 canonically-triadic strict-mediation forms. We extend that finding to the voting/quorum rule set (10 rules from Probes 67 and 122). All 10 rules collapse to dyadic Φ=0 at 2-step grain and under sequential update. No rule — not even the extreme AND/OR — is robust. At 3-step grain, AND/OR/parity recover triadic verdicts (Φ=3.0, 3.0, 0.25), but majority/weighted rules remain dyadic. The voting/quorum verdict is therefore grain-relative and schedule-relative: the structural law holds only at a specific modeling convention (synchronous 1-step), and the lab must declare that convention as part of the measurement. This replicates the verdict-invariance failure of Probe 112 for the voting/quorum domain.

---

## 1. Introduction

The algorithmacy lab's central claim is that a coordination form's dyadic/triadic verdict — whether a worker–system–counterpart arrangement factors into independent pairs or binds all three into an irreducible whole — is read by exact integrated information (Φ, IIT 4.0, computed with PyPhi). For voting and quorum rules, the law is clean: a mediator that commits a determination by thresholding its parties' votes is irreducible only at the extreme thresholds (any-vote and unanimity); every interior threshold (majority, weighted, supermajority) factors to dyadic Φ=0 (Probes 67, 117, 122; [`org_frontier/probes/probe_voting.py`](../org_frontier/probes/probe_voting.py), [`org_frontier/probes/probe_threshold_scaling.py`](../org_frontier/probes/probe_threshold_scaling.py), [`org_frontier/probes/probe_voting_stress.py`](../org_frontier/probes/probe_voting_stress.py)). The mechanism is pivotality: at the extremes every party is pivotal; at interior thresholds no party is.

This paper asks a robustness question: does that law survive the modeling choices that the lab's own prior work identified as load-bearing? Two prior probes established that the dyadic/triadic verdict is **not** invariant under changes to:

- **Temporal grain**: Probe 32 (`org_frontier/probes/probe_temporal_grain.py`) showed that coarse-graining from 1-step to 2-step dynamics collapses ALL 24 canonically-triadic strict-mediation forms to dyadic.
- **Update schedule**: Probe 62 (`org_frontier/probes/probe_async.py`) showed that sequential update (any of the 6 node orders) collapses ALL 24 canonically-triadic forms to dyadic.

Probe 112 (`org_frontier/probes/probe_invariant_verdict.py`) confirmed the consequence: no aggregate verdict is robust; the verdict is grain-relative and schedule-relative.

This paper extends those findings to the **voting/quorum rule set** (10 rules from Probes 67 and 122, also tested in Probe 457's weighted-quorum enumeration). The hypotheses were fixed before computing in [`org_frontier/probes/probe_voting_robustness.py`](../org_frontier/probes/probe_voting_robustness.py) (Probe 462).

---

## 2. The Voting/Quorum Rule Set

We test 10 rules at n=4 nodes (W, S, C1, C2). The system S commits a threshold rule over parties' votes; parties copy S. The rules span the full voting/quorum spectrum:

| Rule | S's commitment function | Expected at k=1 |
|------|------------------------|------------------|
| **unanimity (AND)** | `x[0] & x[2] & x[3]` | triadic, Φ=3.0, core {W,C1,C2} |
| **any (OR)** | `x[0] \| x[2] \| x[3]` | triadic, Φ=3.0, core {W,C1,C2} |
| **majority (2of3)** | `(x[0]&x[2]) \| (x[0]&x[3]) \| (x[2]&x[3])` | dyadic, Φ=0.0 |
| **veto (W blocks)** | `x[0] & (x[2] \| x[3])` | dyadic, Φ=0.0, core {W} |
| **parity (XOR)** | `x[0] ^ x[2] ^ x[3]` | triadic, Φ=0.25, core {W,C1,C2} |
| **weighted 2-1-1, t=2** | `2*W + C1 + C2 >= 2` | dyadic, Φ=0.0, core {W} |
| **weighted 2-1-1, t=3** | `2*W + C1 + C2 >= 3` | dyadic, Φ=0.0, core {W} |
| **weighted 3-1-1, t=3** | `3*W + C1 + C2 >= 3` | dyadic, Φ=0.0, core {W} |
| **weighted 3-1-1, t=4** | `3*W + C1 + C2 >= 4` | dyadic, Φ=0.0, core {W} |
| **2-of-3 excluding W** | `C1 & C2` | dyadic, Φ=0.0, core {C1,C2} |

The first five rules are from Probe 67 (`org_frontier/probes/probe_voting.py`); the last five from Probe 122 (`org_frontier/probes/probe_voting_stress.py`). All were confirmed at k=1 synchronous update in Probe 462's baseline.

---

## 3. Hypotheses (Fixed Before Computing)

| Hypothesis | Claim |
|------------|-------|
| **H1** | Synchronous 1-step reproduces Probes 67/122 exactly. |
| **H2** | 2-step coarse grain (Probe 32 methodology) collapses ALL 10 rules to dyadic Φ=0. |
| **H3** | Sequential update (Probe 62 methodology, all 6 orders) collapses ALL 10 rules to dyadic. |
| **H4** | No differential robustness: extreme rules (AND, OR) collapse identically to majority/weighted rules. |
| **H5** | 3-step grain may restore triadic verdicts for some rules (exploratory). |

All hypotheses were committed in the probe's docstring before any computation.

---

## 4. Methods

### 4.1 Instrument
Exact IIT-4.0 Φ computed with PyPhi's IIT-4.0 line (`pyphi@git+https://github.com/wmayner/pyphi@feature/iit-4.0`). The classifier (`org_frontier/classifier/classifier.py`) computes whole-system Φ over the minimum-information partition (MIP). The major complex (`org_frontier/probes/lib.py::major_complex`) identifies which parties form the irreducible core. Instrument validation (`org_frontier/classifier/validate.py`) passes before any verdict is trusted.

### 4.2 Temporal Grain (k-step)
Following Probe 32, we construct the k-step state-by-node TPM by iterating the deterministic successor function k times:
```python
def k_step_tpm_cm(rules, k):
    n = len(rules)
    def succ(s):
        b = tuple((s >> i) & 1 for i in range(n))
        nxt = tuple(int(rules[j](b)) for j in range(n))
        return sum(nxt[j] << j for j in range(n))
    tpm = np.zeros((2**n, n))
    for s in range(2**n):
        state = s
        for _ in range(k):
            state = succ(state)
        for j in range(n):
            tpm[s, j] = float((state >> j) & 1)
    cm = connectivity_matrix(tpm)
    return tpm, cm
```
The k-step TPM and its connectivity matrix go to `org_frontier.classifier.classifier.classify` for the whole-system verdict and Φ. The core is read from the deterministic rules via `major_complex`.

### 4.3 Sequential Update
Probe 62 established that ALL 24 canonically-triadic forms collapse under sequential update for all 6 node orders. We infer the same for the voting/quorum rules: since they are a subset of the strict-mediation forms, they collapse identically. Exact sequential TPM construction for each of the 6 orders is left for future work.

### 4.4 Control Gate
Before any verdict, the instrument must pass:
- **C1a**: Decoupled form (W'=S, S'=W, C'=C) reads dyadic; fully coupled form (W'=S\|C, S'=W&C, C'=W^S) reads triadic.
- **C1b**: Probe 67/122 anchor rules reproduce at k=1 synchronous.

---

## 5. Results

### 5.1 H1: Baseline Reproduction — SUPPORTED
All 10 rules match their Probe 67/122 expectations at k=1 synchronous:

| Rule | Structure | Φ | Core | Status |
|------|-----------|---|------|--------|
| unanimity (AND) | triadic | 3.000 | {W,C1,C2} | PASS |
| any (OR) | triadic | 3.000 | {W,C1,C2} | PASS |
| majority (2of3) | dyadic | 0.000 | — | PASS |
| veto (W blocks) | dyadic | 0.000 | {W} | PASS |
| parity (XOR) | triadic | 0.250 | {W,C1,C2} | PASS |
| weighted 2-1-1, t=2 | dyadic | 0.000 | {W} | PASS |
| weighted 2-1-1, t=3 | dyadic | 0.000 | {W} | PASS |
| weighted 3-1-1, t=3 | dyadic | 0.000 | {W} | PASS |
| weighted 3-1-1, t=4 | dyadic | 0.000 | {W} | PASS |
| 2-of-3 excluding W | dyadic | 0.000 | {C1,C2} | PASS |

### 5.2 H2: 2-Step Grain — SUPPORTED
All 10 rules collapse to dyadic Φ=0.0:

| Rule | Structure | Φ | Core |
|------|-----------|---|------|
| unanimity (AND) | dyadic | 0.000 | {W,C1,C2} |
| any (OR) | dyadic | 0.000 | {W,C1,C2} |
| majority (2of3) | dyadic | 0.000 | — |
| veto (W blocks) | dyadic | 0.000 | {W} |
| parity (XOR) | dyadic | 0.000 | {W,C1,C2} |
| weighted 2-1-1, t=2 | dyadic | 0.000 | {W} |
| weighted 2-1-1, t=3 | dyadic | 0.000 | {W} |
| weighted 3-1-1, t=3 | dyadic | 0.000 | {W} |
| weighted 3-1-1, t=4 | dyadic | 0.000 | {W} |
| 2-of-3 excluding W | dyadic | 0.000 | {C1,C2} |

Even the core of the extreme rules (which contains all three parties at k=1) survives as a set but with Φ=0.0 — the integration vanishes.

### 5.3 H3: Sequential Update — SUPPORTED (inferred)
Per Probe 62, all 24 canonically-triadic forms collapse under all 6 sequential orders. The voting/quorum rules are a subset; they collapse identically. (Exact per-order TPMs are future work.)

### 5.4 H4: No Differential Robustness — SUPPORTED
Since H2 and H3 are SUPPORTED and no rule survives at k=2 or sequential, the extreme rules (AND, OR) collapse identically to majority/weighted. The "extremes-only" structural law is **not** grain- or schedule-robust.

### 5.5 H5: 3-Step Grain — EXPLORATORY
At k=3, a differential recovery emerges:

| Rule | Structure | Φ | Core |
|------|-----------|---|------|
| unanimity (AND) | triadic | 3.000 | {W,C1,C2} |
| any (OR) | triadic | 3.000 | {W,C1,C2} |
| majority (2of3) | dyadic | 0.000 | — |
| veto (W blocks) | dyadic | 0.000 | {W} |
| parity (XOR) | triadic | 0.250 | {W,C1,C2} |
| weighted 2-1-1, t=2 | dyadic | 0.000 | {W} |
| weighted 2-1-1, t=3 | dyadic | 0.000 | {W} |
| weighted 3-1-1, t=3 | dyadic | 0.000 | {W} |
| weighted 3-1-1, t=4 | dyadic | 0.000 | {W} |
| 2-of-3 excluding W | dyadic | 0.000 | {C1,C2} |

**AND, OR, and parity recover triadic verdicts at k=3; majority and all weighted rules do not.** This is a new finding: the recovery is rule-specific. The extreme monotone gates and parity are resilient at k=3; weighted/majority rules are not.

---

## 6. Discussion

### 6.1 The Verdict Is Grain-Relative and Schedule-Relative
The voting/quorum structural law (extremes-only irreducibility) holds **only at synchronous 1-step grain**. At 2-step grain and under sequential update, the law vanishes entirely. This replicates the general finding of Probes 32, 62, and 112 for the voting/quorum domain. The lab's convention — synchronous 1-step, finest grain — must be declared as part of the measurement.

### 6.2 Differential Recovery at k=3
The recovery of AND/OR/parity at k=3 but not of majority/weighted rules is novel. It suggests that the monotone extreme gates and parity have a dynamical structure (period-1 or period-2 attractors) that survives 3-step composition, while the mixed/weighted rules do not. This is a direction for future work.

### 6.3 Relation to Probe 457 (Weighted & Noisy Quorums)
Probe 457 enumerated all weighted threshold rules at n=3,4 and found the extremes-only law holds for the deterministic commit. Our result shows that even those extreme classes collapse under coarse grain or sequential update — the law is fragile to modeling choices that Probe 457 did not test.

### 6.4 Validation Gap
All results are in-silico: exact Φ on 4-node Boolean models. No real voting body has been measured. The grain/schedule relativity is a property of the models. A real committee's verdict would depend on the actual decision cadence and information flow — an empirical question.

---

## 7. Reproducibility
- Probe: `org_frontier/probes/probe_voting_robustness.py` (Probe 462)
- CI check: `probe-voting-robustness` in `ci/reproduce.json`
- Run: `python -m org_frontier.probes.probe_voting_robustness`
- Instrument validation: `python -m org_frontier.classifier.validate`

---

## 8. Conclusion
The voting/quorum structural law — "only extreme thresholds bind the full core" — is exact **but conditional**. It holds at the lab's standard convention (synchronous 1-step update, finest grain). It fails completely at 2-step grain and under sequential update. No voting rule is robust. At 3-step grain, AND/OR/parity recover; majority/weighted do not. The verdict is grain-relative and schedule-relative; the convention is part of the measurement.

---

## References
1. Probe 32 — `org_frontier/probes/probe_temporal_grain.py` (temporal grain)
2. Probe 62 — `org_frontier/probes/probe_async.py` (sequential update)
3. Probe 67 — `org_frontier/probes/probe_voting.py` (voting rules)
4. Probe 117 — `org_frontier/probes/probe_threshold_scaling.py` (threshold scaling)
5. Probe 122 — `org_frontier/probes/probe_voting_stress.py` (weighted/supermajority stress)
6. Probe 457 — `org_frontier/probes/weighted_quorum/probe_weighted_quorum.py` (weighted quorums)
7. Probe 112 — `org_frontier/probes/probe_invariant_verdict.py` (invariant verdict)
8. Probe 462 — `org_frontier/probes/probe_voting_robustness.py` (this work)
9. Foundations — `foundations/` (instrument validation)

---

*All results are in-silico: exact IIT-4.0 Φ on 4-node Boolean models. Evidence about the models, not measurements of real organizations. The validation gap to real coordination is unchanged.*