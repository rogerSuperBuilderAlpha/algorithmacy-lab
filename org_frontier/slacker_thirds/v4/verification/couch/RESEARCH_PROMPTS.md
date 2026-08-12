# Deep research prompts — contemporary couch for Simmel, Royce, Reich

Six prompts, ordered by how much of the chapter's argument rests on them. Each is written to be run
as-is by a research agent or by a person with library access, and each returns the same artefact: a
dossier in the format of [`../../../research/deep/2026-08-01_s2.md`](../../../research/deep/2026-08-01_s2.md),
whose findings carry a confidence, a vote, verbatim evidence, and a stated relation to a numbered
row of [`../CONTEMPORARY_COUCH_GAPS.md`](../CONTEMPORARY_COUCH_GAPS.md).

**Follow-on packet (2026-08-12 full read):** citation/support gaps that are *not* classic-theory
couch—anonymous reviews, locations/stamp, Reich digest overclaims, FX/banned-edge notes, literacy
lag, rideshare assent—live in [`../SUPPORT_GAPS.md`](../SUPPORT_GAPS.md) with prompts
[`SUPPORT_RESEARCH_PROMPTS.md`](SUPPORT_RESEARCH_PROMPTS.md) (P7–P12).

Phase 5 verification already checked the chapter's primary citations against their sources and found
no contradicted source, no reversed thesis, and no fabricated quotation. That is not the question
here. A referee in sociology, pragmatism, or law will not ask whether Simmel wrote the sentence.
They will ask who else has read it that way, and on the thirty-one rows in the gap list the chapter
cannot yet answer. These prompts go after the answer.

---

## Rules that apply to every prompt

**State the scholar's own thesis before comparing it to ours.** Every row in the gap list is
interpretive, so every check runs the shape of [`../results_schegloff.md`](../results_schegloff.md):
a retrieval log, then the source's thesis stated from retrieved text, then the comparison — in that
order. Reversing the order is how a verifier reads our gloss back into someone else's book. This is
the single rule the whole regime is built around, and this project has already paid for it: a
verdict recorded in `outline_v3.md` travelled through four review panels unread and produced a fatal
error, because every pass read the project's summary of a source rather than the source.

**Verifiers see the claim and the citation, nothing else.** No outline, no earlier dossier, no
gloss file, no draft of the chapter. `v4/extract/*_GLOSSES.md` is quarantined and stays quarantined.

**Verification is not optional.** Every returned citation carries author list, exact title, journal
or press, volume, issue, pages, year, and DOI where one exists, each checked against the publisher
record or Crossref (`https://api.crossref.org/works/{DOI}`). Web-search summaries are leads, never
sources. Say what read depth was reached — full text, abstract, or metadata only — and never assert
a specific claim from an abstract alone. Meyer et al. was attributed to an abstract that does not
contain the finding, and a verifier caught it at p. 1733.

**Carry the provenance class.** Every finding is marked against the ladder in
[`../../factbase/CLAIMS.md`](../../factbase/CLAIMS.md): `A` source retrieved and verbatim on record;
`B` convergence-verified across secondary sources with the primary unopened; `C` second-hand,
abstract-only, single-lens, or metadata-only; `D` needs a person — a library, a paywall, a browser;
`X` forbidden or explicitly unverified. A and B may be written from. C must be marked second-hand in
any draft. D may not be asserted at all.

**Three lenses, and record the disagreement.** Each surviving claim is checked by three independent
verifiers prompted to refute it, and survives at two of three. Print the vote. Where the lenses
split, state the split in the confidence line rather than smoothing it — in the s2 dossier the
dissenting lens on Finding 1 was right, and it changed the section's opening move.

**Report the misses.** Close every run with `Absences (searched for, not found)`, naming what was
searched and what did not turn up. For four of these six prompts a named absence is the most
valuable thing the run can return, because the chapter's claim is that nobody took the deferred case
up. An absence stated precisely converts a gap row to `own-as-author`; silence converts nothing.

**Distinguish evidence from framing.** For each source say whether it gives the chapter (a) couch it
can lean on, (b) a framing it must argue past, or (c) both. The s2 dossier's verdict vocabulary
applies: SUPPORTS, REFUTES, COMPLICATES, BOTH.

**A negative result lands.** A prompt that finds nothing still writes its dossier, still lists its
absences, and still dispositions its rows. Do not pad a thin run with adjacent material.

### Retrieval notes and traps

The chain that works, in order: Crossref, Unpaywall, the Internet Archive and Wayback APIs, Scholar
Gateway `semanticSearch`, Consensus, DuckDuckGo HTML through a text proxy. OpenAlex returns
"insufficient budget," Semantic Scholar and the Google Books API rate-limit, Google Scholar and OATD
return 403. WebSearch has a hard budget and a prior run on this chapter exhausted 200 of 200 before
its five angles had run — spend it on disambiguation and named-work lookups, not on browsing.

- **Wolff's 1950 translation is lending-locked** — 401/403 on direct file access, no snippet view,
  zero indexed hits for its exact English wording. Check against the 1908 German (socio.ch, or the
  archive.org OCR of `soziologieunters00simmrich`) and say which text was read.
- **archive.org OCR renders long-s ligatures as `dafs`, `aufserhalb`, `zusammenschliefst`.** Printing
  those quotes the scanner, not Simmel. Normalize to ß and note the provenance.
- **Page markers in OCR sit after the text they number.** The Wolff check closed with a locator trap
  once already.
- **Disambiguate names before spending budget.** A Consensus query on this chapter returned twenty
  results, twelve of them about Andrew Linklater the IR theorist. Royce, Reich, and Small are all
  common names; Charles A. Reich is not Robert Reich, and Josiah Royce is not the Royce of
  Rolls-Royce corpora.
- **German-language scholarship is the point, not a bonus,** for prompts 1 and 2. Search the German
  strings. `Figur des Dritten`, `Theorien des Dritten`, `Tertiarität`, `der Dritte`,
  `gesellschaftsbildende Vermittlung`, `Zweierkonfigurationen`. The English-language reception
  systematically drops this material.
- **Law reviews are largely open** through HeinOnline mirrors, `openyls.law.yale.edu`, SSRN, and law
  school repositories — prompt 5 should have the best hit rate of the six. German monographs and
  pragmatism collections will have the worst; expect a class-D residue there and name it.

---

## P1 — Simmel's deferred third: Distanz, the invisible church, and whether *Streit* redeems the promise

*Covers A-S1 through A-S6, A-S10, B-S2 through B-S4. Blocking: §§1–3 open on this.*

> Georg Simmel opens the triad chapter of *Soziologie* (1908, p. 103; Wolff 1950, p. 145) by naming a
> third that is not a pair-broker — a power outside the parties whose common relation to them
> establishes a unification among them, exemplified by an alliance of states against a common enemy
> and by the invisible church that unites the faithful through their equal relation to the one God.
> He calls this the *gesellschaftsbildende Vermittlung eines dritten Elementes*, says it is *in
> späterem Zusammenhang zu behandeln*, and gives his ground for setting it aside: the third stands at
> such a *Distanz* that no properly sociological interaction encompasses all three alike, leaving
> only *Zweierkonfigurationen*.
>
> **Find the contemporary scholarship on that passage.** Five questions, in priority order:
>
> 1. **Does anyone notice the promise is not kept?** A project full-text search of the 1908
> *Soziologie* finds the phrase *gesellschaftsbildende Vermittlung eines dritten Elementes* only at
> p. 103. Independent confirmation of the non-return, or a scholar's notice of it, is the single most
> valuable thing this prompt can return.
> 2. **How is the deferral's ground read?** The chapter glosses *Distanz* as the third's not knowing
> which two parties will meet — non-knowledge of particulars. The competing reading is narrower:
> Simmel is only saying there is no genuine three-way interaction, which is a question about whether
> this is a triad at all. Which reading do commentators take, and does anyone take the chapter's?
> 3. **Does *Der Streit* fulfil the promise?** The chapter says the conflict essay belongs to the same
> family — conflict as already a form of association, *man vereinigt sich, um zu kämpfen*, common
> opposition as cement — but is not the deferred analysis. Has anyone argued that *Streit*, or money,
> or the stranger, or spatial order, redeems the p. 103 deferral? Has anyone argued it does not?
> 4. **What is this figure called by others?** The chapter's "deferred third" is its own construct.
> Find the standing names: *Figur des Dritten*, *Theorien des Dritten*, Tertiarität, the institutional
> third, the abstract or generalized third, the distant mediator.
> 5. **Is the invisible church read as unfinished membership theory** (the chapter's A-S10 split, where
> Simmel supplies structure and Royce supplies membership), or as already sufficient for belonging?
>
> Go after: the German *Theorien des Dritten* strand — Bedorf, Fischer and Lindemann's 2010 collection
> and Eßlinger et al. on *Die Figur des Dritten*; the Simmel-Handbuch and the Gesamtausgabe editorial
> apparatus to GSG 11, which is where an editor would flag a promise Simmel left standing; Olli
> Pyyhtinen, who writes directly on Simmel's third and on more-than-human thirds; Gregor Fitzi;
> Natàlia Cantó-Milà and Christian Papilloud on Simmel's relationism, where *Distanz* is a technical
> term; Donald Levine on Simmel's forms and on the American reception; Volkhard Krech and Horst Jürgen
> Helle on Simmel and religion, for the invisible church; Lewis Coser 1956 as the canonical *Streit*
> reception, and whoever has revisited it since.
>
> **What counts as a hit:** a named scholar, quoted verbatim with a locator, who either (a) records
> that the deferral is never redeemed, (b) reads *Distanz* as non-knowledge of particulars, or (c)
> claims some later text fulfils it. **What would falsify the chapter:** a commentator showing Simmel
> does return to the *gesellschaftsbildende Vermittlung* elsewhere in the 1908 *Soziologie* or in the
> *Grundfragen*. Look for that specifically, and if it exists say so plainly — §§1–3 rest on the
> non-return and would need rebuilding, not hedging.

## P2 — Who claims the deferred case: brokerage against the institutional and impersonal third

*Covers A-S7. Falsification probe.*

> The chapter claims that contemporary sociology followed the thirds Simmel kept rather than the one
> he postponed, and that neither Burt's structural holes nor Obstfeld's *tertius iungens* matches the
> Distanz case, because both are brokerage between a known pair by a node in the network.
>
> **The job of this prompt is to find the person who does claim the deferred case, and to state the
> negative precisely if that person does not exist.**
>
> 1. **Confirm the exclusion in the brokerage literature's own words.** Kwon, Rondi, Levin, De Massis
> and Brass (2020) define brokerage as one actor connected to two unconnected alters and state
> exclusion criteria that drop non-human networks and networks outside a work or professional context.
> Get the criteria verbatim with page numbers. Then Burt 1992 and 2005, Obstfeld 2005,
> Obstfeld/Borgatti/Davis 2014, Gould & Fernandez 1989, and Stovel & Shaw's 2012 *Annual Review*: is
> every formal mediation type in these a pair-brokering type? Does any of them admit a third that
> does not know which pair it joins?
> 2. **Then look for the claimant.** Who has argued that a distant, impersonal, or institutional third
> is the Simmelian case that brokerage research left behind? Candidates: Ajunwa's *tertius bifrons*
> (2020) — but check the Simmel genealogy, which an earlier run found to be wrong; Stark & Pais 2020;
> Stark & Vanden Broeck 2024; Kellogg, Valentine & Christin 2020; Fuhse 2013 on concrete versus
> abstract thirds; Lindemann; the *Theorien des Dritten* strand carried over from P1.
> 3. **Check the citation gap.** An earlier run found that the brokerage tradition and the German
> third-theory tradition do not cite each other, and that this is checkable from the PDFs. Re-check it
> and quantify it — a stated, checkable absence is stronger couch than a hedge.
>
> **What counts as a hit:** a scholar who explicitly claims to take up Simmel's deferred third, or who
> explicitly notes that brokerage theory cannot reach it. **What would falsify the chapter:** an
> established line — institutional theory, infrastructure studies, media sociology — that already
> occupies this cell under another name. If it exists, A-S7 does not get hedged; it gets rewritten to
> cite it.

## P3 — Royce's community of memory: meeting, communication, and whether loyalty is constitutive

*Covers A-R1 through A-R4, A-R6 through A-R12, B-R1 and B-R2. Blocking: §§3 and 7.*

> Josiah Royce defines the community of memory and the community of expectation in *The Problem of
> Christianity* (1913), II, 50–51 (1968 reset, p. 248), and states three constituting conditions at
> II, 60–61, II, 67, and II, 68 (1968: 253, 255, 256). The chapter's slogan is that Royce named
> membership among people who never meet face to face, on the strength of the Maori passage at II, 46
> where members may be aloof or even enemies. But the condition at II, 67 requires "distinct selves
> capable of social communication, and, in general, engaged in communication," and Royce frames
> membership as holding among contemporaries at II, 44 and II, 49.
>
> **Three questions, each attached to a specific gap row:**
>
> 1. **Are the three conditions jointly necessary?** (A-R3.) The chapter compresses them to "shared
> relation to an outside past or future is enough for membership," which drops the communication
> condition. What do Royce scholars treat as jointly necessary? If the answer is all three, A-R3 is a
> `reframe`, not a hedge, and the chapter's §3 bridge has to be rebuilt on the conditions Royce
> actually states.
> 2. **Does membership survive the absence of meeting?** (A-R1, A-R6.) Distinguish three things the
> chapter currently runs together: never meeting, not being contemporaries, and not communicating.
> Royce's aloofness passage licenses the first. Does any scholar license the second and third?
> 3. **Is loyalty constitutive of community, or only of conscious community?** (A-R9, A-R10.) The
> chapter uses loyalty to block equating a platform with a community. If loyalty turns out to be a
> condition of *conscious* community only, the block weakens and the chapter must say what remains.
>
> Also settle: whether anyone has applied Royce to ephemeral, place-based, or single-day communities
> (A-R4); to reception and memory communities, which is where the Erickson/Long place-myth join at
> A-R8 would land; and to digital or platform membership, which A-R10 through A-R12 need. On A-R12,
> the chapter uses "membership" in a non-Roycean sense after the Royce section — check whether the
> platform-studies literature on enrollment and assent gives that second sense a name, so the
> equivocation can be resolved by vocabulary rather than by hedging.
>
> Go after: John E. Smith, *Royce's Social Infinite*; Frank Oppenheim's trilogy; Jacquelyn Ann K.
> Kegley on genuine communities and on Royce applied to contemporary community forms; Randall Auxier;
> Kelly Parker, including the Stanford Encyclopedia entry; Mathew Foust, *Loyalty to Loyalty*; Dwayne
> Tunstall; Griffin Trotter; and the runs of *Transactions of the Charles S. Peirce Society* and *The
> Pluralist*. Robert Bellah and colleagues took "community of memory" into *Habits of the Heart*, and
> that is the largest reception surface Royce's phrase has — check what they kept and what they
> dropped, because a referee who knows the phrase will know it from there.
>
> **What counts as a hit:** a scholar stating, with a locator, what the three conditions require of
> each other. **What would falsify the chapter:** a consensus that Royce's communication condition is
> constitutive and non-negotiable, which would make "membership without meeting" a misattribution
> rather than a compression.

## P4 — Can a medium interpret? Royce, Peirce, and non-personal interpreters

*Covers A-R5, A-R6, B-R3, B-R4.*

> Royce holds that interpretation is a triadic relation irreducible to dyads (II, 140 and II, 142;
> 1968: 286–87), with three terms — interpreter, object interpreted, person addressed — and he holds
> that all three are selves (II, 148–49 and II, 211; 1968: 289, 315). The chapter seats the camera in
> the interpreter's place and flags the extension as its own. Note [^10] already records that Royce's
> Colorado Canyon passage, the closest he comes to an impersonal interpreter, is subjunctive
> throughout.
>
> **Find the company the chapter does not yet have.** Who else seats a non-mind, a medium, or a
> machine in the interpreter's position rather than in the position of the object interpreted? The
> distinction matters and most candidates fail it: a camera as something we interpret is unremarkable;
> a camera as the term that interprets one party to another is the chapter's claim.
>
> **The author has ruled out actor-network theory.** Do not return Latour, Callon, or Law as the
> couch. Return instead: the Peircean literature on interpreter versus interpretant, where the
> interpretant is explicitly not a person — Colapietro, Short, Winfried Nöth on machine semiosis and
> on human communication versus machine semiosis, Peter Skagestad on thinking with machines and on
> Peirce's inkstand; biosemiotics and cybersemiotics, where interpretation is attributed to non-human
> systems as a matter of course — Hoffmeyer, Deacon, Søren Brier's *Cybersemiotics*, Kull; and the
> Royce–Peirce interpretation scholarship on whether Royce's own restriction to selves is load-bearing
> or incidental.
>
> Rivals worth naming even though they are not Roycean: Hutchins on distributed cognition, Clark and
> Chalmers on extended mind, Sirůček 2025 on apparatus and algorithmic interpellation. Say what each
> would cost the chapter if adopted instead.
>
> **What counts as a hit:** a scholar who puts a non-person in the interpreter's seat and argues for
> it. **What would falsify the chapter's honesty flag:** finding that the extension is standard and
> uncontroversial in Peirce scholarship, in which case A-R5 stops being "extension is mine" and
> becomes a citation.

## P5 — Reich's reception: what he is taken to have named, and who carried it to private doors

*Covers A-C1 through A-C8, B-C1 through B-C4. Blocking: §4.*

> Charles A. Reich's "The New Property" (*Yale Law Journal* 73, no. 5 (1964): 733–787) supplies the
> chapter's §4: the grantor-power sentence at 751, the livelihood locus at 741, the demand at 783 that
> undisclosed reasons "should no longer be tolerated," and the sentence at 786 that private forms —
> franchises, equities, utilities, "status in private organizations" — "may need added safeguards in
> the future." The chapter builds a four-power taxonomy on this (price, evaluate, remove, withhold),
> marks the taxonomy as its own, and then says Reich named the legal form of the dependence behind
> those powers.
>
> **Two halves, and the first is the hinge.**
>
> 1. **Doctrinal reception: is Reich read as naming a form or as making a demand?** The chapter's A-C1
> and A-C5 turn on this. Reich's 783 passage is a normative demand about undisclosed reasons; the
> chapter reads it as stating a power. What does the reception literature say Reich named? Go to
> *Goldberg v. Kelly* (1970) and what it took from him; *Board of Regents v. Roth* (1972) and the
> entitlement doctrine; *Arnett v. Kennedy* and the bitter-with-the-sweet problem; William Van
> Alstyne's "Cracks in 'The New Property'"; Henry Monaghan's "Of 'Liberty' and 'Property'"; Jerry
> Mashaw's *Due Process in the Administrative State* and *Bureaucratic Justice*; Cynthia Farina;
> Thomas Merrill; Reich's own "Beyond the New Property" and the twenty-five-year symposium. Return the
> standard secondary digest of the article's institutional claims — counterparty writes the terms,
> changes them, decides disputes in its own forum, owes no procedure — with page pins, because A-C4
> currently paraphrases without them.
> 2. **The private extension.** Reich wrote about government largess; the chapter applies the structure
> to private doors on the strength of 786. Who else has? Elizabeth Anderson, *Private Government*;
> Julie Cohen, *Between Truth and Power*; Frank Pasquale on functional sovereignty and the black box;
> Kate Klonick, "The New Governors"; Rory Van Loo on federal rules of platform procedure; K. Sabeel
> Rahman on infrastructural regulation and the new utilities; Danielle Citron on technological due
> process and Citron & Pasquale on the scored society; Margaret Jane Radin, *Boilerplate*; Nancy Kim
> on wrap contracts; Salomé Viljoen; and the deactivation literature — Veena Dubal, Alex Rosenblat's
> *Uberland*. Which of these cite Reich, and which arrive at the same structure without him?
> 3. **Transferable versus non-transferable access** (A-C6). The chapter's guest-list-versus-stamp
> allegory says platform life inherits the grant and drops the demonstration. Find the property and
> contract theory of digital entitlements that governs it.
>
> **What counts as a hit:** a page-pinned secondary statement of what Reich named, and a named scholar
> who carries the grant structure to private platforms. **What would falsify a chapter move:** a
> reception consensus that Reich's contribution is precisely the normative demand and *not* a
> structural taxonomy, which would make A-C1's "named the form" an overstatement to be corrected
> rather than couched.

## P6 — The joins: city and camera as the deferred third, platform as grant plus membership plus Distanz

*Covers A-S8, A-S9, A-R4, A-R8, A-C6, A-C7, A-C8. Second falsification probe.*

> The chapter's own architecture, and the part no primary source can support. Four joins:
>
> 1. Strangers unified only by a common relation to a day, a city, and a camera have the
> deferred-third structure (A-S8).
> 2. The city supplies reach and the camera supplies selection, so the film already shows platform
> shape as a division of labour (A-S9).
> 3. A platform is a grant plus membership-without-meeting plus Distanz (A-C6, A-C7).
> 4. By 1964 three writers had stacked deferred-third structure, membership conditions, and grant form
> as prerequisites — a genealogy nobody has narrated (A-C8).
>
> **Has any of this been done already?** That is the whole question. Search for the film-as-coordinator
> claim, the city-as-outside-potency claim, the reach/selection division, and the 1908–1913–1964
> sequence as a narrated genealogy.
>
> Go after: Feld's 1981 focus theory, which pre-names the hosting mechanism and is already in the
> chapter's apparatus; Mario Small, *Unanticipated Gains*; Duranton and Puga on urban matching; Scott
> McQuire, *The Media City*; Sarah Barns, *Platform Urbanism*; Barbara Mennel, *Cities and Cinema*;
> Tarleton Gillespie on relevance and custodianship; Philip Napoli; the Erickson/Long place-myth line
> already cited at [^21], and the wider place-myth literature it belongs to.
>
> On A-R8, the specific question is whether later audiences taking a place-myth as their own has been
> analyzed as a Roycean community of memory by anyone at all, or whether the join is the chapter's.
>
> **What counts as a hit:** anyone who has made one of the four joins. **The expected result is
> mostly absence,** and an absence here is the finding: it converts these rows to `own-as-author`,
> which obliges the chapter to support each joint explicitly rather than to lean on a classic. Say so
> in those words where it applies, and name what each joint then needs.

---

## Disposition

Every run closes by writing its rows back into
[`../CONTEMPORARY_COUCH_GAPS.md`](../CONTEMPORARY_COUCH_GAPS.md) in that file's own vocabulary:

| status | means |
|---|---|
| `found` | contemporary couch exists and is verified; the dossier names the citation to add |
| `reframe` | the literature says something adjacent, and the chapter's sentence has to move |
| `own-as-author` | nobody has made this move; the chapter owns it and supports each joint |
| `open` | unreachable this pass; the row names what would close it |

A row left `open` without naming what would close it is an unfinished row, not a result.
