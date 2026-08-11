# Claims registry

The controlled vocabulary for the `claims` field on every card. A card says which of these claims its
source carries; `build_index.py --check` rejects any slug not listed here, and the by-section rollup
in [`CARDS_INDEX.md`](CARDS_INDEX.md) is generated from these assignments.

The point of the registry is that "contextual bibliography" should mean something operational. Sorted
alphabetically, a bibliography tells you nothing. Sorted by the claim each source is doing work for,
it answers the question a reviewer actually asks: *what is holding this sentence up?*

A slug records what the manuscript claims, not what is established. When a source turns out not to
carry the claim filed under it, the slug stays and the row says so — `voice-independent-of-outcome`
is the live example — because renaming it would hide the disagreement the library exists to surface.

Add a slug only when the manuscript makes a claim no existing slug covers. Retire one by removing it
here and from every card that used it — `--check` will find any you miss.

| slug | § | the claim it carries |
|---|---|---|
| `framing-argued-past` | 1 | Phygital scholarship treats the technology as an instrument whose consequences turn on design quality and guest acceptance |
| `hospitality-exceeds-service` | 1, 2 | Hospitality is a relational and culturally situated practice, not the efficient provision of services |
| `four-criteria` | 2 | Welcome, recognition, care and negotiated access are constitutive of hospitality rather than enhancements to it |
| `hospitality-not-outcomes` | 2 | A stay that proceeded without incident is not thereby a stay in which anyone was received |
| `conditional-hospitality` | 2 | Every real hospitality sets conditions; the question is who sets them and whether they can be discussed |
| `not-that-triad` | 2, 3 | Existing hospitality and service triads place a context or a participant third; ours places a party that commits binding determinations |
| `platform-unsettled-hosting` | 2 | Platform accommodation already displaced the host, directing conduct while conferring no standing |
| `negotiated-access-by-artefact` | 2 | Whether a guest is received now turns on a record she did not author and cannot carry elsewhere |
| `dual-place-process` | 3 | Digitalization turns the guest's conduct into record; physicalization turns the intermediary's determinations into physical arrangement |
| `withholdings-at-the-crossings` | 3, 4 | The three withheld conditions occur at the crossings between realms, which is what makes the account phygital rather than merely digital |
| `caw-rival` | 3 | The consumer–autonomous technology–worker framework shares the augmentation observation; the conditions are what this paper adds |
| `knowledge-redistribution` | 3 | Knowledge moves to the intermediary, and the asymmetry is manufactured rather than incidental |
| `discretion-redistribution` | 3 | Discretion moves away from the frontline employee, into unrecognized compensating work rather than out of existence |
| `authority-redistribution` | 3 | Authority moves to whoever writes the rules, and non-portable reputation makes leaving expensive by design |
| `integrating-conditions` | 4, 6 | Any coordinating mechanism must produce accountability, predictability and common understanding |
| `poles-as-three-withholdings` | 4 | Substitutive hospitality is mediation under which all three withholdings hold together; augmentative is where they do not |
| `wellbeing-valence` | 4 | The poles carry consequences for well-being at individual, collective and societal registers |
| `neutral-as-habitual-value` | 4, 7 | Experienced neutrality is what substitutive hospitality feels like when working as designed, and is therefore a measurement problem |
| `algorithmacy-observed` | 5 | The competence is documented rather than invented, including in a hospitality setting |
| `accountability-is-a-relation` | 5, 6 | Understanding and predictability are states a party can be in; accountability is a relation no competence reaches |
| `employee-voice-silence` | 5 | Employees hold the same competence and meet the same limit; awareness of the system increases silence |
| `exit-voice-standing` | 5 | Influence runs through leaving or being heard, and leaving becomes unavailable once its costs are raised |
| `affordances-derived` | 6 | The five affordances answer withheld integrating conditions rather than being enumerated |
| `published-nulls` | 6 | Transparency, appeal and the individual right to an explanation each fail in their naive form |
| `institutional-not-trainable` | 6 | Contestability and human accessibility require a grant of authority, not training |
| `human-contact-conditional` | 4, 6 | Guests prefer human staff for emotional dimensions and service failure, conditionally rather than universally |
| `industry-gains-and-transition` | 6 | Phygital arrangements deliver real gains, and the framework sorts the transition difficulties they create |
| `roadmap-not-procurement` | 6 | The transformation sequence cannot be discharged by purchase; the remainder are decisions about who answers |
| `voice-independent-of-outcome` | 7 | Being heard reduces experienced injustice independently of whether the outcome improves — **contested; see [`folger1977voice`](cards/folger1977voice.md), whose source reports an interaction rather than independence** |
| `infrastructure-sinks-from-sight` | 7 | Infrastructure becomes effective as it disappears, which is seamlessness pursued as a design goal |
| `torque` | 7 | The felt twisting when a life is bent to a classification built for someone else |
| `cultural-scripts` | 7 | Guests are categorized before arrival and run from a matching script; mismatch produces failure |
| `constructive-friction` | 7 | Removing effort that is undesirable but valuable destroys the value it was thought to obstruct |
| `remedy-same-instrument` | 7 | The remedy for algorithmic exclusion runs through the same instrument as the harm |
| `limits-and-agenda` | 8 | What the paper does not claim, and the empirical work that would test it |
| `host-question-unasked` | 1, 3 | No account asks whether the algorithmic party occupies a position that owes the guest a welcome; the field has vocabularies for machine hospitableness, role responsibility and governance duty, and none for the duty that constitutes the host's role |
| `guest-obligation-untheorized` | 2 | Commercial hospitality theorizes what the host owes and not what the guest owes — **narrowed 2026-08-11; see [`manfreda2025reciprocal`](cards/manfreda2025reciprocal.md), which theorizes gratitude-driven reciprocation, and [`shi2025residents`](cards/shi2025residents.md), which measures a guest-to-host flow** |
| `competence-not-standing` | 5 | Competence with an algorithmic system is learned and standing to be answered is conferred, and no quantity of the first produces the second |
| `seamlessness-uncritiqued` | 7 | The phygital frameworks state seamlessness as a design goal and have not questioned it as such, while questioning technocentrism, efficiency logics, speed and AI's harms around it |
| `wellbeing-levels-unmet` | 8 | Individual-level automation evidence and collective-level well-being evidence have not met inside a single study |
| `editors-own-ground` | 1, 2, 3, 4, 5, 6, 7, 8 | The claim is established, approached or contested in the special issue editors' own published work before any general literature is called |
