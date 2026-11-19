"""Power analysis for the JR/SHREC follow-up (PREREGISTRATION_FOLLOWUP.md section 4). Uses only the published
4-node study summary (results/study4.json); no new data. Exact binomial power of the preregistered per-classifier
rule: Wilson interval for pi with Bonferroni over 2 classifiers (two-sided alpha 0.05/2 -> z = 2.2414);
'generally separates' iff lower bound > 0.5. Output: results/power_followup.txt"""
import json
import math
import os

from scipy.stats import binom, norm

HERE = os.path.dirname(__file__)
Z = norm.ppf(1 - 0.05 / 2 / 2)


def wilson(k, n, z):
    p = k / n; den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return mid - half, mid + half


def power(pi, n):
    """P(rule resolves in the direction of pi) under Binomial(n, pi)"""
    if pi > 0.5:
        return sum(binom.pmf(k, n, pi) for k in range(n + 1) if wilson(k, n, Z)[0] > 0.5)
    return sum(binom.pmf(k, n, pi) for k in range(n + 1) if wilson(k, n, Z)[1] < 0.5)


def main():
    s = json.load(open(os.path.join(HERE, "results", "study4.json")))["summary"]
    lines = ["per-classifier z (Bonferroni over 2, two-sided 0.05) = %.4f" % Z]
    for nm in ("C2_JRR", "C4_SHREC"):
        k, M = s[nm]["pairs_separated"], s[nm]["M"]
        lo, hi = wilson(k, M, 1.959964)
        lines.append("%s 4-node estimate %d/%d = %.3f ; unadjusted 95%% Wilson [%.3f, %.3f]" % (nm, k, M, k / M, lo, hi))
    lines.append("power (prob. of a resolved verdict in the true direction) by true pi and M:")
    Ms = [200, 300, 400, 500, 600, 800]
    lines.append("   pi   " + " ".join("M=%-5d" % m for m in Ms))
    for pi in (0.40, 0.45, 0.55, 0.575, 0.60, 0.65, 0.70):
        lines.append("  %.3f " % pi + " ".join("%-7.3f" % power(pi, m) for m in Ms))
    lines.append("chosen M = 600: power 0.9+ at the JR point estimate 0.575 and ~1.0 at SHREC 0.70; "
                 "if JR's true pi is 0.55 power is ~0.6 (an unresolved outcome then remains possible).")
    lines.append("available fresh orbit pairs: 1872 - 40 used = 1832")
    open(os.path.join(HERE, "results", "power_followup.txt"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
