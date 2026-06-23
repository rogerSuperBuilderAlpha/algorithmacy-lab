# AGENTS.md — foundations (the instrument-validation arc)

The measure-validation experiments that established exact Φ as the lab's ground-truth instrument: on
systems small enough to compute exact Φ, what tracks integrated information. The shared rules live in the
root [`../AGENTS.md`](../AGENTS.md). This note covers what is local here.

## Layout

Each experiment is a directory with a `FINDINGS.md` and its scripts:
`candidate_audit/`, `cbh_complexity/`, `consciousness_range/`, `emergence_vs_phi/`, `learned_surrogate/`,
`phiid_vs_phi/`, `proxy_audit/`, `psi_vs_phi/`, `structure_suite/`. The connected story is in
[`SYNTHESIS.md`](SYNTHESIS.md); the preprint writeup in [`paper/manuscript.md`](paper/manuscript.md). The
reusable exact-Φ engine many experiments share is [`proxy_audit/exact_phi.py`](proxy_audit/exact_phi.py).

## Add an experiment

- Land it under `foundations/<slug>/` with a `FINDINGS.md` stating the question, the hypothesis, the
  method, and the result — nulls and refutations included.
- Run from the repo root so `foundations.*` resolves; reuse `proxy_audit/exact_phi.py` rather than
  recomputing exact Φ from scratch.

## Verify

- Register each reported number in [`../ci/reproduce.json`](../ci/reproduce.json); a sweep or exact Φ past
  a few nodes is slow, so mark it `"slow": true` to keep it out of the per-PR gate.
- Run `python ci/reproduce.py` from the repo root, then `python tools/build_index.py --check` so the new
  experiment is indexed in the README directory.
