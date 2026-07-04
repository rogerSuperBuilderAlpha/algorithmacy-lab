# Hypotheses — substrates of collective-intelligence research

*Committed before any corpus is harvested or coded. The git history is the pre-registration. The
question: collective-intelligence research studies many kinds of collective — human teams, human
crowds, animal and robotic swarms, multi-agent AI, markets — and asks the same question of each,
whether the group computes something no member holds. Does that research read across its substrates,
or does each substrate grow its own literature that cites itself and ignores the others? Each
hypothesis names the knowledge claim it tests (in the knowledge-weaving typology), its
operationalization, and the outcome that would support versus challenge it.*

The question is descriptive-integrative: it sorts a field's sources by the kind of collective they
study and asks whether the substrates form one conversation or several. It matters to the lab's
program because algorithmacy and the integrated-information lens both treat coordination as
substrate-independent — a claim that only bites if the collective-intelligence field is in fact
fragmented by substrate, which is a thing to measure rather than assume.

## H1 — Fragmented by substrate
- **Knowledge claim (substantive omission / enduring critique):** the substrates proliferate in
  isolation. Human-team, crowd, swarm, AI-multiagent, and market research each cite within their own
  substrate and largely ignore the others, so the citation graph is block-diagonal by substrate.
- **Operationalization:** `lib/bibliometrics.py` cluster matrix over the coded `substrate` as the
  cluster key; within-substrate versus cross-substrate citation links among the corpus seeds.
- **Predicts:** within-substrate links far exceed cross-substrate links (a block-diagonal matrix).
- **Challenged if:** cross-substrate links are comparable to or exceed within-substrate links (the
  substrates read each other).

## H2 — Human teams and crowds dominate
- **Knowledge claim (stylized fact):** the field's mass sits on human collectives. Human-team and
  crowd substrates make up most of the corpus; swarm and AI-multiagent are smaller, newer literatures.
- **Operationalization:** the frequency distribution of the coded `substrate` across the corpus.
- **Predicts:** `human_team` and `crowd` together are a majority of coded sources; `swarm` and
  `ai_multiagent` each smaller.
- **Challenged if:** swarm and AI-multiagent together match or exceed the human substrates.

## H3 — Cross-substrate synthesis is rare
- **Knowledge claim (substantive omission):** few sources reason across substrates. A source that
  substantively spans two or more substrates — comparing human groups to swarms, or crowds to
  multi-agent AI — is the exception, not the rule.
- **Operationalization:** the proportion of coded sources with `spans_multiple = yes`.
- **Predicts:** `spans_multiple = yes` is a small minority (well under a third).
- **Challenged if:** a third or more of sources span two or more substrates.

## Method fixed in advance
- Corpus boundary and search: `coding_protocol.md` and `methods.md` (substantive + procedural gates;
  semantic search + Consensus, then snowball harvest).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`.
- Reliability reported (Fleiss' κ per categorical variable). Any hypothesis the data contradict is
  reported as challenged. If the citation harvest is rate-limited, H2 and H3 are reported from the
  coded corpus and H1 is marked partial.
