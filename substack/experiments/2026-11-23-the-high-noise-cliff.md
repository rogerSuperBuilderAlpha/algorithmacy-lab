# The high-noise cliff is a sign flip

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/high_noise_tie_onset/`.*

Earlier today we found that the "anyone can decide" quorums (OR3 with three parties, ANY4 with four) behave
in two regimes under noise. Up to a 30% misread rate, the whole group is the single group with the highest
integration (Φ, computed exactly with IIT 4.0 in PyPhi). At 40%, the whole group is just one of a crowd:
every group that contains the mediator ties at the top. This study asks where between 30% and 40% the change
happens, and why.

## What we ran

The same model as before: a mediator S reads each party's vote, misreading each one independently with
probability η, and the parties copy S. We stepped η from 0.31 to 0.39 in steps of 0.01 and, at each rate,
listed every group tied for the top φ. We wrote down three predictions before computing anything.

## What we found

- **One sharp switch per form.** OR3 switches at η = 0.36. Its whole Φ is 0.311846 at 0.35 and 0.026429 at
  0.36, where seven groups tie. ANY4 switches at η = 0.33: 0.379397 at 0.32, 0.008841 at 0.33, a 15-way tie.
- **The two forms do not switch together.** We predicted they would. They don't: four parties switch three
  points earlier than three.
- **The winning state moves.** Below the switch, the top is in the all-zero state. From the switch on, it's
  in the state where S reads 0 and every party reads 1.

## Why it's a cliff

We then printed the raw φ PyPhi returns for the whole group at the all-zero state. It falls smoothly from
0.457943 at 0.31 to 0.311846 at 0.35, then reads **−0.181471** at 0.36. For ANY4 it goes from 0.379397 to
**−0.184887** between 0.32 and 0.33. Meanwhile the other state changes smoothly the whole way.

So the drop in Φ is not two states trading places gradually. The all-zero state's φ changes sign in PyPhi's
output, and that knocks it out. A negative Φ has no meaning in IIT 4.0, so we report it as what the software
returned, not as a property of the group. It also means our earlier studies, which skipped states with φ at
or below zero, would have hidden these values without saying so. Checking for that is next.

## Takeaway

When reading Φ off an open harness like PyPhi, a sudden change can come from the computation itself and not
from the system. The fix is to log raw values, negative ones included, before filtering.

*Reproduce:* `python org_frontier/studies/high_noise_tie_onset/run.py --write`
