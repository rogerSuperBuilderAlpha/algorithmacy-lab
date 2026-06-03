# proxy_bridge — can a cheap time-series proxy recover the verdict?

Tests the survey's candidate route past the exact-Φ size ceiling: estimate a cheap proxy from a
coordination form's simulated trajectory and check whether it preserves the literacy/algorithmacy
verdict that exact IIT-4.0 Φ gives on the form's structure.

Reuses this repo's validated machinery: `phiid_vs_phi/phiid_measure.py` (ΦID Φ_R and Φ_WMS from a
time series via `phyid`), `proxy_audit/exact_phi.py` (trajectory simulation + exact Φ), and the
corpus forms from `../corpus/`.

## Run

```bash
~/iit-playground/venv-4.0/bin/python -m org_frontier.proxy_bridge.run [traj_len]
```

Writes `results/bridge.csv` (per form × noise × seed: exact Φ on the deterministic and noisy TPMs,
and both proxies) and prints the separation summary.

## Result

The proxy bridge does **not** hold. Neither Φ_R (rank-AUC 0.563) nor Φ_WMS (0.629) cleanly
separates dyadic from triadic forms. A dyadic form with a direct back-channel
(`hierarchy_backchannel`, exact Φ = 0) draws the highest proxy of all — the cheap measure confuses
statistical dependence with integration. See [`FINDINGS.md`](FINDINGS.md). The verdict needs the
exact structural computation, which is feasible because coordination units are small.

## Files

- `bridge.py` — add noise to a form's TPM; estimate both proxies; return them with exact Φ.
- `run.py` — sweep forms × noise × seeds; write `results/bridge.csv`; report class separation.
- `FINDINGS.md` — the negative result, the failure mode, and what it means for the size ceiling.
