# Facet S — The 2026 HMI trajectory and read-to-check oversight

*Facet S, round 5, 2026-10-15. Agent-drafted (Fable). The author has not reviewed it, and none of the text is the author's.*

## What the facet covers

The facet serves the abstract's first three sentences (`../../ABSTRACT_v4.md`): human–machine interaction has moved to extended reality and integration; "whether on a factory headset or in an enterprise audit log ... the system still sends a person something to read so they can check the machine"; and "That approach assumes a dyad: an operator paired with a tool (Parasuraman, Sheridan, & Wickens, 2000)". Four questions from `round5_items.json`: (1) what the 2020–2026 HMI/HCI, XR, human-centred AI and oversight literature prescribes as the human's role; (2) how the supervisory-control lineage models the parties; (3) where that lineage admits several humans or teams, and whether the machine then becomes a party with its own objective; (4) evidence on how well people check machines by reading.

Existing cards read first: `grahn2026integration`, `mourtzis2026emerging`, `parasuraman2000types`, `parasuraman2010complacency`. Also consulted from the library: `eu2024regulation`, `green2022flaws`, `sheridan1978human`, `lee2004trust`, `alonbarkat2023human`, `sterz2024quest`, `laux2024institutionalised`, `crootof2023humans`, `langer2024effective`, `hutchins1995cockpit`, `santonidesio2018meaningful`, `vaccaro2024when`, `simkute2024ironies` (headers and relevant sections, not re-carded).

New cards (13): `bainbridge1983ironies`, `wiener1980flight`, `klein2004ten`, `onnasch2014human`, `oneill2022human`, `shneiderman2020human`, `enqvist2023human`, `enarsson2022approaching`, `koulu2020proceduralizing`, `lai2023towards`, `quandt2021systematic`, `demouracosta2022augmented`, `rayo2023cognitive`. Four of these keys (`bainbridge1983ironies`, `koulu2020proceduralizing`, `lai2023towards`, plus the long-cited `parasuraman2000types`) already stood in `../references.bib` without a card or with a partial read; they now have cards from full texts. Sections headed "Also used by facet S (2026-10-15)" were appended to `grahn2026integration`, `mourtzis2026emerging`, `parasuraman2000types`, `parasuraman2010complacency` and `eu2024regulation`.

Full texts are saved under `dxd_foundation_local/pdfs/S/` (outside the repo). Two sources (Koulu, Enarsson et al.) were read from the publishers' open-access HTML in a browser because their PDFs refused scripted download; the Chrome tab group was shared with other agents during the session and was navigated away from under me twice, so browser reading stopped after those two and the remaining publisher-blocked items (Goddard 2012, Holzinger et al. 2024, Ariansyah et al. 2022) are listed below as abstract-only.

## Search log

| Source | Query (exact) | Hits | Notes |
| --- | --- | --- | --- |
| Consensus | human oversight of AI systems EU AI Act Article 14 effectiveness human role monitoring | 20 | Sterz, Enqvist, Laux (carded already), Trapani 2026, Corrêa 2025, Banks 2026, Kaltenbrunner 2026, Holzinger 2024, Langer 2025 compliance testing; Enqvist opened and carded |
| Consensus | human-autonomy teaming review empirical literature teammate versus tool | 20 | O'Neill et al. 2020/2022 (carded), Lyons 2021 (already carded), Hagemann 2026 (N=80, abstract only), Kargarnovin 2026 (104 studies, not opened), McNeese 2018, Walliser 2019 |
| Consensus | industrial augmented reality head-mounted display operator information support systematic review | 20 | Fang 2023 HMD AR review (closed), de Moura Costa 2022 (carded), Quandt 2021 (carded), Ariansyah 2022 (OA but blocked), Seeliger 2023, Egger & Masood 2020 |
| Scholar Gateway | Does the supervisory control and levels-of-automation literature model the human as a single operator ... | 0 | "ACCESS_DENIED" — connector unavailable this session |
| Semantic Scholar API (paper/search) | 16 title queries (Bainbridge 1983; Parasuraman & Riley 1997; Endsley 1995; Klein et al. 2004; Hollnagel & Woods 1983; O'Neill 2022; Endsley 2017; Endsley 2023; Shneiderman 2020; Goddard 2012; Onnasch 2014; Wiener & Curry 1980; Wickens 2015; Mackworth 1948; Koulu 2020; Enarsson 2022) | 0 returned | The search endpoint returned empty data; the batch endpoint returned 429 (rate limit) on three attempts |
| Crossref (works?query.bibliographic) | the same 16 plus Strauch 2018, Christoffersen & Woods 2002, Holzinger 2024, Ariansyah 2022, de Moura Costa 2022, Fang 2023, Lai 2023 | 25 queries, 19 resolved | DOIs used for every bib entry; 6 queries failed on rate limiting and were resolved by OpenAlex or a later works/DOI call |
| Crossref (works/DOI) | 16 DOIs of the carded and lead sources | 16 | Bib fields taken from these records (saved in scratchpad crossref_S.txt) |
| OpenAlex (works?filter=doi:…) | 25 DOIs | 25 | Open-access status and pdf locations; found DiVA (Enqvist), DepositOnce (Onnasch), arXiv (Shneiderman), PMC (O'Neill) |
| Europe PMC REST | DOI searches for 7 items; fullTextXML for PMC9284085 and PMC3240751 | O'Neill XML obtained; Goddard XML returned 500 three times | NCBI efetch for PMC3240751 says the publisher does not allow XML download |
| NASA NTRS API | Wiener Curry flight-deck automation promises problems | 2 | TM 81206 PDF downloaded |
| WebSearch | Klein et al. 2004 "Ten challenges" pdf; Hollnagel & Woods 1983 pdf (two queries); Parasuraman & Riley 1997 pdf (two); Endsley 1995 pdf (two); Onnasch 2014 depositonce; Shneiderman 2020 pdf; Christoffersen & Woods 2002 pdf; Endsley 2023 pdf; Endsley & Kiris 1995 pdf; Enarsson diva-portal; Hollnagel Risø-M-2330 | 14 queries | Located DepositOnce record (Onnasch), arXiv (Shneiderman), the Bradshaw archive (Klein, via the site's index page); none for Endsley 1995, Parasuraman & Riley, Hollnagel & Woods |
| WebFetch | archive.cps-vo.org node 62405; depositonce item page; PMC9284085; jeffreymbradshaw.net; helda.helsinki.fi handle; tandfonline full (Enarsson); sciencedirect (Holzinger); nottingham-repository preview (Ariansyah) | 8 | DepositOnce and PMC gave links; Helda (Anubis), T&F, ScienceDirect and Nottingham returned 403 or an access-denied page |
| Direct download (curl) | ckrybus.com (Bainbridge), Bradshaw Dropbox (Klein), DepositOnce (Onnasch), DiVA (Enqvist), arXiv (Shneiderman, Lai), MDPI (de Moura Costa), Frontiers (Quandt), NSF PAR (Rayo), Europe PMC XML (O'Neill) | 10 files | All verified as PDFs or JATS XML; Sage, T&F, OUP, Elsevier and PMC PDFs refused |
| Browser (shared Chrome tab) | Sage HTML (Koulu); T&F HTML (Enarsson); PMC and OUP pages (Goddard) | 2 full reads | Goddard returned the OUP abstract page only; the tab was then taken over by another agent's navigation |

## Read-status legend

- **read in full**: whole text read from an open copy (publisher OA, repository, author archive, arXiv, NTRS).
- **read in part**: most of the text read; the gap is stated in the card.
- **abstract only**: only the abstract or a database record was seen; no card, listed below.
- **not accessible**: no abstract beyond the title was reachable; no card.

| Source | Status | Where read |
| --- | --- | --- |
| Bainbridge 1983 | read in full | journal PDF (mirror) |
| Wiener & Curry 1980 | read in part (NASA TM; Table 1 and guidelines 6–14 missing from the scan) | NTRS |
| Klein, Woods, Bradshaw, Hoffman & Feltovich 2004 | read in full | author archive (Bradshaw) |
| Onnasch, Wickens, Li & Manzey 2014 | read in full | TU Berlin DepositOnce |
| O'Neill, McNeese, Barron & Schelble 2022 | read in full | Europe PMC JATS XML |
| Shneiderman 2020 | read in full (arXiv v2; journal version not seen) | arXiv |
| Enqvist 2023 | read in full | DiVA (publisher PDF) |
| Enarsson, Enqvist & Naarttijärvi 2022 | read in full (HTML; footnotes 65+ skimmed) | T&F HTML in browser |
| Koulu 2020 | read in full (HTML; footnotes 9+ not shown) | Sage HTML in browser |
| Lai, Chen, Liao, Smith-Renner & Tan 2021/2023 | read in full (arXiv v1; FAccT version not seen) | arXiv |
| Quandt & Freitag 2021 | read in full | Frontiers |
| de Moura Costa, Petry & Moreira 2022 | read in full | MDPI |
| Rayo, Cooke, Flach, Hoffman, Smith & Woods 2023 | read in full (p. 183 from an image) | NSF PAR |

## Findings per question

### Q1. What the 2020–2026 literature prescribes as the human's role

**Industrial XR.** The two reviews carded here and the two already carded agree that the headset's job is to present information. De Moura Costa et al. (2022): AR solves "the 'human in the loop' integration problem by augmenting information properly into the operators' field of view" (`demouracosta2022augmented`, p. 3), and "The capacity of augmented reality to display real-time information to the user field of view is essential to insert the human in the loop" (p. 45). Of 32 papers, safety features were the most common application and most were "for informational purposes only" (p. 27); 13 of the 20 safety systems were "passive" (informational), 7 "active" (p. 29); none certified (p. 29). Quandt & Freitag (2021): AR gives "cognitive relief through the location-specific and context-related superimposition of real objects with virtual information" (`quandt2021systematic`, abstract), and after 33 papers "there is no widespread adoption" (p. 14). Mourtzis & Tsakalos (2026) and Grahn et al. (2026) say the same (existing cards). Role prescribed: receive instructions, warnings and status; check the robot's intent from a preview.

**Human-centred AI.** Shneiderman (2020) prescribes "high levels of human control AND high levels of automation" (`shneiderman2020human`, p. 1); reliability rests on "Audit trails and analysis tools to review failures & near misses" and "flight data recorders" (pp. 3–4); trust rests on independent oversight bodies (p. 4). The interface principles are "continuous visual display", "rapid, incremental, and reversible actions" and "informative feedback" (p. 13). He rejects the teammate metaphor outright (p. 5). Role prescribed: operate a controllable device; let organisations read the records.

**Human–AI decision making (HCI).** Lai et al. survey "over 100" studies (2018–2021): the paradigm is "to have models providing predictions, then users can choose to follow or ignore" (`lai2023towards`, §4.2.4, p. 20); the dominant assistance elements are explanations of the prediction and information about the model (Table 3); the alternatives (predict first, cognitive forcing, interactive explanation, user control of inputs) are a minority (§4.2.4). Role prescribed: read a prediction and its explanation, then accept or reject.

**Human–autonomy teaming.** O'Neill et al. review 76 studies: higher agent autonomy generally helps, reliability always helps, transparency is "mixed" and "may create a level of complacency that leads to less vigilance in overseeing or questioning the autonomous agent's work" (`oneill2022human`, Transparency and reliability). Role prescribed: team member who pushes and reads information; still "overseeing".

**Oversight under the EU AI Act.** Enqvist (2023): the overseer works "Through human intermediaries as interpreters of the data produced by the operating algorithms"; without transparency "the human overseers would have nothing substantive to review" (`enqvist2023human`, pp. 517–518); "There is no real point in performing the oversight if the overseer is not provided with information (or system output) in such a representation that it can interpret or understand" (p. 521); the Act leaves "a great deal of room for the providers to determine the detail on what human overseers will be presented with" (p. 525). Koulu (2020): oversight is adopted because "through digital traces and metadata we can easily ascertain that the oversight requirement has been fulfilled ... to have pressed the button, or ticked the box" (`koulu2020proceduralizing`, False promise section), and risks "turning human decision-makers into rubberstamps" (Conclusion). Enarsson et al. (2022): the human in the loop is "the overseer and correcting mechanism for the algorithmic predictions" (`enarsson2022approaching`, §1.2). Article 14(4) itself, in the enacted text, asks the assigned person to understand, monitor, "correctly interpret" the output, override and stop (`eu2024regulation`). Role prescribed: interpret outputs and logs; override; stop.

Summary for Q1: across XR, HCAI, HCI, teaming and law, the prescribed role is reading, monitoring and checking, with override and stop as the acts. The exceptions are design-side: Shneiderman's reversible actions and feedback, Lai et al.'s minority of agency-preserving workflows, and the teaming literature's directability.

### Q2. How the supervisory lineage models the parties

One operator and one automated system, from the start. Wiener & Curry (1980): the human "will be relegated to the post of monitor and decisionmaker, keeping watch for deviations and failures, and taking over when necessary" (`wiener1980flight`, p. 1); their Figure 1 has two dimensions, the operator monitoring the computer and the computer monitoring the operator (p. 13). Bainbridge (1983): the operator "may be expected to monitor that the automatic system is operating correctly" or take over (`bainbridge1983ironies`, p. 775); "The human monitor has been given an impossible task" (p. 776). Sheridan & Verplank (1978) and Parasuraman, Sheridan & Wickens (2000) allocate functions between "the human operator" and "automation" (existing cards). Onnasch et al. (2014) meta-analyse 18 experiments, every one an operator and an aid (`onnasch2014human`). Even the ATC example in Parasuraman et al. (controller, pilot, uplink, p. 293) keeps the operator–automation pair as the unit (existing card, S2-verified). Finding: the lineage's unit is the pair, and the automation has no objective of its own; it is an aid to the operator's task.

### Q3. Where the lineage admits several humans or teams, and whether the machine becomes a party

Three places, and in none does the machine acquire an objective against the people it faces.

- **Joint cognitive systems (Hollnagel & Woods 1983; Rayo et al. 2023).** The unit is the system: "The cognition resides not only in the head of an individual, but in components of the system and their interactions" (`rayo2023cognitive`, p. 184, Cooke); a new tool "may result in adaptations that influence the work patterns of several interdependent people" (p. 183, Smith); Woods calls the levels proposals "obsolete, narrow, and/or counterproductive" (p. 185). Several humans, yes; the machine is a component of one system with one purpose. The 1983 paper itself has no open copy (not accessible).
- **Joint activity and "team player" automation (Klein et al. 2004).** An "ensemble of people" coordinating; agents must enter a Basic Compact, which "involves a commitment to some degree of goal alignment" and "one or more participants relaxing their own shorter-term goals" (`klein2004ten`, p. 91); Challenge 7 is goal negotiation (p. 93). Here the machine does have goals, but the design aim is to align them with the team's; the agent is at best "a young child or a novice" teammate (p. 94).
- **Human–autonomy teaming (O'Neill et al. 2022).** A HAT requires "a common goal as a collective"; 22 of 76 studies had two or more humans, 7 had several agents, 45 of 76 had one human and one agent; all were laboratory simulations, and the authors describe the evidence base as "dyads" (`oneill2022human`). The agent counts as a teammate only above level 5 on the Parasuraman scale, that is, with decision latitude, but never with a divergent objective.
- **Oversight law (Enqvist 2023; Enarsson et al. 2022; Koulu 2020).** The structure is a chain, provider to deployer to overseer to system, with affected persons as rights-holders without an interface (`enqvist2023human`, pp. 518–530); or decision-maker, system and subject (`enarsson2022approaching`, `koulu2020proceduralizing`). Three positions, but the act of oversight is one reader facing one system's output, and the subject does not coordinate with anyone through the system.

Finding: the lineage admits teams and chains; it treats the machine as a tool, a component or an aligned teammate; the interested mediator between two counterparts is absent.

### Q4. Evidence on how well people check machines by reading

- Vigilance: Bainbridge reports from Mackworth that effective attention to a source "on which very little happens" lasts about half an hour (`bainbridge1983ironies`, p. 776); logging does not help: "people can write down numbers without noticing what they are" (p. 776). The original study (`mackworth1948breakdown`) remains inaccessible.
- Complacency and bias: `parasuraman2010complacency` (existing card): detection of automation failures 33% under constant reliability against 82% under variable reliability in multitask conditions; 75% of pilots followed a wrong automated checklist against 25% with paper. Wiener & Curry: a training manager doubled command training after automation bred "inactivity or complacency" in first officers (`wiener1980flight`, p. 9).
- Degree of automation: across 18 experiments, return-to-manual performance fell with automation (tau −.34) and collapsed when action selection was automated (tau −.90 across six studies); the authors attribute the protection of keeping the choice to the generation effect (`onnasch2014human`, pp. 483–485).
- Transparency: in teaming studies, more of the agent's reasoning to read raised workload and in some studies complacency (`oneill2022human`, Transparency and reliability; Wright et al. 2016, Sadler et al. 2016 as cited there).
- A fielded case: the Swedish Social Insurance Agency's partially automated sickness-benefit process hands administrators a machine-generated interruption document and pre-collected facts; the internal audit found investigations insufficient in 67 percent of cases, correct decisions in 76 percent of those, and only about a quarter of cases both properly investigated and correct (`enarsson2022approaching`, §4.3).
- Public-sector experiments: `alonbarkat2023human` (existing card): selective adherence to algorithmic advice in three preregistered experiments.
- Abstract-only: Goddard, Roudsari & Wyatt (2012) report, from 74 included papers, that automation bias is mediated by cognitive style, experience, trust and workload and mitigated by training, accountability, the position of advice on screen and "the provision of information versus recommendation" (OUP abstract); not carded.

Finding: the evidence is consistent that reading to check degrades with time, reliability and the amount handed over; the one lever the dyadic literature finds is keeping the person in the choosing (Onnasch; Parasuraman & Manzey's information-analysis aids), which is the abstract's "epistemic action" in the dyad's own terms.

## What this means for the abstract's sentence

The facet's sentence: "Yet, whether on a factory headset or in an enterprise audit log (Nadella, 2026), the system still sends a person something to read so they can check the machine. That approach assumes a dyad: an operator paired with a tool (Parasuraman, Sheridan, & Wickens, 2000)."

| Claim | Verdict | Grounds |
| --- | --- | --- |
| HMI has moved to XR and integration (sentence 1) | supported | `mourtzis2026emerging`, `grahn2026integration` (existing); `demouracosta2022augmented` dates the HMD turn to 2016–2018 |
| On a factory headset the system sends the person something to read to check the machine | supports a narrower form | The headset mostly sends instructions, warnings and status; checking the robot is one use (trajectory previews, digital twins) among guidance and safety, and most safety content is informational and uncertified (`demouracosta2022augmented`, pp. 27–29, 45). "Something to read" holds; "so they can check the machine" is narrower than the field's own purpose, which is to tell the worker what to do |
| In an enterprise audit log the system sends the person something to read to check the machine | supported | Audit trails as the reliability practice in `shneiderman2020human` (pp. 3–4); Article 12 logs and Article 14 interpretation duties in `enqvist2023human` (pp. 518–523) and `eu2024regulation`; Koulu on the record as the reason oversight is adopted (`koulu2020proceduralizing`); Nadella P15 (`nadella2026models`, existing) |
| That approach assumes a dyad: an operator paired with a tool | supports a narrower form | For the supervisory lineage and HCI decision-support studies the dyad holds (`wiener1980flight`, `bainbridge1983ironies`, `onnasch2014human`, `lai2023towards`; 45 of 76 teaming studies in `oneill2022human`). Joint cognitive systems, joint activity and teaming admit several humans and agents with goals (`rayo2023cognitive`, `klein2004ten`, `oneill2022human`), and oversight law is a provider–deployer–overseer chain (`enqvist2023human`). The defensible form: the approach assumes that the machine serves the person who reads it; it has no place for a mediator with an objective of its own between two counterparts |
| The attribution to Parasuraman, Sheridan & Wickens (2000) | supported, with a caveat | The model's unit is the operator–automation pair (existing card, S2-verified); its own ATC example involves controller and pilot, and Shneiderman (2020) and Woods (2023) both attack the levels model as the field's limiting frame, so the citation names the right anchor but a reviewer can point to the model's multi-person example |
| Implied: checking by reading works badly | supported, inside the dyad | `bainbridge1983ironies`, `onnasch2014human`, `parasuraman2010complacency`, `enarsson2022approaching` §4.3; no study in a triad |

Two things cut against the abstract's direction rather than its sentence. First, the dyadic literature already contains the remedy the abstract proposes: Bainbridge's feedback "within a few seconds" (p. 777), Shneiderman's reversible actions with immediate feedback (p. 13), Onnasch et al.'s "keep the operator in decision and action selection" (p. 486), Klein et al.'s directability and mutual predictability. The abstract's "smoking gun" has to be shown to differ from these by crossing to the triad, not by being feedback or action as such. Second, Shneiderman keeps the dyad on purpose (computers "are not teammates", p. 5), so "assumes a dyad" is, for the leading HCAI statement, a chosen position, not an oversight; the paper should argue against the choice, not describe it as an assumption.

## Abstract-only and inaccessible leads

| Source | Status | What was seen |
| --- | --- | --- |
| Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: a systematic review of frequency, effect mediators, and mitigators. *JAMIA, 19*(1), 121–127. doi:10.1136/amiajnl-2011-000089 | abstract only | OUP abstract page in browser: 13,821 retrieved, 74 included; mediators and mitigators listed, including "the provision of information versus recommendation". PMC3240751 exists but the PMC page, Europe PMC XML (500) and NCBI efetch (publisher forbids XML) all failed |
| Holzinger, A., Zatloukal, K., & Müller, H. (2025). Is human oversight to AI systems still possible? *New Biotechnology, 85*, 59–62. doi:10.1016/j.nbt.2024.12.003 | abstract only | Consensus record; gold OA per OpenAlex but ScienceDirect refused WebFetch and curl |
| Ariansyah, D., et al. (2022). A head mounted augmented reality design practice for maintenance assembly. *Applied Ergonomics, 98*, 103597. doi:10.1016/j.apergo.2021.103597 | abstract only | Consensus record: 3D animation 14% faster than video; eye-gaze; "overreliance" raised from a joint-cognitive-systems view. Nottingham repository preview returned 403 |
| Fang, W., et al. (2023). Head-mounted display augmented reality in manufacturing: A systematic review. *RCIM, 83*, 102567. doi:10.1016/j.rcim.2023.102567 | abstract only | Consensus record; closed |
| Hagemann, V., et al. (2026). Team member or tool? The role of framing in human-autonomy teaming. *IJHCI*. doi:10.1080/10447318.2026.2634249 | abstract only | Consensus record: N = 80, Mars habitat task, no trust or affect difference between framings |
| Kargarnovin, S., et al. (2026). From testbeds to high-stakes work: a review of human-AI teaming domains. *Frontiers in Robotics and AI*. doi:10.3389/frobt.2026.1733942 | abstract only (open, not opened for time) | Consensus record: 104 empirical studies 2015–2025 |
| Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32–64. doi:10.1518/001872095779049543 | abstract only | Search-result abstracts; closed; no repository copy found |
| Endsley, M. R., & Kiris, E. O. (1995). The out-of-the-loop performance problem and level of control in automation. *Human Factors, 37*(2), 381–394 (`endsley1995out` in the bib) | abstract only | As before; one of the 18 studies in `onnasch2014human` |
| Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors, 39*(2), 230–253. doi:10.1518/001872097778543886 | abstract only | Search-result abstracts; closed |
| Endsley, M. R. (2017). From here to autonomy. *Human Factors, 59*(1), 5–27. doi:10.1177/0018720816681350 | not accessible | Closed; cited by `oneill2022human` and `shneiderman2020human` |
| Endsley, M. R. (2023). Supporting human-AI teams: Transparency, explainability, and situation awareness. *Computers in Human Behavior, 140*, 107574 | abstract only | Webinar abstract via WebSearch; closed |
| Hollnagel, E., & Woods, D. D. (1983). Cognitive systems engineering: New wine in new bottles. *IJMMS, 18*(6), 583–600. doi:10.1016/S0020-7373(83)80034-0 | not accessible | Closed; the 1982 Risø report is catalogued but not online; summarised in `rayo2023cognitive` |
| Christoffersen, K., & Woods, D. D. (2002). How to make automated systems team players. *Advances in Human Performance and Cognitive Engineering Research, 2*, 1–12. doi:10.1016/S1479-3601(02)02003-9 | abstract only | Emerald abstract via WebSearch; cited in `klein2004ten` |
| Mackworth, N. H. (1948). The breakdown of vigilance during prolonged visual search (`mackworth1948breakdown`) | not accessible | As before |
| Strauch, B. (2018). Ironies of automation: Still unresolved after all these years. *IEEE THMS, 48*(5), 419–433. doi:10.1109/THMS.2017.2732506 | not accessible | Closed |
| Wickens, C. D., Clegg, B. A., Vieane, A. Z., & Sebok, A. L. (2015). Complacency and automation bias in the use of imperfect automation. *Human Factors, 57*(5), 728–739. doi:10.1177/0018720815581940 | not accessible | Closed; the meta-analysis that would extend `onnasch2014human` |
| Lindgren, I. (2024). Ironies of automation and their implications for public service automation. *Government Information Quarterly*. doi:10.1016/j.giq.2024.101974 | not opened | Hybrid OA per OpenAlex; found via Semantic Scholar's one successful query |
| National Academies (2022). *Human-AI Teaming: State-of-the-Art and Research Needs* | not opened | Free PDF requires a login |
