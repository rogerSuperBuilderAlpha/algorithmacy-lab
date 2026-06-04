"""Probe 75 (#31) — control, exposure, and value capture.

Question: can value capture be read off the structure alongside Φ? Operationalize two Φ-free
quantities per party: CONTROL = the determination's Boolean sensitivity to that party (how much it
shapes the commit), and EXPOSURE = the sensitivity of the party's own next state to the system (how
much it is shaped by the commit). A party with high control and low exposure captures value; high
exposure and low control means captured. Hypothesis: in a triad the principal (when present and in the
core) has high control and low exposure, the worker the reverse. Method: compute control and exposure
per role for named forms and relate to core membership.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_value_capture
"""

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from .lib import major_complex


def sensitivity(rules, j, i, n):
    """Fraction of states where flipping node i changes node j's next value."""
    cnt = 0
    for s in range(2 ** n):
        b = tuple((s >> k) & 1 for k in range(n))
        bf = tuple(v ^ (k == i) for k, v in enumerate(b))
        cnt += int(rules[j](b)) != int(rules[j](bf))
    return cnt / 2 ** n


# system index is 1 in each form
FORMS = {
    ("bottleneck triad", ("W", "S", "C")):
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    ("gig false dyad", ("W", "S", "C")):
        [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])],
    ("principal gates+monitors", ("W", "S", "C", "P")):
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 75 (#31) — control, exposure, value capture")
    print("=" * 78)
    for (name, labels), rules in FORMS.items():
        n = len(labels)
        s = 1
        core, _ = major_complex(rules, labels)
        core = set(core or ())
        print(f"  {name}  (core={sorted(core)})")
        for i, lab in enumerate(labels):
            if i == s:
                continue
            control = sensitivity(rules, s, i, n)        # i -> S
            exposure = sensitivity(rules, i, s, n)        # S -> i
            tag = "captures" if control > exposure + 1e-9 else ("captured" if exposure > control + 1e-9 else "balanced")
            print(f"     {lab:<3} control={control:.2f} exposure={exposure:.2f}  {tag}  "
                  f"{'(in core)' if lab in core else ''}")
    print("=" * 78)
    print("  Reading: control minus exposure is a Φ-free leverage proxy. A party that shapes the")
    print("  determination more than it is shaped by it captures value; the structure says who.")
    print("=" * 78)


if __name__ == "__main__":
    main()
