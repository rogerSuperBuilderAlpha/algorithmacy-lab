# Q72 — Stage 1 review: the cost/proxy frontier

## The question

The motivating intuition behind this whole line was that the cost of a message signals its value. Q63
already found that one cost proxy, the mediator's in-degree, does not recover the verdict. This study
asks the sharper question across the outreach forms built in Q63-Q71: can any cheap structural proxy
(mediator in-degree, total edge count) recover the dyadic/triadic verdict, or is the exact computation
required?

## What the lab already knows that bears on this

- **Cheap proxies do not recover the verdict (Finding 7).** A ΦID or whole-minus-sum proxy separates
  dyadic from triadic only near chance (rank-AUC ≤ 0.63). This study tests the cost-like structural
  proxies on the outreach corpus specifically.
- **The cost proxy is non-monotone (Q63 H4, probe 218).** A substitutable broadcast reads more sources
  than a binding triad yet factors. This study extends that to explicit proxy collisions.
- **Liveness, not structure, carries the verdict (Q63 H5, Q67).** read_recipient and one_shot have the
  same wiring but opposite verdicts, differing only in whether the recipient stays live. A structural
  proxy cannot see liveness.

## The gap

The lab established that cheap proxies fail in general, but has not shown, on the outreach forms, explicit
pairs with identical proxy values and opposite verdicts. No prior probe pins the proxy frontier for the
outreach corpus, so the question is open.
