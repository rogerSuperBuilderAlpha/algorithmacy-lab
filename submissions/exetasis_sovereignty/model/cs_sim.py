"""Minimal threshold-contagion check of Antonio's spec.
Ring of K cliques (size n). Adjacent cliques joined by w random bridge ties.
Threshold rule: node activates when sum of signals from active neighbours >= theta.
Competent active node emits signal 2 instead of 1. Seed: community 0 fully active.
Conditions: none / random competence (budget B) / competence at bridge endpoints (budget B).
"""
import numpy as np, itertools, sys
rng = np.random.default_rng(1)

def build(K, n, w):
    N = K*n
    A = np.zeros((N, N), dtype=np.int8)
    for c in range(K):
        idx = range(c*n, (c+1)*n)
        for i, j in itertools.combinations(idx, 2):
            A[i, j] = A[j, i] = 1
    bridge_nodes = []
    for c in range(K):
        d = (c+1) % K
        src = rng.choice(range(c*n, (c+1)*n), size=min(w, n), replace=False)
        dst = rng.choice(range(d*n, (d+1)*n), size=min(w, n), replace=False)
        for i, j in zip(src, dst):
            A[i, j] = A[j, i] = 1
            bridge_nodes += [i, j]
    return A, sorted(set(bridge_nodes))

def run(A, comp, seed_nodes, theta):
    N = A.shape[0]
    active = np.zeros(N, bool); active[seed_nodes] = True
    weight = np.where(comp, 2, 1)
    while True:
        signal = A @ (active * weight)
        new = (~active) & (signal >= theta)
        if not new.any(): break
        active |= new
    return active.mean()

def experiment(K=8, n=10, theta=2, B=16, reps=200):
    print(f"K={K} n={n} theta={theta} budget B={B} reps={reps}")
    print(f"{'w':>3} {'none':>7} {'random':>7} {'bridge':>7}")
    for w in [1, 2, 3, 4, 6]:
        res = {"none": [], "random": [], "bridge": []}
        for _ in range(reps):
            A, bn = build(K, n, w)
            N = A.shape[0]; seed = list(range(n))
            comp0 = np.zeros(N, bool)
            compR = np.zeros(N, bool); compR[rng.choice(N, B, replace=False)] = True
            compB = np.zeros(N, bool)
            pick = rng.choice(bn, min(B, len(bn)), replace=False); compB[pick] = True
            res["none"].append(run(A, comp0, seed, theta))
            res["random"].append(run(A, compR, seed, theta))
            res["bridge"].append(run(A, compB, seed, theta))
        print(f"{w:>3} {np.mean(res['none']):7.2f} {np.mean(res['random']):7.2f} {np.mean(res['bridge']):7.2f}")

experiment()
print()
# Panel (b): thin bridges (w=1), reach vs budget
K, n, theta, reps = 8, 10, 2, 200
print("w=1: reach vs budget B")
print(f"{'B':>3} {'random':>7} {'bridge':>7}")
for B in [0, 4, 8, 16, 24, 32, 48, 64]:
    rr, rb = [], []
    for _ in range(reps):
        A, bn = build(K, n, 1); N = A.shape[0]; seed = list(range(n))
        compR = np.zeros(N, bool)
        if B: compR[rng.choice(N, B, replace=False)] = True
        compB = np.zeros(N, bool)
        if B: compB[rng.choice(bn, min(B, len(bn)), replace=False)] = True
        rr.append(run(A, compR, seed, theta)); rb.append(run(A, compB, seed, theta))
    print(f"{B:>3} {np.mean(rr):7.2f} {np.mean(rb):7.2f}")
