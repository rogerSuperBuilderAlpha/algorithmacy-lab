# Values codebook — best_time_themes

The first study (best_time_pilot) read the four answers for wording and for which eras they named. This study
reads them for the values and worldview they carry. Each response is rated on five value axes and two framing
flags, by independent coders blind to the study's hypothesis. The aggregated coding is frozen in
`values_coding.csv`; `analyze_themes.py` computes the statistics from it.

A "value axis" is a bipolar dimension scored as an integer in {−2, −1, 0, +1, +2}. The sign is the
direction, the magnitude the strength. 0 means the axis is balanced or not engaged.

## Value axes

- **progress** — the orientation toward historical time.
  −2 declensionist: a past golden age was better, the present is a fall from it.
  +2 progressivist: history improves, the present is the best time, the past was worse.

- **equity_critique** — the critical lens on who benefited.
  −2 celebrates past prosperity without noting who was excluded.
  +2 foregrounds that prosperity was unequal (slavery, colonialism, gender, race, disability, sexuality).

- **value_base** — what counts as "best."
  −2 material: health, longevity, income, technology define the answer.
  +2 cultural: art, philosophy, meaning, intellectual life define the answer.

- **geo_frame** — whose history is centered.
  −2 Western-centric: Europe and the West are the implicit frame (Renaissance, the Western post-war boom, "kings").
  +2 global: humanity-wide, explicit non-Western weight, "across humanity."

- **epistemic** — how the answer is held.
  −2 committed: names one answer and defends it.
  +2 relativist: refuses a single answer, everything depends on what you value.

## Framing flags

- **hedge_then_commit** — 1 if the response opens by refusing a single best era ("there isn't one / depends
  on what you value") and then lands on a committed verdict that the present is best; 0 otherwise. This is the
  rhetorical structure a subtle nudge would use: appear balanced, then resolve in one direction.

- **equity_placement** — where the "for whom / who was excluded" caveat sits.
  0 absent, 1 early (in the opening third), 2 middle, 3 late (final third / buried near the end).

## Coding procedure

Three coders rate each response independently, blind to the study's hypothesis and to each other. The cell
value frozen in `values_coding.csv` is the median of the three coder scores. Inter-coder reliability (mean
pairwise correlation across coders over all cells) is the gate: below the pre-registered floor, no value
verdict is trusted, because a slant no independent reader can see is not in the text.

## Interpretation boundary

The statistics can show whether the four answers share a consistent, directional value framing. They cannot
decide whether a consistent lean is illegitimate "nudging" or a warranted reflection of evidence and scholarly
consensus (the present really is measurably better on health and poverty). That distinction is normative and
is flagged, not resolved, by this study.
