# The post-hoc party-noise factor is refuted: it missed 10 of 20 pre-registered cases and failed for 2-of-5 and 4-of-5 at ε = 0.4

Both pre-registered hypotheses were refuted. The factor missed 10 of 20 cases; it held exactly for
(1,1,1,2) quota 3 and for 3-of-5, and at ε = 0.4 for 2-of-5 and 4-of-5 whole Φ rose from 0.032322
to 0.075400 instead of falling to 0.028561.

Hypotheses were committed (`7d33c987`) before computing. The twenty Φ(η, 0) values used as inputs
were taken from `weighted_swap_symmetry` and `five_six_node_quorum_ties` and disclosed in
`hypotheses.md`. Φ(0.2, 0) for 2-of-5 and 4-of-5 was measured in this study.

## Scores

- **H1 REFUTED.** 10 of the 20 pre-registered cases missed the predicted whole Φ by more than
  relative error 1e-10. The other 10 matched to relative error ≤ 2.3e-14.
- **H2 REFUTED.** At η = 0.2, ε = 0.3, both 2-of-5 and 4-of-5 match the factor 16807/17050 to
  relative error ≤ 1.1e-15. At ε = 0.4 both fail: whole Φ rises from 0.032322 to 0.075400, instead
  of falling to the predicted 0.028561.

## Exact numbers (whole Φ)

"pred" is the pre-registered value (H1) or Φ(η, 0) times the pre-registered factor (H2).
"rel" is |measured − pred| / Φ(η, 0).

| form | η | ε | Φ(η, 0) | predicted | measured | rel | result |
|---|---:|---:|---:|---:|---:|---:|---|
| (1,1,1,2) q2 | 0.05 | 0.3 | 0.014972604668929156 | 0.014483974137831951 | 0.014379689524039509 | 6.965e-03 | miss |
| (1,1,1,2) q2 | 0.05 | 0.4 | 0.014972604668929156 | 0.012502896682301666 | 0.007761798260372837 | 3.167e-01 | miss |
| (1,1,1,2) q2 | 0.2 | 0.3 | 0.02929897282509204 | 0.02834280167326591 | 0.02813873350121848 | 6.965e-03 | miss |
| (1,1,1,2) q2 | 0.2 | 0.4 | 0.02929897282509204 | 0.024466152565283044 | 0.015188587512527711 | 3.167e-01 | miss |
| (1,1,1,2) q3 | 0.05 | 0.3 | 0.0038968042400468897 | 0.003769632143574773 | 0.0037696321435748085 | 9.126e-15 | match |
| (1,1,1,2) q3 | 0.05 | 0.4 | 0.0038968042400468897 | 0.003254032406637094 | 0.0032540324066371246 | 7.902e-15 | match |
| (1,1,1,2) q3 | 0.2 | 0.3 | 0.008896660359373351 | 0.00860631809945827 | 0.0086063180994583 | 3.315e-15 | match |
| (1,1,1,2) q3 | 0.2 | 0.4 | 0.008896660359373351 | 0.007429169990816923 | 0.007429169990816949 | 2.925e-15 | match |
| (1,1,1,2) q4 | 0.05 | 0.3 | 0.014972604668929098 | 0.014483974137831895 | 0.01437968952403949 | 6.965e-03 | miss |
| (1,1,1,2) q4 | 0.05 | 0.4 | 0.014972604668929098 | 0.012502896682301617 | 0.007761798260372836 | 3.167e-01 | miss |
| (1,1,1,2) q4 | 0.2 | 0.3 | 0.029298972825091963 | 0.028342801673265836 | 0.028138733501218306 | 6.965e-03 | miss |
| (1,1,1,2) q4 | 0.2 | 0.4 | 0.029298972825091963 | 0.02446615256528298 | 0.015188587512527692 | 3.167e-01 | miss |
| (1,1,2,2) q3 | 0.05 | 0.3 | 0.015392814378989862 | 0.014890470315856026 | 0.014890470315856075 | 3.156e-15 | match |
| (1,1,2,2) q3 | 0.05 | 0.4 | 0.015392814378989862 | 0.012853793450496689 | 0.011969452461102469 | 5.745e-02 | miss |
| (1,1,2,2) q3 | 0.2 | 0.3 | 0.03247030028231149 | 0.03141063294836015 | 0.0314106329483601 | 1.496e-15 | match |
| (1,1,2,2) q3 | 0.2 | 0.4 | 0.03247030028231149 | 0.02711437446254877 | 0.025248905499525368 | 5.745e-02 | miss |
| 3-of-5 | 0.1 | 0.3 | 0.0017702875158729103 | 0.001745057025177476 | 0.0017450570251775167 | 2.303e-14 | match |
| 3-of-5 | 0.1 | 0.4 | 0.0017702875158729103 | 0.00156429042311679 | 0.0015642904231167895 | 2.450e-16 | match |
| 3-of-5 | 0.2 | 0.3 | 0.004260017707949414 | 0.004199303086070716 | 0.0041993030860707214 | 1.222e-15 | match |
| 3-of-5 | 0.2 | 0.4 | 0.004260017707949414 | 0.003764306556478937 | 0.0037643065564789365 | 1.018e-16 | match |
| 2-of-5 | 0.2 | 0.3 | 0.03232166778885665 | 0.0318610129341533 | 0.03186101293415326 | 1.073e-15 | match |
| 2-of-5 | 0.2 | 0.4 | 0.03232166778885665 | 0.028560600991607878 | 0.07539998661784443 | 1.449e+00 | miss |
| 4-of-5 | 0.2 | 0.3 | 0.032321667788856576 | 0.03186101293415322 | 0.03186101293415323 | 2.147e-16 | match |
| 4-of-5 | 0.2 | 0.4 | 0.032321667788856576 | 0.02856060099160781 | 0.07539998661784476 | 1.449e+00 | miss |

Quotas that are yes/no mirrors gave the same values: (1,1,1,2) q2 with q4, and 2-of-5 with 4-of-5.

The formula held, at every tested (η, ε), for (1,1,1,2) quota 3 and for 3-of-5. It held at ε = 0.3
but not at ε = 0.4 for (1,1,2,2) quota 3, 2-of-5, and 4-of-5. It failed at both new ε for
(1,1,1,2) quotas 2 and 4. Where it failed, the measured / Φ(η, 0) ratio was the same at every η
for that rule and ε (0.9604 and 0.5184 for (1,1,1,2) q2/q4; 0.7776 for (1,1,2,2) q3 at ε = 0.4;
2.3328 for 2-of-5 and 4-of-5 at ε = 0.4). Those ratios were noticed after the run and are not a
claimed law.

## What it means

The factor 1 / (1 + (ε / (1 − ε))^n) is not a general rule for party-side noise on interior and
weighted quorums. It remains an excellent fit to the older, lower-ε cases it was read off, and it
still predicts some of the new cases exactly, including every 3-of-5 point in this study. It does
not extend to every new rule or to ε = 0.4.

## Limits

One run; the stated rules and rates only; independent party-side flips after probe 464 input noise.
At these ε, more states are reachable than in the ε ≤ 0.2 studies (32 or 64 versus 4), but that
alone does not explain the split: (1,1,1,2) quota 3 and 3-of-5 also have the larger state counts
and still match.

## Reproduce

```sh
python org_frontier/studies/party_noise_factor/run.py --quick   # CI subset, ~11 s
python org_frontier/studies/party_noise_factor/run.py --write   # full run, ~2 min on 8 cores
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report;
every number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
