# Davis — Stage 4 methods

## Shared infrastructure

- Two bits per person; rules by `forms.camp_rules(n, edges, signs, k)`; TPM via
  `classifier.tpm_from_rules`; verdict via `probes.lib.verdict`; major complex via `probes.lib.major_complex`.
  Six-unit Φ runs take about seven minutes each on the reference machine; the CI checks are marked slow.
- Dynamics: attractors from the deterministic TPM (synchronous update); rest states by enumeration of camp
  assignments; clusterability and balance by enumerating simple cycles.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}.

## Rule

Person i with camp c_i; ties (i, j) signed ±1. Strain of camp c for i: the number of positive ties to a
j with c_j ≠ c plus negative ties to a j with c_j = c. Next camp: if c_i is valid (< k) and among the
least-strained camps, c_i; else the lowest-numbered least-strained valid camp. Bits: x = camp mod 2,
y = camp div 2.

## Forms

| form | persons | ties | k |
|---|---|---|---|
| ppp, ppm, pmm, mmm | p, o, q | po, pq, oq with the named signs | 2, 3, 4 |
| K4 census | p, o, q, r | all six ties, all 64 sign patterns | 4 (dynamics only) |
| path −− | p, o, q | po −, oq −; no pq | 4 |

## Decision rules

- **H1** CONFIRMED iff at k = 3 and 4 rest states exist for ppp, pmm, mmm and not ppm, and at k = 2 mmm has
  none. REFUTED otherwise.
- **H2** CONFIRMED iff at k = 4 |core persons| = 3 for ppm and < 3 for each of ppp, pmm, mmm. PARTIAL iff
  ppm = 3 but one clusterable pattern also 3, or all clusterable < 3 but ppm < 3. REFUTED otherwise.
- **H3** CONFIRMED iff mmm core persons = 3 at k = 2 and < 3 at k = 3 and 4, and ppm = 3 at k = 2, 3, 4.
  PARTIAL iff the mmm clause holds and ppm's does not, or the reverse. REFUTED otherwise.
- **H4** CONFIRMED iff for all 64 patterns (rest exists) ⇔ clusterable, triangle test = cycle test, and
  every clusterable pattern has one partition. PARTIAL iff the first holds and not the others. REFUTED
  otherwise.
- **H5** CONFIRMED iff the path has ≥ 2 partitions at rest and < 3 core persons. PARTIAL iff one clause.
  REFUTED otherwise.

## Reporting

Each probe prints the control, one line per form, and one verdict. Results in `results/<probe>.json`.
