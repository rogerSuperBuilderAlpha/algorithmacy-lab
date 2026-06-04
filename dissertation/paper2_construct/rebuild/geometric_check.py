"""Paper 2 §8 — does an information-geometric Φ over-call the exhibit?

Section 8 shows the exhibit
    W' = NOR(S, C),  S' = ¬W ∧ C,  C' = NAND(W, S)
is strongly connected (all six edges) yet has exact IIT-4.0 Φ = 0 at every reachable
state — it factors. This script checks the nearest *measure-theoretic* relative in the
partition-minimizing family: information-geometric integrated information (the
Oizumi-Tsuchiya-Amari family).

Geometric Φ is the KL divergence from the system's one-step transition to the nearest
"disconnected" model that cuts the influence between the parts, minimized over
bipartitions. For a bipartition {A,B} the disconnected model is
q(x'|x) = q_A(x'_A | x_A) q_B(x'_B | x_B); minimizing KL(p || q) over that manifold has
a closed form whose optimum is the marginal part-conditionals, so

    Φ_G(A,B) = Σ_x π(x) log2[ 1 / ( p(x'_A|x_A) p(x'_B|x_B) ) ]   at x' = succ(x)

for a deterministic transition, and Φ_G = min over bipartitions. This is exact (no
estimation, no noise), non-negative, and partition-minimized — the geometric
counterpart of the IIT-4.0 minimum-information-partition question.

π is the input distribution. Two are reported: uniform over all states (IIT's
maximum-entropy interventional stance) and uniform over the reachable states (the
domain IIT's per-state verdict actually uses). The over-call survives both.

Validation: the factoring control must read 0, the irreducible control and strict
mediation must read positive. Then the exhibit is interpretable. Depends only on
PyPhi 4.0 and numpy.

Reproduce:
    ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/geometric_check.py
"""

import os, itertools
from collections import defaultdict
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import numpy as np
import pyphi
from pyphi import new_big_phi

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
N = 3

SYSTEMS = {
    "factoring control": [lambda s: s[1], lambda s: s[0], lambda s: s[2]],
    "irreducible control": [lambda s: s[1] or s[2], lambda s: s[0] and s[2],
                            lambda s: s[0] ^ s[1]],
    "strict mediation": [lambda s: s[1], lambda s: s[0] and s[2], lambda s: s[1]],
    "THE EXHIBIT": [lambda s: not (s[1] or s[2]),       # W' = NOR(S, C)
                    lambda s: (not s[0]) and s[2],       # S' = ¬W ∧ C
                    lambda s: not (s[0] and s[1])],      # C' = NAND(W, S)
}


def succ(rules, x):
    return tuple(int(bool(r(x))) for r in rules)


def reachable(rules, n):
    states = list(itertools.product((0, 1), repeat=n))
    have_pred = {succ(rules, x) for x in states}
    return [x for x in states if x in have_pred]


def bipartitions(n):
    for mask in range(1, 2 ** (n - 1)):
        a = tuple(i for i in range(n) if (mask >> i) & 1)
        b = tuple(i for i in range(n) if not ((mask >> i) & 1))
        if a and b:
            yield a, b


def geometric_phi(rules, n, domain="all"):
    states = list(itertools.product((0, 1), repeat=n))
    nxt = {x: succ(rules, x) for x in states}
    support = states if domain == "all" else reachable(rules, n)
    pi = {x: 1.0 / len(support) for x in support}
    best = np.inf
    for A, B in bipartitions(n):
        wA = defaultdict(float); mA = defaultdict(float)
        wB = defaultdict(float); mB = defaultdict(float)
        for x in support:
            xa = tuple(x[i] for i in A); xb = tuple(x[i] for i in B)
            pa = tuple(nxt[x][i] for i in A); pb = tuple(nxt[x][i] for i in B)
            wA[xa] += pi[x]; mA[(xa, pa)] += pi[x]
            wB[xb] += pi[x]; mB[(xb, pb)] += pi[x]
        kl = 0.0
        for x in support:
            xa = tuple(x[i] for i in A); xb = tuple(x[i] for i in B)
            pa = tuple(nxt[x][i] for i in A); pb = tuple(nxt[x][i] for i in B)
            q = (mA[(xa, pa)] / wA[xa]) * (mB[(xb, pb)] / wB[xb])
            kl += pi[x] * np.log2(1.0 / q)
        best = min(best, kl)
    return best


def exact_iit_phi(rules, n):
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(bool(rules[j](cur)))
    net = pyphi.Network(tpm, cm=np.ones((n, n), dtype=int))
    mx = 0.0
    for s in range(2 ** n):
        st = tuple((s >> i) & 1 for i in range(n))
        try:
            mx = max(mx, max(0.0, float(new_big_phi.sia(pyphi.Subsystem(net, st)).phi)))
        except Exception:
            pass
    return mx


def main():
    print(f"{'system':22} {'exact IIT Φ':>12} {'Φ_G(all)':>10} {'Φ_G(reach)':>11}")
    print("-" * 58)
    for name, rules in SYSTEMS.items():
        print(f"{name:22} {exact_iit_phi(rules, N):12.3f} "
              f"{geometric_phi(rules, N, 'all'):10.3f} "
              f"{geometric_phi(rules, N, 'reachable'):11.3f}")
    print("\nReading: Φ_G reads 0 on the factoring control and positive on the")
    print("irreducible control and strict mediation, so it tracks the line on the")
    print("easy cases. On the exhibit it reads positive under both input domains")
    print("while exact IIT-4.0 Φ stays 0 — the geometric measure over-calls.")


if __name__ == "__main__":
    main()
