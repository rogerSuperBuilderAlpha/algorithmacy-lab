"""Retrospective mathematical proof check for the preregistered four-node samples.

Not part of the frozen study protocol and not an additional empirical test.
Reads only recorded pair identifiers, never classifier outcomes.
"""
import json
from pathlib import Path

from . import f4


def audit():
    here = Path(__file__).resolve().parent / "results"
    parent = json.loads((here / "screen4.json").read_text())["study_pairs"]
    followup = json.loads((here / "followup_pairs.json").read_text())["pairs"]
    assert len(parent) == 40 and len(followup) == 600
    n = 0
    for row in parent + followup:
        a, b = tuple(row["a"]), tuple(row["b"])
        assert a != b
        assert f4.signature(*a) == f4.signature(*b)
        # A scalar sequence from each 16-state kernel has order <= 16.
        # Their DIFFERENCE has order <= 32, so k=0..31 is sufficient.
        assert f4.prop1_profiles(*a, 31) == f4.prop1_profiles(*b, 31)
        n += 1
    orders = {}
    for A in f4.invertible_As():
        v = (1, 2, 4, 8)
        for k in range(1, 16):
            v = tuple(f4.AT(A, w) for w in v)
            if v == (1, 2, 4, 8):
                orders[k] = orders.get(k, 0) + 1
                break
        else:
            raise AssertionError("GL(4,2) element order > 15")
    assert sum(orders.values()) == 20160
    assert max(orders) == 15
    return n, sum(orders.values()), max(orders)


if __name__ == "__main__":
    n, matrices, max_order = audit()
    print(f"q221 4-node all-lag certificate: {n}/{n} signatures and k0..31 exact profiles")
    print(f"q221 GL4 order: {matrices} matrices; maximum {max_order}")
