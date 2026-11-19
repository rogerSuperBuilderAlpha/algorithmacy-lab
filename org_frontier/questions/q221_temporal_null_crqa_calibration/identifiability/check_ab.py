"""Verify Hassan's XOR counterexample (in-family version) exactly, and compute the lab's exact-Φ targets."""
import numpy as np
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import exact_profiles as ep

L = ("X", "Y", "H")
SYSTEMS = {
    "A_self": [lambda x: x[0], lambda x: x[1], lambda x: x[2]],
    "B_xor":  [lambda x: x[0], lambda x: x[1], lambda x: x[0] ^ x[1]],
}
lags = np.arange(-ep.MAX_LAG, ep.MAX_LAG + 1)
prof = {}
for name, rules in SYSTEMS.items():
    P = ep.noisy_sbs(rules)
    pi = ep.stationary(P)
    print("==", name, "stationary pi =", np.round(pi, 12).tolist())
    unif = np.full(8, 1 / 8)
    d20 = unif @ np.linalg.matrix_power(P, ep.WARMUP)
    print("   max|uniform-start law after warmup - pi| =", float(np.abs(d20 - pi).max()))
    prof[name] = ep.all_profiles(rules)
    for (i, j), v in prof[name].items():
        if i != j:
            print("   cross %s->%s: max|p-0.5| over lags -20..20 = %.3e" % (L[i], L[j], np.abs(v - 0.5).max()))
    for i in range(3):
        v = prof[name][(i, i)]
        print("   auto %s: lag1..5 match = %s" % (L[i], np.round(v[ep.MAX_LAG + 1:ep.MAX_LAG + 6], 6).tolist()))
    # transient profiles from the uniform start at t = 0 (no warmup) and t = warmup
    tp = ep.all_profiles(rules, dist=unif)
    print("   transient(t0 uniform) cross max|p-0.5| =",
          max(float(np.abs(v - 0.5).max()) for (i, j), v in tp.items() if i != j))
    print("   P(H_t+1 = X_t xor Y_t) noisy = %.6f ; noiseless = %.6f" %
          (ep.xor_triplet_prob(rules), ep.xor_triplet_prob(rules, flip=0.0) if name == "B_xor" else float("nan")))
d = max(float(np.abs(prof["A_self"][k] - prof["B_xor"][k]).max()) for k in prof["A_self"] if k[0] != k[1])
print("max |cross profile A - B| over all ordered pairs, lags -20..20 = %.3e" % d)
for i in range(3):
    print("auto %s: max|A-B| = %.6f" % (L[i], float(np.abs(prof["A_self"][(i, i)] - prof["B_xor"][(i, i)]).max())))
for name, rules in SYSTEMS.items():
    ci, phi, bset, base, drops = ep.phi_targets(rules, L)
    print("PHI", name, "core=%s mcphi(core_indices)=%.6f bottleneck=%s base=%.6f drops=%s"
          % (ci, phi, sorted(bset), base, np.round(drops, 6).tolist()))
