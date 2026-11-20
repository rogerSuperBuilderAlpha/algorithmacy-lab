#!/usr/bin/env python3
"""Build DRAFT_v10.md from DRAFT_v9.md (the authors' rewrite) by targeted edits only.

DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026. No sentence is rewritten as a whole. Three kinds of change:
  T  targeted fixes from reviews/2026-11-13/SYNTHESIS.md, each an exact old -> new replacement that
     must match exactly once in the text (the script stops otherwise);
  M  mechanical house-style passes (Intellect Harvard, JOURNAL_SPEC.md): single quotation marks with
     double inside, punctuation outside the closing mark, British spelling with -ize, spaced en
     rules for dashes, missing spaces, headings and tables as markdown, paste artefacts removed;
  A  assembly: title line, Figure 1 and its caption, AI acknowledgment, references, cases and
     legislation, all copied from DRAFT_v8.md's assembly (v8_2026-11/assembly/).
Writes ../DRAFT_v10.md, ../DRAFT_v10_marked.md (content changes marked against v9 after the
mechanical passes: ~~deleted~~ and **[C: inserted]**) and V10_CHANGES.md's change table.
Usage: python3 build_v10.py
"""
import difflib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MS = HERE.parent
V8A = MS / "v8_2026-11" / "assembly"

raw = (MS / "DRAFT_v9.md").read_text(encoding="utf-8")
raw = raw[raw.index("Abstract\n"):]                     # drop the provenance comment


def prenorm(t):
    """Typographic normalization so edits can be written against one character set."""
    return t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')


# ---------------------------------------------------------------------------------------------
# T: targeted fixes. (old, new, synthesis reference, reason). Old text is v9's, after prenorm.
# ---------------------------------------------------------------------------------------------
T = [
 # Abstract
 ("guests often cannot reach anyone", "guests cannot always reach anyone",
  "§4.11", "The abstract claimed guests 'often' cannot reach anyone; the conclusion says this is still to be measured."),
 ("when it invites travelers in, earns their trust, and controls the physical space, and it keeps them even when",
  "when it invites travelers in, earns their reliance, and controls the physical space, and it keeps the duty of care even when",
  "§2, §4.2, §4.11", "'Trust' → 'reliance', the term the body uses; 'keeps them' (both duties) → 'keeps the duty of care', as the introduction and conclusion state and the body supports (liability for contractors' work 'narrows')."),
 ("During a stay, the guest's standing also requires a timely route to reach someone who can correct a failure on the spot.",
  "During a stay, the guest's claim also requires a timely route to reach someone who can correct a failure.",
  "§2, §4.1, §4.11", "Ground of the further duty: 'standing' → 'claim', as 'During the stay' derives it; 'on the spot' dropped, since the body asks only for correction during the stay."),
 ("outlines five steps for host accountability", "outlines five stages from audit to accountability",
  "§4.11, §4.13", "Table 2 has five 'stages', and only the last is accountability."),
 # Introduction
 ("Hotel managers kept the final say over rates, logging in each day to compare",
  "Hotel managers kept the final say over rates and could log in each day to compare",
  "§5 #28", "Garcia et al.: the manager decides each day whether to log in ('If she logs into the system …'); v8 had 'could log in'."),
 ("Knowing that managers rarely intervened, the vendor designed the pricing engine to exaggerate rate shifts",
  "Because managers rarely intervened, the vendor had an incentive to design the pricing engine to exaggerate rate shifts",
  "§4.8", "The source states an incentive ('The algorithm's designer has an incentive to offer recommendations that exaggerate the change'), not the vendor's knowledge or design."),
 ("Here, digital media adds delight", "Here, on our reading, digital media adds delight",
  "§5 #16", "Staff discretion is not in Batat (2021); v8 marked this as the authors' reading."),
 ("remain within reach and can adjust the experience on the spot.", "remain within reach.",
  "§5 #16", "'Can adjust the experience on the spot' is not in Batat (2021)."),
 ("At resort hotels, pricing authority shifts to a software model",
  "At resort hotels, authority over the pricing rule shifts to a software model",
  "§4.8", "'Pricing authority shifts' contradicted 'kept the final say' two paragraphs earlier; the vendor holds the rule, the managers the price (as 'The vendor' says)."),
 ("though the framework applies to any phygital service where", "though the framework may extend to other phygital services where",
  "§4.9", "'Applies to any phygital service' is not shown; the argument rests on lodging (and Groh's holding is confined to hotels)."),
 ("several parties may owe care simultaneously in proportion to their control.",
  "several parties may owe care simultaneously according to their degree of control.",
  "§5 #25", "Wheat v E Lacon: 'dependent on his degree of control', not proportion."),
 ("Third, the guest's standing during a stay grounds a further duty",
  "Third, the guest's claim during a stay grounds a further duty",
  "§2, §4.1", "Ground of the further duty: 'standing' → 'claim' (see l. 41 and 'During the stay')."),
 # Theoretical context
 ("calling it a relay exposes an operational question", "calling it a relay exposes an operational question",
  None, None),  # placeholder kept out of the table (no change)
 ('describe this movement as "fluidity" (Batat', "describe this movement as fluidity (Batat",
  "§5 #3", "Neither source uses the noun in quotation: Batat 2024: 1220 has 'fluidifying', Batat and Hammedi 2023: 17 'fluid'."),
 ("who retains room for judgment, at each handoff", "who retains room for judgement, at each handoff",
  "M", "British 'judgement' outside legal usage."),
 ("in which another party owes you enforceable care", "in which another party owes the guest enforceable care",
  "§4.13", "Second-person address (Reviewer 3, round one)."),
 ("Elizabeth Telfer similarly treats guest safety as the host's primary obligation",
  "Elizabeth Telfer, as Hemmington reports her, similarly treats guest safety as traditionally the host's primary obligation",
  "§5 #18", "Telfer is read through Hemmington, who reports her as saying 'traditionally the most important responsibility of all was the guest's safety'."),
 ("Read together, these accounts show that admitting", "We read these accounts together as showing that admitting",
  "§5 (panel 01 F3)", "The synthesis is the authors' reading, not something the sources show; v8's form."),
 ("Some scholars doubt whether paid lodging qualifies as hospitality at all, since commercial access ends the moment payment stops (Lashley 2015: 5), leading Slattery to argue that",
  "Some scholars doubt whether a host who charges can be hospitable at all, since commercial access ends the moment payment stops (Lashley 2015: 5), and Slattery argues that",
  "§5 #17", "Lashley (p. 5) doubts the hospitableness of commercial hosting, not whether paid lodging is hospitality; a 2002 article cannot follow from a 2015 one."),
 ("Service research has largely treated the frontline employee as the host",
  "Service research has, on our reading, largely treated the frontline employee as the host",
  "§5 #19", "'Host' never occurs in Odekerken-Schröder et al.; v8 marked this as the authors' reading."),
 ("contestability refers to a technical mechanism", "contestability, as design work mostly uses it, refers to a technical mechanism",
  "§4.7", "Unhedged, the definition makes contestability lose; Alfrink et al. and Lyons et al. already require a human with power to change the decision. v8's hedge."),
 ("examined below, while standing names the position", "examined below; standing does not ground it but names the position",
  "§2, §4.1", "Restores v8's statement that standing does not ground the duty, which closes Reviewer 2's circularity."),
 ("When undercooked burgers from a cooking robot sicken diners, Sharma and Mattila ask",
  "When, in their hypothetical case, undercooked burgers from a cooking robot sicken diners, Sharma and Mattila ask",
  "§5 #29", "The burger case is hypothetical, not an event."),
 ("leaving the question to corporate risk management (2026: 904)", "leaving the question to governance and risk management (2026: 904)",
  "§5 #29", "Sharma and Mattila: 'governance and risk-management for the industry'."),
 # The host's duty in law
 ('"hangs out a sign and opens his house for travelers"', '"hangs out a sign and opens his house for travellers"',
  "§5 #2", "The source spells 'travellers'; the quotation had been Americanized."),
 ('modern English negligence law applies this directly, holding that a hotel that "guests to come and stay"',
  'a modern English court applies this directly, holding that a hotel that "invited guests to come and stay"',
  "§5 #1", "The quotation had lost 'invited' (Al-Najar 2019: para 187); one High Court judgment is 'a modern English court', as v8 had it."),
 ("None of these three elements suffices on its own.", "No single ground suffices on its own.",
  "§4.3", "The sentence named 'these three elements' and then argued it for a different three (undertaking, reliance, vulnerability)."),
 ("(Jeske 2021: §§3–4; Habib", "(Jeske 2021: §§3–4, 7; Habib",
  "§5 #27", "Jeske's reliance clause is at §7."),
 ("occupiers continue to owe care in proportion to their control over the premises", "occupiers continue to owe care according to their degree of control over the premises",
  "§5 #25", "Wheat v E Lacon: 'dependent on his degree of control'."),
 ('Statute still assigns an innkeeper\'s core duties to "the proprietor" alone',
  'Statute still assigns an innkeeper\'s duties to "the proprietor" alone',
  "§4.2", "The 1956 Act does not carry the guest-safety duty, which comes from modern negligence (Al-Najar paras 183, 187); 'core' tied the statute to the two core duties."),
 ("and it gives us a clear test for assigning duties", "and it gives us a test for assigning duties",
  "§4.13", "Sentence grading the paper's own argument."),
 # Approach
 ("we found the problem widely noted but never derived from the host role itself",
  "we found the problem widely noted but, in the literature we searched, never derived from the host role itself",
  "§4.7", "An absence claim needs its search scope; v8's hedge."),
 ("Our claims also carry clear evidentiary and legal bounds.", "Our claims also carry evidentiary and legal bounds.",
  "§4.13", "Sentence grading the paper's own argument."),
 ("Outside European package-travel law, platform-moderation rules, and disability-accommodation mandates, the further duty",
  "Outside European package-travel law, platform-moderation rules, disability-accommodation mandates, and the rules on solely automated decisions, the further duty",
  "§4 (finding 7 of the brief)", "The three lists of exceptions disagreed; this one now matches 'At the touchpoint' (l. 158)."),
 # The parties
 ("These arrangements fail because the link between", "These arrangements fail when the link between",
  "§4.3", "Not every phygital arrangement fails; the sentence states the condition."),
 ("the traditional innkeeper took custody of a stranger's person and belongings",
  "the traditional innkeeper received a stranger's person and belongings",
  "§5 #21", "Sandoval-Strausz does not say custody of the person; v8's verb."),
 ("public service providers are also barred from refusing service on any protected ground (Equality Act 2010, s.29(1))",
  "providers of a service to the public are also barred from refusing service on any protected ground (Equality Act 2010, s. 29(1))",
  "§5 #6", "Section 29(1) binds 'A person … concerned with the provision of a service to the public', not public-sector providers only."),
 ("and a guest who receives substandard service can demand repeat performance",
  "and a consumer guest who receives substandard service can demand repeat performance",
  "§5 #30", "The Consumer Rights Act right belongs to consumers (s. 2(3)), not business travellers."),
 ("(Ferguson v Welsh1987: 7)", "(Ferguson v Welsh 1987: 7)", "M", "Missing space."),
 ("(Naylor v Payling 2004: paras 19, 50; Maguire v Sefton 2006:para 30)", "(Naylor v Payling 2004: paras 19, 50; Maguire v Sefton 2006: para 30)", "M", "Missing space."),
 ("and no English judgment we examined imposes one on a hotel toward an adult guest.",
  "and since the 1957 Act, absent contrary terms, a hotel's contract with its guest implies only the common duty of care (Maguire v Sefton 2006: paras 21–24).",
  "§5 #7", "MacLenan v Segar [1917] 2 KB 325 implied an innkeeper's warranty that premises are as safe as care 'on the part of anyone' can make them; Maguire (paras 21–24) holds that the 1957 Act replaced such terms with the common duty of care. The absolute claim was false as written."),
 ("Yet, they hesitated to exceed 10 to 20 percent of the room rate because management had never defined the limits of their authority",
  "Yet, they hesitated to exceed 10 to 20 percent of the room rate and did not know where their authority ended",
  "§5 #14", "Schumacher and Komppula give the two facts side by side ('Even though', p. 122), not as cause and effect; v8's wording."),
 ("reservation agents often hold formal latitude to override prices suggested by revenue-management software. However, Bendoly (2013) shows that whether they exercise that discretion depends on their own judgment",
  "reservation agents often hold formal latitude to accept rates below those suggested by revenue-management software. However, Bendoly (2013) notes that whether they exercise that discretion depends largely on their own judgement",
  "§5 #15", "Bendoly's abstract (abstract only): agents are 'often given the latitude' to accept rate bids below the system's price, and deviation depends 'in large part' on their judgement; these are premises, so 'notes', not 'shows'."),
 ("Algorithmic tools can strip away even that informal leeway", "Algorithmic tools can strip away even that leeway",
  "§5 (panel 04)", "The latitude was called 'formal' one sentence earlier."),
 ("multiple parties can share that duty in proportion to their control.", "multiple parties can share that duty according to their degree of control.",
  "§5 #25", "Wheat v E Lacon: 'dependent on his degree of control'."),
 ("(2026:78–79)", "(2026: 78–79)", "M", "Missing space."),
 ("vicariously liable under apparent agency because the company exercised a 'significant degree of control over the operation'",
  "vicariously liable under apparent agency because the company held the motel out as its own and kept a 'significant degree of control over the operation'",
  "§5 #11", "Crinkley's apparent agency rests on holding out and reliance (paras 49–52); the court also found the franchisor 'retained a significant degree of control' (para 51)."),
 ("paper.pdf+ 2\n\n", "", "§4.12", "Paste artefact removed."),
 ("Bosma's fieldwork reveals that a single listing", "Bosma reports that a single listing",
  "§5 #23", "The three host roles are Airbnb's categories, not findings of her fieldwork."),
 ("while automated smart locks replace any in-person key handover (2022:605)",
  "while self-check-in can replace the in-person key handover (2022: 605)",
  "§5 #23", "Her host Elli still hands over keys (p. 602), so not 'any'; v8: 'self-check-in replaces the handover of keys'."),
 ("and authority is the power to rewrite the underlying rule or answer for its design.",
  "and authority is the power to rewrite the underlying rule.",
  "§4.13 (terms)", "'Or answer for its design' folded accountability into authority, which 'The host' keeps apart."),
 ("In the European hotel study, the vendor held authority", "In the hotel pricing study, the vendor held authority",
  "§5 #24", "Only the vendor is based in Europe; the study does not locate the hotels."),
 ("a guest can easily reach a staff member who lacks discretion to override a software output, while never reaching the vendor who controls the rule.",
  "a guest can easily reach a staff member with discretion over a single output, while never reaching the vendor who controls the rule.",
  "§4.8", "The paragraph had just said the managers kept discretion; the split is discretion (case) against authority (rule)."),
 ("each firm answers only for its own conduct, because a loose supply chain does not constitute a single moral or legal agent (Kong 2026: 9; Pettit 2007: 195).",
  "no single firm answers for the whole, because a loose supply chain does not constitute a single moral agent (Pettit 2007: 195).",
  "§5 #8, §4.2", "Kong argues the opposite (delegation 'does not diminish principal responsibility'), and 'each firm answers only for its own conduct' contradicted the package-travel rule (l. 51); 'or legal' is not in Pettit."),
 ("rather than a freestanding obligation to monitor every daily interaction (RR v Enfield 2025: paras 80–81)",
  "rather than a freestanding obligation to monitor (RR v Enfield 2025: paras 80–81)",
  "§5 #10", "'Every daily interaction' is not in the judgment; v8: 'not a free-standing duty to monitor'."),
 ("one rule holds consistently: physical control over the guest's space anchors the duty of care, and multiple organizations can share that duty in proportion to their control.",
  "one rule recurs: physical control over the guest's space anchors the duty of care, and multiple organizations can share that duty according to their degree of control.",
  "§4.3, §5 #25", "The brand, the platform, package travel and the state bind without control, so the rule recurs rather than 'holds consistently'; Wheat's 'degree of control'."),
 ("neither the law of delegation nor moral philosophy obliges a delegator", "neither the law of delegation nor its moral philosophy obliges a delegator",
  "§4 (finding 7 of the brief)", "The claim rests on Brandt; the next section derives such a duty from moral philosophy itself. v8: 'its moral philosophy'."),
 # During the stay
 ("and an animated projection fills a single wait before dinner.", "and an animated projection accompanies a single meal.",
  "§5 #16", "Le Petit Chef runs through the meal (Batat 2021: 4), not one wait before it."),
 ("kept quiet about poor conditions because she could not afford to leave (2023)", "kept quiet because she could not leave (2023)",
  "§5 #20", "The source has neither 'poor conditions' nor 'afford'."),
 ("neither host nor guest can assert absolute sovereignty", "neither host nor guest can assert sovereignty",
  "§5 (panel 08)", "'Absolute' is not Bulley's."),
 ("one of the guest's primary forms of power (Moysidou and Stanley 2023)", "one of the guest's forms of power (Moysidou and Stanley 2023)",
  "§5 #20", "The source speaks of 'latent forms of power', not primary ones."),
 ("As Herstein explains in summarizing Joseph Raz's theory of rights, a single claim-right can justify new and shifting duties",
  "As Herstein reports in summarizing Joseph Raz's theory of rights, a single claim-right can seemingly justify new and shifting duties",
  "§5 #13", "Herstein: a claim-right 'seemingly can count in favor of different and changing duties' (§8.4), a view he reports."),
 ("Under the principle of instrumental normativity, an obligation to achieve an end extends to the means necessary to achieve it",
  "Under the principle of instrumental normativity, an 'ought' to achieve an end extends to the means necessary to achieve it",
  "§4.1", "Kiesewetter's principle concerns the transmission of an 'ought' to necessary means, not obligation as such."),
 ("as a matter of right rather than depending on staff goodwill.", "as a matter of right rather than depending on the host's goodwill.",
  "§4.10", "v9 moved the dependence from the host to the staff in three places, which loads the clerk; v8's 'the host's goodwill'."),
 ('which rests partly on general risk to others and is not owed to a specific claimant (2025: 4–5)',
  'which rests partly on general risk to others and which he does not say is owed to anyone (2025: 4–5)',
  "§5 #26", "Hindriks does not say the duty is owed to anyone; v8's wording."),
 ("European and British statutes routinely prioritize live repair over post-hoc payment, requiring package-travel organizers to remedy defects during a trip, service providers to repeat substandard work, and digital platforms to rectify automated worker decisions, turning to compensation only when rectification is impossible",
  "Several European and British statutes prioritize live repair over post-hoc payment, requiring package-travel organizers to remedy defects during a trip, service providers to repeat substandard work, and digital platforms to rectify automated worker decisions or, where that is impossible, to compensate",
  "§5 #9", "Three instruments, not 'routinely'; the compensation-only-if-impossible rule is the platform-work directive's alone (art. 11(3)); the Consumer Rights Act (s. 56(3)(b)) and the package-travel directive (arts 13(3)(b), 14(1)) give price reduction and compensation alongside."),
 ("This temporal boundary also clarifies why studies showing high guest acceptance of hotel automation require careful interpretation. Guests may care little whether a human clerk or a lobby robot gives them directions, because the stakes of that exchange are low (Schmidt et al. 2025).",
  "This temporal boundary also clarifies why studies of guest acceptance of hotel automation require careful interpretation. Guests may care little whether a human clerk or a lobby robot gives them directions (Schmidt et al. 2025), on our reading because the stakes of that exchange are low.",
  "§5 #22", "Schmidt et al. found indifference between robot and human, not 'high acceptance'; the stakes explanation is the authors' gloss."),
 ("Friction is valuable only because it creates a pause", "On this reading, friction is valuable because it creates a pause",
  "§4 (brief finding 10)", "'Only because' contradicted the Le Petit Chef case; v8 marked this as a reading."),
 # At the touchpoint
 ("A facial-recognition kiosk in a lobby, a numeric keypad on a rental door, or a pricing screen at a manager's desk bridges",
  "A facial-recognition kiosk in a lobby or a numeric keypad on a rental door bridges",
  "§4.8", "A manager's pricing screen is not a touchpoint by the paper's own definition (a moment where the guest interacts with the arrangement)."),
 ("That reporting route doesn't always have to end with a human.", "That reporting route does not always have to end with a human.",
  "M", "Contraction."),
 ("most facial-recognition errors cleared up when guests stepped back and tried again",
  "every facial-recognition error cleared up when guests stepped back and tried again",
  "§5 #5", "All 610 guests who reached the face scan were recognized (Xu and Greiffenhagen 2024: Figure 11, p. 5027)."),
 ("When retrying fails, however, repair requires the authority to override the software's output, as when a clerk manually checked in the thirteen guests whom the kiosk rejected (5035).",
  "When retrying cannot help, however, repair requires the authority to override the software's output, as when a clerk manually checked in the thirteen guests whom the kiosk could not process (5035).",
  "§5 #5", "The thirteen were not recognition failures or rejections: the kiosk was off, an ID was unreadable, reservations were not found, a process froze (p. 5035, n. 4)."),
 ('must allow human overseers to "disregard, override or reverse the output,"',
  'must allow human overseers, as appropriate and proportionate, to "disregard, override or reverse the output,"',
  "§5 #12", "Art. 14(4) applies 'as appropriate and proportionate'; v8 carried it."),
 ("Whoever holds that override power must also exercise it with reasonable care.",
  "The host must also ensure that whoever holds that override power exercises it with reasonable care.",
  "§4.10", "In Groh the duty is the hotel's, not the guard's (¶¶ 4, 23)."),
 ("and the guard evicted them into the cold anyway", "and the guards evicted them anyway",
  "§5 #31", "The court lists the weather as a factor but the facts cited do not say it was cold; guards (plural) escorted the group out."),
 ("Training builds competence, whereas organizational rules confer standing.", "Training builds competence, whereas organizational rules confer authority.",
  "§4.1", "Standing is the guest's; for staff the word is authority (and conferred standing would undercut the ground of the duty)."),
 ("as the UN Guiding Principles observe, analyzing complaint patterns", "as the UN Guiding Principles observe, analysing complaint patterns",
  "M", "British spelling."),
 ("can the guest use it without relying on staff goodwill or incurring an unfair penalty?",
  "can the guest use it without relying on the host's goodwill or incurring an unfair penalty?",
  "§4.10", "See l. 117."),
 ("Applying these questions pinpoints exactly where a touchpoint breaks down.", "Applying these questions shows where a touchpoint breaks down.",
  "§4.13", "Sentence grading the paper's own argument."),
 ("the escalation path ended with a clerk authorized to override the kiosk, yet rejected guests had to find that worker themselves; the arrangement passes the third question while failing the second (Xu and Greiffenhagen 2024: 5021, 5035).",
  "the escalation path ended with a clerk able to check guests in by hand, yet guests the kiosk could not process had to find that worker themselves; the arrangement passes the third question while failing the second (Xu and Greiffenhagen 2024: 5035).",
  "§5 #4, #5", "The study says the worker 'manually checked them in', not that the worker was authorized to override; p. 5021 records the worker approaching guests, so only p. 5035 supports the sentence."),
 ("Yet the plaintiffs alleged those guards lacked training", "Yet Groh alleged those guards lacked training",
  "§3.3", "One plaintiff: 'Groh alleges …' (¶ 13)."),
 ("In Great Britain, disability law may entitle a guest to human assistance", "In Great Britain, disability law may entitle a disabled guest to human assistance",
  "§5", "Reasonable adjustments are owed to disabled persons (Equality Act 2010, s. 20)."),
 ("Nor does the lack of a reporting route create a separate legal claim", "Nor, on our reading, does the lack of a reporting route create a separate legal claim",
  "§5 #26", "Kuoni concerns a tour operator; the step to any party that undertook a service is the authors' reading (v8)."),
 ("Design frameworks frequently treat friction-free speed as the primary virtue of automated service",
  "Design frameworks treat smoothness as a central goal of automated service",
  "§4.6", "None of the three cited frameworks treats 'friction-free speed as the primary virtue'; all aim at continuity. v8: 'Smoothness has become a central goal'."),
 ("Batat herself ranks systems built purely for", "Batat ranks systems that create",
  "§4.6", "'Purely' is not in the source (Batat 2026: 13, 16); 'herself' reads as addressed to the editor."),
 ("Preserving trust across a digital crossing requires ensuring", "Preserving trust across a digital crossing, which the phygital literature rightly seeks, requires ensuring",
  "§4.6", "The call asks for continuity and trust across transitions; v8 conceded that the literature rightly seeks them."),
 ("Table 2 organizes these obligations into five sequential stages for hosts", "Table 2 organizes these obligations into five stages for hosts",
  "§4.10", "The stages are not sequential; their order is the authors' (v8's caption)."),
 ("institutional forum that can ask questions and pass judgment (Bovens 2007: 450)", "institutional forum that can ask questions and pass judgement (Bovens 2007: 450)",
  "M", "British 'judgement'."),
 ("Such a forum provides an official venue", "Such a forum, on our account, provides an official venue",
  "§5 (VERIFY_V8_B 18)", "Bovens's forum questions and judges (p. 450); the venue described is the authors' proposal."),
 ("For a small innkeeper, meeting these five stages can be as straightforward", "For a small innkeeper, meeting the first four stages can be as straightforward",
  "§4.10", "Stage 5 needs a forum that can question and judge, and the conclusion requires it to be independent."),
 ("Table 2. Five stages from touchpoint audit to post-stay accountability.", "Table 2. Five stages from touchpoint audit to post-stay accountability (the order is ours).",
  "§4.10", "v8's caption said the order is the authors'."),
 ("A known path to help that does not require a confrontation or depend on staff goodwill", "A known path to help that does not require a confrontation or depend on the host's goodwill",
  "§4.10", "See l. 117."),
 # Conclusion
 ("multiple parties can owe care at once, in proportion to their control.", "multiple parties can owe care at once, according to their degree of control.",
  "§5 #25", "Wheat v E Lacon: 'dependent on his degree of control'."),
 ("Third, during a stay, the guest's standing grounds a further duty", "Third, during a stay, the guest's claim grounds a further duty",
  "§2, §4.1", "Ground of the further duty: 'standing' → 'claim'."),
 ("Phygital systems improve responsiveness and allow small teams to serve far more guests, though experts warn that algorithmic management also intensifies frontline hotel work",
  "Phygital systems can improve responsiveness and allow small teams to serve far more guests, though experts expect algorithmic management also to intensify frontline hotel work",
  "§5 (panel 04)", "The gains carry no source of their own; Jianu et al. is a Delphi forecast, so 'expect', as v8 had it."),
]
T = [t for t in T if t[2] is not None]

# Spelling: US -> British (JOURNAL_SPEC: British English with -ize). Whole words, case kept.
SPELL = [("travelers", "travellers"), ("traveler", "traveller"), ("centered", "centred"), ("center", "centre"),
         ("behavior", "behaviour"), ("labor", "labour"), ("fulfill", "fulfil"), ("percent", "per cent"),
         ("honor", "honour"), ("neighboring", "neighbouring"), ("toward", "towards"), ("afterward", "afterwards")]

HEAD2 = ["INTRODUCTION", "THEORETICAL CONTEXT", "APPROACH", "THE PARTIES TO A PHYGITAL ARRANGEMENT",
         "DURING THE STAY", "AT THE TOUCHPOINT", "CONCLUSION"]
HEAD3 = ["Phygital hospitality", "The host", "The host's duty in law", "The property", "The brand",
         "The platform", "The vendor", "The state"]


def targeted(t):
    for old, new, ref, why in T:
        n = t.count(old)
        if n != 1:
            sys.exit(f"targeted edit matched {n} times: {old[:70]!r}")
        t = t.replace(old, new)
    return t


def quotes(par):
    """Double quotation marks -> single; quotes inside -> double; trailing , or . moved outside."""
    def conv(m):
        inner = m.group(1)
        inner = re.sub(r"(?<![A-Za-z])'([^']+?)'(?![A-Za-z])", r'"\1"', inner)
        tail = ""
        if inner and inner[-1] in ",.":
            inner, tail = inner[:-1], inner[-1]
        return "'" + inner + "'" + tail
    return re.sub(r'"([^"\n]*)"', conv, par)


def spell(t):
    for us, gb in SPELL:
        t = re.sub(rf"\b{us}\b", gb, t)
        t = re.sub(rf"\b{us.capitalize()}\b", gb.capitalize(), t)
    return t


def mechanical(t):
    t = re.sub(r"\s*—\s*", " – ", t)                       # spaced en rule, as the journal prints
    t = t.replace('may be "occupiers"', 'may be \x00occupiers\x01')   # already double inside single
    t = quotes(t)
    t = t.replace('\x00', '"').replace('\x01', '"')
    t = spell(t)
    t = t.replace("s.29(1)", "s. 29(1)").replace("(2022:605)", "(2022: 605)")
    out, lines = [], t.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s == "Abstract":
            out.append("## Abstract")
        elif s.startswith("Keywords:"):
            out.append("**Keywords:**" + s[len("Keywords:"):])
        elif s in HEAD2:
            out.append("## " + s)
        elif s in HEAD3:
            out.append(f"### *{s}*")
        elif s.startswith("Column 1"):
            i += 1
            rows = []
            while i < len(lines) and lines[i].strip():
                rows.append([c.strip() for c in re.split(r"\s{3,}|\t", lines[i].strip())])
                i += 1
            w = len(rows[0])
            out.append("| " + " | ".join(rows[0]) + " |")
            out.append("|" + "---|" * w)
            for r in rows[1:]:
                out.append("| " + " | ".join(r) + " |")
            continue
        elif re.match(r"^Table [12]\. ", s):
            out.append(re.sub(r"^(Table [12]\.)", r"**\1**", s))
        else:
            out.append(ln)
        i += 1
    t = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"


base = prenorm(raw)
v9m = mechanical(base)                 # v9 after the mechanical passes only
v10body = mechanical(targeted(base))   # v9 after targeted and mechanical changes

# A: assembly
head = (V8A / "head_v8.md").read_text(encoding="utf-8")
title = head.split("\n")[0].strip()
tail = (HERE / "tail_v10.md").read_text(encoding="utf-8").strip("\n")   # v8 tail, references re-rendered from cited_keys_v10.txt
fig = (V8A / "figure1.md").read_text(encoding="utf-8").strip("\n")
anchor = "is where a host's duty is either fulfilled or broken (Figure 1)."
assert v10body.count(anchor) == 1
para_end = v10body.index("\n", v10body.index(anchor))
v10body = v10body[:para_end] + "\n\n" + fig + v10body[para_end:]
banner = ("<!--\nDRAFT_v10: the authors' DRAFT_v9 with targeted edits only (v10_2026-11/build_v10.py; every change "
          "listed in v10_2026-11/V10_CHANGES.md and marked in DRAFT_v10_marked.md). The title, Figure 1, the AI "
          "acknowledgment and the reference lists are copied from DRAFT_v8's assembly. Delete this comment before "
          "submission.\n-->\n\n")
(MS / "DRAFT_v10.md").write_text(banner + title + "\n\n" + v10body + "\n" + tail + "\n", encoding="utf-8")

# Marked copy: word-level diff of the body, v9 (mechanical only) against v10.
def tokens(s):
    return re.findall(r"\S+|\n", s)

a, b = tokens(v9m), tokens(mechanical(targeted(base)))
sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
outt = []
def join(ts):
    return " ".join(ts).replace(" \n ", "\n").replace("\n ", "\n").replace(" \n", "\n")
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal":
        outt.append(join(a[i1:i2]))
    else:
        if i2 > i1:
            outt.append("~~" + join(a[i1:i2]) + "~~")
        if j2 > j1:
            outt.append("**[C: " + join(b[j1:j2]) + "]**")
marked = " ".join(outt).replace(" \n", "\n").replace("\n ", "\n")
mbanner = ("<!--\nDRAFT_v10_marked: the body of DRAFT_v10 with every targeted change marked against DRAFT_v9. "
           "~~struck~~ is the authors' v9 wording removed; **[C: …]** is Claude's replacement. Mechanical "
           "house-style changes (quotation marks, British spelling, dashes, spacing, headings, tables) are applied "
           "to both sides and so are not marked; V10_CHANGES.md counts them. Figure 1, the title and the "
           "back matter are not shown here.\n-->\n\n")
(MS / "DRAFT_v10_marked.md").write_text(mbanner + marked + "\n", encoding="utf-8")

# Change table for V10_CHANGES.md
rows = []
v9lines = prenorm((MS / "DRAFT_v9.md").read_text(encoding="utf-8")).split("\n")
for k, (old, new, ref, why) in enumerate(T, 1):
    key = old.split("\n")[0][:40]
    ln = next((n + 1 for n, l in enumerate(v9lines) if key in l), "?")
    rows.append(f"| T{k} | {ln} | {ref} | {old.strip()} | {new.strip() or '(removed)'} | {why} |")
(HERE / "changes_table.md").write_text(  # pasted into V10_CHANGES.md
    
    "| # | v9 line | Synthesis | v9 (before) | v10 (after) | Why, and the source |\n|---|---|---|---|---|---|\n"
    + "\n".join(rows) + "\n", encoding="utf-8")

# Mechanical counts
def count_diff(f):
    return sum(1 for _ in f)
counts = {
    "em-dashes to spaced en rules": base.count("—"),
    "double-quoted spans to single": len(re.findall(r'"[^"\n]*"', targeted(base))),
    "US spellings to British": sum(len(re.findall(rf"\b{us}\b", targeted(base), re.I)) for us, _ in SPELL),
}
print("targeted edits:", len(T), "| mechanical:", counts)
print("wrote DRAFT_v10.md, DRAFT_v10_marked.md, v10_2026-11/changes_table.md")
