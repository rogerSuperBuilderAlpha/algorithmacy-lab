# Findings — one of 88 management abstracts signals any reproducibility practice

Across 88 empirical management and organization papers from 2015–2025, exactly one abstract carries a
visible reproducibility signal, and that one is a registered report whose *subject* is open-science
practice. Open data and shared code appear in zero abstracts. Whatever data-availability practice the
field has adopted, its abstracts do not carry it.

## Intercoder reliability
| variable | Fleiss' κ | agreement |
|---|---|---|
| open_data | 1.000 | 100% |
| code_available | 1.000 | 100% |
| preregistered | 1.000 | 100% |
| method_type | 1.000 | 100% |

Three independent agent coders returned identical signaling codes on all 88 sources. Perfect
agreement here is not a coding triumph; it reflects a signal that is a near-constant zero, trivial to
code. The κ discharges the single-coder objection, but the reliability is itself a datum: there was
almost nothing to disagree about.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | Signaling is uncommon overall | Supported | any-signal 1/88 = 1.1% |
| H2 | Signaling rose 2015–2019 → 2020–2025 | Qualified | 0/40 (0.0%) → 1/48 (2.1%); rests on one paper |
| H3 | Quantitative signal more than qualitative | Qualified | quant 1/64 (1.6%) vs qual 0/8 (0.0%); rests on one paper |

Per-practice rates (adjudicated, lower bounds): open_data 0/88 (0.0%), code_available 0/88 (0.0%),
preregistered 1/88 (1.1%).

## What the data revise
H1 is supported without qualification: in-abstract reproducibility signaling is not merely a minority,
it is nearly absent. The prediction was "a minority"; the finding is "one paper."

H2 and H3 point in the predicted direction, and neither is distinguishable from zero. The rise over
time and the quantitative advantage both trace to the *same single* signaling paper — a 2024
registered-report survey of open research practices, coded quantitative. Remove that one paper and both
comparisons collapse to 0% versus 0%. These are floor effects, not trends. The corpus carries too
little signal to test H2 or H3: the field's abstracts sit on the floor across every year and every
method, so the directional wins are artifacts of where a single atypical paper happened to land.
Direction reported, weight withheld.

The method distribution is worth recording on its own: 64 quantitative, 9 conceptual, 8 qualitative, 7
mixed. The nine "conceptual" sources are open-science topical papers that discuss data sharing and
pre-registration without signaling that the article itself does either. The literature *about* the
practice shows up in abstracts in a way the practice itself does not.

## Limitations
Abstract-only coding is the load-bearing limitation. Data-availability statements, open-materials
notes, and repository links overwhelmingly live in a paper's back matter, not its abstract, and a
growing number of journals generate them from submission metadata rather than author prose.
Abstract-only coding therefore undercounts real practice, and every rate here is a **lower bound**. The
gap between this lower bound and the true rate is exactly the quantity a full-text audit would recover.
The near-zero abstract rate is a real finding about one channel — what a reader or a screening tool
sees first — not a claim that the field deposits no data. The corpus is bounded by the Scholar Gateway
connector's coverage and by English-language indexing, and it is capped at 8 papers per year for an
even trend spread, so it samples the field rather than censusing it. Coders are LLM agents applying a
fixed codebook, not trained human raters; agreement among agent passes is high but does not substitute
for independent human coding.

## Reproduce
```bash
# from the repo root
python3 -m org_frontier.reviews.reproducibility_signaling.build_corpus \
    org_frontier/reviews/reproducibility_signaling/.raw_search
python3 -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/reproducibility_signaling/coding \
    --categorical open_data,code_available,preregistered,method_type \
    --out org_frontier/reviews/reproducibility_signaling/results/frozen.json
python3 -m org_frontier.reviews.reproducibility_signaling.run
```
Registered numbers: any-signal 1/88 (1.1%); κ = 1.000 on all four variables; by-period 0/40 vs 1/48.
