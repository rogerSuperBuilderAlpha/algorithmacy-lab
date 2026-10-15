"""Exact rational all-lag recurrence certificate for the Q221 lead affine pair.

Run from repo root:
python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.exact_all_lags_certificate
No PyPhi dependency. The externally reported q161 target sets are NOT recomputed here.
"""
from fractions import Fraction
from itertools import permutations
import argparse
import json

BITS = tuple(tuple((s >> j) & 1 for j in range(3)) for s in range(8))
NOISE = Fraction(2, 25)
LEAD_A = (9, 6, 10)
LEAD_B = (9, 15, 10)

def rule_value(code, s):
    mask, bias = divmod(code, 2)
    return ((s & mask).bit_count() & 1) ^ bias

def tables(codes):
    return tuple(tuple(rule_value(code, s) for s in range(8)) for code in codes)

def transition(codes):
    tab = tables(codes)
    P = []
    for s in range(8):
        row = []
        for z in range(8):
            prob = Fraction(1)
            for j in range(3):
                prob *= (1 - NOISE) if tab[j][s] == BITS[z][j] else NOISE
            row.append(prob)
        assert sum(row) == 1
        P.append(tuple(row))
    assert all(sum(P[s][z] for s in range(8)) == 1 for z in range(8))
    return tuple(P)

def matmul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(8)), Fraction(0))
                       for j in range(8)) for i in range(8))

def identity():
    return tuple(tuple(Fraction(int(i == j)) for j in range(8)) for i in range(8))

def recurrence(P, max_lag=15):
    # Uniform stationary law follows from exact column normalization above.
    Pk = identity()
    result = {}
    for k in range(max_lag + 1):
        for i in range(3):
            for j in range(3):
                result[(i, j, k)] = sum(
                    (Fraction(1, 8) * Pk[s][z]
                     for s in range(8) for z in range(8)
                     if BITS[s][i] == BITS[z][j]), Fraction(0))
        Pk = matmul(Pk, P)
    return result

def reconstruct_rules_from_one_step_marginals(P):
    """Recover deterministic per-node rule table from fully observed noisy TPM.

    Since Pr(next node j = 1 | current state s) is NOISE or 1-NOISE
    (with NOISE=2/25 < 1/2), thresholding at 1/2 recovers every rule bit.
    """
    means = tuple(tuple(sum((P[s][z] for z in range(8) if BITS[z][j]),
                            Fraction(0)) for s in range(8)) for j in range(3))
    assert all(v in (NOISE, 1-NOISE) for row in means for v in row)
    return tuple(tuple(int(v > Fraction(1, 2)) for v in row) for row in means)

def transform(tab, perm, mask):
    out = [[0] * 8 for _ in range(3)]
    for state in range(8):
        old = sum(((((state >> perm[k]) & 1) ^ ((mask >> k) & 1)) << k)
                  for k in range(3))
        for j in range(3):
            out[perm[j]][state] = tab[j][old] ^ ((mask >> j) & 1)
    return tuple(tuple(row) for row in out)

def certificate():
    a, b = transition(LEAD_A), transition(LEAD_B)
    ra, rb = recurrence(a), recurrence(b)
    assert a != b and ra == rb and len(ra) == 144
    eq = [(list(perm), mask) for perm in permutations(range(3))
          for mask in range(8)
          if transform(tables(LEAD_A), perm, mask) == tables(LEAD_B)]
    assert not eq
    assert reconstruct_rules_from_one_step_marginals(a) == tables(LEAD_A)
    assert reconstruct_rules_from_one_step_marginals(b) == tables(LEAD_B)
    return {
        "status": "exact mathematical verification (no PyPhi run)",
        "candidate_ids": {"P": list(LEAD_A), "Q": list(LEAD_B)},
        "noise": "2/25",
        "state_order": "little endian: X + 2Y + 4H",
        "stationary_distribution": "uniform (verified by exact column sums)",
        "exact_components_equal_lags_0_to_15": len(ra),
        "equality_exact": True,
        "all_lag_proof": ("Cayley-Hamilton: each scalar profile satisfies the degree-8 "
                          "characteristic recurrence of its own 8x8 TPM. "
                          "The difference satisfies the monic order-16 recurrence "
                          "formed by multiplying the two characteristic polynomials. "
                          "Sixteen initial zero values imply equality for every k>=0. "
                          "Stationarity gives r_ij(-k)=r_ji(k)."),
        "state_conditional_one_step_means_recover_all_rule_bits": True,
        "sufficient_information_statement": ("Full-state one-step per-node conditional "
          "means recover every deterministic rule bit by thresholding at 1/2 "
          "under independent flip noise epsilon<1/2; not claimed minimal."),
        "checked_symmetries": 48,
        "isomorphisms_found": eq,
        "reported_q161_bottleneck_sets_not_computed_here": {"P": [0, 2], "Q": [2]},
        "shared_correct_node": 2,
        "limitation": ("Cannot recover both complete bottleneck sets from identical "
                       "population profiles, but choosing H is correct for both under "
                       "single-node membership scoring. This does not assert equality "
                       "of full trajectory laws or finite-sample feature distributions.")
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    result = certificate()
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
            fh.write("\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
