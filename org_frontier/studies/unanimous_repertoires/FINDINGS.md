# The unanimous-state match is only in the forward (effect) value, and the two placements are not the same analysis

H1 and H3 were refuted; H2 was supported. At r = 0.2 the two placements do not have the same cause-and-effect analysis: for OR3 at 0000, cause φ is 1.041518 under mediator-side noise and 2.002920 under party-side noise, while effect φ is 1.041518446253012 either way. The already-known match of system φ is a match of the two effect values. At r = 0.4, mediator effect φ falls to -0.1242086202819146, which is why the match breaks.

Hypotheses were committed (`b87dc190`) before computing. The eight system-φ values used as controls were taken from `placement_equality/results/results.json` and disclosed in `hypotheses.md`; all eight reproduced to the pre-registered 1e-6 tolerance (in fact they matched the stored bits). IIT 4.0 system φ is the minimum of the cause value and the effect value on the minimum information partition.

## Scores

- **H1 REFUTED.** At r = 0.2, OR3 at 0000, the two placements do not match on both the cause analysis and the effect analysis. Cause φ is 1.0415184462530138 (mediator) versus 2.002920088948099 (party). Effect φ is 1.041518446253012 either way (difference 0). The minimum-information partitions are not the same. The cause and effect repertoire arrays do agree to 1e-10, but that is not enough for the pre-registered match, which also required the same partitions and the same cause φ.

- **H2 SUPPORTED.** At r = 0.4, OR3 at 0000, under mediator-only noise, effect φ = −0.1242086202819146 is strictly less than cause φ = 0.17044629498029837, and effect φ equals the stored system φ. Under party-only noise both values are positive (cause 0.6087367677867804, effect 0.1704462949802986) and the system value is their minimum (the effect).

- **H3 REFUTED.** 1-of-4 at 00000 follows the same split as OR3, so the "same pattern" claim in H3 fails on the r = 0.2 half: cause φ is 1.110953009336554 (mediator) versus 2.7017339721219504 (party), while effect φ matches (1.1109530093365476 and 1.1109530093365452). The r = 0.4 half of H3 holds: mediator effect φ = −0.09325477255320004 is strictly less than cause φ = 0.13635703598423907 and equals the stored system φ; party cause 0.87858914938298 and effect 0.13635703598423843 are both positive, and the system value is the effect.

## Exact numbers

| form and state | placement | r | system φ | cause φ | effect φ |
|---|---|---:|---:|---:|---:|
| OR3 at 0000 | mediator | 0.2 | 1.0415184462530138 | 1.0415184462530138 | 1.041518446253012 |
| OR3 at 0000 | mediator | 0.4 | -0.1242086202819146 | 0.17044629498029837 | -0.1242086202819146 |
| OR3 at 0000 | party | 0.2 | 1.041518446253012 | 2.002920088948099 | 1.041518446253012 |
| OR3 at 0000 | party | 0.4 | 0.1704462949802986 | 0.6087367677867804 | 0.1704462949802986 |
| 1-of-4 at 00000 | mediator | 0.2 | 1.110953009336554 | 1.110953009336554 | 1.1109530093365476 |
| 1-of-4 at 00000 | mediator | 0.4 | -0.09325477255320004 | 0.13635703598423907 | -0.09325477255320004 |
| 1-of-4 at 00000 | party | 0.2 | 1.1109530093365452 | 2.7017339721219504 | 1.1109530093365452 |
| 1-of-4 at 00000 | party | 0.4 | 0.13635703598423843 | 0.87858914938298 | 0.13635703598423843 |

In all eight cases, system φ equals effect φ. At r = 0.2, that common effect value is the already-published unanimous-state match (OR3 1.041518446253012; 1-of-4 1.11095300933654). The cause values are not the same across placements, and they are larger than the effect values under party-side noise.

The r = 0.4 mediator system φ at the unanimous state is negative, not zero. `placement_equality` published whole-group Φ as the maximum over reachable states, so this negative value was not the published whole Φ; the findings text there described the unanimous-state value as dropping "to 0."

Partitions at r = 0.2 are not the same across placements, even for the effect analysis, whose φ and repertoire arrays match.

## Noticed after the run

At both r = 0.2 and r = 0.4, and for both OR3 and 1-of-4, the mediator-side cause φ equals the party-side effect φ (differences ≤ 9e-15). For OR3 at r = 0.4 that common value is 0.170446294980298; for 1-of-4 it is 0.136357035984239. The system-φ match at r = 0.2 is the case where the mediator-side effect φ also equals that number; the break at r = 0.4 is the case where the mediator-side effect φ falls below it. The repertoire entries themselves are (1 − r)^n or 1 − (1 − r)^n. These pairings were noticed after the run and are not a claimed law.

## What it means

The two kinds of error do not give the same IIT 4.0 analysis at the unanimous state, even at r = 0.2. They give the same system φ there because both are limited by the forward (effect) value, and those forward values match. At r = 0.4 the coordinator-side forward value at that state goes negative, and the match of system φ ends.

## Limits

OR3 at 0000 and 1-of-4 at 00000 only; r ∈ {0.2, 0.4}; the system-level cause and effect analyses of `new_big_phi.sia`, not a full distinction-by-distinction CES. Independent errors; the same TPM construction as `placement_equality`.

## Reproduce

```sh
python org_frontier/studies/unanimous_repertoires/run.py --quick   # CI subset, ~4 s
python org_frontier/studies/unanimous_repertoires/run.py --write   # full run, ~9 s
```
