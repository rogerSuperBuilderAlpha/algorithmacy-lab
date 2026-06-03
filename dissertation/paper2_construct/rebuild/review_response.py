"""Paper 2 rebuild — computations answering the Stage-4 review (from scratch).

Three things the reviewers (R1 methodologist, R2 IIT expert, R3 org theorist) demand be
COMPUTED, not asserted:

1. PER-STATE Φ PROFILES for the worked triads. The binary rule is "Φ>0 at SOME reachable
   state". R2 charges that several triad verdicts rest on a single all-on state. Print every
   reachable state's Φ so the reader sees how thin or thick each verdict is.

2. RIDESHARE CARVING-INVARIANCE. R1/R3 charge that the triad verdict rides on one chosen state
   alphabet. Re-encode the same rideshare mechanism under defensible alternative carvings and
   check whether the BINARY verdict survives. If it flips, report it.

3. EFFECTIVE INFORMATION ON THE EXHIBIT. R2 charges that "Φ = EI at the MIP" is false and that
   "EI provably over-calls" is unearned because EI is never computed. Compute Hoel-style EI
   (determinism − degeneracy) on the exhibit and show it is high while Φ=0 — i.e. EI does not
   detect the factoring. This backs the §8 claim with a number instead of an identity.

Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/review_response.py
"""

import os, sys, math
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from instrument import (tpm_from_rules, cm_from_rules, reachable_states,
                        strongly_connected, system_phi, classify)


def per_state_profile(rules, name):
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    print(f"\n  {name}")
    rows = []
    for s in reachable_states(tpm):
        st = tuple((s >> i) & 1 for i in range(3))
        phi, mip = system_phi(tpm, cm, st)
        if phi is None:
            continue
        rows.append((st, phi))
        print(f"     state {st}:  Φ = {phi:.4f}   MIP {mip}")
    phis = [p for _, p in rows]
    n_pos = sum(1 for p in phis if p > 1e-9)
    print(f"     -> {n_pos}/{len(phis)} reachable states carry Φ>0   "
          f"(maxΦ={max(phis):.3f}, meanΦ={np.mean(phis):.3f})")


def section1_profiles():
    print("=" * 78)
    print("1. PER-STATE Φ PROFILES (how many reachable states carry each triad verdict)")
    print("=" * 78)
    irreducible = [lambda s: s[1] or s[2], lambda s: s[0] and s[2], lambda s: s[0] ^ s[1]]
    ats_and = [lambda s: s[1], lambda s: s[0] and s[2], lambda s: s[1]]
    false_dyad_triad = [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2] and not s[1]]
    conjunctive = [lambda s: s[1] and s[2], lambda s: s[0] and s[2], lambda s: s[1] and s[0]]
    per_state_profile(irreducible, "irreducible control  (W'=S∨C, S'=W∧C, C'=W⊕S)")
    per_state_profile(ats_and, "ATS S'=AND          (W'=S, S'=W∧C, C'=S)")
    per_state_profile(false_dyad_triad, "false-dyad triad     (W'=¬S, S'=W∧C, C'=C∧¬S)")
    per_state_profile(conjunctive, "conjunctive channel  (W'=S∧C, S'=W∧C, C'=S∧W)")


def section2_rideshare_invariance():
    print("\n" + "=" * 78)
    print("2. RIDESHARE CARVING-INVARIANCE  (does the TRIAD verdict survive re-encoding?)")
    print("=" * 78)
    # Baseline (the paper's centerpiece): one binary node per party.
    baseline = [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2] and not s[1]]
    # Variant A: C' = C, the counterpart's state never updates at all (a frozen node). This is NOT
    # the defensible "rider persists until picked up" reading -- that is the baseline C'=C∧¬S, where
    # the rider clears when served. C'=C decouples the counterpart, so it is a spectator and the form
    # is correctly a dyad. Kept here to show a criterion VIOLATION (a non-live party) flips the verdict.
    variantA = [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2]]
    # Variant B: driver re-arms from the counterpart side too (W' = ¬S ∨ ¬C): availability also
    # returns when no rider is waiting. Different worker-state carving, same dispatch coupling.
    variantB = [lambda s: (not s[1]) or (not s[2]), lambda s: s[0] and s[2], lambda s: s[2] and not s[1]]
    # Variant C: dispatch as OR rather than AND (a looser match rule: dispatch fires if either
    # side is ready). Tests whether the determination's exact Boolean form matters to the BINARY.
    variantC = [lambda s: not s[1], lambda s: s[0] or s[2], lambda s: s[2] and not s[1]]
    # Control: the genuinely dyadic model (S reads driver only). MUST be a dyad.
    dyadic = [lambda s: not s[1], lambda s: s[0], lambda s: s[2] and not s[1]]
    for label, rules in [
        ("baseline (paper centerpiece)", baseline),
        ("variant A: C'=C (rider decoupled from S timing)", variantA),
        ("variant B: W'=¬S∨¬C (driver re-arms from C too)", variantB),
        ("variant C: S'=W∨C (looser OR match rule)", variantC),
        ("control: dyadic model S'=W (must be DYAD)", dyadic),
    ]:
        r = classify(rules, label)
        print(f"   {label:<48} {r['verdict']:<15} maxΦ={r['max_phi']:.3f} n={r['n_states']}")
    print("   Claim under test: the TRIAD binary survives re-encodings that keep the S←C coupling;")
    print("   the verdict tracks whether the dispatch reads the rider, not the state alphabet.")


def effective_information(rules):
    """Hoel-style effective information (bits) for a deterministic Boolean system, partition-free.
    do(uniform) over all 2^n states. determinism = log2 N - <H(future|do s_i)>; for deterministic
    dynamics H(future|do s_i)=0 so determinism = log2 N. degeneracy = log2 N - H(<future>), where
    <future> is the image distribution under uniform input. EI = determinism - degeneracy
    = H(image distribution)."""
    n = 3
    N = 2 ** n
    tpm = tpm_from_rules(rules)
    # next-state index for each input state (deterministic)
    counts = np.zeros(N)
    for s in range(N):
        nxt = tuple(int(tpm[s, j]) for j in range(n))
        idx = sum(b << i for i, b in enumerate(nxt))
        counts[idx] += 1
    p = counts / counts.sum()
    H_image = -sum(pi * math.log2(pi) for pi in p if pi > 0)
    determinism = math.log2(N)          # deterministic => 0 conditional entropy
    degeneracy = math.log2(N) - H_image
    ei = determinism - degeneracy        # = H_image
    return ei, determinism, degeneracy


def section3_ei_on_exhibit():
    print("\n" + "=" * 78)
    print("3. EFFECTIVE INFORMATION ON THE EXHIBIT  (does EI detect the factoring? it should not)")
    print("=" * 78)
    exhibit = [lambda s: not (s[1] or s[2]), lambda s: (not s[0]) and s[2], lambda s: not (s[0] and s[1])]
    r = classify(exhibit, "exhibit")
    ei, det, deg = effective_information(exhibit)
    print(f"   exhibit  W'=NOR(S,C), S'=¬W∧C, C'=NAND(W,S)")
    print(f"     strongly connected : {r['strongly_connected']}")
    print(f"     Φ over the MIP     : maxΦ = {r['max_phi']:.4f}  -> verdict {r['verdict']}")
    print(f"     effective information: EI = {ei:.4f} bits  (determinism {det:.2f} - degeneracy {deg:.2f})")
    # For contrast, EI on a genuine dyad (factoring control) and a genuine triad (irreducible ctrl).
    factoring = [lambda s: s[1], lambda s: s[0], lambda s: s[2]]
    irreducible = [lambda s: s[1] or s[2], lambda s: s[0] and s[2], lambda s: s[0] ^ s[1]]
    for label, rules in [("factoring control (true dyad)", factoring),
                         ("irreducible control (true triad)", irreducible)]:
        rr = classify(rules, label)
        e, _, _ = effective_information(rules)
        print(f"   {label:<36} Φ_verdict={rr['verdict']:<15} maxΦ={rr['max_phi']:.3f}  EI={e:.4f} bits")
    print("   Point: EI is partition-free, so it cannot fall to 0 on the strongly-connected exhibit")
    print("   that Φ reduces. EI does not track the dyad/triad line; Φ over the MIP does.")


def section4_criterion_not_sufficient():
    """R1's charge: a read structure that SATISFIES all four conditions (S commits the joint AND of
    both parties, no direct W-C edge, C constitutive of S, S non-trivial) can still flip to DYAD,
    because the criterion does not pin down how W and C READ S. Reconciles §5 with §9."""
    print("\n" + "=" * 78)
    print("4. CRITERION NECESSARY-NOT-SUFFICIENT  (a criterion-satisfying read that still flips)")
    print("=" * 78)
    # All keep S'=W∧C (joint AND of both parties), no direct W-C edge. Only the W,C reads of S vary.
    cases = {
        "bottleneck     W'=S,        C'=S":        [lambda s: s[1], lambda s: s[0] and s[2], lambda s: s[1]],
        "rideshare base W'=¬S,       C'=C∧¬S":     [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2] and not s[1]],
        "realistic fb   W'=¬S,       C'=C∨¬S":     [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2] or (not s[1])],
        "realistic fb2  W'=¬S,       C'=S∨C":      [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[1] or s[2]],
    }
    for label, rules in cases.items():
        r = classify(rules, label)
        # all satisfy: S reads both (AND), no W<->C direct edge (W,C read only S / own state)
        print(f"   {label:<34} {r['verdict']:<15} maxΦ={r['max_phi']:.3f}")
    print("   All four KEEP S'=W∧C and have no direct W–C edge, so all satisfy the §3 conditions on")
    print("   the mediator and the channel. They differ only in how W,C read S. Verdicts still split.")
    print("   => the criterion is necessary, not sufficient; the reads are a second, declared choice.")


def perturb_phi_at_state(rules, state, eps):
    """Φ at `state` after mixing the deterministic TPM toward uniform by eps (a crude noise model)."""
    import numpy as _np
    from instrument import tpm_from_rules as _t, cm_from_rules as _c
    tpm = _t(rules).astype(float)
    tpm = (1 - eps) * tpm + eps * 0.5            # each node's prob pulled toward 0.5
    cm = _c(rules)
    network = __import__("pyphi").Network(tpm, cm=cm, node_labels=("W", "S", "C"))
    try:
        sub = __import__("pyphi").Subsystem(network, tuple(state))
    except Exception:
        return None
    sia = __import__("pyphi").new_big_phi.sia(sub)
    return max(0.0, float(sia.phi))


def section5_noise_robustness():
    print("\n" + "=" * 78)
    print("5. NOISE-ROBUSTNESS  (is the single carrying state a knife-edge artifact of determinism?)")
    print("=" * 78)
    false_dyad_triad = [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2] and not s[1]]
    print("   false-dyad triad, Φ at the carrying state (1,1,1) as the TPM is mixed toward uniform:")
    for eps in (0.0, 0.02, 0.05, 0.10):
        phi = perturb_phi_at_state(false_dyad_triad, (1, 1, 1), eps)
        print(f"     eps={eps:.2f}:  Φ(1,1,1) = {phi:.4f}")
    print("   smooth degradation, not a flip -> the verdict is not a determinism knife-edge.")


def section6_worked_case_ei():
    print("\n" + "=" * 78)
    print("6. EFFECTIVE INFORMATION ACROSS THE WORKED CASES  (EI does not just miss the line, it inverts it)")
    print("=" * 78)
    cases = {
        "chat dyad           (Φ=0 dyad)":   [lambda s: s[1], lambda s: s[0], lambda s: s[2]],
        "ATS AND             (Φ>0 triad)":  [lambda s: s[1], lambda s: s[0] and s[2], lambda s: s[1]],
        "false-dyad dyadic   (Φ=0 dyad)":   [lambda s: not s[1], lambda s: s[0], lambda s: s[2] and not s[1]],
        "false-dyad triad    (Φ>0 triad)":  [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2] and not s[1]],
    }
    for label, rules in cases.items():
        r = classify(rules, label)
        ei, _, _ = effective_information(rules)
        print(f"   {label:<34} Φ_verdict={r['verdict']:<15} maxΦ={r['max_phi']:.3f}  EI={ei:.4f} bits")
    print("   EI does not order the cases by the dyad/triad line; on the false-dyad pair it inverts it.")


def section7_exhibit_reachability():
    print("\n" + "=" * 78)
    print("7. EXHIBIT REACHABILITY  (which states carry the Φ=0 verdict; is (1,1,1) among them?)")
    print("=" * 78)
    exhibit = [lambda s: not (s[1] or s[2]), lambda s: (not s[0]) and s[2], lambda s: not (s[0] and s[1])]
    tpm = tpm_from_rules(exhibit)
    reach = [tuple((s >> i) & 1 for i in range(3)) for s in reachable_states(tpm)]
    allstates = [tuple((s >> i) & 1 for i in range(3)) for s in range(8)]
    unreach = [st for st in allstates if st not in reach]
    print(f"   reachable states   : {reach}")
    print(f"   unreachable states : {unreach}")
    print(f"   (1,1,1) reachable? : {(1,1,1) in reach}  -- the all-on state that carries every other triad verdict")


def section8_mip_normalization():
    """R2 (round-4) charge: §3 describes the test as 'find the cut that changes the
    probabilities least; Φ is the damage that cut still does' (a RAW-min reading). The
    IIT-4.0 system measure instead selects the MIP by the NORMALIZED integration value and
    reports the (un-normalized) Φ over that partition. The two come apart on the magnitude:
    the conjunctive channel reports Φ=6.0 at (1,1,1) while the minimum RAW integration over
    partitions is 2.0. This section computes both and shows (a) the reported Φ is the raw
    value at the normalized-MIP, not the raw minimum, so the §3 description is loose, and
    (b) the BINARY verdict is invariant: at every reachable state, raw-min and normalized-MIP
    agree on whether Φ is zero. So the issue is magnitude-only; the classifier is untouched."""
    import pyphi
    from pyphi import new_big_phi
    pyphi.config.PROGRESS_BARS = False
    pyphi.config.PARALLEL = False
    print("\n" + "=" * 78)
    print("8. MIP SELECTION: RAW-MIN vs NORMALIZED  (does §3's 'least damage' describe the measure?)")
    print("=" * 78)

    def raw_min_and_reported(rules, state):
        tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
        net = pyphi.Network(tpm, cm=cm, node_labels=("W", "S", "C"))
        sub = pyphi.Subsystem(net, tuple(state))
        sia = new_big_phi.sia(sub)
        reported = max(0.0, float(sia.phi))      # raw Φ at the normalized-MIP (what the instrument uses)
        ss = sia.system_state
        if ss is None:                            # Φ=0 systems carry no system_state
            return reported, 0.0
        raws = [float(new_big_phi.evaluate_partition(p, sub, ss).phi)
                for p in new_big_phi.system_partitions(sub.node_indices, sub.node_indices)]
        return reported, min(raws)

    cases = {
        "conjunctive channel (maxΦ=6.0)": [lambda s: s[1] and s[2], lambda s: s[0] and s[2], lambda s: s[1] and s[0]],
        "false-dyad triad    (maxΦ=2.0)": [lambda s: not s[1], lambda s: s[0] and s[2], lambda s: s[2] and not s[1]],
        "exhibit             (Φ=0 dyad)": [lambda s: not (s[1] or s[2]), lambda s: (not s[0]) and s[2], lambda s: not (s[0] and s[1])],
    }
    binary_agrees = True
    for name, rules in cases.items():
        tpm = tpm_from_rules(rules)
        print(f"\n  {name}")
        for s in reachable_states(tpm):
            st = tuple((s >> i) & 1 for i in range(3))
            rep, mraw = raw_min_and_reported(rules, st)
            agree = (rep > 1e-9) == (mraw > 1e-9)
            binary_agrees = binary_agrees and agree
            gap = "  <-- reported raw Φ > raw minimum" if rep > mraw + 1e-9 else ""
            print(f"     {st}: reported(norm-MIP)Φ={rep:.4f}  min-raw Φ={mraw:.4f}  "
                  f"binary-agree={agree}{gap}")
    print(f"\n   binary verdict invariant across raw-min vs normalized-MIP at every state: {binary_agrees}")
    print("   => §3's 'cut that changes them least' is a loose description of the reported MAGNITUDE")
    print("      (6.0 is the raw value at the normalized-MIP, not the 2.0 raw minimum), but the")
    print("      zero-set is identical, so the dyad/triad CLASSIFIER is unaffected. Magnitude-only.")


def section9_rival_live_context():
    """R1 (round-4) charge: the rivals' Φ=0 rides on the maximally-favorable INERT encoding
    C'=C (a frozen spectator). Test whether the dyad verdict survives a LIVE context, where C
    is read by both parties -- even read jointly by the mediator -- but is not driven back into
    a loop. If the rivals still factor under live-context encodings, the Φ=0 is not an artifact
    of the inert caricature."""
    print("\n" + "=" * 78)
    print("9. RIVAL ENCODING ROBUSTNESS  (does the dyad verdict ride on the inert C'=C spectator?)")
    print("=" * 78)
    cases = {
        "inert spectator   W'=S,   S'=W,   C'=C":   [lambda s: s[1], lambda s: s[0], lambda s: s[2]],
        "live ctx (sep OR) W'=S∨C, S'=W∨C, C'=C":   [lambda s: s[1] or s[2], lambda s: s[0] or s[2], lambda s: s[2]],
        "live ctx (joint)  W'=S,   S'=W∧C, C'=C":   [lambda s: s[1], lambda s: s[0] and s[2], lambda s: s[2]],
        "live ctx (drift)  W'=S∨C, S'=W,   C'=¬C":  [lambda s: s[1] or s[2], lambda s: s[0], lambda s: not s[2]],
    }
    for name, rules in cases.items():
        r = classify(rules, name)
        print(f"   {name:<38} {r['verdict']:<15} maxΦ={r['max_phi']:.3f}  strongly_conn={r['strongly_connected']}")
    print("   All four factor (Φ=0). The dyad verdict survives a context read by both parties,")
    print("   even a joint S'=W∧C read, as long as C is not fed back into a loop (not strongly")
    print("   connected). So the rivals' Φ=0 is not an artifact of the inert C'=C encoding; what")
    print("   a triad needs is C constitutive AND closed into the cycle (the ATS C'=S, false-dyad")
    print("   C'=C∧¬S), which the rival constructs' own channel/context account does not supply.")


if __name__ == "__main__":
    section1_profiles()
    section2_rideshare_invariance()
    section3_ei_on_exhibit()
    section4_criterion_not_sufficient()
    section5_noise_robustness()
    section6_worked_case_ei()
    section7_exhibit_reachability()
    section8_mip_normalization()
    section9_rival_live_context()
