<!-- Version 2 of the manuscript. Drafted by Claude on 2026-10-13 on the author's instruction ("full rewrite but maintain the writing style"; target: Business Ethics Quarterly, 12,000 words). It reworks the author's second draft (AUTHOR_DRAFT_v2.md) in light of the six reviews in review/. Where the author's sentences were sound they are kept; everything else is Claude's and is the author's only once he has revised it. Notes for the author are in MANUSCRIPT_v2_NOTES.md. -->

# Algorithmacy: Institutional Domination, Triadic Mediation, and the Limits of Literacy in Algorithmic Governance

## Abstract

AI-ethics frameworks routinely prescribe "AI literacy" and explanation as the main safeguards against algorithmic harm. Yet when reading and writing became conditions of civic and legal standing, the deepest injuries did not arise from an uneducated public. Institutions that held the test, the access, and the record inflicted them. This paper reads the history of that transition to theorize algorithmacy—the relational competence demanded when two human parties coordinate through an algorithmic intermediary that reads both and commits an outcome binding on both. Using internal critique, I identify five things institutions did with literacy: they gated standing on a discretionary test, withheld the competence by law, let a written record override what was said, enclosed the means of print, and oversold literacy's returns. I describe the positions those institutions held with the republican concept of domination, and I argue that algorithmic intermediaries now hold the same positions. Two differences sharpen the problem. The intermediary adapts to the person it reads, and no independent party with binding authority stands at the point of decision, as notaries, second interpreters, and pleas such as *non est factum* once stood beside human scribes. From the argument I derive three duties for the operators of algorithmic intermediaries: structural refusal, declared operating envelopes, and counter-delegation.

**Keywords:** algorithmic management; AI literacy; domination; internal critique; platforms; history of literacy

## 1. Introduction

People now reach credit, work, and civic standing through algorithmic systems that read their behavior and commit binding decisions. Scholars who write on the ethics of these systems agree on a first duty: do no harm. Jobin, Ienca, and Vayena (2019) reviewed 84 sets of AI-ethics guidelines and found non-maleficence named in 60 and beneficence in 41. In business ethics and in regulation, the remedy most often derived from that duty is to inform the affected person—to mandate disclosure, to ground a right to an explanation (Kim & Routledge, 2022), and to train the user under the banner of "AI literacy." The remedy has a known limit. Edwards and Veale (2017, p. 67) call reliance on individual rights to explanation a "transparency fallacy," because "Individual data subjects are not empowered to make use of the kind of algorithmic explanations they are likely to be offered." Berthon, Pitt, and Campbell (2019, p. 457) report of digital addiction that "information is necessary, but not sufficient to change behavior." Williams (2018, p. 101) writes of the attention economy that education is necessary and not sufficient, "Nor will 'media literacy' alone lead us out of this forest." Kamperman and Graff (2026, p. 36) look to the history of reading for the reason: the AI-literacy movement repeats the myth that "Literacy is a certain or guaranteed path to economic security." The comparison between learning to read and learning to live with algorithms is therefore already on the table (Vee, 2013; Kamperman & Graff, 2026). Those who have drawn it center the skill and its oversold returns, and they leave the institutional positions around the skill unexamined.

Overselling, however, was the smallest part of what went wrong when reading became a condition of legal and civic standing. The actors who held the test, the access, and the record committed the deeper wrongs, and they committed them with literacy. When Alabama's constitutional convention met in 1901 to write a literacy test into the franchise, its president told the delegates what they had gathered to do: "within the limits imposed by the Federal Constitution, to establish white supremacy in this State" (Alabama Constitutional Convention, 1901, p. 8). Decades earlier, Hugh Auld forbade his wife to teach Frederick Douglass to read because learning would "forever unfit him to be a slave" (Douglass, 1845, p. 33). And when the Supreme Court of Canada decided in 1999 what a Mi'kmaq treaty of 1760 had promised, it observed of such treaties that "The Indian parties did not, for all practical purposes, have the opportunity to create their own written record of the negotiations" (*R. v. Marshall*, 1999, para. 14). None of these injuries was an educational deficit or a broken promise. Each was the use of a position that opened once a competence became compulsory—the examiner's, the teacher's, the record-keeper's.

That history matters because the positions are occupied again. When a job applicant and an employer, a borrower and a lender, or a driver and a rider deal with each other through a platform, two human parties coordinate through an automated third party that reads both and enforces an outcome binding on both. I call the competence this arrangement demands algorithmacy. The intermediary holds the test: where employers share a screening vendor, 4% of applicants who apply to ten positions are recommended for rejection from all ten (Bommasani et al., 2026). It controls access to the competence: a ride-hail driver has "about 15 seconds" to accept a trip and is "not shown destination or fare information" beforehand (Rosenblat & Stark, 2016, p. 3762). And it keeps the record: drivers who inquire about a decision "usually receive template responses" (Rosenblat & Stark, 2016, p. 3771). If the lesson of the literacy transition were that reformers oversold reading, better training and clearer explanations would answer it. If the wrongs lay with whoever held the test, the access, and the record, an ethics that educates the user addresses the wrong party.

I therefore read the record of the literacy transition for what named institutions—legislatures, courts, churches, and a chartered company—did with written competence once standing depended on it. I judge those practices by internal critique: a practice counts as an ethical failure when contemporaries condemned it, when the institution broke a standard it professed, or when the outcome fell short of what its sponsors promised. Five practices meet that test: gating standing on a discretionary reading test, withholding the competence by law, letting a written record override what was said, enclosing the means of print by charter, and promoting individual literacy as the cure for a structural condition. I treat this history as evidence about institutions and its algorithmic counterpart as a bounded analogy, and for each practice I name the property the analogy rests on and the point at which it gives way.

The paper makes three contributions to normative business ethics. First, it replaces the diffuse charge that "society" failed to spread literacy with five documented practices and their actors, and it reserves a collective charge for the international campaigns that set targets and missed them. Second, it moves the analogy between literacy and algorithmic mediation from the user's skill to the positions around the medium, which is where four of the five failures lie and where earlier critiques of AI literacy do not reach (Brandt, 1998; Kamperman & Graff, 2026). Third, it identifies what differs this time—the intermediary adapts to the person it reads, and no independent party with binding authority checks it at the point of decision—and it derives from that difference three duties for the operators of algorithmic intermediaries.

The argument runs in four steps. Section 2 defines the relation, describes the positions with the republican concept of domination, and states the standard by which I judge them. Section 3 documents the five practices and what the record does not show. Section 4 maps the positions onto algorithmic intermediaries and marks the two points where the analogy gives way. Section 5 derives the duties and answers three objections; Section 6 states the limits of the evidence.

## 2. Framework: A Relation, a Position, and a Standard

### 2.1 Algorithmacy as a relation among three parties

Policy talk about AI pictures a person and a machine: a user prompts a model, an applicant submits a form, and the software answers. The picture leaves someone out. Most consequential algorithmic systems stand between people who need something from each other, and I use *algorithmacy* for the competence that standing-between demands: the capacity to coordinate with another person through an automated third party that reads both and commits an outcome binding on both. A screening vendor stands between an applicant and an employer. A credit bureau's score stands between a borrower and a lender. A ride-hail platform stands between a driver and a rider. Not every algorithmic encounter has this shape—a lender that scores its own applicants, or a platform that moderates its own users' posts, is one party judging another—and I confine the term to cases that do.

Simmel gave the sociology of this shape. The third element in a triad may be an impartial mediator who wishes "to save the group unity from the danger of splitting up," or it may be the third who profits: "the non-partisan may also use his relatively superior position for purely egoistic interests" (Simmel, 1950, p. 154). Which of these a given intermediary is depends on who pays it and whose instructions it carries. Many platforms occupy both of Simmel's roles and a further one: the ride-hail firm presents itself as the neutral matcher of driver and rider, earns a commission on each match, and is also the driver's contractual counterparty. Section 4 returns to that doubling, because the law has historically treated the neutral third and the interested counterparty under different rules.

The word invites two objections, and the triad answers both. Kamperman and Graff (2026, p. 35) fault AI-literacy initiatives that "use literacy uncritically as a metaphor." Street's critique of what he called the autonomous model of literacy cuts deeper: the model assumes that introducing literacy "will have the effect of enhancing their cognitive skills, improving their economic prospects, making them better citizens, regardless of the social and economic conditions that accounted for their 'illiteracy' in the first place" (Street, 2003, p. 77). A term ending in "-acy" can smuggle that assumption back in. I do not claim that dealing with an algorithm is a kind of reading, or that mediation alters cognition. Algorithmacy names a relation among three parties, and the comparison with literacy that follows is a comparison of the positions that open around a competence once institutions make it compulsory.

Literacy scholars have a concept close to those positions. Brandt (1998) defined the sponsors of literacy as agents "who enable, support, teach, or model, as well as recruit, regulate, suppress, or withhold literacy and gain advantage by it in some way." Her sponsor stands between a learner and literacy. The intermediary I describe stands between two people and an outcome: it need not teach or withhold anything to hold the test that sorts them and the record that binds them. Brandt's concept explains who profits from a competence. The triad adds who decides between its holders.

The nearest precedent for the comparison itself is Vee (2013), who sets programming beside the history of mass literacy and concludes that as more of social life is conducted through code, "the power balance is once again shifting toward those who are skilled in this new literacy technology" (p. 55). I read the same history to a different conclusion. In the cases below, power went less to the skilled than to whoever examined, taught, and recorded them, and the skilled were often people like Douglass, who had the competence and none of the positions.

### 2.2 Domination as the description of a position

The positions need a description that does not depend on anyone's bad intent. Republican political theory supplies one. On Pettit's account, a person is free to the extent that no one has "the capacity to interfere in their affairs on an arbitrary basis" (Pettit, 1997, as quoted in Lovett, 2026); domination is the standing capacity, whether or not anyone exercises it, which is why the slave of a kindly master remains unfree. The registrar who chooses the passage an applicant must read and alone judges the answer holds that capacity over the applicant. So does the party that drafts the only record of an agreement the other party cannot read.

Three clarifications keep the concept honest. First, I use domination to describe positions, not to condemn them. Lovett (2026) notes that republicans define arbitrary power procedurally or by the absence of control, not as unjust power, so that calling a position dominating leaves open whether a given exercise of it was wrong. Section 2.3 supplies the standard of wrongness. Second, the concept does not require that the holder be unconstrained in every respect. Statutes, contracts, and competition limit what a platform may do, as constitutions limited what a registrar might do; the question in each case is whether the affected person can know the rule in advance and contest its application to an independent party. Third, the concept has already reached the workplace and the platform. Muldoon and Raekstad (2023) apply it to ride-hail and delivery work, where information asymmetries decrease "workers' ability both to understand and contest the decisions that are made over them" (p. 596) and "Workers have had their accounts deleted by an algorithm without warning and with no right to contest the decision" (p. 599). They locate the dominating agent in owners and managers. I follow them in holding the operator responsible, and I add the second party: the intermediary's reading binds the rider, the employer, or the lender as well, and neither flank can check it.

Republican theory also says what removes arbitrariness, and the answer shapes Section 5. On the procedural view, power is non-arbitrary when it follows rules that are common knowledge; on the democratic view, when those subject to it control it (Lovett, 2026). Coping is not enough: "Just because one is better able to cope with arbitrary power, it does not follow that one's domination is any less" (Lovett, 2026). A person who has learned to predict a system that can change its rules at will has gained skill and no standing.

### 2.3 The standard: internal critique, applied to both periods

By what standard did the institutions of the literacy transition fail? Importing a present-day theory to condemn 1740 or 1901 invites the charge Butterfield (1931) made against history written as the ratification of the present. I use a narrower instrument. Walzer (1988) describes social criticism as "an internal argument," conducted by a critic who asks whether "standards [are] available to him that are internal to the practices and understandings of his own society, and at the same time properly critical" (p. 34), and he observes that "The same men and women who act badly create and sustain the standards by which (at least sometimes) they know themselves to act badly" (p. 42). From that method I draw three benchmarks. They are mine, built on his premise. A practice counts as an ethical failure if (1) contemporaries condemned it in the moral vocabulary of their time, (2) the institution broke a standard it publicly professed, or (3) the outcome fell systematically short of what its sponsors promised.

Two points about this choice. The benchmarks apply to both periods: Section 5 judges platform operators by the standards they profess, the objections their contemporaries raise, and the promises made on their behalf, and it uses nothing else. And the choice is a discipline I adopt, not a constraint that the avoidance of anachronism forces. Moody-Adams (1994) argues that the "standards of their own day" defence rests on a mistake: theories that excuse past wrongdoers "base hypotheses about what some agent(s) could not do solely on evidence of what the agent(s) did not do" (p. 294), when the ignorance in question was often affected—"choosing not to know what one can and should know" (p. 296). On her argument a present-day standard would not be unfair. I keep to internal benchmarks because they are sufficient for four of the five practices and because they make the fifth case's weakness visible: for the record over the voice, contemporary objection is thin, and I say so in Section 3.3.

Moody-Adams also bears on who failed. "A culture," she writes, "cannot be an 'agent' of anything" (p. 304). The practices below are the acts of legislatures, courts, a chartered company, and conference sponsors, and I name them.

### 2.4 What the charge is not

The charge is against what institutions did with literacy, never against literacy. People sought it at cost. Johansson (1985, p. 64) describes a Swedish church program in which reading was "everybody's calling and right"; Washington (1901, p. 30) remembered "a whole race trying to go to school" after emancipation. Graff, the historian most associated with debunking literacy's promises, wrote that "Literacy did carry certain benefits" (Graff, 1979, p. 19). The same holds for the algorithmic case: nothing here denies that people gain from understanding the systems that sort them. The argument concerns what the holders of three positions may do while people learn.

## 3. Five Things Done with Literacy

The five practices below share a structure. In each, an institution held a position that literacy's new importance had created, and used it over people who could not check the use. For each I give what was done, by whom, on what stated ground, who objected, and what ended it. Table 1 in Section 4 sets the five beside their present-day counterparts.

### 3.1 The gate

The plainest practice is the reading test as a gate: an examination neutral on its face, administered at an official's discretion, to exclude a targeted group from standing. The voter literacy tests of the American South after Reconstruction are the best documented.

The Fifteenth Amendment barred denial of the vote on account of race, so Southern conventions built facially neutral barriers. John B. Knox, presiding over Alabama's convention in 1901, stated the purpose in his opening address: "And what is it that we want to do? Why it is within the limits imposed by the Federal Constitution, to establish white supremacy in this State" (Alabama Constitutional Convention, 1901, p. 8). The device worked through discretion. The Supreme Court later described how registrars in the covered states applied the tests, giving white applicants easy passages or help and Black applicants difficult ones without help (*South Carolina v. Katzenbach*, 1966, at 312). The Court's footnotes give the texture. In Louisiana a white applicant "satisfied the registrar of his ability to interpret the state constitution by writing, 'FRDUM FOOF SPETGH'"; in Panola County, Mississippi, "the registrar required Negroes to interpret the provision of the state constitution concerning 'the rate of interest on the fund known as the "Chickasaw School Fund"'" (at 312, nn. 12–13). The test measured the examiner's wishes. Knox himself recorded the objection. Reviewing Mississippi's rule that a voter must "understand" a constitutional clause when read, he observed that the decision "is exclusively in the hands of the registrars," and conceded that "the objection has been urged with force that it perpetuates the very form of abuse which we are seeking to escape" (Alabama Constitutional Convention, 1901, p. 11).

The second benchmark applies as well as the first. The states that tested for reading had run the schools. In *Gaston County v. United States* (1969), the Court refused to let a county reinstate a literacy test after it had maintained "separate and inferior schools" for its Black residents. The effect of the Southern restrictions as a whole, of which the test was one part, was large: a reviewer reports Kousser's finding that turnout fell from 64 percent of eligible voters in the 1880s to 30 percent in the first decade of the new century, and that black-belt Democrats "wanted to eliminate the voting of poor whites as well as blacks" while "Populists, Republicans, and blacks consistently opposed the new laws" (Holmes, 1975, pp. 270–271).

The device traveled. Natal's Immigration Restriction Act of 1897 required a migrant to write in a European language, and the colony's Premier explained why the American model would not do: the people he meant to exclude were "perfectly well able to read and write in their own language" (quoted in Lake, 2006). Australia's Immigration Restriction Act of 1901 followed Natal's, excluding anyone who "fails to write out at dictation and sign in the presence of the officer a passage of fifty words in length in an European language directed by the officer" (s. 3(a)); the test remained in law until 1958. Natal and Australia show a feature the Southern tests share: whoever chooses the language and the passage holds the gate. In Latin America the literacy rule came earlier and lasted longer. Engerman and Sokoloff (2001, pp. 23–25) find literacy requirements in the early constitutions of most of the new republics; Brazil's Saraiva Law of 1881 made reading and writing a condition of enrolment, and Brazil kept illiterate citizens off the rolls until 1985.

Contemporaries named the wrong. When Congress passed a literacy test for immigrants in 1897, President Cleveland vetoed it: "It is said, however, that the quality of recent immigration is undesirable. The time is quite within recent memory when the same thing was said of immigrants who, with their descendants, are now numbered among our best citizens" (Cleveland, 1897). President Wilson vetoed the same device in 1917 because it "is not a test of character, of quality, or of personal fitness, but would operate in most cases merely as a penalty for lack of opportunity in the country from which the alien seeking admission came" (Wilson, 1917). Congress enacted it over his veto. The voting tests ended when the Voting Rights Act of 1965 suspended them where its formula applied and the 1970 amendments barred them nationwide. No one ended them by learning to read better.

### 3.2 The withheld competence

Where keeping people incompetent kept them governable, institutions forbade the teaching. South Carolina's Negro Act of 1740 fined anyone who taught an enslaved person to write. Between 1829 and 1834 Georgia, Virginia, Alabama, and North Carolina passed acts of their own; each is narrower than its usual summary, and Virginia's of April 1831, for instance, barred assemblies of free Black people for instruction and the paid teaching of slaves. A reviewer of Williams's history of Black education gives the legislators' ground in a phrase: "Fearing insurrection, southern state legislatures made it a crime for persons to instruct slaves or free blacks to read and write" (Margo, 2005, p. 590).

The fullest statement of the rationale is a slaveholder's, as Douglass reports it. Hugh Auld "at once forbade Mrs. Auld to instruct me further, telling her, among other things, that it was unlawful, as well as unsafe, to teach a slave to read"; learning, Auld said, "would forever unfit him to be a slave. He would at once become unmanageable, and of no value to his master" (Douglass, 1845, p. 33). Douglass taught himself, and recorded what the competence was worth inside a closed system: "It had given me a view of my wretched condition, without the remedy. It opened my eyes to the horrible pit, but to no ladder upon which to get out" (Douglass, 1845, ch. VII). I return to that sentence in Section 4, because it is the earliest statement I know of a point the algorithmic literature has rediscovered: comprehension is not leverage.

Objection at the time is on the record. Margaret Douglass, a white woman prosecuted in Norfolk in 1853 for teaching free Black children to read, told the court that she would be "a single sufferer under the operation of one of the most inhuman and unjust laws that ever disgraced the statute book of a civilized community" (M. Douglass, 1854, p. 36). She served a month in jail.

The practice was not American only, though elsewhere it attached to reading matter and language more often than to the alphabet. In 1531 the Queen of Spain instructed the House of Trade to stop "books of fiction in the vernacular" from going to the Indies, "since this is bad practice for the Indians and something with which it is not well for them to be concerned or read" (quoted in Leonard, 1992, pp. 81–84); the order was repeated in 1536 and 1543. In the Russian Empire the Valuev circular of 1863 halted religious and educational publishing in Ukrainian on the ground that "a [distinct] Little Russian ... language did not, does not and cannot exist," and the Ems decree of 1876 tightened the ban until 1905 (Moser, 2017, p. 3). In British India the exclusion ran through custom that the state's schools tolerated. Jotirao Phule told the Education Commission in 1882 that "The Mahars, Mangs, and other lower classes are practically excluded from all schools owing to caste prejudices," and he appealed to the Queen's Proclamation for separate schools (Phule, 1882)—an objection by a contemporary, invoking the ruler's own professed standard.

Two limits apply. No source I have read measures what the American statutes achieved, and the reviewer of Williams notes that she does not test whether they were effective (Margo, 2005, p. 591). And several of these bans leaked: the Spanish orders were repeated because they were not obeyed. The failure I record is the order and its stated ground.

### 3.3 The record over the voice

The third practice arose where an agreement was made by speech and proved by writing. The party that wrote the record bound the party that could not make its own.

That writing should outrank speech is a legal choice, not a property of writing. In the shari'a courts of highland Yemen that Messick studied, "the manuals discuss witnessing support for documents, but they do not consider documents to be potential evidence" (Messick, 1993, pp. 209–210): doctrine put the oral testimony of reliable witnesses first, even as practice relied on documents. Where the common law chose the document, the consequences fell on those who had no documents of their own. Deciding in 1999 whether a Mi'kmaq man could rely on promises made in treaty talks of 1760, the Supreme Court of Canada held that "the Nova Scotia judgments erred in concluding that the only enforceable treaty obligations were those set out in the written document of March 10, 1760" (*R. v. Marshall*, 1999, para. 40), having observed that the Indigenous parties to such treaties had no practical opportunity to create their own written record (para. 14). Two years earlier the Court had warned that under a trial judge's approach, "the oral histories of aboriginal peoples would be consistently and systematically undervalued by the Canadian legal system" (*Delgamuukw v. British Columbia*, 1997, para. 98).

The Treaty of Waitangi shows the third party at work. In February 1840 William Hobson negotiated for the Crown with Māori rangatira through the missionary Henry Williams, who had made the Māori text and interpreted "sentence by sentence" (Waitangi Tribunal, 2014, p. 355). More than 500 rangatira eventually signed; 39 signed the English text (p. 386). The English text ceded sovereignty. The Māori text, the Tribunal found, did not, and the rangatira who signed it "did not cede their sovereignty" (p. xxii). Williams was not a disinterested translator. His bishop had written to him weeks earlier instructing him to support Hobson's efforts to obtain cession (p. 506), and he held land. Whether he deceived is disputed among the historians the Tribunal reviews—Ward doubts it, while Belich calls the choice of terms "a deliberate or semi-deliberate act of deceit" (pp. 414–415)—and the Tribunal's own judgment is measured: Williams "may have been honest in his choice of 'kawanatanga'" but "must, however, have known that tino rangatiratanga conveyed more than what was set out in the English text" (p. 514).

On the benchmarks this practice is the weakest of the five. The standard comes mostly from later courts. One contemporary did raise the danger: on the day of signing, the missionary printer William Colenso asked Hobson whether the chiefs understood the articles (Waitangi Tribunal, 2014, p. 352). Beyond that, the record of objection is thin, and I do not claim more than Moody-Adams's argument allows—that a thin record of objection does not show the actors could not have known.

The same era also shows what a society does when it takes the danger seriously, and this matters more for the present argument than the wrong itself. Castile's Pragmática of Alcalá (1503) required notaries to keep a register and to read their notes to the parties and witnesses present—"las lean presentes las partes e los testigos"—and required a witness to sign for a party who could not (Almeida Cabrejas, 2019, p. 24, quoting the law). At Anglo-Iroquois councils, "When doubts about an interpreter's integrity or ability arose on either the Indian or the English side, others were employed, formally or informally, to 'assist' and check the accuracy of his translations" (Hagedorn, 1988, p. 61). English law gave a plea, *non est factum*, to the person who could not read and had "a written contract falsely read over to him" (*Foster v. Mackinnon*, 1869, at 711). These safeguards were imperfect. A reviewer of Burns's study of Cuzco reports that notaries "could manipulate the legal record in the service of a powerful client or on their own account" (Andrien, 2012, p. 145), and in *Foster* the person who misdescribed the paper was the other party to it. But each safeguard placed someone other than the writer at the point where the record was made, or gave the bound party a way to undo it.

### 3.4 The monopoly

The fourth practice concerns the means of the medium. In England the Crown chartered the Stationers' Company in the reign of Philip and Mary—4 May 1557 by the regnal year—and the charter confined printing to the Company's members and gave its wardens powers of search and seizure (Arber, 1875, vol. 1, pp. xxviii–xxxii). The Licensing Act of 1662 (14 Car. II c. 33) capped the number of master printers at twenty. The regime lapsed in 1695.

Objection came from outside and inside. Milton's pamphlet of 1644 put it as a matter of trade: "Truth and understanding are not such wares as to be monopolized and traded in by tickets and statutes and standards" (Milton, 1644). A year earlier the Company itself had petitioned Parliament against eleven of its own members who held the patents for the most profitable books, calling them "Monopolizers of Printing the most vendable Bookes of worth and quantity now in use" (Arber, 1875, vol. 1, p. 583).

This case carries the least weight of the five. It is one kingdom; I have found no count of those shut out; and every early modern state regulated print in some fashion, so the monopoly is not a departure from a free baseline. I include it because it shows the fourth position plainly: beside the examiner, the teacher, and the record-keeper stands the owner of the press.

### 3.5 The promise

The fifth practice is the only one with actors at world scale. The World Conference on Education for All at Jomtien in 1990 proposed, among targets that "countries may wish" to adopt, reducing adult illiteracy "to, say, one-half its 1990 level by the year 2000" (World Conference on Education for All, 1990, para. 8). The world rate fell by about a quarter, from 25.4 to 18.9 percent (UNESCO Institute for Statistics, 2026). At Dakar in 2000 the World Education Forum committed to "Achieving a 50 per cent improvement in levels of adult literacy by 2015" (World Education Forum, 2000). The monitoring report of 2015 records that illiteracy fell from 18 to an estimated 14 percent, "which means the Dakar target of halving illiteracy was not achieved" (UNESCO, 2015). In 2024, 739 million adults could not read and write a simple statement, 63 percent of them women (UNESCO Institute for Statistics, 2026).

Missed targets alone would be a failure of delivery. The ethical failure is the premise beneath them, which Graff named the literacy myth. Studying three Ontario cities in 1861, he found that for an unskilled or semiskilled worker, "Doing his or her job seldom, if ever, required the use of reading and writing" (Graff, 1979, p. 302), and he concluded that "literacy was more valuable to the society's goals and needs than to those of most individuals within it" (p. 321). Street's autonomous model, quoted in Section 2.1, is the same premise seen from anthropology: literacy offered as a remedy "regardless of the social and economic conditions." Marketing scholars have documented the general form. Giesler and Veresiu (2014) trace how responsibility for structural problems is shifted onto the individual consumer, with the "financially literate consumer" among their cases. A competence is promoted; the condition it was to cure persists; and the person who was to acquire it bears the blame.

Graff's qualifications belong in the account. Skilled and clerical work did demand literacy, and he reports differential access to the artisanal level and its rewards (1979, p. 302); the myth was an exaggeration of something true. Nor was the doubt his alone. He quotes W. B. Hodgson, who warned in 1868 that "the power to read does not in the least determine the use to which it is put" (p. 301). A contemporary named the overselling while it was under way, so the first benchmark is met as well as the third.

### 3.6 What the record does not show

Three things qualify the account, and a referee should have them before the analogy is drawn.

First, the record is not a survey. The exclusionary gate with a stated purpose is documented for the American South and Natal; the withheld competence chiefly for the American slave states; the record over the voice for colonial treaties; the monopoly for one kingdom. I claim that named institutions did these five things, not that every literate society did.

Second, the counter-evidence is real. The Swedish program that made reading "everybody's calling and right" also compelled it, and tied confirmation and marriage to the examination (Johansson, 1985, p. 64): the achievement and the gate sat in one institution. Bans leaked, as Section 3.2 noted. Illiterate people used notaries for their own ends, and the Castilian registers Almeida Cabrejas studied are full of witnesses signing at the request of parties who could not (2019, p. 29). The third party was not always the stronger side's instrument.

Third, the gravest wrong done in the name of schooling is not a failure of literacy and I do not count it as a sixth practice. Canada's Truth and Reconciliation Commission (2015) and the United States Department of the Interior (Newland, 2022) document the removal of Indigenous children, forced labor, abuse, and the suppression of languages. Neither attributes the harm to the teaching of reading. What those reports do establish, and what Section 5 uses, is narrower: participation was compulsory, and one language of record was enforced.

## 4. The Positions, Occupied Again

### 4.1 The mapping

Table 1 sets each practice beside its present-day counterpart and states the property the comparison rests on. The property matters more than the resemblance: an analogy that does not say what carries it invites governance aimed at the wrong feature of a system.

**Table 1. Five positions, then and now**

| Position | Literacy transition | Property compared | Algorithmic intermediary | Where the comparison is weak |
| --- | --- | --- | --- | --- |
| The gate | Reading tests administered at a registrar's or officer's discretion (*Katzenbach*, 1966; Immigration Restriction Act 1901) | Standing depends on being read by a party one cannot question | Shared screening models that reject the same applicants across employers (Bommasani et al., 2026) | The present gate is the intermediary's reading of the person, not a test of the person's competence |
| The withheld competence | Laws against teaching (Douglass, 1845; Moser, 2017) | The party that gains from incompetence controls access to the competence | Trips offered without destination or fare (Rosenblat & Stark, 2016); opaque evaluations (Rahman, 2021) | No law forbids learning; trade secrecy and interface design do the withholding |
| The record | A written text binding a party who could not make its own (*Marshall*, 1999; Waitangi Tribunal, 2014) | One side holds the binding record of what both agreed | Decisions and their grounds held by the platform; template replies (Rosenblat & Stark, 2016) | The user has agreed to standard terms; the law treats that as assent |
| The means | A chartered monopoly of print (Arber, 1875) | Few hands hold the means of the medium | Concentrated infrastructure for training and serving models | Not established here; see Section 6 |
| The promise | Literacy as the cure for a structural condition (Graff, 1979; UNESCO, 2015) | A competence sold as the remedy for a position | "AI literacy" as the safeguard (Kamperman & Graff, 2026) | Its advocates act in good faith, as many literacy campaigners did |

Take the gate first. Bommasani and colleagues (2026) study roughly three million applicants screened by a single vendor's models and find that 4% of those who apply to ten positions are recommended for rejection from all ten, a rate above chance; applicants, they write, "would need to apply widely in order to ensure their applications are considered by a human." The registrar's discretion has no counterpart in intent—nothing in the study suggests a purpose to exclude—but it has one in structure. A single reader's judgment follows the applicant from door to door, and the applicant cannot ask it a question.

The withheld competence maps onto design. Rosenblat and Stark (2016, p. 3762) found that Uber drivers had about fifteen seconds to accept a trip and were not shown its destination or fare. Rahman (2021) studied a labor platform that replaced a visible rating with an opaque evaluation, and found that workers could not work out what the criteria were and that the opacity itself disciplined them. No statute forbids these workers to learn how they are judged. The firm that gains from their not knowing controls what they can find out, which is the property the comparison rests on.

The record maps most closely, and it is the case where the triad matters. The intermediary's log is the only record of what passed between the two parties, and its determination is what binds them. A driver who disputes a fare, a rider who disputes a charge, and an applicant who asks why she was screened out all argue against a record they did not make and cannot inspect.

The promise maps without strain, because its present form is the subject of an existing literature. Kamperman and Graff (2026) show the AI-literacy movement repeating the literacy myth; Edwards and Veale (2017) show that the explanation a person is offered is one she is poorly placed to use; Giesler and Veresiu (2014) describe the general mechanism by which a structural problem becomes an individual's task. What the history adds is the company the promise keeps. Literacy was oversold by people who did not run the registrar's office. The promise mattered because it drew attention toward the learner while the other four positions did their work, and the same division of attention is visible now: a public debate about whether users understand AI proceeds beside a set of decisions about who may screen, withhold, and record.

The fourth position, the means, I leave as an open row. The Stationers held printing by a grant that anyone could read. Whether the infrastructure on which present intermediaries run is held in a comparable way is an empirical question about markets in computing and data that this paper has not examined, and the three duties do not depend on the answer.

### 4.2 Comprehension without leverage

The defense of explanation assumes that a person who understands a decision can act on it. Kim and Routledge (2022) ground a right to explanation in the trust that a firm's customers and workers place in it, and I do not dispute that such a right exists. The question is what the right delivers when nothing else changes.

Douglass answered in 1845. Reading gave him "a view of my wretched condition, without the remedy." The same structure appears in the platform evidence. Dubal (2023, p. 1984), reviewing drivers' efforts to obtain and analyze their own data, concludes that "Knowledge alone will not end or mitigate the precarities of digitalized pay." The evidence is not that knowledge is useless. Cameron (2024) finds that ride-hail drivers who learn the system use that knowledge in tactics of engagement and deviance, and that both kinds of tactic end by eliciting their consent to the work. Knowledge buys an individual worker room to maneuver inside terms she cannot alter. Republican theory predicts as much: coping with arbitrary power does not reduce it (Section 2.2).

### 4.3 The first difference: the medium answers back

The analogy gives way at two points, and both make the present case harder.

A page does not change with its reader. Once a person could read a statute, the statute read the same to her as to the registrar, and literacy could be turned against those who had rationed it; the Company's own members used print to petition against the Company. An algorithmic intermediary is a different kind of thing. Yeung (2016) describes data-driven decision systems as "extremely powerful and potent due to their networked, continuously updated, dynamic and pervasive nature," operating through a recursive loop in which the person's response to the system becomes an input to its next move. Her analysis concerns one user and one choice architect, and I extend it with caution to the triad. But the implication for a remedy by education is direct. A skill aimed at a fixed text accumulates. A skill aimed at a system that updates on the learner's behavior may be chasing its own shadow, and the party that holds the system decides how fast it moves.

### 4.4 The second difference: who checks the third party

The second difference concerns the safeguards of Section 3.3. I state it carefully, because the strong version—that algorithmic intermediaries operate with no procedural checks at all—is false.

Law now supplies checks. In the European Union, the Platform Work Directive requires that a decision to restrict, suspend, or terminate a platform worker's account be taken by a human being, and gives the worker a right to written reasons and to a review (Directive (EU) 2024/2831, arts. 10–11); member states must transpose it by 2 December 2026. The Digital Services Act requires that decisions on complaints be "taken under the supervision of appropriately qualified staff, and not solely on the basis of automated means" (Regulation (EU) 2022/2065, art. 20(6)), and it creates certified out-of-court dispute bodies. The General Data Protection Regulation gives a person subject to a solely automated decision the right to obtain human intervention and to contest it (Regulation (EU) 2016/679, art. 22(3)). For business users of platforms, a separate regulation requires a statement of reasons "on a durable medium" before an account is restricted (Regulation (EU) 2019/1150, art. 4). Contract law adds unconscionability, which asks whether a party, "considering his obvious education or lack of it," had "a reasonable opportunity to understand the terms of the contract" (*Williams v. Walker-Thomas Furniture Co.*, 1965), and courts and regulators stand behind all of these.

What survives is narrower and, I think, more telling. Three features of the old safeguards have no settled counterpart.

The first is timing. The notary read the instrument to the parties before they were bound. The modern rule runs the other way: "A contract need not be read to be effective," and "Competent adults are bound by such documents, read or unread" (*Hill v. Gateway 2000, Inc.*, 1997). The checks listed above operate after the decision.

The second is independence at the first instance. Under the Directive and the Regulation the first reviewer is the platform's own staff; the human intervention the GDPR guarantees is intervention "on the part of the controller." The independent bodies the Digital Services Act creates "shall not have the power to impose a binding settlement" (art. 21). A worker can reach a court, but a court is not at the point of decision, and the cost of reaching it falls on the weaker party.

The third is the separation of roles. The civil-law notary's professed duty runs to both parties and to the weaker of them (Union Internationale du Notariat, 2004, 2005). The standard-form contract belongs to a different legal world, in which one party drafts and the other adheres. A platform that mediates between driver and rider is at once Simmel's third and the driver's counterparty, the drafter of the terms and the keeper of the record of their performance. The historical safeguards assumed that these were different people.

So the claim is this: no independent party with binding authority stands at the point where an algorithmic intermediary's reading becomes a decision, and no rule requires anyone to read, explain, and certify a person's understanding before she is bound. The checks that exist are recent, regional, after the fact, and in the first instance the intermediary's own.

## 5. Three Duties of the Intermediary's Operator

### 5.1 The ground of the duties

If the injuries of algorithmic mediation come from positions and not from deficits in the user, the remedy belongs to whoever holds the positions. I ground the duties in the same three benchmarks that Section 3 applied to the past.

Operators break a standard they profess. The guidelines Jobin and colleagues counted are largely the industry's own, and non-maleficence leads them. A firm that publishes a commitment to avoid harm while keeping a decision procedure its subjects can neither foresee nor contest stands where the state stood in *Gaston County*: it tests for a competence under conditions it has itself arranged. Contemporaries condemn the practice, in the vocabulary of their time—drivers, the scholars who study them, and legislators (Rosenblat & Stark, 2016; Dubal, 2023; Muldoon & Raekstad, 2023). And the outcome falls short of the promise: explanation and literacy are offered as safeguards, and the evidence of Section 4.2 is that they leave the terms untouched.

The benchmarks say that something is owed. Republican theory says what: rules that are common knowledge, and a share of control for those subject to them (Section 2.2). The three duties below are those two requirements applied to the three positions. Structural refusal answers the gate. A declared operating envelope answers the withheld competence. Counter-delegation answers the one-sided record. Table 2 summarizes them.

**Table 2. Three duties of the operator**

| Position | Duty | What it requires | What it is not |
| --- | --- | --- | --- |
| The gate | Structural refusal | A route to the same standing that does not pass through the intermediary's reading, at no penalty | A right to exit a market that offers nowhere else to go |
| The withheld competence | Declared operating envelope | Advance, binding limits on what the system may do to the person, known to both parties | Disclosure of how the system works |
| The record | Counter-delegation | The person's own record and reader, and an independent party able to bind the operator on a dispute | An explanation supplied by the operator |

The duties fall first on operators—the firms that design and run the intermediary—because they hold the positions and can change them. They do not fall only there. Young's social-connection model holds that "all agents who contribute by their actions to the structural processes that produce injustice have responsibilities to work to remedy these injustices" (Young, 2006), and the employers who adopt a screening vendor, the lenders who buy a score, and the legislators who could require any of the three duties are such agents. Young's model is forward-looking and shared; it assigns no blame, and I use it only to say who else must act. The operator's duty rests on the simpler ground that it holds a position of power over people who cannot check it and professes not to harm them.

One alternative should be set aside. Balkin (2016) proposed treating platforms as information fiduciaries with duties of loyalty to their users. Khan and Pozen (2019, p. 504) reply that "A fiduciary with sharply opposed loyalties teeters on the edge of contradiction": the firm's officers owe their duties to stockholders. The triad adds a further difficulty, since an intermediary between a driver and a rider cannot be loyal to both in the fiduciary's sense. The notary's duty was never loyalty. It was impartiality toward two parties and care for the weaker, enforced by an office the parties did not control. The duties below aim at that structure.

### 5.2 Against the gate: structural refusal

Hirschman (1970) taught a generation to see exit as the customer's first defense. Exit protects no one when every door leads to the same reader. The applicant whom a shared model rejects from ten positions has ten exits and one examiner. Section 3.6 recorded what compulsory participation meant at its worst; the milder modern form is a market in which declining the intermediary's reading means declining to take part.

Structural refusal is the duty to keep open a route to the same standing that does not pass through the intermediary's reading, and to attach no penalty to taking it. For hiring, it means a human assessment available on request and weighed on the same footing. For credit, manual underwriting at comparable speed. The idea has antecedents: Zong and Matias (2024) treat refusal as something a system can be designed to honor, and the GDPR's article 22 already gives a narrow right not to be subject to solely automated decisions.

Two objections need answers. The first is cost: a second track is expensive, and a firm that maintains one may price it so that no one uses it. The duty therefore specifies no penalty, and it is the reason the duty cannot rest on the operator's goodwill; Hoeksema (2023) argues that exit and consent are the weakest answers to platform power for exactly this reason. The second objection is that the human on the second track may be no fairer than the model. That may be so. The duty does not promise a better reader. It denies any single reader the position of the registrar.

### 5.3 Against the withheld competence: declared operating envelopes

The obvious remedy for withheld knowledge is disclosure, and disclosure fails. Bakos, Marotta-Wurgler, and Trossen (2009) tracked visitors to software retailers and found that between one and two in a thousand opened the license agreement. Ben-Shahar and Schneider (2011, p. 672) quote the conclusion of that research: "No matter how prominently [end-user license agreements] are disclosed, they are almost always ignored." A fuller account of a model's workings would be read by fewer people still, and Section 4.3 gives a further reason to doubt it: the account describes a system that will have changed.

A declared operating envelope is a different instrument. It does not describe how the system works. It states in advance, and binds the operator to, the limits of what the system may do to the person: for a driver, the minimum pay for a trip of a given time and distance, the information shown before acceptance, the grounds on which an account may be suspended; for a borrower, the kinds of data that may not enter the score. The person need not understand the model to know where she stands, as a tenant need not understand the landlord's finances to know the rent.

European law has begun to require a part of this. The Platform Work Directive obliges platforms to tell workers "the categories of data and the main parameters that such systems take into account and the relative importance of those main parameters in the automated decision-making" (Directive (EU) 2024/2831, art. 9(1)(b)). That is a duty to inform about the method. An envelope goes one step further, from describing the parameters to committing to bounds on the result.

The envelope meets the procedural requirement of Section 2.2—rules that are common knowledge—and by itself no more. Lovett's caution applies: predictability does not end domination if the party who declared the rule can redeclare it at will. An envelope is therefore only as good as the constraint on changing it, which is why it needs the third duty beside it. Firms will object that publishing limits exposes trade secrets and invites gaming. An envelope discloses outputs the firm commits to, not the method that produces them, and a limit that can be gamed only by meeting it is not a harm.

### 5.4 Against the one-sided record: counter-delegation

People who could not read did not, on the whole, protect themselves by becoming scribes. They brought their own: a witness to sign, a second interpreter to check the first. Counter-delegation is the duty to make the modern equivalent possible—to let the person keep her own record of what passed through the intermediary and bring her own reader to it, and to submit disputes to a party the operator does not control.

Others have proposed the technical half. Li and colleagues (2022) outline assistants that would run on a gig worker's side, logging offers and pay and pooling the data across workers. Citron (2008) argued that automated decision systems owe their subjects audit trails. Dubal (2023) reports what happens when workers try to build such records under present law: the data requests help contest individual errors and have not changed the firms' practices.

That result marks the limit of the technical half. A user's software agent is not a notary. In agency law, as Kolt (2025) quotes the Restatement, "At present, computer programs are instrumentalities of the persons who use them": the agent carries its user's interest and no duty to anyone else, and it is itself a new third party whose supplier has interests of its own. The notary's force came from an office with authority over both sides. Counter-delegation therefore has two parts. The operator must permit and not obstruct the user-side record—operators today invoke terms of service against tools that collect it—and a dispute must be decidable against that record by a body that can bind the operator. The Digital Services Act's out-of-court bodies are the nearest existing model, and they lack the binding power (art. 21).

### 5.5 What design cannot do

Two limits. The duties are worth what their enforcement is worth. Mittelstadt (2019) argued that principles alone cannot guarantee ethical AI. Berthon, Pitt, and Campbell (2019) reached the regulatory conclusion for digital addiction: "we argue that public policy solutions are required" (p. 457), because "Consumers on their own struggle to maintain equanimity with regard to their digital experiences" (p. 463). The duties here are duties of the operator, and I expect them to be discharged where a legislature or a regulator makes them so. Some practices may warrant prohibition instead; Dubal (2023) argues as much for individualized pay.

The second limit is the fourth position. Nothing in the three duties touches concentration in the means of the medium, and the paper has not shown that such concentration exists in the form the Stationers' charter gave it. If it does, the remedy lies in competition and regulatory policy, not in the design of any one intermediary.

### 5.6 Three objections

*The users consented.* A driver taps to accept the platform's terms and an applicant clicks to submit; on a liberal view of contract, that settles the matter. The history gives two replies. Consent to a gate one cannot avoid is thin: the Southern voter also "chose" to present himself to the registrar. And consent to terms does not reach the positions. The applicant consents to be assessed. She does not consent to an assessment she cannot question following her to every employer in a sector, and the law of unconscionability already asks whether a party had "a reasonable opportunity to understand the terms" (*Williams v. Walker-Thomas Furniture Co.*, 1965). The republican point is prior to both replies: a person may consent to an arrangement and be dominated within it, as the slave of the kindly master is.

*The law already provides.* Section 4.4 listed what European law now requires, and an objector may say the duties are redundant. They are partly anticipated, which I take as support. The Platform Work Directive's human decision on termination is a fragment of structural refusal; its duty to inform workers about automated systems is a fragment of the envelope. But each provision is confined to a sector or a jurisdiction, each places the first review inside the firm, and none supplies the binding independent party on which counter-delegation depends. The argument here gives those scattered rules a common rationale and says what they still lack.

*The history is ornament.* If domination is the wrong and republican theory supplies the remedy, why detour through 1740 and 1901? Because the history does work that the theory cannot. It shows that the positions are separable—that the examiner, the teacher, and the record-keeper are different offices that can be held and abused independently—where a general charge of platform power runs them together. It shows which remedies worked: the tests ended by statute and the treaties were reread by courts, while better readers changed neither. And it supplies the one thing a purely theoretical argument lacks, a record of safeguards that societies built when they took an intermediary's power seriously, against which the present arrangement can be measured. The duties in this section are the notary's office, the second interpreter, and the suspended test, restated for a third party that is no longer a person.

## 6. Limits

The historical argument rests on cases, and the cases are narrow in three ways. They come chiefly from English-speaking jurisdictions and their empires, with Spanish, Russian, and Indian cases as checks. They are stronger for some practices than others: the gate and the withheld competence are documented with statutes, stated purposes, and contemporary objectors; the record over the voice rests on later courts and one disputed interpreter; the monopoly on one kingdom. And several of the books a historian would expect are known to me through reviews, which I have cited as reviews. I selected the cases by working outward from the four positions—looking for dated acts, stated grounds, and contemporary objectors—and I have reported in Section 3.6 the cases that cut the other way. A historian who began from a sample of literate societies instead of from the positions might weigh the practices differently.

The analogy is bounded by what it compares. It compares positions, and it cannot show intent: nothing here establishes that any operator means to exclude, to keep people ignorant, or to falsify a record, as Knox and Auld said they meant to. Nor does it predict that harms of the earlier scale will recur.

The triad limits the scope of the duties. They are derived for intermediaries that stand between two parties and bind both—hiring vendors, credit bureaus, labor and exchange platforms. Where one party scores another directly, the gate and the record are still present but the third party is not, and the argument about notaries does not transfer without more work. The present-day evidence is likewise limited to hiring, ride-hail, and platform labor. I have not examined search, content moderation, or public administration.

Finally, the normative frame is deliberately thin. Domination describes the positions; internal critique supplies the standard; and I have not argued that the three duties exhaust what non-domination requires. A fuller republican treatment would ask what control by the affected means for a system with millions of users, which is a question about institutions more than about design.

## 7. Conclusion

The passage from speech to writing as the medium of standing was not a steady enlargement of freedom. At each point where a competence became compulsory, a position opened beside it—examiner, teacher, record-keeper, owner of the press—and institutions used those positions over people who could not check them. The remedy that worked was rarely more reading. Legislatures suspended the tests; courts read the oral promise back into the treaty; and where societies took the scribe's power seriously, they put a second person in the room.

Algorithmic intermediaries hold the first three of those positions today, with two differences: the medium adjusts to the person it reads, and the second person is missing at the moment of decision. To tell workers, borrowers, and applicants that their protection lies in AI literacy is to offer the fifth practice as the cure for the other four. The duties argued for here—a route around the gate, limits declared in advance, and a record and a reader of one's own with an independent party to hear the dispute—ask the operator of the intermediary to accept what the notary's office once imposed on the scribe. They leave open the question with which any account of mediation should end: who checks the third party, and who appoints the checker.

## References

Alabama Constitutional Convention. (1901). *Official proceedings of the Constitutional Convention of the State of Alabama, May 21st, 1901, to September 3rd, 1901* (Vol. 1). Address of John B. Knox, pp. 7–12.

Almeida Cabrejas, B. (2019). "No firmó porque dijo no saber": Alfabetizados y analfabetos en documentos notariales de CODEA de los siglos XVI y XVII. *Philologia Hispalensis, 33*(1), 21–41. https://doi.org/10.12795/ph.2019.v33.i01.02

Andrien, K. J. (2012). [Review of the book *Into the archive: Writing and power in colonial Peru*, by K. Burns]. *Journal of Interdisciplinary History, 43*(1), 144–145.

Arber, E. (Ed.). (1875). *A transcript of the registers of the Company of Stationers of London, 1554–1640 A.D.* (Vol. 1). Privately printed.

Bakos, Y., Marotta-Wurgler, F., & Trossen, D. R. (2009). *Does anyone read the fine print? Testing a law and economics approach to standard form contracts* (Working Paper No. 09-04). NET Institute.

Balkin, J. M. (2016). Information fiduciaries and the First Amendment. *U.C. Davis Law Review, 49*, 1183–1234.

Ben-Shahar, O., & Schneider, C. E. (2011). The failure of mandated disclosure. *University of Pennsylvania Law Review, 159*, 647–749.

Berthon, P., Pitt, L., & Campbell, C. (2019). Addictive de-vices: A public policy analysis of sources and solutions to digital addiction. *Journal of Public Policy & Marketing, 38*(4), 451–468. https://doi.org/10.1177/0743915619859852

Bommasani, R., Bana, S. H., Creel, K. A., Jurafsky, D., & Liang, P. (2026). Algorithmic monocultures in hiring. In *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency* (pp. 6351–6382). ACM. https://doi.org/10.1145/3805689.3812400

Brandt, D. (1998). Sponsors of literacy. *College Composition and Communication, 49*(2), 165–185.

Butterfield, H. (1931). *The Whig interpretation of history*. G. Bell and Sons.

Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures consent through constant and confined choices. *Administrative Science Quarterly, 69*(2), 458–514. https://doi.org/10.1177/00018392241236163

Citron, D. K. (2008). Technological due process. *Washington University Law Review, 85*(6), 1249–1313.

Cleveland, G. (1897, March 2). *Veto message* [on a bill to amend the immigration laws]. The American Presidency Project.

*Delgamuukw v. British Columbia*, [1997] 3 S.C.R. 1010 (Supreme Court of Canada).

Directive (EU) 2024/2831 of the European Parliament and of the Council of 23 October 2024 on improving working conditions in platform work. *Official Journal of the European Union*, L, 11.11.2024.

Douglass, F. (1845). *Narrative of the life of Frederick Douglass, an American slave. Written by himself*. Anti-Slavery Office.

Douglass, M. (1854). *Educational laws of Virginia: The personal narrative of Mrs. Margaret Douglass, a Southern woman, who was imprisoned for one month in the common jail of Norfolk, under the laws of Virginia, for the crime of teaching free colored children to read*. John P. Jewett.

Dubal, V. (2023). On algorithmic wage discrimination. *Columbia Law Review, 123*(7), 1929–1992.

Edwards, L., & Veale, M. (2017). Slave to the algorithm? Why a "right to an explanation" is probably not the remedy you are looking for. *Duke Law & Technology Review, 16*(1), 18–84.

Engerman, S. L., & Sokoloff, K. L. (2001). *The evolution of suffrage institutions in the New World* (Working Paper No. 8512). National Bureau of Economic Research. https://doi.org/10.3386/w8512

*Foster v. Mackinnon* (1869) L.R. 4 C.P. 704.

*Gaston County v. United States*, 395 U.S. 285 (1969).

Giesler, M., & Veresiu, E. (2014). Creating the responsible consumer: Moralistic governance regimes and consumer subjectivity. *Journal of Consumer Research, 41*(3), 840–857. https://doi.org/10.1086/677842

Graff, H. J. (1979). *The literacy myth: Literacy and social structure in the nineteenth-century city*. Academic Press.

Hagedorn, N. L. (1988). "A friend to go between them": The interpreter as cultural broker during Anglo-Iroquois councils, 1740–70. *Ethnohistory, 35*(1), 60–80. https://doi.org/10.2307/482433

*Hill v. Gateway 2000, Inc.*, 105 F.3d 1147 (7th Cir. 1997).

Hirschman, A. O. (1970). *Exit, voice, and loyalty: Responses to decline in firms, organizations, and states*. Harvard University Press.

Hoeksema, B. (2023). Digital domination and the promise of radical republicanism. *Philosophy & Technology, 36*(1). https://doi.org/10.1007/s13347-023-00618-7

Holmes, W. F. (1975). [Review of the book *The shaping of Southern politics: Suffrage restriction and the establishment of the one-party South, 1880–1910*, by J. M. Kousser]. *Journal of Southern History, 41*(2), 270–272. https://doi.org/10.2307/2206040

Immigration Restriction Act 1901 (Cth), No. 17 of 1901 (Australia).

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence, 1*(9), 389–399.

Johansson, E. (1985). Popular literacy in Scandinavia about 1600–1900. *Historical Social Research, 10*(2), 60–64. https://doi.org/10.12759/hsr.10.1985.2.60-64

Kamperman, S., & Graff, H. J. (2026). On "AI literacy": The rhetorical and historical fallacies of a movement and its marketing. *Change: The Magazine of Higher Learning, 58*(4), 34–39. https://doi.org/10.1080/00091383.2026.2706429

Khan, L. M., & Pozen, D. E. (2019). A skeptical view of information fiduciaries. *Harvard Law Review, 133*, 497–541.

Kim, T. W., & Routledge, B. R. (2022). Why a right to an explanation of algorithmic decision-making should exist: A trust-based approach. *Business Ethics Quarterly, 32*(1), 75–102.

Kolt, N. (2025). Governing AI agents. *Notre Dame Law Review, 101*.

Lake, M. (2006). From Mississippi to Melbourne via Natal: The invention of the literacy test as a technology of racial exclusion. In A. Curthoys & M. Lake (Eds.), *Connected worlds: History in transnational perspective* (ch. 13). ANU Press.

Leonard, I. A. (1992). *Books of the brave: Being an account of books and of men in the Spanish conquest and settlement of the sixteenth-century New World*. University of California Press.

Li, T. J.-J., Lu, Y., Clark, J., Chen, M., Cox, V., Jiang, M., Yang, Y., Kay, T., Wood, D., & Brockman, J. (2022). A bottom-up end-user intelligent assistant approach to empower gig workers against AI inequality. In *2022 Symposium on Human-Computer Interaction for Work* (pp. 1–10). ACM. https://doi.org/10.1145/3533406.3533418

Lovett, F. (2026). Republicanism. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. https://plato.stanford.edu/entries/republicanism/

Margo, R. A. (2005). [Review of the book *Self-taught: African American education in slavery and freedom*, by H. A. Williams]. *Journal of Economic History, 65*(2), 590–591.

Messick, B. (1993). *The calligraphic state: Textual domination and history in a Muslim society*. University of California Press.

Milton, J. (1644). *Areopagitica: A speech for the liberty of unlicensed printing*.

Mittelstadt, B. (2019). Principles alone cannot guarantee ethical AI. *Nature Machine Intelligence, 1*(11), 501–507. https://doi.org/10.1038/s42256-019-0114-4

Moody-Adams, M. M. (1994). Culture, responsibility, and affected ignorance. *Ethics, 104*(2), 291–309.

Moser, M. (2017). Introduction. *East/West: Journal of Ukrainian Studies, 4*(2), 3–7. https://doi.org/10.21226/T2DK9B

Muldoon, J., & Raekstad, P. (2023). Algorithmic domination in the gig economy. *European Journal of Political Theory, 22*(4), 587–607. https://doi.org/10.1177/14748851221082078

Newland, B. (2022). *Federal Indian Boarding School Initiative investigative report* (Vol. 1). U.S. Department of the Interior.

Pettit, P. (1997). *Republicanism: A theory of freedom and government*. Oxford University Press.

Phule, J. (1882). Memorial addressed to the Education Commission. In *Education Commission, Bombay* (Vol. 2, pp. 140–145). Calcutta, 1884.

*R. v. Marshall*, [1999] 3 S.C.R. 456 (Supreme Court of Canada).

Rahman, H. A. (2021). The invisible cage: Workers' reactivity to opaque algorithmic evaluations. *Administrative Science Quarterly, 66*(4), 945–988. https://doi.org/10.1177/00018392211010118

Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (General Data Protection Regulation). *Official Journal of the European Union*, L 119, 4.5.2016.

Regulation (EU) 2019/1150 of the European Parliament and of the Council of 20 June 2019 on promoting fairness and transparency for business users of online intermediation services. *Official Journal of the European Union*, L 186, 11.7.2019.

Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 (Digital Services Act). *Official Journal of the European Union*, L 277, 27.10.2022.

Rosenblat, A., & Stark, L. (2016). Algorithmic labor and information asymmetries: A case study of Uber's drivers. *International Journal of Communication, 10*, 3758–3784.

Simmel, G. (1950). *The sociology of Georg Simmel* (K. H. Wolff, Ed. & Trans.). Free Press.

*South Carolina v. Katzenbach*, 383 U.S. 301 (1966).

Street, B. V. (2003). What's "new" in New Literacy Studies? Critical approaches to literacy in theory and practice. *Current Issues in Comparative Education, 5*(2), 77–91.

Truth and Reconciliation Commission of Canada. (2015). *Honouring the truth, reconciling for the future: Summary of the final report of the Truth and Reconciliation Commission of Canada*.

UNESCO. (2015). *Education for All 2000–2015: Achievements and challenges. EFA Global Monitoring Report 2015* (Summary).

UNESCO Institute for Statistics. (2026). *Adult illiterate population and adult literacy rate, 15+ years* (February 2026 data release) [Data set].

Union Internationale du Notariat. (2004). *Principles of notarial ethics*.

Union Internationale du Notariat. (2005). *Principles of the notarial function*.

Vee, A. (2013). Understanding computer programming as a literacy. *Literacy in Composition Studies, 1*(2), 42–64. https://doi.org/10.21623/1.1.2.4

Waitangi Tribunal. (2014). *He Whakaputanga me te Tiriti / The Declaration and the Treaty: The report on stage 1 of the Te Paparahi o Te Raki inquiry* (Wai 1040). Legislation Direct.

Walzer, M. (1988). Interpretation and social criticism. In S. M. McMurrin (Ed.), *The Tanner lectures on human values* (Vol. 8, pp. 1–80). University of Utah Press.

Washington, B. T. (1901). *Up from slavery: An autobiography*. Doubleday, Page.

*Williams v. Walker-Thomas Furniture Co.*, 350 F.2d 445 (D.C. Cir. 1965).

Williams, J. (2018). *Stand out of our light: Freedom and resistance in the attention economy*. Cambridge University Press. https://doi.org/10.1017/9781108453004

Wilson, W. (1917, January 29). *Message to the House of Representatives returning without approval "An act to regulate the immigration of aliens to, and the residence of aliens in, the United States"*. The American Presidency Project.

World Conference on Education for All. (1990). *World declaration on education for all and framework for action to meet basic learning needs*. Inter-Agency Commission.

World Education Forum. (2000). *The Dakar framework for action. Education for all: Meeting our collective commitments*. UNESCO.

Yeung, K. (2016). "Hypernudge": Big Data as a mode of regulation by design. *Information, Communication & Society, 20*(1), 118–136. https://doi.org/10.1080/1369118X.2016.1186713

Young, I. M. (2006). Responsibility and global justice: A social connection model. *Social Philosophy and Policy, 23*(1), 102–130. https://doi.org/10.1017/S0265052506060043

Zong, J., & Matias, J. N. (2024). Data refusal from below: A framework for understanding, evaluating, and envisioning refusal as design. *ACM Journal on Responsible Computing, 1*(1), 1–23. https://doi.org/10.1145/3630107
