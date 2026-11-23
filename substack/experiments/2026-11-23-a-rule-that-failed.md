# A sharper rule that failed on every test, and what it showed instead

*We predicted four outcomes from a more precise rule. All four came out the other way. The failure shows that reversing the go-between's output doesn't matter; how it combines its two inputs does.*

## The question

The [last post](2026-11-23-testing-the-match.md) found that a switch-dependent go-between stays bound with
a "both" or "either" platform when it uses the same kind of rule, but not with an "exactly one" platform.
We proposed a sharper version based on which output the switch can force the go-between into, and wrote
four predictions down before running anything.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Same five members, with the platform working the switch. New go-between rules: "not both" (the reverse of
"both") and "neither" (the reverse of "either"), each with a "both" platform and an "either" platform. We
also ran an "exactly one" platform with an "either" go-between. Six cases, about 28 seconds.

## What we found

| platform says go if… | go-between passes on if… | we predicted | whole-system Φ |
|---|---|---|---:|
| both | both (control) | — | 2.0 |
| both | neither | bound | 0 |
| both | not both | not bound | 2.0 |
| either | not both | bound | 0 |
| either | neither | not bound | 2.0 |
| exactly one | either | bound | 0.5 |

**All four predictions from the sharper rule were wrong**, each in the same direction. "Not both" behaves
exactly like "both", and "neither" exactly like "either". The numbers and the tightest-bound groups are
identical.

That matches an [earlier result](2026-11-23-relay-flips.md): a go-between who reverses the message changes
nothing. What decides whether the group holds together is how the go-between combines the platform's
message with the switch, "both needed" or "either is enough", and whether that matches the platform's own
rule. Across four studies that now covers 18 "both"/"either" cases with no exception. We noticed this after
the run, so it still needs a test set up in advance.

The "exactly one" platform stayed bound (Φ = 0.5) for the third go-between rule in a row.

## What it means

A go-between stays bound with a "both" or "either" platform when it works on the same terms: "both needed"
with "both needed", "either is enough" with "either is enough". Passing the result on straight or reversed
makes no difference. For algorithmacy, the line where a platform's binding stops can be set by whether the
people along a chain combine signals the same way the platform does. Whether they pass those signals on
faithfully or reversed does not set it.

## Limits

Yes/no units, everyone updates at once, five members, the platform always works the switch, one "exactly
one" case. Ties are judged at a 1e-9 cutoff, pooled over all states where the top value appears.

## The code

- Study: [org_frontier/studies/forcing_match/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/forcing_match)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/forcing_match/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/forcing_match/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/forcing_match/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
