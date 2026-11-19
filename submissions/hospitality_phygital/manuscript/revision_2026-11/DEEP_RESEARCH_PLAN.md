<!-- Drafted by Claude (Opus 5.5) on 10 Nov 2026 for Roger and Pierre, from the full reviews (manuscript/reviews/journal_2026-11/REVIEWS_FULL.md) and the Fable review (research/FABLE_REVIEW_2026-11-10.md). A plan for the authors to change, not a decision. -->

# Deep research plan: the duties of the host

10 November 2026 · resubmission due 14 December 2026

## Why this plan replaces part of RESEARCH_PLAN.md

`RESEARCH_PLAN.md` (8 Nov) was built from the editor's summary of Reviewers 2 and 3. The full reviews ask for more:

- **Reviewer 2** wants a theory of role obligation in commercial hospitality. It should say what activates the obligation, who first bears it, what can and cannot be delegated, and how it is shared among hotel company, operator, employee, platform and vendor. Reviewer 2 also wants to know what makes hospitality different from banking or healthcare.
- **Reviewer 3** says the paper equates hosting with the reception desk, treats authority as absolute, and treats the welcome as "a single duty" cut off from its social and organisational context.

All of this points at one weakness: the host's first-order duty to the guest is assumed, not built. The paper sources the duty to *answer* after delegation (Kong, Kropf et al., Nissenbaum). The duty to *host* rests on one secondary quotation (King 1995, cited by Xiang et al. 2022) and on Lashley 2000, which the library holds at metadata depth only.

Two changes to the 8 Nov plan:

1. **Drop its exclusion rule.** It kept out "liability-allocation papers without a theory of the duty's origin". Reviewer 2 now asks for exactly that allocation.
2. **Add three traditions the library lacks entirely:**
   - innkeeper and public-calling law;
   - role-obligation theory;
   - the allocation of duties across several firms.

## The core question

> What is the commercial host obliged to do for the guest? What brings that obligation into force, who holds it, and which parts can be handed to an employee, a contractor or a system?

The answer has to say what is specific to hospitality. It also has to work beyond the hotel front desk.

## Workstreams

The ten research questions come from the Fable review, §7. Priority A is the host-duty foundation and runs first. Priority B covers the rest of the reviewers' asks.

### H1 · Where the host's obligation comes from (A)
**Questions 1, 4, 5.** Reviewer points R2.1, R2.2a–b, R2.4, R3.11. Outline §2.1 and §2.3.

The H1 file holds the deliverable, the search plan, the include/exclude rules and the leads for this workstream. The other workstreams follow the same pattern.

- **Innkeeper and common-calling law (UK and US).**
  - What brings the duty into force: holding out to the public, admission, arrival.
  - What the duty contains: the duty to receive, safety, care of goods.
  - Who holds it.
  - Modern public-accommodation law.
  - Has hospitality scholarship used this doctrine? A first check suggests not.
- **The hospitableness literature.** Is the host's duty treated as a personal virtue or as the obligation of a role or organisation? How does this literature reconcile it with commerce? Sources: Telfer; King 1995; Lashley 2000 read in full; Brotherton; O'Gorman.
- **Comparison with other services.** Do banks, hospitals and retailers already carry duties that apply before any harm, and can they make negotiated exceptions? If they do, what is left that is distinctive of hosting?
- **Search tools:** Consensus, Scholar Gateway, OpenAlex, and legal-history sources found through the web. Every case and statute needs a primary citation.

### H2 · What can be delegated, and standing without circularity (A)
**Questions 2 and 10.** Reviewer points R2.2c, R2.1b, R2.3. Outline §2.2, §2.4, §3 and Table 1 in §5.

- **Role obligation.**
  - Hart, *Punishment and Responsibility*, on role-responsibility (unread; needs a read with page locators).
  - Hardimon (1994) on role obligations.
  - Vincent on the many senses of responsibility.
  - Each could give a principled answer to "what cannot be delegated".
- **Non-delegable duties in tort**, especially an occupier's or innkeeper's duty that stays put when a contractor does the work. This is the closest legal parallel to the paper's claim, so it needs to be tested against Kong's control-based account.
- **Directed duties** (Darwall, read alongside the newer literature on directed obligation). How do they separate three things: the first-order duty, the obligee's standing, and accountability for breach? The aim is to define standing without reference to answering. That removes the circularity Reviewer 2 found.

### H3 · Who the host is when several firms share the job (B)
**Questions 3 and 8.** Reviewer points R2.1e, R2.2d, R3.8, R2.5b. Outline §2.1, §4 and §9.

- **How guest-facing duties are split** among owner, brand or franchisor, management company, employee, booking platform and technology vendor. Sources: hospitality management contracts, platform terms, and the "many hands" literature.
- **Which party holds itself out as host.** This links back to H1's holding-out trigger.
- **Hosting beyond the hotel desk:** restaurants, bars, events, short-term rentals, and unstaffed or app-only hotels. Who is treated as host in each, and where does the role thin out?

### H4 · What guests owe; negotiation and bounded authority (B)
**Questions 6 and 7.** Reviewer points R1.2, R3.9, R3.10, R2.3. Outline §3 and §4.

- **Reciprocal duties of guests**, and when a guest loses the claim to be received or heard. Sources: Pitt-Rivers' "law of hospitality", Shryock, Candea and da Col, and innkeeper law's grounds for refusing a guest.
- **Host–guest negotiation**, which is Reviewer 1's request. Empirical studies of hotels, restaurants and bars where a guest's request changed the outcome, and of the limits organisations place on frontline authority.
- **Library material not yet used:**
  - Golubovskaya et al. (pp. 1286, 1297);
  - Beatty et al. (p. 167);
  - Slattery (pp. 24–25);
  - Shryock on bad guests;
  - Di Domenico and Lynch. Their host had full authority and was present, yet guests still stayed silent. That complicates the paper's "address" thesis and has to be faced.

### H5 · Which decisions need immediate recourse (B)
**Question 9.** Reviewer points R2.5a, R3.7. Outline §5, §7 and §9.

- **Typologies of automated decisions** by stakes, reversibility and time-criticality.
- **Which decisions need a reachable person at the moment of decision**, and which can wait for a later appeal. This becomes the paper's set of boundary conditions.

## Method and guards

These follow the 27 Oct rule for research runs:

- **Search.**
  - Every candidate work gets a Crossref or OpenAlex record before it gets a card.
  - Everything the Fable review lists is an unverified lead until checked; it tags 66 of them.
- **Read.**
  - Priority-A sources are read in full, with page locators.
  - Nothing is cited from memory or from someone else's quotation. Lashley is the current example: the library knows that sentence only through Slattery.
- **Cards.** Every new source gets a card in `library/cards/`, and then `build_index.py` is run.
- **Verify.**
  - A verifier pass checks every quotation and locator against the source.
  - Fable then reads the priority-A cards by hand, as in the earlier fable_3 and fable_4 passes.
- **Budget.**
  - The reference list must still shrink by about 40 entries net, so each workstream gets a limit:

    | Workstream | Most new sources it can add |
    |---|---|
    | H1 | 4 |
    | H2 | 3 |
    | H3 | 2 |
    | H4 | 2 |
    | H5 | 1 |

  - Anything over its limit has to replace a source already cited.
- **Output per workstream:** a synthesis of one to two pages (`research/WS_H1_….md` and so on). Each claim gets a locator, and the synthesis ends by saying which reviewer points it answers.

## Timeline

| Dates | Work |
|---|---|
| 11–12 Nov | H1 and H2 searches; records for every lead; order PDFs (add to `PAPERS_TO_GET.md`) |
| 13–18 Nov | H1 and H2 full reads and cards; H3, H4 and H5 searches run alongside |
| 19–20 Nov | H3, H4 and H5 reads and cards; verifier pass; Fable hand-check |
| 21 Nov | **Synthesis memo, "The duties of the host":** the literature map and the three candidate positions, now with evidence behind them |
| 22–23 Nov | **Authors decide the position** and revise the pitch in their own words |
| 24 Nov – 7 Dec | Redraft (later than the 20 Nov start in the old plan) |
| 8–14 Dec | Response letter, read-aloud, submission |

This compresses drafting by four days. The alternative is to cut H5 to a paragraph and fold H3 into H1.

## Decisions for the authors

1. **The position.** The Fable review §5 sets out three:
   - **threshold sovereignty**, which is the current position;
   - **public calling**, which grounds the duty in innkeeper law;
   - **institutional role obligation.**

   Fable recommends using role obligation as the frame, public calling as its evidence, and threshold sovereignty as description. The research above is designed to test all three, so the choice can wait until 21 Nov.
2. **Figure 1.** Reviewer 2 refers to a "Figure 1" that does not appear in `DRAFT.md` or in the 8 Nov copy of the submitted text. Check the Word file that was actually submitted.
3. **Word budget.** The journal's limit is 9,000 words. The new §2 theory, boundary conditions and agenda that the reviewers ask for need room, so decide what gets cut.
4. **Reviewer 3's comment on AI assistance and style.** The current outline keeps the epigrammatic register that Reviewer 3 objected to. Your own read-aloud should settle this, not another AI pass.
