"""Load and validate an encodings file: one coordinative structure, several rival encodings.

The file format is specified in ``encode/SCHEMA.json``. An encoding is admissible only if

  * every party has a rule, written as a Boolean expression over party names;
  * every rule cites evidence (a source, a locator, and the quoted passage it rests on);
  * the mediator's rule names the alternative reading the evidence does not rule out;
  * the predicted verdict and its reason are stated before anything is computed.

These checks are what make the encoding step auditable, whether a person or a language model
drafted the encoding. ``validate_file`` returns a list of problems; an empty list means admissible.
"""

import json
from typing import List

from .rules import compile_rule

STRUCTURES = ("dyadic", "triadic")


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def labels_of(doc: dict, enc: dict) -> tuple:
    """An encoding may override the structure's party list (e.g. pooled drivers D1, D2)."""
    if enc.get("labels"):
        return tuple(enc["labels"])
    return tuple(p["label"] for p in doc["parties"])


def validate(doc: dict) -> List[str]:
    problems = []
    for key in ("structure", "parties", "encodings"):
        if key not in doc:
            problems.append(f"missing top-level field {key!r}")
    if problems:
        return problems
    mediator = doc.get("mediator")
    seen = set()
    for enc in doc["encodings"]:
        eid = enc.get("id", "?")
        if eid in seen:
            problems.append(f"[{eid}] duplicate encoding id")
        seen.add(eid)
        labels = labels_of(doc, enc)
        rules = enc.get("rules", {})
        for p in labels:
            if p not in rules:
                problems.append(f"[{eid}] no rule for party {p}")
                continue
            try:
                compile_rule(rules[p], labels)
            except (ValueError, SyntaxError) as e:
                problems.append(f"[{eid}] {e}")
            ev = enc.get("evidence", {}).get(p, [])
            if not ev:
                problems.append(f"[{eid}] rule for {p} cites no evidence")
            for item in ev:
                for k in ("source", "locator", "quote"):
                    if not str(item.get(k, "")).strip():
                        problems.append(f"[{eid}] evidence for {p} lacks {k!r}")
        if mediator and mediator in labels:
            alt = enc.get("alternative", {}).get(mediator)
            if not alt or not str(alt.get("rule", "")).strip() or not str(alt.get("why", "")).strip():
                problems.append(f"[{eid}] the mediator's rule ({mediator}) names no alternative reading")
            else:
                try:
                    compile_rule(alt["rule"], labels)
                except (ValueError, SyntaxError) as e:
                    problems.append(f"[{eid}] alternative: {e}")
        pred = enc.get("predicted", {})
        if pred.get("structure") not in STRUCTURES or not str(pred.get("reason", "")).strip():
            problems.append(f"[{eid}] no predicted verdict and reason (fix the prediction before computing)")
        bp = enc.get("bypass")
        if bp:
            for k in ("party", "downstream", "upstream"):
                if bp.get(k) not in labels:
                    problems.append(f"[{eid}] bypass {k} {bp.get(k)!r} is not a party")
    return problems


def validate_file(path: str) -> List[str]:
    return validate(load(path))
