# The Chicken-and-Egg Feed: First Causes, Loops, and Φ in Stylized Post Spread

code + data: `org_frontier/questions/q218_chicken_egg_feed/` ; probe #454 in `probes/PROBES.md`

## Abstract
A celebrity's post, a feed, and an audience were modeled as eleven small Boolean networks: broadcast, word
of mouth, chronological and engagement-ranked feeds, with and without a celebrity who reacts to engagement
and an audience that sees itself, plus feedforward and ring controls. Exact IIT-4.0 Φ classified each form,
four ten-rule encoding sweeps tested robustness, and each form's causal graph was checked for a first cause
(a part that influences the rest without being influenced back). Every form with a first cause read Φ = 0,
a known consequence of IIT's definition. Removing the first cause was not sufficient: 13 of 35 loop forms
still factored, including the headline engagement-feed loop with a reacting celebrity, whose core is the
celebrity–feed pair alone. Word of mouth with a reacting celebrity and no feed was the most integrated form
(Φ = 6.000). Two pre-registered hypotheses were refuted. The models are stylized and make no claim about any
real platform.

## Introduction
"Which came first, the outrage or the amplification?" has a structural form: if one part drives the rest
without being driven back, the arrangement has a first cause; if every part depends on every other, no part
comes first. The lab's thesis ties irreducibility (Φ > 0) to coordination that cannot be split into pairs.
The question is whether engagement-reactive feeds create such irreducibility, and whether the feed, the
audience's mutual visibility, or the celebrity's reaction is what does it.

## Related work
Threshold and cascade models describe spread from seeds and from observing others (Granovetter 1978;
Bikhchandani et al. 1992; Banerjee 1992; Kempe et al. 2003), complex contagion requires reinforcement
(Centola and Macy 2007; Centola 2010), and visible popularity counts amplify inequality (Salganik et al.
2006). Online cascades range from broadcast to viral (Goel et al. 2016), and false news spreads farther
(Vosoughi et al. 2018). Ranked feeds shape exposure (Bakshy et al. 2015) and amplify political content
relative to a chronological control (Huszár et al. 2022); recommenders that learn from responses to their
own recommendations form feedback loops (Chaney et al. 2018; Jiang et al. 2019). IIT defines Φ over the
minimum partition (Tononi 2004; Albantakis et al. 2023), purely feedforward systems have Φ = 0 (Oizumi et
al. 2014), and the unfolding argument notes that behavior does not fix Φ (Doerig et al. 2019). PyPhi computes
it (Mayner et al. 2018). Full report: `literature/deep_research_report.md` (18 verified sources).

## Hypotheses
Fixed in `hypotheses.md` before computation. H1: feedforward forms Φ = 0 (a known property, run as a
control). H2: an unmoved celebrity factors the whole; the loop core excludes the celebrity. H3: a celebrity
who reacts to trending closes the loop, giving a triadic form with all four in the core. H4: recurrence
without an engagement feed also binds. H5: Φ > 0 if and only if the causal graph is strongly connected (the
converse in at least 90% of forms), and the engagement loop is triadic in at least 8 of 10 feed rules.

## Methods
Nodes P (celebrity), F (feed), A and B (fans). Eleven forms with rules and rationale in `methods.md`; for
example FEED-ENG-REACT is P' = F, F' = P ∧ (A ∨ B), A' = F, B' = F. Whole-system verdict and major complex from
the lab classifier; strong connectivity from the connectivity matrix; four sweeps replace one rule by each
two-input function depending on both inputs. Controls passed first. A tie table and three variants added
after the first run are labeled exploratory.

## Results
**H1 confirmed.** BROADCAST, FEED-CHRONO and CHAIN: Φ = 0.000, no subset of two or more nodes with Φ > 0.

**H2 confirmed (6/6).** CONTAGION core {A,B} (2.000), FEED-ENG {F,A,B} (2.000), FEED-ENG-COUNTS {F,A,B}
(6.000), all with whole-system Φ = 0.

**H3 refuted (0/4).** FEED-ENG-REACT: Φ = 0, core {P,F} (2.000). FEED-ENG-REACT-COUNTS: Φ = 0, core {A,B} tied
with {P,F} at 2.000.

**H4 confirmed (3/3).** WOM-REACT 6.000, FEED-CHRONO-REACT 1.000, RING 2.000.

**H5 refuted (1/3).** No triadic form lacks strong connectivity (0 of 51). Of 35 strongly connected forms 22
are triadic (0.63). The engagement-loop feed rule binds in 4/10 encodings. Other sweeps: FEED-ENG 0/10,
FEED-ENG-REACT-COUNTS fan rule 6/10, WOM-REACT celebrity rule 9/10.

**Exploratory.** With one fan the engagement loop is the canonical triad (Φ = 2.000, core {P,F,A}); with a feed
that needs both fans it binds all four (Φ = 3.000); with heterogeneous fans it still factors to {P,F}.
Figure: `results/chicken_egg.png`.

## Discussion
The "no clear first cause" intuition maps onto strong connectivity of the causal graph, and its contrapositive
(a first cause implies Φ = 0) is IIT's own feedforward property, confirmed here without exception but not
new. The informative results are the failures of the converse. An engagement feed and a reacting celebrity
form a genuine chicken-and-egg loop, yet the audience is substitutable (either fan suffices), so the loop
that binds is celebrity ↔ feed and the whole factors. This is the lab's substitution and quorum logic in a
new setting: a party is bound only if it makes a difference. Word of mouth with a reacting celebrity binds
more strongly than any feed form, so in these models the algorithm is neither necessary nor sufficient for
irreducibility.

## Limitations
Stylized 3–4 node synchronous models with stipulated rules; two fans stand in for an audience. Results vary
with the rule encoding (S1 4/10, S3 6/10). Ties and the exploratory variants were not pre-registered. Φ
reflects causal structure, not behavior (Doerig et al. 2019), and no claim about consciousness is made. IIT
4.0 only (Q215). The validation gap to real platforms is unchanged.

## References
Albantakis, L., et al. (2023). doi:10.1371/journal.pcbi.1011465.
Bakshy, E., Messing, S., & Adamic, L. A. (2015). doi:10.1126/science.aaa1160.
Banerjee, A. V. (1992). doi:10.2307/2118364.
Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). doi:10.1086/261849.
Centola, D. (2010). doi:10.1126/science.1185231.
Centola, D., & Macy, M. (2007). doi:10.1086/521848.
Chaney, A. J. B., Stewart, B. M., & Engelhardt, B. E. (2018). doi:10.1145/3240323.3240370.
Doerig, A., Schurger, A., Hess, K., & Herzog, M. H. (2019). doi:10.1016/j.concog.2019.04.002.
Goel, S., Anderson, A., Hofman, J., & Watts, D. J. (2016). doi:10.1287/mnsc.2015.2158.
Granovetter, M. (1978). doi:10.1086/226707.
Huszár, F., et al. (2022). doi:10.1073/pnas.2025334119.
Jiang, R., Chiappa, S., Lattimore, T., György, A., & Kohli, P. (2019). doi:10.1145/3306618.3314288.
Kempe, D., Kleinberg, J., & Tardos, É. (2003). doi:10.1145/956750.956769.
Mayner, W. G. P., et al. (2018). doi:10.1371/journal.pcbi.1006343.
Oizumi, M., Albantakis, L., & Tononi, G. (2014). doi:10.1371/journal.pcbi.1003588.
Salganik, M. J., Dodds, P. S., & Watts, D. J. (2006). doi:10.1126/science.1121066.
Tononi, G. (2004). doi:10.1186/1471-2202-5-42.
Vosoughi, S., Roy, D., & Aral, S. (2018). doi:10.1126/science.aap9559.

Full entries in `literature/references.bib`.
