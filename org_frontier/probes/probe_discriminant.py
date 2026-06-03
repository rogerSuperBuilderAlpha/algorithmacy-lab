"""Probe 15 — HMC vs algorithmacy structural signature (discriminant validity).

Paper 1 distinguishes algorithmacy from human–machine communication (HMC). In HMC the system is the
worker's end-partner: a two-party loop, no constituted third human. In algorithmacy the system
mediates the worker and another constituted human, and commits a joint determination. The constructs
should separate structurally: HMC dyadic, algorithmacy triadic.

H15: every HMC form classifies dyadic; every algorithmacy form triadic — a clean separator, with no
overlap. This is the construct's discriminant-validity claim, made structural.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_discriminant
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C")

# HMC: the system is the worker's partner; C is unconstituted (decoupled). S reads only W.
HMC = {
    "hmc_chat":      [lambda x: x[1], lambda x: x[0],        lambda x: x[2]],   # W<->S loop
    "hmc_assistant": [lambda x: x[1], lambda x: 1 - x[0],    lambda x: x[2]],   # S responds to W
    "hmc_tool":      [lambda x: x[0] & x[1], lambda x: x[0], lambda x: x[2]],   # worker uses a tool
    "hmc_recommender": [lambda x: x[1], lambda x: x[0],      lambda x: 1 - x[2]],  # C present but uncoupled
}

# Algorithmacy: the system mediates W and a constituted C; joint determination, parties track S.
ALGO = {
    "algo_bottleneck": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    "algo_or":         [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]],
    "algo_false_dyad": [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])],
    "algo_xor":        [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
}


def main():
    print("PROBE 15 — HMC vs algorithmacy structural signature")
    print("=" * 78)
    results = {}
    for fam, forms in (("HMC", HMC), ("ALGORITHMACY", ALGO)):
        print(f"  [{fam}]")
        for k, r in forms.items():
            v = verdict(r, LABELS)
            core, phi = major_complex(r, LABELS)
            results[k] = v.structure
            print(f"    {k:<18} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    hmc_dyadic = all(results[k] == "dyadic" for k in HMC)
    algo_triadic = all(results[k] == "triadic" for k in ALGO)
    print("=" * 78)
    print(f"  HMC all dyadic: {hmc_dyadic} ; algorithmacy all triadic: {algo_triadic}")
    print(f"  -> verdict separates the two construct families: "
          f"{'YES, cleanly' if hmc_dyadic and algo_triadic else 'NO (overlap)'}")
    print("=" * 78)


if __name__ == "__main__":
    main()
