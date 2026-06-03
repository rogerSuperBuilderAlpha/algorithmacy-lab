# principal — does the corporate principal join the irreducible core?

Paper 1 argues platforms are corporate-authored, with a principal whose objectives neither party
controls. This asks whether that principal P belongs to the irreducible coordination or sits outside
it, by computing the **major complex** (the maximally irreducible subset of nodes) for four ways of
coupling P to the worker–system–counterpart triad.

## Run

```bash
~/iit-playground/venv-4.0/bin/python -m org_frontier.principal.run
```

Writes `results/principal.csv`: per form, the whole-system verdict, the major complex, and whether P
is in it.

## Result

See [`FINDINGS.md`](FINDINGS.md). The principal joins the irreducible core **only under bidirectional
coupling** — it must both gate the determination (S reads P) and respond to it (P reads S). Ownership
alone, gating alone, or monitoring alone leave P outside; the core stays the W–S–C triad (Φ = 2.0).
Ownership is not constitutive; dynamic two-way participation is.

The experiment also shows why the **major complex**, not whole-system Φ, is the right object when a
form may contain spectator nodes: an idle principal makes the whole four-node system factor (Φ = 0)
while the W–S–C triad inside stays irreducible at Φ = 2.0.

## Files

- `forms.py` — the four named principal-coupling forms with rationale.
- `run.py` — whole-system verdict + major complex per form.
- `sweep.py` — population sweep (16 forms) pinning the exact condition: P joins iff S reads P AND P
  reads ≥1 party (bidirectional). Also surfaces the core-contraction wrinkle ({S,P} can displace
  W and C).
- `results/principal.csv`, `results/sweep.csv` — the tables.
- `FINDINGS.md` — the result, the population sweep, the org-theory reading, and the methodological note.
