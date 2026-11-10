# WS H3: Who the host is when several firms share the job

Research run rr-2026-11-h · 10 November 2026 · questions Q3 and Q8 (FABLE_REVIEW §7)

*Drafted by Claude (H3 workstream agent). None of this is the authors' wording. I edited no manuscript, plan, bibliography, CLAIMS or index file, and I committed nothing.*

**Conflicts flagged.**

1. The repo `CLAUDE.md` says to commit and push after every step. `RUN_BRIEF_H.md` says not to commit. I followed the brief.
2. `RUN_BRIEF_H.md` gives `read_depth: full` and `verified: primary-legal-source`. `library/build_index.py` accepts only `full-text` and only `verified | crossref-verified | corrected`. I used the validator's values. The card for the case says `verified: verified`, and its `source_basis` records "primary-legal-source", following the `eu2024aiact` precedent.
3. `build_index.py --check` fails every new held card that has no `references.bib` entry. That includes my four new cards and the cards other workstreams created. The brief forbids me to edit the bib, so the main session must add the entries or accept the failure. My cards raise no other validation error.

---

## 1. What was searched

All searches ran on 10 November 2026. Scholar Gateway returned `ACCESS_DENIED` and was not used.

| Tool | Exact query | Considered | Kept → card | Dropped, and why |
|---|---|---|---|---|
| Consensus | `accountability in algorithmic supply chains many hands distributed responsibility` | 15 | Cobbe, Veale & Singh 2023 (card) | Widder & Nafus 2023, downloaded but not carded: it studies developers' sense of responsibility, not allocation to a served party. Constantinescu & Kaptein 2025: the record exists, but Cobbe covers the multi-firm case more directly. Cooper et al. 2022: the record exists, but it is a within-organisation many-hands account. Martin 2018 and Rahman et al. 2024: relevant, not read, over cap |
| Consensus | `hotel management contract owner operator brand franchise relationship guest` | 15 | none | Whalen & Sisson 2022: the abstract says "most travellers do not understand the difference between a corporate-owned and -managed hotel and a franchised hotel". The full text was blocked by a bot wall at T&F and the Napier repository, so it stays abstract only and uncarded. van Ginneken et al. 2019: the abstract says "Misunderstandings of the hotel management agreement can cause confusion as to where risks and responsibilities lie" [UNVERIFIED — no record found, VERIFY_H_v2]. Paywalled, not read. de Roos 2012 chapter, Beals & Denton 2005, Melissen & Wood 2016, Cruz et al. 2024, Zhang et al. 2015: about owner–operator economics and performance, not duties to guests |
| Consensus | `Airbnb host responsibility obligations to guests platform liability short-term rental` | 15 | Kaniadakis & Farmaki 2022 (card); Farmaki et al. 2019 (card); Filatova-Bilous 2021 (card) | Maese 2015: an Airbnb host as innkeeper versus landlord. The PDF was blocked, and the innkeeper-law content is H1's. Kramer 2024, *European Law Open*: shifts the regulatory burden to hosts. The PDF was blocked. Kreeger & Smith 2023 (CHQ): the abstract says "hosts are ultimately responsible for complying with other public policy regulations". Not read. Leoni & Parker 2019, Cocola-Gant et al. 2021 ("corporate hosts"): relevant to Q8, not read, over cap. Regulation-effects papers: out of scope |
| Consensus | `unstaffed contactless self-service hotel guest experience absence of staff` | 15 | none | Chang et al. 2022 (AM read, see §3); Çeltek 2024; Sthapit et al. 2024; Du et al. 2024; Liu & Hung 2020/2021. All measure acceptance or satisfaction. None asks who answers to the guest |
| Consensus | `franchisor vicarious liability apparent agency hotel guest injury` | 15 | led to Crinkley (card) | Kliavkoff 1994 (CHRAQ 35(1) 59–73): a hospitality-venue article on hotel franchisor apparent agency. Record exists, paywalled, abstract only. Terry & Huan 2019 (Monash LR) and Emerson 2019: both say the public cannot see the franchise structure. Not read; noted as the counter-trend |
| Consensus | `Monetizing network hospitality Airbnb hospitality sociability hosts` | 10 | none | Ikkala & Lampinen 2015 and Lampinen & Cheshire 2016: both verify Fable leads. Paywalled, not read. Christensen 2026 (*Geoforum*, "Modes of Hospitality") is a candidate for Q8. Not read |
| Consensus | `service failure complaint handling recovery in unmanned or self-service hotels without staff guest recourse` | 10 | none | Liu et al. 2026 (*J. Consumer Behaviour*): human versus robot apology in unmanned hotels. Abstract only. Chen & Tussyadiah 2021 (*Annals*): service failure in P2P accommodation. Not read |
| Consensus | `who is the host in commercial hospitality restaurants bars events hosting role duty of care to patrons` | 10 | none | Davies et al. 2020 (JST): P2P social-dining hosts. The abstract reports "an uneven risk burden between hosts and platforms with regards liability". Not read. Hancock et al. 2008 ("host responsibility" in licensed venues), Malkin & Voon 2007, Linton 2012, Orr 1995 (commercial versus social host liability for alcohol): abstract only, relevant to bars, see §3 |
| Consensus | `problem of many hands moral responsibility public officials Thompson` | 8 | none | Verifies Thompson 1980 and van de Poel et al. 2015 (see §2) |
| WebSearch | `Crinkley v. Holiday Inns 844 F.2d 156 apparent agency franchisor hotel` and `hotel franchisor apparent agency guest injury court opinion "holding out" Holiday Inn franchisee liability` | ~20 links | Crinkley, full opinion from law.resource.org | Sims v. Marriott (W.D. Ky. 2001), Murphy v. Holiday Inns (Va. 1975), Bright v. Sandstone (Ga. App. 2014), Marchionda v. Embassy Suites: known only through search snippets and law-firm summaries. Not read, not cited |
| Crossref / OpenAlex / Semantic Scholar / Unpaywall / OpenLibrary | DOI and title lookups for every lead in §2 | — | — | — |
| EUR-Lex / curia | CJEU C-390/18 *Airbnb Ireland* | — | — | EUR-Lex returned an empty WAF page and curia redirected. The primary text was not read and the judgment was not carded |

---

## 2. Fable leads, traditions (f) and (h)

| Lead (FABLE_REVIEW §4) | Outcome |
|---|---|
| Thompson 1980, "Moral responsibility of public officials: the problem of many hands", APSR | **Verified record**: DOI 10.2307/1954312. Not read, not carded. Cobbe et al. (arXiv p. 1) restate it |
| Bovens, *The Quest for Responsibility* (1998) | **Verified record**: OpenLibrary, Cambridge UP 1998, ISBN 0521481635. Not read |
| van de Poel, Royakkers & Zwart (2015) | **Verified record**: DOI 10.4324/9781315734217 (Routledge). Not read |
| Cooper et al., "Accountability in an algorithmic society" (FAccT 2022) | **Verified record**: DOI 10.1145/3531146.3533150. Not read. Cobbe et al. 2023 is preferred for the multi-firm question |
| French (1984); List & Pettit (2011) | **Verified records**: OpenLibrary lists French, Columbia UP 1984, and List & Pettit, OUP 2011. Not read. They concern whether an organisation can bear duties, which sits closer to H2 |
| Young 2006, social connection model | **Verified record**: *Social Philosophy and Policy* 23(1), DOI 10.1017/s0265052506060043. Not read |
| deRoos, "Hotel management contracts: past and present", CHQ (2010) | **Verified record**: DOI 10.1177/1938965509354865. Paywalled, not read |
| Franchisor and brand liability under apparent agency ("I can name no case") | **Verified with a primary source.** *Crinkley v. Holiday Inns, Inc.*, 844 F.2d 156 (4th Cir. 1988), read in full and carded. The doctrine is contested across jurisdictions (§3) |
| Platform terms and regulation; Edelman & Geradin, "Efficiencies and regulatory shortcuts" (2016) | **Record exists, details differ.** Crossref and OpenAlex hold an SSRN 2015 working paper (DOI 10.2139/ssrn.2658603). Kaniadakis & Farmaki cite it as an HBS working paper (2015). Farmaki et al. cite a *Stanford Technology Law Review* version. I found no record of the journal version and did not read it. Airbnb's own terms of service were not fetched |
| GDPR controller and processor | No primary text read. Cobbe et al. summarise CJEU joint-controllership case law (arXiv pp. 7–8). That account is secondary |
| Germann Molz 2026 in full | Out of H3's assigned upgrades and not attempted. It remains the largest unread source |
| Farmaki, Stergiou & Kaniadakis, "Self-perceptions of Airbnb hosts' responsibility" | **Verified and read** in the accepted manuscript (JST 30(5) 983–1003, DOI 10.1080/09669582.2019.1707216). The content matches the Fable guess: what hosts think they owe. Duties to guests are a minor part of it. Carded, held |
| Ikkala & Lampinen 2015 (CSCW); Lampinen & Cheshire 2016 (CHI) | **Verified records**: DOIs 10.1145/2675133.2675274 and 10.1145/2858036.2858092. Paywalled, not read |
| Germann Molz "2014a", network hospitality | **Verified record.** The 2018 article's reference list gives "(2014a), 'Toward a network hospitality', First Monday, 19:3", and Crossref matches it (DOI 10.5210/fm.v19i3.4824). Not read |
| Tuomi, Tussyadiah & Stienmetz, CHQ ("about 2021") | **Record exists, details differ**: CHQ, published online 25 May 2020, DOI 10.1177/1938965520923961. Not read |
| McCartney & McCartney, "Rise of the machines", IJCHM (2020) | **Verified record**: DOI 10.1108/ijchm-05-2020-0450. Not read |
| Wirtz et al., "Brave new world", JOSM (2018) | **Verified record**: DOI 10.1108/JOSM-04-2018-0119. Not read |
| Evidence on unstaffed or contactless hotels ("I can name no study") | **Records exist; the content differs from what the paper needs.** Studies of unmanned smart hotels exist (Chang et al. 2022, IJHM, DOI 10.1016/j.ijhm.2022.103249; Çeltek 2024; Sthapit et al. 2024; Liu et al. 2026). All of them measure acceptance, satisfaction or forgiveness. None asks who holds the host's duties or how a guest reaches someone with authority (gap statement, §3) |

No lead in (f) or (h) came back with no record at all.

---

## 3. Synthesis: who the host is when several firms share the job

**Three questions travel together under the word "host".** They are who receives the guest, who controls the terms, and who appears to the guest as the provider. In a single-owner inn one party answers all three. In each format below they come apart, and the sources disagree about which answer makes a party the host.

**Branded hotels.** In a branded hotel the guest typically faces three firms: the owner of the building, the operator that runs it day to day, and the brand. *Crinkley* names all three as defendants. The owners were sued "as the actual owners of the motel", TRAVCO "as the entity in actual day-to-day control", and Holiday Inns on "apparent agency" (844 F.2d 156, para 7). The court affirmed a jury verdict holding the brand answerable to the guests, on apparent agency, for a property it did not own and did not operate day to day; the owners and the operator were held liable too (para 9). The majority found that the brand "retained a significant degree of control over the operation" through the franchise agreement (para 51, 844 F.2d at 166); "played no role in its management" is the dissent's view (para 57). The ground for the brand's liability was that the brand had operated its system to "create the appearance" that the property was its own, and that the guests relied on that appearance in choosing it (paras 49–52).

The test has two parts. The principal must have "represented or permitted it to be represented" that the operator was its agent, and the guest must have dealt with the operator "in reliance on such representations" (para 50). The court decided only that the evidence "sufficed to support submission of this theory" to the jury (para 50), and it called the reliance evidence "marginal" (para 52). It gave two reasons and marked one limit:

- A disclaimer in the franchise agreement "is not alone determinative" (para 51).
- The only sign of the franchise was a notice in the restaurant (para 51).
- Limit, not a reason: reliance fails where the guest did not choose the hotel. The court distinguished a guest whose employer required the stay (footnote 3).

The dissent calls the brand "an innkeeper not responsible for managing the premises" (Wilkinson, J., para 58). The phrase states the paper's problem exactly.

The doctrine does not settle the matter everywhere. Search-result abstracts indicate that many courts in the US and Australia now refuse to treat branding alone as holding out. Terry & Huan (2019) conclude that Australian law has "largely" [UNVERIFIED — no record found, VERIFY_H_v2] insulated franchisors, and Emerson (2019) surveys consumers to show that the public does not know who runs a franchised outlet [UNVERIFIED — no record found, VERIFY_H_v2]. I read neither past the abstract, so the draft can say "a court has held", not "courts hold".

The hospitality literature describes the same opacity from the guest's side. Whalen & Sisson (2022) report, at abstract depth, that "most travellers do not understand the difference between a corporate-owned and -managed hotel and a franchised hotel". Van Ginneken et al. (2019) report, also at abstract depth, that even the parties to a management agreement confuse "where risks and responsibilities lie" [UNVERIFIED — no record found, VERIFY_H_v2].

**Platforms and short-term rentals.** For the platform, the law uses two tests in parallel. Filatova-Bilous (2021) separates an objective test from a subjective one:

- The objective test asks whether the platform has "decisive influence" over "the price, the quality of services ..., the conditions of access" (p. 8). On this test the CJEU found Airbnb "a pure intermediary" (p. 3).
- The subjective test asks "how the users perceived the operator's role" (pp. 12–13). Under it, a Danish court held that Booking.com was not liable for a host's breach because the guest "should have understood" that Booking.com "alone acted as an intermediary" (p. 13).

The subjective test is the platform's version of the hotel holding-out test. That parallel is my synthesis, not the author's claim.

Platform terms push the guest-facing duties downward. In Germann Molz's gloss on the "lean platform", Airbnb "is not in the hospitality business", and hosts are "responsible ... for all of the tasks of cleaning up after and caring for guests" (2018, p. 243). The platform's status "as a platform that connects people" is what lets it "claim exemption" from other regulation (p. 243). The same shedding of duties appears when platforms profit "while transferring legal and tax liabilities onto homeowners" (p. 245).

Hosts experience this as responsibilisation. In Kaniadakis & Farmaki's interviews, responsibility is "removed from the digital platform owners ... and transferred to individuals" (2022, p. 2), leaving "a responsibility vacuum" (p. 2). Hosts list what they owe guests: "good quality services" and being "accurate, decent and honest" (Table 2, p. 16). They resist the hotel role: "I am not a butler though nor am I a receptionist in a hotel" (p. 14). Farmaki et al. add that some hosts "diffuse responsibility to the platform or even to guests" (2019, AM p. 16). The two studies very probably share one dataset (35 European hosts recruited through a COST Action; Farmaki et al. AM p. 6), so they are not independent corroboration.

**Technology vendors.** For the vendor, the most precise account comes from outside hospitality. Cobbe, Veale & Singh (2023) argue that algorithmic systems are now assembled by "a group of organisations ... each retaining control over component systems they provide as services to others" (arXiv p. 2). Their account has four elements:

- Responsibility is "distributed among several actors", and "there is ... typically no one actor in overall control" (p. 7).
- Each actor sees only to an "accountability horizon" (p. 8). "In many cases ... no actor will have sufficient knowledge of or control over both production and deployment" (p. 9).
- The deploying customer is likely the data controller, while the vendor that built the system positions itself as a processor and "disclaim[s] legal accountability" in its terms (pp. 8, 10).
- In data-protection law, they report, "the CJEU has consistently held that the factual situation outweighs contractual ... arrangements" (p. 8); challenging providers' claims "would involve litigation or regulatory investigation" (p. 8). They state no general allocation rule; that allocation *should* follow factual control is my step, not theirs. Responsibility is partial and unequal across actors (p. 8).

Applied to a hotel, a pricing or check-in system supplied by a vendor puts the operator in the deployer's seat. The operator carries the duties without seeing the model, and the vendor sees the model but not the guest. That application is mine.

**Where the host role thins out (Q8).** The sources show five things:

1. **Short-term rentals.** "Host" is already several roles. Airbnb distinguishes "primary hosts", "listing admins or owners" and "co-hosts" (Bosma 2022, p. 601). The owner receives the payout, while the co-host "help[s] ... take care of their home and guests" (p. 601) under instructions from the app. Hosting is "broken down into separate types of labor that can or cannot be outsourced, automated, and optimized", and Airbnb's integration of these practices "suggest[s] that Airbnb is willing to further decentralize the figure of the host" (p. 605). Self-check-in, which Airbnb requires only for a listing to be eligible for business travellers, lets guests enter "without meeting anyone in person", which Bosma calls "transforming hosting into ghosting" (p. 605). In this format the party with the payout, the party with the keys and the party with the rules are three different parties.
2. **Unstaffed hotels.** Chang et al. describe "unmanned" hotels that "operate for 24-hours with no human staff throughout the whole operating system" (2022, AM p. 4, paraphrasing and citing Wu et al. 2019, without quotation marks), and they study satisfaction and loyalty. I found no work that asks who holds the host's duties, or how a guest reaches a person with authority, in unstaffed, self-check-in or app-only hotels. I searched Consensus with `unstaffed contactless self-service hotel guest experience absence of staff` and `service failure complaint handling recovery in unmanned or self-service hotels without staff guest recourse` on 10 November 2026. Scholar Gateway was unavailable. The nearest work, Liu et al. (2026, abstract only), tests whether a human should join a robot's apology, and it finds the human matters most in "high-severity service failures".
3. **Bars.** The law distinguishes commercial from social hosts. In Canada "commercial hosts owe a duty of care to their impaired patrons, social hosts ordinarily do not" [UNVERIFIED — no record found, VERIFY_H_v2] (Malkin & Voon 2007, abstract only). "Host responsibility" is also a regulatory term for licensed venues [UNVERIFIED — no record found, VERIFY_H_v2] (Hancock et al. 2008, abstract only). None of these was read.
4. **Peer-to-peer dining.** Davies et al. (2020, abstract only) report "an uneven risk burden between hosts and platforms with regards liability".
5. **Events.** I found no source on hosting duties at events in this run.

**Answer to Q3 and Q8, briefly.** Across these formats the sources allocate the host's duties by two different criteria:

- **Control.** Who runs the premises, sets the terms, or exercises "decisive influence" (the operator in *Crinkley*; the objective test in Filatova-Bilous; the CJEU's factual-control rule that Cobbe et al. report).
- **Appearance.** Whose name the guest relied on (apparent agency in *Crinkley*; the subjective test in Filatova-Bilous).

Platforms and vendors arrange their terms to fail both tests. They disclaim control in contract (Cobbe et al., p. 10) and present themselves as intermediaries (Germann Molz 2018, p. 243; Filatova-Bilous, p. 13). The host role thins out where control and appearance point at different parties, and where the guest has no one to rely on. The clearest cases are platform-mediated rentals with self-check-in (Bosma, p. 605) and unstaffed hotels, where the literature has not yet asked the question.

---

## 4. What this means for the paper's position (FABLE_REVIEW §5)

- **Position A, threshold sovereignty, is weakened.** In every multi-firm format, control of the premises is split. Owner, operator and brand each held part of it in *Crinkley*, and the owner, co-host and lock vendor each hold part of it in Bosma. That is the "divided-sovereignty problem" Fable predicted. A sovereignty ground does not say which of the three is host.
- **Position B, public calling (holding out), is supported, with a cost.** *Crinkley* is a located instance of a court holding a hotel brand to the guest because it held the property out as its own and the guest relied on that. Filatova-Bilous shows a subjective, appearance-based test for platforms; that it is "the same" test as hotel holding out is my inference. The test gives R2.1e an answerable question: who did the guest rely on? The costs are three:
  - The doctrine is jurisdiction-bound and contested (§3).
  - It turns on the guest's reliance, so it thins where the guest did not choose the hotel (*Crinkley*, footnote 3).
  - Platforms design themselves out of it by presenting as intermediaries.
- **Position C, institutional role obligation, is supported on multi-actor allocation.** The sources treat "host" as a role that firms split, share and decompose. Bosma's primary host, co-host and listing admin are literally platform-defined roles (p. 601). Cobbe et al. say responsibility is partial and unequal across actors (p. 8), which is the shape Reviewer 2's "several actors at once" needs. The sources do not tell C which occupant is the host. H3 proposes (no source makes this split) that B's holding-out test can fill that gap: the role's obligations attach to the party that presents itself as host, while the duties are performed by the party in control. *Crinkley* does not support the split, since the owners and operator in control were held liable to the guests as well (para 9).
- **Net.** H3 supports Fable's recommendation (C as frame, B as evidence) and adds a refinement the authors may want, which is H3's own proposal, not a holding: **holding out fixes who answers to the guest; control fixes who performs.** In *Crinkley* holding out added a party who answers (US, one circuit, North Carolina law); it did not move the answer away from the controllers. The current outline treats "the institution" as one party (FABLE_REVIEW §1, R2.1e). On this evidence that is defensible only if "the institution" means the party that holds itself out to the guest, and the paper says so.

---

## 5. Reviewer points answered, and sources recommended to enter

**Answered:**

- R2.1e and R2.2d, fully. The allocation among owner, brand, operator, platform and vendor, with a test for who holds out.
- R2.1c and R2.2b, in part. On H3's proposal, the holder includes whoever holds out as host.
- R3.8 and R2.5b, in part. Short-term rentals and unstaffed hotels are where the role decomposes. The literature gap on unstaffed hotels belongs in §9.
- R2.2e, in part. Cobbe et al. show that the multi-firm mechanism is general, which supports conceding R2.4 on mechanism.

**Recommended to enter (cap 2):**

1. **`crinkley1988holiday`**: primary legal source, §2.1 and §4. It is the hotel-specific answer to "who holds out as host". State the jurisdiction.
2. **`cobbe2023understanding`**: §2.1, §4 and §9. It covers the vendor and the many-firm structure. Map the arXiv pages to the proceedings pages before quoting.

**Already in the library and under-used:**

- `germannmolz2018scale`, p. 243, new in this run, and p. 245, for the platform.
- `bosma2022platformed`, pp. 601 and 605, for where the host role thins out. It is held. It could replace a weaker platform source rather than add to the count.

**Held, ranked below the cap:** `kaniadakis2022responsibilisation` (3), `filatovabilous2021platform` (4), `farmaki2019selfperceptions` (5).

**Proposed new claim id** (not added to CLAIMS.md): `host-by-holding-out`, for §2 and §4. "When several firms share the hosting, a party that held itself out as host and on which the guest relied can also be answerable to the guest, alongside the parties in control; one US court (4th Cir., North Carolina law) has so held on apparent agency." That a holding-out party answers while the party in control performs is H3's proposal; `crinkley1988holiday` does not support the split, because the owners and operator were held liable too. Sources: `crinkley1988holiday` (one jury-submitted apparent-agency holding), `filatovabilous2021platform` (the platform-side appearance test); `cobbe2023understanding` reports the CJEU factual-control rule but states no allocation rule.

**Not upgraded:** `chengfoley2019`, already full text, with nothing new for H3; `edelman2017discrimination`, because no open copy was reachable this run.

---

## Corrections after verification

*Added in rr-2026-11-h after VERIFY_H_v2 (2026-11-10).*

- §3: *Crinkley* "neither owned nor ran" replaced; the majority found the brand retained significant control (para 51, 844 F.2d at 166), and "no role" is the dissent (para 57). Holding restated as one apparent-agency verdict sent to a jury, reliance "marginal", owners and operator also liable (paras 9, 50, 52).
- §3: "three reasons" corrected to two reasons and one limit (footnote 3).
- §4–5: "holding out fixes who answers; control fixes who performs" and the `host-by-holding-out` claim labelled as H3's proposal, with the jurisdiction caveat in the claim text; *Crinkley* does not support the split.
- §3: Cobbe et al. no longer said to state that allocation "should follow factual control"; they report the CJEU data-protection rule (arXiv p. 8 = proceedings p. 1193).
- §3: Farmaki et al. locator corrected from AM p. 14 to AM p. 16; shared dataset with Kaniadakis & Farmaki noted.
- §3: Filatova-Bilous "how the users perceived…" locator corrected to pp. 12–13. §4: "the same appearance test" marked as my inference.
- §3: Bosma's hedge ("willing to further decentralize") and the business-traveller condition on required self-check-in restored.
- §3: Chang et al. paraphrase and cite Wu et al. 2019; "quoting" removed.
- §1, §3: the five unverified abstract-level items (Terry & Huan, van Ginneken et al., Malkin & Voon, Emerson, Hancock et al.) marked inline as unverified.
