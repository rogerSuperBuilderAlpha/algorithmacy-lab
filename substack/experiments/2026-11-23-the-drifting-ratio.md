# A fitted formula for the drifting ratio missed by a quarter

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/drifting_ratio/`.*

When one person has more weight than anyone else, the whole group is much more loosely bound than
its strongest part, and that gap changes with the error rate. An earlier counting rule, which says
the gap is a fixed whole number, does not apply here. This study fitted a formula to six
already-published numbers from two such votes, then predicted the gap for a new one: four people
with weights (1,1,1,3) who pass at 3, where the weight-3 person can pass the vote alone.

The formula said the strongest part's φ would be 199.9024781081887, 102.76545826383659, and
54.04909345311601 times the whole group's Φ, at error rates of 5%, 10%, and 20%. The run gave
147.06517413692788, 76.2763609973792, and 41.48368774874131. Each prediction was high by about a
quarter (relative errors 0.264, 0.258, and 0.232). So the formula is not a general rule for this
kind of vote.

Two other predictions held. At every rate, the strongest part was exactly the coordinator together
with the weight-3 person. And the complement rule, passing at 4, gave the same whole Φ, the same
top φ, and the same ratio, at every rate.

The fit used two earlier votes in which one person can also pass the vote alone: (1,1,1,2) passing
at 2, and (1,1,2,3) passing at 3. A third published series, (1,1,1,2) passing at 3, was set aside
because that heavy voter cannot pass the vote alone, and there the ratio slowly rises rather than
falls. The new vote was in the falling-ratio group, and the formula still missed.

*Reproduce:* `python org_frontier/studies/drifting_ratio/run.py --write`
