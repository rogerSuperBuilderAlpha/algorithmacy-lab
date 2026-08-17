# Copyeditor's review — `chapter/chapter_v3.md`

**Verdict: major revisions.** The apparatus is in far better shape than the v2 audit would predict — all
71 notes resolve, in order, with no orphans and no duplicates — but three notes carry errors I verified
against sources this pass (a wrong given name in note 64, a wrong given name plus a stripped diacritic in
note 63, a wrong page locator in note 45), one note prints a quotation the project's own research file
marks as untested, and §7 miscounts the chapter's own list of platform powers. Two of those are the kind
of thing a reviewer finds in ten minutes with a DOI resolver.

---

## Step 0 — register

The first person, the contractions, the scenes-before-theses, the questions asked and answered: I read
these as the chapter's method and I have not touched them. Every rewrite below is at least as plain and
at least as active as what it replaces, or it is not here.

Two things I would ordinarily flag and am not flagging: the em-dash count (40 across 53 paragraphs) and
the "X rather than Y" count (13). In a chapter whose entire argument is a distinction between two kinds
of third, contrastive syntax is the load. Three instances are decoration and I name them in Part 2; the
other ten earn their place.

---

# Part 1 — Citation mechanics, note-to-sentence fit, and internal arithmetic

## 1.1 The structural audit passes

Worth saying first, because it is unusual. Body references run 1–71 in strict ascending order. Note
definitions run 1–71 with no gaps. Every note in the body resolves to a definition; every definition is
called exactly once. No note is orphaned, none is duplicated, and no note number is reused. I checked
this mechanically, not by eye.

The discipline the outline imposed on locators has also mostly held. Where `outline_v3.md` said "attach
no page numbers" (Rosenfeld et al.), the chapter attaches none. Where it said "cite the range and the
section name" (Ramírez Berg), the chapter does exactly that. Where it said Cameron's body was
unreachable, note 54 ends "abstract." Where it said the Bengesser landing-page numbers must never be
read as evidence about recommendation, §7 says so in the body. That is the behaviour of a manuscript
that has been through a real verification pass, and I want the author to know I could tell.

## 1.2 Three citation errors I verified this pass

I retrieved a source for each of these. I am asserting them.

**(a) Note 64 names the wrong person.** The chapter prints:

> [^64]: Anne Brodsky et al., *Journal of Media Literacy Education* 12, no. 3 (2020): 43–57.

The lead author is **Jessica E. Brodsky**. I resolved DOI `10.23860/JMLE-2020-12-3-5`, which lands at
`digitalcommons.uri.edu/jmle/vol12/iss3/5`: "Assessing and fostering college students' algorithm
awareness across online contexts," by Jessica E. Brodsky, Dvora Zomberg, Kasey L. Powers, and Patricia
J. Brooks, 43–57. "Anne Brodsky" is a different scholar (Anne E. Brodsky, community psychology, UMBC).
The name appears nowhere in `research/deep/2026-08-01_s6.md`, which gives only surnames — so it was
supplied at drafting. The note also carries **no article title at all**, which on its own makes the
source unfindable.

**(b) Note 63 names the wrong person and strips a diacritic.** The chapter prints "Emilija Gagrcin,
Teresa K. Naab, and Rebecca Grub." Crossref on `10.1177/14614448241291137` returns **Emilija Gagrčin,
Teresa K. Naab, Maria F. Grub** — the surname carries an acute accent and the third author is Maria, not
Rebecca. Both entries in note 63 are also **titleless**. The titles of record are "Algorithmic media use
and algorithm literacy: An integrative literature review" (Gagrčin et al.) and "What do we know about
algorithmic literacy? The status quo and a research agenda for a growing field" (Oeldorf-Hirsch and
Neubaum). Volume, issue and pages are correct in both.

**(c) Note 45 puts the Poulaki quotation on the wrong page.** The chapter pins "the self-reflexive
agency of the camera" at p. 135. The project's own three-lens record
(`research/deep/2026-08-01_s4.md`, lines 340–346) locates it at **ch. 8, p. 153**:

> Ch. 8, p. 153, verbatim: "…a parcours which is not motivated by narrative action and causality but
> rather by the self-reflexive agency of the camera."

Page 135 is the *other* Poulaki quotation the chapter uses — the *Gomorrah* one — which the same record
gives as "Ch. 7, p. 135, verbatim, in full: 'The link that indirectly connects them is primarily the
setting—the housing complex where they both live—and the character of Maria…'" That quotation is
currently footnoted at note 46 to "103–4, 152–53." So the two Poulaki pins are, in effect, swapped: the
page the chapter cites for the camera sentence is the page the *Gomorrah* sentence is actually on, and
the *Gomorrah* sentence is cited to a range that does not include it.

## 1.3 A quotation in print that the project marked untested

Note 37:

> [^37]: Pierson, quoted in Marc Savlov, "Slack to the Future," *Austin Chronicle*, January 21, 2011.

Three problems, in ascending order.

1. **Savlov 2011 has no entry in `outline_v3.md`.** The §4 bibliography runs Bordwell 1985, Bordwell
   2008, Chatman, Slugan, Thomson-Jones, Ramírez Berg, Walters, Poulaki ×2, Münsterberg, Joyce, Moretti,
   Jeong, Stone. No Savlov. The §1 bibliography does not have him either. So this is the one source in
   the chapter that never went through the verification protocol the outline describes on its first page.
2. **`research/deep/2026-08-01_s4.md` flags this exact quotation.** Line 904: "**Not tested this pass,
   and load-bearing in section 4:** the Pierson craft note ('not a single jump cut, always in a flow')
   and the Linklater 'comprehensive architecture' quotation, both sourced to Savlov, 'Slack to the
   Future'… Put them in the next run." It was not put in the next run; it went to print.
3. **The wording does not match the research file's.** The chapter prints "not a single jump cut, and
   the passage from one scene to the next is always in a flow." The research file's rendering is "not a
   single jump cut, always in a flow." One of these is a paraphrase and I cannot tell which from here.

Given the standing caution about the nine errors in the predecessor, this is the note I would fix first.
Either retrieve the *Chronicle* page and quote it exactly, or paraphrase Pierson without quotation marks.

## 1.4 Internal arithmetic

**(a) §7 counts to four against a §5 that counts to three. This is the worst structural error in the
chapter.** §5 is explicit:

> What a decade of subsequent work adds is a precise account of what a selector can do that a camera
> cannot, and it comes to three things. The first is that it prices each match… The second thing is that
> it reads the parties… The third thing is that it can remove a party…

Three powers: **price, read, remove**. §7 then says:

> Amazon publishes its own account of how titles are licensed for Prime Video, and three of the powers
> described above are in it. It reads… It removes… And it declines to explain… The fourth power is
> missing from the page and I am not going to supply it; Amazon publishes nothing about pricing.

Only **two** of §5's three powers are on that page. The third item §7 lists — declining to explain — was
never established as a power in §5. And "the fourth power" turns out to be pricing, which *is* one of
§5's three. `outline_v3.md` shows where this came from: its §7 entry says Amazon "publishes three of the
chapter's four powers — reading, removal, and refusal of explanation." The outline was working with four.
§5 shipped with three. §7 kept the outline's count.

Two clean repairs, and the author should pick, not split the difference. Either add refusal of
explanation as §5's fourth power (Binns et al. already supplies it — "The driver cannot see the
passenger's fare in the app, and Uber bars him from asking the passenger directly" is a refusal of
explanation with a prohibition attached), or rewrite §7's sentence to count to three.

**(b) §6 miscounts the verbs in a quotation it prints in the same sentence.** The chapter:

> …calling cinema "the single most inclusive cultural horizon in which the traumatic effects of
> modernity were reflected, rejected or disavowed, transmuted or negotiated" — though she bounds herself
> to 1920s-to-1950s mainstream Hollywood, and *negotiated* is the last of four verbs in a list that
> opens with rejected.

The quoted list has **five** past participles — reflected, rejected, disavowed, transmuted, negotiated —
and it opens with **reflected**, not rejected. `outline_v3.md` says "'negotiated' is the fourth verb in
a list that opens with 'rejected or disavowed'," which is true of the clause *after* "reflected"; the
chapter compressed the outline's note and lost the first verb. A reader counting the words on the page
catches this instantly, and the point survives intact once fixed.

**(c) "thirty years later" points at the wrong decade.** §3:

> Reuben May finds the same discretion at work in commercial gatekeeping thirty years later, Austin
> included.[^34]

The sentence sits at the end of a paragraph about *Papachristou* (1972). Thirty years after 1972 is
2002; May's article is 2022. The intended anchor is presumably the film's 1990, which is 32 years. Say
which.

**(d) Arithmetic that checks out, for the record.** 27,100 + 23,145 = 50,245 (note 30 / §3). 55% of
twenty experienced viewers = eleven (§6, and the chapter correctly writes "eleven"). Walters 1990 to
Ramírez Berg 2006 = sixteen years (§4). Housing 48.0 against population 34.6, Austin 11.6 against Dallas
15.3 and Houston 15.8 — all match the outline's verified rows.

## 1.5 Claims in the body with no note on them

**(a) The whole opening paragraph of §7.** Four factual claims, no note:

> Pierson, a producer's representative whose job was introducing films to buyers, took it to them. The
> Dobie booked it on its own judgment and held it eleven weeks. Orion Classics bought it and released it
> nationally on a top of sixteen screens…

The eleven weeks and the sixteen screens were noted at [^3] in §1, six pages earlier; "the Dobie booked
it on its own judgment" and Pierson's role are not noted anywhere. §7's first note is [^67], and it
arrives two paragraphs in.

**(b) The *Film Comment* anecdote, which is also contested in the source.** §7:

> The earlier gate had responded — a paragraph in *Film Comment* reached a buyer, who telephoned
> relatives in Austin to ask whether the Dobie sellouts were real.

No note. The material is documented — `research/deep/2026-08-01_s7.md` traces it to Macor, whose
bibliography gives Horton, "Stranger Than Texas," *Film Comment* (July–August 1990): 77–78, with the
endnote pinning 78 — so this is a missing note rather than a missing fact. But the same research file
raises something sharper (lines 715–718): Macor's sentence continues "but Pierson insists that Barker
had done this before he traveled to Maine in early August," and the file's verdict is that clipping it
"converts a contested account into a settled one, and the contest is precisely about whether the phone
call was verification or theatre." The chapter's "had responded" takes the settled version. Two
participants disagreeing about who checked what and when is better evidence for a chain made of people
than a tidy anecdote is.

**(c) The Dallas and Houston vacancy rates.** §3:

> Dallas that year sat at 15.3 percent vacancy and Houston at 15.8, so Austin was the tighter market of
> the three; what it had was a great deal of room and 50,245 students at the university in the middle of
> it.[^30]

Note 30 is IPEDS enrollment. It says nothing about vacancy. Those two figures come from the same census
table as Austin's 11.6 (note 29, two sentences up), and a reader auditing the sentence finds an
enrollment file cited for a housing statistic.

**(d) Three counts the author took off the screen.** "What the film does next it does about three dozen
times" (§1); "Of the ninety-eight credited roles, almost none meet twice" (§1 — note 2 sources the
count, not the meeting); "this one gives it about two [minutes], then leaves the son mid-arrest" (§4).
All three are countable and none is sourced. In a chapter this scrupulous about the difference between
98 credited roles and Rosenbaum's "around 90," leaving its own counts unattributed is a mismatch of
standards.

**(e) No note establishes the viewing copy.** The chapter cites "end credits" at [^1] and describes
scenes throughout — the coffee-shop monologue, the pap-smear seller, the arrest, the oblique-strategies
card. Chicago wants one note fixing the print: which transfer, which edition, viewed when. The outline's
§4 author-only list already says the disc is needed for the scene material, so this note has to be
written anyway.

## 1.6 Notes whose content does not match the sentence they hang on

**Note 15 corrects an error the chapter does not make.** The sentence is about Obstfeld's joining
broker. The note ends: "The term *tertius iungens* is Obstfeld's coinage, not Simmel's; it appears
nowhere in Wolff's translation." The chapter never writes *tertius iungens*. It is a good correction
aimed at a claim that is not on the page; either use the term in the body so the correction has
something to correct, or move it into whatever note handles the Simmel genealogy.

**Note 2 sources the count but not the claim.** The sentence: "Of the ninety-eight credited roles,
almost none meet twice." The note documents 98/97 and the range of contemporary counts. Nothing in it
addresses "almost none meet twice."

**Note 47 makes an unsourced factual assertion.** "The driver-facing interface has changed substantially
since; Uber now shows an estimated fare and the nearest cross streets before acceptance." That is a
claim about the present state of a commercial product, in a note, with no citation. `outline_v3.md` §5
supplies exactly the two sources for it — Uber Blog, 8 April 2021 ("You'll always see fare, destination,
and distance if you accept 5 of your last 10 trips") and Uber Blog, 5 March 2025 ("we'll show the cross
streets closest to the pickup and dropoff points"). Add them.

**Note 3 covers two of four facts.** The sentence carries 16mm, summer 1989, $23,000, eleven weeks at
the Dobie, Orion Classics the following July, over a million dollars, sixteen screens. The NYT piece
supports 16mm, $23,000 and the eleven weeks; Box Office Mojo supports the gross and the screen ceiling.
**"in the summer of 1989" is supported by neither.** Macor is the obvious home for it.

**Note 4 enumerates six critics for a body list of seven.** The body names "Ebert, Hinson, Howe, Turan,
*Variety*, Canby, Jonathan Rosenbaum." Note 4 gives Turan plus five and does not mention Hinson, who is
at note 5. Since the claim is an exhaustive negative *over the enumerated set*, the enumeration in the
note should be complete: add "and Hinson, cited below at note 5."

**Note 4 also omits the one countervailing sentence the outline told the chapter to carry.**
`outline_v3.md` on *Variety*: "the second sentence leans toward a comprehension complaint. *Job:*
include it *because* it cuts the other way. A reader will find it." The sentence is "Basic problem,
given the absence of storyline, is that interest quickly rises and falls by virtue of who happens to be
on screen." I think the chapter's claim survives it — losing interest is not losing the thread — but the
survival should be shown, not assumed, and one clause in note 4 does it.

## 1.7 Locators that are too wide, unsettled, or from an uncited issue

- **Note 22 prints a page the outline said to settle first.** "Finkel et al., 'Online Dating,' 3." The
  outline: "the access/communication/matching definitions at p. 3 by two lenses' header count, p. 4 by a
  third — **settle this before citing**." It was cited without being settled. Either confirm against the
  version of record or print "3–4."
- **Note 33 pins two pages that were never verified.** "*Papachristou*… at 156–58, 164." The outline
  lists the confirmed pins as 158, 159, 164 and 170. Page 156 is the caption and syllabus. Narrow it to
  158 and 164.
- **Note 28 carries a figure from an issue it does not cite.** The note cites *Trends* 3, no. 8 (April
  1990) and then states "By May 1990 both Dallas and Houston had fallen to eight permits apiece." The
  May data is in *Trends* 3, no. 11 (July 1990) — the outline cites both issues. Add the second.
- **Note 68 drops the SEC locator.** For a Form 10-K the accession number is the locator; the outline
  has it (0000950142-94-000054, filed 15 June 1994). Add it or an EDGAR URL.
- **Note 46 pins three quotations to one range with no mapping.** "103–4, 152–53" covers the *Gomorrah*
  link, the "primarily informational" characterisation, and the catalogue/system line, in an order the
  reader cannot reconstruct. Order the pins to match the order of the quotations, and fix p. 135 into the
  set (see 1.2c).
- **Note 38 pins one page for two claims from two.** Note 38 gives Bordwell 1985 at 62. The sentence it
  hangs on carries both the "no sender" quotation (p. 62) and the list of what narration does — suppress,
  restrict, generate curiosity, set a tone — which the outline locates at p. 53. Print "62, and 53 for
  the functions."

## 1.8 Disclosure asymmetry

The chapter discloses its reading limits in exactly one place: note 10, "I have read the abstract only."
That is admirable and it creates an expectation the other notes do not meet.

- **Note 18 (Feld 1981)** carries the definition on which the chapter's central term rests. The outline:
  "**The article itself was never opened** — Unpaywall reports closed, no OA PDF. The p. 1016 definition
  is stable across five independent quoting sources but remains second-hand." A reader who trusts note 10
  will read note 18 as first-hand. This is the founding citation of the chapter's own coinage; it should
  either be obtained or disclosed.
- **Note 38 (Bordwell 1985)** is convergence-verified — the outline says "No page image; the Archive scan
  is lending-restricted. Flag as convergence-verified until a library copy is checked."
- **Note 21 (Small & Gose)**: outline says "**Body not retrieved — cite the abstract's four conditions
  and nothing deeper.**" The chapter says "the conditions they list" without saying where they are listed.
- **Note 6 (Pierson)** cites the Hyperion book as though it were the text consulted. The outline is blunt:
  "**Nobody in this project has opened the Hyperion book**; there is no print pagination." The text used
  is the Criterion reprint of 18 September 2013. Cite the reprint, with its date, as the version consulted.
  (`research/deep/2026-08-01_s7.md` also gives the publisher as Faber where the outline gives Hyperion —
  the 1996 US first edition is Hyperion, so the outline is probably right, but the two files disagree and
  someone should settle it before print.)

`outline_v3.md`'s §7 has a fourth item on this list that has not made it into the chapter at all: "the
producer's representative has no scholarly literature at all, which means Pierson's memoir is not one
account among several but *the* account — a dependency the section should name, since its whole 1991 half
rests on it." §7 does not name it. One sentence buys a great deal of credibility.

## 1.9 Chicago consistency

**Serial comma: the body and the notes disagree systematically.** Notes use it — "Michael J. Rosenfeld,
Reuben J. Thomas, and Sonia Hausen" (n. 23); "Omar Besbes, Francisco Castro, and Ilan Lobel" (n. 49);
"Cathrin Bengesser, Matthew Hilborn, and Jeanette Steemers" (n. 69); "Sermin Ildirar, Daniel T. Levin,
Stephan Schwan, and Tim J. Smith" (n. 59). The body drops it — "Michael Rosenfeld, Reuben Thomas and
Sonia Hausen"; "Besbes, Castro and Lobel"; "Cathrin Bengesser, Matthew Hilborn and Jeanette Steemers";
"sharing, matching and learning"; "a person, place or activity"; "plot, career and convergence"; "film,
cinema, montage or shot"; "reflected, rejected or disavowed" (that one is the source's). Chicago takes
the serial comma. Adopt it in the body, or at minimum make the three author-name lists match their notes.

**Titles silently truncated.** I checked these against Crossref this pass. All eight are missing a
subtitle that the note should carry, and in four cases the missing subtitle is exactly what the body
claims the source is:

| Note | Chapter prints | Title of record |
|---|---|---|
| 20 | "Brokerage and Brokering" | "Brokerage and Brokering: An Integrative Review and Organizing Framework for **Third Party Influence**" |
| 20 | "Assortative Meeting and Mating" | "Assortative Meeting and Mating: Unintended Consequences of **Organized Settings** for Partner Choices" |
| 23 | "Disintermediating Your Friends" | "Disintermediating your friends: How online dating in the United States displaces other ways of meeting" |
| 54 | "The Making of the 'Good Bad' Job" | "The Making of the 'Good Bad' Job: How **Algorithmic Management Manufactures Consent Through Constant and Confined Choices**" |
| 58 | "Reexamining the Kuleshov Effect" | "Reexamining the Kuleshov effect: Behavioral and neural evidence from authentic film experiments" |
| 61 | "Edit Blindness" | "Edit Blindness: The relationship between attention and global change blindness in dynamic scenes" |
| 62 | "What Would Jaws Do? The Tyranny of Film" | "What Would Jaws Do? The Tyranny of Film **and the Relationship between Gaze and Higher-Level Narrative Film Comprehension**" |
| 70 | "After the 'Great Studio Pullback of '08'" | "After the 'Great Studio Pullback of '08': **Late Indiewood and American Independent Film Theatrical Distribution in the Age of Streaming (2008–2019)**" |

The body of §2 calls Halevy et al. "the *Academy of Management Annals* review of third-party influence"
and Kalmijn and Flap "the leading study of organised settings." Both descriptions are lifted from
subtitles the notes do not print. Restore them and the body's characterisations become checkable in one
step. (Note 66 already carries Heiland's subtitle in full, so the house rule is subtitles-in — these are
lapses, not a policy.)

**Italics.**
- Note 62: *Jaws* is a film title inside an article title and takes italics — "What Would *Jaws* Do?"
- Note 52: *beschikking* is a foreign term on first use and takes italics.
- Note 9 puts the comma outside the inner quotation: `a kind of 'baton-passing',"`. US practice, which
  the rest of the chapter follows, puts it inside: `a kind of 'baton-passing,'"`.

**Ellipses.** The chapter uses a spaced ellipsis everywhere — "for a few seconds or a few minutes … until";
"We'll have these transitional characters. … It won't"; "primarily the setting … and the character of
Maria" — except once, in the Hinson quotation: "with miraculous ease… Linklater's control." Make it match.

**Short forms.**
- Note 43 shortens "Charles Ramírez Berg" to "Berg" twice ("Berg's own definition…"). *Ramírez Berg* is
  the surname; the short form is "Ramírez Berg." The body has it right both times, which makes the note
  the outlier.
- Body §3 has "Reuben May" where the note has "Reuben A. Buford May." Crossref renders him "Reuben A. B.
  May." He publishes under the three-part form; use it, or use "May" alone.

**Other mechanics.**
- Note 4 gives *Variety* no date. The outline says the piece is archived under 31 December 1990 with a
  crew block reading "Extract of a review from 1991." Print the archived date and say so, or the one
  source in the list whose date is genuinely ambiguous is the one with no date at all.
- Note 42 renders the Bordwell ellipsis as "*Slacker*. …" where the outline has "*Slacker*…". The added
  period asserts that Bordwell's sentence ends there. If it does not, drop the period.
- Note 61's "2, no. 2 (2008): 6, 1–17" reads as two page ranges. *JEMR* paginates by article: write
  "2, no. 2 (2008): article 6, 1–17."
- Note 8 leaves three *Washington Post* items (nn. 4, 5, 8) sharing one title and one date, one of which
  is an interview. The outline explains it — "the '(R)' heading is the *Post* archive's page furniture,
  shared with the Hinson and Howe pages" — and note 8 should say so in six words, or the apparatus looks
  broken.
- Note 48's proceedings title of record is "Proceedings of the 2025 ACM Conference on Fairness,
  Accountability, and Transparency." *FAccT '25* is fine as a short form if it is introduced; on a single
  appearance, give the full name.

**Numerals.** One sentence mixes the two conventions on parallel results: "all twenty made the
spatio-temporal link and eleven read sadness into the face, on the soup sequence the figure was 30
percent." Make the parallel results parallel in form, and give "the figure" an antecedent — as written,
the preceding clause has offered two numbers and the reader cannot tell which one 30 percent replaces.

## 1.10 What the chapter needs and does not have: a bibliography

The editor query commits to Chicago notes-and-bibliography. There is no bibliography. Here is the spec.

- **Coverage.** One entry per work cited, alphabetised by the first author's surname, checked in both
  directions: every note resolves to an entry, every entry is called by at least one note. The outline's
  own instruction ("Master reference list… checked both directions") has not been executed.
- **Count.** 71 notes resolve to roughly 60 distinct works, once Simmel ×2, Macor ×2, Pierson ×2, Finkel
  ×2, Rosenfeld ×2, Dubal ×2, Ildirar/Levin/Schwan/Smith ×2 and Poulaki ×2 are collapsed, and the
  see-also items in nn. 45, 49 and 58 (Poulaki 2014, Castillo, Barratt, Cao) are broken out as entries in
  their own right. Those four currently exist only inside other notes and would vanish from an
  auto-generated list.
- **Bibliography form, not note form.** Surname first; periods for the commas; full page ranges for
  articles and chapters; no pin cites.
- **Sort keys that will go wrong if nobody sets them.** *Ramírez Berg, Charles* files under R. *May,
  Reuben A. Buford* under M. *Van Kleek, Max* under V. *De Massis, Alfredo* under D. *Gagrčin, Emilija*
  under G, with the diacritic. *Papachristou v. City of Jacksonville* belongs in a separate Cases
  section, not interfiled alphabetically, and so do *Uber Technologies, Inc. v. City of Seattle* and the
  Gerechtshof Amsterdam beschikking.
- **Categories that need their own treatment.** Chicago handles these badly by default and the collection
  will not fix them for you: two court decisions and one Dutch appellate order; two census publications
  and one NCES data file; one SEC filing; one corporate documentation page (Amazon); one trade
  periodical (*Texas Real Estate Center Trends*); one film; one database record (AFI) and one box-office
  record (Box Office Mojo); one unpublished thesis (Poulaki). I would set up three lists — Works Cited,
  Cases and Statutes, Primary and Documentary Sources — and say so in a headnote.
- **Living pages need retrieval dates and archive URLs.** The Amazon page (n. 71) is dated "last updated
  August 5, 2025," which is Amazon's date, not the author's. Add "accessed [date]" and an Internet Archive
  snapshot; the outline says the same about the Uber Help pages. The Criterion reprint of Pierson, the AFI
  record and the Box Office Mojo record all need URLs and access dates too.
- **DOIs.** Chicago wants them where they exist. Every journal article in this chapter has one, and
  `outline_v3.md` already carries them; it is a transcription job, not a research job.

---

# Part 2 — The four bans, and the AI-slop audit

## Ban 1 — no metaphor doing argumentative work

Mostly held, and held better than most chapters that adopt the rule. Two live cases.

**"Cheap space buys unstructured time, and unstructured time is what this film is about."** (§3) This is
the causal claim of the paragraph, and the only version of it on the page is a metaphor. Everything
around it is literal and counted — 48.0 percent, 632 permits, $346, 11.6 percent — which makes the one
figurative link stand out as the place where the argument is not doing the work.

**"His word is string, and the important property of a string is that it has an order."** (§4) The
chapter has borrowed Bordwell's metaphor and then reasoned from a property of the vehicle. It is saved,
just, by the sentence two lines later — "In presentation it is an ordered walk: scene one, then scene
two, in that sequence, chosen" — which states the claim literally. Put that sentence first and the
string becomes what the ban permits: an illustration of a claim already made.

**Not a violation, and I want to be clear about it:** "Enclosure" as §7's title. It is a title, and
titles are allowed to be figures. But the word is never unpacked anywhere in the section, and it carries
a specific historical argument (common land, fenced) that the section neither makes nor disclaims. One
clause would settle it.

## Ban 2 — no throat-clearing

One clear violation. §6:

> What is actually measured is this. Sermin Ildirar and Louise Ewing ran the classic Kuleshov
> montages…

The first sentence exists to announce that the second is coming. Delete it; the paragraph starts better
on Ildirar and Ewing, and the contrast with the preceding Benjamin/Hansen paragraph is sharper without a
signpost between them.

"Two qualifications, both real." (§2) is borderline and I would keep it — it carries a count and a
concession, which is content.

## Ban 3 — no meta-commentary, no cross-references

One violation, in §7: **"three of the powers described above are in it."** "Described above" is the
banned construction, and the sentence is also where the count breaks (Part 1, §1.4a). Fixing both at
once: "Amazon publishes its own account of how titles are licensed for Prime Video, and it names two of
those powers itself."

## Ban 4 — no unexplained jargon

Four terms a general reader does not own, none glossed. The chapter is so good at this elsewhere —
*dérive* gets "a drift, which is movement without a chooser"; civil inattention gets "the glance and
withdrawal by which strangers in public leave each other alone"; nonterminal gets "offering no natural
exit"; *tertius gaudens* gets "who profits from their quarrel" — that the four misses read as oversights
rather than policy.

1. **"diegetic sound"** (§6). Film-studies term of art.
2. **"the 180-degree rule"** (§6). Ditto, and the sentence turns on what violating it costs.
3. **"assortative matching"** (§3). Economics term of art, and the sentence turns on the sign.
4. **"*divide et impera*"** (§2). The example that follows gives the sense, but a reader without Latin
   meets an italicised phrase and a bare "is."

Two more that I would leave alone but flag for the author's judgment: "agglomeration" (§3), which is
named and then described but never defined, and "algorithmic literacy" (§6), which arrives in a phrase
about two reviews and stands for a field.

## AI-slop audit

The chapter passes, and passes on measurement rather than impression. Across 5,414 body words:

| Tic | Count | Rate /1,000 | Target |
|---|---|---|---|
| `, not` | 2 | 0.4 | — |
| ` rather than ` | 13 | 2.4 | — |
| `is not a` / `is not the` | 4 | 0.7 | — |
| `It is not…It is` | 0 | 0 | — |
| **combined antithesis** | **19** | **3.5** | under 5 |
| self-narrating rigor phrases | 0 | 0 | 0 |
| paragraphs opening on a fragment under six words | 6 of 53 | 1 in 9 | at most 1 in 3 |

No "stated plainly," no "it is worth noting," no "crucially," no empty closer. Agentless passive is down
to two instances in the body, one of which I would fix ("The setting was named in 1981 and has been
studied since" → "Feld named the setting in 1981 and sociologists have studied it since"). Paragraph
openings vary: some on a scene, some on a short declarative, some on the long sentence that carries the
idea. That is a register, not a metronome.

Of the thirteen "rather than" constructions, ten mark distinctions the argument genuinely turns on. Three
are decoration and would go unmissed: "I want one instance rather than a pattern" (§3), "The authors
propose this rather than show it" (§6), "The acquisition market changed shape rather than shrinking" (§7).

---

# Part 3 — Ranked, paste-ready revisions

**1. Note 64 — wrong author (fatal).**

```
[^64]: Jessica E. Brodsky, Dvora Zomberg, Kasey L. Powers, and Patricia J. Brooks, "Assessing and
Fostering College Students' Algorithm Awareness Across Online Contexts," *Journal of Media Literacy
Education* 12, no. 3 (2020): 43–57. Two studies of US college students (N=222, N=244).
```

**2. Note 63 — wrong author, stripped diacritic, no titles (fatal).**

```
[^63]: Emilija Gagrčin, Teresa K. Naab, and Maria F. Grub, "Algorithmic Media Use and Algorithm
Literacy: An Integrative Literature Review," *New Media & Society* 28, no. 1 (2026): 423–447 — a
systematic review of 169 studies; Anne Oeldorf-Hirsch and German Neubaum, "What Do We Know About
Algorithmic Literacy? The Status Quo and a Research Agenda for a Growing Field," *New Media & Society*
27, no. 2 (2025): 681–701, at 696. Word-boundary searches over the full text of both, reference lists
included.
```

**3. Note 45 / note 46 — the Poulaki pins are swapped (serious).**

```
[^45]: Maria Poulaki, *Before or Beyond Narrative? Towards a Complex Systems Theory of Contemporary
Films* (PhD thesis, Universiteit van Amsterdam; Amsterdam: Rozenberg, 2011), 153. See also Poulaki,
"Network Films and Complex Causality," *Screen* 55, no. 3 (2014): 379–395.

[^46]: Poulaki, *Before or Beyond Narrative?*, 135 (the *Gomorrah* link), 104 (interactions as
informational), 103–4 (the catalogue and the system).
```

**4. §7 — the power count (serious).** Replace:

> Amazon publishes its own account of how titles are licensed for Prime Video, and three of the powers
> described above are in it.

with:

> Amazon publishes its own account of how titles are licensed for Prime Video, and it claims two of the
> three powers in its own words, plus one the ride-hail cases only imply.

Then, after the three quotations, replace "The fourth power is missing from the page and I am not going
to supply it; Amazon publishes nothing about pricing" with:

> Pricing is the one power missing from the page, and I am not going to supply it; Amazon publishes
> nothing about what it pays.

**5. §6 — the Hansen verb count (serious).** Replace:

> and *negotiated* is the last of four verbs in a list that opens with rejected

with:

> and *negotiated* is the last of five, in a list that opens with reflected and gets to rejected and
> disavowed before it gets anywhere near negotiation

**6. Note 37 — unverified quotation (serious).** Until the *Chronicle* page is retrieved, drop the
quotation marks and the note, and let the observation stand on the film:

> No character introduces another. Nothing is cut against anything: the film's transfers happen inside
> the movement, and even the arrest, which is cut together, breaks nothing.

If the page is retrieved, restore the quotation with the exact wording and add Savlov to the
bibliography.

**7. §7 — the uncited opening paragraph and the *Film Comment* anecdote (serious).** Add a note after
"sixteen placements argued for one at a time":

```
[^66a]: Pierson, "Slacking Off"; Macor, *Chainsaws, Slackers, and Spy Kids*, 104, 106–7; Box Office
Mojo, release record rl3815867905. Pierson's memoir is the only sustained account of a producer's
representative at work; there is no scholarly literature on the role, so the 1991 half of this section
rests on a participant.
```

And for the anecdote, keep the disagreement instead of resolving it:

> The earlier gate had responded — Robert Horton's paragraph in *Film Comment* reached Michael Barker,
> who telephoned his Austin relatives to ask whether the Dobie sellouts were real, though Pierson says
> Barker had already made that call.[^66b]

**8. §3 — the vacancy figures have no note (serious).** Attach note 29 to the sentence that uses them,
or extend note 30:

```
[^30]: Dallas and Houston rental vacancy rates from the same table as note 29. Enrollment: U.S.
Department of Education, NCES, IPEDS Fall Enrollment 1989, file EF1989_A, UNITID 228778 (27,100 +
23,145).
```

**9. §7 — name the vice-president (moderate, and it strengthens the section).** The whole paragraph
turns on address being possible, and it currently withholds the address. `research/deep/2026-08-01_s7.md`
has her, verbatim from Macor p. 113: "Susan Blodgett, vice president of Orion's Home Video division."

> Linklater and Pierson took the video release to Susan Blodgett, vice-president of Orion's home video
> division, and lost.

and, at the section's end:

> That last sentence is the modern counterpart of Susan Blodgett saying no. She said no, and Linklater
> knew whom to ask.

**10. §6 — throat-clearing (moderate).** Delete "What is actually measured is this." and begin the
paragraph "Sermin Ildirar and Louise Ewing ran the classic Kuleshov montages…"

**11. §6 — two unglossed terms (moderate).**

> The same team then complicated their own result. Adding sound recorded inside the scene — a voice, a
> door, traffic — let first-time viewers manage transitions that had defeated them in the silent
> studies, including cuts that jump the camera to the far side of the action, which experienced viewers
> read without noticing.

**12. §3 — one unglossed term (moderate).**

> Giordano Mion and Paolo Naticchioni add a complication worth keeping: in bigger markets, like matches
> with like *less*, not more.

**13. §3 — the metaphor carrying the claim (moderate).**

> Cheap space leaves people with hours nobody has a claim on, and those hours are what this film is
> about.

**14. §3 — "thirty years later" (moderate).**

> Reuben A. Buford May finds the same discretion at work in commercial gatekeeping in 2022, Austin
> included.

**15. Note 47 — sourcing the interface claim (moderate).**

```
…The driver-facing interface has changed substantially since: Uber Blog, April 8, 2021 ("You'll always
see fare, destination, and distance if you accept 5 of your last 10 trips"), and Uber Blog, March 5,
2025 ("we'll show the cross streets closest to the pickup and dropoff points").
```

**16. Note 18 — disclose the second-hand definition (moderate).**

```
[^18]: Scott L. Feld, "The Focused Organization of Social Ties," *American Journal of Sociology* 86,
no. 5 (1981): 1015–1035. The definition is Feld's at 1016; I have it from five independent quoting
sources rather than from the article, which I could not obtain.
```

**17. §1 — source the counts (minor).** Add to note 2: "Handoffs and repeat encounters counted from
[edition], [date]; I make it about three dozen transfers and no character who appears in two separated
scenes." Add a note 1a fixing the viewing copy.

**18. Note 4 — complete the enumeration and carry the countervailing sentence (minor).**

```
…and Jonathan Rosenbaum, "Slacker," *Chicago Reader*, August 23, 1991; Hinson is at note 5. The
*Variety* notice comes closest to a comprehension complaint — "interest quickly rises and falls by
virtue of who happens to be on screen" — but that is a complaint about attention, not about knowing who
is on screen. The 1990–91 trade press, the *Village Voice* and *Sight and Sound* could not be reached.
```

**19. §7 — "described above" (minor).** Covered by revision 4.

**20. §2 — passive (minor).** "The setting was named in 1981 and has been studied since" → "Feld named
the setting in 1981 and sociologists have worked on it since."

**21. Mechanical sweep (minor).** Serial comma into the body; subtitles restored in nn. 20 ×2, 23, 54,
58, 61, 62, 70; *Jaws* italicised in n. 62; *beschikking* italicised in n. 52; the comma inside the
inner quotation in n. 9; the spaced ellipsis in n. 5; "Ramírez Berg" for "Berg" in n. 43; the *Variety*
date in n. 4; the accession number in n. 68; "article 6" in n. 61; the second *Trends* issue in n. 28;
"3–4" or a settled "3" in n. 22; "158, 164" in n. 33; "62, and 53 for the functions" in n. 38.

---

# Verdict

**Major revisions.** Not because the chapter is unsound — the argument is in good order and the
apparatus is unusually well built — but because three of the errors above are of a kind that costs a
manuscript its credit with a reader who checks one thing at random. A wrong first name, a wrong page
locator, and a list that counts to three in one section and four in another are all findable in minutes.
The fixes are almost all mechanical; the exception is note 37, which needs a page retrieved, and §7's
opening, which needs a note written.

# Biggest genuine strength

The note-to-claim discipline where it holds is better than most published work in this field. Note 61
scopes a widely misquoted figure correctly ("The figure is 25.1 percent for within-scene cuts") and the
body honours the scoping ("about a quarter of the cuts joining one view of a scene to the next"). Note 51
lets Dubal mark her own inference and stops there. Note 54 says "abstract" rather than pretending to a
page. Note 43 says outright which half of the distinction is Ramírez Berg's and which is the author's:
"the distinction between story-world chain and presentation-order walk is mine." Note 1 records a
disagreement between the print and Criterion's website and declines to explain how it arose. That is a
scholar telling you where the floor is, and it is rarer than it should be.

# The one thing only the author can supply

**The disc, a stopwatch, and a note that says which copy.** Four claims in the body are counts off the
screen — about three dozen transfers, ninety-eight roles of whom almost none meet twice, roughly two
minutes on the arrest, the oblique-strategies card — and no one but the author can make them. They are
also the only claims in a chapter of 71 notes that currently rest on nothing. Watching it once with a
notepad closes them all, and closes the outline's standing author-only item at the same time. The
*Austin Chronicle* page behind note 37 is the same kind of job: one retrieval, ten minutes, and the last
unverified quotation in the manuscript goes away.

---

# VERIFY — what I could not confirm

Everything here is a request, not a correction. I did not retrieve these.

1. **Turan (n. 4).** `research/deep/2026-08-01_s1.md` confirms the chapter's longer rendering, including
   "for a few seconds or a few minutes," and notes the ellipsis elides "there are apparently close to
   100, and counting them is probably as good a way as any to pass the time." Verified in the project
   record, not by me against the *LA Times*.
2. **Moretti (n. 44).** The chapter prints network analysis making plot lose "its temporal dimension for
   ever." That string appears nowhere in the research files. What
   `research/deep/2026-08-01_s4.md` verifies at Pamphlet 2, p. 3 is different wording — "the edges have
   no 'direction'… I just couldn't find a non-clumsy way to visualize weight and direction" and "Time
   turned into space." The pamphlet is too large for my fetch tool. **Check this one before print.**
3. ***Papachristou* (n. 33).** The research record verifies "amenities of life" as the quoted fragment.
   The chapter prints "amenities of life as we have known them." The longer string is plausible and I
   could not confirm it.
4. **Chatman (n. 39), p. 134.** Confirmed in the research record at p. 134 by two independent citing
   works. Not confirmed against the book.
5. **Bordwell (n. 42).** The chapter's "*Slacker*. …" adds a sentence-ending period the outline's
   rendering ("*Slacker*…") does not have.
6. **Dubal (n. 51).** The chapter attributes "We have no way to judge the accuracy of this statement" to
   Dubal's own footnote. The first-person plural in a single-authored article is odd; check whether the
   sentence is hers or quoted from a report she cites.
7. **Rosenfeld et al. (n. 23).** The outline renders *human* in italics inside the disintermediation
   definition; the chapter sets it roman. Check whether the emphasis is the authors'.
8. **Macor 113–14 (n. 67).** The 7,000 cassettes and 20,000 books are verbatim in the research record
   from Macor pp. 113–14, but the 20,000 figure there is Pierson speaking ("the number I always
   heard—20,000 copies"), and Pierson's own essay says "over 20,000." The chapter's flat "sold 20,000"
   sands off both hedges.
9. **Pierson's publisher.** `outline_v3.md` gives Hyperion, New York, 1996; `research/deep/
   2026-08-01_s7.md` gives Faber, 1996. Settle it.
10. **Gagrčin et al. and Oeldorf-Hirsch & Neubaum issue years.** Crossref gives online-first dates of
    2024 and 2023 against the chapter's issue years of 2026 and 2025. The volume/issue numbers support
    the chapter; confirm the issue years on the journal's own pages.
11. **Smith, Essex & Bedford (n. 65).** Crossref's deposit carries no subtitle. The outline says "The
    subtitle is part of the title of record." Confirm against Berghahn.
12. **"MoPac"** (§3). The Austin expressway is normally set MoPac, capital P. The chapter has "Mopac."
13. **"The first book of film psychology"** (§6). An unsourced superlative about Münsterberg. Common,
    probably right, and worth either a source or a hedge.

**Closed this pass, so the author can stop worrying about them.** Binns et al.: the ACM deposit gives
"Jake Stein," not "Jake M. L. Stein" — the outline's open check resolves in the chapter's favour.
Castillo: *Econometrica* 93, no. 5 (2025): 1811–1854 confirmed. Ramirez (n. 11): the *Places Journal*
deposit has no accent, so the chapter's spelling is right. Macor ch. 4 at 87–114, Feld at 86(5):
1015–1035, Kwon et al. at 46(6): 1092–1120, Bengesser et al. at 31(5): 1511–1531, Loschky et al.,
Besbes et al., Mion & Naticchioni, Obstfeld, Gould & Fernandez, Hansen, Schegloff, Thomson-Jones,
Slugan, Boom and Heiland all confirmed against Crossref exactly as the chapter has them.
