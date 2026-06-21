# v9 findings — event-level PR and review coordination

v8 ran the behavioral instrument on weekly commit activity and found it too coarse: it recorded
co-presence, not the review-and-merge structure where a maintainer's gatekeeping lives. v9 reads that
structure directly, from PyPhi's pull-request history, where the merge actor is observed. Where v8 was
mostly null, v9 confirms most of its predictions, because the encoding now carries the coordination's
causal content. Reproduce with [`analyze.py`](analyze.py).

## The merge gate is a real veto player, partly shared

Of 71 merged pull requests with a recorded merger, the maintainer wmayner merged 42, a 59% majority.
Three others merged the rest: dviggiano 18, isacdaavid 10, rlmv 1. Twenty-two distinct authors opened
pull requests; four parties merged them. The merge right is concentrated against a spread of
authorship, the bottleneck the lab's [veto-player](../../threads/veto_player/THREAD.md) prior describes,
observed in real data. The veto is not exclusive: 37% of merges are self-merges by an author who holds
merge rights. The maintainer is the dominant gate, one of a few.

## The gate disintermediates over time

The self-merge share climbs across the project's life. Through 2014 to 2017 every merged pull request
passed through the maintainer, a 0% self-merge rate. By 2022 it was 20%, and in 2023 it reached 79%.
The maintainer's merge-time gate loosened as contributors earned merge rights, the
[disintermediation](../../threads/disintermediation/THREAD.md) prior observed as a decade-long trend.
The veto did not vanish; it moved upstream, to the granting of merge rights, where it no longer shows
in the merge events themselves.

## The lifecycle is directed but fast

Every merged pull request was merged on or after the day it opened, 71 of 71 with non-negative latency,
and the 31 of 32 review events that attach to a merged pull request fall between its open and its
merge. The open-to-merge order holds. The median latency is zero days: most pull requests open and
merge the same day. The directed structure is real and time-compressed, which is why v8's weekly
binning saw synchrony instead of a lead. The order lives below the daily resolution, in the event
sequence, where v9 reads it.

## The elicited merge triad is irreducible

The role triad — author, merge gate, codebase — under the institutional merge rule that a change enters
iff a pull request is opened and a party with merge rights merges it, is triadic with exact Φ of 2.0
and the gate in the major complex. This is the first real-coordination Φ from an elicited model. The
merge rule is known from how the platform works, not fit to noisy activity, and the data fills in who
occupies the gate. The structural reading the lab built on synthetic forms holds on a real coordination
once the coordination is read at the level where its determination is committed.

## The predictions, settled

- **H1 — the maintainer is the merge gate.** Confirmed, with nuance. wmayner merged the 59% majority;
  the gate is dominant, not exclusive.
- **H2 — the merge process is a constitutive triad.** Confirmed. The elicited triad is triadic, Φ 2.0,
  gate in the core.
- **H3 — the lifecycle is directed.** Confirmed. Open precedes merge everywhere, reviews fall between,
  the latency is non-negative and fast.
- **H4 — the gate disintermediates over time.** Confirmed. Self-merge rises from 0% early to 79% by
  2023.
- **H5 — few gates, many authors.** Confirmed. Twenty-two authors, four mergers.

## What v9 establishes

v8 located the validation gap in the encoding; v9 closes it. Reading the coordination at the event
level, where the merge actor is recorded, the lab's veto-player and disintermediation priors both
appear in a real organization, and Φ runs on an elicited institutional model, the merge rule known a priori.
The honest limits stay marked: the veto is shared not exclusive, the latency is fast enough that the
directed order sits below daily resolution, and the review culture is light, 33 review events across
104 pull requests. The next step is the same instrument on a project with a heavier review process,
where the reviewer role carries more of the coordination and the gate's grip can be compared across
governance styles.
