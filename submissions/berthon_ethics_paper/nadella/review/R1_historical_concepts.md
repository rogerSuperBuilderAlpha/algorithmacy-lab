# R1 — Historical concepts and claims

*Run R1 of the R round, 2026-10-24. Agent-drafted. The author has not reviewed it. This file reviews substance only:
whether each historical concept is used as the historians who own it use it, and whether each historical claim is the
consensus, a contested reading, or neither. It proposes no wording.*

## Scope

- Ledger rows H01–H29 and L01–L06 (`../../consolidation/CONCEPT_LEDGER.md`), read against the draft as it now
  stands; rows the draft no longer uses are noted where the omission matters (H12, H13 Graff and Jomtien, H17, H26).
- Premises A2, A3, B1 (`../ARGUMENT_AND_OUTLINE.md` v2).
- `../manuscript/DRAFT_v1.md`: the abstract (ll. 12–20); the opening's history (ll. 54–61, 72–78); §2 (ll. 142–289);
  the historical claims inside §3 (ll. 313–317, 346–351, 364–366, 384–387, 398, 421–423, 431–434), §4 (ll. 447–455,
  466, 492–501) and §5 (ll. 520–533, 535–544, 549–552); footnote `[^stationers]` (l. 554).
- Cards: the N2/N3 cards in `../../literature/cards/berthon_ethics_paper/` and the course cards they cite, as
  adjudicated in `../facets/ADJUDICATION.md`; `AUDIT_N7a.md` was read in full and its corrections are taken as applied.
- Seven new cards (facet R1): `lassiter1959northampton`, `foxe1837acts`, `knapp2015duty`, `thomson1759enquiry`,
  `deazley2008commentary1662`, `blayney2013stationers` (secondary), `clegg1997press` (abstract).

## Search log

All requests on 2026-10-24, curl with a plain user agent or the WebFetch tool. No email address, `mailto` or Unpaywall.
No paywall, bot wall or CAPTCHA was bypassed; each block is logged. Downloads, each in its own subdirectory of
`~/iit-playground/berthon_ethics_local/pdfs/nadella/R1/`, were read with `python3 -I` or `pdftotext`.

| # | Source | Exact query or URL | Hits | Notes |
|---|---|---|---|---|
| 1 | Repo reads | `BRIEF_R.md`; `facets/BRIEF.md`; `CONCEPT_LEDGER.md` (all rows); `ARGUMENT_AND_OUTLINE.md`; `DRAFT_v1.md` (whole); `N2_*.md`; `N3_*.md`; `AUDIT_N7a.md`; `ADJUDICATION.md`; `CARD_INDEX.md` greps; cards `saenger1997space`, `odonnell2000saenger`, `garrett1998saenger`, `parkes1992pause`, `heilmann2020reading` (dxd), `lestrange1934graucob`, `upton1875tribilcock`, `katzenbach1966south`, `gaston1969gaston`, `alabama1901official`, `sudore2006use`, `graff1991literacy`, `johns2002how`, `arber1875transcript`, `eisenstein2002`, `johns1998` (ade), `israeli2022requerimiento`, `pennsylvania1851minutes`, `spain1805novisima`, `lely1883judicature`, `statutesrealm1817vol3`, `parker1877south`, `spain1944reglamento`; dxd facets A and K (Saenger and Parkes provenance) | n/a | Fixed what the existing library already settles and where its quotations come from. |
| 2 | archive.org full-text search (`be-api.us.archive.org/fts/v1/search`) | `"provided shortcuts for achieving the reading skills"`; `"not a general history of literacy"`; `"until the mid-tenth century"`; `"elitist literate mentality"`; the first two also scoped to `identifier:spacebetweenword0000saen` | 1; 1; 5; 4; 0; 0 | The two Saenger 1997 sentences hit **only** the unauthorised upload `space-between-words-the-origins-of-silent-reading`; the authorised lending scan `spacebetweenword0000saen` returned nothing (not indexed for guests). `"elitist literate mentality"` also hits `literacyorality0000unse` (Olson and Torrance, *Literacy and Orality*, CUP 1991, an authorised lending scan: Saenger's 1991 chapter carries the same sentence) and a 1998 *Lingua Franca* scan. Wording confirmed on a clean route for the 1991 chapter only; no page. |
| 3 | archive.org metadata | `metadata/literacyorality0000unse`; `metadata/spacebetweenword0000saen` | 2 | 1991 CUP volume; the 1997 scan is `access-restricted-item: true`. |
| 4 | De Gruyter | `degruyterbrill.com/document/doi/10.1515/9781503619081/html` | HTTP 202, empty | Same as N2. Not retried. |
| 5 | Crossref `query.bibliographic` / `works/<doi>` | Blayney 2013; Watson 1995; Ganz 1987; Spencer 1973; Astbury 1978; Clegg 1997; Merrell 2006; Hanke 1938; Knapp 2015 | 7 resolved | DOIs: `10.1017/cbo9781139542715`; `10.2307/2865345` (Speculum 70(4) 822–864); `10.1484/j.viator.2.301384` (Viator 18, 23–44); `10.1017/s0008197300090255` (CLJ 32(1) 104–122); `10.1093/library/s5-xxxiii.4.296` (Library s5-33(4) 296–322); `10.1017/cbo9780511585241`. Merrell 2006 (WMQ 63(4) 777–826) and Hanke 1938 have no Crossref record; Knapp has no DOI. Records saved under `R1/crossref/`. |
| 6 | OpenAlex `works/doi:` | Watson, Spencer, Ganz, Astbury | 4 | All `is_oa: false`, no `oa_url`. OpenAlex `search=`/`filter=title.search` queries returned nothing usable (4 queries). |
| 7 | Caselaw Access Project | `static.case.law/us/360/CasesMetadata.json`; `.../html/0045-01.html` | 200 | *Lassiter v. Northampton* with star pages. Card. |
| 8 | archive.org advancedsearch and download | `title:(acts and monuments) AND creator:(foxe) AND year:[1837 TO 1849]`; `actsmonumentsofj03foxe_djvu.txt`; `actsmonumentsof03foxe_djvu.txt` | 19; 2 | Cattley vol. 3 (1837), two independent scans. Arundel's seventh constitution fixed at p. 245 in both. Card. |
| 9 | WebSearch; curl | `Knapp "Is There a Duty to Read" Hastings Law Journal 2015 pdf`; `propertyinsurancecoveragelaw.com/.../Knapp-66.4-1.pdf`; `repository.uclawsf.edu` search | 9; 200; no result parsed | Journal typeset PDF obtained from a law-firm repost; the UC Law SF repository search page gave no parsable result. Card (partial). |
| 10 | archive.org advancedsearch and download | `title:(enquiry into the causes of the alienation)`; `enquiryintocause00thom_djvu.txt` | 6; 200 | Thomson 1759. Card. |
| 11 | copyrighthistory.org | `showRecord.php?id=commentary_uk_1695` (WebFetch: "Object Not Found"); `record_uk_1695` (record only, no commentary link); `record_uk_1662`; `commentary_uk_1662` (curl, 200) | — | Deazley's 1662 commentary, §6 "John Locke and the Lapse of the Licensing Act", read in full. Card. |
| 12 | WebSearch | `Blayney "Stationers' Company and the Printers of London" 1557 charter censorship review` | 10 | Led to Smyth's LRB review (open) and Helen Smith's TLS review (paywalled; the SHAKSPER repost returned 403). |
| 13 | WebFetch; curl | `lrb.co.uk/v37/n16/adam-smyth/231538-198977-15635` | 200 | Read in full; saved. Secondary card for Blayney. |
| 14 | WebFetch | `doi.org/10.1017/cbo9781139542715` → `cambridge.org/core/product/identifier/9781139542715/type/book`; same for `9780511585241` (Clegg) | 200; 200 | Descriptions and chapter lists only; chapters behind login. Saved. |
| 15 | WebFetch | `canlii.org/en/on/onca/doc/1978/1978canlii1446/...` (*Tilden Rent-A-Car v. Clendenning*) | 403 | Blocked. Not retried. |
| 16 | WebSearch | `Merrell "I desire all that I have said" Teedyuscung 1756 ... William and Mary Quarterly 2006` | 9 | HSP catalogue record confirms WMQ 63(4) (Oct. 2006) 777–826. Text not reached (JSTOR). |
| 17 | Consensus; Scholar Gateway | not used | — | The scope items are primary texts and named monographs; Crossref, OpenAlex and archive.org covered them. |

## Entries

Each entry: what the draft says (line numbers); how the owning literature treats it (exact quotation with locator from
a source opened in this or an audited round; cards named); the gap; verdict.

### R1-01. *Scriptio continua* "for most of antiquity" (l. 151)

Draft: "For most of antiquity a Latin or Greek text ran without spaces between its words."
Literature: Heilmann (2020, pp. 182–183; dxd card `heilmann2020reading`, read in full there) follows Wingo and the
Vindolanda tablets on the Roman use of interpuncts and their abandonment in the second century; the dxd card's own
relation note says "The Latin evidence (interpuncts, then their decline) shows that spacing was not a one-time
invention in the seventh century." Saenger's own introduction (facet A, p. 9–11 of the unauthorised copy) says the same.
Gap: Latin was word-separated by points for the Republic and early Empire; unspaced Latin is a second-century
adoption from Greek practice. Verdict: **narrower** (true of Greek throughout and of Latin after c. 200 AD).

### R1-02. Silent reading in antiquity (ll. 152–153)

Draft cites Knox (1968, 434–435). Card `dxd_foundation/knox1968silent` (verified verbatim in N7a's sample, pp.
432–435); Gavrilov (1997) and Burnyeat (1997) carded in dxd. The draft's claim is the classicists' consensus since
1968 and is stated without overreach. Verdict: **holds**.

### R1-03. "The scribes' correction": Insular word separation moved work from reader to artifact (ll. 55–58, 155–164)

Draft: Insular scribes separated words "for readers who met Latin as a foreign tongue (Parkes 1992, 1; Saenger 1997,
83–87)"; "the scribes moved work from the person to the artifact".
Literature: Saenger (1997, p. 2, via facet A) premises the book on "a correlation between a propensity to read orally
... and the threshold in the duration of cognitive activity needed to achieve lexical access in that culture's
script". O'Donnell (2000, ¶4; card `odonnell2000saenger`) calls the physiology-to-practice link "the most venturesome
and vulnerable part of the book". Heilmann (2020, p. 178) says Saenger's arguments "cannot carry the burden of proof"
and "presuppose precisely what must be proved", and quotes Vatri (2012, 639): "there is no reason to assume that
reading unspaced text is a particularly demanding cognitive task in itself, and Saenger's model must be rejected"
(p. 181). Heilmann concedes the slowing for untrained modern readers (p. 180) and reads the ancient complaints as
about learners (n. 28). Parkes (1992, p. 1; snippet, facet K): "Because many had to learn Latin as a foreign language,
there was a need for conventions which made it easier to read."
Gap: the draft takes the cost-to-learners reading, which survives Heilmann, and avoids the silent-reading causal
claim, which does not. "The scribes' correction" is the paper's term; no historian periodizes with it. The Saenger
dating (Irish, before 692 and 713; Continent mid-tenth century, standard mid-eleventh) is Saenger's own chronology,
confirmed by Tunbridge (1992), a thesis supervised by Parkes and so not an independent test (facet A).
Verdict: **contested** (the paper must say that Saenger's physiological premise is rejected by Vatri and Heilmann and
that the claim it keeps is the narrower one about learners; the periodizing label is the paper's own).

### R1-04. Saenger quoted (ll. 160–162, p. 85; l. 175, p. x; dates at ll. 158–159, 166–167)

Draft quotes Saenger (1997, 85) at length and (1997, x) in part, and relies on pp. 83, 87, 100.
The Saenger rule (`facets/BRIEF.md` §6; `ADJUDICATION.md` §5.2): a quotation may stand only after a clean route shows
the same words on the same page. Search 2 above: both sentences are found by archive.org full-text search **only in the
unauthorised upload**; the authorised lending scan returns nothing; Google Books served a CAPTCHA in N2; De Gruyter
returns an empty page. The 1991 chapter's twin of the p. 11 sentence is in an authorised scan, but that is a different
work and page.
Gap: the draft's two direct quotations and three page citations rest on the copy the brief forbids quoting from.
Verdict: **unsupported** (as quotation and page citation, until a library copy or Google Books in a browser confirms
pp. x, 83, 85, 87, 100).

### R1-05. "The conventions of the Carolingian page were set from above" (ll. 166–172, 174–178)

Draft: cites Charlemagne's *Epistola generalis* (Boretius 1883, 80–81) for the claim that the page's conventions
"belonged to the ruler and the church".
Literature: the capitulary texts concern the correction of texts, not page layout: the king corrected "universos
veteris ac novi instrumenti libros, librariorum imperitia depravatos" (no. 30, p. 80) and fixed the homiliary "nostra
... auctoritate" (p. 81); c. 72 asks for correct books because men "per inemendatos libros male rogant" (p. 60) (card
`boretius1883capitularia`, verified verbatim in N7a; N7a N2-2 already cut the overreach on c. 72). The N2 facet's own
verdict: "Holds as custody of correct text; no source ties it to word separation" (N2 (d)). Saenger's chronology (facet
A, p. 34) has the Carolingian page *aerated*, not word-separated, with separation reaching the Continent only in the
mid-tenth century (p. 100); Parkes's chapter "Carolingian *Renovatio*: Augmenting Old Notation with New Symbols" (pp.
30–34, card structure only) credits scribes with the new graphic conventions. The historians of the script reform
(Ganz 1987, `ganz1987preconditions`, record only; McKitterick 1989, record only in N2) are unread; N2 (b) already
warned that "a library read is needed before the paper says the Carolingian page was held only from above".
Gap: the draft slides from custody of the *text* (emendatio, which the sources show) to custody of the page's
*conventions* (which no source in hand shows and which Saenger's chronology places later and elsewhere).
Verdict: **misused** (the cited sources carry custody of correct text, not of the convention the moment is about);
the moment's duality survives if restated as custody of the text and of the books read in church.

### R1-06. The Stationers' charter: terms, date and purpose (ll. 182–189, 313–315, fn. l. 554)

Draft: the charter "confined printing to members of the company or to holders of royal letters patent", gave search and
seizure, and "Custody of the medium was given to the trade that profited from it, as an instrument of the Crown's
control of what could be read".
Literature: the charter's terms and preamble are as the draft says (card `arber1875transcript`, pp. xxviii–xxxi,
verified). Date: "4 May 1557" (Smyth 2015 reporting Blayney; card `blayney2013stationers`); the footnote's regnal-year
reasoning is right. Purpose is where the owning literature has moved. Blayney (2013), as Smyth reports him, separates
the Company's motive (enforcing its new commercial monopoly) from the Crown's (regulating the trade after the Marian
purge of Edwardian printers), and treats the received Greg–Blagden account as error. Clegg (1997, description; card
`clegg1997press`) finds Elizabethan press control "not a routine nor a consistent mechanism but an individual response
to particular texts". Johns (2002, p. 119; card `johns2002how`): licensing "was part and parcel of the regimes of
privilege and registration, which were designed to protect good works as well as to hinder bad".
Gap: the draft states the Arber–Siebert reading as fact. The trade's custody holds; "an instrument of the Crown's
control of what could be read" is one side of a live dispute, and the record of enforcement (Clegg) is thin.
Verdict: **contested** (name Arber/Siebert against Blayney, Clegg and Johns; keep the custodian, qualify the purpose).

### R1-07. Trade objections 1577–1586; Wolfe and Bourne; "guardians of the press" (ll. 191–198)

All quotations are Deazley's (2008, §§4–5) from Arber vols. 1–2, verified verbatim in N7a (N2-7); Arber vols. 2 and 4
remain lending-only (N2 gaps). The draft attributes them correctly. Verdict: **holds** (period voices at one remove).

### R1-08. The 1586 and 1637 decrees and the 1662 Act (ll. 198–202)

Cards `deazley2008commentary1586`, `starchamber1637decree` (items II, XV, pp. 9–10, 16), `statutesrealm1819vol5`
(verified). Deazley 2008 (1662 commentary, §2): the Act "represents the last occasion on which the censorship of the
press was formally and strategically linked to the protection of the economic interests of the Stationers' Company".
Verdict: **holds**.

### R1-09. "Reading itself was licensed": the 1543 Act, and "statutes that licensed who could read" (ll. 59, 204–216, 225–227)

Draft: the Act's bar on "woomen nor artificers ... husbandemen nor laborers" (p. 896), its professed purpose, the
1546 *Supplication*, the 1547 repeal; the opening speaks of "statutes that licensed who could read" and §2.2 closes on
"the license to read to a designated few".
Literature: the Act's text and preamble are verified (`statutesrealm1817vol3`, pp. 896–897). N2's own finding (claim
5): "The bar lasted four years (1543–1547) and was repealed by the next reign, not by the barred ... the paper should
not treat it as a standing print-era regime." The *Supplication*'s identification with the Act is "probable, not shown"
(N7a N2-13; adjudicated), and the draft now says so (ll. 213–216). The plural "statutes" has one instance. And licensed
reading predates print: Arundel's seventh constitution (1409) ordered "that no man read any such book, libel or
treatise, now lately set forth in the time of John Wickliff, or since ... until the said translation be allowed by the
ordinary of the place" (Foxe 1837, vol. 3, p. 245; card `foxe1837acts`, two scans).
Gap: the draft presents licensed reading as a print-stage institution; the record shows a four-year statute repeating a
manuscript-era canon.
Verdict: **narrower** (one Act, four years, a pre-print precedent; "statutes" should be singular or dropped).

### R1-10. Cranmer's prologue as the professed standard (ll. 209–211)

Card `cranmer1846miscellaneous` (p. 121, verified); N7a N2-10 narrowed "exactly those groups" to "several of those
groups", and the draft's wording ("among the proper readers ... artificers, husbandmen") already fits the narrower form.
Verdict: **holds**.

### R1-11. Tridentine Index Rule IV and its enforcement (ll. 216–220)

Cards `manuzio1564index` (p. 15) and `reusch1883index` (pp. 333–336), verified; the draft carries N7a's correction
(Spain and Portugal banned outright under their own indices; north of the Alps often not observed). Johns (2002, p.
119): "in France, for example, the Index was effectively ignored." Verdict: **holds**.

### R1-12. The Commons' reasons of 1695 (ll. 220–224)

Draft: "When licensing ended, Parliament itself gave the reasons", quoting reasons 3 and 12.
Literature: quotations verified (`commons1803journal`; N7a N2-4, N2-5 applied: "others", not authors). Deazley (2008,
1662 commentary, §6; card `deazley2008commentary1662`): the Act "finally expired" in May 1695 after the Commons
refused to revive it; the committee's arguments "like Locke's, had little to do with freedom of speech and the liberty
of the press" and "preferred instead to focus on the more practical and commercial implications"; Kenyon: "rather than
any abstract love of freedom". Astbury (1978) is the authority Deazley cites and is unread (paywall).
Gap: the draft uses the reasons for monopoly and self-dealing, which is what the literature says they were; it should
not let "when licensing ended" imply a verdict on licensing. Verdict: **holds** (narrowed to trade grievances; lapse by
expiry, not repeal).

### R1-13. "The duty to read" as a concept; *Upton* (ll. 231–234, 398)

Draft: "Courts developed a duty to read", quoting *Upton* (1875, 50); §3.3 calls the vendors' terms "*Upton*'s rule in
a new medium".
Literature: *Upton* quotations exact at p. 50 (card `upton1875tribilcock`, verified). Knapp (2015; card
`knapp2015duty`): the "duty to read" "is not a 'duty' imposed by contract, but rather a statement about how parties"
are treated (p. 1085); it is "commonly expressed ... in two ways: as a 'duty,' and as a 'presumption'" (p. 1085), is
overcome by interpretation, lack of assent, mistake and fraud (pp. 1089–1092), and "would better be denominated as 'a
presumption of knowing assent'" (p. 1083). Macaulay (1966) is the classic treatment (Knapp n. 1; not opened).
Gap: the owning literature treats the "duty" as a label for a rebuttable allocation of risk with standard defences; the
draft treats it as an obligation courts imposed. *Upton* itself concerned a literate investor holding the documents
(card note).
Verdict: **narrower** (keep the courts' phrase; state it as a presumption of assent with defences, which is also what
the draft's "carry the risk" correction must be measured against).

### R1-14. *L'Estrange* "made the same rule absolute" (ll. 234–237; opening l. 59; §5 l. 530)

Draft: the signer "is bound, and it is wholly immaterial whether he has read the document or not"; Maugham L.J.'s
regret; the opening: "courts that bound the signer to whatever she signed".
Literature: Scrutton L.J.'s sentence begins "When a document containing contractual terms is signed, then, in the
absence of fraud, or, I will add, misrepresentation, the party signing it is bound" (p. 403; card
`lestrange1934graucob`, verified); the court was the Divisional Court, not the Court of Appeal (headnote, p. 395);
Maugham L.J.: "I regret the decision to which I have come, but I am bound by legal rules" (p. 405). Spencer (1973,
CLJ 32: 104–122, `spencer1973signature`, record only) is the standing critique; *non est factum* (`foster1869mackinnon`,
H10) and later statute (UCTA 1977) cabin the rule; *Tilden v. Clendenning* (Ont. C.A. 1978) could not be opened (403).
Gap: "absolute" omits the fraud and misrepresentation limbs stated in the rule itself and the *non est factum*
exception the ledger already carries (H10).
Verdict: **narrower**.

### R1-15. *Parker v. South Eastern Railway* (ll. 237–240)

Draft: the company "was 'entitled to assume that he can read, and that he understands the English language' (423,
Mellish L.J.)"; "The reading was the signer's work, and the courts treated it as done."
Literature: quotation exact (card `parker1877south`, p. 423). But Mellish L.J. denied any duty to read an unsigned
ticket and asked whether the company "did what was reasonably sufficient to give the plaintiff notice of the
condition" (p. 424); Baggallay L.J. put "the onus of proof ... upon the company" (p. 425); new trials were ordered for
the depositors (N7a N3-17, N3-18 applied). N7a: A3 "does not hold on this source".
Gap: *Parker* is the counter-current to the signature rule, not an instance of it; the presumed English reader is the
one phrase that points the draft's way.
Verdict: **narrower** (use it for the presumed reader, not for "treated as done").

### R1-16. The Requerimiento: Castilian procedure, colonial loss, "Castile's own standard" (ll. 242–250, 346–351, 421–423)

Draft: Israeli's account of the *testimonio de requerimiento* and its colonial loss; "The colonial use broke Castile's
own standard for the procedure"; §3.4: Nadella's disclosure "leaves those affected where the requerimiento left its
addressees: informed after the fact that something was done to them".
Literature: Israeli (2022) quotations exact (card `israeli2022requerimiento`, verified; N7a N3-5's hedges, "it is
doubtful", "It is not clear at all", are in the draft). On origin the literature divides: Seed (1995, ch. 3; card
`seed1995ceremonies`, review depth) roots the ritual in the Islamic summons; Israeli reports and qualifies that via
Devereux and Herzog (pp. 39–40, n. 8) and roots it in Castilian notarial practice; Muldoon (1980) and Pagden place the
text in canon-law debate on infidel *dominium*, which "makes the colonial requerimiento coherent by its own jurists'
standard, which Israeli does not dispute" (card, Critical notes). So "Castile's own standard" is Israeli's standard;
by the canonists' standard the form was defensible, and Las Casas and Oviedo (ledger H18) are the contemporaries who
objected.
On timing: the Requerimiento was read *before* the attack (ledger H18: "Read aloud in Spanish before an attack"); its
failure was notice the hearer could not understand or answer, not notice after the fact.
Verdicts: ll. 242–250 **contested** (name Seed and Muldoon beside Israeli; the A3 limb should rest on Las Casas and
Oviedo as well as Castilian procedure); l. 422 **wrong** (the addressees were informed before, not after; the shared
property is notice without the means to answer).

### R1-17. Alabama 1901, *Katzenbach*, *Gaston* (ll. 252–259, 385–387)

Draft: Knox's "to establish white supremacy" (p. 8) and his recorded objection (p. 11); *Katzenbach* (310, 312);
*Gaston* (293).
Literature: all quotations verified in the course cards (`alabama1901official`, `katzenbach1966south`,
`gaston1969gaston`). The complication is *Lassiter v. Northampton County Board of Elections*, 360 U.S. 45 (1959; card
`lassiter1959northampton`): a unanimous Court held that "The ability to read and write likewise has some relation to
standards designed to promote intelligent use of the ballot" (p. 51), "We do not sit in judgment on the wisdom of that
policy" (p. 53), and the North Carolina test was "not a calculated scheme to lay springes for the citizen" (p. 54).
*Katzenbach* reaffirmed *Lassiter* (383 U.S. at 333) and suspended the tests for purpose, framing and administration
(pp. 333–334); *Gaston* turned on "separate and inferior schools" under §4(a), a statutory burden, not a constitutional
defect (card notes). The *Katzenbach* account of administration rests on suits in three States (card, Critical notes).
Gap: by the era's own judicial lights the gate as such was lawful until 1965; what the courts condemned was design,
administration and state-caused illiteracy. The draft's "Literacy also became a gate" and §3.3's "registrars, bishops,
master printers" hold; the A3 verdict attaches to the registrars' discretion and the schools, not to literacy as a
qualification.
Verdict: **narrower**.

### R1-18. Virginia and North Carolina, 1831 (ll. 259–262)

Cards `virginia1831acts` (p. 107, s. 4) and `northcarolina1831acts` (preamble; ch. VI), read on the page images and
verified in N7a. The two statutes belong to each State's 1830–31 session; "the same session" is loose across two
legislatures but not wrong. Verdict: **holds**.

### R1-19. Dakar's promise and the 2015 GMR (ll. 262–266; §3.4 l. 431)

Quotations exact (`unesco2000dakar` para. 7(iv); `unesco2015education` p. 135, with the report's hedge "may be the
consequence of" carried into the draft). Jomtien (H13) is no longer used; N7a N3-30/31 found Jomtien's halving target
optional and found no source for "blamed the learner", and the draft uses neither. Verdict: **holds**.

### R1-20. The Pragmática of 1503 (ll. 268–270, 537–538)

Draft: "Isabella's Pragmática of 1503, as the *Novísima Recopilación* (1805, 144–45) preserves it".
Literature: heading "D.ª Isabel en Alcalá por pragmática de 7 de Junio de 1503 cap. 1." (p. 144); the reading
"presentes las partes y los testigos", the witness's signature, the party's copy (leyes III, V) all exact (card
`spain1805novisima`, read on the page images, verified). The card's caution stands: this is the 1805 compilation's text,
not the 1503 print; Marchant (2015, carded) reads the 1503 text. Andrien's review of Burns (carded, H10) records Cuzco
notaries who served the powerful despite the rule. Verdict: **holds** (as a professed standard; not as practice).

### R1-21. Easton 1757: Teedyuscung's clerk (ll. 270–274, 349–350, 384–385, 526)

Draft: the demand (p. 656), the Governor's "entirely unprecedented" (p. 664), "a stronger remedy, demanded by the party
himself".
Literature: minutes exact (card `pennsylvania1851minutes`, verified; the "three or four Times" sentence is
Pumpshire's, N7a N3-19). Thomson (1759, pp. 110–112; card `thomson1759enquiry`) supplies the motive the minutes omit:
Teedyuscung "had seen the Secretary of the Province, at the last Easton Treaty, throw down his Pen, and declare he
would not take Minutes when Complaints were made against the Proprietors" (p. 110), and names the clerk as "one Charles
Thomson, who had, at the particular Request of Mr. Peters, taken Minutes at the last Easton Treaty" (p. 112), that is,
the author himself, writing for the Friendly Association. Croghan and Weiser alleged Quaker prompting (minutes pp.
657–658). Merrell (2006, WMQ 63: 777–826; record only) studies the rival minutes of 1756.
Gap: the correction holds and now has the objector's own stated reason; "demanded by the party himself" is true of the
demand and incomplete about the clerk, who was a Quaker schoolmaster the Province's secretary had used the year before.
Verdict: **holds** (contested on who stood behind the clerk; state both).

### R1-22. The 1883 jurat (ll. 274–276, 364–366, 529–530)

Draft §2.3: the officer certifies the reading and that the deponent "seemed perfectly to understand it"; §5: "as the
1883 rule refused an affidavit without the officer's certificate".
Literature: r. 13 exact (card `lely1883judicature`, pp. 276–277, image-checked). The sanction clause continues: "unless
the court or a judge is otherwise satisfied that the affidavit was read over to and appeared to be perfectly understood
by the deponent" (pp. 276–277); the margin note "Extended to blind persons in 1883" shows the illiterate-deponent rule
predates 1883 (card). Re Longstaff gives no reason (N7a N3-11 applied).
Gap: §5's "refused" overstates a rule with a judicial escape; "1883" dates the consolidation, not the rule.
Verdict: **narrower** (for l. 530; §2.3's statement holds).

### R1-23. Spain's art. 193 (ll. 276–278)

Draft: "Spain's notarial regulation counts a reading as complete only when ... 'cabal conocimiento de su alcance y
efectos' (Spain 1944, art. 193)".
Literature: the quoted paragraph is the text as amended by RD 45/2007, in force 30 January 2007 (card
`spain1944reglamento`: "The 2007 wording of art. 193 is a late development. I did not read the earlier versions").
Gap: the citation year implies a 1944 standard; the standard quoted is 2007. Verdict: **narrower** (date the wording).

### R1-24. Sudore et al. 2006 (ll. 278–281)

Draft: 28 percent "after the form was read to them", 98 percent "after teaching to a standard".
Literature: "Only 28% of subjects answered all comprehension questions correctly on the first pass"; "With a
teach-to-goal strategy, 98% of participants who engaged in the consent process achieved complete comprehension" (card
`sudore2006use`, abstract and Results, verified). The form was already simplified to sixth-grade level and read aloud;
the design is descriptive with no control arm; 98% is of the 204 who completed. Verdict: **holds** (narrow, as the
draft states it).

### R1-25. Los Angeles grade cards (ll. 281–283, 531–532)

Draft: "associated with a 13.1 percent fall" (Simon et al. 2005, 32).
Adjudication §6 (A2 disclosure): association from an ecologic design with named confounds; Jin and Leslie's abstract
has diners reading the letter and restaurants improving. The draft carries "associated with" and "an inspector's
judgment in a letter on the door". Verdict: **holds** (as corrected).

### R1-26. The two courses as a periodization: "the scribes' correction" vs "the print stage" (title; abstract ll. 15–17; ll. 55–61, 146–147, 285–289, 549–552)

Draft: "The record holds two courses"; "its growth was governed twice"; "the insider-risk architecture repeats the print
stage and not the scribes'".
Literature: (a) Licensed reading predates print (Arundel 1409, R1-09). (b) Print also moved work onto the artifact:
Parkes's chapter "The Technology of Printing and the Stabilization of the Symbols" (pp. 50–61; card structure);
Eisenstein's "standardization, dissemination, and fixity" (Johns 1998, p. 10, snippet in `ade/johns1998`), against which
Johns holds that fixity "was far rarer and harder to discern ... than most modern historians assume" (p. 36) and was a
social achievement (`johns2002how`, p. 121: the bishop of Freising checking each printed missal). (c) The Insular
correction ran under church custody, as the draft itself concedes (ll. 166–172). (d) The press regime described is
England's (ledger H11: "One kingdom, no count of the excluded"); Johns (2002, p. 119) "can think of no Protestant state
before 1695 without a press regime", and the Index was ignored in France. (e) The draft's own l. 147 says "the choice
could go either way".
Gap: no historian in the library periodizes literacy's growth into these two stages; the two "courses" are choices
present in each period, and the draft's own evidence (Arundel; Carolingian custody; print's fixity) shows both choices
in both periods. The analogy (A6) does not need the periodization; it needs the property.
Verdict: **narrower** (two recurring choices, not two stages; "print stage" is defensible only as a label for England's
press regime 1557–1695, which the paper should say).

### R1-27. The Johns–Eisenstein debate (ledger H12; implicit at ll. 182–227)

The draft argues the Johns side (custody and licensing made print what it was) without naming Eisenstein's thesis that
the press itself democratized and fixed texts. Cards: `johns2002how` (full), `ade/eisenstein2002` (second-hand via
Johns), `ade/johns1998` (snippets). Eisenstein (2002) remains unread (OUP paywall, N2). Verdict: **contested** (the
paper must name the debate it is taking a side in).

### R1-28. Graff's "literacy myth" and the require/reward distinction (ledger H13, H16, H17; not in the draft)

Graff (1979/1991, p. 2; card `graff1991literacy`, pending on 1979 pagination): "A literacy myth surrounds us"; literacy
"was not the benefit to individuals that it was promised to be" (p. 321). The ledger's "optional reward vs mandatory
gate" is the paper's distinction, not Graff's (H17; facet L2). The draft now rests "oversold promise" on Dakar and the
GMR alone and cites neither Graff nor Kamperman and Graff (2026), who own the transfer of the myth to AI literacy (card
`kamperman2026ai`, full). Verdict: **holds** as the ledger states it; the draft's omission leaves §3.4's "competence
promised at scale" without the literature that names the pattern.

### R1-29. "Governed twice" and "custody" (ll. 55–61, 285–289)

"Custody of the medium" is the paper's term (ledger facet O); historians speak of regulation, licensing, privilege and
patents (Deazley; Johns; Clegg). As a frame it is clear and the draft defines it by cases. Verdict: **holds** (as the
paper's own analytic term, so long as it is not attributed to the historians).

### R1-30. Limits rows L01, L02, L06

L01 (cases mostly English-speaking, many books known through reviews) is borne out by this run: Blayney, Clegg, Seed,
Eisenstein, Ganz, Astbury, Watson, Merrell, Spencer are known at review, description or record depth. L06 (Clanchy,
Goody, Nussbaum, Willis, Sudore, Graff to be read in library copies) stands; add Saenger pp. x, 83–87, 100 and
Parkes p. 1. L02 (positions, not intent) is respected throughout §2. Verdict: **holds**; the library list grows.

## Verdict table

| ID | Concept / claim | Draft lines | Verdict | Evidence (card + locator) | Fix to the argument |
|---|---|---|---|---|---|
| R1-01 | *Scriptio continua* "for most of antiquity" | 151 | narrower | `dxd/heilmann2020reading` pp. 182–183 (interpuncts; second-century abandonment) | Greek throughout; Latin unspaced only after c. 200 AD |
| R1-02 | Silent reading in antiquity | 152–153 | holds | `dxd/knox1968silent` pp. 434–435 | — |
| R1-03 | Insular word separation moved work to the artifact; "the scribes' correction" | 55–58, 155–164 | contested | `dxd/odonnell2000saenger` ¶4; `dxd/heilmann2020reading` pp. 178, 181 (Vatri); facet K Parkes p. 1 | Keep the learners' cost; state that Saenger's physiological premise is rejected by Vatri and Heilmann; the label is the paper's |
| R1-04 | Saenger quoted and paged (pp. x, 83, 85, 87, 100) | 158–162, 166–167, 175 | unsupported | Search 2: wording found only in the unauthorised upload; `ADJUDICATION.md` §5.2 | No quotation or page from Saenger until a library copy or Google Books in a browser confirms each page |
| R1-05 | Carolingian page's conventions "set from above" | 166–178 | misused | `boretius1883capitularia` pp. 60, 80–81 (correction of texts); N2 (d) "no source ties it to word separation"; Saenger p. 34, 100 via facet A | Custody of the corrected text and of the books read in church; conventions of layout spread from scriptoria |
| R1-06 | Stationers' charter as "an instrument of the Crown's control of what could be read" | 182–189, 313–315, 554 | contested | `arber1875transcript` pp. xxviii–xxxi (terms); `blayney2013stationers` (Smyth: Company's commercial motive vs Crown's regulation); `clegg1997press` (not routine); `johns2002how` p. 119 | Custodian: the trade (holds). Purpose: Arber/Siebert vs Blayney/Clegg/Johns, both named |
| R1-07 | 1577–1586 trade objections; Wolfe; Bourne | 191–198 | holds | `deazley2008commentary1586` §§4–5 | — |
| R1-08 | 1586 and 1637 decrees; 1662 Act | 198–202 | holds | `starchamber1637decree` pp. 9–10, 16; `statutesrealm1819vol5`; `deazley2008commentary1662` §2 | — |
| R1-09 | "Reading itself was licensed"; "statutes that licensed who could read" | 59, 204–216, 225–227 | narrower | `statutesrealm1817vol3` pp. 896–897; N2 claim 5 (four years); `foxe1837acts` p. 245 (1409 licence) | One Act, 1543–47, repealed by the next reign; licensed reading is a manuscript-era practice the Act repeated |
| R1-10 | Cranmer's prologue as professed standard | 209–211 | holds | `cranmer1846miscellaneous` p. 121 (N7a N2-10) | — |
| R1-11 | Rule IV and enforcement | 216–220 | holds | `manuzio1564index` p. 15; `reusch1883index` pp. 333–336 | — |
| R1-12 | Commons' reasons 1695 | 220–224 | holds (narrower) | `commons1803journal` reasons 3, 12; `deazley2008commentary1662` §6 ("little to do with ... liberty of the press") | Trade and monopoly grievances; lapse by expiry after refusal to revive |
| R1-13 | "Courts developed a duty to read"; *Upton* | 231–234, 398 | narrower | `upton1875tribilcock` p. 50; `knapp2015duty` pp. 1083, 1085, 1089–1092, 1108–1110 | A presumption of knowing assent with defences (fraud, misrepresentation, mistake), not an obligation |
| R1-14 | *L'Estrange* "absolute"; "bound the signer to whatever she signed" | 59, 234–237, 530 | narrower | `lestrange1934graucob` pp. 395, 403, 405 ("in the absence of fraud, or ... misrepresentation"; Divisional Court); `foster1869mackinnon` (H10) | Signature binds absent fraud, misrepresentation or *non est factum* |
| R1-15 | *Parker*: "the courts treated it as done" | 237–240 | narrower | `parker1877south` pp. 423–425 (no duty to read an unsigned ticket; onus on the company) | Use *Parker* for the presumed English reader only |
| R1-16a | Requerimiento: Castilian procedure; "broke Castile's own standard" | 242–250, 346–351 | contested | `israeli2022requerimiento` pp. 47–48, 62 and Critical notes (Seed; Muldoon/Pagden); `seed1995ceremonies` | Name Seed's Islamic-summons origin and the canonists' defence; rest A3 on Las Casas and Oviedo as well |
| R1-16b | Addressees "informed after the fact" | 421–423 | wrong | Ledger H18 ("Read aloud in Spanish before an attack"); `israeli2022requerimiento` p. 62 | Notice before the act, in a form the hearer could not understand or answer |
| R1-17 | The gate: Alabama 1901; *Katzenbach*; *Gaston*; "by the era's own lights" | 252–259, 385–387 | narrower | `alabama1901official` pp. 8, 11; `katzenbach1966south` pp. 310, 312, 333–334; `gaston1969gaston` p. 293; `lassiter1959northampton` pp. 51, 53–54 | The courts allowed the qualification (*Lassiter* 1959, unanimous) and condemned purpose, administration and state-made illiteracy |
| R1-18 | Virginia and North Carolina 1831 | 259–262 | holds | `virginia1831acts` p. 107; `northcarolina1831acts` preamble | — |
| R1-19 | Dakar promise; 2015 GMR | 262–266, 431 | holds | `unesco2000dakar` 7(iv); `unesco2015education` p. 135 | — |
| R1-20 | Pragmática of 1503 | 268–270, 537–538 | holds | `spain1805novisima` pp. 144–145; `andrien2012burns` (practice) | Professed standard, not practice |
| R1-21 | Easton 1757: the clerk "demanded by the party himself" | 270–274, 349–350, 384–385, 526 | holds (contested on the clerk) | `pennsylvania1851minutes` pp. 656–657, 664–665; `thomson1759enquiry` pp. 110–112 | Demand Teedyuscung's; motive the secretary's refusal in 1756; clerk a Quaker schoolmaster, Quaker prompting alleged |
| R1-22 | 1883 jurat "refused an affidavit without the officer's certificate" | 274–276, 364–366, 529–530 | narrower | `lely1883judicature` pp. 276–277 ("unless the court or a judge is otherwise satisfied"; margin note) | Certificate required, with a judicial escape; the rule predates 1883 |
| R1-23 | Spain's art. 193 "cabal conocimiento" | 276–278 | narrower | `spain1944reglamento` (amended by RD 45/2007) | The standard quoted dates from 2007 |
| R1-24 | Sudore 28% / 98% | 278–281 | holds | `sudore2006use` abstract, Results | — |
| R1-25 | Grade cards 13.1% | 281–283, 531–532 | holds | `simon2005impact` pp. 32, 35; `jin2003effect` | — |
| R1-26 | Two courses as periods: "scribes' correction" vs "print stage" | title, 15–17, 55–61, 146–147, 285–289, 549–552 | narrower | `foxe1837acts` p. 245; `parkes1992pause` ch. pp. 50–61 (structure); `johns2002how` pp. 119, 121; `ade/johns1998` pp. 10, 36; ledger H11 | Two recurring choices in every period; "print stage" only as England's press regime 1557–1695 |
| R1-27 | Johns–Eisenstein debate | 182–227 (implicit); ledger H12 | contested | `johns2002how`; `ade/eisenstein2002` (second-hand) | Name Eisenstein's thesis and the side taken |
| R1-28 | Graff's literacy myth; require/reward | ledger H13, H16, H17; absent from draft | holds | `graff1991literacy` pp. 2, 19, 321; `kamperman2026ai` | The pattern §3.4 names has an owning literature the draft does not cite |
| R1-29 | "Custody of the medium" | 55–61, 285–289 | holds | ledger facet O; Deazley, Johns, Clegg (regulation, privilege, licensing) | The paper's term, not the historians' |
| R1-30 | Limits L01, L02, L06 | §5 549–552 | holds | this run's blocks | Add Saenger pp. x, 83–87, 100 and Parkes p. 1 to the library list |

Counts: holds 15 (two with a narrowing noted, R1-12 and R1-21) · narrower 9 · misused 1 · contested 4 · unsupported 1 · wrong 1.

## Gaps and blocks

| Item | Why not read | Where a Bentley library user would find it |
|---|---|---|
| Saenger, *Space between Words* (1997), pp. x, 83, 85, 87, 100 | Authorised scan lending-only; archive.org FTS indexes only the unauthorised upload; Google Books CAPTCHA (N2); De Gruyter empty page | Print (Stanford UP 1997) or the De Gruyter e-book (doi:10.1515/9781503619081) via library login; Google Books id `w3vZaFoaa3EC` in a browser. Also Saenger's 1991 chapter in Olson and Torrance, *Literacy and Orality* (CUP), for the "elitist literate mentality" sentence |
| Parkes, *Pause and Effect* (1992), p. 1 and pp. 50–61 | Lending-only; the p. 1 sentence known from a snippet (facet K) | Print or the Routledge 2016 reprint (doi:10.4324/9781315247243) |
| Blayney, *The Stationers' Company and the Printers of London* (2013), vol. 2, chs. 10–11 | Cambridge Core login | Cambridge Core (doi:10.1017/cbo9781139542715) or print; Helen Smith's TLS review (19 Dec. 2014) via library TLS access |
| Clegg, *Press Censorship in Elizabethan England* (1997), chs. 1–2 | Cambridge Core login | Cambridge Core (doi:10.1017/cbo9780511585241) or print |
| Eisenstein, "An Unacknowledged Revolution Revisited", AHR 107(1) (2002) 87–105 | OUP paywall (N2) | JSTOR or Oxford Academic via library |
| Watson, "Censorship and Cultural Change in Late-Medieval England", Speculum 70(4) (1995) 822–864 | JSTOR; not OA | JSTOR via library (doi:10.2307/2865345); for the Latin text, Wilkins, *Concilia*, iii |
| Ganz, "The Preconditions for Caroline Minuscule", Viator 18 (1987) 23–44 | Brepols; not OA | Brepols online via library (doi:10.1484/j.viator.2.301384); with McKitterick 1989 chs. 4, 6 (N2 gaps) |
| Astbury, "The Renewal of the Licensing Act in 1693 and its Lapse in 1695", The Library s5-33(4) (1978) 296–322 | OUP paywall | Oxford Academic via library (doi:10.1093/library/s5-xxxiii.4.296) |
| Spencer, "Signature, Consent, and the Rule in *L'Estrange v Graucob*", CLJ 32(1) (1973) 104–122 | Cambridge Core | Cambridge Core via library (doi:10.1017/s0008197300090255); Macaulay, 19 Vand. L. Rev. 1051 (1966), HeinOnline |
| *Tilden Rent-A-Car Co. v. Clendenning* (1978) 18 O.R. (2d) 601 (Ont. C.A.) | CanLII returned 403 | CanLII in a browser; Westlaw Canada |
| Merrell, "'I desire all that I have said ... may be taken down aright'", WMQ 63(4) (2006) 777–826 | JSTOR; no Crossref record | JSTOR via library; with Merrell, *Into the American Woods* (1999), print (N3 gap) |
| Seed, *Ceremonies of Possession* (1995), ch. 3; Muldoon (1980); Faudree (2015); Hanke, "The Requerimiento and Its Interpreters", Revista de Historia de América 1 (1938) 25–34 | Closed (N3 gaps); Hanke not in Crossref | Print / JSTOR via library |
| Arber, *Transcript*, vols. II and IV | Lending-only (N2) | Library copy or HathiTrust in a browser |
| Knapp 2015, journal copy | Read from a law-firm repost of the typeset PDF; the UC Law SF repository search gave no parsable result | `repository.uclawsf.edu/hastings_law_journal/vol66/iss4/` in a browser, to confirm the copy |
