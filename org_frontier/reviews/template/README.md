# <Review title> — the question in one line

*Copy this `template/` directory to `org_frontier/reviews/<slug>/` (`lower_snake_case`) and fill in
every placeholder. Delete this note when done.*

**Question.** <the one orienting question about the literature — exploratory / descriptive /
evaluative / integrative / explanatory>

**Status.** <in progress | complete>. Result: <one-line headline, once computed>.

The falsifiable claims are in [`hypotheses.md`](hypotheses.md) (committed before any result). The
corpus boundary, search, and coder design are in [`methods.md`](methods.md); the codebook in
[`coding_protocol.md`](coding_protocol.md). Findings in [`FINDINGS.md`](FINDINGS.md).

## Reproduce

```bash
python -m org_frontier.reviews.lib.harvest <slug>/seeds.json --out <slug>/edges/
python -m org_frontier.reviews.lib.reliability <slug>/coding --categorical <vars> --set <vars> --out <slug>/results/frozen.json
python -m org_frontier.reviews.lib.bibliometrics <slug>/edges --clusters <slug>/clusters.json
python -m org_frontier.reviews.<slug>.run
```
