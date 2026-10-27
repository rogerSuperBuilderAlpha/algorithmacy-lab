# Review of the full draft received 2026-10-13 ("new version")

*Written by Claude on 2026-10-13 at the author's request ("i need a full review"). One reader, one pass.
Every factual check below was made against a source record this project holds: the verified card
library (`literature/library/`), the audits (`literature/audit/`), the merged bibliography
(`literature/references.bib`, where each DOI was resolved at Crossref), and the journal pages opened on
2026-10-13 (`venue/HCI_STRUCTURE.md`). Where the project holds no record, the item is marked "not
checked". Nothing in the draft was changed.*

## Verdict

The architecture is right for *Human–Computer Interaction* and the argument is stronger than the last
version. The draft cannot be submitted as it stands, for one reason above all: **the reference list is
unreliable**. At least 39 of about 105 entries do not match the published record, and seven statements
in the text reverse or misstate what their sources found. A reviewer who checks three references will
find one that does not exist as cited.

## 1. What works

- The introduction is continuous prose, states its contribution outright, and runs in the order the
  journal's recent papers use.
- Section 2 now reviews HCI's own transparency literature and answers Özçetin et al. (2023) directly.
  That reply (2.2, last paragraph) is the best passage in the draft.
- The four-target taxonomy of disclosure (4.1) resolves the tension the research kept raising: a stated
  property of a rule (Target 3) is a different thing from a rulebook (Target 4).
- Convention B is restated as "valid and noise-filtered first, plain second, and low-latency third".
- The unilateral-modification test (7.1) gives section 7 an argument of its own.
- Section 8 is a research agenda with a discrete-time control arm, and 9.2 says which claims are the
  paper's own.
- Each convention ends in a "Design opening", the form the journal's own papers use.

## 2. The reference list

### 2a. Entries that do not match the record (39)

| Entry in the draft | What the record shows |
| --- | --- |
| Hutchins (1995), *Cognition in the Wild* | The quotations at p. 282 are from "How a cockpit remembers its speeds", *Cognitive Science* 19(3), 265–288 |
| Jhaver, Bruckman, & Gilbert (2019), "Does transparency in moderation improve behavior?" | The finding cited is from Jhaver, Appling, Gilbert, & Bruckman (2019), "'Did you suspect the post would be removed?'", *PACM HCI* 3(CSCW), Article 192 |
| Rayner, Fischer, & Pollatsek (1998), "Punctuation and space between words", *Perception & Psychophysics* | "Unspaced text interferes with both word identification and eye movement control", *Vision Research* 38(8), 1129–1144 |
| Vaccaro et al. (2024), "Explanations do not improve…", pp. 1102–1118 | "When combinations of humans and AI are useful: A systematic review and meta-analysis", *Nature Human Behaviour* 8, 2293–2303 |
| Schemmer, Hemmer, Kühl, Benz, & Satzger (2022), *PACM HCI* | Schemmer, Hemmer, Nitsche, Kühl, & Vössing, "A meta-analysis of the utility of explainable artificial intelligence in human-AI decision-making", AIES 2022, 617–626 |
| Gonczarowski et al. (2024), "Menu representations…", *AER* 114(6) | "Describing deferred acceptance and strategyproofness to participants: Experimental analysis"; held as a working paper |
| Masuda, Okano, & Stern (2022), *Games and Economic Behavior* | Masuda, Mikami, Sakai, Serizawa, & Wakayama, "The net effect of advice on strategy-proof mechanisms: an experiment for the Vickrey auction", *Experimental Economics* 25, 902–941 |
| Larson, List, & Metcalfe (2016), *Journal of Finance* 71(5) | "Can myopic loss aversion explain the equity premium puzzle? Evidence from a natural field experiment with professional traders"; an NBER working paper |
| Rahmandad & Gary (2023), "Why human learning fails…", 34(1), 12–35 | "Delays impair learning and can drive convergence to inefficient strategies", *Organization Science* 34(6), 2392–2414 |
| Rahman (2019), *The Invisible Leash* | *Invisible Cages: Algorithmic Evaluations in Online Labor Markets* (Stanford dissertation) |
| Cameron & Rahman (2022), *Academy of Management Annals* 16(1) | *Organization Science* 33, 38–58; the subtitle is "…the co-constitution of control and resistance in the gig economy" |
| Ghalme, Nair, Eilat, Ingel, & Rosenfeld (2021) | Fourth author is Talgam-Cohen |
| Bechavod, Ligett, Wu, & Ziani (2022), "Information design for strategic classification", NeurIPS | Bechavod, Podimata, Wu, & Ziani, "Information discrepancy in strategic learning"; held as an arXiv preprint |
| Engel & Malone (2018), "…metric of collective intelligence", *Cognitive Science* | "Integrated information as a metric for group interaction", *PLOS ONE* 13, e0205335 |
| Barrett, Mediano, Rosas, & Seth (2026), *Neural Computation* | Barrett, Milinkovic, Mediano, Rosas, Bor, & Barnett, "Integrated information theory: the good, the bad and the misunderstood"; a preprint |
| Casella et al. (2024), "Mediated bargaining", *JET* 215 | "On the fragility of mediation: Theory and experimental evidence", *JEEA* 24, 801–850 (2026); read as a 2024 working paper |
| Charness, Samek, & van de Ven (2022), "The design of laboratory experiments…", 1–29 | "What is considered deception in experimental economics?", *Experimental Economics* 25, 385–412 |
| Matsuo, Tanaka, & Yamada (2026), *Human–Computer Interaction* | Matsuo, Liu, Hiraoka, & Wada, "An educational human machine interface providing request-to-intervene trigger and reason explanation…", *IEEE Transactions on Human-Machine Systems* 56(3), 650–661 |
| Crabtree (2025), "Human-computer interaction as a design science" | "H is for human and how (not) to evaluate qualitative research in HCI"; posted online, no volume in Crossref |
| Disley & Khan (2026), 41(2), 112–148 | Posted online September 2026 as pp. 1–42 with no volume; co-authors not checked |
| Dix (2024), 39(3), 205–244 | 41(2), 126–153 |
| Özçetin et al. (2023), 38(5–6), 389–422 | 40(1–4), 171–194 |
| Suzor (2018), *Lawless* | The quotation is from "Digital constitutionalism: Using the rule of law to evaluate the legitimacy of governance by platforms", *Social Media + Society* 4(3) |
| Nadella (2026), "Governing frontier models as insider risks… Microsoft Executive Research Whitepaper" | "Models as insider risks in the super intelligence era", a post on X and on his blog, 10 October 2026. No whitepaper |
| Oberschelp (1995), "Algorithmacy: Der Stiefbruder der Literacy…", *Informatik Spektrum* | "Developing analytical competency through informatics teaching", in Watson & Tinsley (Eds.), *Integrating Information Technology into Education*, pp. 115–126; the word is on p. 121 |
| Westwell (2018), *Early Medieval Europe* 26(3) | *The Dissemination and Reception of the Ordines Romani in the Carolingian Church, c. 750–900* (Cambridge dissertation) |
| Chantavarin & Leung (2025), *Journal of Memory and Language* | "The effects of interword spacing and morphological complexity in reading Thai: An eye-tracking study", *Language and Cognition* 17 |
| Winskel et al. (2009), *Vision Research* 49(24) | "Eye movements when reading spaced and unspaced Thai and English…", *Journal of Memory and Language* 61(3), 339–351 |
| Cabrera et al. (2023), "…with behavioral feedback", *TOCHI* | "Improving human-AI collaboration with descriptions of AI behavior", *PACM HCI* 7(CSCW1) |
| Alfrink et al. (2023), *TOCHI* 30(4) | *Minds and Machines* 33, 613–639 |
| Vasconcelos et al. (2023), "Generation mutualism…", CHI | "Explanations can reduce overreliance on AI systems during decision-making", *PACM HCI* 7(CSCW1), Article 129; last author Krishna |
| Douek (2024), "The limits of platform constitutionalism", *Harvard Law Review* | "The Meta Oversight Board and the empty promise of legitimacy", *Harvard Journal of Law & Technology* 37(2), 373–445 |
| Brehmer & Nählinder (2004), *Human Factors* 46(1) | "Achieving what cannot be done: Coping with the time constants in a dynamic decision task", conference proceedings |
| Bar-Gill et al. (2024), "Algorithmic recommendations and merchant performance" | "Helping small businesses become more data-driven: A field experiment on eBay", *Management Science* 70, 7345–7372 |
| Rees-Jones & Skowronek (2018), *JET* 178 | "An experimental investigation of preference misrepresentation in the residency match", *PNAS* 115, 11471–11476 |
| Ashlagi & Gonczarowski (2018), 564–602 | "Stable matching mechanisms are not obviously strategy-proof", *JET* 177, 405–425 |
| Heilmann, M. (2020), *Classical Philology* 115(2) | Heilmann, J., "Reading early New Testament manuscripts: scriptio continua, 'reading aids', and other characteristic features", in *Material Aspects of Reading in Ancient and Medieval Cultures*, pp. 177–196 |
| Nouwens, Liccardi, Veale, Karger, & Mackay (2020) | Fifth author is Kagal |
| Arteaga, Kapor, & Neilson (2022) | Fourth author Zimmerman; "…in centralized school choice" |

### 2b. Not checked

The project holds no record for these, so they are unverified: Bansal et al. (2021), Ehsan et al.
(2021), Kosmyna et al. (2025), Körber (2019), Wischnewski et al. (2023), Wolfe (2021), Mozannar et al.
(2024), Casner et al. (2014), Metzger & Parasuraman (2001), Herlocker et al. (2000), Lee & Moray (1994),
Eisenstein (1969), Thorgeirsson et al. (2026), Terveen & McDonald (2005), and the two entries dated
**2027** (Pucci, Piro, & Matera; Sáenz & De Russis). Given the rate in 2a, each needs checking against
Crossref before it stays. The 2027 dates are in the future.

### 2c. Cited in the text with no entry in the list

Knijnenburg et al. (2012); Simkute et al. (2024); Lee et al. (2025); Horvath et al. (2022); Sheridan &
Verplank (1978); Ishowo-Oloko et al. (2019); Lyons et al. (2021); Kluger & DeNisi (1998); Mertens et al.
(2022); Street (2003); Scribner & Cole (1981); FCA (2014); FSB (2014); NYDFS (2015); Oversight Board
(2022); CERT (2022); RFC 8890; the EU regulations and directive other than 2024/2831; the two cases and
the statutes.

### 2d. In the list and never cited

Arteaga et al.; Ashlagi & Gonczarowski; Balkin; Bar-Gill et al.; Bechavod et al.; Brehmer & Nählinder;
Crabtree; Dietvorst et al.; Dix; Douek; Hardt et al.; Lee & Moray; Rees-Jones & Skowronek; Scaife &
Rogers; Thorgeirsson et al.; Vicente & Rasmussen; Wickens & Carswell.

## 3. Statements that reverse or misstate their sources

| # | Where | The draft says | The source says |
| --- | --- | --- | --- |
| 1 | 4.2 | When communities "posted detailed explanations for moderation removals, sanctioned participants reported lower perceived procedural fairness than when removals were unexplained" | The reverse. Users who received an explanation judged the removal fairer (β = .384). Users who had *read the rules* judged it less fair (β = −.314). Survey, not an experiment (Jhaver et al., 2019, Table 5). The introduction has it right |
| 2 | 3.3 | For experienced readers of Chinese, inserting spaces "slows fixation rates and disrupts comprehension (Bai et al., 2008)" | Bai et al. found no difference between word-spaced and normal text (5,239 against 5,221 ms). Character spacing was slower |
| 3 | 3.3 | "For children or non-native learners… spaces provide a helpful scaffold" | Child learners of Chinese read spaced text more slowly and less accurately (Bassetti & Masterson, 2012); the learner contrast in Cui et al. (2023) is not significant |
| 4 | 6.2 | The menu "raised comprehension from 56% to 71%. Sincere play increased from 48% to 59%" | Two different baselines. Understanding: 71% against 58% and 56%. Straightforward play: 59%, against 56% for the traditional description (p = 0.47, no difference) and 48% for a near-zero-information control (Gonczarowski et al., 2024) |
| 5 | 4.2 | Layout "shifted consent rates by orders of magnitude, while changing the textual disclosure language produced no detectable effect" | Removing the opt-out button raised consent by 22 to 23 percentage points (Nouwens et al., 2020). The claim about text was not found |
| 6 | 7.2 | The industry "attempted self-regulation through the FX Global Code… But voluntary soft-law adherence failed… until public financial regulators intervened" (2014–15) | The chronology is reversed. The fines came in 2014–15; the Code followed in 2017. Principles 7, 9, 36, 39 and 40 concern complaints, disclosure and terms, not last look or pre-hedging |
| 7 | 7.3 | The P2B Regulation and the DSA "merely mandate that platforms describe their ranking parameters and terms in plain language… changing nothing about operational mechanics" | P2B Art. 3 requires 15 days' notice of changes to terms. DSA Arts. 17 and 20 require a statement of reasons and an internal complaint system; Arts. 53–54 give a complaint to a regulator and damages |

Other statements that go beyond their sources:

- **Seira et al. (4.2, intro).** One bank's field experiment with messages, not "Mexican credit card
  companies" under a mandate. Delinquency rose for two client groups by 0.011 points, 7.4% of the mean.
  "The disclosure made the debt feel insurmountable" is not in the paper.
- **Poursabzi-Sangdeh et al. (4.2).** "An illusion of competence" is the draft's mechanism. The authors
  conjecture information overload, and the effect holds in three of four experiments on one unusual case.
- **Ben-Shahar & Schneider (4.1).** The quotation "the most common and least effective regulatory
  technique in modern law" (p. 665) is not the wording the audit found on that page. The "bright caloric
  label" is not their example; theirs is restaurant letter grades (p. 743), which they hedge.
- **Vasconcelos et al. (2.1)** is cited for misplaced confidence. The paper shows explanations *reducing*
  overreliance in a hard task. **Parasuraman & Manzey** do not use "transparency paradox".
- **Nadella (4.3).** The post has seven principles, not "three pillars". "Halt switches" is in quotation
  marks and is not his phrase; he writes of an emergency brake. The people affected are not "handed the
  tamper-proof human-readable audit log"; P20 promises them disclosure of incidents.
- **Saenger (3.1).** "Confined to an elite, highly trained scribal caste" and "impossible to parse
  phonologically" are not his. Celtic and Old English do share roots with Latin; his point is that the
  Irish and English learned Latin as a foreign language. The distinctiones are an ancient system, and
  "codex page indexing by the eleventh century" has no source here. The conclusion says "before the
  eighth century"; the body says late seventh.
- **Carolingian sources (3.3, 7.3).** None of them mentions word separation, and Insular spacing predates
  them. "Held accountable to readers by external sovereign authority" is the draft's reading.
- **Chen, Mislove, & Wilson (5.3).** The bug is Uber's own account; "an engineering synchronization bug
  in their geospatial grid" adds detail the paper does not give.
- **Ghalme et al. (5.2)** is a machine-learning theory paper and cannot be cited for gig workers sharing
  screenshots. The driver vignette (second phone, "two blocks north") is not in Lee et al. or Kellogg et
  al. as described.
- **Oberschelp (5.1)** did not treat algorithmacy as "procedural programming literacy for
  schoolchildren". He used the word once, undefined, for mental algorithmic skill without tools.
- **Rahmandad & Gary (5.3).** "Even after hundreds of trials" and "superstitious heuristics" are not
  theirs; delay and noise had different effects.
- **RFC 8890 (7.2)** is from the IAB and does not "explicitly declare that internet standards do not bind
  proprietary platforms".
- **Alfrink et al. and Lyons et al. (2.3)** are about contestability and do not describe a mediator that
  reads both sides and commits a binding allocation.

## 4. The argument

1. **The abstract and introduction still condemn all disclosure; section 4.1 does not.** The taxonomy
   says Target 4 fails, and 6.2 relies on Target 3 working (Masuda et al.). The thesis sentence should
   say which disclosure is the category error.
2. **"HCI remains oriented around dyadic interaction" (2.3) will be contested.** CSCW is the study of
   multi-party systems, and AI-mediated communication is an established HCI topic. The project holds
   Hohenstein et al. (2023) on exactly this. The claim needs narrowing to transparency and explanation
   research, with that literature cited.
3. **The second introduction paragraph says "In none of these settings does the algorithm issue a
   determination binding both parties".** Jhaver et al. is a platform setting. The sentence refers to the
   two helpful cases and should say so.
4. **Claim 1 is not falsifiable as written.** "Strictly positive integrated information (Φ > 0) that
   cannot be factored" is a definition, and the measure proposed is a proxy. Engel and Malone had no
   mediator. Barrett et al. say Φ has only ever been computed by proxy. State the claim as a comparison
   the data could fail, and say the application to human triads is untested. This also keeps the paper
   inside the lab's own rule that irreducibility is explored, not established.
5. **Claim 4 introduces "verifiable cryptographic… lock-in"** with no source and no arm in the protocol.
6. **Scope boundary 2 overstates Convention A.** "Rests on established empirical mechanism design" sits
   beside a result in which the best presentation did not beat the traditional one on play.
7. **Scope boundary 3 says nudging "alters choice presentation within an unchanged game".** The nudge and
   boost literature is the nearest rival and needs more than one sentence (Hertwig & Grüne-Yanoff, 2017).
   Mertens et al. also class re-representation of information with informational interventions.
8. **"Following the model established by Terveen and McDonald (2005)".** Nobody on this project has read
   it.
9. **Section 5.3 says platforms "deliberately disrupt ecological validity"**, then correctly separates
   secrecy from noise. The opening sentence should match the distinction that follows.

## 5. Fit to *Human–Computer Interaction*

- **Length.** By my estimate the body runs to about 6,500 words, roughly half the journal's norm (not counted by script; the draft arrived as pasted text). Its articles average 35 printed pages; the
  four read ran 9,000 to 17,000 words. Sections 2, 5 and 7 are thin against their models.
- **Roadmap.** A numbered list with bold labels. The journal's introductions end in prose.
- **Diagrams.** Eight ASCII boxes. They need to be real figures, and three (the dyad, the page shift, the
  literacy/algorithmacy contrast) add nothing the prose does not say.
- **Voice.** "I" in the introduction, "we" in sections 3, 7 and 8. Sole authors in this journal write "I".
- **Convention B has three names**: "valid, low-latency feedback" (abstract), "ecological feedback
  immediacy" (body), and "Radical" survives nowhere, which is right. Pick one.
- **Evidence.** The journal says "every paper should have empirical evidence that validates its results".
  Convention B has none from a triad, and the draft says so only in 9.2. Say it in section 6.
- **Prior posting.** Still to raise with the editor.

## 6. Prose

The author's own style rules ban emphasis openers. The draft opens sentences with "Importantly," and
"Notably,"; it uses the "not X; it is Y" frame repeatedly ("The failure is not an empirical anomaly; it
is a category error"); and it ends paragraphs on epigrams ("an audit log is an
autopsy report"). "Zenith", "apex", "shatters", "paranoia", "victim" and "heroic" overstate. The best
paragraphs are the plain ones: the reply to Özçetin et al. and the definition of the custody test.

## 7. Order of repair

1. Rebuild the reference list from `literature/references.bib`, which holds the verified record for
   nearly every source in 2a. Check the sixteen entries in 2b against Crossref. Reconcile 2c and 2d.
2. Correct the seven reversals in section 3 above, then the overstated attributions.
3. Narrow the thesis to Target 4 disclosure and fix the dyad claim in 2.3.
4. Rewrite Claim 1 and drop or source Claim 4's cryptographic clause.
5. Read Terveen and McDonald (2005) before citing it as the model.
6. Lengthen sections 2, 5 and 7; turn the roadmap into prose; settle "I"; name Convention B once.
7. The author's read-aloud pass.
