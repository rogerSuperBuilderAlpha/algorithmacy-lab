<!-- Drafted by Claude (Opus 5.5), workstream H2 of run rr-2026-11-h, 10 Nov 2026, for Roger and Pierre. None of this is the authors' wording. Nothing committed. -->

# Workstream H2 — What can be delegated, and standing without circularity

Run rr-2026-11-h · 10 November 2026 · Questions 2 and 10 of FABLE_REVIEW §7 · reviewer points R2.2c, R2.1b, R2.3 · outline §2.2, §2.4, §3, §5 Table 1 (PITCH_AND_OUTLINE.md numbering).

## 0. Conflicts flagged before acting

1. **Commit rule.** The repo CLAUDE.md says to branch, commit and push after every step. RUN_BRIEF_H says not to commit. I followed the brief and committed nothing.
2. **Verification tiers.** RUN_BRIEF_H lists `publisher-verified | catalogue-verified | primary-legal-source`. `library/build_index.py` accepts only `verified | crossref-verified | corrected` (l. 39). I used validator-legal values: `crossref-verified` where I fetched a Crossref record, and `verified` for the case, with "primary-legal-source" written into `source_basis` (the precedent is `eu2024aiact`). `--check` on my cards fails only for "not in references.bib", the expected failure for new held cards. I did not regenerate CARDS_INDEX.md.
3. **Section numbers.** The brief asks for outline numbers 1–10; the validator's section table is the old 1–9. All my cards use numbers ≤ 5, so both read correctly. Each card says "outline numbering (rr-2026-11-h)".
4. **No Hart card.** I was assigned `hart*` "if present". No such card exists, and the Postscript was unreachable, so I did not create one (see §2).

## 1. What was searched (all 10 Nov 2026)

| # | Tool | Query (exact) | Outcome |
|---|---|---|---|
| 1 | Crossref `query.bibliographic` | ten lead strings: Hardimon Role Obligations J Phil 1994; Vincent structured taxonomy; Thompson What is it to wrong someone; Wallace Moral Nexus; Cornell Wrongs rights third parties; Sreenivasan Duties and their direction; May Directed duties; Murphy juridical foundations non-delegable; Stevens non-delegable duties vicarious liability; Hart Postscript | Records for all ten (table §2) |
| 2 | Consensus | non-delegable duty of care tort theory independent contractor assumption of responsibility (30) | Woodland commentary; Brodie 2010; George 2014 LQR; **Morgan 2015 CLJ** (OA AM); Beuermann 2017; Witting 2006; Nolan 2019 on assumption of responsibility. Kept Morgan (OA, leading critique). Others dropped: closed, or about vicarious liability only |
| 3 | Consensus | non-delegable duty applied to artificial intelligence or automated systems liability of deployer (30) | AI-liability papers (Buiten et al. 2023; Custers et al. 2025; Huberman 2021; Gredka-Ligarska 2025; Kong 2026). None applies the non-delegable duty doctrine in the abstract |
| 4 | Consensus | role obligations delegation professional institutional duties what cannot be delegated (30) | Nursing-delegation practice literature; Norman & Reed 2010 logic of delegation. Nothing on the theory of role obligation. Dropped |
| 5 | OpenAlex `search` | `"non-delegable" algorithm`; `"nondelegable duty" "artificial intelligence"`; `"role obligations" "artificial intelligence"`; `"directed duties" standing accountability`; `"non-delegable" hotel` (the first query, `"non-delegable duty" "artificial intelligence"`, returned an API error) | 570 / 24 / 256 / 449 / 216 hits; top 12 each inspected. Kept: **Liau 2023** (Standing in Private Law, intro OA), **Bradley 2026** (CJLJ, OA but HTTP 429), May 2026 CJP. AI hits are preprints (Upadhyay & Joshi 2026, Zenodo; Gilly 2026, SSRN; Zinzilieta, lawyers' "nondelegable duty to think") |
| 6 | Scholar Gateway | one natural-language query on accountability coming apart from directed obligation | **ACCESS_DENIED** (as in WS_A and WS_B) |
| 7 | WebSearch | Woodland judgment pdf; Hardimon pdf; Hart Postscript "role-responsibility" pdf; May Directed Duties pdf; Thompson pdf; Hardimon definition phrase | Found the National Archives judgment, the Thompson author PDF, the Moreau manuscript. No OA copy of Hardimon, Hart, May |
| 8 | Internet Archive advancedsearch | title (punishment and responsibility) AND creator hart | Four copies, all `access-restricted-item: true` |
| 9 | Unpaywall / OpenAlex locations | Cornell 2015, May 2015, Hardimon, Sreenivasan, Morgan, Vincent, Bradley | OA only for Cornell (UMich repository: Cloudflare 403; Wayback 429), Morgan (Cambridge repository: retrieved), Bradley (Cambridge: 429; SSRN: 403) |
| 10 | Full-text grep of Gredka-Ligarska 2025 (Utrecht LR, OA) | "non-delegable", "independent contractor", "Woodland" | No occurrence: this AI-liability paper works entirely through vicarious liability |

**Gap statement.** I found no peer-reviewed work that applies the tort doctrine of non-delegable duties, or the philosophy of role obligation, to a hotel or hospitality operator's use of automated systems. Searches: Consensus (queries 2–4), OpenAlex (query 5), Crossref, 10 Nov 2026; Scholar Gateway unavailable. The nearest work is a non-peer-reviewed preprint arguing that an Indian employer "may lawfully delegate the exercise of managerial judgment to a computational system, but it cannot delegate away legal responsibility" (Upadhyay & Joshi 2026, Zenodo 10.5281/zenodo.23156829, abstract only, not carded). The AI-liability literature I sampled routes the deployer's liability through vicarious liability or strict liability, not through a non-delegable duty (Gredka-Ligarska 2025, full text grep; Consensus query 3 abstracts).

## 2. Leads: outcomes

| Lead (FABLE §4(e), DEEP_RESEARCH_PLAN H2, brief) | Record | Read | Outcome |
|---|---|---|---|
| Hart, *Punishment and Responsibility*, Postscript (role-responsibility) | Crossref 10.1093/acprof:oso/9780199534777.003.0009, pp. 210–237 (2008 2nd ed.); OpenAlex abstract lists "role-responsibility" among its topics | No. OUP closed; IA copies lending-only | **Verified, not read.** Not carded. Known here only via Kropf et al. p. 2 and Santoni de Sio & Mecacci §2 |
| Hardimon 1994, "Role Obligations" | Crossref 10.2307/2940934, J. Phil. 91(7): 333–(363) | No (JSTOR only) | **Carded at metadata depth** (`hardimon1994role`). Fable's description (contractual vs non-contractual roles) is unverified; the definition circulating at p. 334 was seen only in secondary sources |
| Vincent 2011, "A structured taxonomy of responsibility concepts" | Crossref 10.1007/978-94-007-1878-4_2, pp. 15–35 | No (closed, no repository copy) | **Verified, not read.** Not carded. Kropf et al. quote her forward/backward questions (p. 2) |
| Non-delegable duty (Woodland v Swimming Teachers Association [2013] UKSC) | Primary source: [2013] UKSC 66, National Archives Find Case Law | **Full** | **Carded** `woodland2013uksc`. The case is reported as *Woodland v Essex County Council*; that "Swimming Teachers Association" was the lower-court name is unverified (the saved judgment does not show it). Fable's recollection ("when a duty holder remains liable for a function it has contracted out") is correct |
| Leading scholarship on non-delegable duties | Morgan 2015 CLJ (Crossref); Murphy 2007 and Stevens 2007 chapters in *Emerging Issues in Tort Law* (Crossref record for Murphy's chapter, 10.5040/9781472560070.ch-014); Beuermann 2017 Med L Rev; Brodie 2010 | Morgan **full** (AM); others no | **Carded** `morgan2015liability`. Murphy, Stevens, Beuermann, Brodie: records seen, not read, not carded |
| Darwall 2013 | held | re-read | **Upgraded** (4 quotes, Threat 3) |
| Thompson 2004 | Crossref 10.1093/oso/9780199261888.003.0014, pp. 333–384 | **Full** (author PDF with published running heads) | **Carded** `thompson2004wrong` |
| Wallace 2019, *The Moral Nexus* | Crossref 10.23943/princeton/9780691172170.001.0001 | Book and chapter abstracts only | Not carded. Abstract: moral demands "are directed to other individuals, who have claims that the agent comply" |
| Sreenivasan 2010, "Duties and their direction" | Crossref 10.1086/652303, Ethics 120: 465–494 | No | Verified, not read, not carded |
| May 2015, "Directed duties" | Crossref 10.1111/phc3.12239, Phil Compass 10: 523–532 | Abstract | Not carded. Abstract: three theories of direction (control, demand, interest), all facing "serious difficulties" |
| Cornell 2015, "Wrongs, rights and third parties" | Crossref 10.1111/papa.12054, PPA 43: 109–143 | Abstract (OA copy blocked) | Folded into `cornell2025wrongs` (abstract) with Cornell's 2025 book and Bradley 2026 |
| Feinberg 1970 (§7 Q10) | WS_B: Crossref record, closed | No | Not re-searched |
| Fiduciary theory, Goodin, Scheffler, Simmons (FABLE §4(e)) | not searched | — | Outside H2's questions; left to H1/H3 |
| Moreau, "Morality and Role Obligations" (found by search, not a Fable lead) | **No record found** in Crossref (author query, 30 works) or OpenAlex | **Full** (NYU Law PDF, 28 pp.) | **Not carded** (guard 1). It names "obligations of hosts to guests and guests to hosts" as institutional role obligations (ms pp. 2, 4) and calls a commander's duty "non-delegable" (ms p. 12). Cite only if it is published |

## 3. Synthesis

*Drafted by Claude for the authors to accept, rewrite or reject.*

### 3.1 What can be delegated (Q2)

**The law separates the work from the duty, and grounds the duty in an undertaking, not in control of the environment.** Lord Sumption's formulation is the cleanest statement available: the work required to perform a non-delegable duty "may well be delegable, and usually is. But the duty itself remains the defendant’s" [woodland2013uksc, para 7]. Such a duty has three features: it arises from "an antecedent relationship" with the claimant, it is "a positive or affirmative duty to protect", and it is "personal to the defendant" by virtue of that relationship [para 7]. What makes it personal is an assumed responsibility — the defendant must be taken to have assumed "responsibility for the exercise of due care by any one to whom he may delegate its performance" [para 11] — imputed where the claimant is in the defendant's "custody, charge or care" and "has no control over how the defendant chooses to perform" [para 23(2)–(3)]. Morgan's commentary puts the same structure in plainer words: "No duty of care can be delegated, but its performance may well be" [morgan2015liability, AM pdf p. 7]; what remains is "a duty to ensure that care is taken" [AM pdf p. 8].

**That ground differs from Kong's, though less than it first appears.** Kong grounds the deployer's retained answerability in "guidance control over the act of delegation" [kong2026delegation, p. 4], and also treats *assuming* a role as "itself an exercise of control" [p. 4]. Woodland likewise grounds the duty in an assumption of responsibility [woodland2013uksc, para 11], and it still treats control as essential, but control of a particular kind: the defendant is liable "not because he has control but in spite of the fact that he may have none", and the essential element is "control over the claimant for the purpose of performing a function for which the defendant has assumed responsibility" [para 24; see para 23(2)]. The two accounts are not strictly opposed. They reach the same conclusion — the delegator still answers — and differ on what is controlled: Kong's route runs through control of the *act of delegating*; Woodland's runs through a relation of *charge over the person received*. The paper's claim about the host is of the second kind.

**The law also draws a line the paper can use for the multi-firm question.** A party is not liable where "their own duty is not to perform the relevant function but only to arrange for its performance" [para 25(3)]; the Ministry of Defence escaped liability for a contracted hospital because it had not delegated "any function which the Ministry had assumed personal responsibility to carry out" [para 24]. *Perform* versus *arrange* is a test for which firm holds a duty: the operator that receives the guest, not necessarily the platform that sold the night. That application is my inference and needs H1/H3's innkeeper and holding-out material behind it.

**Role-obligation theory says less than the paper hoped, so far as it could be read.** Hart and Vincent were unreachable. Through Kropf et al., Vincent's account asks "What obligations are associated with the role of P?" [kropf2026blame, p. 2], and role duties are "specific obligations that would not exist without that role" [p. 3] which especially expand "positive duties" [p. 4 n. 3]. That supports the claim that the host role carries positive duties beyond general morality. It does not, on what was read, say what part of a role can be handed to another. The only located answer to that question is the law's: the performance passes, the assumed undertaking does not.

**Limits.** Woodland's category is built on "especially vulnerable or dependent" claimants — patients, children, prisoners, care-home residents [para 23(1)] — and the court warns against the exception "eating up the rule" [para 22]. An adult hotel guest is not obviously in that class, and the judgment never mentions inns or hotels (full-text search). Morgan adds that in contract the stricter duty is already the default [AM pdf p. 7], so a paying guest may need the tort doctrine less than a pupil does. Woodland makes the same point for paid services: "The responsibilities of fee-paying schools are already non-delegable because they are contractual, and the possibility of contracting out of them is limited by legislation" [woodland2013uksc, para 25(5)]. That the hotel's terms can narrow the duty is my inference, within that statutory limit. The paper should borrow the *structure* (delegable work, retained undertaking, ground in the relationship), not claim that English law already treats a hotel's duties to guests as non-delegable.

### 3.2 Standing without circularity (Q10)

**Darwall's definition builds in the accountability that the paper then defines through standing.** Darwall defines bipolar obligation through accountability: someone is obligated to another "just in case the obligee has the individual discretionary authority to make demands of the obligor ... and to hold the obligor personally accountable" [darwall2013bipolar, OSO abstract], and he glosses second-personal authority as "standing to address claims and demands and hold accountable" [p. 36]. Bradley names this family of views the "Obligation-Accountability Nexus" [cornell2025wrongs, Bradley 2026 abstract]. Darwall himself is not circular: he analyses bipolar obligation in terms of accountability, in one direction only. The loop arises when a paper takes standing from Darwall and then also defines accountability as answering someone with standing.

**Thompson supplies the relation without the accountability (my reading of his table, not his statement).** His bipolar forms — "X has a duty to Y to do A", "X has a right against Y", "X wronged Y by doing A" [thompson2004wrong, p. 335] — fix who owes what to whom; none of them, on my reading, mentions answering. Thompson's objection to Rawls points the same way: on Rawls's account all participants "are positioned to charge the promisor", and that is why the account misses the promisee "to whom the promisor had a duty" [p. 339]. Being placed to charge is not what makes someone the party owed. One counterweight: in the legal key Thompson's persons "are defined as possible parties to a lawsuit" [p. 352]. He sets them against "merely monadic" forms such as "X has a duty to do A" [p. 338], which is the distinction the paper needs between a hotel's general duties (e.g., to comply with regulation) and its duty *to the guest*. The same relation can be "sung" in different keys — legal, ludic, moral [p. 352] — and a corporation can be a "jural or legal person" in such an order [p. 355]. So a hotel company can be the obligor in a commercial order of right, and the guest the party to whom it owes.

**Two published lines keep the claim apart from the power to press it.** Darwall himself concedes that "an obligee or right holder need not actually claim her right or demand compliance with it in order for the right to exist" [darwall2013bipolar, p. 35]. Liau builds a book on the legal version: "who can enforce a right?" and "who has the right?" are "a separate distinct question" [liau2023standing, pdf p. 1]; in tort, the primary right, the secondary right to damages and the power to sue can "be split up" [pdf p. 7]. Cornell argues at book length that wrongs and rights are "fundamentally distinct moral phenomena" [cornell2025wrongs, publisher abstract; abstract only]; Bradley reads this as separating accountability practices, rooted in wrongs, from obligations, rooted in rights [Bradley 2026 abstract, in cornell2025wrongs]. One terminological hazard: Liau's "standing" *is* the enforcement power [pdf pp. 1, 5] — the paper's "exercised" side — so the paper must flag its own usage or a legally trained reader will see the circle again.

### 3.3 Proposed non-circular definitions

*Drafted by Claude. Each term is defined only from terms above it. The grounding source is named; anything not in the source is marked as the paper's own step.*

| # | Term | Proposed definition | Grounded in |
|---|---|---|---|
| 1 | **Obligation** (first-order) | A directed duty the host owes *to* the guest — to receive, protect, attend to and hear the guest — which arises when the host undertakes to receive a person into its charge | Directed form: thompson2004wrong p. 335. Arising from an undertaking towards someone in one's charge: woodland2013uksc paras 7, 11, 23(2). The content list and the application to hosting are the paper's own (H1 to ground). H1 found that the duty to *receive* binds before any reception, on the holding-out, and that the remaining duties are fixed at admission (maese2015rethinking p. 501); "arises when the host undertakes to receive" fits the second group only |
| 2 | **Standing (held)** | The guest's position as the party to whom obligation (1) is owed — the correlative claim | thompson2004wrong p. 335 ("X has a right against Y"); hohfeld1913fundamental pp. 32–33. Holds whether or not it is claimed: darwall2013bipolar p. 35 |
| 3 | **Standing (exercised)** | The guest's actually pressing that claim — asking, objecting, requesting an exception — to a party able to receive it | darwall2013bipolar pp. 31–32 (insist, complain, seek apology); the legal analogue is liau2023standing's enforcement power (pdf pp. 1, 5). "Able to receive it" (reachability) is the paper's own addition (WS_B Threat 2) |
| 4 | **Responsibility** | The holder's retained duty to see that obligation (1) is performed by whoever does the work — staff, contractor or system | woodland2013uksc paras 5, 7; morgan2015liability AM pdf pp. 7–8 ("a duty to ensure that care is taken") |
| 5 | **Authority** | The power, assigned by the organisation, to change the decision or the rule in a given case | The definition is the paper's own (with H4's evidence on bounded frontline authority). woodland2013uksc para 25(1) uses "authority" in another sense, the school's authority *over the pupil*, and ties that to answerability for its delegated exercise; it does not ground authority over a decision or rule |
| 6 | **Accountability** | The second-order arrangement through which the holder of (4) answers to the guest for how (1) was performed, and through which (3) can be exercised | bovens2007accountability pp. 450, 452 (actor answers, forum questions); kong2026delegation pp. 3–5 (answerability stays with the delegator). Kept distinct from (1)–(2): cornell2025wrongs (abstract); thompson2004wrong p. 339 (being placed to charge is not being the one owed; my reading) |

The order breaks R2.3's loop. Standing (2) is fixed by the obligation (1) and mentions no answering. Accountability (6) is defined last, from (1), (3) and (4). The paper's diagnosis can then be stated without the circle: under algorithmic mediation the guest still *holds* standing (2), because the host's obligation persists — the paper's own application of Woodland's structure (para 7), which says nothing about hosts or hotels; what fails is the *exercise* (3), because accountability (6) offers no one with authority (5) to receive it.

## 4. What this means for the paper's position (FABLE_REVIEW §5)

- **Institutional role obligation (C) is strengthened in structure but not in source.** Woodland and Morgan give C its missing delegation rule (tasks pass, the undertaken duty does not), and Thompson gives it a commercial "key" in which a corporation can be the obligor. But the philosophy of role obligation itself (Hart, Hardimon, Vincent) remains unread, and Kong's control-based account is the only full-text role theory in the library. If C is chosen, its ground on the page will be the *assumption of responsibility* (Woodland), not "the role" in the abstract. Woodland's assumption is "imputed" by law (para 11), and H1's legal history rejects an undertaking as the ground of the innkeeper's duty: "English law, not the innkeeper's express commitment, imposed the duty" (bogen1996innkeeper, p. 75; p. 52). The two workstreams therefore ground C differently.
- **Public calling (B) gains a bridge.** Woodland's ground — an undertaking towards a person received into one's charge — is close to the innkeeper's holding-out-and-receiving trigger that H1 is testing, and its "perform versus arrange" line (para 25(3)) is the delegation rule B needs. Woodland does not mention innkeepers, so the link must come from H1's sources.
- **Threshold sovereignty (A) gets no support from Woodland's second category, and some from its first.** For duties arising from a relationship, Woodland rejects control of the environment as the essential element and puts "control over the claimant" in its place (para 24). For the hazard and nuisance cases it affirms that control of the environment is "a fundamental feature" (para 24) and that the duty is personal because of "the defendant’s occupation of the land" (para 12). Woodland says nothing about hosts, so it does not decide A. It shows that the retained-duty structure the paper borrows runs through charge over the person, not control of the space.
- **Against Kong (R2.2e).** The paper can now say what it adds: Kong conserves answerability through control over the act of delegating (p. 4); the paper's duty is a first-order, directed, positive duty that stays with the party who undertook to receive the guest (the paper's application of Woodland paras 7, 24, which concern schools and hospitals) — before any harm, and owed *to* someone (Thompson p. 335).
- **R2.4 honestly answered.** The non-delegable category is the law of hospitals and schools (Woodland paras 14–16, 23); the judgment does not place hotels in it, so the paper borrows the structure from those settings. Hospitality is not unique on this axis — which the September panel already found. What hospitality may add (from H1) is the holding-out trigger and the duty to receive.

## 5. Reviewer points answered and sources recommended (cap 3)

| Reviewer point | Answered by |
|---|---|
| R2.2c (what can / cannot be delegated) | woodland2013uksc paras 7, 11, 23–25; morgan2015liability AM pp. 7–8 |
| R2.1b (why it remains after delegation) | woodland2013uksc paras 7, 11, 34 (undertaking); kong2026delegation p. 5 (already held) |
| R2.3a (circularity) | thompson2004wrong pp. 335, 338; darwall2013bipolar OSO abstract and p. 36 (diagnosis); cornell2025wrongs (abstract) |
| R2.3b (held vs exercised) | darwall2013bipolar p. 35; liau2023standing pdf pp. 1, 5, 7 |
| R2.2e (vs Kong / algorithmic accountability) | woodland2013uksc para 24 against kong2026delegation p. 4 |

**Recommended to enter (cap 3), ranked:**
1. `woodland2013uksc` — the delegation rule and its ground (R2.2c, R2.1b, R2.2e). Full text.
2. `thompson2004wrong` — the directed relation defined without accountability (R2.3a). Full text.
3. Third slot, authors choose: `morgan2015liability` (a scholarly gloss on the doctrine; full text) **or** `liau2023standing` (held vs exercised in law; introduction only). I lean to neither until the authors decide whether the paper needs a second legal source; Darwall p. 35, already held, covers held-versus-exercised.

Held, not recommended now: `cornell2025wrongs` (abstract), `hardimon1994role` (metadata). Upgraded: `darwall2013bipolar`, `kropf2026blame`. Not upgraded (nothing new read): `kong2026delegation`, `hohfeld1913fundamental`, `santonidesio2021gaps`, `nissenbaum1996accountability`.

**Proposed claim ids** (CLAIMS.md not edited): `duty-stays-work-moves` — the work of hosting can be handed to staff, contractors or systems; the undertaken duty stays with the party that assumed it (structure from woodland2013uksc para 7; the application to hosting is the paper's); `standing-defined-before-accountability` — standing is the guest's position as the one owed the host's duty, defined without reference to answering; accountability is the later arrangement through which it is exercised (thompson2004wrong p. 335; darwall2013bipolar p. 35 for held-versus-exercised only, since Darwall's same paragraph ties bipolar obligation to the obligee's authorities).

## 6. For the verifier — look hardest at

1. **Woodland's scope.** Every use must stay with the structure, not imply that hotels already owe non-delegable duties (paras 22–23(1); no mention of inns).
2. **Thompson pagination.** The author PDF carries the printed running heads; spot-check pp. 335, 338, 352, 355 against the OUP volume, and settle 2004 versus 2006 for the volume's year.
3. **Darwall's abstract quote** is from the OSO chapter abstract, not the printed chapter; cite it as such or replace it with p. 36.
4. **Liau and Morgan locators** are eprint/AM pages. Liau's "general standing rule" quote (pdf p. 5) is set in a two-column box in the eprint; the words are exact, the layout interleaves a label.
5. **Kropf's Vincent quotes** are second-hand for Vincent; do not cite Vincent from them.

## Corrections after verification

*Added in rr-2026-11-h after VERIFY_H_v1 (2026-11-10).*

- §3.2: "the circle … is inside the paper's main source" reworded; Darwall is not himself circular, and the loop arises only if the paper also defines accountability through standing (VERIFY_H_v1, WS_H2 finding 1).
- §3.1: "Woodland holds the reverse" of Kong narrowed; both ground the role in assumption, and the difference is control of the act versus charge over the person (finding 2).
- §3.3: "host's obligation persists [woodland para 7]" marked as the paper's application; Woodland says nothing about hosts (finding 3).
- §3.2: Thompson's monadic example changed from duties "to a regulator" (bipolar in his terms) to "to comply with regulation" (finding 4); "relation without the accountability" labelled as my reading (finding 5).
- §3.2: "accountability practices" attributed to Bradley's gloss, not Cornell's abstract (finding 6).
- §2: "Swimming Teachers Association" as the lower-court name marked unverified (finding 7).
- §5: Darwall p. 35 limited to held-versus-exercised in the proposed claim (Darwall card note on p. 35).

## Fable corrections

Fable-checked rr-2026-11-h (2026-11-10). I read this file in full against woodland2013uksc, thompson2004wrong, morgan2015liability, liau2023standing and darwall2013bipolar as corrected, and against their saved sources. The seven corrections above are right. I did not re-check the Kong, Kropf, Bovens, Cornell or Bradley material, which is outside my list. I changed the following.

1. **§3.1, first heading.** "not in control" became "not in control of the environment". Para 24 keeps "control over the claimant" as "the essential element"; the paragraph below already said so and the heading did not.
2. **§3.1, Limits.** "the hotel's terms can narrow it" was stated as fact. It is an inference, and Woodland para 25(5) says contracting out of a paid provider's responsibilities "is limited by legislation". Para 25(5) is now quoted: it is the judgment's own statement that paid services are non-delegable by contract.
3. **§3.2, Thompson.** Added p. 339 (being placed to charge the promisor does not single out the promisee) as located support for the reading, and p. 352 (persons defined as possible parties to a lawsuit) as its counterweight. §3.3 row 6 now cites p. 339, not p. 335, for keeping accountability distinct.
4. **§3.3 row 5, Authority.** Woodland para 25(1) speaks of authority over the pupil, not authority over a decision or rule. The row no longer cites it as ground for the definition.
5. **§3.3 row 1, Obligation.** Noted that H1's sources put the duty to receive before reception; "arises when the host undertakes to receive" covers only the duties fixed at admission.
6. **§4, Position C.** Added that Woodland's assumption is imputed by law and that Bogen (H1) rejects an undertaking as the ground of the innkeeper's duty.
7. **§4, Position A.** "is weakened" outran the card. Woodland affirms control of the environment and occupation of land as the ground of its first category (paras 12, 24) and is silent on hosts. Reworded.
8. **§4, Against Kong; §4, R2.4; §5, proposed claim id.** Three further places cited Woodland for a statement about hosts or implied that hotels sit in the non-delegable category (the scope breach VERIFY_H_v1 finding 3 caught once). Each is now marked as the paper's application.
