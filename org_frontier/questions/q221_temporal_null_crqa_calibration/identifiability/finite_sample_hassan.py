"""Finite-sample check of Hassan's ORIGINAL A/B systems (as reconstructed from his H lag-1 self-match of 0.92 vs
0.50): X and Y are i.i.d. fair coins (NOT expressible as deterministic rule + flip, so crqa.trajectory cannot
generate them); H follows a deterministic rule plus independent 8% flip noise:
    A_hassan: H_{t+1} = H_t            (self-copy)   ; B_hassan: H_{t+1} = X_t XOR Y_t.
Generation is a small custom loop; ALL scoring uses q220's own stage2.observe code (read-only import), with
q220's settings (600 steps after 20 warm-up, MAX_LAG 10, PROM_FLOOR 0.05, MIN_PAIRS 30).
Seeds: numpy default_rng(42_000 + r), r = 0..R-1 (disjoint from q220 and the q221 pilot range).
Also prints the exact conditional mutual information I(H_{t+1}; X_t, Y_t | H_t) for these systems."""
import math
import sys
import numpy as np

from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob

STEPS, WARMUP, FLIP, MAX_LAG, PROM_FLOOR, MIN_PAIRS = 600, 20, 0.08, 10, 0.05, 30
R = int(sys.argv[1]) if len(sys.argv) > 1 else 400


def gen(kind, rng):
    h = int(rng.random() < 0.5)
    x, y = int(rng.random() < 0.5), int(rng.random() < 0.5)
    out = []
    for t in range(WARMUP + STEPS):
        hn = h if kind == "A" else (x ^ y)
        if rng.random() < FLIP:
            hn ^= 1
        x, y, h = int(rng.random() < 0.5), int(rng.random() < 0.5), hn
        if t >= WARMUP:
            out.append((x, y, h))
    return np.array(out, dtype=int)


res = {}
for kind in ("A", "B"):
    s = {k: [] for k in ("maxprom", "maxcc", "any", "noev", "lag0", "Hauto1")}
    for r in range(R):
        raw = gen(kind, np.random.default_rng(42_000 + r))
        c = ob.coupling(np.arange(STEPS), raw, MAX_LAG, "timestamp", MIN_PAIRS)
        iu = np.triu_indices(3, 1)
        p = c["prom"][iu]
        cc = ob.centrality(c["prom"], PROM_FLOOR)
        s["maxprom"].append(p.max()); s["maxcc"].append(cc.max()); s["any"].append(float((p > PROM_FLOOR).any()))
        s["noev"].append(float(cc.max() <= 0))
        s["lag0"].append(np.mean([(raw[:, a] == raw[:, b]).mean() for a, b in zip(*iu)]))
        s["Hauto1"].append((raw[1:, 2] == raw[:-1, 2]).mean())
    res[kind] = s
print("Hassan-version systems, R = %d each, seeds 42000..%d" % (R, 42_000 + R - 1))
for k in ("maxprom", "maxcc", "any", "noev", "lag0", "Hauto1"):
    a, b = np.array(res["A"][k]), np.array(res["B"][k])
    print("%-8s A %.4f ±%.4f   B %.4f ±%.4f" % (k, a.mean(), a.std(ddof=1) / np.sqrt(R), b.mean(), b.std(ddof=1) / np.sqrt(R)))
h2 = lambda p: -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
print("exact CMI I(H';X,Y|H): A = 0 (H' depends on H only); B = H(H'|H) - H(H'|X,Y,H) = 1 - h2(0.08) = %.6f bits"
      % (1 - h2(FLIP)))
