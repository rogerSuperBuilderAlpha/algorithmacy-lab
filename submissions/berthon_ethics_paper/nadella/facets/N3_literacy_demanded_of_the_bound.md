# N3 — Literacy demanded of the bound: where the institutions put the reading, the record and the competence

*Facet N3, round 1, 2026-10-24. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

**What this facet covers.** The third moment of the outline's record section, "Literacy demanded of the bound": the
duty to read (L'Estrange, Upton, Hill, Parker), the jurat for deponents who cannot read, the record over the voice,
the Requerimiento, the anti-literacy acts, the oversold promise (Jomtien, Dakar, the 2015 GMR, Graff), deficit
construction (Frahm et al.), capacity from below and sponsored scaffolds, and the counter-visions the paper offers as
corrections (the Pragmática of 1503, Spain's notarial rules, second interpreters and the bound party's own clerk,
probate r. 13, Jones v. Meehan, read-aloud and teach-back). I sought refutation as hard as support: disclosure
regimes with a measured protective effect, read-aloud that works, notaries who served the stronger party, the
Requerimiento judged by its own standard, and literacy campaigns that kept their promise.

**The question the synthesis answers.** Where did the medium's institutions put the reading, the record and the
competence, and which corrections checked understanding or moved risk? Short answer, argued in (c): the failures put
all three on the person bound, and the corrections that the record holds mostly moved the reading or the record to
an officer or a second party owed to the weaker side. Few of them checked understanding; the ones that did (the 1883
jurat, teach-back, Spain's art. 193) checked by impression or conversation, not by a test the person controls.

**Premises and outline sections served.** A2 and A3 (the failures: record kept by one side; disclosure in place of
understanding; the burden of reading on the person bound; competence withheld then oversold), B1 (the corrections
share a property), outline record moment 3, and the precedents for duties D04 (the person's own record), D06 (check
understanding), D07 (change the medium at the point of use) and D08 (scaffold).

**Legend for read status.** *Read in full* = I opened the whole text (or the whole operative act or opinion) this
session. *Read in part* = I opened the text and read the pages named. *Abstract only* = a database abstract or
record and nothing else. *Not accessible* = I could not open the text; the entry says why. *Carded, not reread* =
an existing card in `literature/cards/`, cited for context only.

**Count by read status (33 sources).** Read in full 12 (Parker, Hill, Jones, Israeli, Virginia 1831, North Carolina
1830-31, Frahm et al., the UIS release list, Nishimura et al., Tam et al., Simon et al., and Crider's review of
Seed); read in part 8 (Lely and Foulkes, Andrews, the Pennsylvania minutes, the Novísima Recopilación, Jomtien, the
2015 GMR, Alvord 1868, Kempf); abstract only 6 (Muldoon, Faudree, Tamariz et al., Flory and Emanuel, Ha Dinh et al.,
Jin and Leslie); not accessible 7 (Seed's book, Palacios Rubios, Graff 1979, Burns 2005, Fleming 2016, Merrell 1999,
any Korea source). Items in (e) that I did not search for are not counted. Existing cards cited without rereading are
listed at the end of (b) and are not counted.

---

## (a) Search log

All requests ran on 2026-10-24 with curl and a plain user-agent. No email address was sent to any service; Unpaywall
was not used; no bot wall, captcha or paywall was bypassed. Downloads are in
`~/iit-playground/berthon_ethics_local/pdfs/nadella/N3/<subdirectory>/`.

| # | Source | Exact query or URL | Hits | Notes |
|---|---|---|---|---|
| 1 | Repo reads | `facets/BRIEF.md`; `ARGUMENT_AND_OUTLINE.md`; `RESEARCH_PLAN.md`; `README.md`; `COVERAGE_PREMISES.md`; `sources/bec_facet_V2`, `V4`, `V5`, `dxf_facet_L` (greps and read sections); ledger rows H04, H07, H10, H13, H18, H19, H22-H25, N07; `CARD_INDEX.md` grep for every scope item | n/a | Fixed which cards to upgrade: hill1997gateway, virginia1831acts, northcarolina1831acts (writer-grounded); israeli2022requerimiento, jones1899meehan, wcefa1990world (partial). |
| 2 | Crossref | `api.crossref.org/works/10.1177/0162243921999100` | 1 | Frahm et al., STHV 47(1) 174-216; issued online 15 Mar 2021. |
| 3 | Local PDF | `nadella/N3/frahm2021.pdf` (copied to `frahm2022/`) | 43 pp. | pdftotext; read pp. 174-205. |
| 4 | Local copy | `pdfs/V2/israeli2022.pdf` and `.txt` | 26 pp. | Read pp. 37-62 in full this time. |
| 5 | Local copy | `pdfs/V3/cap_jones_meehan.txt` | 175 U.S. 1-32 | Read pp. 12-32, which the old card had not. |
| 6 | archive.org advancedsearch | `identifier:law-reports-common-pleas*` | 15 | `law-reports-common-pleas_1876-1877_2` = 2 C.P.D.; Parker at pp. 416-430. |
| 7 | archive.org | `.../law-reports-common-pleas_1876-1877_2/page/n450.jpg`, `n454.jpg` (pp. 423, 427) | 2 images | Page check for Parker; leaf map from `/metadata/<id>/page_numbers`. |
| 8 | archive.org advancedsearch | `title:(rules of the supreme court) AND year:[1883 TO 1900]` | 51 | `judicatureacts180000jmle` (Lely and Foulkes 1883), `supremecourtjud00stongoog` (Andrews 1885). |
| 9 | archive.org | page images n363 (Lely p. 276), n395 (Andrews p. 331) | 2 | Confirmed Ord. XXXVIII r. 13 and the Re Longstaff note. |
| 10 | openjurist.org | `openjurist.org/105/f3d/1147` | 403 | Cloudflare challenge; stopped. |
| 11 | Caselaw Access Project | `static.case.law/f3d/105/CasesMetadata.json`; `.../html/1147-01.html`; `static.case.law/us/522/CasesMetadata.json`; `.../html/0808-06.html` | 200 | Hill with star pages *1148-*1151; cert. denied 522 U.S. 808 (6 Oct 1997). |
| 12 | archive.org advancedsearch | `title:(acts passed at a general assembly of the commonwealth of virginia) AND year:[1830 TO 1832]`; variants; NC equivalents | 0 | Session laws not on archive.org under these titles. |
| 13 | Google Books API | `volumes?q=acts passed general assembly commonwealth virginia 1831` | 429 | "Queries per day" quota 0; not retried. |
| 14 | HathiTrust | `catalog.hathitrust.org/Search/Home?lookfor=...` | 403 | Not retried. |
| 15 | Encyclopedia Virginia | the 1831 act's page; its "ORIGINAL IMAGES" `wp-content/uploads/2020/11/11750_...jpg`, `11751_...jpg` | 200 | 600-dpi page images of pp. 107-108 (HathiTrust uc1.a0001803188 stamp). |
| 16 | NC ANCHOR → NC Digital Collections | ANCHOR page; `digital.ncdcr.gov/Documents/Detail/acts-passed-...-1830-1831/1955764?item=2080405`; image via the viewer's own thumbnail URL | 200 | Printed ch. VI with OCR; IIIF manifest URL returned "Page Not Available". Page number illegible. |
| 17 | archive.org advancedsearch | `title:(novisima recopilacion)` | 26 | `BRes002064` (t. V, 1805); OCR grep for "1503"; tít. XXIII at pp. 144-145; images n148-n150. |
| 18 | archive.org advancedsearch | `title:(minutes of the provincial council of pennsylvania) OR title:(colonial records of pennsylvania)` | 70 | `minutesprovinci00coungoog` (vol. VII, 1851). Index "Indians require a Clerk, 656"; images of pp. 656, 657, 664, 665, 689, 690. |
| 19 | archive.org advancedsearch | `creator:(Alvord) AND title:(report schools freedmen)`; `title:(semi-annual report on schools for freedmen)` | 2; 5 | First report (Jan. 1866) not found; fifth report (Jan. 1868) read; search-inside used to locate pages; images n10, n15, n17. |
| 20 | archive.org search-inside | `literacymythlite0000graf`, queries for Graff pp. 19, 301-302, 321 | "Item not available" | Lending-restricted; Graff stays writer-grounded. |
| 21 | Wayback availability | `archive.org/wayback/available?url=unesdoc.unesco.org/images/0023/002322/232205e.pdf` (default and `&timestamp=2016`) | 2026 capture (HTML shell); 2017 capture (PDF) | GMR 2015 full report, 516 pp.; read ch. 4. |
| 22 | UIS API | `api.uis.unesco.org/api/public/versions` | 200 | Latest data still "February 2026 Data Release" (versions to 7 May 2026); `uis2026adult` is current. |
| 23 | OpenAlex | `works/doi:` for 10.1001/jama.292.13.1593, 10.1186/1472-6939-14-28, 10.1086/531318, 10.1080/10609164.2016.1150029, 10.11124/jbisrir-2016-2296, 10.2307/981289, 10.1162/003355303321675428 | 7 | OA status and abstracts; one DOI I guessed for Jin and Leslie was wrong and I found the right one by title search. |
| 24 | OpenAlex search | `effect of information on product quality restaurant hygiene grade cards`; `How to Say Things with Wars requerimiento`; `John Wyclif rights of infidels requerimiento re-examined`; `Ceremonies of Possession Europe conquest New World Seed`; `Korea literacy campaign 1945 adult illiteracy eradication`; `Cuban literacy campaign 1961 evaluation` | 5 each | Leads: Simon 2005 (DRUM), Crider review of Seed (H-Net), Kempf 2014. Nothing on Korea. |
| 25 | OpenAlex search | `illiteracy eradication South Korea 1950s literacy campaign Hangul adult education`; `Korea adult literacy rate 1945 1958 illiteracy`; `literacy campaigns that succeeded historical review mass literacy`; `Flory Emanuel informed consent understanding systematic review 2004` | 7-8 each | No usable Korea source; found Tam 2015 and Tamariz 2013. |
| 26 | OpenAlex search | `escribanos notaries indigenous colonial fraud abuse`; `notaries colonial Spanish America power writing indigenous litigants`; `second interpreter treaty council Merrell Teedyuscung`; `Into the Archive Writing and Power in Colonial Peru Burns review` | 5-10 each | Fleming 2016 (Gettysburg) found; Burns reviews all closed. |
| 27 | BMC | `bmcmedethics.biomedcentral.com/counter/pdf/10.1186/1472-6939-14-28` | Client challenge | Stopped; used Europe PMC XML (row 28). |
| 28 | Europe PMC REST | `search?query=DOI:...`; `PMC3733934/fullTextXML`; `PMC4371493/fullTextXML`; `PMC3539038/fullTextXML` | 200, 200, 500 | Nishimura and Tam full text; Tamariz not open. Abstracts for Flory, Tamariz, Ha Dinh. |
| 29 | Springer | `link.springer.com/content/pdf/10.1007/s11606-012-2133-2.pdf` | Client challenge | Tamariz at abstract depth. |
| 30 | SSRN | `doi.org/10.2139/ssrn.322883` (Jin and Leslie) | 403 | Abstract depth. |
| 31 | DRUM (UMD) | `hdl.handle.net/1903/6641` → bitstream | 200 | Simon et al. 2005, 5 pp. |
| 32 | H-Net | `h-net.org/reviews/showpdf.php?id=649` | 200 | Crider's review of Seed 1995. |
| 33 | UBC Critical Education | `ices.library.ubc.ca/.../download/183269/184389` | 200 | Kempf 2014, 20 pp. |
| 34 | Gettysburg Cupola | `cupola.gettysburg.edu/ghj/vol15/iss1/4` (200); PDF `cgi/viewcontent.cgi?article=1151&context=ghj` | "Just a moment..." | Cloudflare challenge on the PDF; stopped. |
| 35 | archive.org advancedsearch | `title:(Into the American Woods) AND creator:(Merrell)`; `title:(De las islas del mar oceano)` | 2; 45 | Merrell: lending-only scans; Palacios Rubios 1954 edition not among the 45. |

Consensus and Scholar Gateway were not used: the scope items are mostly primary legal and historical texts, and
OpenAlex plus Europe PMC covered the empirical searches.

---

## (b) Entries

### Q1. The duty to read and the burden of reading

**Parker v. South Eastern Railway Co. (1877) 2 C.P.D. 416 (C.A.).** Key `parker1877south`; card
`literature/cards/berthon_ethics_paper/parker1877south.md`. Exists: archive.org Law Reports item with page map;
pages 423 and 427 checked on the images. **Read in full** (pp. 416-430). The Court of Appeal ordered new trials for
two cloak-room depositors whose tickets limited liability on the back. Mellish L.J. held there was no duty to read
an unsigned ticket; the question was whether the company "did what was reasonably sufficient to give the plaintiff
notice of the condition" (p. 424). In framing it he let the company "assume that he can read, and that he
understands the English language" (p. 423), and denied the particular depositor any allowance for "his exceptional
ignorance or stupidity or carelessness" (p. 423); a shipper ignorant of bills of lading "must bear the consequences
of his own exceptional ignorance" (p. 422). Bramwell L.J.: "The putting of it into their hands was equivalent to
saying, “Read that.”" (p. 427). Baggallay L.J. put "the onus of proof ... upon the company" (p. 425).
**Bearing:** complicates A2 (H19). Parker refuses a duty to read and puts notice on the issuer, but defines notice by
a presumed English reader, which keeps the burden on the person who cannot read.

**Hill v. Gateway 2000, Inc., 105 F.3d 1147 (7th Cir. 1997), cert. denied, 522 U.S. 808.** Key `hill1997gateway`;
upgrade card `literature/cards/berthon_ethics_paper/hill1997gateway.md`. Exists: CAP volume metadata and the 522 U.S.
order entry. **Read in full** with star pages. Pin cites now fixed: "A contract need not be read to be effective"
(at 1148); "Cashiers cannot be expected to read legal documents to customers" and "Competent adults are bound by such
documents, read or unread" (at 1149). The court prefers writing because "oral recitation would not avoid customers’
assertions (whether true or feigned) that the clerk did not read term X to them, or that they did not remember or
understand it" (at 1149). **Bearing:** supports A2 (H19, H07).

### Q2. The jurat and certified reading for those who cannot read

**Rules of the Supreme Court 1883, Ord. XXXVIII r. 13, in Lely and Foulkes (4th edn, 1883).** Key
`lely1883judicature`; card `literature/cards/berthon_ethics_paper/lely1883judicature.md`. Exists: archive.org item,
title page "Fourth Edition ... Henry Sweet ... 1883". **Read in part** (pp. 276-277; image of p. 276 checked). The
officer "shall certify in the jurat that the affidavit was read in his presence to the deponent, that the deponent
seemed perfectly to understand it, and that the deponent made his signature in the presence of the officer"; without
the certificate the affidavit is unusable unless the court is satisfied it "appeared to be perfectly understood by
the deponent" (pp. 276-277). Margin: "Extended to blind persons in 1883". **Bearing:** supports B1 in part (the
reading and an impression of understanding are certified by an officer, not the party); narrows A2/H22 (more than
disclosure, less than a test).

**Andrews, *The Supreme Court of Judicature Acts ... with Rules of Court and Forms issued up to 1885* (1885).** Key
`andrews1885supreme` (bib only; noted on the Lely card). **Read in part** (p. 331, image checked). Same rule; case
note: "The statement of a managing clerk that he had read over and explained the affidavit to an illiterate witness
was held insufficient to satisfy the Judge, and the affidavit was therefore directed to be taken off the file (Re
Longstaff, W. N. 1884, 216)". **Bearing:** supports B1: the reader must not be the interested party's agent.

### Q3. The record over the voice, and the bound party's own record

**Minutes of the Provincial Council of Pennsylvania, vol. VII (1851): Easton treaty, July-August 1757.** Key
`pennsylvania1851minutes`; card `literature/cards/berthon_ethics_paper/pennsylvania1851minutes.md`. Exists:
archive.org item with page map; six page images checked. **Read in part** (pp. 656-665, 689-690). Teedyuscung, who
could not read, "demanded that he might have a Clerk, to be appointed by himself, to take down the Minutes of the
Treaty, who should compare his Proceedings with the other Clerks before they leave the Table", which he called "the
most certain means to searching out the Truth" (p. 656). Four provincial commissioners backed him because "he and his
People are illiterate Persons" (p. 657). The Governor: "No Indian Chief, before you, ever demanded to have a Clerk"
(p. 664), then yielded; Charles Thomson sat beside the official clerk "and began to take Minutes, without asking
Permission of the Governor" (p. 665). On 1 August the Delawares' own text was read back "three or four Times" before
they approved it (p. 689). **Bearing:** supports B1 and A3 strongly; a direct precedent for D04.

**Jones v. Meehan, 175 U.S. 1 (1899).** Key `jones1899meehan`; upgrade card
`literature/cards/berthon_ethics_paper/jones1899meehan.md`. **Read in full** (pp. 1-32). Beyond the canon (pp. 10-11),
the Court found it "unnecessary to consider the competency of the extrinsic evidence ... of what took place between
the representatives of the parties at the negotiations" (pp. 23-24), so it construed text rather than checking
understanding. The negotiation journal it reports shows Moose Dung "weighing and deliberating on every separate
provision" (p. 5). It discounted an affidavit signed by mark as "mere matter of form" to the signer (p. 31). The
canon's practical winners were the white lessees whose $25 lease beat a later $200 lease (pp. 6-8, 32).
**Bearing:** narrows B1 (moves risk; does not check understanding); complicates A2/H07.

### Q4. The Requerimiento

**Israeli, "The Requerimiento in the Old World" (2022).** Key `israeli2022requerimiento`; upgrade card
`literature/cards/berthon_ethics_paper/israeli2022requerimiento.md`. Exists: Crossref matched (LHR 40(1) 37-62).
**Read in full** (pp. 37-62). In Castile the addressee answered, "the notary was obliged to document the addressee’s
response" (p. 47), addressees took time and counsel, and in 1417 each side brought a notary (p. 48). The colonial
form lost the shared community (p. 61); orders to translate were probably not followed, and "the ultimate function of
record making was self-legitimation" (p. 62). **Bearing:** supports A2 and A3 (H18: the colonial use broke Castile's
own standard); B1 narrower (the Castilian checks gave a hearing and a second record, not a check of understanding).

**Seed, *Ceremonies of Possession* (1995), ch. 3.** Key `seed1995ceremonies`; secondary card
`literature/cards/berthon_ethics_paper/seed1995ceremonies.md`. **Not accessible** (book; no open copy). Crider's
H-LatAm review (1996) **read in full**. Paraphrase: Seed reads the Requerimiento as a read-aloud, usually
untranslated protocol rooted in the Islamic summons, and contrasts French ceremonies that attended to native
responses. **Bearing:** supports A2/A3 at review depth only; not to be quoted.

**Muldoon, "John Wyclif and the Rights of the Infidels: The Requerimiento Re-Examined", *The Americas* 36(3) (1980)
301-316, doi 10.2307/981289.** Key `muldoon1980john` (bib only). Crossref matched. **Abstract only** (OpenAlex).
Muldoon argues that the text sits in the canonistic debate on infidel dominium and is not a "useless legalism". This
is the strongest "defender by its own standard" I found: by canon-law reasoning the Requerimiento was coherent.
**Bearing:** complicates A3 (judged by its jurists' standard the form was defensible; Israeli's Castilian standard
and Las Casas's objection still break it).

**Faudree, "Reading the Requerimiento Performatively", *Colonial Latin American Review* 24(4) (2015) 456-478, doi
10.1080/10609164.2016.1150029.** Key `faudree2015reading` (bib only). Crossref matched. **Abstract only** (OpenAlex
gives only the opening of the article, quoting Oviedo on Palacios Rubios). Israeli (2022, pp. 38, 46-47) reports her
argument that critics denied the conditions for the speech act: hearers could not understand and could not answer.
**Bearing:** supports A2/A3 through Israeli.

**Palacios Rubios, *De las islas del mar Océano* (with Zavala's introduction, 1954).** Key
`palaciosrubios1954islas` (bib only). **Not accessible**; not found on archive.org (search 35). His view survives in
Oviedo's carded report (he said the conscience was satisfied "si se hiçiesse como el requirimiento lo diçe").

### Q5. Anti-literacy acts (H04)

**Virginia, Acts 1830-31, ch. XXXIX (7 April 1831).** Key `virginia1831acts`; upgrade card
`literature/cards/berthon_ethics_paper/virginia1831acts.md`. **Read in full** on the printed page images (pp.
107-108). The print matches the transcription: s. 4 makes meetings of free Black people "for teaching them reading
or writing" unlawful assemblies (p. 107); s. 6 fines white people who teach slaves "for pay or compensation" (p.
108). **Bearing:** supports A2 (H04), narrower than a general ban.

**North Carolina, Acts 1830-31, ch. VI.** Key `northcarolina1831acts`; upgrade card
`literature/cards/berthon_ethics_paper/northcarolina1831acts.md`. **Read in full** on the page image. The printed act
**corrects ANCHOR's transcription**: s. I also punishes anyone who "shall give or sell to such slave or slaves any
books or pamphlets", and a free person of colour "shall be fined, imprisoned, or whipped, at the discretion of the
court" (ANCHOR gives whipping only and omits the books clause). The preamble gives the ground: teaching slaves "has a
tendency to excite dissatisfaction in their minds and to produce insurrection and rebellion". **Bearing:** supports
A2 (H04); the preamble is the legislature's own statement that reading would serve the people denied it.

### Q6. The oversold promise and deficit construction (H13)

**World Declaration on Education for All and Framework for Action (Jomtien, 1990).** Key `wcefa1990world`; upgrade
card `literature/cards/berthon_ethics_paper/wcefa1990world.md`. **Read in part** (Declaration whole; Framework paras
1-42). The Declaration promises basic education "for the first time in history — an attainable goal" (Preamble), and
meeting basic learning needs "confers upon them a responsibility" (Art. 1.2). The literacy target is optional:
countries "may wish to set their own targets" including halving adult illiteracy, "say, one-half its 1990 level by the
year 2000" (Framework para. 8). Learners are "a vital human resource that needs to be mobilized" who must see that
benefits "exceed the costs the participants must bear" (para. 31). **Bearing:** supports A2 (oversold; deficit framed
in the learner); narrows A3 (Jomtien's numeric target was not a pledge).

**EFA Global Monitoring Report 2015, full report, ch. 4.** Key `unesco2015education`; card
`literature/cards/berthon_ethics_paper/unesco2015education.md`. **Read in part** (pp. 135-147). "The rate of
illiteracy is likely to have dropped slightly from 18% in 2000 to 14% in 2015, which means that the Dakar target of
halving illiteracy has not been achieved" (p. 135). Cohort analysis of 30 countries: gains came from younger, better
schooled cohorts, "not due to the implementation of effective literacy programmes" (p. 135); "considerable doubt is
cast on the impact of efforts to improve the literacy skills of adult populations since 2000" (p. 144). The language
of campaigns "often portrays illiteracy as a ‘social illness’ which can be ‘eradicated’", which can "stigmatize
illiteracy ... particularly if political leaders declare the country to be ‘illiteracy-free’" (p. 147); Yo Sí Puedo
has had "no independent evaluations" (p. 147). National agencies that monitor and reduce illiteracy at once face
"pressure to show progress or to restrict access to data by independent assessors" (p. 143). **Bearing:** supports A2
and A3 strongly.

**Frahm, Doezema and Pfotenhauer, "Fixing Technology with Society" (2022).** Key `frahm2022fixing`; card
`literature/cards/berthon_ethics_paper/frahm2022fixing.md`. Exists: Crossref matched. **Read in full** (pp.
174-205). A "deficit logic ... frames a lack of societal engagement in innovation governance as a major barrier to
the uptake and dissemination of new technologies", which lets institutions "present “Responsible Innovation”
frameworks as the solution" (p. 175) and "locates both the power to correctly diagnose problems and enact solutions
within international organizations" (p. 203). **Bearing:** supplies the mechanism for A2's "oversold" (an institution
names what the public lacks so its framework is the fix); the transfer to literacy is the facet's.

**UIS data release check.** Key `uis2026adult` (reused). **Read in full** (the API's version list). The latest release
is still February 2026; the existing card is current. **Bearing:** none new.

**Graff, *The Literacy Myth* (1979).** Key `graff1991literacy` (reused). **Not accessible** for upgrade: archive.org's
1979 scan is lending-restricted and search-inside returned "Item not available". The card stays writer-grounded.

### Q7. Capacity from below and sponsored scaffolds (H25); literacy campaigns that kept their promise

**Alvord, *Fifth Semi-Annual Report on Schools for Freedmen* (1 January 1868).** Key `alvord1868fifth`; card
`literature/cards/berthon_ethics_paper/alvord1868fifth.md`. **Read in part** (pp. 1-14; images of pp. 7, 12, 14).
"Of the whole number of schools 1,000 are sustained wholly or in part by the freedmen, and they own 364 of the
buildings used for school purposes"; 3,544 of 6,492 teachers were Black (p. 14). Quoting his 1866 report, a Louisiana
petition carried "the names and marks (X) of such a long list of parents, ignorant themselves, but begging that their
children might be educated; promising that ... they would pay for it" (p. 7). **Bearing:** supports H25 (capacity
from below).

**Kempf, "The Cuban Literacy Campaign at 50" (2014).** Key `kempf2014cuban`; card
`literature/cards/berthon_ethics_paper/kempf2014cuban.md`. Exists: DOI resolves at doi.org (no Crossref record).
**Read in part** (pp. 1-8). The campaign "reduced the illiteracy rate from almost 24% to 3.9%" (p. 3, citing Huberman
and Sweezy 1969), was followed by "battles" to the ninth grade (1980-1985), and carried 26 political themes (pp. 4,
7). **Bearing:** refutes "competence oversold and unmet" as a general rule (on declared figures); supports "scaffolds
served their sponsors".

**Korea (post-1945 literacy).** **Not accessible**: two OpenAlex searches (rows 24-25) found nothing usable. Gap.

### Q8. Counter-visions: the notary, the Pragmática, and checking understanding

**Novísima Recopilación (1805), lib. X, tít. XXIII, leyes I-V (Pragmática of Alcalá, 7 June 1503).** Key
`spain1805novisima`; card `literature/cards/berthon_ethics_paper/spain1805novisima.md`. **Read in part** (pp.
144-145, images). Notaries must read the note "presentes las partes y los testigos", and if a party cannot sign, a
witness signs and the notary records it (p. 144); the party gets its signed copy within three days (ley III), copies
are collated "en presencia de las partes" (ley IV), and either party may have the instrument "aunque la otra parte no
la pida" (ley V, p. 145). **Bearing:** supports B1's "work moved to a party owed to both sides" and D04 (the party's
own copy); **does not** support "checked understanding".

**Nishimura et al., "Improving understanding in the research informed consent process" (2013).** Key
`nishimura2013improving`; card `literature/cards/berthon_ethics_paper/nishimura2013improving.md`. Crossref matched.
**Read in full** (Europe PMC XML). Enhanced forms and extended discussion raised understanding; multimedia did not
reach significance; "No category of intervention managed to have consistent efficacy"; "there is still no substitute
for a good conversation". A read-aloud trial (Ford et al. 2008) moved understanding from 48% to 52% (p = 0.012). The
abstract and the results disagree on two pooled SMDs (extended discussion 0.53 vs 1.03; multimedia 0.30 vs 0.32).
**Bearing:** supports A2 and D06; the read-aloud evidence narrows the thesis only slightly.

**Tam et al., "Participants' understanding of informed consent in clinical trials over three decades" (2015).** Key
`tam2015participants`; card `literature/cards/berthon_ethics_paper/tam2015participants.md`. Crossref matched. **Read
in full**. Pooled understanding 52.1% (randomization) to 75.8% (freedom to withdraw); understanding "had not
increased over 30 years"; low literacy predicts poorer understanding of randomization. **Bearing:** supports A2 and
A3.

**Tamariz et al., "Improving the informed consent process for research subjects with low literacy" (2013).** Key
`tamariz2013improving`; abstract card. Crossref matched. **Abstract only** (Springer challenge; no open PMC text).
Teach-back or teach-to-goal gave the highest comprehension; simplified forms the lowest; six studies, one randomized.
**Bearing:** supports D06 and B1 at abstract depth.

**Flory and Emanuel, "Interventions to improve research participants' understanding in informed consent for
research" (2004), *JAMA* 292(13) 1593-1601.** Key `flory2004interventions` (bib only). Crossref matched. **Abstract
only** (Europe PMC). One-to-one time with a study member or neutral educator was "the most effective available way";
multimedia and enhanced forms had "only limited success"; lower education predicted less understanding. **Bearing:**
supports A2/D06.

**Ha Dinh et al., "The effectiveness of the teach-back method ... for people with chronic disease" (2016), *JBI
Database* 14(1) 210-247.** Key `hadinh2016effectiveness` (bib only). Crossref matched. **Abstract only**. Twelve
studies; teach-back improved disease knowledge, adherence and self-efficacy, with inconsistent effects on readmission.
**Bearing:** supports D06 (checking understanding works outside consent too).

### Q9. Refutation: disclosure regimes with a measured protective effect

**Simon et al., "Impact of Restaurant Hygiene Grade Cards on Foodborne-Disease Hospitalizations in Los Angeles
County" (2005).** Key `simon2005impact`; card `literature/cards/berthon_ethics_paper/simon2005impact.md`. Exists:
Europe PMC record (PMID 15794461; no DOI). **Read in full**. Posting letter grades "within 5 feet of the point of
entry" was "associated with a 13.1 percent decrease (p < .01)" in foodborne-disease hospitalizations, sustained to
2000 (p. 32); confounds include a television exposé and more inspections (p. 35). **Bearing:** refutes the strong form
of "disclosure does not protect"; sharpens B1, because the reading is done by an inspector and the diner reads one
letter.

**Jin and Leslie, "The Effect of Information on Product Quality" (2003), *QJE* 118(2) 409-451.** Key `jin2003effect`;
abstract card. Crossref matched. **Abstract only** (SSRN 403). Same natural experiment; restaurants improved hygiene.
**Bearing:** as Simon.

### Q10. Notaries serving the stronger party

**Burns, "Notaries, Truth, and Consequences", *American Historical Review* 110(2) (2005) 350-379, doi 10.1086/531318.**
Key `burns2005notaries` (bib only). Crossref matched. **Not accessible** (closed; OpenAlex has no abstract). The
carded Andrien review of Burns's 2010 book remains the only read source on notaries in Cuzco serving the powerful.
Israeli (2022, pp. 46-47) adds one more: Castilian notaries who refused to record or hand over testimonios "because
the addressee was a powerful or fearful individual" or from partisanship. **Bearing:** complicates B1: the notary's
professed duty to both sides was not self-enforcing.

**Fleming, "'Where We May Oftener Converse Together': Translation of Written and Spoken Communication in Colonial
Pennsylvania", *Gettysburg Historical Journal* 15(1) (2016), article 4.** Key `fleming2016where` (bib only). **Not
accessible** (Cloudflare challenge on the PDF; landing-page metadata only).

**Merrell, *Into the American Woods* (1999).** Key `merrell1999into` (bib only). **Not accessible** (archive.org
lending-only). The Easton minutes (Q3) carry the point Merrell is cited for.

**Existing cards cited, not reread:** `lestrange1934graucob`, `upton1875tribilcock`, `washington2004bailey`,
`morales2008sun`, `specht2002netscape`, `moj1998practice32`, `messick1993calligraphic`, `marshall1999`,
`badger1996`, `delgamuukw1997`, `lascasas1876historia`, `oviedo1853historia`, `helps1855spanish`, `douglass1845narrative`,
`margo2005williams`, `unesco2000dakar`, `unesco2015efa`, `uis2026adult`, `graff1991literacy`, `giesler2014creating`,
`kamperman2026ai`, `street2003whats`, `bhola1984campaigning`, `alvord1866report`, `roberts1835memoirs`,
`hagedorn1988friend`, `andrien2012burns`, `almeida2019firmo`, `marchant2015expedicion`, `uinl2005ethics`,
`uinl2005function`, `spain1944reglamento`, `spain1862ley`, `uk1987noncontentious`, `sudore2006use` (all
`berthon_ethics_course/`).

---

## (c) Synthesis by question

### Where did the institutions put the reading?
On the person bound, and on a presumed reader. L'Estrange and Upton bind the signer regardless (carded); Hill binds
"read or unread" and rejects reading aloud as costly and useless (at 1149). Parker is the instructive middle case:
Mellish L.J. denies a duty to read an unsigned ticket and makes the issuer prove notice, yet measures notice against
a reader of English and refuses allowance for "exceptional ignorance" (pp. 422-423). The burden thus moves off the
diligent reader and stays on the person who cannot read. Where the bound party could not read at all, the law
supplied a reader: the 1503 notary reads before parties and witnesses (Nov. Rec. X.23.1), the 1883 officer reads and
certifies (Ord. XXXVIII r. 13), the probate registrar satisfies himself (carded r. 13). The colonial Requerimiento
kept the reading and dropped the hearer: no translation in practice, no answer, no court (Israeli, pp. 61-62).

### Where did they put the record?
With the stronger side, and the record was the legal product. Israeli shows the colonial testimonio served
"self-legitimation" (p. 62); the Easton Governor called a second record "unprecedented and against my Judgement"
(p. 664); Hill prefers the drafter's writing because recitation leaves disputes about what was said (at 1149). The
corrections split the record: the 1503 Pragmática gives each party its copy (leyes III, V); Castilian addressees
had their answers recorded and could bring their own notary (Israeli, pp. 47-48); Teedyuscung put his own clerk at
the table and had his text read back "three or four Times" (pp. 665, 689).

### Where did they put the competence?
They withheld it by statute (Virginia ss. 4-6; North Carolina ch. VI, now with the books clause), then promised it at
scale and blamed the learner when it did not arrive. Jomtien declared education for all attainable and made its
beneficiaries responsible (Art. 1.2, para. 31); the 2015 GMR found the Dakar target missed and adult programmes
largely without measurable effect (pp. 135, 143-144), named the "eradication" language and declared
"illiteracy-free" status as harmful (p. 147), and admitted that the agencies grading literacy have a conflict of
interest (p. 143). Frahm et al. give the mechanism a name: deficit construction. Against this, competence was built
from below (Alvord: 1,000 schools sustained by freedpeople, p. 14) and, in Cuba, by a sponsor who kept its declared
promise and pressed on to the ninth grade (Kempf, pp. 3, 7).

### Which corrections checked understanding, and which moved risk?
Few checked understanding. The 1883 jurat certifies an impression ("seemed perfectly to understand"), done by an
officer and not by the party's clerk (Re Longstaff). Spain's art. 193 (carded) and teach-back (Tamariz, Ha Dinh,
Sudore carded) check by conversation. The read-aloud trial in Nishimura's review moved understanding four points.
Most corrections instead **moved the work or the record**: the 1503 notary and the party's copy, the Easton clerk,
the grade card's inspector. Jones v. Meehan moved risk to the drafter by construction and expressly declined to rest
on evidence of what the Indians understood (pp. 23-24). The one disclosure regime with a clean measured protective
effect (Simon 2005) works because nobody at the point of use reads: an inspector reads, and the artefact carries one
letter.

### Claims the sources contradict

1. **B1 as written** ("the work moved to the artefact, or to a party owed to the weaker side, *and* someone checked
   the person's understanding"). The conjunction fails for the Pragmática (no check; Nov. Rec. X.23.1-5), Jones v.
   Meehan (pp. 23-24), the Easton clerk (a record, not a check) and the grade card. The property the corrections
   share is the first limb; the second holds only for the jurat, art. 193, teach-back and probate r. 13.
2. **Ledger H10's "the Pragmática of 1503 (notes read 'presentes las partes e los testigos')"** is right on the
   reading but should add what the law also gives: the party's own copy within three days and on demand (leyes
   III, V). The manuscript line "requiring public readings of instruments before witnesses" (ledger 04:74) is
   accurate and incomplete.
3. **Legacy card `northcarolina1831acts`** rests on a transcription that omits the books-and-pamphlets clause and
   misstates the penalty for a free person of colour; the printed act agrees with the 1837 Revised Statutes.
4. **Ledger H13's "Jomtien proposed halving"** is right, but the proposal was an optional dimension ("may wish ...
   say, one-half", para. 8). "Promise unmet" should be pinned to the Declaration's "can and must be met" and to
   Dakar's goal 4, not to a Jomtien commitment.
5. **"Disclosure in place of understanding" as a general failure** (A2) is contradicted by the grade-card evidence
   (Simon 2005; Jin and Leslie 2003). The failure the record supports is disclosure that leaves the reading to the
   person bound.
6. **"Competence withheld then oversold"** as a pattern of literacy's growth meets the Cuban counter-case (declared
   figures, Kempf; Bhola carded) and Nepal's confirmed cohort gain (GMR 2015, p. 144). It is a recurrent failure, not
   a law.
7. **Jones v. Meehan as a correction "for" the Indians** (ledger H23): its effect in the case was to uphold a white
   lessee's cheap early lease against an Interior-approved later one (pp. 6-8, 32).
8. **Facet V5's figure "268,420 tutors"** (from Bhola) differs from Kempf's 120,632 volunteers plus 147,788 paid
   teachers (Kempf p. 3, citing Huberman and Sweezy); both report 3.9% residual illiteracy.

---

## (d) What the argument can rest on

| Premise / claim | Cards that carry it (read status) |
|---|---|
| A2: the burden of reading on the person bound (H19) | `hill1997gateway` (full; pins 1148-1149); `lestrange1934graucob` (full, carded); `parker1877south` (full; with the narrowing that Parker denies a duty to read but presumes an English reader) |
| A2: record kept by one side (H07) | `israeli2022requerimiento` (full, p. 62); `pennsylvania1851minutes` (part, p. 664); `hill1997gateway` (full, at 1149) |
| A2: disclosure in place of understanding (H22, H24) | `tam2015participants` (full); `nishimura2013improving` (full); `israeli2022requerimiento` (full, p. 62). Narrow to "disclosure that leaves the reading to the person bound" (`simon2005impact`, full) |
| A2: competence withheld (H04) | `virginia1831acts` (full, page images); `northcarolina1831acts` (full, page image) |
| A2: competence oversold (H13) | `unesco2015education` (part, pp. 135-147); `wcefa1990world` (part); `frahm2022fixing` (full, for the mechanism) |
| A3: promise unmet (H13) | `unesco2015education` (part, p. 135); `unesco2000dakar` (part, carded) |
| A3: contemporaries objected / a professed standard broken (H18, record) | `israeli2022requerimiento` (full, pp. 47, 61-62); `pennsylvania1851minutes` (part, pp. 656-657); `lascasas1876historia` (full, carded) |
| B1 limb 1: work or record moved to an artefact or to a party owed to the weaker side | `spain1805novisima` (part, pp. 144-145); `pennsylvania1851minutes` (part); `lely1883judicature` (part); `simon2005impact` (full) |
| B1 limb 2: someone checked understanding | `lely1883judicature` (part; an impression); `tamariz2013improving` (abstract); `sudore2006use` (full, carded); `spain1944reglamento` (part, carded). Thin: no full-text source shows a test the person controls in a historical setting |
| D04 precedent (the person's own record) | `pennsylvania1851minutes` (part); `spain1805novisima` (part, leyes III, V) |
| D06 precedent (check understanding, carry the risk) | `lely1883judicature` (part); `jones1899meehan` (full; risk only); `nishimura2013improving` (full) |
| D08 precedent (scaffold owed and delivered) | `kempf2014cuban` (part; declared figures); `alvord1868fifth` (part); `bhola1984campaigning` (part, carded) |

---

## (e) Gaps and blocks (for the library list)

| Item | Why not read | Where a Bentley library user would find it |
|---|---|---|
| Seed, *Ceremonies of Possession* (Cambridge UP, 1995), ch. 3, pp. 69-99 | No open copy | Print or ebook via library catalogue; ISBN 978-0-521-49748-0 (per Crider's review) |
| Graff, *The Literacy Myth* (Academic Press, 1979), pp. 2, 17-19, 301-302, 321 | archive.org lending-only; search-inside restricted | Print via interlibrary loan; compare with the 1991 Transaction pages the arm holds |
| Burns, "Notaries, Truth, and Consequences", AHR 110(2) (2005) 350-379 | Closed | JSTOR or Oxford Academic (AHR) |
| Burns, *Into the Archive* (Duke UP, 2010) | Closed | Ebook via library (Duke UP / JSTOR) |
| Muldoon, *The Americas* 36(3) (1980) 301-316 | Closed | JSTOR (doi 10.2307/981289) |
| Faudree, CLAR 24(4) (2015) 456-478; Faudree, *Journal of Linguistic Anthropology* 22 (2012) 182-200 | Closed | Taylor & Francis; Wiley (via library proxy) |
| Merrell, *Into the American Woods* (Norton, 1999) | archive.org lending-only | Print via catalogue |
| Fleming, *Gettysburg Historical Journal* 15(1) (2016) art. 4 | Cloudflare challenge | Open on the web in a browser: cupola.gettysburg.edu/ghj/vol15/iss1/4 |
| Palacios Rubios, *De las islas del mar Océano* (with Zavala's introduction, FCE, 1954) | Not found | Catalogue / interlibrary loan |
| *Libro de las Bulas y Pragmáticas de los Reyes Católicos* (1503 print) | Not searched beyond the Novísima Recopilación | Facsimile editions via interlibrary loan; Biblioteca Digital Hispánica |
| Jin and Leslie, QJE 118(2) (2003) 409-451 | SSRN 403; journal closed | Oxford Academic (QJE) via library |
| Tamariz et al., JGIM 28(1) (2013) 121-126 | Springer challenge; PMC not open | Springer via library proxy |
| Flory and Emanuel, JAMA 292(13) (2004) 1593-1601 | Closed | JAMA Network via library |
| Re Longstaff, Weekly Notes 1884, 216 | Not searched | Law Reports Weekly Notes (HeinOnline / Westlaw UK) |
| Huberman and Sweezy, *Socialism in Cuba* (1969), pp. 25-26 (Kempf's source for Cuban figures) | Not searched | Print via catalogue |
| Korea's post-1945 literacy campaign | No source found in two OpenAlex searches | Korean education history in library databases (e.g. ERIC, Korea Journal) |
| Alvord's first report (1 January 1866) as published | Not found on archive.org | Senate Executive Documents, 39th Cong., 1st Sess. (U.S. Congressional Serial Set, ProQuest) |
| North Carolina 1830-31 session laws: page number of ch. VI | Scan's folio illegible | NC Digital Collections in a browser (higher-resolution viewer), or the printed volume |
