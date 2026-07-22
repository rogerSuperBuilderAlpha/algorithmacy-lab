# Coding protocol (codebook) — substrates of collective-intelligence research

Code each source from its title + abstract. Code what the SOURCE studies — the kind of collective it
investigates, how it studies it, and whether it reasons across more than one kind — not what this
review predicts. You are one of several independent coders; do not consult another coder's output.
When a variable does not apply, use `na`. When genuinely unsure between two values, pick the better
fit — disagreement is expected and measured.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id (copy it verbatim from the corpus record).

- **substrate** — the kind of collective the source centrally studies. Pick the one it foregrounds:
  - `human_team` — a bounded human group: a work team, committee, jury, task group, small
    face-to-face or organizational group, group-decision or group-cognition study.
  - `crowd` — a large, loosely coupled set of humans: crowdsourcing, wisdom of crowds, online
    crowds, aggregation of many independent human judgments, collective attention.
  - `swarm` — animal collectives or biological/robotic swarms: ant/bee colonies, flocks, schools,
    swarm robotics, superorganisms, self-organized collective animal behavior.
  - `ai_multiagent` — artificial multi-agent systems: multi-agent reinforcement learning, LLM
    agent collectives, agent-based AI societies, machine collective intelligence.
  - `market` — price/market aggregation of dispersed information: prediction markets, information
    markets, betting/forecasting markets, market-as-computation.
  - `hybrid` — human-machine collectives as the central object: human-AI teams, human-computation
    systems where the human-machine mix is the point, centaur/cyborg collective intelligence.
  - `na` — the source studies collective intelligence in general with no single substrate
    foregrounded, or the substrate cannot be determined from title + abstract.

- **method** — how the source produces its knowledge about the collective:
  - `empirical` — reports observations or measurements of real collectives (experiments, field data,
    surveys, behavioral studies, data analysis).
  - `model` — a formal, computational, mathematical, or simulation model (agent-based simulation,
    analytic model, mechanism design, algorithm) as the central contribution.
  - `conceptual` — a review, theory piece, framework, or essay; no new data and no new formal model.

- **spans_multiple** — does the source SUBSTANTIVELY treat two or more of the substrates above
  (compare them, build a framework across them, transfer a mechanism from one to another)?
  - `yes` — the source develops two or more substrates as part of its argument (e.g. draws an
    explicit parallel between human groups and swarms, or between crowds and multi-agent AI).
  - `no` — the source stays within a single substrate; a passing one-line mention of another
    substrate does not count as spanning.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"smith2020","substrate":"human_team","method":"empirical","spans_multiple":"no"}`

Code every source in the corpus (`literature/corpus.jsonl`). If capacity runs low, code in list order
and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 tests within- vs cross-substrate citation; it needs an honest `substrate` call, not a spread.
  Assign the substrate the source actually foregrounds.
- H2 predicts `human_team` and `crowd` dominate. A corpus heavy in `swarm` or `ai_multiagent` is a
  real disconfirming datum — code the substrate the source studies, not the expected balance.
- H3 predicts `spans_multiple = yes` is rare. A source that genuinely reasons across two substrates
  is a real disconfirming datum — record it as `yes`. Do not inflate `yes` on a passing mention.
