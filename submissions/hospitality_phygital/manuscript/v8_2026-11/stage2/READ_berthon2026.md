<!-- DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026, as a v8 Stage 2 reader. Every quotation is verbatim from the version of record with its printed page. My interpretation is marked "My reading". Items marked YOURS wait for the authors. -->

# Reading report: Berthon et al. (2026), 'Access and Ownership in the Phygital'

Berthon, P., Lim, W. M., Pizzichini, L., Raquel, S., Rindfleisch, A. and Soon, P.-S. (2026), 'Access and Ownership in the Phygital: Toward a Phygital–Accesship Typology with Implications for Consumer Well-being', *Journal of Macromarketing*, 46:3, pp. 408–425, doi 10.1177/02761467251413156. Open access, CC BY-NC 4.0.

I read all 18 pages (printed pp. 408–425, references and biographies included) from `manuscript/revision_2026-11/research/sources/berthon2026accesship/vor.pdf`, column by column from a per-page extraction, because the `-layout` text interleaves the columns. I then ran a word-boundary term search over all 18 pages. A script checked every quotation in the card against the article text; all are verbatim. The card is `library/cards/berthon2026accesship.md` (status held, flag `co-author-self-citation`).

## For the authors first

1. **Anonymity. YOURS.** Pierre Berthon is this article's first and corresponding author (p. 408) and a co-author of the submission. `JOURNAL_SPEC.md` records the journal's rule: "Strict anonymity is accorded to both contributors and referees". Two facts on p. 420 sharpen the question. The article "was conducted as part of the American Phygital Association Summit 2025", and its Associate Editor was Wided Batat, lead editor of this special issue. A third-person citation does not name the submission's authors. Leaning on the coinage 'accesship' or the Streams/Tokens/Lends/Keeps labels could still point a summit attendee toward them. The 2026-08-09 precedent in `manuscript/NOTES.md` (an Algorithmacy Lab source marked DO-NOT-CITE as deanonymizing) concerned an unpublished, unretrievable source. It does not settle a published, open-access article. Whether to cite this article, and how, is your call. I have not decided it.
2. **The validator rejects the flag the brief specified.** `build_index.py` lists the allowed flags as `do-not-cite`, `must-engage`, `abstract-only-debt`, `swap-candidate`, `no-retained-copy` and `claim-contradicted`. `--check` therefore fails this card on `flag 'co-author-self-citation'`. The fix is one word added to `FLAGS` (line 40). Making that change was outside my brief, so I left it.
3. **The article's Batat citation.** It quotes Batat's phygital definition as "Batat (2024b) ... (p. 10)" (p. 411). The words are on printed p. 1229 of the PH-CX article in *Journal of Strategic Marketing* 32:8, pp. 1220–1243, its tenth page; I checked the library's copy. Its 2024a/2024b labels are the reverse of ours: its 2024b is our `batat2024phcx` (rendered 2024a). If v8 uses the definition, cite `batat2024phcx` at p. 1229 directly.
4. **Not committed.** The repository's CLAUDE.md asks agents to commit and push after each step. The brief said not to, and I followed the brief. Both files are uncommitted.

## Q1. Definitions and the typology

**Phygital.** The article treats phygital as the *type* of a solution and coins accesship for its *mode*: "phygital focuses on the nature (type) of a solution (Lim, 2026a) while accesship focuses on the nature (mode) of acquisition (Pierce et al., 2003)" (p. 408). It works with dominance rather than pure types: "phygital denotes hybrid composition, yet hybrid solutions vary in which (dominant) element delivers the core value at entry, thus we use digital-dominant versus physical-dominant as shorthand for relative dominance" (pp. 408–409). The definition it adopts is Batat's: a phygital solution "integrates a combination of physical, human, digital and media content elements, platforms, technologies, and extended realities" (p. 411). It glosses that as "In essence, phygital solutions fuse the tangible (physical) and the intangible (digital) to create hybrid consumption experiences (Batat & Hammedi, 2023; Lim, 2026a)" (p. 411). The conclusion restates it as "the continuum from physical to digital, including hybrid arrangements" (p. 420).

**Access and ownership.** "Ownership typically implies a long-term, even permanent, time horizon and provides both functional and symbolic benefits, whereas access is more temporary and primarily provides functional benefits" (p. 410). "Ownership also confers a more complete bundle of property rights, including control, customization, transferability, and responsibility for risk, whereas access arrangements restrict rights but reduce maintenance burdens and financial commitments" (p. 410). Table 1 (p. 412) sets the contrast on four dimensions: "Time-bound rights and journey structure", "Responsibility and maintenance", "Transferability and legal rights" and "Cost structure".

**Accesship.** "We define accesship as the access–ownership structure through which a solution is acquired and governed over time, ranging from temporary, contract-based use rights (e.g., memberships, rentals, subscriptions) at the one end to permanent legal ownership at the other end, with hybrid arrangements in between." (p. 411). "Hence, accesship is orthogonal to phygital: a digital good can be owned permanently (e.g., a non-fungible token (NFT) or purchased e-book) and a physical good can be temporarily accessed (e.g., a leased vehicle or rented apparel)." (p. 411).

**The typology (PAT).** It is a 2 × 2: "the two rows of this typology represent the type of solution (i.e., digital-dominant versus physical-dominant) while the two columns represent its mode of acquisition (i.e., access-dominant versus ownership-dominant)" (p. 412). "The four quadrants should be viewed as anchor configurations rather than pure categories. Classification is based on the solution’s dominant core at entry" (p. 412). The cells, from Table 2 (p. 413):

| | Access-dominant | Ownership-dominant |
|---|---|---|
| Digital-dominant | **Streams**: "Solutions anchored in temporary digital access, where continued participation progressively unlocks additional benefits over time" (music streaming) | **Tokens**: "Solutions anchored in permanent digital ownership, where owning the digital asset enables sequenced digital enrichment over time" (a Bandcamp album) |
| Physical-dominant | **Lends**: "Solutions anchored in temporary physical access, where the time-limited use experience is extended through integrated (digital) complements during the access period" (a library vinyl record) | **Keeps**: "Solutions anchored in permanent physical ownership, where (digital) complements enhance the owned object’s core value proposition (e.g., functionality and longevity)" (a turntable) |

Every cell is a 'sequenced solution': "intentionally designed customer journeys that deliver value in staged phases, with later phases contingent on earlier adoption or continued participation" (note 1, p. 420).

## Q2. Consumer well-being

**Definition and gap.** "Within macromarketing, consumer well-being is conceptualized as (dis)satisfaction arising from aggregate consumption experiences across acquisition, possession, consumption, maintenance, and disposal" (p. 410). The article's own gap is that "the phygital literature has remained largely silent about these implications", meaning the harms of digital and physical solutions (p. 409).

**Mechanisms and propositions.** Materialism, need for touch and psychological ownership "yield competing predictions" (p. 414). Under materialism, digital-dominant (P1, p. 414) and access-dominant (P4, p. 415) solutions "are more likely to support consumer well-being". Under need for touch and psychological ownership, physical-dominant (P2, p. 415) and ownership-dominant (P5, p. 415) solutions do. P3 (p. 415) and P6 (p. 416) predict "higher levels of acquisition satisfaction, lower levels of possession satisfaction, and little relationship with maintenance or disposal satisfaction" for digital-dominant and access-dominant solutions. Satisfaction is the stated "proxy of consumer well-being" (Table 3, p. 414).

**Harms.** These are lock-ins and opaque costs (p. 416), and loss of "continued access when a service is discontinued or a license is revoked" (p. 417). The article also names "hidden (and often recurring) costs and subscription lock-ins that disproportionately burden low-income or digitally vulnerable users" (p. 417). The gap between psychological and legal ownership, it says, "represents a grey zone that may increase consumer vulnerability and potentially lead to consumer exploitation" (p. 419).

**Prescriptions to firms.** "These two dimensions represent strategic levers that firms can pull" (p. 416). Firms "should invest in personalization, curated journeys, and community features that cultivate psychological ownership and perceived control in the absence of title transfer" (p. 416), "thereby shifting competitive advantage toward onboarding ease, continuity guarantees, and low-friction exit" (p. 416). "Hence, firms should disclose the total cost of use, provide low-friction cancellations, and design equitable tiers (e.g., student/low-income pricing) to avoid exploitative practices associated with “roach-motel” subscription flows" (p. 416).

**Prescriptions to policy.** "Accordingly, policy revisions are needed to enhance protections for access-based and digital-dominant solutions by mandating license transparency, continuity and termination disclosures, as well as meaningful remedies when access is withdrawn." (p. 417). "As a remedy, regulators can require total cost of use disclosures, friction-reduced cancellation flows, and protections against predatory price subscriptions" (p. 417). Policy could also impose repair and recirculation standards on Lends, and promote "interoperability, portability, and license transparency in order to preserve competition and reduce switching costs" (p. 417).

## Q3. To whom, and by whom?

**Who should act, and who benefits: named.** The safeguards go to "firms" in general (p. 416), and to "policymakers" and "regulators" (p. 417). The beneficiaries are consumers, with "low-income or digitally vulnerable users" singled out (p. 417). The conclusion gives each addressee a task: "firms must carefully design solutions that balance control and flexibility; consumers must navigate new solutions that may be detrimental to their well-being; and policymakers must grapple with outdated assumptions regarding property, risk, and responsibility in increasingly fluid marketplaces" (p. 420).

**Allocation between parties: one passage, two-party and descriptive.** "Under access arrangements, providers typically retain responsibility for upkeep and liability (Moeller & Wittkowski, 2010) while ownership transfers these burdens to the consumer." (p. 411; Table 1, p. 412: access, "Maintenance and liability largely handled by provider"; ownership, "Owner responsible for care, maintenance, and associated costs").

**Safeguards as owed, or divided among several firms: not found after a full read.** No safeguard is said to be owed: the words owe, duty, obligation and safeguard do not occur. No passage divides responsibility among several firms, though the examples involve several: the Keeps turntable gains value through "streaming partnerships" (p. 413), Tokens are bought "through platforms such as Bandcamp" (p. 413), and ride-sharing platforms appear at p. 417. Nor does the article say who supplies the "meaningful remedies when access is withdrawn" (p. 417). Sections checked: the abstract; Introduction; Literature Review (Physical Versus Digital; Access Versus Ownership; Consumer Well-Being); Conceptual Framework (Accesship as a Complement to the Phygital; From Ownership to Access-Based Solutions; Integrating Accesship and Phygital; Toward a Typology, with all four quadrants); Tables 1–4; Conceptual Propositions (Type of Solution; Mode of Acquisition); Implications (for Firms, Consumers, Public Policy); Future Research Directions (Solution Typology; Psychological Mechanisms and Well-Being Outcomes; Societal Implications); Conclusion; Acknowledgments; note 1; references; biographies.

## Q4. Seamlessness, friction, continuity, control, lock-in, revocation; recourse

**Seamless, frictionless:** neither word occurs. The nearest is "phygital merges physical tangibility with digital fluidity" (p. 420), and "increasingly fluid marketplaces" (p. 420).

**Friction** (every use):
- "Digital-dominant and access-dominant solutions are predicted to yield higher acquisition satisfaction as they typically lower initiation frictions (e.g., effort, time, and upfront financial commitment) and allow consumers to begin use quickly." (Table 3 notes, p. 414)
- "thereby shifting competitive advantage toward onboarding ease, continuity guarantees, and low-friction exit." (p. 416)
- "Hence, firms should disclose the total cost of use, provide low-friction cancellations, and design equitable tiers ... to avoid exploitative practices associated with “roach-motel” subscription flows (i.e., easy to sign up but difficult and frustrating to cancel)" (p. 416)
- "As a remedy, regulators can require total cost of use disclosures, friction-reduced cancellation flows, and protections against predatory price subscriptions (Sheil et al., 2024)." (p. 417)

**Continuity, continued access, revocation, withdrawal** (every use bearing on access; "continued participation" in Table 2 and note 1 concerns staged benefits):
- "continuity guarantees" (p. 416, quoted above)
- "Moreover, consumers may face limitations on functionality, interoperability, or even continued access when a service is discontinued or a license is revoked (Calo, 2013)." (p. 417)
- "policy revisions are needed to enhance protections for access-based and digital-dominant solutions by mandating license transparency, continuity and termination disclosures, as well as meaningful remedies when access is withdrawn." (p. 417)

**Lock-in:**
- "Access-dominant models (i.e., Streams, Lends) can expand a firm’s customer base by lowering upfront costs but may also create lock-ins and opaque cost structures." (p. 416)
- "access-heavy formats (i.e., Streams, Lends) can broaden participation, yet introduce the risks of hidden (and often recurring) costs and subscription lock-ins that disproportionately burden low-income or digitally vulnerable users." (p. 417)
- Related: "interoperability, portability, and license transparency in order to preserve competition and reduce switching costs" (p. 417).

**Control** (every use; all concern property rights or the consumer's perceived control):
- "Ownership also confers a more complete bundle of property rights, including control, customization, transferability, and responsibility for risk" (p. 410)
- "physical-dominant and ownership-dominant solutions are predicted to better support well-being as they enhance sensory engagement and perceived control" (Table 3 notes, p. 414)
- "their intangibility and/or contractual boundedness can weaken enduring control, personalization, and attachment relative to more tangible and ownership-based solutions" (Table 3 notes, p. 414)
- "The tangible nature of a physical solution should also enhance well-being by providing consumers with a stronger sense of identity and control (Belk, 1988)." (p. 415)
- Belk quoted: "The conceptual domain of possessiveness should include … a desire for the greater control of ownership rather than the lesser control of rental, borrowing, leasing." (p. 415)
- "In addition to providing materialistic individuals with a greater sense of control (which should help assuage their inherent insecurities), owning (rather than accessing) a solution keeps consumers on the hedonic treadmill" (p. 415)
- "the sense of control afforded by this state is more likely to manifest when an object is in one’s possession (Sharma et al., 2021)" (p. 415)
- "Atasoy and Morewedge (2018) find that touching an object establishes a perception of perceived control" (p. 415)
- "accessed solutions confer only temporary possession and (thus) typically limit consumers’ ability to claim, personalize, and control the solution" (p. 415)
- "cultivate psychological ownership and perceived control in the absence of title transfer" (p. 416)
- "tactile trials or haptic cues to foster perceived control and psychological ownership" (p. 416)
- "These measures preserve the well-being pathways tied to perceived control and psychological ownership (i.e., P2 and P5), even when legal ownership is absent." (p. 417)
- "firms must carefully design solutions that balance control and flexibility" (p. 420)

**Recourse, complaint, correction, redress, a human to reach:** none of these words occurs, and the article never mentions contact with a person. "Human" appears only inside the Batat definition (p. 411) and in reference titles. The only remedy language is "meaningful remedies when access is withdrawn" and "As a remedy, regulators can require" (both p. 417). Neither says who provides the remedy, or by what route a consumer reaches it.

## Q5. Hospitality, accommodation, hotels, guests, hosts

The body never mentions hospitality, hotels, hosts or guests. "Guest" occurs only in the reference list (p. 422) and in an author biography (p. 424). Accommodation appears twice:
- "For example, it requires considerably less effort, money, and time to rent a historic villa in Tuscany via Airbnb than to try to buy one. As a result, acquisition satisfaction should be higher for solutions that are accessed versus owned." (p. 415)
- "work on access-based consumption in the sharing economy suggests that access can enhance well-being through mechanisms such as positive social interactions between providers and users (Medina-Hernandez et al., 2024)" (p. 410). The cited study's title concerns guests' experiences on peer-to-peer accommodation platforms (p. 422).

No AI or algorithmic system enters the argument either. "AI" appears only in two reference titles (pp. 421, 422) and one biography (p. 425).

My reading: on the article's own axes a stay is physical-dominant and access-dominant, a Lends. The article never says so, and v8 cannot attribute it.

## Q6. Control as a ground, dependence, who answers when access fails

**Control as the ground of a duty: absent.** Control in this article belongs to the consumer, as a property right or a perceived state (Q4). The provider's position appears once, as a typical allocation by mode of acquisition: providers "typically retain responsibility for upkeep and liability" (p. 411). My reading: that line is the nearest thing to the paper's ground. Even so, it differs in three ways. It rests on mode of acquisition, not on control of the guest's space. It describes what is typical, citing Moeller and Wittkowski, and asserts no duty. And it concerns upkeep and liability, not care for safety.

**Dependence on a provider: present, as a harm.** Consumers of accessed solutions use what "are typically owned by another entity" (p. 415), and they can lose "continued access when a service is discontinued or a license is revoked" (p. 417). Lock-ins and switching costs keep them dependent (pp. 416–417). The divergence between psychological and legal ownership "may increase consumer vulnerability" (p. 419), and RQ8 asks "What ethical or legal challenges emerge when consumers form psychological ownership of solutions they do not legally own?" (p. 419). The article never calls this reliance a ground of anyone's responsibility.

**Who answers when access fails: open.** Policy should mandate "meaningful remedies when access is withdrawn" (p. 417). The article does not say who answers, to whom, or how fast. My reading: this is the opening the paper's further duty fills. The paper's claim is a duty to keep some timely route by which a failure in the guest's case reaches someone able to correct it.

**Touchpoints.** The article uses the word three times, always for stages of a firm-designed journey: "experiences that unfold dynamically across time and touchpoints" (p. 411), "firms design successive touchpoints that deepen engagement" (p. 413), "orchestrated journeys that unfold across time, touchpoints, and modalities" (p. 414). None concerns failure at a touchpoint.

## Verdict on the gap statement

Working statement: "Phygital research prescribes safeguards for trust, fairness and well-being, but says neither to whom they are owed nor which of several firms owes them."

**For this article: partly supported.** Clause by clause:

| Clause | Verdict | Basis |
|---|---|---|
| prescribes safeguards for well-being | holds | firm prescriptions (p. 416); policy prescriptions (p. 417) |
| for trust, fairness | not supported here | neither word occurs; nearest are "equitable tiers", "exploitative practices" (p. 416), "predatory price subscriptions" (p. 417). Other sources must carry these |
| says neither to whom they are owed | holds only if "owed" is read strictly | it names who should act (firms, regulators) and who benefits (consumers, "low-income or digitally vulnerable users", p. 417), but frames nothing as owed. A reviewer could answer the clause with p. 416 ("firms should ... provide low-friction cancellations") |
| nor which of several firms owes them | holds | "firms" stays generic; multi-firm examples (pp. 413, 417) get no allocation; the only allocation is provider versus consumer (p. 411) |

One more tension. The article itself says the phygital literature "has remained largely silent" on well-being harms (p. 409). My reading: on that account, safeguard prescriptions in phygital research are recent and few. v8 should not imply a settled tradition of them.

A possible rewording, Claude-drafted and for you to accept, change or drop: *Phygital research has begun to prescribe safeguards for consumer well-being — clear disclosure, easy exit, remedies when access is withdrawn — and addresses them to 'firms' and regulators in general; it does not say to whom they are owed as duties, nor which of several firms owes them when one service is assembled from several firms' parts.* If you decline to cite this article, the gap sentence must rest on other sources.

## Where it could sit in v8

My reading, subject to your anonymity ruling:

1. **The well-being material: the best fit.** One or two third-person sentences. Phygital research has turned to well-being and named the withdrawal of access as a harm (pp. 409, 417). It asks for "meaningful remedies when access is withdrawn" without saying who provides them (p. 417). The paper's further duty, a timely route from a failure in the guest's case to someone able to correct it, answers that open question for the stay. The provider-retains-upkeep line (p. 411) can stand beside it as the article's only allocation, and it is two-party.
2. **The conclusion's research directions: secondary.** RQ8's "grey zone" between psychological and legal ownership (p. 419) and the open question of who answers when access fails (p. 417) could frame one direction. The guest holds a room she does not own, through several firms' systems, so she sits in that grey zone during the stay. This is my reading, not the article's.
3. **The theory section on phygital hospitality: a weak fit.** The article has nothing on hospitality, and v8 does not need the accesship construct. At most one clause: phygital scholarship now separates a solution's type from its mode of acquisition (pp. 408, 411). I would not place it here.

## Proposed claim slugs (for CLAIMS.md; not added)

| slug | § | the claim it carries |
|---|---|---|
| `phygital-safeguards-unallocated` | v8 positioning | Phygital research prescribes well-being safeguards to firms and regulators in general, without saying to whom they are owed or which of several firms owes them |
| `access-withdrawal-remedy-open` | v8, K7 | Phygital and access-based consumption research calls for remedies when a provider withdraws access, without naming who provides the remedy or the route to it |

On the card I used existing slugs only: `framing-argued-past`, `wellbeing-valence`, `exit-voice-standing`, `novelty-neighbour`.

## Leads from its reference list (titles only; not read, not verified)

None of these is in the library. Each needs retrieval and a full read before it carries anything.
- Lim, W. M. (2026a), 'Let's get phygital: The bright and dark sides of generative AI for phygital customer experience', *Journal of Strategic Marketing*, doi 10.1080/0965254X.2025.2595087 (listed p. 422). It is the only AI-and-phygital title in the list, and the article leans on it for its definition of phygital.
- Lee, D.-J., Yu, G. B. and Sirgy, M. J. (2024), 'Reflections on phygital experiences: Conceptual boundaries, wellbeing benefits and methodological suggestions', *Qualitative Market Research*, 27:3, pp. 515–522 (p. 422). Phygital and well-being.
- Klaus, P. P. (2024), 'Phygital – The emperor's new clothes?', *Journal of Strategic Marketing*, 32:8, pp. 1172–1179 (p. 422). A critique from within the phygital literature.
- Medina-Hernandez, V. C., Marine-Roig, E. and Ferrer-Rosell, B. (2024), guests' experiences on non-profit and for-profit peer-to-peer accommodation platforms, *Information Technology and Tourism*, 26:2, pp. 255–291 (p. 422).
- Sheil, A. et al. (2024), manipulative subscription and cancellation flows, CHI 2024 (p. 423); and Perzanowski, A. and Schultz, J. (2016), *The End of Ownership* (p. 423). Both concern exit friction and revoked access.
