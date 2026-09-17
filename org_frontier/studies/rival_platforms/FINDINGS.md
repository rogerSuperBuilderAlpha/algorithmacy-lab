# Rival platforms — findings

**Verdict: RIVAL_ENCODING.** Two platforms sharing a worker do not have
a single winner rule. Substitutable `W'=S1∨S2` / XOR → **equal-Φ
rivalry**: each reachable state selects one platform triad with W
(leftover W-free dyads allowed). Asymmetric W-response or extractive
`S←W` → **one platform captures** W. Joint `W'=S1∧S2` with cross-reads
→ **span both**. Idle / spectator W → **drops** from every max-Φ core.
Extends #73’s separate-cores result to rivalrous platforms: encoding
decides compete / capture / span / drop.

In-silico; candid N (designed n=5 panel). Hypotheses fixed in
`hypotheses.md`. Cited: #73; multiparty multihome; Q210; #29–#31
pointers only. Closed lanes stay closed.

## Hypotheses

| H | result |
|---|---|
| H1 compete / one captures W | **SUPPORTED** (2 compete + 6 one-wins) |
| H2 worker spans both / shared | **SUPPORTED** (3 span forms) |
| H3 worker drops / collapse | **SUPPORTED** (2 drop forms) |

## Panel (selected)

| form | Φ | witnesses (max-Φ cores) | reading |
|---|---:|---|---|
| ctrl_p1 / ctrl_p2 | 2 | {W,S1,C1} / {W,S2,C2} | single-platform contrast |
| either_OR | 2 | {W,S1,C1}; {W,S2,C2}; {S2,C2} | **compete** (state picks) |
| xor_W | 2 | both platform captures + dyads | **compete** |
| prefer_p1 / p2 | 2 | {W,Si,Ci} + leftover dyad | **one wins** |
| extract_p1 / p2 | 2 | {W,Si} + other dyad | **extractive capture** |
| span_joint | 2 | {W,S1,C1,S2,C2} | **span** |
| cross_read | 3 | {W,S1,C1,S2,C2} | **span** (Φ=3) |
| both_AND | 2 | full span **or** {S2,C2} | span with W-free rival |
| w_sticky / spectator | 2 | {S2,C2} only | **drop** |

## Winner rule

1. **Rivalry:** when W responds to either platform (OR/XOR) and both
   triads are alive, max Φ is tied across platform cores; the state
   selects which platform holds W.
2. **Capture:** W←Si only, or Si'=W extractive, hands W to that
   platform’s max-Φ complex (other platform may keep a W-free dyad).
3. **Span:** joint `W'=S1∧S2` plus cross-reads (Ci←W or Ci←Sj) merges
   both platforms and W into one complex.
4. **Drop:** non-responsive W leaves only W-free platform dyads at
   max Φ.

## vs #73 and multihome

#73 (multi-role across platforms) kept cores separate — one triad as
major complex. Here the worker is on *both* platforms as worker: under
OR/preference the same separation appears as **competition for W**, not
fusion. Span is possible, but only under joint binding + cross-reads —
stronger than multihome_both’s Ci←Si alone (which still admits a
W-free rival witness).

## Reading

Gig multi-homing is encoding-sensitive. Redundant platforms compete for
the worker’s standing in the major complex; preference or extractive
coupling picks a winner; only all-binding with cross-coupling puts the
worker in a shared two-platform core; a worker who ignores both drops
out. Same structural cut as #73, applied to rivalrous rather than
role-split platforms.

## Limits

Boolean n=5 designed panel; equal-Φ rivalry is state-selected among
tied maxima; no organization measured.

## Best next

**#33** — regulator capture (alt **#34** algorithmic transparency).

## Reproduce

```
python org_frontier/studies/rival_platforms/analyze_rival.py
```
(~50 s)
