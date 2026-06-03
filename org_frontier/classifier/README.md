# classifier — does a coordination form demand literacy or algorithmacy?

A public tool. Drop in a model of a coordination form, get back a structural verdict: the form
is **dyadic** (it factors along party lines) and demands only **literacy**, or it is **triadic**
(irreducible) and demands **algorithmacy**. The verdict is exact IIT-4.0 Φ over the
minimum-information partition, computed with PyPhi.

This is the first build from the [`landscape/`](../landscape/) survey, which found the field has
never pointed PyPhi at human coordination. The theory is laid out in the essay
[`../essays/literacy_or_algorithmacy.md`](../essays/literacy_or_algorithmacy.md).

## The verdict

| Φ over the MIP | structure | competence demanded |
|---|---|---|
| Φ_MIP = 0 | dyadic — some party-respecting cut factors the form | **literacy** |
| Φ_MIP > 0 | triadic — no cut factors it; parties bound through the mediator | **algorithmacy** |

The test is Φ over the minimum-information partition (the least-damaging cut PyPhi finds), **not**
Φ over the complete cut, which over-calls every coupled dyad a triad. See
[`concepts.md`](concepts.md) and [`methods.md`](methods.md).

It is a **classifier**, validated behaviourally at the binary contrast. It is **not** a graded
readability score: Φ magnitude depends on the encoding and is not a reliable scale (the
dissertation withdrew that claim). Read the binary verdict; treat the magnitude as at most an
ordinal hint.

## Use

All commands run from the repo root with the IIT-4.0 venv.

```bash
# 1. Validate the instrument on its own controls FIRST (compute, don't assert).
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.validate

# 2. Classify the built-in library and write results/verdicts.csv.
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.run

# 3. Classify a single form by name, or your own JSON model.
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.cli --list
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.cli --form gig_false_dyad
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.cli --model my_form.json
```

Or import it:

```python
from org_frontier.classifier import classify_rules
# rules are per-party (little-endian: 0=Worker, 1=System, 2=Counterpart)
v = classify_rules([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])
print(v.competence)   # "algorithmacy"
```

## Files

- `classifier.py` — the importable tool: `classify`, `classify_rules`, the `Verdict` dataclass.
- `forms.py` — built-in library of validated coordination forms + their expected verdicts.
- `validate.py` — instrument controls + regression suite (run before trusting verdicts).
- `run.py` — classify the library, write `results/verdicts.csv`.
- `cli.py` — command-line front end (by name or JSON model).
- `concepts.md`, `methods.md` — the construct mapping and the design.
- `FINDINGS.md` — verdict table + caveats (written after the first run).

## Status

Scaffolded. Core reuses the dissertation's proven 3-node oracle
(`dissertation/paper2_construct/`) and the repo's exact-Φ oracle (`proxy_audit/exact_phi.py`).
Next: broaden `forms.py` into the coordination-form TPM library (broadcast, market, hierarchy),
and add the proxy bridge so the verdict can be estimated from interaction time-series.
