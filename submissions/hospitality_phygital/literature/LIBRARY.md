# The library — contextual bibliography for *Who Hosts the Guest?*

Every source the paper cites, organized by the work it does, with three annotations per entry: where
it sits in the paper, what the source itself argues, and what it uniquely adds. A closing section
lists the verified entries held in the bib but not cited, with one line each on why they are held.
Machine-readable citation data lives in [`references.bib`](references.bib) (172 entries, every one
carrying a verification date and read depth); the research provenance lives in
[`FOUNDATION.md`](FOUNDATION.md) Parts 1–7, with the P9 pass written up separately in
[`P9_FINDINGS.md`](P9_FINDINGS.md); claim-level verdicts in
[`../manuscript/CLAIMS.md`](../manuscript/CLAIMS.md). This file is the reader's map, not the source
of record — regenerate section placements from `cited_keys.txt` and the manuscript if the draft
moves.

Entries marked ⚠ are abstract-depth: citation verified, substantive attribution restricted under
the standing rule (no effect size or mechanism from an abstract alone). Entries marked ⚠⚠ are
metadata-only, with content unread — nothing may be attributed to them at all until the full text is
in hand.

**This file is not the source of record.** [`../library/cards/`](../library/cards) is: one card per
source, with structured frontmatter, a controlled claim vocabulary in
[`../library/CLAIMS.md`](../library/CLAIMS.md), and a CI gate in `build_index.py` that fails on a
stale index, an unknown claim slug, a citation with no card, a status that disagrees with the
manuscript, or a verification tier the bibliography does not support. This file is the prose view of
the same material: it reads continuously, groups by argument, and is where the reasoning about how
sources relate to each other lives. When the two disagree, the cards win.

Keeping both is a decision rather than an oversight, and it has one rule. Facts about a source —
status, read depth, verification, which sections use it — belong in the card and are checked. Prose
about how sources bear on each other belongs here and is not. Do not record a fact only here; the
check cannot see it, and the 8 August build failed for exactly that reason.

**State, 2026-08-11.** The P9 sources are now in `references.bib` (234 entries) and carry cards. The
card library was reconciled against the manuscript in the same pass, which found it badly stale: 101
validation errors, none from the new cards. Nine citekeys had been renamed by the verification sweeps
without the cards following, six of them year corrections the project itself had made; sixteen cards
understated their status; four were orphaned. All are fixed. Fifty-four errors remain, all of one
kind — a source the manuscript cites that has no card — and they are listed in `CARDS_INDEX.md`.
Most of their content already exists in this file and can be migrated.

---

## 1. The special issue's editors — the paper's spine

Not a positioning obligation and not a courtesy layer. After P9 this cluster carries the paper's
structure: every claim Pierre's abstract makes is placed first against what Batat, Mosca and De Vos
have themselves published, and only then against the general literatures. Three relations recur, and
the paper uses all three. **Warrant**, where an editor has already established the premise a section
needs — Casalegno, Civera, Mosca and Freeman on role reallocation; Batat's transformative luxury
agenda on individual and collective well-being. **Nearest approach**, where an editor comes close and
stops — Mosca and Civera on customers judging corporate account-giving, which lacks only the forum;
Shabnam et al. naming the agency gap without specifying it. **Live objection**, where an editor
disagrees — Mosca and La Rosa recommending that technology be concealed, which is the transparency
affordance's best antagonist.

Read as a group they also hold seamlessness as a value while criticizing nearly everything adjacent
to it, which is exactly the narrow claim §7 now makes.

### 1a. Batat

**Batat, W. (2024). 'What does phygital really mean? A conceptual introduction to the phygital
customer experience (PH-CX) framework.' *Journal of Strategic Marketing* 32:8.** ⚠
*In the paper:* §1 common ground; §3 positioning; §7 as the stated commitment to fluidity the
seamlessness critique addresses.
*Argument:* phygital customer experience is a design problem of blending physical and digital
elements across tangible and intangible dimensions, organized by driving forces, connectors and
pillars, aimed at "fluidifying the journeys of customers from online to offline and inversely."
*Adds:* the field's founding framework and its name; also the clearest primary-text evidence that
smoothness is a stated value rather than an oversight — the quoted "fluidifying" is from her own
abstract. Component-level detail remains unverified at full text; §3 deliberately stays above it.

**Batat, W. (2026). 'Phygital service research (PSR): advancing FSR and TSR toward human-first
experience design in hybrid physical-digital ecosystems.' *Journal of Services Marketing* 40:4.** ⚠
*In the paper:* §1; §3 (names experience as "ethically and technologically mediated").
*Argument:* extends transformative and frontline service research into hybrid ecosystems, placing
guests, hosts, employees and communities at the centre of design and directing the field toward
positive impact at individual, community and environmental levels.
*Adds:* the bridge between the special issue and transformative service research, and the phrase
that prevents the paper claiming mediation is absent from PSR — the paper's precise claim is that
PSR names mediation without specifying its redistribution.

**Batat, W. (2026). 'The phygital intelligence value experience (PHIVE) matrix: the good, the bad,
and the ugly of AI marketing for customer experience design.' *Journal of Strategic Marketing*,
online 2 June 2026.** ⚠⚠ *(metadata verified; abstract unretrievable; full text owed — the highest
priority read in the project)*
*In the paper:* §3 ¶4 and §7 ¶1 — the self-critical turn the seamlessness claim must be narrowed
against.
*Argument:* unknown beyond the title, which establishes that the lead editor now theorizes negative
and harmful valences of AI-driven phygital customer experience design.
*Adds:* the single item that decides how §7's claim is worded. If her dark sides include smoothness,
the claim narrows again; if they do not, the paper can say that the phygital programme criticized
AI's harms, its technocentrism and its efficiency logics while leaving seamlessness itself alone —
which is the strongest available form of the argument. Nothing may be attributed to it until read.

**Batat, W. (2024). 'Phygital customer experience in the metaverse: a study of consumer sensory
perception of sight, touch, sound, scent, and taste.' *Journal of Retailing and Consumer Services*
78, 103786.** ⚠
*In the paper:* §7 ¶1 — the second of three primary quotations establishing seamlessness as a stated
goal.
*Argument:* sensory replication across physical and digital settings is selective; some senses (taste)
are pointless to reproduce. Abstract states the design objective directly: "The goal is to create a
seamless merge between physical and digital settings."
*Adds:* the cleanest single sentence in the corpus in which seamlessness is named as the goal rather
than implied. The paper quotes it. Note that the study's own critical finding is a feasibility limit,
not a value critique, which is the distinction §7 turns on.

**Batat, W. & Hammedi, W. (2023). 'The extended reality technology (ERT) framework for designing
customer and service experiences in phygital settings: a service research agenda.' *Journal of
Service Management* 34:1, 10–33.** ⚠
*In the paper:* §7 ¶1 — the third quotation, and the earliest.
*Argument:* extended reality technologies create "a continuum in terms of customer value from
physical to digital settings and vice versa"; sets a service-research agenda for designing with them.
*Adds:* continuum-as-value stated inside a service-research framework, which is where the paper's
own argument lives; also the natural citation for the taxonomy of phygital technologies that the
paper then distinguishes from algorithmic intermediaries with hosting functions.

**Batat, W. (2022). 'Transformative luxury research (TLR): an agenda to advance luxury for
well-being.' *Journal of Macromarketing* 42:4, 609–623.** ⚠
*In the paper:* §8 ¶2 — the well-being architecture, arriving before TSR.
*Argument:* proposes a transformative research agenda asking how luxury ecosystems "affect the
individual and collective well-being at the economic, cognitive, emotional, and social levels,"
spanning consumer and production spheres and macro-level stakeholders.
*Adds:* the two-level well-being structure the editor's revision request asks for, in the lead
editor's own words and her own transformative lineage. This is why §8 no longer opens on Anderson and
Ostrom: the levels are hers first, and the service-ecosystem framing follows.

**Batat, W. (2022). 'Luxury service brand extensions and their spillover effects on customers'
evaluations of luxury gastronomy foodservice.' *Hospitality & Society* 12:3, 265–298.** ⚠
*In the paper:* §2 — the venue anchor.
*Argument:* qualitative study (n=35) showing brand-extension spillover depends on extension type,
strategic orientation and consumer familiarity with luxury gastronomy.
*Adds:* the demonstration that the lead editor has published in the target journal. Its substantive
content is peripheral to the argument; its citation value is that the paper knows the venue's own
record, which is precisely what the editor's seventh ask is about.

**Batat, W. (2021). 'The role of luxury gastronomy in culinary tourism: an ethnographic study of
Michelin-starred restaurants in France.' *International Journal of Tourism Research* 23:2, 150–163.**
(read in full — introduction and framework)
*In the paper:* §2 ¶2 — the five criteria, couched before Derrida.
*Argument:* the lived luxury experience is co-produced through interaction with service providers and
other customers and with environmental elements; carries her programmatic definition of luxury
consumption as "a response to a search for emotions, pleasure, uniqueness, consideration, and greatest
services" and of luxury as "a personal experience... symbolic, social, ideological, subjective, and
emotional."
*Adds:* *consideration* — an editor's own word for something very close to recognition, in a
hospitality setting, in an ethnography. It lets §2 introduce the relational criteria from inside the
special issue's own scholarship rather than importing them from hospitality philosophy and then
justifying the import.

**Batat, W. (2021). 'How augmented reality (AR) is transforming the restaurant sector: investigating
the impact of "Le Petit Chef" on customers' dining experiences.' *Technological Forecasting and
Social Change* 172, 121013.** ⚠
*In the paper:* §4 ¶3 — the editor-native augmentative vignette.
*Argument:* case study of an AR-animated dining experience finding enhancement across sensory,
affective, behavioural, social and intellectual dimensions and improvement in food well-being, while
identifying the psychological factors behind adoption and rejection.
*Adds:* the lead editor's own hospitality-venue technology study, and it is an augmentative case by
the paper's own condition — the technology enriches a meal that people still host. Citing it makes
the augmentative pole concrete in her work before the paper generalizes.

**Batat, W. (2019). *Experiential Marketing: Consumer Behavior, Customer Experience and the 7Es*.
Routledge.** ⚠
*In the paper:* §2 ¶2 — the scaffold under the five criteria.
*Argument:* replaces product-centric logic with experience-centric logic across seven Es —
experience, exchange, extension, emphasis, empathy capital, emotional touchpoints, emic/etic process
— and opens on consumer empowerment as the driver of new brand opportunity.
*Adds:* a mapping the paper can make in one sentence: empathy capital to care, emotional touchpoints
to presence and welcome, the emic and etic process to recognition, exchange and extension to
negotiated access. Also the corpus's foundational statement that empowerment is the experiential
paradigm's aim, which is what coordinative sovereignty specifies when the counterparty is an
algorithm. No second edition exists; the 2020 companion is a case-study volume with a food, tourism
and leisure chapter.

**Batat, W. (2025). '"Binge delivery" behaviors among digital natives: a phygital exploration of
status, empowerment, and vulnerability.' *Qualitative Market Research* 28:5, 941.** ⚠⚠ *(metadata
verified, content unread)*
*In the paper:* §7 ¶1 or §8 ¶2 — the editor's own evidence that frictionless phygital consumption
carries costs.
*Argument:* title-level only — empowerment and vulnerability held together in on-demand phygital
consumption among digital natives.
*Adds:* the empirical half of the narrowing. She has found the costs of frictionless delivery without
naming seamlessness as the design value responsible, which is the precise shape of the opening the
paper enters.

### 1b. Mosca

**Casalegno, C., Civera, C., Mosca, F. & Freeman, R. E. (2020). 'Circular economy and
relationship-based view.' *Symphonya* 1/2020.** (read in full, open access)
*In the paper:* §3 ¶5 — the redistribution premise, and §1 ¶6.
*Argument:* the circular economy is "an open and dynamic loop of relationships" turning on "the
reallocation of stakeholder roles," whose power and responsibilities should "overlap and converge,"
enabling emergent joint value creation.
*Adds:* the strongest warrant in the whole editor corpus, and it is co-authored with Freeman. Roles
and responsibilities reallocate; obligations converge rather than evaporate. That is §3's premise
stated generally by an editor, which lets the paper ask its question — what fails to travel with the
redistribution — instead of first arguing that redistribution happens.

**Civera, C., Mosca, F., Casalegno, C. & Maple, P. (2018). 'Customers' judgments and misjudgments of
corporate responsibility communication: a cross-country investigation of the effects on confidence
and trust within the banking sector.' *Psychology & Marketing* 35:2.** (read in full)
*In the paper:* §5 ¶4 — accountability's nearest approach inside the editor corpus.
*Argument:* focus-group and comparative-case study across Italy and the UK showing that both
over-communication and under-communication of corporate responsibility produce customer misjudgment
and lower confidence; distinguishes confidence from trust; grounded in Freeman's stakeholder
approach.
*Adds:* an editor already treating the firm's account-giving as something stakeholders judge, and
already showing that talk without answerability corrodes confidence. What the account lacks is the
forum — the party with an obligation to answer and to bear consequences — which is exactly what
Bovens supplies and what the paper's fourth condition turns on. The nearest-approach relation in its
clearest form.

**Mosca, F. & Civera, C. (2017). 'The evolution of CSR: an integrated approach.' *Symphonya*
1/2017.** (read in full, open access)
*In the paper:* §4 ¶1 — the augmentative and substitutive distinction, couched.
*Argument:* distinguishes residual CSR (compliance rhetoric, harm minimization) from integrated CSR
(intrinsic stakeholder commitment, redesigned business models); urges the shift from transactional
company-stakeholder to collaborative company-partner relations with joint decision-making.
*Adds:* an editor's own binary between performing the form of a responsibility and occupying the
position of it. The analogy to augmentative and substitutive hospitality is close enough to carry the
distinction's intuition before Okhuysen and Bechky make it checkable.

**Mosca, F. & La Rosa, E. (2019). '4.0 technology within fashion and luxury production.' *Symphonya*
2/2019.** (read in full, open access)
*In the paper:* §6 ¶1 — the live objection that opens the transparency affordance.
*Argument:* managers see value in Industry 4.0 while customers hold negative attitudes toward
technology in luxury production; the authors therefore recommend keeping technological implementation
undisclosed to preserve perceived authenticity, while insisting that Industry 4.0 "is not about
complete automation but rather about human–machine interaction."
*Adds:* an editor arguing for invisibility, which is the position §6 exists to answer. The paper does
not route around it: concealment here is a response to consumer distrust, managed by hiding rather
than by answering, which is a withholding of common understanding treated as a communications problem.
Meeting the objection in an editor's own data is worth more than any number of agreeable citations.

**Mosca, F. (2026). 'Artificial intelligence as a strategic inflection point: implications for firms,
industries, and global competitiveness.' *Journal of Emerging Perspectives* 2, 3–7.** (read in full,
open access)
*In the paper:* §5 ¶2 and §6 ¶1 — the affordances and the surviving human competence, in an editor's
words.
*Argument:* editorial positioning AI as general-purpose strategic infrastructure; managerial work
shifts toward "interpretation and validation"; the governance requirements are "AI literacy, model
governance, and ethical oversight," with explicit endorsement of the EU AI Act's transparency and
human-oversight requirements for high-risk systems; labour effects acknowledged as "brutally uneven."
*Adds:* two things at once. Transparency and human oversight named as the answer by an editor, which
is the affordance set's warrant; and interpretation named as the human work that survives
algorithmic infrastructure, which is the competence §5 specializes. Also the counterweight to Mosca
and La Rosa 2019 — the same editor, seven years later, on the other side.

**Mosca, F., Giacosa, E. & Zagni, L. M. (2021). 'The evolution of distribution in the luxury sector:
from single to omni-channel.' IGI Global.** ⚠
*In the paper:* §6 ¶4 — bypass-ability.
*Argument:* luxury firms choose between direct control of e-commerce and indirect distribution
through specialized intermediaries, differentiated by segment; digital integrates with rather than
overcomes traditional channels.
*Adds:* channel structure as a deliberate governance choice that preserves alternatives — the
editor's own vocabulary for what bypass-ability protects at the level of the encounter.

**Bertoldi, B., Giachino, C., Mosca, F. & Stupino, M. (2018). 'Facebook and Twitter, social networks
for culture: an investigation on museums.' *Mercati & Competitività* 2/2018.** ⚠
*In the paper:* §8 ¶2 — the collective register, optional.
*Argument:* counting likes is insufficient; users "must feel part of museums' life and interact with
it"; museums shift from object focus to visitor experience.
*Adds:* participation rather than reach as the metric, which is the pre-history of the 2025 museums
paper and a small, cheap way to show the paper has read the editor's line rather than his latest
article.

### 1c. De Vos

**De Vos, S., Qesja, B. & Lipnickas, G. (2023). 'E-interaction behaviour and customer experience: the
role of psychological comfort.' Global Marketing Conference at Seoul.** ⚠
*In the paper:* §5 ¶2 — interpretation and specification, couched.
*Argument:* in online credence services, the customer's experience of the provider is shaped
indirectly by service interactions — specifically "service manner and need identification" — through
psychological comfort.
*Adds:* an editor isolating *need identification* as the interactional work that makes mediated
service feel hosted. That is the paper's interpretation and specification components under another
name, established in an editor's own study before the folk-theory literature is called.

**Ala, M., De Vos, S., Nair, S. & Orrell, J. (2022). 'Developing ethical mindedness and ethical
imagination in postgraduate professionally oriented education.' Springer.** ⚠
*In the paper:* §3 ¶6 — discretion, couched.
*Argument:* ethical mindedness and ethical imagination are dispositions beyond rule-following,
because "compliance alone cannot guarantee ethical behavior when [professionals] encounter unforeseen
dilemmas."
*Adds:* the discretion argument stated by an editor, in one quotable sentence, about professional
judgment exceeding what rules can specify. Substitutive mediation's defining limitation is that it
cannot absorb this; saying so with an editor's sentence is better than saying it with Lipsky alone.

**De Vos, S., Qesja, B., Lipnickas, G. & Harris, J. (2024). 'Exploring the higher education
experiences of students living with disabilities: an online MBA case study.' *Journal of Marketing
Management* 40:5–6, 450–480.** ⚠
*In the paper:* §8 ¶2 — the valences.
*Argument:* uses the psycho-emotional model of disability to build a typology of enchantment,
re-enchantment and disenchantment in digitally mediated education, identifying enabling and disabling
factors beyond the curriculum.
*Adds:* three valences in an editor's own empirical work on a digitally mediated service, which is
what the editor's fourth revision request asks the paper to supply. Enchantment, disenchantment and
re-enchantment map onto positive, negative and recovered outcomes more precisely than a
positive/negative/neutral scheme does, and the recovery case is the one the paper's affordances aim
at.

**De Vos, S., Qesja, B., Lipnickas, G. & Harris, J. (2026). 'Applying an experiential lens to the
strength-based approach for students living with disabilities: insights from online higher education
professionals.' *Journal of Business Research* 210, 116165.** ⚠
*In the paper:* §8 ¶2 — the mechanism under the valences.
*Argument:* high student-customer orientation and high respect embody the strength-based approach;
respect and inclusive practices mediate effects on inclusivity, commitment and satisfaction with
support services.
*Adds:* respect as the mediating variable in mediated service, from an editor, in 2026 — a relational
rather than transactional mechanism, which is the paper's premise measured.

**De Vos, S. & Qesja, B. (2022). 'Effective consumer journey: personalizing touchpoints and
optimizing conversion for mature-age online MBA prospective students.' AMS Proceedings.** ⚠
*In the paper:* §6 ¶4 — human accessibility.
*Argument:* two personas, one of whom prefers direct phone contact with a human recruiter; generic
and intrusive pitches without personalization impede conversion; effective advisors are prompt,
friendly and non-intrusive.
*Adds:* an editor's own evidence that some users need a reachable person, which the paper then
sharpens: what matters is not the person but the authority the person carries.

### 1d. The adjacent field the paper argues past

**Brochado, A., De Vos, S., et al. (2026). 'Is phygital the new normal? A literature review of the
evolution of services marketing.' *Journal of Services Marketing* 40:4.** ⚠
*In the paper:* §1 common ground and complication — its phrase "consumer-centred and
technology-enabled" is quoted as the field's self-description and used as the paper's premise.
*Argument:* systematic review of 105 phygital studies, 2017–2025; phygital experience is the
corpus's core, tied to journeys and retail strategy, with applications in luxury, tourism, culture.
*Adds:* the authoritative field map, co-authored by an SI editor, whose summary adjective
("technology-enabled") is itself the capacity-vocabulary evidence for the paper's complication.

**De Vos, S., et al. (2026). 'Enhancing phygital employee experience in high-involvement
professional service organizations.' *Journal of Services Marketing*, ahead-of-print.** ⚠
*In the paper:* §1 concern — employees resist where the technology's purpose is obscured.
*Argument:* phygital competencies (digital literacy, data fluency, cross-channel orchestration) are
unevenly supported; employees stay engaged when technology is clearly linked to a higher purpose
and resist when the connection is obscured.
*Adds:* the transparency affordance arriving from the staff side, in an SI editor's own empirical
work — obscured purpose produces resistance before any guest is involved.

**Mosca, F., Civera, C., Chiaudano, V. & Shakil, H. (2025). 'Phygital museums as catalysts for
inclusivity, well-being, and human-centric cultural experiences.' *Journal of Macromarketing*
46:3.** ⚠
*In the paper:* §1 contribution block — the redistribution-of-agency precedent the paper extends.
*Argument:* phygitalization reconfigures an institution's spatial and relational boundaries and
disperses authority among institutional and non-institutional actors; read as broadly emancipatory.
*Adds:* redistribution of authority stated inside the phygital literature by an SI editor — and the
gap the paper enters, since the museum case never asks what obligation travels with the dispersed
agency.

**Shabnam, S., Roy, S. K., et al. (2026). 'Transformative phygital service research (TPSR): an
agenda for future research.' *Journal of Services Marketing* 40:4.** (read in full)
*In the paper:* §1; §3 (the named gap); §7 (critiques opacity and rigidity, not smoothness).
*Argument:* existing frameworks do not explain how algorithmic systems redirect, constrain or
reconfigure agency; sets a transformative agenda for phygital service research.
*Adds:* the phygital programme's own statement of the gap the paper fills — cited so the gap is
theirs, not asserted — and the demonstration that the friction critique is absent from the
programme's most critical document.

**Tussyadiah, I. (2020). 'A review of research into automation in tourism.' *Annals of Tourism
Research* 81.**
*In the paper:* §1 — the adoption-and-acceptance framing the paper argues past.
*Argument:* curates automation research in tourism around adoption, acceptance, and the redesign of
service delivery.
*Adds:* the authoritative statement of what the field's questions have been, which is what lets the
paper say its question is different without caricaturing anyone.

**Wirtz, J., et al. (2023). 'Digital service technologies, service robots, AI, and the strategic
pathways to cost-effective service excellence.' *The Service Industries Journal* 43:15-16.**
*In the paper:* §1 — the efficiency framing.
*Argument:* service robots and digital technologies are strategic instruments for cost-effective
service excellence.
*Adds:* the cleanest expression of technology-as-instrument in the service literature; also a CFP
reference, so citing it signals the paper knows the call's own canon.

**Xu, F. Z., et al. (2020). 'Facial recognition check-in services at hotels.' *JHMM* 30:3.** and
**Boo, H. C. & Chua, B.-L. (2022). 'An integrative model of facial recognition check-in technology
adoption intention.' *IJCHM* 34:11.**
*In the paper:* §1 (willingness questions at the threshold); §6 (bypass-ability — guests weigh
privacy against benefit).
*Argument:* both model biometric check-in adoption as a privacy-calculus decision by the guest.
*Adds:* the threshold studied as a question about guest acceptance — the paper's foil — and the
empirical basis for treating declining the digital path as a real guest behaviour rather than an
edge case.

## 2. Hospitality theory — the journal's ground (§2)

The tradition that makes the host argument possible: hospitality as relational practice, the host
as a position with duties, the guest as a party with standing.

**Lashley, C. (2000). 'Towards a theoretical understanding.' In *In Search of Hospitality*.**
*In the paper:* §1, §2 — the three-domains architecture.
*Argument:* hospitality operates simultaneously in commercial, private and social domains, with the
commercial domain inheriting meaning from the other two.
*Adds:* the inheritance claim — a hotel's obligations descend from the household and the social
rules of receiving strangers, not from the service contract. The paper's duty argument stands on
this.

**Hemmington, N. (2007). 'From service to experience: understanding and defining the hospitality
business.' *The Service Industries Journal* 27:6.**
*In the paper:* §1 complication, §2 — the misdescription claim.
*Argument:* hospitality businesses are persistently misdescribed as service operations and better
understood through the host–guest relationship, generosity, theatricality.
*Adds:* the attributed version of "hospitality exceeds provision," which lets the paper make a
field-level claim through a named scholar instead of a proclamation.

**Lynch, P., Germann Molz, J., McIntosh, A., Lugosi, P. & Lashley, C. (2011). 'Theorizing
hospitality.' *Hospitality & Society* 1:1.**
*In the paper:* §1, §2 — the journal's founding frame.
*Argument:* hospitality is a lens on social control, exchange and metaphor; the journal exists to
foster critical, interdisciplinary hospitality scholarship.
*Adds:* the home-venue anchor: none of its three registers is service quality, which is the paper's
§2 point made by the journal's founders on page one of issue one.

**Lynch, P., McIntosh, A., Lugosi, P., Germann Molz, J. & Ong, C. E. (2021). 'Hospitality &
Society: critical reflections on the theorizing of hospitality.' *H&S* 11:3.** and **Lynch, P., et
al. (2021). 'Theorizing hospitality: a reprise.' *H&S* 11:3.** (both read in full)
*In the paper:* §1, §2 — the decade review and renewed critical call.
*Argument:* the journal's first decade treated hospitality as a lens on power, identity, belonging
and exclusion; the reprise renews the call to treat the concept as social analysis, not sector.
*Adds:* fit evidence and the venue's prose exemplar — this pair also calibrated the manuscript's
register (REGISTER.md).

**Lynch, P. (2017). 'Mundane welcome: hospitality as life politics.' *Annals of Tourism Research*
64.** (read in full)
*In the paper:* §1 concern, §2 (the tactical-and-ethical tension), §7 (welcome as "social oil"
noticed only on failure).
*Argument:* ordinary welcome is a tactical accomplishment deployed to negotiate the world day by
day, held in unresolved tension with a Levinasian ethics; closes pessimistic about "hospiety."
*Adds:* three load-bearing pieces — the guard against a moral reading of guest standing, the
micro-host/macro-host distinction, and the social-oil line that opens the seamlessness critique in
the field's voice. The audit corrected the paper's earlier over-resolution of his tension.

**Bulley, D. (2015). 'Ethics, power and space: international hospitality beyond Derrida.' *H&S*
5:2-3.** (read in full)
*In the paper:* §1 concern, §2 — authority past the threshold.
*Argument:* Derrida's concentration on the sovereign threshold moment is too narrow; hospitality is
a spatial relation whose power is exercised continuously inside the space, through tactics that
contain a guest who resists, with ethics and power constitutively linked.
*Adds:* the licence for a paper about mediation *after* admission — recognition, routing, pricing
run the length of a stay — from the target journal's own pages.

**Derrida, J. & Dufourmantelle, A. (2000). *Of Hospitality*.**
*In the paper:* §2 — the conditional/unconditional distinction.
*Argument:* unconditional hospitality is impossible and necessary; every practised hospitality sets
conditions.
*Adds:* the critical edge on negotiated access: the interesting question is who sets the conditions
and whether they stay open to discussion — which becomes computational in this paper.

**Lugosi, P. (2008). 'Hospitality spaces, hospitable moments.' *Journal of Foodservice* 19:2.**
*In the paper:* §2 — hospitality resists reduction to outcomes.
*Argument:* hospitable moments are emergent and partly unscripted, arising within interaction
rather than delivered by it.
*Adds:* the premise that a stay proceeding without incident has not thereby been received — the
wedge between smooth outcomes and hospitality that §7 widens.

**Pijls, R., Groen, B. H., Galetzka, M. & Pruyn, A. T. H. (2017). 'Measuring the experience of
hospitality: scale development and validation.' *IJHM* 67.** (read in full, incl. predecessor)
*In the paper:* §1, §2 — re-scoped by the audit: the scale measures the *feeling*, not the
position.
*Argument:* the guest's experience of hospitality resolves into inviting, care and comfort.
*Adds:* the field's own instrument locating hospitality in the guest's sense of acknowledgment —
cited as the trace standing leaves in experience. The predecessor study's "autonomy" dimension
(valuing *not having to ask*) is why the paper no longer cites this as an agency measure.

**Kekstaite, J. (2022). 'Beyond Derrida: fragments of feminist hospitality.' *H&S* 12:2.** ⚠
*In the paper:* §2 — reciprocity as achievement.
*Argument:* reciprocity in hosting illegalized migrants is an achievement internal to hospitality
rather than a background condition.
*Adds:* the implication the paper needs: what is achieved can be designed away.

**Munasinghe, S., Hemmington, N., Schänzel, H. & Poulston, J. (2022). 'Hospitality beyond the
commercial domain: a triadic conceptualisation.' *IJHM* 107.** ⚠
*In the paper:* §2 — the *other* triad, explicitly distinguished.
*Argument:* the host–guest encounter is conditioned by a third element, the wider social and
cultural context.
*Adds:* the disambiguation the title-word "triadic" demands: their third element is a context that
conditions; the paper's is a party that acts, decides and binds.

**Beatty, S. E., et al. (2016). 'Frontline service employee compliance with customer special
requests.' *JSR* 19:2.** ⚠
*In the paper:* §2 — the rival account of the exception, engaged and converted.
*Argument:* special-request outcomes are employee compliance decisions, driven by compliance
factors against policy, risk and resource deterrents.
*Adds:* the strongest non-standing explanation of exception-granting; the paper's answer — the
employee decides, and hospitality is what obliges somebody to decide rather than refuse by default
— is now stated against it rather than left implicit.

**Manfreda, A. & Harkison, T. (2025). 'Beyond exchange: decoding reciprocal hospitableness in luxury
lodge experiences.' *Journal of Hospitality and Tourism Management* 62, 173–187.** ⚠ *(journal
article abstract; the 2023 conference precursor read in full)*
*In the paper:* §2 ¶4 — the guest-obligation absence, now narrowed against it.
*Argument:* multiple-case study of New Zealand luxury lodges proposing reciprocal hospitableness
across guests, hosts, staff, communities and environments; guests reciprocate concretely — tidying
rooms for housekeeping, returning glasses to the bar, praising staff in reviews — and the authors
frame this explicitly as gratitude-driven reciprocation rather than formal obligation or
indebtedness.
*Adds:* the only commercial-setting work that theorizes guest-to-host flows, and the reason §2's
absence claim had to narrow. It also supplies the narrowing: they theorize what the grateful guest
gives back, and the paper's question is what the guest is *owed* and owes in virtue of the relation.
Their own disclaimer of obligation is the paper's warrant.

**Salazar, N. B. (2026). 'Restorying hospitality in times of biopolitics and polycrisis: a
multi-scalar, more-than-human perspective.' *Hospitality & Society* 16:1, 83–97.** ⚠
*In the paper:* §8 ¶2 — the multi-scalar warrant, from inside the journal.
*Argument:* reads hospitality up, down and sideways across scales and beyond the human, holding that
its fundamental meaning is mutual care, and proposes planetary conviviality as its extension.
*Adds:* the journal's own current statement that hospitality is analysable at several levels at once,
which is what §8's individual and collective registers need and what the editor's well-being request
asks for. Published in the same issue as Germann Molz 2026, so citing both signals the paper has read
the issue rather than a search result.

**Manfreda, A., Bisson, A., Lee, C., Scerri, M., Marcial, G. A. & Presbury, R. (2025). 'The pedagogy
of hospitableness: a transformative approach for hospitality workforce development.' *Journal of
Hospitality & Tourism Research* 49:8, 1447–1461.** ⚠
*In the paper:* §2 ¶4 or held — supports the absence claims.
*Argument:* proposes conditions and practices that trigger, support and accelerate a hospitable
service mindset, grounded in transformative learning theory and foregrounding connectedness.
*Adds:* evidence that even the newest hospitableness theory locates the capacity entirely on the host
and worker side. Useful as the demonstration that the guest side of the relation remains
untheorized, rather than as a source for any positive claim.

**Shi, F., Han, X. & Samaniego-Chávez, C. E. (2025). 'Residents' perceived benefits of host-guest
interaction: scale development and validation.' *Journal of Travel Research* 64:4, 950–965.** ⚠
*In the paper:* §2 ¶4 — the instrument absence, now narrowed against it.
*Argument:* develops and validates a five-dimension scale — emotional lift, local pride, altruism,
destination attraction, self-development — measuring what residents perceive they gain from
interacting with tourists, and shows it predicts interaction intentions and support for tourism.
*Adds:* a validated instrument measuring a guest-to-host flow, which kills the unqualified absence.
The narrowing that survives: the host here is a destination resident, the construct is a benefit
accruing to the host rather than conduct directed at one, and there is no commercial service
relation. §2 must say guest conduct toward a *commercial* host, and must also exclude the customer
incivility tradition by specifying positive or obligational constructs.

## 3. Platform hospitality — who hosts, already unsettled (§2)

**Cheng, M. & Foley, C. (2019). 'Algorithmic management: the case of Airbnb.' *IJHM* 83.**
*In the paper:* §2, §8 — hosting as algorithmically managed work.
*Argument:* Airbnb hosts are directed through pricing and ranking systems by a platform that
confers no employment relation.
*Adds:* hosting itself managed by algorithm, in a hospitality journal — the entry point for the
whole who-hosts question.

**Roelofsen, M. & Minca, C. (2018). 'The Superhost.' *Geoforum* 91.**
*In the paper:* §2.
*Argument:* the Superhost badge disciplines the hosting body; a platform's definition of good
hosting comes to govern its performance.
*Adds:* the platform writing the definition of good hosting — authority over the role's content,
not merely its rewards.

**Liang, S., et al. (2017). 'Be a "Superhost".' *IJHM* 60.**
*In the paper:* §2.
*Argument:* the badge measurably gates search visibility and bookings.
*Adds:* why hosts chase the badge — the material stakes behind Roelofsen and Minca's discipline.

**Leick, B., et al. (2024). 'Professionalisation of rural Airbnb hosts.' *Scandinavian Journal of
Hospitality and Tourism*.** and **Bosma, J. (2022). 'Platformed professionalization.' *Environment
and Planning A* 54:4.**
*In the paper:* §2.
*Argument:* rural and career hosts professionalize and improve performance without gaining
authority over the rules that govern them.
*Adds:* the pattern outside urban markets: competence rising, standing flat — the
competence/standing separation §5 formalizes, observed in the field.

**Farmaki, A. & Kaniadakis, A. (2020). 'Power dynamics in peer-to-peer accommodation.' *IJHM*
89.** ⚠
*In the paper:* §2 — the general lesson.
*Argument:* platform interdependencies reconstitute the power relations of hosting and reshape what
hosting practically consists of.
*Adds:* hospitality scholarship registering a third party in the host–guest relation before
information systems arrived to announce one — the sentence §2 closes on.

**Germann Molz, J. (2026). 'Guests without hosts: on the digital biopolitics of network hospitality.'
*Hospitality & Society* 16:1, 63–82.** ⚠⚠ *(abstract and publisher page; full text owed before
submission)*
*In the paper:* §1 ¶3, §3 ¶8, and the close — the framing engagement, not a footnote.
*Argument:* reads Airbnb as an inhospitable form of institutional and algorithmic governance in which
platform systems render hosts visible, self-disciplining and ultimately erasable; works through the
figure of the absent Superhost and the mobile neighbour; the phrase also covers automated
substitution of human workers, while holding open a second reading of collaborative sociality.
*Adds:* the single most important item in the library. The target journal, five months before the
submission window, by the author of its founding network-hospitality line, on the paper's terrain.
It retires the claim that Riordan 2024 is the journal's nearest engagement with algorithmic
mediation. It is also the paper's best opening: she asks what becomes of hospitality when the host is
erased, and the paper asks whether the party that took over the host's functions inherited the host's
obligation. Her title poses a question this paper answers, and her frame — biopolitical,
platform-specific, focused on the human host's fate — leaves the successor's position untouched.

**Germann Molz, J. (2018). 'Discourses of scale in network hospitality: from the Airbnb home to the
global imaginary of "belong anywhere".' *Hospitality & Society* 8:3, 229–251.** ⚠
*In the paper:* §2 ¶6 — the lineage the 2026 paper extends.
*Argument:* analyses how Airbnb's scalar rhetoric, running from home to neighbourhood to "belong
anywhere," allocates responsibility, authority and belonging in network hospitality.
*Adds:* allocation of *authority and responsibility* named as the platform's rhetorical work eight
years before the paper's argument, in this journal. Citing it establishes that the paper joins a line
rather than arriving from information systems.

**Weaver, A. (2025). '"Fast hospitality" and technology: contemporaneous connections between "liquid"
and "solid" in modern times.' *Hospitality & Society*.** ⚠
*In the paper:* §7 ¶1 — the in-journal critique the seamlessness claim must be narrowed against.
*Argument:* critiques technology-driven speed in hospitality through Bauman's liquid and solid,
reading fast hospitality as corporate profit-seeking smoothing of the encounter.
*Adds:* proof that this journal has criticized the smoothing of hospitality, which is why §7's claim
narrows to seamlessness as a *design value* inside phygital frameworks. Weaver's critique is
tempo-and-political-economy; the paper's is a critique of a stated design goal on the grounds of what
it withholds from the guest.

**Gao, X., Tan, C. & Wan-Zainal-Shukri, W. H. (2026). 'Hostessing by robots? Hotel customers'
experiences of gendered robotic services.' *Hospitality & Society*, online first.** ⚠
*In the paper:* §3 ¶2 or held — the journal's robot study.
*Argument:* qualitative study of Chinese hotel guests finding that robotic service de-feminizes
hostessing and produces unexpected qualities of non-human hospitality.
*Adds:* the journal's only empirical robot-hospitality piece, and current, so referees will have read
it. Its "non-human hospitality" is affective and gendered rather than positional, which keeps it a
courtesy citation rather than a competitor — but not citing it in a paper about machines performing
hosting functions would be conspicuous.

## 4. The guest at the threshold (§2, §7)

**Edelman, B., Luca, M. & Svirsky, D. (2017). 'Racial discrimination in the sharing economy.'
*AEJ: Applied Economics* 9:2.**
*In the paper:* §2.
*Argument:* field experiment; distinctively African-American names substantially less likely to be
accepted on Airbnb.
*Adds:* the harm located in a design decision of the intermediary, beyond any individual host's
conduct — mediated exclusion as architecture.

**Cui, R., Li, J. & Zhang, D. (2020). 'Reducing discrimination with reviews in the sharing
economy.' *Management Science* 66:3.**
*In the paper:* §2 (the arresting finding), §7 (the remedy-through-the-instrument complication).
*Argument:* a single positive review statistically closes the racial acceptance gap.
*Adds:* both halves of the paper's threshold argument: negotiated access administered by an
artefact (a record the guest did not author and cannot carry elsewhere), and the remedy that
deepens the mediation — now cited with the audit's conditional-on-any-review qualifier.

**Fourcade, M. & Healy, K. (2013). 'Classification situations.' *Accounting, Organizations and
Society* 38:8.** and **Cheney-Lippold, J. (2011). 'A new algorithmic identity.' *TCS* 28:6.**
*In the paper:* §7.
*Argument:* market classification sorts life chances (Fourcade & Healy); algorithmic categories are
inferred and continuously recomputed (Cheney-Lippold).
*Adds:* respectively, the material consequences of sorting, and the reason no stable standard
exists to appeal to even in principle — the theoretical floor under torque.

## 5. Triad prior art (§1, §3) — conceded, not claimed

The dated series establishing that the three-party structure is nine years old. The paper cites
these to concede the triad in a sentence and press what none of them asks.

**Bitner, M. J., Brown, S. W. & Meuter, M. L. (2000). 'Technology infusion in service encounters.'
*JAMS* 28:1.** — technology as infused *tool*; the encounter still a dyad. Adds the earliest
antecedent and the first capacity-name in the paper's vocabulary list.

**Larivière, B., et al. (2017). '"Service Encounter 2.0".' *JBR* 79.** — technology, employee and
customer as three roles; earliest explicit three-way framing. Adds the date the triad actually
enters the literature, which disciplines every novelty claim downstream.

**van Doorn, J., et al. (2017). 'Domo arigato Mr. Roboto.' *JSR* 20:1.** — automated social
presence substituting for the employee. Adds the second capacity-name and the affect-side framing
the paper's list needs.

**Odekerken-Schröder, G., et al. (2021). 'The service triad.' *JOSM* 33:2.** — the literal term,
tested empirically with robot, customer, frontline employee. Adds the name "service triad" in
print, five years before Gursoy.

**Li, M., Yin, D., Qiu, H. & Bai, B. (2021). 'A systematic review of AI technology-based service
encounters.' *IJHM* 95.** — the "encounter triad" in hospitality's own review, with AI as mediator
or facilitator across four modes. Adds the hospitality-native concession citation, which is why it
appears in five sections.

**Gursoy, D. (2026). 'Reconceptualizing customer experience co-creation and service delivery in
the age of artificial intelligence.' *JHMM* 35:2.** ⚠ (full text still owed)
*Argument:* co-creation recast as hybrid triadic configurations of customers, employees and AI;
AI as algorithmic actor with distributed agency, transforming interpretive labour.
*Adds:* the most recent hospitality statement of the triad and the paper's nearest neighbour; his
closing division (precision to the machine, empathy to the human) draws exactly the line the paper
questions, which is why he is engaged rather than avoided.

**Xing, Y. & Zhang, J. Z. (2026). 'The algorithmic guest: AI as a co-creator in customer
experience management.' *IJCHM* 38:4.** ⚠ — AI as co-creator, the title notwithstanding. Adds the
newest capacity-name and evidence that even "guest"-titled work declines the host question.

**Belanche, D., Casaló, L., Flavián, C. & Schepers, J. (2020). 'Robots or frontline employees?'
*JOSM* 31:2.** ⚠
*In the paper:* §1, §3 (the nearest miss), §6 (guests attribute failure to the firm).
*Argument:* customers attribute responsibility for robot service failure to the firm, expecting
less improvement from the machine.
*Adds:* two services in one source — the demonstration that blame attribution is not held
obligation, and the human-accessibility evidence that automation does not relocate answerability in
the guest's eyes.

**Lee, W. & Lu, L. (2024). 'The hospitable thought that counts: an emerging theory of "AI
consciousness" in genuine hospitality.' *International Journal of Hospitality Management* 123.** ⚠
*In the paper:* §3 ¶2 — the nearest miss inside hospitality's flagship journal.
*Argument:* builds a framework in which AI service providers deliver genuine hospitality only insofar
as consumers attribute consciousness to them, with propositions comparing AI and human
hospitableness.
*Adds:* the closest single competitor to the host question, and the clearest illustration of what the
literature asks instead. It is an attributional theory — can the guest experience the machine as
hospitable — standing exactly where the normative question should be. The paper's differentiation is
one sentence: whether a party is perceived as hospitable and whether it occupies a position that owes
are different questions, and only the second has an answer that does not depend on the guest's
credulity.

**Liu, G., et al. (2026). 'Conceptualizing hospitableness in human–robot hospitality interactions.'
*International Journal of Hospitality Management*.** ⚠
*In the paper:* §3 ¶2 — the position declined by construction.
*Argument:* develops robotic hospitableness as felt welcome, attentiveness and reassurance across
robot-mediated, robot-assisted and robot-personified dimensions, casting robots as co-creators of
hospitable experience.
*Adds:* welcome treated as an experiential output to be designed rather than a duty owed. Read
alongside Lee and Lu, it shows the field has a developed vocabulary for machine hospitableness and
none for machine obligation.

## 6. Machine ethics and the obligation question (§3)

The fields where "what does a machine owe" is a live question — the paper stands on them and marks
the difference.

**Kropf, M., Spöck, C. & Werner, R. (2026). 'Blame the robot: role responsibility and ethical
issues regarding AI-based care robots.' *International Journal of Social Robotics* 18:2.** ⚠
*In the paper:* §3 — the question-type, asked for care.
*Argument:* care robots cannot bear moral responsibility but can hold *role responsibility*,
grounded in the social function they occupy; appropriate targets of thin praise and blame.
*Adds:* obligation assigned to a machine from role occupancy, without consciousness — the audit's
most consequential find, and the paper's proof that its move is a transposition, not an invention.
Care is owed in virtue of need; welcome in virtue of arrival.

**Santoni de Sio, F. & Mecacci, G. (2021). 'Four responsibility gaps with artificial
intelligence.' *Philosophy & Technology* 34:4.** ⚠
*In the paper:* §3.
*Argument:* systematizes the responsibility gap into four — culpability, moral accountability,
public accountability, active responsibility — cataloguing which obligations fail to travel when
agency moves to machines.
*Adds:* the citation that keeps the paper from restating the responsibility-gap thesis as fresh;
"active responsibility" is the forward-looking obligation the host question concerns.

**Introna, L. D. (2010). 'The "measure of a man" and the ethos of hospitality.' *AI & Society*
25:1.** ⚠
*In the paper:* §3 — the inversion.
*Argument:* Levinasian-Derridean case for an ethics of hospitality *toward* technology: ethical
dwelling with artefacts that have nothing in common with us.
*Adds:* the boundary fact stated in one sentence: philosophy of technology has theorized the
machine as the guest at the threshold and never as the one who keeps it.

**Liu, G. G., Benckendorff, P. & Walters, G. (2026). 'Conceptualizing hospitableness in
human-robot hospitality interactions.' *IJHM* 135.** ⚠
*In the paper:* §3.
*Argument:* "robotic hospitableness" in three modes (robot-mediated, robot-assisted,
robot-personified), producing felt welcome; robots as co-creators rather than replacements.
*Adds:* the newest hospitality-specific capacity name, which declines the host position *by
construction* — the strongest confirmation of the paper's vocabulary claim, cited so a
title-skimming reviewer cannot mistake it for the question already answered.

**Sharma, A. & Mattila, A. (2025). 'Rights and responsibilities of hospitality service robots.'
*Journal of Hospitality & Tourism Research*, online.** ⚠
*In the paper:* §3 ¶3 — the third duty vocabulary, and the one closest to home.
*Argument:* puts the responsibilities of hospitality service robots on the research agenda, framed as
business governance — liability, safety, data protection, consent — together with the ethics of how
humans treat robots.
*Adds:* the pattern completed. Care is owed in virtue of need, fiduciary duty in virtue of trust,
governance duties in virtue of risk. Welcome is owed in virtue of arrival, and it is the only one of
the four that constitutes the role rather than regulating it. Having a hospitality-journal source for
the governance vocabulary lets §3 make that contrast without leaving the field.

**Mestre, J. (2025). 'Hospitality and the informational at-home.' *Proceedings of the Association for
Information Science and Technology*.** ⚠
*In the paper:* §3 ¶3 — the confirmation that the reversal is unmade.
*Argument:* Derridean deconstruction in information ethics, with the human as host of the
informational at-home and privacy as what grounds hosthood against becoming hostage.
*Adds:* the check on the paper's boldest absence claim. Where Derrida meets information technology in
2025, the human is still the host and the system is still what threatens or serves that position.
Introna's machine-as-guest has not been turned over, and the paper can say so citing the place it
would have happened.

## 7. Algorithmic management and the employee half (§3)

**Rahman, H. A. (2021). 'The invisible cage.' *ASQ* 66:4.** (read in full)
*In the paper:* §3 — knowledge moves toward the intermediary.
*Argument:* an opaque evaluation regime steers freelancers' conduct precisely because it cannot be
read; workers experiment, self-constrain, and labour to satisfy criteria withheld from them.
*Adds:* control through opacity rather than command — the mechanism of the knowledge
redistribution, from the platform side.

**Calo, R. & Rosenblat, A. (2017). 'The taking economy.' *Columbia Law Review* 117.**
*In the paper:* §3.
*Argument:* platform information asymmetries are manufactured and held, constituting the
arrangement's central resource.
*Adds:* asymmetry as design rather than accident — why the withholding framework treats it as a
choice an arrangement makes.

**Möhlmann, M., Zalmanson, L., Henfridsson, O. & Gregory, R. W. (2021). 'Algorithmic management
of work on online labor platforms.' *MISQ* 45:4.**
*In the paper:* §3 — reworded by the audit: matching and control as twin dimensions.
*Argument:* platform algorithmic management spans two parallel dimensions, algorithmic matching and
algorithmic control.
*Adds:* the general form of platform direction; the audit corrected the paper's earlier temporal
gloss ("matching that has become control") to the authors' actual parallel structure.

**Christin, A. (2017). 'Algorithms in practice.' *Big Data & Society* 4:2.**
*In the paper:* §3.
*Argument:* algorithmic instruments in journalism and justice arrive as would-be substitutes for
professional judgement; practitioners buffer, ignore and game them.
*Adds:* categories of judgement relocated from practitioner to vendor's model — the adjacent-field
mechanism for the discretion redistribution.

**Lipsky, M. (1980). *Street-Level Bureaucracy*.**
*In the paper:* §3.
*Argument:* frontline workers' discretion — deciding what should be done in the particular case —
is the substance of policy as experienced.
*Adds:* the definition of what is being relocated. Without Lipsky, "discretion moves" has no
content.

**Pedersen, K. Z. & Pors, A. S. (2022). 'Discretionary responses in frontline encounters.'
*JPART* 33:1.**
*In the paper:* §3 — the qualification.
*Argument:* standardizing technologies bring rough categories that generate *new* discretionary
work as practitioners compensate for what the categories miss.
*Adds:* why displacement is the wrong word: judgement is pushed into unrecognized compensating
work — a claim that keeps §3 honest and non-determinist.

**Jianu, B., Ashton, M. & Lugosi, P. (2025). 'Integrating algorithmic management in hotels.'
*IJHM* 129.** ⚠ (Delphi)
*In the paper:* §3, §8.
*Argument:* frontline hotel managers negotiate continually between system direction and the
judgement their role demands; standardization intensifies work and obliges managers to translate
algorithmic decisions to those affected.
*Adds:* hospitality-native (expert-panel) evidence of the translator role — the manager as the
person who explains decisions neither party made.

**Spektor, F., et al. (2023). 'Charting the automation of hospitality.' *PACM HCI* 7:CSCW1.**
*In the paper:* §3.
*Argument:* interdisciplinary review of frontline hospitality automation; harms concentrate where
adoption attends to management stakeholders alone.
*Adds:* the review that names the field's worker-side blind spot — the basis for the paper's
split-verdict honesty about guest-facing evidence.

**Spektor, F., et al. (2023). 'Designing for wellbeing: worker-generated ideas on adapting
algorithmic management in the hospitality industry.' *DIS '23*.** (read in full)
*In the paper:* §1 concern, §3 — the documented case.
*Argument:* a hotel room-assignment system fixes work sequence, withholds the day's task list,
prices rooms in contractual credits, and offers a rejection affordance workers fear to use.
*Adds:* relocation of judgement documented *in a hotel* — the paper's claim ceases to be an analogy
here. NSF-repository full text; one of the few sources read whole.

**Spektor, F., et al. (2025). 'Working together: algorithmic management and peer relationships in
the hospitality industry.' *DIS '25*.** (read in full)
*In the paper:* §1, §3; its key finding underwrites §5's sovereignty construct.
*Argument:* the same platform strains peer coordination — digital assignment displaces face-to-face
delegation, disadvantages non-native English speakers, breeds workarounds.
*Adds:* the single best fact in the corpus for the competence/standing separation: the
self-sequencing affordance letting attendants reorder their own rooms was not a feature; the union
bargained it into the contract. Adjustability existed because an institution constituted the forum.

**Bendoly, E. (2013). 'Real-time feedback and booking behavior in the hospitality industry.'
*Journal of Operations Management* 31:1-2.** (read substantially)
*In the paper:* §3 — cited as a complication, not support.
*Argument:* revenue-management prescriptions function as guidelines; agents hold sanctioned
latitude, and the measurement regime, not the prescription, moves their judgement.
*Adds:* the front-desk counter-flow that keeps the discretion claim honest: the algorithm
re-anchors judgement rather than displacing it, where the work is guest-facing.

**Garcia, D., Tolvanen, J. & Wagner, A. K. (2026). 'Strategic responses to algorithmic
recommendations: evidence from hotel pricing.' *Management Science* 72:1.** ⚠
*In the paper:* §3.
*Argument:* hotel revenue managers' deviations from algorithmic prices are persistent and
anticipated by the recommendation design itself.
*Adds:* the durability of human latitude at scale — the audit's counter-flow evidence, cited so
the redistribution claim acknowledges movement in both directions.

**Scott, S. V. & Orlikowski, W. J. (2012). 'Reconfiguring relations of accountability.'
*Accounting, Organizations and Society* 37:1.**
*In the paper:* §3 — authority moves toward the rule-writer.
*Argument:* TripAdvisor materialized a new accountability relation in the travel sector;
establishments reorient conduct toward the ranking while older channels of answerability thin.
*Adds:* the triad observed in the travel sector a decade early, and the vocabulary of
accountability *relations* being reconfigured by an artefact.

**Zervas, G., Proserpio, D. & Byers, J. (2021). 'A first look at online reputation on Airbnb.'
*Marketing Letters* 32:1.** and **Teubner, T., Hawlitschek, F. & Adam, M. (2019). 'Reputation
transfer.' *BISE* 61:2.**
*In the paper:* §3.
*Argument:* platform ratings inflate and concentrate near the top (Zervas); reputation correlates
only weakly across platforms (Teubner).
*Adds:* why leaving is expensive by design — standing that does not travel locks the host in,
compounding the authority shift.

**Fuller, L. & Smith, V. (1991). 'Consumers' reports: management by customers in a changing
economy.' *Work, Employment and Society* 5:1.** ⚠
*In the paper:* §3 — the craft paragraph's lineage.
*Argument:* firms enlist customer evaluations as a labour-control instrument — management by
customers.
*Adds:* thirty-five years of priority for the control form the platforms instrumented; converts
the paper's felt-control argument from novelty claim to old form, new instrument.

**Spektor, F., Fox, S. E., Min, S., Sarfo, G., Stringam, B., Riordan, C. A., Rho, H. J., Begleiter, B.
& Forlizzi, J. (2025). 'Working together: algorithmic management and peer relationships in the
hospitality industry.' *Proceedings of DIS 2025*.** ⚠
*In the paper:* §3 ¶6–7 — the hotel-floor evidence.
*Argument:* study of unionized hotel housekeeping on the US West Coast finding that an algorithmic
management tool disrupts communication and coordination among workers even when carefully configured,
with design strategies proposed for relational service work.
*Adds:* the strongest available evidence that the disruption is structural rather than a
configuration failure, and it is set in hotels rather than gig platforms. The unionized setting also
does work for §5: these are workers with conferred standing, which makes the contrast with the guest
sharper.

**Krzywdzinski, M., et al. (2024). 'Between control and participation: the politics of algorithmic
management.' *New Technology, Work and Employment*.** ⚠
*In the paper:* §3 ¶5 — the knowledge redistribution.
*Argument:* algorithmic management in conventional logistics produced centralization of knowledge and
disempowerment of workers even where surveillance was not the intent.
*Adds:* the redistribution decoupled from bad intent, which is what the paper's argument requires. It
lets §3 say the movements happen by design rather than by design failure, and without any claim about
what managers wanted.

**Keegan, A., et al. (2025). 'Algorithmic management in organizations? From edge case to center
stage.' *Annual Review of Organizational Psychology and Organizational Behavior*.** ⚠
*In the paper:* §4 ¶1 — the scaffolding under the Bovens translation.
*Argument:* reviews algorithmic management's move from gig-economy edge case to mainstream
organizational phenomenon and theorizes a gray zone of actors ambiguously inside or outside
organizational boundaries.
*Adds:* the reason the paper's accountability translation is not ad hoc. Okhuysen and Bechky's
accountability is task clarity among colleagues; the guest is not a colleague, and the review supplies
the general form of that problem — the field already recognizes that algorithmic management reaches
parties the organization does not employ.

## 8. Coordination theory and the automation ladder (§4)

**Okhuysen, G. A. & Bechky, B. A. (2009). 'Coordination in organizations: an integrative
perspective.' *Academy of Management Annals* 3:1.**
*In the paper:* §4 — the derivation's spine.
*Argument:* any coordinating mechanism must produce accountability, predictability and common
understanding.
*Adds:* the three integrating conditions from which the withholding inversion, the substitutive
condition and ultimately the five affordances are derived. The audit added the translation
sentence distinguishing their task-accountability from Bovens' answerability.

**Parasuraman, R., Sheridan, T. B. & Wickens, C. D. (2000). 'A model for types and levels of human
interaction with automation.' *IEEE SMC-A* 30:3.** ⚠
*In the paper:* §4 — conceded and distinguished.
*Argument:* automation is gradable by type and level of what it takes from the human operator.
*Adds:* the human-factors lineage the paper's condition must acknowledge; distinguished on four
grounds — one-dimensional, operator-inside-the-loop, no dimension for silent rule movement, none
for answerability.

**Raisch, S. & Krakowski, S. (2021). 'Artificial intelligence and management: the
automation-augmentation paradox.' *AMR* 46:1.** (read in full)
*In the paper:* §4.
*Argument:* automation and augmentation cannot be cleanly separated at task-allocation level; they
are interdependent across time and organizational levels.
*Adds:* the non-separability thesis, absorbed as motivation: if the designer-side distinction
dissolves, the place to draw it is the encounter, where what this guest could discover, anticipate
and contest are answerable questions.

**Kim, S., et al. (2021). 'Preference for robot service or human service in hotels.' *IJHM* 93.**
and **Hou, Y., Zhang, K. & Li, G. (2021). 'Service robots or human staff.' *Tourism Management*
83.**
*In the paper:* §4 — the human-preference floor and its conditionality.
*Argument:* guests broadly accept service robots yet prefer human staff for emotional dimensions
and service failure (Kim); the preference shifts with social crowding rather than expressing fixed
attachment (Hou).
*Adds:* the empirical basis for "the design question is where a person must remain reachable" —
stated conditionally, as the evidence is.

**Hemmer, P., Schemmer, M., Vössing, M. & Kühl, N. (2025). 'Complementarity in human-AI
collaboration: concept, sources, and evidence.' *European Journal of Information Systems*.** ⚠
*In the paper:* §4 ¶1 — the published rival, cited and differentiated.
*Argument:* formalizes complementary team performance — the human-AI pair must outperform both the
human alone and the AI alone — grounds it in information and capability asymmetry, and reviews
evidence showing complementarity is rare.
*Adds:* the one published checkable condition in this space, which the paper must engage or a referee
will. Three differences carry the engagement: theirs is an ex-post performance test, ours an ex-ante
diagnostic; theirs is defined over organization-internal decision tasks, ours over guest-facing
touchpoints; and a performance metric has no place for answerability to a party outside the
organization, which is the condition the paper's third withholding turns on.

**Yuan, Y., Hao, F. & Liu, S. (2026). 'Augment or replace? AI implementation and employee job
insecurity.' *International Journal of Contemporary Hospitality Management* 38:8, 2503–2522.** ⚠
*In the paper:* §4 ¶1 — the hospitality stipulation.
*Argument:* three scenario experiments with US and UK hospitality employees manipulating front-of-house
AI as replacement or augmentation; both raise job insecurity, replacement more, mediated by
identity-value threat and moderated by technology readiness.
*Adds:* the nearest hospitality operationalization of the distinction, and it stipulates the
distinction as an experimental manipulation rather than deriving a criterion for it — which is
precisely the gap §4 fills. Its finding that augmentation also produces insecurity independently
supports the non-separability the paper inherits from Raisch and Krakowski.

**Hatherley, J. (2025). 'A moving target in AI-assisted decision-making: dataset shift, model
updating, and the problem of update opacity.' *Ethics and Information Technology* 27, art. 20.** ⚠
*In the paper:* §4 ¶2 and §6 ¶3 — the predictability inversion, named.
*Argument:* model updating introduces a distinct kind of opacity in which users cannot know how or why
an update changed a system's reasoning; standard explainability remedies are ill-equipped for it;
canvasses bi-factual explanations, dynamic model reporting and update compatibility.
*Adds:* the concept the paper's predictability argument has been describing without a name. Update
opacity also does work in §6: it explains why announced change is a separate affordance rather than a
subset of transparency, since a system can be fully explained today and silently different tomorrow.

## 9. Folk theories, algorithmic competence, and the constructs (§5)

**Jhaver, S., Karpfen, Y. & Antin, J. (2018). 'Algorithmic anxiety and coping strategies of
Airbnb hosts.' *CHI '18*.**
*In the paper:* §5 — the capacity documented in hospitality.
*Argument:* Airbnb hosts reverse-engineer search ranking, build folk theories, compare notes, and
orient to two audiences at once — the guest and the algorithm.
*Adds:* hospitality algorithmacy observed before it was named, in an accommodation setting; the
double-audience finding is the construct's clearest field expression.

**Eslami, M., et al. (2016). 'First I "like" it, then I hide it: folk theories of social feeds.'
*CHI '16*.**
*In the paper:* §5.
*Argument:* users construct folk theories of opaque curation and reorganize conduct around them
even without economic stakes.
*Adds:* the general form of interpretation under opacity — evidence the competence belongs to the
mediation form, not to precarity.

**Bishop, S. (2019). 'Managing visibility on YouTube through algorithmic gossip.' *New Media &
Society* 21:11-12.** and **Cotter, K. (2019). 'Playing the visibility game.' *NM&S* 21:4.**
*In the paper:* §5.
*Argument:* folk theories circulate socially into semi-institutionalized practice (Bishop);
influencers treat visibility as an inferable, contestable game (Cotter).
*Adds:* the social circulation and strategic-play dimensions of the competence — what
interpretation looks like when it matures.

**Ytre-Arne, B. & Moe, H. (2021). 'Folk theories of algorithms.' *Media, Culture & Society*
43:5.**
*In the paper:* §5.
*Argument:* folk theorizing is general across a representative population sample.
*Adds:* generality — the competence is not a platform-worker specialty.

**DeVito, M. A., et al. (2017). '"Algorithms ruin everything".' *CHI '17*.** and **DeVito, M. A.
(2021). 'Adaptive folk theorization as a path to algorithmic literacy on changing platforms.'
*PACM HCI* 5:CSCW2.** ⚠
*In the paper:* §5.
*Argument:* folk theorizing sharpens when systems change without notice (2017); adaptation to
change is the core of algorithmic literacy itself (2021).
*Adds:* the priors for the tracking component — which is why §5 claims no novelty of content for
its components and differentiates on derivation from withholdings alone.

**Christ-Brendemühl, S. & Schaarschmidt, M. (2019). 'Frontline backlash: service employees'
deviance from digital processes.' *Journal of Services Marketing* 33:7.**
*In the paper:* §5.
*Argument:* technology-induced role ambiguity drives frontline staff to deviate from digital
processes in constructive and destructive directions.
*Adds:* employee-side competence and its limit — deviation can rescue an encounter without altering
who decides.

**Cheng, M., Zhang, L. & Wang, H. (2025). 'The effect of artificial intelligence awareness on
frontline service employees' silence.' *IJCHM* 37:5.** ⚠
*In the paper:* §2 (context), §5 (the sharper finding), §8.
*Argument:* AI awareness increases frontline hotel employees' silence, mediated by perceived
psychological-contract breach.
*Adds:* the paradox the paper builds on: the employees who understand the system best may be
precisely those who stop speaking about it. P8 established that this registers an increment on a
pre-existing baseline.

**Zhou, L., Lei, X., Liu, M., Huang, X. & Hou, R. (2025). 'Algorithmic competency of on-demand labor
platform workers: scale development, antecedents, and consequences.' *Asia Pacific Journal of Human
Resources* 63:2.** (read in full, key sections; open access)
*In the paper:* §5 ¶1 — the collision, cited and turned.
*Argument:* develops and validates the first scale of algorithmic competency across five samples of
Chinese on-demand platform workers, with four dimensions: understanding algorithmic management (its
exemplar is folk theorizing — "I develop theories about task-allocating and score-calculating
algorithms based on my own experience"), embracing it, leveraging it, and remediating its
deficiencies. Competency predicts customer-oriented service behaviour and gig-work identification.
*Adds:* the reason §5 must argue rather than assert its decomposition, and the best available reason
for coordinative sovereignty. Three differentiators hold: the construct is worker-only and
gig-specific; embracing is willingness to trust, an attitude rather than a competence, which is why
the scale cannot carry a normative argument; and remediating folds the capacity to appeal into
individual competency, which is exactly the conflation the paper exists to undo. The capacity to
lodge an appeal is not the standing to be answered, and their scale measures the first while the
construct name promises the second.

**Gagrčin, E., Naab, T. K. & Grub, M. F. (2024). 'Algorithmic media use and algorithm literacy: an
integrative literature review.' *New Media & Society*.** ⚠
*In the paper:* §5 ¶1 — the licence for a domain-specific decomposition.
*Argument:* integrative review of 169 studies framing algorithm literacy through experiential
learning; states that the field lacks defined core competencies and calls for task- and
domain-specific approaches.
*Adds:* the field asking for what the paper supplies. It converts "we propose three components" from
an assertion into a response, and it establishes that the absence of specification and tracking from
existing definitions — Dogruel's four components, Swart's triad, Cotter's practical knowledge — is a
gap the field has itself noticed.

**Lin, H. (2025). 'Oscillation between resist and to not? Users' folk theories and resistance to
algorithmic curation on Douyin.' *Social Media + Society*.** ⚠
*In the paper:* §5 ¶5 — the separation, at its sharpest.
*Argument:* walkthrough and diary-interview study of 31 users showing that folk theories are espoused
as resistance resources while behaviour contradicts them; resistance stays constrained within the
dominant use of the platform's affordances, partly through digital resignation in the face of strict
platform regulation.
*Adds:* competence documented and its non-conversion into influence documented in the same study.
This is the empirical shape of the paper's central distinction, and it forecloses the reading that
better-informed users would simply do better.

**Draper, N. A., Hoffmann, C. P., Lutz, C., Ranzini, G. & Turow, J. (2024). 'Privacy resignation,
apathy, and cynicism: introduction to a special theme.' *Big Data & Society*.** ⚠
*In the paper:* §5 ¶5 — resignation detached from ignorance.
*Argument:* the current statement of the digital-resignation line, theorizing resignation, apathy and
cynicism as structurally cultivated stances rather than knowledge deficits.
*Adds:* the defence against the paper's most likely misreading. If resignation followed from not
understanding, the answer would be education, and the affordance division would collapse into
training. The lineage's own position is that competent users resign because of what the arrangement
offers them, which is the paper's claim in the privacy register.

## 10. Voice, exit, and hospitality labour (§5, from P8)

**Hirschman, A. O. (1970). *Exit, Voice, and Loyalty*.**
*In the paper:* §5 — the organizing distinction for coordinative sovereignty.
*Argument:* responses to organizational decline run through exit or voice, moderated by loyalty.
*Adds:* the frame in which mediation-you-cannot-exit makes voice the only remaining route — and the
scheme Zientara et al. bring home to hospitality.

**Dowding, K., John, P., Mergoupis, T. & Van Vugt, M. (2000). 'Exit, voice and loyalty: analytic
and empirical developments.' *EJPR* 37:4.**
*In the paper:* §5.
*Argument:* sharpens EVL's analytic distinctions and empirical record.
*Adds:* the caveat structure that keeps the paper's use of Hirschman current rather than nostalgic.

**Morrison, E. W. (2014). 'Employee voice and silence.' *Annual Review of Organizational
Psychology and Organizational Behavior* 1.**
*In the paper:* §5 — voice in the sense that matters.
*Argument:* voice and silence are distinct, multiply-motivated behaviours; channels that dignify
decisions already taken differ from consequential input.
*Adds:* the distinction between process-feature voice and voice that reaches someone able to act —
load-bearing for the sovereignty construct. (Morrison's 2023 decade update is the flagged upgrade.)

**Jung, H. S. & Yoon, H. H. (2019). 'The effects of social undermining on employee voice and
silence.' *Journal of Service Theory and Practice* 29:2.** ⚠
*In the paper:* §5 — the baseline.
*Argument:* undermining by supervisors, coworkers and customers each depresses hotel employees'
voice and raises silence.
*Adds:* the guest as one of three documented suppressors of voice before any algorithm — the
triadic suppression fact.

**Al-Hawari, M. A., Bani-Melhem, S. & Quratulain, S. (2020). 'Abusive supervision and frontline
employees' attitudinal outcomes.' *IJCHM* 32:3.** ⚠
*In the paper:* §5.
*Argument:* silence mediates abusive supervision into reduced capacity to satisfy customers.
*Adds:* silence as the sector's existing transmission mechanism between managerial conduct and
service outcomes — the channel the algorithm later occupies.

**Papadopoulos, O., Lopez-Andreu, M. & Jamalian, M. (2021). 'Violation and lack of awareness of
employment rights in the UK's hotel industry.' *Industrial Relations Journal* 52:4.** ⚠
*In the paper:* §5 — the structural baseline.
*Argument:* fragmentation, isolation and insecure status make silence the dominant response to
grievance in UK hotels; the individual-rights model has "no substance" for precarious workers.
*Adds:* the strongest single warrant for the compounding claim: suppression documented as the
sector's baseline state, independent of technology, in a Western hotel labour market.

**Zientara, P., Adamska-Mieruszewska, J. & Bąk, M. (2023). 'Unpicking the mechanism underlying
hospitality workers' intention to join a union and intention to quit.' *IJHM* 108.** ⚠
*In the paper:* §5.
*Argument:* Hirschman-framed UK survey; dissatisfaction predicts intention to quit and does not
predict intention to unionize.
*Adds:* exit-over-voice demonstrated in hospitality, in the paper's own theoretical vocabulary.

**Rydzik, A. & Kissoon, C. S. (2021). 'Decent work and tourism workers in the age of intelligent
automation and digital surveillance.' *Journal of Sustainable Tourism* 30:12.** ⚠
*In the paper:* §5 — the anticipation.
*Argument:* automation and surveillance risk exacerbating existing precarisation and shifting power
further toward employers, absent worker-centric regulation.
*Adds:* the compounding claim stated in a tourism-native venue — argued, not measured, and cited at
exactly that strength.

**Lin, W., Zhang, M., Zhang, W. & Zhang, C. (2026). 'Will employees still speak up under algorithmic
management? The differential effects of distinct algorithmic functions — evidence from the Meituan
platform in China.' *Systems* 14:5, 569.** (read in full; open access)
*In the paper:* §5 ¶3 — the citation that keeps the P8 claim honest.
*Argument:* 351 matched employee-supervisor pairs; algorithmic directing, scheduling and monitoring
reduce voice through lowered felt responsibility for constructive change, while algorithmic feedback
raises it; the moderator tested is work locus of control.
*Adds:* the quantitative nearest neighbour, and the proof that the interaction P8 named remains
untested. Its design moderates on an individual disposition and contains no climate construct at all,
so §5 can say the interaction is open and point at the study that came closest without testing it.
The differential finding — feedback raises voice where direction suppresses it — also supports the
paper's refusal to issue a verdict on the technology.

**Duggan, J., Dasgupta, P., McDonnell, A., Carbery, R. & Sherman, U. (2026). 'Tensions in algorithmic
HRM: worker voice and organizational silencing in app-based platform work.' *International Journal of
Human Resource Management* 37:8, 1432–1465.** ⚠
*In the paper:* §5 ¶3 — the mechanism, qualitatively.
*Argument:* qualitative study of food-delivery work finding that algorithmic HRM control fosters
enforced silence and voicelessness — an inability to express concerns or contest decisions — with
non-organizational actors compounding or mitigating it, and frustration running to cynicism and
detachment.
*Adds:* silence named as *enforced* rather than chosen, which is the version of the claim the paper
needs, and a second literature converging on the same reading as Cheng et al. 2025 from a different
method.

## 11. Accountability, contestation, and the affordances (§5, §6)

**Bovens, M. (2007). 'Analysing and assessing accountability: a conceptual framework.' *European
Law Journal* 13:4.** (read in full)
*In the paper:* §4 (translation sentence), §5 (the relational definition).
*Argument:* accountability is a relationship between an actor and a forum: the actor owes
explanation; the forum can question and judge.
*Adds:* the canonical definition the paper's competence/standing separation rests on — cited, per
the audit, instead of argued fresh.

**Metcalf, J., Singh, R., Moss, E., Tafesse, E. & Watkins, E. A. (2023). 'Taking algorithms to
courts.' *FAccT '23*.** ⚠
*In the paper:* §5.
*Argument:* algorithmic accountability is relational; assessment regimes work only where a forum
holds standing against the actor.
*Adds:* the relational reading pressed into algorithmic governance — and the neighbouring use of
"standing" the sovereignty construct distinguishes itself from.

**Citron, D. K. & Pasquale, F. (2014). 'The scored society.' *Washington Law Review* 89.**
*In the paper:* §5.
*Argument:* scoring systems owe the scored due process.
*Adds:* the legal register of the same point — what is owed is procedural, which no guest skill
can self-supply.

**Ananny, M. & Crawford, K. (2018). 'Seeing without knowing.' *New Media & Society* 20:3.**
*In the paper:* §5, §6 — the normative objection to transparency.
*Argument:* the transparency ideal fails as accountability: seeing inside a system does not create
the capacity to act on what is seen.
*Adds:* disclosure-without-audience — the null that forces transparency to be specified with
standing attached.

**Edwards, L. & Veale, M. (2017). 'Slave to the algorithm?' *Duke Law & Technology Review* 16.**
*In the paper:* §6 — the legal objection.
*Argument:* an individual right to explanation underdelivers; attention belongs on systemic,
ex-ante obligations.
*Adds:* the "transparency fallacy" and the redirect toward design-time duties — why explanation
binds the designer rather than waiting on a guest who thinks to ask.

**Vaccaro, K., Sandvig, C. & Karahalios, K. (2020). '"At the end of the day Facebook does what it
wants".' *PACM HCI* 4:CSCW2.** ⚠ (full text owed; "outcomes constant" unverified)
*In the paper:* §5, §6 — the empirical null that sets the bar.
*Argument:* appeal designs tested against a no-appeal baseline produced no improvement in perceived
accountability; participants contested goals and automation itself.
*Adds:* the finding that a grievance channel internal to the rule-writer absorbs contest instead of
transferring standing — the bar every contestability design must clear.

**Martin, K. & Waldman, A. (2022). 'Are algorithmic decisions legitimate?' *Journal of Business
Ethics* 183:3.** (read in full)
*In the paper:* §6 — the post-null positive.
*Argument:* large-sample vignette studies; appeals were the only governance mechanism conferring
legitimacy on adverse algorithmic decisions, while oversight and audit lowered it.
*Adds:* the legitimacy dividend of appeal — and a second null for mere oversight — which sharpens
rather than overturns the Vaccaro bar.

**Yurrita, M., et al. (2023). 'Disentangling fairness perceptions in algorithmic
decision-making.' *CHI '23*.** ⚠
*In the paper:* §6, twice.
*Argument:* contestability raises perceived procedural fairness; human oversight raises nothing.
*Adds:* the pair of findings that both support contestability and hand human accessibility its
fresh null — oversight without authority moves nothing, hence "the person is not the affordance;
the authority is."

**Lee, M. K., et al. (2019). 'Procedural justice in algorithmic fairness.' *PACM HCI* 3:CSCW.** ⚠
*In the paper:* §6.
*Argument:* outcome control — letting affected parties adjust algorithmic outcomes — improved
perceived fairness across all tested conditions.
*Adds:* adjustability's best evidence, and the precedent for deriving interface requirements from a
justice theory.

**Almada, M. (2019). 'Human intervention in automated decision-making.' *ICAIL '19*.** and
**Alfrink, K., Keller, I., Kortuem, G. & Doorn, N. (2023). 'Contestable AI by design.' *Minds and
Machines* 33.**
*In the paper:* §6.
*Argument:* contestation must be designed across a system's lifecycle, not bolted onto its end
(Almada); contestability is specifiable as a design framework (Alfrink et al.).
*Adds:* the constructive alternative after the nulls — contestability reaching the rule, with a
reviewer holding authority to reverse.

**Hewagama, G., Boxall, P., Cheung, G. & Hutchison, A. (2019). 'Service recovery through
empowerment?' *IJHM* 81.** ⚠
*In the paper:* §6.
*Argument:* hotels grant complaint-handling authority by rank; empowerment in recovery is rationed.
*Adds:* the hospitality-native fact that authority to reverse is already an organizational
variable — claim 20 in miniature, inside the industry.

**Yeung, K. (2017). '"Hypernudge": Big Data as a mode of regulation by design.' *Information,
Communication & Society* 20:1.**
*In the paper:* §6 — adjustability's foil.
*Argument:* big-data-driven choice architectures regulate by continuous, personalized nudging.
*Adds:* why an unadjustable default path is choice architecture and not choice.

**Lv, L., et al. (2024). 'Information autonomy in personalized travel recommendation.'** ⚠ and
**Morosan, C. & DeFranco, A. (2016). 'Modeling guests' intentions to use hotel apps.' *IJCHM*
28:9.**
*In the paper:* §6.
*Argument:* privacy concern falls and attitudes improve where presentation preserves the
traveller's sense of autonomy over her information (Lv); hotel-app acceptance runs through
perceived control (Morosan & DeFranco).
*Adds:* the mechanism behind adjustability — guests object to personalization they cannot steer,
a pattern the hotel literature has carried for a decade.

**Shen, Z. & Jin, L. (2024). 'Bargaining with algorithms.' *Journal of Retailing* 100:3.** ⚠
*In the paper:* §5 — the precision paragraph.
*Argument:* five studies; consumers do make counteroffers to algorithms, adjust them less than
against humans, defer to perceived algorithmic precision, with the deference strongest among
lower-income consumers.
*Adds:* the finding that forced the counterparty claim's reformulation and now supports it: the
addressee survives automation; deference to it deepens, unevenly by income.

**Denegri-Knott, J., Zwick, D. & Schroeder, J. E. (2006). 'Mapping consumer power.' *European
Journal of Marketing* 40:9-10.** (read in full)
*In the paper:* §5 — the boundary.
*Argument:* consumer power divides into sovereignty (choice and exit), cultural power (de Certeau's
tactics), and discursive power.
*Adds:* the tradition "coordinative sovereignty" must be distinguished from — aggregate market
power against encounter-level standing — plus the de Certeau precursor to the tactical-guest
reading, credited rather than discovered.

**Bayamlıoğlu, E. (2022). 'The right to contest automated decisions under the GDPR: beyond the
so-called "right to explanation".' *Regulation & Governance* 16:4.** ⚠
*In the paper:* §5 — the legal counterparty.
*Argument:* GDPR article 22(3)'s guarantee of human intervention, expression of view and
contestation is a due-process provision, with a two-layer transparency framework for implementing
it.
*Adds:* the statutory near-enactment of the paper's ask-decline-explain verbs — the reason the
counterparty claim must be stated as authority-over-rules rather than absence of any addressee.

**Shryock, A. (2012). 'Breaking hospitality apart: bad hosts, bad guests, and the problem of
sovereignty.' *JRAI* 18:S1.** ⚠
*In the paper:* §5.
*Argument:* hospitality is a test of sovereignty — enacting autonomy and exchange, openness and
closure, in one social space.
*Adds:* the anthropological prior on sovereignty-and-hospitality; cited so the paper's coordinative
case enters a conversation rather than a vacuum.

**Fink, M. (2025). 'Human oversight under Article 14 of the EU AI Act.' SSRN working paper 5147196.**
(read in full)
*In the paper:* §6 ¶4 — the anchor for the authority distinction.
*Argument:* a pro forma human who rubber-stamps fails Article 14's effectiveness standard; meaningful
oversight requires genuine authority to override; overseers without it become liability sponges,
absorbing responsibility without control; oversight also serves procedural rights — a reasoned
decision, a hearing, an effective remedy.
*Adds:* the paper's own distinction, arrived at independently and in legal form. "Liability sponge" is
the reachable person without authority, named. Working paper status is the one caution: check for
journal placement before submission, and do not lean on it alone where a peer-reviewed source will do.

**Sterz, S., Baum, K., Biewer, S., Hermanns, H., Lauber-Rönsberg, A., Meinel, P. & Langer, M. (2024).
'On the quest for effectiveness in human oversight: interdisciplinary perspectives.' *Proceedings of
FAccT 2024*.** ⚠
*In the paper:* §6 ¶4 — token oversight made nameable.
*Argument:* oversight is effective only when the overseer has causal power over the system, epistemic
access to it, self-control, and fitting intentions.
*Adds:* a four-part test that turns "meaningful oversight" from a slogan into something a property can
fail. It sits between Yurrita's oversight null and Fink's legal standard and gives §6 its criterion.

**Li, H. & Sun, Z. (2025). 'Is algorithmic accessibility sufficient? The pivotal role of accessibility
and accountability in shaping trust in automated decision-making.' *Governance* 38:4.** (read in
part, full text passages)
*In the paper:* §6 ¶4 — the closest published analogue to the paper's distinction.
*Argument:* defines algorithmic accessibility as openness of the process to contestation and shows it
is not sufficient on its own; accountability — appeal, redress, an answerable party — is pivotal for
trust, working through procedural justice.
*Adds:* an empirical demonstration that access without an answerable party does not produce what
access is supposed to produce, in the same Lind and Tyler tradition §7 already uses for voice. It is
the paper's affordance division tested in a governance setting.

**Yurrita, M., Verma, H., Balayn, A., Alfrink, K., Gadiraju, U. & Bozzon, A. (2025). 'Identifying
algorithmic decision subjects' needs for meaningful contestability.' *Proceedings of the ACM on
Human-Computer Interaction* 9 (CSCW).** ⚠
*In the paper:* §6 ¶3 — the contestability affordance's strongest new ally.
*Argument:* 21 interviews with short-term rental hosts facing an illegal-holiday-rental detection
system; decision subjects need collaborative sense-making, support in contesting, and clarity about
who is accountable; contestability is framed as cooperative work, individual and collective.
*Adds:* the contestability literature arriving in a hospitality-adjacent setting, with subjects who
are hosts. Its finding that subjects need to know *who is accountable* before they can contest is the
paper's counterparty argument in the users' own words.

**Hirsbrunner, S. D., Kleemann, S. & Tahraoui, M. N. (2025). 'Contestation in artificial intelligence
as a practice.' *Frontiers in Communication*.** ⚠
*In the paper:* §6 ¶3 — the friendly amendment.
*Argument:* argues that contestability by design is too system-centred; legal obligations and
technical transparency may not be enough to enable contestation, which requires structural capability
on the stakeholder's side, organizational culture and legal context; distinguishes institutionalized
from situative bottom-up contestation.
*Adds:* the paper's own division — some affordances individuals can supply and some only institutions
can — stated from the design side. Citing it prevents §6 from reading as a claim that contestability
can be built into an interface.

**Choi, J. & Chao, M. M. (2024). 'For me or against me? Reactions to AI (vs. human) decisions.'
*Personality and Social Psychology Bulletin*.** ⚠
*In the paper:* §6 ¶4 — the productive complication.
*Argument:* six experiments, N = 2,794, finding that when the outcome is unfavourable, AI deciders are
perceived as fairer than humans, attributed to perceived unemotionality; reminders of algorithmic bias
erase the gap.
*Adds:* evidence against a warm-body reading of human accessibility, which the paper should welcome
rather than manage. A guest turned down by an algorithm may not want a person as such; what she wants
is someone who can change the answer. The finding pushes the affordance toward authority, which is
where the argument was already going.

**Pigac, T., Lee, A. & Huang, A. (2026). 'Navigating transparency in AI-powered luxury hospitality: a
dynamic guest-centric approach.' *Cornell Hospitality Quarterly* 67:3, 283–297.** ⚠
*In the paper:* §6 ¶1 — the nearest published guest-facing design framework.
*Argument:* 50 guest interviews yielding a dynamic transparency protocol — tiered disclosure adapted
to guest segment and journey stage — in which low-digital-comfort guests want human-mediated
disclosure while digitally fluent guests want dashboards and traceability.
*Adds:* convergent empirical support for transparency at the point of effect, and the measure of what
is left. It covers one of five affordances, frames transparency as trust management rather than as an
answer to a coordination withholding, and has nothing on adjustability, announced change,
contestability or bypass. Citing it is how §6 shows its contribution is a set and a derivation rather
than a list.

## 12. Seamlessness, friction, and torque (§7)

**Star, S. L. & Ruhleder, K. (1996). 'Steps toward an ecology of infrastructure.' *Information
Systems Research* 7:1.** and **Star, S. L. (1999). 'The ethnography of infrastructure.' *American
Behavioral Scientist* 43:3.**
*In the paper:* §7.
*Argument:* infrastructure becomes effective as it sinks out of sight (1996); classifications
carry a master narrative, a presumed point of view rendered as the shape of the blanks (1999).
*Adds:* seamlessness read as that sinking pursued deliberately — the political mechanism of the
cost's invisibility.

**Bowker, G. C. & Star, S. L. (1999). *Sorting Things Out*.**
*In the paper:* §7 — torque.
*Argument:* classification systems bend lives that do not fit them; the felt twisting is torque.
*Adds:* the name for what the non-fitting guest experiences — the concept the algorithmic case
industrializes.

**Costanza-Chock, S. (2020). *Design Justice*.** (chapter read)
*In the paper:* §7 — the documented case.
*Argument:* design encodes the matrix of domination; the airport body scanner that must be told
male or female reads any non-fitting body as an anomaly, whichever button is pressed.
*Adds:* torque at travel's own threshold with no negotiation surface at all — the strongest
documented instance of the paper's exception-foreclosure claim.

**Lind, E. A., Kanfer, R. & Earley, P. C. (1990). 'Voice, control, and procedural justice.'
*JPSP* 59:5.** (read in full)
*In the paper:* §7 — the repaired voice anchor.
*Argument:* voice offered after a decision, explicitly incapable of altering it, still raises
fairness judgements — value-expressive, non-instrumental voice is real.
*Adds:* the evidence that voice has standing-value independent of outcome influence, which is what
frictionless design actually withholds.

**Folger, R. (1977). 'Distributive and procedural justice.' *JPSP* 35:2.** (read in full)
*In the paper:* §7 — cited for the interaction, post-audit.
*Argument:* voice combined with outcome improvement produced *lower* fairness than improvement
alone — the frustration effect.
*Adds:* the conditionality: voice read as never having borne on anything backfires. The audit
caught the paper citing this for the opposite; it now carries the condition, which strengthens the
argument.

**Goodwin, C. & Ross, I. (1992). 'Consumer responses to service failures.' *JBR* 25:2.** (read in
full)
*In the paper:* §7.
*Argument:* voice paired with tangible redress shapes fairness perceptions in service recovery;
voice without bearing disappoints.
*Adds:* the frustration effect's service-domain instance — the conditionality holds where the paper
lives.

**Padigar, M., Li, Y. & Manjunath, C. N. (2024). '"Good" and "bad" frictions in customer
experience.' *Psychology & Marketing* 42:1.**
*In the paper:* §7 — the consumer-research ally, with the narrowing owned.
*Argument:* four friction types by task desirability and value; removing constructive friction can
destroy the value it obstructed, and some frictions are valued for their own sake.
*Adds:* the in-discipline warrant that friction removal has costs — the paper deliberately sets
aside the effort-valued cases and keeps only the negotiation-occasion argument.

**Phillips, C., Russell-Bennett, R. & Kowalkiewicz, M. (2024). 'The physical frictionless
experience.' *The Service Industries Journal* 44:13-14.** ⚠
*In the paper:* §7.
*Argument:* frictionless retail service erodes experience memorability.
*Adds:* the cost of smoothness extending beyond the guests a system fails to fit — smoothness
costs even its beneficiaries something.

**Chalmers, M. & Galani, A. (2004). 'Seamful interweaving.' *DIS '04*.**
*In the paper:* §7 — the design lineage.
*Argument:* seams — visible joins and imperfections — are resources for action; revealing them lets
people work with a system as well as through it.
*Adds:* the design-theory position that makes the seamlessness critique constructive rather than a
complaint.

**Nguyen, Q., Yankholmes, A., Ladkin, A. & Osman, H. (2024). 'National stereotypes in the
cross-cultural service encounter.' *Tourism Review* 80:7.** ⚠
*In the paper:* §7.
*Argument:* hotel staff categorize guests by nationality pre-arrival and run scripted encounters;
mismatch produces service failure and on-the-spot re-scripting.
*Adds:* the cultural scripting problem documented pre-automation — and the improvisational moment
algorithmic categorization removes.

**Mattila, A. (1999). 'The role of culture in the service evaluation process.' *JSR* 1:3.** and
**Torres, E. N., Fu, X. & Lehto, X. (2014). 'Examining key drivers of customer delight.' *IJHM*
36.** and **Walters, G., et al. (2021). 'Commercial hospitality in tourism: a global comparison of
what culturally matters.' *IJHM* 95.** (Walters read in full)
*In the paper:* §7.
*Argument:* cultural background shapes what counts as good service (Mattila; Torres); twelve facets
of commercial hospitality differ significantly across 2,248 tourists from Asia-Pacific and Europe
(Walters).
*Adds:* cultural variation in service expectations from single-site to at-scale — the ground truth
algorithmic norm-fitting flattens.

**Wang, P. Q. (2024). 'Personalizing guest experience with generative AI in the hotel industry.'
*Current Issues in Tourism* 28:4.** ⚠
*In the paper:* §7.
*Argument:* hotel managers doubt generative systems can carry a specific hospitality culture or
respond to contingency.
*Adds:* practitioner scepticism from inside the industry — the managers' own version of the
paper's contingency argument.

**Filippas, A., Horton, J. J. & Golden, J. (2022). 'Reputation inflation.' *Marketing Science*
41:4.** ⚠
*In the paper:* §7.
*Argument:* platform ratings inflate over time until they carry less information.
*Adds:* the named pattern for reputation remedies degrading their own signal — cited so the paper
does not coin what platform economics already named.

**Ehsan, U., Liao, Q. V., Passi, S., Riedl, M. O. & Daumé III, H. (2024). 'Seamful XAI:
operationalizing seamful design in explainable AI.' *Proceedings of the ACM on Human-Computer
Interaction* 8 (CSCW).** ⚠
*In the paper:* §7 ¶4 — the post-Chalmers ally.
*Argument:* co-design with 43 practitioners and end-users showing that revealing seams — the
sociotechnical gaps a system's design papers over — helps users anticipate harms and augments their
agency, rather than degrading the experience.
*Adds:* seamfulness converted from an aesthetic preference into an agency argument, which is exactly
§7's move, made twenty years after Chalmers and Galani and in the AI setting. It is the citation that
prevents the friction argument reading as nostalgia.

**Natali, C., Naiseh, M., Cabitza, F. & Frischmann, B. M. (2025). 'Better AI with designed friction:
theories, applications and research agenda.' IOS Press.** ⚠
*In the paper:* §7 ¶4 — friction as the mechanism of oversight.
*Argument:* argues that seamless-UX orthodoxy undermines oversight, and catalogues cognitive forcing
functions, seamful design and programmed friction as deliberate inefficiencies that foster engagement,
critical reasoning and user agency.
*Adds:* the bridge between §6 and §7. If meaningful oversight requires the overseer to notice, and
seamless design is built so that nothing is noticed, then the seamlessness critique and the
affordances are one argument rather than two.

**Chen, Z. & Schmidt, R. (2024). 'Exploring a behavioral model of "positive friction" in human-AI
interaction.' DUXU, HCII 2024, Springer.** ⚠
*In the paper:* §7 ¶4 — the named strand.
*Argument:* a behavioural model of when deliberate friction benefits users and systems — pause,
reflection, error-catching — across user, AI and designer perspectives.
*Adds:* the term of art. It lets the paper say that a design literature on positive friction exists
and that it has not reached hospitality, which is a cleaner claim than arguing friction's value from
first principles.

**Mameli, E., Scarles, C., Stangl, B. & Frohlich, D. (2026). 'A comprehensive framework for phygital
tourism experiences.' *Information Technology & Tourism* 28:1.** ⚠
*In the paper:* §7 ¶1 — the gap, demonstrated at its most current.
*Argument:* integrative framework for phygital tourism experience design built from 57 articles and 84
industry cases.
*Adds:* the newest phygital framework, treating seamlessness as an unexamined goal with no discussion
of friction anywhere in it. It is how §7 shows the gap is present rather than historical.

**Andreev, H., Kosmas, P., Livieratos, A. D., Theocharous, A. L. & Zopiatis, A. (2025). 'Destination
(un)known: auditing bias and fairness in LLM-based travel recommendations.' *AI* 6:9, 236.** ⚠
*In the paper:* §7 ¶3 — the cultural case, updated.
*Argument:* audit of two large language models across 216 traveller profiles finding measurable bias
in every category tested across six bias families, with a public-interest re-ranking layer proposed.
*Adds:* the Nguyen line brought forward to generative systems, with the scripting now measured rather
than inferred. Every category tested is the phrase that does the work.

**Gao, Z. & Thebault-Spieker, J. (2026). 'Is your chatbot a tourist or a townie? Quantifying
geographic and localness disparities in LLM representations of place.' *Proceedings of the ACM on
Human-Computer Interaction*.** ⚠
*In the paper:* §7 ¶3 — the sharpest formulation available.
*Argument:* over 12,000 question-answer pairs showing that language models carry an urban advantage
and fail on relational, community-held knowledge of place.
*Adds:* the mediating system shown to be structurally a tourist — competent at what is written down
about a place and incompetent at what is known by living there. For a paper about whether a machine
can host, this is close to a demonstration in a different register, and the phrasing is a gift.

## 13. Well-being and outcomes (§8, from P7)

**Anderson, L. & Ostrom, A. L. (2015). 'Transformative service research: advancing our knowledge
about service and well-being.' *JSR* 18:3.**
*In the paper:* §8 — the TSR anchor.
*Argument:* TSR's remit spans individuals, employees, families, communities, society and ecosystem,
with indicators of both increasing and decreasing well-being at its centre.
*Adds:* the licence for the editor's positive/negative framing as orthodoxy, and the bridge from
this paper to the special issue's PSR ancestry.

**Galeone, A. & Sebastiani, R. (2021). 'Transformative service research in hospitality.' *Tourism
Management* 87.** ⚠
*In the paper:* §8.
*Argument:* hospitality organizations realize transformative potential for individual and
collective well-being across hedonic and eudaimonic dimensions.
*Adds:* the individual/collective split inside hospitality — the levels framing without the
automation link, which is exactly the half-gap the paper claims.

**Uysal, M., Sirgy, M. J., Woo, E. & Kim, H. (2016). 'Quality of life (QOL) and well-being
research in tourism.' *Tourism Management* 53.**
*In the paper:* §8.
*Argument:* the standard review separating tourist QOL from resident and community QOL.
*Adds:* the route from encounter-level well-being to population scale without inventing the bridge.

**Pan, S.-Y., Lin, Y. & Wong, J. W. C. (2025). 'The dark side of robot usage for hotel
employees.' *Tourism Management* 106.** ⚠
*In the paper:* §8 — the negative valence, employee side.
*Argument:* robot risk awareness predicts workplace withdrawal and lower intention to stay in
hospitality; the authors recommend augmentation over automation.
*Adds:* the paper's augmentative argument stated in a *Tourism Management* paper's own operational
recommendation.

**Nayak, S., Budhwar, P. & Malik, A. (2025). 'Unveiling the hidden costs of AI in hospitality.'
*IJHM* 129.** ⚠
*In the paper:* §8.
*Argument:* algorithmic HRM raises stress and erodes well-being and commitment among hospitality
workers.
*Adds:* the negative valence for algorithmic management specifically, hospitality-native.

**Christou, P., Simillidou, A. & Stylianou, M. C. (2020). 'Tourists' perceptions regarding the
use of anthropomorphic robots.' *IJCHM* 32:11.** ⚠
*In the paper:* §8 — the ambivalence.
*Argument:* 78 interviews; guests favour anthropomorphic robots while reporting frustration and
sadness at their use in a human-driven industry.
*Adds:* the guest-side evidence that something recognition-shaped is at stake — genuinely
two-directional, which serves the three-valence requirement honestly.

**Parkinson, J., Schuster, L. & Mulcahy, R. (2022). 'Online third places.' *JSR* 25:1.** (read in
full)
*In the paper:* §8 — the design-dependence finding.
*Argument:* technologically mediated third places produce both community bonds and well-being *and*
isolation and fragmentation, with the direction set by identifiable design choices.
*Adds:* structurally the paper's own claim — which outcome obtains depends on design — demonstrated
for belonging under mediation, and the best single source in the outcome cluster.

**Riordan, T. (2024). 'Digitally mediated hospitality and algorithmic hostility in the platform
economy.' *Hospitality & Society* 14:3.** ⚠
*In the paper:* §3 (the journal's name for the negative pole), §8 (the societal register).
*Argument:* multi-sited ethnography of platform food-delivery work; proposes a *virtual domain*
extending Lashley's three and *algorithmic hostility* as hospitality's counter-concept at the
human-digital frontier.
*Adds:* the target journal's own prior theorization of algorithmic mediation — the concept the
paper extends into the phygital hotel, and the highest fit-signal citation in the corpus.

---

**Moganadas, S. R., Goh, G. G. G., Cheah, C. S. & Shidik, G. F. (2026). 'Navigating employee
well-being in the age of digital transformation: a PRISMA-based systematic review.' *Societies* 16:7,
213.** (read in full; open access)
*In the paper:* §8 ¶2 — the first half of the absence claim, cited rather than asserted.
*Argument:* PRISMA review of 57 articles from 2014 to 2025 on digital transformation and employee
well-being, organized into digital transformation conditions, resources and demands, mediating
processes, contextual factors and well-being outcomes; concludes that well-being depends on how
intensified demands and resources are configured and interpreted in context, and that prior findings
remain fragmented across technologies, disciplines and constructs.
*Adds:* a 2026 systematic review covering AI and algorithmic systems that stays entirely at the
individual level. The paper's claim that automation evidence has not met collective well-being
evidence now rests on a review's own scope rather than on the paper's failure to find something.

**Dar, H., Singh, K. & George, B. (eds) (2026). *Tourism Technology, Sustainability, and Local
Community Empowerment*. Routledge.** ⚠
*In the paper:* §8 ¶2 — the other half.
*Argument:* examines how smart tourism technologies — AI, internet of things, big data, digital
platforms, smart infrastructure — can produce more inclusive and empowered communities.
*Adds:* technology tied to community-level empowerment with no individual well-being outcome in view.
Held beside Moganadas it shows the two literatures are adjacent and unjoined, which is a stronger
claim than either makes alone.

**Park, S., Lee, J. Z. & Lehto, X. Y. (2026). 'Transforming hotel lobbies via community-centered
design: crafting a vibrant social hub for guests.' *Journal of Hospitality & Tourism Research* 50:2,
170–187.** ⚠
*In the paper:* §8 ¶2 — the proof that the levels can meet.
*Argument:* choice-based conjoint study of lobby design elements integrating local community
character, finding that preferred combinations build sense of place and community among local and
non-local guests and bridging design attributes to guest well-being.
*Adds:* individual well-being and community joined in one hospitality study, through physical design
and without any automation. It converts the absence from a limitation of the field's ambition into a
specific gap: the levels meet when hospitality designs space, and have not met when it designs
algorithms.

## Held, not cited — forty-five verified entries in reserve

Grouped by why they are held. Every entry is Crossref- or publisher-verified with read depth in
the bib; none may enter the manuscript on its note alone.

**Editor corpus, held for positioning depth:** Batat (2024b) research paradigm (read in full;
methodological, cite if a reviewer asks where agency sits in the paradigm); Batat (2026b) HFPV
(ecosystem-level governance — the level-of-analysis differentiator); Mosca & Chiaudano (2020)
(the extension-of-brand-control position, engaged in prose without citation at present — add if §7
names it); Mosca & Chiaudano/Batat chapters (2022, 2024) (institutional connective tissue);
De Vos et al. (2021) mixed emotions/credence services (the knowledge-redistribution point in
credence-goods clothing); Corinaldesi (2025) (the only secondary source naming PH-CX's structure).

**Triad prior art, concession already carried by cited members:** Robinson et al. (2020)
(explicitly dyadic 2×2 — kept to *prevent* miscitation; third verification catch); Wirtz et al.
(2018) frontline robots typology; Fan et al. (2024) chatbot-employee triad; van Doorn et al.
(2023) CAW framework (was cited in an earlier draft §3; superseded by the tighter concession
list); Roederer et al. (2026) AI as third agent; Zheng et al. (2025) phygital tourism triad
(name-collision item; full text retrievable by hand from Surrey); Suh (2026) phygital ecosystems;
Mieli et al. (2024) phygital time geography; Kaliyamurthy & Schau (2025) algorithmic constraint;
Zha et al. (2024) (checked: its paradoxes do not include smoothness — held to prevent re-checking).

**Hospitality theory bench:** Lugosi (2021) hospitality-tourism nexus (register exemplar;
cite-ready); Gill et al. (2022) ordinary welcome editorial; Anastasiadou et al. (2024) hospitable
destinations (fit-signal only, first cut); Moysidou & Stanley (2023) gendered homestay power;
Paloniemi (2024) sharing-economy hospitality; Ariffin (2013) (verified lead, content
uncharacterized — read before citing); Shryock's companion Candea & da Col (2012); Ladegaard
(2021) and Spier (2024) (round-1 guest-side bench); Ert et al. (2016) host photos and trust.

**Algorithmic management bench:** Jianu et al. (2025) 'The toll of resisting' (content unverified
at depth — the modelled exit terminus is P8-relevant; obtain full text); Kamalahmadi et al. (2021)
restaurant JIT scheduling (servers reduce upselling — strongest §3 bench player); Mutari & Figart
(2026) configuration-dependence; Cheon & Erickson (2025) warehouse work-games; Griesbach et al.
(2019) control as spectrum; Vieira & Junte (2025) algorithmic brokers (online-first, recheck at
proof); Burrell (2016) opacity taxonomy (cut from §3 in trim; restore if the chosen-vs-intrinsic
opacity distinction is needed).

**Outcome bench:** Della Corte et al. (2023) robot trust + its 2024 corrigendum (cite together or
not at all); Tussyadiah et al. (2020) robot trust in *Annals*; Rosenbaum et al. (2007) third-place
attachment; Feng et al. (2023) connectedness pathway (does not test automation — never cite as if
it does); Lei et al. (2024) 'Touch over tech' (human-accessibility floor; was cited pre-trim);
Li et al. (2019) AI awareness and turnover (first cut against Pan et al.); Yu & Margolin (2024)
record-less minority hosts (bridge host-to-guest explicitly if used); Addis et al. (2022) CFP-core
food experience design; Tlili et al. (2023) metaverse (CFP-core only).

**Do not cite:** the two Algorithmacy Lab anchors — unretrievable by referees and deanonymizing
under blind review; held for internal provenance, enforced by the render guard.
