# AI fidelity displace (#40)

Does an AI that online-learns C's policy displace C, and does that
track model fidelity (#69)? Fidelity ladder = honest training proxy
(not actual SGD).

| file | role |
|---|---|
| `hypotheses.md` | H1–H3 fixed before compute |
| `analyze_fidelity.py` | exact Φ ladder |
| `FINDINGS.md` | SHARP_FULL_DISPLACE |
| `results/panel.csv` | written by the smoke |

```
python org_frontier/studies/ai_fidelity_displace/analyze_fidelity.py
```
