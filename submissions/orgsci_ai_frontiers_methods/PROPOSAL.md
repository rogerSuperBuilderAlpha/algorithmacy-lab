# Computing the Triad: An AI-and-PyPhi Pipeline for Testing Whether Coordinative Infrastructure Is Irreducible

[DRAFTED by Claude, 26 Oct 2026, v3, planned against the CFP PDF only. Stage 1 proposal for *Organization Science*, "AI-Enabled Frontiers in Organizational Science" (due 1 Nov 2026). Every number reproduces from the submission repository with `python reproduce.py`; the repository URL replaces [REPOSITORY URL] once it is created. v1 and v2 are retired; see git history.]

## The structural fact strategy needs and cannot see

Rahman's (2021) freelancers worked under a score that moved without notice, and among the things they could not decipher was who had moved it, the client or the platform. Curchod, Patriotta, Cohen and Neysen (2020) describe eBay's customer reviews as enacting triadic relationships among the platform operator, buyers and sellers, where a dyadic exchange had stood. Stark and Pais (2020) give the platform a triangular geometry in which the owner co-opts providers and users alike, and Cameron (2024) draws an algorithmic labor triangle. Organizations increasingly coordinate through such infrastructure: a dispatch system between driver and rider, an engine between claimant and adjuster, an AI agent between two firms. The literature calls these arrangements triadic by description. Nobody computes it.

The surface does not settle it. In the complete family of 256 three-party structures in which the outer parties have no direct link and must coordinate through a mediator, 24 are irreducibly triadic. The intuitive test, that the mediator reads both parties, is necessary but nowhere near sufficient: it holds for 160 structures, of which 24 are triadic, and fails for 96, of which none is. Most arrangements with a platform in the middle still factor into pairs.

Irreducibility is a strategic fact. It says who is bound to whom, who can leave, and what a redesign would change. We have built a method that computes it exactly for any small coordinative structure written as a model of who reads whom and what each party commits. We have not yet built the model of what to do about it. This proposal describes the method, shows it working, and lays out how we will build the strategic model on top of it.

## The pipeline: what AI does, what PyPhi computes, what the researcher decides

1. **Bound and name.** The researcher fixes one recurring act (one match, one claim, one merge), names the parties as nodes, and states what each party's active bit means and what that binary collapses. *Built, as a written field protocol with a coding scheme, interview guide and ethics note.*
2. **Encode.** A language model drafts rival Boolean encodings of the arrangement, one per defensible reading. Each party's next state is an expression over the parties it reads, such as `P' = D and R`, and every rule must quote the passage it rests on. For the mediator, the model must also say whether the evidence shows it *committing* on a joint condition, *conveying* one party's signal, or *storing* inputs for someone else. A second, adversarial prompt then searches for the most different readings the evidence still permits: commit versus convey, interchangeable parties, and outside options. Every encoding carries a predicted verdict fixed before anything is computed. A checker rejects any rule whose quotation does not appear verbatim in the source. *Built as prompts, a schema and the checker, and run on two cases; ingestion of interview transcripts at scale is planned.*
3. **Compute.** For each encoding the rules become a state-by-node transition matrix and a connectivity matrix. PyPhi's implementation of integrated information theory 4.0 (Albantakis et al., 2023; Mayner et al., 2018) evaluates every reachable state and returns system integrated information Φ over the minimum-information partition (the cut that damages the cause–effect structure least), together with the major complex, the subset of parties that forms the irreducible core. If Φ is zero in every state, some cut along party lines leaves the structure intact and the arrangement is *dyadic*. If Φ is positive in any state, no cut does, and it is *triadic*. *Built.*
4. **Validate first.** Before reading any verdict, the instrument must reproduce its controls: a structure with a decoupled party reads dyadic, and a fully coupled one reads triadic. If either fails, every script refuses to run. *Built.*
5. **Report the spread.** The pipeline computes every approved encoding, reports the Φ gap and core overlap between rival readings, and names the single rule whose change flips the verdict. A verdict that holds across every defensible encoding is robust. One that does not is contested, and the flipping rule is the fact fieldwork must settle. *Built.*
6. **Read the structure.** Three readings follow from the verdict. *Who is bound* is the major complex. *The mediator's position* comes from a lesion test: a bottleneck carries the coordination; an enricher adds to a coordination that survives its removal; capture binds the mediator to some parties and leaves others out; a bypassed mediator sits outside a core the parties form themselves. *Intrinsic or contingent* comes from restoring a forbidden direct tie: an intermediary that does integrative work stays in the core, while one held there only by a constraint on bypassing it drops out. *Built.*

The division of labour is the design. The model proposes readings at a breadth no single coder sustains; PyPhi decides each exactly; the researcher bounds the act, approves encodings, fixes predictions and interprets the result for strategy.

## A walk-through: gig dispatch

The repository's first worked example applies the pipeline to a stipulated description of one dispatch event. The platform's manual says the system "assigns a trip only when an eligible driver is available and a rider has confirmed the request." A driver says "It's a suggestion, it follows what I do." The manual adds that "any eligible driver in range may be assigned," and some riders text their regular driver when the app is slow.

The platform's account encodes as `D' = P, P' = D and R, R' = P`. PyPhi returns Φ = 2.0 at the state where all three are active, with all three parties in the core and the platform a bottleneck. Restoring a direct driver–rider tie leaves the platform in the core, so its place is intrinsic. The driver's account changes one rule, `P' = D`, and the structure factors (Φ = 0). The pipeline reports that this single rule carries the whole disagreement, so the question a study must answer is whether dispatch commits or relays. Pooling drivers, `P' = (D1 or D2) and R`, also factors the structure and removes the individual driver from the core, leaving platform and rider bound.

Holding the platform's rule fixed and varying outside options gives the strategic reading. With both sides captive, the platform is a bottleneck. With a complementary direct tie, it is an enricher. With a captive driver and a mobile rider, it captures the driver; give the driver the option instead and the lock-in moves to the rider. Only symmetric options leave the platform outside the core. For a platform, a drivers' collective or a regulator, these are the structural consequences of each lever. Which lever to pull in which circumstance is the strategic model we will build.

The AI step ran on this case. Given the description alone, the drafter reproduced the two rival readings a human coder wrote, with every quotation verbatim. The adversary then found the driver pool and the substitute direct tie, and declined a complementary tie that the text does not support. Both of its predictions failed when computed. It expected the pooled structure to stay triadic, but it factors. It expected the direct-tie structure to factor, but it stays irreducible with the platform bypassed. The model found the readings, and PyPhi decided them. On a second case, insurance-claim routing, the drafter declined to write rules for four of five designs because the description did not specify them, and the checker rejected the file. The gate worked as intended.

## What we have done

The repository ([REPOSITORY URL]) holds the pipeline as installable code, four worked examples (gig dispatch, insurance-claim routing, a code-review gate, and a dealer contrasted with a clearinghouse), the logged AI runs, the field protocol, 19 tests, and one command that reproduces all 17 reported results in about two minutes on a laptop.

The reference results show why the verdict must be computed rather than read off a diagram, and why its encoding must be searched rather than chosen. Beyond the 256-structure census:
- Two standard time-series proxies for integration separate dyadic from triadic structures at rank-AUC 0.563 and 0.629, barely above chance.
- In ten invented organizations, the computed verdict matched the reading fixed before computing in nine. Four flipped under a second encoding the same story permits.
- An adversary limited to readings the evidence permits flipped the point verdict on all 101 contested accounts it attacked.

Encoding sensitivity is the method's central fact, and the pipeline reports it instead of hiding it. The outside-option law behind the walk-through holds on 60 of 60 random configurations. One outside contributor, working on their own machine with an AI assistant, took a new question (who decides an insurance claim?) through the laboratory's protocol to a reproducible result.

## What we hope to do

Stage 2 (January–May 2027) would build three things.

- **The encoding module, before the February workshop.** It will ingest interview transcripts, documents and logs; attach a locator to every rule; run the drafter and the adversary on open-weight as well as commercial models; and put a researcher's approval between drafting and computing. We will measure agreement between the AI drafter and two human coders against the coding scheme's bar (Krippendorff's α of 0.80), so workshop participants can run their own cases.
- **The strategic model (February–April).** An actor-indexed table maps a structural position (verdict, core, mediator regime, intrinsic or contingent) and a design lever (add or remove a binding, break or restore liveness, require all parties or allow substitutes, open or close a bypass, change an outside option) to its consequence: who stays bound, who is freed, whether the mediator survives. Every cell is a computation the pipeline can already run. The model is structural and makes no claims about economic value.
- **Validation on real cases (March–May).** We will encode 10 to 15 published platform and algorithmic-management cases from their own text and report, for each, the verdict under every defensible encoding and the detail that would decide between them. The interview packet for gig dispatch is complete and will be fielded once ethics approval is in hand.

The Stage 3 article would report the pipeline, the walk-through, the table of published cases, the lever table and the agreement between AI and human coders. If development stops short, a letter reporting encoding sensitivity alone would still serve anyone who computes structure from text.

## Key risks

- **Encoding sensitivity.** This is the main risk. A verdict is exact for its encoding, not for the organization. The design response is to search the space of encodings, require human sign-off, and count a case as robust only when every defensible encoding agrees.
- **The validation gap.** A verdict on a model says nothing yet about how workers experience an arrangement; that needs fieldwork.
- **Scale.** Exact Φ is practical to about ten binary parties. Most coordination units have three to five.
- **The model.** The drafter currently runs on a commercial model, and an open-weight configuration is planned. The strategic model does not yet exist.
- **Ethics.** Verdicts concern arrangements, not persons. Field cases proceed only under approval. The same analysis that shows a platform how capture works shows workers and regulators which move dissolves it.

## How organizational science would change

Structural claims about triadic infrastructure would become computed, comparable and contestable. A study would publish its encodings, and a reader could rerun the verdict under a rival reading. Typologies built on description could be tested against one standard: Thompson's (1967) ordering of pooled, sequential and reciprocal interdependence collapses at its top step when computed. Strategy would gain a vocabulary of levers with exact structural consequences. Daft and Lewin (1990) asked organization studies to break out of the normal-science straitjacket. Borrowing an exact measure of irreducibility from another field, with AI doing the reading that makes it usable, is one way out, and the repository is where anyone can start.

## References

Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures consent through constant and confined choices. *Administrative Science Quarterly*, 69(2), 458–514.

Curchod, C., Patriotta, G., Cohen, L., & Neysen, N. (2020). Working for an algorithm: Power asymmetries and agency in online work settings. *Administrative Science Quarterly*, 65(3), 644–676. https://doi.org/10.1177/0001839219867024

Daft, R. L., & Lewin, A. Y. (1990). Can organization studies begin to break out of the normal science straitjacket? An editorial essay. *Organization Science*, 1(1), 1–9.

Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

Rahman, H. A. (2021). The invisible cage: Workers' reactivity to opaque algorithmic evaluations. *Administrative Science Quarterly*, 66(4), 945–988. https://doi.org/10.1177/00018392211010118

Stark, D., & Pais, I. (2020). Algorithmic management in the platform economy. *Sociologica*, 14(3), 47–72. https://doi.org/10.6092/issn.1971-8853/12221

Thompson, J. D. (1967). *Organizations in action: Social science bases of administrative theory*. McGraw-Hill.
