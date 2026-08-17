# Deep-research literature map, round 3 (2026-07-16)

Rounds 1 and 2 mapped the terrain and closed the trail of unverified anchors. Round 3 does something
different: it grounds the drafts themselves. Each of the nine posts now exists in a numbered draft, and
this round ran two agents over every one — a Fable grounding pass that re-checked each load-bearing claim
against the primary text, the secondary literature, and the repo, and an Opus adversarial pass that tried
to refute the grounding digest before it entered the library. Eighteen agents, nine posts, the full
`research/post{1..9}.digest.json` set. The corrections below are the checker's corrected verdicts, not the
grounder's first draft of them.

This file is a standing map, not a citation source. Page-numbered quotations behind a paywall were often
confirmed against reviews, repository scans, or the German *Werke* rather than the printed English page,
and the "verify before print" residue at the end lists what a drafter must still open.

**Verification key.** `[✓]` confirmed against a source this round · `[~]` real work, but an interior quote
or page rests on a secondary, not a fetched primary page · `[gate]` physical or paywalled check owed ·
`[✗]` refuted, or a correction to carry.

## The strategic finding still holds, and the round tightened it

The signature bridge — Hegel's "when is a many also a one" read against a causal-irreducibility / Φ
criterion — remains **genuinely unmade**, and the nine drafts hold the novelty claim at exactly the
altitude that makes it safe: homology of boundary, not identity of criterion, and never "Hegel anticipated
Φ." Every guard_check came back clean on anticipation. Where a draft's sentence drifted toward identity,
the checker caught it and named the fix. Post 2's close said a domination-held binding "leaves the same
mark on a cause-and-effect structure wherever it appears, and that Hegel drew that mark first and
hardest"; because "that mark" is defined two clauses earlier as the program's causal signature, "Hegel
drew that mark" half-credits him with the causal truthmaker. The one-word repair — Hegel drew that
*boundary* — keeps the bridge at homology. Posts 4, 5, and 6 carry anticipation-leaning openers ("He
does not anticipate a causal-irreducibility criterion... He replaces it" is the fixed form; "Hegel ran
that test in 1821, by hand" is the flagged one), and in each case the guard arrives, only sometimes too
late in the piece. The pattern across all nine is the same: the bridge is drawn correctly, and the risk
is local, editorial, and already flagged.

The round added a second, quieter confirmation. The closest published neighbors the drafts surface — Lazarus
2025 on Smith/Hegel social ontology, Christiaens 2025 and Taylor 2017 on republican exit/voice, Daniel
James 2020 on the state-organism — all draw the boundary in a **recognitive or normative** register. None
computes a partition-sensitive quantity over a cause-effect structure. The neighbors have gotten closer
since Round 1, and the gap they leave is still the series' whole reason to exist beside them.

## Cross-cutting findings

Four axes recur across the nine. Stating them once here keeps the per-post notes short.

### The causal-realist-vs-not axis, and why even the strongest ally stops short

Post 1 sets the frame: a metaphysical-revival reading of Hegel's *Logic* (Kreines, Stern, Taylor) versus a
non-metaphysical / normativity reading (Brandom, Pinkard, Pippin). The series needs the revival wing to
have a Hegelian target at all — "the true is the whole" has to name an ontology, not a stance. But the
revival reading is **explanatory**, not efficient-causal. Kreines's own term is "insubstantial holism"
(*Reason in the World*, ch. 7), and Yeomans glosses him as "metaphysically pluralistic, epistemologically
monistic." That hands a reviewer the ground/cause distinction against a partition-of-cause-effect reading.

Post 3 shows how far even the most ontologically committed ally goes and where it stops. Georg Sans reads
the Syllogism chapter as an ontological argument — "conceptual relations as such are real," the chapter
"aims at establishing the Concept as something objective, to wit really existing." Yet the page that
closes the gate is the one that limits him: "Subjectivity as well as objectivity are determinations of the
Concept as such and do not refer directly either to mind or to nature" (Sans 2018, p. 202, now pinned from
the Tübingen OA PDF). Sans's objective syllogism is real, but its reality is teleological and
self-realizing, and it refers to *neither* mind *nor* nature. It licenses "the syllogism is a real
structure of the whole." It does not license "a causal cause-effect structure whose irreducibility is
partition-sensitive." That last step is the series' own to make, in every post that leans on the ontology.
Pippin's *Realm of Shadows* reads logic *as* metaphysics, not deflationarily — so the "thin reading" the
drafts sometimes invoke as a foil is not Pippin's either. The axis matters because the drafts must never
let "real structure" quietly become "causal structure" on the strength of an anchor that refuses the move.

### The teleology threat lands on Posts 1, 4, and 6

Karen Ng's *Hegel's Concept of Life* (OUP 2020) and James Kreines's "The Logic of Life" (2008) are the
sharpest threat in the series, and they are threats precisely because they are also the anchors that let
Hegel win. Ng: inner purposiveness moves regulative→constitutive, life "opens up the space of reasons,"
the organism is its own end, a self-producing unity whose members are constituted by their role in its
self-production. Kreines: Hegel is a realist, not a regulativist, about living teleology — "we can have
objective knowledge of this natural teleology." The ground of the organism's irreducibility, on both
readings, is inner teleology and self-production, which a Φ measure **neither entails nor requires** (Φ
could score high for a system that is in no sense self-productive). The honest form of Hegel's win is that
he *replaces* the unity criterion with inner purposiveness — not that he anticipates a causal one, and not
that Φ was "really measuring" teleology all along. Post 4 makes this its content and stakes its one
original result on the crossing inside the chemical process (di Giovanni SL pp. 647–649), where Hegel's
own bookkeeping ("these three syllogisms fall apart") and the partition ordering dissociate; that crossing
is what makes the anticipation reading false rather than merely disavowed. Post 6 states the same gap as
HC1: a *Glied* is defined teleologically, by reciprocal contribution to the whole's self-maintenance
(Corti 2022, verbatim from the PMC OA text), while the partition test reads only resistance to a cut — the
overlap is extensional, the gap is direction-of-definition. Post 1 introduces the threat and concedes it
force; Posts 4 and 6 test it rather than assume it away.

### The standing cheap-test objection

Post 9 foregrounds the objection the whole program inherits: the operators and the power concept "may need
little of the Φ machinery to stand." The receipts cut both ways. Time-series proxies recover the
dyadic/triadic verdict only near chance (STRUCTURAL_FINDINGS #7: Φ_R rank-AUC 0.621, Φ_WMS 0.547, ≤0.63),
but a cheap **structural** proxy — total edge count — hits 0.966 in-family (q82), and a learned surrogate
scores 1.000 in-distribution while collapsing to 0.250 accuracy across sizes (q81). The answer the repo's
CLAUDE.md mandates is not to concede the demotion: the surplus Φ buys is structural (which members, how
much, and a cross-boundary binding a cheap test cannot see), and the exact-regime boundary is the finding,
not an embarrassment. The recurring guard risk across the series is **not** anticipation — it is the
author-voice temper paragraph tipping into self-defeat. Post 4's "a criterion that cannot be wrong because
it cannot be run," Post 6's lines 242–251, and Post 9's "a thin one to hang two years on" plus its sneer
at "the sanctioned line about principled exploration" all cross from stating the objection into endorsing
the demotion. Every one is fixable the same way: keep the objection at full strength, cut the
self-deprecating verdict, let the affirmative case in the next paragraph carry the answer.

### The homology altitude and its two guards, for the series

Two guards govern every post. **Guard one:** never "Hegel anticipated Φ" — the claim is homology of
boundary, not identity of criterion. Its failure mode is a slip toward identity, and it slips through
nouns, not arguments (Post 2's "mark," Post 8's "is *Beisichselbstsein*" downgraded to "objective
condition of"). **Guard two:** never demote Φ — no "calculator," "decorative," "hollow," "unnecessary," and
every scope-limit paired with the affirmative case in the same breath. Its failure mode is the temper
paragraph. Both guards held across all nine drafts. Neither holds automatically under editing: the
ladder-relative self-deprecation in several posts stays safe only while its paired affirmative clauses
survive the cut, so the standing instruction is — if a paragraph is trimmed, trim the self-deprecation
first.

## Per-paper residue

**Post 1 — Two Holisms.** Confirmed anchors: the five *PhG* Preface fragments (§§3/17/18/20), all
verbatim against the bilingual Pinkard text, and EL §135 (Wallace) as the lowest essential relation `[✓]`.
Sharpest threat: Ng's living-unity reading, which lands first here and which Post 4 later tests. Corrections
the verify pass caught: relabel the marxists.org source — it is the bilingual published Pinkard text, not a
"draft," so the wording gate downgrades to a pagination courtesy check `[✗→gate]`; and treat Taylor p. 242
at the same confidence tier as the other page gates rather than as harder-confirmed `[~]`. New scholarship:
Tononi & Boly, "IIT: A Consciousness-First Approach to What Exists," arXiv:2510.25998 (29 Oct 2025), IIT's
own ontological statement; and Barrett et al., "IIT: the good, the bad and the misunderstood,"
arXiv:2604.11482 (13 Apr 2026), a shield for the modest instrument framing `[✓]`. Load-bearing gates: the
five physical-book checks (Ng pages, Stern pp. 155–57, Malabou p. 134, Pinkard pagination, Kreines p. 9),
plus the do-not-attribute on Yeomans (below). Watch: "mine knows nothing at all" concedes more than IIT
claims (Tononi & Boly read the Φ-structure as intrinsic existence) — a deliberate choice that must not
harden elsewhere into "Φ is a blind mechanical number."

**Post 2 — Master and Slave.** Confirmed anchors: Pippin 2011 (authority in acknowledgment, p. 90) and
Brandom 2019 (the "mirror of morons," p. 342), and the finding that the structural self-defeat reading is
*mainstream*, held from Kojève through Brandom — not the program's discovery `[✓]`. Sharpest threat:
Cunniff 2026 ("The Master's Problem," EJP, doi 10.1111/ejop.70089), who denies there is any dissolution —
the master wants "trembling obedience," not sincere endorsement, and "gets precisely the recognition he
wants," relocating the self-conflict to a King Midas means-end structure; Saunders 2026 (*Proc. Aristotelian
Soc.* 126(1): 39–57) draws the moral: "what's wrong with the master is not that they undermine themselves,
it's that they fail to respect others." A causal test inherits this desire-relativity, along with Wood's
community of masters and Fanon's master-who-wants-work, rather than escaping it. Correction: "Hegel drew
that mark" → "that boundary" (the one identity-drift sentence in the post) `[✗]`. New scholarship: Ng 2024,
"Fanon and Hegel on the Recognition of Humanity" (*Hegel Bulletin* 45(3): 571–597, doi 10.1017/hgl.2024.25,
OA), which pressures the flat "Fanon made the same puncture" framing and — since Ng is the series' named
threat author — offers a one-clause inoculation; Reichl 2026 (EJP 34(1): 152–162) as optional company;
Badenhorst, "Fanon, Hegel, and the Problem of Reciprocity" (*Hegel Bulletin*), surfaced but `[unverified]`.
Load-bearing: the two-channel verdict (recognition channel self-liquidating, labor channel real
coordination) rests on ¶190 and the Reconstruction record (Ransom & Sutch, Foner, Du Bois) and survives
whatever the master wants — it is what holds the post up if Cunniff is right. Gates: Saunders p. 50/p. 55
exact wording, Cunniff Early-View pins, and the unbuilt n=3 master–slave–world model, until which the
body's analogy flag must stay.

**Post 3 — The Syllogism.** Confirmed anchor: Sans 2018, now fully page-pinned from the Tübingen OA PDF
(the mind-or-nature quote at p. 202 closed the last gate) `[✓]`. Threat: Stein 2016, who makes the
syllogism derivative of the Concept — it "might show how and that they relate but it will not tell us what
they are." Corrections: the state-triad is EL **§198R** (the Remark, B&D p. 273), and v5's "fix" to the
main paragraph was a mis-correction — Sans's own citation "§ 198 Remark; 273" settles it; propagate to
Post 6 `[✗]`. The flagged clause "no party is a veto" is unbacked (q112 shows every core party of the
mediated triad holds a veto), and the checker further caught that the digest's proposed replacement "even
thirds" is *also* unbacked — use "even shares" (q149 ring spread 0.000; q113 all-required), never "even
thirds" `[✗]`. And the di Giovanni p. 588 sentence's front clause is unverified; quote only the fragment
"everything rational is a syllogism" `[gate]`. New scholarship: none newer than 2026-07-10; the only new
artifact is the Sans OA PDF itself. Load-bearing: the move from "objective syllogism is really existing" to
"partition-sensitive causal structure" is the series' own, made explicitly in "The Move the Resemblance
Does Not License."

**Post 4 — The Ladder (mechanism / chemism / teleology).** Confirmed anchors: the di Giovanni SL crossing
exhibit (pp. 645–649) verbatim, Kreines 2008, and — an upgrade this round — both B&D Encyclopedia pins
(§194 Add. 2, §204 Remark), verified verbatim against the actual B&D text, so only the print page numbers
(270, 277) remain `[✓]`. Sharpest threat: Ng 2020, on whom the no-anticipation guard rests, with Ebeturk
2023 (teleology "misplaced," a direct passage from chemism to life) recast as dissent, not concession.
Corrections the verify pass caught, both missed by the grounder: Koch's p. 149 quote is wrong — she wrote
"structures of external purposiveness **provide the conditions for the individuation of** mechanical
objects," not "constitute mechanical objects," a distinction Koch is deliberate about `[✗]`; and the
digest's own §213-boundary entry mislabels di Giovanni SL pp. 268/282 for what is a **B&D Encyclopedia**
locus, and marks "verified" what should be "gated" `[✗]`. New scholarship: the "Hegel and Teleology"
special issue (*Hegel Bulletin* 44/1, 2023, eds. Maraguat and Kreines) as framing context; a Ng "The
Objectivity of the Concept" lead `[unverified]`; a PhilEvents workshop, flag-only. Load-bearing: the
crossing inside chemism is the paper's one original result — remove it, or show it rests on an uncomputed
cross-system comparison, and the paper collapses to "our formalism is decidable and Hegel's is not," which
is table stakes; the owed acid–medium–base toy is the computation that would close it. Author-only: the
temper paragraph in "What the Bracketing Buys" must be ratified or softened.

**Post 5 — Interdependence Without Unity.** Confirmed anchors: the PR §§182–189 loci (Wood/Nisbet), Waszek
1988 for the Scottish reception, and the quorum receipts (seed 11, 400 forms: k=1 triadic 12/400, k=2
0/400, k=3 12/400, S the veto player in every integrating draw) `[✓]`. Threat: Kain 2015 reads the
deficiency as economic-distributive, not structural non-wholeness, and holds that Hegel *has* a workable
social-democratic remedy; Lazarus 2025 is the published recognitive counter-reading a referee would wield.
Corrections: the Smith pin-factory quote is trimmed without an ellipsis (restore "could scarce, perhaps,
with his utmost industry, make one pin in a day") `[✗]`; a second Smith slip the grounder missed — "ten
workers, each performing a single narrow operation" overstates Smith, whose ten men split ~18 operations,
"some... two or three distinct operations" each `[✗]`; "Ferguson, who supplied the term 'civil society'
itself" is too strong → "whose *Essay* gave the tradition its title," cited to Waszek `[✗]`; and three
anticipation-leaning openers land before the guards — pull one guard forward `[✗]`. New scholarship:
Lazarus, "From the invisible hand to the rabble" (*CJE* 49(6): 1163–1185, doi 10.1093/cje/beaf046), the
nearest published neighbor, which must be named; Herzog, *Inventing the Market: Smith, Hegel, and Political
Theory* (OUP 2013); Ruda, *Hegel's Rabble* (Continuum 2011); Ferro 2023 as optional positioning `[✓]`.
Load-bearing lab upgrade: `studies/coordination_logic_atlas/FINDINGS.md` gives a deterministic cross-n law
(interior thresholds factor to exactly zero at n=3,4,5; k=1 and k=n reach Φ=n−1 with the full party set in
core), which upgrades the one-seed 0/400 to a registered law.

**Post 6 — Parts and Members.** Confirmed anchors: Corti 2022 (both quotes verbatim from the PMC OA text,
closing the Springer paywall gate) for the self-maintenance definition of a member, and the six lab
receipts (idle principal contracts the core to {S,P}; 115/115 argmax-Shapley; the cyclic triad's 0/78, top
share 0.333, 13% vs 10%) `[✓]`. Threat: Ng 2020 and Kreines — realist teleology as the ground Φ neither
entails nor requires, the HC1 gap the draft rests on. Top correction: the state-as-three-syllogisms passage
is the **Anmerkung (Remark) to EL §198**, not the main paragraph — draft v3 introduced this error, and it
must be reverted; same §198R correction as Post 3, and it propagates `[✗]`. New scholarship: Daniel James,
"Social Organisms: Hegel's Organisational **View** of Social Functions" (Routledge 2020, doi
10.4324/9780429435393-12), a convergent political-angle anchor for the teleological-definition side — note
PhilPapers mis-indexes it as "Theory," so do not "fix" it the wrong way `[✓/gate]`. Author-only: the temper
paragraph (lines 242–251) leans self-defeating — keep the concession language ("reads only the symptom,"
"brackets teleology," "decoration") pinned to the Hegel bridge, never onto Φ. Minor: the draft's §198
rotation assigns middles P, U, I where Hegel's canonical order is P, I, U — all three still mediate once, but
a referee may note the departure.

**Post 7 — The Necessary Middle (Korporation).** Confirmed anchors: Heiman 1971 (paraphrase-only, since the
Round-2 verbatim was likely fabricated), and the `irreducibility_catalog` and `dual_function_entities`
receipts, all verbatim (51 entries = 38 real + 13 literature types; necessary 13 / contingent 25 / partial
7 / reducible 6; margins 2.0 / 0.0 / 1.585 / 0.0) `[✓]`. Threat: the recognitive rival family (the
corporation confers a normative-attitudinal good invisible to the instrument), sharpened by Ruda's rabble —
integration without standing, so "necessary middle" must be scoped to "those the corporation admits."
Corrections the verify pass downgraded from the grounder's "verified" to gates: Herzog 2015's "Hegel Society
of America Proceedings 22" is unconfirmed — cite the Buchwalter volume (*Hegel and Capitalism*, SUNY 2015,
pp. 147–162) `[✗]`; Heiman pp. 111–135 is a plausible-not-verified span `[gate]`; and James 2017 "collects
the critical debate around the passage" overstates → "around the *Philosophy of Right*" `[✗]`. Repo fix: the
passage card mis-pins "second family" to §253R; it is §252 `[✗]`. New scholarship: Ruda 2011 (threat and
platform precedent); Herzog 2015 (corporation as coordination/ethos institution, blunting the "coordination
is the lab's import" objection); Visser & Arnold 2022 ("Recognition and Work in the Platform Economy,"
*Phil. of Management* 21: 31–45, prior-art for the platform-recognition half); Bernacchio 2022;
Herrmann & Ellmers 2017; Ross 2008 `[✓]`. Author-only: reword "a case built for exactly that question" to
kill the anticipation flavor.

**Post 8 — At Home in the Other (Freedom).** Confirmed anchors: Patten 1999 and Neuhouser 2000 (the latter
anchor *and* threat: the two-condition rationality test, of which the causal criterion operationalizes at
most the objective half), Hirschman 1970, the *Beisichselbstsein* loci (PR §7 Addition verbatim against
Nisbet), and the coordinative-sovereignty receipts `[✓]`. Threat: Neuhouser's recognitive condition (2);
and the round's sharpest additions, Christiaens 2025 and Taylor 2017, which already map exit/voice onto a
freedom concept (non-domination) without Hegel or causal structure — sharper foils than Berlin, because the
necessary-mediator verdict is exactly what undercuts exit-republicanism. Corrections: the PR §5R fanaticism
clause is not verbatim (re-set to Nisbet's full sentence via Knowles 2002) `[✗]`; the PR §158A love quote is
not Nisbet — fix to Werner's Nisbet wording `[✗]`; the concession that "readers have made that pairing
before" (exit↔negative, voice↔positive) is unsourced — a targeted search found no such published mapping, so
rewrite as "the pairing suggests itself," which *strengthens* the originality claim `[✗]`; and in-draft, "the
bypass margin, zero or full" contradicts q213's four-cell spectrum (partial = 1.585) `[✗]`. The verify pass
**reversed** one grounder correction: Roy 2006's pages are **225–255**, correct as the draft has them — the
digest's inferred 225–256 read a PDC end-marker slug as a page number; leave it and drop that gate `[✗]`.
New scholarship: Christiaens, "Platform cooperativism and freedom as non-domination in the gig economy"
(*EJPT* 24(2): 176–199); Taylor, *Exit Left* (OUP 2017); Honneth, *Freedom's Right* (Columbia UP 2014, the
stronger cite than 1995 for the recognitive-membership sentence); Muldoon & Raekstad 2023; Krijnen 2019
`[✓/gate]`. Load-bearing: the Hirschman↔Hegel gap is re-confirmed still unmade, a small original
contribution; the refutation condition is that the instrument returns the same verdict for the marriage and
the sweatshop, and the post's competence ends at the subjective half.

**Post 9 — The Ledger.** Confirmed anchors: Maybee 2020 (SEP), the q210/q211 core-merger as the one
computed sublation exhibit (single triad Φ=2.0; AND channel major complex {S1,W2,S2,C2} spanning both
triads at Φ=3.0), and the containment guard (only the major complex was read; a certified nested complex is
a category error under IIT exclusion) `[✓]`. This post carries the most corrections, all confirmed: two SL
quotes the draft hangs on Maybee — "a new concept but one higher and richer... therefore contains it" and
"nothing extraneous is introduced" — are **Hegel's own words** quoted in the SEP entry (SL-dG 33 / SL-M 54),
so re-attribute to di Giovanni SL p. 33 and add an SL entry to the References `[✗]`; the enumerated
three-senses Aufhebung quote tagged (Fuchs 2003) is **not in that chapter** — it comes from the undated
fuchsc.net essay, so swap to the chapter's own pp. 209–210 sentences `[✗]`; the "thin one to hang two years
on" demotion framing plus the sneer at "the sanctioned line about principled exploration" must be cut per
CLAUDE.md `[✗]`; and "scalable proxies recover the verdict only near chance" should say "**time-series**
proxies" (q82's edge count hits 0.966 in-family) `[✗]`. New scholarship: Lawvere's "Hegelian taco" (AMAST,
U. Iowa, 1989, pp. 51–74, taco definition at 70–73) and Lawvere 1991 (LNM 1488) — a third formal ancestor
of *Aufhebung* to name alongside Fuchs and Günther, whose categorical which-level-resolves definition
strengthens rather than threatens the "missing quantitative step" claim; arXiv 2503.03439 (2025) shows the
line is live math `[✓]`. A negative sweep found no 2024–26 quantitative measure on sublation and no
Hegel-and-IIT paper, so the hedged "may be the first to put an irreducibility number on the moment a
smaller whole survives inside a larger one" stands.

## New scholarship since 2026-07-10

Everything the round surfaced that the two prior memos did not have, with its relevance and status.

- **Tononi & Boly, "IIT: A Consciousness-First Approach to What Exists,"** arXiv:2510.25998 (29 Oct 2025).
  IIT's own ontological statement (to exist is to have cause-effect power upon itself). Post 1 pedigree
  footnote. `[✓]`
- **Barrett, Milinkovic, Mediano, Rosas, Bor, Barnett & Seth, "IIT: the good, the bad and the
  misunderstood,"** arXiv:2604.11482 (13 Apr 2026). Authoritative critical clarification; shield for the
  modest instrument framing. Post 1. `[✓]`
- **Ng, "Fanon and Hegel on the Recognition of Humanity,"** *Hegel Bulletin* 45(3) (2024): 571–597, doi
  10.1017/hgl.2024.25 (OA). Develops Fanon's recognition toward a universal humanity; pressures Post 2's
  flat "Fanon made the same puncture." `[✓]`
- **Reichl, "Leopoldo Zea on the Role of Hegel's Master–Slave Dialectic...,"** *EJP* 34(1) (2026): 152–162.
  Reception history; optional company for Post 2's "Century of Readers." `[✓]`
- **Badenhorst, "Fanon, Hegel, and the Problem of Reciprocity,"** *Hegel Bulletin*. Directly on the
  reciprocity assumption Fanon denies; year/volume/pages `[unverified]`. Post 2.
- **Lazarus, "From the invisible hand to the rabble: Smith, Hegel and social ontology,"** *CJE* 49(6)
  (2025): 1163–1185, doi 10.1093/cje/beaf046. The nearest published neighbor to Post 5; recognitive social
  ontology, so it sharpens rather than pre-empts. Must be named. End page 1185 to confirm. `[✓/gate]`
- **Herzog, *Inventing the Market: Smith, Hegel, and Political Theory*,** OUP 2013 (subtitle is "Political
  Theory," not "Economy"). Standard systematic Smith/Hegel comparison; Post 5 anchor. `[✓]`
- **Ruda, *Hegel's Rabble: An Investigation into Hegel's Philosophy of Right*,** Continuum 2011 (ISBN
  9781441156938). Standard rabble monograph; prior-art for Post 5's rabble paragraphs and a scope threat +
  platform precedent for Post 7. `[✓]`
- **Ferro, "From Rechtsphilosophie to Staatsökonomie,"** *EJP* 31(1) (2023): 80–96, doi
  10.1111/ejop.12784. Hegel's transformation of political economy; optional Post 5 positioning. `[✓]`
- **Daniel James, "Social Organisms: Hegel's Organisational View of Social Functions,"** Routledge 2020,
  doi 10.4324/9780429435393-12 (PhilPapers mis-indexes "View" as "Theory"). State-organism organs defined
  by functional contribution; Post 6 convergent anchor. `[✓/gate]`
- **Herzog, "Two Ways of 'Taming' the Market: Why Hegel Needs the Police and the Corporations,"** in
  Buchwalter (ed.), *Hegel and Capitalism*, SUNY 2015, pp. 147–162. Corporations as ethos-forming
  coordination spaces; Post 7. (Drop the unconfirmed "Proceedings 22" tag.) `[✓]`
- **Visser & Arnold, "Recognition and Work in the Platform Economy: A Normative Reconstruction,"** *Phil.
  of Management* 21 (2022): 31–45, doi 10.1007/s40926-021-00172-2. Honneth-style "normative paradox";
  prior-art for Post 7's platform-recognition half. `[✓]`
- **Bernacchio, "Hegelian Reflections on Agency, Alienation, and Work,"** *Phil. of Management* 21(4)
  (2022): 523–544. Expressivist theory of the firm; Post 7 positioning. `[✓]`
- **Herrmann & Ellmers (eds.), *Korporation und Sittlichkeit*,** Fink 2017 (contributors incl. Herzog,
  Klikauer, Vieweg, Jütten). German state-of-the-debate collection; Post 7 one-line positioning. `[✓]`
- **Ross, "Hegel on the Place of Corporations within Ethical Life,"** Springer 2008, doi
  10.1007/978-1-4020-8401-0_5. Earlier business-ethics application; Post 7 prior-art. `[✓]`
- **Christiaens, "Platform cooperativism and freedom as non-domination in the gig economy,"** *EJPT* 24(2)
  (2025): 176–199. Nearest living neighbor to Post 8's co-op-and-cage; republican, not causal. `[✓]`
- **Taylor, *Exit Left: Markets and Mobility in Republican Thought*,** OUP 2017. Argues *for* exit as the
  remedy; a sharper foil than Berlin for Post 8, since the necessary-mediator verdict undercuts it. `[✓]`
- **Honneth, *Freedom's Right: The Social Foundations of Democratic Life*,** Columbia UP 2014. Builds
  "social freedom" on Hegel's being-with-oneself-in-the-other; the stronger cite than Honneth 1995 for
  Post 8's recognitive-membership sentence. `[✓]`
- **Muldoon & Raekstad, "Algorithmic domination in the gig economy,"** *EJPT* 22(4) (2023): 587–607.
  Grounds Post 8's driver case in the published gig-work literature. `[✓]`
- **Krijnen, "Being at Home with Oneself in the Whole,"** in *Concepts of Normativity: Kant or Hegel?*,
  Brill 2019. Second scholarly hook for *Beisichselbstsein*; Brill paywall `[gate]`. Post 8.
- **Knowles, *Routledge Philosophy GuideBook to Hegel and the Philosophy of Right*,** Routledge 2002. The
  verification vehicle for Nisbet's §5R fanaticism clause; optional Post 8 secondary witness. `[✓]`
- **Zabel, "The Institutional Turn in Hegel's Philosophy of Right,"** *Hegel Bulletin* 36/1 (2015):
  80–104. Freedom via institutions; convergent with Post 8's third section; paywalled `[gate]`.
- **Lawvere, "Display of graphics... the Hegelian 'taco'"** (AMAST, U. Iowa, 1989, pp. 51–74) and Lawvere,
  "Some thoughts on the future of category theory," LNM 1488 (1991), pp. 1–13. The categorical
  formalization of *Aufhebung* (the minimal level that resolves a lower level's opposites); a third
  ancestor for Post 9, structural not quantitative, so the "missing quantitative step" claim survives with
  it named. `[✓]`
- **"Lawvere's fourth open problem: Levels in the topos of symmetric simplicial sets,"** arXiv:2503.03439
  (2025). Shows the Lawvere-*Aufhebung* line is a live research program; one-clause support if Lawvere is
  added. `[✓]`

Three negative results are themselves reportable. The Hegel↔Hirschman exit/voice mapping is re-confirmed
still unmade (Post 8, an original contribution). No published exit↔negative-liberty / voice↔positive-liberty
mapping exists — an over-concession to remove from Post 8, not a prior-art gap. And no 2024–26 quantitative
measure on sublation-as-emergence and no Hegel-and-IIT paper surfaced (Post 9).

## The residue to carry

**Open gates — physical-copy and paywalled.** Most primary Hegel quotations are locus-verified and often
German-verified, with the English wording and pagination still owed against the printed page. The heaviest
concentrations: the Wood/Nisbet PR wordings for Posts 5, 6, 7, 8, and 9 (§185 "corruption(s)," §244 ellipsis,
§253 Standesehre, §255 "based in... itself" and the §255-Addition guild lines, §278R "separate existence,"
§303R, §308's lowercase "corporations," §5R, §158A, §260 first sentence, §75R/§163, the Preface owl); the
B&D Encyclopedia pages for §§194/204/216/218/135-Zusatz/198R/§§200–203; the di Giovanni SL p. 588 front
clause and the new p. 33 SL entry for Post 9; the Hackett EL §24 Z2 English; the PhG ¶590 Pinkard wording
against the CUP 2018 print; and the secondary interiors still behind paywalls (Ng pp. 43/234/10/171/259,
Kreines "Logic of Life" print pagination, Stern pp. 155–57, Heiman pp. 111–135, Roy, Lazarus end page). None
blocks a post; each blocks its own quotation.

**"Do not attribute" cautions.** These are the traps a drafter or a later verify pass could re-introduce:

- Do **not** attribute "Hegel has no solution" to Kain — that is the Marxist reading he *disputes* (Post 5).
- Do **not** attribute "rather than holism in the traditional sense" to Yeomans — the word "holism" never
  appears in his NDPR review; and Ng's p. 43 sentence is Gentry's paraphrase, never a Ng quote (Post 1).
- Do **not** quote Koch as "constitute mechanical objects" — she wrote "provide the conditions for the
  individuation of mechanical objects" (Post 4).
- Do **not** attribute the two SL "higher and richer" / "nothing extraneous" quotes to Maybee — they are
  Hegel's, quoted in the SEP entry; and the enumerated three-senses *Aufhebung* quote is not in the Fuchs
  2003 chapter (Post 9).
- Do **not** claim "readers have made that pairing before" for exit/voice ↔ Berlin — no such mapping was
  found (Post 8).
- Do **not** "correct" Roy 2006's pages to 225–256 — 225–255 is right (Post 8).
- The state-triad is **§198R**, the Remark, not the main paragraph — the recurring mis-pin across Posts 3,
  6, and 9.
- Keep Heiman paraphrase-only; the earlier verbatim was likely fabricated (Post 7). Keep Knox's "caste"
  (for *Zunft*) and "aggregate/frightful" out of the Nisbet quotations (Posts 6, 7).

**The one author-only item per paper.** Each post has a single thing no grounding pass can settle — a lived
case to supply, a temper paragraph to ratify, or a term to freeze:

- **Post 1:** ratify the ladder-relative self-deprecation ("low instrument," "bottom-rung," "mine knows
  nothing at all") — safe only while its paired affirmative clauses survive editing.
- **Post 2:** own or soften the mixed-verdict come-down ("a construal for readers to test, not a result"),
  and decide whether to take Ng 2024's one-clause Fanon inoculation.
- **Post 3:** supply the real anonymized middle for the opener, and **freeze the flagship term** (integrator
  vs. necessary middle) across Posts 4–9 — the one naming decision that binds the whole back half.
- **Post 4:** ratify or soften the "What the Bracketing Buys" temper paragraph.
- **Post 5:** soften the opening "ran that test in 1821" metaphor to a verdict-shaped phrase.
- **Post 6:** rewrite the self-defeating temper paragraph (lines 242–251) so its concession language stays
  on the Hegel bridge, never on Φ.
- **Post 7:** reword "a case built for exactly that question," and decide whether to add Ruda's scope clause
  ("necessary for those the corporation admits").
- **Post 8:** rewrite the Berlin concession to "the pairing suggests itself," and supply the driver's lived
  case.
- **Post 9:** cut the demotion verdict ("a thin one to hang two years on," and the sneer at "the sanctioned
  line about principled exploration"), keeping the objection at full strength.

## Provenance

Nine posts, eighteen agents (a Fable grounding pass and an Opus adversarial pass per post), 2026-07-16;
digests at `library/research/post{1..9}.digest.json`, each carrying its `.digest` and `.verdict`. Overall
verdicts: sound for Posts 1, 2, 5, 6, 7, 9; needs-correction for Posts 3, 4, 8 (corrections listed above,
none touching the thesis). The strategic finding is unchanged from Rounds 1 and 2 and better supported: the
Hegel-against-a-causal-irreducibility bridge is unmade, and the series holds it at homology.
