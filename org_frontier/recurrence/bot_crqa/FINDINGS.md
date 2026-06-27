# bot_crqa — findings

The behavioral instrument run on the v11 bot-merged history (`../bot_merged/`), daily bins, 22 days
(2026-06-01 to 2026-06-22): 150 author opens, 50 approvals (a partial GitHub-review view), 150 bot merges.

| hypothesis | verdict | key numbers |
|---|---|---|
| bH1 the conduit fires downstream (upstream→merge lag ≥ 0) | refuted | open→merge lag +0 d, but approval→merge lag −1 d (merge leads the partial approval series) |
| bH2 the bot merge is the behavioral hub, beats shuffle null | refuted | merge centrality 0.182 < shuffle-null mean 0.316, p = 0.937 — *below* chance |
| bH3 approval–merge is the highest-determinism pair | refuted | highest is author–merge (0.720), above author–approval (0.572) and approval–merge (0.548) |
| bH4 the author is the least central role | refuted | the author is the *most* central role (0.325), above merge (0.182) and approval (0.143) |

## All four refuted — and the refutations agree: the machine merger has no behavioral signature

The pre-registered picture was the v9 one: a merge actor that is the behavioral hub, with the upstream
roles feeding it. Every part of that fails here, and the failures are consistent. The bot merge is not the
hub; its coupling centrality sits *below* a time-shuffle null (p = 0.94), so its real merge timing carries
*less* sharp directional coupling than a random permutation. The role that drives the rhythm is the author:
author-opens is the most central series, and the merge tracks it as a same-day echo — author–merge has the
highest determinism (0.720) at lag zero. In this dense window most pull requests open and merge the same
day, so the bot's merges reproduce the author's opening rhythm and add no temporal structure of their own.

Read against v9, the contrast is the result. v9's human merge gate was the behavioral hub — most central,
far above its shuffle null (p = 0.0005). v11's machine merger is the opposite: high raw co-occurrence with
upstream activity but no independent directional signal, a centrality below chance. The behavioral
signature of this conduit is its absence. That diverges from the structural reading, where v11 placed the
bot *inside* the irreducible core: the bot is a structural member and a behavioral pass-through at once,
which is the channel-versus-actor distinction v11 raised, now visible as a split between the two
instruments.

The conduit intuition that motivated the hypotheses was right in spirit and wrong in operationalization. A
transparent conduit was expected to be a *central* relay (bH2); instead a transparent conduit is one with
*no* independent centrality. The refutation of bH2 — merge centrality below the null — is the cleanest
evidence for the conduit reading, not against it, but it is a refutation of the pre-registered claim and is
reported as one. The approval-based hypotheses (bH1, bH3) are further weakened by the partial approval data.

## Caveats

A 22-day window (short for CRQA) on one project, with the approval series a partial GitHub-review view
(50 events against 150 merges). The same-day open-merge dynamics dominate the daily grain, so the lead-lag
is largely unresolved, as in v9. The conduit-as-absence reading is a post-hoc interpretation of four
refuted hypotheses, not a pre-registered confirmation. Evidence about the behavioral instrument on one real
bot-merged coordination, paired with the structural reading, not a population.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python org_frontier/recurrence/bot_crqa/analyze_crqa.py`
