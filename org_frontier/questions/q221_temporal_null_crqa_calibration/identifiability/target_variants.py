"""Step-11 audit, part 2: is the P/Q bottleneck difference an artefact of how q161 'removes' a node?
q161 freeze (as implemented): node k's RULE := constant 0, but cm_from_rules / tpm_from_rules still treat k as a
network element whose state PyPhi perturbs uniformly; other nodes keep reading it. Residual = major-complex Phi of
that 3-node network, max over its reachable states.
Alternative (IIT background-condition reading): keep the ORIGINAL network; hold node k fixed at value v as a
background condition (it is outside every candidate subsystem; PyPhi conditions on its current state); residual =
max over states reachable in the original dynamics with x_k = v, and over subsystems S not containing k, of system
phi of S.  Drop_k = base - residual; B = argmax drops (TOL 1e-6).  Reported for v = 0 and 1."""
import itertools

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import bottleneck_set
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES

pyphi.config.PROGRESS_BARS = False
L = ("X", "Y", "H")
TOL = 1e-6
PAIR = {"P = aff(9,6,10)": ("aff", 9, 6, 10), "Q = aff(9,15,10)": ("aff", 9, 15, 10),
        "aff(9,15,12)": ("aff", 9, 15, 12), "aff(9,6,11)": ("aff", 9, 6, 11), "aff(9,14,10)": ("aff", 9, 14, 10)}
# survivor pairs: (P,Q) ; (aff(9,6,10), aff(9,15,12)) ; (aff(9,6,11), aff(9,14,10))


def phi(net, st, nodes):
    try:
        return float(new_big_phi.sia(pyphi.Subsystem(net, st, nodes)).phi)
    except Exception:  # unreachable state for this subsystem
        return None


def background_variant(rules, v):
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=L)
    reach = [tuple((s >> i) & 1 for i in range(3)) for s in reachable_states(tpm, 3)]
    base = max((x for st in reach for r in (1, 2, 3) for S in itertools.combinations(range(3), r)
                for x in [phi(net, st, S)] if x is not None), default=0.0)
    drops = []
    for k in range(3):
        others = [i for i in range(3) if i != k]
        res = [x for st in reach if st[k] == v for r in (1, 2) for S in itertools.combinations(others, r)
               for x in [phi(net, st, S)] if x is not None]
        drops.append(base - (max(res) if res else 0.0))
    mx = max(drops)
    B = set() if mx <= TOL else {i for i, d in enumerate(drops) if abs(d - mx) <= TOL}
    return base, [round(d, 6) for d in drops], sorted(B)


def main():
    for nm, fid in PAIR.items():
        rules = ps.table_form(TABLES[fid])
        B, base, drops = bottleneck_set(rules, L)
        print("== %s  q161 freeze-rule target: base %.3f drops %s B %s" % (nm, base, [round(float(d), 6) for d in drops], sorted(B)))
        for v in (0, 1):
            b, d, Bv = background_variant(rules, v)
            print("   background-condition variant, x_k = %d: base %.3f drops %s B %s" % (v, b, d, Bv))


if __name__ == "__main__":
    main()
