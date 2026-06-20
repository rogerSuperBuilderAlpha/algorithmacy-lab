"""The hierarchy thread — twenty questions on the architecture of scale.

The scale thread found one mediator cannot bind a large coordination (a single hub binds two workers 10% of
the time, three workers 2%, four workers 0%), and the two-hubs thread found a second hub binds five parties
40% of the time. Those two facts, at five parties, are the anchors. This thread drills twenty consecutive
questions into how coordination is structured beyond one mediator, all at four parties or fewer — the size
exact Φ runs fast — measuring the rate at which each architecture commits, reads as an irreducible whole.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/hierarchy/hierarchy.py

Deterministic: fixed seed, fixed form counts.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.classifier.classifier import classify_rules

SEED = 11
F = 100   # forms per architecture (n<=4)


def build(arch, n, rng):
    rules = [None] * n
    for node, ins in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), ins[0]) if len(ins) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
    return rules


def rate(arch, n, forms=F):
    rng = random.Random(SEED)
    L = tuple("ABCD"[:n])
    tri = sum(classify_rules(build(arch, n, rng), L).structure == "triadic" for _ in range(forms))
    return f"{tri}/{forms} = {100 * tri / forms:.0f}%", tri, forms


def survive(arch, n, drop, forms=F):
    """Commit the n-node form, then drop one node (force its state to 0) and re-read the n-1 rest."""
    rng = random.Random(SEED)
    L = tuple("ABCD"[:n])
    keep = [i for i in range(n) if i != drop]
    tri = kept = 0
    for _ in range(forms):
        rules = build(arch, n, rng)
        if classify_rules(rules, L).structure != "triadic":
            continue
        tri += 1
        sub = [(lambda y, _r=rules[i]: _r(y[:drop] + (0,) + y[drop:])) for i in keep]
        if classify_rules(sub, tuple("ABCD"[:len(keep)])).structure == "triadic":
            kept += 1
    return f"{kept}/{tri}", kept, tri


def main():
    print("# The architecture of scale — twenty questions (n<=4; five-party anchors cited).")
    print("# Anchors (scale, two-hubs threads): 1 hub binds 4 workers 0%; 2 hubs bind 3 workers 40%.")
    print()

    print("## Span of one hub")
    print(f"Q1  1 hub, 2 workers (n=3): {rate({0:[2],1:[2],2:[0,1]}, 3)[0]}")
    print(f"Q2  1 hub, 3 workers (n=4): {rate({0:[3],1:[3],2:[3],3:[0,1,2]}, 4)[0]}")
    print()

    print("## A second hub, two workers (n=4)")
    print(f"Q3  2 hubs share both workers:        {rate({0:[2,3],1:[2,3],2:[0,1],3:[0,1]}, 4)[0]}")
    print(f"Q4  2 hubs, also reading each other:  {rate({0:[2,3],1:[2,3],2:[0,1,3],3:[0,1,2]}, 4)[0]}")
    print(f"Q5  2 hubs split the workers (one each): {rate({0:[2],1:[3],2:[0,3],3:[1,2]}, 4)[0]}")
    print(f"Q6  2 hubs, one reads both, one reads one: {rate({0:[2,3],1:[2,3],2:[0,1],3:[0]}, 4)[0]}")
    print()

    print("## What the hub reads (n=3, 1 hub + 2 workers)")
    print(f"Q7  hub reads both workers:  {rate({0:[2],1:[2],2:[0,1]}, 3)[0]}")
    print(f"Q8  hub reads one worker:    {rate({0:[2],1:[2],2:[0]}, 3)[0]}")
    print(f"Q9  workers also read each other (back-channel): {rate({0:[1,2],1:[0,2],2:[0,1]}, 3)[0]}")
    print()

    print("## Depth — layers (n=4)")
    print(f"Q10 chain 2 workers -> mid -> top: {rate({0:[2],1:[2],2:[0,1,3],3:[2]}, 4)[0]}")
    print(f"Q11 top also reads the workers (matrix): {rate({0:[2,3],1:[2,3],2:[0,1,3],3:[0,1,2]}, 4)[0]}")
    print()

    print("## Flat vs mediated at three parties")
    print(f"Q12 flat triangle (all-to-all, n=3): {rate({0:[1,2],1:[0,2],2:[0,1]}, 3)[0]}")
    print(f"Q13 hub-mediated (n=3):              {rate({0:[2],1:[2],2:[0,1]}, 3)[0]}")
    print()

    print("## Redundant vs differentiated hubs (n=4, 2 hubs 2 workers)")
    def redundant(forms=F):
        rng = random.Random(SEED); L = tuple("ABCD"); tri = 0
        for _ in range(forms):
            g = _rule_of_set([rng.randint(0, 1) for _ in range(4)], [0, 1])
            rules = [_rule_of_one(rng.randint(0, 3), 2), _rule_of_one(rng.randint(0, 3), 3), g, g]
            tri += classify_rules(rules, L).structure == "triadic"
        return f"{tri}/{forms} = {100 * tri / forms:.0f}%"
    print(f"Q14 hubs identical (redundant):   {redundant()}")
    print(f"Q15 hubs independent (default):   {rate({0:[2,3],1:[2,3],2:[0,1],3:[0,1]}, 4)[0]}")
    print()

    print("## Resilience — lesion a node from the committed two-hub form (n=4 -> n=3)")
    two_hub = {0: [2, 3], 1: [2, 3], 2: [0, 1], 3: [0, 1]}
    print(f"Q16 drop a hub, rest still triadic:    {survive(two_hub, 4, 2)[0]}")
    print(f"Q17 drop a worker, rest still triadic: {survive(two_hub, 4, 0)[0]}")
    print()

    print("## The hub's gate at scale (n=4, 1 hub + 3 workers)")
    def gate3(g, forms=F):
        rng = random.Random(SEED); L = tuple("ABCD"); tri = 0
        for _ in range(forms):
            rules = [_rule_of_one(rng.randint(0, 3), 3), _rule_of_one(rng.randint(0, 3), 3),
                     _rule_of_one(rng.randint(0, 3), 3), g]
            tri += classify_rules(rules, L).structure == "triadic"
        return f"{tri}/{forms} = {100 * tri / forms:.0f}%"
    print(f"Q18 hub = AND of 3 workers:    {gate3(lambda x: x[0] & x[1] & x[2])}")
    print(f"Q19 hub = parity of 3 workers: {gate3(lambda x: x[0] ^ x[1] ^ x[2])}")
    print()

    print("## The law")
    print("Q20 commitment by (hubs, workers), n<=4 plus cited five-party anchors:")
    print(f"     1 hub : 2w={rate({0:[2],1:[2],2:[0,1]},3)[2] and rate({0:[2],1:[2],2:[0,1]},3)[0]}  "
          f"3w={rate({0:[3],1:[3],2:[3],3:[0,1,2]},4)[0]}  4w=0% (cited)")
    print(f"     2 hubs: 2w={rate({0:[2,3],1:[2,3],2:[0,1],3:[0,1]},4)[0]}  3w=40% (cited)")


if __name__ == "__main__":
    main()
