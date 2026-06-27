# Q205 — findings

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | F0 immediate triad: triadic, Φ_MIP = 2.000 |
| H2 represented latency stays triadic | confirmed | F1 (n=4, buffer B): triadic, Φ_MIP = 1.000 |
| H3 the delay node is load-bearing | confirmed | major complex of F1 = {S, C, B}, Φ = 2.000; B is in the core |
| H4 hidden latency hides integration | confirmed | F2 (one-step TPM over W,S,C only): dyadic, Φ_MIP ≈ 0 |
| H5 estimation alone preserves integration | confirmed | estF0 (same estimation, no latency): triadic, Φ_MIP = 0.765 |

**Through-line.** A one-step exact Φ misses lagged coordination only when the lag is left out of the model.
The integrated conjunctive triad keeps its triadic verdict when a one-step delay is inserted as a buffer
node B (F1): the form stays irreducible, the buffer enters the major complex, and the irreducible core is
{S, C, B} at Φ = 2.0. The same dynamics observed through a one-step transition matrix over only the
parties and the mediator (F2) factor completely — dyadic, Φ ≈ 0 — because the worker's next state depends
on the mediator's value one step earlier, which the current observed state does not carry. The reading is
specific to the unrepresented delay, not to the estimation procedure: estimating the same way from the
immediate triad (estF0) still reads triadic at Φ = 0.765. Two facts sharpen the picture beyond a yes/no.
Representing the delay halves the whole-system Φ_MIP (2.0 to 1.0) even though the maximal complex still
reaches 2.0, so latency redistributes integration rather than leaving it untouched. And the worker drops
out of F1's major complex while the buffer enters it: the delay node becomes the load-bearing member, and
the worker now reaches the loop only through it. This turns the q204 caveat into a usable rule — a low
one-step Φ on a coordination with known lag means the lag is unmodeled, and giving the delay its own node
recovers the integration.

**Caveats.** In-silico Boolean models with exact Φ, n ≤ 4, a single one-step delay and one reference
triad. The hidden-latency TPM is estimated from a 20000-step trajectory with 5% output noise at seed 0;
the F2 verdict is the best one-step Markov approximation to a process that is not one-step Markov, which is
exactly the instrument an analyst applies to a real lagged series. Evidence about the instrument's blind
spot, not a measurement of any organization. Longer delays, multiple buffers, and stochastic mediators are
open (queued as follow-ups).

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q205_latency_feedback.probe_latency_feedback`
