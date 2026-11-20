# R3 — The normative frame: non-domination, internal critique, the analogy rule, and the objections

*Run R3, 2026-10-24. Agent-drafted. The author has not reviewed it.*

## 1. Scope

- Ledger rows: K01, K02, K03, K12, K14 (as they bear on the frame); N01, N02, N04, N05, N06, N08, N15, N17.
- Premises: A1, A6, A7, A8.
- Draft passages (`../manuscript/DRAFT_v1.md`): abstract (ll. 10-20); the thesis and contribution paragraphs (ll. 72-87);
  §1 (ll. 94-140); the pairing passages that apply the frame (ll. 314-320, 384-390, 402-407, 419-434, 436-440); §4
  (ll. 442-509); the Lovett quotation at ll. 506-507.
- Inputs read: `../facets/N5_beq_frame_method_republican.md`, `../facets/N6_counter_case_and_gap_search.md` (c) Q5-Q6
  and (d), `../facets/AUDIT_N7b.md` Table N5, `../facets/ADJUDICATION.md`, `../ARGUMENT_AND_OUTLINE.md` v2, and the
  cards named in §4 below. Sources opened this run: Gädeke 2020 (publisher PDF via Utrecht), Lazar 2024 (two arXiv
  preprints), the first page of Benn and Lazar 2022, and the local copies behind existing cards (Lovett SEP, Bartha
  SEP, Walzer Tanner, Hamilton preprint, Ben-Shahar and Schneider, Kolt).

Substance only. Nothing below concerns wording.

## 2. Search log

All on 2026-10-24. "curl" = scripted GET with a browser user-agent string; no challenge page was bypassed; every 403
was logged and left.

| # | Source | Query / URL | Result | Notes |
|---|---|---|---|---|
| 1 | Repo | ledger K*, N*; DRAFT_v1 ll. 1-140, 300-330, 376-520; ARGUMENT_AND_OUTLINE; N5, N6, AUDIT_N7b, ADJUDICATION, DRAFT_NOTES; CARD_INDEX greps (pettit, lovett, hamilton, maas, muldoon, gädeke, hoeksema, anderson, walzer, jaeggi, celikates, fraser, samson, bartha, ketokivi, qadri, shamir, frahm, wood, bruner, scherer, palazzo, lindman, calo, ben-shahar, kugelberg, gowans, young, lazar, sparks, sunstein, phillips, whelan, hussain) | n/a | Existing cards listed in §4 |
| 2 | Crossref | `works/<doi>` for Gädeke 2020, Maas 2022, Pea 2004, Wood et al. 1976, Shamir 2008, Hussain and Moriarty, Whelan 2012, Scherer and Palazzo 2011, Scherer et al. 2016, Blunt 2015, Lovett 2010, Pettit 2012 | 12/12 matched | Monist DOI for Lovett 2001 wrong in my guess; found by query (#4) |
| 3 | OpenAlex | `works/doi:` for the twelve above | OA routes: Gädeke (Wiley pdfdirect, Utrecht), Maas (ScienceDirect, DOAJ), Pea (HAL), Wood (Wiley, UNAL), Whelan (SSRN), Scherer 2011/2016 (Wiley; CBS) | Shamir, Hussain and Moriarty, Blunt closed |
| 4 | Crossref | `query.bibliographic` for Sparks and Jayaram; Lazar "Governing the Algorithmic City"; Lazar "Legitimacy, Authority"; Lovett Monist 2001; Sunstein 1993; Anderson 2017; Stahl; Gourevitch 2013; Taylor 2017; Hussain and Moriarty; Benn and Lazar; Maas 2023; Susskind; Jongepier and Klenk; Lovett 2012 | 14 of 15 found | Susskind *Digital Republic* has no Crossref record in the top hits |
| 5 | OpenAlex | `works/doi:` for Lazar P&PA 2025, Sparks 2022, Benn and Lazar 2021, Gourevitch 2013, Lovett 2012, Sunstein 1993, Stahl SSRN, Lazar OSPP 2024, Anderson 2017, Maas SSRN 2023 | OA: Sparks (PhilPapers archive), Benn and Lazar (Cambridge PDF; Cambridge repository), Lazar 2024 (arXiv 2208.08628), Stahl (hcommons), Maas 2023 (SSRN) | Lovett 2012, Gourevitch, Sunstein, Anderson closed |
| 6 | arXiv API | `all:"algorithmic city" AND au:lazar`; `au:lazar_s AND ti:legitimacy` | 1; 0 | arXiv 2410.20720v1 (Lecture I) |
| 7 | curl | Wiley `pdfdirect` for Gädeke, Wood et al., Scherer and Palazzo 2011, Scherer et al. 2016 | 403 ×4 | Bot wall; stopped |
| 8 | curl | Utrecht DSpace handle 1874/407680 → REST `pid/find` → bundles → bitstream `dbdb5eee-...` | 200 PDF | Gädeke publisher version, CC BY-NC-ND; sha256 in card |
| 9 | curl | HAL `telearn.hal.science/hal-00190619/document`; `hal.science/hal-00190619/document` | 200 HTML "Making sure you're not a bot!" ×2 | Bot check; stopped. Pea 2004 not read |
| 10 | curl | UNAL repository handle unal/81955 | 200 HTML | A Spanish thesis on scaffolding, not Wood et al.; not used |
| 11 | curl | CBS Research postprint `andreas_rasche_managing_for_political_postprint.pdf` | 403 | Stopped |
| 12 | curl | SSRN Delivery (Whelan 2012); SSRN landing (Maas 2023) | 403 ×2 | Stopped |
| 13 | curl | ScienceDirect `/pii/S2666659621000159/pdf` (Maas 2022); DOAJ API record | 403 challenge page (1.2 MB HTML); DOAJ fulltext link points back to ScienceDirect | Stopped. Gold OA behind a bot wall |
| 14 | curl | PhilPapers archive `SPARBA.pdf` (Sparks and Jayaram); `BENWWW-3.pdf` | 403 ×2 | Stopped |
| 15 | curl | De Gruyter landing `document/doi/10.1515/mopp-2020-0066/html` | 202, empty body | Stopped |
| 16 | curl | Cambridge repository handle 1810/364054 → bitstream `d974263b-...` | 200 PDF, 1 page | First page only (abstract) of Benn and Lazar; existing full card `algorithmacy_design_ethics/bennlazar2022` used instead |
| 17 | curl | arXiv `pdf/2208.08628`; `pdf/2410.20720v1` | 200 PDF ×2 | Lazar 2024 (26 pp.), Lazar Lecture I (53 pp.) |
| 18 | curl | hcommons DOI 10.17613/m6dg7b; 10.17613/qapb5-rv284; `hcommons.org/deposits/item/hc:11849/` | 302 → empty; 202 empty | Stahl 2013 not read |
| 19 | curl | Bentley scholars `philosophy_facpubs/11` → `cgi/viewcontent.cgi?article=1010` | landing 200; PDF 403 | bepress bot wall; stopped. Hussain and Moriarty not read |
| 20 | curl | Chicago Unbound `journal_articles/8479` → `cgi/viewcontent.cgi?article=12380` | landing 200; PDF 403 | bepress bot wall; stopped. Sunstein 1993 not read |
| 21 | curl | `tannerlectures.utah.edu/Anderson%20manuscript.pdf` | 200 HTML (site page, no PDF) | Anderson lectures not online; book closed |
| 22 | WebSearch | Anderson *Private Government* Tanner lecture pdf; Pea 2004 pdf; Sunstein 1993 pdf chicagounbound; Hussain Moriarty pdf | 4 searches | Led to #19-21; an IU course-site copy of Pea (JSTOR-derived) was found and not used |
| 23 | Local | Lovett SEP (N5 copy) keyword read: dependen, procedural, democratic, common knowledge, employer, market, consumer, Kramer, Carter, Goodin, contestat | n/a | §§1.2, 1.3, 2.1, 2.2, 4.1, 4.2 |
| 24 | Local | Bartha SEP (N5 copy): prima facie, plausib, Prior Association, Potential for Generalization, critical disanalogy, stare decisis, normative, moral | n/a | §§2.3, 3.5.2, 4.4; "moral" and "practical reasoning" return nothing |
| 25 | Local | Walzer Tanner (M4 copy), pp. 57-70: minimal code, violence, Nineveh, universal | n/a | pp. 65-66 quoted below |
| 26 | Local | Ben-Shahar and Schneider (M3 decoded text): disclosee, illitera, innumera, overload, accumulation, sophisticated, advice | n/a | pp. 647, 687, 711-712, 742 |
| 27 | Local | Hamilton preprint (N5 copy): Sparks, Not Interested, extreme costs, whatever kinds | n/a | p. 6, p. 10, p. 5 |
| 28 | Local | Kolt (C2_law text): "third part" | 4 hits | pp. 335, 361-364 region |
| 29 | Consensus / Scholar Gateway | not called | — | N5 reported the Consensus quota exhausted until 1 Nov; not retried |

## 3. Entries

Each entry: what the draft says (lines), what the owning literature says (quotation and locator, from a copy I
opened or a card whose quotation the N-round audit verified), the gap, the verdict.

### R3-01. The definition of domination (N04; A1; ll. 98-101, 130-134)

**Draft.** The fourth question is "the republican question of whether anyone holds 'the capacity to interfere in
their affairs on an arbitrary basis' (Pettit, as cited in Lovett 2026, §1.2)" (ll. 100-101); domination "is the
standing capacity" (ledger N04).

**Literature.** Lovett: "a person or group enjoys freedom to the extent that no other person or group has 'the
capacity to interfere in their affairs on an arbitrary basis' (1999, 165; cf. Pettit 1997, 2001, 2012, 2014)"
(SEP §1.2; card `lovett2026republicanism`). Pettit's book definition, as Gädeke quotes it: "(1) they have the capacity
to interfere (2) on an arbitrary basis (3) in certain choices that the other is in a position to make" (Gädeke
2020, 201, citing Pettit 1997b, 52; card `gadeke2020mugger`). Lovett adds that "on either view, arbitrariness simply
means uncontrolled and vice versa" (SEP §2.2).

**Gap.** None in the definition. The quoted words are Pettit 1999, 165 on Lovett's own attribution (card
`pettit1997republicanism`); the draft's "as cited in Lovett" is accurate but the reference list has no Pettit entry
(ll. 570-773 checked), so the quoted author has no record. The outline (A1 row) and AUDIT_N7b (l. 161) already note
that Lovett and Hamilton support only the fourth question; the draft's §1 says so (l. 99-100).

**Verdict: holds** (record to add: Pettit 1999, as Lovett cites it).

### R3-02. Is "domination" of a customer by a firm's agent a standard republican use? (N04, N05, K12; A7; ll. 76-78, 402-407, 436-440, 465-470)

**Draft.** The insider architecture "puts the second party under a power she cannot contest, which is domination in
the republican sense" (ll. 77-78); the worked case is a customer whose refund an agent denies (ll. 402-407); the
consent reply names "her bank, her insurer, her employer's screening system" (l. 468).

**Literature.** Two republican positions. (a) Pettit's ecumenical account: any actual capacity to interfere
arbitrarily dominates; "Pettit himself explicitly considers the mugger to be an instance of domination" (Gädeke
2020, 202) and "Pettit holds that, in principle, a vulnerability class may consist of just one person" (215, n. 53).
On this account the draft's use is standard. (b) The structural account: "Domination, I maintain, is a structurally
constituted form of power" (199); "Purely interactional forms of power, which are based on an opportunistic capacity
to interfere, however, are not instances of domination. Hence, whether and whom the mugger dominates depend on
whether his power is structurally enabled and thus serves as the basis of a persisting status asymmetry" (200);
"Paradigmatic cases of domination, like slavery and marriage, are institutionally stabilized forms of
relationships" (202). Lovett's own gloss is "the absence of any structural dependence on arbitrary power or
domination" (SEP §1.3). The business-ethics applications the ledger relies on are all standing relations: Muldoon
and Raekstad's drivers under "the owners and managers [who] operate as a group agent of domination" (593-594; card
`muldoon2023algorithmic`), Hoeksema's platform users (card `hoeksema2023digital`), Anderson's employees (not opened;
Lazar reports her as treating employers' "ability to issue coercive directives backed by threats of force", Lecture I,
24). Pettit on markets: under "extremely idealistic assumptions" a well-functioning market leaves no one dependent
"on any particular master" (Pettit 2006, 142; card `pettit2006freedom`); Lovett: "markets as such need not involve
domination (Pettit 2006), and indeed when well-ordered might reduce it (Taylor 2017)" (SEP §4.1).

**Gap.** The draft treats every person an enterprise agent acts on as dominated. On account (b) an episodic
encounter (a refund denied once, by a vendor the customer can leave) is opportunistic power, not domination, unless
the organisation's capacity is structurally enabled (terms that make the user "solely responsible", no sanction, no
forum, no alternative) and expresses a persisting status asymmetry. The draft has the materials for that showing
(ll. 393-399 on the terms; l. 468 on bank, insurer, employer) but states the conclusion for the general customer.
The firm-side application is also not the draft's innovation: Muldoon and Raekstad (598) already place the
customer in the triad as a dominator of the worker (card, "I add the second party" graded narrower).

**Verdict: contested, and narrower.** The use is standard on Pettit's account and a stretch on Gädeke's and
Lovett's; the paper must name both, locate the dominator in the organisation (not the agent), and confine the claim
to relations with structural dependency (bank, insurer, employer, public-service channels), conceding the episodic
retail case.

### R3-03. What makes the power arbitrary: procedural or democratic (N04; A1, A5, A7; ll. 133-134, 314-320, 436-440)

**Draft.** The question is "whether the person acted on is exposed to a power she can neither check nor contest"
(ll. 133-134); the envelope is "declared to the organization and enforced for it. The person on whom an agent acts
sees none of it" (ll. 309-310); "No duty in the architecture makes the envelope known or binding to the person it
constrains the agent toward" (ll. 317-318).

**Literature.** Lovett: on the procedural view "Power is not arbitrary ... to the extent that it is reliably
controlled by effective rules, procedures, or goals that are common knowledge to all persons or groups concerned
(Lovett 2010, 2022)", and constraints "must be resilient over a wide range of possible changes"; on the democratic
view "Power is not arbitrary ... to the extent that it is directly or indirectly controlled by the concerned persons
or groups themselves" (Pettit 2012, 57-58) (SEP §2.2). Pettit's contestatory requirements, reasons open to debate,
inclusiveness, impartial "courts of appeal", are stated for state power (SEP §4.2). Gädeke separates the two
conditions: "Not every structurally constituted capacity to interfere is dominating. The power of a judge is
structurally constituted, yet whether it is subject to effective controls—and thus whether it is dominating—is a
separate matter" (205, n. 23).

**Gap.** A declared envelope is a rule-governed capacity. On the procedural view it fails the "common knowledge to
all persons ... concerned" condition (the second party does not know it) and the resilience condition (the deployer
can change it by update, as `seele2022greenwashing` 1070 notes). On the democratic view it fails because the person
acted on has no control. The draft's "neither check nor contest" straddles both without saying which, and
`pettit1997republicanism` (critical notes) already records N1's warning that the manuscript merges them. Hamilton's
view that vendor-granted controls "create antipower for users" (p. 10; card `hamilton2025digital`) is the published
position that cuts the other way and the draft does not meet it.

**Verdict: narrower.** The condemnation holds on either view, but by different conditions (common knowledge and
resilience; control by the affected); the paper must state the condition it uses and answer Hamilton on
vendor-granted controls.

### R3-04. Non-domination "carries the old verdicts across centuries" (N04, N01; A7; ll. 76-78, 129-134)

**Draft.** Domination "in the republican sense that carries the old verdicts across centuries" (l. 78); republicans
have carried their account "from Machiavelli and Locke through early modern feminists to basic income" (ll.
130-132), citing Lovett §4 and Hamilton p. 5.

**Literature.** Lovett §4: classical elitism "might merely reflect the accidental prejudices of their day", and
contemporary republicans "do not aim to anachronistically implement the republicanism of yore for its own sake"
(card). Hamilton: "Republican liberty has, then, been applied to whatever kinds of domination develop" (preprint 5;
card). Celikates and Flynn: external critique "refers to standards and standpoints that are not (or not yet)
recognized" by those criticised (§2.1; card `celikates2023critical`).

**Gap.** Both sources describe applying a value to new cases. Neither says that a past community's verdicts travel.
The literacy-era verdicts the paper relies on (Commons 1695, the 1546 *Supplication*, Maugham L.J.) were not
republican verdicts; non-domination re-judges both periods by one present standard. That is external critique on the
SEP taxonomy, and it does not "carry" anyone's old verdict. Hamilton is an arXiv preprint of an Oxford Intersections
chapter (card: published pagination not seen), a thin authority for the paper's second route; Lovett §4 is enough on
its own.

**Verdict: narrower.** Route 2 is a present external standard applied to both eras, not a carrier of the past's
verdicts; A7 should be restated so.

### R3-05. The rival frame a referee will raise: legitimacy and authority (N04; A1, A5, A7, CB)

**Draft.** The paper uses non-domination as its only cross-era standard and names no rival (§1; §4).

**Literature.** Lazar builds a frame for the same object. Algorithmic intermediaries exercise "intermediary power",
which "constitutes (in whole or part) the social relations that it mediates ... since refusal is impossible unless
it is intentionally designed in" (Lecture I, 14); "LLMs like Claude and ChatGPT govern their users" (19). He rejects
the republican frame: "the tendency of the republican ideal of non-domination to conflate an internally diverse
suite of normative concerns into a single value that has less explanatory power than separately focusing on
(probabilistic negative) liberty, relational equality, and collective self-determination" (20, n. 80; also 2024, PDF
8, n. 27). Governing power must meet procedural legitimacy, "ex ante limitation of what power can be used to do; in
medias res constraints on precisely how power can be exercised; ex post contestability and accountability" (2024,
PDF 11), and proper authority: "Benevolent, procedurally legitimate authoritarianism remains authoritarian and is
inadequate for governing" (Lecture I, 23); "the ultimate source of the authority to exercise power is the community
subject to that power" (23). AI firms "invariably settle questions of safety unilaterally and intransparently, in
ways that would not pass even the loosest standards of procedural legitimacy and proper authority" (24). Lovett
records the older reduction: non-domination "is really just another (more obscure) way of talking about security of
non-interference (Goodin 2003; Carter 2008; Kramer 2008; Moen 2024)" (SEP §2.1).

**Gap.** Lazar reaches the draft's conclusions about the deployer's self-declared envelope (A5) and about notice
without standing (A4) without non-domination, and gives reasons against using it. A BEQ referee who knows this
literature will ask why the paper chose the republican frame. Lazar's three components also give the draft's four
questions a published mapping: the brake is in medias res constraint, the record is publicity, "contest" is ex post
contestability. His authority condition bears on CB: duties a firm adopts for itself do not confer authority, so the
six duties need an external authoriser (regulation or the people acted on) to meet his "who" question. His p. 37
supports B2 (designers "must take responsibility for what people do within those relationships").

**Verdict: contested.** The paper must either defend non-domination against Lazar's conflation charge and the
Goodin-Carter-Kramer reduction, or adopt legitimacy-and-authority as the content of "contest" and keep
non-domination for the exit-and-consent replies where it is strongest.

### R3-06. Walzer's internal criticism as "the paper's first method"; the three benchmarks (N01, N02; A3, A7; ll. 114-121)

**Draft.** "Walzer, whose account of internal criticism gives this paper its first method" (l. 114); the three
benchmarks are contemporaries' objection, a professed standard broken, a promise unmet (ledger N01; ll. 73-75).

**Literature.** Walzer: "Social criticism, for such people, is an internal argument" (Tanner, 34); the prophet's
message "depends upon previous messages" (59); "Judgment would be entirely arbitrary if it did not refer to standards
with which the people were, or were supposed to be, familiar" (70, n. 17) (card `walzer1988interpretation`).
Celikates and Flynn: internal critique "refers to standards and standpoints that are already recognized by those
criticized" (§2.1). Von Samson on Jaeggi: critique by a formation's own "promises" (1316-1317; card
`vonsamson2025immanent`). Gowans on Williams: appraisal is appropriate "in real confrontations, but not in notional
ones" (§7; card `gowans2026moral`).

**Gap.** Only benchmark 2 is internal critique in Walzer's or the SEP's sense, and benchmark 3 is Jaeggi's
promise-critique, which von Samson treats as a variant of immanent critique. Benchmark 1 (contemporaries objected)
is not a critical method at all; it is historical evidence that a standard was recognised and that the confrontation
was real for those who made it (N6 Q6). The draft presents the three as one method. N5 and the outline already
narrowed A7 to two routes; the residual problem is that §1 still calls the whole frame "internal criticism".

**Verdict: narrower.** The method is: benchmark 1 as evidence of recognition; benchmark 2 (and 3 in present tense)
as internal critique of Microsoft; non-domination as external critique. Each should be labelled as what it is.

### R3-07. Can internal critique of professed standards be paired with an era-crossing standard? (N01, N04; A7; ll. 114-134)

**Draft.** Two routes: Microsoft's professions, and non-domination (ll. 122-134).

**Literature.** Walzer himself pairs a thick internal morality with a thin universal one. Jonah in Nineveh: "Conversation
is parasitic on commonality, and since commonality is minimal here, we can imagine only a minimal conversation ...
the talk would be thin, centered on those moral understandings that don't depend upon communal life" (Tanner, 65);
"The prophet judges Israel's neighbors only for violations of a minimal code ... Of the substantive social morality of
these peoples, their domestic practices and institutions, Amos, like Jonah in Nineveh, has nothing to say" (66). Von
Samson: immanent critique "is methodology, not metaethics" (1318); "We might have signed a contract. We might have made
a promise. All that matters is that the normative authority of these norms is independently justifiable" (1318).
Celikates and Flynn report Jaeggi's reconstructive critique as "neither a mere description of what exists nor a
normative demand imposed on what exists from the outside" (§2.3). Lovett: the challenge for republicans is "to show
how it fits into a broader moral framework, and specifically, the comparative weight we should assign to republican
freedom vis-à-vis other important goods" (SEP §2.3).

**Gap.** None of these authors calls the pairing incoherent; Walzer practises it and von Samson prescribes it. Two
limits follow. First, Walzer's minimal code covers "violence" to strangers and says nothing of "domestic practices
and institutions" (66); full republican non-domination, applied to the internal design of a firm's systems, is a
thick, particular theory, not Walzer's thin code, so route 2 cannot borrow Walzer's warrant and must defend its own
authority (Lovett §2.3). Second, on Jaeggi's line an external standard is a demand "imposed ... from the outside", the
charge a critical theorist will press; the draft does not meet it. Fraser's dilemma (`vonsamson2025immanent`, 1308)
also cuts at route 1: granting authority to Microsoft's "de facto governing norms" "renders social critique
structurally conservative". Route 1 ratifies Microsoft's Responsible AI Standard as the measure, and that standard is
Microsoft's to revise (Lovett's resilience condition, §2.2).

**Verdict: holds, in a narrower form.** Coherent, provided route 2 is labelled external critique and defended on its
own, and route 1 is stated with the conservatism cost acknowledged.

### R3-08. Does the draft's analogy test match Bartha? (O03; A6; ll. 104-112, 314-320, 386-390)

**Draft.** Bartha's articulation model "asks for more: a 'Prior Association' in the source domain between the shared
features and the feature to be projected, and 'no critical disanalogy between the domains'" (ll. 104-106); "What
carries the verdict is the property the historical judgment turned on" (ll. 109-110); each subsection "records the
disanalogy that comes closest to breaking it" (l. 112).

**Literature.** Bartha §3.5.2: "Prior Association. There must be a clear connection, in the source domain, between
the known similarities (the positive analogy) and the further similarity that is projected to hold in the target
domain"; "Potential for Generalization. There must be reason to think that the same kind of connection could obtain
in the target domain. More pointedly: there must be no critical disanalogy between the domains." Scope: analogical
arguments "can establish this sort of prima facie plausibility"; "an analogy is used to show that a conjecture is
worth taking seriously" (§2.3); Bartha's justification "is also limited to analogical arguments directed at
establishing prima facie plausibility, rather than degree of probability" (§4.1, as read). Precedent: "It
pre-supposes a common set of social values" (§4.4) (card `bartha2019analogy`; AUDIT_N7b l. 153: carrying a verdict
across is the facet's extension).

**Gap.** Three. (a) Bartha's model licenses prima facie plausibility; the draft says the pairing "carries the
verdict". On Bartha the analogy makes it plausible that the present design is wrong on the same ground, and the two
routes of §1 do the normative work. (b) "No critical disanalogy" is a condition to be met, not a disanalogy to be
recorded; the draft's §3 names the nearest disanalogy and defers it ("Section 4 weighs them", l. 316), so §4 must show
each named disanalogy is not critical. For the envelope the draft does this (duties under ordinary law, met at ll.
471-481); for the brake ("the authorized person may act on the second party's behalf", l. 387) it answers in one
sentence. (c) Prior association must be shown case by case: that the contemporaries condemned the practice because of
the position (custody, record, reading), not for other reasons (monopoly, trade, doctrine). §1 asserts it; the showing
is R1's and R4's to check. Seele and Schultz and Ketokivi et al. are correctly cited for the procedure only (cards:
explanatory analogy; "silent on normative transfer").

**Verdict: narrower.** The test matches Bartha's two conditions; its conclusion is plausibility, not verdict; the
"closest disanalogy" must be shown non-critical, not only recorded.

### R3-09. Contribution 1: against political CSR (O02, D05; A4, A8, CB; ll. 80-82, 477-481)

**Draft.** "Against political corporate social responsibility's hope that firms can fill governance gaps through
voluntary deliberation, it shows what the gap looks like from the position of the party the firm's systems act on
(Lindman, Mäkinen, and Kasanen 2023)" (ll. 80-82); §4: asking Big Tech "to neutralise their power over their
stakeholders and police their own activities ... seems to be asking too much" (Lindman 152).

**Literature.** Lindman et al. report political CSR as firms that fill "governance gaps in global business via
democratic deliberations in multi-stakeholder initiatives" (145-146, citing Scherer and Palazzo 2011) and favour
"high liberal" CSR: regulation and antitrust (card `lindman2023big`). Scherer and Palazzo 2011 (primary) was not
opened (Wiley 403; N6 Cloudflare). Two in-field critiques exist and were not opened: Whelan 2012, *BEQ* 22(4),
"The Political Perspective of Corporate Social Responsibility: A Critical Research Agenda" (Crossref; SSRN 403),
and Hussain and Moriarty 2018, *JBE* 149(3), "Accountable to Whom? Rethinking the Role of Corporations in Political
CSR" (Crossref; the Bentley repository PDF returned 403). Lazar: duties a firm adopts unilaterally lack authority
(Lecture I, 23-24).

**Gap.** (a) The contribution claim stands on a secondary statement of the position it opposes. (b) BEQ has already
published an internal critique of PCSR (Whelan) and JBE one by a Bentley author (Hussain and Moriarty, whose
accountability-reversal argument is, from the record, close to the draft's "oversight for the party that already
holds power"); the novelty claim must be stated against them. (c) Tension: the draft cites Lindman's high-liberal
reply (regulation, not firms) against PCSR, then assigns six duties to designers and firms (§5). Lindman et al.
would call that another instance of asking firms to police themselves; Lazar would say it fails the "who" question.
D05 ("what design cannot do") is the place to resolve it, by stating the duties as the standard a regulator or a
contract enforces, not as voluntary CSR.

**Verdict: narrower, and contested** on (c). The contribution survives as "the view from the party acted on", with
Whelan and Hussain and Moriarty acknowledged and the duties placed outside voluntary deliberation.

### R3-10. Contribution 2: disclosure fails "in who must read" (K14, O07, H24; A2, A4; ll. 82-83, 483-490)

**Draft.** "Against the defense of disclosure as respect for autonomy, it locates the failure of disclosure in who
must read (Calo 2012)" (ll. 82-83).

**Literature.** Ben-Shahar and Schneider locate the failure in the disclosee already: the reasons mandates fail
include "most importantly, ... the ability of disclosees to use them" (647); "The overload effect arises when a
disclosure ... is too copious and complex for the disclosee to handle effectively. The accumulation problem arises
because so many disclosures assail disclosees that they cannot possibly attend to more than a fraction of them"
(687); "Rates of innumeracy are worse than rates of illiteracy" (712, after the literacy figures on 711); disclosure
is inequitable because "the poor have harder problems that require more information and experience, but they have
less ability to use the information" (742; card `benshahar2011failure`, pages confirmed this run in the local text).
Calo's own defence is not the reader's autonomy but discipline through other readers: notices work "not because
consumers will actually read and act on them. Rather, they improve privacy because of the behavior the requirement to
disclose tends to trigger" (1060); his remedy is a change of medium (1034) (card `calo2012against`).

**Gap.** "Who must read" is the skeptics' established diagnosis, in the article the draft's own reference list
carries. What the draft adds is positional: move the reading to another party or to the artefact (the clerk, the
inspector's grade card). Calo's visceral notice (1034) and Ben-Shahar and Schneider's turn to intermediaries and
advice (742-743) partly anticipate even that. The draft's §4 handles Calo correctly (ll. 486-490); the contribution
sentence overstates.

**Verdict: narrower.** Restate as "shifts the reading to a party owed to the weaker side", with Ben-Shahar and
Schneider for the disclosee failure and Calo for the medium.

### R3-11. Contribution 3: a mechanism added to Frahm et al.'s deficit construction (H13, H25; A2, A3, A4; ll. 83-85, 431-434)

**Draft.** The paper "adds a mechanism to Frahm, Doezema, and Pfotenhauer's (2022) account of deficit construction:
an architecture that frames the problem as a deficit of oversight can supply oversight to the one party that already
holds power" (ll. 84-85); §3.4 pairs Nadella's skilling promise with Dakar and then: "The insider post constructs a
deficit of oversight and fills it with oversight for the one party that already holds power" (ll. 433-434).

**Literature.** Frahm et al.'s deficit is a public's: "a democratic deficit of innovation—that frames a lack of
societal engagement in innovation governance as a major barrier to the uptake and dissemination of new technologies"
(175); the RRI project posits "citizens as insufficiently equipped to appreciate the benefits" (200); the solution
"locates both the power to correctly diagnose problems and enact solutions within international organizations"
(203) (card `frahm2022fixing`; the card grades A4 "holds as analogy ... if the paper shows the vendor names the user's
deficit and sells the fix").

**Gap.** Frahm's mechanism is: name a deficit in the public, offer your framework as the fix, gain authority. The
draft's "deficit of oversight" is a deficit Nadella attributes to the deploying organisation (it cannot verify the
model), and the fix is given to that organisation; no public is constructed as lacking. The structural match to Frahm
is the skilling promise ("20 million people", "scaffolding for human potential", ll. 426-428), where the vendor names
the user's deficit and sells the credential. The "added mechanism" is a different mechanism from Frahm's, and the
sentence at ll. 84-85 presents it as an extension.

**Verdict: narrower.** Re-aim contribution 3 at skilling (M11) as a Frahm case, or state the oversight mechanism as
the paper's own, not Frahm's extended.

### R3-12. Responsibilization (N17; O08; CB D08; ll. 502-509)

**Draft.** "Scaffolding the person is responsibilization by another name" (ll. 504-505); no source is cited in §4.

**Literature.** Giesler and Veresiu, from Shamir: four processes "through which responsibility is shifted away from
the state and corporations and the responsible consumer subject is shaped" (841); the WEF "shifted the problem of
financial debt away from the level of better financial regulation to a need for more conscious individual financial
decision makers" (851) (card `giesler2014creating`). The card's critical notes record that Shamir "describes
corporations as one target of responsibilization" (841). Docherty and Valderrama Barragán: Meta's curricula arrange
"relationships of responsibilized control" (17), and a literacy "devoid of the collective could serve simply to
redistribute, rather than challenge, the primary responsibility of the individual" (18) (card
`docherty2026civilizing`). Shamir 2008 itself: record only (closed).

**Gap.** The objection is stated without its literature, and the literature has a second edge the draft misses: on
Shamir's account firms are responsibilized too, through voluntary codes and CSR. A referee can read CB's six duties
as responsibilization of the designer, the move Lindman et al. and Hussain and Moriarty distrust (R3-09). The draft's
four conditions on a scaffold (ll. 507-509) answer the first edge; nothing answers the second.

**Verdict: holds for the objection; narrower for the reply.** Cite the lineage; say why duties on designers are not
voluntary codes (R3-09's fix).

### R3-13. Scaffolding: the four conditions (N17, D08; CB; ll. 507-509)

**Draft.** A scaffold is owed only if "it is built into the system, owed rather than offered, withdrawn only as the
person's ability grows, and paired with the operator's own check" (ll. 507-509).

**Literature.** Wood, Bruner and Ross 1976 (not opened; Wiley 403) coined the term for tutoring. "Fading" is Collins,
Brown and Newman's: the master "reduces his participation (fades)" once the learner has the skill (2-3; card
`collins1987cognitive`, which credits the group with the term). Pea 2004 (not opened; HAL bot check) is, from the
Crossref record and title, the standard argument that the concept has lost its meaning; the extended-mind
literature treats permanent tool support as cognitive extension, not scaffolding (not opened this run).

**Gap.** Two of the four conditions pull against each other. "Withdrawn only as the person's ability grows" is the
learning-sciences criterion (fading), which presupposes a learner whose competence the scaffold builds. The second
party is not a learner of the enterprise's agent; she meets it once, or at intervals, and the record's own
corrections that the draft praises (Teedyuscung's clerk, the inspector's grade card, the second interpreter) were
permanent offices, never faded. "Built into the system" fits those precedents; "withdrawn as ability grows" does
not. Nadella's "scaffolding for human potential" (l. 427) is Pea's loose sense. The paper has to choose: a scaffold
that fades (then it is for learners, and D08 is a skilling duty), or a permanent affordance (then "scaffold" is the
wrong family and D07, change the medium, already covers it).

**Verdict: contested.** The four conditions are not jointly satisfiable for the second party; D08 must be either a
fading scaffold for users or a standing affordance for those acted on.

### R3-14. The "second party" and the enterprise-as-customer framing (K01, K02, O06; A4, A8, CA; ll. 44-52, 457-463)

**Draft.** The person acted on is "a second party" (l. 48) and "those people are as outside the architecture as the
signer was outside the drafting of her contract" (ll. 462-463).

**Literature.** In agency law the person the agent deals with is the third party; Kolt proposes "inclusivity":
agents should be "loyal not only to the best interests of their (direct) users but to a broader and more inclusive
cluster of societal values and interests", because of "negative externalities on third parties" (335; card
`kolt2025governing`, read in the local text this run). Lazar calls both sides "mediatees" and holds that
intermediaries "shape their relationship, typically in ways that profit the intermediary" (Lecture I, 15). Gädeke
calls interpersonal domination "a triadic relationship between dominator, dominated, and ... peripheral agents"
(207). Phillips 2003, *BEQ* 13(1), "Stakeholder Legitimacy" (Crossref; not opened), is the venue's own frame for
parties to whom a firm owes obligations without a contract.

**Gap.** The label "second party" names the third party of agency law and the stakeholder of BEQ's home theory; a
BEQ reader versed in either will ask why a new term, and whether the deployer's customer is a normative stakeholder
(Phillips) with a claim the paper's duties specify. Kolt's inclusivity principle is prior work for B2 and should be
cited as such. Gädeke's triad gives the paper a way to place the model supplier: a peripheral agent that sustains
the organisation's position. The enterprise concession itself (ll. 457-463) is sound and is N6's rank-1 repair.

**Verdict: narrower.** Keep the position; relate it to agency law's third party, stakeholder legitimacy and Kolt's
inclusivity; say what the republican label adds.

### R3-15. The consent and exit reply (K12, N15; A8; ll. 465-470)

**Draft.** "Consent to an unavoidable channel is thin"; exit "carries what Hamilton (2025, 10) calls 'extreme
costs'"; where the agent acts for her bank or insurer "there is no contract between her and the agent's supplier".

**Literature.** Pettit 1997, 62, via Lindblom: a relationship "consensual in origin" can still be domination (card
`pettit1997republicanism`, narrower, secondary). Pettit 2006: exit protects only where "no one would depend on any
particular master", under "extremely idealistic assumptions" (142; card). Hoeksema: republicans "cannot rely on the
idea of exit options or of rationally consenting citizens" (reprint 67; card). Hamilton p. 10 as quoted (card).
Gädeke: domination "is a position of power" that holds whatever the dominator does (207).

**Gap.** None in substance; the reply is the republican one. Two cautions: Hamilton's "extreme costs" concerns
Google's data infrastructure and social media, not enterprise agents; and the no-contract point is the agency-law
point of R3-14, which strengthens the reply if named.

**Verdict: holds.**

### R3-16. The historicist reply: Walzer's "new relevance" (N01; A8; ll. 492-501)

**Draft.** Walzer "also explained why the prophets could invoke" the Exodus law: "against a background of urban
growth and class differentiation that gave that law, and all the Exodus laws, a new relevance" (Walzer 1988, 70); "A
medium that demands a new competence of everyone ... gives the literacy record that kind of relevance" (ll. 497-501).

**Literature.** Walzer, 70, as quoted (card). The passage concerns Israel's own law regaining force in Israel under
changed conditions; the same lecture holds that the law "isn't universally known" and "it's not obvious that our ideas
are unjust" (69), and that a detached critic gets only "a minimal conversation" (65).

**Gap.** The "new relevance" reply works only inside a shared tradition. It therefore serves route 1, where Microsoft
stands inside Anglo-American contract and consumer law and its own professions, and the Kugelberg and Kugelberg
objection ("AI reshapes the practices", card p. 10) is met by their own concession that the approach "can recommend
fundamental reform when a practice no longer serves the values that justify it" (10). It does not make the literacy
record as a whole relevant to Microsoft; for that the paper has only route 2, which Williams's relativism of distance
does not touch (Gowans §7: the present appraisal is a real confrontation).

**Verdict: narrower.** The reply holds for the tradition Microsoft is inside; route 2 answers the rest.

### R3-17. Are the seven objections the strongest a BEQ referee would raise? (A8; ll. 442-509)

**Draft.** Seven: history as ornament; the bound party misidentified; consent; the law provides; disclosure respects
autonomy; historicism; scaffolding as responsibilization.

**Stronger or missing objections, with sources opened or carded.**

1. *Automation reduces domination.* Sparks and Jayaram argue (Hamilton's report, preprint 6; card `sparks2022rule`,
   secondary) that algorithmic governance can decrease domination because algorithms have no will and remove human
   discretion. The draft's refund agent acts inside a declared envelope and is more rule-bound than a clerk. Reply
   available: the arbitrariness is the organisation's uncontrolled power over the envelope (Muldoon and Raekstad
   593-594; Gädeke 205 n. 23), and rule-boundedness toward the deployer is not control by the person acted on
   (Lovett §2.2). The draft does not make it.
2. *Wrong frame.* Lazar's conflation charge and legitimacy-authority alternative (R3-05), and the Goodin-Carter-Kramer
   reduction of non-domination to secure non-interference (Lovett §2.1). If the reduction holds, the paper needs
   only the probability of harm, and Moffatt-type cases do the work without republicanism.
3. *No structural dependency, so no domination* for the episodic customer (Gädeke 200, 208; R3-02).
4. *The duties lack authority.* "Benevolent, procedurally legitimate authoritarianism remains authoritarian" (Lazar,
   Lecture I, 23): six duties designed in by the firm are still the firm's unilateral settlement of the "who"
   question. Hussain and Moriarty (record only) press the same against PCSR.
5. *Paternalism, in BEQ's own pages.* Scherer et al. 2023: paternalism "remains, in a political sense, a form of
   interference with one's liberty" and can produce organized immaturity (422; card `scherer2023guest`, verifier:
   "the paternalism objection's strongest in-venue form"). The draft's objection 5 meets Calo's autonomy point, not
   this one, and duties 4 (check understanding) and 6 (scaffold) are its targets.
6. *Immanent critique's conservatism.* Fraser's dilemma (von Samson 1308): route 1 grants authority to Microsoft's
   "de facto governing norms". The draft cites von Samson for support and does not face the cost.
7. *The individual remedy misses the structural problem.* Benn and Lazar: "assessing Automated Influence from the
   individual perspective at all largely misses the point"; the problems "are collective action problems" (§6; card
   `algorithmacy_design_ethics/bennlazar2022`, full). Five of the six duties are owed to individuals one at a time
   (refusal route, envelope, counter-record, check, scaffold); only the standards duty is collective.
8. *Firm-side responsibilization* of CB (R3-12).

The seven the draft has are the right first set; N6 ranked them. Objections 1, 2, 4 and 5 above are each stronger
than the draft's objections 1 (ornament) and 6 (historicism), because each is published, in or near the venue, and
aimed at the frame rather than at the history.

**Verdict: narrower.** The set is incomplete; at least 1, 2 (or 4), 3, 5 and 7 must be met.

### R3-18. Lovett's "better able to cope" against the scaffold (N04, N17; ll. 506-507)

**Draft.** "Just because one is better able to cope with arbitrary power," Lovett (2026, §2.2) writes, "it does not
follow that one's domination is any less."

**Literature.** SEP §2.2, exact (card; AUDIT_N7b verified). Context: Lovett's procedural view, explaining why
constraints must be resilient rather than the subject adaptable.

**Gap.** None; the sentence is used as Lovett uses it. One consequence the draft could add: the same sentence cuts
against the paper's own D08 if the scaffold raises the person's coping and leaves the envelope uncontrolled, which is
why condition four (the operator's own check) carries the weight.

**Verdict: holds.**

### R3-19. Abstract against §1: which route carries the thesis (ll. 10-20, 72-78)

**Draft.** The abstract judges the architecture "by that era's own objections and broken promises, and by Microsoft's
own professed standards" (ll. 16-17) and does not mention non-domination; the thesis paragraph makes domination the
carrier of the old verdicts (ll. 76-78); the keywords list "non-domination" (l. 22).

**Gap.** A substance inconsistency, not a wording one: the abstract states an argument of one route (internal), §1 an
argument of two. Given R3-04 and R3-06, the argument that survives is: internal critique binds Microsoft where it
professes; non-domination judges the rest; the history supplies the positions and the precedents. The abstract should
state that argument or the body the abstract's.

**Verdict: narrower** (the frame as stated in two places is two different frames).

## 4. Cards used

Opened this run and carded (facet R3): `gadeke2020mugger` (partial), `lazar2024governing` (partial),
`lazar2024legitimacy` (partial), `sparks2022rule` (secondary, via Hamilton). Existing cards relied on, with their
audited quotations: `lovett2026republicanism`, `hamilton2025digital`, `walzer1988interpretation`,
`celikates2023critical`, `vonsamson2025immanent`, `bartha2019analogy`, `ketokivi2017reasoning`,
`seele2022greenwashing`, `kugelberg2026practice`, `gowans2026moral`, `calo2012against`, `frahm2022fixing`,
`lindman2023big` (all `berthon_ethics_paper`); `pettit1997republicanism`, `pettit2006freedom`,
`muldoon2023algorithmic`, `hoeksema2023digital`, `giesler2014creating`, `docherty2026civilizing`,
`scherer2023guest`, `benshahar2011failure`, `kolt2025governing`, `collins1987cognitive` (`berthon_ethics_course`);
`bennlazar2022` (`algorithmacy_design_ethics`). Local texts behind `lovett2026republicanism`, `bartha2019analogy`,
`walzer1988interpretation`, `hamilton2025digital`, `benshahar2011failure` and `kolt2025governing` were reopened for
the quotations above that the cards do not carry (search log #23-28).

## 5. Verdict table

| ID | Concept / claim | Draft lines | Verdict | Evidence (card + locator) | Fix to the argument |
|---|---|---|---|---|---|
| R3-01 | Domination defined as the capacity to interfere arbitrarily | 98-101 | holds | `lovett2026republicanism` §1.2; `gadeke2020mugger` 201; `pettit1997republicanism` (attribution to Pettit 1999, 165) | Add the Pettit 1999 record Lovett cites |
| R3-02 | A firm's agent "dominates" the customer it acts on | 76-78, 402-407, 436-440, 468 | contested; narrower | `gadeke2020mugger` 199, 200, 202, 208, 215 n. 53; `lovett2026republicanism` §1.3, §4.1; `muldoon2023algorithmic` 593-594; `pettit2006freedom` 142 | Dominator = the organisation; claim confined to structurally dependent relations (bank, insurer, employer, public channel); episodic retail case conceded; Pettit vs Gädeke named |
| R3-03 | Arbitrariness: "neither check nor contest" | 133-134, 309-318 | narrower | `lovett2026republicanism` §2.2 (procedural: common knowledge, resilience; democratic: control by the affected), §4.2; `gadeke2020mugger` 205 n. 23; `hamilton2025digital` 10 | State the condition used; answer Hamilton on vendor-granted controls |
| R3-04 | Non-domination "carries the old verdicts across centuries" | 76-78, 129-134 | narrower | `lovett2026republicanism` §4; `hamilton2025digital` 5; `celikates2023critical` §2.1 | Route 2 is a present external standard applied to both eras; it re-judges, it does not carry |
| R3-05 | Non-domination as the frame, with no rival named | §1, §4 | contested | `lazar2024governing` 14, 19, 20 n. 80, 23, 24, 37; `lazar2024legitimacy` PDF 1, 5, 8 n. 27, 11; `lovett2026republicanism` §2.1 (Goodin, Carter, Kramer) | Defend the frame against the conflation charge and the reduction, or adopt legitimacy/authority as the content of "contest" |
| R3-06 | Walzer's internal criticism as "the first method"; three benchmarks | 114-121; 73-75 | narrower | `walzer1988interpretation` 34, 59, 70 n. 17; `celikates2023critical` §2.1; `vonsamson2025immanent` 1316-1317; `gowans2026moral` §7 | Benchmark 1 = evidence of recognition; 2 (and 3, present tense) = internal critique; non-domination = external critique |
| R3-07 | Internal critique paired with an era-crossing standard | 114-134 | holds (narrower) | `walzer1988interpretation` 65-66 (minimal code; thin talk); `vonsamson2025immanent` 1318; `celikates2023critical` §2.3; `lovett2026republicanism` §2.3 | Coherent; label route 2 external and defend it; acknowledge Fraser's conservatism cost on route 1 |
| R3-08 | Analogy test = Bartha's articulation model | 104-112, 316, 387 | narrower | `bartha2019analogy` §3.5.2, §2.3 (prima facie plausibility), §4.4; `seele2022greenwashing` 1065; `ketokivi2017reasoning` 650 | Conclusion is plausibility, not verdict; each "closest disanalogy" shown non-critical; prior association shown per case (R1, R4) |
| R3-09 | Contribution 1: against political CSR | 80-82, 477-481 | narrower; contested on the duties | `lindman2023big` 145-146, 152; records: Whelan 2012 (BEQ), Hussain and Moriarty 2018 (JBE); `lazar2024governing` 23-24 | State the contribution against Whelan and Hussain and Moriarty; place CB's duties outside voluntary deliberation (D05) |
| R3-10 | Contribution 2: disclosure fails "in who must read" | 82-83, 483-490 | narrower | `benshahar2011failure` 647, 687, 711-712, 742; `calo2012against` 1034, 1060 | Restate as shifting the reading to a party owed to the weaker side |
| R3-11 | Contribution 3: a mechanism added to Frahm et al. | 83-85, 431-434 | narrower | `frahm2022fixing` 175, 200, 203 | Re-aim at skilling (M11) as a Frahm case, or own the oversight mechanism as the paper's |
| R3-12 | Scaffolding is responsibilization | 502-509 | holds (objection); narrower (reply) | `giesler2014creating` 841, 851; `docherty2026civilizing` 17-18; Shamir 2008 (record) | Cite the lineage; answer the firm-side responsibilization reading of CB |
| R3-13 | The four conditions on a scaffold | 507-509 | contested | `collins1987cognitive` 2-3 (fading); Wood et al. 1976 and Pea 2004 (records, not opened) | D08 as a fading scaffold for users, or a standing affordance for those acted on (then D07) |
| R3-14 | "Second party"; enterprise-as-customer | 44-52, 457-463 | narrower | `kolt2025governing` 335 (inclusivity; third parties); `lazar2024governing` 15; `gadeke2020mugger` 207; Phillips 2003 (record) | Relate to agency law's third party, stakeholder legitimacy and Kolt; say what the republican label adds |
| R3-15 | Consent and exit reply | 465-470 | holds | `pettit1997republicanism` (62 via Lindblom); `pettit2006freedom` 142; `hoeksema2023digital` 67; `hamilton2025digital` 10; `gadeke2020mugger` 207 | None; name the agency-law no-contract point |
| R3-16 | Historicist reply via Walzer's "new relevance" | 492-501 | narrower | `walzer1988interpretation` 65, 69, 70; `kugelberg2026practice` 10; `gowans2026moral` §7 | Reply holds inside the shared tradition (route 1); route 2 answers the rest |
| R3-17 | The seven objections are the strongest | 442-509 | narrower | `sparks2022rule` (via `hamilton2025digital` 6); `lazar2024governing` 20 n. 80, 23; `gadeke2020mugger` 200; `scherer2023guest` 422; `vonsamson2025immanent` 1308; `bennlazar2022` §6 | Add: automation reduces domination; wrong frame / no authority; no structural dependency; in-venue paternalism; individual remedies miss the structure |
| R3-18 | Lovett's "better able to cope" | 506-507 | holds | `lovett2026republicanism` §2.2 | None; note it also binds D08 |
| R3-19 | Abstract (one route) vs §1 (two routes) | 10-20, 72-78 | narrower | this review, R3-04, R3-06 | One statement of the frame in both places |

Counts: holds 4 (R3-01, R3-07, R3-15, R3-18; R3-12 holds for the objection) · narrower 11 (R3-03, R3-04, R3-06, R3-08,
R3-09, R3-10, R3-11, R3-14, R3-16, R3-17, R3-19; R3-12's reply) · contested 4 (R3-02, R3-05, R3-09 on the duties,
R3-13) · misused 0 · unsupported 0 · wrong 0.

## 6. Gaps and blocks

| Source | Why not read | Where a Bentley library user would find it |
|---|---|---|
| Pettit, P. (1997), *Republicanism*, OUP; (1999) "Republican Freedom and Contestatory Democratization", in *Democracy's Value*, CUP, 163-190; (2012) *On the People's Terms*, CUP | Closed; not retried | Oxford Scholarship Online / Cambridge Core via the library; print in the catalogue. Pages: 1997, 52, 62, 68-9, 73-4, 122, 186-7; 1999, 165; 2012, 7, 57-58, 63 |
| Lovett, F. (2010), *A General Theory of Domination and Justice*, OUP (doi 10.1093/acprof:oso/9780199579419.001.0001); (2012) "What counts as arbitrary power?", *J. Political Power* 5(1) | Closed | Oxford Scholarship Online; Taylor & Francis via the library. 2010 pp. 53, 72 are the ones Gädeke cites |
| Gädeke 2020 | **Read** (Utrecht publisher PDF) | — |
| Anderson, E. (2017), *Private Government*, Princeton UP (doi 10.1515/9781400887781) | Book closed; the Utah "Anderson manuscript" URL cited in reviews no longer serves a PDF | Princeton UP ebook or print via the catalogue; the 2015 Princeton Tanner Lectures page lists the two lectures without text |
| Maas, J. (2022), "A Neo-Republican Critique of AI Ethics", *J. Responsible Technology* 9, 100022 | ScienceDirect challenge page (gold OA behind a bot wall); DOAJ fulltext link returns to ScienceDirect | ScienceDirect in a browser (open access); DOAJ record 9830212f07814fda8e605db45b15e323 |
| Maas, M. M. (2023), "AI is Like… A Literature Review of AI Metaphors and Why They Matter for Policy", SSRN 4612468 | SSRN 403 | SSRN in a browser; Institute for Law & AI site |
| Sparks, J. and Jayaram, A. (2022), "Rule by Automation", *Moral Philosophy and Politics* (doi 10.1515/mopp-2020-0066) | PhilPapers archive 403; De Gruyter landing 202 empty | De Gruyter via the library; PhilPapers archive SPARBA in a browser. Secondary card written from Hamilton p. 6 |
| Benn, C. and Lazar, S. (2022), *CJP* 52(1) | First page only here; the ade card `bennlazar2022` is full and audited | Cambridge Core (open access) |
| Lazar, S. (2025), "Governing the Algorithmic City", *Philosophy & Public Affairs* (doi 10.1111/papa.12279) | Version of record not opened (Wiley); the arXiv Lecture I preprint was read | Wiley via the library; check pagination against the preprint locators in `lazar2024governing` |
| Lazar, S. (2024), OSPP vol. 10 chapter | Chapter pages (28-56 per the repo bib) not seen; arXiv preprint read | Oxford Academic via the library |
| Jaeggi, R. (2018), *Critique of Forms of Life*; Fraser, R. (2023), *Proc. Aristotelian Soc.* 123(2); Stahl, T. (2013) "What is Immanent Critique?", SSRN 2357957 / (2022) *Immanent Critique*, Rowman & Littlefield | Closed; OUP 403 (N5); hcommons deposit redirect empty, SSRN not retried | De Gruyter/Harvard ebook; Oxford Academic; hcommons or SSRN in a browser; Bloomsbury Collections. N5's list stands |
| Walzer, M. (1994), *Thick and Thin*, Notre Dame UP; (1987) *Interpretation and Social Criticism*, Harvard UP | Not searched online (books); the Tanner text was used for the minimal-code passages | Library catalogue; *Thick and Thin* ch. 1 is the fuller statement of the minimal code |
| Sunstein, C. R. (1993), "On Analogical Reasoning", *Harvard Law Review* 106(3), 741-791 (doi 10.2307/1341662) | Chicago Unbound PDF 403 (bepress bot wall) | HeinOnline or JSTOR via the library; Chicago Unbound in a browser. Step (4), the principle that explains the source case, is the analogue of Bartha's prior association for law |
| Hussain, W. and Moriarty, J. (2018), "Accountable to Whom?", *JBE* 149(3), 519-534 (doi 10.1007/s10551-016-3027-8) | Springer closed; the Bentley repository PDF (scholars.bentley.edu/philosophy_facpubs/11) returned 403 to scripted requests | Bentley's own repository in a browser; Springer via the library. A Bentley author; the paper should engage it |
| Whelan, G. (2012), "The Political Perspective of Corporate Social Responsibility: A Critical Research Agenda", *BEQ* 22(4) (doi 10.5840/beq201222445) | SSRN 403; Cambridge closed | Cambridge Core (BEQ) via the library |
| Scherer, A. G. and Palazzo, G. (2011), *JMS* 48(4); Scherer, Rasche, Palazzo and Spicer (2016), *JMS* 53(3) | Wiley 403 ×2; CBS postprint 403 | Wiley via the library; CBS Research in a browser for the 2016 postprint |
| Shamir, R. (2008), "The age of responsibilization", *Economy and Society* 37(1), 1-19 | Closed | Taylor & Francis via the library |
| Pea, R. D. (2004), *J. Learning Sciences* 13(3), 423-451 | HAL served a bot check twice; an IU course-site copy (JSTOR-derived) was found and not used | Taylor & Francis or JSTOR (stable 1466943) via the library; HAL hal-00190619 in a browser |
| Wood, D., Bruner, J. S. and Ross, G. (1976), *J. Child Psychology and Psychiatry* 17(2), 89-100 | Wiley 403 | Wiley via the library |
| Phillips, R. (2003), "Stakeholder Legitimacy", *BEQ* 13(1), 25-41 | Not tried (record only) | Cambridge Core via the library |
| Blunt, G. D. (2015), "On the source, site and modes of domination", *J. Political Power* 8(1); Gourevitch, A. (2013), *Political Theory* 41(4); Taylor, R. S. (2017), *Exit Left*, OUP | Closed; not tried beyond records | Taylor & Francis; SAGE; Oxford Scholarship Online via the library |
| Consensus and Scholar Gateway | Not called (quota exhausted per N5; resets 1 Nov) | Rerun "republican domination firm customer algorithm", "legitimacy intermediary power AI", "immanent critique corporate standards" next round |
