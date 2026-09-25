# Live session — runbook for the assistant

Load this with `@submissions/triadic_reduction/talk/LIVE_SESSION.md` before the talk. During the session it
yields only to `CLAIM.md`.

## Purpose

During slide 21 the author reads out an audience member's coordination scenario, a sentence naming three
to five parties and who acts on whom. You turn that sentence into a small Boolean model, compute
integrated information (Φ, IIT 4.0 via PyPhi) with the lab's own reader, and put three plain lines on
screen in under a minute. You compute nothing yourself: `read()` and `contingency_test` do the work, and
`talk/live/show.py` only formats their output. The room watches the translation as much as the number,
so show the rules before you run them.

## Environment

- Repo root: `/Users/ludwitt/iit-playground/wt-triadic-reduction`. Run every command from there.
- Python: `~/iit-playground/venv-4.0/bin/python` (3.12, PyPhi IIT-4.0 line). Set `PYPHI_WELCOME_OFF=true`.
- Write scratch files only under `submissions/triadic_reduction/talk/live/`. Never edit lab code during
  the session, and do not touch git.
- One call is one fresh process. PyPhi keeps no cache on disk (`REDIS_CACHE False`), so every form is
  recomputed. The pre-flight runs warm the imports and the OS file cache, not Φ.

## Pre-flight, T−30 minutes (off the projector)

1. `source ~/iit-playground/venv-4.0/bin/activate && export PYPHI_WELCOME_OFF=true && cd <repo root>`.
2. `python -m org_frontier.classifier.validate` prints `Instrument validated` (3.2 s in rehearsal). It
   also prints the words the talk keeps off screen, so run it before the projector is on.
3. Run the four rehearsed prompts and clique_4 through the helper (the commands are in the table below).
   Each output must match the table character for character. If one does not, stop and use slide 22.
4. Start the assistant pinned to the rehearsed model: `claude --model claude-opus-5-5`. Keep Sonnet 5
   as the fallback (`/model`) for a slow network. Load this runbook with `@`.
5. Terminal font at 20 pt or larger; each helper line fits in about 70 columns.
6. Network: the assistant needs it and the computation does not. Check both anyway.
7. Battery above 80 % or on mains; notifications off.

## From a sentence to rules

One node per party, one capital letter each. Keep to three or four nodes; five only when at most one
party reads more than one other (see the limits below). Every party's next state is a fixed function of the current states:
synchronous, one tick, deterministic.

**State convention.** Rules are little-endian (GETTING_STARTED.md §4). With labels `"AMB"`, `x[0]` is
A, `x[1]` is M and `x[2]` is B, and `rules[j](x)` returns node j's next bit. A rule is a Python
expression in `x`.

| the sentence says | rule for that party |
| --- | --- |
| "follows", "relays", "copies", "waits on" B | `x[b]` |
| "only when both" A and B | `x[a] & x[b]` |
| "either" A or B | `x[a] \| x[b]` |
| "opposes", "does the opposite of" A | `1 - x[a]` |
| "majority" of three (the voter counts itself, as in Simmel's form) | `sum(x) >= 2` |
| "at least k of" A, B, C, D | `x[a] + x[b] + x[c] + x[d] >= k` |
| "all agree" | `x[0] & x[1] & x[2]` (every party) |
| "watches but does nothing" | it reads others and nobody reads it; it falls out of the core, so say so |
| "can deal directly" | the bypass call below, not a new rule |

Four rules govern the translation.

- **Ask what each party responds to.** A sentence rarely says. If it is silent, ask the author one
  question ("what does the driver react to?") or run both readings side by side. In rehearsal one
  sentence gave Φ = 2.0 or Φ = 0.0 depending on that answer alone (see the rating example below).
- **Avoid self-copies** (`x[i]` in party i's own rule) unless the sentence says a party holds its own
  state. A self-copying node is a complex of one; the helper reports it as "keeps its own state".
- **Print the rules in words** before running, one line per party, so the author can read them out:
  "M goes on only when A and B both do; A and B each follow M."
- **Do not add parties the sentence lacks** to make the model more interesting.

## The calls

The helper, from the repo root (the import resolves because `python -c` puts the cwd on the path):

```bash
python -c 'from submissions.triadic_reduction.talk.live.show import show; show("dispatcher", "AMB", ["x[1]", "x[0] & x[2]", "x[1]"])'
```

The same helper from the command line, which works from any directory:

```bash
python submissions/triadic_reduction/talk/live/show.py dispatcher AMB "x[1]" "x[0] & x[2]" "x[1]"
python submissions/triadic_reduction/talk/live/show.py car_dealer MDB "x[2]" "x[0]" "x[1]" --bypass D B M
```

`show(name, labels, rules, bypass=None, mode="replace", raw=False)`. `bypass=(party, downstream, upstream)`
asks "what if downstream could deal with upstream directly?": downstream reads upstream instead of its
old source (`mode="replace"`, the franchise-law case) or as well as it (`mode="add"`, `--add`, a
back-channel). `raw=True` (`--raw`) also prints the reader's own audit line, which is what CI registers.

The raw fallback needs no helper. Paste it with the rules as lambdas:

```bash
python -c 'from org_frontier.thinkers.peirce.probe_peirce_joint_determination import read; read("dispatcher", (("A","M","B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]))'
python -c 'from org_frontier.classifier.contingency import contingency_test as ct; print(ct([lambda x: x[2], lambda x: x[0], lambda x: x[1]], ("M","D","B"), "D", downstream="B", upstream="M").line())'
```

Never call `verdict(...).structure`, `classifier.cli`, `simmel.forms.evaluate`, `validate` or any probe
script on screen: all of them print the CI label words.

## What goes on screen, and what to say

The helper prints three lines and nothing else; leave them as the last thing on screen. The author reads
them out. When the author asks what a line means, answer with the words in the last column.

| line | meaning | say |
| --- | --- | --- |
| `Whole, Φ = 2.0` | no cut into parts leaves the parts running as before | "This one does not come apart." |
| `Factors, Φ = 0.0` | some cut leaves the parts unchanged | "This one comes apart into pieces." |
| `Core: A, B, M` | the largest set that holds together | "These parties hold together." |
| `Core: A, B   (outside: M)` | M can be cut away without loss | "M can be cut away without loss." |
| `Set by two others: M by A+B, inside the core` | M's next state depends on A and B jointly, inside the whole | "M is set by A and B together, inside the whole: the talk's triad, in this model." |
| `…, no whole holds them` | joint determination in a system that factors | "Set by two together, but nothing holds them in one whole." |
| `(tied reading)` | the reader found tied purviews; the reading is not robust | "The reader finds a tie here, so treat that line as weak." |
| `Set by two others: nobody` | nobody is jointly determined | "Nobody here is set by two others." |

A whole with nobody set by two others is common: a ring of one-input copies is one (Φ = 2.0, README
"Triad criterion"), and so is the car dealer, a ring of three relays. When the helper prints `Whole` over `Set by two others: nobody`,
say "a whole, but nobody is set by two others; wholeness is not yet the triad."

With `bypass`, the helper prints before → after: Φ, the core, then the party's fate in words
("needed only while the direct deal is barred", "still needed when they can deal directly", "still in,
but the whole weakens", "never needed").

Under the first result only, print one more line for the author to read: **"These are small Boolean
models, not people."**

## What never to claim

CLAIM.md is locked; these lines bind the live session.

- Not that Φ > 0 means a triad, or algorithmacy (CLAIM.md:75). Wholeness is the first line; the triad is
  the third line inside the second.
- No CI label words on screen, spoken or printed (CLAIM.md:76). The helper never prints them. The arm's
  directory name appears in the typed path; do not comment on it.
- Nothing about the audience member's real workplace, platform or rule (CLAIM.md:97). The model is the
  sentence as translated, not their firm. Say "your sentence, as I translated it".
- Not that the result "refutes Quine" (CLAIM.md:100) or refutes Quinean reductionism (CLAIM.md:61), and
  not that it resolves the debate (CLAIM.md:62).
- Not that joint determination and wholeness cross "both ways" (CLAIM.md:81).
- A live number is computed, not registered. It goes on no slide and into no paper until it is in
  `ci/reproduce.json` (CLAIM.md:82; README ground rule 3). If asked, say "computed just now, not yet
  registered".
- Do not interpret beyond the three lines. If the room wants more, offer to log it as a question.

## Size and time limits (measured 2026-09-25, this laptop, venv-4.0)

Wall time for one call includes about 1.5 s of Python and PyPhi import.

| form | nodes | compute | wall (one process) |
| --- | --- | --- | --- |
| rehearsed three-node forms | 3 | 0.07–0.48 s | 1.6–2.4 s |
| dealer with bypass | 3 | 0.9–1.2 s | 2.4 s |
| clique_4 (every party reads all others) | 4 | 7.2 s (10.5 s with other jobs running) | 8.8 s |
| auction, four suppliers, any bid clears | 5 | 9.2 s | about 11 s |
| auction, four suppliers, two bids clear | 5 | 2.1 s | about 4 s |
| clique_5 (every party reads all others) | 5 | 569.5 s | 9.5 min |
| auction, five suppliers, any bid clears | 6 | Φ and core alone 55.5 s; full read stopped at 15 min | over 15 min |

Density costs more than size. Any four-node form finishes in about 10 s. A five-node form is safe only
when at most one party reads more than one other (the auction star, 9.2 s); a dense five-node form took
9.5 minutes. Refuse six: say "six parties takes minutes; here is the four-party version", and drop the
parties the sentence cares least about. If a call runs past 30 s, interrupt it (Ctrl-C) and shrink the
form.

## Rehearsed prompts (run 2026-09-25 on Opus 5.5; every output matched its registered string)

The sentences are the ones the author may seed if the room is quiet. Prompt 2 is reworded from the
design brief so that the sentence matches the registered form, in which nobody reads the manager.

| # | sentence | parties and rules | helper output (rehearsed) | registered (CI check) | compute / process |
| --- | --- | --- | --- | --- | --- |
| 1 | "The dispatcher assigns only when driver and rider both accept; both wait on the dispatcher." | A driver, M dispatcher, B rider: `x[1]`, `x[0] & x[2]`, `x[1]` | `Whole, Φ = 2.0` / `Core: A, B, M` / `Set by two others: M by A+B, inside the core` | `control Φ_MIP=2.000000  core=('A', 'B', 'M') … jd=True  in_whole=True   M <- AB (φ=2.000)` (thinkers-peirce-jd) | 0.27 s / 1.8 s |
| 2 | "Client and worker now answer each other directly; the manager still hears both, but nobody waits on the manager." | A client, M manager, B worker: `x[2]`, `x[0] & x[2]`, `x[0]` | `Factors, Φ = 0.0` / `Core: A, B   (outside: M)` / `Set by two others: nobody` | `mediator_eliminated … Φ_MIP=0.000000  core=('A', 'B') coreΦ=2.000` (thinkers-simmel-h4-nonpartisan) | 0.11 s / 1.6 s |
| 3a | "A three-person committee decides by majority …" | A, B, C, each `sum(x) >= 2` | `Factors, Φ = 0.0` / `Core: none` / `Set by two others: C by A+B, no whole holds them (tied reading)` | `majority_triad Φ_MIP=0.000000  core=() … jd=True  in_whole=False  C <- AB (φ=0.500, tied)` (thinkers-peirce-jd) | 0.36 s / 2.2 s (3a and 3b together) |
| 3b | "… then by unanimity." | A, B, C, each `x[0] & x[1] & x[2]` | `Whole, Φ = 6.0` / `Core: A, B, C` / `Set by two others: A by B+C; B by A+C; C by A+B, inside the core` | `unanimity_triad … Φ_MIP=6.000000  core=('A', 'B', 'C') coreΦ=6.000` (thinkers-simmel-h3-majority) | 0.48 s |
| 4 | "A dealer stands between maker and buyer; then let the maker sell direct." | M maker, D dealer, B buyer: `x[2]`, `x[0]`, `x[1]`; bypass D, B reads M | `Whole, Φ = 2.0  ->  B deals with M directly: Factors, Φ = 0.0` / `Core: B, D, M  ->  B, M` / `D: needed only while the direct deal is barred` | `contingent margin=2.000  D in core: constrained=True bypass=False  (Phi 2.000 -> 0.000)` (q213-contingent-irreducibility) | 1.18 s / 2.4 s |

The helper's third line for 3b (unanimity) and the bypass core `B, M` in 4 are computed but not
registered; the registered parts are Φ and the cores shown in the fifth column.

The pre-flight and fallback commands, in order:

```bash
python submissions/triadic_reduction/talk/live/show.py dispatcher AMB "x[1]" "x[0] & x[2]" "x[1]"
python submissions/triadic_reduction/talk/live/show.py mediator_eliminated AMB "x[2]" "x[0] & x[2]" "x[0]"
python submissions/triadic_reduction/talk/live/show.py majority_triad ABC "sum(x) >= 2" "sum(x) >= 2" "sum(x) >= 2"
python submissions/triadic_reduction/talk/live/show.py unanimity_triad ABC "x[0] & x[1] & x[2]" "x[0] & x[1] & x[2]" "x[0] & x[1] & x[2]"
python submissions/triadic_reduction/talk/live/show.py car_dealer MDB "x[2]" "x[0]" "x[1]" --bypass D B M
python submissions/triadic_reduction/talk/live/show.py clique_4 ABCD "x[1] & x[2] & x[3]" "x[0] & x[2] & x[3]" "x[0] & x[1] & x[3]" "x[0] & x[1] & x[2]"
```

Practice only: "four people who each wait on all three others" is clique_4, `Whole, Φ = 12.0`, core
A, B, C, D, each set by the other three (registered `clique_4 … Φ_MIP=12.000000`, thinkers-simmel-h2-number).

Two fresh sentences went through the recipe end to end in rehearsal.

| sentence | translation | helper output | compute |
| --- | --- | --- | --- |
| "A platform shows each driver's rating to the rider only after both accept." (a) both respond to what the platform shows | D, P, R: `x[1]`, `x[0] & x[2]`, `x[1]` | `Whole, Φ = 2.0` / `Core: D, P, R` / `Set by two others: P by D+R, inside the core` | 0.17 s |
| (b) each keeps their own acceptance | `x[0]`, `x[0] & x[2]`, `x[2]` | `Factors, Φ = 0.0` / `Core: none that binds two parties (R only keeps its own state)` / `nobody` | 0.07 s |
| (c) the rider reacts to the rating, the driver keeps their own | `x[0]`, `x[0] & x[2]`, `x[1]` | `Factors, Φ = 0.0` / `Core: P, R (outside: D)` / `P by D+R, no whole holds them` | 0.08 s |
| "Four suppliers bidding through one auctioneer." Any bid clears | A–D each `x[4]`; U `x[0] \| x[1] \| x[2] \| x[3]` | `Whole, Φ = 4.0` / `Core: A, B, C, D, U` / `Set by several others: U by A+B+C+D, inside the core` | 9.2 s |
| Two bids clear | U `sum(x[:4]) >= 2` | `Factors, Φ = 0.0` / `Core: none` / `U by A+B, no whole holds them` | 2.1 s |

One sentence, three readings, two verdicts: the rating sentence is why the recipe says to ask what
each party responds to. None of these numbers is registered.

## Failures and fallbacks

| failure | do this |
| --- | --- |
| assistant slow (over 20 s to answer) | `/model` to Sonnet 5, or the author types the helper command from the table |
| network down | the author types the one-liners from the tables above into a plain terminal; the computation is local |
| a rule errors (`IndexError`, `NameError`) | count labels against rules; rules use only `x`, `&`, `\|`, `1 -`, `sum`, `all`, `any`, `range` |
| a call runs past 30 s | Ctrl-C, drop a party, rerun |
| the output surprises the room | read the three lines, give the translation again, offer to log it; do not improvise a theory |
| a pre-flight output differs from the table | do not run live; use slide 22 |
| laptop down | slide 22: the rehearsed forms and their registered outputs |

## Afterwards

1. Log every run to `submissions/triadic_reduction/talk/live/ALGOCON-2026-10-xx.md` (xx is the talk
   day): the sentence verbatim, who asked (a name only with their consent), the labels and rules, the
   three lines and the raw line, the seconds, and whether the asker accepted the translation.
2. A live form becomes a lab question only through the protocol:
   `python -m org_frontier.protocol.new_question --slug <slug> --question "<one line>"`. The live form's
   result already exists, so label it "exploratory, computed live at ALGOCON 2026 before
   pre-registration", or commit `hypotheses.md` for an unrun variant first and then compute.
3. Register every number the question reports in `ci/reproduce.json`, copied verbatim from a real run,
   and check it with `python ci/reproduce.py <check-name>`.
4. `python tools/build_index.py`.
5. The author opens the pull request into `contrib` (`gh pr create --base contrib`). No agent pushes or
   opens it.
