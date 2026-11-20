<!-- DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026. The record of every change from DRAFT_v9 (the authors' rewrite) to DRAFT_v10. Built by build_v10.py; the table below is generated from the script's edit list, so it lists exactly what was applied. -->

# DRAFT_v10: what changed from DRAFT_v9, and what did not

Roger asked for the reviewer pack's targeted changes only, applied to his rewrite as v10, with nothing rewritten as a whole. The rule followed:
- every change replaces the fewest words that fix one finding of `reviews/2026-11-13/SYNTHESIS.md`;
- no sentence is rewritten as a whole, and no new sentence or paragraph is added, apart from the assembly items below;
- where a fix needed new argument or new prose, it is listed under 'Not done' for the authors.

**Files**
- `DRAFT_v10.md`: the manuscript.
- `DRAFT_v10_marked.md`: the body with each targeted change marked. `~~struck~~` is v9's wording removed; **[C: …]** is Claude's replacement. Mechanical changes are not marked; they are counted below.
- `v10_2026-11/build_v10.py`: the script that makes both from DRAFT_v9.md. It stops if any edit's old wording does not occur exactly once.

## What was done

**1. Targeted fixes (T1–T94, the table below).** Each row gives the v9 wording, the v10 wording, the synthesis finding and the source. Most changes are a few words; none is a whole sentence of new prose. They fall into five groups:
- **The thesis stated one way** (synthesis §2):
  - 'standing' → 'claim' as the ground of the further duty, in the abstract, introduction and conclusion;
  - v8's sentence that standing does not ground the duty, restored at 'The host' ¶4;
  - 'keeps them' → 'keeps the duty of care' in the abstract.
- **Wrong facts corrected** (synthesis §5): all 31 ledger items. Two only in part: Hemmington's page and *R (DMA)*'s 'section 149' detail each need a source check (see 'Not done', item 16).
- **Hedges restored** where v9 had dropped what v8's source checks had established: 'on our reading', 'seemingly', 'as appropriate and proportionate', 'as Hemmington reports her', 'in the literature we searched' and others.
- **Overstatements narrowed**:
  - 'routinely';
  - 'one rule holds consistently';
  - 'applies to any phygital service';
  - 'in proportion to their control', in five places;
  - three adjectives grading the paper's own argument.
- **Staff and goodwill**: 'staff goodwill' → 'the host's goodwill' in three places; 'organizational rules confer standing' → 'authority'.

**2. Mechanical house style (not marked; JOURNAL_SPEC.md and the journal's printed model):**
- 21 unspaced em-dashes → spaced en rules ( – ), as *Hospitality & Society* prints them (Germann Molz 2018 uses 59 and no em rules);
- 32 double-quoted spans → single quotation marks, with quotations inside them in double marks and closing commas and full stops moved outside;
- 29 US spellings → British with -ize: traveller(s), per cent, centre/centred, behaviour, labour, fulfil, honour, neighbouring, towards, afterwards. 'Organizer' and 'realized' are correct under -ize and stay. 'Judgement' replaces 'judgment' three times outside legal usage (T-rows);
- missing spaces; one contraction;
- curly and straight marks normalized;
- headings and the two tables in markdown;
- the paste artefacts removed ('paper.pdf+ 2'; the 'Column 1 …' rows).

**3. Assembly (copied, not written):**
- **Title line**: v8's.
- **Figure 1** and its caption: v8's figure, placed after 'At the touchpoint' ¶1, where v9 cites it.
- **AI acknowledgment**: v8's text.
- **Reference list, Cases and Legislation**: v8's, less Kropf et al. (2026), which v9 no longer cites; the list now holds 62 entries.

**4. Reference-list repairs** (in the shared `literature/references.bib`, so v8's list would show them too), each verified by the copyeditor panelist (08) against the source or Crossref:
- **Slattery**: the journal title is now *Journal of Hospitality, Leisure, Sport and Tourism Education*.
- **Blackstone**: vol. 3, with `render_refs.py` taught to print a book's volume.
- **Hindriks and Min and Kim**: article numbers 145 and 2.
- **Golubovskaya et al., Hindriks and Kong**: a capital after the colon in the title.

## Checks

| Check | Result |
|---|---|
| Body words, `wordcount.py` | 8,606 (9,000 cap) |
| Abstract | 199 words (100–200) |
| `check_citations.py DRAFT_v10.md cited_keys_v10.txt` | citations OK |
| `preflight.py DRAFT_v10.md` | 19 of 23 |
| `library/build_index.py --check` | OK |

The four preflight failures are known false positives:
- legislation and hand-listed cases the citation resolver cannot parse;
- 'App. 274' in a case reference;
- six double marks, all quotations inside quotations;
- 'advertising', 'likewise' and 'promise', which the checker misreads as -ise endings.

## Not done: these need the authors' writing or decision

Each needs new prose or a choice, so none was attempted. Synthesis references in brackets.

1. **A roadmap** at the end of the introduction, the journal's convention (§4.8).
2. **The scope sentence.** v8 left aside machine agency, guests who cannot report, and hosts in their own homes. It answers R2.5, and restoring it would bring Kropf et al. back into the list (§4.8).
3. **Why hospitality** (R2.4), for example Bulley's 'keep that welcome open', or Pitt-Rivers's turned plate (§4.9).
4. **Who owes the route** under shared control, or when a platform holds itself out, and what binds the vendor to act on forwarded reports (§4.4).
5. **The binding conditions in one place.** The contradictions are removed: 'No single ground', 'one rule recurs', and the abstract's 'reliance'. A sentence or small table saying which condition binds which duty for which party still has to be written (§4.3).
6. **Whether receiving is a core duty.** Two core duties are named, and the property section lists three (§4.2).
7. **Positioning the contribution** against:
   - contestability (Alfrink et al.; Lyons et al.);
   - UN Guiding Principles 29 and 31;
   - Cobbe et al.;
   - seamful design (Chalmers and Galani);
   - TPSR's escalation pathways (Shabnam et al. 2026: 14);
   - Suh et al.'s stakes proposition.

   Credit Sharma and Mattila with the two core duties, and Ariyogi et al. with the sympathy-without-power point (§4.7).
8. **Interruptibility**: a definition, its placement, the timing mismatch (it names a pause before effect; the further duty runs past it), and an audit question that uses it (§4.6).
9. **Table 1.** Each item needs a content decision:
   - row 1's 'Yes' against a route of 'None';
   - the overlap of rows 1 and 2;
   - no low-stakes row;
   - when the stay begins;
   - the 'Authors' analysis' rows;
   - on-site staff against self-check-in rentals (§4.10).
10. **Table 2, stage 3**: what the worker is protected from. Panel 04 proposes penalty for a good-faith override, under Directive 2024/2831 art. 10(2) (§4.10).
11. **Q5**: a time standard. **Q6**: one question or two (§4.10).
12. **The opening case.** Garcia is kept, and lines 11 and 15 are corrected. Whether to open on Xu and Greiffenhagen instead, given that Garcia has no guests and is not a touchpoint, is yours (§4.8).
13. **'Phygital' in the introduction's first four paragraphs** (§4.8).
14. **Unargued or unsourced sentences:**
    - 'a natural person needs to sit at the end of the line' (At the touchpoint ¶3);
    - 'Algorithmic tools can strip away even that leeway' (The property ¶3; Spektor et al. 2023: 628 is held and would source it);
    - 'Walking out during a stay carries substantial financial and practical costs' (During the stay ¶1).
15. **Germann Molz (2026)**: whether 'the next step' survives a full reading. Her abstract already covers robots and AI (§5, VERIFY).
16. **Three source checks still open:**
    - the version-of-record page for the Hemmington quotation (p. 15 is the author version's);
    - whether v8's 'derived from section 149 of the 2010 Act' belongs in the *R (DMA)* sentence;
    - Lord Pearson's attribution in Wheat (R1's VERIFY).
17. **The AI acknowledgment.** It is v8's text, which says Claude drafted the revised article. v10 is your rewrite with Claude's targeted edits, so it must be rewritten to say what happened.
18. **Figure 1.** It is v8's figure; confirm that its labels still match v10.
19. **The front matter and the letters.** The Statement of Contribution, the Highlights and the response letters still match v8, not v10.
20. **Reference-list items left:**
    - headline capitals for book titles;
    - the encyclopedia editions and 'Accessed' dates;
    - Baum and Laux's editors;
    - the 'Accessed' dates on the United Nations and OSTP entries.
21. **Pierre's sentences.** v9 paraphrased all of them, and v10 restores none.

## The targeted changes

| # | v9 line | Synthesis | v9 (before) | v10 (after) | Why, and the source |
|---|---|---|---|---|---|
| T1 | 5 | §4.11 | guests often cannot reach anyone | guests cannot always reach anyone | The abstract claimed guests 'often' cannot reach anyone; the conclusion says this is still to be measured. |
| T2 | 5 | §2, §4.2, §4.11 | when it invites travelers in, earns their trust, and controls the physical space, and it keeps them even when | when it invites travelers in, earns their reliance, and controls the physical space, and it keeps the duty of care even when | 'Trust' → 'reliance', the term the body uses; 'keeps them' (both duties) → 'keeps the duty of care', as the introduction and conclusion state and the body supports (liability for contractors' work 'narrows'). |
| T3 | 5 | §2, §4.1, §4.11 | During a stay, the guest's standing also requires a timely route to reach someone who can correct a failure on the spot. | During a stay, the guest's claim also requires a timely route to reach someone who can correct a failure. | Ground of the further duty: 'standing' → 'claim', as 'During the stay' derives it; 'on the spot' dropped, since the body asks only for correction during the stay. |
| T4 | 5 | §4.11, §4.13 | outlines five steps for host accountability | outlines five stages from audit to accountability | Table 2 has five 'stages', and only the last is accountability. |
| T5 | 11 | §5 #28 | Hotel managers kept the final say over rates, logging in each day to compare | Hotel managers kept the final say over rates and could log in each day to compare | Garcia et al.: the manager decides each day whether to log in ('If she logs into the system …'); v8 had 'could log in'. |
| T6 | 11 | §4.8 | Knowing that managers rarely intervened, the vendor designed the pricing engine to exaggerate rate shifts | Because managers rarely intervened, the vendor had an incentive to design the pricing engine to exaggerate rate shifts | The source states an incentive ('The algorithm's designer has an incentive to offer recommendations that exaggerate the change'), not the vendor's knowledge or design. |
| T7 | 13 | §5 #16 | Here, digital media adds delight | Here, on our reading, digital media adds delight | Staff discretion is not in Batat (2021); v8 marked this as the authors' reading. |
| T8 | 15 | §5 #16 | remain within reach and can adjust the experience on the spot. | remain within reach. | 'Can adjust the experience on the spot' is not in Batat (2021). |
| T9 | 15 | §4.8 | At resort hotels, pricing authority shifts to a software model | At resort hotels, authority over the pricing rule shifts to a software model | 'Pricing authority shifts' contradicted 'kept the final say' two paragraphs earlier; the vendor holds the rule, the managers the price (as 'The vendor' says). |
| T10 | 19 | §4.9 | though the framework applies to any phygital service where | though the framework may extend to other phygital services where | 'Applies to any phygital service' is not shown; the argument rests on lodging (and Groh's holding is confined to hotels). |
| T11 | 19 | §5 #25 | several parties may owe care simultaneously in proportion to their control. | several parties may owe care simultaneously according to their degree of control. | Wheat v E Lacon: 'dependent on his degree of control', not proportion. |
| T12 | 19 | §2, §4.1 | Third, the guest's standing during a stay grounds a further duty | Third, the guest's claim during a stay grounds a further duty | Ground of the further duty: 'standing' → 'claim' (see l. 41 and 'During the stay'). |
| T13 | 31 | §5 #3 | describe this movement as "fluidity" (Batat | describe this movement as fluidity (Batat | Neither source uses the noun in quotation: Batat 2024: 1220 has 'fluidifying', Batat and Hammedi 2023: 17 'fluid'. |
| T14 | 31 | M | who retains room for judgment, at each handoff | who retains room for judgement, at each handoff | British 'judgement' outside legal usage. |
| T15 | 31 | §4.13 | in which another party owes you enforceable care | in which another party owes the guest enforceable care | Second-person address (Reviewer 3, round one). |
| T16 | 35 | §5 #18 | Elizabeth Telfer similarly treats guest safety as the host's primary obligation | Elizabeth Telfer, as Hemmington reports her, similarly treats guest safety as traditionally the host's primary obligation | Telfer is read through Hemmington, who reports her as saying 'traditionally the most important responsibility of all was the guest's safety'. |
| T17 | 35 | §5 (panel 01 F3) | Read together, these accounts show that admitting | We read these accounts together as showing that admitting | The synthesis is the authors' reading, not something the sources show; v8's form. |
| T18 | 37 | §5 #17 | Some scholars doubt whether paid lodging qualifies as hospitality at all, since commercial access ends the moment payment stops (Lashley 2015: 5), leading Slattery to argue that | Some scholars doubt whether a host who charges can be hospitable at all, since commercial access ends the moment payment stops (Lashley 2015: 5), and Slattery argues that | Lashley (p. 5) doubts the hospitableness of commercial hosting, not whether paid lodging is hospitality; a 2002 article cannot follow from a 2015 one. |
| T19 | 37 | §5 #19 | Service research has largely treated the frontline employee as the host | Service research has, on our reading, largely treated the frontline employee as the host | 'Host' never occurs in Odekerken-Schröder et al.; v8 marked this as the authors' reading. |
| T20 | 41 | §4.7 | contestability refers to a technical mechanism | contestability, as design work mostly uses it, refers to a technical mechanism | Unhedged, the definition makes contestability lose; Alfrink et al. and Lyons et al. already require a human with power to change the decision. v8's hedge. |
| T21 | 41 | §2, §4.1 | examined below, while standing names the position | examined below; standing does not ground it but names the position | Restores v8's statement that standing does not ground the duty, which closes Reviewer 2's circularity. |
| T22 | 43 | §5 #29 | When undercooked burgers from a cooking robot sicken diners, Sharma and Mattila ask | When, in their hypothetical case, undercooked burgers from a cooking robot sicken diners, Sharma and Mattila ask | The burger case is hypothetical, not an event. |
| T23 | 43 | §5 #29 | leaving the question to corporate risk management (2026: 904) | leaving the question to governance and risk management (2026: 904) | Sharma and Mattila: 'governance and risk-management for the industry'. |
| T24 | 47 | §5 #2 | "hangs out a sign and opens his house for travelers" | "hangs out a sign and opens his house for travellers" | The source spells 'travellers'; the quotation had been Americanized. |
| T25 | 49 | §5 #1 | modern English negligence law applies this directly, holding that a hotel that "guests to come and stay" | a modern English court applies this directly, holding that a hotel that "invited guests to come and stay" | The quotation had lost 'invited' (Al-Najar 2019: para 187); one High Court judgment is 'a modern English court', as v8 had it. |
| T26 | 49 | §4.3 | None of these three elements suffices on its own. | No single ground suffices on its own. | The sentence named 'these three elements' and then argued it for a different three (undertaking, reliance, vulnerability). |
| T27 | 49 | §5 #27 | (Jeske 2021: §§3–4; Habib | (Jeske 2021: §§3–4, 7; Habib | Jeske's reliance clause is at §7. |
| T28 | 51 | §5 #25 | occupiers continue to owe care in proportion to their control over the premises | occupiers continue to owe care according to their degree of control over the premises | Wheat v E Lacon: 'dependent on his degree of control'. |
| T29 | 51 | §4.2 | Statute still assigns an innkeeper's core duties to "the proprietor" alone | Statute still assigns an innkeeper's duties to "the proprietor" alone | The 1956 Act does not carry the guest-safety duty, which comes from modern negligence (Al-Najar paras 183, 187); 'core' tied the statute to the two core duties. |
| T30 | 53 | §4.13 | and it gives us a clear test for assigning duties | and it gives us a test for assigning duties | Sentence grading the paper's own argument. |
| T31 | 57 | §4.7 | we found the problem widely noted but never derived from the host role itself | we found the problem widely noted but, in the literature we searched, never derived from the host role itself | An absence claim needs its search scope; v8's hedge. |
| T32 | 59 | §4.13 | Our claims also carry clear evidentiary and legal bounds. | Our claims also carry evidentiary and legal bounds. | Sentence grading the paper's own argument. |
| T33 | 59 | §4 (finding 7 of the brief) | Outside European package-travel law, platform-moderation rules, and disability-accommodation mandates, the further duty | Outside European package-travel law, platform-moderation rules, disability-accommodation mandates, and the rules on solely automated decisions, the further duty | The three lists of exceptions disagreed; this one now matches 'At the touchpoint' (l. 158). |
| T34 | 65 | §4.3 | These arrangements fail because the link between | These arrangements fail when the link between | Not every phygital arrangement fails; the sentence states the condition. |
| T35 | 69 | §5 #21 | the traditional innkeeper took custody of a stranger's person and belongings | the traditional innkeeper received a stranger's person and belongings | Sandoval-Strausz does not say custody of the person; v8's verb. |
| T36 | 69 | §5 #6 | public service providers are also barred from refusing service on any protected ground (Equality Act 2010, s.29(1)) | providers of a service to the public are also barred from refusing service on any protected ground (Equality Act 2010, s. 29(1)) | Section 29(1) binds 'A person … concerned with the provision of a service to the public', not public-sector providers only. |
| T37 | 69 | §5 #30 | and a guest who receives substandard service can demand repeat performance | and a consumer guest who receives substandard service can demand repeat performance | The Consumer Rights Act right belongs to consumers (s. 2(3)), not business travellers. |
| T38 | 71 | M | (Ferguson v Welsh1987: 7) | (Ferguson v Welsh 1987: 7) | Missing space. |
| T39 | 71 | M | (Naylor v Payling 2004: paras 19, 50; Maguire v Sefton 2006:para 30) | (Naylor v Payling 2004: paras 19, 50; Maguire v Sefton 2006: para 30) | Missing space. |
| T40 | 71 | §5 #7 | and no English judgment we examined imposes one on a hotel toward an adult guest. | and since the 1957 Act, absent contrary terms, a hotel's contract with its guest implies only the common duty of care (Maguire v Sefton 2006: paras 21–24). | MacLenan v Segar [1917] 2 KB 325 implied an innkeeper's warranty that premises are as safe as care 'on the part of anyone' can make them; Maguire (paras 21–24) holds that the 1957 Act replaced such terms with the common duty of care. The absolute claim was false as written. |
| T41 | 73 | §5 #14 | Yet, they hesitated to exceed 10 to 20 percent of the room rate because management had never defined the limits of their authority | Yet, they hesitated to exceed 10 to 20 percent of the room rate and did not know where their authority ended | Schumacher and Komppula give the two facts side by side ('Even though', p. 122), not as cause and effect; v8's wording. |
| T42 | 73 | §5 #15 | reservation agents often hold formal latitude to override prices suggested by revenue-management software. However, Bendoly (2013) shows that whether they exercise that discretion depends on their own judgment | reservation agents often hold formal latitude to accept rates below those suggested by revenue-management software. However, Bendoly (2013) notes that whether they exercise that discretion depends largely on their own judgement | Bendoly's abstract (abstract only): agents are 'often given the latitude' to accept rate bids below the system's price, and deviation depends 'in large part' on their judgement; these are premises, so 'notes', not 'shows'. |
| T43 | 73 | §5 (panel 04) | Algorithmic tools can strip away even that informal leeway | Algorithmic tools can strip away even that leeway | The latitude was called 'formal' one sentence earlier. |
| T44 | 75 | §5 #25 | multiple parties can share that duty in proportion to their control. | multiple parties can share that duty according to their degree of control. | Wheat v E Lacon: 'dependent on his degree of control'. |
| T45 | 79 | M | (2026:78–79) | (2026: 78–79) | Missing space. |
| T46 | 79 | §5 #11 | vicariously liable under apparent agency because the company exercised a 'significant degree of control over the operation' | vicariously liable under apparent agency because the company held the motel out as its own and kept a 'significant degree of control over the operation' | Crinkley's apparent agency rests on holding out and reliance (paras 49–52); the court also found the franchisor 'retained a significant degree of control' (para 51). |
| T47 | 89 | §4.12 | paper.pdf+ 2 | (removed) | Paste artefact removed. |
| T48 | 91 | §5 #23 | Bosma's fieldwork reveals that a single listing | Bosma reports that a single listing | The three host roles are Airbnb's categories, not findings of her fieldwork. |
| T49 | 91 | §5 #23 | while automated smart locks replace any in-person key handover (2022:605) | while self-check-in can replace the in-person key handover (2022: 605) | Her host Elli still hands over keys (p. 602), so not 'any'; v8: 'self-check-in replaces the handover of keys'. |
| T50 | 97 | §4.13 (terms) | and authority is the power to rewrite the underlying rule or answer for its design. | and authority is the power to rewrite the underlying rule. | 'Or answer for its design' folded accountability into authority, which 'The host' keeps apart. |
| T51 | 97 | §5 #24 | In the European hotel study, the vendor held authority | In the hotel pricing study, the vendor held authority | Only the vendor is based in Europe; the study does not locate the hotels. |
| T52 | 97 | §4.8 | a guest can easily reach a staff member who lacks discretion to override a software output, while never reaching the vendor who controls the rule. | a guest can easily reach a staff member with discretion over a single output, while never reaching the vendor who controls the rule. | The paragraph had just said the managers kept discretion; the split is discretion (case) against authority (rule). |
| T53 | 99 | §5 #8, §4.2 | each firm answers only for its own conduct, because a loose supply chain does not constitute a single moral or legal agent (Kong 2026: 9; Pettit 2007: 195). | no single firm answers for the whole, because a loose supply chain does not constitute a single moral agent (Pettit 2007: 195). | Kong argues the opposite (delegation 'does not diminish principal responsibility'), and 'each firm answers only for its own conduct' contradicted the package-travel rule (l. 51); 'or legal' is not in Pettit. |
| T54 | 107 | §5 #10 | rather than a freestanding obligation to monitor every daily interaction (RR v Enfield 2025: paras 80–81) | rather than a freestanding obligation to monitor (RR v Enfield 2025: paras 80–81) | 'Every daily interaction' is not in the judgment; v8: 'not a free-standing duty to monitor'. |
| T55 | 109 | §4.3, §5 #25 | one rule holds consistently: physical control over the guest's space anchors the duty of care, and multiple organizations can share that duty in proportion to their control. | one rule recurs: physical control over the guest's space anchors the duty of care, and multiple organizations can share that duty according to their degree of control. | The brand, the platform, package travel and the state bind without control, so the rule recurs rather than 'holds consistently'; Wheat's 'degree of control'. |
| T56 | 109 | §4 (finding 7 of the brief) | neither the law of delegation nor moral philosophy obliges a delegator | neither the law of delegation nor its moral philosophy obliges a delegator | The claim rests on Brandt; the next section derives such a duty from moral philosophy itself. v8: 'its moral philosophy'. |
| T57 | 113 | §5 #16 | and an animated projection fills a single wait before dinner. | and an animated projection accompanies a single meal. | Le Petit Chef runs through the meal (Batat 2021: 4), not one wait before it. |
| T58 | 113 | §5 #20 | kept quiet about poor conditions because she could not afford to leave (2023) | kept quiet because she could not leave (2023) | The source has neither 'poor conditions' nor 'afford'. |
| T59 | 113 | §5 (panel 08) | neither host nor guest can assert absolute sovereignty | neither host nor guest can assert sovereignty | 'Absolute' is not Bulley's. |
| T60 | 113 | §5 #20 | one of the guest's primary forms of power (Moysidou and Stanley 2023) | one of the guest's forms of power (Moysidou and Stanley 2023) | The source speaks of 'latent forms of power', not primary ones. |
| T61 | 115 | §5 #13 | As Herstein explains in summarizing Joseph Raz's theory of rights, a single claim-right can justify new and shifting duties | As Herstein reports in summarizing Joseph Raz's theory of rights, a single claim-right can seemingly justify new and shifting duties | Herstein: a claim-right 'seemingly can count in favor of different and changing duties' (§8.4), a view he reports. |
| T62 | 115 | §4.1 | Under the principle of instrumental normativity, an obligation to achieve an end extends to the means necessary to achieve it | Under the principle of instrumental normativity, an 'ought' to achieve an end extends to the means necessary to achieve it | Kiesewetter's principle concerns the transmission of an 'ought' to necessary means, not obligation as such. |
| T63 | 117 | §4.10 | as a matter of right rather than depending on staff goodwill. | as a matter of right rather than depending on the host's goodwill. | v9 moved the dependence from the host to the staff in three places, which loads the clerk; v8's 'the host's goodwill'. |
| T64 | 119 | §5 #26 | which rests partly on general risk to others and is not owed to a specific claimant (2025: 4–5) | which rests partly on general risk to others and which he does not say is owed to anyone (2025: 4–5) | Hindriks does not say the duty is owed to anyone; v8's wording. |
| T65 | 121 | §5 #9 | European and British statutes routinely prioritize live repair over post-hoc payment, requiring package-travel organizers to remedy defects during a trip, service providers to repeat substandard work, and digital platforms to rectify automated worker decisions, turning to compensation only when rectification is impossible | Several European and British statutes prioritize live repair over post-hoc payment, requiring package-travel organizers to remedy defects during a trip, service providers to repeat substandard work, and digital platforms to rectify automated worker decisions or, where that is impossible, to compensate | Three instruments, not 'routinely'; the compensation-only-if-impossible rule is the platform-work directive's alone (art. 11(3)); the Consumer Rights Act (s. 56(3)(b)) and the package-travel directive (arts 13(3)(b), 14(1)) give price reduction and compensation alongside. |
| T66 | 134 | §5 #22 | This temporal boundary also clarifies why studies showing high guest acceptance of hotel automation require careful interpretation. Guests may care little whether a human clerk or a lobby robot gives them directions, because the stakes of that exchange are low (Schmidt et al. 2025). | This temporal boundary also clarifies why studies of guest acceptance of hotel automation require careful interpretation. Guests may care little whether a human clerk or a lobby robot gives them directions (Schmidt et al. 2025), on our reading because the stakes of that exchange are low. | Schmidt et al. found indifference between robot and human, not 'high acceptance'; the stakes explanation is the authors' gloss. |
| T67 | 134 | §4 (brief finding 10) | Friction is valuable only because it creates a pause | On this reading, friction is valuable because it creates a pause | 'Only because' contradicted the Le Petit Chef case; v8 marked this as a reading. |
| T68 | 138 | §4.8 | A facial-recognition kiosk in a lobby, a numeric keypad on a rental door, or a pricing screen at a manager's desk bridges | A facial-recognition kiosk in a lobby or a numeric keypad on a rental door bridges | A manager's pricing screen is not a touchpoint by the paper's own definition (a moment where the guest interacts with the arrangement). |
| T69 | 142 | M | That reporting route doesn't always have to end with a human. | That reporting route does not always have to end with a human. | Contraction. |
| T70 | 142 | §5 #5 | most facial-recognition errors cleared up when guests stepped back and tried again | every facial-recognition error cleared up when guests stepped back and tried again | All 610 guests who reached the face scan were recognized (Xu and Greiffenhagen 2024: Figure 11, p. 5027). |
| T71 | 142 | §5 #5 | When retrying fails, however, repair requires the authority to override the software's output, as when a clerk manually checked in the thirteen guests whom the kiosk rejected (5035). | When retrying cannot help, however, repair requires the authority to override the software's output, as when a clerk manually checked in the thirteen guests whom the kiosk could not process (5035). | The thirteen were not recognition failures or rejections: the kiosk was off, an ID was unreadable, reservations were not found, a process froze (p. 5035, n. 4). |
| T72 | 142 | §5 #12 | must allow human overseers to "disregard, override or reverse the output," | must allow human overseers, as appropriate and proportionate, to "disregard, override or reverse the output," | Art. 14(4) applies 'as appropriate and proportionate'; v8 carried it. |
| T73 | 142 | §4.10 | Whoever holds that override power must also exercise it with reasonable care. | The host must also ensure that whoever holds that override power exercises it with reasonable care. | In Groh the duty is the hotel's, not the guard's (¶¶ 4, 23). |
| T74 | 142 | §5 #31 | and the guard evicted them into the cold anyway | and the guards evicted them anyway | The court lists the weather as a factor but the facts cited do not say it was cold; guards (plural) escorted the group out. |
| T75 | 144 | §4.1 | Training builds competence, whereas organizational rules confer standing. | Training builds competence, whereas organizational rules confer authority. | Standing is the guest's; for staff the word is authority (and conferred standing would undercut the ground of the duty). |
| T76 | 144 | M | as the UN Guiding Principles observe, analyzing complaint patterns | as the UN Guiding Principles observe, analysing complaint patterns | British spelling. |
| T77 | 149 | §4.10 | can the guest use it without relying on staff goodwill or incurring an unfair penalty? | can the guest use it without relying on the host's goodwill or incurring an unfair penalty? | See l. 117. |
| T78 | 156 | §4.13 | Applying these questions pinpoints exactly where a touchpoint breaks down. | Applying these questions shows where a touchpoint breaks down. | Sentence grading the paper's own argument. |
| T79 | 156 | §5 #4, #5 | the escalation path ended with a clerk authorized to override the kiosk, yet rejected guests had to find that worker themselves; the arrangement passes the third question while failing the second (Xu and Greiffenhagen 2024: 5021, 5035). | the escalation path ended with a clerk able to check guests in by hand, yet guests the kiosk could not process had to find that worker themselves; the arrangement passes the third question while failing the second (Xu and Greiffenhagen 2024: 5035). | The study says the worker 'manually checked them in', not that the worker was authorized to override; p. 5021 records the worker approaching guests, so only p. 5035 supports the sentence. |
| T80 | 156 | §3.3 | Yet the plaintiffs alleged those guards lacked training | Yet Groh alleged those guards lacked training | One plaintiff: 'Groh alleges …' (¶ 13). |
| T81 | 158 | §5 | In Great Britain, disability law may entitle a guest to human assistance | In Great Britain, disability law may entitle a disabled guest to human assistance | Reasonable adjustments are owed to disabled persons (Equality Act 2010, s. 20). |
| T82 | 158 | §5 #26 | Nor does the lack of a reporting route create a separate legal claim | Nor, on our reading, does the lack of a reporting route create a separate legal claim | Kuoni concerns a tour operator; the step to any party that undertook a service is the authors' reading (v8). |
| T83 | 160 | §4.6 | Design frameworks frequently treat friction-free speed as the primary virtue of automated service | Design frameworks treat smoothness as a central goal of automated service | None of the three cited frameworks treats 'friction-free speed as the primary virtue'; all aim at continuity. v8: 'Smoothness has become a central goal'. |
| T84 | 160 | §4.6 | Batat herself ranks systems built purely for | Batat ranks systems that create | 'Purely' is not in the source (Batat 2026: 13, 16); 'herself' reads as addressed to the editor. |
| T85 | 160 | §4.6 | Preserving trust across a digital crossing requires ensuring | Preserving trust across a digital crossing, which the phygital literature rightly seeks, requires ensuring | The call asks for continuity and trust across transitions; v8 conceded that the literature rightly seeks them. |
| T86 | 162 | §4.10 | Table 2 organizes these obligations into five sequential stages for hosts | Table 2 organizes these obligations into five stages for hosts | The stages are not sequential; their order is the authors' (v8's caption). |
| T87 | 162 | M | institutional forum that can ask questions and pass judgment (Bovens 2007: 450) | institutional forum that can ask questions and pass judgement (Bovens 2007: 450) | British 'judgement'. |
| T88 | 162 | §5 (VERIFY_V8_B 18) | Such a forum provides an official venue | Such a forum, on our account, provides an official venue | Bovens's forum questions and judges (p. 450); the venue described is the authors' proposal. |
| T89 | 162 | §4.10 | For a small innkeeper, meeting these five stages can be as straightforward | For a small innkeeper, meeting the first four stages can be as straightforward | Stage 5 needs a forum that can question and judge, and the conclusion requires it to be independent. |
| T90 | 164 | §4.10 | Table 2. Five stages from touchpoint audit to post-stay accountability. | Table 2. Five stages from touchpoint audit to post-stay accountability (the order is ours). | v8's caption said the order is the authors'. |
| T91 | 169 | §4.10 | A known path to help that does not require a confrontation or depend on staff goodwill | A known path to help that does not require a confrontation or depend on the host's goodwill | See l. 117. |
| T92 | 177 | §5 #25 | multiple parties can owe care at once, in proportion to their control. | multiple parties can owe care at once, according to their degree of control. | Wheat v E Lacon: 'dependent on his degree of control'. |
| T93 | 177 | §2, §4.1 | Third, during a stay, the guest's standing grounds a further duty | Third, during a stay, the guest's claim grounds a further duty | Ground of the further duty: 'standing' → 'claim'. |
| T94 | 179 | §5 (panel 04) | Phygital systems improve responsiveness and allow small teams to serve far more guests, though experts warn that algorithmic management also intensifies frontline hotel work | Phygital systems can improve responsiveness and allow small teams to serve far more guests, though experts expect algorithmic management also to intensify frontline hotel work | The gains carry no source of their own; Jianu et al. is a Delphi forecast, so 'expect', as v8 had it. |
