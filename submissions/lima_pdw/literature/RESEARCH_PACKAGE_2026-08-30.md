# CMC/HMC Literature Strengthening Pass — 2026-08-30

## Scope

The citation-accuracy audit (`literature/CITATION_TIERED_AUDIT_2026-08-30.md`) verified all 83
existing citations for factual accuracy. This is a different task: *coverage*, not accuracy. The
author's concern: "it feels like we are missing some literature... there is a LOT more out on CMC and
HMC that we really should include to demonstrate that we are experts on their concepts."

This pass reconciles `manuscript/PAPER.md` against `literature/cards/`'s 74-card
`communication-competence` cluster (mostly full-text-read, mostly uncited) and the stale
`literature/RESEARCH_PACKAGE_2026-08-26.md`, before running a narrow external search for anything
that internal reconciliation can't supply. Planning (tiering, batching, model assignment) was done by
a Fable-model agent, per the author's instruction; see `/Users/ludwitt/.claude/plans/zany-tumbling-riddle.md`
for the full plan.

**Screening logic every candidate is run through:** the paper's own four-part test (line 167 of
`PAPER.md`: does a framework (a) model individual capacity, (b) keep the human counterpart active and
interdependent, (c) make the intermediary autonomously evaluate-and-bind both parties, (d) name a
genuine vacancy rather than a terminological dispute), plus an independent reviewer-expectation rating
(MUST-CITE / EXPECTED / OPTIONAL). No cap on genuine-gap recommendations — every batch reports
everything it finds; the author makes the final integration cut.

**This pass produces a recommendations report only. No agent edits `PAPER.md` or any card.**
Batch reports are appended below as they complete, followed by a synthesized, deduplicated
recommendation table.

---

## Batch C1 — Manky (2025) full-text access attempt

**Outcome: full text NOT obtained.** No legitimate channel produced the article. No repo files were edited; no email was sent.

### Channels tried

1. **Institutional page (Universidad del Pacífico faculty site)** — partial success. Confirms current email `wo.manky@up.edu.pe`, ORCID `0000-0003-1741-3461`. No self-archived copy of this article found.
2. **Universidad del Pacífico repository** — failure, nothing matching this title/DOI.
3. **PUCP repository** — failure.
4. **ORCID profile** — inconclusive (fetch tool returned malformed response); worth a manual check.
5. **ResearchGate** — failure; no RG entry exists yet for this specific article (so no "Request full-text" button available). Two related, likely-lower-relevance Manky papers exist on RG if useful for context.
6. **Academia.edu** — failure (403).
7. **Google Scholar "all versions"** — failure (CAPTCHA-blocked; not bypassed).
8. **Wiley green-OA accepted manuscript** — failure, explainable: article published online 5 Sept 2025, so as of today (30 Aug 2026) it's ~12 months post-publication — plausibly still within a 12–24 month embargo window, consistent with no deposit found anywhere.
9. **Bentley ILL** — confirmed viable, not submitted. DOI 10.1111/ntwe.70005; log in via Bentley library credentials, search the catalog/discovery layer, use "Request via ILL" if not licensed. Typical turnaround a few days to ~1–2 weeks. **This is likely the most reliable near-term path given the embargo timing.**
10. **Draft email to Omar Manky** — written, NOT sent, requesting the accepted manuscript/preprint for citation-verification purposes ahead of the workshop submission. Full text saved at the agent's scratchpad location; reproduced in full below for convenience.

> Subject: Request for accepted manuscript — "Reimagining Work Security in Latin America's Platform Economy" (NTWE, 2025)
>
> Dear Professor Manky,
>
> I am writing ahead of a paper development workshop submission that cites your article "Reimagining Work Security in Latin America's Platform Economy: Workers' Strategies Amid Urban Violence" (New Technology, Work and Employment, 41(1), 33-44, doi:10.1111/ntwe.70005) as a key motivating example. I was unable to access the published version through my institution's subscriptions, and I would like to verify a specific empirical detail — how drivers use platform metrics to assess passenger safety — directly against your text before the citation goes into the submission.
>
> Would you be willing to share a copy of the accepted manuscript or a preprint? I would be glad to cite whichever version you prefer once the workshop draft is finalized.
>
> Thank you for your time, and congratulations on the publication.
>
> Best regards,
> [Your name / affiliation / email]

**Email address caveat:** `wo.manky@up.edu.pe` is the better-sourced candidate (confirmed via a direct page fetch), but a separate AI-generated search summary surfaced a slightly different address (`wo.mankyb@up.edu.pe`) that looks like a search-artifact conflation with his middle name — **verify the address manually on the live faculty page before sending.**

### Net status of the Manky claim

Still unverified at full-text depth. The abstract-level support (platforms provide "data-driven oversight of passengers and routes," "mitigating physical risks") remains consistent with PAPER.md's characterization, but the specific "reads an opaque metric to decide whether to accept a passenger" mechanism is not yet confirmed against primary text. Two live paths remain open: send the drafted email (after confirming the address), or use Bentley ILL. See Batch B2 below for whether a second corroborating source was found.

---

## Batch A1 — Revalidate stale research package (`RESEARCH_PACKAGE_2026-08-26.md`)

**Headline finding: 12 of 15 numbered recommendations in the stale package are already integrated into the current draft** — several more thoroughly than the package's own proposed insert. One is obsolete (the draft's methodology moved past what it would have supported). Only **two genuinely open gaps** remain.

### INTEGRATED (12 items, no action needed)
Field stocktakings (Oeldorf-Hirsch, Gagrčin, Iyamu) — L157. Fourth party (Katsh & Rifkin; Wing et al.) — L27, L163, L252. Curchod triad/visibility gap — L165, L252 (one small unused sub-point: Curchod's "coalition" framing between invisible buyers and the platform owner — optional, not reviewer-visible). Cameron — L165, L256 (one small residual: Cameron's consent mechanism could be added as a second named rival alongside Rahman's dependence variable at L137's Study-3-controls sentence — optional). Rahman's 18 clients — L133. Zhou item 6 (appeal) — L121. Hancock "between people" — L93. Insider-research quartet (Brannick & Coghlan, Anteby, Mercer, Ferguson et al.) — L572, L284. Abidin visibility labour — L159. Healy & Pekarek — L165, L409. Jarrahi & Sutherland (2019) — L141. The 2026 rivals (Hong, Scolari, Ayasrah, Mahy & Li) — L327. Bowen (sensitizing concepts) — L591. Tracy (no longer an orphan) — L572. Laupichler/SNAIL — L241.

### OBSOLETE (1 item)
Saunders et al. (2018) on saturation-based stopping rules — the draft's Empirical Strategy section (L626) explicitly uses an *abductive-sufficiency* stopping criterion instead of grounded-theory saturation, which is what Saunders would have grounded. Citing it now would import vocabulary the draft has deliberately moved away from. No action unless a future revision reverts to saturation.

### STILL OPEN (2 items — the only genuine gaps this batch found)

**1. The AI-MC/HMC empirical set** — Hohenstein & Jung (2020), Hohenstein et al. (2023), Mieczkowski et al. (2021), Jakesch et al. (2019), Edwards et al. (2014). None appear anywhere in `PAPER.md`. Four-part test: mixed by source — Hohenstein et al. (2023) and Hohenstein & Jung (2020) come closest (both put two humans and an intervening AI system in frame and measure attribution/accountability redistribution) but the AI in both "absorbs blame after the fact" rather than committing a binding determination — so these sources *confirm the paper's boundary from outside* rather than threaten it. Mieczkowski et al. (2021) keeps both parties present/in-contact throughout (useful methodologically, not as a rival). Jakesch et al. (2019) and Edwards et al. (2014) measure a different explanandum (the machine's own perceived competence).
   - **Reviewer expectation: EXPECTED**, not MUST-CITE. A CMC/HMC-literate reviewer who knows Hancock, Naaman & Levy (2020) well would expect its empirical successors cited, particularly Hohenstein et al. (2023) — the largest, most-cited empirical AI-MC study. Absence is a missed strengthening move, not an exposed flank (none of the four threaten the central claim).
   - **Placement proposal 1:** After L99's Hancock/AI-MC passage (the "message receiver is assumed to understand and accept that agency" sentence), add 1-2 sentences citing Hohenstein & Jung (2020) and Hohenstein et al. (2023) as empirical confirmation of exactly that vulnerability — participants penalize the suspected-AI-assisted party, and the AI absorbs blame rather than issuing a binding verdict. Converts an assertion about the literature's silence into a citation of what the literature found when it looked.
   - **Placement proposal 2:** In "Constitutive Operations" at the *specifying intent* definition (L202) or in Appendix B/C's instrument discussion, cite Mieczkowski et al. (2021)'s referential-communication paradigm as a validated behavioral (non-self-report) measure of grounding. Jakesch et al. (2019)'s "replicant effect" pairs naturally with Proposition 2's stratified-fluency claim (L268) — one clause. Edwards et al. (2014) is weakest/optional.

**2. DigComp 2.2 (Vuorikari et al. 2022) and UNESCO (2024).** Neither appears in `PAPER.md`. Both fail the four-part test the same instructive way: DigComp's Area 2 (Communication/collaboration) holds the human counterpart, its AI appendix holds the system, "the two never appear in the same relation" (per card). UNESCO's teacher framework is the sharper near-miss — it names "human accountability" as a competency (1.2), landing directly on the paper's own withholding vocabulary, but its entire normative program is to *keep* accountability intact against erosion, whereas algorithmacy's premise is that accountability has *already* been withheld with no regulatory appeal.
   - **Reviewer expectation: EXPECTED for DigComp, borderline MUST-CITE for UNESCO** — the near-miss is exactly the kind a hostile reviewer surfaces to suggest the "vacancy" is just a naming dispute.
   - **Placement proposal:** Both belong in "What These Boundaries Share" (L153-169), immediately after the field-stocktakings paragraph (L157) and before the visibility-labour paragraph (L159) — a natural third/fourth entry in a list the section already runs, not a new subsection. The UNESCO citation specifically strengthens the "four analytical conditions" paragraph (L167): UNESCO's student is exactly the "downstream beneficiary of a professional's duty" exclusion category the current list of exclusions doesn't yet instantiate with a citation.

**Net: neither open item threatens the paper's central claim; both are legitimate, well-scoped strengthening opportunities that fit as background citations inside existing sections — no new hearing needed for either.**

---

## Batch A2 — Classical CMC media theory (11 sources)

Walther (1992, 1996, 2007); Short, Williams & Christie (1976); Daft & Lengel (1986); Daft, Lengel & Trevino (1987); Dennis & Valacich (1999); Dennis, Fuller & Valacich (2008); Clark & Brennan (1991); Biocca, Harms & Burgoon (2003); Zhao (2003). **None of these eleven sources appear anywhere in the current `PAPER.md`** — confirmed by full-text read and grep.

### GENUINE GAP — recommend (7 of 11)

| Source | Reviewer expectation | Placement | What it does |
|---|---|---|---|
| **Walther (1992) + (1996)** | MUST-CITE | New hearing OR folded into Spitzberg hearing — see structural question below | See below — the single most important finding of this batch |
| Walther (2007) | EXPECTED | Proposition 2 / Uneven Distribution (L242, 266–268) | Supplies a testable rival mechanism (cognitive slack vs. accumulated learning) for uneven distribution — gives Study 3 a falsifier it currently lacks |
| Daft & Lengel (1986) | MUST-CITE (OS/OT audience) | "Constitutive Operations" (L197–199), the "opacity withholds the rule" sentence | Precise vocabulary (uncertainty vs. equivocality) for what the worker actually faces — she isn't short of data, she faces equivocality no channel resolves |
| Daft, Lengel & Trevino (1987) | MUST-CITE | "What These Boundaries Share" (L153–169), ~150–200 words, same move the section already runs for other near-misses | The nearest neighbor construct from organization theory itself (not comm studies/HCI) — an OS/OT PDW audience is more likely to reach for this one than Spitzberg or Guzman & Lewis; its absence is conspicuous given how hard the section already works to exhaust adjacent literatures |
| Dennis, Fuller & Valacich (2008) | MUST-CITE | Paired with Daft & Lengel at L197–199 | Modern successor vocabulary ("convergence") — names precisely what the arrangement withholds, sharper than the paper's current "common understanding, withheld" |
| Clark & Brennan (1991) | MUST-CITE | Spitzberg hearing critique (L73–77) or "Why Each Operation Requires the Full Triad" (L213–221), ~150–250 words | Arguably the single most theoretically load-bearing item on this list — grounding theory states *why* coorientation collapses (no mutual evidence of uptake is structurally available), giving theoretical warrant rather than just description for why the construct splits into separate interpreting/specifying-intent operations |
| Biocca, Harms & Burgoon (2003) | EXPECTED | Conclusion's measurement discussion (L325) or Appendix C | Construct-validity precedent for perceived-vs-actual understanding, needed once "interpreting" gets operationalized |

### MARGINAL — optional (3)
- Short, Williams & Christie (1976) — canon-origin term for "social presence," but superseded by Biocca et al. (2003) for real engagement; no need for the 1976 text itself.
- Dennis & Valacich (1999) — useful only as a reflexive caution (richness theory's own empirical collapse); a footnote if the paper wants to preempt "does this construct travel" skepticism, not required.
- Zhao (2003) — nice illustration that even the most systematic prior taxonomy of mediated configurations is two-place throughout; not required.

### NOT RELEVANT
None — all 11 sources cleared at least MARGINAL.

### The structural question: does anything require an eighth hearing?

**Yes — Walther (1992/1996) is a genuinely close near-miss, closer than any of the seven existing hearings.** Every current hearing satisfies two of the four conditions and fails the other two instructively; Walther satisfies (a) individual capacity and (b) active, interdependent counterpart as robustly as any current hearing, and fails only (c) — the channel never autonomously evaluates or binds. That's a categorically closer miss than Daft/Lengel/Trevino, whose failure on (c) is total rather than partial.

**The concrete threat:** Walther's adaptation thesis — that communicators develop, through experience and without instruction, the capacity to convey what a narrow channel was thought unable to carry — reads like "specifying intent" under a different name, argued decades before the paper's own "acquired through participation, not instruction" claim (L241). A CMC-literate reviewer will very plausibly ask: *how is this not Walther's adaptation thesis with an algorithm swapped in for the human receiver?* The paper currently has no answer on the page — though a clean one exists: Walther's loop closes because the *same* party that receives the message also evaluates and replies to it; in the triad, the party that evaluates (the intermediary) is not the party whose understanding matters (the counterpart), and neither returns anything resembling a reply. This is the same minimal-pair move the paper already runs successfully against AI-mediated communication ("An editor is not a judge," L97) — just missing for the source that needs it most.

**Two options, with real costs (not a recommendation — the author's call):**

*Option A — new eighth hearing.* Insert between "Computer-Mediated Communication Competence" and "Human–Machine Communication" (~after L77). ~600–900 new words matching the existing hearings' structure. Also requires: a new Table 1 row; changing every "seven candidate constructs" reference to "eight" (abstract L9, introduction L31, section opener L52, the L167 cross-reference); one added clause in the L155 cross-construct synthesis paragraph.

*Option B — fold into the existing Spitzberg hearing.* Expand L67–77 by ~300–500 words, naming Walther explicitly under "the relational communication tradition" Spitzberg is already said to be rooted in (L71), running the same near-miss argument inside that hearing. Lower structural cost (no renumbering, no new Table row, no abstract edit) but risks blurring two distinct theoretical lineages (Spitzberg's five-dimension model, Walther's four-component model) into one subsection.

---

## Batch A3 — HMC / CASA / AI-MC empirical (18 sources)

Nass & Moon (2000); Reeves & Nass (1996); Sundar & Nass (2000); Sundar & Kim (2019); Guzman (2018, ed. vol.); Guzman, McEwen & Jones (2023); Jakesch et al. (2019); Mieczkowski et al. (2021); Hohenstein & Jung (2020); **Hohenstein et al. (2023)**; Jung, Martelaro & Hinds (2015); Sebo et al. (2020); Traeger et al. (2020); Seeber et al. (2020); Suchman (2007); Elish (2019); Natale (2021); Krämer (2015). **None appear anywhere in `PAPER.md`.**

### GENUINE GAP — recommend (16 of 18)

| Source | Reviewer expectation | Placement | What it does |
|---|---|---|---|
| **Hohenstein et al. (2023)** *Scientific Reports* | **MUST-CITE — priority, single strongest addition in this batch** | AI-MC section after L99, and/or the accountability paragraph L252 | Direct empirical warrant for the paper's central mechanism: participants who *suspected* AI assistance evaluated their partner more negatively and the relationship suffered — "the benefit accrues to the interaction; the cost accrues to an individual, on the basis of a suspicion that may be wrong." Converts the accountability-forfeiture claim from assertion to evidence. |
| Sundar & Nass (2000) | MUST-CITE | *Interpreting* discussion (~L215) | Experimental proof that source-attribution is a live cognitive problem users must resolve — direct empirical grounding for "one signal from which to infer two minds" |
| Guzman, McEwen & Jones (2023), SAGE Handbook | MUST-CITE | HMC section (~L89) | Converts "the field's self-description" from an inference about one article to a documented fact about the field's entire 65-chapter organizing taxonomy |
| Hohenstein & Jung (2020) | MUST-CITE | Accountability-benchmark paragraph (~L252) | Experimental demonstration that inserting a computational agent into a two-person exchange redistributes blame away from the parties — companion to Elish (2019), whose term it borrows |
| Sebo et al. (2020), HRI lit review | MUST-CITE | "Adjacent disciplines" paragraph (~L163–167) | Systematic-review-level confirmation that an entire neighboring field (HRI/robots-in-groups) has not asked the paper's capacity question either — upgrades the vacancy claim from "seven constructs miss it" to "a systematic review of a neighboring literature confirms it too" |
| Suchman (2007) | MUST-CITE | *Interpreting* definition (~L201, L215) and "Acquisition through Participation" (~L241) | The theoretical mechanism behind why the interpretive burden falls entirely on the participant — machine has only a thin, pre-categorized trace of her conduct; she has rich access to its |
| Elish (2019) | MUST-CITE | Accountability paragraph (~L252) and the paradox section (~L254–256) | Structural explanation for why responsibility defaults to the visible human party; also inoculates the construct itself against the charge that algorithmacy does the platform's attributional work for it |
| Nass & Moon (2000) | EXPECTED | Second rival hypothesis alongside Rahman (~L137, L242) | Mindless CASA scripting as a rival explanation for Proposition 2's predicted variance — Study 3 needs a mindful/mindless processing check |
| Sundar & Kim (2019), machine heuristic | EXPECTED | Covariate/control discussion (~L185, L137) | A worker's belief that "machine = objective" could inflate algorithmacy scores independent of actual developed competency — discriminant-validity threat worth naming/controlling for |
| Jakesch et al. (2019) | EXPECTED | *Specifying intent* paragraph (~L217) | Signal provenance read comparatively against a cohort — grounds intent-specification as positional not absolute |
| Mieczkowski et al. (2021) | EXPECTED | Appendix C instrument discussion (~L315–325) | 50-year-validated behavioral (non-self-report) instrument for whether meaning reached a partner — candidate for Study 2, with the caveat it assumes co-presence and needs modification |
| Jung, Martelaro & Hinds (2015) | EXPECTED | "Adjacent disciplines" paragraph (~L163–165) | Closest HRI analog — robot *proposes*, gate *determines*; sharpens condition (c) |
| Traeger et al. (2020), PNAS | EXPECTED | Near Proposition 3 (~L270–272) | Well-powered finding that disclosed machine fallibility *improves* coordination — supports the inference that opacity actively degrades coordination, not merely withholds information |
| Seeber et al. (2020) | EXPECTED–MUST-CITE | "Adjacent disciplines" / L167 | Participates-vs-adjudicates distinction parallels the ODR support/decider distinction the paper already draws from Wing et al. — shows the boundary condition recurs whenever a field puts a machine among people |
| Natale (2021) | EXPECTED | RQ1/Interpreting instrument discussion (~L306–320) | Validity caution: interfaces are designed to make users *feel* their inferences land regardless of accuracy — a limitation worth naming for the self-report arm |
| Krämer (2015) | OPTIONAL | One clause, "What These Boundaries Share" (~L155–159) or intro (~L27) | "A messenger who has become a principal" — portable, sharpened phrase for what distinguishes the intermediary from a transmission channel |

### MARGINAL — optional (2)
- Reeves & Nass (1996), *The Media Equation* — genealogical precursor to Guzman & Lewis's "communicative subject" move; Nass & Moon (2000) already carries this load.
- Guzman (2018, edited volume) — cite alongside Guzman & Lewis (2020) purely for field-founding acknowledgment; no new argumentative content.

### NOT RELEVANT
None — all 18 sources bear on the argument at some level (consistent with the cards having been built against this manuscript's own claims).

---

## Batch B2 — Second corroborating source for the Manky (2025) claim

**Card-library check: no match.** `hong2026.md` (China) explicitly excludes the passenger/customer from its skill framework; `rosenblatstark2016.md` (US) treats ratings as managerial discipline, not counterpart-safety assessment; neither fits. `healy2024.md` is listed in `INDEX.md` but the card file is a broken link.

**Recommended candidate, full text obtained and read: Oliveira, P. T. G. de, & Junges, J. R. (2023). "Digital food delivery platforms: working conditions and health risks." *Saúde e Sociedade*, 32(3), e220642en. DOI: 10.1590/S0104-12902023220642en.** Diamond OA, verified via OpenAlex + live SciELO PDF. Qualitative study, 14 semi-structured interviews with iFood motorcycle couriers, São Leopoldo/Porto Alegre, Brazil.

**The corroborating passage (p.8):** couriers read platform-relayed delivery information (address, customer name) as a safety signal to detect ambush/robbery setups — *"Some addresses are fake for robberies, they send the address and rob you, they give someone else's name" (I1)*; *"You never know where you are taking the meal, it may turn out to be a scam" (I12)*. Couriers "must be familiar with the delivery site in order not to fall into 'trick addresses.'"

**Fit assessment:** Corroborates the *general* mechanism well (Latin American platform workers reading platform-conveyed information in real time to judge physical safety before completing a job), but the specific instrument differs from Manky's claim — address/name pattern-recognition against robbery risk, not a numeric rating/score read to accept-or-decline a passenger. Strongest available hedge, not a verbatim match.

**Second-tier lead, not yet usable:** Bonhomme, Ustek-Spilda & Arriagada (2024), *NTWE* 40(2), 195–213 — same journal as Manky, Chile, migrant food-delivery workers, algorithmic surveillance. Abstract-only (Wiley 403'd; KCL repository copy embargoed until 24 September 2026). Describes surveillance *of* workers/resistance, not counterparty-safety assessment — may not fit even once accessible. Worth a re-check after the embargo lifts only if Manky remains unresolved then.

**Recommendation:** cite Oliveira & Junges (2023) as a supplementary/hedging citation alongside Manky (2025) if Manky's specific mechanism can't be confirmed at full-text depth — genuine, fully open, directly-read evidence of the general pattern, even though the specific signal type differs.

---

## Batch A4 — Communicative-competence lineage (17 sources)

Habermas (1970); Wiemann (1977, 1980); Canale & Swain (1980); Bachman (1990); Duran (1983); McCroskey (1982); Rubin (1982, 1985, 1994); Jablin & Sias (2001); Spitzberg (1983, 2013, 2015); Hannawa & Spitzberg (2015, eds.); Bunz & Montez (2015); Canary & Spitzberg (1987). **The paper currently cites only Spitzberg (2006) and Spitzberg & Cupach (1984) from this entire lineage.**

**Key finding, stated directly:** the gap isn't that Spitzberg (2006)/(1984) are thin — it's that the paper makes several specific, separable claims elsewhere (the derivation-of-three-operations discipline, the skill/competence categorical cut, acquisition-through-participation, the third operation's distinctness from "just adaptability") that a competence-literate reviewer will check against named prior art the two existing Spitzberg citations don't themselves supply.

**Habermas (1970) — direct answer to the key question:** earns a brief anchor paragraph, not a load-bearing role. His is a *counterfactual-ideal* competence; algorithmacy is a *positive-withholding* one. The distinction is cheap to state and risky to skip, since Habermas is the other famous coinage of "communicative competence" — silence could read as unfamiliarity with the term's philosophical branch.

### GENUINE GAP — MUST-CITE (7)

| Source | Placement | What it does |
|---|---|---|
| **Jablin & Sias (2001)** | "Acquisition through Participation" bullet (~L241) | **Single most dangerous omission in the batch** — sits on the paper's home turf (organizational communication); their "assimilation" argument (newcomers acquire competence through participation, not instruction, inferring competence from how others respond) is structurally close to the paper's own acquisition-through-participation property. A reviewer who knows this chapter will ask directly why it's absent. |
| Canale & Swain (1980) + Bachman (1990), jointly | "Constitutive Operations: The Tripartite Model" (~L197-212) | The standard citation pair whenever a paper claims to *decompose* a competence into a principled component set — exactly what the paper's operations-derivation move does. Canale & Swain's "strategic competence" (sustaining communication when enabling conditions are absent) is close enough to the paper's own logic that an applied-linguistics-literate reviewer would ask if algorithmacy reinvented it. |
| Spitzberg (2015) | "Categorical Delineation," Distinction-from-Skill bullet (~L231) | The paper stakes real weight on "competency, not skill" using a trainability/codifiability cut that is NOT the field's own cut (Spitzberg's mature molecular-behavior/molar-competence-as-impression distinction). Since the paper explicitly claims Spitzberg's lineage as warrant one paragraph later, failing to align with or explicitly decline his own cut reads as borrowing a lineage's name without its distinctions. |
| Hannawa & Spitzberg (2015, eds.) | "What These Boundaries Share" (~L157), alongside the existing systematic-review citations | The communication discipline's own 22-chapter stocktaking as of 2015, every chapter retaining a human counterpart, none addressing a three-party non-human-adjudicator arrangement — slots directly into the pattern the paper already runs with Oeldorf-Hirsch/Gagrčin/Iyamu. |
| Bunz & Montez (2015) | Distinction-from-Skill bullet (~L231) | Their finding that 20 years of CMC-competence-adjacent measures failed to survive a platform change is citable empirical precedent for the paper's currently-asserted (not evidenced) claim that proprietary, dynamic rules "preclude the codification rule-based skill acquisition requires." |
| Duran (1983) | *Keeping track* definition (~L203, L219) | Nearest antecedent to the paper's third operation — his Communicative Adaptability Scale measures noticing-and-revising to a changed situation. Paper needs the answer on the page (his actor reads a *visible* partner; algorithmacy's worker reads only outcomes from an unannounced system) before a reviewer asks "isn't this just adaptability?" |

### GENUINE GAP — EXPECTED (4)
- **Wiemann & Backlund (1980)** — sharpest available statement of a circularity risk in the paper's own design (if algorithmacy is partly measured through gate outcomes, a worker who fares well scores high by construction). Placement: Zhou et al. hearing (~L113-125) as discriminant-validity anchor.
- **McCroskey (1982)** — willingness/ability distinction exposes an unaddressed scope problem: a worker who correctly infers the gate's logic and *declines* to comply (reasoned non-compliance) would score low as currently specified, and the construct can't currently distinguish that from incapacity. Placement: Uneven Distribution (~L242).
- **Canary & Spitzberg (1987)** — precedent that appropriateness/effectiveness dissociate empirically (template for the paper's claim that interpreting and specifying intent don't travel together); also a genuine second rival hypothesis for Proposition 2 (attribution bias in the platform's rating apparatus could explain variance rather than capacity) alongside the existing Rahman-derived controls at L137.
- **Habermas (1970)** — see key question above; one anchor paragraph in the "Extant Constructs" preamble or opening of "Categorical Delineation."

### MARGINAL — optional (5)
Wiemann (1977) — Spitzberg's own ancestor; the descendant (already cited) covers the point. Spitzberg (1983) — an earlier draft of a position already cited at full strength; could be a co-citation, not a new paragraph. Rubin (1982) — a genuine methodological alternative (criterion-referenced behavioral assessment) worth one line in Appendix C material if there's room; not closing an anticipated gap. Rubin & Martin (1994) — the paper already runs this "derivation vs. collection" argument against three other targets (Long & Magerko, Sutherland et al., Zhou et al.); a fourth risks reading as padding.

### NOT RELEVANT (2)
Rubin (1985) — pure validity-study follow-up, superseded by the paper's already-cited modern psychometric authorities. Spitzberg (2013) — compact restatement for a health-professions audience, fully covered by the paper's existing Spitzberg citations and the recommended Spitzberg (2015) addition.

---

## Batch A5 — Interaction order, mediation, and full-cluster sweep

**Coverage confirmed complete: 7 (Part 1) + 46 (A2/A3/A4's rosters) + 21 (screened here) = 74 cards, matching `literature/INDEX.md`'s count exactly.** Ten Part-2 cards were flagged by this batch as already fully and correctly engaged in the current draft despite their own card text reading as if the gap were still open (Fortunati & Edwards 2020; Gibbs et al. 2021; Guzman & Lewis 2020; Hancock et al. 2020; Healy & Pekarek 2025; Long & Magerko 2020; Katsh & Rifkin 2001; Wing et al. 2021; Spitzberg 2006; Spitzberg & Cupach 1984) — a useful confirmation that the cards' own "Relation to the argument" notes are stale pointers, consistent with what A1–A4 also found.

### Part 1 — GENUINE GAP, MUST-CITE (5)

| Source | Placement | What it does |
|---|---|---|
| **Simmel (1902) + (1950)** | **Highest priority in this batch.** Two uses: (1) opening of "Extant Constructs"/"Coordination-Form Gap," as the classical warrant that dyad vs. triad is a qualitative structural difference, not an added party; (2) the construct's definitional passage, using Simmel's mediator/arbitrator distinction — the platform resembles an *arbitrator* (decides for two parties) except neither party conferred that authority nor can withdraw it, unlike Simmel's arbitrator | Never cited anywhere despite the paper's entire structural argument (dyad vs. triad, mediator vs. binding third party) building on ground Simmel staked out in 1902/1950. An organization-theory reviewer versed in the classical sociology this journal's tradition draws on (Blau, Coser, Granovetter — already cited) will notice the omission immediately. Engaged-framework treatment, full paragraph, not a footnote. |
| Wall, Stark & Standifer (2001) | "What These Boundaries Share," alongside Katsh & Rifkin/Wing et al. | Precise external formulation of condition (d): mediation is triadic and non-binding, arbitration is binding but consensual and reasoned — the platform gate is binding, non-consensual, and unreasoned, a cell no third-party literature occupies. Stronger than the paper's current "constructs inherit a dyad" framing. |
| Katsh & Rabinovich-Einy (2017), *Digital Justice* | Expand the existing ODR discussion (currently just Katsh & Rifkin 2001 + Wing et al.) | The mature, 16-years-later, closer-fitting statement — "determinations issued at scale by a system, binding on two parties who do not meet, without reasons, with no contest route" is nearly verbatim the paper's own definition. Its absence next to the 2001 book is a real gap. |
| Vuorikari et al. (2022), DigComp 2.2 | Cross-construct synthesis (L157) or the AI Literacy hearing | Independently confirms A1's finding — the EU's flagship decade-long competence framework is conspicuously absent from a rival-construct survey that otherwise reaches for smaller instruments. |
| UNESCO (2024) | Near the Wing(2016)/accountability-withholding passage | Independently confirms A1's finding — UNESCO's "human accountability" competency presumes the professional retains and must actively keep authority over the tool; algorithmacy's premise is that authority has already been ceded structurally, with no regulatory framework restoring it. |

### Part 1 — GENUINE GAP, lower priority (1)
Goffman (1979 + 1981) — animator/author/principal split gives precise vocabulary for the *interpreting* deficit (a platform verdict's principal cannot be identified); the 1981 radio-announcer case is the closest pre-digital analogue to dual-audience encoding. EXPECTED paired, OPTIONAL standalone.

### Part 1 — MARGINAL (1)
Peters (1999) — one sentence only, per its own card's caution: reframes what's withheld as not contact-as-such but *the possibility of ever finding out*, since a verdict arrives shaped like feedback and explains nothing.

### Part 2 — GENUINE GAP (8, screened beyond A2–A4's rosters)

| Source | Verdict | What it does |
|---|---|---|
| **Johnson (2004)** | **MUST-CITE — single sharpest find in this whole batch** | *Communication Theory* has, in fact, theorized competence for a three-party arrangement — but from the structural-hole broker's side. Nobody theorizes the far-side party's competence. A precise, falsifiable, citable formulation of the vacancy claim, arguably sharper than the paper's current statement. Placement: "What These Boundaries Share," alongside the Curchod/Cameron/Healy & Pekarek paragraph — communication theory addressed a three-party arrangement, just from the wrong side. |
| Hymes (1972) | EXPECTED | Direct ancestor of Spitzberg & Cupach (1984), the paper's own named warrant — absent despite that. Placement: "Categorical Delineation," one paragraph tracing the genealogy. |
| Livingstone (2004) | EXPECTED | External, pre-platform precedent for the individualization critique the paper's Propositions 1/3 already make implicitly. Grounds a self-generated caution in established critique rather than leaving it to read as an invented hedge. |
| Obstfeld (2005) | EXPECTED | *Tertius iungens* vocabulary, from the paper's own home journal (ASQ) — platforms self-describe as connective while structurally rewarded for keeping worker and counterpart apart. Also a methodological precedent for an individual-difference scale of a triadic disposition (Appendix C). |
| Burt (1992) | EXPECTED | Structural-hole theory supplies a *mechanism* for why the platform withholds coordination conditions — not oversight, but the third party's advantage consisting precisely in controlling flow/timing between two unconnected parties. Converts a descriptive "withholds conditions" claim into an explained one. |
| Deardorff (2006) | EXPECTED | Field's clearest precedent for a *process-ordered* (not coordinate) competence model — background support for treating the three operations as sequenced rather than flat. |
| Chomsky (1965) | OPTIONAL | Genealogical root beneath the "competence" terminology the paper uses throughout without naming its origin — pairs with the Hymes recommendation as one clause tracing competence/performance → communicative competence → relational competence → algorithmacy. |
| Edwards, Edwards, Spence & Shelton (2014) | OPTIONAL | Taxonomic footnote distinguishing competence-*of*-the-machine vs. competence-*through*-the-machine — one clause. |

### Part 2 — MARGINAL (2)
Buhrmester, Furman, Wittenberg & Reis (1988) — the paper already has this empirical precedent via Zhou et al.'s own discriminant validity data. Caplow (1968) — an interesting stress-test (triads resolve into two-against-one coalitions) but its formalism assumes strategic agents choosing allies, which the algorithm isn't; one sentence at most. Chen & Starosta (2000) — fair self-critical point (algorithmacy's operations are cognitive/behavioral only, missing a dispositional facet) but the citation itself is weakly verified (non-Crossref-indexed journal, flagged by its own card as the cluster's weakest identifier) — verify before using if pursued.

### Part 2 — NOT RELEVANT, already engaged (10)
Fortunati & Edwards (2020); Gibbs et al. (2021); Guzman & Lewis (2020); Hancock et al. (2020); Healy & Pekarek (2025); Long & Magerko (2020); Katsh & Rifkin (2001); Wing et al. (2021); Spitzberg (2006); Spitzberg & Cupach (1984) — all already substantively cited; their cards' "not yet cited" framing is simply stale.

---

## Batch B1 — 2024–2026 CMC/HMC currency sweep

**No candidate cleared the GENUINE GAP bar.** Checked the current tables of contents for both flagship venues a CMC/HMC reviewer would look at first: *Human-Machine Communication*'s current volume (7 articles, every one a dyadic human-AI study) and *JCMC* 31(4) (AI-companion privacy, digital disconnection, and a GenAI-relational-maintenance study whose "friend" never actually participates in the interaction — fails condition (b), no active counterpart). **This is itself a useful finding, not a null result:** the two venues most likely to contain a genuine rival haven't moved past the dyadic frame the paper diagnoses, as of their newest issues. That corroborates the vacancy claim rather than threatening it.

Five external candidates were individually screened and verified via two independent records each; all were ruled NOT RELEVANT or MARGINAL — organizational/collective-capability theory already excluded by the paper's own capability-vs-competency distinction (Stelmaszak, Möhlmann & Sørensen 2024, *MISQ*), low-profile-venue reviews naming a "human-AI-human" configuration where the AI is still a conduit not an evaluator (Afgiansyah et al. 2026), single-user-plus-chatbot conversation analysis with no counterpart (Klowait & Erofeeva 2025), and two sources sitting inside the paper's already-saturated accountability/contestation cluster.

**One low-risk optional addition:** Liu, Liu & Wei (2026), "Thinking, fast, and artificial: processing fluency in AI-mediated relational maintenance planning," *JCMC* 31(4), zmag018 — could support a single sentence like "as recently as 2026, JCMC's own AI-mediated-communication work stays inside the sender/receiver-plus-assistant frame," strengthening the vacancy claim with a citation this current. Not necessary, genuinely optional.

**Caveat on this batch's reliability:** the session's WebSearch and Consensus search budgets were both exhausted before this batch could use them (by prior batches earlier in this pass), and Semantic Scholar was rate-limited throughout. The batch substituted OpenAlex's direct API (worked reliably) and targeted WebFetch to publisher/DOI pages, verifying every candidate via two independent records — but this was narrower than a full WebSearch-driven pass, and CHI 2025/2026 and CSCW 2025/2026 proceedings specifically could not be browsed (ACM DL blocked WebFetch with 403). If higher confidence is wanted, this batch could be re-run once budgets reset — but given how saturated the currently accessible venues already are with dyadic-frame work, this is a low-priority follow-up, not an open exposure.

---

# Synthesis

All 8 wave-1 batches complete; no wave-2 gap-directed search was needed (B1's currency sweep found nothing external the internal library and A2–A5 hadn't already surfaced or exceeded). All 74 communication-competence cards confirmed screened by exactly one batch (A1 + A2's 11 + A3's 18 + A4's 17 + A5's 7+21 = full cluster, cross-confirmed by A5's own coverage count).

## The one decision needed before anything else: does Walther earn an eighth hearing?

**Walther (1992, 1996) — social information processing theory / the hyperpersonal model — is a genuinely close near-miss on the paper's own four-part test, closer than any of the paper's current seven hearings.** It satisfies individual capacity and active/interdependent counterpart as robustly as any existing hearing, and fails only on autonomous-binding-intermediary. A2 spells out the exact risk: a CMC-literate reviewer will very plausibly read the "specifying intent" operation and ask "how is this not Walther's adaptation thesis with an algorithm swapped in?" — a question the paper currently has no answer to on the page, though a clean one exists (Walther's loop closes because the *same* party who receives the message evaluates and replies; in the triad, the party that evaluates is not the party whose understanding matters, and neither returns anything resembling a reply).

**Two options, with real costs, neither decided here:**
- **Option A — new eighth hearing** (~600–900 words): new subsection, new Table 1 row, "seven" → "eight" in the abstract/intro/L52/L167 cross-reference, one added clause at L155.
- **Option B — fold into the existing Spitzberg hearing** (~300–500 words added to L67–77): lower structural cost, no renumbering, but risks blurring two distinct theoretical lineages into one subsection.

This is the single highest-leverage decision in this whole research pass, and it should be made before any integration work starts, since it changes how several other recommendations below get placed.

## If you only have time to add a handful of sources

Five different batches (A2–A5), working independently and blind to each other's conclusions, each singled out one source as the standout finding in their own assigned territory. That convergence is itself a signal — these are the sources most likely to matter to an expert reviewer:

1. **Simmel (1902, 1950)** — A5: "highest priority in this batch." The classical warrant for treating a triad as a different structural form, not a dyad-plus-one — underneath the paper's entire structural argument, and never cited.
2. **Johnson (2004)** — A5: "single sharpest find in Part 2." Communication theory *has* studied a three-party arrangement's competence demands — from the broker's side. Nobody theorizes the far-side party. Sharper than the paper's own current vacancy statement.
3. **Clark & Brennan (1991)**, grounding theory — A2: "arguably the single most theoretically load-bearing item on this list." Explains *why* coorientation collapses (no mutual evidence of uptake is structurally available) — theoretical warrant, not just description, for why the construct splits into separate operations.
4. **Hohenstein et al. (2023)**, *Scientific Reports* — A3: "the single strongest addition in this batch." Direct empirical evidence that a system's involvement in a coordination gets attributed to a party, consequentially, without her being able to contest it — converts the accountability-forfeiture claim from assertion to evidence.
5. **Jablin & Sias (2001)** — A4: "the single most dangerous omission in the batch." Sits on the paper's own home turf (organizational communication); their "assimilation" argument is structurally close to the paper's own acquisition-through-participation property.
6. **Suchman (2007)**, *Human-Machine Reconfigurations* — the deepest available theoretical statement of why the interpretive burden falls entirely on the worker.
7. **Katsh & Rabinovich-Einy (2017)**, *Digital Justice* — the mature, 16-years-later successor to the one ODR source currently cited; comes closer to the paper's own definition than anything else found in this pass.
8. **Walther (1992, 1996)** — pending the structural decision above.

## Full recommendation table (everything GENUINE GAP or MARGINAL, deduplicated across batches)

**Tier MUST-CITE (a CMC/HMC-literate reviewer would likely notice the absence):**
Simmel (1902, 1950); Johnson (2004); Clark & Brennan (1991); Hohenstein et al. (2023); Jablin & Sias (2001); Suchman (2007); Katsh & Rabinovich-Einy (2017); Walther (1992, 1996) [pending structural decision]; Wall, Stark & Standifer (2001); Elish (2019); Daft & Lengel (1986); Daft, Lengel & Trevino (1987); Dennis, Fuller & Valacich (2008); Sundar & Nass (2000); Guzman, McEwen & Jones (2023); Hohenstein & Jung (2020); Sebo et al. (2020); Canale & Swain (1980) + Bachman (1990); Spitzberg (2015); Hannawa & Spitzberg (2015, eds.); Bunz & Montez (2015); Duran (1983); Vuorikari et al. (2022, DigComp 2.2); UNESCO (2024).

**Tier EXPECTED (strengthens a specific point; a reviewer might ask, wouldn't be alarmed by its absence):**
Walther (2007); Biocca, Harms & Burgoon (2003); Nass & Moon (2000); Sundar & Kim (2019); Jakesch et al. (2019); Mieczkowski et al. (2021); Jung, Martelaro & Hinds (2015); Traeger et al. (2020); Seeber et al. (2020); Natale (2021); Wiemann & Backlund (1980); McCroskey (1982); Canary & Spitzberg (1987); Habermas (1970) [anchor only]; Goffman (1979, 1981); Hymes (1972); Livingstone (2004); Obstfeld (2005); Burt (1992); Deardorff (2006); AI-MC/HMC empirical set (Edwards et al. 2014, lowest priority of that cluster).

**Tier OPTIONAL/MARGINAL (name-check level, or genuinely skippable):**
Krämer (2015); Chomsky (1965); Peters (1999); Wiemann (1977); Spitzberg (1983); Rubin (1982); Rubin & Martin (1994); Short, Williams & Christie (1976); Dennis & Valacich (1999); Zhao (2003); Reeves & Nass (1996); Guzman (2018, ed. vol.); Caplow (1968); Chen & Starosta (2000, verification-flagged — confirm before use); Buhrmester et al. (1988); Liu, Liu & Wei (2026, B1's optional currency addition).

**NOT RELEVANT / already covered — no action:** Rubin (1985); Spitzberg (2013); and the 10 cards A5 confirmed already substantively engaged (Fortunati & Edwards 2020; Gibbs et al. 2021; Guzman & Lewis 2020; Hancock et al. 2020; Healy & Pekarek 2025; Long & Magerko 2020; Katsh & Rifkin 2001; Wing et al. 2021; Spitzberg 2006; Spitzberg & Cupach 1984).

## The Manky (2025) empirical gap

Full text not obtained (Wiley embargo, ~12 months post-publication — plausible explanation for why no channel produced it). Two live paths: the drafted-not-sent author email (C1), or Bentley ILL. **A real corroborating source was found and full-text verified**: Oliveira & Junges (2023), Brazilian food-delivery couriers reading platform-relayed address/name data as a safety signal against robbery — same general mechanism (Latin American platform workers reading platform information for physical safety), different specific signal (address pattern vs. rating score). Recommend as a hedging citation alongside Manky if the specific mechanism stays unconfirmed by submission time.

## What this pass did not do

No `PAPER.md` edits. No card edits. This is a recommendations report; integration is separate follow-on composition work, and the volume of MUST-CITE items above (23) is almost certainly more than fits in an 11-day window even generously — the shortlist above is offered as a starting cut, not a mandate to add all 23.

