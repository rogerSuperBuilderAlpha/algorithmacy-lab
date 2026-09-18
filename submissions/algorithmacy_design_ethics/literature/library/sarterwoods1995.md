# Sarter, N. B., & Woods, D. D. (1995). How in the world did we ever get into that mode? Mode error and awareness in supervisory control. *Human Factors*, 37(1), 5–19.

**Identifier:** doi:10.1518/001872095779049516 · **Read depth:** abstract_only (verbatim abstract from the Consensus/Semantic Scholar index; article paywalled at SAGE; not among the PDFs archived from Woods's CSEL site) plus a secondary summary (Resilience Roundup newsletter page, unverified against the paper) and the authors' own restatements in Christoffersen & Woods (2002) and Klein et al. (2004), both read in full · **Source-tier:** peer-reviewed, flagship HF journal; conceptual synthesis of the authors' field and simulator studies · **Evidence basis:** secondary · **Parties modeled:** human–technology (flight crew and cockpit automation) · **Relation last checked:** 2026-09-18

## What it argues

The abstract: new technology "provides practitioners with a large number of functions and options," but "this flexibility has a price. Because the human supervisor must select the mode best suited to a particular situation, he or she must know more than before about system operations... as well as satisfy new monitoring and attentional demands to track which mode the automation is in and what it is doing to manage the underlying processes. When designers proliferate modes without supporting these new cognitive demands, new mode-related error forms and failure paths can result." Mode error had been a human–computer-interaction concept; "the increased capabilities and the high level of autonomy of new automated systems appear to have created new types of mode-related problems," and the paper draws on "a series of studies of pilot-automation interaction in commercial glass cockpit aircraft" to give "an expanded view of mode error that takes into account the new demands imposed by more automated systems." The secondary summary reports the simulator study behind it as 20 pilots, with 65% unaware in an aborted-takeoff scenario that the automation still controlled thrust, 15% able to describe the active mode and its settings, and 4 of 20 managing the automation correctly, plus the Indian Airlines 605 "open descent" case in which five different routes activated the mode; treat those figures as unverified until checked against the paper. The authors' later gloss (Klein et al. 2004, p. 93) is Wiener's trio: pilots "wondering what the automation is currently doing, why it's doing that, and what it will do next."

## Relation to the argument

Structural axis, and the classic statement of the interpretive burden that the construct's "infer what the intermediary is doing" inherits: the operator must reconstruct the automation's state from its behaviour because the automation does not announce it, and mode changes can be triggered indirectly rather than by the operator's own input. On this pass's question: a crew of two shares one automation, and the secondary summary notes that mode transitions can be caused by "other users' actions" — the second pilot is a source of uncommanded mode change, which is the nearest the classic corpus comes to an automation that has taken input from someone other than the person now reading it. But that second pilot is same-side, shares the goal, and could speak directly; the direct channel survives and the structure is a crew–automation dyad over one aircraft. No counterpart party and no external objective appear.

## Caution

Abstract-only for the paper itself; the numbers above come from a newsletter summary and the underlying simulator study is Sarter and Woods (1994), not this paper, so the attribution is doubly indirect. The setting is the Boeing 737-300 / A320 glass cockpit of the early 1990s. Mode error is a design critique of feedback, not a claim about the automation's objective.

---

## S2 adversarial verification (2026-09-18)

**Verdict:** confirmed

**What I checked:** Re-fetched the abstract from the Consensus index (DOI 10.1518/001872095779049516) and compared it word for word with the card; the article itself was not opened (SAGE returns 403; no PubMed record).

**Findings:** Abstract quotations are verbatim; the card's ellipsis covers "and the operation of the system". The 20-pilot / 65% / 15% / 4-of-20 figures come from a newsletter and remain unverified, as the card already states. The Relation section stays inside what the abstract supports.

---

## Relation to Principle III — bounded outputs, not mechanistic interpretability (cluster F pass, 2026-09-18)

**Remedy locus:** artifact (design the automation so its modes and transitions are visible and few).

This card carries the single most load-bearing distinction for Principle III, and it should be stated without hedging: **the operator needs to know what regime the automation is in, not how it computes inside it.** The abstract's own terms are exact. The supervisor "must know more than before about system operations ... as well as satisfy new monitoring and attentional demands to track *which mode the automation is in and what it is doing* to manage the underlying processes," and the failures come "when designers proliferate modes without supporting these new cognitive demands." Mode error is not, on the abstract's account, a failure to understand the autopilot's control law; the abstract locates the new demand in tracking "which mode the automation is in and what it is doing," while also saying the supervisor "must know more than before about system operations" — so the underlying studies do report knowledge gaps about mode behaviour as well as awareness failures, and this card, read only in abstract, cannot say how the two divide. What it can say is that the failure the authors name is a failure to know *which* mode is active and how it was entered — Wiener's trio, in the authors' later gloss, of "wondering what the automation is currently doing, why it's doing that, and what it will do next." Every term there is behavioural: current regime, cause of the transition, next behaviour. None asks for the internals. That is Principle III's positive content in human-factors vocabulary: a mediator should have few regimes, should announce which it is in, should not change regime on inputs the party cannot see (the second pilot's uncommanded mode change is the cockpit's version of the counterpart's action re-setting the mediator), and its outputs within a regime should be bounded so that "what it will do next" is answerable. Mechanistic interpretability answers a question no pilot asked. The engineering vocabulary for the same distinction is the operational design domain (SAE 2021, clause 3.21): the driver needs the ODD and the fallback regime, not the perception stack. Leveson (2011) supplies the design rationale — a declared regime with bounded outputs is a passive control, mode-tracking by the human an active one with "greatly increased" failure modes — and Chen, Zaharia and Zou (2024) supply the platform-era case, a service whose regime changed between March and June without a mode annunciator. The paper should carry two cautions from this card: the paper itself was read only in abstract, so the distinction rests on the abstract and on the authors' restatements in Christoffersen & Woods (2002) and Klein et al. (2004); and the crew is a same-side dyad over one aircraft, so "which regime" in the triad has to include regimes the other party's inputs select.


---

## S2 adversarial verification (2026-09-18, pivot round)

**Verdict:** corrected

**What I checked:** New-material only (the Principle III section). The card is abstract-only and the article is still paywalled; checked the section's claims against the S2-verified abstract and its cross-references against sae2021j3016.md (clause 3.21), leveson2011.md ("greatly increased") and chen2024.md (March-to-June drift).

**Findings:** One overreach fixed. The section asserted that "the pilots in the underlying studies understood perfectly well what each mode does," which an abstract-only read cannot support and which the abstract's own clause that the supervisor "must know more than before about system operations" cuts against (the underlying Sarter and Woods studies report gaps in pilots' knowledge of mode behaviour as well as awareness failures). The sentence now states what the abstract locates the new demand in, concedes that knowledge gaps are part of the picture, and confines the regime/internals distinction to what the authors name. The abstract quotations are verbatim; the three cross-references are supported by the sister cards; the section's own two cautions (abstract-only; same-side dyad) stand.
