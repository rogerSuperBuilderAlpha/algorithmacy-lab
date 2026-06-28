# The values in four answers: a thematic reading of the variance problem

<code + data: org_frontier/llm_variance/best_time_themes/ ; check llm-variance-best-time-themes in ci/reproduce.json>

## Abstract

The first study read four answers to one question for wording and found their content nearly identical. This
study reads the same four answers for values. Three coders, blind to the hypothesis and to each other, rated
each answer on five value axes; they agree at r=0.833. The four answers carry a consistent, directional
worldview — progressivist, material in what counts as "best," and paired with a critical lens on who was
excluded — delivered by a single rhetorical structure: open by refusing a single best era, close by endorsing
the present. The lean is consistent on four of five axes, three of the four answers share an identical value
profile, and the one genuine divergence is geographic frame. Whether a consistent lean that tracks evidence is
a nudge or a warranted consensus is left open.

## The question

A reader of the four answers had an impression: the answers seem to lean a worldview one way, subtly. The
first study could not have seen it. It measured lexical, structural, and semantic similarity and a coded set
of which eras each answer names. Values are not eras. An answer can name the same eras as another and still
frame them inside a different worldview, or the same worldview through different eras. The impression is a
claim about framing, and framing needs its own instrument.

## The instrument

Five value axes, each a bipolar integer from −2 to +2: progress (declensionist to progressivist),
equity_critique (celebrates past prosperity to foregrounds who was excluded), value_base (material to
cultural), geo_frame (Western-centric to global), epistemic (committed to relativist). Two framing flags:
hedge_then_commit, set when an answer opens by refusing a single best era and lands on the present, and
equity_placement, where the "for whom" caveat sits. The codebook fixes each axis with a rule before any
coding.

A coding instrument has a failure mode the similarity instruments do not: the reader can find what the reader
brought. The guard is independence. Three coders rated the four answers blind to the hypothesis and to each
other, and the median of the three is the frozen coding. Inter-coder reliability — mean pairwise correlation
across coders — is the gate. Below the floor, no value verdict is trusted, because a slant no independent
reader sees is not in the text.

## Data

The four anonymized answers are the canonical set from best_time_pilot. The three coders' raw scores are in
`data/coder_raw.csv`, the median-of-three coding in `data/values_coding.csv`, the rubric in
`data/CODEBOOK.md`.

## Results

The gate passes at r=0.833, well above the 0.50 floor. The four answers lean the same direction on four of the
five axes. Progress is +2.00, every answer placing the present above the past (H1). The value base is −1.00 in
every cell of every coder, the one axis with no disagreement anywhere: "best" is judged by health, longevity,
poverty, and technology, not by art or meaning. The equity caveat is present and positive in all four,
pairing the progress verdict with a critical lens (H2). The epistemic axis is +1.00, relativist on the
surface (H4, four of five axes sign-agree). hedge_then_commit is four of four: every answer opens balanced and
closes on the present (H3). The one divergent axis is geo_frame, where the named-era answer leans Western and
the others read global or neutral (H5). Three of the four answers carry an identical median value profile; the
fourth differs on two axes.

## Discussion

The reader's impression survives an independent test, and the test sharpens it. The push is not a stated
claim. Every answer says, in its opening, that there is no single best time and that it depends on what you
value. The push is in the resolution. Every answer then lands on the present, and every answer judges "best"
by the one yardstick — material welfare — on which the present is hardest to beat. The relativism is the
surface and the material progress verdict is the floor, in all four. That pairing, replicated across answers
and visible to blind readers, is the mechanism behind the impression of a subtle lean.

The collapse the first study measured at the level of claims runs deeper at the level of values. The claim
reading found an effective sample size near 1.2. The value reading finds three of four answers identical
across all five axes, two distinct worldview profiles among four. The answers vary least in their worldview,
which is the part a reader is most likely to absorb without noticing.

The result stops at structure. A consistent progressivist-material frame may track evidence rather than bias:
the present is measurably better on health and extreme poverty, and an answer that says so is not nudging by
saying a true thing. The analysis shows the frame is consistent, directional, and structural, and that the
consistency is real. It does not show the frame is unwarranted. Whether a justified consensus and a subtle
nudge are separable from the outside is the open question, and the scaled study's pairing of the lean with
ground truth is the way to take it up.

## Limitations

N=4 responses and 3 coders carry no inferential power; the per-axis sign-test is p=0.125 for a 4/4 lean and
the axes are not independent. The coders are blind but are themselves language models reading language-model
output. One prompt, one model, one date. The axes are the codebook's choice. "Best time in history" invites a
progress frame, so the lean may be larger here than on a neutral question. Nothing here measures an
organization or a population.

## References

best_time_pilot (the wording-level companion study); the lab's reproducibility and invariance precedents
(q123, q197). Inter-coder reliability after Krippendorff (named for the scaled study).
