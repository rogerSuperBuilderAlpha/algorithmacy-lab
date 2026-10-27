# C — Did a change in page conventions spread reading? (tests H-cause)

*Corrected on 2026-10-12 against `../audit/AUDIT_01.md`: 9 factual fixes.*

*Facet C of the DXD foundation-paper literature review, 2026-10-12. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

**What this facet covers.** (1) What the standard histories of medieval, early modern and ancient literacy name as the drivers of the spread of reading (Clanchy, Stock, McKitterick, Graff, Houston, Cressy, Cipolla, Eisenstein/Johns, Goody, Street, Scribner and Cole, Havelock, Harris). (2) Whether any of them treats word separation, punctuation, script reform or layout as a cause or enabling condition, and with what weight; silence is reported as a finding with the search evidence. (3) Dates of spacing against dates and estimates of literacy. (4) Evidence on how novices were taught, and Saenger's "phonetic" versus "comprehension" literacy. (5) Modern cross-script evidence: orthographic depth, Hangul, the Turkish reform of 1928, Chinese simplification. (6) The strongest statements that technology or script design alone does not produce literacy.

**The question the synthesis answers.** Does any credible scholar support the author's phrase that the move from *scriptio continua* to spaces between words "ignited literacy" (H-cause), or do the sources support the weaker claim that spacing moved parsing work from reader to page and lowered a cost (H-cost)? Section (c) gives a verdict, the most defensible sentence, and the claims in the author's framing that the sources contradict.

**Legend for read status.**
- *Read in full*: I read the whole text this session. **No book in this facet reaches this level.**
- *Read in part, search-inside*: the book is a borrowable scan on archive.org that I did not borrow. I queried archive.org's public full-text search API (`be-api.us.archive.org/fts/v1/search`), which returns OCR snippets of about one line around each hit, plus an index of hits. Each quotation below is one such snippet, normalised for OCR hyphenation and spacing only. I did not see the surrounding paragraph, and the API gives a scan-page index, not the printed page number, so **no printed page locator is given unless the book's own index or contents supplies it**. Re-check every quotation in context before it enters a draft. A search result of "0 hits" means the term is absent from the OCR text archive.org indexed; OCR can drop words, so a zero is strong evidence of rarity, not proof of absence.
- *Abstract only*: database abstract (Consensus, Crossref) read, text not.
- *Not accessible*: record verified, no text or abstract.
- *Review only*: I read a review's account of the work.

The snippet route is the same thing as a library user's search-inside box. The Cluster H cards in `algorithmacy_design_ethics/literature/library/` rest on secondary reading for most of these books; the entries below add search-inside evidence, not a full read.

---

## (a) Search log

All searches ran on 2026-10-12.

| # | Source | Exact query / request | Hits | Notes |
|---|---|---|---|---|
| 1 | Repo | Read `RESEARCH_PLAN.md`, `REUSE.md`, Part 2 facet E, library cards `clanchy2013`, `street1984`, `havelock1963`, `ong1982`, `scribner1981`, `INDEX.md` 331-384 | n/a | Reused: Havelock card (re-verified below), Part 2 facet E for Saenger/Parkes chronology. |
| 2 | archive.org `advancedsearch` | titles of 14 works (Clanchy, Stock, McKitterick, Graff x2, Houston, Cipolla, Cressy, Eisenstein, Goody, Scribner and Cole, Street, Saenger, Olson and Torrance) | identifiers found for all but Harris | Harris, *Ancient Literacy*: no archive.org item found under title or author. |
| 3 | archive.org full-text API | for each book, `"word separation"`, `"separation of words"`, `"word division"`, `"scriptio continua"`, `"scriptura continua"`, `"silent reading"`, `Saenger`, `punctuation`, `"Carolingian minuscule"`, `"spaces between"`, `"between words"`, `"word spacing"`, `"word-separation"`, each `AND identifier:<item>` | see entries | The core of the silence evidence. Identifiers are given in each entry. |
| 4 | archive.org full-text API | follow-ups per book (e.g. `"caroline minuscule"`, `legibility`, `"lay literacy"`, `"largely a response to need"`, `"supply of readers"`, `"runs across the page"`, `"physiology of reading"`) | see entries | Used to widen snippet context. |
| 5 | archive.org full-text API (global) | `"phonetic literacy" "comprehension literacy"` | 39 items | Found Zieman 2008, Thomas 1992 and others citing or criticising Saenger's pair. |
| 6 | archive.org full-text API (global) | `"autonomous model" "ideological model" Street` | 761 | Located Street 1984 (`unset0000unse_e6x6`). |
| 7 | Crossref `/works/{doi}` | 10.1348/000712603321661859; 10.1037/0033-2909.131.1.3; 10.1484/J.VIATOR.2.301476; 10.4159/9780674038370; 10.1017/s0020743811000900; 10.1016/j.labeco.2024.102618; 10.1080/20780389.2025.2450331; 10.1093/wsr/wsr002; 10.1111/ehr.12538; 10.1086/214978; 10.1177/0956797610363406; 10.1353/phl.1991.0070; 10.1017/jea.2025.6 | 13 of 14 resolved | Titles, containers, volumes, pages matched. Hong et al. is vol. 71 (2018), online 2017. 10.1017/S0003055400210234 (a guess) returned nothing and is not used. |
| 8 | OpenAlex `works?search=` | Saenger Books of Hours; Seymour/Aro/Erskine; Hangul literacy; Turkish reform; Rawski | 0 | Daily free budget exhausted ("Rate limit exceeded"). Not retried. Rawski, *Education and Popular Literacy in Ch'ing China* (1979), is therefore **unchecked** and not cited. |
| 9 | Unpaywall | Seymour et al. 2003; Ziegler and Goswami 2005 | `is_oa: false`, no locations | Both paywalled; no author copy found. |
| 10 | Consensus | `orthographic depth and speed of literacy acquisition across European languages` | 20 | Seymour et al. abstract read; Ziegler et al. 2010 abstract read. |
| 11 | Consensus | `Turkish alphabet reform 1928 effect on literacy rates schooling` | 20 | Wood 1929, Yilmaz 2011, Filiztekin 2025 abstracts read. |
| 12 | Consensus | `Hangul design and Korean literacy: script or schooling` | 20 | Pae 2011 and others; used mainly for design claims. |
| 13 | Consensus | `Korean literacy rate rise after 1945 illiteracy campaign Hangul history schooling` | 20 | Clemens 2025 review, Becker et al. 2024, Hong et al. 2018, Ivanova 2026. |
| 14 | Consensus | `effect of Chinese character simplification on literacy rates evidence` | 20 | No causal estimate found. Weng 2023, Kuzuoglu 2022, Li 2004 are context only. |
| 15 | Consensus | `Harris Ancient Literacy rates of literacy in the Greek and Roman world estimate 10 percent` | 20 | Zanker 1991 and Sherratt 1989 reviews of Harris read (abstracts reproduce the review text). |
| 16 | WebSearch | `Saenger "Books of Hours and the Reading Habits of the Later Middle Ages" "phonetic literacy" "comprehension literacy"`; `historians criticism Saenger Space Between Words ...` | 0 useful | Returned blogs and catalogue pages only. Nothing relied on. |
| 17 | Scholar Gateway `semanticSearch` | `Did the introduction of word separation in medieval manuscripts increase literacy rates?` | error | `ACCESS_DENIED: Access denied`. Not retried. |
| 18 | archive.org metadata | each item identifier | n/a | Every book item is `access-restricted` (lending library). I did not borrow or download any of them. |

A copy of Saenger's *Space Between Words* also sits on archive.org as an upload from a pirate-library mirror (item `space-between-words-the-origins-of-silent-reading`). Its search snippets surfaced in the global search. I **do not rely on it**: every Saenger quotation below was re-confirmed against the lending-library scan `spacebetweenword0000saen`, and I downloaded nothing from either.

---

## (b) Entries

Order: the two sources that bear most directly on H-cause (Saenger and Saenger's critics); then the histories of literacy; then the theory and the Vai evidence; then the cross-script evidence.

### B1. Saenger and the reception of "phonetic" and "comprehension" literacy

**saenger1997space** — Saenger, P. (1997). *Space between words: The origins of silent reading*. Stanford University Press. DOI 10.1515/9781503619081.
- *Verification:* Crossref (via Part 2 facet E); archive.org lending scan `spacebetweenword0000saen` (514 scan pages).
- *Read status:* read in part, search-inside (items 3-4 above). Nothing else was read this session. Part 2 facet E holds the snippet-level chronology.
- *What it says about literacy as a whole.* Saenger disclaims the question. Preface: "this book, which, I would stress, is not a general history of literacy. Instead, I have attempted to explain the physiological and psychological influence of word separation on the reading [process]" (preface, snippet; the object after "reading" is cut). On p. 11 (the audit corrects "front matter") he lists "the greater diffusion of literacy throughout all social strata of the population" among the "advantages that modern readers perceive as accruing from ease of reading", which the ancients "seldom viewed as advantages". He attaches this to ease of reading in general and presents it as a modern value; he offers no evidence that spacing raised the number of readers (AUDIT_01, Problems item 4).
- *Spacing as pedagogy for novices.* "The exclusive use of a syllabary method of presenting text to novice readers, necessitating the oral reconstruction..." (snippet; the sentence is cut, and it concerns the pre-separation teaching of beginners). Other snippets: "manuscripts and early printed books intended for beginning readers also followed the practice of inserting additional [marks]"; "regular word separation was not a sign of a low level of literacy or defective Latinity" (about an eleventh-century scribe; the sentence is cut). Saenger therefore treats separation both as help to the beginner and as a feature of competent scribes.
- *Why it came late.* "that modern readers perceive as accruing from ease of reading were seldom viewed as advantages by the ancients"; Part 2 facet E reports p. 11: "The notion that the greater portion of the population should be autonomous and self-motivated readers was entirely foreign to the elitist literate mentality of the ancient world." This is a **demand-side** explanation: the ancient world did not want mass reading, so it did not adopt spacing.
- *Spread.* Contents (OCR snippet, merged): "Chapter 15 Twelfth and Thirteenth Centuries: The Spread of Canonical Separation, 244". The audit finds this is chapter 14, "The Twelfth and Thirteenth Centuries" (opening p. 243), and that "The Spread of Canonical Separation" is a section at p. 244; chapter 15 is "Written Culture at the End of the Middle Ages"; "The Spread of Word Separation from England to the Low Countries"; "...to Northern France". Dates for facet A to settle.
- *Bearing:* **Supports H-cost** (separation simplified a physiological task). **Complicates H-cause**: the author most cited for the thesis calls his book "not a general history of literacy" and gives the ancient world's lack of wish for mass reading as the reason spacing was absent, which makes the demand for readers precede the page convention.

**saenger1991separation** — Saenger, P. (1991). The separation of words and the physiology of reading. In D. R. Olson & N. Torrance (Eds.), *Literacy and orality* (ch. 12). Cambridge University Press.
- *Verification:* contents and index in `literacyorality0000unse` (archive.org lending scan; the book is Olson and Torrance 1991).
- *Read status:* read in part, search-inside. Chapter pagination not seen (the index snippet suggests the chapter runs about pp. 198-214; unconfirmed).
- *What it says:* "Word separation, by altering the physiology of reading and thereby simplifying the reading process, enabled the reader to simultaneously [...]" and "...more difficult texts with greater ease" (two adjacent snippets). The editors' introduction, summarising the chapter, says Saenger "points out that while syllabic scripts such as Hebrew have used word separation since antiquity, alphabetic scripts (Greek and Latin) abandoned [it]" and that "Japanese syllabary transcriptions contain no word separation and impose on the young reader the formidable burden of word recognition through the synthetic [method]" (the second sentence reads as Saenger's own, but the snippet's speaker is uncertain).
- *Bearing:* **Supports H-cost.** The claim is about reading efficiency for the fluent reader, not about who reads. The Hebrew sentence is a counter-datum to H-cause: a separated script from antiquity, with no mass literacy attached.

**saenger1982silent** — Saenger, P. (1982). Silent reading: Its impact on late medieval script and society. *Viator, 13*, 367-414. DOI 10.1484/J.VIATOR.2.301476.
- *Verification:* Crossref. *Read status:* not accessible (Brepols is bot-walled; Part 2 facet E logged the same). Cited by Clanchy and Graff (see below).

**saenger1989books** — Saenger, P. (1989). Books of Hours and the reading habits of the later Middle Ages. In R. Chartier (Ed.), *The culture of print* (page range **not found**). Princeton UP.
- *Verification:* the title and the Chartier container are confirmed by the bibliographies of Houston 2002 and Clanchy 1993 (snippets); the page range and publisher were not found.
- *Read status:* not accessible. Known through secondary use:
  - Houston (2002) cites it for comprehension literacy: "This meant reading silently and with full understanding (Saenger 1989: 142)".
  - Two other books paraphrase the pair: one (Margery Kempe study, item `margerykempesmed0000yosh`) writes that Saenger "categorizes reading ability into two types: phonetic literacy, defined by the ability to decode texts syllable [by syllable]... and comprehension literacy, defined as the ability to decode a written [text silently word by word and understand it]". The ancient-history volume (Thomas 1992, below) quotes the definition: "'Comprehension literacy' was 'the ability to decode a text silently word by word' and understand it fully; 'phonetic literacy' was the ability to 'decode texts syllable [by syllable] orally', close to oral rote memorization."
- *Bearing:* the pair is a classification of **reader types**, not an account of what caused readers to appear. It fits the author's interest in who can read in what way, but it ties the shift to late-medieval devotional use, with the Book of Hours as the evidence.

**zieman2008singing** — Zieman, K. (2008). *Singing the new song: Literacy and liturgy in late medieval England*. University of Pennsylvania Press.
- *Verification:* archive.org metadata (`singingnewsongli0000ziem`). *Read status:* read in part, search-inside.
- *What it says:* a criticism of the "phonetic literacy" category. "Saenger, by contrast, identifies 'phonetic literacy' as a skill possessed by lay users of Latin..."; "modern perceptions of 'phonetic literacy' are, I suspect, based less on medieval evidence than on our own experience of, for [example...]" (snippet cut). Zieman's point (as far as the fragments show) is that medieval people did not hold a single scale on which "decoding without understanding" counts as lesser literacy.
- *Bearing:* **complicates** the use of Saenger's pair as a measure of who "could read". A fuller read is needed before this entry supports any claim stronger than "a specialist in the field disputes the category".

**thomas1992literacy** — Thomas, R. (1992). *Literacy and orality in ancient Greece*. Cambridge University Press.
- *Verification:* archive.org metadata. *Read status:* read in part, search-inside.
- *What it says:* applies Saenger's pair to antiquity: "'Phonetic literacy' seems particularly relevant to the ancient context where reading was not done [silently...]". Also: "treat literacy as if it were a monolithic skill may be a modern fallacy."
- *Bearing:* **complicates** H-cause. An ancient historian treats unspaced reading as a different kind of literacy, not a lack of it.

### B2. Histories of literacy that name drivers

For each: identifiers, read status, what drivers they name, what the term search returned. All are search-inside only.

**clanchy1993from** — Clanchy, M. T. (1993). *From memory to written record: England 1066-1307* (2nd ed.). Blackwell. (The repo card `clanchy2013` covers the 3rd edition, Wiley-Blackwell 2013.) Item `frommemorytowrit0000clan_e1n6_2ed`, 438 scan pages.
- *Read status:* read in part, search-inside.
- *Drivers named.* Administration and the habits of record. Chapter 10 is titled "Practical Literacy"; Part II is "The Literate Mentality". "The book therefore describes the growth of a literate mentality" (preface/introduction snippet). Another snippet: "Emphasis on practical literacy is a commonplace of twentieth-century culture" followed by a "not necessarily an inevitable process" clause (snippet cut). Government: "extended to nearly every sphere of government, both central and local" (ch. 10 snippet). On the pace of change: "Individuals still had few books of any size, and reading aloud persisted."
- *Word separation.* The index has "word separation" under "format and layout of writings" with a page given as 130 (index snippets: "word separation, 130"; "word separation see format and layout"; "format and layout of writings, 104-5, 131-5, 141-3, 172-4, 280-1"). Clanchy treats it as one feature of how twelfth-century documents were laid out, in a chapter on the technology of writing. Other term hits: `"scriptio continua"` 0; `"separation of words"` 0; `"word division"` 0; `"spaces between"` 0; `"silent reading"` only in notes citing Saenger (1982) and Kittay; `"Carolingian minuscule"` 1 hit (a comparison with the later script); `Saenger` only in bibliography notes (the 1982 *Viator* paper and the 1989 Chartier chapter). The audit also found a sentence beginning "Word separation was developed by Irish and Anglo-Saxon monks" (OCR-garbled), so Clanchy does state the Irish origin; the zero for "separation of words" holds for that phrasing only. Sentence and page: NEEDS LIBRARY CHECK.
- *Bearing:* **Refutes the ignition framing from the field's founding English-language case.** Clanchy's drivers are the king's government, lawyers and landholders' need for documents; spacing is a page-layout detail on p. 130.

**stock1983implications** — Stock, B. (1983). *The implications of literacy: Written language and models of interpretation in the eleventh and twelfth centuries*. Princeton UP. Item `implicationsofli0000stoc` (626 scan pages).
- *Read status:* read in part, search-inside.
- *Drivers named.* Interpretive communities organised around a text: ch. on "Textual communities", with the heresies at Orleans (1022), Arras (1025) and Monforte (1028) as cases. "In this sense they were 'textual communities.'" Also "the notion that literacy is identical [with ...]" (snippet cut): Stock objects to equating literacy with the ability to write or read Latin.
- *Term search:* `"word separation"` 0; `"separation of words"` 0; `"word division"` 0; `"scriptio continua"` 0; `"scriptura continua"` 0; `"silent reading"` 0; `Saenger` 0 (although the Saenger 1997 acknowledgements thank Stock, and Saenger cites Stock); `punctuation` 0; `"Carolingian minuscule"` 0; `"between words"` hits are about the relation of words to things.
- *Bearing:* **Silent.** The medieval history of literacy that Saenger himself cites as an influence does not mention spacing or punctuation.

**mckitterick1989carolingians** — McKitterick, R. (1989). *The Carolingians and the written word*. Cambridge UP. Item `carolingianswrit0000mcki` (314 scan pages).
- *Read status:* read in part, search-inside.
- *Drivers named.* The state and church: the *Admonitio generalis* of 789, which "had decreed that schools were to be [established at monasteries and cathedrals]" (snippet cut); law and the written word; the "literacy of the laity" chapter; "levels of at least pragmatic literacy were high enough for there to be some relation [between written and oral...]" (snippet cut); she follows Parkes on "pragmatic literacy".
- *Script.* The book discusses Carolingian minuscule in detail as a regional hand: "A clear St Gall version of the caroline minuscule emerged by the third decade of the ninth [century]". Term search: `legibility` 0; `legible` 0; `punctuation` 0; `"reading aloud"` 0; `"read aloud"` 0; `"word divisions"` 0; `"easier to read"` 0; `Saenger` 0 (not in the OCR, though the book predates Saenger 1997 by eight years; Saenger's 1982 article exists).
- *Bearing:* **Silent on word separation and legibility** in the one standard book on the literacy of the century in which Carolingian minuscule spread. Script appears as a palaeographic and institutional matter (scriptoria, regions), not as an access matter.

**graff1987legacies** — Graff, H. J. (1987). *The legacies of literacy: Continuities and contradictions in western culture and society*. Indiana UP. Item `legaciesoflitera0000graf` (522 scan pages).
- *Read status:* read in part, search-inside.
- *Drivers named / thesis.* Graff's thesis is that the "literacy myth" fails: the snippets include "the 'literacy myth' no longer serves as a satisfactory [guide]" and a chapter on a "printing myth": "'printing myth,' to rest beside the 'literacy myth.'... Despite the undoubted significance of [printing]..."; "the myth of printing and the book has grown up with the literacy myth." On the quality of mass literacy: "Mass literacy was, however, never a highly skilled one; it was socially, sexually [stratified]" (snippet cut).
- *Script and silent reading.* Graff does touch the topic, briefly: "Latin punctuation developed to assist such readers" (readers who received most literature orally, snippet); "portability and readability became a greater concern. Silent reading was spreading, too."; "Personal, private, and individualized silent reading was becoming more common, but oral reading [was] not disappearing."; "The style of totally silent reading developed slowly and probably with some [difficulty]". Saenger is cited twice (1982 *Viator*; notes at "Culture, pp. 162-163, 164"). `"word separation"` 0; `"scriptio continua"` 0; `"Carolingian minuscule"` 0.
- *Bearing:* **Complicates** H-cause. Graff mentions silent reading and punctuation as developments inside the late Middle Ages, in a book whose argument is that technologies, print included, are mythologised as causes of literacy. Here is a credible historian who names the page features, and gives them a supporting, not a driving, role.

**graff1979literacy** — Graff, H. J. (1979). *The literacy myth: Literacy and social structure in the nineteenth-century city*. Academic Press. Item `literacymythlite0000graf`.
- *Read status:* read in part, search-inside. Two hits for "silent reading" (nineteenth-century school pedagogy: "At mid-century, before silent reading was valued as a pedagogical tool...") and zero for the other terms. The book's period is the nineteenth century. The title's argument (literacy does not automatically produce the economic and moral benefits ascribed to it) is general; I did not read it here.

**houston2002literacy** — Houston, R. A. (2002). *Literacy in early modern Europe: Culture and education 1500-1800* (2nd ed.). Longman. Item `literacyinearlym0000hous_i9l5` (326 scan pages).
- *Read status:* read in part, search-inside.
- *Drivers named.* Schooling, Reformation and Counter-Reformation, social and economic need, printing as a secondary factor. "Schooling must be seen in the context of social and economic [conditions]"; schooling "was more often an expression of social practices than it was an independent stimulator of literacy" (two snippets, the second reconstructed from "for learning as much as it was an independent stimulator of literacy"; treat the wording as approximate). "The invention and spread of printing by movable type was the most significant [of the autonomous developments]" followed by a statement that "the development of printing was episodic and its impact, as with any innovation [was ...]" (snippets cut). The Reformation's effects were "not always immediate. In Prussia and Denmark it was not the Lutheran Reformation of the [sixteenth century that mattered...]".
- *Term search:* `"word separation"` 0; `"scriptio continua"` 0; `punctuation` appears only for the quality of writers' spelling; `"silent reading"` 1 (Danish *indenadslesning* contrasted with oral reading, "first developed among the laity during the [period]"); `Saenger` 2 (the Chartier chapter, p. 142, as above).
- *Bearing:* **Refutes** a spacing-first account of the spread of reading in the period when literacy rose fastest in Europe. Houston uses Saenger only for the definition of a kind of reading.

**cressy1980literacy** — Cressy, D. (1980). *Literacy and the social order: Reading and writing in Tudor and Stuart England*. Cambridge UP. Item `literacysocialor0000davi` (266 scan pages).
- *Read status:* read in part, search-inside.
- *Drivers named.* "The evidence indicates that the penetration of literacy in England was largely a response to need, need felt selectively in different trades [and regions]" (snippet cut after "trades"). Religion and schools: he discusses and qualifies Lockridge's thesis ("England's precocious literacy in protestantism... Intense protestantism supplied the drive to found schools"), noting that a "combination of religion and utility, rather than protestantism alone, [singled out New England]". Teaching: a chapter on the pedagogy of basic literacy under "Elizabethan and Stuart" schoolmasters (Mulcaster, Bullokar, Clement's *Petie schole*).
- *Numbers (England, signatures and marks).* "Aggregate figures for the sixteenth century are not readily available, but a reasonable guess might place male illiteracy around 80% and female illiteracy close to 95% at the time of the accession of Elizabeth" (1558). Another snippet: "The general level of literacy in England at the accession of George III would have astonished the proponents of [the old view]", with an earlier clause that a proportion "was reduced to about two out of three by the time of the accession of George III" (the subject of that proportion is unclear in the snippet; do not use as a male-literacy figure without checking).
- *Term search:* `"word separation"` 0; `"scriptio continua"` 0; `"silent reading"` 0; `Saenger` 0; `punctuation` hits are editorial notes ("Spelling and punctuation have been modernized") and one chapter reference to the *teaching* of punctuation.
- *Bearing:* **Refutes** ignition for England 1500-1750: the rise follows need and schools, 550 years after continental spacing.

**cipolla1969literacy** — Cipolla, C. M. (1969). *Literacy and development in the West*. Penguin. Item `literacydevelopm0000unse_r1i6` (150 scan pages; Cipolla's name confirmed in the item text).
- *Read status:* read in part, search-inside.
- *Drivers named.* Economic surplus and need, state and church action, and print. "The smallness of the economic surplus remaining in hand after the satisfaction of elementary economic needs"; "The reason for this was essentially economic" (about social stratification of schooling); "On occasion, enlightened rulers such as Charlemagne and Emperor Lothar I gave a helpful hand."; on print: "All this changed - with the invention of printing. It made more sense for the common people to acquire the art of [reading]." The Reformation "indirectly... also had beneficial effects on education"; Counter-Reformation concern too.
- *Term search:* all of `"word separation"`, `"scriptio continua"`, `"silent reading"`, `Saenger`, `punctuation`, `minuscule` return 0.
- *Bearing:* **Silent**; the book is the standard economic-history account, and its drivers are incentives, religion and the state, with print as the late stimulus.

**eisenstein1979printing** — Eisenstein, E. L. (1979). *The printing press as an agent of change*. Cambridge UP. Item `printingpressas01eise`.
- *Read status:* read in part, search-inside. `"word separation"` 0, `"scriptio continua"` 0, `punctuation` 1 (printed books supplied "regularly numbered pages, punctuation marks, section breaks, running heads, indices" as new reading aids), `Saenger` several (only the 1978 *Colard Mansion* article, on printing in Bruges, and a remark that Saenger "would have us place [certain data] in the post-Reformation [period]"). The press is her agent of change; punctuation and layout are print-era aids. Johns's critique (card `johns2002`) holds that uniformity was a social achievement, not a property of the press, and the repo card is the only treatment I rely on here.
- *Bearing:* the one thesis in this set that puts a page technology in the causal role places it in the fifteenth century, after spacing was already general, and layout (not spacing) is the affordance she names. **Complicates**: if anyone's mechanism is "interface change spreads reading", it is print's, and Johns and Graff dispute it.

**goody1986logic** — Goody, J. (1986). *The logic of writing and the organization of society*. Cambridge UP. Item `logicofwritingor0000good`.
- *Read status:* read in part, search-inside. All 13 terms return 0, including `punctuation` and `"silent reading"`. The index scan works (other terms hit), so this is a real silence in the OCR. Goody's account of writing's effects is institutional (bureaucracy, religion, law) and about the invention of writing, not about page layout. The repo card `goody1986` is TOC-level only.

**ong1982orality** — Ong, W. J. (1982). *Orality and literacy*. Methuen. Item `oralityliteracyt00ongw`; repo card `ong1982` (chs. 3-5 read).
- *Read status:* read in part, search-inside plus the card. One passage of interest: manuscripts "commonly ran words together or kept spaces between them minimal. Eventually, however, print [...]" (snippet; sentence cut), and "the greater legibility of print... ultimately makes for rapid, silent reading" (two snippets). Ong ties word spacing and legibility to **print**. `Saenger` 0; `"scriptio continua"` 0.
- *Bearing:* **Complicates**; in the most-cited orality theory, spacing consolidates with print. Per the standing ruling, Ong's cognitive claims are out of scope for DXD; this entry matters only for who he credits.

### B3. Theory: literacy is not a self-acting technology

**street1984literacy** — Street, B. V. (1984). *Literacy in theory and practice*. Cambridge UP. Item `unset0000unse_e6x6` (270 scan pages); repo card `street1984` (secondary).
- *Read status:* read in part, search-inside.
- *What it says:* the autonomous/ideological distinction: "shall characterise them as the 'ideological' model and the 'autonomous' model of literacy respectively" (snippet); the Olson, Hildyard and Goody strands are the "autonomous" targets; he criticises claims that "literacy in itself constructs superior logical functions". On writing conventions: "Recent writers (Crystal, 1976; Linell, 1983; Deuchar, 1983; Stubbs, 1980) have challenged this view" (that written conventions mirror speech). **Directly on point:** "In Vai script there are no spaces between either words or sentences and the reader has [to ...]" (snippet; the continuation is cut). Street also writes of the pre-print period that reading "was a long and laborious process; and that silent reading as we know it was very rare; until the advent of printing" (snippet, probably reporting a position he goes on to qualify; the speaker is uncertain).
- *Bearing:* **Supports** the claim that a convention of the page does not by itself define what a reader can do. Street offers no account of word separation as a cause; the Vai mention is a passing example.

**scribner1981psychology** — Scribner, S., & Cole, M. (1981). *The psychology of literacy*. Harvard UP. Item `psychologyoflite00sylv` (366 scan pages); repo card `scribner1981` (secondary via Ong).
- *Read status:* read in part, search-inside. This is the strongest evidence in the facet.
- *What it says:*
  - The Vai script, a syllabary used in Liberia, is unspaced: "A string of syllabic characters runs across the page without division into words or phrases." (ch. 3 area, near "Figure 3.2. The modern Vai syllabary"; printed page not seen).
  - It was learned informally: "Vai script does not require an extended period of study and is customarily learned in adulthood"; "Unlike English schooling, Vai literacy was traditionally obtainable in the countryside"; respondents said they had begun to learn at "fourteen or fifteen years of age" (three snippets).
  - Literacy without schooling had no general cognitive effect: "We could obtain no evidence that literacy in Vai script (or other [...]) [produces general cognitive effects]" (snippet cut); the question posed is "Does literacy per se (that is, literacy without schooling) [produce ...]"; "effects of schooling" were stronger: "was weak compared with effects of schooling". They name their framework "a practice account of literacy".
  - A passage on English: "[conventions of English] tried to introduce word spacing and punctuation. But these attempts at standardization [...]" (snippet; the subject is a historical English scribal convention, but the sentence is cut).
- *Bearing:* Vai is a documented unspaced syllabary used by a small adult population and learned informally in adulthood by respondents who had not gone to school (Scribner and Cole). It does not show whether spacing lowers the cost for learners; Heilmann (n. 24, citing Vatri 639) notes that Saenger himself uses Vai (Saenger p. 4) and that Thai is the closer comparison for Greek.

**havelock1963preface** — Havelock, E. A. (1963). *Preface to Plato*. Harvard UP / Belknap. Items `prefacetoplato0000have`; repo card `havelock1963`.
- *Read status:* the repo card (pp. 38-41, "probable" pagination, verified verbatim in an earlier pass) plus this session's snippet check of the key phrases.
- *Verified this session (snippets):* "upon the supply of readers, and this depended on a universalisation of [letters]"; "The reading trauma, to use a modern term, had to be imposed at [the primary level of schooling]"; "by the middle of the fourth century the silent revolution had been accomplished". Full quotations in the card.
- *Bearing:* **Supports** H-cost and the schooling driver. Havelock's decisive variable is "the supply of readers", produced by primary schooling. He names no page convention. A classicist can still be cited against the author's sentence: the "reading trauma" was imposed by an educational system, not removed by a script.

**harris1989ancient** — Harris, W. V. (1989). *Ancient literacy*. Harvard UP. DOI 10.4159/9780674038370.
- *Verification:* Crossref. *Read status:* review only. No lending copy found (log row 2). Two reviews were read in the Consensus abstracts: Zanker (1991, *Philosophy and Literature* 15:173-175, DOI 10.1353/phl.1991.0070) and Sherratt (1989, *Antiquaries Journal*, as a section of a longer review whose DOI points to a different book; the review text on Harris is intact).
- *What the reviews report.* Zanker: Harris "convincingly shows that the ancient world lacked some of the major preconditions for widespread literacy, especially urbanization, subsidized schools, technology for the inexpensive copying of texts, a state economy complex enough to require at least a semi-literate population, and an official acceptance of the belief... that literacy might improve the quality of life of the lower social orders." Numbers: "fifth-century Attica attained a literacy level of only 5 percent to 10 percent, and certain cities of the Hellenistic age like Rhodes formed the high point at 20 percent to 30 percent (the level reached by England in the period from 1580 to 1700), while literacy in the Roman Empire never achieved more than 15 percent." Sherratt gives "15 per cent total adult literacy would be the highest likely estimate" for classical Athens and imperial Italy, and says Harris is "sceptical of the ideas of Goody... and Havelock". The 20-30 per cent figure for Rhodes is Zanker's report of Harris; the audit did not find it in Harris, whose own text uses 20-30% as the male-literacy benchmark for England 1580-1700 and puts antiquity "well below" it.
- *Bearing:* **Complicates** H-cause. Zanker reports that an unspaced antiquity reached, in some cities, the literacy level that spaced England reached in 1580-1700 [unverified: see AUDIT_01; Harris's own text puts antiquity "well below" the 20-30% England benchmark] (the equivalence is Zanker's, and Harris's estimates are disputed; see Warkentin's 2020 review of Frampton in the Consensus result, and Johnson and Parker 2009). Harris's list of preconditions contains no page convention. I could not check whether the book discusses interpuncts or word division; flag for a library user.

### B4. Modern cross-script evidence

**seymour2003foundation** — Seymour, P. H. K., Aro, M., & Erskine, J. M. (2003). Foundation literacy acquisition in European orthographies. *British Journal of Psychology, 94*(2), 143-174. DOI 10.1348/000712603321661859.
- *Verification:* Crossref. *Read status:* **read in full (card: library/seymour2003foundation.md)**; first read as abstract only (Consensus). Unpaywall: not open access.
- *What it says (abstract):* "children from a majority of European countries become accurate and fluent in foundation level reading before the end of the first school year. There are some exceptions, notably in French, Portuguese, Danish, and, particularly, in English." "The rate of development in English is more than twice as slow as in the shallow orthographies." The body gives the ratio as "about 2.5:1" (English readers need "2½ or more years" for what most European children reach in the first year, pp. 167–168; a regression extrapolation on reading age, not an observed time-to-mastery). Letter-sound knowledge does not differ between the languages (about 90% or better in every group, p. 151); the gap sits in word and nonword reading (Tables 5 and 6, pp. 153, 156). Cause: "fundamental linguistic differences in syllabic complexity and orthographic depth".
- *Bearing:* **Supports H-cost in the narrow sense** that orthographic design changes the **rate** of acquisition **among children in school**. It says nothing about who gets to school.

**ziegler2005reading** — Ziegler, J. C., & Goswami, U. (2005). Reading acquisition, developmental dyslexia, and skilled reading across languages: A psycholinguistic grain size theory. *Psychological Bulletin, 131*(1), 3-29. DOI 10.1037/0033-2909.131.1.3.
- *Verification:* Crossref. *Read status:* not accessible (abstract not retrieved; Unpaywall reports no open copy). Cited by the research plan only.
- **Ziegler et al. (2010)**, *Psychological Science 21*(4), 551-559, DOI 10.1177/0956797610363406: abstract read. "Most predictors of reading performance were relatively universal across these alphabetic languages, although their precise weight varied systematically as a function of script transparency." *Read status:* **read in full (card: library/ziegler2010orthographic.md)**. Not the same bearing as Seymour: it reports predictors of reading (reading speed and accuracy) in Grade 2 in five alphabetic languages, not rates of acquisition, and the paper restricts its claim to alphabetic scripts and flags Chinese as unexplored (p. 557).

**Turkey 1928.**
- **wood1929latinizing** — Wood, M. M. (1929). Latinizing the Turkish alphabet. *American Journal of Sociology, 35*(2), 194-203, DOI 10.1086/214978. Abstract only. A contemporary sociologist: "The old Turkish writing required nearly five hundred separate Arabic characters. Its difficulty to learn was a factor in Turkish educational lag"; but "The master-stroke in spreading knowledge of the new alphabet came with the opening of the national schools on January 1, 1929", with a four-month course for illiterates and fines for those aged sixteen to forty who could not read and had not attended. **This is the closest thing to an "interface change plus state campaign" case, and it needs both halves.**
- **yilmaz2011learning** — Yilmaz, H. (2011). Learning to read (again): The social experiences of Turkey's 1928 alphabet reform. *IJMES, 43*(4), 677-697, DOI 10.1017/s0020743811000900. Abstract only: it stresses "the actual processes, institutions, and lived experiences" and "the persistence of the Ottoman script", against a picture of silent obedience.
- **filiztekin2025unification** — Filiztekin, A. (2025). *Economic History of Developing Regions, 40*, 80-97, DOI 10.1080/20780389.2025.2450331. Abstract only: district-level data 1927-1945; "in districts where state presence was strong literacy rates increased faster, confirming the importance of state capacity"; slower in districts with a larger Kurdish minority.
- *Bearing on all three:* **Complicates** and half-supports. The script change plausibly lowered learning cost (Wood), but the measured variation in the following decades tracks state presence and schooling (Filiztekin), and the spread was uneven.
- *Not verified:* a figure circulating in a secondary article (literacy "from about 8 per cent in 1928 to over 20 per cent in 1935") appeared only in a Consensus abstract of an article about a music magazine; I did not follow it. Do not cite it. A census-based series is needed.

**Korea and Hangul.**
- **pae2011korean** — Pae, H. K. (2011). Is Korean a syllabic alphabet or an alphabetic syllabary. *Writing Systems Research, 3*(2), 103-115, DOI 10.1093/wsr/wsr002. Abstract only: describes the script as meeting Rogers's criteria "easily acquired by the beginning reader and efficient for the skilled reader" ("arguably").
- **clemens2025korea** — Clemens, W. (2025). Review of Cha and Pardo, *Korea: A new history of South and North*. *Journal of East Asian Studies, 25*, 159-162, DOI 10.1017/jea.2025.6. Read in full (card: library/clemens2025korea.md). The reviewer says: Hangeul sponsored in 1443 "to facilitate literacy"; "initially denounced and disparaged by the Korean educated class"; "by 1912 literacy in Korea was only 20 percent. It rose to over 60 percent by 1940." These figures are the **reviewer's own**, unsourced and not marked as the book's (the reference list does not support them); do not describe them as what Cha and Pacheco Pardo report. I have not checked them against a census.
- **ivanova2026process** — Ivanova, Y. (2026). A process of implementing the Korean alphabet on the Korean peninsula. *Ezikov Svyat, 24*(1), DOI 10.37708/ezs.swu.bg.v24i1.9. Read in full (card: library/ivanova2026process.md; the card adds statements about spacing in the body that are new to the project, and dates the Kabo reforms to 1894 and the first joint hangul-and-hanja newspaper to 1886, p. 138). Abstract: "for centuries the Korean alphabet was marginalized and associated with women, children, and the lower social classes." (DOI not Crossref-checked.)
- **becker2024conquering** — Becker, S. O., et al. (2024). Conquering Korea for Jesus. *Labour Economics, 91*, 102618, DOI 10.1016/j.labeco.2024.102618. Read in full (card: library/becker2024conquering.md). Printed abstract: Protestant church density predicts 1930 literacy, instrumented on missionary location, and Presbyterians did better than Methodists. The quotation earlier given here ("Protestantism played a crucial role in the accumulation of human capital") does not appear in the PDF (abstract or text) and is withdrawn. Flag: Becker and Won date the start of government efforts to teach Hangul to "the Gabo Reform in 1886" (p. 6), while Ivanova (p. 138) dates the Kabo reforms to 1894 and the joint newspaper to 1886; one has the date wrong or they mean different things.
- **hong2018colonization** — Hong, J., et al. (2018). Colonization and education. *Economic History Review, 71*(3), 938-964, DOI 10.1111/ehr.12538. Abstract only: early-colonial literacy "was strongly correlated with the historical presence of civil exam passers" and with private schools.
- *Bearing:* **Refutes the interface-spreads-competence model on the best test case in the set.** A script built for ease of learning existed from 1443-1446 and sat largely unused by the educated for centuries. Literacy rose in the twentieth century with mission and colonial schools, nationalism, and post-1945 campaigns. Credit goes to schools and institutions in every source I read.

**China.** I found no causal estimate for simplification or pinyin and did not read any full text. Context only (abstracts): Weng (2023, *Harvard Journal of Asiatic Studies*, DOI 10.1353/jas.2023.a938222) on the 1935-36 simplification being withdrawn for printing-cost reasons; Kuzuoglu (2022, *Modern Chinese Literature and Culture*, DOI 10.3366/mclc.2022.0003) on the 1920s-30s mass literacy movement and "basic Chinese"; Li (2004, *Written Communication*, DOI 10.1177/0741088303262843) on the "protoliteracy" view. None isolates the script. Gap.

---

## (c) Synthesis

### 1. Drivers the historians name

| Work | Named drivers | Weight given to page conventions |
|---|---|---|
| Clanchy 1993 | royal government, law, landholders' need for documents, a "literate mentality" | index entry "word separation, 130" under "format and layout", and a sentence crediting Irish and Anglo-Saxon monks with developing word separation (sentence and page: NEEDS LIBRARY CHECK); he lists no effect on who could read |
| Stock 1983 | heterodox and reform groups organised around texts | none (0 hits for every term) |
| McKitterick 1989 | Carolingian legislation, schools, church, lay pragmatic literacy | none (0 hits for legibility, punctuation, word division) |
| Graff 1987 | continuity and contradiction; schooling, church, state; the "literacy" and "printing" myths | punctuation and silent reading mentioned as supporting developments |
| Houston 2002 | schooling, church, social and economic need, print as secondary | none |
| Cressy 1980 | "a response to need", schools, religion | none |
| Cipolla 1969 | economic surplus, rulers, Reformation, print | none |
| Eisenstein 1979 | the printing press | punctuation and layout are print-era aids |
| Goody 1986 | writing's institutional effects | none |
| Street 1984 | social practice, not the script ("ideological" model) | Vai example only |
| Scribner and Cole 1981 | schooling vs. practice; Vai script | unspaced, learned informally |
| Havelock 1963 | "supply of readers" by primary schooling | none |
| Harris 1989 | preconditions: cities, schools, cheap copying, state, belief | none reported by reviews |

Silence is the finding on the second question: of ten standard histories, I found word separation indexed or discussed in one (Clanchy, an index entry and one sentence crediting Irish and Anglo-Saxon monks) and silent reading or punctuation mentioned in two others (Graff, Eisenstein). Four of the ten (Stock, McKitterick, Cipolla, Goody) return zero on every spacing or silent-reading term. The OCR caveat applies.

### 2. Timeline against numbers

- **Spacing** (dates for facet A to settle; these are Saenger's, as reported in Part 2 facet E and in the lending scan's contents): Insular scribes seventh and eighth centuries; Continental scribes did not adopt separation "until the mid-tenth century" (Saenger p. 100), and separation was "standard and ubiquitous" by the mid-eleventh century (p. 176 [page to check in a library copy]); reference-reading skills reached the Continent "beginning in the late tenth century" (p. 4); chapter 14, "The Twelfth and Thirteenth Centuries" (p. 243), with the section "The Spread of Canonical Separation" (p. 244).
- **Literacy.** Antiquity, unspaced: Attica 5-10 per cent, Hellenistic high points 20-30 per cent, Roman empire at most 15 per cent (Harris, via Zanker and Sherratt reviews; disputed; the 20-30 per cent for Rhodes is Zanker's report of Harris and is unverified in Harris: see AUDIT_01). England: male illiteracy "around 80%" and female "close to 95%" at Elizabeth's accession in 1558 (Cressy, "a reasonable guess"). Cressy's text also reports "nearly 90%" adult male literacy by 1800 for Scotland (not England; the audit confirmed the neighbouring text is on Scotland).
- **The gap.** Spaced writing was standard on the Continent by the mid-eleventh century (Saenger p. 176 [page to check in a library copy]) and in England well before the Conquest, yet English male literacy was a fifth by 1558. Taking c. 1050 as "the mid-eleventh century", 1558 − 1050 = 508, about five centuries during which the interface was fixed and the rate stayed low. (The earlier "about the year 1000" and "five and a half centuries", 1558 − 1000 = 558, rested on a date that is not Saenger's.) The historians' account of what filled the gap is in the table above: documents for government and landholding (Clanchy), lay schooling and Carolingian reform (McKitterick), Reformation and Counter-Reformation schooling (Houston), economic need (Cressy, Cipolla), print (Cipolla, Eisenstein, qualified by Graff and Houston), and the state (Turkey, Korea).
- **Another gap.** Zanker reports that Harris puts unspaced Rhodes at what England reached in 1580-1700 [unverified: see AUDIT_01; in Harris's own text 20-30% is the male-literacy benchmark for England 1580-1700 and antiquity falls "well below" it]. The inference that an unspaced script is compatible with a literacy rate of 20-30 per cent in a city with schools is withdrawn until Harris is checked.

### 3. Evidence on teaching

- Saenger describes a "syllabary method of presenting text to novice readers" before separation, and says beginners' texts got extra marks; he never shows separation reduced the length of training or the number of people trained. His chapter in Olson and Torrance says separation simplified the reading **process**.
- Cressy documents the Tudor and Stuart pedagogy of basic literacy as a teaching problem solved by schoolmasters.
- Havelock: "reading trauma" imposed at the primary level.
- Scribner and Cole: Vai (unspaced) learned informally in adulthood without long study.
- Seymour et al.: among European orthographies in school, the authors attribute the slower English rate (about 2.5:1 in the body, "more than twice as slow" in the abstract, against the shallow orthographies) to syllabic complexity and orthographic depth; word spacing is not tested.
- **Nobody I found argues that separation lowered the training needed to teach a population to read.** The nearest is Saenger's process claim, which is about speed and ease for readers who already read.

### 4. Cross-script test of "interface change spreads a competence"

The population-scale tests (Turkey, Korea) do not isolate the script from the campaign. In both, the ease of the new script is plausible and cited, and in both the variation in outcomes tracks schooling, state capacity, missions and campaigns. The within-school test (Seymour) shows that orthographic design changes the rate of acquisition, so H-cost has support there; Ziegler et al. (2010) report predictors of reading in Grade 2 in alphabetic scripts, not rates of acquisition, and add nothing on this point. Spacing is a different property from orthographic depth, and none of these studies tests it.

### 5. Verdict on H-cause against H-cost

- **H-cost: supported where the sources speak.** The physiology and efficiency claim (Saenger 1991, 1997) is the only place a source argues a mechanism, and the within-school orthography studies show the principle. Part 2 facet E and the planned facet D hold the experimental reading side.
- **H-cause: not supported by any historian of literacy I could read.** The drivers named are institutions, need, schooling, religion, state and print. Saenger, the strongest candidate, disclaims a literacy history ("not a general history of literacy"), and on p. 11 he lists "the greater diffusion of literacy throughout all social strata of the population" among the "advantages that modern readers perceive as accruing from ease of reading", which the ancients "seldom viewed as advantages"; he attaches this to ease of reading in general, presents it as a modern value, and offers no evidence that spacing raised the number of readers. Nobody credible quoted here argues "ignition".
- **"Necessary-ish enabling condition, not ignition"?** Even "necessary" is hard to support. Unspaced Vai spread informally, and unspaced Greek cities reached 15-30 per cent [unverified: see AUDIT_01]; spaced Hebrew from antiquity did not produce mass literacy. What remains defensible is a narrower enabling claim: spacing plausibly made **fast silent reading of difficult texts by non-native readers** easier, which mattered for scholastic and devotional reading from the twelfth century. That is a claim about a kind of reading, not about who could read.
- **The causal arrow may run backwards.** Part 2 facet E reports Parkes (1992, p. 1) that where Latin was "a foreign language, there was a need for conventions which made it easier to read" (snippet-level). On that account, new learners (the Irish, the English) produced spacing. The facet does not settle it, but a demand-side reading is in the literature, and Saenger's own explanation of ancient absence is demand-side too.

### 6. The most defensible sentence

*Agent-drafted suggestion for the author to accept, revise or discard:*

> Separating words moved some of the work of parsing from the reader to the page, which made fluent silent reading of difficult Latin easier (Saenger 1991); the historians of literacy do not credit it with the spread of reading, which they attribute to schools, religion, administration and commerce, and, later, print.

A tighter fallback: "Word separation lowered a cost of reading; it did not by itself raise the number of readers."

### 7. Claims in the author's framing the sources contradict

1. **"Ignited literacy."** No history of literacy read here credits word separation. Clanchy, Cressy, Houston and Cipolla name administrative, economic, religious and schooling causes; Saenger says his book is "not a general history of literacy".
2. **"Word separation did not train the populace to read *scriptio continua*; it changed the interface so that reading no longer required the training."** (From `draft.md:263`, quoted in the research plan.) Qualified at three points: Vai script is an unspaced syllabary learned informally in adulthood (Scribner and Cole), which does not show whether spacing lowers the cost for learners; where training was heavy, the sources locate it in schooling (Havelock's "reading trauma", Houston, Cressy); spaced scripts (Hebrew, per Saenger's editors) coexisted with restricted literacy.
3. **Timing.** Continental spacing standard by the mid-eleventh century (Saenger p. 176) against English male literacy of about 20 per cent in 1558 (Cressy); mass literacy came in the eighteenth and nineteenth centuries (Houston, Graff).
4. **The interface-change model at population scale.** Hangul (from 1443) and the Turkish alphabet (1928) both show the script alone is not what the sources credit; schools and campaigns are.
5. **The framing "one move".** Not tested here (facet A and the research plan, problem 4), but Graff's and Eisenstein's "printing" and "literacy" myths are exactly the move from one convention to a general cause.
6. **Possibly: "reading as a skill created by the page."** Zieman and Thomas argue that decoding without comprehension was a legitimate kind of literacy in its setting.

---

## (d) Gaps and unverified leads

- **No book was read in full.** Every history of literacy above was queried by search-inside; none was borrowed. A library user should open: Clanchy 1993, ch. on "Writing" around p. 130 and the index entry; Saenger 1997 preface and the passage around "greater diffusion of literacy throughout all social strata"; Saenger's conclusion; McKitterick ch. 1 and the script chapter; Houston ch. 1-2 and the printing chapter; Graff 1987, the Middle Ages chapter near the "silent reading" and "Latin punctuation" hits; Scribner and Cole ch. 3 and the schooling chapters.
- **Printed page numbers** are missing for all snippet quotations. The archive.org full-text API gives scan indices only.
- **Harris, *Ancient Literacy***: no accessible copy; read only through two reviews. Whether Harris discusses interpuncts or word division is unchecked (copy needed from a library or a lending copy).
- **Saenger 1982 (*Viator*) and 1989 (Chartier)**: not accessible. The 1989 chapter's pagination and publisher are unverified. Brepols is bot-walled; the Chartier volume is a library book.
- **Ziegler and Goswami 2005** (paywalled, abstract not retrieved); **Seymour et al. 2003** (now read in full, card).
- **Stock 1983 and McKitterick 1989**: the zero-hit results rely on OCR; the McKitterick scan is 314 pages and Stock's 626, which suggests the OCR covers the book, but I did not verify page counts against the printed books.
- **Eisenstein and Johns**: no full text; relied on search-inside and repo cards that are themselves secondary.
- **Goody, Havelock, Ong**: no new reading beyond snippets and the repo cards; Goody 1986 is TOC-level in the repo and 0-hit here.
- **Zieman 2008**: the criticism of "phonetic literacy" needs the full page (Zieman's introduction) before it carries weight.
- **Turkey and Korea numbers**: the "8 per cent to 20 per cent" (Turkey) and "20 per cent in 1912, 60 per cent in 1940" (Korea, via a review) figures are not verified against census sources. A source for Turkish census literacy (1927, 1935, 1945) and for Korean colonial-period literacy is needed.
- **China**: nothing causal on simplification or pinyin; Rawski (1979) unchecked because OpenAlex rate-limited me.
- **Reviews of Saenger** (Aronoff, Richter, Mulchahey, Hanna, Walker, Baeuml; named in `REUSE.md`): not retrieved; facet B covers them.
- **Anyone arguing ignition?** I found no one credible. Candidates a human could check: later popularisations that cite Saenger; Olson's *The World on Paper* (1994) and Stock's later work are not examined here. A claim in a source I could not open (Saenger 1982) could be stronger than his 1997 disclaimer.
- **Scholar Gateway**: `ACCESS_DENIED`. **OpenAlex**: free daily budget exhausted.

## Changes after full-text cards (2026-10-13)

- `becker2024conquering`: the quotation "Protestantism played a crucial role in the accumulation of human capital" withdrawn (not in the PDF); replaced with the printed abstract's claim; added the Gabo 1886 versus Ivanova 1894 date flag; read status "read in full (card)".
- `clemens2025korea`: the literacy figures are the reviewer's own, unsourced, not the book's; read status "read in full (card)".
- `ivanova2026process`: read status "read in full (card)"; noted that the body's statements on spacing are new to the project and that the card dates the 1894 Kabo reforms and 1886 newspaper.
- `seymour2003foundation`: added the body's "about 2.5:1" ratio, that letter-sound knowledge does not differ, and that the gap sits in word and nonword reading; read status "read in full (card)"; Seymour paragraph and gaps list updated.
- `ziegler2010orthographic`: "same bearing as Seymour" replaced; the paper measures predictors of Grade 2 reading, not acquisition rates, and restricts its claim to alphabetic scripts (p. 557).

Synthesis verdicts changed: one. Old: "The within-school tests (Seymour, Ziegler) show that orthographic design changes the rate of acquisition, so H-cost has support there." New: "The within-school test (Seymour) shows ... so H-cost has support there; Ziegler et al. (2010) report predictors of reading ... not rates of acquisition, and add nothing on this point."
