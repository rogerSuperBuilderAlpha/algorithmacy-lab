"""Equality (2): exact equivalence of observed-process LAWS L(Y_0:T) for ALL T, for the lead pair P/Q, where Y is a
coordinate projection of the stationary noisy chain (one channel, a pair of channels, or all three).
Method: each projected process is a hidden Markov process (state x, emission y = proj(x)). Two such processes have
identical laws for every T iff the linear functionals f_w = pi M(w_1) ... M(w_T) 1 agree for every string w. Exact
decision by the Tzeng / Schutzenberger span algorithm: BFS over strings maintaining a basis (exact rationals) of
span{(pi_P M_P(w), pi_Q M_Q(w))}; the laws agree iff every basis vector v satisfies v . (1, -1) = 0. The span
has dimension <= 16, so the BFS terminates. M_y(x, x') = P(x, x') 1[proj(x') = y]; initial vector pi restricted to
proj(x) = y_0 is handled by starting from (pi * 1[proj = y]) for every y."""
from fractions import Fraction
from itertools import combinations

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES, tpm, stationary

P_ID, Q_ID = ("aff", 9, 6, 10), ("aff", 9, 15, 10)


def proj(s, chans):
    return tuple((s >> c) & 1 for c in chans)


def reduce(v, basis):
    v = list(v)
    for piv, b in basis:
        if v[piv] != 0:
            f = v[piv] / b[piv]
            v = [a - f * c for a, c in zip(v, b)]
    return v


def equivalent(chans, a=P_ID, b=Q_ID):
    Ps, pis = [], []
    for fid in (a, b):
        M = tpm(TABLES[fid]); Ps.append(M); pis.append(stationary(M))
    ys = sorted({proj(s, chans) for s in range(8)})

    def step(vec, y):  # vec = (vP[8], vQ[8]) -> apply M_y to both
        out = []
        for k in range(2):
            v = vec[8 * k: 8 * k + 8]
            out += [sum(v[s] * Ps[k][s][z] for s in range(8)) if proj(z, chans) == y else Fraction(0) for z in range(8)]
        return out

    basis, queue = [], []
    for y in ys:
        v = [pis[k][s] if proj(s, chans) == y else Fraction(0) for k in range(2) for s in range(8)]
        queue.append(v)
    nvec = 0
    while queue:
        v = queue.pop(0)
        r = reduce(v, basis)
        if any(x != 0 for x in r):
            piv = next(i for i, x in enumerate(r) if x != 0)
            basis.append((piv, r))
            nvec += 1
            for y in ys:
                queue.append(step(v, y))
    # law equality <=> every spanning vector gives equal total mass in P and Q blocks
    ok = all(sum(b[:8]) == sum(b[8:]) for _, b in basis)
    return ok, nvec


def main():
    names = "XYH"
    print("sanity: P vs P (all channels) equal: %s ; Hassan's isomorphic pair aff(6,9,5)/aff(11,9,5), X only: %s ; "
          "first candidate nsi(0,3,3)/aff(6,9,5), X only: %s"
          % (equivalent((0, 1, 2), P_ID, P_ID)[0], equivalent((0,), ("aff", 6, 9, 5), ("aff", 11, 9, 5))[0],
             equivalent((0,), ("nsi", 0, 3, 3), ("aff", 6, 9, 5))[0]))
    for r in (1, 2, 3):
        for chans in combinations(range(3), r):
            ok, d = equivalent(chans)
            print("observed channels %-3s: law of the projected process equal for ALL T: %s (span dim %d)"
                  % ("".join(names[c] for c in chans), ok, d))


if __name__ == "__main__":
    main()
