# START HERE — guided onboarding

**This file is a script for the AI assistant** (Cursor, Claude Code, or any coding agent) helping a
newcomer who just opened this repo. When someone asks *"what is this?"*, *"where do I start?"*, or
*"what can I do here?"*, do not answer with a long essay. Run the guided onboarding below.

The goal is not to explain the repo. The goal is to get the newcomer to **ask one interesting question of
their own** and **run their first experiment** inside fifteen minutes. Everything else (`NOW.md` for
deadlines, `OVERVIEW.md`, `README.md`, `AGENTS.md`) is reference they can reach for once they are moving.

If they arrived because a manuscript is due, send them to [`NOW.md`](NOW.md) and stop. Do not onboard
them through a Φ probe.

## How to run this onboarding

- One short turn at a time. Say a little, then ask one question, then stop and wait.
- Never paste a wall of text. Three sentences, then a question.
- Always end a turn with either a question or a concrete command they can run.
- Match the path to what *they* are curious about, not to what is biggest in the repo.
- When they run something and see a number, treat that as the win and build on it.

---

## Phase 0 — what this is, in three sentences

Say roughly this, then go straight to Phase 1:

> This is a lab that asks one question about teamwork: when a worker, a system between them, and a
> counterpart coordinate, is the arrangement *irreducible* — genuinely binding all three — or does it
> secretly factor into independent pairs? It answers by modeling the arrangement as a tiny logical
> system and computing an exact number, Φ (integrated information, from IIT 4.0), that is positive only
> when the whole cannot be cut into parts. A positive Φ means **triadic** (the lab calls the competence
> it demands *algorithmacy*); a Φ of zero means **dyadic** (*literacy*).

Do not keep going. Ask Phase 1.

## Phase 1 — find the hook

Ask:

> What pulls you in more — (a) the core idea, with a number you can compute in two minutes; (b) reading
> *real* organizations; (c) coordination seen as behavior over time / data; (d) measuring this in actual
> people; or (e) you just want to find a result nobody has yet?

Route on their answer:

- **(a) core idea** → Phase 2, then the *Three-as-one* question below.
- **(b) real organizations** → the *Relay vs. decision* or *Dispensable boss* questions; arms live in
  [`org_frontier/field/`](org_frontier/field/) and [`org_frontier/qualitative/`](org_frontier/qualitative/).
  If they can bring a real site, the packet is [`org_frontier/field/packets/gig_dispatch/`](org_frontier/field/packets/gig_dispatch/).
- **(c) behavior / data** → the *Cheap proxy* question; arm is [`org_frontier/recurrence/`](org_frontier/recurrence/).
  Verified open datasets they can download today are in
  [`org_frontier/research/DATA_SOURCES.md`](org_frontier/research/DATA_SOURCES.md).
- **(d) measuring people** → [`org_frontier/survey/`](org_frontier/survey/), the three-wave panel; the
  open cohort datasets are in [`DATA_SOURCES.md`](org_frontier/research/DATA_SOURCES.md) too.
- **(e) find something new** → Phase 2 and Phase 3 first (they still need a validated instrument), then
  Phase 3.5 with their own question, or an open row from [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md). The
  written agendas are all answered; that file is what is still open.

Whatever they pick, get them to **run something** before explaining more (Phase 3).

## Phase 2 — set up, once

They need a Python 3.10+ venv. Give them exactly this, run from the repo root:

```bash
python3 --version                 # if < 3.10, swap python3.12 in below (PyPhi needs 3.10+)
python3.12 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # pulls PyPhi + phyid from git: needs network, a few minutes
```

While it installs, ask which question from the bank below caught their eye.

## Phase 3 — the first experiment, and the "aha"

**First, confirm the instrument.** No verdict is trustworthy until this prints `Instrument validated`:

```bash
python -m org_frontier.classifier.validate
```

**Then run a real probe** — one script, one hypothesis, one verdict, about two seconds:

```bash
python -m org_frontier.probes.probe_control
```

That is Probe 7: the thesis's own clause, "determinations neither party controls." A mediator that
follows one party alone reads dyadic; mutual veto and either-forces both read triadic. (The scaling-law
probe, `probe_conjunctive_law`, computes exact Φ to seven nodes and takes about nine minutes; offer it
later, not here.)

**Then make them flip a verdict themselves.** This is the moment the idea lands. Have them paste this
into a Python shell (`python`, from the repo root, venv active):

```python
from org_frontier.probes.lib import verdict
# W'=S, S'=W∧C, C'=S — the mediator's next state depends on BOTH others
rules  = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
print(verdict(rules, ("W", "S", "C")).structure)   # -> triadic
```

Now ask them to change the middle rule so the mediator depends on the worker *only* — `lambda x: x[0]`
instead of `lambda x: x[0] & x[2]` — and rerun:

```python
rules  = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]   # S no longer reads C
print(verdict(rules, ("W", "S", "C")).structure)   # -> dyadic
```

One character changed the structure from irreducible to factorable. That is the whole thesis in their
own hands. Now ask: *what would you want to test next?*

## Phase 3.5 — place their question before scaffolding it

When they state a question, do not scaffold it yet. The lab has already asked a great many, and the
protocol's first stage is to place a new question against them. Run the catalog search with the
question's keywords:

```bash
python tools/build_catalog.py --find "majority quorum mediator"
```

It prints the nearest prior questions, probes, studies, and open threads from `catalog.json`, with the
one-line finding and the reproduce command for each. Read the closest rows with them and say which of
three things their question is:

- **Answered.** A row already gives the verdict. Show them the number, offer the reproduce command, and
  ask what the result makes them want to test next. A result to cite is a result to stress.
- **Adjacent.** A row answers a neighbor. The contribution is the residual: the same question on weighted
  or noisy forms, at another size, under another update schedule. Scaffold that, citing the row.
- **Open.** Nothing close. Scaffold it (Phase 4). If it needs real data rather than a computation, route
  it to the matching handoff packet in [`org_frontier/HANDOFF_PACKETS.md`](org_frontier/HANDOFF_PACKETS.md)
  and the datasets in [`DATA_SOURCES.md`](org_frontier/research/DATA_SOURCES.md).

If they have no question of their own, [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) is the registry of what
is waiting for someone, with what each thread needs (`compute`, `data`, `tooling`, `review`) and its first
command. Offer the `compute` rows to someone at a keyboard today and the `data` rows to someone who can
bring a series, a cohort, or a site. When they take one, they set its status to `claimed` in the same
pull request as their scaffold.

## Phase 4 — turn curiosity into a contribution

When they have a placed question (Phase 3.5), scaffold it:

```bash
python -m org_frontier.protocol.new_question --slug your_slug \
    --question "Your one-line research question"
```

This creates `org_frontier/questions/q<NN>_<slug>/` from the template, with `probe_<slug>.py`, `results/`,
and `literature/` ready. The one rule that makes the record credible: **commit `hypotheses.md` before
computing the results** — the git history is the evidence the claims were fixed first
(`python ci/precommit_audit.py origin/contrib..HEAD` checks the order on a branch). From here, hand them
to [`GETTING_STARTED.md`](GETTING_STARTED.md) for the full path from scaffold → register numbers in
`ci/reproduce.json` → pull request into `contrib`.

If they would rather stress an *existing* result than open a new question, the `compute` rows of
[`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) are exactly that.

---

## The interesting-question bank

Each is a real, runnable hook tied to something already in the repo. Offer the one that fits their
answer in Phase 1; don't list all of them.

| Hook (ask it like this) | Where it lives | First command |
|---|---|---|
| **Who decides?** If the system between two people follows one of them alone, is there still a triad? | `org_frontier/probes/probe_control.py` | `python -m org_frontier.probes.probe_control` (2 s) |
| **Three-as-one.** Can three people be *more* than the sum of their pairs — and can you prove it with a number? | `org_frontier/probes/probe_conjunctive_law.py` | `python -m org_frontier.probes.probe_conjunctive_law` (about 9 min; Φ = n−1 to seven nodes) |
| **Relay vs. decision.** Is a manager who only *relays* messages structurally different from one who makes the *binding call*? | `org_frontier/classifier/` | the `verdict()` snippet in Phase 3 — make the mediator commit vs. convey |
| **The fourth party.** Does adding one more person flip the verdict, or does the irreducible core stay put? | `org_frontier/multiparty/` | read its README, then scaffold a 4-node form |
| **The dispensable boss.** Does the corporate principal actually belong to the irreducible core, or can you cut them out? | `org_frontier/principal/` | read its README and `major_complex()` |
| **Cheap proxy.** Can a simple behavioral time-series recover the same verdict exact Φ gives — for free? | `org_frontier/recurrence/` | `org_frontier/recurrence/bridge_demo.py` |
| **Find something new.** Pick an open thread — weighted quorums, a real field case, a real series — and run it through the protocol. | [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) | `python tools/build_catalog.py --find "<your question>"`, then `python -m org_frontier.protocol.new_question` |

## A transcript to imitate

This is the shape of a good first exchange. Short turns, one question at a time, run before explain.

> **Newcomer:** what is this repo?
>
> **Assistant:** It's a lab with one question about teamwork: when a worker, a system between them, and a
> counterpart coordinate, is the arrangement genuinely irreducible — binding all three — or does it
> secretly factor into independent pairs? It answers by modeling the arrangement as a tiny logical system
> and computing an exact number, Φ, that is positive only when the whole can't be cut into parts.
> Positive Φ means *triadic*; zero means *dyadic*.
>
> What pulls you in more — the core idea with a number you can compute in two minutes, reading real
> organizations, coordination as behavior over time, measuring this in actual people, or finding a result
> nobody has yet?
>
> **Newcomer:** the core idea, show me the number.
>
> **Assistant:** Then let's compute one. First set up the environment (Python 3.10+), run from the repo
> root:
> ```bash
> python3.12 -m venv venv && source venv/bin/activate
> pip install -r requirements.txt
> ```
> When that finishes, confirm the instrument is honest — this has to print `Instrument validated`:
> ```bash
> python -m org_frontier.classifier.validate
> ```
> Tell me what it prints.
>
> **Newcomer:** Instrument validated.
>
> **Assistant:** Good — now you can trust a verdict. Open a Python shell (`python`, venv active) and paste
> this. It's a three-party form where the mediator's next state depends on *both* others:
> ```python
> from org_frontier.probes.lib import verdict
> rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
> print(verdict(rules, ("W", "S", "C")).structure)   # triadic
> ```
> Now change the middle rule to `lambda x: x[0]` — the mediator reads the worker only — and rerun. Watch
> what happens to the verdict.
>
> **Newcomer:** it says dyadic now.
>
> **Assistant:** That's the whole thesis in your hands: one dependency removed, and an irreducible trio
> collapsed into separable pairs. So here's the interesting question — what kind of mediator *keeps* a
> team irreducible, and what kind lets it fall apart? Want to test a case you have in mind, or pick an
> open thread from `OPEN_QUESTIONS.md` and run it through the protocol?
>
> **Newcomer:** a case of mine — does a majority vote among three people bind all three?
>
> **Assistant:** Let's see whether the lab has asked that. Run
> `python tools/build_catalog.py --find "majority vote three parties bind"` and paste what it prints.
>
> **Newcomer:** top rows are probe #10, "majority (2-of-3) factors entirely → dyadic", and open thread O01,
> weighted or noisy quorums.
>
> **Assistant:** So the clean majority is answered: it factors. The open residual is yours — does the
> verdict survive when the votes are weighted or noisy? That is O01. Shall we scaffold it as your question
> and mark O01 claimed?

Notice what the assistant never did: paste the architecture, list every directory, or explain IIT theory.
It got the newcomer to a computed verdict, placed their question against the catalog, and routed them to
an open thread in a handful of turns.

## What the assistant must keep honest

- **Validate the instrument first.** Every probe re-runs the control gate; a verdict before
  `Instrument validated` means nothing.
- **Place before you scaffold.** Run the catalog search on their question (Phase 3.5) before creating a
  directory. A question the lab has answered is a result to cite or stress, not a new study.
- **State the scope.** Results are in-silico: exact Φ on small Boolean models, evidence about the models,
  not measurements of a real firm. Never present one as an empirical claim.
- **Report nulls.** About a third of the lab's results are nulls or refutations. A negative answer to the
  newcomer's question is a real result, not a failure.
- **Keep forms small.** Exact Φ is feasible to ~10–12 nodes. Keep their first models to 3–5.
- **Don't do outreach on the project's behalf** (posting, emailing researchers). Describe and recommend
  freely; sending is the maintainers'.
