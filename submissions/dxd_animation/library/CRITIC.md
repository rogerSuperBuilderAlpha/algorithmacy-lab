# CRITIC — coverage of the outline by the library (S9, run dxda-lib-2026-11)

> [Built by Claude (opus subagent), 2026-11-05, stage S9.]

I read `../SOURCE.md` (Pass 2 governs), `../OUTLINE.md`, `README.md`, `FACETS.md`, `triage/DECISIONS.md`
(including the Checkpoint B rulings), `INDEX.md`, `TRACKER.tsv`, `CITED_WORKS.md`, `HAND_CHECK.md`,
`BROWSER_LIST.md`, and the cards named below. Every statement about a source comes from its card in
`cards/`; read depths come from each card's frontmatter as `TRACKER.tsv` lists them. Pointer keys (works
held in other lab libraries) carry the depth `CITED_WORKS.md` gives them; I did not open those cards. Quoted
lines are the cards' own words, or the source's words as the card quotes them. Nothing here edits SOURCE,
OUTLINE, CHECK or any card.

Depth codes: **full** full_text, **part** partial, **abs** abstract, **meta** metadata, **ptr** pointer
(depth as CITED_WORKS gives it).

## The headline

The library carries the outline's frame well and its mechanism badly. Three works read in full
(`stark2024animation`, `maeda2025anthropomorphism`, `jones2026animating`) carry c4, the claim that an LLM
interface is an animation. The stream-timing studies (`gnewuch2022opposing`, `tan2026impact`,
`anderl2024conversational`, `bhat2025dynamic`) give c5 measured support. But every source on what animation
*is made of* — McLaren's interstices, Silvio's projection and numerical disjunct, Thomas and Johnston's
principles, Wertheimer's apparent motion, Smith's attentional continuity — sits at abstract or metadata
depth, or reaches the lab only through L. Stark. §4 is the section the outline says argues "from what
animation is *made of*". It has the least full text under it.

A second pattern runs across the full-text cards: on four claims they cut against the outline, not for it
(see "Where the cards cut against the outline"). The writer cannot treat those cards as support without
reading their Caution and use sections.

## Coverage by claim

| claim | full / part | abs / meta | ptr | load-bearing on abs/meta only? |
|---|---|---|---|---|
| c1 moving goal | weinmann2016digital, johnson2012beyond, maier2022no (full); jachimowicz2019when, saracay2026beyond, subramonyam2024bridging, shi2026siren, wadi2026shopping (part) | bettman1998constructive, chen2026do, schneider2018digital, guttman1998agent, lipshitz2001taking, simonson2008will, ash2018digital (abs); norman1986cognitive, payne1992behavioral, slovic1995construction, simon1955behavioral, klein2006making (meta) | hutchins1985direct, gray2018dark, nouwens2020dark (full); norman1988psychology, simon1997 (weak) | **Yes, for the moving goal itself** (below) |
| c2 human user | subramonyam2024bridging (part) | bettman1998constructive, lipshitz2001taking (abs); klein2006making, simon1955behavioral, slovic1995construction (meta) | zhang1994representations, scaife1996external, risko2016cognitive, eslami2016first (full) | **Yes, for "biological" and "emotional"** |
| c3 platform | hollanek2023ai, cameron2024social, stanton2006distributed, endsley2017from (full); wadi2026shopping (part) | ananny2018seeing, flyverbom2016transparency, siles2019mutual, chiou2023trusting (abs); sheridan2002humans, horvitz1999principles (meta) | stark2024principles (D. Stark), burrell2016how (full) | **Yes, for the transparency critique** |
| c4 LLM as animation | stark2024animation, maeda2025anthropomorphism, jones2026animating, shanahan2023role, abercrombie2023mirages, bhat2025dynamic, natale2019if (full) | silvio2010animation, weizenbaum1966eliza, epley2007seeing, mori2012uncanny, luger2016like (abs); silvio2019puppets (meta) | — | No, but **Silvio is reached only through Stark** |
| c5 missing frames | gnewuch2022opposing, tan2026impact, anderl2024conversational, bhat2025dynamic, dragicevic2011temporal, ruddell2008from (full); may2003using (part) | shneiderman1984response, gnewuch2018faster, cholodenko2014first (abs); furniss2008art, lamarre2009anime, wells1998understanding (meta) | andes2024 (part), xiaoyang2025 (full), hzhu2026 (part), dehaene-cohen-2007 (weak) | **Yes, for McLaren** |
| c6 lock-in; user animates | stark2024animation, maeda2025anthropomorphism, jones2026animating, smith2008edit, schwan2000do, tan2026impact, anderl2024conversational, natale2019if (full) | anderson1993myth, hoerl2015seeing, epley2007seeing, gambino2020building, appel2012does, magliano2011impact, weizenbaum1966eliza, gnewuch2018faster, siles2019mutual, mori2012uncanny, luger2016like (abs); wertheimer1912experimentelle, wertheimer2012experimental, smith2012attentional, steinman2000phi, heider1944experimental, mccloud1993understanding (meta) | zacks2009 (part); pitts2023, ongchoco2023 (abs) | **Yes, for the perceptual lock-in** |
| c7 triad | stark2024animation, maeda2025anthropomorphism, shanahan2023role, cameron2024social, stanton2006distributed (full) | silvio2010animation, chiou2023trusting (abs); silvio2019puppets, ngai2004animatedness, bukatman2012poetics, heider1944experimental, wells1998understanding (meta) | — | **Yes, for Silvio's ground of the triad** |
| c8 animator's methods | chevalier2016animations, dragicevic2011temporal, hollanek2023ai, abercrombie2023mirages, siskind2024would, ruddell2008from (full); may2003using (part) | lasseter1987principles, ananny2018seeing, flyverbom2016transparency, ash2018digital (abs); thomas1981illusion, chang1993animation, heer2007animated, gonzalez1996does, lamarre2009anime, horvitz1999principles (meta) | cox2016design, bucinca2021trust (full) | **Yes, for the methods themselves** |
| c9 gap | stark2024animation, maeda2025anthropomorphism, jones2026animating, shanahan2023role, siskind2024would, cameron2024social (full) | chiou2023trusting (abs); gonzalez1996does (meta) | — | No; see `GAP_CHECK.md` |

## Coverage by section

### §1 Introduction and §2 Conversion-era design (c1) — *Human factors and design*

The conversion-era toolkit is well read. Weinmann et al. (full) supply "digital nudging" and "there is no
neutral way to present choices" (p. 433); Johnson et al. (full) supply the tool inventory; Jachimowicz et al.
(part) supply *d* = 0.68; Maier et al. (full) supply the publication-bias contrast. Dark patterns rest on two
full-text pointers (gray2018dark, nouwens2020dark) and on Shi et al. (part).

**The moving goal has no source.** Every full or partial card that touches c1 keeps the goal fixed, and each
card says so:

- `saracay2026beyond` (part): "CoPref does not move the goal. It states that the user has 'some latent target
  item' in mind" (p. 3); the user "only becomes aware of more features of a target that stays put."
- `wadi2026shopping` (part): "Its goal is fixed at the start of one run and does not move during the
  interaction."
- `subramonyam2024bridging` (part): "the authors keep the goal fixed and study the step from goal to
  intention." Its "moving target" (p. 14) is a trap: it "refers to the sweet spot for AI and interface design
  shifting," not a user's goal.
- `weinmann2016digital` (full): "Weinmann and colleagues never ask where the user's goal comes from."
- `jachimowicz2019when` (part): "The inference from 'endorsement presumes a fixed target' to 'defaults
  presuppose a fixed goal' is the paper's own."

The only card on a chatbot at goal formation, `chen2026do` ("Do Not Think Ahead of Me"), is **abs**. The
constructed-preference anchors are **abs** (bettman1998constructive) or **meta** (payne1992behavioral,
slovic1995construction); the lab sees Bettman's claim in full only as Saracay et al. report it (p. 3). So §2's
"DXD starts a step earlier, at goal formation" rests on: Hutchins et al. (ptr, full) for the gulfs;
Subramonyam et al. (part) for "In much of HCI work, stage two – forming the intention – is assumed as given"
(p. 3); `norman1986cognitive` (**meta**, anchor, load-bearing); and `norman1988psychology` (ptr; CITED_WORKS row
8 says "the card body says no text of the book was read"). **§2's goal-first claim about Norman has no
full-text support from Norman himself.** The moving goal must stand as the author's argument, built on
constructed preference, and the paper should say so.

The verb in Pass 2 ("Choice architecture proves") stays flagged: `johnson2012beyond` (full) says "It does not
support 'proves'," and `jachimowicz2019when` carries the meta-analytic evidence instead.

### §3.1 The user is human (c2) — *Cognition*

No card in this library supports c2 at full depth. The outline's own §3.1 sources are four full-text pointers
(Zhang & Norman, Scaife & Rogers, Risko & Gilbert, Eslami et al.) that this run did not re-card.
`subramonyam2024bridging` (part) is the only card here, and it covers cognition only: "Emotion appears once in
the text I searched, in passing… They say nothing on the biological side. The card does not support the claim
that the user is biological, cognitive and emotional." **"Biological" and "emotional" have no source in any
library the run consulted.** The NDM card (`lipshitz2001taking`) is **abs**.

### §3.2 The platform environment (c3) — *Human factors and design*

Opacity and co-optation rest on full-text pointers (`burrell2016how`, which "quotes the three forms
verbatim (p. 1)" per the FACETS lead correction; D. Stark & Vanden Broeck through `stark2024principles`).
`hollanek2023ai` (full) adds "corporate strategies of secrecy and user interfaces that hide traces of
AI-driven personalization."

**The transparency critique rests only on an abstract.** `ananny2018seeing` is **abs** and anchors c3 and c8.
Its card says the phrase "across a relational environment" "is not in the abstract, so this card cannot
confirm it," and that the abstract's subject "is accountability and governance… not a user's decision."
Pass 2 quotes the work; OUTLINE §3.2 and §5 lean on it twice. `flyverbom2016transparency` (abs) adds nothing
the reader can quote.

**The triad and the HF dyad.** Checkpoint B ruling 4 holds that the HF "triads" are not real triads and are
less examined. The full-text reads support the ruling in substance, which the cards record without adopting it:

- `cameron2024social` (full): the Deployer is "an interested external agent" (p. 1408), but the interests "are
  general and vary by case"; its action through the robot is offered "as readings and predictions"; the model
  is "Named and sketched" and "still remains to be formally tested" (p. 1413).
- `stanton2006distributed` (full): agents are task roles with "different, but potentially compatible"
  purposes (p. 5); Fable's hand-check: "no designer or deployer acts through the artefact on the user."
- `endsley2017from` (full): more parties appear, but they share a goal (p. 23).
- `chiou2023trusting` (**abs**): "conflicting goals with no owner named." Checkpoint D needs the full text.

So the softened §3.2 wording now has full-text support for two of its three parts (canonical HF models take
one operator and one aid; added parties share a goal). Its third part, that the interested third party
enters HF only recently, rests on Cameron (full) and Chiou (**abs**). The paper must still cite Cameron as
prior work on a triad (DECISIONS finding a).

### §3.3 The design move is aesthetic (c4)

`stark2024animation` (full) carries c4 directly ("I argue ChatGPT and similar chatbots… can be best understood
as animated characters," p. 1663). `jones2026animating` (full) is a second use of Silvio, not wholly
independent: "Luke Stark (2023) makes the same argument about LLMs" (p. 42). `maeda2025anthropomorphism`
(full) applies Stark's frame with Stark as second author and "should not count" as independent confirmation.

**Silvio is never read.** `silvio2019puppets` is **meta** and `silvio2010animation` is **abs**. Pass 2's
"Building on Teri Silvio's (2019) theory" rests on Stark's quotation at p. 1664. The attribution itself is
disputed: Stark (2024, p. 1664) gives the definition to Silvio (2019, p. 52); Maeda & L. Stark (2025, p. 1662)
give the same words to Silvio (2010), with no page. Both cards say only Silvio's own texts can settle it.

### §4.1 Opaque: the missing frames (c5) — *Perception*

The stream is the best-supported part of the outline. Gnewuch et al. 2022 (full) show that chronemic cues
are "often overlooked due to their invisibility" (p. 785); Tan et al. (full) call latency "a tunable design
variable"; Bhat (full) shows the frames change perceived character while perceived effectiveness stays flat;
Anderl et al. (full) tie visible typing to discernment. Each card names its stretch (one wait, not frames; a
screencast, not interaction), and Tan et al. report "no effect of latency on behaviour, trust or workload."

**McLaren has no citable source.** Pass 2's "As Norman McLaren (1968) observed" rests on `furniss2008art`
(**meta**, page unknown) and `sifianos1995definition` (no record; reserve). `century2022norman` returned 403
(BROWSER_LIST 43). The open text on limited animation, `ruddell2008from` (full), "never says the unseen frames
are the animator's craft" and reports Lamarre at second hand; `lamarre2009anime` is **meta**. **§4.1's
definition of the craft ("the art of movements that are drawn") has no source the paper can cite today.**

### §4.2 Co-optive: locking in (c6) — *Perception → Cognition*

Part (a), the perceptual mechanism, rests only on abstract and metadata cards: `wertheimer1912experimentelle`
(**meta**), `wertheimer2012experimental` (**meta**), `anderson1993myth` (**abs**), `smith2012attentional`
(**meta**, anchor), and the two contrast cards that dispute CHECK F12, `hoerl2015seeing` (**abs**) and
`steinman2000phi` (**meta**). **§4.2's "apparent motion, not persistence of vision" rests on X = Wertheimer
(metadata) and Y = Anderson & Anderson (abstract); no full-text support, and the two works that contest the
fix (Hoerl; Steinman et al.) are also unread.** HAND_CHECK notes that Hoerl's Warwick accepted version is now in
the local folder; the card needs a re-write, not a browser.

Part (b), event boundaries, has two full reads on live-action film (`smith2008edit`, `schwan2000do`), plus
`zacks2009` (ptr, part); `magliano2011impact` is **abs**. Schwan et al. cut the outline's version: "cuts did not
drive how viewers segmented, and they did not change overall recall" (pp. 219–222). Ongchoco et al., the
anchoring result the outline cites for "boundaries limit anchoring," is a pointer at **abs**.

Part (c), the user as animator, is well read: Stark p. 1667 ("The final uncompensated animator…"), Maeda &
L. Stark ("users as co-designers," p. 1665), Jones ("fill in the blanks," p. 41). All three make the
co-optation "attentional and emotional… not perceptual." The outline's (a) and (c) therefore meet in no single
source.

### §4.3 Triadic: character, animator, viewer (c7) — *Action*

The triad's structure has strong full reads, but they pull against the singular animator (next section).
Its Silvian ground (projection versus introjection, the numerical disjunct, "hard to separate") reaches the
lab only through Stark (pp. 1664, 1668). `ngai2004animatedness` and `bukatman2012poetics` are **meta** and
`load: exists`.

**The Action heading has no card in this library.** The outline's Action claim is that "the user's action can
land on the character (the reply) or on the animator." No card here studies where a user acts. The outline's
sources for it are three Spaces pointers: `huq2026` (part, abstract and §1), `zhou2026check` (part, abstract,
§1, §2) and `chen2026cua` (full). `horvitz1999principles` (**meta**) is the only F8 card on when an agent should
act or ask. See "Course coverage" below.

### §5 The animator's methods for DXD (c8) — *Human factors and design*

**The methods themselves are unread.** `thomas1981illusion` is **meta** (anchor, load-bearing), with year,
subtitle and publisher unsupported by any record this run (HAND_CHECK batch 4). `lasseter1987principles` is
**abs**: "the principle list c8 needs is in no record read." Pass 2 cites Chevalier et al. for "the core
methodologies of the animator"; `chevalier2016animations` (full) "does not describe the animator's methods"
and lists animation as "a distractor to fight boredom when the system is busy," which is close to the "hide
the frames" option the outline rejects. The one worked case of an animator's principle carried into an
interface and measured is `dragicevic2011temporal` (full, slow-in/slow-out), and it cuts the transfer:
interface work "has largely been dominated by design principles from general animation that may not
necessarily transfer to interaction design." `may2003using` (part) is the precedent for borrowing a craft,
with a caution of its own (editors may be "following their change in gaze rather than driving it").

The two failed options are better served. Hiding the frames: Chevalier (full), Siskind et al. (full, magic
used for concealment). Exposing the backend: Hollanek (full: showing the insides "does not show whose
interest the system serves"), Ananny & Crawford (**abs**), and Abercrombie et al. (full) as the "damp the
character" position, which the card narrows: they argue "for choosing cues by context, not for removing them
all" (p. 4783).

### §6 Limits and next steps (c9)

See `GAP_CHECK.md`. §6 also needs a sentence on the plural animator and on Maeda & L. Stark's governance move.

### §7 Conclusion

No sources required.

## Where the cards cut against the outline

1. **Stark's many animators against the singular animator (c7).** `stark2024animation`: "his animators are
   many: staff, raters, moderators, authors and the user. The paper's singular 'unseen "animator"' stretches
   him." Stark's own line: "Animated characters… are typified by the distributed agency of their creation and
   enlivenment" (p. 1666). `maeda2025anthropomorphism` sharpens it into three layers ("Primary Agents… Secondary
   Agents… Mediators," p. 1663), and `jones2026animating` lists "a plural field of co-producers, not a viewer,
   character and animator triad." The author must read "animator" as a role many parties fill, or concede the
   plurality.
2. **Stark's opacity is hidden labour, not missing frames (c5).** `stark2024animation`, c5 bullet: "no support.
   Stark's opacity is the 'obfuscation of human labor', the hidden animators, not missing frames. A use for c5
   would stretch him." Maeda & L. Stark agree: "animation disguises—or at least distracts from—this fact"
   (p. 1663), where the fact is the network.
3. **Stark's co-optation is attentional, not perceptual (c6).** "He says nothing about frames, thresholds or
   apparent motion, so the 'lock in' half of c6 needs other sources." His "chain of influence is only one-way"
   (p. 1668) sits against the user-as-animator layer.
4. **Stark's consequence is regulation, not craft (c8).** "his own proposals are governance, and his 'AI
   iconoclasm' questions design that encourages projection" (p. 1669). Maeda & L. Stark want "guardrails… to
   prevent excessive animation" (p. 1670) and at times to "eschew anthropomorphic AI altogether." The paper must
   say why DXD's craft does not deepen the projection both papers worry about.
5. **Saracay's fixed target against c1.** "the source supports 'preference is constructed' and cuts against
   the strong version of the paper's c1, a goal that changes (raincoat to umbrella)." The authors themselves
   assume preferences are "stable and never forgotten" (p. 6).
6. **Shi's diffuse authorship against the interested platform (c3, c7).** `shi2026siren`: "their authorship is
   diffuse, shaped by data, objectives, and prompts rather than a single designer" (p. 5); "We do not ascribe
   intent to the LLM itself" (p. 6). The card reads this as "closer to a dyad plus an owner than to a triad with
   an animated character."
7. **Subramonyam's gap is not a moving goal (c1).** "Cite for the intention-stage gap, not a moving goal"
   (HAND_CHECK batch 4); the capability gap is "the users' inability to formulate 'how to' procedures" (p. 6).
8. **Tan's ethics passage against c8.** Deliberately slowing a reply "sits uneasily between positive friction
   and potential deception" (§5.5). An animator who paces the stream to the decision is exactly that designer.
9. **Silvio's concession against a hard triad (c7).** Stark quotes Silvio: "in practice, performance and
   animation are [hard] to separate" (p. 1668); the Silvio 2010 abstract says the two models "interact." The
   third term must stand as an analytic distinction (CHECK F4).
10. **Shanahan's simulator against the animator (c7).** In role play the simulator "'has no agency of its own'
    (p. 496), unlike an animator who decides frames to produce an effect on a viewer." A reviewer will raise
    role play as the rival frame.

## Course coverage: HF700-1's four headings

| heading | outline sections | full-text support in this library | verdict |
|---|---|---|---|
| Perception | §4.1, §4.2(a) | Stream timing: four full cards with measured results. Film continuity: two full cards. Lock-in mechanism: none (all abs/meta). | Adequate for the stream; thin for the mechanism |
| Cognition | §3.1, §4.2(b) | None in this library at full depth; four full-text pointers outside it; "emotional" and "biological" unsupported | Thin, carried by pointers |
| Action | §4.3 | **None.** No card studies where the user acts; three Spaces pointers (two partial) and one metadata card (Horvitz) | **Thinnest** |
| Human factors and design | §2, §3.2, §5 | Conversion toolkit and dark patterns well read; HF dyad and triad well read; the animator's methods unread | Adequate except §5's methods |

**Action is the thin heading.** The outline maps the triad onto Action, but every c7 card concerns the
structure of the triad (who animates), not the user's acts within it. The proposal's Action paragraph
("sanctioned and subversive writes") is carried with no source in this library. A short card set on user
intervention in agent runs, or full cards for `huq2026` and `zhou2026check`, would close it. **Cognition comes
second**: §3.1 has no card of its own, and the outline lists only pointers for it.

## Housekeeping found while reading

- README's S8 row lists `POINTERS.md`, and DECISIONS twice says pointers are added "for POINTERS.md". The file
  does not exist in `library/`. The pointer keys above come from FACETS and CITED_WORKS.
- `chevalier2016animations`, `dragicevic2011temporal` and `maeda2025anthropomorphism` were obtained after
  BROWSER_LIST was written (its "Update" note); rows 41, 47 and 48 are stale.
- `abercrombie2023mirages`, `natale2019if` and `ruddell2008from` each offer an untagged c6 (or c3/c5) fit;
  HAND_CHECK leaves the tagging to the author.
- `wertheimer1912experimentelle`: the registry row still carries Sekuler's DOI (HAND_CHECK batch 4); S8's DOI
  check passed because the card has none.

## Ten BROWSER_LIST items that would most strengthen the paper

Ranked by how much of the outline each copy would move from abstract or metadata to full text.

| rank | row | key | why |
|---|---|---|---|
| 1 | 1 | `silvio2019puppets` | p. 52 is the definition Pass 2 builds on and the source of c4 and c7. The lab holds it only through Stark, and the Silvio 2010/2019 attribution conflict between Stark and Maeda & L. Stark can only be settled here. |
| 2 | 2 | `silvio2010animation` | The projection/introjection contrast, the "hard to separate" concession (p. 432) and "structuring trope" (p. 422): the ground of the triad (c7). Settles the other half of the attribution conflict. |
| 3 | 24 | `thomas1981illusion` | §5's whole argument is "apply the animator's methods"; no card in the run reads a single principle. Without it, c8 rests on Chevalier (which "does not describe the animator's methods") and on Dragicevic's one principle. |
| 4 | 3 (+38, 43) | `furniss2008art` (or Sifianos 1995; Century 2022) | McLaren's "art of movements that are drawn" is §4.1's definition of the craft and has no citable source. Any one of the three closes CHECK F1. |
| 5 | 8 | `ananny2018seeing` | Pass 2 quotes it; §3.2 and §5 both rest on it; "across a relational environment" is unconfirmed. The only anchor of c3's transparency critique and of §5's "expose the backend" foil. |
| 6 | 7 | `smith2012attentional` | Anchor for c6 at metadata depth. The attentional theory of continuity is the nearest film-perception statement of "locking in" and the bridge to the Spaces eye-tracking study. |
| 7 | 21 | `steinman2000phi` | With Hoerl (whose accepted version is already in the local folder; the card needs a re-write), it decides whether CHECK F12's "apparent motion, after Wertheimer" names the right phenomenon (finding b). §4.2(a) cannot be drafted safely without it. |
| 8 | 6 (+54) | `wertheimer2012experimental` (and the 1912 URN scan) | The primary source for the lock-in, in English and German. The URN route for 1912 is untried and may not need the author's browser. |
| 9 | 13 | `chen2026do` | The only chatbot study the library has at goal formation (c1, anchor). It would give the moving goal one empirical source that does not keep the target fixed — or show that it does. |
| 10 | 9 | `chiou2023trusting` | Ruling 4 asks the cards to record what each HF source counts as its third party; Chiou is the one HF triad candidate still unread, and Checkpoint D waits on it. "Co-operators of automation" and "semiotics" also make it the HF paper most likely to overlap c9. |

Next in line: `norman1986cognitive` (row 12; §2's goal-first claim about Norman), `bettman1998constructive`
(row 11; constructed preference, c1/c2 anchor), `lasseter1987principles` (row 39; principles across media,
c8), `gnewuch2018faster` (row 20; the AIS PDF location HAND_CHECK names may open in a browser).
