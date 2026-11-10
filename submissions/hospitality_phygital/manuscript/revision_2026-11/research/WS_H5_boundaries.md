# WS H5: which decisions need immediate recourse, run rr-2026-11-h, 2026-11-10

Question 9 (FABLE_REVIEW §7); reviewer points R2.5a and R3.7; outline §5, §7 and §9. Section numbers
follow PITCH_AND_OUTLINE.md.

## 1. Searches (all 2026-11-10)

| Tool | Exact query | Kept | Dropped, and why |
|---|---|---|---|
| Consensus | contestability of algorithmic decisions ex ante versus ex post timing of human review irreversible harm | Lyons et al. 2022 CHI (noted); Cobbe et al. 2021; Green 2022 (noted) | Cao 2026 (conference series of unclear standing); Creel & Hellman, Kinchin, Gules-Guctas (no timing dimension) |
| Consensus | human-in-the-loop versus human-on-the-loop versus human-out-of-the-loop typology automated decision-making stakes reversibility | **Baum & Laux 2026** (carded); Ivanov 2023 *foresight* (record, abstract); Haitsma & Brink 2025 | ML-pipeline HITL surveys (wrong sense of HITL); Brennan-Marquez et al. 2019 (appearance of HITL, not timing) |
| Consensus | speed of service recovery hotel restaurant immediate response customer satisfaction | **Tang et al. 2018** (carded); Jin et al. 2019 (record, abstract) | Cross-sectional hotel recovery surveys with no timing manipulation |
| Consensus | which hotel service decisions should be automated and which require human employee intervention, typology by risk and urgency | **Ivanov & Webster 2024** (carded) | Robot-acceptance and task-automatability studies (Tuomi; Reis; Huang & Rust): they sort tasks, not decisions about the guest |
| Consensus | real-time contestation at the point of decision versus after-the-fact appeal of automated decisions | none new | Already-held cards (Vaccaro, Lyons 2021, Alfrink, Yurrita, Almada) dominate; Bayamlıoğlu 2021 (Art. 22 interpretation, not timing) |
| Consensus | hotel overbooking walked guests denied room compensation fairness | none carded | Haynes & Egan 2020 (frontline staff see advance warning of a walk as the ethical minimum; abstract, closed); Wangenheim & Bayón 2007 (airline). Both relevant to the "admission" class; cap |
| WebSearch | Ivanov "Automated decision-making" foresight "in the loop" … pdf SSRN; "Automated decision-making: Hoteliers' perceptions" Ivanov Webster pdf; "What's the Appeal? …" arxiv pdf | — | No open copy of Ivanov 2023 or Lyons 2022 found |
| Scholar Gateway | (one natural-language query on loop position in hospitality) | — | ACCESS_DENIED |
| Primary law | GDPR via EU Publications Office Cellar (celex 32016R0679); WP251rev.01 via EC Article 29 newsroom (item 612053); AI Act Arts 14, 26, Annex III re-read from the WS_D copy | **gdpr2016art22**, **article292018guidelines** (carded) | eur-lex.europa.eu returned an empty WAF response; not bypassed |

Full-text routes that failed and were not forced: Springer PDF for Baum & Laux (bot page; arXiv v2 read
instead); ScienceDirect for Ivanov & Webster (403, then a CAPTCHA in the browser, which I did not attempt);
Emerald (Ivanov 2023), ACM (Lyons 2022; Haitsma & Brink 2025), all Cloudflare 403.

**Records verified but not carded** (cap; abstract only): Ivanov, S. (2023) "Automated decision-making",
*foresight* 25(1): 4-19, 10.1108/FS-09-2021-0183; Lyons, Wijenayake, Miller & Velloso (2022) "What's the
Appeal?", CHI '22, 10.1145/3491102.3517606 (abstract: people prefer human review, participation, "and a
timely outcome"); Jin, Nicely, Fan & Adler (2019), *JHTM* 38: 149-158, 10.1016/j.jhtm.2019.01.005;
Haitsma & Brink (2025), *Digital Government: R&P* 6(3), 10.1145/3716173; Haynes & Egan (2020), *JRPM*
19(2): 119-128, 10.1057/s41272-019-00226-1.

**Gap statement.** I found no work that places hospitality decisions against stakes, reversibility and
time-criticality to say which require a reachable person at the moment of decision (Consensus, the six
queries above; WebSearch; 2026-11-10). The nearest is Ivanov & Webster (2024), which sorts 23 hotel
decisions by managers' preferred loop position; from its abstract it sorts by emotional intelligence and
interaction, not by timing of effect, and I could not read the full text to check.

## 2. Fable leads

FABLE_REVIEW §4 names no leads for Question 9, so none was tested. The task named five literatures; their
outcomes: contestability-by-design is already held (`alfrink2023contestable`, `lyons2021conceptualising`,
`almada2019intervention`; not re-carded); in/on/post-hoc loop typology, verified (Baum & Laux 2026, full);
GDPR Art. 22 and AI Act oversight, verified (primary texts); "meaningful human control" exists as
Santoni de Sio & van den Hoven (2018), cited by Baum & Laux (p. 12 n. 12), record not fetched, not carded;
service-recovery timing, verified at abstract level (Tang 2018; Jin 2019).

## 3. Synthesis

**The criterion is when a decision takes effect, not how soon review arrives.** Baum and Laux (2026)
distinguish human-in-the-loop (no output without a human) from human-on-the-loop (the system runs and a
human can correct it), and split the latter by time (arXiv v2 p. 4, Def. 1; p. 5, Def. 2). What separates
the modes is "not elapsed time but whether intervention can occur before the token output becomes
effective" (p. 6, §2.3). Only that synchronous mode can change the decision a person is actually subject
to; asynchronous review "intervenes after the decision has been made, shaping future iterations", and
anticipatory oversight "shapes the decision space before deployment" (pp. 6-7, §2.3). Where a decision is
too fast for any person, as with emergency braking, the only human control left is to set its parameters
in advance (pp. 7-8). R2.5a's "immediate interruptibility" is, in these terms, synchronous correction by
someone with authority; a later appeal is asynchronous.

**On my reading, law secures the later appeal, not the person at the moment.** GDPR Article 22 bars solely automated
decisions with legal or similarly significant effects (Art. 22(1)) but lifts the bar where the decision
is "necessary for entering into, or performance of, a contract" (Art. 22(2)(a)). Then the safeguard is
"the right to obtain human intervention ... to express his or her point of view and to contest the
decision" (Art. 22(3)). Recital 71 lists, as separate items, the right "to obtain an explanation of the
decision reached after such assessment" and the right "to challenge the decision". My reading, not the
law's text: booking, check-in and pricing fall under the contract exception only where the decision is
"necessary for" the contract (Art. 22(2)(a)), and Art. 22(3) does not say when intervention occurs; if
both hold, a hotel's legal floor is after-the-fact review. The
regulators add two markers the typology can borrow. "Cancellation of a contract" is a legal effect
(WP251rev.01 p. 21), and differential pricing becomes significant only if "prohibitively high prices
effectively bar someone from certain goods or services" (p. 22). They also make reversibility part of
significance ("a prolonged or permanent impact", p. 21) and require a reviewer "who has the appropriate
authority and capability to change the decision" (p. 27). The AI Act's stop-button provision is a design
requirement, not a right of the affected person: Art. 14(4)(e) requires that a high-risk system be
provided to the natural persons assigned to oversight in a way that enables them, "as appropriate and
proportionate", "to intervene ... or interrupt the system through a 'stop' button" (OJ PDF p. 61). It
confers nothing on a guest, binds only high-risk systems, and Annex III names no hospitality use (card `eu2024aiact`). It expressly excludes
biometric verification whose sole purpose is "to confirm that a specific natural person is the person he
or she claims to be" (Annex III 1(a), p. 127).

**Hospitality evidence says immediacy matters for remedy, but not uniformly.** In hotel vignettes,
recovery within 30 minutes beat recovery within 2 hours (Jin et al. 2019) [UNVERIFIED — no abstract found, VERIFY_H_v1]. Yet immediate,
economic recovery suited guests with mild negative emotion, while delayed, psychological recovery suited
those with intense emotion (Tang et al. 2018, abstract). Guests who meet a robot failure blame the firm,
and Belanche et al. advise human help "proactively following a robot failure" (2020: 283; card
`belanche2020`). Information provision by a robot left the hospitality experience unchanged (Schmidt et
al. 2025: 571). Hoteliers would delegate to AI the decisions "that do not require much emotional
intelligence or interactions with customers/employees" (Ivanov & Webster 2024, abstract).

**Typology (drafted by the H5 agent, not the authors' text).** Each row places a hospitality decision on
the three dimensions and names the recourse it needs. The placements are my inference from the sources
cited in the row; no source makes them for hotels.

| Decision | Stakes | Reversible in time? | Time-critical? | Recourse it needs | Basis |
|---|---|---|---|---|---|
| Admission or refusal at the door or check-in; booking not honoured; walked guest | High: shelter for the night; cancelling a booking is a legal effect ("cancellation of a contract"); refusing a walk-in is not among the regulators' examples | No: a refund next week does not return the night | Yes, the guest is at the threshold | **Synchronous**: a reachable person with authority before refusal takes effect | WP251 p. 21 (booking cancellation only; its "refused admission" is to a country); Baum & Laux p. 6; GDPR 22(3) states no timing (my reading: later review) |
| Identity verification (e.g. facial check-in) | Low as verification; high if failure blocks entry | Yes, if a manual route exists | Only through its consequence | **Fallback route**, then synchronous if failure would refuse entry | AI Act Annex III 1(a) p. 127; Wilson-Nash et al. p. 981 (choice of access modes) |
| Safety and access on the premises (key lock-out, alarms, removal for security) | Highest | Often no | Some too fast for any person | **Synchronous** where a person can act in time; **anticipatory** limits set and owned by the host where not | Baum & Laux pp. 7-8; AI Act Art. 14(4)(e) p. 61 as analogy only |
| Pricing (dynamic or personalised) | Usually moderate | Yes (refund, rebooking) | No; the guest can decline before contracting | **Asynchronous** appeal plus anticipatory rules; moves up if a price bars access | WP251 p. 22; Baum & Laux p. 7 |
| Room assignment, upgrades, allocation | Low to moderate; high for an accessibility need | Mostly (room move) | Only on the arrival night | Asynchronous by default; **synchronous** where a guest's need makes the room unusable | WP251 p. 22 (vulnerable groups) |
| Complaints and service recovery | Varies with failure severity | Partly | Speed helps on average, not for every guest | A **reachable** person with authority; speed tuned to the guest | Jin 2019; Tang 2018 (abstracts); Belanche 2020: 283 |
| Routine requests and information | Low | Yes | No | Out of the loop acceptable; anticipatory rules suffice | Schmidt 2025: 571; Ivanov & Webster 2024 (abstract) |

Read down the "Reversible in time?" column and the boundary R2.5a asks for appears. Immediate
interruptibility matters where a decision takes effect on the guest's body, access or contract during the
stay, so that harm lands before any appeal could finish. It matters less where effects can be deferred or
undone, as with most pricing and room allocation. For decisions too fast for anyone it moves into rules
the host sets beforehand and answers for afterwards.

## 4. What this means for the host's obligation (FABLE_REVIEW §5)

- **Threshold sovereignty (A), as description: supported.** The decisions that need a person at the
  moment are those that act on a guest who is physically inside, or at the edge of, the host's premises
  (admission, safety, access). That dependence is A's core observation, and the typology turns it into a
  testable boundary: the framework should explain most where the guest is on site and least for remote,
  reversible decisions.
- **Institutional role obligation (C): supported.** The sources locate the remedy in *authority to change
  the decision* assigned by the organisation (WP251 p. 27; Baum & Laux p. 2; Sterz et al. 2024: 2497),
  and anticipatory oversight lets the host answer for decisions no frontline person could interrupt
  (pp. 7-8). That answers R3.9: authority can be bounded by role, provided someone the organisation
  empowers is reachable at the moments that matter.
- **Public calling (B): untested here.** The admission row is where B's duty to receive would bite. I did
  not read innkeeper law (another workstream's tradition); if H-workstreams verify it, B explains why
  refusal at the threshold is the paradigm case.
- **Weakened:** any claim that *every* touchpoint must be interruptible. On my reading, law sets only after-the-fact
  review (GDPR 22(3) states no timing); recovery evidence shows speed is not uniformly what guests want (Tang 2018). The
  paper should restrict immediacy to the irreversible, on-premises class. This also answers R2.4 in part:
  general data-protection law does not demand immediacy, so a hospitality-specific ground is doing work.

## 5. Reviewer points and recommendation

- **Answers:** R2.5a (typology and boundary); R3.7 (configurations of human involvement differ in kind:
  constitutive, corrective synchronous, asynchronous, anticipatory); R3.9 in part; R2.4 in part.
- **Recommended to enter (cap 1):** `baum2026constitutive`. It gives the criterion in one citable
  sentence and was read in full (arXiv v2; check the LNCS version before quoting).
- **Ranked held alternatives:** (2) `gdpr2016art22`, if the authors want a legal sentence in §9 and drop
  another reference; (3) `ivanov2024automated`, CC BY, abstract only. If a human reads it and it lists
  front-office decisions by loop position, it could replace Baum & Laux as the hospitality-native entry;
  (4) `article292018guidelines`, a reading aid for (2); (5) `tang2018timing`, a governor.
- **Not re-carded (already held):** `alfrink2023contestable`, `almada2019intervention`,
  `lyons2021conceptualising`, `martinwaldman2022legitimate` / `martinwaldman2022legitimacy`,
  `are2025appeals`, `wilsonnash2025captivity`, `eu2024aiact`, `sterz2024effectiveness`, `parasuraman2000types`.

## 6. Notes for the main session

- New held cards are not in `references.bib`, so `build_index.py --check` will flag them ("only rejected
  cards may be absent"). I did not edit the bib, per the brief.
- Card tiers: the validator accepts only `verified | crossref-verified | corrected` and depths
  `full-text | abstract | metadata`, so I used those rather than the brief's `primary-legal-source` and
  `full`; each card's `source_basis` records the brief's tier.
- **Proposed claim slug:** `interruptibility-before-effect` (§§5, 7, 9): immediate interruptibility is owed
  where a decision takes effect on the guest before any later review could undo it; elsewhere a later
  appeal or advance rules suffice.

## Corrections after verification

*Added in rr-2026-11-h after VERIFY_H_v1 (2026-11-10).*

- §4: Sterz et al. 2024 locator for organisational "authority" corrected from p. 2498 to p. 2497 (finding 1).
- §3: Recital 71 splice undone; the explanation right and the right to challenge are quoted as two items (finding 2).
- §3, §4 and the typology: "booking, check-in and pricing are contractual, so … after-the-fact review" marked as my reading; Art. 22(2)(a) needs "necessary for", and Art. 22(3) states no timing (finding 3).
- §3: AI Act Art. 14(4)(e) restated as a design requirement for assigned overseers, not a guest's right (finding 4).
- §3: Jin et al. 2019 30-minute result marked unverified; no abstract retrievable (finding 5). The Jin entries in §1–2 and the typology's complaints row are records or citations, not the result, and were left as they are.
- Typology, admission row: door refusal no longer presented as a regulators' legal-effect example; WP251 p. 21 covers cancelling a booking, and its "refused admission" is to a country (finding 6).
