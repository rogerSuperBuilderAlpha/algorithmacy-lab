# Part 2 — The Ethics of Decision Experience Design: Outline

<!-- Claude-drafted outline (Fable 5.1), 2026-10-01, from PITCH.md (source), the live Part 1
(2026-09-30), the arm README rulings, and algorithmacy_design_ethics/DRAFT.md. Nothing here is
author text. Every seed source carries a status flag:
  [card]   verified reference card exists in the lab (path given once, in §E of the facet list)
  [bib]    entry in decision_experience_design/literature/references.bib or cited in live Part 1
  [verify] cited from memory; must be matched to a database record before it enters a draft
Source status is not upgraded here; "[verify]" items may turn out wrong in year, venue or claim. -->

**Working title.** *Decision Experience Design, Part 2: What Design Owes a Person Who Cannot Leave*

**Form.** Substack essay, 6,000–8,000 words body, register of the live Part 1: formal, author–date
APA, few first-person sentences, headed sections, closing with falsifiable propositions, limitations,
and References.

---

## (a) Thesis

Part 1 ended on structural intervention over visual legibility and four propositions about
algorithmacy as a competence that predicts decision quality through an adaptive intermediary. Part 2
asks what that competence makes the designer owe the person who decides through the intermediary.
The prevailing answer in design ethics is disclosure and choice: tell the person what the system
does, arrange the options well, and let an informed chooser decide, including the decision not to
participate. That answer presupposes exit (Hirschman, 1970). Where algorithmic coordination governs
credit, triage, hiring, platform work and civic information, exit is unavailable or ruinously priced,
so disclosure informs a person about a system they must use regardless, and choice architecture
arranges options for a chooser who is in fact a participant. The ethical obligation shifts from
informing a chooser to building the conditions under which a participant can acquire operational
skill: an interface that displays the system's declared operating envelope (so that behavior is
predictable, in the sense Kahneman and Klein (2009) require for learning), that scaffolds steering
through direct, low-cost channels for intent, and that fades the scaffold as skill grows, paired with
counter-delegation and structural refusal (the three design-ethics principles). Conversational
interfaces are the case that tests the thesis: they bought adoption by removing friction and in
exchange handed the user an unpaid verification burden that neither predicts nor teaches. The
history of reading supplies an analogy for what design can do (make a skill ordinary by giving it
visual structure), not a mechanism (algorithmacy does not restructure cognition; Street, 1984). The
deskilling debate is re-posed accordingly: the ethical question is not whether people retain the
literacy they had but whether design affords the competence they now need, and an ethics of meaning
(Martela & Steger, 2016) and of technomoral virtue (Vallor, 2016) says why that affordance is a duty
rather than a product feature.

---

## (b) Jargon table

Rule 4 governs: prefer the literature's term where one exists; a coined term survives only with a
one-sentence definition tied to the nearest existing construct. Decisions below are recommendations
for the author's ruling.

| Pitch term | Nearest established construct(s) | Decision |
| --- | --- | --- |
| **algorithmacy** | The lab's own construct, defined in Part 1 on the numeracy model (Peters et al., 2006 [bib]); three operations: interpreting, specifying intent, keeping track. | KEEP-WITH-DEFINITION. "Algorithmacy is the competence to decide through an opaque, adaptive intermediary that reads several parties and commits binding outcomes — to interpret it, to specify intent through it, and to keep track of it as it changes (Part 1)." |
| **algorithmacy-first** | "Competence-first" has no established home; the nearest is boosting's aim of building durable competence rather than steering behavior (Hertwig & Grüne-Yanoff, 2017 [bib]). | DROP as a slogan. Write "design that takes algorithmacy as its target competence" or "designing for algorithmacy." |
| **triadic coordination** | Part 1's "triadic intermediary"; Simmel's tertius (Simmel, 1950 [card]); the Lima paper's opacity/adaptivity/bindingness. | KEEP-WITH-DEFINITION, once, as "coordination through an intermediary." "Coordination is triadic when a third party reads both human parties and commits an outcome that binds them both (Part 1)." Thereafter prefer "coordination through an intermediary." |
| **cooptive / coopted** | "Binding" (Part 1); "mandatory participation"; Lima paper's "coordinative co-optation" (lab-internal); Berthon & Pitt's attention not under our control (2019 [card]). | REPLACE-WITH "binding" for the structural property and "mandatory participation" or "unavoidable" for the social fact. Use "co-optation" only if citing the Lima paper. |
| **literacy crutch / conversational literacy interface / "chat scroll"** | Conversational interface, natural-language interface (HCI); Shneiderman's direct-manipulation vs. conversational contrast (1983 [verify]); Hutchins, Hollan & Norman (1985 [bib]). | REPLACE-WITH "conversational interface" and state the empirical claim (verification burden, overreliance, prompting difficulty) rather than the pejorative. |
| **sounding out** | Verification burden / cost of verification (Vasconcelos et al., 2023 [bib]); gulf of evaluation (Hutchins et al., 1985 [bib]); Bainbridge's monitoring irony (1983 [card]). | REPLACE-WITH "serial verification" or "verification burden." The phrase may survive once, inside the reading analogy, quoted as analogy. |
| **scriptio continua (as metaphor)** | Word separation and visual syntax as scribal design (Saenger, 1997 [card]; Parkes, 1992 [verify]); silent reading in antiquity (Knox, 1968 [verify]; Gavrilov, 1997 [card]; Burnyeat, 1997 [card]). | KEEP as an explicitly flagged analogy, confined to one section, with the contested history stated correctly (ruling 1). Never as a mechanism claim and never paired with "silent reading internalized consciousness." |
| **epistemic janitor** | Unpaid verification labor; Bainbridge's operator demoted to monitor (1983 [card]); heteromation (Ekbia & Nardi, 2017 [card, dial]); Woods's "solution filter" (1985 [bib]). | DROP. Write "unpaid verification labor" and cite the human-factors line. |
| **false equity of disclosure** | Privacy self-management (Solove, 2013 [verify]); "transparency fallacy" (Edwards & Veale, 2017 [verify]); "seeing without knowing" (Ananny & Crawford, 2018 [card]); the biggest lie on the internet (Obar & Oeldorf-Hirsch, 2020 [verify]). | REPLACE-WITH "the limits of notice-and-consent" / "the transparency ideal and its limits." The equity point survives as a claim: disclosure distributes information, not capacity. |
| **exit / "there is no exit"** | Exit, voice, loyalty (Hirschman, 1970 [card]); structural refusal (Zong & Matias, 2024 [card]); lock-in. | KEEP-WITH-DEFINITION. "Exit is Hirschman's (1970) term for leaving a relation rather than acting on it from inside; where exit is unavailable or ruinously priced, voice is the only remaining channel." Write "unavoidable" or "mandatory participation" rather than "no exit" as a slogan. |
| **decision experience (vs. choice architecture)** | Part 1's thesis term; choice architecture (Thaler & Sunstein, 2008 [card]; Johnson et al., 2012 [bib]); "decision experience" in Peterson & Cheng (2022 [bib]). | KEEP-WITH-DEFINITION. "Choice architecture arranges the options a chooser faces; decision experience design designs the conditions — predictability, channels for intent, scaffolding — under which a person decides through an intermediary and learns to do so better (Part 1)." |
| **parametric steering** | Direct manipulation (Shneiderman, 1983 [verify]; Hutchins et al., 1985 [bib]); modification channel (Dietvorst et al., 2018 [bib]); Part 1's "channel for intent." | REPLACE-WITH "direct manipulation" for the interaction style and "channel for intent" for the design principle. |
| **latent canvas / spatialization** | Spatial, structured representations; design-space exploration tools; direct-manipulation interfaces. No single construct. | DROP. Where a concrete example is needed, name it (a 2-D parameter map, a constraint diagram) rather than the coinage. |
| **state signaling / dynamic constraint visualization** | System-state feedback (Norman, 1990 [card]); Ecological Interface Design's constraint display (Vicente & Rasmussen, 1992 [bib]); declared operating envelope (Part 1, design-ethics principle 3). | REPLACE-WITH "feedback on system state" and "display of the declared operating envelope." Ruling 2: it displays the envelope; it does not explain the model. |
| **pre-attentive signaling / sensory signaling** | Pre-attentive visual features (Treisman & Gelade, 1980 [verify]; Healey & Enns, 2012 [bib]); uncertainty visualization (Padilla et al., 2018; Kale et al., 2019; Hullman, 2020 [all verify]). | REPLACE-WITH "pre-attentive visual features," cited. Not a coinage. |
| **experiential decision loops** | Rapid, unequivocal feedback as a learning condition (Kahneman & Klein, 2009 [bib]); feedback loops (Norman, 1990 [card]); testing when cheap (Zhang, Liao & Bellamy, 2020 [bib]). | REPLACE-WITH "feedback loops that meet the Kahneman–Klein learning conditions." |
| **progressive epistemic elevation** | Scaffolding and fading (Wood, Bruner & Ross, 1976 [verify]); cognitive apprenticeship (Collins, Brown & Newman, 1989 [verify]); training-wheels interface (Carroll & Carrithers, 1984 [verify]); boosting (Hertwig & Grüne-Yanoff, 2017 [bib]). | REPLACE-WITH "scaffolding and fading." |
| **scaffolded interface syntax** | Scaffolding (above) applied to the interface; EID's visual geometry of constraints (Vicente & Rasmussen, 1992 [bib]). | REPLACE-WITH "scaffolded interface" or "an interface that displays the operating envelope and fades its scaffolds." |
| **triadic grammar** | Mental model of error boundaries (Bansal et al., 2019 [bib]); "theory of machine" (Logg et al., 2019 [bib]); gist of the intermediary's rules (Reyna & Brainerd, 2023 [bib]). | DROP. Write "a working model of the intermediary's boundaries and tendencies." |
| **algorithmate (adj.)** | Parallel to "numerate/literate"; no usage in the literature. | DROP. Write "competent in algorithmacy." If the author wants the adjective, define it once by the numerate parallel and use it sparingly. |
| **algorithmic white space** | Seamful design (Chalmers & Galani, 2004 [bib]); friction / cognitive forcing functions (Buçinca et al., 2021 [bib]); sludge as the opposite (Sunstein, 2021 [card]); Vallor's communicative friction (2016 [card]). | DROP. Write "designed friction" or "seams," citing those. |
| **deskilling** | Braverman (1974 [verify]); the deskilling controversy (Attewell, 1987 [verify]); moral deskilling (Vallor, 2015 [card]); automation complacency (Parasuraman & Manzey, 2010 [bib]). | KEEP-WITH-DEFINITION. "Deskilling, in Braverman's (1974) sense, is the removal of skill from a job by the design of its tools and tasks; Vallor (2015) extends it to moral skill, where a tool removes the occasions for practice." |
| **frictionless adoption / "frictionless UX"** | Seamless vs. seamful design (Weiser; Chalmers & Galani, 2004 [bib]); Vallor's "dubious ideal" of frictionless interaction (2016, pp. 161–164 [card]); sludge (Sunstein, 2021 [card]). | KEEP as ordinary English, cited to Vallor and Chalmers; not a coinage. |
| **media revolution / literacy regress / "epistemic nostalgia"** | Great Divide thesis (Ong, 1982 [card]; Goody & Watt, 1963 [card]) and its critique (Street, 1984 [card]; Scribner & Cole, 1981 [card]). | DROP the mechanism claim (ruling 1). The history enters only as analogy. |
| **Verbeek's invisible scripts** | Script is Akrich's (1992 [card]) and Latour's (1992 [card]) term; Verbeek's is mediation (2005, 2011 [card]). | Fix attribution: "scripts (Akrich, 1992; Latour, 1992), taken up in Verbeek's (2005, 2011) mediation theory." |
| **Martela & Steger tripartite** | Coherence, purpose, significance (Martela & Steger, 2016 [card], full text read). | Correct as stated. KEEP. |

---

## (c) Argument spine (9 sections, ~7,400 words body)

### 1. Where Part 1 stopped, and the question it leaves (≈550 words)
**Claims to earn.** (i) Part 1 established algorithmacy as a competence on the numeracy model and
argued structural intervention over legibility; (ii) a competence claim raises an ethical question —
if decision quality through an intermediary depends on a learnable competence, who owes whom the
conditions for learning it; (iii) the prevailing answer (disclose, arrange, let choose) is the one
this essay examines.
**Evidence.** Part 1's propositions (self-citation); the three design-ethics principles
(counter-delegation, structural refusal, operational predictability) from the design-ethics arm.
**Hook forward.** The prevailing answer presupposes that the person can leave.

### 2. Mandatory participation: what disclosure assumes (≈1,000 words)
**Claims.** (i) Notice-and-consent and transparency regimes presuppose a chooser who can decline;
(ii) Hirschman's exit/voice/loyalty gives the vocabulary — where exit is foreclosed, only voice
remains, and voice needs a channel; (iii) in credit, triage, hiring, platform work and information
discovery, exit is unavailable or priced as marginalization; (iv) so disclosure distributes
information without distributing capacity, and consent collapses into ritual.
**Evidence.** Hirschman (1970 [card]); Solove (2013 [verify]) on privacy self-management; Ananny &
Crawford (2018 [card]) ten limits of transparency; Edwards & Veale (2017 [verify]) on the
explanation right; Obar & Oeldorf-Hirsch (2020 [verify]) on unread policies; Nissenbaum (2011
[card], p. 43) on burdening individuals; Zong & Matias (2024 [card]) on refusal; Berthon & Pitt
(2019 [card]) and Williams (2018 [card]) on mandatory attention; Eslami et al. (2015 [bib]) on
unawareness. Domain cases: Calo & Rosenblat (2016 [bib]); Rosenblat & Stark (2016 [card, dial]);
Kellogg, Valentine & Christin (2020 [card, dial]). Vallor (2024 [card], p. 196) on contestability
and redress as "low-hanging fruit."
**Hook.** If the person cannot leave, the ethics of the options they face is the next thing to check.

### 3. Choice architecture as an ethics, and its limit (≈850 words)
**Claims.** (i) Nudge's ethical defense (libertarian paternalism) rests on preserved freedom to
choose otherwise and on an identifiable architect; (ii) both fail under adaptive, multi-sided
intermediaries (Part 1: hypernudge, autonomous choice architect); (iii) sludge and dark patterns show
the same levers run in reverse; (iv) boosting is the behavioral tradition's own turn toward
competence, and it names the right aim — durable skill that outlasts the intervention — but is still
framed around information literacy; (v) the nudge effect-size literature means a DXD ethics cannot
rest on nudge heuristics anyway.
**Evidence.** Thaler & Sunstein (2008 [card]); Sunstein (2021 [card]) sludge; Gray et al. (2018
[bib]); Mathur et al. (2019, 2021 [bib]); Yeung (2017 [bib]); Mills & Sætra (2024 [bib]); Hertwig &
Grüne-Yanoff (2017 [bib]); Kozyreva et al. (2020 [bib]); Maier et al. (2022), Szaszi et al. (2022),
DellaVigna & Linos (2022) [all bib]. Autonomy critiques of nudging: to be located in facet A
(e.g., Hausman & Welch 2010 [verify]; Bovens 2009 [verify]).
**Hook.** The industry's chosen remedy for algorithmic complexity was not a nudge; it was a chat box.

### 4. The conversational interface: adoption bought with verification (≈1,250 words)
**Claims.** (i) Conversational interfaces minimize the gulf of execution at entry (anyone can type)
and maximize the gulf of evaluation (the output must be read and checked serially); (ii) the
empirical record shows prompting is opportunistic and socially miscalibrated (Zamfirescu-Pereira et
al., 2023 [card]), that users cannot envision what the system can do (gulf of envisioning), and that
overreliance rises when verification costs more than accepting (Vasconcelos et al., 2023 [bib]);
(iii) direct manipulation and pre-attentive encoding reduce the evaluation cost by moving system
state into perception rather than text; (iv) uncertainty visualization research shows when that
works and when it misleads; (v) the ethical point: an interface that bought adoption by hiding the
operating envelope behind fluent text transferred the cost of coordination to the user as unpaid
verification labor, and gave nothing back as predictability or skill. Ruling 2 applies throughout:
the alternative is not "explaining the model" but displaying its envelope.
**Evidence.** Shneiderman (1983 [verify]); Hutchins, Hollan & Norman (1985 [bib]); Bainbridge (1983
[card]); Zamfirescu-Pereira et al. (2023 [card]); Subramonyam et al. (2024, "gulf of envisioning"
[verify]); Vasconcelos et al. (2023 [bib]); Buçinca et al. (2021 [bib]); Bansal et al. (2021 [bib]);
Lee et al. (2025 [bib]); Treisman & Gelade (1980 [verify]); Healey & Enns (2012 [bib]); Padilla et
al. (2018 [verify]); Kale et al. (2019 [verify]); Hullman (2020 [verify]); recent CHI/CSCW
sensemaking-with-LLM studies (facet B to locate). Vicente & Rasmussen (1992 [bib]) for the
constraint-display precedent and its expert-operator limit (Part 1).
**Hook.** Readers have faced an interface that made them sound everything out before.

### 5. The scribes' remedy: an analogy, stated carefully (≈700 words)
**Claims.** (i) Latin inscriptions used interpuncts; scriptio continua became the standard for Latin
book hands around the 1st–2nd c. CE; Irish and Anglo-Saxon scribes introduced systematic word
separation in the 7th–8th c. (Saenger, 1997; Parkes, 1992), and it spread to the Continent over the
following centuries; (ii) silent reading existed in antiquity (Knox, 1968; Gavrilov, 1997; Burnyeat,
1997; Johnson, 2000), so the claim is not that word separation made silent reading possible but that
visual syntax made fluent, private reading ordinary and lowered the skill threshold for entry;
(iii) that is a design finding — the scribes did not tell readers to listen harder; they changed the
page — and it licenses exactly one inference for DXD: an interface can make an operational skill
ordinary by giving the system's structure a visual form; (iv) it licenses nothing about
consciousness (ruling 1; Street, 1984).
**Evidence.** Saenger (1997 [card]); Parkes (1992 [verify]); Knox (1968 [verify]); Gavrilov (1997
[card]); Burnyeat (1997 [card]); Johnson (2000 [card]); Clanchy (2013 [card]) and Havelock (1963
[card], supply of readers) for the institutional register; Street (1984 [card]); Scribner & Cole
(1981 [card]). Eisenstein (1979 [card]) only via Johns (2002 [card]) if used at all.
**Hook.** The analogy also bounds what the "deskilling" complaint can mean.

### 6. The deskilling debate, re-posed (≈1,000 words)
**Claims.** (i) Deskilling has a sociology (Braverman, Attewell, Adler & Borys) and an archetype
(Socrates in the *Phaedrus* on writing and memory), and the archetype is instructive because the
feared loss was real and the new competence was still worth acquiring; (ii) the recent LLM evidence
is mixed and much of it preliminary: productivity gains inside the frontier with error spikes outside
it (Dell'Acqua et al., 2026 [bib]), reduced effort and confidence effects (Lee et al., 2025 [bib];
Fernandes et al., 2026 [bib]), cognitive offloading as a general mechanism (Risko & Gilbert, 2016
[bib]); Gerlich (2025) and Kosmyna et al. (2025) are to be checked for peer-review status and
sample before any use; (iii) the ethical question is not retention of literacy but acquisition of
the competence mandatory participation now requires — Vallor's criterion (does the tool obviate or
aid the exercise of judgment; 2015 [card], p. 113) and the Kahneman–Klein conditions (predictable
environment, rapid unequivocal feedback) decide whether a design deskills, and conversational
interfaces fail both; (iv) "deskilling" and "upskilling" are therefore properties of the design, not
of the technology.
**Evidence.** Braverman (1974 [verify]); Attewell (1987 [verify]); Adler & Borys (1996 [verify],
enabling vs. coercive formalization); Plato, *Phaedrus* 274c–275b [verify edition]; Vallor (2015
[card]); Parasuraman & Manzey (2010 [bib]); Risko & Gilbert (2016 [bib]); Dell'Acqua et al. (2026
[bib]); Noy & Zhang (2023 [verify]); Brynjolfsson, Li & Raymond (2025 QJE [verify]); Lee et al.
(2025 [bib]); Gerlich (2025 [verify, status]); Kosmyna et al. (2025 [verify, preprint status]);
Kahneman & Klein (2009 [bib]).
**Hook.** If deskilling is a property of design, then upskilling is a design problem with a literature.

### 7. Learning design under mandatory participation (≈1,250 words)
**Claims.** (i) The learning sciences already know how people acquire operational skill with complex
systems: scaffolding that fades (Wood, Bruner & Ross), cognitive apprenticeship (modeling, coaching,
fading), worked examples under cognitive load limits (Sweller), productive failure (Kapur), training
wheels (Carroll), legitimate peripheral participation (Lave & Wenger), and boosting as the behavioral
version; (ii) these transfer to DXD on three conditions the intermediary violates by default:
predictability (the envelope holds still long enough to learn), feedback (cheap, fast, unequivocal
tests), and a channel through which intent can be registered and its effect seen; (iii) hence the
design obligation: display the declared operating envelope (predictability, not explanation), give a
low-cost direct channel for intent (Dietvorst's modification right), make tests cheap, fade the
scaffold, and keep updates backward-compatible; (iv) these are paired with, not substitutes for,
counter-delegation and structural refusal — a scaffold without standing teaches a person to work a
system that still binds them unilaterally.
**Evidence.** Wood, Bruner & Ross (1976 [verify]); Collins, Brown & Newman (1989 [verify]); Sweller,
van Merriënboer & Paas (2019 [bib]); Kapur (2008 [verify]); Carroll & Carrithers (1984 [verify]);
Lave & Wenger (1991 [verify]); Norman (1983 [verify]) and Johnson-Laird (1983 [verify]) on mental
models; Hertwig & Grüne-Yanoff (2017 [bib]); Bansal, Nushi et al. (2019 [bib]) on compatible
updates; Dietvorst et al. (2018 [bib]); Kahneman & Klein (2009 [bib]); Bainbridge (1983 [card]);
Viljoen (2021 [bib]) and Delacroix & Lawrence (2019 [bib]) for counter-delegation; Zong & Matias
(2024 [card]) for refusal; Alfrink et al. (2023 [bib]) contestability.
**Hook.** Why call this an obligation and not a feature: because what it protects is meaning.

### 8. An ethics of meaning for decision experience design (≈800 words)
**Claims.** (i) Martela & Steger's three meanings map onto the three obligations: coherence
(comprehensibility) is met by predictability, not transparency; purpose (self-directed goals) is met
by a channel for intent and the skill to use it; significance (that one's action counts) is met by
standing — counter-delegation and refusal; (ii) Vallor's technomoral virtues require occasions for
practice, and a design that removes them (frictionless, unpredictable, un-steerable) is the moral
deskilling she names; (iii) Verbeek's mediation theory and the script concept (Akrich, Latour) say
designers materialize morality whether they intend to or not, so the question is only which script;
(iv) self-determination-theory design (METUX) and the HCI meaning framework show how to evaluate a
design on these terms rather than on engagement; (v) the obligation statement: where participation is
mandatory, a design that offers disclosure without predictability, steering, and standing fails the
person it mediates even if every disclosure is accurate.
**Evidence.** Martela & Steger (2016 [card], full text); Vallor (2015, 2016 [card]); Verbeek (2005,
2006, 2011 [card]); Akrich (1992 [card]); Latour (1992 [card]); Peters, Calvo & Ryan (2018 [card]);
Mekler & Hornbæk (2019 [card]); Desmet & Pohlmeyer (2013 [verify]); Jobin, Ienca & Vayena (2019
[card]) on protection without promotion.
**Hook.** These are claims that can be wrong, and the last section says how.

### 9. Propositions, agenda, limitations (≈600 words)
**Propositions (draft; to refine).** P5 (adoption–competence dissociation): conversational
interfaces will show higher adoption and lower measured algorithmacy gain than structured interfaces
displaying the same system's envelope, holding task constant. P6 (scaffold fading): interfaces that
fade scaffolds after demonstrated competence will produce higher retained decision quality than
either permanent scaffolds or none. P7 (scaffold without standing): scaffolding without a channel
for intent and a refusal path will raise skill without raising willingness to decide through the
intermediary or perceived autonomy (ties to Part 1's P4 and Vaccaro, Sandvig & Karahalios, 2020).
P8 (meaning): coherence, purpose, and significance scores (Martela & Steger-derived items) will track
predictability, channel existence, and standing respectively, not disclosure volume.
**Limitations.** The history is analogy; the learning-sciences transfer is untested on adaptive
intermediaries; several deskilling studies are preprints or self-report; the ethics claims are
normative and the propositions test their empirical presuppositions, not the norms.

---

## (d) Five research facets

### A. choice_architecture_exit
**RQ-A1.** Under what conditions does the libertarian-paternalist defense of choice architecture
(preserved freedom to choose otherwise; identifiable architect) hold, and which of those conditions
fail under adaptive, multi-sided intermediaries?
**RQ-A2.** What does the notice-and-consent / transparency critique establish about disclosure's
limits, and does any of it already reach the no-exit case (mandatory use) explicitly?
**RQ-A3.** How does Hirschman's exit–voice–loyalty frame map onto unavoidable algorithmic systems,
and what does the platform-work literature say about voice channels where exit is foreclosed?
**RQ-A4.** For credit scoring, clinical triage, automated hiring, and platform dispatch, what is the
documented cost of non-participation (the price of exit)?
**Seed sources.** Thaler & Sunstein (2008) [card]; Sunstein (2021) [card]; Hertwig & Grüne-Yanoff
(2017) [bib]; Hausman & Welch (2010), Bovens (2009), Rebonato (2012) [verify]; Hirschman (1970)
[card; also coordinative_sovereignty/literature/library/cards/hirschman1970exit.md]; Solove (2013,
*Harvard Law Review*) [verify]; Ananny & Crawford (2018) [card]; Edwards & Veale (2017, *Duke Law &
Technology Review*) [verify]; Obar & Oeldorf-Hirsch (2020, *Information, Communication & Society*)
[verify]; Nissenbaum (2011) [card]; Zong & Matias (2024) [card]; Calo & Rosenblat (2016) [bib];
Rosenblat & Stark (2016), Kellogg et al. (2020), Vallas & Schor (2020), Johnston & Land-Kazlauskas
(2018), Maffie (2023) [cards, dial/CS]; Yeung (2017), Mills & Sætra (2024) [bib].

### B. chat_interfaces_cognition
**RQ-B1.** What controlled evidence compares conversational/LLM interfaces with structured,
direct-manipulation, or visual tools on decision accuracy, verification time, overreliance, and
calibration?
**RQ-B2.** What do CHI/CSCW studies since 2023 show about prompting difficulty, the gulf of
envisioning, and sensemaking with LLM output — and do any measure skill gain over sessions?
**RQ-B3.** Which pre-attentive and uncertainty-visualization findings bear on displaying an
intermediary's operating envelope (confidence, boundary, trade-off) without text — and where does
visual encoding mislead?
**RQ-B4.** Does any study report the division of cognitive labor in chat use (reading/verifying vs.
deciding), i.e., the verification burden as a measured quantity?
**Seed sources.** Shneiderman (1983, *IEEE Computer*) [verify]; Hutchins, Hollan & Norman (1985)
[bib]; Bainbridge (1983) [card]; Zamfirescu-Pereira et al. (2023) [card]; Subramonyam et al. (2024,
CHI, "gulf of envisioning") [verify]; Vasconcelos et al. (2023), Buçinca et al. (2021), Bansal et al.
(2021), Lee et al. (2025), Fernandes et al. (2026) [bib]; Treisman & Gelade (1980) [verify]; Healey &
Enns (2012) [bib]; Padilla, Creem-Regehr, Hegarty & Stefanucci (2018) [verify]; Kale, Kay & Hullman
(2019/2021) [verify]; Hullman (2020) [verify]; Shneiderman (2020) [bib]; Amershi et al. (2019) [bib];
Vicente & Rasmussen (1992) [bib].

### C. learning_sciences
**RQ-C1.** What do scaffolding-and-fading, cognitive apprenticeship, and training-wheels research
establish about acquiring operational skill with complex interactive systems, and what are the
conditions (feedback timing, task predictability) under which fading works?
**RQ-C2.** What does cognitive load theory (worked examples, expertise reversal) imply for an
interface that must teach while being used — including the risk that permanent scaffolds hurt
experts?
**RQ-C3.** Does productive failure or legitimate peripheral participation offer a model for learning
under mandatory participation (no choice of task, no classroom)?
**RQ-C4.** Has boosting been applied to operational competence with algorithmic systems rather than
to information literacy, and with what results?
**RQ-C5.** What does the mental-models literature say about learning a system whose rules move
(adaptive intermediaries), and does any learning-sciences work address non-stationary task
environments?
**Seed sources.** Wood, Bruner & Ross (1976, *J. Child Psychology & Psychiatry*) [verify]; Collins,
Brown & Newman (1989, in Resnick ed.) [verify]; Sweller, van Merriënboer & Paas (2019) [bib];
Kalyuga et al. (2003, expertise reversal) [verify]; Kapur (2008, *Cognition and Instruction*)
[verify]; Carroll & Carrithers (1984, *Communications of the ACM*) [verify]; Lave & Wenger (1991)
[verify]; Norman (1983, in Gentner & Stevens) [verify]; Johnson-Laird (1983) [verify]; Hertwig &
Grüne-Yanoff (2017) [bib]; Kozyreva et al. (2020) [bib]; Kahneman & Klein (2009) [bib]; Bansal,
Nushi et al. (2019) [bib]; Kulesza et al. (2012) [bib].

### D. deskilling_debate
**RQ-D1.** What did the labor-process deskilling debate (Braverman, Attewell, Adler & Borys) settle
about whether deskilling is a property of technology or of the design of work?
**RQ-D2.** What is the current empirical status of LLM upskilling/deskilling claims — effect
direction, design (field vs. lab vs. self-report), and peer-review status — for Dell'Acqua et al.,
Noy & Zhang, Brynjolfsson et al., Lee et al., Gerlich, and Kosmyna et al.?
**RQ-D3.** What does cognitive-offloading research say about when offloading degrades retained skill
and when it does not?
**RQ-D4.** How does the *Phaedrus* complaint function as the archetype, and what have scholars said
about whether the feared loss (memory) was real and the gain (literacy) worth it?
**RQ-D5.** Does automation-complacency research supply a measurable criterion for "deskilling by
design" that transfers to adaptive intermediaries?
**Seed sources.** Braverman (1974) [verify]; Attewell (1987, *Work and Occupations*) [verify]; Adler
& Borys (1996, *ASQ*) [verify]; Vallor (2015) [card]; Plato, *Phaedrus* 274c–275b (Nehamas & Woodruff
trans. or Hackett) [verify edition]; Risko & Gilbert (2016) [bib]; Dell'Acqua et al. (2026) [bib];
Noy & Zhang (2023, *Science*) [verify]; Brynjolfsson, Li & Raymond (2025, *QJE*) [verify]; Lee et al.
(2025) [bib]; Gerlich (2025, *Societies*) [verify status and sample]; Kosmyna et al. (2025, arXiv
"Your Brain on ChatGPT") [verify preprint status]; Parasuraman & Manzey (2010) [bib]; Parasuraman,
Molloy & Singh (1993) [bib]; Ekbia & Nardi (2017) [card, dial].

### E. reading_history_meaning
**RQ-E1.** What is the defensible chronology of interpuncts, scriptio continua, Insular word
separation, and Continental adoption, and which claims in Saenger (1997) do Parkes (1992) and the
classicists contest?
**RQ-E2.** What does the Knox/Gavrilov/Burnyeat/Johnson literature establish about silent reading
in antiquity, so that the essay's analogy uses "made ordinary," never "made possible"?
**RQ-E3.** How do Martela & Steger's coherence, purpose, and significance map onto design
obligations, and has any HCI or design work already used the tripartite model this way (Mekler &
Hornbæk; Desmet & Pohlmeyer; Peters, Calvo & Ryan)?
**RQ-E4.** Where in Vallor (2016) are the occasions-for-practice and communicative-friction passages,
and which technomoral virtues (moral attention, prudence, technomoral wisdom) bear on steering an
intermediary?
**RQ-E5.** What exactly do Akrich (1992) and Latour (1992) mean by script, and how does Verbeek
(2005, 2011) take it up, so that the pitch's attribution is corrected?
**Seed sources.** Saenger (1997) [card: dial_response_algorithmacy/literature/cards/
saenger-1997-space-between-words.md, flagged "soften"]; Parkes (1992, *Pause and Effect*) [verify];
Knox (1968, *GRBS* "Silent Reading in Antiquity") [verify]; Gavrilov (1997) [card, not read in full];
Burnyeat (1997) [card, not read in full]; Johnson (2000) [card, not read in full]; Clanchy (2013),
Havelock (1963), Street (1984), Scribner & Cole (1981), Ong (1982), Eisenstein (1979), Johns (2002)
[cards: algorithmacy_design_ethics/literature/library/]; Martela & Steger (2016) [card, full text];
Vallor (2015, 2016, 2024) [cards]; Verbeek (2005, 2006, 2011, 2015) [cards]; Akrich (1992), Latour
(1992) [cards]; Peters, Calvo & Ryan (2018) [card, full text]; Mekler & Hornbæk (2019) [card, full
text]; Desmet & Pohlmeyer (2013, *International Journal of Design*) [verify].

---

## Open questions for the author (not decided here)

1. Keep "algorithmate" as an adjective (by the numerate parallel) or drop it entirely? Outline
   recommends drop.
2. Should Part 2 restate the Φ moderator/mediator line from Part 1, or leave information theory out
   of the ethics piece? Outline leaves it out except as a back-reference.
3. The cohort-discussion ask in the pitch (where are you "sounding things out") could close the essay
   as a reader prompt; the Part 1 register did not do this. Include or not?
4. Gerlich (2025) and Kosmyna et al. (2025): use only if facet D confirms status; otherwise cite
   Lee et al. (2025) and Fernandes et al. (2026) alone for the self-report/metacognition line.
