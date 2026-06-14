# Q62 — findings

Excluded outer singleton cut against Q43 return-path typing on the back-channel panel after Q61 established
tied-seam↔type co-extensiveness. Sixteen aligned one-sided ceiling pairs, all triadic at max_phi=2.0.
Instrument control passed in every probe: triadic, max_phi=2.000000, MIP `2 parts: {W,SC}`.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 excluded complement of tied | confirmed | complement matches 16/16; mismatches 0/16. |
| H2 excluded inversely tracks type | confirmed | inverse type matches 16/16; direct type matches 0/16. |
| H3 excluded determined by tied | confirmed | within-tied excluded heterogeneity 0/16; W-tied+excl W 0/8; C-tied+excl C 0/8. |
| H4 no third independent joint | confirmed | distinct joint labels 2; (W,seq,C) 8/8; (C,rec,W) 8/8. |
| H5 excluded norm uniform | confirmed | excluded norm 1.0 on 16/16; excluded-W spread 0.000000; excluded-C spread 0.000000. |

**Through-line.** The excluded outer singleton cut at normalized_phi=1.0 carries no independent
return-path signal once tied seam and type are known. Excluded is the tied complement on 16/16 pairs and
inversely encodes the same two-way partition return-path typing names. The triple (tied, type, excluded)
collapses to two joint cells. Norm asymmetry (0.5 vs 1.0) does not lift max_phi discrimination at the
excluded subpanel level.

**Caveats.** n=3 deterministic Boolean models, AND/implication family with bijective parity back-channels;
excluded read from Q57 partition scan. Real organizations remain beyond reach.

**Reproduce.**

```bash
python -m org_frontier.questions.q62_excluded_cut_signal.probe_excluded_complement
python -m org_frontier.questions.q62_excluded_cut_signal.probe_inverse_type_track
python -m org_frontier.questions.q62_excluded_cut_signal.probe_tied_determines_excluded
python -m org_frontier.questions.q62_excluded_cut_signal.probe_no_third_joint
python -m org_frontier.questions.q62_excluded_cut_signal.probe_excluded_norm_phi
```
