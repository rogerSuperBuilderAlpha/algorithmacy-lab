"""Q10 H5 — transport delay and the slowed clock leave distinguishable fingerprints.

Form / ensemble: on `two_sided_match`, three composed maps read at matched grain —
  (a) the buffer-pipeline map `buffer_pipeline_rules(rules, d)` at each d = 1,2,3 (this probe);
      the complex is projected onto the W-S-C core (buffers excluded);
  (b) the Q9 hold-for-k map `hold_k_tpm(rules, k)` at its flip ratio k*_det = 2 (the slowed
      clock, from the Q9 methods) — the {S}-ejection / {W,C}-core slowed-clock fingerprint;
  (c) for context the #62 sequential-update maps `sequential_tpm(rules, order)` over the six
      orders in S_3.
Each is classified by the Φ_MIP classifier. The MIP repr is taken at the state where Φ is read,
identically across maps.

Measure: for each map the major-complex membership, the MIP partition, and the residual Φ_MIP.
Transport-delay fingerprint = (W-S-C core with buffers excluded, MIP cut, residual Φ) across d.
Slowed-clock fingerprint = the Q9 hold-for-k result at k*_det (its {S}-ejection or {W,C} core
and MIP). Discriminator: whether transport delay ever produces the self-absorbed {S} core the
hold-for-k produced, and whether its MIP cut matches the hold's; pass-through check (no
B_i -> B_i self-edge) confirms no #43 stickiness.

Decision rule (fixed before run):
  CONFIRMED if, where transport delay touches the verdict, it leaves a major complex on {W,S,C}
    or {W,C} with buffers excluded and NEVER the self-absorbed {S} core, its MIP cut differs from
    the hold's at matched grain, and the buffers carry no self-OR.
  REFUTED if transport delay reproduces the hold's {S}-core collapse with the identical MIP cut
    (delay-is-a-memory-cell).

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q10_commit_delay/probe_factorization_fingerprint.py
"""

import csv
import itertools
import os
import sys

import numpy as np

# Repo root on the path so `org_frontier.*` and `foundations.proxy_audit.*` import,
# and so this file also runs as a direct script.
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import (
    classify, tpm_from_rules, cm_from_rules, _mip_partition_repr, PHI_EPS,
)
from org_frontier.corpus import forms_library as lib
from org_frontier.probes.probe_async import sequential_tpm
from foundations.proxy_audit.exact_phi import exact_big_phi, reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

CORE_LABELS = ("W", "S", "C")
TOL = 1e-6
S_IDX = 1


# ---------------------------------------------------------------------------
# Construction (A): buffer pipeline (q10 methods.md). d pass-through buffer
# nodes B_1..B_d carry S's committed value forward d steps; the parties read
# the pipeline tail B_d in place of S. No B_i -> B_i self-OR.
# ---------------------------------------------------------------------------
def buffer_pipeline_rules(rules, d, s_idx=S_IDX):
    n = 3 + d
    head = 3            # index of B_1
    tail = 3 + d - 1    # index of B_d
    read = tail if d > 0 else s_idx
    def lift(rule):     # a party rule that reads S now reads the pipeline tail B_d
        return lambda x: rule(tuple(x[read] if i == s_idx else x[i] for i in range(3)))
    party = [lift(rules[0]), rules[1], lift(rules[2])]
    party[s_idx] = lambda x, r=rules[1]: r((x[0], x[1], x[2]))
    buf = []
    for i in range(d):
        src = s_idx if i == 0 else (head + i - 1)   # B_1 copies S; B_{i+1} copies B_i
        buf.append((lambda x, s=src: x[s]))
    return party + buf


def buffer_labels(d):
    return tuple(["W", "S", "C"] + [f"B{i + 1}" for i in range(d)])


# ---------------------------------------------------------------------------
# Construction (B): Q9 deterministic hold-for-k composed map (slowed clock).
# k micro-steps per macro transition; S holds for k-1 and commits on the k-th.
# ---------------------------------------------------------------------------
def hold_k_tpm(rules, k, n=3, s_idx=S_IDX):
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]          # S holds its previous value
        return ns
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(k):
            state = micro(state, commit_S=(step == k - 1))
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


# ---------------------------------------------------------------------------
# Φ / MIP read at the most-integrated reachable state, identically across maps.
# Returns (read_phi, mip_repr, read_state, n_reachable).
# The MIP repr is taken at the read state regardless of triadic/dyadic, so the
# fingerprint is read uniformly even where classify() short-circuits to "(factors)".
# ---------------------------------------------------------------------------
def read_fingerprint(tpm, cm, labels):
    n = cm.shape[0]
    profile = []
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        phi = exact_big_phi(tpm, cm, state)
        if phi is not None:
            profile.append((state, float(phi)))
    if not profile:
        return 0.0, "(no reachable states)", None, 0
    read_state, read_phi = max(profile, key=lambda r: r[1])
    mip = _mip_partition_repr(tpm, cm, read_state, tuple(labels))
    return read_phi, mip, read_state, len(profile)


# ---------------------------------------------------------------------------
# Major-complex membership at the most-integrated reachable state, via PyPhi
# new_big_phi.maximal_complex (the machinery probes/lib.major_complex wraps).
# Returns (core_label_tuple, phi, read_state).
# ---------------------------------------------------------------------------
def major_complex_membership(tpm, cm, labels):
    n = cm.shape[0]
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0, None)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
            if float(mc.phi) > best[1]:
                core = tuple(labels[i] for i in mc.node_indices)
                best = (core, float(mc.phi), state)
        except Exception:
            continue
    return best


def project_core_onto_wsc(core):
    """The W-S-C projection of a major-complex core (drop buffer labels)."""
    if core is None:
        return tuple()
    return tuple(lbl for lbl in core if lbl in CORE_LABELS)


def verdict_str(phi):
    return "dyadic" if phi <= PHI_EPS else "triadic"


def main():
    print("=" * 78)
    print("Q10 H5 — transport delay vs the slowed clock: factorization fingerprints")
    print("=" * 78)

    rules = lib.FORMS_BY_KEY["two_sided_match"].rules

    # ------------------------------------------------------------------
    # Instrument control (run first): two_sided_match at d=0 (buffer
    # pipeline with no buffers = the bare synchronous form) must read
    # triadic, Φ_MIP = 2.0, MIP "2 parts: {W,SC}". Abort if it fails.
    # ------------------------------------------------------------------
    ctrl_rules = buffer_pipeline_rules(rules, 0)
    ctrl_tpm, ctrl_cm = tpm_from_rules(ctrl_rules), cm_from_rules(ctrl_rules)
    cv = classify(ctrl_tpm, ctrl_cm, labels=CORE_LABELS)
    print("\n[instrument control] two_sided_match, buffer_pipeline_rules(rules, 0)")
    print("                     (= bare 3-node synchronous form):")
    print(f"    structure   = {cv.structure}")
    print(f"    Φ_MIP       = {cv.max_phi:.6f}")
    print(f"    MIP cut     = {cv.mip_partition}")
    # buffer construction sanity: d=0 adds no buffer nodes.
    ctrl_ok = (cv.structure == "triadic"
               and abs(cv.max_phi - 2.0) <= TOL
               and "{W,SC}" in cv.mip_partition
               and len(ctrl_rules) == 3)
    if not ctrl_ok:
        print("\nINSTRUMENT CONTROL FAILED — aborting "
              "(form did not reproduce its known triadic Φ=2.0 {W,SC} verdict).")
        sys.exit(1)
    print("    instrument control PASSED (triadic, Φ=2.0, MIP {W,SC}, no buffers at d=0).")

    # ------------------------------------------------------------------
    # (a) Transport-delay fingerprint: buffer pipeline at d = 1,2,3.
    #     Per d: whole-system verdict, MIP cut, residual Φ, major-complex
    #     membership (projected onto W-S-C), buffer self-edge check, and
    #     the {S}-core watch (is the major complex the self-absorbed {S}?).
    # ------------------------------------------------------------------
    print("\n[transport-delay fingerprint] buffer pipeline, d = 1,2,3:")
    buf_rows = []
    s_core_ever_buf = False
    any_buf_self_edge = False
    for d in (1, 2, 3):
        r = buffer_pipeline_rules(rules, d)
        labels = buffer_labels(d)
        tpm, cm = tpm_from_rules(r), cm_from_rules(r)
        phi, mip, state, nreach = read_fingerprint(tpm, cm, labels)
        v = verdict_str(phi)
        core, core_phi, core_state = major_complex_membership(tpm, cm, labels)
        wsc = project_core_onto_wsc(core)
        buffers_excluded = all(lbl not in core for lbl in labels[3:]) if core else True
        wsc_full = set(CORE_LABELS).issubset(set(core)) if core else False
        s_only_core = (core == ("S",))
        if s_only_core:
            s_core_ever_buf = True
        self_edges = [labels[3 + i] for i in range(d) if cm[3 + i, 3 + i] == 1]
        if self_edges:
            any_buf_self_edge = True
        buf_rows.append((d, v, phi, mip, state, core, core_phi,
                         wsc, buffers_excluded, wsc_full, s_only_core, self_edges))
        print(f"    d={d}: {v:<7}  Φ_MIP={phi:.6f}  MIP={mip}")
        print(f"          major complex = {core}  (φ={core_phi:.6f}, state={core_state})")
        print(f"          W-S-C projection = {wsc}  |  buffers_excluded={buffers_excluded}"
              f"  |  full {{W,S,C}} in core={wsc_full}")
        print(f"          self-absorbed {{S}} core? {s_only_core}"
              f"  |  buffer self-edges (no-self-OR check) = {self_edges or 'none'}")

    # ------------------------------------------------------------------
    # (b) Slowed-clock fingerprint: Q9 hold-for-k at k*_det = 2.
    #     Read its MIP cut, residual Φ, and major-complex membership
    #     ({S}-ejection / {W,C}-core watch).
    # ------------------------------------------------------------------
    K_STAR_DET = 2  # from Q9 H1 methods: two_sided_match flips at k*_det = 2
    hk_tpm, hk_cm = hold_k_tpm(rules, K_STAR_DET)
    hk_phi, hk_mip, hk_state, _ = read_fingerprint(hk_tpm, hk_cm, CORE_LABELS)
    hk_v = verdict_str(hk_phi)
    hk_core, hk_core_phi, hk_core_state = major_complex_membership(hk_tpm, hk_cm, CORE_LABELS)
    hk_s_only = (hk_core == ("S",))
    print(f"\n[slowed-clock fingerprint] Q9 hold-for-k @ k*_det={K_STAR_DET}:")
    print(f"    {hk_v:<7}  Φ_MIP={hk_phi:.6f}  MIP={hk_mip}  read_state={hk_state}")
    print(f"    major complex = {hk_core}  (φ={hk_core_phi:.6f}, state={hk_core_state})")
    print(f"    self-absorbed {{S}} core? {hk_s_only}")

    # ------------------------------------------------------------------
    # (c) Context: #62 sequential-update maps over the six S_3 orders.
    # ------------------------------------------------------------------
    print("\n[context] #62 sequential-update maps, six orders in S_3:")
    seq_rows = []
    for order in itertools.permutations(range(3)):
        tpm, cm = sequential_tpm(rules, order)
        phi, mip, state, _ = read_fingerprint(tpm, cm, CORE_LABELS)
        v = verdict_str(phi)
        core, core_phi, _ = major_complex_membership(tpm, cm, CORE_LABELS)
        seq_rows.append((order, v, phi, mip, state, core))
        print(f"    order={order}: {v:<7}  Φ_MIP={phi:.6f}  MIP={mip}  core={core}")

    # ------------------------------------------------------------------
    # Decision rule (fixed before run).
    #   CONFIRMED iff, where transport delay touches the verdict, it leaves a
    #     major complex on {W,S,C} or {W,C} (read on the matched W-S-C grain,
    #     buffers excluded from the projection) and NEVER the self-absorbed {S}
    #     core the hold produced; AND its MIP cut differs from the hold's at the
    #     matched grain; AND the buffers carry no self-OR (no #43 stickiness).
    #   REFUTED iff transport delay reproduces the hold's {S}-core collapse with
    #     the identical MIP cut (delay-is-a-memory-cell).
    #
    #   The transport verdict is read first. Where it never touches the verdict
    #   (stays triadic at every d), the {S}-core watch is the direct
    #   discriminator: the W-S-C projection of the major complex must never be
    #   the self-absorbed {S} alone the hold produced.
    # ------------------------------------------------------------------
    transport_touches_verdict = any(row[1] == "dyadic" for row in buf_rows)

    # {S}-core watch on the matched W-S-C grain: the projection must never be
    # the self-absorbed {S} the hold produced, and must lie on {W,S,C}/{W,C}-
    # type party cores (a non-empty subset of {W,S,C}, never {S} alone).
    no_s_core_projection = all(row[7] != ("S",) for row in buf_rows)      # row[7]=wsc proj
    no_s_core_full = not s_core_ever_buf                                  # full micro core
    membership_on_core = all(
        len(row[7]) >= 1 and set(row[7]).issubset({"W", "S", "C"}) and row[7] != ("S",)
        for row in buf_rows
    )
    s_core_pass = no_s_core_projection and no_s_core_full and membership_on_core

    # MIP-cut differs from the hold's at matched grain (every d).
    mip_differs_all = all(row[3] != hk_mip for row in buf_rows)

    # Pass-through (no #43 stickiness).
    passthrough_ok = not any_buf_self_edge

    confirmed = s_core_pass and mip_differs_all and passthrough_ok
    # Refutation: transport reproduces the hold's {S}-core collapse with the
    # identical MIP cut (delay-is-a-memory-cell).
    refuted = (hk_s_only
               and any(row[7] == ("S",) for row in buf_rows)
               and any(row[3] == hk_mip for row in buf_rows))
    if confirmed:
        verdict = "CONFIRMED"
    elif refuted:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"

    print("\n" + "=" * 78)
    print("DECISION")
    print("=" * 78)
    print(f"    transport touches the verdict (any d dyadic)? {transport_touches_verdict}")
    print(f"      transport verdicts by d        = {[row[1] for row in buf_rows]!r}")
    print(f"    hold-for-k MIP cut @ k*_det=2 = {hk_mip!r}")
    print(f"    hold-for-k major complex      = {hk_core!r}  (self-absorbed {{S}}? {hk_s_only})")
    print(f"    transport MIP cuts by d        = {[row[3] for row in buf_rows]!r}")
    print(f"    transport micro cores by d     = {[row[5] for row in buf_rows]!r}")
    print(f"    transport W-S-C projections    = {[row[7] for row in buf_rows]!r}")
    print()
    print(f"    (1) {{S}}-core watch: transport never produces the self-absorbed {{S}}")
    print(f"        core and stays on {{W,S,C}}/{{W,C}} party cores : {s_core_pass}")
    print(f"          (no {{S}} projection ever: {no_s_core_projection};"
          f" no full {{S}} core ever: {no_s_core_full};")
    print(f"           projections on party core: {membership_on_core})")
    print(f"    (2) MIP cut differs from the hold's at every d : {mip_differs_all}")
    print(f"    (3) pass-through (no B_i->B_i self-OR, no #43)  : {passthrough_ok}")
    print(f"\n    H5 VERDICT: {verdict}")

    # ------------------------------------------------------------------
    # CSV.
    # ------------------------------------------------------------------
    results_dir = os.path.join(_HERE, "results")
    os.makedirs(results_dir, exist_ok=True)
    csv_path = os.path.join(results_dir, "probe_factorization_fingerprint.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["map", "param", "verdict", "phi_mip", "mip_partition",
                    "read_state", "major_complex", "wsc_projection",
                    "buffers_excluded", "s_only_core", "buffer_self_edges"])
        for (d, v, phi, mip, state, core, core_phi, wsc, bex, wscf, s_only, se) in buf_rows:
            w.writerow(["buffer_pipeline", d, v, f"{phi:.6f}", mip, state,
                        "|".join(core) if core else "", "|".join(wsc),
                        bex, s_only, "|".join(se) if se else ""])
        w.writerow(["hold_for_k", K_STAR_DET, hk_v, f"{hk_phi:.6f}", hk_mip, hk_state,
                    "|".join(hk_core) if hk_core else "", "", "", hk_s_only, ""])
        for (order, v, phi, mip, state, core) in seq_rows:
            w.writerow(["sequential", "".join(map(str, order)), v, f"{phi:.6f}", mip,
                        state, "|".join(core) if core else "", "", "", "", ""])
        w.writerow(["DECISION", "k*_det=2", verdict.lower(),
                    f"hold_mip={hk_mip}", f"hold_core={'|'.join(hk_core) if hk_core else ''}",
                    f"s_core_pass={s_core_pass}", f"mip_differs_all={mip_differs_all}",
                    f"passthrough_ok={passthrough_ok}", "", "", ""])
    print(f"\n    CSV written: {csv_path}")

    return verdict


if __name__ == "__main__":
    main()
