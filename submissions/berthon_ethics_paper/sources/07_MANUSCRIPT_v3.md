<!-- Version 2 of the manuscript. Drafted by Claude on 2026-10-13 on the author's instruction ("full rewrite but maintain the writing style"; target: Business Ethics Quarterly, 12,000 words). It reworks the author's second draft (AUTHOR_DRAFT_v2.md) in light of the six reviews in review/. Where the author's sentences were sound they are kept; everything else is Claude's and is the author's only once he has revised it. Notes for the author are in MANUSCRIPT_v2_NOTES.md. -->

# Algorithmacy: Institutional Domination, Triadic Mediation, and the Limits of Literacy in Algorithmic Governance

## Abstract

AI-ethics frameworks routinely prescribe "AI literacy" and explanation as the main safeguards against algorithmic harm. Yet when reading and writing became conditions of civic and legal standing, the deepest injuries did not arise from an uneducated public. Institutions that held the test, the access, and the record inflicted them. This paper reads the history of that transition to theorize algorithmacy—the relational competence demanded when two human parties coordinate through an algorithmic intermediary that reads both and commits an outcome binding on both. Using internal critique, I identify five things institutions did with literacy: they gated standing on a discretionary test, withheld the competence by law, let a written record override what was said, enclosed the means of print, and oversold literacy's returns. I describe the positions those institutions held with the republican concept of domination, and I argue that algorithmic intermediaries now hold the same positions. Two differences sharpen the problem. The intermediary adapts to the person it reads, and no independent party with binding authority stands at the point of decision, as notaries once stood beside human scribes. <!-- v3: P1-002 AUTHOR --> From the argument I derive three duties for the operators of algorithmic intermediaries: structural refusal, declared operating envelopes, and counter-delegation.

**Keywords:** algorithmic management; AI literacy; domination; internal critique; platforms; history of literacy

## 1. Introduction

People now reach credit, work, and civic standing through algorithmic systems that read their behavior and commit binding decisions (Citron, 2008, p. 1252; Directive (EU) 2023/2225, recital 56). <!-- v3: P1-004 --> Most published guidelines on the ethics of these systems name a duty to do no harm. <!-- v3: P1-005 --> Jobin, Ienca, and Vayena (2019) reviewed 84 sets of AI-ethics guidelines and found non-maleficence named in 60 and beneficence in 41. In business ethics and in regulation, a prominent remedy derived from that duty is to inform the affected person—to mandate disclosure, to ground a right to an explanation (Kim & Routledge, 2022), and to train the user under the banner of "AI literacy." <!-- v3: P1-008 --> The remedy has a known limit. Edwards and Veale (2017, p. 67) call reliance on individual rights to explanation a "transparency fallacy," because "Individual data subjects are not empowered to make use of the kind of algorithmic explanations they are likely to be offered." Berthon, Pitt, and Campbell (2019, p. 457) report of digital addiction that "information is necessary, but not sufficient to change behavior." Williams (2018, p. 101) writes of the attention economy that education is necessary and not sufficient, "Nor will 'media literacy' alone lead us out of this forest." Kamperman and Graff (2026, p. 36) look to the history of reading for the reason: the AI-literacy movement repeats the myth that "Literacy is a certain or guaranteed path to economic security." The comparison between learning to read and learning to program (Vee, 2013) or to use AI (Kamperman & Graff, 2026) is therefore already on the table. <!-- v3: P1-018 --> Those who have drawn it center the skill and its returns: Vee sees power shifting toward the skilled, and Kamperman and Graff, who name the technology companies behind the movement (pp. 35–36), find the returns oversold. Neither asks what is owed by whoever holds the test, the access, or the record. <!-- v3: P1-019 FC AUTHOR -->

Overselling, however, was the smallest part of what went wrong when reading became a condition of legal and civic standing. The actors who held the test, the access, and the record committed the deeper wrongs, and they committed them with literacy. When Alabama's constitutional convention met in 1901 to write a literacy test into the franchise, its president told the delegates what they had gathered to do: "within the limits imposed by the Federal Constitution, to establish white supremacy in this State" (Alabama Constitutional Convention, 1901/1940, p. 8). <!-- v3: ASM-2 AUTHOR --> Decades earlier, Hugh Auld forbade his wife to teach Frederick Douglass to read because learning would "forever unfit him to be a slave" (Douglass, 1845, p. 33). And when the Supreme Court of Canada decided in 1999 what a Mi'kmaq treaty of 1760 had promised, it observed of such treaties that "The Indian parties did not, for all practical purposes, have the opportunity to create their own written record of the negotiations" (*R. v. Marshall*, 1999, para. 14). None of these injuries was an educational deficit or a broken promise. Each was the use of a position that opened once a competence became compulsory—the examiner's, the teacher's, the record-keeper's.

That history matters because the positions are occupied again. When a job applicant and an employer, a borrower and a lender, or a driver and a rider deal with each other through a platform, two human parties coordinate through an automated third party that reads both and enforces an outcome binding on both. I call the competence this arrangement demands algorithmacy. The intermediary holds the test: where employers share a screening vendor, 4% of applicants who apply to ten positions are recommended for rejection from all ten (Bommasani et al., 2026). It controls access to the competence: a ride-hail driver has "about 15 seconds" to accept a trip and is "not shown destination or fare information" beforehand (Rosenblat & Stark, 2016, p. 3762). And it keeps the record—Uber claims its data are "akin to an objective, third-party witness," so that "its interpretation should be conclusive" (Rosenblat & Stark, 2016, p. 3765)—and drivers who inquire "usually receive template responses" (Rosenblat & Stark, 2016, p. 3771). <!-- v3: P1-031; P1-032 AUTHOR --> If the lesson of the literacy transition were that reformers oversold reading, better training and clearer explanations would answer it. If the wrongs lay with whoever held the test, the access, and the record, an ethics that educates the user addresses the wrong party.

I therefore read the record of the literacy transition for what named institutions—legislatures, courts, churches, and a chartered company—did with written competence once standing depended on it. I judge those practices by internal critique: a practice counts as an ethical failure when contemporaries condemned it, when the institution broke a standard it professed, or when the outcome fell short of what its sponsors promised. Five practices meet that test: gating standing on a discretionary reading test, withholding the competence by law, letting a written record override what was said, enclosing the means of print by charter, and promoting individual literacy as the cure for a structural condition. I treat this history as evidence about institutions and its algorithmic counterpart as a bounded analogy, and for each practice I name the property the analogy rests on and the point at which it gives way.

The paper makes three contributions to normative business ethics. First, it replaces the diffuse charge that "society" failed to spread literacy with five documented practices and their actors, and it reserves a collective charge for the international campaigns that set targets and missed them. Second, it moves the analogy between literacy and algorithmic mediation from the user's skill to the positions around the medium, which is where four of the five failures lie and where earlier critiques of AI literacy do not reach (Kamperman & Graff, 2026). <!-- v3: P1-035 --> Third, it identifies what differs this time—the intermediary adapts to the person it reads, and no independent party with binding authority checks it at the point of decision—and it derives from that difference three duties for the operators of algorithmic intermediaries.

The argument runs in four steps. Section 2 defines the relation, describes the positions with the republican concept of domination, and states the standard by which I judge them. Section 3 documents the five practices and what the record does not show. Section 4 maps the positions onto algorithmic intermediaries and marks the two points where the analogy gives way. Section 5 derives the duties and answers three objections; Section 6 states the limits of the evidence.

## 2. Framework: A Relation, a Position, and a Standard

### 2.1 Algorithmacy as a relation among three parties

Policy talk about AI pictures a person and a machine: a user prompts a model, an applicant submits a form, and the software answers. The picture leaves someone out. Most consequential algorithmic systems stand between people who need something from each other, and I use *algorithmacy* for the competence that standing-between demands: the capacity to coordinate with another person through an automated third party that reads both and commits an outcome binding on both. A screening vendor stands between an applicant and an employer. A credit bureau's score stands between a borrower and a lender. A ride-hail platform stands between a driver and a rider. Not every algorithmic encounter has this shape—a lender that scores its own applicants, or a platform that moderates its own users' posts, is one party judging another—and I confine the term to cases that do.

Simmel gave the sociology of this shape. The third element in a triad may be an impartial mediator who wishes "to save the group unity from the danger of splitting up," or it may be the third who profits: "the non-partisan may also use his relatively superior position for purely egoistic interests" (Simmel, 1950, p. 154). Which of these a given intermediary is depends on who pays it and whose instructions it carries. Many platforms occupy both of Simmel's roles and a further one: the ride-hail firm presents itself as the neutral matcher of driver and rider (Rosenblat & Stark, 2016, p. 3761), earns a commission on its matches (*Uber BV v Aslam*, 2021, [11]), <!-- v3: FC2-14 --> and is also the driver's contractual counterparty (*Uber BV v Aslam*, 2021, [52]). <!-- v3: P2-004; P2-005; P2-006 --> Section 4 returns to that doubling, because the law has historically treated the neutral third and the interested counterparty under different rules.

The word invites two objections, and the triad answers both. Kamperman and Graff (2026, p. 35) fault AI-literacy initiatives that "use literacy uncritically as a metaphor." Street's critique of what he called the autonomous model of literacy cuts deeper: the model assumes that introducing literacy "will have the effect of enhancing their cognitive skills, improving their economic prospects, making them better citizens, regardless of the social and economic conditions that accounted for their 'illiteracy' in the first place" (Street, 2003, p. 77). A term ending in "-acy" can smuggle that assumption back in. I do not claim that dealing with an algorithm is a kind of reading, or that mediation alters cognition. Algorithmacy names a relation among three parties, and the comparison with literacy that follows is a comparison of the positions that open around a competence once institutions make it compulsory.

Literacy scholars have a concept close to those positions. Brandt (1998, p. 166) defined the sponsors of literacy as agents "who enable, support, teach, model, as well as recruit, regulate, suppress, or withhold literacy—and gain advantage by it in some way." <!-- v3: P2-013 --> Her sponsor stands between a learner and literacy. The intermediary I describe stands between two people and an outcome: it need not teach or withhold anything to hold the test that sorts them and the record that binds them. Brandt's concept explains who profits from a competence. The triad adds who decides between its holders.

A near precedent for the comparison itself is Vee (2013), who sets programming beside the history of mass literacy and concludes that as more of social life is conducted through code, "the power balance is once again shifting toward those who are skilled in this new literacy technology" (p. 55). <!-- v3: P2-017 --> I read the same history to a different conclusion. In the cases below, power went less to the skilled than to whoever examined, taught, and recorded them, and the skilled were often people like Douglass, who had the competence and none of the sanctioned positions. <!-- v3: P2-018 AUTHOR -->

### 2.2 Domination as the description of a position

The positions need a description that does not depend on anyone's bad intent. Republican political theory supplies one. On Pettit's account, a person is free to the extent that no one has "the capacity to interfere in their affairs on an arbitrary basis" (Pettit, 1999, p. 165, as quoted in Lovett, 2026); domination is the standing capacity, whether or not anyone exercises it, which is why the slave of a kindly master remains unfree. <!-- v3: P2-019 --> The registrar who chooses the passage an applicant must read and alone judges the answer holds that capacity over the applicant. So does the party that drafts the only record of an agreement the other party cannot read.

Three clarifications keep the concept honest. First, I use domination to describe positions, not to condemn them. Lovett (2026) notes that republicans define arbitrary power procedurally or democratically, and on either view as uncontrolled power, not as unjust power, so that calling a position dominating leaves open whether a given exercise of it was wrong. <!-- v3: P2-021 --> Section 2.3 supplies the standard of wrongness. Second, the concept does not require that the holder be unconstrained in every respect. Statutes, contracts, and competition limit what a platform may do, as constitutions limited what a registrar might do; the question in each case is whether the affected person can know the rule in advance and contest its application to an independent party. Third, the concept has already reached the workplace and the platform. Muldoon and Raekstad (2023) apply it to ride-hail and delivery work, where information asymmetries decrease "workers' ability both to understand and contest the decisions that are made over them" (p. 596) and "Workers have had their accounts deleted by an algorithm without warning and with no right to contest the decision" (p. 599). They locate the dominating agent in owners and managers. I follow them in holding the operator responsible, and I extend their treatment of the second party, whom they already count among the worker's dominators (p. 598): the intermediary's reading binds the rider, the employer, or the lender as well, and neither flank can check it. <!-- v3: P2-N04 AUTHOR -->

Republican theory also says what removes arbitrariness, and the answer shapes Section 5. On the procedural view, Lovett's own, power is non-arbitrary when it follows rules that are common knowledge; on the democratic view, which Lovett illustrates from Pettit (2012, pp. 57–58, as cited in Lovett, 2026), when those subject to it control it (Lovett, 2026). <!-- v3: P2-N06 FC AUTHOR --> Coping is not enough: "Just because one is better able to cope with arbitrary power, it does not follow that one's domination is any less" (Lovett, 2026). A person who has learned to predict a system that can change its rules at will has gained skill and no standing.

### 2.3 The standard: internal critique, applied to both periods

By what standard did the institutions of the literacy transition fail? Importing a present-day theory to condemn 1740 or 1901 invites the charge Butterfield (1931) made against history written as the ratification of the present. I use a narrower instrument. Walzer (1988) describes social criticism as "an internal argument," conducted by a critic who belongs to the society he criticizes, and one of the two worries he answers is whether "standards [are] available to him that are internal to the practices and understandings of his own society, and at the same time properly critical" (p. 34); he observes that "The same men and women who act badly create and sustain the standards by which (at least sometimes) they know themselves to act badly" (p. 42). <!-- v3: P2-031 FC AUTHOR --> From that method I draw three benchmarks. They are mine, built on his premise. A practice counts as an ethical failure if (1) contemporaries condemned it in the moral vocabulary of their time, (2) the institution broke a standard it publicly professed, or (3) the outcome fell systematically short of what its sponsors promised.

Two points about this choice. The benchmarks apply to both periods: Section 5 judges platform operators by the standards they profess, the objections their contemporaries raise, and the promises made on their behalf, and it uses nothing else. And the choice is a discipline I adopt, not a constraint that the avoidance of anachronism forces. Moody-Adams (1994) argues that the "standards of their own day" defence rests on a mistake: theories that excuse past wrongdoers "base hypotheses about what some agent(s) could not do solely on evidence of what the agent(s) did not do" (p. 294), when the ignorance in question was often affected—"choosing not to know what one can and should know" (p. 296). I infer from her argument that a present-day standard would not be unfair. <!-- v3: P2-038 --> I keep to internal benchmarks because they are sufficient for four of the five practices and because they make the fifth case's weakness visible: for the record over the voice, contemporary objection is thin, and I say so in Section 3.3.

Moody-Adams also bears on who failed. "A culture—independent of agents who perpetuate culture—cannot be an 'agent' of anything," she writes (p. 304). <!-- v3: P2-039 FC --> The practices below are the acts of legislatures, courts, a chartered company, and conference sponsors, and I name them.

### 2.4 What the charge is not

The charge is against what institutions did with literacy, never against literacy. People sought it at cost. Johansson (1985, p. 64) describes a Lutheran church program in Scandinavia that declared reading "everybody's calling and right" and often enforced it by compulsion and church discipline; Washington (1901, p. 30) remembered "a whole race trying to go to school" after emancipation. <!-- v3: P2-041 FC AUTHOR --> Graff, the historian who named the literacy myth, wrote that "Literacy did carry certain benefits" (Graff, 1979/1991, p. 19). <!-- v3: ASM-1 --> <!-- v3: P2-045 --> The same holds for the algorithmic case: nothing here denies that people gain from understanding the systems that sort them. The argument concerns what the holders of three positions may do while people learn.

## 3. Five Things Done with Literacy

The five practices below share a structure. In each, an institution held a position that literacy's new importance had created, and used it over people who could not check the use. For each I give what was done, by whom, on what stated ground, who objected, and what ended it. Table 1 in Section 4 sets the five beside their present-day counterparts.

### 3.1 The gate

The plainest practice is the reading test as a gate: an examination neutral on its face, administered at an official's discretion, to exclude a targeted group from standing. The voter literacy tests of the American South after Reconstruction are the best documented.

The Fifteenth Amendment barred denial of the vote on account of race, so Southern conventions built facially neutral barriers (*South Carolina v. Katzenbach*, 1966, at 310–311). <!-- v3: P3-001 --> John B. Knox, presiding over Alabama's convention in 1901, stated the purpose in his opening address: "And what is it that we want to do? Why it is within the limits imposed by the Federal Constitution, to establish white supremacy in this State" (Alabama Constitutional Convention, 1901/1940, p. 8). <!-- v3: ASM-2 AUTHOR --> The device worked through discretion. The Supreme Court later described how registrars in Alabama, Louisiana and Mississippi applied the tests, giving white applicants easy versions or help and Black applicants difficult ones without help (*South Carolina v. Katzenbach*, 1966, at 312). <!-- v3: P3-004; P3-N01 --> The Court's footnotes give the texture. In Louisiana a white applicant "satisfied the registrar of his ability to interpret the state constitution by writing, 'FRDUM FOOF SPETGH'"; in Panola County, Mississippi, "the registrar required Negroes to interpret the provision of the state constitution concerning 'the rate of interest on the fund known as the "Chickasaw School Fund"'" (at 312, nn. 12–13). The test measured the examiner's wishes. Knox himself recorded the objection. Reviewing Mississippi's rule that a voter must "understand" a constitutional clause when read, he observed that the decision "is exclusively in the hands of the registrars," and conceded that "the objection has been urged with force that it perpetuates the very form of abuse which we are seeking to escape" (Alabama Constitutional Convention, 1901/1940, p. 11) <!-- v3: ASM-2 AUTHOR -->—and he answered it in the name of "the purity of the ballot," not of the voters the test would exclude. <!-- v3: P3-008 FC AUTHOR -->

The second benchmark applies as well as the first. The states that tested for reading had run the schools. In *Gaston County v. United States* (1969, at 293), the Court refused to let a county reinstate a literacy test after it had maintained "separate and inferior schools" for its Black residents. <!-- v3: P3-009 --> The effect of the Southern restrictions as a whole, of which the test was one part, was large: a reviewer reports Kousser's finding that turnout fell from 64 percent of eligible voters in the 1880s to 30 percent in the first decade of the new century, that the laws themselves cut turnout by an average of 37 percent, and that black-belt Democrats "wanted to eliminate the voting of poor whites as well as blacks" while "Populists, Republicans, and blacks consistently opposed the new laws" (Holmes, 1975, pp. 270–271). <!-- v3: P3-N02 AUTHOR -->

The device traveled. Natal's Immigration Restriction Act of 1897 required a migrant to write in a European language (Natal Act No. 1, 1897, as described in Keith, 1912, vol. 2, p. 1082), and the colony's Premier explained why Natal had to "go one step further than the American Bill": the people he meant to exclude were "perfectly well able to read and write in their own language" (quoted in Lake, 2006, p. 221). <!-- v3: P3-071; P3-013; P3-069 --> Australia's Immigration Restriction Act of 1901 followed Natal's, excluding anyone who "fails to write out at dictation and sign in the presence of the officer a passage of fifty words in length in an European language directed by the officer" (s. 3(a)); the test remained in law until 1959 (Migration Act 1958, s. 4 and Schedule; in force 1 June 1959). <!-- v3: P3-016 --> Natal and Australia show a feature the Southern tests share: whoever chooses the language and the passage holds the gate, though the United States' Immigration Act of 1917 let the migrant choose the language, if not the passage (s. 3, 39 Stat. 877). <!-- v3: FC2-17 AUTHOR --> In Latin America the literacy rule came earlier and, in several republics, lasted longer. <!-- v3: P3-018 --> Engerman and Sokoloff (2001, pp. 22–23) find literacy requirements in the early constitutions of most of the new republics; Brazil's Saraiva Law of 1881 made reading and writing a condition of new enrolment from 1882 (Decreto n. 3.029, 1881, art. 8), and Brazil kept illiterate citizens off the rolls until 1985 (Emenda Constitucional n. 25, 1985; Aleixo & Kramer, 2010, p. 68), although Engerman and Sokoloff date the constitutional rule to 1891 and its end to 1988, the year the new Constitution confirmed the change. <!-- v3: P3-017; P3-019; P3-020; P3-N07 FC AUTHOR -->

Contemporaries named the wrong. When Congress passed a literacy test for immigrants in 1897, President Cleveland vetoed it: "It is said, however, that the quality of recent immigration is undesirable. The time is quite within recent memory when the same thing was said of immigrants who, with their descendants, are now numbered among our best citizens" (Cleveland, 1897). He called the ability to read and write "a misleading test of contented industry" (para. 13). <!-- v3: P3-N03 AUTHOR --> President Wilson vetoed the same device in 1917 because it "is not a test of character, of quality, or of personal fitness, but would operate in most cases merely as a penalty for lack of opportunity in the country from which the alien seeking admission came" (Wilson, 1917). Congress enacted it over his veto (Immigration Act of 1917, 39 Stat. 874). <!-- v3: P3-024 --> The voting tests ended when the Voting Rights Act of 1965 suspended them where its formula applied (79 Stat. 437, s. 4) and the 1970 amendments suspended them nationwide until 1975 (s. 6, 84 Stat. 314, 315). <!-- v3: P3-025; P3-026 --> <!-- v3: FC2-13 --> No one ended them by learning to read better.

### 3.2 The withheld competence

Where keeping people incompetent kept them governable, institutions forbade the teaching (see *South Carolina v. Katzenbach*, 1966, at 311 n. 10). <!-- v3: P3-N04 AUTHOR --> South Carolina's Negro Act of 1740 fined anyone who taught an enslaved person to write (South Carolina, 1740/1840, s. 45, p. 413). <!-- v3: ASM-4 FC --> <!-- v3: P3-071 --> Between 1829 and 1834 Georgia, Virginia, Alabama, and North Carolina passed acts of their own (General Assembly of Georgia, 1830, s. 11; General Assembly of Virginia, 1831, ch. XXXIX; General Assembly of Alabama, 1832, s. 10; General Assembly of North Carolina, 1831); two of them are narrower than their usual summary, and Virginia's of April 1831, for instance, barred assemblies of free Black people for instruction and the paid teaching of slaves. <!-- v3: ASM-3 --> <!-- v3: P3-071; P3-029 FC --> A reviewer of Williams's history of Black education gives the legislators' ground in a phrase: "Fearing insurrection, southern state legislatures made it a crime for persons to instruct slaves or free blacks to read and write" (Margo, 2005, p. 590).

The fullest statement of the rationale is a slaveholder's, as Douglass reports it. Hugh Auld "at once forbade Mrs. Auld to instruct me further, telling her, among other things, that it was unlawful, as well as unsafe, to teach a slave to read"; learning, Auld said, "would forever unfit him to be a slave. He would at once become unmanageable, and of no value to his master" (Douglass, 1845, p. 33). Douglass learned anyway, from white boys he "converted into teachers" (p. 38), and recorded what the competence was worth inside a closed system: "It had given me a view of my wretched condition, without the remedy. It opened my eyes to the horrible pit, but to no ladder upon which to get out" (Douglass, 1845, p. 40, ch. VII). <!-- v3: P3-N05; P3-034 --> I return to that sentence in Section 4, because it is the earliest statement I know of a point the algorithmic literature has rediscovered: comprehension is not leverage.

Objection at the time is on the record. Margaret Douglass, a white woman prosecuted in Norfolk in 1853 for teaching free Black children to read, told the court that she would be "a single sufferer under the operation of one of the most inhuman and unjust laws that ever disgraced the statute book of a civilized community" (M. Douglass, 1854, p. 36). She served a month in jail.

The practice was not American only, though elsewhere it attached to reading matter and language more often than to the alphabet. In 1531 the Queen of Spain instructed the House of Trade to stop "books of fiction in the vernacular" from going to the Indies, "since this is bad practice for the Indians and something with which it is not well for them to be concerned or read" (quoted in Leonard, 1949/1992, pp. 81–84); the order was repeated in 1536 and 1543. <!-- v3: R13 FC --> In the Russian Empire the Valuev circular of 1863 halted religious and educational publishing in Ukrainian on the ground that "a [distinct] Little Russian ... language did not, does not and cannot exist," and the Ems decree of 1876 tightened the ban until 1905 (Moser, 2017, p. 3). In the Bombay Presidency of British India the exclusion ran through custom that the state's schools tolerated. <!-- v3: P3-046 --> Jotirao Phule told the Education Commission in 1882 that "The Mahars, Mangs, and other lower classes are practically excluded from all schools owing to caste prejudices," and he appealed to the Queen's Proclamation for separate schools (Phule, 1882, p. 142)—an objection by a contemporary, invoking the ruler's own professed standard. <!-- v3: P3-044 -->

Two limits apply. No source I have read measures what the American statutes achieved, and the reviewer of Williams notes that she does not test whether they kept free Black people from learning (Margo, 2005, p. 591). <!-- v3: P3-047 --> And several of these bans leaked: the Spanish orders were repeated because they were not obeyed (Leonard, 1949/1992, pp. 81–83). <!-- v3: P3-048; R13 FC --> The failure I record is the order and its stated ground.

### 3.3 The record over the voice

The third practice arose where an agreement was made by speech and proved by writing. The party that wrote the record bound the party that could not make its own.

That writing should outrank speech is a legal choice, not a property of writing. In the shari'a courts of highland Yemen that Messick studied, "the manuals discuss witnessing support for documents, but they do not consider documents to be potential evidence" (Messick, 1993, pp. 209–210): doctrine put oral testimony first, even as practice relied on documents. <!-- v3: P3-050 --> Where the common law chose the document, the consequences fell on those who had no documents of their own. Deciding in 1999 whether a Mi'kmaq man could rely on promises made in treaty talks of 1760, the Supreme Court of Canada held that "the Nova Scotia judgments erred in concluding that the only enforceable treaty obligations were those set out in the written document of March 10, 1760" (*R. v. Marshall*, 1999, para. 40), having observed that the Indigenous parties to such treaties had no practical opportunity to create their own written record (para. 14). Two years earlier the Court had warned that under a trial judge's approach, "the oral histories of aboriginal peoples would be consistently and systematically undervalued by the Canadian legal system" (*Delgamuukw v. British Columbia*, 1997, para. 98).

The Treaty of Waitangi shows the third party at work. In February 1840 William Hobson negotiated for the Crown with Māori rangatira through the missionary Henry Williams, who had made the Māori text and interpreted "sentence by sentence" (Waitangi Tribunal, 2014, p. 355). More than 500 rangatira eventually signed; 39 signed the English text (p. 386). The English text ceded sovereignty. The Māori text, the Tribunal found, did not, and the rangatira who signed it "did not cede their sovereignty" (p. xxii). Williams was not a disinterested translator. His bishop had written to him weeks earlier instructing him to support Hobson's efforts to obtain cession (p. 506), and, as Moon and Fenton note, he held significant land (p. 417). <!-- v3: P3-058 --> Whether he deceived is disputed among the historians the Tribunal reviews—Ward doubts it, while Belich thinks it likely that Williams's use of *rangatiratanga* was "a deliberate or semi-deliberate act of deceit" (pp. 414–415)—and the Tribunal's own judgment is measured: Williams "may have been honest in his choice of 'kawanatanga'" but "must, however, have known that tino rangatiratanga conveyed more than what was set out in the English text" (p. 514). <!-- v3: P3-059 FC -->

On the benchmarks this practice is the weakest of the five. The standard comes mostly from later courts. One contemporary did raise the danger: on the day of signing, the missionary printer William Colenso asked Hobson whether the chiefs understood the articles (Waitangi Tribunal, 2014, pp. 352, 373). <!-- v3: P3-061 --> Beyond that, the record of objection is thin, and I do not claim more than Moody-Adams's argument allows (1994, pp. 294, 296)—that a thin record of objection does not show the actors could not have known. <!-- v3: P3-062 -->

The same era also shows what a society does when it takes the danger seriously, and this matters more for the present argument than the wrong itself. Castile's Pragmática of Alcalá (1503) required notaries to keep a register and to read their notes to the parties and witnesses present—"las lean presentes las partes e los testigos"—and required a witness or another person who could write to sign for a party who could not (Almeida Cabrejas, 2019, p. 24, quoting the law as printed in Marchant Rivera, 2015). <!-- v3: P3-064 --> At Anglo-Iroquois councils, "When doubts about an interpreter's integrity or ability arose on either the Indian or the English side, others were employed, formally or informally, to 'assist' and check the accuracy of his translations" (Hagedorn, 1988, p. 61). English law gave a plea, *non est factum*, to the person who could not read and had "a written contract falsely read over to him" (*Foster v. Mackinnon*, 1869, at 711). These safeguards were imperfect. A reviewer of Burns's study of Cuzco reports that notaries "could manipulate the legal record in the service of a powerful client or on their own account" (Andrien, 2012, p. 145), and in *Foster* the person who misdescribed the paper was a party to it, the bill's acceptor. <!-- v3: P3-067 --> But each safeguard placed someone other than the writer at the point where the record was made, or gave the bound party a way to undo it.

### 3.4 The monopoly

The fourth practice concerns the means of the medium. In England the Crown chartered the Stationers' Company in the reign of Philip and Mary—4 May 1557 by the regnal year, though Arber dates it 1556—and the charter confined printing to the Company's members and holders of royal patents and gave its wardens powers of search and seizure (Arber, 1875, vol. 1, pp. xxviii–xxxii). <!-- v3: P4-002, P4-003 --> The Licensing Act of 1662 (14 Car. II c. 33) capped the number of master printers at twenty, besides the King's and the universities' printers, and reached that number by admitting no new master until deaths and removals brought the existing ones down to it (s. X, p. 431). <!-- v3: FC2-2 --> The regime lapsed in 1695 (Johns, 2002, p. 124). <!-- v3: P4-007 -->

Objection came from outside and inside. Milton's pamphlet of 1644, against licensing, put it in the language of trade: "Truth and understanding are not such wares as to be monopolized and traded in by tickets and statutes and standards" (Milton, 1644/2006). <!-- v3: P4-N02 AUTHOR; P4-009 FC --> In January 1643 the Company itself had petitioned the House of Commons against eleven of its own members, many of whom held the patents for the most profitable books, calling them "Monopolizers of Printing the most vendable Bookes of worth and quantity now in use" (Arber, 1875, vol. 1, p. 583). <!-- v3: P4-010, P4-011 -->

This case carries the least weight of the five. It is one kingdom; I have found no count of those shut out; and every Protestant state before 1695 regulated print in some fashion (Johns, 2002, p. 119), so the monopoly is not a departure from a free baseline. <!-- v3: P4-014 --> I include it because it shows the fourth position plainly: beside the examiner, the teacher, and the record-keeper stands the owner of the press.

### 3.5 The promise

The fifth practice is the only one with actors at world scale. The World Conference on Education for All at Jomtien in 1990 proposed, among targets that "countries may wish" to adopt, reducing the adult illiteracy rate "to, say, one-half its 1990 level by the year 2000" (World Conference on Education for All, 1990, para. 8). <!-- v3: P4-017 --> The world rate fell by about a quarter, from 25.4 percent in 1990 to 18.9 percent in 2000 (UNESCO Institute for Statistics, 2026). <!-- v3: P4-N04 AUTHOR --> At Dakar in 2000 the World Education Forum committed to "achieving a 50 per cent improvement in levels of adult literacy by 2015" (World Education Forum, 2000, para. 7(iv)). <!-- v3: P4-019 --> The monitoring report of 2015 records that illiteracy fell from 18 to an estimated 14 percent, "which means the Dakar target of halving illiteracy was not achieved" (UNESCO, 2015, p. xiii). <!-- v3: P4-020 --> The same report calls the movement "a qualified success" (p. xv). <!-- v3: P4-N03 AUTHOR --> In 2024, 739 million adults could not read and write a simple statement, 63 percent of them women (UNESCO Institute for Statistics, 2026).

Missed targets alone would be a failure of delivery. The ethical failure is the premise beneath them, which Graff named the literacy myth. Studying three Ontario cities in the mid-nineteenth century, he observed that for an unskilled or semiskilled worker, "Doing his or her job seldom, if ever, required the use of reading and writing" (Graff, 1979/1991, p. 302), and he concluded that "literacy was more valuable to the society's goals and needs than to those of most individuals within it" (p. 321). <!-- v3: P4-024; P4-N05 AUTHOR --> Street's autonomous model, quoted in Section 2.1, is the same premise seen from anthropology: literacy offered as a remedy "regardless of the social and economic conditions." Marketing scholars have documented the general form. Giesler and Veresiu (2014, pp. 841, 843) trace how responsibility for structural problems is shifted onto the individual consumer, with the "financially literate consumer" among their cases. <!-- v3: P4-028 --> A competence is promoted; the condition it was to cure persists; and the person who was to acquire it bears the blame.

Graff's qualifications belong in the account. Clerical work did demand literacy, and skilled work more often than unskilled, and he reports differential access to the artisanal level and its rewards (1979/1991, p. 302); the myth was an exaggeration of something true. <!-- v3: P4-029; P4-N05 AUTHOR --> Nor was the doubt his alone. He quotes W. B. Hodgson, who warned in 1868 that "the power to read does not in the least determine the use to which it is put" (p. 301). A contemporary named the overselling while it was under way, so the first benchmark is met as well as the third.

### 3.6 What the record does not show

Three things qualify the account, and a referee should have them before the analogy is drawn.

First, the record is not a survey. The exclusionary gate with a stated purpose is documented for the American South and Natal; the withheld competence chiefly for the American slave states; the record over the voice for colonial treaties; the monopoly for one kingdom. I claim that named institutions did these five things, not that every literate society did.

Second, the counter-evidence is real. The Scandinavian Lutheran program that made reading "everybody's calling and right" also compelled it, and tied confirmation and marriage to the examination (Johansson, 1985, p. 64): the achievement and the gate sat in one institution. <!-- v3: P4-034 --> Bans leaked, as Section 3.2 noted. Illiterate people used notaries to make their own deeds, and the Castilian notarial documents Almeida Cabrejas studied are full of witnesses signing at the request of parties who could not (2019, p. 29). <!-- v3: P4-039, P4-040 --> The third party was not always the stronger side's instrument.

Third, the gravest wrong done in the name of schooling is not a failure of literacy and I do not count it as a sixth practice. Canada's Truth and Reconciliation Commission (2015) and the United States Department of the Interior (Newland, 2022) document the removal of Indigenous children, forced labor (Truth and Reconciliation Commission of Canada, 2015, p. 59; Newland, 2022, pp. 59–61), abuse (Newland, 2022, p. 56), and the suppression of languages. <!-- v3: P4-042 --> Neither attributes the harm to the teaching of reading. What those reports do establish, and what Section 5 uses, is narrower: participation could be compelled (Truth and Reconciliation Commission of Canada, 2015, p. 62; Newland, 2022, p. 36), and one language of instruction and speech was enforced. <!-- v3: P4-044; P4-045 AUTHOR -->

## 4. The Positions, Occupied Again

### 4.1 The mapping

Table 1 sets each practice beside its present-day counterpart and states the property the comparison rests on. The property matters more than the resemblance: an analogy that does not say what carries it invites governance aimed at the wrong feature of a system (Qadri et al., 2026). <!-- v3: P4-N01 -->

**Table 1. Five positions, then and now**

| Position | Literacy transition | Property compared | Algorithmic intermediary | Where the comparison is weak |
| --- | --- | --- | --- | --- |
| The gate | Reading tests administered at a registrar's or officer's discretion (*Katzenbach*, 1966; Immigration Restriction Act 1901) | Standing depends on being read by a party one cannot question | Shared screening models that recommend rejecting the same applicants across employers (Bommasani et al., 2026) <!-- v3: P4-048 --> | The present gate is the intermediary's reading of the person, not a test of the person's competence |
| The withheld competence | Laws against teaching and against print in a language (Douglass, 1845; Moser, 2017) <!-- v3: P4-050 --> | The party that gains from incompetence controls access to the competence | Trips offered without destination or fare (Rosenblat & Stark, 2016); opaque evaluations (Rahman, 2021) | No law forbids learning; trade secrecy and interface design do the withholding |
| The record | A written text binding a party who could not make its own or check it (*Marshall*, 1999; Waitangi Tribunal, 2014) <!-- v3: P4-054 FC AUTHOR --> | One side holds the binding record of what both agreed | Platform claims its reading of its data is conclusive in disputes; template replies (Rosenblat & Stark, 2016, pp. 3765, 3771) <!-- v3: P4-055 --> | The user has agreed to standard terms; the law treats that as assent where notice was reasonable (*Hill v. Gateway 2000*, 1997; *Specht v. Netscape*, 2002) <!-- v3: P4-056 --> |
| The means | A chartered monopoly of print (Arber, 1875) | Few hands hold the means of the medium | Compute for training and serving models supplied by a few cloud firms (Competition and Markets Authority, 2023) <!-- v3: P4-058 --> | Not established here; see Section 6 |
| The promise | Literacy as the cure for a structural condition (Graff, 1979/1991; World Education Forum, 2000) <!-- v3: P4-059; P4-N05 AUTHOR --> | A competence sold as the remedy for a position | "AI literacy" as "a sure path to economic security" (Kamperman & Graff, 2026, p. 34) <!-- v3: P4-060 FC AUTHOR --> | Its advocates have moral aims, as many literacy campaigners did (Graff, 1979/1991, p. 298) <!-- v3: P4-061 AUTHOR; P4-N05 AUTHOR --> |

Take the gate first. Bommasani and colleagues (2026) study roughly three million applicants screened by a single vendor's models and find that 4% of those who apply to ten positions are recommended for rejection from all ten, a rate above chance; applicants, they write, "would need to apply widely in order to ensure their applications are considered by a human" (p. 6351). <!-- v3: P4-064 --> The registrar's discretion has no counterpart in intent—nothing in the study suggests a purpose to exclude—but it has one in structure. A single vendor's judgment follows the applicant from door to door, and the applicant cannot ask it a question. <!-- v3: P4-N06 AUTHOR -->

The withheld competence maps onto design. Rosenblat and Stark (2016, p. 3762) found that Uber drivers had about fifteen seconds to accept a trip and were not shown its destination or fare. Rahman (2021; see also Rahman, 2019, pp. 42–43) studied a labor platform that replaced a visible rating with an opaque evaluation, and found that workers could not work out what the criteria were (Rahman, 2019, pp. 117, 128) and experienced the evaluation itself as a form of control. <!-- v3: P4-068, P4-070 --> <!-- v3: FC2-12 --> No statute forbids these workers to learn how they are judged. The firm that gains from their not knowing controls what they can find out, which is the property the comparison rests on.

The record maps most closely, and it is the case where the triad matters. The intermediary claims its log as the authoritative record of what passed between the two parties, and its determination is what binds them (Rosenblat & Stark, 2016, p. 3765). <!-- v3: P4-071 FC --> A driver who disputes a fare, a rider who disputes a charge, and an applicant who asks why she was screened out all argue against a record they did not make and cannot readily inspect (Directive (EU) 2024/2831, recital 63). <!-- v3: P4-071 -->

The promise maps without strain, because its present form is the subject of an existing literature. Kamperman and Graff (2026) show the AI-literacy movement repeating the literacy myth; Edwards and Veale (2017, p. 67) show that the explanation a person is offered is one she is poorly placed to use; Giesler and Veresiu (2014) describe the general mechanism by which a structural problem becomes an individual's task. <!-- v3: P4-073 --> What the history adds is the company the promise keeps. Literacy was oversold by people who did not run the registrar's office. The promise mattered because it drew attention toward the learner while the other four positions did their work, and the same division of attention is visible now: a public debate about whether users understand AI proceeds beside a set of decisions about who may screen, withhold, and record.

The fourth position, the means, I leave as an open row. The Stationers held printing by letters patent, a public grant. <!-- v3: P4-076 --> Whether the infrastructure on which present intermediaries run is held in a comparable way is an empirical question about markets in computing and data that this paper has not examined (but see Posada et al., 2021), and the three duties do not depend on the answer. <!-- v3: P4-N07 AUTHOR -->

### 4.2 Comprehension without leverage

The defense of explanation assumes that a person who understands a decision can act on it. Kim and Routledge (2022, p. 88) ground a right to explanation in the trust that a firm invites from its data subjects, such as its customers and employees, when it seeks their consent, and I do not dispute that such a right exists; EU law now grants a legal one (*CK v Dun & Bradstreet Austria*, 2025, para. 57). <!-- v3: P5-001; P5-N01 AUTHOR --> The question is what the right delivers when nothing else changes.

Douglass answered in 1845. Reading gave him "a view of my wretched condition, without the remedy." The same structure appears in the platform evidence. Dubal (2023, p. 1984), reviewing drivers' efforts to obtain and analyze their own data, concludes that "Knowledge alone will not end or mitigate the precarities of digitalized pay." The evidence is not that knowledge is useless. Cameron (2024) finds that ride-hail drivers who learn the system use that knowledge in tactics of engagement and deviance, and that both kinds of tactic end by eliciting their consent to the work. Knowledge buys an individual worker room to maneuver inside terms she cannot alter. Republican theory predicts as much: coping with arbitrary power does not reduce it (Section 2.2).

### 4.3 The first difference: the medium answers back

The analogy gives way at two points, and both make the present case harder.

A page does not change with its reader. Once a person could read a statute, the statute read the same to her as to the registrar, and literacy could be turned against those who had rationed it; the Company used print to petition the Commons against eleven of its own members, many of whom held the patents for the most profitable books. <!-- v3: P5-008 --> An algorithmic intermediary is a different kind of thing. Yeung (2017) describes Big Data–driven nudges as "extremely powerful and potent due to their networked, continuously updated, dynamic and pervasive nature," operating through a recursive loop in which the person's response to the system becomes an input to its next move. <!-- v3: P5-009, P5-012 --> Her analysis concerns one user and one choice architect, and I extend it with caution to the triad. But the implication for a remedy by education is direct. A skill aimed at a fixed text accumulates. A skill aimed at a system that updates on the learner's behavior may be chasing its own shadow, and the party that holds the system decides how fast it moves.

### 4.4 The second difference: who checks the third party

The second difference concerns the safeguards of Section 3.3. I state it carefully, because the strong version—that algorithmic intermediaries operate with no procedural checks at all—is false.

Law now supplies checks. In the European Union, the Platform Work Directive requires that a decision to restrict, suspend, or terminate a platform worker's account be taken by a human being, and gives the worker a right to written reasons for decisions taken or supported by automated systems and to a review by the platform (Directive (EU) 2024/2831, arts. 10(5), 11); member states must transpose it by 2 December 2026. <!-- v3: P5-013, P5-014 --> The Digital Services Act requires that decisions on complaints be "taken under the supervision of appropriately qualified staff, and not solely on the basis of automated means" (Regulation (EU) 2022/2065, art. 20(6)), and it creates certified out-of-court dispute bodies, though ride-hail services may fall outside it (*Elite Taxi*, 2017, para. 40). <!-- v3: P5-N03 AUTHOR --> The General Data Protection Regulation gives a person a right not to be subject to a solely automated decision with legal or similarly significant effects and, where such a decision rests on a contract or her explicit consent, the right to obtain human intervention and to contest it (Regulation (EU) 2016/679, art. 22(1)–(3); on a credit bureau's score on which a lender "draws strongly," *OQ v Land Hessen*, 2023, paras. 52, 61, 73). <!-- v3: P5-019; P5-N02 AUTHOR --> <!-- v3: FC2-15 --> For business users of platforms, a separate regulation requires a statement of reasons "on a durable medium" no later than the time a restriction of a business user's goods or services takes effect, and at least 30 days before its account is terminated (Regulation (EU) 2019/1150, art. 4(1)–(2)). <!-- v3: P5-020 --> Contract law adds unconscionability, which asks whether a party, "considering his obvious education or lack of it," had "a reasonable opportunity to understand the terms of the contract" (*Williams v. Walker-Thomas Furniture Co.*, 1965, p. 449), and courts and regulators stand behind all of these. <!-- v3: P5-022 -->

What survives is narrower and, I think, more telling. Three features of the old safeguards have no settled counterpart.

The first is timing. Under the Castilian rule of 1503, the notary read the instrument to the parties before they were bound (Almeida Cabrejas, 2019, p. 24). <!-- v3: P5-024 --> The settled rule runs the other way: "A contract need not be read to be effective," and "Competent adults are bound by such documents, read or unread" (*Hill v. Gateway 2000, Inc.*, 1997, pp. 1148–1149; see *Upton v. Tribilcock*, 1875, p. 50). <!-- v3: P5-025, P5-026 --> Most of the checks listed above operate after the decision. <!-- v3: P5-027 -->

The second is independence at the first instance, a gap Kaminski and Urban (2021, p. 2039) find in private-sector contestation—though they would accept an arbiter who holds "an independent position within a company"—and Lindblom (2019) in the employer's own grievance channels. <!-- v3: P5-N05 AUTHOR --> <!-- v3: FC2-6 AUTHOR --> Under the Directive and the two platform Regulations the first reviewer is the platform's own staff; the human intervention the GDPR guarantees is intervention "on the part of the controller." <!-- v3: P5-028 --> The independent bodies the Digital Services Act creates "shall not have the power to impose a binding settlement" (art. 21(2)). <!-- v3: P5-030 --> A worker can reach a court, but a court is not at the point of decision, and the cost of reaching it falls on the weaker party, though the Digital Services Act's bodies must be free of charge or at a nominal fee to her (art. 21(5)). <!-- v3: P5-N04 AUTHOR -->

The third is the separation of roles. The civil-law notary's professed duty runs to both parties and to the weaker of them (Union Internationale du Notariat, 2004, 2005). The standard-form contract belongs to a different legal world, in which one party drafts and the other typically adheres (Kessler, 1943, p. 632). <!-- v3: P5-033 --> <!-- v3: FC2-5 --> A platform that mediates between driver and rider is at once Simmel's third (Simmel, 1950, pp. 145–169) and the driver's counterparty, the drafter of the terms and the keeper of the record of their performance. <!-- v3: P5-034 --> The historical safeguards assumed that these were different people; Crawford and Schultz (2014, pp. 120, 127) ask for a like separation in big-data systems, of designer, executive and adjudicator, so that those roles stay "appropriate and distinct." <!-- v3: P5-N06 FC AUTHOR --> <!-- v3: FC2-4 -->

So the claim is this: no independent party with binding authority stands at the point where an algorithmic intermediary's reading becomes a decision, and no rule requires anyone to read, explain, and certify a person's understanding before she is bound; the nearest, in EU credit law, requires only "adequate explanations" before the agreement is concluded (Directive 2014/17/EU, arts. 14, 16; Directive (EU) 2023/2225, art. 12, applying from 20 November 2026 under art. 48), and the newer directive's one notarial role has a notary "confirm" that the consumer is guaranteed certain rights, not that she understands them (art. 26(8)). <!-- v3: P5-036 AUTHOR --> <!-- v3: FC2-7 AUTHOR --> The algorithm-specific checks that exist are recent, regional, mostly after the fact, and in the first instance the intermediary's own. <!-- v3: P5-037; P5-N07 AUTHOR -->

## 5. Three Duties of the Intermediary's Operator

### 5.1 The ground of the duties

If the injuries of algorithmic mediation come from positions and not from deficits in the user, the remedy belongs to whoever holds the positions. I ground the duties in the same three benchmarks that Section 3 applied to the past.

Operators break a standard they profess. The guidelines Jobin and colleagues counted are in part the industry's own (23 of 84), and most of them name non-maleficence (60 of 84). <!-- v3: P5-038, P5-039 --> A firm that publishes a commitment to avoid harm while keeping a decision procedure its subjects can neither foresee nor contest stands where the county stood in *Gaston County*: it tests for a competence under conditions it has itself arranged. <!-- v3: P5-040 --> Contemporaries condemn the practice, in the vocabulary of their time—drivers, YouTubers, the scholars who study them, and legislators (Rosenblat & Stark, 2016; Dubal, 2023; Muldoon & Raekstad, 2023; García-Ruiz & Rocchi, 2026, p. 21, n. 4; Directive (EU) 2024/2831, recitals 4, 8). <!-- v3: P5-043; P5-N08 AUTHOR --> <!-- v3: FC2-8 --> And the outcome falls short of the promise: explanation and literacy are offered as safeguards, and the evidence of Section 4.2 is that they leave the terms untouched.

The benchmarks say that something is owed. Republican theory offers two answers, and the duties meet both: rules that are common knowledge, and a share of control for those subject to them (Section 2.2). <!-- v3: P5-045 AUTHOR --> The three duties below are those two requirements applied to the three positions. Structural refusal answers the gate. A declared operating envelope answers the withheld competence. Counter-delegation answers the one-sided record. Table 2 summarizes them.

**Table 2. Three duties of the operator**

| Position | Duty | What it requires | What it is not |
| --- | --- | --- | --- |
| The gate | Structural refusal | A route to the same standing that does not pass through the intermediary's reading, at no penalty | A right to exit a market that offers nowhere else to go |
| The withheld competence | Declared operating envelope | Advance, binding limits on what the system may do to the person, known to both parties | Disclosure of how the system works |
| The record | Counter-delegation | The person's own record and reader, and an independent party able to bind the operator on a dispute | An explanation supplied by the operator |

The duties fall first on operators—the firms that design and run the intermediary—because they hold the positions and can change them. They do not fall only there. Young's social-connection model holds that "all agents who contribute by their actions to the structural processes that produce injustice have responsibilities to work to remedy these injustices" (Young, 2006, abstract; see also Young, 2005, p. 709), and the employers who adopt a screening vendor, the lenders who buy a score, and the legislators who could require any of the three duties are such agents. <!-- v3: P5-046 --> Young's model is forward-looking and shared; its point "is not to blame" (Young, 2005, p. 722), and I use it only to say who else must act, though she keeps the liability model alongside her own (Young, 2005, p. 719). <!-- v3: P5-047 --> <!-- v3: FC3-3 AUTHOR --> The operator's duty rests on the simpler ground that it holds a position of power over people who cannot check it and professes not to harm them.

One alternative should be set aside. Balkin (2016) proposed treating platforms as information fiduciaries with duties of loyalty to their users. Khan and Pozen (2019, p. 504) reply that "A fiduciary with sharply opposed loyalties teeters on the edge of contradiction": the firm's officers owe their duties to stockholders. The triad adds a further difficulty, since an intermediary between a driver and a rider cannot be loyal to both in the fiduciary's sense, though Claassen (2024), drawing on the political literature on fiduciary relations, holds that a fiduciary can serve beneficiaries with competing interests under a duty of "reasonableness" and "fairness." <!-- v3: P5-N10 FC AUTHOR --> The notary's duty was never loyalty. Its professed form is impartiality toward two parties and care for the weaker (Union Internationale du Notariat, 2004, 2005), enforced by an office the parties do not control. <!-- v3: P5-053 FC AUTHOR --> The duties below aim at that structure.

### 5.2 Against the gate: structural refusal

Economists, Hirschman (1970, p. 17) observed, are biased "in favor of exit and against voice": they see exit as the customer's first defense. <!-- v3: P6-001 AUTHOR --> Exit protects no one when every door leads to the same reader; even Pettit's (2006, p. 142) case for exit assumes that "no one would depend on any particular master." <!-- v3: P6-N01 AUTHOR --> The applicant whom one vendor's models reject from ten positions has ten exits and one examiner. <!-- v3: P6-002 --> Section 3.6 recorded what compelled participation meant at its worst; the milder modern form is a market in which declining the intermediary's reading means declining to take part. <!-- v3: P6-003 -->

Structural refusal is the duty to keep open a route to the same standing that does not pass through the intermediary's reading, and to attach no penalty to taking it. For hiring, it means a human assessment available on request and weighed on the same footing, which the rule implementing New York City's audit law expressly does not require <!-- v3: FC2-16 --> (New York City Department of Consumer and Worker Protection, 2023, 6 RCNY § 5-304(a)); Bhargava and Assadi (2024, p. 201) argue, from the employer's side, that interviews "should thus not be entirely replaced by algorithms." <!-- v3: P6-N04 FC AUTHOR; P6-N03 AUTHOR --> For credit, manual underwriting at comparable speed. The idea has antecedents: Zong and Matias (2024, p. 10:1) treat refusal as itself an act of design and count among its facets whether it can "reduce or redistribute penalties experienced by refusers," and the GDPR's article 22 already gives a narrow right not to be subject to solely automated decisions. <!-- v3: P6-004 -->

Two objections need answers. The first is cost: a second track is expensive, and a firm that maintains one may price it so that no one uses it. The duty therefore specifies no penalty, and it is the reason the duty cannot rest on the operator's goodwill. Hoeksema (2023, p. 15) argues, on other grounds, that republicans "cannot rely on the idea of exit options or of rationally consenting citizens" against platform power. <!-- v3: P6-006 FC --> The second objection is that the human on the second track may be no fairer than the model. That may be so. The duty does not promise a better reader. It denies any single reader the position of the registrar.

### 5.3 Against the withheld competence: declared operating envelopes

The obvious remedy for withheld knowledge is disclosure, and disclosure fails. Bakos, Marotta-Wurgler, and Trossen (2009) tracked visitors to software retailers and found that between one and two in a thousand opened the license agreement. Ben-Shahar and Schneider (2011, p. 672) quote one of that study's authors, Marotta-Wurgler: "No matter how prominently [end-user license agreements] are disclosed, they are almost always ignored." <!-- v3: P6-009 --> A fuller account of a model's workings would be read by fewer people still, and Section 4.3 gives a further reason to doubt it: the account describes a system that will have changed.

A declared operating envelope is a different instrument. It does not describe how the system works. It states in advance, and binds the operator to, the limits of what the system may do to the person (a model card declares "out-of-scope use cases" but binds no one; Mitchell et al., 2019, Figure 1): for a driver, the minimum pay for a trip of a given time and distance, the information shown before acceptance, the grounds on which an account may be suspended; for a borrower, the kinds of data that may not enter the score. <!-- v3: P6-N05 FC AUTHOR --> The person need not understand the model to know where she stands, as a tenant need not understand the landlord's finances to know the rent.

European law has begun to require a part of this. The Platform Work Directive obliges platforms to tell workers "the categories of data and the main parameters that such systems take into account and the relative importance of those main parameters in the automated decision-making" (Directive (EU) 2024/2831, art. 9(1)(b)(iii)). <!-- v3: P6-011 --> That is a duty to inform about the method. An envelope goes one step further, from describing the parameters to committing to bounds on the result.

The envelope meets the procedural requirement of Section 2.2—rules that are common knowledge—and by itself no more. Lovett's caution applies (a slave who can predict his master is not thereby freer; Lovett, 2026, §2.2): predictability does not end domination if the party who declared the rule can redeclare it at will. <!-- v3: P6-014 --> An envelope is therefore only as good as the constraint on changing it, which is why it needs the third duty beside it; for business users, EU law already requires 15 days' notice of a change, on pain of nullity (Regulation (EU) 2019/1150, art. 3(2)–(3)). <!-- v3: P6-N06 AUTHOR --> Firms will object that publishing limits exposes trade secrets and invites gaming. An envelope discloses outputs the firm commits to, not the method that produces them, and a limit that can be gamed only by meeting it is not a harm.

### 5.4 Against the one-sided record: counter-delegation

People who could not read did not, on the whole, protect themselves by becoming scribes. They relied on others: a witness to sign at their request (Almeida Cabrejas, 2019, p. 29), a second interpreter to check the first (Hagedorn, 1988, p. 61). <!-- v3: P6-015 --> Counter-delegation is the duty to make the modern equivalent possible—to let the person keep her own record of what passed through the intermediary and bring her own reader to it, and to submit disputes to a party the operator does not control.

Others have proposed a version of the technical half built into the operator's own system, and they judge contestation outside that system insufficient (Alfrink et al., 2023). <!-- v3: P6-N07 AUTHOR --> <!-- v3: FC2-3 --> Li and colleagues (2022) outline assistants that would run on a gig worker's side, logging offers and pay and pooling the data across workers. Citron (2008) argued that government automated decision systems owe their subjects audit trails. <!-- v3: P6-017 --> Dubal (2023, pp. 1984–1986) reports what happens when workers try to build such records under present law: pooled data have helped some contest suspensions based on errors, and she argues that transparency requests alone are "ineffectual." <!-- v3: P6-018 -->

That result marks the limit of the technical half. A user's software agent is not a notary. In agency law, as Kolt (2026, p. 345) quotes the Restatement, "At present, computer programs are instrumentalities of the persons who use them": the agent carries its user's interest and owes no duty to anyone, and it is itself a new third party whose supplier has interests of its own. <!-- v3: P6-019 P6-020 --> The notary's force came from an office whose holder was liable to the party he harmed (Marchant Rivera, 2015). <!-- v3: P6-022 --> <!-- v3: FC2-11 --> Counter-delegation therefore has two parts. The operator must permit and not obstruct the user-side record—one operator has invoked its terms of service against a worker-side tool that read its order data, though that tool kept no record (Fischels, 2021)<!-- v3: FC2-9 -->—and a dispute must be decidable against that record by a body that can bind the operator. Lindblom (2019, p. 206) argues for checks on employer power "outside the domain of the firm," in unions rather than courts, <!-- v3: FC2-10 --> and Crawford and Schultz (2014, p. 127) for a "neutral data arbiter" in big data. <!-- v3: P6-023; P6-N08 FC AUTHOR --> The Digital Services Act's out-of-court bodies are the nearest existing model, and they lack the binding power (art. 21(2)). <!-- v3: P6-024 -->

### 5.5 What design cannot do

Two limits. The duties are worth what their enforcement is worth. Mittelstadt (2019) argued that principles alone cannot guarantee ethical AI. Berthon, Pitt, and Campbell (2019) reached the regulatory conclusion for digital addiction: "we argue that public policy solutions are required" (p. 457), because "Consumers on their own struggle to maintain equanimity with regard to their digital experiences" (p. 463). The duties here are duties of the operator, and I expect them to be discharged where a legislature or a regulator makes them so. Some practices may warrant prohibition instead; Dubal (2023, p. 1989) argues as much for individualized pay. <!-- v3: P6-029 -->

The second limit is the fourth position. Nothing in the three duties touches concentration in the means of the medium, and the paper has not shown that such concentration exists in the form the Stationers' charter gave it. If it does, the remedy lies in competition and regulatory policy, not in the design of any one intermediary.

### 5.6 Three objections

*The users consented.* A driver taps to accept the platform's terms and an applicant clicks to submit; on a liberal view of contract, that settles the matter. The history gives two replies. Consent to a gate one cannot avoid is thin: the Southern voter also "chose" to present himself to the registrar. And consent to terms does not reach the positions (cf. Lindblom, 2019, p. 189). <!-- v3: P6-N10 AUTHOR --> The applicant consents to be assessed. She does not consent to an assessment she cannot question following her to every employer in a sector, and the law of unconscionability already asks whether a party had "a reasonable opportunity to understand the terms" (*Williams v. Walker-Thomas Furniture Co.*, 1965, p. 449). <!-- v3: P6-031 --> The republican point is prior to both replies: a person may consent to an arrangement and be dominated within it (Pettit, 1997, p. 62, as quoted in Lindblom, 2019, p. 199). <!-- v3: P6-032 AUTHOR -->

*The law already provides.* Section 4.4 listed what European law now requires, and an objector may say the duties are redundant. They are partly anticipated, which I take as support. The Platform Work Directive's human decision on termination is a fragment of structural refusal; its duty to inform workers about automated systems is a fragment of the envelope. But each provision is confined to a sector or a jurisdiction, each places the first review inside the firm, and none supplies, at the point of decision, the binding independent party on which counter-delegation depends. <!-- v3: P6-038 --> The argument here gives those scattered rules a common rationale and says what they still lack.

*The history is ornament.* If domination is the wrong and republican theory supplies the remedy, why detour through 1740 and 1901? Because the history does work that the theory cannot. It shows that the positions are separable—that the examiner, the teacher, and the record-keeper are different offices that can be held and abused independently—where a general charge of platform power runs them together. It shows which remedies worked: the voting tests ended by statute and the treaties were reread by courts and a tribunal, while better readers did not end the tests (*South Carolina v. Katzenbach*, 1966, at 312 n. 13). <!-- v3: P6-039 P6-040; P6-041 AUTHOR --> And it supplies the one thing a purely theoretical argument lacks, a record of safeguards that societies built when they took an intermediary's power seriously, against which the present arrangement can be measured. The duties in this section are the notary's office, the second interpreter, and the suspended test, restated for a third party that is no longer a person.

## 6. Limits

The historical argument rests on cases, and the cases are narrow in three ways. They come chiefly from English-speaking jurisdictions and their empires, with Spanish, Brazilian, Russian, Indian, Swedish, and Yemeni cases as checks. <!-- v3: P6-042 --> They are stronger for some practices than others: the gate and the withheld competence are documented with statutes, stated purposes, and contemporary objectors; the record over the voice rests on later courts and one disputed interpreter; the monopoly on one kingdom. And several of the books a historian would expect are known to me through reviews, which I have cited as reviews. I selected the cases by working outward from the four positions—looking for dated acts, stated grounds, and contemporary objectors—and I have reported in Section 3.6 the cases that cut the other way. A historian who began from a sample of literate societies instead of from the positions might weigh the practices differently.

The analogy is bounded by what it compares. It compares positions, and it cannot show intent: nothing here establishes that any operator means to exclude or to keep people ignorant, as Knox and Auld said they meant to, or to falsify a record. <!-- v3: P6-047 --> Nor does it predict that harms of the earlier scale will recur.

The triad limits the scope of the duties. They are derived for intermediaries that stand between two parties and bind both—hiring vendors, credit bureaus, labor and exchange platforms. Where one party scores another directly, the gate and the record are still present but the third party is not, and the argument about notaries does not transfer without more work. The present-day evidence is likewise limited to hiring, ride-hail, and platform labor. I have not examined search, content moderation, or public administration.

Finally, the normative frame is deliberately thin. Domination describes the positions; internal critique supplies the standard; and I have not argued that the three duties exhaust what non-domination requires. A fuller republican treatment would ask what control by the affected means for a system with millions of users, which is a question about institutions more than about design.

## 7. Conclusion

The passage from speech to writing as the medium of standing was not a steady enlargement of freedom. At each point where a competence became compulsory, a position opened beside it—examiner, teacher, record-keeper, owner of the press—and institutions used those positions over people who could not check them. The remedy that worked was rarely more reading. Legislatures suspended the tests; courts read the oral promise back into the treaty; and where societies took the scribe's power seriously, they put a second person in the room.

Algorithmic intermediaries hold the first three of those positions today, with two differences: the medium adjusts to the person it reads, and the second person is missing at the moment of decision. To tell workers, borrowers, and applicants that their protection lies in AI literacy is to offer the fifth practice as the cure for the other four. The duties argued for here—a route around the gate, limits declared in advance, and a record and a reader of one's own with an independent party to hear the dispute—ask the operator of the intermediary to accept what the notary's office once imposed on the scribe. They leave open the question with which any account of mediation should end: who checks the third party, and who appoints the checker.

## References

An Act for preventing the frequent Abuses in printing seditious treasonable and unlicensed Bookes and Pamphlets and for regulating of Printing and Printing Presses, 14 Car. II c. 33 (1662). In *Statutes of the Realm* (Vol. 5, pp. 428–433). <!-- v3: P4-006 FC --> <!-- v3: FC2-1 -->

Alabama Constitutional Convention. (1940). *Official proceedings of the Constitutional Convention of the State of Alabama, May 21st, 1901, to September 3rd, 1901* (Vol. 1). Wetumpka Printing. (Original work published 1901) Address of John B. Knox, pp. 7–16. <!-- v3: R01 FC AUTHOR; P1-023; P1-N01 AUTHOR -->

Aleixo, J. C. B., & Kramer, P. (2010). Os analfabetos e o voto: Da conquista da alistabilidade ao desafio da elegibilidade. *Senatus, 8*(2), 68–79. <!-- v3: P3-020 -->

Alfrink, K., Keller, I., Kortuem, G., & Doorn, N. (2023). Contestable AI by design: Towards a framework. *Minds and Machines, 33*(4), 613–639. https://doi.org/10.1007/s11023-022-09611-z <!-- v3: B23; P6-N07 AUTHOR -->

Almeida Cabrejas, B. (2019). "No firmó porque dijo no saber": Alfabetizados y analfabetos en documentos notariales de CODEA de los siglos XVI y XVII. *Philologia Hispalensis, 33*(1), 21–41. https://doi.org/10.12795/ph.2019.v33.i01.02

Andrien, K. J. (2012). [Review of the book *Into the archive: Writing and power in colonial Peru*, by K. Burns]. *Journal of Interdisciplinary History, 43*(1), 144–145. https://doi.org/10.1162/jinh_r_00366 <!-- v3: R02 -->

Arber, E. (Ed.). (1875). *A transcript of the registers of the Company of Stationers of London, 1554–1640 A.D.* (Vol. 1). Privately printed.

*Asociación Profesional Elite Taxi v Uber Systems Spain SL*, Case C-434/15 (Court of Justice of the European Union, Grand Chamber, 20 December 2017). <!-- v3: B13; P5-N03 AUTHOR -->

Bakos, Y., Marotta-Wurgler, F., & Trossen, D. R. (2009). *Does anyone read the fine print? Testing a law and economics approach to standard form contracts* (Working Paper No. 09-04). NET Institute.

Balkin, J. M. (2016). Information fiduciaries and the First Amendment. *U.C. Davis Law Review, 49*(4), 1183–1234. <!-- v3: R03 -->

Ben-Shahar, O., & Schneider, C. E. (2011). The failure of mandated disclosure. *University of Pennsylvania Law Review, 159*, 647–749.

Berthon, P., Pitt, L., & Campbell, C. (2019). Addictive de-vices: A public policy analysis of sources and solutions to digital addiction. *Journal of Public Policy & Marketing, 38*(4), 451–468. https://doi.org/10.1177/0743915619859852

Bhargava, V. R., & Assadi, P. (2024). Hiring, algorithms, and choice: Why interviews still matter. *Business Ethics Quarterly, 34*(2), 201–230. https://doi.org/10.1017/beq.2022.41 <!-- v3: B21; P6-N04 AUTHOR -->

Bommasani, R., Bana, S. H., Creel, K. A., Jurafsky, D., & Liang, P. (2026). Algorithmic monocultures in hiring. In *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency* (pp. 6351–6382). ACM. https://doi.org/10.1145/3805689.3812400

Brandt, D. (1998). Sponsors of literacy. *College Composition and Communication, 49*(2), 165–185. https://doi.org/10.58680/ccc19983181 <!-- v3: R04 -->

Butterfield, H. (1931). *The Whig interpretation of history*. G. Bell and Sons.

Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures consent through constant and confined choices. *Administrative Science Quarterly, 69*(2), 458–514. https://doi.org/10.1177/00018392241236163

Citron, D. K. (2008). Technological due process. *Washington University Law Review, 85*(6), 1249–1313.

*CK v Magistrat der Stadt Wien (Dun & Bradstreet Austria)*, Case C-203/22, ECLI:EU:C:2025:117 (Court of Justice of the European Union, 27 February 2025). <!-- v3: B11 FC; P5-N01 AUTHOR -->

Claassen, R. (2024). Wealth creation without domination: The fiduciary duties of corporations. *Critical Review of International Social and Political Philosophy, 27*(3), 317–338. https://doi.org/10.1080/13698230.2022.2113224 <!-- v3: B17; P5-N10 AUTHOR -->

Cleveland, G. (1897, March 2). *Veto message* [on a bill to amend the immigration laws]. The American Presidency Project. https://www.presidency.ucsb.edu/node/205983 <!-- v3: R05 -->

Competition and Markets Authority. (2023). *AI foundation models: Initial report*. https://www.gov.uk/government/publications/ai-foundation-models-initial-report <!-- v3: B28; P4-058 -->

Crawford, K., & Schultz, J. (2014). Big data and due process: Toward a framework to redress predictive privacy harms. *Boston College Law Review, 55*(1), 93–128. <!-- v3: B15; P6-N08 P5-N06 AUTHOR -->

Decreto n. 3.029, de 9 de janeiro de 1881 (Lei Saraiva) (Brazil). <!-- v3: B30; P3-019 -->

*Delgamuukw v. British Columbia*, [1997] 3 S.C.R. 1010 (Supreme Court of Canada).

Directive (EU) 2023/2225 of the European Parliament and of the Council of 18 October 2023 on credit agreements for consumers and repealing Directive 2008/48/EC. *Official Journal of the European Union*, L, 2023/2225, 30.10.2023. http://data.europa.eu/eli/dir/2023/2225/oj <!-- v3: B09 FC; P1-004 P5-036 -->

Directive (EU) 2024/2831 of the European Parliament and of the Council of 23 October 2024 on improving working conditions in platform work. *Official Journal of the European Union*, L, 11.11.2024.

Directive 2014/17/EU of the European Parliament and of the Council of 4 February 2014 on credit agreements for consumers relating to residential immovable property and amending Directives 2008/48/EC and 2013/36/EU and Regulation (EU) No 1093/2010. *Official Journal of the European Union*, L 60, 28.2.2014, p. 34. <!-- v3: B10 FC; P5-036 AUTHOR -->

Douglass, F. (1845). *Narrative of the life of Frederick Douglass, an American slave. Written by himself*. Anti-Slavery Office.

Douglass, M. (1854). *Educational laws of Virginia: The personal narrative of Mrs. Margaret Douglass, a Southern woman, who was imprisoned for one month in the common jail of Norfolk, under the laws of Virginia, for the crime of teaching free colored children to read*. John P. Jewett; Jewett, Proctor & Worthington. <!-- v3: R06 FC -->

Dubal, V. (2023). On algorithmic wage discrimination. *Columbia Law Review, 123*(7), 1929–1992. https://columbialawreview.org/content/on-algorithmic-wage-discrimination/ <!-- v3: R23 -->

Edwards, L., & Veale, M. (2017). Slave to the algorithm? Why a "right to an explanation" is probably not the remedy you are looking for. *Duke Law & Technology Review, 16*(1), 18–84.

Emenda Constitucional n. 25, de 15 de maio de 1985 (Brazil). <!-- v3: B30; P3-020 -->

Engerman, S. L., & Sokoloff, K. L. (2001). *The evolution of suffrage institutions in the New World* (Working Paper No. 8512). National Bureau of Economic Research. https://doi.org/10.3386/w8512

Fischels, J. (2021, July 31). Why DoorDash drivers are on strike. NPR. https://www.npr.org/2021/07/31/1023265561/why-doordash-drivers-are-on-strike <!-- v3: B06; P6-023 -->

*Foster v. Mackinnon* (1869) L.R. 4 C.P. 704.

García-Ruiz, P., & Rocchi, M. (2026). Can work be meaningful under algorithmic management? A MacIntyrean perspective. *Business Ethics Quarterly, 36*(1), 3–30. https://doi.org/10.1017/beq.2025.5 <!-- v3: B18; P5-N08 AUTHOR -->

*Gaston County v. United States*, 395 U.S. 285 (1969).

General Assembly of Alabama. (1832). *Acts passed at the thirteenth annual session of the General Assembly of the State of Alabama*. <!-- v3: B30; P3-071 -->

General Assembly of Georgia. (1830). *Acts of the General Assembly of the State of Georgia, passed in Milledgeville at an annual session in November and December, 1829*. Camak & Ragland. <!-- v3: B30; P3-071 --> <!-- v3: FC3-1 -->

General Assembly of North Carolina. (1831). An act to prevent all persons from teaching slaves to read or write, the use of figures excepted. In *Acts passed by the General Assembly of the State of North Carolina, at the session of 1830–31*. Lawrence & Lemay. Transcribed in ANCHOR, State Library of North Carolina, https://www.ncanchor.org/anchor/primary-source-bill-prevent <!-- v3: B30; P3-071; REF P3-071 North Carolina FC -->

General Assembly of Virginia. (1831). An act to amend the act concerning slaves, free negroes and mulattoes (7 April 1831), ch. XXXIX. In *Acts passed at a General Assembly of the Commonwealth of Virginia* (pp. 107–108). <!-- v3: B30; P3-071 -->

Giesler, M., & Veresiu, E. (2014). Creating the responsible consumer: Moralistic governance regimes and consumer subjectivity. *Journal of Consumer Research, 41*(3), 840–857. https://doi.org/10.1086/677842

Graff, H. J. (1991). *The literacy myth: Cultural integration and social structure in the nineteenth century*. Transaction. (Original work published 1979) <!-- v3: P4-N05 AUTHOR; R07 superseded -->

Hagedorn, N. L. (1988). "A friend to go between them": The interpreter as cultural broker during Anglo-Iroquois councils, 1740–70. *Ethnohistory, 35*(1), 60–80. https://doi.org/10.2307/482433

*Hill v. Gateway 2000, Inc.*, 105 F.3d 1147 (7th Cir. 1997).

Hirschman, A. O. (1970). *Exit, voice, and loyalty: Responses to decline in firms, organizations, and states*. Harvard University Press.

Hoeksema, B. (2023). Digital domination and the promise of radical republicanism. *Philosophy & Technology, 36*(1), Article 17. https://doi.org/10.1007/s13347-023-00618-7 <!-- v3: R08 -->

Holmes, W. F. (1975). [Review of the book *The shaping of Southern politics: Suffrage restriction and the establishment of the one-party South, 1880–1910*, by J. M. Kousser]. *Journal of Southern History, 41*(2), 270–272. https://doi.org/10.2307/2206040

Immigration Act of 1917, ch. 29, 39 Stat. 874 (United States). <!-- v3: B30; P3-024 -->

Immigration Restriction Act 1901 (Cth), No. 17 of 1901 (Australia).

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence, 1*(9), 389–399. https://doi.org/10.1038/s42256-019-0088-2 <!-- v3: R09 -->

Johansson, E. (1985). Popular literacy in Scandinavia about 1600–1900. *Historical Social Research, 10*(2), 60–64. https://doi.org/10.12759/hsr.10.1985.2.60-64

Johns, A. (2002). How to acknowledge a revolution. *American Historical Review, 107*(1), 106–125. https://doi.org/10.1086/ahr/107.1.106 <!-- v3: P4-007 P4-014 -->

Kaminski, M. E., & Urban, J. M. (2021). The right to contest AI. *Columbia Law Review, 121*, 1957–2048. <!-- v3: B14; P5-N05 AUTHOR -->

Kamperman, S., & Graff, H. J. (2026). On "AI literacy": The rhetorical and historical fallacies of a movement and its marketing. *Change: The Magazine of Higher Learning, 58*(4), 34–39. https://doi.org/10.1080/00091383.2026.2706429

Keith, A. B. (1912). *Responsible government in the dominions* (Vol. 2). Clarendon Press. <!-- v3: B30; P3-071 -->

Kessler, F. (1943). Contracts of adhesion—Some thoughts about freedom of contract. *Columbia Law Review, 43*(5), 629–642. https://doi.org/10.2307/1117230 <!-- v3: B01; P5-033 -->

Khan, L. M., & Pozen, D. E. (2019). A skeptical view of information fiduciaries. *Harvard Law Review, 133*, 497–541.

Kim, T. W., & Routledge, B. R. (2022). Why a right to an explanation of algorithmic decision-making should exist: A trust-based approach. *Business Ethics Quarterly, 32*(1), 75–102. https://doi.org/10.1017/beq.2021.3 <!-- v3: R10 -->

Kolt, N. (2026). Governing AI agents. *Notre Dame Law Review, 101*(1), 335–386. <!-- v3: R11 -->

Lake, M. (2006). From Mississippi to Melbourne via Natal: The invention of the literacy test as a technology of racial exclusion. In A. Curthoys & M. Lake (Eds.), *Connected worlds: History in transnational perspective* (pp. 209–229). ANU E Press. https://doi.org/10.22459/cw.03.2006 <!-- v3: R12 P3-069 -->

Leonard, I. A. (1992). *Books of the brave: Being an account of books and of men in the Spanish conquest and settlement of the sixteenth-century New World*. University of California Press. (Original work published 1949) <!-- v3: R13 -->

Li, T. J.-J., Lu, Y., Clark, J., Chen, M., Cox, V., Jiang, M., Yang, Y., Kay, T., Wood, D., & Brockman, J. (2022). A bottom-up end-user intelligent assistant approach to empower gig workers against AI inequality. In *2022 Symposium on Human-Computer Interaction for Work* (pp. 1–10). ACM. https://doi.org/10.1145/3533406.3533418

Lindblom, L. (2019). Consent, contestability, and unions. *Business Ethics Quarterly, 29*(2), 189–211. https://doi.org/10.1017/beq.2018.25 <!-- v3: B07; P6-032 P6-N08 P6-N10 P5-N05 AUTHOR -->

Lovett, F. (2026). Republicanism. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. https://plato.stanford.edu/entries/republicanism/

Marchant Rivera, A. (2015). La expedición del documento notarial castellano en el tránsito a la Modernidad: De la nota registral a la matriz del protocolo notarial. In N. Ávila Seoane, J. C. Galende Díaz, & S. Cabezas Fontanilla (Eds.), *Paseo documental por el Madrid de antaño* (pp. 331–347). Universidad Complutense; Fundación Hospital de San José de Getafe. https://hdl.handle.net/10630/10782 <!-- v3: B05; P6-022 P3-064 -->

Margo, R. A. (2005). [Review of the book *Self-taught: African American education in slavery and freedom*, by H. A. Williams]. *Journal of Economic History, 65*(2), 590–591.

Messick, B. (1993). *The calligraphic state: Textual domination and history in a Muslim society*. University of California Press. https://doi.org/10.1525/9780520917828 <!-- v3: R14 -->

Migration Act 1958 (Cth), No. 62 of 1958 (Australia). <!-- v3: B30; P3-016 -->

Milton, J. (2006). *Areopagitica: A speech for the liberty of unlicensed printing to the Parliament of England*. Project Gutenberg. https://www.gutenberg.org/ebooks/608 (Original work published 1644) <!-- v3: P4-009 FC -->

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency* (pp. 220–229). ACM. https://doi.org/10.1145/3287560.3287596 <!-- v3: B22; P6-N05 AUTHOR -->

Mittelstadt, B. (2019). Principles alone cannot guarantee ethical AI. *Nature Machine Intelligence, 1*(11), 501–507. https://doi.org/10.1038/s42256-019-0114-4

Moody-Adams, M. M. (1994). Culture, responsibility, and affected ignorance. *Ethics, 104*(2), 291–309. https://doi.org/10.1086/293601 <!-- v3: R15 -->

Moser, M. (2017). Introduction. *East/West: Journal of Ukrainian Studies, 4*(2), 3–7. https://doi.org/10.21226/T2DK9B

Muldoon, J., & Raekstad, P. (2023). Algorithmic domination in the gig economy. *European Journal of Political Theory, 22*(4), 587–607. https://doi.org/10.1177/14748851221082078

New York City Department of Consumer and Worker Protection. (2023). *Notice of adoption of final rule* [Automated employment decision tools, 6 RCNY §§ 5-300 to 5-304]. https://rules.cityofnewyork.us/wp-content/uploads/2023/04/DCWP-NOA-for-Use-of-Automated-Employment-Decisionmaking-Tools-2.pdf <!-- v3: B20 FC; P6-N03 AUTHOR -->

Newland, B. (2022). *Federal Indian Boarding School Initiative investigative report* (Vol. 1). U.S. Department of the Interior.

*OQ v Land Hessen (SCHUFA Holding)*, Case C-634/21, ECLI:EU:C:2023:957 (Court of Justice of the European Union, 7 December 2023). <!-- v3: B12; P5-N02 AUTHOR -->

Pettit, P. (1997). *Republicanism: A theory of freedom and government*. Oxford University Press.

Pettit, P. (2006). Freedom in the market. *Politics, Philosophy & Economics, 5*(2), 131–149. https://doi.org/10.1177/1470594X06064218 <!-- v3: B19; P6-N01 AUTHOR -->

Phule, J. (1882). A statement for the information of the Education Commission (19 October 1882). In *Education Commission, Bombay: Vol. 2. Evidence taken before the Bombay Provincial Committee and memorials addressed to the Education Commission* (pp. 140–145). Superintendent of Government Printing. (Volume published 1884) <!-- v3: R16 FC; P3-070 -->

Posada, J., Weller, N., & Wong, W. H. (2021). We haven't gone paperless yet: Why the printing press can help us understand data and AI. In *Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society* (pp. 864–872). ACM. https://doi.org/10.1145/3461702.3462604 <!-- v3: P4-N07 AUTHOR -->

Qadri, R., Prabhakaran, V., & Denton, R. (2026). *"AI is (not) the new ..": A diagnostic analogy framework for generative AI's cultural impacts* (arXiv:2609.31482). arXiv. https://arxiv.org/abs/2609.31482 <!-- v3: B26; P4-N01 (revised) -->

*R. v. Marshall*, [1999] 3 S.C.R. 456 (Supreme Court of Canada).

Rahman, H. A. (2019). *Invisible cages: Algorithmic evaluations in online labor markets* [Doctoral dissertation, Stanford University]. https://purl.stanford.edu/fc567cc8525 <!-- v3: B29; P4-068 -->

Rahman, H. A. (2021). The invisible cage: Workers' reactivity to opaque algorithmic evaluations. *Administrative Science Quarterly, 66*(4), 945–988. https://doi.org/10.1177/00018392211010118

Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (General Data Protection Regulation). *Official Journal of the European Union*, L 119, 4.5.2016.

Regulation (EU) 2019/1150 of the European Parliament and of the Council of 20 June 2019 on promoting fairness and transparency for business users of online intermediation services. *Official Journal of the European Union*, L 186, 11.7.2019.

Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 (Digital Services Act). *Official Journal of the European Union*, L 277, 27.10.2022.

Rosenblat, A., & Stark, L. (2016). Algorithmic labor and information asymmetries: A case study of Uber's drivers. *International Journal of Communication, 10*, 3758–3784.

Simmel, G. (1950). *The sociology of Georg Simmel* (K. H. Wolff, Ed. & Trans.). Free Press.

*South Carolina v. Katzenbach*, 383 U.S. 301 (1966).

South Carolina. (1840). An act for the better ordering and governing negroes and other slaves in this Province (Act No. 670). In D. J. McCord (Ed.), *The statutes at large of South Carolina* (Vol. 7, pp. 397–417). A. S. Johnston. (Original work published 1740) <!-- v3: B30; P3-071; ASM-4 FC -->

*Specht v. Netscape Communications Corp.*, 306 F.3d 17 (2d Cir. 2002). <!-- v3: P4-056 -->

Street, B. V. (2003). What's "new" in New Literacy Studies? Critical approaches to literacy in theory and practice. *Current Issues in Comparative Education, 5*(2), 77–91. https://doi.org/10.52214/cice.v5i2.11369 <!-- v3: R17 -->

Truth and Reconciliation Commission of Canada. (2015). *Honouring the truth, reconciling for the future: Summary of the final report of the Truth and Reconciliation Commission of Canada*.

*Uber BV v Aslam* [2021] UKSC 5 (UK Supreme Court). <!-- v3: B27; P2-006 -->

UNESCO. (2015). *Education for All 2000–2015: Achievements and challenges. EFA Global Monitoring Report 2015* (2nd ed.). <!-- v3: R18 FC; P4-020 -->

UNESCO Institute for Statistics. (2026). *Adult illiterate population and adult literacy rate, 15+ years* (February 2026 data release) [Data set].

Union Internationale du Notariat. (2004). *Principles of notarial ethics*.

Union Internationale du Notariat. (2005). *Principles of the notarial function*.

*Upton v. Tribilcock*, 91 U.S. 45 (1875). <!-- v3: B02; P5-026 -->

Vee, A. (2013). Understanding computer programming as a literacy. *Literacy in Composition Studies, 1*(2), 42–64. https://doi.org/10.21623/1.1.2.4

Voting Rights Act Amendments of 1970, Pub. L. No. 91-285, 84 Stat. 314 (United States). <!-- v3: B30; P3-026 -->

Voting Rights Act of 1965, Pub. L. No. 89-110, 79 Stat. 437 (United States). <!-- v3: B30; P3-025 -->

Waitangi Tribunal. (2014). *He Whakaputanga me te Tiriti / The Declaration and the Treaty: The report on stage 1 of the Te Paparahi o Te Raki inquiry* (Wai 1040). Legislation Direct.

Walzer, M. (1988). Interpretation and social criticism. In S. M. McMurrin (Ed.), *The Tanner lectures on human values* (Vol. 8, pp. 1–80). University of Utah Press; Cambridge University Press. <!-- v3: R19 P2-033 -->

Washington, B. T. (1901). *Up from slavery: An autobiography*. Doubleday, Page.

*Williams v. Walker-Thomas Furniture Co.*, 350 F.2d 445 (D.C. Cir. 1965).

Williams, J. (2018). *Stand out of our light: Freedom and resistance in the attention economy*. Cambridge University Press. https://doi.org/10.1017/9781108453004

Wilson, W. (1917, January 29). *Message to the House of Representatives returning without approval "An act to regulate the immigration of aliens to, and the residence of aliens in, the United States"*. The American Presidency Project.

World Conference on Education for All. (1990). *World declaration on education for all and framework for action to meet basic learning needs*. Inter-Agency Commission.

World Education Forum. (2000). *The Dakar framework for action. Education for all: Meeting our collective commitments*. UNESCO.

Yeung, K. (2017). "Hypernudge": Big Data as a mode of regulation by design. *Information, Communication & Society, 20*(1), 118–136. https://doi.org/10.1080/1369118X.2016.1186713 <!-- v3: R21 P5-012 -->

Young, I. M. (2005). Responsibility and global justice: A social connection model. *Anales de la Cátedra Francisco Suárez, 39*, 709–726. https://doi.org/10.30827/acfs.v39i0.1040 <!-- v3: B04; P5-046 P5-047 --> <!-- v3: FC3-4 -->

Young, I. M. (2006). Responsibility and global justice: A social connection model. *Social Philosophy and Policy, 23*(1), 102–130. https://doi.org/10.1017/S0265052506060043

Zong, J., & Matias, J. N. (2024). Data refusal from below: A framework for understanding, evaluating, and envisioning refusal as design. *ACM Journal on Responsible Computing, 1*(1), Article 10. https://doi.org/10.1145/3630107 <!-- v3: R22 -->
