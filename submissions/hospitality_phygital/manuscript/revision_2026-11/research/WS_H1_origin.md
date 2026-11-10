<!-- Drafted by Claude (Opus 5.5), workstream H1, run rr-2026-11-h, 10 Nov 2026. None of this is the authors' wording. No manuscript, plan, bib, CLAIMS or index file edited; nothing committed. -->

# WS H1 · Where the host's obligation comes from

10 November 2026 · run rr-2026-11-h · questions Q1, Q4, Q5 (FABLE_REVIEW §7) · reviewer points R2.1, R2.2a–b, R2.4, R3.11

## 0. Conflicts flagged before acting

1. **Card vocabulary.** RUN_BRIEF_H asks for `verified: primary-legal-source | catalogue-verified` and `read_depth: full`. `library/build_index.py` accepts only `verified ∈ {verified, crossref-verified, corrected}` and `read_depth ∈ {full-text, abstract, metadata}`. I followed the validator, as `eu2024aiact` already does, and wrote "primary-legal-source" into each statute or case card's `source_basis`.
2. **Validator and the bib.** Every new card fails `build_index.py --check` with "not in references.bib", and the crossref-verified ones also fail "bib note does not" say crossref-verified. The brief forbids me to edit `references.bib`, so the main session has to add the entries or keep the cards out of the check. No other validator error comes from my cards. I did not run `build_index.py` in write mode, because that rewrites `CARDS_INDEX.md`.
3. **Assigned card that did not exist.** No card existed for King, Telfer or O'Gorman. I created `king1995what` (abstract), `telfer1995hospitableness` (metadata) and `ogorman2009origins` (full text, read by WS_A on 8 Nov). I count none of the three against the cap.

## 1. What I searched

All on 10 Nov 2026.

| # | Tool | Exact query or target | Hits considered | Kept |
|---|---|---|---|---|
| 1 | Consensus | `innkeeper common law duty to receive guests hospitality management host obligation` (page_size 40) | 39 | Bogen 1996; Ganesh 2018. Logged, not carded: Molot 1968; Sherry's *Cornell Quarterly* law columns (1964–95); Othman et al. 2018 (Malaysia); Hussain & Abdullah 2013 |
| 2 | Consensus | `hospitableness commercial hospitality host virtue motive obligation Telfer Lashley` (40) | 40 | Abstract-level evidence only for §4 Q5: Blain & Lashley 2014; Lashley 2015; Lashley 2008; Ramdhony & D'Annunzio-Green 2018; Line et al. 2025; Poulston 2015 |
| 3 | Consensus | `what distinguishes hospitality from other services banking healthcare duty of care guest bodily presence premises` (30) | 30 | King 1995 (abstract); healthcare-hospitality reviews logged |
| 4 | Consensus | `host obligation in commercial hospitality as an organisational or role duty rather than individual hospitableness` (25) | 25 | Lashley 2014 editorial (abstract); Poulston 2015 (abstract); Lugosi 2014 (held) |
| 5 | Consensus | `innkeeper duty compared with fiduciary duties of banks and duties of hospitals and common carriers duty to serve` (20) | 20 | Logged: Colyer 1966; Arterburn 1927; Hall 2019 (hospitals not fiduciaries); McMeel 2021 (bank–customer at arm's length); Beuermann 2017 (H2); Boone et al. 2021 (H3) |
| 6 | Scholar Gateway | Q5 natural-language query | — | **Failed: ACCESS_DENIED.** That corpus was not searched |
| 7 | OpenAlex | title_and_abstract search for `innkeeper`, `common calling`, `duty to receive`, `public accommodation`, filtered to ISSNs of *Hospitality & Society*, IJHM, IJCHM, *Annals*, CHQ, JHTR, RHM | 13 / error / 1 / 14 | None uses the doctrine to ground host obligation (§5 gap statement) |
| 8 | OpenAlex | `No Right to Exclude…`, `Hotel: An American History`, `law of innkeepers and hotels`, `hospitality law innkeeper duty to receive guests` | 24 | Bogen 1996 (found here first, with OA link) |
| 9 | Crossref | bibliographic queries for every FABLE §4(a) and §4(d) lead (§2 below) | — | Records listed in §2 |
| 10 | Unpaywall / Semantic Scholar | DOIs of King, Telfer, Lashley 2000, Lashley 2015, Blain & Lashley, Germann Molz 2026, Sandoval-Strausz, Wyman, Burdick, Ganesh, Maese, Poulston | — | Sandoval-Strausz (bronze), Maese (green) |
| 11 | Primary law | legislation.gov.uk (via Wayback; the live site returned HTTP 202 with no body), Cornell LII, Caselaw Access Project (static.case.law), Internet Archive (Coke's Reports 1777; Modern Reports XII 1769), JSTOR Early Journal Content | — | HPA 1956 s 1; OLA 1957 s 2; EqA 2010 s 29; PAR 2015 regs 18–19; 42 USC 2000a; 42 USC 1395dd; Heart of Atlanta; Calye's Case; Lane v Cotton |
| 12 | WebSearch | Lane v Cotton text; Constantine judgment text; Singer 1996 PDF; Lashley 2015 PDF | — | Leads to the routes above; no full text for Constantine, Singer or Lashley 2015 |

**Blocked routes, not bypassed.** BAILII (Anubis bot check), Cambridge Core (HTTP 429; used the Wayback copy), Taylor & Francis and AJOL (403 / empty), Intellect (Cloudflare), SSRN (403), Justia and the LoC U.S. Reports PDF (403), CourtListener (needs authentication), Revista Hospitalidade (timeout). The Chrome extension was not connected.

## 2. Fable leads: outcomes

**Tradition (d), legal history**

| Lead | Outcome |
|---|---|
| *Calye's Case* (1584) | **Verified**, read (8 Co Rep 32a, 1777 translation). **Content differs from the Fable gloss:** the innkeeper keeps "the goods and chattels of his guest, and not his person" (fol. 33b). The 1584 duty did not include the guest's safety |
| *Lane v Cotton* (1701) | **Verified**, read (12 Mod 472, 484–485). The innkeeper passage is Holt CJ **dissenting** |
| *Constantine v Imperial Hotels* [1944] KB 693 | **Record found, text not read.** Only secondary sources reached me (Wikipedia; Colyer 1966 abstract, which calls it the one reported case). BAILII and ICLR were blocked. Not carded |
| Hotel Proprietors Act 1956 | **Verified, and the wording matches the Fable recollection** (s 1(3)). Carded |
| Occupiers' Liability Act 1957 | **Verified** (s 2). Carded as a governor: the safety duty is owed by every occupier |
| Civil Rights Act 1964 Title II; *Heart of Atlanta* | **Verified**, both read and carded |
| Wyman 1904; Burdick 1911 | **Verified** (Crossref), Part I of each read in full |
| Beale, *Law of Innkeepers and Hotels* (1906) | **Record exists** (reviews: Yale LJ 10.2307/785526; Columbia LR 10.2307/1110030). Book not read |
| Singer 1996, *No Right to Exclude* | **Citation attested** (90 Nw U L Rev 1283; cited by Sandoval-Strausz p. 63 n. 15 and a 2025 amicus brief). No DOI or full text reached. Not carded |
| Sandoval-Strausz 2005 (LHR) | **Verified, read; content as Fable guessed.** Carded |
| Sandoval-Strausz, *Hotel: An American History* (2007) | **Record exists** (book reviews in Crossref, e.g. 10.1086/ahr.113.5.1517-a; a chapter DOI 10.12987/9780300149999-011). Not read |
| *Woodland v Swimming Teachers* [2013] | Not searched: H2's remit |
| Platforms as common carriers or public accommodations | No specific work found. Maese 2015 (student note) applies innkeeper law to Airbnb hosts. Carded, low rank |

**Tradition (a), hospitality studies**

| Lead | Outcome |
|---|---|
| Telfer 1995; Telfer 2000/01 chapter | **Records exist** (10.1080/05568649509506530; 10.1016/b978-0-7506-5431-9.50007-x, Crossref year 2001). Closed. Metadata card |
| Telfer, *Food for Thought* | **Record exists** (10.4324/9780203002308; Crossref gives the 2012 reissue). Not read |
| King 1995 | **Verified** (IJHM 14(3–4), 219–234). Abstract only. **The abstract does not state the obligation that Xiang et al. attribute to King**, and it frames the paper around hospitals adopting hospitality |
| Lashley 2000 | Crossref: pp. **1–17** (card said 1–16), year **2001**. Closed. Still metadata |
| Selwyn 2000 | **Record exists** (pp. 18–37, 10.1016/b978-0-7506-5431-9.50006-8). Not read |
| Brotherton & Wood 2000 | Crossref lists the *In Search of Hospitality* chapter (pp. 134–156) under **Brotherton alone**. Noted on `brotherton1999towards` |
| Lashley, Lynch & Morrison 2007; Ritzer 2007 | **Records exist** (10.4324/9780080465692; Ritzer pp. 129–139). Not read |
| O'Gorman 2009 | Read (WS_A copy). **Carded.** It does not discuss innkeeper law |
| O'Gorman 2010 book | **Record exists** (10.23912/978-1-906884-08-6-990). Not read |
| Germann Molz & Gibson | **Record exists**, but Crossref gives the Routledge 2016 edition (10.4324/9781315595795), not 2007. Not read |
| Aramberri 2001 | **Verified** (*Annals* 28(3), 738–761). No abstract. Not read |
| Lashley 2015; Blain & Lashley 2014; Tasci & Semrad 2016 | **Records exist** (Tasci & Semrad: IJHM 53, 30–41). Abstracts read for the first two, none for the third. Full text blocked (T&F/AJOL) |
| Bell 2007 | **Record exists** (*Progress in Human Geography*). Not read (R3.8; H5/H3) |

## 3. Card ledger

**New (status `held`, `generated_run: rr-2026-11-h`)**

| Citekey | Depth | Rank for entry |
|---|---|---|
| `uk1956hotel` | full-text | **1** |
| `sandovalstrausz2005travelers` | full-text | **2** |
| `bogen1996innkeeper` | full-text | **3** |
| `us1964civilrights` | full-text | **4** |
| `heartofatlanta1964motel` | full-text | 5 |
| `lane1701cotton` | full-text | 6 |
| `calye1584case` | full-text | 7 |
| `burdick1911origin` | full-text (Part I) | 8 |
| `wyman1904law` | full-text (§§ I–II) | 9 |
| `ganesh2018wirtbarkeit` | abstract | 10 (read first) |
| `maese2015rethinking` | full-text (§§ III.B–IV) | 11 |
| `uk1957occupiers`, `uk2010equality`, `uk2015payment`, `us1986emtala` | full-text | governors for R2.4; not for entry |
| `ogorman2009origins`, `king1995what`, `telfer1995hospitableness` | full / abstract / metadata | records of sources already in the outline |

**Upgraded (assigned):**
- `lashley2000towards`: DOI added, pages and year corrected, still metadata.
- `germannmolz2026`: three abstract quotations added, still abstract.
- `shryock2012breaking`: five new located quotations on commerce and on guests.
- `brotherton1999towards`: authorship note added.

## 4. Synthesis

### Q1. What brought the innkeeper's duties into force, what they contained, who bore them

**Activation.** The common law bound the *common* innkeeper, the one who kept a house open to travellers. It did not bind someone who lodged a friend: a private host whose servants rob the lodger "shall not answer for it" [calye1584case, fol. 32a]. By the eighteenth century the courts stated the activation as a profession or holding-out. Holt CJ put it as having "made Profession of a Trade which is for the Publick Good" [lane1701cotton, 12 Mod at 484]. In Blackstone's formulation, an innkeeper who "hangs out a sign and offers his house for travellers" makes "an implied engagement to entertain all persons who travel that way" [burdick1911origin, p. 518]. In 1623 Chamberlaine J said that putting up a sign and lodging travellers sufficed [bogen1996innkeeper, p. 88]. English statute now states the activation in one sentence. A hotel is "an establishment held out by the proprietor as offering food, drink and, if so required, sleeping accommodation, without special contract, to any traveller presenting himself who appears able and willing to pay a reasonable sum … and who is in a fit state to be received" [uk1956hotel, s 1(3)].

The trigger therefore has two sides:
- the host's holding-out;
- the guest's presenting, under conditions on the guest (traveller, able to pay, fit).

Capacity limits it. Holt said "If the Inn be full … the Action would not lie" [lane1701cotton, p. 484]. US law adds a second step, admission. Once a guest "presents himself" and is accepted, the parties' rights and duties "are at once fixed by law rather than by contract" [maese2015rethinking, p. 501, a student note citing Beale].

**Content.** Sandoval-Strausz gives the standard summary: "bed, board, and hearth" [sandovalstrausz2005travelers, p. 63]. These are three duties:
- to receive any traveller willing to pay;
- to provide food;
- to keep the guest's property safe.

The third was strict. The innkeeper "is bound in law to keep them safe without any stealing or purloining" [calye1584case, fol. 33a], and later answered even for "other guests or any unidentified party" [sandovalstrausz2005travelers, p. 65].

**What the old duty left out.** It did not cover the guest's body: the innkeeper keeps the guest's goods "and not his person" [calye1584case, fol. 33b]. A duty to protect the guest's person is a later addition. US law states it as "an affirmative duty to exercise reasonable care in the protection of the guest" [maese2015rethinking, p. 503]. English law states it as the occupier's "common duty of care" to *all* visitors [uk1957occupiers, s 2(1)–(2)].

**Holder.** The innkeeper, answering for the servants who did the work. He is charged for "a default in him or his servants" [calye1584case, fol. 33a], and "answerable not only for the acts or negligence of his servants" [sandovalstrausz2005travelers, p. 65]. Statute fixes the holder by name. The duties "attach to the proprietor of such an hotel and shall not attach to any other person" [uk1956hotel, s 1(1)].

**Why the law imposed it: disputed.** I found four accounts in the legal-historical literature:
- *Holding out as a general undertaking* [burdick1911origin, pp. 515–516, 522].
- *Virtual monopoly and the traveller's dependence*: "the traveller is so in the hands of the innkeeper that only an affirmative law can protect him" [wyman1904law, p. 159].
- *The vulnerability of travellers away from home* [sandovalstrausz2005travelers, pp. 62–63], who disagrees with Singer's public-calling ground [p. 63 n. 15].
- *Crime control and strict liability for goods.* Bogen calls the undertaking theory "not so much a theory as a tautology" and the public-office analogy "a product of duties imposed rather than a cause of them" [bogen1996innkeeper, p. 52]. He concludes that the duty to serve "was incidental to the innkeeper's liability for losses of his lodgers" [p. 91].

On one point the four agree. Once imposed, the duty belonged to a status that a person entered by entering the trade: "the obligation became an element of the status of an innkeeper" [bogen1996innkeeper, p. 52]. Innkeepers "do not deal upon contracts as others do" [Eyre J in *Newton v Trigg*, quoted in bogen1996innkeeper, p. 90].

**Into public-accommodation law.** The Supreme Court called state public-accommodation laws codifications of "the common-law innkeeper rule" [heartofatlanta1964motel, 379 U.S. at 261]. Title II lists "any inn, hotel, motel, or other establishment which provides lodging to transient guests" first. It also exempts owner-occupied buildings with five or fewer rooms [us1964civilrights, § 2000a(b)(1)]. Bogen gives the modern function of the right of access as "to protect against discrimination" [bogen1996innkeeper, p. 91]. Sandoval-Strausz shows how the traveller's "duties and privileges had to be turned into rights" before that could happen [sandovalstrausz2005travelers, p. 54].

**Has a hospitality scholar used the doctrine to ground host obligation?** No, as far as these searches reach. I found no work in *Hospitality & Society*, IJHM, IJCHM, *Annals of Tourism Research*, *Cornell Hospitality Quarterly*, JHTR or *Research in Hospitality Management* that uses the innkeeper's common-law duty to ground the host's obligation. The searches were OpenAlex title/abstract searches for "innkeeper", "duty to receive" and "public accommodation" restricted to those ISSNs (the "common calling" query returned an error), plus Consensus queries 1, 4 and 5 in §1, all on 10 Nov 2026. Scholar Gateway was unavailable.

What does exist:
- Practitioner law columns in hospitality journals describe the duties without theorising them, for example Sherry in CHQ and Alberto in JHTR (titles only, from Consensus).
- O'Gorman (2009) notes "increasing legal control" of the trade [ogorman2009origins, pdf p. 11] but does not discuss innkeeper law.
- Ganesh (2018), a legal theorist, joins the innkeeper to Kant's hospitality. His abstract states that for innkeepers hospitality "is a legal obligation, not a matter of philanthropy" [ganesh2018wirtbarkeit, abstract].

### Q4. Banks, hospitals, retailers: what remains distinctive of hosting

Reviewer 2 is right that pre-harm duties are not unique to hospitality. Today:
- every UK service provider "must not discriminate against a person requiring the service by not providing the person with the service" [uk2010equality, s 29(1)];
- banks may not discriminate when consumers "apply for or access a payment account" [uk2015payment, reg 18(1)];
- a US hospital emergency department must screen "any individual" who "comes to the emergency department" and asks [us1986emtala, § 1395dd(a)];
- every occupier owes every visitor a duty of reasonable care for safety [uk1957occupiers, s 2(2)].

The paper's first differentiator, "prior to harm" (PO §2.3), therefore does not separate the hotel from R2's comparators. The second, "includes the exception", gets no support from the law I read. The occupier's duty can be varied "by agreement" [uk1957occupiers, s 2(1)], which is a general power, not something owed. The innkeeper's duty contains no negotiated exception.

Three things remain distinctive on the evidence read:

1. **A historically special status for the trade.** The general duty to serve all comers once bound several common callings. It "now attached only to common carriers by land and water (including ferrymen) and innkeepers" [burdick1911origin, p. 523]. The shopkeeper stayed free to refuse [wyman1904law, p. 159]. Modern anti-discrimination statutes have since narrowed the gap.
2. **What is received.** The hotel receives the stranger's body and belongings into its house overnight. The duty is owed to a traveller "away from their home communities and in unfamiliar surroundings" [sandovalstrausz2005travelers, pp. 62–63] for the length of a stay ("bed, board, and hearth", p. 63). By contrast, the hospital's statutory duty is triggered by an emergency and ends at stabilisation or transfer [us1986emtala, § 1395dd(b)(1)].
3. **A duty fixed by status rather than contract** once the guest is received [bogen1996innkeeper, p. 90; maese2015rethinking, p. 501].

None of the three is "obligation" as such. A one-line concession to R2.4 is accurate on this evidence: the mechanism is general, and hospitality contributes a status whose duties to the person received are old, specific and enforced. That matches FABLE_REVIEW §5, Recommendation, point 2.

Comparative scholarship found at abstract level only:
- Hall (2019): courts do not treat hospitals as fiduciaries.
- McMeel (2021): the orthodox bank–customer relation is at arm's length.
- King (1995): the field's most cited source for the host's obligation was written about hospitals adopting hospitality [king1995what, abstract].

### Q5. Virtue or role, and how commerce is reconciled

Most of this section rests on abstracts. Every full text in this line was closed or blocked (Telfer, King, Lashley 2000, Lashley 2015, Blain & Lashley 2014).

At abstract level, the hospitableness literature treats the host's duty as a *personal disposition or motive*, measured in individuals:
- Blain & Lashley (2014) describe "differences amongst individuals in the commitment to being hospitable", hosts "not motivated by ulterior motives", and an instrument "to measure the strength of genuine hospitality in individuals" (abstract).
- Lashley (2015) describes "a research instrument that can be used to identify those individuals who are driven by a personal desire to be hospitable to others" (abstract).
- The held full text of Liu et al. agrees: hospitableness is "a host's disposition to care for a guest without expectation of reciprocity" [liu2026hospitableness, p. 2].
- Golubovskaya et al. treat hospitality as "an attitude and spirit with which service is performed" [golubovskaya2017meaning, p. 1287].

The same line names obligation, but as a *social* duty now weakening. Lashley's 2014 editorial calls "the duty of the host to welcome and protect guests … a central feature of human morality" and says these "obligations no longer have the central importance that they once did" (abstract). Blain and Lashley (2014) note "changing levels of obligation to be hospitable" (abstract).

Commerce gets reconciled in three ways:
- **Selecting hospitable people.** Lashley 2015's instrument; Ramdhony & D'Annunzio-Green 2018, on transposing hospitableness "to commercial settings without a wholesale erosion of its altruistic and moral core" through talent management (abstract).
- **Denying that commercial hospitality is necessarily inauthentic.** Lashley 2008: "not inevitable that commercial hospitality is necessarily inauthentic" (abstract).
- **Locating the moral duty in the server's intrinsic motive.** Poulston 2015, in *Hospitality & Society*: "the transactional nature that pervades what is essentially a moral duty", with motives "primarily intrinsic" (abstract).

I found no hospitableness work that assigns the host's duty to an organisation or a role. The search covered Consensus queries 2 and 4 (§1), 10 Nov 2026; Scholar Gateway was unavailable. The only located statement that the commercial host's hospitality is an obligation rather than a disposition comes from outside the field: Ganesh's legal theory (abstract) and the law itself.

Shryock, read in full, adds a warning. He hands the care of strangers to "the hospitality industry" [shryock2012breaking, p. S30]. He then describes host–guest relations in that sphere as "depersonalized, formulaic, monetized, and designed to insulate all parties from the risks and inconveniences of sharing" [pp. S30–S31], and his informants "would never confuse karam with the hospitality offered to tourists" [p. S31].

## 5. What this means for the three positions (FABLE_REVIEW §5)

**Position B, public calling: half-supported.**
- *Supported as activation and holder.* Holding out plus a presenting traveller activates the duty [uk1956hotel, s 1(3)]. The proprietor holds it and answers for servants [s 1(1); calye1584case, fol. 33a]. The duty was special to innkeepers and carriers [burdick1911origin, p. 523]. These are documented facts, and they answer R2.1a, R2.1c, R2.2a–b and part of R2.4.
- *Weakened as justification.* The best legal history denies that holding out explains the duty [bogen1996innkeeper, p. 52]. The paper can say *what* brings the duty into force and *who* holds it. It cannot say the law shows *why*.
- *Thin in content.* Goods, not the person [calye1584case, fol. 33b]. No exception, no explanation. The innkeeper's duty in the old law was not a duty of welcome.

**Position C, institutional role obligation: strengthened.**
- The law treats innkeeping as a *status* entered by taking up the trade, with duties "fixed by law rather than by contract" [bogen1996innkeeper, pp. 52, 90; maese2015rethinking, p. 501].
- The holder answers for those who perform [calye1584case, fol. 33a; sandovalstrausz2005travelers, p. 65].
- That is role obligation with a delegation rule built in, which is what R2.2 asks for.
- The hospitableness literature does not supply the role; at abstract depth it supplies the rival (personal virtue). C therefore has to state its difference from the Telfer–Lashley line, and it can now point to a non-hospitality source (law) for the claim that the commercial host's duty is an obligation of a status, not a virtue.

**Position A, threshold sovereignty: weakened as ground, kept as rationale.**
- *For:* Wyman's dependent traveller [p. 159] and Sandoval-Strausz's vulnerable stranger [pp. 62–63] support A's *rationale*, the guest in another's house.
- *Against, on the holder:* the law did not put the duty on whoever controls the space. It put it on the innkeeper as such, and today on "the proprietor … and … not … any other person" [uk1956hotel, s 1(1)]. Control and holder can come apart.
- *Against, on Shryock:* the outline's main anthropological source now cuts against carrying karam's obligation over to the industry [shryock2012breaking, pp. S30–S31].

**Net.** H1 supports FABLE_REVIEW §5's recommendation: C as the frame, B for activation, holder and delegation evidence, A as description. It adds two constraints:
- do not claim the law explains *why* the commercial host is bound;
- do not claim the legal duty was a duty of welcome or of personal safety.

**Repairs to the outline (for the authors):**
1. PO §2.1 "Lashley (2000) holds…": still second-hand.
2. PO §2.1 "Commercial thresholds have historically guaranteed 'protection, sanctuary and security' (O'Gorman 2009)": an uncited conclusion sentence [ogorman2009origins, pdf p. 11].
3. PO §2.3 "Prior to harm": does not separate hospitality from banks or hospitals (Q4 above).
4. Pitch l. 21 "simply because they walked in the door": contradicted by the statutory conditions [uk1956hotel, s 1(3)].

## 6. Reviewer points answered, and sources recommended to enter (cap 4)

| Reviewer point | How H1 answers it | Sources |
|---|---|---|
| R2.1a / R2.2a (what activates) | Holding out plus a presenting, paying, fit traveller; admission fixes the status | uk1956hotel; bogen1996innkeeper |
| R2.1c / R2.2b (who bears it) | The proprietor, answering for servants | uk1956hotel; sandovalstrausz2005travelers |
| R2.2c (delegation), in part | Servants perform, innkeeper answers (passed to H2 with the OLA s 2(4)(b) contractor rule as counter-case) | calye1584case; uk1957occupiers |
| R2.4 (why hospitality) | Honest concession plus the three residual differences in §4 Q4 | sandovalstrausz2005travelers; burdick1911origin; governors |
| R2.5b (formats) | Inn against "any other establishment"; owner-occupied exemption | uk1956hotel; us1964civilrights |
| R3.10 (guests' duties) | Pay, be fit, obey reasonable rules; lien; ejection | uk1956hotel; sandovalstrausz2005travelers p. 63 |
| R3.11 (welcome is not one thing) | Only indirectly: even the legal duty was three duties (bed, board, hearth) with conditions | sandovalstrausz2005travelers |

**Recommended to enter (4), in order:**
1. `uk1956hotel`: activation and holder in one statutory sentence.
2. `sandovalstrausz2005travelers`: historian's bridge; content, ground and route to public accommodation.
3. `bogen1996innkeeper`: the origin dispute and the status point. It keeps the paper from overclaiming.
4. `us1964civilrights`: modern scope and the owner-occupied boundary (R2.5b, R3.8).

If the authors prefer one jurisdiction, swap 4 for `heartofatlanta1964motel` or drop it.

**Must obtain before §2.1 can be written:**
- King 1995 (the outline's only content sentence rests on it);
- Lashley 2000;
- Telfer 2000/01;
- Germann Molz 2026;
- Ganesh 2018;
- Lashley 2015 and Blain & Lashley 2014 (OA on T&F and AJOL, but blocked to this session).

**Proposed CLAIMS.md slugs (not added):**
- `host-duty-activation`: the commercial host's duty is activated by holding out and a presenting traveller.
- `host-duty-holder`: the duty attaches to the proprietor and survives performance by servants.
- `host-duty-origin-contested`: legal history disputes why innkeepers were bound.

## 7. For the verifier

- **Calye and Lane quotations come from eighteenth-century OCR.** Long s was modernised and marginal notes interrupt several passages (Lane p. 484, "bis" for "his"; Calye fol. 33a). Check against the page images of the two Internet Archive items.
- **The *Heart of Atlanta* pages** (260, 261, 284) come from CAP page labels. Confirm against an official U.S. Reports copy.
- **The HPA 1956, OLA 1957, EqA 2010 and PAR 2015 texts are Wayback captures** of legislation.gov.uk, not live fetches. Confirm the current versions.
- **Burdick pp. 515–516 and Sandoval-Strausz pp. 62–63 quotations cross page breaks**, with footnotes intervening in the extracted text.
- **All Q5 claims about Lashley, Blain & Lashley, Poulston, Ramdhony and Lashley 2014 are abstract-level.** They come from Consensus records and are not carded. Nothing beyond the abstract may enter the draft.
