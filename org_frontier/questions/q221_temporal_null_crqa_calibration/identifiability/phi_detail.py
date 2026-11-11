"""Exact IIT-4.0 targets for the A/B systems with the lab's own functions (read-only imports from q161,
probes.lib, classifier), plus a per-state / per-candidate-subsystem listing to expose ties, and the exact
conditional mutual information I(H_{t+1}; X_t, Y_t | H_t) of the noisy q220 generator."""
import itertools
import math
import numpy as np
import pyphi
from pyphi import new_big_phi, exceptions

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
    core_indices, bottleneck_set, mc_phi)
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import exact_profiles as ep

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
L = ("X", "Y", "H")
SYSTEMS = {
    "A_self": [lambda x: x[0], lambda x: x[1], lambda x: x[2]],
    "B_xor":  [lambda x: x[0], lambda x: x[1], lambda x: x[0] ^ x[1]],
}
print("pyphi config: IIT_VERSION=%s REPERTOIRE_DISTANCE=%s" % (
    getattr(pyphi.config, "IIT_VERSION", "?"), getattr(pyphi.config, "REPERTOIRE_DISTANCE", "?")))


def cmi_h(rules, flip=ep.FLIP):
    """Exact I(H_{t+1}; X_t, Y_t | H_t) in bits under the stationary law of the noisy chain."""
    P = ep.noisy_sbs(rules, flip)
    pi = ep.stationary(P)
    joint = {}
    for s in range(8):
        x, y, h = ep.bits(s, 3)
        for s2 in range(8):
            h2 = ep.bits(s2, 3)[2]
            joint[(x, y, h, h2)] = joint.get((x, y, h, h2), 0) + pi[s] * P[s, s2]

    def marg(keep):
        m = {}
        for k, v in joint.items():
            kk = tuple(k[i] for i in keep)
            m[kk] = m.get(kk, 0) + v
        return m
    p_h, p_xyh, p_hh2 = marg([2]), marg([0, 1, 2]), marg([2, 3])
    I = 0.0
    for (x, y, h, h2), v in joint.items():
        if v > 0:
            I += v * math.log2(v * p_h[(h,)] / (p_xyh[(x, y, h)] * p_hh2[(h, h2)]))
    return I


h2 = lambda p: -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
for name, rules in SYSTEMS.items():
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    print("=" * 70, "\n", name)
    print("TPM (state-by-node, little-endian rows s=0..7):", tpm.astype(int).tolist())
    print("CM (cm[i,j]=1 iff j reads i):", cm.tolist())
    v = verdict(rules, L)
    print("verdict: structure=%s max_phi=%s" % (v.structure, v.max_phi))
    print("q161 core_indices:", core_indices(rules, L), " mc_phi:", mc_phi(rules, L))
    bset, base, drops = bottleneck_set(rules, L)
    print("q161 bottleneck_set: B=%s base=%.6f drops=%s" % (sorted(bset), base, [round(d, 6) for d in drops]))
    net = pyphi.Network(tpm, cm=cm, node_labels=L)
    rs = reachable_states(tpm, 3)
    print("reachable states:", rs)
    for s in rs:
        st = ep.bits(s, 3)
        mc = new_big_phi.maximal_complex(net, st)
        mcs = "null" if isinstance(mc, new_big_phi.NullPhiStructure) else "%s phi=%.4f" % (
            tuple(L[i] for i in mc.node_indices), float(mc.phi))
        subs = []
        for r in (1, 2, 3):
            for nodes in itertools.combinations(range(3), r):
                try:
                    sub = pyphi.Subsystem(net, st, nodes)
                    phi = float(new_big_phi.phi_structure(sub).big_phi) if hasattr(new_big_phi, "phi_structure") else float("nan")
                except Exception as e:
                    phi = float("nan")
                try:
                    sia = new_big_phi.sia(pyphi.Subsystem(net, st, nodes))
                    phi = float(sia.phi)
                except Exception as e:
                    pass
                subs.append("%s:%.3f" % ("".join(L[i] for i in nodes), phi))
        print("  state %s  maximal_complex=%s  | system-phi(sia) per candidate: %s" % (st, mcs, " ".join(subs)))
    for k in range(3):
        frozen = list(rules)
        frozen[k] = (lambda x: 0)
        print("  clamp %s->0: core=%s mc_phi=%.4f" % (L[k], core_indices(frozen, L), mc_phi(frozen, L)))
    print("CMI I(H';X,Y|H) = %.6f bits ; 1-h2(0.08) = %.6f" % (cmi_h(rules), 1 - h2(0.08)))
    print("CMI noiseless-rule limit (flip 1e-9) = %.6f" % cmi_h(rules, 1e-9))
