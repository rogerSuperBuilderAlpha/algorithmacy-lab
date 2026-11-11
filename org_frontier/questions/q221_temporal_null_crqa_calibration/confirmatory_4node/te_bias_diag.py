"""EXPLORATORY (post hoc, not preregistered): why does finite-sample TE separate pairs whose exact
population TE is identical? For each such study pair: (1) check long-run empirical TE (T = 200,000)
against the exact value for both members; (2) at T = 600, compare per-member mean finite TE with the
exact value (i.e. the plug-in bias) on fresh seeds 4380000+ (outside all study ranges)."""
import json, os, sys
import numpy as np
from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node import f4, study4 as s4

OUT = os.path.join(os.path.dirname(__file__), "results")


def main():
    rows = json.load(open(os.path.join(OUT, "study4.json")))["pairs"]
    finite_only = [r for r in rows if r["exact_maxdiff"]["C1_TE"] <= 1e-12 and r["separates"]["C1_TE"]]
    out = []
    for r in finite_only:
        q = r["q"]; rec = dict(q=q, members=[])
        for m, sysm in enumerate((r["a"], r["b"])):
            rules = f4.rules_of(*sysm)
            ex = np.array(s4.exact_pop(*sysm)["C1_TE"])
            xl = trajectory(rules, 200000, np.random.default_rng(4380000 + 10 * q + m), flip=s4.FLIP, warmup=s4.WARM).astype(int)
            longrun = np.array(s4.f_TE(xl))
            short = np.array([s4.f_TE(trajectory(rules, s4.STEPS, np.random.default_rng(4390000 + 1000 * q + 500 * m + k),
                                                 flip=s4.FLIP, warmup=s4.WARM).astype(int)) for k in range(200)])
            rec["members"].append(dict(system=sysm, max_abs_longrun_minus_exact=float(np.abs(longrun - ex).max()),
                                       mean_bias_T600=(short.mean(0) - ex).tolist(), sd_T600=short.std(0).tolist()))
        b0, b1 = (np.array(m["mean_bias_T600"]) for m in rec["members"])
        rec["max_abs_bias_difference"] = float(np.abs(b0 - b1).max())
        out.append(rec)
        print(q, "longrun-exact", [round(m["max_abs_longrun_minus_exact"], 5) for m in rec["members"]],
              "max |bias0-bias1|", round(rec["max_abs_bias_difference"], 5), "typical sd", round(float(np.median(rec["members"][0]["sd_T600"])), 5))
    json.dump(dict(label="exploratory (post hoc)", pairs=out), open(os.path.join(OUT, "te_bias_diag.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
