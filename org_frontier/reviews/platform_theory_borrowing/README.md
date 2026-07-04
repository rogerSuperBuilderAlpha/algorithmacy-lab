# Platform theory borrowing — which parent theories platform-governance research imports

**Question.** Which parent theories does platform-governance research import, in what mode, and how has
the mix shifted over time? (descriptive)

**Status.** Complete. Result: see [`FINDINGS.md`](FINDINGS.md).

The falsifiable claims are in [`hypotheses.md`](hypotheses.md) (fixed before coding). The corpus
boundary, search, and coder design are in [`methods.md`](methods.md); the codebook in
[`coding_protocol.md`](coding_protocol.md). Findings in [`FINDINGS.md`](FINDINGS.md); the ORM-register
write-up in [`paper.md`](paper.md).

## Reproduce

```bash
python3 -m org_frontier.reviews.lib.reliability org_frontier/reviews/platform_theory_borrowing/coding \
    --categorical parent_theory,borrowing_mode,multi_theory \
    --out org_frontier/reviews/platform_theory_borrowing/results/frozen.json
python3 -m org_frontier.reviews.platform_theory_borrowing.run
```
