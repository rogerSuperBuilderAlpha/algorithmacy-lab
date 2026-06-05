"""Probe <N> (H<k>) — <one-line title>.

Question: <the sub-question this test answers>. Hypothesis: <H_k claim>. Method: <the form/ensemble, the
measure, the decision rule>. Instrument control: <the known form and value verified before the comparison>.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q<NN>_<slug>.probe_<slug>
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex   # or max_phi_float
from org_frontier.classifier.classifier import classify_rules, tpm_from_rules

LABELS = ("W", "S", "C")

FORMS = {
    # "name": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
}


def main():
    print("PROBE <N> (H<k>) — <title>")
    print("=" * 64)
    # instrument control first
    # ctrl = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS)
    # assert ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < 1e-6, "control failed"
    for name, rules in FORMS.items():
        v = verdict(rules, LABELS)
        core, phi = major_complex(rules, LABELS)
        print(f"  {name:<24}{v.structure:<10}Φ={v.max_phi:.3f}  core={core}")
    print("=" * 64)
    print("  Reading: <what the result says about H<k>>")
    print("=" * 64)


if __name__ == "__main__":
    main()
