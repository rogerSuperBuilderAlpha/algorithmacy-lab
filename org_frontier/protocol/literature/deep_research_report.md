# The methodology behind the six-stage protocol — a literature survey

Deep-research run, June 2026. Five search angles (strong inference and multiple working
hypotheses; pre-registration and registered reports; verification and validation of
simulation/agent-based models; autonomous AI-driven discovery and its failure modes;
reproducibility and computational-research practice). Twenty-four claims survived a 3-vote
adversarial verification check; one claim was killed. Twenty-three of the survivors are carried
into the synthesis below. Every load-bearing source is a primary peer-reviewed article or the
canonical classic; no blog or forum source is load-bearing.

The question: how should rigorous AI-augmented, hypothesis-driven, in-silico research be
conducted, and where does the specific six-stage per-question protocol sit against that
literature. The protocol's stages: (1) cursory review of prior work, (2) deep literature
research, (3) fix five falsifiable working hypotheses with their nulls before any computation,
(4) specify methods per hypothesis, (5) run the computational tests against a ground-truth
instrument, (6) write a full quantitative paper that reports nulls and refutations as
first-class results.

---

## 1. The classical backbone: multiple working hypotheses

The protocol's stage 3 — fix several falsifiable hypotheses with their nulls before computing —
descends directly from Chamberlin's 1890 method of multiple working hypotheses. Chamberlin
prescribes bringing up every rational explanation of a phenomenon and developing every tenable
hypothesis at once, so the investigator becomes "the parent of a family of hypotheses" and is
"forbidden to fasten his affections unduly upon any one" [Chamberlin 1890/1965]. The reason is a
named failure mode of single-hypothesis work. Once one explanation is offered, the mind performs
"an unconscious selection and magnifying of the phenomena that fall into harmony with the theory
and support it, and an unconscious neglect of those that fail of coincidence," degenerating into
"the partiality of paternalism" [Chamberlin 1890/1965]. Chamberlin's diagnosis is psychological:
the central fault is "the admission of intellectual affection to the place that should be
dominated by impartial intellectual rectitude," and the multiple-hypotheses method works by
neutralizing the investigator's emotional partiality [Chamberlin 1890/1965].

Holding several hypotheses at once is the structural defense against confirmation bias that the
protocol builds into stage 3. The protocol gets this right.

Whether the number should be five is not something Chamberlin licenses. He says "every tenable
hypothesis," a count set by the phenomenon, not a fixed quota. A modern reconstruction sharpens
the point. Yanco et al. (2020) give a five-step pre-data-collection workflow for ecology — specify
candidate hypotheses, write a formal model for each, generate sampling distributions from
simulated data, quantify the variance within and overlap between those distributions, then revise
and repeat [Yanco 2020]. They argue pre-data-collection modelling "should be considered the
default mode for scientific investigations" because models built before data increase clarity and
transparency about hypotheses [Yanco 2020]. This parallels the protocol's pre-commit-then-simulate
structure and supplies a principled basis for vetting hypotheses by simulation before any real
test.

The same paper supplies the caution the protocol must absorb. Pre-data modelling exists to detect
"degenerate" relationships, where multiple distinct processes produce indistinguishable patterns,
and "noisy" relationships, where one mechanism produces varied patterns [Yanco 2020]. This is an
identifiability problem. It governs whether a fixed set of hypotheses can even be told apart by the
chosen instrument. A count of five is informative only if the five are identifiable under the
instrument; an arbitrary quota of five is not automatically informative, and could fix on
hypotheses the instrument cannot separate. Two further limits attach. The workflow is scoped to
ecology, so transferring it to Boolean-model organizational work is a domain extrapolation. And the
authors note the workflow does not by itself overcome the cognitive barriers to generating good
hypotheses and cannot guarantee that all plausible processes were found [Yanco 2020]. The
five-hypothesis rule is defensible as a discipline against single-hypothesis attachment. It is not
principled as a fixed number.

## 2. Pre-registration and registered reports

Stage 3's "before any computation" clause is a pre-registration move. The canonical definition:
pre-registration commits to analytic steps without advance knowledge of the research outcomes,
"usually accomplished by posting the analysis plan to an independent registry such as
clinicaltrials.gov or osf.io" [Nosek 2018]. A second standard definition adds the content and the
venue: "declaring a research plan (for example, hypotheses, design and statistical analyses) in a
public registry before the research outcomes are known" [Hardwicke 2023]. Both definitions name a
public registry. The protocol's internal pre-commitment satisfies the timing requirement — fix
before compute — but not the public, timestamped, discoverable-registry requirement that the
literature treats as the operative form. An internal pre-commitment is a weaker variant.

The argued benefits are two and should be kept separate. Pre-registration reduces the risk of bias
by encouraging outcome-independent decision-making, and it increases transparency, letting others
assess the risk of bias and calibrate their confidence in the reported outcomes [Hardwicke 2023].
The mechanism is enforcing the distinction between confirmatory prediction and exploratory
postdiction. Testing genuine predictions is what gives diagnostic evidence for explanatory claims;
presenting postdictions as predictions "can increase the attractiveness and publishability of
findings by falsely reducing uncertainty" [Nosek 2018]. When analytic choices are made after seeing
the data — the garden of forking paths — it can become "impossible to estimate the paths that could
have been selected if the data had looked different," rendering findings uninterpretable [Nosek
2018]. Registered Reports extend this by granting in-principle acceptance before results are known,
which reduces publication bias and the problem that published results are not representative of all
studies performed [Lakens 2024]. The shared core: transparency around the line between decisions
made before data collection and post-hoc decisions made afterward [Lakens 2024].

The evidence on whether pre-registration delivers is mixed, and this is the part the protocol
should weigh most carefully. An analysis of 15,992 test statistics from RCTs in 15 leading
economics journals (2018–2021) found no meaningful difference in the distribution of test
statistics between pre-registered and non-pre-registered studies [Brodeur 2024]. The reduction
appears only when pre-registration is accompanied by a complete pre-analysis plan; studies with a
complete PAP are significantly less p-hacked [Brodeur 2024]. The authors conclude it is the
pre-analysis plan, not the act of registration in itself, that ensures credibility [Brodeur 2024].
For the protocol this is the load-bearing finding. Stage 4 — specify methods per hypothesis — is
the analogue of the PAP, and it is stage 4, not the bare pre-commitment of stage 3, that does the
credibility work. A pre-commitment that fixes hypotheses but leaves the per-hypothesis test
underspecified would, on this evidence, buy little.

The pre-registration benefits are argued and partly contested, not settled empirical fact. Lakens
et al. (2024) describe these as design intents — pre-registration and Registered Reports "aim to"
counteract bias [Lakens 2024]. A claim that the practices have been shown to achieve their
bias-reduction goals and additionally improve study quality was tested and refuted in this run;
that stronger reading is not supported. A live conceptual debate also bears on stage 3. Ledgerwood
(2018) argues that two functions are commonly conflated: pre-registering a theoretical directional
prediction clarifies how a hypothesis is constructed and enables theory falsifiability, while
pre-registering an analysis plan clarifies how evidence is produced and enables type I error
control [Ledgerwood 2018]. These are distinct goals. And type I error control via a pre-analysis
plan is useful not only in confirmatory work but also in exploratory, theory-building work;
restricting analysis-plan pre-registration to the confirmatory phase is an error [Ledgerwood 2018].
The protocol's stage 3 mixes both functions — directional hypotheses with their nulls (theory
falsifiability) plus a method per hypothesis (error control). Keeping the two functions explicit,
rather than treating "pre-register" as one undifferentiated act, is the lesson.

## 3. Verifying and validating the in-silico instrument

Stage 5 runs the tests against a ground-truth instrument. The validation literature names what
makes such a run trustworthy and where it can fail. The foundational move for comparing models is
"docking" or alignment: determining whether two independently developed computational or
agent-based models can produce the same results, a way of verifying and validating models against
one another rather than only against empirical data [Axtell 1996]. Docking offers a graded standard
of equivalence at three weakening levels — numerical identity (exactly the same output),
distributional equivalence (statistically indistinguishable output distributions), and relational
equivalence (the same qualitative ordinal relationships among variables) [Axtell 1996]. For a
protocol that tests Boolean-model results against an instrument, this taxonomy is the right yardstick
for asking how strongly a second model or instrument confirms a result.

Alignment is also a debugging process, not a confirmation ritual. When Axtell, Axelrod, Epstein and
Cohen reimplemented Axelrod's culture model inside the Sugarscape framework, the attempt surfaced
hidden errors, ambiguities, and undocumented assumptions in the original models [Axtell 1996]. The
act of forcing two models into equivalence is what exposes the unstated assumptions. The protocol
gains the same benefit only if stage 5 includes an alignment or replication step, not a single
in-silico run reported as ground truth.

The validation gap is the protocol's sharpest exposure, and the docking literature states its own
limit: equivalence testing between models does not replace external validity assessment against the
target system [Axtell 1996]. Two Boolean models of an organization can be numerically identical and
both wrong about real organizations. Showing that an in-silico result is robust across models, or
matches a ground-truth instrument, establishes internal and cross-model validity. It does not close
the gap to real organizations. The protocol should treat a passed computational test as evidence
about the model, not yet as evidence about the world the model stands for.

## 4. Autonomous and AI-driven discovery: documented failure modes

The protocol is AI-augmented, which the verified source set does not address directly. The
adversarial check did not confirm load-bearing primary claims about autonomous discovery systems
(Sakana's AI Scientist, LLM hypothesis generation, automated ML/science agents), so the strongest
statements this report can make on that branch rest on the general open-science literature above
rather than on system-specific evidence verified in this run. This is a gap, flagged in the
open questions.

What the surrounding literature implies is still usable. Three failure modes are the ones an
AI-augmented pipeline must guard against, and each maps to a defense the protocol already contains
or should add. Fabricated or incorrect citations are caught only if stage 2's deep literature
research verifies each source against the primary document, not against a generated summary.
Plausible-but-wrong reasoning that survives review because it reads fluently is exactly the
postdiction-dressed-as-prediction risk Nosek names, and the defense is the pre-commitment of stage
3 plus the per-hypothesis method of stage 4, which prevent the analysis from being shaped to fit a
fluent narrative after the fact [Nosek 2018]. Confirmation and novelty bias is the Chamberlin
failure mode, and the multiple-hypotheses structure of stage 3 is the classical defense
[Chamberlin 1890/1965]. The protocol's stage 6 — reporting nulls and refutations as first-class
results — is the right counter to novelty bias and to publication bias [Lakens 2024]. The design
is well-aimed at the documented risks. Verifying that an AI executor actually honors the
pre-commitment, rather than reconstructing it post hoc, is the open problem this run could not
close.

## 5. Where the protocol sits

The six-stage protocol is a coherent assembly of established norms. Stages 1–2 are ordinary
literature work, with the AI-specific hazard that generated citations must be checked against
primaries. Stage 3 is Chamberlin's multiple working hypotheses fused with a pre-registration-style
pre-commitment. Stage 4 is the pre-analysis plan, which the economics evidence identifies as the
component that actually buys credibility. Stage 5 is the in-silico test, judged by the docking
standard of equivalence and exposed to the model-to-world validation gap. Stage 6 reports nulls
and refutations as first-class results, the registered-reports answer to publication and novelty
bias.

What it gets right: holding multiple falsifiable hypotheses against confirmation bias; fixing
hypotheses and methods before computing; specifying a method per hypothesis; reporting nulls. What
it must watch: the internal pre-commitment is weaker than a public registry and earns its
credibility through the stage-4 plan, not through pre-commitment alone; five is a useful discipline
but an arbitrary count, and is informative only if the five hypotheses are identifiable under the
instrument; the computational test validates the model and at most a second model, not the real
organization, so the Boolean-model-to-organization gap remains open; and AI fluency can dress a
wrong line of reasoning as a confirmed prediction, which only genuine pre-commitment and
source-level verification defeat.

---

## Sources

Open-access status in brackets. All load-bearing sources are primary peer-reviewed or the
canonical classic.

1. Chamberlin TC (1890). The method of multiple working hypotheses. Reprinted in *Science*
   148(3671):754–759 (1965). doi:10.1126/science.148.3671.754.
   https://www.whoi.edu/cms/files/chamberlin65sci_72744.pdf [OA reprint; primary classic]
2. Yanco SW, McDevitt A, Trueman CN, Hartley L, Wunder MB (2020). A modern method of multiple
   working hypotheses to improve inference in ecology. *Royal Society Open Science* 7(6):200231.
   doi:10.1098/rsos.200231. [OA, PMC7353960]
3. Nosek BA, Ebersole CR, DeHaven AC, Mellor DT (2018). The preregistration revolution. *PNAS*
   115(11):2600–2606. doi:10.1073/pnas.1708274114. [OA, PMC5856500]
4. Hardwicke TE, Wagenmakers EJ (2023). Reducing bias, increasing transparency and calibrating
   confidence with preregistration. *Nature Human Behaviour* 7:15–26.
   doi:10.1038/s41562-022-01497-2. PMID 36707644.
5. Brodeur A, Cook N, Hartley J, Heyes A (2024). Do pre-registration and pre-analysis plans reduce
   p-hacking and publication bias? Evidence from 15,992 test statistics and suggestions for
   improvement. *Journal of Political Economy: Microeconomics* 2(3). doi:10.1086/730455.
   [preprints: IZA DP 15476; SSRN 4180594]
6. Lakens D, Mesquida C, Rasti S, Ditroilo M (2024). The benefits of preregistration and Registered
   Reports. *Evidence-Based Toxicology* 2(1). doi:10.1080/2833373X.2024.2376046.
7. Ledgerwood A (2018). The preregistration revolution needs to distinguish between predictions and
   analyses. *PNAS* 115(45):E10516–E10517. doi:10.1073/pnas.1812592115. [OA, PMC6233109]
8. Axtell R, Axelrod R, Epstein JM, Cohen MD (1996). Aligning simulation models: A case study and
   results. *Computational and Mathematical Organization Theory* 1(2):123–141.
   doi:10.1007/BF01299065. [OA preprint: websites.umich.edu/~axe/research/Aligning_Sim.pdf]

### Supporting / context sources surfaced during verification

9. Gelman A, Loken E (2013). The garden of forking paths. Working paper, Columbia University.
   http://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf [origin of the
   "forking paths" concept; context]
10. Nosek BA, Mellor DT, et al. (2018). Reply to Ledgerwood: Predictions without analysis plans are
    inert. *PNAS* 115(45):E10518. doi:10.1073/pnas.1816418115. [the published rejoinder to source 7]
11. Scheel AM, Schijen MRMJ, Lakens D (2021). An excess of positive results: Comparing the
    standard psychology literature with Registered Reports. *Advances in Methods and Practices in
    Psychological Science* 4(2). doi:10.1177/25152459211007467. [OA; 96% vs 44% positive-result
    evidence on publication bias]
12. Szollosi A, Donkin C (2021). Arrested theory development: The misguided distinction between
    exploratory and confirmatory research. *Perspectives on Psychological Science* 16(4).
    doi:10.1177/1745691620966796. [critique of the confirmatory/exploratory distinction; context]
13. Betini GS, et al. (2017). Why are we not evaluating multiple competing hypotheses in ecology
    and evolution? *Royal Society Open Science* 4:160756. doi:10.1098/rsos.160756. [OA; context for
    source 2]
14. Sargent RG (2013). Verification and validation of simulation models. *Journal of Simulation*
    7:12–24. doi:10.1057/jos.2012.20. [the standard V&V reference; cited for context, not verified
    in this run]

## Open questions carried forward

1. The autonomous-AI-discovery branch is unverified. No primary claim about Sakana's AI Scientist,
   LLM hypothesis generation, or automated ML/science agents survived the adversarial check in this
   run. A dedicated sweep of that literature — including documented fabricated-citation rates and
   review-survival of fluent-but-wrong reasoning — is needed before the protocol's AI-augmentation
   claims can be evaluated against system-specific evidence.
2. Is five hypotheses ever principled? The literature licenses "every tenable hypothesis" and
   identifiability-vetting, not a fixed count. Whether five is a useful default for Boolean-model
   organizational work, or simply arbitrary, is unresolved.
3. How is the model-to-organization validation gap to be closed? Docking establishes cross-model
   equivalence but explicitly does not replace external validity. What empirical anchor would let a
   Boolean-model result speak about real organizations?
4. Does an internal pre-commitment without a public registry capture the credibility benefit? The
   economics evidence says the pre-analysis plan, not the registry act, is operative — but no source
   tested an internal-only pre-commitment, so equivalence to public pre-registration is assumed, not
   shown.

## Caveats on exhaustiveness

Twenty-three verified claims across five intended angles, but the coverage is uneven. The classical
backbone (Chamberlin), the open-science branch (Nosek, Hardwicke, Brodeur, Lakens, Ledgerwood), and
the model-alignment branch (Axtell) are each anchored on primary sources with unanimous or
near-unanimous votes. The autonomous-AI-discovery branch and the broad reproducibility/V&V branch
are thin: Sargent (source 14) is named for completeness but was not verified in this run, and no
AI-system source was confirmed. Several open-science sources returned HTTP 403 on the publisher page
and were verified through indexed abstracts and OA mirrors rather than full text; the verbatim
quotes were confirmed, but full-text reading was not always possible. The pre-registration benefits
are argued design intents and partly contested, not settled empirical facts; the one strong-form
claim that the practices have been shown to achieve their goals was refuted. This set is strong
evidence on the methodology the protocol draws on; it is not an exhaustive census of the
AI-for-science literature the protocol will also be judged against.
