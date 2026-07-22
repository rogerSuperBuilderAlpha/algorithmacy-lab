# Findings — the algorithmic-management literature describes control and measures worker reactions

A coded corpus of 66 algorithmic-management sources splits its labor unevenly. Control and worker
experience take three-quarters of the field's attention; productivity and firm performance take 4.5
percent. The evidence base is majority conceptual and qualitative. And the field's signature claim —
that algorithmic management is a new form of control over workers — is carried almost entirely by
conceptual and qualitative sources: not one of the 22 sources whose focal outcome is control reports
quantitative evidence. The quantitative studies exist, but they measure worker reactions (engagement,
burnout, stress), not the control claim itself.

## Intercoder reliability
Three independent agent coders applied a fixed codebook to title and abstract, blind to one another.

| variable | Fleiss' kappa | agreement | interpretation |
|---|---|---|---|
| claim_type | 0.747 | 82.8% | substantial |
| evidence | 1.000 | 100.0% | almost perfect |
| outcome | 0.895 | 92.9% | almost perfect |

Kappa this high across three coders discharges the single-coder objection: the distributions below are
not one reader's construal. Evidence type was unanimous on all 66 sources — method is stated plainly in
abstracts. Claim type, the most interpretive variable, still reached substantial agreement.

## Results
Verdicts on the majority-vote adjudicated dataset (n = 66).

| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | Outcomes skew to control + worker experience; performance rare | Supported | control+experience 49/66 (74.2%); performance 3/66 (4.5%) |
| H2 | Mostly conceptual/qualitative; quantitative uncommon | Supported | conceptual+qualitative 46/66 (69.7%); quantitative 16/66 (24.2%), +mixed 30.3% |
| H3 | "Algorithm controls workers" asserted widely, tested rarely | Supported | control-outcome sources 0/22 quantitative; stylized-fact-control subset 91% conceptual/qualitative vs 30% corpus-wide |

### H1 — the outcome mix
Worker experience (27 sources) and control (22) together are 74.2 percent of the corpus. Performance is
three sources: an algorithmic-bias-and-HRM-effectiveness study, a gig-worker safety-behavior study, and
a mixed-methods study of proactive customer-service performance. All three reach performance through a
worker-level mechanism, not through a firm productivity measure. The category the managerial literature
would foreground — does algorithmic management make the operation more productive — is nearly absent.

### H2 — the evidence base
Conceptual work (25) and qualitative work (21) are 69.7 percent of the corpus. Quantitative sources are
16 (24.2 percent), rising to 20 (30.3 percent) with the four mixed-methods studies. Quantitative is a
real and growing minority, concentrated in the most recent years and in survey studies of gig-worker
psychology. It remains, for now, at the field's margin.

### H3 — control described, reactions measured
The sharpest result is a cross-tabulation. Of the 22 sources whose focal outcome is control, zero are
quantitative and one is mixed; the other 21 are conceptual or qualitative. The 12 sources that assert
control as an established fact (claim_type = stylized_fact) rest 91.7 percent on conceptual or
qualitative evidence. Meanwhile every quantitative study of a control-adjacent construct measures a
worker reaction instead — engagement, burnout, technostress, thriving — coded to worker experience, not
control. The field's quantitative apparatus is pointed at how workers feel, not at whether the control
claim holds. The control claim functions as a stylized fact: 12 sources assert it and 28 more assume it
to motivate other work, and it is the least tested premise in the corpus.

## What the data revise
The three hypotheses are supported, and H3 sharpens into a more specific claim than pre-registered. The
control proposition is tested less than asserted, and in the sources that foreground it, it is almost
never tested quantitatively — 21 of 22 control-outcome sources are conceptual or qualitative. The quantitative turn in this literature is real but has routed around the
founding claim: it studies the worker's response to control rather than the reach or existence of
control. That is a live opening for measurement, located precisely.

## Limitations
The coders are three LLM agents applying a fixed codebook, not trained human raters; agreement among
agent passes is high but is not a substitute for independent human coding. Coding used title and
abstract only, so a study's full method or a secondary outcome can be missed — a paper that computes a
control measure in its body but abstracts on worker reactions would be coded to worker experience.
Systematic literature reviews were coded as conceptual, a defensible but consequential call for H2. The
corpus is bounded by two semantic-search connectors and English-language indexing, and it oversamples
HRM and organizational-behavior venues relative to the sociology and information-systems wings of this
literature; the 4.5-percent performance share is an estimate for this corpus, not a census. Performance
as an outcome may be underrepresented because operations-management and platform-economics work on
algorithmic efficiency uses different vocabulary and sits outside the search frame.

## Reproduce
```bash
# 1. rebuild the corpus from the saved semantic-search payloads + the Consensus seed
python3 -m org_frontier.reviews.algorithmic_management_claims.build_corpus --sg-dir <scholar_gateway_txt_dir>
# 2. reliability + adjudicated dataset
python3 -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/algorithmic_management_claims/coding \
    --categorical claim_type,evidence,outcome \
    --out org_frontier/reviews/algorithmic_management_claims/results/frozen.json
# 3. hypothesis tests + summary.json
python3 -m org_frontier.reviews.algorithmic_management_claims.run
```
Registered numbers: `results/summary.json` (n, the H1/H2/H3 shares) and the reliability table above.
