# K — Training before and after word separation, and every causal claim made from separation

*Audited 2026-10-13 (AUDIT_06.md); WRONG, OVERSTATED and STITCHED rows corrected in place.*

*Facet K, 2026-10-13. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

**What this facet covers.** (1) How readers were taught before word separation (Quintilian, Dionysius of Halicarnassus, the grammarians, school papyri; Cribiore, Marrou, Bonner, Morgan, Johnson). (2) How they were taught after it (Reynolds, Orme, Black, Grendler, Riché, Saenger on novices). (3) Whether any scholar claims, tests or denies that separation shortened, eased or removed the training. (4) A catalogue of every causal claim made from separation to anything else, with its reception. (5) Reverse causation: readers who produced separation. Facets A, B and C hold Saenger's record, the dispute over silent reading, and the historians of literacy; I do not repeat them and cite them by name where I build on them.

**The question the synthesis answers.** Is the absence of a "separation shortened training" claim real or an artefact of where facets B and C looked, and what do scholars actually claim from separation? That tells the author what the sentence at `draft.md:263` can rest on (rulings D1, D2).

**Legend for read status.**
- *Read in full*: whole text read from an open copy (Quintilian 1.1 and 1.8.1–2 in Butler's Loeb translation via Penelope; Roberts's 1910 Dionysius; Davidson's 1874 Thrax, §§1–2). Updated 2026-10-13 from the full-text cards: Quintilian is now *read in part (card)*: 1.1, 1.7, 1.5.6 and 1.8.1–5 read closely; Dionysius is *read in part (card)*: ch. XXV English, pp. 265–270, read; the Demosthenes analysis, pp. 252–264, skimmed; Thrax is *read in part (card)*: §§1–14 and the closing section read, §§15–24 skimmed.
- *Snippet*: read as OCR snippets of about one line (roughly 20 words) returned by the archive.org full-text search (`be-api.us.archive.org/fts/v1/search`) over the borrowable scan named in the entry. I quote only text a snippet shows; where I join two overlapping snippets I say so. The API gives no printed page, so I write "page not available" and give the chapter or section where the snippet shows one. I did not borrow any book. Quotations are normalised for OCR hyphenation and spacing only.
- *Abstract only*, *not accessible*: as in facets A and B.
- *Zero hits (whole-book)*: the API reports a total of 0 for a phrase across the whole scanned book. This is a reliable null for the OCR text (a missed OCR word is possible), so I report it as "no hit for X in the lending scan of Y".

**A note on tool use.** Google Books search-inside and the Google Books API returned zero results or a daily-quota error throughout, so every page locator for a modern book below that is not given comes from facets A–C, or is marked "page not available". I used the Unpaywall API once with an e-mail address that is not the one named in the plan (it is the address in my session context); I did not use it again.

---

## (a) Search log

| # | Source | Exact query | Hits | Notes |
| --- | --- | --- | --- | --- |
| 1 | Penelope (LacusCurtius), Butler's Quintilian | `Thayer/E/Roman/Texts/Quintilian/Institutio_Oratoria/1A*.html`, `1B*`, `1C*` | 3 pages fetched | Read 1.1.15–37 and 1.8.1–2. Perseus's own text URL returned a blank record; Penelope worked |
| 2 | archive.org item `cu31924026465165` | djvu text of Roberts 1910 | full text | Ch. XXV read in the translation; Greek not checked |
| 3 | archive.org item `grammarofdionysi00dionuoft` | djvu text | full text | Davidson 1874, §§1–2 |
| 4 | archive.org FTS, item `gymnasticsofmind0000crib` (Cribiore 2001) | `"word division"`; `"divided into syllables"`; `scriptio continua`; `"word separation"`; `syllabic`; `"bars or dots"`; `"uncertain readers"`; `"lectional signs"`; `Quintilian reading`; `Dionysius Halicarnassus` | 0; 1 each (multi-snippet); `"word division"` 0 | Item is access-restricted to guests, FTS still returns snippets |
| 5 | same, Cribiore 1996 `writingteacherss0000crib` | `"word division"`; `"syllabic division"`; `"divided into syllables"`; `scriptio continua`; `"separation of words"`; ten stitching queries | all > 0 | Section "Syllabic Division, Word Separation, and Verse Distinction" located |
| 6 | same, Marrou `historyofeducati0000marr` | `"word division"`; `"scriptio continua"`; `"not only was there no punctuation"`; `"separated as in our modern primers"` | 0; 1; 1; 1 | Three overlapping snippets stitched |
| 7 | same, Bonner `educationinancie0000bonn` | `"word division"`; `"scriptio continua"`; `praelectio`; `"silent reading"`; `"learning to read"` | 1; 0; 1; 0; 1 | Only a plate caption mentions syllabic word-division |
| 8 | same, Morgan `literateeducatio0000morg` | `"word division"`; `"scriptio continua"`; `"divided into syllables"`; `syllables` | 0; 0; 1; 1 | |
| 9 | same, Johnson 2010 `readersreadingcu0000john` | `"word division"`; `"scriptio continua"`; `Saenger`; `"years of training"`; `Quintilian`; `"emerging readers"` | 1; 1; 1; 0; 1; 1 | Located the "emerging readers" sentence |
| 10 | same, Reynolds 1996 `medievalreadingg0000reyn` | `"word division"`; `"word separation"`; `"scriptio continua"`; `"separation of words"`; `"spacing"`; `Saenger`; `"silent reading"`; `"space between words"` | all 0 | Whole-book null on every separation term |
| 11 | same, Orme 2001 `medievalchildren00orme` and Orme 2006 `medievalschoolsf0000orme` | the same eight queries | all 0 in both | Whole-book null in both books |
| 12 | same, Black 2001 `humanismeducatio0000blac` | same eight | `"word separation"`, `"word division"`, `"scriptio continua"`, `Saenger`: 0; `"silent reading"`: 1; `"spacing"`: 1 (line spacing) | |
| 13 | same, Grendler 1989 `schoolinginrenai0000gren` | same eight | all 0 except `"spacing"` (1, about typography) | |
| 14 | same, Riché 1976 `educationculture0000rich` | `"word separation"`; `"scriptio continua"`; `"spaces between"`; `Saenger` | all 0 | |
| 15 | same, Saenger 1997 `spacebetweenword0000saen` | about 35 phrase queries (novice, syllabary, shortcuts, heresy, erotic, autograph, dictation, scholastic, private devotion, literacy diffusion) | each 1 (multi-snippet) | Snippets only; pages from facets A and C where they gave one |
| 16 | same, Saenger 1982 in `viator_1982_13` (whole volume) | `"word separation" literacy`; `"word separation" beginners`; `"word separation" "foreign language"` | 1; 0; 0 | |
| 17 | same, Parkes 1993 `pauseeffectintro0000park` | 10 queries (foreign language, grammar of legibility, silent reader, ordinatio, learners, Saenger) | `"learners"` 0, `Saenger` 0 | The book does not cite Saenger |
| 18 | same, Cavallo and Chartier `historyofreading0000unse` | `"word separation"`; `"silent reading"`; `"spaces between words"`; `"easier to read"` + 12 stitching queries | all > 0 | Attribution of the passages to the Introduction is mine; see K13 |
| 19 | same, Rouse and Rouse in `renaissancerenew0000unse`; Rouse 1979 `preachersflorile0000rous` | `"word separation"`; `"silent reading"`; `Saenger`; `"scriptio continua"`; `"spacing"` | all 0 | |
| 20 | same, Chartier `orderofbooksread0000char`; Carruthers `bookofmemorystud0000carr`; Stock `listeningfortext00stoc` | `"word separation"`; `Saenger`; `"silent reading"` | 0 for `"word separation"` in all three | Each cites Saenger in notes only |
| 21 | same, reviews in `sim_` periodical scans | Speculum 74(3); AHR 106(2); Canadian J. of History 36(2); Library Quarterly 70(1) and 65(2); Language in Society 31(4); Raritan 20(1); Notes and Queries 47(1) | all returned the review | Snippets only |
| 22 | same, Wagner, Venezky and Street, `literacyinternat0000unse` | `"The History of Reading" Saenger`; `"word separation"`; literacy-diffusion phrases | found Saenger's own chapter | |
| 23 | same, Blake 2002 `literacylearning0000blak`; Baron 2000 `alphabettoemailh00baro_0` | `"word separation"`; `Saenger`; `"spaces between words"` | > 0 | Secondary uses only |
| 24 | archive.org FTS, global (unscoped) | `"word separation" "learning to read"`; `"word separation" "easier to learn to read"`; `"word separation" "spread of literacy"`; `"word separation" "wider literacy"`; `"separation of words" "mass literacy"`; `"Illich" "word separation" Hugh`; `"word separation" "reference reading"`; `"word separation" "private devotion" Saenger` | 623; 1; 175; 10; 91; 70; 54; 59 | Read the top 12 hits of each by title and snippet. None argues that separation shortened teaching. Hits were Saenger, Cavallo and Chartier, Lyons 2010, Blake 2002, Baron 2000, handbooks and school-teaching texts |
| 25 | archive.org `advancedsearch` | titles for about 30 books | identifiers found for all except Mak 2011, Illich 1993 and Bäuml | Illich and Mak: no FTS route |
| 26 | Crossref | 8 DOIs (Hanna, Richter, Walker, Mulchahey, Bäuml, Aronoff, Saenger's Illich review, Gilliard) | 8/8 resolved, titles match | |
| 27 | Crossref bibliographic | Cribiore 1996 and 2001, Reynolds, Johnson | DOIs found: 10.3998/mpub.9749698 (Cribiore 1996, closed on Unpaywall); 10.1515/9781400844418 (Cribiore 2001); 10.1017/cbo9780511470356 (Reynolds); 10.1093/acprof:oso/9780195176407.001.0001 (Johnson) | Morgan 1998: no Crossref hit |
| 28 | WebSearch (2) | Irish scribes and foreign-language learners; Saenger reviews and critique of the causal link | 20 | Popular pages and blogs only; nothing used |
| 29 | Google Books API; `books.google.com/books?jscmd=SearchWithinVolume2` | Saenger `w3vZaFoaa3EC`: `syllabary`, `novice` | 429 quota; `number_of_results: 0` | Not usable this session |
| 30 | Scholar Gateway | not tried | n/a | Failed in every earlier run, per the plan |
| 31 | Unaccessed | JSTOR, Brepols, Cambridge Core for Hanna, Bäuml, Gilliard, Parkes 1976, Rouse and Rouse offprint | not opened | Section (d) |

---

## (b) Entries

### Part 1. Ancient training

#### K1. Quintilian, *Institutio oratoria* 1.1 and 1.8

**quintilian1920institutio** — Quintilian. *The Orator's Education* [*Institutio oratoria*], Book 1. Tr. H. E. Butler (Loeb), Loeb Classical Library, vol. 1 (London: Heinemann; New York: Putnam), 1920. Penelope/LacusCurtius transcription, `penelope.uchicago.edu/Thayer/E/Roman/Texts/Quintilian/Institutio_Oratoria/1A*.html` and `1C*.html`. The Loeb page numbers below are the ones the transcription marks (odd pages carry the English).
- *Verification:* the transcription carries section numbers; I did not check the Latin.
- *Read status:* **read in part (card: library/quintilian1920institutio.md)**: Preface, 1.1 in full (1.1.15–37), the opening of 1.2, 1.5.6, 1.7 in full and 1.8.1–5 read closely; the rest of Book 1 not read.
- *What it says (Butler's words):*
  - 1.1.15: "Some hold that boys should not be taught to read till they are seven years old, that being the earliest age at which they can derive profit from instruction and endure the strain of learning." Quintilian argues against waiting.
  - 1.1.24–26 on method: he disapproves of teaching "the names and order of the letters before their shapes"; "The method, however, to which we have objected in teaching the alphabet, is unobjectionable when applied to syllables."
  - 1.1.30, c. Loeb p. 35: "As regards syllables, no short cut is possible: they must all be learnt, and there is no good in putting off learning the most difficult; this is the general practice, but the sole result is bad spelling."
  - 1.1.32–33, c. p. 37: "You will hardly believe how much reading is delayed by undue haste." "Reading must therefore first be sure, then connected, while it must be kept slow for a considerable time, until practice brings speed unaccompanied by error."
  - 1.1.34, p. 37 (the sentence Heilmann reads as about learners): "For to look to the right, which is regularly taught, and to look ahead depends not so much on precept as on practice; since it is necessary to keep the eyes on what follows while reading out what precedes, with the resulting difficulty that the attention of the mind must be divided, the eyes and voice being differently engaged."
  - 1.8.1–2, Loeb p. 147: "Reading remains for consideration. In this connexion there is much that can only be taught in actual practice, as for instance when the boy should take breath, at what point he should introduce a pause into a line, where the sense ends or begins, when the voice should be raised or lowered, and when he should increase or slacken speed… In this portion of my work I will give but one golden rule: to do all these things, he must understand what he reads."
  - 1.7.17, p. 139: Quintilian rejects an old convention of adding an *e* before *i* in endings because "such a practice will be an actual hindrance to those who are learning to read"; so he judges a spelling convention by whether it hinders learners. His test, "within the limits prescribed by usage," is that "words should be spelt as they are pronounced" (1.7.30–31, p. 145). Chapter 1.7 is about letters, doubling, diphthongs and abbreviations, not the spacing of words.
- *What it does not say:* it contains no word about word division, spacing or the look of the text (1.7 included). The difficulty it names is divided attention between eye and voice, and the reader's job of finding where to breathe and pause. It places the child's slowness in the alphabet-syllable-word sequence, not in the layout. Quintilian gives no length of training in years.
- *Bearing:* **complicates** H-cost. The teaching of reading in Quintilian is a slow, staged drill in syllables, and Quintilian says phrasing and pause "can only be taught in actual practice" (1.8.1; the word *praelectio* is Bonner's, K7, not Quintilian's 1.8.1-2). That is training the reader must do whatever the page looks like. It also shows the aid that exists later (marks for pauses) was a teacher's job in his world, not the page's.

#### K2. Dionysius of Halicarnassus, *De compositione verborum*, ch. 25

**dionysius1910composition** — Dionysius of Halicarnassus. *On Literary Composition, being the Greek text of the De compositione verborum*, ed. and tr. W. Rhys Roberts. London: Macmillan, 1910. Item `cu31924026465165`, archive.org. Chapter XXV, "How prose can resemble verse". Chapter XXV runs from p. 251 to p. 270 in Roberts (card); the Plato tablet story is on pp. 265–267 and the reading passage is on p. 269.
- *Verification:* archive.org metadata; title and editor on the title page of the djvu text.
- *Read status:* **read in part (card: library/dionysius1910composition.md)**: the English of ch. XXV, pp. 265–270, read through to the end of the reading passage and its notes, and the first page of the chapter; pp. 252–264 skimmed. I did not read the Greek.
- *The passage (Roberts's translation, ch. XXV, p. 269):* "When we are taught to read, first we learn off the names of the letters, then their forms and their values, then in due course syllables and their modifications, and finally words and their properties, viz. lengthenings and shortenings, accents, and the like. After acquiring the knowledge of these things, we begin to write and read, syllable by syllable and slowly at first. And when the lapse of a considerable time has implanted the forms of words firmly in our minds, then we deal with them without the least difficulty, and whenever any book is placed in our hands we go through it without stumbling, and with incredible facility and speed."
- *Roberts's note on the passage:* he cites Wilkins's remark that "Some have supposed that Dionysius here describes the method of acquiring the power of reading, not by learning the names of the letters first, but by learning their powers", then rejects it ("hardly consistent with his language") and cites Athenaeus's chant of syllables, and an Attic terracotta school plate "doubtless intended for use in schools, contains a number of syllables".
- *What it does and does not say:* Dionysius uses reading acquisition as an analogy for the trained writer's ease with word-order; he says nothing about word division. What it gives the paper: (i) the Greek sequence letters, forms, values, syllables, words; (ii) "a considerable time" is the cost, and what it buys is fluent, effortless reading of whatever book is handed over. That last point is the same one the physiological critics of Saenger make (facet B, Heilmann): trained readers of unspaced text read fluently.
- *Bearing:* **complicates** the author's sentence at one remove: the ancient sources locate the burden in a long drill that ends in fluency, not in a defect of the page. Not evidence for or against separation lowering the drill.

#### K3. Dionysius Thrax (attributed), *Technē grammatikē*, §§1–2

**thrax1874grammar** — *The Grammar of Dionysios Thrax*, tr. Thomas Davidson, *Journal of Speculative Philosophy* 8 (1874). Item `grammarofdionysi00dionuoft`. The authorship of the *Technē* as we have it is disputed in the scholarship; I did not check that literature and call the work "attributed".
- *Read status:* **read in part (card: library/thrax1874grammar.md)**: headnote and §§1–14 (pp. 3–11) and the closing section read closely; §§15–24 skimmed. Davidson's headnote says the work's authenticity "is now generally admitted" (p. 3); I did not check this against current scholarship, so I still call the work "attributed".
- *Quotation (§2, "On Reading"):* "Reading is the rendering of poetic or prose productions without stumbling or hesitancy. It must be done with due regard to expression, prosody, and pauses… from the pauses, the meaning intended to be conveyed." §1 lists "Trained reading with due regard to Prosody" as the first of the six parts of grammar. Davidson's footnote: "Prosody… includes everything designated by diacritical marks — aspiration, accentuation, quantity, and sometimes pauses."
- *Bearing:* the first part of the ancient grammarian's work is *trained reading* with attention to pauses, so the reader's task of phrasing was taught, as an art, by the grammarian. **Complicates** H-cost; says nothing about separation.

#### K4. Cribiore, *Writing, Teachers, and Students in Graeco-Roman Egypt* (1996)

**cribiore1996writing** — Cribiore, R. (1996). *Writing, Teachers, and Students in Graeco-Roman Egypt*. American Studies in Papyrology 36. Atlanta: Scholars Press. DOI 10.3998/mpub.9749698 (Crossref title: "Writing, Teachers and Students in Graeco-Roman Egypt"; year given as 1995 online; closed on Unpaywall). Lending scan `writingteacherss0000crib`.
- *Verification:* Crossref record; archive.org metadata.
- *Read status:* **snippet**. Section "Syllabic Division, Word Separation, and Verse Distinction" located within ch. 3, "The School Exercises"; printed pages not available.
- *What the snippets say (joined from overlapping windows):*
  - "Besides the syllabaries, many exercises show how the division of words into syllables was [practised]…"
  - "…the division of words into syllables or the separation of words from one another to facilitate reading, will elucidate how students worked and learned…"
  - "Once a student had practiced enough with words divided into syllables, in theory he was ready for more serious and challenging reading. The continuous blocks of writing,…"
  - "…individual words were not separated by spaces—scriptio continua. This feature of ancient writing must…" (cut), and "…distinguish words written in continuous blocks (scriptio continua). According to Quintilian, people usually advised the beginner to keep looking to the right when starting to read…"
  - On Latin: "Although in Latin word division appears regularly until the end of the first century AD,…"; and, of wax tablets, "a transitional stage: a few tablets show interpunct and word division by space".
- *Bearing:* **supports** the point that teachers knew and used the aid for novices: school texts divide words into syllables, or separate words, and teachers move the student on to continuous script ("ready for more serious and challenging reading"). This is the clearest contemporary evidence in this facet that the aid existed in antiquity, was reserved for beginners, and was removed at the next stage of training. I could not see her wording about *why* the continuous text followed, or any claim that it shortened the course.

#### K5. Cribiore, *Gymnastics of the Mind* (2001)

**cribiore2001gymnastics** — Cribiore, R. (2001). *Gymnastics of the Mind: Greek Education in Hellenistic and Roman Egypt*. Princeton: Princeton University Press. DOI 10.1515/9781400844418. Scan `gymnasticsofmind0000crib`.
- *Verification:* Crossref (title matches; Crossref type "edited-book"); archive.org.
- *Read status:* **snippet**; printed pages not available.
- *Snippets (verbatim, normalised):* "Sometimes books addressed the needs of uncertain readers through consistent word separation. Part of a hexameter poem about Hero…" (cut); "exercises at this level show words divided into syllables by means of bars or dots or included in sets according to number of syllables, that is, monosyllables…"; "Since books for beginning readers were not produced on a regular basis, models prepared by teachers fulfilled…" (cut); "teachers' models presented longer excerpts in scriptio continua that addressed relatively advanced students"; "…of letters without word separation (scriptio continua) and without pauses between major sections"; "initial link — the letters of the alphabet — that led to syllables, words, and sentences"; "the effectiveness of building on syllables to teach reading and writing properly was not questioned throughout…" (cut). On Dionysius: "the first century b.c.e., the writer Dionysius of Halicarnassus, for instance, says that it was…" (cut).
- *Bearing:* **supports**. Books for the uncertain reader carried "consistent word separation", exercises for beginners divided words into syllables, and the advanced student's models were in *scriptio continua*. Ancient teachers matched the page to the learner's stage. This is the strongest source here for a design precedent in antiquity itself, and it cuts against "ignited": the aid was known and was deliberately withdrawn.

#### K6. Marrou, *A History of Education in Antiquity*

**marrou1956history** — Marrou, H.-I. (1956). *A History of Education in Antiquity*. Tr. G. Lamb. New York: Sheed and Ward (many reprints; the scan I searched is `historyofeducati0000marr`, a later reprint whose year and pagination I did not capture).
- *Read status:* **snippet**; printed page not available. Locator: chapter on the Hellenistic school, section "The Reading Lesson — The Alphabet — The Syllables — Words — Texts and Anthologies" (contents snippet).
- *Snippets, joined from three overlapping windows (the join is mine):* "It was not so easy for the child to read these as it is for our modern child today, because the Greeks used a scriptio continua in which not only was there no punctuation but even the words themselves were not separated from each other." On syllables: "the syllables separated as in our modern primers". Elsewhere: "manuscripts we possess, were always in scriptio continua."
- *Bearing:* **supports** a one-line claim that scriptio continua made the child's reading harder, with no evidence offered in the snippets. This is the nearest I found, in a standard history of education, to the author's intuition; it is an assertion about *difficulty for the child*, not about training length or the number of readers. I could not tell what "these" refers to.

#### K7. Bonner, *Education in Ancient Rome*

**bonner1977education** — Bonner, S. F. (1977). *Education in Ancient Rome: From the Elder Cato to the Younger Pliny*. London: Methuen; Berkeley: University of California Press. Scan `educationinancie0000bonn`.
- *Read status:* **snippet**; printed page not available.
- *Snippets:* a plate caption, "Section of teaching manual, showing syllabic word-division (third-century B.C. papyrus, MS 65445, Cairo Museum)"; "orderly progression from letters to syllables, and from syllables to words, and from words to sentences"; "a praelectio, or 'preliminary reading'" with "the most essential [part]…" cut. On Roman children learning Greek: "This must have presented at first a formidable obstacle, and even children learning to read in their own language needed some initial…" (the "obstacle" is Greek as a second language, not script layout).
- *Bearing:* **supports** the existence of the aid in a third-century BC school manual. No hit for `scriptio continua`, `silent reading` or `"separate the words"`.

#### K8. Morgan, *Literate Education in the Hellenistic and Roman Worlds*

**morgan1998literate** — Morgan, T. (1998). *Literate Education in the Hellenistic and Roman Worlds*. Cambridge: Cambridge University Press. Scan `literateeducatio0000morg`.
- *Read status:* **snippet**; printed page not available.
- *Snippets:* "four-syllable names beginning with 'E', divided into syllables to make them easier to read" (a school text); "…with learning letters, syllables and words, though there is no direct evidence" (cut); Quintilian quoted: "There is no short-cut to syllables: they must all be learned thor[oughly]".
- *Bearing:* **supports** K4 and K5 on one point: syllable division was a school device "to make them easier to read". No hit for `"word division"` or `scriptio continua`.

#### K9. Johnson, *Readers and Reading Culture in the High Roman Empire* (2010)

**johnson2010readers** (key reused; facet B) — Johnson, W. A. (2010). *Readers and Reading Culture in the High Roman Empire: A Study of Elite Communities*. Oxford: Oxford University Press. DOI 10.1093/acprof:oso/9780195176407.001.0001 (Crossref title matches). Scan `readersreadingcu0000john`.
- *Read status:* **snippet**; chapter 1 area, printed page not available. Facet B read only reviews of this book.
- *Snippets (joined from overlapping windows; the join is mine):* "Greeks and Romans knew perfectly well, for instance, the utility of word division—the Greek school texts on papyri bear eloquent testimony to the need for emerging readers to practice syllable and word division." Also: "…word division was discarded by the Romans in deference to Greek aesthetic and cultural traditions"; "…necessitating years of advanced study to fully apprehend." (the closing mark in the OCR is probably note 39; the words are Johnson's own, per the auditor); "The upshot of all this is that the bookroll culture in the high empire was one designedly reserved for elite of a certain stripe, able and willing…" (cut); "Strict functionality, clearly, is not a priority in bookroll design."
- *Bearing:* **supports** the "known and reserved for novices" point from a classicist who rejects Saenger's physiology. It adds the other half: for the elite, the training was the point. Johnson reads the cost of unspaced script as a social filter, not a defect. **Complicates** the author's sentence: if the training was designed to exclude, removing it is a change in who may enter, a claim about the elite's choice, not an accident of interface.

---

### Part 2. Training after separation

#### K10. Reynolds, *Medieval Reading* (1996)

**reynolds1996medieval** — Reynolds, S. (1996). *Medieval Reading: Grammar, Rhetoric and the Classical Text*. Cambridge Studies in Medieval Literature 27. Cambridge: Cambridge University Press. DOI 10.1017/cbo9780511470356 (Crossref title "Medieval Reading"). Scan `medievalreadingg0000reyn`.
- *Read status:* **snippet**; chapter 1 ("Learning to read: the classics and the curriculum"), printed pages not available.
- *Snippets:* "In other words, even at its very earliest stages, learning to read 'means learning to read a foreign language. This has the most profound effect on the reading practice I analyse in this book" (the OCR shows the closing quotation mark misplaced); "crucial to realise that the alphabet the puer learns is not the alphabet of the mother-tongue"; "Sometimes the Psalter itself was used to teach the syllables"; "the most common way to learn the alphabet, the syllables and the paternoster". On the glossator: "Glosses like this take the place of punctuation… It is the lack of punctuation in the manuscript text that causes the glossator [to…]" (cut).
- *Zero hits (whole-book):* `"word separation"`, `"word division"`, `"scriptio continua"`, `"separation of words"`, `"spacing"`, `Saenger`, `"silent reading"`, `"space between words"`.
- *Bearing:* **complicates** the author's sentence strongly. In the standard book on how medieval readers learned, the training is an alphabet, syllables, psalter, Donatus course in a foreign language, and the book's account of medieval reading never mentions word separation. For the Insular case it agrees with Parkes: the demand came first (learners of a foreign tongue).

#### K11. Orme, *Medieval Children* (2001) and *Medieval Schools* (2006)

**orme2001medieval** — Orme, N. (2001). *Medieval Children*. New Haven: Yale University Press. Scan `medievalchildren00orme`. **orme2006medievalschools** — Orme, N. (2006). *Medieval Schools: From Roman Britain to Renaissance England*. New Haven: Yale University Press. Scan `medievalschoolsf0000orme`.
- *Read status:* **snippet**; printed pages not available (ch. 7 "Learning to Read" in the first; the Anglo-Saxon chapter of the second).
- *Snippets:* Orme 2001: "children learning to read were made to decipher the Paternoster as their first piece of…" (cut); "Grammars had to be written that taught Latin as a foreign language, unlike Roman grammars which assumed an understanding…"; a chapter section "Learning Syllables". Orme 2006: "For many, learning to read must have involved learning Latin as a foreign language, making it difficult to pick up such knowledge informally"; "The alphabet of letters learnt in Anglo-Saxon England was the Latin alphabet"; "Once pupils could read words and sentences, they could learn Latin texts".
- *Zero hits (whole-book), both books:* `"word separation"`, `"word division"`, `"scriptio continua"`, `"separation of words"`, `"spacing"`, `Saenger`, `"silent reading"`, `"space between words"`.
- *Bearing:* **complicates**. Same pattern as Reynolds: the burden is Latin, and the sequence is alphabet, prayers, syllables. The authority on medieval children's schooling never mentions separation.

#### K12. Black, Grendler, Riché

**black2001humanism** — Black, R. (2001). *Humanism and Education in Medieval and Renaissance Italy*. Cambridge: Cambridge University Press. Scan `humanismeducatio0000blac`. **grendler1989schooling** — Grendler, P. F. (1989). *Schooling in Renaissance Italy: Literacy and Learning, 1300–1600*. Baltimore: Johns Hopkins University Press. Scan `schoolinginrenai0000gren`. **riche1976education** — Riché, P. (1976). *Education and Culture in the Barbarian West, Sixth through Eighth Centuries*. Tr. J. J. Contreni. Columbia: University of South Carolina Press. Scan `educationculture0000rich`.
- *Read status:* **snippet**; printed pages not available.
- *Black snippets:* "The introduction to reading by learning the alphabet and then syllables was a technique going back [to antiquity]" (cut); "earlier middle ages, too, children began with the alphabet and proceeded to syllables: as Remigius of Auxerre…" (cut); "standard reading syllabus of carta/tabula, psalter and Donatus"; "silent reading of pupil-owned copies" in a late medieval Italian classroom (from Bonvesin).
- *Grendler snippets:* "pages of syllables, the good scholar was ready to read words composed of two two-letter syllables"; "the alphabet… the Pater Noster, Ave Maria, Symbolum"; "First, the pupils read aloud and learn the alphabet. Next, they begin to join…".
- *Riché snippets:* "First, letters and syllables, then the 'eight parts of speech'"; "old he learned the notae litterarum—that is, the alphabet—at home".
- *Zero hits (whole-book):* for `"word separation"`, `"scriptio continua"` in all three; Black and Grendler also have none for `Saenger`. Riché also none for `Saenger` (the book predates him).
- *Bearing:* **complicates** and **refutes** the "no longer required the training" reading for the period after separation: Italian schools from the fourteenth to the sixteenth centuries, long after canonical separation, still taught the alphabet, syllable pages, psalter and Donatus in sequence, and Black says that method goes back to antiquity. The instruction did not change shape when the page changed.

#### K13. Saenger on novices (1997; 1999 chapter)

**saenger1997space** (key reused; facets A–C) — Saenger, P. (1997). *Space Between Words: The Origins of Silent Reading*. Stanford: Stanford University Press. Scan `spacebetweenword0000saen`.
- *Read status:* **snippet** (this facet); facets A and C hold earlier snippets and the page checks.
- *On novices and the syllabary method (ch. 1; Blake 2002 cites the passage as "Saenger 1997, 4, 5, 6"; the auditor found this sentence is about Japanese kana, p. 3, not Greek or Latin teaching; on p. 6 Saenger says young children "tend initially to write in scriptura continua"):* "The exclusive use of a syllabary method of presenting text to novice readers, necessitating the oral reconstruction of units of meaning from phonetic components…"; Also, in the same area, a fragment on "conditions for rapid lexical access" that "allows Chinese children to develop silent reading at an earlier age". I could see only these fragments and cannot state his full argument for the chapter.
- *The nearest sentence to the author's:* "Word separation, the diastole, the hyphen, and eventually the trait d'union in Insular books provided shortcuts for achieving the reading skills that an elite among the ancients had mastered only through a prolonged and arduous grammatical apprenticeship." (p. 85, confirmed by the auditor). It is a list: word separation is one of four devices, the other three being marks. It names *Insular books* and the reading skills of an elite; Saenger's learner argument is on p. 91. It is Saenger's own claim that the aid replaced the elite's apprenticeship with a shortcut. He gives it without a measure of time or numbers. A second Anglo-Saxon grammarian (Bede) follows in the next sentence.
- *Also (p. 13 per facet A, wording confirmed here):* "As a consequence, even readers of modest intellectual capacity could read more swiftly…"
- *Explicit disclaimers:* the book "is not a general history of literacy" (facet A, p. x; wording confirmed in my snippet: "which, I would stress, is not a general history of literacy. Instead, I have attempted to explain the physiological…"). On p. 11 (facet A) he lists "the greater diffusion of literacy throughout all social strata of the population" among the benefits modern readers see in ease of reading; my snippet confirms the wording.
- *Bearing:* **supports** H-cost in its narrowest form (Insular books, an elite's reading skills, a prolonged apprenticeship shortened) and **does not support** H-cause for literacy. Note it is the one passage in the corpus that says the apprenticeship was shortened. It is a claim without a test.

**saenger1999history** — Saenger, P. (1999). The history of reading. In D. A. Wagner, R. L. Venezky and B. V. Street (Eds.), *Literacy: An International Handbook* (Boulder, CO: Westview Press), ch. 2, starting p. 11 (contents snippet, OCR garbled; end page not seen). Scan `literacyinternat0000unse`. Not in the repo bib.
- *Verification:* the contents list in the scan shows "2 The History of Reading, Paul Saenger"; the chapter's opening matches.
- *Read status:* **snippet**.
- *Snippets (the key ones):* "The history of written communication in the West may be divided [into…]" and "first comprises the discipline of the history of reading, the second constitutes the history of literacy. The history of reading deals with the qualitative question of how people…" (cut); "The history of literacy is concerned with quantitative questions relating to the diffusion of these various reading skills to different strata of society." And: "…after 1200 constitute events more important for the history of literacy than for the history of reading and are thus marginal [to this chapter]"; "questions of social class and gender, central to the history of literacy, are of only marginal import to [it]" (the closing words are cut). On the twelfth century: "the far more legible and visually perfected written Latin language of the twelfth century was a second language to readers…" (cut). Also: "Totally silent reading, without movement of the tongue and…".
- *Bearing:* **the single most useful sentence for Q3.** In 1999 Saenger himself separates the history of reading (how people read) from the history of literacy (the diffusion of reading skills to strata of society), says his chapter is about the first, and treats class and gender as marginal to it. He therefore does not claim that separation spread literacy. **Refutes H-cause as a claim of Saenger's.**

#### K14. Parkes, *Pause and Effect* (1992/1993)

**parkes1992pause** (key reused; facet A). Lending scan `pauseeffectintro0000park` (the University of California Press edition, 1993).
- *Read status:* **snippet**; facet A holds earlier snippets and the chapter pages (ch. 2, pp. 20–29; ch. 3, pp. 30–34).
- *This session, verbatim:* "Because many had to learn Latin as a foreign language, there was a need for conventions which made it easier to read. Over the centuries these…" (cut); "New conventions, such as word separation, features of layout and punctuation, were developed to make it easier for readers to extract the information conveyed in the written medium"; "The Anglo-Saxons learned the practices of word-separation, layout and punctuation from Irish teachers"; "…words as pattern-units, in order to speed the eye of the reader from one letter to the next within a word"; "Texts were mostly read aloud." Of the sixth century on: "attitudes… Isidore of Seville (c. 560–636) could state a preference for silent reading".
- *Zero hits:* `Saenger`, `"learners"`.
- *Bearing:* Parkes gives a **cause running from readers to script** (many had to learn Latin as a foreign language, hence the need for conventions) and the effect as ease of reading. He names no literacy outcome and never cites Saenger. **Supports** H-cost; **opposes** the author's direction (page → reader) only in the sense that the readers came first.

---

### Part 3. Causal claims from separation, and their reception

#### K15. Saenger 1982 (*Viator* 13) and 1997: the claims

**saenger1982silent** (key reused) — the whole of *Viator* 13 (1982) is in the scan `viator_1982_13`; it is access-restricted but FTS returns snippets. Facet A could not open the article; I read snippets only.
- *Read status:* **snippet**; article pp. 367–414; per-snippet pages not available.
- *Snippets:* "…the reduced paravoleal vision which resulted from lack of word separation. The introduction of word separation in the seventh century permitted fewer and longer saccades" (physiological claim; the part Vatri and Heilmann reject; facet B); "…ruling class, literate in a script without word separation, had no clear images of words correctly spelled…"; "…writing, and revising Roman scripts without word separation made autograph composition slow and tedious".

The catalogue of claims in 1997 (each quote from my snippets of `spacebetweenword0000saen`; "page not available" unless a page is from facet A):

| Claim from separation to… | Wording | Evidence offered | Reception |
| --- | --- | --- | --- |
| Silent, rapid reading | Reviewers' form, not Saenger's: see K16. Saenger: "even readers of modest intellectual capacity could read more swiftly" (p. 13, facet A) | The physiology of reading, manuscripts | Contested: Knox (silent reading attested long before any spacing; he never mentions word separation or the training of readers, so he bears on the silent-reading half only), Vatri, Heilmann (facet B); O'Donnell (2000, ¶3): "some will dissent from … his claim that the textual practices he observes were the necessary and sufficient condition of the rise of silent reading", and the stretch from the physiology chapter to the theory is "the most venturesome and vulnerable part of the book" (¶4); Cavallo and Chartier (K17) |
| Reference reading and the scholastic book | "thoughts, which without these tools would not have been possible" (cf. facet A, p. 122); "Separated script was an indispensable medium for this new learning" (page not available); "use, implying the scanning of text, would not have been possible in aerated script" | Manuscript layout and page apparatus, twelfth to thirteenth centuries | Claimed, not tested by any reviewer I could read; Rouse and Rouse explain the apparatus without separation (K18) |
| Private devotion | "…prayers in the first-person singular intended for intense private devotion; no equivalent can be found in unseparated [books]" (page not available) | Insular prayer books | No reviewer I could read comments on this link |
| Heresy and censorship | Section heading "Private Study and Heresy" (contents, p. 264); "Already in the eleventh century, heresy was linked to solitary intellectual curiosity and speculation"; "The transition to silent reading and composition, by providing a new dimension of privacy…" (cut); "In England, the mere possession of Lollard writings was legal grounds for formal charges of heresy" | Cases (Berengar of Tours, Lollards) | Not tested by any reviewer I could read; the Raritan reviewer (K16) objects to the "relentless teleology" of the whole |
| Authorship and autograph composition | "authors had generally composed by dictation to a scribe, in large measure because of the difficulty of composing while writing in [scriptura continua]"; Guibert of Nogent wrote on parchment "because of the lack of privacy when composition depended upon dictation to a secretary" | Authors' own manuscripts (Richer of Reims's autograph corrections) | Not tested |
| Erotic and private reading | "Private reading stimulated a revival of the antique genre of erotic art" | Decoration in books, Guibert and Odo of Orléans | Not tested |
| Vernacular reading | Section "Lay Society and Vernacular Texts" (contents, p. 265); "…the same practice of silent reading and composition for vernacular literary texts that…" (cut) | Vernacular manuscripts | Hanna notes the vernacular lag (K16); Richter (K16) |
| Literacy diffusion | None. p. 11 lists it as a *modern* advantage; 1999 chapter assigns it to a different history (K13) | n/a | n/a |

#### K16. Reviews of Saenger 1997 (reachable at snippet depth)

Facet B opened O'Donnell (TMR 2000) and Garrett (1998) in full and Aronoff's abstract. Below, the reviews I could reach through scans of the journal issues. Printed review pages come from Crossref.

**hanna1999saenger** — Hanna, R. (1999). Review. *Speculum* 74(3), 830–831. DOI 10.2307/2886848 (Crossref title matches). Scan `sim_speculum_1999-07_74_3`. **Snippet.**
- "While there is much in *Space between Words* that will be of great interest to students of late Caroline books and their…" (cut). "Saenger argues that the distance between Latin and the Celtic and Germanic vernaculars…" (cut). "Saenger argues that, not only is word division native-tongue-determined, it may also reflect other features of…" (cut). "While Saenger carefully describes a revolution that would underlie such a Derridean…" (cut). "Chapters 8–9, for example, examine the proliferation of word separation as linked with specific authors (Gerbert, Abbo, Heriger), their texts, and their…" (cut).
- *Bearing:* Hanna reports Saenger's Insular-learner explanation as an argument. I could not see whether she accepts it, or what her objection is.

**richter2001saenger** — Richter, M. (2001). Review. *American Historical Review* 106(2), 627–628. DOI 10.1086/ahr/106.2.627. Scan `sim_american-historical-review_2001-04_106_2`. **Snippet.**
- "…Saenger, generally sober and rather understated, calls this the 'great divide' (p. 12) and 'a revolution' (p. 48). The practice began in those countries that had received Latin as a foreign language. Pride of place goes here to Ireland, the first Western country to adopt…"
- "But it took more than half a millennium before space between words found acceptance in the Romania rather than the traditional scriptura continua. Saenger suggests convincingly that this was due to the relatively greater familiarity there with the Latin language…" (cut).
- *Bearing:* **a reviewer who endorses the reverse cause** ("convincingly"): separation took hold where Latin was foreign and lagged where it was familiar. He notes the half-millennium.

**mulchahey2001saenger** — Mulchahey, M. M. (2001). Review. *Canadian Journal of History* 36(2), 323–325. DOI 10.3138/cjh.36.2.323. Scan `sim_canadian-journal-of-history_2001-08_36_2`. **Snippet.**
- "Saenger is convinced, however, that the critical juncture in the history of reading in the Latin West came earlier, when medieval scribes began to make concessions to the reader in the form of visual cues such as punctuation and word separation which greatly aided the mental recognition of words and units of meaning." "Thus, as a minor premise, the emergence of proper word separation over the course of the medieval period was likely the single most important factor enhancing readers' ability to comprehend written text rapidly and silently." "Saenger's book is impressive for the sheer weight of archival research that lies behind it." Her close: "…alike a very great service, in teaching us how to read the *Space Between Words*."
- *Bearing:* a summary in her own words ("as a minor premise… likely the single most important factor"); she does not dissent. Reception: positive, not tested.

**walker2000saenger** — Walker, T. D. (2000). Review. *The Library Quarterly* 70(1), 166–167. DOI 10.1086/603182. Scan `sim_library-quarterly_2000-01_70_1`. **Snippet.** "[The] thrust of his work is that the introduction of word separation led to the development of silent reading during the Middle Ages." Descriptive; "a textbook for this specialized field" of the chapters on the nomenclature of word separation. No evaluation of the causal claim.

**aronoff2002saenger** — Aronoff, M. (2002). Review. *Language in Society* 31(4), 624–628. DOI 10.1017/s0047404502254056. Scan `sim_language-in-society_2002-09_31_4`. **Snippet** (facet B had the abstract only).
- "…more plausible) reason that S gives for why word separation might have begun in the British Isles is that Latin was a foreign language for its Irish and British learners." (the opening of the sentence is cut)
- "Word separation is the simplest device for ensuring quick recognition of words in succession, while…"; "…easily lend themselves more readily to rapid silent comprehension"; "The level of detail in this core half of the book is truly remarkable." Abstract (facet B): "impressive, fascinating, and exasperating".
- *Bearing:* a linguist calls the learner explanation "plausible" and, in the part visible, accepts the speed claim as ordinary psycholinguistics. I did not see the "exasperating" passage.

**raritan2000review** — Review essay on Saenger, Manguel and Johns (author not identified), *Raritan* 20(1) (Summer 2000), review of Saenger at p. 105 per the issue contents. Scan `sim_raritan_summer-2000_20_1`. **Snippet.** "Nonetheless, I am put off by the relentless teleology of *Space Between Words*. Like Eric Havelock, who similarly argued long ago for the progressive development of writing and its attendant [effects]…" (cut); "If Saenger's claims are right, then (much like Johns) he has produced an argument about the origins of…" (cut). Also: "exclusively a story of Latin text production Saenger tells— made possible the quicker, silent, and, in turn, more private apprehension of the written word."
- *Bearing:* the clearest reviewer objection I found to the *form* of the causal claim (teleology). Author unnamed; citable only after a person identifies him or her.

**nq2000saenger** — Review in *Notes and Queries* 47(1) (March 2000), reviewer unnamed in my snippets. Scan `sim_notes-and-queries_2000-03_47_1`. **Snippet.** Descriptive: "Saenger shows that word separation was pioneered by non-romance cultures"; "appear to have been won over by the advantages of word separation until much later". No dissent in the snippets.

**Not reached:** Bäuml 2002 (*Written Language & Literacy* 5(1), 131–134, DOI 10.1075/wll.5.1.08bau, verified at Crossref), Lyons 2001, the *Choice* note, any review by Ganz or Brown (I found none under those names). Section (d).

#### K17. Cavallo and Chartier (eds.), *A History of Reading in the West* (1999)

**cavallo1999history** (key reused; facet A). Scans `historyofreading0000unse` and `historyofreading0000cava`.
- *Read status:* **snippet**; the sentences below are from the volume's opening survey; I could not confirm from snippets which editor wrote them or the page, so I attribute them to "the editors' Introduction (to be confirmed)". The two passages on antiquity quoted below ("absence of breaks" and "sonorization") are Jesper Svenbro's, ch. 1, pp. 51-52 (AUDIT_06).
- *Verbatim (joined from overlapping windows):* "The first is the line, where in the early Middle Ages, the appearance of word separation made silent reading possible. The next is the page, which underwent two transformations: in the fourteenth and fifteenth centuries…" (cut). On antiquity (Svenbro, not the editors): "The absence of breaks in the written line was indeed a hindrance to silent reading, and it remained so. It was not an insurmountable obstacle, however, as we can surmise…" (cut); Svenbro's next sentence cites Saenger: "According to Paul Saenger, in the Middle Ages word division was a necessary condition for the dissemination of the practice of silent reading". And (Svenbro): "…sonorization of writing was negatively programmed by the absence of spaces between words, and since sonorization was valued as a good in itself, why should anyone feel the need to abandon the scriptio continua that was a technical impediment to the…" (cut).
- *Bearing:* book historians state the claim *separation made silent reading possible* flatly, then Svenbro (ch. 1) qualifies it for antiquity ("not an insurmountable obstacle"), while citing Saenger for word division as "a necessary condition for the dissemination of the practice of silent reading", and gives a social reason for not abandoning *scriptio continua*. The line, then the page: separation is the first of a chain of layout changes, which supports problem 4 (a bundle). No literacy claim in the snippets.

#### K18. The apparatus of the scholastic book: Rouse and Rouse, Parkes 1976, Illich, Chartier, Carruthers, Mak

**rouse1982statim** (key reused; marked "not accessible" in the repo bib because of an earlier run; I now have snippets) — Rouse, R. H. and Rouse, M. A. (1982). *Statim invenire*: Schools, preachers, and new attitudes to the page. In R. L. Benson and G. Constable (Eds.), *Renaissance and Renewal in the Twelfth Century* (Cambridge, MA: Harvard University Press), pp. 201–225 (the contents snippet gives p. 201; the end page is from the running heads). Scan of the volume `renaissancerenew0000unse`.
- *Read status:* **snippet**.
- *Snippets:* the title page: "Statim invenire: Schools, Preachers, and New Attitudes to the Page"; "a reader facing a book of eight hundred pages might well be grateful"; "…'STATIM INVENIRE' direct ancestor of all later alphabetical…"; a note citing Parkes's "The influence of the concepts of *ordinatio* and *compilatio* on the development of the book".
- *Zero hits (whole volume):* `"word separation"`, `Saenger`, `"silent reading"`, `"scriptio continua"`, `"spacing"`. One hit for `"separation of words"`, about hyperbaton.
- *Bearing:* **the standard account of the twelfth-century reference apparatus does not use word separation as a cause.** The title gives the cause as schools, preachers and new attitudes to the page. So the Rouses and Saenger stand side by side: Saenger claims separation was necessary for the apparatus (K15), the Rouses explain the apparatus by the readers' need to find things quickly and do not mention separation. No scholar I read adjudicates between them.

**Parkes 1976 (*ordinatio* and *compilatio*)** — cited in the Rouses' note and in *Pause and Effect* (hits in K14). Not opened. In *Pause and Effect* the snippet ties scholastic readers' needs to punctuation: "In these circumstances scholastic readers needed to identify the boundaries of…" (cut); "The habits of scholastic authors also influenced the use of punctuation". **Not accessible** as an article: *Medieval Learning and Literature: Essays Presented to Richard William Hunt* (Oxford: Clarendon Press, 1976), pp. 115–141; page range from memory, unverified.

**illich1993vineyard** (key reused) — Illich, I. (1993). *In the Vineyard of the Text: A Commentary to Hugh's* Didascalicon. Chicago: University of Chicago Press. **Not accessible** (no FTS route). What I know is Saenger's review: **saenger1995illich** — Saenger, P. (1995). Review of Illich. *The Library Quarterly* 65(2), 244–246. DOI 10.1086/602782 (Crossref title matches). Scan `sim_library-quarterly_1995-04_65_2`. **Snippet.** "…his thesis is clearly that Hugh of Saint Victor represented the crucial change from the oral reader mentality that had originated…"; "However, his assertion that the change to visual silent reading was occurring precisely during the period when Hugh composed and revised his *Didascalicon*…" (cut); "…to skim the written page, a practice only possible due to the word separation that was standard in twelfth-century Parisian…"; "In fact the canonical word separation necessary for silent reading (superbly illustrated by Illich's dust jacket reproduced…" (cut).
- *Bearing:* Saenger, reviewing Illich in 1995, supplies the missing mechanism himself ("a practice only possible due to the word separation"). Illich's claim as the reviewer reports it is about the date of the shift to visual reading; the separation link is Saenger's gloss. I cannot say what Illich wrote on separation.

**chartier1994order**, **carruthers2008book**: scans `orderofbooksread0000char` and `bookofmemorystud0000carr`. **Snippet.** Chartier, *The Order of Books* (1994): no hit for `"word separation"` or `scriptio continua`; notes cite Saenger on silent reading in "Communities of Readers". Carruthers, *The Book of Memory* (2nd ed., 2008): no hit for `"word separation"` or `scriptio continua`; one note reads "for earliest medieval uses of word spacing see especially Saenger, *Space Between Words*, and Parkes, *Pause and Effect*". Neither builds an argument on separation. **Mak 2011** (**mak2011page**): **not accessible**; not on archive.org, Google Books quota-blocked. Stock 1983 and 1990: `listeningfortext00stoc` returns no hit for `"word separation"` (facet C had Stock 1983 at part depth).

#### K19. Later uses

**blake2002literacy** — Blake, B. E. (2002). *Literacy and Learning: A Reference Handbook*. Santa Barbara: ABC-CLIO. Scan `literacylearning0000blak`. **Snippet.** A school-literacy handbook with a chapter "How We First Read: Texts with No Word Separation". "It is hard to imagine that the…" and "Why did it take so long for writers to make reading easier by leaving spaces between words?" Cites Saenger 1997, pp. 2, 4–6 on how children learn to read in Chinese, Burmese, and with recitation as "an important part of elementary reading instruction". **Bearing:** the one place in the corpus that moves Saenger's ease-of-reading argument into a book about teaching reading. It is a reference handbook for teachers. It repeats Saenger and adds no evidence.

**baron2000alphabet** — Baron, N. S. (2000). *Alphabet to Email: How Written English Evolved and Where It's Heading*. London: Routledge. Scan `alphabettoemailh00baro_0`. **Snippet.** Two separate snippets: "spaces between words when copying original Latin texts, making it visually easier to make out both the lexicon and grammar", and "copying texts in Irish (that is, their native tongue), they didn't introduce word separation, but grouped words…" (cut). The auditor found the two snippets are adjacent sentences: Insular (Irish) scribes introduced spaces when copying Latin; copying texts in Irish, their native tongue, they grouped words by stress or phrasing instead. Also "The evolutionary process was slow." **Supports** the learner-first direction from a linguist reading Saenger.

**lyons2010history**: Lyons, M. (2010). *A History of Reading and Writing in the Western World*. Basingstoke: Palgrave Macmillan. Scan `historyofreading0000lyon`. **Snippet.** Section "Word separation and silent reading": "from the seventh century onwards, according to Paul Saenger, the separation of words significantly assisted…" (cut); "But by the twelfth century, word separation was universal in Europe". Secondary summary; no new evidence.

---

## (c) Synthesis

### Q1. Training before separation

The sources agree on the sequence. Dionysius: letters, forms, values, syllables, words, "syllable by syllable and slowly at first" (ch. XXV). Quintilian 1.1.30–33 says syllables cannot be shortcut and reading "must be kept slow for a considerable time" before speed arrives. Bonner and Marrou both describe a syllable stage. None gives a length for learning to read alone; Cribiore (2001, p. 171) speaks of "one or two years of elementary instruction" for many students. Quintilian argues for starting before seven (1.1.15-20).

Two points matter for the author's sentence.

1. **The aid existed and was kept for novices.** Cribiore (1996) describes school exercises in which words are divided into syllables, "or the separation of words from one another" is used "to facilitate reading"; for higher-level texts she lists "separation of words by spaces or bars" among the features that mark a text as meant for students (p. 72). Cribiore (2001) describes syllable division "by means of bars or dots". Cribiore (1996, p. 48) writes that once a student had practiced with words divided into syllables, "in theory he was ready for more serious and challenging reading", but that "the continuous blocks of writing, however, made word divisions necessary as a further aid for the pupil" until accents could take over. Cribiore (2001) reports "consistent word separation" for "uncertain readers" and says teachers copied short excerpts of Isocrates "with words and syllables separated for students who were learning to read", while "some teachers' models presented longer excerpts in scriptio continua that addressed relatively advanced students". Bonner's plate caption shows "syllabic word-division" in a third-century BC manual. Johnson (2010, p. 20) writes that "the Greek school texts on papyri bear eloquent testimony to the need for emerging readers to practice syllable and word division." Teachers divided syllables, and sometimes words, for novices; syllable division gave way to ordinary texts, and Cribiore (1996, p. 48) has word division continuing as a further aid until accents replaced it.
2. **The unspaced text was the end of training, not its obstacle (my inference).** Dionysius, using reading as an analogy for composition, says that after "a considerable time" we go through "any book" "with incredible facility and speed"; he says nothing about word division. Johnson describes a literature "itself challenging, in many prominent cases necessitating years of advanced study to fully apprehend", and concludes that "the bookroll culture in the high empire was one designedly reserved for elite of a certain stripe" (2010, p. 31). Marrou is the plainest source here on the child's difficulty with *scriptio continua*: "It was not so easy for the child to read these as it is for our modern child today", because of *scriptio continua* ("these" are the ordinary texts that followed passages split into syllables); Cribiore (1996, p. 48) says the continuous blocks made word division "necessary as a further aid for the pupil".

Thrax's "trained reading" shows that part of the burden was teaching phrasing and pause, which Quintilian says "can only be taught in actual practice" (1.8.1; Thrax §2); spacing does not do this. Bonner (K7) names the *praelectio*.

### Q2. Training after separation

The same sequence continued, and the sources do not describe a change when separation arrived. Reynolds says that "even at its very earliest stages, learning to read means learning to read a foreign language" [unverified: see AUDIT_06] (inner quotation marks dropped; confirm in print), with an alphabet that "is not the alphabet of the mother-tongue". Orme (2006) says that "for many, learning to read must have involved learning Latin as a foreign language". Black reports that the sequence of alphabet then syllables is "a technique going back" before the Middle Ages, and that the Italian reading syllabus remained *carta*, psalter, Donatus. Grendler records syllable pages, then words, in the Renaissance primers. Riché describes letters and syllables first, then the eight parts of speech. In each of Reynolds, both Orme books, Black (for separation terms), Grendler and Riché, a whole-book search finds no hit for "word separation", "scriptio continua" or "Saenger" (log rows 10–14). The standard accounts of how medieval and Renaissance children learned to read do not mention separation as a feature of the teaching.

Saenger's account of novices in the Introduction concerns Japanese kana (p. 3); on p. 6 he adds that young children "tend initially to write in scriptura continua" because it represents uninterrupted speech. The other nearby text is the "shortcuts" sentence (K13).

### Q3. Does any scholar claim, test or deny that separation shortened, eased or removed the training?

I found no work that tests or denies it, and none that claims it for populations, other than Saenger's p. 11 and p. 13 remarks (below), in these sources: the archive.org lending scans of Cribiore (1996, 2001), Marrou, Bonner, Morgan, Johnson, Reynolds, Orme (two books), Black, Grendler, Riché, Parkes, Saenger (1982, 1997, 1999), Cavallo and Chartier, Rouse and Rouse, Chartier, Carruthers, Stock; the reviews of Saenger in the issue scans of *Speculum*, *AHR*, *CJH*, *Library Quarterly*, *Language in Society*, *Raritan*, *Notes and Queries*; and eight unscoped full-text queries over the whole archive.org text corpus (log rows 1–24). The facet C "silence" is therefore real, but it is narrower than "nobody says anything": three kinds of statement come close.

- **For the narrow form.** Saenger 1997 (p. 85): "Word separation, the diastole, the hyphen, and eventually the trait d'union in Insular books provided shortcuts for achieving the reading skills that an elite among the ancients had mastered only through a prolonged and arduous grammatical apprenticeship." Parkes (p. 1 per facet A; my snippet; Parkes introduces the point for Latin in the West generally): "Because many had to learn Latin as a foreign language, there was a need for conventions which made it easier to read." Aronoff and Richter report the same Insular explanation. Marrou says the child found *scriptio continua* harder. Blake (2002) repeats the ease argument for a teaching audience. Svenbro (in Cavallo and Chartier 1999, pp. 51-52) allows that the absence of breaks "was not an insurmountable obstacle" to silent reading, but reports Saenger's view that in the Middle Ages "word division was a necessary condition for the dissemination of the practice of silent reading".
- **Against the wide form.** Saenger (1999) separates the history of reading from the history of literacy, which "is concerned with quantitative questions relating to the diffusion of these various reading skills to different strata of society", and holds that class and gender are "of only marginal import to the history of reading". Saenger 1997: "not a general history of literacy".
- **Silent where it should speak.** Reynolds, Orme, Black, Grendler and Riché contain no hit for "word separation" or "scriptio continua" in the OCR of the scans I searched; Riché (1976) and Grendler (1989) were written before Saenger's book, and Black and Riché do discuss silent reading.

The author's sentence therefore has one nearby statement, Saenger's "shortcuts" sentence, and it is about Insular books and the reading skills of an elite (Saenger's argument that Insular readers were learners of Latin appears on p. 91), bundles separation with three marks, and brings no measure.

### Q4. The catalogue of causal claims

See the table in K15, and K16 to K19 for reception. In short: the claims run from separation to **silent and rapid reading** (Saenger; repeated by Cavallo and Chartier, Mulchahey, Walker, Lyons, Garrett); to **reference reading and scholasticism** (Saenger; absent from the Rouses' own explanation); to **private devotion, heresy, authorship, erotic and vernacular reading** (Saenger alone, with Illich's date for visual reading glossed by Saenger). Reviewers repeat the claims and do not test the individual links. The two negative reactions I could read are of kind: O'Donnell on "necessary and sufficient" (facet B) and the Raritan reviewer on "relentless teleology". Facet B holds the critics who reject the physiology.

### Q5. Reverse causation

| Scholar | Direction | Wording |
| --- | --- | --- |
| Parkes | readers to script | "Because many had to learn Latin as a foreign language, there was a need for conventions which made it easier to read." |
| Saenger | both ways | Irish scribes separated for learners; the Continent adopted for scholars (facet A, pp. 83–97, 120); in 1997 he also writes of the scribe's "unconscious quest" (p. 33, facet A) |
| Richter (reviewer) | readers to script | "The practice began in those countries that had received Latin as a foreign language." Romance regions lagged because of "the relatively greater familiarity there with the Latin language" |
| Aronoff (reviewer) | readers to script | Saenger's learner reason, "much more plausible" than the Syriac model, for why word separation "might have begun" in the British Isles: "Latin was a foreign language for its Irish and British learners" |
| Baron | readers to script | Insular (Irish) scribes introduced spaces when copying Latin; copying texts in Irish, their native tongue, they grouped words by stress or phrasing instead |
| Svenbro (in Cavallo and Chartier 1999, ch. 1) | both | "since sonorization was valued as a good in itself, why should anyone feel the need to abandon the scriptio continua that was a technical impediment to the development of silent reading?" |
| Johnson | social, elite choice | Word division in Latin literary texts "was discarded by the Romans in deference to Greek aesthetic and cultural traditions"; the bookroll "designedly reserved" for an elite |

Two reviewers single out the learner explanation or the Romance lag for approval (Aronoff: "much more plausible" than the Syriac model; Richter: "convincingly" for the Romance lag); the others I could read describe the silent-reading claim without testing it.

### Q6. Verdict

| Claim | Class | Basis |
| --- | --- | --- |
| Insular separation arose to ease reading for learners of Latin as a foreign language | (b) claimed, endorsed by two reviewers as plausible, untested | Saenger (p. 91, 83-89), Parkes; Richter and Aronoff report it, Aronoff as "much more plausible"; Baron. Reynolds and Orme show only that Latin was a foreign language |
| Ancient teachers divided syllables, and sometimes words, for novices; syllable division gave way to ordinary texts for advanced students | (a) supported | Cribiore 1996, 2001 ("some"), Johnson, Bonner, Morgan; Marrou |
| Separation shortened Insular learners' apprenticeship (the "shortcuts" sentence) | (b) claimed, untested | Saenger 1997 p. 85; I found no reviewer comment on it in the snippets I could read (Hanna and Baeuml unread) [unverified: see AUDIT_06]; no measure |
| Separation made silent reading possible, or rapid reading | (b) claimed and contested | Saenger; Cavallo and Chartier; Mulchahey; against: Knox (silent reading attested before spacing; no mention of word separation), Vatri, Heilmann, O'Donnell 2000 ¶3 on "necessary and sufficient" |
| Separation enabled reference reading and the scholastic apparatus | (b) claimed; Rouse and Rouse give an explanation that does not mention it | Saenger; Rouse and Rouse (1982) explain the apparatus by readers' need to find things and do not mention separation; the paper predates Saenger's book, so it is not a reply to him |
| Separation → private devotion, heresy, autograph composition, erotic reading, vernacular reading | (b) claimed by one author, not tested | Saenger 1997 and 1982 |
| Separation → greater literacy, or a larger body of readers | (c) no source I read says separation raised literacy | Saenger lists "the greater diffusion of literacy throughout all social strata" among the advantages of ease of reading that moderns perceive (p. 11) and says "even readers of modest intellectual capacity could read more swiftly" (p. 13) |
| Separation → the populace no longer needed training | (c) claimed by nobody found | Reynolds, Orme, Black, Grendler show the training (alphabet, syllables, psalter, Latin) unchanged |

**What the sentence at `draft.md:263` can be made to say that scholars support.** I do not rewrite it. The supported material, with the quotations, is:
1. Teachers in antiquity already used word or syllable division as a novice aid (Cribiore 1996, p. 48: "in theory he was ready for more serious and challenging reading", with word division kept "as a further aid"; Johnson, p. 20: "the need for emerging readers to practice syllable and word division").
2. In the Insular case, separation and other marks were said to give a "shortcut" to what an elite had learned by "a prolonged and arduous grammatical apprenticeship" (Saenger 1997, p. 85) for readers who "had to learn Latin as a foreign language" (Parkes, speaking of Latin in the West generally).
3. The training in the later Middle Ages and Renaissance was an alphabet, syllable and psalter course in a foreign language (Reynolds; Orme; Black; Grendler), with no source giving separation a place in it.
4. "Populace": no source credits separation with reaching the populace; Saenger's own 1999 chapter assigns diffusion to the history of literacy, though his 1997 book lists "the greater diffusion of literacy throughout all social strata" among the advantages of ease of reading that moderns perceive (p. 11).

### Claims the sources contradict or qualify

1. **"It changed the interface so that reading no longer required the training" (`draft.md:263`).** Qualified. Saenger's "shortcuts" for Insular learners is the nearest statement and it shortens an apprenticeship; it does not remove one (Saenger 1997 p. 85). After separation was standard, Italian and English schools still taught alphabet, syllables, psalter and Latin (Black; Grendler; Orme 2006: "for many, learning to read must have involved learning Latin as a foreign language").
2. **"The populace."** No source supports it. Saenger (1999) separates the history of reading from the history of literacy, which "is concerned with quantitative questions relating to the diffusion of these various reading skills to different strata of society", and holds that class and gender are "of only marginal import to the history of reading"; the readers served by separation were Latin learners, then clerics and scholars (facets A and C).
3. **That the difficulty of unspaced script was the main training burden.** Reynolds: "even at its very earliest stages, learning to read means learning to read a foreign language" [unverified: see AUDIT_06]. The burden named is Latin. Dionysius and Johnson both treat the end state as fluent.
4. **That the unspaced page had no aid for the novice.** Cribiore 1996 and 2001, Bonner and Johnson show ancient teachers separating syllables and words for beginners.
5. **That antiquity could not have seen the benefit.** Johnson (2010, p. 20): "Greeks and Romans knew perfectly well, for instance, the utility of word division". Their choice not to use it for adult texts is a social one.
6. **Facet A's gloss of the "shortcuts" sentence as about separation alone.** The sentence bundles "Word separation, the diastole, the hyphen, and eventually the trait d'union".
7. **Silent reading as the product.** Svenbro (in Cavallo and Chartier 1999, pp. 51-52) allows that the absence of breaks "was not an insurmountable obstacle" to silent reading, but reports Saenger's view that in the Middle Ages "word division was a necessary condition for the dissemination of the practice of silent reading".
8. **Reference reading as caused by separation.** Rouse and Rouse (1982) explain the apparatus by readers' need to find things and do not mention separation; the paper predates Saenger's book, so it is not a reply to him.

---

## (d) Gaps and unverified leads

**Could not open; where a human with library access finds them.**
- Cribiore 1996 (closed; Unpaywall) and 2001: read the sections on syllabic division and word separation, and the Hero passage, for her stated reasons and the length of each stage.
- Marrou, *History of Education in Antiquity*, the Hellenistic reading-lesson chapter: what "these" refers to in "It was not so easy for the child to read these".
- Saenger 1997 p. 3 (Japanese kana) and p. 6 (novices), p. 85 ("shortcuts"; page confirmed by the auditor), p. 264 ("Private Study and Heresy"), p. 265: page numbers for every K15 claim marked "page not available".
- Saenger 1982 (*Viator* 13, 367–414): Brepols bot wall; the open "bronze" copy at `brepolsonline.net/doi/epdf/10.1484/J.VIATOR.2.301476`.
- Saenger 1999 in Wagner, Venezky and Street (1999), ch. 2: confirm start and end pages; check the sentences on diffusion in print.
- Cavallo and Chartier 1999, Introduction: which editor wrote the "line and page" passage, and its page.
- Hanna (*Speculum* 74(3), 830–831, DOI 10.2307/2886848): her evaluation, not just her summary. Bäuml (*Written Language & Literacy* 5(1), 131–134, DOI 10.1075/wll.5.1.08bau). Gilliard 1993. Lyons 2001 review.
- Illich 1993 and Mak 2011: no route to the text. Driver's *Speculum* review of Mak (DOI 10.1017/s0038713413001322).
- Parkes 1976, on *ordinatio* and *compilatio*, and Rouse and Rouse 1982 in print: for whether either mentions separation in the body.
- The *Raritan* reviewer and the *Notes and Queries* reviewer: names.
- Stutzmann, any dated-manuscript test of Saenger's chronology (facet A could not find one).
- Dionysius of Halicarnassus: the Greek; Usher's Loeb translation, which supersedes Roberts for any quotation in the paper.
- Dionysius Thrax: the authenticity literature, before the paper cites the *Technē* as ancient evidence.

**Unverified or weak.** The joins of snippets in Marrou, Johnson, Cribiore 1996, Cavallo and Chartier and Baron are mine; a print copy should confirm each sentence. Nothing in this facet is quotable in the paper at "full text" depth, by the repo's rule (`../algorithmacy_ot/README.md:29-41`), except Quintilian, Roberts's Dionysius and Davidson's Thrax.

**Not found despite search.** Any study measuring the length or cost of learning to read spaced against unspaced Latin for medieval learners; any modern experiment on Latin or Greek novices. The closest modern evidence is in facet D (children and second-language readers).

## Changes after audit (2026-10-13)

- Q1, length of training: "None gives a length of training in years" narrowed to "a length for learning to read alone"; Cribiore (2001, p. 171) gives "one or two years of elementary instruction" for many students.
- Q1 point 1, "teachers took the aid away": now says syllable division gave way to ordinary texts, while word division continued "as a further aid" until accents (Cribiore 1996, p. 48). The Cribiore 1996 pieces (syllable exercises; "spaces or bars" at p. 72; 2001 "bars or dots") are no longer run together, and "advanced students in scriptio continua" is limited to "some" models.
- Q1 point 2: Dionysius is an analogy for composition and says nothing about word division; the "end of training, not its obstacle" heading is marked as my inference. Johnson's "years of advanced study" describes the literature, not the script. "Marrou is the only source" changed to "the plainest source", since Cribiore (1996, p. 48) also reports the difficulty.
- Q1, praelectio: not in Quintilian 1.8.1-2; the point now rests on Quintilian's "can only be taught in actual practice", and the praelectio is credited to Bonner.
- Q2, Saenger on novices: the "syllabary" sentence is about Japanese kana (p. 3), not pre-separation Greek or Latin teaching; removed as evidence about Latin teaching and replaced with the p. 6 statement.
- Q2, Orme and Reynolds: "for many" restored in Orme (2006); Reynolds' inner quotation marks dropped and flagged unverified.
- Q3, Cavallo and Chartier: the two quotations are Svenbro's. Removed from "Against the wide form" (they say nothing on literacy diffusion) and moved to "For the narrow form", because Svenbro's next sentence cites Saenger for word division as "a necessary condition for the dissemination of the practice of silent reading". The Q5 table row and claim 7 changed to match.
- Q3, Saenger 1999: "marginal to his chapter" replaced by his actual statement that class and gender are "of only marginal import to the history of reading"; the scope disclaimer does not settle whether Saenger links ease of reading to literacy, and "I found no work that ... claims it for populations" now carries an exception for Saenger 1997 pp. 11 and 13.
- Q3, "Silent where it should speak": now states the OCR zero hit and that Riché and Grendler predate Saenger's book.
- Q3 closing sentence: the "shortcuts" sentence is about Insular books and an elite's reading skills; the learner argument is on p. 91.
- Q5, Baron: the scribes are Insular (Irish), not Anglo-Saxon, and the Irish-language copying result is the reverse of the earlier reading.
- Q5 closing sentence: "the only causal claim a reviewer endorses as 'convincing' and 'plausible'" replaced; "convincingly" (Richter) is about the Romance lag and "much more plausible" (Aronoff) is comparative and hedged.
- Q6 row 1 (Insular separation to ease reading for Latin learners): (a) supported changed to (b) claimed, endorsed by two reviewers as plausible, untested. Reynolds and Orme show only that Latin was foreign, and no source tests it.
- Q6 row 2 (ancient teachers): restated as syllables, and sometimes words, divided for novices; syllable division gave way to ordinary texts. Class (a) kept.
- Q6 row 3 (shortcuts): "no reviewer comments" changed to "none in the snippets I could read (Hanna and Baeuml unread)", marked unverified.
- Q6 row 5 and claim 8 (reference reading): "rival explanation" withdrawn; the Rouses' 1982 paper predates Saenger's book, so it is not a reply to him.
- Q6 row 7 and the supported-sentence list item 4 (literacy): "claimed by nobody found" changed to "no source I read says separation raised literacy", with Saenger's p. 11 and p. 13 remarks stated.
- Claims 1 and 3: Orme's "for many" restored; the Reynolds marks flagged.


## Changes after full-text cards (2026-10-13)

Source: `audit/CARD_FACET_CHECKS.md`, Facet K section and the B-section notes that name Facet K; the card, including its S2 section, is the authority.

- `quintilian1920institutio`: 1.1.34 is on p. 37 (not pp. 37–39); 1.8.1–2 on p. 147 (not p. 148); 1.7.17 (p. 139) added: he judges a spelling convention by whether it hinders learners, and 1.7 says nothing about spacing; read status corrected from "read in full" to read in part (card), since the rest of Book 1 was not read.
- `dionysius1910composition`: chapter XXV runs pp. 251–270, not "between running heads 265 and 269"; the reading passage is on p. 269 and the tablet story on pp. 265–267; "says nothing about word division" confirmed. Read in part (card).
- `thrax1874grammar`: quotations confirmed; read status corrected from "read in full for §§1–2" to read in part (card: §§1–14 and the closing section; §§15–24 skimmed); "attributed" kept.
- `knox1968silent` (K rows on silent reading): Knox never mentions word separation or the training of readers; the two table rows now say so. Read in full (card).
- `odonnell2000saenger` (same rows): quotation now exact (¶3 "some will dissent from … necessary and sufficient"; ¶4 "most venturesome and vulnerable part"); he calls the chronicle sound and the causal claim the likelier to fail. Read in full (card). `odonnell1994parkes` is not cited in this facet; the card's correction (the *Viator* article is cited in the 2000 review, not the 1994 one) concerns facet B, so no change here.
- `ker2012johnson`: not cited in this facet; the card's note (Ker does not discuss training of novices, so no purchase on Johnson's "emerging readers" sentence) needs no change.

Synthesis verdicts changed: none. Q1 still reads that the ancient sources place the burden in a long drill, not in the page; 1.7.17 adds that Quintilian weighs a convention by its cost to learners, but he never applies the test to spacing.
