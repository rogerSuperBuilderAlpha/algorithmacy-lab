"""Build MANIFEST.json: machine-readable record of q221 candidates and experiments (commands, seeds, spec commits,
result-file SHA-256, software versions). Run: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.build_manifest"""
import hashlib
import json
import os
import platform
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
M = "org_frontier.questions.q221_temporal_null_crqa_calibration"


def sha(path):
    p = os.path.join(HERE, path)
    return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


def versions():
    import numpy
    import scipy
    v = dict(python=platform.python_version(), numpy=numpy.__version__, scipy=scipy.__version__)
    try:
        import pyphi
        v["pyphi_iit_version"] = str(pyphi.config.IIT_VERSION)
    except Exception as e:  # noqa: BLE001
        v["pyphi"] = "unavailable: %s" % e
    v["pyphi_commit"] = "b78d0e342d37175cbd55cf35a6d52ae035b4c50f (feature/iit-4.0)"
    return v


EXPERIMENTS = [
    dict(name="bounded_search", category="exploratory search", script="identifiability/pair_search.py",
         seeds="none (deterministic)", results=["identifiability/results/pair_search.txt", "identifiability/results/pair_search.json"]),
    dict(name="candidate_verification", category="exploratory search", script="identifiability/verify_candidates.py",
         seeds="none", results=["identifiability/results/verify_candidates.txt", "identifiability/results/verify_candidates.json"]),
    dict(name="adjudication_q220_pipeline", category="finite-sample check (exploratory)", script="identifiability/adjudicate.py",
         seeds="trajectory default_rng(43000 + r), r < 400", results=["identifiability/results/adjudicate.txt", "identifiability/results/adjudicate.json"]),
    dict(name="exact_screen", category="exploratory search (re-filter, no new search)", script="identifiability/screen_exact.py",
         seeds="none", results=["identifiability/results/screen_exact.txt", "identifiability/results/screen_exact.json"]),
    dict(name="iso_check_matched_candidate", category="exploratory search", script="identifiability/iso_check_hassan_pair.py",
         seeds="none", results=["identifiability/results/iso_check_hassan_pair.txt"]),
    dict(name="lead_pair_exact_phi", category="exploratory search", script="identifiability/rep_verify.py",
         seeds="none", results=["identifiability/results/rep_verify.txt"]),
    dict(name="lead_pair_finite_sample_hassan_script", category="finite-sample check (exploratory)",
         script="identifiability/lead_pair_finite_sample.py", seeds="0..299 per system",
         results=["identifiability/results/pinned_env_runs/lead_pair_finite_sample.json"]),
    dict(name="affine_theory_check", category="theory (exact check of proved propositions)", script="identifiability/affine_theory.py",
         seeds="none", results=["identifiability/results/affine_theory.txt"]),
    dict(name="survivor_baselines", category="finite-sample check (exploratory)", script="identifiability/baselines_survivors.py",
         spec_commit="35313d47", seeds="train 44000..44099, test 44100..44299",
         results=["identifiability/results/baselines_survivors.txt", "identifiability/results/baselines_survivors.json"]),
    dict(name="structural_baselines_heldout_families", category="structural prediction pilot (exploratory)",
         script="identifiability/structural_baselines.py", spec_commit="ecd014dd (crash fix 2nd commit, spec unchanged)",
         seeds="form draws default_rng(2210001/2210002); trajectories default_rng(450000 + 10*index + r); bootstrap 2210003",
         results=["identifiability/results/structural_baselines.txt", "identifiability/results/structural_baselines.json"]),
    dict(name="null_pilot_pearson", category="pilot calibration (exploratory)", script="independent_audit/null_pilot.py",
         seeds="2212026", results=["independent_audit/null_pilot_results.json"]),
    dict(name="null_extension_surrogates", category="pilot calibration (exploratory)", script="identifiability/null_extension.py",
         spec_commit="6ad206a3", seeds="2215001", results=["identifiability/results/null_extension.txt", "identifiability/results/null_extension.json"]),
    dict(name="variant_reconciliation", category="exploratory search", script="identifiability/variants_abc.py",
         seeds="none", results=["identifiability/results/variants_abc.txt"]),
    dict(name="process_law_equivalence", category="theory (exact decision, equality 2)",
         script="identifiability/process_law_equivalence.py", seeds="none",
         results=["identifiability/results/process_law_equivalence.txt"]),
    dict(name="target_audit_q161", category="target audit (step 11)", script="identifiability/target_audit.py",
         seeds="none", results=["identifiability/results/target_audit.txt"]),
    dict(name="target_variants_background_condition", category="target audit (step 11)",
         script="identifiability/target_variants.py", seeds="none", results=["identifiability/results/target_variants.txt"]),
    dict(name="edge_removal_check", category="target audit (step 11)", script="identifiability/edge_removal_check.py",
         seeds="none", results=["identifiability/results/edge_removal_check.txt"]),
    dict(name="q220_intermediates", category="finite-sample check (exploratory)", script="identifiability/q220_intermediates.py",
         seeds="trajectory default_rng(43000..43004)", results=["identifiability/results/q220_intermediates.json"]),
]
TESTS = ["identifiability/test_invariants.py", "identifiability/test_invariants_extra.py (expensive tier: Q221_SLOW=1)",
         "identifiability/test_q220_regression.py"]

CANDIDATES = [
    dict(id="A/B/C (A_self, B_xor, B_xor_memory)", status="rejected", reason="q161 targets ineligible (empty B) - rule 1", facts="see variants_abc.txt"),
    dict(id="nsi(0,3,3) vs aff(6,9,5)", status="rejected", reason="constant node X'=0; X marginal 2/25 vs 1/2", facts="preserved as failing example in test_invariants.py"),
    dict(id="aff(6,9,5) vs aff(11,9,5)", status="rejected", reason="isomorphic: swap Y,H + flip Y,H values (48-group)", facts="iso_check_hassan_pair.txt"),
    dict(id="aff(9,6,10) vs aff(9,15,10)", status="surviving (lead)",
         facts="equal marginals/auto/cross all lags; same major complex {X,H}, Phi 2; q161 B {X,H} vs {H}; not isomorphic; "
               "background-condition target {X,H} vs {X,H} (difference vanishes; TARGET_AUDIT.md)"),
    dict(id="aff(9,6,10) vs aff(9,15,12)", status="surviving (pairwise-identifiability only)",
         facts="q161 B {X,H} vs {H}; background-condition {X,H} vs {X,Y,H} (second ineligible, |B|=3)"),
    dict(id="aff(9,6,11) vs aff(9,14,10)", status="surviving (pairwise-identifiability only)",
         facts="q161 B {X,H} vs {H}; background-condition {X,H} vs {X,H} (difference vanishes)"),
]


def main():
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=HERE).stdout.strip()
    for e in EXPERIMENTS:
        e.setdefault("spec_commit", "none (not a prespecified evaluation)")
        e["command"] = "python -m %s.%s" % (M, e["script"][:-3].replace("/", "."))
        e["sha256"] = {r: sha(r) for r in e["results"]}
    for c in CANDIDATES:
        c.setdefault("reason", "survived exact screen (screen_exact.txt)")
        c.setdefault("facts", "screen_exact.txt; target_variants.txt")
    man = dict(schema_version="1", study="q221", protocol="protocol.md", tests=TESTS,
               rejected_candidates_file="identifiability/results/rejected_candidates.json", status="DRAFT, exploratory; no confirmatory evidence", generated_at_commit=head,
               versions=versions(), experiments=EXPERIMENTS, candidates=CANDIDATES,
               search_counts=dict(forms=8192, candidate_pairs=7488, no_constant=6816, equal_marginals=6432,
                                  equal_self_recurrence=180, equal_cross=180, non_isomorphic_raw=144,
                                  non_isomorphic_node_perm_unique=24, non_isomorphic_48group_unique=3))
    missing = [r for e in EXPERIMENTS for r, h in e["sha256"].items() if h is None]
    assert not missing, missing

    def nonull(x):
        assert x is not None
        if isinstance(x, dict):
            [nonull(v) for v in x.values()]
        elif isinstance(x, list):
            [nonull(v) for v in x]
    nonull(man)
    json.dump([c for c in CANDIDATES if c["status"] == "rejected"],
              open(os.path.join(HERE, "identifiability/results/rejected_candidates.json"), "w"), indent=1)
    json.dump(man, open(os.path.join(HERE, "MANIFEST.json"), "w"), indent=1)
    files = sorted({r for e in EXPERIMENTS for r in e["results"]} | {"identifiability/results/rejected_candidates.json"})
    with open(os.path.join(HERE, "results", "checksums.sha256"), "w") as f:
        for r in files:
            f.write("%s  %s\n" % (sha(r), r))
    print("MANIFEST.json written; %d experiments, %d candidates; missing results: %s"
          % (len(EXPERIMENTS), len(CANDIDATES), [r for e in EXPERIMENTS for r, h in e["sha256"].items() if h is None]))


if __name__ == "__main__":
    main()
