# AUDIT_N7a: adversarial audit of the history-side cards and facet claims (N2, N3)

*Auditor N7a, 2026-10-24. Agent-drafted. The author has not reviewed it, and none of the text is the author's. I wrote
none of the cards or facets audited here. I changed no card, facet or other file; this is the only file I wrote in the
repo.*

**Date.** 2026-10-24.

**Scope.** (1) The 37 new cards with `facet: N2` or `facet: N3` in `literature/cards/berthon_ethics_paper/`. (2) The
claims in sections (c) and (d) of `N2_custody_of_the_medium_page_and_press.md` and `N3_literacy_demanded_of_the_bound.md`
that bear on A2, A3, A5 and B1, and the N2/N3 rows of "Round-1 findings" in `nadella/COVERAGE_PREMISES.md`. (3) Six
legacy history-side cards (graff1991literacy, pike1873history, willis2008against, nussbaum2011creating,
statute1827criminal, roberts1835memoirs), plus a check of whether each round-1 upgrade card fixes its old card's
problem. (4) The seeded legacy sample of nine cards.

**Checks run.**
1. sha256 recomputed for every card's `local_path` (37 new, 15 legacy). All 35 new cards with a file match; the two
   abstract cards (jin2003effect, tamariz2013improving) have `null`, as they should. All legacy files present match.
2. Exact-string check of every quotation in every card (whitespace, line-break hyphens, long s and curly quotes
   normalised), by script, then by eye for each miss. Most misses were OCR noise or card prose caught by the quote
   extractor; each real difference is reported below.
3. Page check. For OCR books I located each quotation between the printed running heads. For a second route I
   downloaded independent scans of Hall (`hallschronicleco00halluoft`), Boretius (`monumentagermani00geseuoft`),
   Tyndale (`03565678.emory.edu`) and the *Four Supplications* (`asupplicacyonfo00cowpgoog`, plus the page image of
   p. 64 from `asupplicacyonfo01cowpgoog`), and the page image of Pike p. 300. I viewed the page images the cards rely
   on (Virginia pp. 107-108, North Carolina ch. VI, Novísima pp. 144-145, Lely p. 276 and Andrews p. 331, Pennsylvania
   pp. 664, 689, 690, Alvord pp. 7 and 14). For Havelock and Nussbaum I used archive.org full-text search on the
   lending scans (`be-api.us.archive.org/fts/v1/search`), which returns wording but no page. A Cranmer second scan
   (`miscellaneouswri0000thom_j3c0`) returned HTTP 500; I deleted the error file.
4. Crossref record and `filter=updates:` for every DOI in scope (frahm, jin, israeli, nishimura, tam, tamariz, almeida,
   burnyeat, holmes): titles, venues, volumes, pages and years agree; no update or retraction notice on any.
   kempf2014cuban's DOI is a DataCite DOI (resolves at doi.org to UBC; DataCite record names Kempf); it has no Crossref
   record, as the card says. OpenAlex confirmed Frahm et al. is hybrid OA (CC BY-NC) and gave Jin and Leslie's
   abstract, which matches the card's paraphrase. Europe PMC gave Tamariz's abstract, which matches.
5. Each quotation read against the claim hung on it in the card and the facet.
6. Every new card parses with `cardlib.parse_card` (read-only); `basis` and `doi` are as stated.
7. Saenger rule and provenance: every N2/N3 card copy comes from a public-domain scan, an open repository, a court or
   parliamentary database, or an OA publisher. No N2/N3 card quotes Saenger. One sampled legacy card (havelock1963)
   rests on an unauthorised community upload of an in-copyright book.

**Disclosure.** No e-mail address, `mailto` or Unpaywall call was used. No paywall, bot wall or CAPTCHA was met or
bypassed in this audit (I did not try Google Books search-inside). No Chrome tools, no git. Downloads, each in its own
subdirectory of `~/iit-playground/berthon_ethics_local/pdfs/nadella/N7a/` and read with `python3 -I`:
`hall/hallschronicleco00halluoft_djvu.txt` (sha256 `1d37d931e44c833e…`), `boretius/monumentagermani00geseuoft_djvu.txt`
(`c411235a867a9dad…`), `tyndale/03565678_djvu.txt` (`9cfa4226275fb2cf…`),
`supplications/asupplicacyonfo00cowpgoog_djvu.txt` (`4f099ad8f75dd97d…`), `supplications/sup01_n91.jpg`
(`6f5cb1af0fc27f07…`), `pike/n335.jpg` (`ddd27283695bbedb…`).

**Result in one line.** The quotations and page locators on the 37 new cards hold almost without exception (no
fabricated quotation, no hash mismatch, no wrong page found); the faults lie in what the cards and syntheses build on
them: a number that is wrong twice (Cuban tutors; the Jones lease rent), a mislabelled statute, and sixteen claims that
outrun their text, the heaviest being that the 1546 *Supplication* is a direct objector to the 1543 Act, and the
facets' readings of the grade-card study, Jomtien, Israeli p. 62 and the 1695 Commons reasons.

Status key: VERIFIED verbatim / VERIFIED paraphrase / WRONG / OVERSTATED / NEEDS LIBRARY CHECK / COULD NOT CHECK.
"Page: two routes" means the page was fixed in two independent scans or a scan plus a page image; "page: running
heads" means one scan, with the quotation bracketed by printed running heads in the OCR.

---

## Table 1. Facet N2: cards and synthesis claims

| # | Facet/card and line | Claim or quotation as written | Source and locator | Status | What I found | Fix |
|---|---|---|---|---|---|---|
| N2-1 | `boretius1883capitularia`, Key facts; N2 (b), (c) Q1 | No. 30: "religiosis lectoribus nostrae ditioni subiectis"; "librariorum imperitia depravatos … examussim correximus"; "inconsonantes perstrepere soloecismos"; "nostra eadem volumina auctoritate constabilimus"; c. 72 "per inemendatos libros male rogant"; no. 29 "si gratiam nostram habere vis" | MGH Capit. 1, pp. 60, 79, 80, 81 | VERIFIED verbatim | All present. Page: two routes (`capitulariaregum01bore` and `monumentagermani00geseuoft` both put no. 30 on pp. 80-81, c. 72's passage on p. 60). Boretius's dating note (Alcuin at court from 781) is on p. 80 as stated. The OCR "constabiliraus" carries Boretius's variant note "c) stabilivimus 1", which the card does not mention. | None needed; optionally note the variant. |
| N2-2 | `boretius1883capitularia`, Summary and A5; N2 (c) Q1 | c. 72 "opens schools to" servile and free-born boys, "which widens whom the page served"; the texts "name the beneficiaries … in the schools boys of servile condition" | MGH Capit. 1, pp. 59-60 | OVERSTATED | The clause asks that clergy by their good life draw ("protrahantur") to God's service "not only children of servile condition but also sons of free men", and that there be "scolae legentium puerorum". It concerns recruiting boys to God's service and schools for them; it names no lay readership. "Widens whom the page served" reads a recruitment clause as access for readers. | "c. 72 asks clergy to draw boys of servile as well as free birth into God's service and to keep schools for reading boys (p. 60)." Drop "widens whom the page served". |
| N2-3 | `brinklow1874complaynt` | p. 54 "How they bare men from readyng the Byble! …"; "to shutt it vp from the peple"; p. 79 "nor suffre their seruawtes to haue it"; editor's date "about A.D. 1542" | EETS 1874, pp. 54, 79 | VERIFIED verbatim | All present; page: running heads ("54 THE BISHOPS AND THE BIBLE"; "THE CITIZENS REFUSE THE BIBLE. 79"). The card's "narrower" verdict (no mention of the Act) is right. | None. |
| N2-4 | `commons1803journal`, Key facts; N2 (b), (c) Q3 | Reasons 1, 3, 8, 9, 12, 16 and the Streater proviso, quoted | CJ 11, 17 April 1695 (BHO pp. 305-308) | VERIFIED verbatim | Every quotation exact, with the reason numbers right. The entry has 17 numbered reasons plus "Lastly" (Streater). BHO marks no page break, so pp. 305-306 rests on the Copyright History record, as the card says. | None. |
| N2-5 | `commons1803journal`, A3 ("whom it harmed (scholars, authors, …)"); N2 (d), "Refutation: registration protected authors" row ("the Commons in 1695 said it took authors' 'Labour and Right'") | The Commons said the Register took authors' labour and right | Reason 3 | OVERSTATED | Reason 3 says the Company had "an Opportunity to enter a Title to themselves, and their Friends, for what belongs to, and is the Labour and Right of, others". It names no authors, and says "Opportunity", not that titles were taken. No reason names authors. | "The Commons said the Register gave the Company 'an Opportunity to enter a Title' to what is 'the Labour and Right of, others' (reason 3)." Drop "authors" from the card's list of the harmed. |
| N2-6 | N2 (c) Q3 | "the Commons on 17 April 1695, whose seventeen reasons ended licensing" | CJ 11; Deazley 1637 s. 5 | VERIFIED paraphrase | The reasons were for disagreeing to the Lords' clause that would revive the 1662 Act; the Act then lapsed ("its expiration in May 1695", Deazley). "Ended licensing" compresses refusal-to-revive plus expiry. Seventeen numbered reasons plus a closing proviso objection. | "whose reasons for refusing to revive the Act preceded its expiry in May 1695". |
| N2-7 | `deazley2008commentary1586` | 1577 complaint; "close to 200 printers … no more than ten stationers"; Wolfe; Bourne 3 Feb 1586; patentees 4 May 1586; "guardians of the press"; decree ordinances 3-4; Greg's 30 vs 147 entries; Clegg's 13% | copyrighthistory.org commentary, ss. 4-5, nn. 7, 12, 19-31 | VERIFIED verbatim | Every quotation and section placement exact. The period voices are Deazley's quotations of Arber, which the card says. | None. |
| N2-8 | `deazley2008commentary1637` | "almost universally acknowledged … high point"; Blagden; Loewenstein "with two exceptions …"; "simply encouraged"; "rhetoric of authorial responsibility"; July 1641; "its expiration in May 1695" | commentary ss. 4-5 | VERIFIED verbatim | All exact, sections right. | None. |
| N2-9 | `cranmer1846miscellaneous` | p. 118 "two sorts"; p. 121 "Here may all manner of persons …"; p. 122 "convenient and good …", "royal assent", Nazianzen "It is not fit …" | Parker Soc. 1846, pp. 118-122 | VERIFIED verbatim | All present; page: running heads (p. 118 marker, "120 PREFACE", "122 PREFACE", "PREFACE … 123"; p. 121 inferred between 120 and 122). Second scan unavailable (HTTP 500). | None; second route still wanted for p. 121. |
| N2-10 | `cranmer1846miscellaneous`, Summary | "Three years later 34 & 35 Hen. VIII c. 1 barred exactly those groups" | Act, p. 896; prologue p. 121 | OVERSTATED | Cranmer's list includes lords, ladies, officers, lawyers, merchants, tenants, "mean men". The Act bars women (but lets noble and gentle women read to themselves), artificers, prentices, journeymen, serving men of yeoman degree or under, husbandmen and labourers, and lets merchant householders read privately. It barred some of the named groups, not "exactly those". | "barred several of the groups Cranmer had named: women below gentle rank, artificers, husbandmen". |
| N2-11 | `foxe1838acts` | p. 527 "advancement of popery, under the colour of religion"; the reading-bar sentence; the purgation sentence; ed. n. on Gibson | Cattley vol. 5, p. 527 | VERIFIED verbatim | All exact; page: running head "QUALIFICATIONS OF THE SIX ARTICLES. 527". The editor's note also dates the session's end to May 1543, which supports the card's dating correction. | None. |
| N2-12 | `furnivall1871four`, Key facts | p. 64 "Finally, thei haue procured a lawe … x. pound by yere …"; "We appeale … indifferent or not"; p. 65 "disable them for readers"; p. 66 "restore vnto vs …"; p. 67 "frely come to it, and read therin" | EETS ES 13, pp. 61-68 | VERIFIED verbatim | Page 64: two routes; I read it on the page image of `asupplicacyonfo01cowpgoog` leaf n91 ("x. pound"; margin "unless he can spend £10 a year"). A third scan's OCR (`00cowpgoog`) reads "2. pound", an OCR error. pp. 65-67 present in three OCRs under the right heads. Editor's dating ("1546 for the third") confirmed. | None. |
| N2-13 | `furnivall1871four`, Summary and A3; N2 (b) "this is the contemporary objector facet B did not find"; (c) Q3 "yes, one direct objector exists"; claim 1; (d) "Holds on one direct objector"; COVERAGE A2/A3 N2 row "a contemporary objector found" | The *Supplication* is a direct contemporary objection to 34 & 35 Hen. VIII c. 1 | p. 64 vs Act pp. 896-897 | OVERSTATED | The petition objects to "a lawe" that no one may "haue the Scripture in his house" unless he can spend £10 a year. The Act bars *reading* by rank and sex and has no income or possession test (I read the reading clauses, pp. 896-897). The petition never names the Act. Identifying the two is the facet's inference; the facets already flag the mismatch but still score the petition as "the" objector. | "A 1546 petition objects to 'a lawe' passed in Parliament that kept the English Scripture from those who could not 'spend x. pound by yere' (p. 64). Its likeliest target is 34 & 35 Hen. VIII c. 1, but its criterion matches no text found." Treat A3's objection limb for 1543 as probable, not established. |
| N2-14 | `hall1809chronicle` | p. 866 "licensed you so to do …"; "disputed, rymed, song and iangeled …"; "our Counsayl or to vs …" | Hall 1809, p. 866 | VERIFIED verbatim | All present; page: two routes (`cu31924027958713` and `hallschronicleco00halluoft` both bracket the passage between the heads for 866 and 867). | None. |
| N2-15 | `isambert1828recueil`; N2 claim 6; (c) Q5 | arts. 110-111, "ne lieu à demander interprétation"; "sur l'intelligence des mots latins"; "en langage maternel françois et non autrement"; editor: "l'acte le plus important du règne", "écrits en Français" | Isambert t. XII, no. 188, pp. 622-623, note | VERIFIED verbatim | All present; art. 110 and most of 111 under the "622" head, the close of 111 under "623". Editor's note verified. The card's OCR repairs are correct. | None. |
| N2-16 | `manuzio1564index` | Rule IV "quos intellexerint … in scriptis habeant"; sanction; booksellers; Rule III "uiris tantum doctis & piis"; Rule VI | Index 1564, pp. 14-16 | VERIFIED verbatim | All present after long-s normalisation; page: running heads ("u REGVLAE INDICIS" = 14; "LIBRORVM PROHIB. 15"; "16 REGVLAE INDICIS"). | None. |
| N2-17 | `milton1644areopagitica` | p. 34 the Order and "every mans Copy"; p. 58 "monopoliz'd …"; p. 76 "tolerated Popery"; p. 79 "old patentees" and "power of a few" | Arber 1868 reprint | VERIFIED verbatim | All present; page: running heads (34, 58, "7«" = 76, 79). The upgrade fixes the old card's lack of pagination. | None. |
| N2-18 | `reusch1883index` | Clement VIII's observation; "einfach wiederhergestellt"; "curialistischen Anschauung"; Spain 1551/1559 and 1790; "in praxi diesseits der Alpen …"; Serarius; Véron; Belgium 1570, Tournai 1600 | Reusch Bd. 1, pp. 333-336 | VERIFIED verbatim | All present under the right heads. Reusch also quotes Billuart (c. 1750) and Ferraris that the Holy See tolerated vernacular reading in France, Germany, England and Poland (p. 336), which strengthens the non-enforcement point. | None. |
| N2-19 | N2 (c) Q5 "It bound in Spain (total ban from 1551), Portugal, Italy and Belgium"; `reusch1883index` Where used ("Rule IV bound hard in Spain, Portugal …") | Rule IV bound in Spain and Portugal | Reusch pp. 334-335 | OVERSTATED | Reusch shows Spain and Portugal went further than Rule IV: Spain's own indices banned all vernacular Bibles outright from 1551, and Lisbon 1624 was stricter still. That is not Rule IV binding; it is a harsher national rule. Italy and Belgium are the cases where Rule IV's licence system was enforced. | "Rule IV was enforced in Italy and Belgium; Spain and Portugal banned vernacular Bibles outright under their own indices; north of the Alps it was often not observed (Reusch pp. 334-336)." |
| N2-20 | `starchamber1637decree` | preamble; items II, IV, XV, XXXIII; Commons order 29 Jan. 1642 "doe neither print, nor reprint any thing without the name and consent of the Author" | Arber 1868, pp. 9-24 | VERIFIED verbatim | All present; item XV on p. 16 and XXXIII on p. 23 by running heads. The 1642 order follows "FINIS" with no head; p. 24 is inferred, as the card says. | Confirm p. 24 on the image or cite "Arber 1868, after p. 23". |
| N2-21 | `starchamber1637decree`, Critical notes ("The Commons order of 1642 is a protection for authors (consent and name)") | 1642 order protects authors | Arber 1868, p. 24 | OVERSTATED | The order requires the author's name and consent and punishes a printer who omits them "as both Printer and Author thereof". On its face it fixes responsibility for content as much as it protects authors; the companion card `deazley2008commentary1637` itself reads the name rule as "authorial responsibility", not protection. | "The 1642 order requires the author's name and consent and treats a printer who omits them as the author; it serves responsibility for content and, secondarily, the author's consent." |
| N2-22 | `statutesrealm1817vol3`; N2 (b), (c) Q4 | preamble "to be reade by his loving Subject …"; "lower sorte"; reading bar; "shall of his clemencye thinke good …"; "other thenne be above lymited"; purgation "as manye or moo"; "chaunge and altre"; side-note "See Stat. 1 Edw. VI. c.12. § 2." | SoR vol. 3, pp. 893-897 | VERIFIED verbatim | All present; the heads (895, 896, 897 at page tops) put the reading clause and the preamble on p. 896 and purgation and "chaunge and altre" on p. 897. The side-note is a foot-note to the chapter list (p. 893). Same file as facet B (hash match). | None. |
| N2-23 | N2 (c) Q5 "1543 as protective": purgation by witnesses, a one-year limit, a month's notice of new doctrine | SoR vol. 3, p. 897 | VERIFIED paraphrase | All three are in the text: "within oone yere next after suche offence"; "till oone moneth be paste … every psone maie have notice". | None. |
| N2-24 | `statutesrealm1819vol4`; N2 claim 4; (d) H20 row | 1 Edw. VI c. 12 repeals the 1543 Act (p. 19); peers have the benefit "though they cannot read" (p. 21) | SoR vol. 4, pp. 18-22 | VERIFIED paraphrase | Both paraphrases match the damaged OCR (p. 19 head "A.D.1547 … c 12. 19"; p. 21 between heads 20 and 22). The card rightly quotes nothing. | None, beyond the clean copy the card asks for. |
| N2-25 | `statutesrealm1819vol4`, Summary | "The first statute of Edward VI's first Parliament (1547) on treasons and felonies" | SoR vol. 4 | WRONG | The Act is chapter 12 of the session (1 Edw. VI c. 12), as the card's own heading says; the OCR shows c. 11 ending on p. 18. | "Chapter 12 of Edward VI's first Parliament (1547), on treasons and felonies". |
| N2-26 | `tyndale1848doctrinal` | p. 394 "impossible to establish the lay-people in any truth …"; p. 393 "in this they be all agreed …"; pp. 393-394 "amaze them …" | Parker Soc. 1848 | VERIFIED verbatim | Page: two routes (`doctrinaltreatis00tynduoft` and `03565678.emory.edu` both put "all agreed" on 393 and "owls" and "establish" on 394). The Act's "craftye false and untrue translacion of Tyndale" is on SoR vol. 3 p. 894 as the card says. | None. |
| N2-27 | N2 (b) saenger1997space; (d) A2/A5 row; COVERAGE A2 (first moment) | Saenger p. 11: ancient elitism kept the costly script; "UNSUPPORTED for quotation" | unauthorised archive.org upload, p. 11 | NEEDS LIBRARY CHECK | Compliant with BRIEF §6 in form: no card quotes Saenger, and the facet marks the passage unquotable. But N2 (b) carries Saenger's wording without quotation marks ("in his words as relayed by ledger H26, foreign to the elitist literate mentality of the ancient world"), which is a quotation in substance from an unclean route. I did not attempt Google Books (CAPTCHA risk). | Drop the near-verbatim phrase from N2 (b) until a clean route (library copy or Google Books in a browser, id `w3vZaFoaa3EC`) confirms p. 11. |
| N2-28 | N2 claim 2 | `transcriptofregi02statuoft` is Eyre and Rivington 1640-1708 vol. 2 (1913), not Arber II | archive.org metadata | VERIFIED paraphrase | Metadata: "A transcript of the registers of the Worshipful Company of Stationers, from 1640-1708", 1913, vol. 2. Facet B's search used the wrong book. | None. |
| N2-29 | N2 claim 3 | "Innis's 1694 is wrong" | CJ 11; Deazley | OVERSTATED | 1695 is right in New Style. The facet did not open Innis, and the Commons proceedings on renewal ran through February-April 1694/5, so a "1694" can be an Old Style date rather than an error. | "The Act lapsed in 1695 (New Style); check whether Innis's 1694 is Old Style before calling it wrong." |
| N2-30 | N2 claim 5 | The 1543 bar lasted four years and was repealed by the next reign | SoR vol. 4, p. 19 | VERIFIED paraphrase | Holds on the repeal clause (paraphrase depth). | None. |
| N2-31 | N2 claim 7 | The petition's income test contradicts the Act's rank-and-sex criteria | Furnivall p. 64; SoR vol. 3 p. 896 | VERIFIED verbatim | Confirmed on both texts (see N2-12, N2-13). | None; but see N2-13 for what follows from it. |
| N2-32 | N2 (c) Q4 | Professed standard broken in three texts: Cranmer p. 121; the injunction recalled at p. 67; the Act's preamble p. 896 | as cited | VERIFIED verbatim | All three quotations exact at the pages given. | None. |
| N2-33 | N2 (c) Q2 | 1586 decree froze new presses until the bishops judged fit and made breach of Company ordinances a Star Chamber offence; 1637 Register condition and "Twentie Master Printers"; "The Company sought both decrees" | Deazley 1586 s. 5; decree items II, XV; Deazley 1637 s. 4 (Blagden) | VERIFIED verbatim | Each element is in the cited text; "sought both" rests on Blagden's "like the 1586 decree was promoted by the Company". | None. |

---

## Table 2. Facet N3: cards and synthesis claims

| # | Facet/card and line | Claim or quotation as written | Source and locator | Status | What I found | Fix |
|---|---|---|---|---|---|---|
| N3-1 | `alvord1868fifth`; N3 (b) Q7, (c) | p. 7 petition "names and marks (X) …"; "thirty feet in length"; "colored teachers can be taught"; "20,000 teachers"; p. 14 "1,000 are sustained wholly or in part … own 364"; "3,544 colored"; tuition $65,319 75 | Alvord 1868, pp. 7, 14 | VERIFIED verbatim | All present on the page images (p. 7 head visible; the p. 14 crop fits leaf n17 = p. 14 by the same offset as n10 = p. 7). Arithmetic: 1,000/3,084 = 32%; 3,544/6,492 = 55%. `pages_read` says p. 12 was checked on image n15, but no n15 image is in the card's folder. | Save n15 or drop the p. 12 image claim from `pages_read`. |
| N3-2 | `frahm2022fixing` | p. 175 "new deficit logic …", "present 'Responsible Innovation' frameworks as the solution"; p. 176; p. 179; p. 195; p. 200; p. 201; p. 203 "locates both the power …"; p. 182 "quasi-comparative" | STHV 47(1) 174-216 | VERIFIED verbatim | Every quotation on the page given. Crossref agrees (online 15 Mar 2021, issue 2022); no updates. | None. |
| N3-3 | N3 (c) "Where did they put the competence?" | "Frahm et al. give the mechanism a name: deficit construction" | Frahm pp. 175, 201 | OVERSTATED | Frahm et al. name deficit construction for Responsible Innovation at the OECD and EC and never mention literacy. N3 (b) and the card say the transfer is the facet's; (c) drops that caveat. | "Frahm et al.'s 'deficit construction' (pp. 175, 201), which they find in innovation policy, fits this pattern; the transfer to literacy is ours." |
| N3-4 | `israeli2022requerimiento`; N3 (b) Q4 | pp. 39, 42, 46, 47, 48, 61, 62 quotations | LHR 40(1) 37-62 | VERIFIED verbatim | Every quotation on its page (PDF p. 1 = p. 37). Crossref agrees; no updates. The upgrade fixes the old card's partial read. | None. |
| N3-5 | N3 (c) "Where did they put the reading?" | "The colonial Requerimiento kept the reading and dropped the hearer: no translation in practice, no answer, no court (Israeli, pp. 61-62)" | Israeli p. 62 | OVERSTATED | Israeli: "it is doubtful that such instructions were actually fulfilled"; "It is not clear at all that these records ever ended up in courts". He hedges translation and court; the facet states both as fact. | "translation probably not given, no recorded answer, and no evidence that the records reached a court (Israeli, pp. 61-62)". |
| N3-6 | `hill1997gateway`; N3 (b) Q1, (c) | "need not be read to be effective" (1148); "Cashiers cannot …", "Competent adults are bound … read or unread", "oral recitation would not avoid …" (1149); cert. denied 522 U.S. 808 | CAP 105 F.3d 1147 | VERIFIED verbatim | Every pin cite falls after the right star page. Cert. denial entry present ("No. 96-1760 … Certiorari denied"); its sha256 matches the card. Upgrade fixes the old card's missing pins. | None. |
| N3-7 | `jin2003effect` | abstract paraphrase | OpenAlex abstract | VERIFIED paraphrase | Abstract matches, including "not fully explained by consumers substituting". Crossref agrees; no updates. | None. |
| N3-8 | `jones1899meehan` | p. 1 syllabus; p. 4 "by marks only"; p. 5 Moose Dung "weighing and deliberating …", "touched the pen"; pp. 6-7 notary and interpreter; pp. 10-12 canon and McLean; p. 23 holding; pp. 23-24 "unnecessary to consider …"; p. 31 "mere matter of form" | 175 U.S. 1-32 (CAP) | VERIFIED verbatim | All present after the right star pages. | None. |
| N3-9 | `jones1899meehan`, Summary and Critical notes ("a later lease at eight times the rent that the Interior Department had approved"); N3 (b) "a later $200 lease"; claim 7 | Jones's lease was $200 and Interior approved it | 175 U.S. at 7 | WRONG | The lease was made at $200, but the Secretary of the Interior approved it on 27 Dec. 1894 "upon condition … that the annual rent should be four hundred dollars". As approved it was sixteen times the Meehans' $25, not eight. | "a later lease that the Interior Department approved at $400 a year (made at $200), against the Meehans' $25 (pp. 6-7)". |
| N3-10 | `lely1883judicature`; N3 (b) Q2 | r. 13 text; sanction; margin "Extended to blind persons in 1883"; Andrews p. 331 Re Longstaff note | Lely 1883 pp. 276-277; Andrews 1885 p. 331 | VERIFIED verbatim | Text and margin note present; Andrews note read on the page image, exact. | None. |
| N3-11 | N3 (b) Andrews ("supports B1: the reader must not be the interested party's agent"); (c) "done by an officer and not by the party's clerk (Re Longstaff)"; `lely1883judicature` A2 ("a party's own clerk could not do the reading") | Re Longstaff establishes that the party's clerk may not be the reader | Andrews p. 331 | OVERSTATED | The note says only that a managing clerk's statement that he read over and explained the affidavit "was held insufficient to satisfy the Judge". It gives no reason; the rule itself requires the officer's certificate, which may be why. | "A managing clerk's own statement that he had read and explained the affidavit did not satisfy the judge (Re Longstaff, per Andrews p. 331); the reason is not given." |
| N3-12 | `kempf2014cuban` | p. 3 "over 120,632 volunteer teachers, along with 147,788 trained and paid teachers … 24% to 3.9%"; p. 4 "unparalleled", "26 political themes"; p. 7 "first grade reading level", "Battle for the Ninth Grade" | Critical Education 5(4) | VERIFIED verbatim | All present at the pages given. | None. |
| N3-13 | `kempf2014cuban` Critical notes ("the counts of teachers do not [match]"); N3 claim 8 ("268,420 tutors" … "differs from Kempf's 120,632 volunteers plus 147,788 paid teachers") | Kempf's and Bhola's counts disagree | Kempf p. 3; `bhola1984campaigning` p. 97 | WRONG | 120,632 + 147,788 = 268,420, Bhola's total. Bhola's breakdown (card): 120,632 popular instructors + 13,016 workers' brigades + 100,000 Conrado Benítez brigades + 34,772 teachers; 13,016 + 100,000 + 34,772 = 147,788. The figures reconcile exactly. What differs is Kempf's label: he calls the brigadistas and teachers together "trained and paid teachers". | "Kempf's two figures sum to Bhola's 268,420; Kempf labels the brigades and teachers (147,788) as 'trained and paid teachers', which Bhola's breakdown does not support." Withdraw claim 8. |
| N3-14 | `nishimura2013improving` | baseline 54%/50%; abstract SMDs; body SMDs 1.03 and 0.32; Ford 2008 48% vs 52%, p = 0.012; "no substitute for a good conversation"; "No category … consistent efficacy"; illiterate-groups caveat | Europe PMC XML PMC3733934 | VERIFIED verbatim | All present; the abstract/body discrepancy is real (abstract 0.53 and 0.30; body 1.03 and 0.32). Crossref agrees (article 28). | None. |
| N3-15 | `northcarolina1831acts`; N3 claim 3 | preamble; s. I with "give or sell … any books or pamphlets" and "fined, imprisoned, or whipped"; ss. II-III; ANCHOR omits both | NC Digital Collections image; ANCHOR page | VERIFIED verbatim | Read on the image: all exact; lash range "not exceeding thirty-nine … nor less than twenty". ANCHOR's saved text omits the books clause and gives whipping alone, as the card says. The upgrade fixes and corrects the old card. | None. |
| N3-16 | `parker1877south` | p. 421 "wholly immaterial"; p. 422 "exceptional ignorance"; p. 423 "assume that he can read …", "stupidity or carelessness", "under no obligation to read"; p. 424 "reasonably sufficient"; p. 425 onus; p. 426; p. 427 "Read that"; p. 428 "on trust", "implied understanding" | 2 C.P.D. 416 | VERIFIED verbatim | All present; page placement worked out from the OCR's header pattern (verso numbers lead, recto numbers trail), consistent with the card's image checks of pp. 423 and 427. | None. |
| N3-17 | `parker1877south`, A3 ("holds in part. Two juries and Baggallay L.J. would have found for the depositors … the dispute was live within the court") | Contemporaries objected | pp. 417, 426 | OVERSTATED | Jury verdicts and one judge's view of the evidence are a dispute about facts in one case, not contemporaries objecting to the burden of reading as a wrong. Baggallay agreed to a new trial. | "A3: does not hold on this source; the verdicts and Baggallay's view show the facts were contested, not that anyone objected to the rule." |
| N3-18 | N3 (c) "Where did they put the reading?" | "Mellish L.J. denies a duty to read an unsigned ticket and makes the issuer prove notice" | pp. 423-425 | OVERSTATED | Mellish frames the question as whether the company "did what was reasonably sufficient to give the plaintiff notice"; the words on onus ("the onus of proof is, however, upon the company") are Baggallay's (p. 425). | "Mellish L.J. denies a duty to read and asks whether the company gave reasonable notice (pp. 423-424); Baggallay L.J. puts the onus on the company (p. 425)." |
| N3-19 | `pennsylvania1851minutes`; N3 (b) Q3 | p. 656 demand; p. 657 "illiterate Persons", "undoubted Right"; p. 664 "No Indian Chief, before you …", "entirely unprecedented and against my Judgement"; p. 665 Thomson; p. 689 "three or four Times"; p. 690 "exceed my Ancestors", Croghan "quite a new Method" | Minutes vol. VII | VERIFIED verbatim | Read pp. 664, 689, 690 on the images: exact. pp. 656-657 placed by OCR between garbled heads, consistent with the card's images. Two nuances: the "three or four Times" sentence is Pumpshire's bracketed addition ("[John Pumpshire said, I will just mention this in Addition, we ordered him to read it over …]"); and on p. 689 the Governor, not only Croghan, calls it "quite a new Method". | Attribute the read-back sentence to Pumpshire speaking for the Delawares. |
| N3-20 | `seed1995ceremonies` | review paraphrase: read aloud "usually without benefit of translators"; Islamic and Jewish traditions; French attention to native responses; "relic of the first half of the sixteenth century" | Crider, H-LatAm 1996 | VERIFIED paraphrase | All in the review. Secondary card, no quotation from Seed: compliant. | None. |
| N3-21 | `simon2005impact` | p. 32 grading device and "13.1 percent decrease (p < .01)"; p. 35 hidden-camera exposé, more inspections, ecologic design | J Env Health 67(7) 32-36 (DRUM copy) | VERIFIED verbatim | All present on the journal pages (the DRUM file is the journal's pages). Jin and Leslie are co-authors, as the jin card says. | None. |
| N3-22 | N3 (c) "the one disclosure regime with a clean measured protective effect (Simon 2005) works because nobody at the point of use reads"; claim 5; COVERAGE A2 N3 row ("restaurant grade cards cut hospitalisations 13.1%") | Grade cards caused a 13.1% fall, cleanly, by a known mechanism | Simon pp. 32, 35; Jin and Leslie abstract | OVERSTATED | Simon reports an association ("was associated with") from an ecologic design and names three confounds (TV exposé, more inspections, retraining). Not "clean". The mechanism "nobody reads" is the facet's; Jin and Leslie's abstract says the cards changed restaurants' behaviour and made demand respond to hygiene, which means diners did read the letter. | "Grade cards were associated with a 13.1% fall in foodborne-disease hospitalisations (ecologic, confounded; Simon pp. 32, 35); Jin and Leslie attribute the gain mainly to restaurants improving. The reading the diner does is one letter, produced by an inspector." |
| N3-23 | `spain1805novisima`; N3 claim 2 | ley I "las lean, presentes las partes y los testigos …"; "sea en sí ninguna …"; ley III three days; ley IV "en presencia de las partes"; ley V "aunque la otra parte no la pida" | Nov. Rec. t. V, pp. 144-145 | VERIFIED verbatim | Read on the images: exact. Ley IV's collation in the parties' presence concerns copies (traslados) and processes for appeal, which the card's summary states correctly. | None. |
| N3-24 | `tam2015participants` | 103 studies/135 cohorts; 75.8%, 53.3%, 52.1%, 54.9%; "had not increased over 30 years"; Discussion quotations | Bull WHO 93(3) (PMC4371493) | VERIFIED verbatim | All present. Crossref agrees; no updates. | None. |
| N3-25 | `tam2015participants`, A2 ("After decades of signed, disclosed, often read-aloud consent") | consent was often read aloud | Tam, all sections | OVERSTATED | The review does not report how often consent was read aloud. | Drop "often read-aloud". |
| N3-26 | `tamariz2013improving` | abstract paraphrase | Europe PMC abstract | VERIFIED paraphrase | Six of 281 studies, one randomized; teach-back/teach-to-goal highest; readability changes lowest; one-to-one time "based on the results of a single study". Matches. Crossref agrees (online 2012, issue 2013). | None. |
| N3-27 | `unesco2015education`; N3 (b) Q6 | pp. 135, 137, 143, 144, 145, 146, 147 quotations | GMR 2015 full report (Wayback 2017 capture) | VERIFIED verbatim | Every quotation on its printed page (PDF page = printed + 17 confirmed on three pages). Nepal's cohort gain is on p. 144 as claim 6 says. | None. |
| N3-28 | N3 (c) "the 2015 GMR found the Dakar target missed and adult programmes largely without measurable effect (pp. 135, 143-144)" | adult programmes had no measurable effect | GMR pp. 135, 144 | OVERSTATED | The report hedges: progress "may be the consequence of" cohort replacement "and not due to … effective literacy programmes" (p. 135); "considerable doubt is cast on the impact" (p. 144). It credits Nepal and Kha Ri Gude. | "the GMR found that most measured gains came from younger cohorts and cast 'considerable doubt' on the impact of adult programmes (pp. 135, 144)". |
| N3-29 | `virginia1831acts`; N3 (b) Q5 | heading; s. 4 "for teaching them reading or writing", "twenty lashes"; s. 5; s. 6 "for pay or compensation"; s. 8 | Acts 1830-31, pp. 107-108 | VERIFIED verbatim | Read on both images: exact; page break between ss. 5 and 6 confirmed. The upgrade fixes the old card. | None. |
| N3-30 | `wcefa1990world`; N3 claim 4; COVERAGE A3 N3 row | Preamble "960 million"; "for the first time in history — an attainable goal"; Art. 1.1, 1.2, 4; closing "can and must be met"; para. 8 "may wish to set their own [targets]", "say, one-half"; para. 9; para. 31 | ERIC OCR | VERIFIED verbatim | All present (OCR "tars" for "targets", flagged by the card). | None. |
| N3-31 | N3 (c) "They withheld it by statute …, then promised it at scale and blamed the learner when it did not arrive. Jomtien … made its beneficiaries responsible (Art. 1.2, para. 31)" | Jomtien blamed the learner | Jomtien Art. 1.2; para. 31; GMR p. 147 | OVERSTATED | Art. 1.2 says meeting learning needs "confers upon them a responsibility" to respect heritage, educate others and further social justice; para. 31 says learners must see benefits exceed their costs. Neither blames learners for failure. The nearest support is GMR p. 147: campaign language "can stigmatize illiteracy". | "then promised it at scale; the 2015 GMR warns that campaign language 'can stigmatize illiteracy' (p. 147)." Drop "blamed the learner" unless a source that does so is found. |
| N3-32 | N3 claim 1; (d) B1 limb 2; COVERAGE B1 N3 row | B1's second limb holds only for the jurat, art. 193, teach-back and probate r. 13 | Nov. Rec.; Jones pp. 23-24; Easton; Simon; Lely | VERIFIED paraphrase | The new cards bear this out (Pragmática: no check; Jones: declined the negotiation evidence; Easton: a record; grade cards: an inspector). The jurat checks only an impression ("seemed perfectly to understand"). Art. 193 and probate r. 13 are carded elsewhere and not rechecked here. | None. |
| N3-33 | N3 claim 2 | the Pragmática gives the party its own copy within three days and on demand (leyes III, V) | Nov. Rec. p. 145 | VERIFIED verbatim | Exact on the image. | None. |
| N3-34 | N3 claim 6; COVERAGE A3 N3 row (Cuba, Nepal) | Cuba (declared figures) and Nepal are counter-instances | Kempf pp. 3, 7; GMR p. 144 | VERIFIED paraphrase | Holds, provided "declared" stays attached to Cuba (GMR p. 147: Yo Sí Puedo has "no independent evaluations"). | None. |
| N3-35 | COVERAGE D04 N3 row; N3 (c) "Where did they put the record?" | Teedyuscung's own clerk at Easton, 1757; text read back "three or four Times" | Minutes pp. 664-665, 689 | VERIFIED paraphrase | Holds (see N3-19 for the Pumpshire attribution). | None. |
| N3-36 | N3 (c) "Which corrections checked understanding" | jurat certifies an impression; read-aloud trial moved understanding four points | Lely p. 276; Nishimura Table 4 | VERIFIED verbatim | "seemed perfectly to understand"; 48% to 52%. | None. |

---

## Table 3. Legacy history-side cards (item 3)

| # | Card | Claim or quotation as written | Source and locator | Status | What I found | Fix / recommendation |
|---|---|---|---|---|---|---|
| L-1 | `graff1991literacy` | pp. 2, 19, 301, 302, 321 quotations | 1991 Transaction reissue (local), claimed as 1979 | NEEDS LIBRARY CHECK | Every quotation present in the local text at the stated pages (p. 2, 19 in `intro-original.txt`; 301, 302, 321 under the chapter 7 running heads). The defect the card records stands: the pages come from the 1991 reissue, and the 1979 scan is lending-only, so 1979 pagination is unconfirmed. | Keep pending. Either cite the 1991 reissue or check the pages in a 1979 copy. |
| L-2 | `pike1873history` | p. 300 gaolers sentence; p. 301 "taught to read in prison"; p. 483 note on *Liber Assisarum* art. 11 | Pike vol. 1 | VERIFIED verbatim | All present under running heads; p. 300 confirmed on the page image (leaf n335). Two routes. The card's caution that Cross's broader "indictable" rule outruns Pike is right. | Mark `true`. |
| L-3 | `willis2008against` | abstract and draft pp. 3-4, 6, 43-46 quotations | SSRN draft (FAIR Canada copy) | VERIFIED verbatim | All three manuscript quotations present in the draft PDF. But the card's Summary still opens "This card rests on the abstract only; the repository returned 403", which the second-pass notes contradict (the draft was read). Published pages and the title hyphen remain unread. Crossref has no record. | `corrected`: replace the stale first Summary sentence with "Read in the 2008 SSRN draft; the published Iowa L. Rev. text is not read." Keep printed pages flagged. |
| L-4 | `nussbaum2011creating` | p. 20 "might cut off the avenues …"; "at least a threshold level of these ten Central Capabilities" | lending scan `creatingcapabili0000nuss` (FTS) | NEEDS LIBRARY CHECK | I reran FTS: both strings return one hit each in the lending scan. The page (p. 20) rests on the card's chained highlights and an OCR head, one route; no local copy (`local_path: null`). | Keep pending until a library copy confirms p. 20. |
| L-5 | `statute1827criminal` | title and date p. 85; preamble; s. VI p. 86; s. VII; s. VIII; s. XV; s. XVI p. 87 | Statutes of the UK vol. 11 (OCR) | VERIFIED verbatim | All present (OCR "he/hut/thnt" as the card says); s. VI between the heads for 86 and 87. | Mark `true`. |
| L-6 | `roberts1835memoirs` | p. 67 letter heading and "sedition, disaffection …"; p. 72 "hearty concurrence", "I allow of no writing for the poor", "always teach them ourselves"; pp. 72-73 books | Roberts vol. II (Harper 1835) | VERIFIED verbatim | All present under running heads 67, 72, 73; title page "Vol. II … Harper". | Mark `true`. |

**Do the round-1 upgrades fix the old cards' problems?** I compared each superseding card's basis with the old card's.
- `hill1997gateway`: old card writer-grounded for want of pin cites and the cert. denial; new card supplies both from
  CAP star pages. **Fixed.**
- `virginia1831acts`: old card rested on a transcription; new card reads the printed pages. **Fixed.**
- `northcarolina1831acts`: old card rested on ANCHOR; new card reads the printed page and corrects ANCHOR on two
  material points. **Fixed.**
- `milton1644areopagitica`: old card had no pagination; new card has Arber 1868 page locators. **Fixed.**
- `israeli2022requerimiento`: old card read pp. 37-40, 46-47; new card reads the whole article. **Fixed.**
- `jones1899meehan`: old card stopped at p. 12; new card reads to p. 32. **Fixed, but introduces the rent error at
  N3-9.**
- `wcefa1990world`: old card read the goals paragraphs only; new card reads the Declaration and Framework paras 1-42.
  **Fixed.**
- `boretius1883capitularia`: old card read c. 72 only; new card adds nos. 29-30. **Fixed, but see N2-2.**

---

## Table 4. Seeded legacy sample (item 4; seed 20261024, base rate)

| # | Card | Claim or quotation as written | Source and locator | Status | What I found | Agree? |
|---|---|---|---|---|---|---|
| S-1 | `berthon_ethics_course/almeida2019firmo` | "con la consiguiente firma de uno de los testigos, como ordenaba la pragmática" (p. 29); 932 documents (p. 22); CODEA 2273 (p. 23); law via Marchant (p. 24); "falsas firmas" (p. 27); "aún insuficientes" (p. 39) | Philologia Hispalensis 33(1), local text | WRONG | Everything checks except the p. 29 quotation, whose first words are "(y la consiguiente firma …" in the source, not "con la". The card is marked `true`. Crossref agrees (volume/issue swapped there, as the card notes); no updates. | Disagree (minor misquotation inside quotation marks). Fix: "y la consiguiente firma de uno de los testigos, como ordenaba la pragmática de Alcalá". |
| S-2 | `dxd_foundation/burnyeat1997postscript` | Cambridge Core extract; nn. 1, 2, 3, 10, 12 | saved Cambridge Core page | VERIFIED verbatim | Extract and footnotes exact. The card is candid that the main text is unseen. COVERAGE lists it as "partial+verified"; the card's own evidence basis is "secondary". Crossref agrees; no updates. | Agree (the COVERAGE label overstates its depth). |
| S-3 | `berthon_ethics_course/delgamuukw1997` | paras. 87, 93, 98 (two), 99; McLachlin J. para. 209; 11 Dec. 1997; no. 23799 | SCC text | VERIFIED verbatim | All at the paragraphs given. | Agree. |
| S-4 | `algorithmacy_design_ethics/havelock1963` | pp. 39-41 quotations ("supply of readers", "craft literacy", "silent revolution", "oral state of mind") | archive.org `preface-to-plato-havelock` | NEEDS LIBRARY CHECK | Wording confirmed on a clean route: FTS on the 1963 lending scan `prefacetoplato01have` returns each string. Pages still unconfirmed (the card says "probable"). Provenance: the card's copy is a community upload of an in-copyright 1963 book (`opensource`/`community` collections), an unauthorised copy of the kind BRIEF §6 treats as locate-only. The S2 verdict "confirmed" did not note this. | Disagree on status: quotations should rest on the lending scan, with pages confirmed in a library copy. |
| S-5 | `berthon_ethics_course/holmes1975kousser` | pp. 270-272 quotations; 64%/30%/37% | JSH 41(2) review PDF | VERIFIED verbatim | All present ("exConfederate" loses its hyphen in extraction). Crossref agrees; no updates. | Agree. |
| S-6 | `berthon_ethics_course/israeli2022requerimiento` | pp. 39, 46, 47 quotations | LHR 40(1) | VERIFIED verbatim | All on the pages given. Superseded by the N3 card. | Agree. |
| S-7 | `dxd_foundation/knox1968silent` | pp. 421, 422, 427, 432-435 quotations | GRBS 9(4) scan | VERIFIED verbatim | All at the pages given (PDF page 1 = 421). | Agree. |
| S-8 | `berthon_ethics_course/mccord1840statutes` | p. 397 title and preamble; p. 413 s. XLV; s. XLIII; p. 417 s. LVIII and assent; Act No. 702 | McCord vol. 7 OCR | VERIFIED verbatim | All present under running heads; s. XLV's "hereafter taught to write" sits inside the card's ellipsis. No. 702's title says it revives the 1740 Act. | Agree. |
| S-9 | `berthon_ethics_course/unesco2000dakar` | paras. 1, 2, 5, 7(iv); Expanded Commentary paras. 4, 37 | hrlib text | VERIFIED verbatim | All present at the lines given. | Agree. |

**Legacy-sample disagreement rate: 2 of 9 cards (22%)**: one minor misquotation in a `true` card (almeida) and one
provenance and page problem in a "confirmed" card (havelock). Seven of nine agree outright. On a sample this size the
rate is a rough base rate, not an estimate with a tight interval.

---

## Counts

| | N2 (Table 1) | N3 (Table 2) | Legacy (Table 3) | Sample (Table 4) | Total |
|---|---|---|---|---|---|
| Rows checked | 33 | 36 | 6 | 9 | **84** |
| VERIFIED verbatim | 19 | 19 | 4 | 7 | **49** |
| VERIFIED paraphrase | 5 | 6 | 0 | 0 | **11** |
| WRONG | 1 | 2 | 0 | 1 | **4** |
| OVERSTATED | 7 | 9 | 0 | 0 | **16** |
| NEEDS LIBRARY CHECK | 1 | 0 | 2 | 1 | **4** |
| COULD NOT CHECK | 0 | 0 | 0 | 0 | **0** |

VERIFIED (both kinds): 60 of 84. Hash checks: 35 of 35 new-card files match; 11 of 11 legacy files present match (nussbaum2011creating has no file; the three dxd/algorithmacy-format cards
carry no `local_path`).
Crossref: 9 DOIs checked, no update or retraction notices.

---

## Recommendations to the lead

**Mark `true`** (quotations, pages, hash and basis all hold): brinklow1874complaynt, deazley2008commentary1586,
deazley2008commentary1637, foxe1838acts, hall1809chronicle, isambert1828recueil, manuzio1564index,
milton1644areopagitica, statutesrealm1817vol3, tyndale1848doctrinal, frahm2022fixing, hill1997gateway,
israeli2022requerimiento, jin2003effect (abstract card), nishimura2013improving, northcarolina1831acts,
pennsylvania1851minutes (with the Pumpshire attribution noted), seed1995ceremonies (secondary card), simon2005impact,
spain1805novisima, tamariz2013improving (abstract card), unesco2015education, virginia1831acts, wcefa1990world;
legacy pike1873history, statute1827criminal, roberts1835memoirs.

**Mark `corrected`, with the fix:**
- boretius1883capitularia: c. 72 is a recruitment-and-schools clause; drop "widens whom the page served" (N2-2).
- commons1803journal: reason 3 says "others", not authors; drop "authors" from the list of the harmed (N2-5).
- cranmer1846miscellaneous: "barred exactly those groups" → "barred several of those groups" (N2-10).
- furnivall1871four: the petition objects to "a lawe" with an income-and-possession test; its identity with the 1543
  Act is probable, not shown (N2-13).
- reusch1883index: Spain and Portugal banned outright under their own indices; Rule IV was enforced in Italy and
  Belgium (N2-19).
- starchamber1637decree: the 1642 order fixes responsibility as much as it protects authors; p. 24 is inferred
  (N2-20, N2-21).
- statutesrealm1819vol4: "the first statute" → "chapter 12" (N2-25).
- alvord1868fifth: remove the p. 12 image claim from `pages_read` or save image n15 (N3-1).
- jones1899meehan: Interior approved Jones's lease at $400, not $200; "eight times" → sixteen times (N3-9).
- kempf2014cuban: Kempf's two figures sum to Bhola's 268,420; the difference is labelling (N3-13).
- lely1883judicature: Re Longstaff gives no reason; do not say the party's clerk "could not do the reading" (N3-11).
- parker1877south: A3 "holds in part" → "does not hold on this source" (N3-17).
- tam2015participants: drop "often read-aloud" (N3-25).
- legacy willis2008against: replace the stale "abstract only; 403" Summary sentence (L-3).
- sample almeida2019firmo: "con la" → "y la" in the p. 29 quotation (S-1).

**Keep `pending`:** graff1991literacy (1979 pagination unconfirmed), nussbaum2011creating (p. 20 on one route, no
local copy); and, in the sample, havelock1963 should be re-sourced from the lending scan and its pages confirmed
before it carries quotations.

**Facet text the lead should not carry into the paper as written** (all in Tables 1-2): N2 (b)/(c)/(d) and COVERAGE
"one direct objector" (N2-13); N2 (d) "authors' 'Labour and Right'" (N2-5); N2 Q5 "bound in Spain" (N2-19); N2 claim 3
"Innis's 1694 is wrong" (N2-29); N2 (b) Saenger phrase (N2-27); N3 (c) Israeli "no translation … no court" (N3-5);
Mellish and the onus (N3-18); Frahm "give the mechanism a name" (N3-3); "blamed the learner" (N3-31); GMR "largely
without measurable effect" (N3-28); grade cards "clean" and "cut 13.1%" (N3-22, also the COVERAGE A2 row); claim 8 on
the Cuban tutors (N3-13).
