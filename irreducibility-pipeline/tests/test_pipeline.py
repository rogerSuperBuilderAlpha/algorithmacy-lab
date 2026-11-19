"""Tests: instrument controls, the rule parser, the evidence gate, and the worked examples."""

import json
import os

import pytest

from irreducibility.core import classify_rules, major_complex
from irreducibility.validate import factoring_control, irreducible_control, FORMS, EXPECTED
from irreducibility.rules import compile_rule
from irreducibility.encoding import validate
from irreducibility.encode_check import check_quotes
from irreducibility.analyze import analyze
from irreducibility.regime import regime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = os.path.join(ROOT, "examples")


def test_controls():
    assert classify_rules(factoring_control()).structure == "dyadic"
    v = classify_rules(irreducible_control())
    assert v.structure == "triadic" and abs(v.max_phi - 0.830075) < 1e-4


@pytest.mark.parametrize("name", sorted(FORMS))
def test_regression_forms(name):
    assert classify_rules(FORMS[name]()).structure == EXPECTED[name]


def test_strict_mediation_triad():
    rules = FORMS["strict_mediation_triad"]()
    v = classify_rules(rules)
    assert v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-9
    assert set(major_complex(rules, ("W", "S", "C"))[0]) == {"W", "S", "C"}


def test_parser_matches_lambda():
    labels = ("D", "P", "R")
    f = compile_rule("D and R", labels)
    g = compile_rule("(D or R) and not P", labels)
    h = compile_rule("D xor R", labels)
    for s in range(8):
        x = tuple((s >> i) & 1 for i in range(3))
        assert f(x) == (x[0] & x[2])
        assert g(x) == ((x[0] | x[2]) & (1 - x[1]))
        assert h(x) == (x[0] ^ x[2])


@pytest.mark.parametrize("bad", ["__import__('os')", "D + R", "D and Q", "2"])
def test_parser_rejects(bad):
    with pytest.raises((ValueError, SyntaxError)):
        compile_rule(bad, ("D", "P", "R"))


def _doc(name):
    with open(os.path.join(EX, name, "encodings.json"), encoding="utf-8") as f:
        return json.load(f)


def test_gate_rejects_rule_without_evidence():
    doc = _doc("01_gig_dispatch")
    doc["encodings"][0]["evidence"]["P"] = []
    assert any("cites no evidence" in p for p in validate(doc))


def test_gate_rejects_missing_prediction():
    doc = _doc("01_gig_dispatch")
    del doc["encodings"][0]["predicted"]
    assert any("predicted" in p for p in validate(doc))


def test_gate_rejects_invented_quote():
    doc = _doc("01_gig_dispatch")
    doc["encodings"][0]["evidence"]["P"][0]["quote"] = "The platform decides everything."
    assert check_quotes(doc, os.path.join(EX, "01_gig_dispatch"))


def test_gig_dispatch():
    rep = {r["id"]: r for r in analyze(_doc("01_gig_dispatch"))["encodings"]}
    assert rep["A"]["structure"] == "triadic" and set(rep["A"]["core"]) == {"D", "P", "R"}
    assert rep["A"]["regime"] == "BOTTLENECK" and rep["A"]["contingency"]["kind"] == "intrinsic"
    assert rep["B"]["structure"] == "dyadic"
    assert rep["C"]["structure"] == "dyadic" and set(rep["C"]["core"]) == {"P", "R"}
    assert [rep[k]["regime"] for k in ("O1", "O2", "O3", "O4", "O5")] == \
        ["BOTTLENECK", "ENRICHER", "CAPTURE", "CAPTURE", "BYPASSED"]
    assert set(rep["O3"]["core"]) == {"D", "P"} and set(rep["O4"]["core"]) == {"P", "R"}


def test_insurance_claim():
    rep = {r["id"]: r for r in analyze(_doc("02_insurance_claim"))["encodings"]}
    assert set(rep["pipe"]["core"]) == {"C", "E", "A"}
    assert set(rep["gated"]["core"]) == {"C", "E"}
    assert set(rep["loop"]["core"]) == {"E", "A"}
    assert set(rep["loop_nolearn"]["core"]) == {"C", "A"}
    assert rep["frozen"]["structure"] == "dyadic"


def test_dealer_vs_clearinghouse():
    rep = {r["id"]: r for r in analyze(_doc("04_dealer_vs_clearinghouse"))["encodings"]}
    assert rep["dealer"]["contingency"]["kind"] == "contingent"
    assert rep["clearinghouse"]["contingency"]["kind"] == "intrinsic"


def test_regime_three_way_platform():
    L = ("W", "S", "C")
    S = lambda x: x[0] & x[2]
    assert regime([lambda x: x[1], S, lambda x: x[1]], L, "S") == "BOTTLENECK"
    assert regime([lambda x: x[1] & x[2], S, lambda x: x[1] & x[0]], L, "S") == "ENRICHER"
    assert regime([lambda x: x[1] | x[2], S, lambda x: x[1] | x[0]], L, "S") == "BYPASSED"
