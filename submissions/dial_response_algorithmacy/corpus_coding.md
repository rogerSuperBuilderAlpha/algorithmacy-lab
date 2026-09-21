# Corpus coding sheet — algorithmacy interfaces in the DIAL corpus

**Status:** coding record for [`draft.md`](draft.md) (2026-09-21). Every `[A#]` and `[M#]` tag in the article resolves to a row here and to Appendix A of the draft.

## Design

This is a secondary re-coding of a fixed published corpus. Belousov, Macey, Bujić, Ojell-Järventausta and Hamari (2027) analysed 25 science-fiction novels (their Table 1 / Table A.1, indexed A1–A25) for digitally induced altered states of consciousness. I hold their corpus fixed and re-code it against a different inclusion criterion, then extend it with the six works already catalogued in [`../scifi_interfaces_algorithmacy/works/`](../scifi_interfaces_algorithmacy/works/) (indexed M1–M6).

### Inclusion criterion — cooptive commit

A scene qualifies when both hold:

1. **An algorithmic third party sits between a party and a counterpart.** The mediator has a rule of its own that transforms what passes through it; it is a party, not a wire. The counterpart may be another person, a population, or the party's own later state (internal reach).
2. **A party is depicted reading or writing that mediator's commitments** — inferring or inspecting its rule, or rewriting its state through a designed or subverted channel.

Belousov et al.'s criterion (input discrepancy: signals from one system yield content associated with another) is neither necessary nor sufficient here. A neuromod that flattens grief qualifies for them; it qualifies for me only if the scene shows the party or someone else reading or writing the mod's rule.

### Framework — reach × act

| | **Read: interpretive** | **Read: structural** | **Write: sanctioned** | **Write: subversive** |
|---|---|---|---|---|
| **Internal reach** (state the party alone later meets) | 1 Folk theorizing | 2 Backend reading | 5 Training by response | 6 Subversive affordance |
| **External reach** (state other parties later meet) | 3 Shared folk theory | 4 Audit | 7 Operator commit (a: centralized; b: distributed) | 8 Protocol shipping |

### Evidence tags

- `extract` — the scene is quoted or paraphrased in Belousov et al. (2027) §4–5 or summarised in their Table A.1. Section given.
- `canon` — the scene is not in their article but is a well-documented, widely discussed scene of the work; page-checkable by any reader with the book.
- `to verify` — my recollection of the work supplies the reading; it should be checked against the text before submission. Phrased conditionally in the draft.
- `thin` — the work contains an algorithmic mediator by their criterion but no scene of a party reading or writing its rule that I can support. Reported as such.

Coder: Roger Hunt, with drafting assistance from a coding agent; single coder, no inter-rater check. See draft §3.3 and §6.

---

## A. Belousov et al.'s corpus

### A1 — *A Memory Called Empire* (Martine, 2019)

Mediator: the imago machine — a neural implant carrying a predecessor's memories and personality, merged with each new host so that the line persists across bodies. Table A.1 summary.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Mahit integrates Yskandr's imago; integration reshapes the line the next host inherits | 5 Training by response → leaks to 7b | `extract` (A.1 summary) | Internal write whose product is external by design |
| The imago is sabotaged before installation by a Lsel official | 7a Operator commit | `canon` | Write access held by the station's council, not the host |
| Mahit and Yskandr negotiate control of shared memory and affect after the malfunction | 2 Backend reading | `to verify` | Host inspecting the imago's rule from inside |

### A2 — *Altered Carbon* (Morgan, 2002)

Mediator: cortical stack plus needlecast and virtual matrices; memory as broadcast content; direct-to-brain advertising. Table A.1 summary; extracts §4.1, §4.3, §4.7, §4.8.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Direct-to-brain advertising inducing the urge to buy | 7a Operator commit | `extract` §4.7 | Sanctioned external write on the recipient |
| Interrogators run the protagonist in a virtual matrix "similar to the ones used in psychosurgery" | 7a Operator commit | `extract` §4.8 block quote | Operator holds the world's parameters |
| Envoy conditioning; the protagonist alters his own perception of reality by trained control | 5 Training by response | `extract` (A.1 summary) | Sanctioned internal write installed by an institution |
| Recorded memories sold as first-person content | 7b Distributed commit | `extract` §4.3 | One party's experience becomes another's input |

### A3 — *Aristoi* (Williams, 1992)

Mediator: the daimon implant that lets sub-identities communicate and operate avatars; the shared oneirochronon. Table A.1 summary; extracts §4.1, §4.5, §4.6.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Sub-identities read one another and coordinate design decisions through the implant | 2 Backend reading | `extract` §4.6 | Structural self-read across daimones |
| Aristoi hold write access over planets and the public virtual realm; ordinary citizens do not | 7a Operator commit | `extract` (A.1 summary) | Stratified console |
| A rogue Aristos maintains a hidden world outside the sanctioned realm | 8 Protocol shipping | `to verify` | Subversive external write by an insider |

### A4 — *Blindsight* (Watts, 2006)

Mediator: neural implants that let crew "feel" data; surgically partitioned personalities; Heaven (public cyberspace with memory of the outside blocked); the ship's Captain acting through a proxy. Table A.1 summary; extracts §4.2, §4.6 block quote, §4.8, §5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| The Gang of Four: "four fully conscious hub personalities … all working in parallel" | 2 Backend reading | `extract` §4.6 block quote | Internal structural read/write among partitions |
| Citizens enter Heaven and block memories of the external world | 5 Training by response | `extract` §4.8 | Sanctioned internal write |
| The ship's AI directs the mission through the vampire commander; the crew infer this late | 4 Audit | `canon` | Crew reading who actually holds the commit |

### A5 — *Echopraxia* (Watts, 2014)

Mediator: neuromodifying implants as career condition; non-invasive dream control; hive minds; military mind control; internet-connected implants open to spambots. Table A.1 summary; extracts §4.4 block quote, §4.5 block quote, §4.7 block quote, §5.1.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Brüks learns in his sleep through non-invasive dream control to keep up with augmented peers | 5 Training by response | `extract` §4.4 block quote | Sanctioned internal write under labour pressure |
| "Some spambot hacks in and leaves me with an irresistible urge to buy…" | 3 Shared folk theory | `extract` §4.7 block quote | A baseline's folk model of what implants expose him to |
| Military exploitation of mind control as a weapon; "soul mates made to order" | 7a Operator commit | `extract` §4.5, §4.7, A.1 | Sanctioned external write on recipients |
| Hive-mind collectives coordinate as one cognitive system | 7b Distributed commit | `extract` (A.1 summary) | Members co-write the collective state |

### A6 — *Glasshouse* (Stross, 2006)

Mediator: assembler gates whose reconstruction step distorts censored memories; implants receiving backups; keyword-triggered aphasia. Table A.1 summary; extracts §4.5, §4.7, §5.4, §5.5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Keyword aphasia signals to allies that a person's memories have been altered | 4 Audit | `extract` (A.1 summary), §4.7 | Structural read of another party's mediator state |
| The authoritarian regime's virus rewrites memories during gate reconstruction | 7a Operator commit | `extract` (A.1 summary) | Centralized write embedded in shared infrastructure |
| Opponents build implants and backup channels that bypass the gates' rewrite | 8 Protocol shipping | `extract` (A.1 summary) | Community ships a protocol over the vendor's stack |

### A7 — *Judas Unchained* (Hamilton, 2005)

Mediator: brain implants through which an alien suppresses will and implants ideas received as one's own; brain-to-brain skill download. Table A.1 summary; extracts §4.3, §4.7, §4.8, §5.1.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| The Starflyer implants ideas recipients perceive as their own | 7a Operator commit | `extract` §4.7, A.1 | Party cannot read the rule that writes it |
| Skill and memory download between brains | 5 Training by response | `extract` §4.8 | Sanctioned internal write |

### A8 — *Neuromancer* (Gibson, 1984)

Mediator: the matrix accessed through trodes; simstim; an AI that manipulates perception of time and dream content. Table A.1 summary; extracts §4.8, §5.1.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Case reads the matrix's structure directly from inside | 4 Audit | `canon` | Structural read of shared state |
| Wintermute alters perception of time and imposes ideas through dream content | 7a Operator commit | `extract` (A.1 summary) | AI as operator |
| The crew runs an icebreaker against a corporate core to rewrite the AI's constraints | 8 Protocol shipping | `canon` | Subversive external write |
| Simstim: Case rides Molly's sensorium | 4 Audit | `canon` | Structural read of a counterpart's state through the mediator |

### A9 — *Pandora's Star* (Hamilton, 2004)

Mediator: personality-recording implants, memory transmission, obsessive-work implants, advertising that increases desire to stay. Table A.1 summary; extracts §4.2, §4.5, §4.7, §5.5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Implants induce obsessive desire to work; users edit incriminating or traumatic memories | 5 Training by response | `extract` (A.1 summary), §4.5 | Sanctioned internal write in a labour market |
| Advertising increases the desire to stay at a venue | 7a Operator commit | `extract` §4.7 | Sanctioned external write |
| Police read and transmit memories to other implants | 4 Audit / 7a | `extract` (A.1 summary) | Structural read of another's stored state |

### A10 — *Permutation City* (Egan, 1994)

Mediator: cyberspace hosting uploaded Copies; computing power as currency; user-editable personality, memory, and perception. Table A.1 summary; extracts §4.1, §4.3 block quote, §4.8, §5.1, §5.2.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Copies edit their own moods, drives, and memories ("mood-altering 'drugs' … with a precision … no real chemical could ever have achieved") | 5 Training by response | `extract` §4.3 block quote | Sanctioned internal write |
| A Copy runs experiments on his own execution to inspect how his state is computed | 2 Backend reading | `canon` | Structural self-read |
| A founder designs the rules of a world other Copies inhabit | 7a Operator commit | `canon` | Centralized write over a shared world |
| Inhabitants of a simulated planet reject the founders' account of their origin | 4 Audit (failed) | `to verify` | Counterparts read the world's rule and refuse the operator's claim |

### A11 — *Quarantine* (Egan, 1992)

Mediator: neural mods that disable emotions, alter attitudes, and impose loyalty; the user knows his beliefs about mods are mod-induced. Table A.1 summary; extracts §4.1 block quote, §4.5, §4.7, §5.2, §5.5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| "I have a mod that … defines my responses. I don't grieve for her." | 2 Backend reading | `extract` §4.1 block quote | The party reads his own mediator's rule and states it |
| An organisation installs a loyalty mod in its operatives | 7a Operator commit | `extract` §4.7 ("artificial absolute loyalty in workers"), A.1 | Sanctioned external write |
| The protagonist redefines the loyalty mod's referent from inside to break its hold | 6 Subversive affordance | `canon` | Subversive internal write through the mod's own rule |

### A12 — *Revelation Space* (Reynolds, 2000)

Mediator: ubiquitous implants and ship-linked BCIs; entities hijack hosts through compromised implants. Table A.1 summary; extracts §4.1, §4.2 (omniscience, information-unity), §4.7, §4.8, §5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Crew merge with ship systems and feel "dissolved into these machines" | 2 Backend reading | `extract` (A.1 summary), §4.2 | Structural read of a shared system from inside |
| An entity compromises implants and takes control of its host | 7a Operator commit | `extract` (A.1 summary) | External write the host cannot read |
| Artificial memories supplement the environment; performers' states shared | 7b Distributed commit | `extract` §4.7, §4.1 | Party-to-party state transfer through the mediator |

### A13 — *Silently and Very Fast* (Valente, 2011)

Mediator: a house AI living in a family's evolving implants, learning its hosts through their dreams across generations. Table A.1 summary; extracts §4.3, §4.8, §5.1.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Each generation of the family teaches the AI through dream-communication; later generations inherit what earlier ones taught | 7b Distributed commit | `extract` (A.1 summary), §4.8 | The cleanest cooptive commit in the corpus: engagement is development another party meets |
| Orgasm on demand through direct stimulation | 5 Training by response | `extract` §4.3 | Sanctioned internal write |

### A14 — *Snow Crash* (Stephenson, 1992)

Mediator: the Metaverse; a visual bitmap that fires a neurolinguistic virus in programmers; a broadcasting corporation's cult. Table A.1 summary; extracts §4.7.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| A broadcasting magnate spreads the virus through screens and a franchise religion | 7a Operator commit | `extract` (A.1 summary), §4.7 | Centralized write; recipients cannot read the rule |
| The protagonist reverse-engineers the virus with a library daemon | 4 Audit | `canon` | Structural read of a shared attack |
| A counter-program is deployed to stop the virus | 8 Protocol shipping | `to verify` | Subversive external write |

### A15 — *Synners* (Cadigan, 1992)

Mediator: brain sockets and synthetic neurons that let consciousness content be programmed and transmitted; a corporation ships the sockets; a stroke propagates through the network. Table A.1 summary; extracts §4.1, §4.5, §4.6, §4.7, §5.2, §5.3.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| A socketed artist treats external devices as parts of his own brain and expands beyond his body | 2 Backend reading | `extract` §4.6, A.1 | Structural self-read that becomes shared state |
| His stroke propagates as a virus through the network to other socketed users | 7b Distributed commit (unintended) | `extract` (A.1 summary) | One party's state rewrites the shared mediator others meet |
| Off-grid hackers run a parallel rig and coordinate to contain the virus | 8 Protocol shipping | `canon` | Community ships a protocol over the vendor's stack |
| Implanting ideas for political ends | 7a Operator commit | `extract` §4.7 | Sanctioned external write |

### A16 — *TekWar* (Shatner, 1989)

Mediator: Tek chips that immerse a user in controlled dreams; memory modification. Table A.1 summary; extracts §4.1, §4.7.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| A user selects dream content on a Tek chip | 5 Training by response | `extract` (A.1 summary) | Sanctioned internal write |
| Memory correction imposed by others | 7a Operator commit | `extract` §4.7 | `thin`: no scene of reading the rule supported |

### A17 — *The Algebraist* (Banks, 2004)

Mediator: memory decoding, erasing, and implanting by factions; BCI mind-merging; Tream gear for shared controlled dreams. Table A.1 summary; extracts §4.3, §4.6, §4.7 block quote, §4.8, §5.4.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| "His controllers had not even bothered to implant false memories incriminating anyone…" | 7a Operator commit | `extract` §4.7 block quote | Centralized write for legal fabrication |
| Communes co-author a shared controlled dream through Tream gear | 7b Distributed commit | `extract` (A.1 summary) | Multiple parties with sanctioned write |

### A18 — *The Lathe of Heaven* (Le Guin, 1971)

Mediator: a biofeedback device (the Augmentor) through which a psychiatrist directs a patient's reality-altering dreams. Table A.1 summary.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| The psychiatrist scripts the patient's dreams to reshape reality for everyone | 7a Operator commit | `extract` (A.1 summary) | The paradigm of centralized external write |
| The patient's dreams undercut the instructions (dreaming a solution the operator did not order) | 8 Protocol shipping | `canon` | Subversive write from the "recipient" seat |
| The operator turns the device on himself; the patient disconnects it | 6 → 8 | `canon` | Subversive write that ends the operator's write access |

### A19 — *The Stars My Destination* (Bester, 1956)

Mediator: military implants altering perception of time, obtained by bribery. Table A.1 summary; extracts §4.5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| The protagonist bribes his way to combat implants | 5 Training by response | `extract` (A.1 summary), §4.5 | `thin`: mediator has a fixed rule; no reading or rewriting scene supported |

### A20 — *The Terminal Man* (Crichton, 1972)

Mediator: a computer-controlled brain stimulator that interrupts seizures by pleasurable shocks. Table A.1 summary; extracts §4.3, §5.3.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| The brain habituates to the shocks and begins to provoke seizures to receive more | 6 Subversive affordance | `extract` (A.1 summary) | The party games the device's designed feedback rule |
| Physicians monitor and adjust the device from outside | 4 Audit / 7a | `extract` (A.1 summary) | Clinical write access over another's mediator |

### A21 — *Ubik* (Dick, 1969)

Mediator: half-life suspension in which the dying share a consciousness space; a predator consumes half-lifers; a protective spray constructed by the others. Table A.1 summary; extracts §4.3, §4.8.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| The trapped protagonists read graffiti, coins, and messages as signs of who is running their reality | 3 Shared folk theory | `canon` | Collective interpretive read of the shared mediator |
| A predator rewrites the others' shared reality | 7a Operator commit | `extract` (A.1 summary) | Subversive from the victims' view, sanctioned by the mediator's rule |
| Half-lifers construct Ubik as a protective artefact against him | 8 Protocol shipping | `extract` (A.1 summary) | Community ships a counter-protocol inside the mediator |

### A22 — *Vast* (Nagata, 1998)

Mediator: ship-merged bodies, virtual copies embedded in other people's minds, self-editing to "feel human". Table A.1 summary; extracts §4.2 block quote, §4.5, §5.1, §5.5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| "She was a point of perception without mass or volume" — dissolved into the ship's structure | 2 Backend reading | `extract` §4.2 block quote | Structural read of a shared system from inside |
| Crew edit their own memories to keep feeling human | 5 Training by response | `extract` (A.1 summary), §5.5 | Sanctioned internal write |
| Ghosts embedded in other minds dissolve and transmit gained memories | 7b Distributed commit | `extract` (A.1 summary) | One party's copy rewrites another's state |

### A23 — *Vurt* (Noon, 1993)

Mediator: shared dreams built from edited recordings of others' dreams; club DJs stream blends into dancers' implants. Table A.1 summary; extracts §4.1, §4.3, §4.4, §4.7, §5.3, §5.4.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| A DJ blends dream recordings and streams them into the crowd's implants | 7b Distributed commit | `extract` (A.1 summary), §4.1 | Sanctioned external write by a non-vendor |
| Advertising promoted inside the dream medium | 7a Operator commit | `extract` §4.7 | Centralized write |
| Users trade folk rules about which feathers are safe and how to get out | 3 Shared folk theory | `to verify` | Community rule-inference |
| Illegal or bootleg dream-recordings circulate outside sanction | 8 Protocol shipping | `to verify` | Subversive external write |

### A24 — *Wetware* (Rucker, 1988)

Mediator: headsets that enhance pleasant perception; implants in captive humans suppressing will. Table A.1 summary; extracts §4.1, §4.7, §5.3, §5.4.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| Humans wear headsets to enhance pleasant aspects of the environment | 5 Training by response | `extract` (A.1 summary), §4.1 | Sanctioned internal write |
| Robots implant captive humans with will-suppressing devices | 7a Operator commit | `extract` (A.1 summary), §4.7 | `thin` on reading; write is clear |

### A25 — *When Gravity Fails* (Effinger, 1986)

Mediator: brain-socket chips granting temporary skills (add-ons) or personalities (moddies). Table A.1 summary; extracts §4.1, §4.4, §4.7, §5.3, §5.5.

| Scene | Cell | Tag | Note |
|---|---|---|---|
| The protagonist refuses to be wired for fear of losing his identity | 1 Folk theorizing | `extract` (A.1 summary) | Interpretive self-model of what the mediator would do |
| A patron has him wired against his wishes; employers alter workers' behaviours to suit tasks | 7a Operator commit | `extract` §4.7, A.1 | External write over a dependent party |
| Once wired, he chips in add-ons that block pain and fear on demand | 5 Training by response | `extract` (A.1 summary) | Sanctioned internal write |
| A criminal wears the moddies of famous killers | 5 Training by response | `extract` (A.1 summary) | Same cell, opposite valence |

## B. Extension corpus — the catalogued works

Source for each: the work file in [`../scifi_interfaces_algorithmacy/works/`](../scifi_interfaces_algorithmacy/works/) and the engagement-layer reading in [`../scifi_interfaces_algorithmacy/ENGAGEMENT_LAYER.md`](../scifi_interfaces_algorithmacy/ENGAGEMENT_LAYER.md). Tag `catalog` marks scenes already documented there.

### M1 — *The Matrix* (Wachowski, 1999)

| Scene | Cell | Tag |
|---|---|---|
| Cypher reads raw code as "blonde, brunette, redhead" | 4 Audit | `catalog` |
| Operators load skills into a body and open exits from the console | 7a Operator commit | `catalog` |
| Plugged-in humans live inside the product layer without read access | (boundary: no read or write) | `catalog` |

### M2 — *The Feed* (2019)

| Scene | Cell | Tag |
|---|---|---|
| Developers rearrange glowing hexagons while the population is plugged in | 7a Operator commit | `catalog` |
| Implanted users' streamed memories and reactions are the material developers rearrange | 7b Distributed commit (unwitting) | `catalog` |
| Users form theories of what the Feed does to them; possession scenes | 3 Shared folk theory | `catalog` |
| Off-grid resistance extracts the hardware | (boundary: exit, not write) | `catalog` |

### M3 — *Upload* (2020–)

| Scene | Cell | Tag |
|---|---|---|
| Nathan toggles his own bandwidth flag and invisibility | 6 Subversive affordance | `catalog` |
| Nathan redistributes digital resources to other residents | 8 Protocol shipping | `catalog` |
| Horizen administrators manage Lakeview's parameters | 7a Operator commit | `catalog` |
| Nathan and Nora work out the monitoring's blind spots to communicate | 3 Shared folk theory | `catalog` |

### M4 — Embodied co-pilot (semi-autonomous vehicles / HAT)

| Scene | Cell | Tag |
|---|---|---|
| A driver forms a folk theory of why the car braked | 1 Folk theorizing | `catalog` |
| Drivers share theories of the vehicle's behaviour | 3 Shared folk theory | `catalog` |
| Interventions become training data for the fleet policy other drivers meet | 7b Distributed commit | `catalog` |
| Manual override | 6 Subversive affordance (when it defeats the designed handoff) | `catalog` |

### M5 — Omniscient curator (recommender oracles)

| Scene | Cell | Tag |
|---|---|---|
| A user theorises the recommender as social being or trainable machine | 1 Folk theorizing | `catalog` |
| "Algorithmic pairing": swiping and lingering to teach the system | 5 Training by response | `catalog` |
| Everyone's teaching becomes the recommender the next user meets | 7b Distributed commit | `catalog` |
| Data obfuscation to confuse the oracle | 6 Subversive affordance | `catalog` |

### M6 — Algospeak and infrapolitical resistance

| Scene | Cell | Tag |
|---|---|---|
| A community builds a shared map of the classifier's blind spots | 3 Shared folk theory | `catalog` |
| The community ships a working protocol over the vendor's classifier; each evasion retrains it | 8 Protocol shipping | `catalog` |
| Gig workers coordinate on encrypted side-channels against the employer app | 8 Protocol shipping | `catalog` |

---

## C. Cell membership summary

| Cell | Works |
|---|---|
| 1 Folk theorizing | A25, M4, M5 |
| 2 Backend reading | A1†, A3, A4, A10, A11, A12, A15, A22 |
| 3 Shared folk theory | A5, A21, A23†, M2, M3, M4, M6 |
| 4 Audit | A4, A6, A8, A9, A10†, A14, A20, M1 |
| 5 Training by response | A1, A2, A4, A5, A7, A9, A10, A13, A16, A19‡, A22, A24, A25, M5 |
| 6 Subversive affordance | A11, A18, A20, M3, M4, M5 |
| 7a Operator commit — centralized | A1, A2, A3, A5, A6, A7, A8, A9, A10, A11, A12, A14, A15, A16‡, A17, A18, A20, A21, A23, A24‡, A25, M1, M2, M3 |
| 7b Operator commit — distributed | A2, A5, A12, A13, A15, A17, A22, A23, M2, M4, M5 |
| 8 Protocol shipping | A3†, A6, A8, A14†, A15, A18, A21, A23†, M3, M6 |

† at least one `to verify` tag; ‡ `thin`.

## D. Leakage — internal cells that become external in the narrative

Recorded because §5 of the draft argues that internal reach is a literacy fiction the corpus itself undoes.

| Work | Internal scene | How it leaks |
|---|---|---|
| A1 | Host integrates the imago (5) | The integrated line is what the next host receives (7b) |
| A5 | Brüks learns in sleep (5) | The competitive norm that forces it is set by everyone else's implants (7b) |
| A11 | Nick reads his own mod (2) | The mod was installed by an employer with its own objective (7a) |
| A13 | Family members dream with the AI (5) | Their teaching is the AI later generations inherit (7b) |
| A15 | Mark expands into the net (2) | His stroke becomes a network virus (7b) |
| A20 | Benson games his stimulator (6) | Physicians hold the adjustment console (7a) |
| A25 | Marîd chips add-ons (5) | The wiring was ordered by his patron (7a) |
| M4 | Driver's override (6) | Becomes fleet training data (7b) |
| M5 | User trains own feed (5) | Becomes everyone's recommender (7b) |
