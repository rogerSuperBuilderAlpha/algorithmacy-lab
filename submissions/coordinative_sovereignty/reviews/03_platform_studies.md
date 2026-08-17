# Peer Review — Platform Studies / Algorithmic Management lens

**Reviewer standpoint:** platform studies and algorithmic management (Stark & Pais; Stark & Vanden Broeck on co-optation; Rosenblat & Stark; Kellogg, Valentine & Christin; Möhlmann on algorithm sensemaking; Cutolo & Kenney on platform dependence; Rahman's invisible cage; Zuboff).
**Target:** `chapter/chapter.md`, "Algorithmacy and Sovereignty," §1–§10, full body plus apparatus.

---

## Step 0 — Register

Impersonal academic chapter, APA 7, double-anonymized; judged against the house invariants (named agents + active voice, claim-first, concrete anchors, verified cites, varied rhythm), not against the impersonal register, which is correct here and not flagged. On the repo's own slop metrics the draft is close to clean: the antithesis machine barely fires (one `, not`, one `rather than`, no `is not a/the/an`, three benign `it does not` clauses across ~9,000 words), so this review spends its slop budget on the two failures that *are* present — verbatim over-repetition of one point and light anthropomorphic drift — and its main energy on substance.

---

## Part 1 — Theory and structure, §1–§10

### §1 Introduction

The compliance-vs-capture hook is the right one and it lands: the ISV, the merchant, the creator are exactly the platform-dependent figures the field studies, and Cutolo & Kenney (2021), Rahman (2021), and Rahman et al. (2024) are the right anchors. Two things a platform-studies referee flags at the outset.

First, the opening triad of vignettes ("An independent software vendor… A merchant… A creator…") is asserted, not sourced. These are the empirical bread-and-butter of the field and there are canonical cites for each — app-store dependence (Cutolo & Kenney, 2021, is used later), marketplace-ranking shocks, creator demonetization. Anchoring at least one vignette to a documented case at first mention would stop a referee reading the hook as stylized. The chapter has the cites; it withholds them until §3.

Second, "sovereignty has never stood alone… paired with a communicative sensibility" is the load-bearing move of the whole chapter and it is introduced as assertion. That is acceptable in an introduction that §2 then earns, and §2 does earn it, so this is a signpost note, not an objection.

### §2 Sovereignty and its sensibilities

Strong, and largely outside my lane (media theory, orality-literacy, Habermas/Anderson/Innis/Eisenstein). Two lane-relevant observations. The nesting argument in §2.3 — each sensibility layers on the prior, and "the literate response is to demand more disclosure… because reading is what the literate know how to do" — is the sharpest diagnostic sentence in the chapter and it is precisely the mechanism a platform-studies audience will accept: it names *why* transparency regulation keeps missing. Keep it. The claim that digital sovereignty "is the literate sensibility carried into the digital domain" is a strong reading that some digital-sovereignty scholars would contest (they would say control of infrastructure is not reducible to reading), but the chapter only needs the weaker claim that its *instruments* are technologies of reading and writing, which is defensible. No change required; just be aware the strong framing is doing rhetorical work the argument does not strictly need.

### §3 The platform turn — the central section (weighted)

This is where a platform-studies referee spends most of the review. The architecture — separate the coordination *logic* (old), the *topology* of the triad (old, Simmel/Burt/Obstfeld), and the novel *conjunction* of opacity + interest + adaptivity — is genuinely good analytic hygiene and it preempts the obvious "algorithmic management is just hierarchy in new clothes" objection (Kellogg et al., 2020; Rahman, 2021) by conceding it and relocating the novelty. That triage is the section's best move and it is faithful to how the field argues.

But four problems, in descending severity.

**(1) The co-optation reading is attributed to the wrong paper and pushed harder than its source will bear.** The chapter builds its "fourth term" on Stark and Vanden Broeck (2024). The co-opt-as-fourth-coordination-mechanism scheme — hierarchies command, markets contract/compete, networks collaborate, platforms co-opt — originates in **Stark and Pais (2020), "Algorithmic Management in the Platform Economy," *Sociologica*** [VERIFY exact vol/issue/pages], which the chapter does not cite at all. Stark & Vanden Broeck (2024) is the follow-on. A Stark-attuned referee will treat the missing origin cite as a priority-of-credit error, and it is an easy fix: cite Stark & Pais (2020) as the source of the typology and Stark & Vanden Broeck (2024) as its development.

The deeper issue is *faithfulness of reading*. Stark's co-optation is an economic-sociology-of-valuation claim: platforms harness participants' own lateral activity and data, and "co-opt" is used in a relatively neutral, generative register — the platform enrolls and *recombines* user activity, not primarily a domination claim. The chapter grafts onto it a strong extractive-domination reading — "enrolled into a coordination authored by an interested third party," "a determination," "the platform extracts the surplus" — and reinforces it with Zuboff (2019) and Cutolo & Kenney (2021). That fusion is defensible as *the chapter's own* synthesis, but as written it reads as though Stark asserts the domination claim, and Stark does not. Two sentences distinguishing what Stark & Pais describe (co-optation as a coordination principle) from what the chapter adds (the political economy of interested mediation) would make the reading honest and, paradoxically, stronger — it would let the chapter own its critical move instead of laundering it through a cite whose author is more ambivalent. This is the single most important §3 revision for a platform-studies referee.

**(2) The "interested, adaptive mediator" drifts into anthropomorphizing the algorithm — the field's cardinal sin.** The chapter is *usually* careful ("set by a firm that neither of them works for"), but the drift is real and repeated: "it pursues objectives of its own and revises its rules continuously in their pursuit" (§3); "The system stands between them and pursues objectives of its own"; "It optimizes for ends of its own" (§3.1). Kellogg et al. (2020) and Christin's body of work exist precisely to deny that the algorithm is a stable, interested actor: it is a contested terrain, continuously reconfigured by product managers, A/B tests, content-policy teams, and worker gaming. The interest belongs to the *firm*; the adaptivity is *human-driven reconfiguration*, not the system's autonomous pursuit of ends. As written, a referee reads the chapter as reifying "the algorithm" into an agent — the exact move Möhlmann, Kellogg, and Christin caution against — and will not trust the rest. The fix is cheap and does not weaken the argument: consistently locate the interest in the operator and treat opacity/adaptivity as properties the operator *maintains*. The chapter even has the better formulation available in §4 ("Opacity is a rent-preserving strategy"), which correctly makes opacity an operator's choice. Bring that agentive discipline forward into §3.

**(3) "Adaptive" is asserted without an anchor.** "revises its rules continuously" is the load-bearing novelty claim and it has no citation. The field has the anchor — continuous experimentation / A/B testing / the decoupling of algorithm-as-designed from algorithm-as-deployed (Christin, 2020 [VERIFY]; and the algorithm-sensemaking premise in Möhlmann et al., 2023, that formal disclosure never catches up to the deployed system). Anchor "adaptive" or a referee reads the third of the three novel features as unsupported.

**(4) Kellogg et al. is under-used — the chapter cites its own best ally and flattens it.** Kellogg, Valentine & Christin (2020) is "the new *contested terrain* of control": their argument is that algorithmic control is *met by* worker resistance and gaming, and that terrain is contested. The chapter cites the paper only for the "hierarchy in new clothes" objection it then sets aside. But the resistance/gaming half of Kellogg *is* algorithmacy in the field — workers building theories and shaping conduct to a system they cannot see is the translational competence §4 defines. The chapter leaves its strongest empirical support on the table. Pull the contested-terrain framing into §3 or §4 and the algorithmacy construct gains a documented base instead of standing on a coinage.

Two smaller §3 notes. The Simmel/Burt/Obstfeld triad citation is apt and shows the referee the author knows the topology is old; good. And Rosenblat & Stark (2016), the canonical study of Uber drivers' information asymmetries, is absent — a conspicuous gap given that the driver/rider triad is the chapter's opening illustration in §3.1 and its ride-hail example in §5.2 (see below).

### §3.2 Why literacy cannot reach it

The four-part structure (Burrell opacity → Ananny & Crawford no-channel → Cutolo & Kenney / Rahman no-leverage → Hildebrandt text-vs-code law) is well built and each cite is deployed accurately. Burrell's third opacity (scale/mathematics, surviving source release) is stated correctly. Ananny & Crawford's "transparency without an institution to act" is stated correctly. Rahman's invisible cage — reactivity to an unseen, shifting target, where the reaction is itself control — is stated correctly and is one of the most faithful redeployments in the chapter. Wood et al. (2019) on the flexibility-inside-control point is exactly right.

One caution: the four parts are presented as four *independent* structural facts, but parts 2 and 3 (no channel; no leverage) are closely coupled — Ananny & Crawford's missing institution and Rahman et al.'s unreachable accountability layer are nearly the same claim viewed from governance and from the worker. A referee will not object, but tightening the seam (or explicitly noting they are two faces of one gap) would prevent the section reading as padded to reach the rhetorically satisfying "four."

### §3.3 The political economy of interested mediation (weighted)

This is the paragraph a two-sided-markets referee will circle, and it has one real error and one imprecision.

**The error:** "that structural position… is **a source of rent independent of any service the mediator provides**." This contradicts the very literature the sentence cites. In Rochet & Tirole (2003) the platform's take is disciplined by both sides' participation constraints and reflects genuine cross-group-externality internalization — a real coordination service. In Armstrong & Wright (2007) the "competitive bottleneck" rent is extracted over access to the *single-homing* side by the *multihoming* side, and it is a *competitive* outcome, not a costless topological tax. "Independent of any service" is precisely what these models deny: the rent is the price of an access/matching service, bounded by the outside options of both sides. As written, the chapter cites Rochet–Tirole and Armstrong–Wright to support a claim they refute. The fix is to say what the chapter actually means: the bottleneck confers *pricing power over access* that persists even when the mediator's marginal service is small, because both sides must route through it — power, not costless rent. Distinguish **bottleneck power** (the topological fact) from **bottleneck rent** (the economic surplus, which is disciplined by homing patterns and outside options). That distinction is also what the §5 diagnostic needs, since multihoming (invoked in §5.3 via Eisenmann et al., 2006) is exactly the mechanism that turns bottleneck power into contestable-or-not rent.

**The imprecision:** "which the economics of two-sided markets (Rochet & Tirole, 2003) calls a competitive bottleneck (Armstrong & Wright, 2007)." The term "competitive bottleneck" is Armstrong's / Armstrong & Wright's, not Rochet & Tirole's. Rochet & Tirole give the two-sided-market framework; the bottleneck coinage is the second cite. Re-sequence so the term is attributed to its author: "the two-sided-market literature (Rochet & Tirole, 2003; Armstrong & Wright, 2007) identifies a *competitive bottleneck* — where one side single-homes, the platform holds monopoly power over access to it." That version is both correct and *stronger*, because the single-homing condition is exactly the platform-dependence Cutolo & Kenney document (the seller who cannot multihome because no alternative exists at scale).

The rest of §3.3 is good. "essential to a platform's value and powerless within it at the same time" is a clean statement of the Cutolo & Kenney thesis. "Opacity as rent-preserving strategy" (developed in §4) is the correct political-economy reading and it belongs partly here. And the closing "A transparent bottleneck is still a bottleneck" is a genuinely good line — see the style audit for the one place it is doubled.

### §4 Algorithmacy

The construct is the chapter's original contribution and it is positioned honestly against the adjacent literatures — algorithmic literacy (Dogruel et al., 2022), critical data literacy (Pangrazio & Selwyn, 2019; Sander, 2020), folk theories (DeVito, 2021; Eslami et al., 2016), algorithm sensemaking (Möhlmann et al., 2023), anticipatory compliance (Bucher et al., 2021). Three problems, the first substantive.

**(1) The "spectatorship vs working-from-within" line is overdrawn against the strongest neighbors, and it makes the novelty claim look larger than it is.** "These competences mostly describe spectatorship: recognizing that a system is at work, interpreting its outputs, reflecting on its effects." That is fair to Dogruel and to the critical-data-literacy strand. It is *not* fair to Möhlmann et al. (2023), Bucher et al. (2021), or DeVito (2021), which are the three named just before and after it. Algorithm sensemaking is workers *acting on and revising* theories of the system that manages them; anticipatory compliance is workers *shaping conduct in advance* to an unseen algorithm; adaptive folk theorization is *iterative revision as the platform changes*. All three are working-from-within, and all three already contain the "temporal" dimension the chapter claims as its distinctive third part. The chapter concedes as much two sentences later ("Algorithm sensemaking is the inferential part of algorithmacy under another name… the translational part has a field record too"), which contradicts the "spectatorship" framing it just used. A referee reads this as the construct overclaiming its distance from prior work and then quietly walking it back.

The honest and defensible novelty claim is narrower and the chapter should make *it*: algorithmacy's contribution is (a) the *integration* of inferential + translational + temporal into one named competence and (b) the *embedding of that competence inside the irreducible triad* with a formal necessary/contingent test attached — not the discovery of any one part, all of which are documented. Reframing §4 around integration-plus-embedding rather than "these others only spectate" would survive a referee; the current framing invites the objection that algorithmacy relabels Möhlmann + Bucher + DeVito.

**(2) The "temporal" part is the least novel and is presented as the most.** Möhlmann's sensemaking is *iterative and continuous by definition*; DeVito's folk theorization is explicitly about *changing platforms*. "Holding a strategy through undisclosed change" is real but it is already in the cited work. Either source the temporal part to those authors (which strengthens it) or find the genuinely new element in it — plausibly that the temporal challenge compounds when the *counterpart* is also adapting, i.e., the triad, not the dyad.

**(3) The worked examples (the marketplace seller; the halved-orders morning) are excellent and are the chapter's most concrete pages.** No change — these are exactly the kind of anchors the house style demands, and the delivery-speed re-weighting story is a faithful miniature of algorithm sensemaking. If anything, move one of them earlier (into §3.1) so the abstract triad arrives already illustrated.

The §4 political-economy turn — "the actors best placed to model the system are the large ones already advantaged within it… a competence distributed like capital distributes standing like capital" — is a genuinely good and non-obvious point, and it is the chapter's own. Keep it prominent; it is more original than the "spectatorship" contrast it sits near.

### §5 The necessary/contingent diagnostic

The bypass counterfactual (restore the direct tie, recompute whether the mediator still binds) is a clean device and the four-way sort (necessary / contingent / partial / reducible) is genuinely useful for managers. The Hahl et al. (2016) brokerage anchor is apt. Two platform-studies concerns.

**(1) The binary risks over-crispness, and the ride-hail example exposes it.** "A ride-hail platform… matches riders and drivers in real time, which is integrating work, and stands between a rider and driver who could re-contact each other directly, which is a bypassable relationship gate." A referee who knows Rosenblat & Stark (2016) will object that this *asserts* the classification the section is supposed to *derive*. Whether real-time matching at scale is genuinely necessary integrating work, or whether it is a contingent gate held in place by the platform's deliberate suppression of driver–rider contact information, surge opacity, and anti-steering design, is *exactly the contested question* — and Rosenblat & Stark document that Uber actively engineers the non-bypassability the chapter treats as natural. The chapter should either (a) show its work on one hard algorithmic case rather than asserting the verdict, or (b) concede that the necessary/contingent status of platform matching is itself often *manufactured* — that platforms invest in making contingent gates look necessary — which is a *deepening* of the argument, not a concession. This connects straight to §4's "opacity as rent-preserving strategy": the same firm that keeps its rules opaque also engineers the gate's apparent necessity. Right now §5 treats necessity as a fact of nature; the platform-studies reading is that necessity is partly a *design achievement the powerful defend*.

**(2) The examples are almost all old-economy (car dealer, clearinghouse, interpreter, hotel/OTA).** The OTA/rate-parity case (§5.4) is the best worked example in the chapter and does show the test under real bypass pressure — keep it. But for a platform-studies audience the diagnostic needs to bite on a *genuinely algorithmic* mediation where the answer is hard and human-contested, not on a franchised dealer where a statute is the whole story. The app-store example (§5.4) is closer and good; lean on it and the ride-hail case, and do the ride-hail classification *carefully* per point (1).

### §5.3 Exit and voice

The Hirschman mapping (exit ↔ contingent/bypassable, voice ↔ necessary) is elegant and the multihoming bridge (Eisenmann et al., 2006) is the right economics. Dasgupta et al. (2025) and Smith & Burrows (2021) are well chosen. One missing Hirschman nuance a referee will want: Hirschman's own central dynamic is that **exit can undermine voice** — the most quality-sensitive members leave first, draining the collective capacity to press for change. In the platform "portfolio of mediators" (§5.4), an actor who exits the contingent functions (multihomes, book-direct) may thereby *reduce* the collective leverage available for voice on the necessary ones — the hotel that recovers margin on book-direct guests has less incentive to join a collective push on the aggregation function. The chapter's clean exit/voice partition (exit here, voice there) misses this coupling. Engaging it would make the portfolio argument more sophisticated and would head off the most obvious Hirschman objection.

### §6 Coordinative sovereignty — the definition

The four-theory convergence (Pettit/Skinner non-domination; Mackenzie & Stoljar / Nedelsky relational autonomy; Markell's insufficiency-of-non-domination; Ostrom's commons) is the strongest constructive section and it is outside my core lane. Lane-relevant notes. Muldoon & Raekstad (2022) on algorithmic domination is exactly the right republican anchor and is used faithfully — and the chapter correctly notes it "often recommends exit through cooperative ownership," distinguishing its own voice-within stance. The differentiation from neighbors (Bannerman's relational sovereignty; Pasquale's functional sovereignty; Cohen's platform sovereign) is careful and fair: "Coordinative sovereignty looks at the same relationship from the other end" is a legitimate and precise gap-claim. The three clarifications (more than worker rights; transparency does not produce it; not anti-platform) preempt the three misreadings a referee would actually raise. Good.

One substantive push. The Ananny & Crawford "legibility without standing" point appears *again* here (§6, third clarification), having already carried §3.2 and §3.3 and about to carry §7 and §8. See the style audit — this is the chapter's one genuinely over-repeated argument, and §6 is where to state it definitively and then refer back.

### §7 Realizing coordinative sovereignty

The institutional survey (platform cooperativism / Scholz; data trusts / Delacroix & Lawrence, Micheli et al.; collective bargaining / works councils; contestability / Alfrink et al.; interop-and-portability as *exit* moves; oversight boards / Klonick; DSA researcher access + platform-work directive) is well organized by the diagnostic, and sorting instruments into exit-restoring (contingent functions) vs voice-building (necessary functions) is the section's payoff and it works. Lei (2021) on platform architecture shaping where contention can organize is a sharp inclusion. Two notes. First, the section is honest about limits (cooperativism's scale/capital problem; oversight boards' dependence on the platform that constitutes them) — good, and rare. Second, contestability (Alfrink et al., 2023) is doing a lot of work as the case-level voice mechanism; a referee may want one sentence on why case-level contestation, which the chapter itself says "stops short of a share in how the system is governed," nonetheless counts as building coordinative sovereignty rather than merely reprising the rights/protections the §6 clarification distinguished from standing. The distinction between *contesting a determination* and *holding a share in governance* is load-bearing for the construct and slightly blurred here.

### §8 Implications

The independent-variation thesis (high digital sovereignty + low coordinative sovereignty = "impeccably compliant and strategically captured," and the reverse via the platform-work directive) is the chapter's testable core and it is stated crisply. The 2×2 is genuinely useful and the platform-work-directive example (workers gain standing while owning zero infrastructure) is a real, well-chosen empirical anchor (European Parliament & Council, 2024). The honesty about measurement — "argued but not tested" until instruments exist — is exactly right and a referee will respect it. The openness-vs-control reframing (§8, policymakers) — that a closed sovereign national platform "reproduces the co-optation it was meant to escape, now under a domestic flag" — is a strong, original policy point and it is the best paragraph in §8. No substantive objection; the section is disciplined.

### §9 Future research

The four directions (algorithmacy instrument anchored to a behavioral criterion; coordinative-sovereignty instrument discriminated from psychological empowerment (Spreitzer, 1995) and from digital-sovereignty measures; the two-step design that classifies mediators before measuring response; reported-vs-afforded standing via the formal model) are well specified and the discriminant-validity worries are the right ones. The behavioral-criterion anchor for algorithmacy (accuracy of an actor's predictions of how the system will treat a set of moves) is a genuinely good operationalization and follows directly from Möhlmann's sensemaking. No objection.

### §10 Conclusion

Clean recap; the exit/voice/computable-line summary is faithful to the body. Two style flags only (see Part 2): the "constitutive priesthood" flourish and the closer verge on purple, and the conclusion re-states the Ananny & Crawford point and the independent-variation thesis one more time each. Trim the recaps to references-back.

---

### What a platform-studies referee would demand, in one list

1. **Cite Stark & Pais (2020)** as the origin of the co-opt-as-fourth-mechanism typology; keep Stark & Vanden Broeck (2024) as its development. [VERIFY exact ref.]
2. **Distinguish Stark's (neutral, valuation) co-optation from the chapter's (extractive, domination) reading** — own the critical synthesis instead of attributing it to Stark.
3. **De-anthropomorphize the mediator in §3** — locate interest in the operator, adaptivity in human reconfiguration (Kellogg et al.; Christin; Möhlmann).
4. **Fix the two-sided-markets economics in §3.3** — "rent independent of any service" contradicts Rochet–Tirole and Armstrong–Wright; distinguish bottleneck *power* from bottleneck *rent*; attribute "competitive bottleneck" to Armstrong & Wright and tie it to single-homing = platform dependence.
5. **Anchor "adaptive"** to continuous experimentation / algorithm-as-deployed decoupling (Christin, 2020 [VERIFY]).
6. **Pull Kellogg's "contested terrain" (resistance/gaming) into §3–§4** — the chapter's best empirical ally, currently used only to dismiss an objection.
7. **Narrow the algorithmacy novelty claim** — integration + triad-embedding, not "others only spectate"; the spectatorship line is unfair to Möhlmann, Bucher, DeVito and self-contradicts.
8. **Cite Rosenblat & Stark (2016)** and classify the ride-hail matching case *carefully* — necessity is partly a design achievement the platform defends, not a fact of nature.
9. **Engage Hirschman's exit-undermines-voice dynamic** in the portfolio argument (§5.3–§5.4).

---

## Part 2 — Style / slop audit (register-aware)

The draft is, by the repo's own metrics, clean: the antithesis machine fires perhaps three times in 9,000 words, self-narrating-virtue phrases are absent, and fragment-openers are rare. The real slop is elsewhere.

**Slop 1 — verbatim over-repetition of the Ananny & Crawford point (the chapter's one genuine repeat offender).** The "legibility/transparency without standing/an-institution-to-act-on-it" argument is made five times, in near-identical words:

- §3.2: "A disclosure that no party has standing to contest is a fact without a consequence."
- §3.3: "A transparent bottleneck is still a bottleneck, and a disclosed objective the coordinated actor has no standing to contest is still an objective imposed on it."
- §6: "Legibility without standing yields a disclosure no one can act on (Ananny & Crawford, 2018)."
- §7: "This answers the failure Ananny and Crawford (2018) identify. Transparency without an institution to act on it yields nothing."
- §8: "Platform coordination breaks that assumption by supplying legibility without standing."

*Failure:* Rule 4 (say each point once, in the place it belongs; the repo names "limitation recaps" as the repeat offender — this is one). Five statements of one idea.
*Fix:* State it definitively once, in §3.2 (where the Ananny & Crawford cite belongs). In §6, §7, §8 refer back ("the legibility-without-standing gap of §3.2") rather than re-arguing. Keep §7's version only if it adds the *institutional* turn (a bargaining unit is the missing institution) — that is new content, so it earns its place; strip the restated premise from it.

**Slop 2 — the doubled "still a X / still an X" construction.** §3.3: "A transparent bottleneck is **still a bottleneck**, and a disclosed objective… is **still an objective imposed on it**." The first clause is a good line; the second copies its shape for cadence and adds little (a disclosed objective one cannot contest is the transparent bottleneck, restated).
*Failure:* mechanized parallelism for rhythm (Rule 7: triads/parallels only when each member carries distinct content).
*Fix:* "A transparent bottleneck is still a bottleneck. Disclosure changes what the coordinated actor can see, not what it can contest."

**Slop 3 — the "spectatorship" line contradicts the next sentence.** §4: "These competences mostly describe spectatorship… interpreting its outputs, reflecting on its effects." followed shortly by "Algorithm sensemaking is the inferential part of algorithmacy under another name… the translational part has a field record too."
*Failure:* internal contradiction dressed as a distinction; the claim is retracted a paragraph after it is made.
*Fix:* Drop "spectatorship" for the three from-within neighbors. Reserve the outside/inside contrast for Dogruel-style *awareness* scales, and state the real novelty positively: "Algorithmacy integrates three competences the field has documented separately — sensemaking (Möhlmann et al., 2023), anticipatory compliance (Bucher et al., 2021), and adaptive folk theorization (DeVito, 2021) — and places them inside the irreducible triad, where the actor coordinates with a counterpart *through* the system as the system pursues the operator's ends."

**Slop 4 — anthropomorphic agency (style face of the substantive §3 problem).** "it pursues objectives of its own and revises its rules continuously in their pursuit"; "The system… pursues objectives of its own"; "It optimizes for ends of its own."
*Failure:* Rule 1's spirit (name the real agent). The agent is the firm; the system executes.
*Fix:* "a mediator whose operator pursues objectives of its own and reconfigures its rules continuously in their service"; "a system through which a firm optimizes for ends the coordinated parties do not share."

**Slop 5 — purple closer.** §10: "whether it will stay concentrated among a new constitutive priesthood… the stakes are the sovereignty of everyone who now coordinates through a system they cannot see."
*Failure:* empty-grandeur closer (the "priesthood" metaphor is unearned; the chapter never developed a clerical-monopoly analysis).
*Fix:* Either earn "priesthood" earlier (the §2.2 literate-clerical-few point could seed it) or cut to the plainer, stronger line already present: "held by a narrow class of those who can model and act within the systems that coordinate the rest."

**Non-issue, for the record:** the impersonal-agentive register is correct and consistent; "the chapter argues," "Stark and Vanden Broeck write," "Ananny and Crawford show" are all house-compliant. Paragraph openers lean on "The" but rarely as sub-six-word fragments; acceptable. No `I/we`. This draft does not have the repo's characteristic slop; its problems are substantive, not stylistic.

---

## Part 3 — Line-level revisions (paste-ready)

**§3, the novelty conjunction — de-anthropomorphize + anchor "adaptive."**
Replace:
> It is opaque: its determinations are produced by high-dimensional systems that resist interpretation. And it is interested and adaptive: it pursues objectives of its own and revises its rules continuously in their pursuit.

with:
> It is opaque: its determinations are produced by high-dimensional systems that resist interpretation (Burrell, 2016). And it is interested and adaptive: its operator pursues objectives of its own and reconfigures the system's rules continuously in their service, through the ongoing experimentation that keeps the deployed algorithm ahead of any disclosure of it (Christin, 2020 [VERIFY]; Möhlmann et al., 2023).

**§3, co-optation origin — fix the attribution.**
Replace:
> Stark and Vanden Broeck (2024) write that where actors in hierarchies command, in markets contract, and in networks collaborate, on platforms they are co-opted: enrolled into an algorithmic system without delegated authority and without the explicit contracts that mark employment or exchange.

with:
> Stark and Pais (2020) name the fourth term: where actors in hierarchies command, in markets compete, and in networks collaborate, on platforms they are co-opted — enrolled into an algorithmic system without delegated authority and without the explicit contracts that mark employment or exchange (developed in Stark & Vanden Broeck, 2024). Their co-optation is first a claim about coordination, not domination; the political economy that makes it a relation of power is this chapter's addition (§3.3).

**§3.3, the economics error — the priority fix.**
Replace:
> that structural position, which the economics of two-sided markets (Rochet & Tirole, 2003) calls a competitive bottleneck (Armstrong & Wright, 2007), is a source of rent independent of any service the mediator provides. A mediator through which all coordination must flow captures a share of the value of that coordination simply by standing where it stands.

with:
> that structural position is what the two-sided-market literature (Rochet & Tirole, 2003; Armstrong & Wright, 2007) calls a competitive bottleneck: where one side single-homes because no alternative platform exists at scale (Cutolo & Kenney, 2021), the mediator holds monopoly power over access to it. The bottleneck confers pricing power over access that persists even when the mediator's marginal service is small, because both sides must route through it. The power is topological; the rent it yields is disciplined by the sides' outside options, which is why multihoming (§5.3) is what turns bottleneck power into contestable rent.

**§3.3, the doubled line.**
Replace:
> A transparent bottleneck is still a bottleneck, and a disclosed objective the coordinated actor has no standing to contest is still an objective imposed on it.

with:
> A transparent bottleneck is still a bottleneck. Disclosure changes what the coordinated actor can see, not what it can contest.

**§4, the spectatorship line — replace with the honest novelty claim.**
Replace:
> These competences mostly describe spectatorship: recognizing that a system is at work, interpreting its outputs, reflecting on its effects.

with:
> Awareness scales of this kind measure recognition that a system is at work and knowledge of how it works in principle. Algorithmacy names something the field has documented in pieces but not integrated: sensemaking of the managing algorithm (Möhlmann et al., 2023), anticipatory compliance that shapes conduct to an unseen system (Bucher et al., 2021), and folk theorization revised as the platform changes (DeVito, 2021). Its contribution is to hold these three together and place them inside the irreducible triad, where the point is to coordinate with a counterpart through a system pursuing the operator's ends.

**§5.2/§5.4, the ride-hail classification — show the work.**
Replace:
> A ride-hail platform likewise matches riders and drivers in real time, which is integrating work, and stands between a rider and driver who could re-contact each other directly, which is a bypassable relationship gate.

with:
> A ride-hail platform matches riders and drivers in real time, plausibly integrating work at scale, and stands between a rider and driver who could re-contact each other directly. Whether that relationship gate is genuinely bypassable is contested: the platform engineers its non-bypassability by suppressing contact information and holding the parties' identities (Rosenblat & Stark, 2016). The classification is therefore partly a fact about the platform's design, not only about the coordination — a reminder that necessity can be manufactured and defended, which §4's account of opacity as a rent-preserving strategy predicts.

**§5.3, Hirschman nuance — one sentence to add** after the exit/voice mapping:
> Hirschman also warned that exit can undermine voice: the actors most able to leave are those whose departure most weakens a collective push to stay and reform. In the portfolio of §5.4 this couples the two responses — an actor who exits a platform's contingent functions may thereby drain the leverage available for voice on its necessary ones.

**§6, third clarification — refer back instead of re-arguing.**
Replace:
> Second, transparency does not produce it. Legibility without standing yields a disclosure no one can act on (Ananny & Crawford, 2018), and coordinative sovereignty is the standing that would make the disclosure matter.

with:
> Second, transparency does not produce it. The legibility-without-standing gap of §3.2 is exactly the gap coordinative sovereignty names; the standing is what would make a disclosure matter, and it comes before any act of disclosure.

**§10, the purple closer.**
Replace:
> Whether coordinative sovereignty becomes a general condition or remains the possession of an algorithmate few will depend on whether algorithmacy can be democratized as literacy was, or whether it will stay concentrated among a new constitutive priesthood.

with:
> Whether coordinative sovereignty becomes a general condition or stays the possession of an algorithmate few will depend on whether algorithmacy can be democratized as literacy was, or stays concentrated among the narrow class that can model and act within the systems that coordinate the rest.

---

## Verdict

**Accept with major revisions.** The construct is real, the gap it fills is real, and the chapter is unusually well built and unusually clean on prose. But three substantive fixes are prerequisites for a platform-studies venue, not polish: (1) the two-sided-markets economics in §3.3 is stated in a form the cited sources refute; (2) the co-optation reading mis-attributes and over-reads Stark; (3) the mediator is intermittently anthropomorphized in exactly the way the field (Kellogg, Christin, Möhlmann) exists to forbid. None threatens the thesis; all are correctable without weakening it.

**Most important single fix:** §3.3. "A source of rent independent of any service the mediator provides" cites Rochet–Tirole and Armstrong–Wright against their own content. Replace it with the bottleneck-power / bottleneck-rent distinction tied to single-homing platform dependence. This is the one error a specialist referee will not wave past, and fixing it *strengthens* the political economy rather than softening it.

## Biggest strength

The disaggregation thesis — digital sovereignty (a literacy/reading construct over infrastructure) and coordinative sovereignty (an algorithmacy/standing construct over coordination) vary independently, so a firm can be "impeccably compliant and strategically captured" — is a genuinely original, testable, and useful claim, and the platform-work-directive vs market-conduct-remedy pairing in §8 gives it real empirical teeth. The necessary/contingent diagnostic, sorting institutions into exit-restoring and voice-building, does honest organizational work that neither the digital-sovereignty literature nor the algorithmic-management literature currently offers.

## The one thing only the author can supply

**A single genuinely algorithmic, hard case worked all the way through the necessary/contingent test — showing the classification is *derived*, not asserted, and acknowledging where the platform has *manufactured* apparent necessity.** The OTA/rate-parity case is close but its gate is a contract, so the statute does the work; the ride-hail and app-store cases are asserted. Only the author can decide which case to commit to and do the labor of classifying its functions against real evidence (contact-suppression, surge opacity, distribution vs payment gating), including the reflexive point that platforms invest in making contingent gates look necessary. That worked case is what would convert the diagnostic from an elegant device into a demonstrated method — and it is the thing a platform-studies referee will most want to see before believing the construct travels beyond old-economy brokerage.
