# An Exact Test for Triadic Coordination: Integrated Information as Shared Infrastructure for Organization Science

[DRAFTED by Claude, 26 Oct 2026, for the author's read-aloud. Research proposal for *Organization Science*, AI-Enabled Frontiers (Stage 1, due 1 Nov 2026). Anonymous: no author names, no repository owner, no lab name. Every number here was re-run on 26 Oct 2026 or is tied to a regression check; see TECHNICAL_APPENDIX.md.]

## The problem: triads asserted, never tested

Organization scientists now describe much platform work as triadic. Curchod, Patriotta, Cohen and Neysen (2020) found that on eBay, customer reviews set the platform operator, buyers and sellers in a triadic relationship where a dyadic exchange had once stood. Stark and Pais (2020) gave the platform a triangular geometry in which the owner co-opts providers and users at once, without delegating authority to either. Cameron (2024) drew an algorithmic labor triangle of worker, customer and algorithm. Each study settles the structure by description. None supplies a test that tells a reader when a three-party arrangement is irreducibly three-party and when it factors into two-party relations that happen to share a platform.

The distinction carries theoretical weight. If the triad factors, existing dyadic accounts of control, exchange and competence apply pair by pair, and the third party is a channel. If it does not factor, those accounts miss the thing that binds the parties together, and the competence a worker needs changes with it. Thompson (1967) met an older version of the same problem when he ranked pooled, sequential and reciprocal interdependence by their coordination burden. His ranking also rests on description.

We propose a shared instrument that settles the structural question exactly for any arrangement written down as a formal model, and an AI-enabled research loop that runs the instrument under human direction. The instrument already exists and has been validated on its own controls. Under it, 170 research questions have been taken to fixed hypotheses and run, and 168 have reached a written paper. The development stage would turn both into infrastructure that other organization scientists can use on their own cases.

## What we have done

**The instrument.** A coordination form becomes a small Boolean network: one node per party, and for each node a rule that sets its next state from the current states of the others. A worker who acts when the platform signals, a platform that commits a match only when both worker and customer are available, and a customer who rates on what the platform shows are three such rules. On that network we compute integrated information under integrated information theory 4.0 (Albantakis et al., 2023), using PyPhi (Mayner et al., 2018). The computation searches every way of cutting the network into parts and finds the minimum-information partition, the cut that damages the network's cause–effect structure least. Integrated information over that partition (Φ_MIP) is the verdict. Φ_MIP = 0 means some cut along party lines leaves the structure intact, so the form is *dyadic*. Φ_MIP > 0 means no such cut exists, so the form is *triadic*. We read only this binary verdict. Φ's magnitude depends on how a form is encoded and does not work as a scale.

Every run begins by reproducing known controls. A strict-mediation triad, in which the platform reads both parties and each party reads the platform, must read triadic at Φ = 2.0. A form in which the counterpart is decoupled from the other two must read dyadic. If a control fails, the run stops.

**Three results that make the case for an exact test.** The first is a census. Strict mediation means the two outer parties have no direct link and must coordinate through the third. Of the 256 forms in the complete three-party strict-mediation family, 24 (9.4%) are triadic. Most arrangements with a platform in the middle still factor.

The second result shows that intuition misleads. A natural rule says a form is triadic when the mediator reads both parties. The census shows the rule is necessary: none of the 96 forms that fail it is triadic. It is far from sufficient: 24 of the 160 forms that meet it (15.0%) are triadic. The rest factor, because the parties' own rules break the loop that would bind them.

The third result closes an apparent shortcut. Exact Φ is costly beyond a handful of nodes, so a researcher might estimate integration from interaction time series instead. We simulated eight coordination forms under noise and computed two standard time-series proxies, ΦID's Φ_R and whole-minus-sum Φ. Neither recovers the verdict: their rank-AUCs against the exact classification are 0.563 and 0.629, where 0.5 is chance. The failure has a concrete cause. A dyadic hierarchy with a direct worker–counterpart back-channel produces strong statistical dependence, and the proxy scores it (Φ_R = 0.205) above two of the three triadic forms (0.106 each). The proxies measure dependence, and dependence is not integration. Coordination units are small, so the exact computation remains feasible where it is needed.

**The research loop.** The instrument sits inside a six-stage protocol that AI agents can execute end to end and a researcher directs. For each question, agents (1) place it against the lab's logbook of prior results, (2) run a literature search that must return sourced references and state whether the gap is open, (3) write five hypotheses with their nulls, (4) write a method for each hypothesis with a decision rule, (5) write and run the probes against the instrument, beginning with the controls, and (6) assemble a paper that reports refuted hypotheses as refuted. Stages 3 and 4 are committed before any computation runs, which gives each question a pre-analysis plan in the sense Brodeur, Cook, Hartley and Heyes (2024) found effective against p-hacking. The researcher chooses the question, reads each stage's output and accepts or rejects the result. A regression suite of 542 commands re-runs the code behind every reported number and fails if the printed output changes.

One worked question shows what the loop produces. We asked whether the verdict reproduces Thompson's ordering when each interdependence type is built as a three-node form under one convention. It does not. Pooled interdependence reads dyadic (Φ = 0), while sequential and reciprocal both read triadic (Φ = 2.0), so the top step of the ordering collapses. Pooled and sequential each split by construction: pooled turns triadic when one node is jointly determined by all contributors, and sequential turns triadic when a return edge closes the chain. The loop also refuted its own proposed replacement, a two-primitive rule based on joint determination and feedback. Four forms share the same pair of primitives, three of them with identical wiring, and they still split across both verdicts.

## What we will do

The development stage would turn a working lab instrument into infrastructure in three steps.

**A released classifier with a model-writing guide.** The classifier already accepts a form as a JSON file of per-party rules and returns the verdict, the core of parties bound into the irreducible structure, and the controls it passed. We will package it for installation, write a guide that walks a researcher from an arrangement described in prose to rules, and publish a library of labelled reference forms (hierarchy, relay, marketplace, ranking, arbitration) that a new model can be compared against.

**A case-to-model module.** Writing the model is where judgement enters, and published studies describe arrangements in prose. We will build a module in which a language model reads a case description and drafts several candidate encodings, each with the textual evidence for every rule. A researcher approves, edits or rejects each encoding before it reaches the classifier. The module reports the verdict for every approved encoding, never only the preferred one. A ten-case field demonstration with invented organizations already shows why: four of the ten arrangements change verdict under a second encoding that the same story permits. A ride-hail dispatch, for example, reads triadic when one driver is matched to one rider and dyadic when drivers form an interchangeable pool.

**A first application to the platform literature.** We will run the module and classifier on 10 to 20 published platform and algorithmic-management cases, starting with those that call themselves triadic. For each case we will report the candidate encodings, the verdict under each, and the textual detail that would decide between them. The output is a structured answer to a question the literature has left open: which of its triads are irreducible under every defensible encoding, which depend on an encoding choice the original study did not make, and which factor.

## Key risks

**Encoding sensitivity.** The verdict belongs to the model first and to the organization only through the model. Two researchers can encode the same case differently and reach different verdicts. We treat this as the central risk and design for it: the module produces several encodings, the classifier reports a verdict for each, and a case counts as triadic only if every defensible encoding agrees.

**The validation gap.** A verdict on a Boolean model is evidence about that model. It is not yet evidence that real workers experience the arrangement as irreducible. Closing this gap requires fieldwork that pairs a verdict with observation, and the development stage will not close it. A field protocol for that step exists in draft and has run only on invented cases. We will state this limit in every output.

**Model drafting.** A language model may misread a case or invent a rule the text does not support. Every rule in a candidate encoding must cite its supporting passage, and no encoding reaches the classifier without a researcher's approval.

**Computational cost.** Exact Φ grows steeply with network size. The full census of 256 three-party forms runs in about a second on a laptop; beyond about ten nodes the exact computation becomes impractical. Most coordination units are small, and for larger panels a researcher can screen with a cheap classifier and compute exactly only where the screen is uncertain.

## How organization science would change

Structural claims about coordination would become exact, comparable and open to challenge. A study that calls an arrangement triadic could publish its model, and a reader could rerun the verdict, change one rule and see whether the claim survives. Typologies built on description, Thompson's among them, could be tested against a common standard. Theory could then ask a sharper question than whether platforms are triadic: under what structural conditions an arrangement binds its parties irreducibly, and therefore when a worker's competence must extend beyond reading one counterpart to reading the arrangement as a whole. The research loop makes that program cumulative. Every question leaves behind its hypotheses, methods, code, refutations and a regression check, so the next researcher starts from a verified record.

## References

Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Brodeur, A., Cook, N., Hartley, J., & Heyes, A. (2024). Do pre-registration and pre-analysis plans reduce p-hacking and publication bias? Evidence from 15,992 test statistics and suggestions for improvement. *Journal of Political Economy Microeconomics*, 2(3). https://doi.org/10.1086/730455

Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures consent through constant and confined choices. *Administrative Science Quarterly*, 69(2), 458–514.

Curchod, C., Patriotta, G., Cohen, L., & Neysen, N. (2020). Working for an algorithm: Power asymmetries and agency in online work settings. *Administrative Science Quarterly*, 65(3), 644–676. https://doi.org/10.1177/0001839219867024

Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

Stark, D., & Pais, I. (2020). Algorithmic management in the platform economy. *Sociologica*, 14(3), 47–72. https://doi.org/10.6092/issn.1971-8853/12221

Thompson, J. D. (1967). *Organizations in action: Social science bases of administrative theory*. McGraw-Hill.
