# v11 — a bot-merged coordination (a model-bound field study)

v9 and v10 read projects where a human merges a pull request. v11 reads Kubernetes, where the Prow/Tide bot
merges mechanically once a reviewer lgtms, an OWNER approves, and CI passes. The merge actor is a machine,
which makes this a model-bound field study, with the determination rule elicited from the platform's
documented process instead of from interviews, and a test of the cognition arm's channel-versus-actor
distinction on a real arrangement.

## The pipeline

- [`fetch_bot_merges.py`](fetch_bot_merges.py) → [`prs.csv`](prs.csv), [`approvals.csv`](approvals.csv) —
  150 merged pull requests (author, dates, the bot merge actor) and the human approvals captured as GitHub
  reviews, the frozen provenance.
- [`HYPOTHESES.md`](HYPOTHESES.md) — four predictions, committed before the analysis ran.
- [`analyze.py`](analyze.py) — the merge actor, the human approvers, and the elicited-Prow Φ.
- [`FINDINGS.md`](FINDINGS.md) — the results.

## The result, in one line

The machine merges every pull request and the humans approve, and the elicited model refines the
channel-versus-actor distinction: the bot is a member of the irreducible core, because it stands in the
merge cycle, and a functional conduit, because it commits nothing — removing it preserves the binding. The
actor is the human approval upstream; bot-merging separates the act that commits from the act that
executes. See [FINDINGS.md](FINDINGS.md).

## On the validation gap

This closes a piece of the gap and marks the rest. The behavioral and structural instruments ran on real
coordination data the lab did not generate, with the determination rule taken from a documented process.
It leaves a worker's experience of the arrangement unmeasured; that is the qualitative and survey
arms' work, and it needs real people. The rule here is institutional and public, which is the easiest
elicitation; an interview-based field study of a coordination whose rule is not documented is the harder
step still open.
