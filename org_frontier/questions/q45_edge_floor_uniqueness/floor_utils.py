"""Shared helpers for Q45 edge-floor probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.classifier.classifier import cm_from_rules  # noqa: E402
from org_frontier.corpus.forms_library import structural_tags  # noqa: E402

LABELS = ("W", "S", "C")
CANON = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

AND_INDEX = 1
OR_INDEX = 7
XOR_INDEX = 6
XNOR_INDEX = 9
PARITY_INDICES = {XOR_INDEX, XNOR_INDEX}

# little-endian two-input truth tables (4 bits)
_TWO_INPUT_TABLES = [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6, "control failed"
    assert v.mip_partition == "2 parts: {W,SC}", f"control MIP {v.mip_partition!r}"
    return v


def edge_count(rules):
    return int(cm_from_rules(rules).sum())


def s_index(label):
    return int(label.split("_S")[1].split("_")[0])


def s_table_index(rules):
    """Return the two-input truth-table index for the mediator (node 1)."""
    for idx, table in enumerate(_TWO_INPUT_TABLES):
        ok = True
        for w in (0, 1):
            for c in (0, 1):
                if rules[1]((w, 0, c)) != table[w | (c << 1)]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return idx
    return -1


def is_conjunctive_strict(rules):
    tags = structural_tags(rules)
    return (
        tags.get("strict_mediation")
        and tags.get("mediator_reads_both")
        and s_table_index(rules) == AND_INDEX
    )


def fn_from_table(table):
    return lambda a, b: table[(a & 1) | ((b & 1) << 1)]


def enumerate_all_wirings():
    """Yield (index, rules) for all 4096 n=3 wirings."""
    for i, ta in enumerate(_TWO_INPUT_TABLES):
        for j, tb in enumerate(_TWO_INPUT_TABLES):
            for k, tc in enumerate(_TWO_INPUT_TABLES):
                fa, fb, fc = fn_from_table(ta), fn_from_table(tb), fn_from_table(tc)
                rules = [
                    lambda x, fa=fa: fa(x[1], x[2]),
                    lambda x, fb=fb: fb(x[0], x[2]),
                    lambda x, fc=fc: fc(x[0], x[1]),
                ]
                yield i * 256 + j * 16 + k, rules
