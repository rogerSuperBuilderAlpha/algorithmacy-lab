# algorithmacy-lab

An open computational lab that applies **exact integrated information** (Φ, from IIT 4.0, computed with
[PyPhi](https://github.com/wmayner/pyphi)) to **organizational coordination theory**, and runs an
**AI-assisted research protocol** that takes a question to a finished quantitative paper.

The thesis it tests: a coordination form is **dyadic** when its cause-effect structure factors into
independent pieces (it demands *literacy*), and **triadic** when the structure stays irreducible across
the worker–system–counterpart partition (it demands *algorithmacy*). On systems small enough to compute
exact Φ, that verdict is exact, not a proxy.

> **Scope, stated up front.** Results here are *in-silico*: exact Φ on small Boolean dynamical models of
> coordination. They are evidence about the models. A validation gap separates them from empirical claims
> about real organizations (cross-model agreement is internal validity, not external validity). This is a
> research program and a proof-of-method, not peer-reviewed findings about real firms.

## The lab — [`org_frontier/`](org_frontier/)

The active program. Start at [`org_frontier/README.md`](org_frontier/README.md).

- **The research protocol** — a fixed six-stage pipeline (review → deep research → five hypotheses fixed
  before computing → methods → run against the exact-Φ instrument → full paper), made runnable end to end.
  See [`org_frontier/protocol/`](org_frontier/protocol/) and the method essay
  [`org_frontier/essays/studying_algorithmacy.md`](org_frontier/essays/studying_algorithmacy.md).
- **The logbook** — 134 exact-Φ experiments ("probes"), each with question, hypothesis, method, and
  result, about a third of them nulls or refinements. [`org_frontier/probes/PROBES.md`](org_frontier/probes/PROBES.md).
- **A worked paper** — the first question run through the automated pipeline (does the verdict reproduce
  Thompson's interdependence typology? — it does not):
  [`org_frontier/questions/q43_thompson_interdependence/paper.md`](org_frontier/questions/q43_thompson_interdependence/paper.md).
- **Essays** — [`org_frontier/essays/`](org_frontier/essays/): a ~10k-word catalog of every experiment, the
  literacy-or-algorithmacy argument, and the how-to-research piece.
- **The agenda** — 50 open questions: [`org_frontier/RESEARCH_AGENDA_50_V2.md`](org_frontier/RESEARCH_AGENDA_50_V2.md).

## Foundations — [`foundations/`](foundations/)

The measure-validation arc that established exact IIT-4.0 Φ as a ground-truth instrument before the lab
applied it. Seven experiments ask *what tracks integrated information*, plus two paper engagements. Headline:
no single cheap number is integrated information, but the information needed to recover it is distributed
across several cheap signals, and the measures sharing IIT's whole-minus-parts structure carry the most of
it. Full index and figures in [`foundations/README.md`](foundations/README.md).

## Setup

Requires Python ≥ 3.10 and PyPhi's IIT-4.0 line.

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Run an org_frontier probe, or a foundations experiment, from the repo root:

```bash
python -m org_frontier.probes.probe_conjunctive_law          # a lab probe
python -m foundations.proxy_audit.run 15 1 && python -m foundations.proxy_audit.analyze
```

## Repository note

This working tree also contains a separate, private dissertation repository nested at `dissertation/`,
gitignored and invisible to this repo. Where you run git from decides which remote you touch. See
[`REPO_LAYOUT.md`](REPO_LAYOUT.md) before committing.

## License and citation

MIT — see [LICENSE](LICENSE). To cite, see [CITATION.cff](CITATION.cff).

## Contributing and publishing

Contributions are welcome, and the record is meant to grow by them. [`PUBLISHING.md`](PUBLISHING.md)
describes how to publish an essay or a study here: fork, open a pull request into the `contrib` branch,
pass a reproducibility-first public review, and get merged. Both `contrib` and `main` are branch-protected;
every change is a pull request, the `reproduce-the-numbers` workflow re-derives each registered number,
and a merge needs one approving review. The aspiration is a community of maintainers who sign off on
submissions in a peer review that is reproducible by construction. Code and probe conventions are in
[`CONTRIBUTING.md`](CONTRIBUTING.md).
