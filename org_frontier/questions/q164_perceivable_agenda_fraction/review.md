# q164 — review

## Claims and support

- D1 mean discrimination AUC 0.96 (approve 0.92, deny 1.00) for telling the interested k=2 mediator
  from the faithful k=0 gate by W↔C cross-recurrence peak prominence. Computed in
  `interested_perception.interested_vs_faithful_auc` over 120 vs 120 sampled traces per agenda. The
  raw AUC sits below 0.5 (0.08, 0.00), so the reported figure is the discrimination AUC
  max(auc, 1−auc).
- The 0.67 triadic-detection control is the battery's published D1 reading, reproduced from
  `theory_batteries.battery_direct_perception` during construction.
- D2 marginal fit errors per k computed in `interested_perception.marginal_fit_error`, 200 trials of
  200 draws each, against a matched-k random strict gate. Partial-regime mean 0.250 vs 0.186.

## Verdicts

- H1 REFUTED. The null (AUC ≥ 0.67) holds at 0.96. The agenda is the louder signal, not the fainter
  one. The probe reports this against its own prior prediction.
- H2 SUPPORTED in the partial regime k ∈ {1, 2, 3}. The k=3 reversal and the k=4 tie are in the
  table, so the support is bounded to where the override competes with the parties.

## Threats

- The D1 faithful class is a single fixed gate, so its spread is noise-only. That is the intended
  null: the question is whether the interested traces sit apart from the one faithful structure. A
  faithful class drawn from several gates would test a different question (interested vs any faithful
  gate) and is left to a follow-up.
- The matched-k random gate pushes k entries to the agenda value, so it is not a pure random gate.
  The plain random gate (D2 baseline 0.23) is reported alongside for reference. The matched control
  is the honest "at matched k" comparison the hypothesis names.
- The non-monotone D2 curve means the H2 verdict depends on the regime chosen. The regime k ∈ {1, 2,
  3} was fixed before computing in the probe docstring and methods, and the full table is reported.

## Reproducibility

Seeded `random.Random` throughout. Three runs confirmed byte-identical. Control passes
(`triadic`, max_phi 2.0).

## Scope

Small Boolean models, synthetic outcome traces. Evidence about the instruments and the construct, not
a measurement of a real platform.
