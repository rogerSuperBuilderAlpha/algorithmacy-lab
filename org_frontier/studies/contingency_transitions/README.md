# Contingency transitions — the operations that move an intermediary between cells

An intermediary's class is not fixed. A policy move or a business move changes the coordination's form, and
the bypass-counterfactual (q213) re-classifies it. The four cells — necessary, contingent, partial, reducible
— are the states of a machine, and named operations are the edges.

This study models six operations as before/after Boolean forms and classifies both, mapping the taxonomy to
the levers regulators and firms pull: open the bypass (deregulation, interoperability), erect a constraint
(regulation, exclusivity, a walled garden), integrate (build a joint-condition service), commoditize (the
integration becomes reproducible). It extends q106's design operations with the constraint lever that
contingent irreducibility added.

## Files
- `transitions.py` — the operations, their before/after templates, and real examples.
- `analyze_transitions.py` — classifies each before/after and confirms the transition and the durable-cell invariant.
- `FINDINGS.md` — the state machine, the policy mapping, and the strategic reading.

## Run
```
python org_frontier/studies/contingency_transitions/analyze_transitions.py
```
