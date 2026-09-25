"""Live demo helper for the ALGOCON talk (talk/LIVE_SESSION.md): three plain lines for one Boolean form.

It computes nothing of its own. Φ, the core and joint determination come from the Peirce reader
(org_frontier/thinkers/peirce/probe_peirce_joint_determination.read); the bypass question comes from
org_frontier/classifier/contingency.contingency_test. It never prints the classifier's structure label.

Import (from the repo root, in venv-4.0):
    from submissions.triadic_reduction.talk.live.show import show
    show("dispatcher", "AMB", ["x[1]", "x[0] & x[2]", "x[1]"])                  # three lines
    show("dealer", "MDB", ["x[2]", "x[0]", "x[1]"], bypass=("D", "B", "M"))     # D the party; B reads M

Command line (same forms):
    python submissions/triadic_reduction/talk/live/show.py dispatcher AMB "x[1]" "x[0] & x[2]" "x[1]"
    python submissions/triadic_reduction/talk/live/show.py dealer MDB "x[2]" "x[0]" "x[1]" --bypass D B M

A rule is a Python expression in x (x[0] is the first label) or a callable. Rules are little-endian:
rules[j](x) returns node j's next bit.
"""

import contextlib
import io
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.thinkers.peirce.probe_peirce_joint_determination import read  # noqa: E402
from org_frontier.classifier.contingency import contingency_test  # noqa: E402

KIND = {  # contingency_test's four kinds, in words for the room
    "contingent": "needed only while the direct deal is barred",
    "intrinsic": "still needed when they can deal directly",
    "partial": "still in, but the whole weakens when they deal directly",
    "reducible": "never needed: outside the core already",
}
SAFE = {"__builtins__": {"sum": sum, "int": int, "all": all, "any": any, "range": range, "len": len}}  # rule calls


def _rule(r):
    if callable(r):
        return r
    return lambda x, e=r: int(eval(e, dict(SAFE, x=x)))


def _phi(v):
    return "Φ = %s" % round(float(v), 3)


def _names(xs):
    return ", ".join(xs) if xs else "none"


def show(name, labels, rules, bypass=None, mode="replace", raw=False):
    """Print three lines. bypass=(party, downstream, upstream): downstream reads upstream directly."""
    labels = tuple(labels)
    rules = [_rule(r) for r in rules]
    if len(rules) != len(labels):
        raise ValueError("%d labels, %d rules" % (len(labels), len(rules)))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rec = read(name, (labels, rules))
    if raw:
        print(buf.getvalue().rstrip())
    if bypass:
        party, down, up = bypass
        c = contingency_test(rules, labels, party, downstream=down, upstream=up, mode=mode)
        if raw:
            print("  " + c.line())
        word = lambda p: "Whole" if round(p, 6) > 0 else "Factors"  # noqa: E731
        print("%s, %s  ->  %s deals with %s directly: %s, %s"
              % (word(c.phi_constrained), _phi(c.phi_constrained), down, up,
                 word(c.phi_bypass), _phi(c.phi_bypass)))
        print("Core: %s  ->  %s" % (_names(sorted(c.core_constrained)), _names(sorted(c.core_bypass))))
        print("%s: %s" % (party, KIND[c.kind]))
        return {"read": rec, "contingency": c}
    core = rec["core"]
    out = [x for x in labels if x not in core]
    print("%s, %s" % ("Whole" if rec["phi_mip"] > 0 else "Factors", _phi(rec["phi_mip"])))
    if len(core) == 1:  # a node that copies itself is a complex of one; it binds nobody
        print("Core: none that binds two parties   (%s only keeps its own state)" % core[0])
    else:
        print("Core: %s%s" % (_names(core), "   (outside: %s)" % _names(out) if core and out else ""))
    jd = rec["jd_elements"]
    if not jd:
        print("Set by two others: nobody")
        return rec
    head = "Set by two others" if all(len(i["purview"]) == 2 for i in jd.values()) else "Set by several others"
    # read()'s in_whole test, element by element: in the core, with two or more of its setters in the core
    inside = {x: rec["phi_mip"] > 0 and x in core and len(set(core) & set(i["purview"])) >= 2
              for x, i in jd.items()}
    tag = {True: "inside the core", False: "no whole holds them"}
    mixed = len(set(inside.values())) > 1
    who = "; ".join("%s by %s%s" % (x, "+".join(i["purview"]), " (%s)" % tag[inside[x]] if mixed else "")
                    for x, i in jd.items())
    tied = "" if rec["post_hoc_jd_tie_robust"] else " (tied reading)"
    print("%s: %s%s%s" % (head, who, "" if mixed else ", " + tag[any(inside.values())], tied))
    return rec


def main(argv):
    bypass, mode = None, "replace"
    if "--add" in argv:
        argv, mode = [a for a in argv if a != "--add"], "add"
    if "--bypass" in argv:
        i = argv.index("--bypass")
        bypass, argv = tuple(argv[i + 1:i + 4]), argv[:i]
    show(argv[0], argv[1], argv[2:], bypass=bypass, mode=mode, raw="--raw" in sys.argv)


if __name__ == "__main__":
    main([a for a in sys.argv[1:] if a != "--raw"])
