# Qualitative research — reading real coordination against the priors

The lab's in-silico work builds a catalog of priors: Boolean coordination forms carried to an exact Φ
verdict and a cooperative-game structure, each a pre-disclosed expectation about a recognizable kind of
coordination (the [prior-catalog essay](../essays/the_prior_catalog.md) sets out why the baselines are built
first, in quantity, before any real arrangement is read). Qualitative research is the arm that reads real
coordination. It is where the catalog meets the world.

This arm has two modes, and both are first-class.

**Model-bound.** A study takes one real coordination act — a dispatch, a hiring gate, a clinical handoff —
through the [field protocol](../field/PROTOCOL.md) to a dyadic or triadic verdict. The qualitative work is
upstream of the computation: interviews, observation, and document analysis produce the Boolean rules that
say who reads whom and how each party updates. The verdict is only as good as those rules, so the rules are
the contribution. A model-bound study is the program's bridge across the validation gap, one arrangement at
a time, against the priors assembled in the catalog.

**Stand-alone.** A study documents a coordination setting on its own terms — a thick description of how the
parties experience the arrangement, what they take the system to be doing, where they disagree about who
decides. It produces no Φ verdict and needs none. It is valued as a record of a coordination kind, a
candidate for later modeling, and as data about algorithmacy as a lived competence: how a worker reconstructs
a hidden counterpart, compresses intent into the few signals a system accepts, and tracks rule changes the
system makes without announcement.

## What a qualitative contribution is

A study lands in `org_frontier/qualitative/` as its own subdirectory, built from the
[template](template/README.md). It states the setting and its boundary, names the parties, says which methods
produced the evidence, and reports what was found. A model-bound study adds the elicited rules and a verdict
pre-registered before the computation. A stand-alone study reports the description and what it reveals about
the coordination. Either way the study names which prior in the catalog it speaks to, so a reader can place
it against the nearest pre-disclosed expectation.

The discipline that makes the catalog credible carries over. A computational study commits its hypotheses
before it runs; a qualitative study commits its interview guide, coding scheme, and bit calibration before
the fieldwork, so the git history shows the questions were fixed before the answers. Disagreement among the
parties about what determines an action is data, modeled both ways and reported under each.

## Read next

- [METHODS.md](METHODS.md) — eight qualitative methods adapted to the program, each tied to a step of the
  field protocol and to the question of whether a system commits a determination or conveys a signal.
- [TOPICS.md](TOPICS.md) — an open agenda of coordination settings, each paired with the prior it would test
  and the qualitative questions it raises.
- [template/](template/README.md) — the scaffold for a study, with the pre-registration discipline.
- [The field protocol](../field/PROTOCOL.md) — the nine-step method a model-bound study follows.

## How to contribute

The workflow is the lab's standard one (see [CONTRIBUTING.md](../../CONTRIBUTING.md)): branch off `contrib`,
build the study from the template, commit the coding scheme before the fieldwork, open a pull request into
`contrib`. A qualitative study registers no reproduced number, since it computes none; the directory check
confirms it is indexed. A maintainer reviews the argument, the evidence per rule, and the prose.
