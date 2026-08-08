# Deep research prompts — round 2

Eight prompts, ordered by critical path. Each one is written to be run as-is by a research agent or
a human with database access, and each returns the same artefact: verified citations with a stated
relation to a named section of [`../manuscript/OUTLINE.md`](../manuscript/OUTLINE.md).

Rounds 1a (dissertation library), 1b (chapter pass), and 1c (guest-side acquisition) are recorded in
[`FOUNDATION.md`](FOUNDATION.md). This round goes after what those left thin.

---

## Rules that apply to every prompt

**Venue discipline.** Preferred venues, in order: *Hospitality & Society*; *International Journal of
Hospitality Management*; *Tourism Management*; *Annals of Tourism Research*; *International Journal
of Contemporary Hospitality Management*; *Journal of Hospitality Marketing & Management*; *Tourist
Studies*; *Journal of Sustainable Tourism*. Then top organization, information-systems, and HCI
venues where the hospitality literature is genuinely silent. **Reject** pay-to-publish and
unindexed outlets outright — round 1c surfaced several on a personalization search and stocked none
of them. Returning nothing beats returning those.

**Verification is not optional.** Every returned citation carries author list, exact title, journal,
volume, issue, pages, year, and DOI, each checked against the publisher record or Crossref
(`https://api.crossref.org/works/{DOI}`). Web-search summaries are leads, never sources: round 1c
found a search summary crediting a paper to the wrong two authors. State the read depth reached —
full text, abstract, or metadata only — and never assert a specific claim from an abstract alone.

**Report the misses.** Close every run with what was searched and *not* found. A named absence is a
finding this paper can use; silence reads as coverage that was never achieved.

**Distinguish evidence from framing.** For each source say whether it supplies (a) evidence the paper
can lean on, (b) a framing the paper argues past, or (c) both. Round 1c's biometric check-in sources
were most valuable as (c), and that only became visible because the question was asked.

**Length discipline.** The manuscript is 7,600 words against an 8,000 ceiling. Ten superb sources per
prompt beat forty adequate ones. Rank by load-bearing value, not recall.

---

## P1 — Hospitality's own theorizing line *(blocking; §2, 950 words)*

> The paper must ground itself in hospitality social science before it critiques phygital design, and
> §2 is the section a domain reviewer reads first. Find the hospitality-theory scholarship on
> **host–guest power, the cultural scripts that govern welcome, and the distinction between
> commercial hospitality and hospitality as a social and moral practice.**
>
> Already held: Lynch et al. (2021) *H&S* ten-year theorizing audit; Lugosi (2021) *Tourist Studies*;
> Lashley (2000) three domains; Derrida and Dufourmantelle (2000).
>
> Go after: the *Hospitality & Society* theorizing line since 2011 — including the journal's own
> founding statements and any reprise or reply pieces; hospitableness as a construct and its
> measurement; the critical-hospitality-studies engagement with Derrida, Kant, and the ethics of
> unconditional welcome as taken up **by hospitality scholars rather than philosophers**; work on the
> host's authority over the threshold and the guest's obligations; cultural variation in what counts
> as welcome.
>
> The specific claim §2 must support: hospitality has always specified something that flows back to
> the guest — recognition, care, negotiated access — and that return is constitutive of the practice
> rather than a service enhancement. Find the sources that establish it in the field's own voice.
>
> Return 8–12 sources ranked by how directly they let this paper speak the journal's native
> vocabulary. Flag any that are themselves special-issue or editorial pieces in *H&S*, since citing
> the journal's own theorizing signals fit.

## P2 — Algorithmic management inside hospitality operations *(blocking; §3, 1,050 words)*

> The framework treats employee discretion as co-equal with guest agency, and the CFP explicitly
> invites "power structures and guest-staff relationships." The evidence currently comes from
> ride-hail, freelancing, journalism, and short-term rental. **The employee half argues by analogy
> and needs hospitality-native grounding.**
>
> Find empirical work on algorithmic direction of hotel and restaurant frontline work: property
> management systems and CRM-driven task allocation; revenue-management systems and the opacity of
> their pricing decisions to the staff who must explain them to guests; algorithmic and
> just-in-time scheduling in hotels; housekeeping quota and productivity tracking; performance
> scoring built from guest reviews; automated upsell and upgrade prompts that constrain what a
> front-desk agent may offer.
>
> Already held: Möhlmann et al. (2021) *MISQ*; Rahman (2021) *ASQ*; Christin (2017); Lipsky (1980);
> Cheng and Foley (2019) *IJHM* on Airbnb hosts.
>
> The claim §3 must support: algorithmic systems relocate the categories of judgement out of the
> frontline employee's discretion and into a system the employee can neither see nor overrule — and
> this happens in hotels, not only on platforms.
>
> Return 8–12 sources. Mark clearly which are hospitality-sector and which are adjacent service
> sectors; if the hospitality-native evidence genuinely does not exist, say so plainly, because a
> stated absence is itself citable and would reshape §3's claim from *documented* to *predicted*.

## P3 — Cultural variation and categorical exclusion in algorithmic welcome *(§7, and CFP aim 3)*

> The CFP asks for work on "inclusive and culturally sensitive design" and "socio-cultural dynamics."
> The paper claims that guests whose needs fall outside algorithmically constructed norms lose the
> surface on which to be received as exceptions. **That claim currently rests on general
> classification theory, not on hospitality or cross-cultural evidence.**
>
> Find: cross-cultural work on service and hospitality expectations under standardized or automated
> systems; studies of guests whose requirements do not fit standard categories — disability and
> accessibility needs, religious and dietary requirements, family and kinship arrangements that
> booking systems do not model, name and identity mismatches at check-in; research on how
> personalization systems handle atypical guests; language and interface access as a condition of
> welcome.
>
> Already held: Bowker and Star (1999) on *torque*; Fourcade and Healy (2013); Cheney-Lippold (2011);
> Lyon (2003); Edelman et al. (2017); Cui et al. (2020).
>
> The test for a strong hit: does the source show a real guest meeting a category that does not fit
> them, and what happened next? Conceptual pieces about inclusive design are weaker than one
> documented mismatch.
>
> Return 6–10 sources. Note explicitly whether accessible-tourism scholarship engages algorithmic
> mediation at all, or treats technology only as an accessibility aid — that distinction decides
> whether the paper cites it as support or as a gap.

## P4 — What contestation looks like when it works *(§6, 1,250 words)*

> §6 currently rests on three published nulls: Ananny and Crawford (2018) on transparency without a
> forum, Vaccaro et al. (2020) on the internal appeal that moved nothing, Edwards and Veale (2017) on
> the transparency fallacy. **A design section that only reports failures cannot make a design
> recommendation.**
>
> Find the positive cases. Where has contestation of an algorithmic decision actually delivered
> standing to the party contesting it, and what structural feature made the difference? Look for:
> external and independent review bodies, including certified out-of-court dispute settlement under
> the EU Digital Services Act Article 21 and comparable regimes; ombuds and ADR schemes in consumer
> services; regulatory or statutory appeal that binds the rule-writer; empirical evaluations of
> contestable-by-design systems in the field rather than in the lab; sectoral analogues in
> travel — airline denied-boarding compensation regimes, hotel overbooking and walk protections,
> OTA dispute processes.
>
> Already held: Alfrink et al. (2023); Almada (2019); Citron and Pasquale (2014).
>
> The structural question to answer: the dissertation this paper draws on derives that accountability
> is a relation between parties rather than a state a party can be in, so no individual competence
> manufactures a forum. **Which institutional arrangements have actually constituted the forum, and
> what did they require?** That answer is what §6's contestability affordance should specify.
>
> Return 8–12 sources, and separate legal-instrument descriptions from evaluations of whether the
> instrument worked.

## P5 — Friction as a design value *(§7, 650 words)*

> §7 argues that a frictionless encounter can be less hospitable. It has Chalmers and Galani (2004)
> on seams, Star and Ruhleder (1996) on infrastructure becoming effective as it sinks out of sight,
> and Folger (1977) on voice reducing experienced injustice independently of outcome. **It needs the
> line of work that treats friction as something a designer adds on purpose.**
>
> Find: deliberate friction, microboundaries, and speed bumps in interaction design; seamful design
> after Chalmers; "slow technology" and reflective design; friction in consumer and service settings
> where effort produces meaning, value, or commitment; any hospitality or service-design work
> arguing that effort or waiting is constitutive of the experience rather than a defect.
>
> The claim §7 must support: removing the surface on which negotiation happens removes something the
> encounter needed, and this is a design position with a lineage — not a complaint about technology.
>
> Return 6–10 sources. Note which come from HCI and which from service or consumer research; §7
> reads better if the argument can be made at least partly in the target field's own literature.

## P6 — PH-CX and PSR, read closely enough to complement rather than restate *(§3)*

> The special issue is guest-edited by the author of both frameworks the CFP builds on, and this
> paper positions itself alongside them. **Restating experience design in mediation vocabulary would
> be the fastest route to rejection.**
>
> Read closely: Batat (2024) PH-CX in *Journal of Strategic Marketing*; Batat (2024) guest editorial
> on the phygital research paradigm in *Qualitative Market Research*; Batat (2026) phygital service
> research in *Journal of Services Marketing*. Extract each framework's actual components — PH-CX's
> driving forces, connectors, and pillars; PSR's relation to FSR and TSR; the human-first
> commitments each states.
>
> Then answer three questions precisely. What does each framework already say about power, agency,
> and who decides? Where does the mediation argument add something the framework does not contain
> rather than renaming what it does? And what is the most generous accurate statement of the
> relationship — extension, complement, or friendly critique?
>
> Also survey work applying or extending PH-CX and PSR since 2024, to see whether the mediation
> question has been taken up already.
>
> Return a positioning memo of roughly 800 words plus a citation list, not a source dump. The output
> §3 needs is two or three sentences that place this paper against Batat's frameworks accurately and
> without deference.

## P7 — Belonging, trust, and well-being as outcomes the affordances claim to move *(§6, §8)*

> The abstract states that the five affordances "influence whether algorithmic mediation strengthens
> or weakens guest agency, employee discretion, interpersonal recognition, belonging, trust, and
> well-being." **Seven outcome variables are asserted and none is currently sourced.** A reviewer in
> a service-research-adjacent field will notice.
>
> For each of belonging, trust, and well-being, find the hospitality and service literature that
> establishes it as a studied outcome of the service encounter, and any work connecting it to
> technological mediation, automation, or reduced human contact.
>
> Then answer the harder question: **which of these seven can the paper responsibly claim to affect,
> and which should be softened to plausible mechanisms rather than stated influences?** A conceptual
> paper may propose relationships, but it should not imply established ones.
>
> Return 8–12 sources plus an explicit recommendation on the abstract's claim, including which terms
> should stay and which should be marked as propositions for future research. Note that the abstract
> is a co-author's locked text, so the recommendation is advisory.

## P8 — Employee voice in hospitality, specifically *(§3, §5)*

> Coordinative sovereignty rests on voice, and the current apparatus is general: Hirschman (1970),
> Dowding et al. (2000), Morrison (2014) on employee voice and silence, Folger (1977). **None is
> hospitality-native, and hospitality has its own labour conditions — high turnover, seasonal and
> migrant workforces, tipping, and a service culture that scripts deference to guests.**
>
> Find: employee voice and silence in hotels and restaurants; the effect of guest-review-based
> evaluation on what frontline staff will say; whether hospitality's service scripts suppress voice
> independently of any algorithm; work on migrant and precarious hospitality labour and its access to
> grievance channels.
>
> The claim §5 must support: withholding voice is a harm in its own right, and hospitality's
> employment conditions may already withhold it before any algorithm arrives — which would mean
> algorithmic mediation compounds an existing condition rather than creating a new one. **If that is
> what the literature shows, it is a stronger and more honest claim than the one the paper currently
> makes.**
>
> Return 8–12 sources, and state clearly whether the compounding reading is supported, unsupported,
> or untested.

---

## Sequencing

P1 and P2 gate drafting: §2 and §3 are the first two sections written, and both currently lack
domain grounding. Run them first and in parallel.

P4, P6, and P7 gate specific sections but not the schedule — they can run while §2 and §3 are being
written, since each feeds a later section.

P3, P5, and P8 sharpen the argument and are the first candidates to drop if time runs short. Dropping
them costs depth, not correctness, provided the manuscript states what it did not survey.

## Output convention

Every run must:

1. **Add or update a card** in [`../library/cards/`](../library/cards/) for every source it touched —
   admitted, held or rejected — with a fresh `generated_run`. A rejected candidate gets a card and a
   `rejected_reason`; that is how the reasoning survives.
2. **Flip displaced sources to `superseded`** with `superseded_by` set, rather than deleting them.
3. **Add verified entries** to [`references.bib`](references.bib) with `note = {verified <date>}`.
4. **Append a numbered part** to [`FOUNDATION.md`](FOUNDATION.md) that cites citekeys.
5. **Run `python3 ../library/build_index.py`** and commit the regenerated index.

Steps 1, 2, 3 and 5 are enforced by `build_index.py --check` in CI. Step 4 is narrative and is not
enforced, which is acceptable now that it is no longer the only record of anything.

This convention replaces an earlier one that asked a run to update `field_map.md` by hand. Two rounds
skipped it and the map went stale, which is why cluster state is now computed rather than asserted. A
run that finds nothing still writes the absence — into a card if it concerns a source, into
[`../library/VENUE_RULINGS.md`](../library/VENUE_RULINGS.md) if it concerns an outlet.
