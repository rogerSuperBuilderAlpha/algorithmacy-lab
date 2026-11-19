# dxd_animation facets

> **[Drafted by Claude (Fable), 2026-11-05, stage S1. For the author's approval at Checkpoint A.]** S2 searches
> from this file (`tools/search.py Fn --from FACETS.md` reads the `**Queries:**` bullets) and S3 triages
> against it. Marks: **[R: id]** a Crossref, OpenAlex or OpenLibrary record matched author, title and year
> today; **[unconfirmed]** no record matched (the detail stays as the plan gave it, unfixed); "added S1" not
> in the plan, resolved alike; `pointer: key` an existing card in another lab library (`registry.tsv`);
> `upgrade: key` an abstract-only card in `../../dxd_animator/literature/library/cards/` that S5 reads in
> full instead of writing a new card. Nothing below comes from memory: every identifier was returned by a
> lookup this run, every key by the registry.

## Where the claims sit

| Facet | Claims | Outline sections | New | Upgrade |
|---|---|---|---|---|
| F1 Animation theory and the animator's craft | c4, c5, c7, c8 | §3.3, §4.1, §4.3, §5 | 7 | 5 |
| F2 Apparent motion and film perception | c6 | §4.2 | 6 | 3 |
| F3 Anthropomorphism, the ELIZA effect, the media equation | c4, c6 | §3.3, §4.2 | 5 | 3 |
| F4 Stream timing: typing delays, token pacing, latency | c5 | §4.1 | 6 | 0 |
| F5 Deciding with a moving goal | c1, c2 | §1, §2, §3.1 | 7 | 3 |
| F6 Choice architecture, digital nudging, dark patterns | c1 | §2 | 4 | 1 |
| F7 Platform opacity, co-optation, transparency critique | c3 | §3.2 | 3 | 0 |
| F8 The HF automation dyad versus a triad | c3, c7 | §3.2, §4.3 | 4 | 1 |
| F9 Interface animation in HCI | c8 | §5 | 5 | 1 |
| F10 Agent-mediated shopping and agentic commerce | c1 | §1, §2 | 2 | 0 |
| G Gap check | c9 | §6 | 2 | 0 |
| **Total** | | | **51** | **17** |

New plus upgrade is 68 (after the lead's Burrell correction), under the ceiling of 70. The new-card count sits below the plan's 55–65 because
17 planned anchors already have abstract-only cards in `dxd_animator` (see "The dxd_animator library"
below). If the author keeps upgrades outside the ceiling, each facet's "stretch" line raises the new
count to 60.

## The dxd_animator library (found 2026-11-05)

`../../dxd_animator/` (opened 2026-11-03; agent-drafted, not reviewed by the author) carries the same
thesis as a call for papers and 31 cards, all read from abstract and record only. Its three pillars and
six strands map onto the facets here:

| dxd_animator | Cards | Facet here |
|---|---|---|
| Pillar 1, S1 decision-making | Simon 1955; Slovic 1995; Klein, Moon & Hoffman 2006; Vohs et al. 2008; Thaler & Sunstein 2008; Johnson et al. 2012 | F5, F6 |
| Pillar 1, S2 UX critique | Fogg 2002; Gray et al. 2018; Mathur et al. 2019 | F6 |
| Pillar 1, S3 human–AI interaction | Horvitz 1999; Lee & See 2004; Luger & Sellen 2016; Amershi et al. 2019; Bansal et al. 2021; Vasconcelos et al. 2023 | F8 (Luger & Sellen also F3) |
| Pillar 2, S4 platforms | Gillespie 2010; Burrell 2016; Kellogg et al. 2020; Rahman 2021 | F7 |
| Pillar 3, S5 animation | Wertheimer 1912; Thomas & Johnston 1981; Lasseter 1987; Anderson & Anderson 1993; Chang & Ungar 1993; McCloud 1993; Wells 1998; Lamarre 2009 | F1, F2, F9 |
| Pillar 3, S6 character and anthropomorphism | Heider & Simmel 1944; Reeves & Nass 1996; Epley, Waytz & Cacioppo 2007; Mori et al. 2012 | F3 (Heider & Simmel also F2) |

Its seven open research questions fall as follows: Q1 (what DXD measures) → F5, F6; Q2 (which decisions
to surface, Horvitz) → F8; Q3 (lock-in as apparent motion, not persistence of vision) → F2; Q4 (do
timing, anticipation, staging transfer) → F1, F9; Q5 (limited animation shows its gaps) → F1; Q6 (who
animates a chat agent) → F7, F8; Q7 (where the analogy breaks: users talk back) → F3, G.

Anchors it holds that the plan lacked, now adopted as upgrades: Heider & Simmel 1944, Lasseter 1987,
McCloud 1993, Mori et al. 2012, Horvitz 1999, Luger & Sellen 2016, Simon 1955, Klein, Moon & Hoffman
2006. Cards it holds that no facet here needs: Amershi et al. 2019, Bansal et al. 2021, Vasconcelos et
al. 2023, Vohs et al. 2008, Fogg 2002, Thaler & Sunstein 2008 (the last two are pointers in other
libraries anyway). They stay where they are.

**Either home works.** If the library lives here, an upgrade becomes a card in this README's frontmatter
with `prior_cards: [<dxd_animator key>]` and the old card is left alone (README rule 3). If the library
lives in `dxd_animator`, its cards gain a `Facet:` field with the F-tags below, and the new cards are
written in its H1 format with the same facet and claim tags. The facet definitions, queries and targets
are the same in both cases.

## F1 Animation theory and the animator's craft (c4, c5, c7, c8)

**Establish.** What animation theory says animation is, from the animator's side: McLaren's "art of
movements that are drawn", the interstices as the site of the craft (c5); Silvio's projection and
numerical disjunct, the ground of the triad (c7) and of Stark's chatbot-as-character (c4); the
principles the animator works with (timing, anticipation, staging, limited animation) that §5 translates
into DXD moves (c8). This facet also settles CHECK F1 (the McLaren date) and F3/F4 (Silvio's wording).

**Queries:**
- `definition of animation McLaren movements that are drawn`
- `animation theory interstices between frames`
- `Silvio animation projection performance introjection`
- `limited animation gaps style anime`
- `twelve principles of animation timing anticipation staging`
- `animatedness puppet character agency theory`

**Anchors.**
- Sifianos 1995, "The definition of animation: A letter from Norman McLaren", *Animation Journal* 3(2) [unconfirmed: Crossref returns no record for the journal; OpenAlex answered 503/429 on three tries]. The McLaren source (c5); CHECK F1. S2 retries OpenAlex and WorldCat before S4 fetches.
- Thomas & Johnston 1981, *Disney Animation: The Illusion of Life* [R: OL2924612W, Abbeville 1981; the OpenLibrary author field is garbled ("Thomas Johnson, Ollie Johnson"), so S4 checks the copy in hand] — `upgrade: thomas1981illusion`. The principles (c8); CHECK F11.
- Silvio 2010, "Animation: The new performance?", *J. Linguistic Anthropology* [R: 10.1111/j.1548-1395.2010.01078.x]. Projection vs introjection, "hard to separate" (c7); CHECK F4.
- Silvio 2019, *Puppets, Gods, and Brands* [R: 10.1515/9780824880989; OL21338441W]. The definition Stark quotes, p. 52 (c4); CHECK F3.
- Ngai, "Animatedness", in *Ugly Feelings* [R: 10.4159/9780674041523-003; Crossref and OpenLibrary date the book 2004, the plan said 2005 → `registered_year`]. Animatedness as being moved by another (c7).
- Bukatman 2012, *The Poetics of Slumberland* [R: 10.1525/9780520951501; OL21528072W]. Animated spirits and the animating spirit (c7).
- Lamarre 2009, *The Anime Machine* [R: OL17203968W] — `upgrade: lamarre2009anime`. Limited animation makes the gap a style (c5, c8); dxd_animator Q5.
- Wells 1998, *Understanding Animation* [R: OL2708440W; Crossref 10.4324/9781315004044 is the 2013 e-edition] — `upgrade: wells1998understanding`. Reference for terms.
- Lasseter 1987, "Principles of traditional animation applied to 3D computer animation" [card DOI 10.1145/37402.37407; S4 re-checks] — `upgrade: lasseter1987principles`. The principles survive a change of medium (c8); dxd_animator Q4.
- McCloud 1993, *Understanding Comics* [no registry lookup today; the card gives no DOI] — `upgrade: mccloud1993understanding`. Closure between panels, the reader supplies the gap (c6).
- Furniss 1998, *Art in Motion* [R: OL767180W; 2008 revised ed. OL25196771W], added S1. Reprints McLaren's definition (CHECK F1); fallback if Sifianos cannot be had.
- Cholodenko 1991, *The Illusion of Life: Essays on Animation* [R: OL8658250W], added S1, exists-only. The title Silvio 2010 echoes (p. 428 per CHECK F11); card only if S3 finds it cited.

**Target.** 7 new (Sifianos, Silvio 2010, Silvio 2019, Ngai, Bukatman, Furniss, one from search), 5
upgrades. Stretch: 9 new (add Cholodenko and one search hit).

**Pointers.** `stark2024animation` is this library's own first card (L. Stark 2024, [R:
10.1145/3630106.3658995], F1 and F3). No other library holds an animation-theory card: the registry has
no Sifianos, Silvio, Ngai, Bukatman or Furniss.

## F2 Apparent motion and film perception (c6)

**Establish.** The "lock-in" is apparent motion, which Wertheimer measured, not persistence of vision,
which Anderson & Anderson call a myth (CHECK F12). Film perception then shows an active viewer
supplying continuity across cuts, and event-boundary work (held in `spaces`) gives the gaps a
decision-level effect. This facet carries §4.2's whole Perception load.

**Queries:**
- `apparent motion Wertheimer phi phenomenon`
- `persistence of vision myth film perception`
- `continuity editing attention edit blindness`
- `film cuts event segmentation comprehension`
- `active viewer perception of film ecological`

**Anchors.**
- Wertheimer 1912, "Experimentelle Studien über das Sehen von Bewegung", *Zeitschrift für Psychologie* 61 [unconfirmed as the 1912 article: no Crossref record; OpenAlex 503/429] — `upgrade: wertheimer1912experimentelle`. Caution for that card: its DOI 10.1068/p251243 resolves to Sekuler 1996, "Motion perception: A modern view of Wertheimer's 1912 monograph", *Perception* [R], not to Wertheimer; the card names a scan at gestalttheory.net, which S4 fetches. Quote in German first (README rule 7).
- Wertheimer 2012, *On Perceived Motion and Figural Organization* (Spillmann ed., MIT Press), "Experimental studies on seeing motion" [R: 10.7551/mitpress/9222.003.0003; book 10.7551/mitpress/9222.001.0001]. The English text to gloss against the German.
- Anderson & Anderson 1993, "The myth of persistence of vision revisited", *J. Film and Video* 45(1) [R: OpenAlex W165434426] — `upgrade: anderson1993myth`. CHECK F12.
- Cutting 2005, "Perceiving scenes in film and in the world", in Anderson & Anderson (eds), *Moving Image Theory* [chapter unconfirmed; the volume is R: OL18489457W, Southern Illinois UP 2005]. Film perception as ecological (c6).
- Smith 2012, "The attentional theory of cinematic continuity", *Projections* 6(1) [R: 10.3167/proj.2012.060102]. Continuity is an attentional achievement (c6).
- Schwan, Garsoffky & Hesse 2000, "Do film cuts facilitate the perceptual and cognitive organization of activity sequences?", *Memory & Cognition* [R: 10.3758/bf03213801; Crossref spells "activitiy"]. Cuts at boundaries help (c6).
- Smith & Henderson 2008, "Edit blindness", *J. Eye Movement Research* [R: 10.16910/jemr.2.2.6], added S1. Viewers miss cuts (c6); links to the Spaces eye-tracking study.
- Hochberg & Brooks, "Film cutting and visual momentum" [R: 10.1093/oso/9780195176919.003.0014, OUP ebook dated 1992; first published earlier, S4 fixes the year], added S1, exists-only unless S3 ranks it.
- Heider & Simmel 1944, "An experimental study of apparent behavior" [card DOI 10.2307/1416950] — `upgrade: heider1944experimental`. Viewers animate moving shapes: the co-optive mechanism before any character is drawn (c6; also F3).
- Sekuler 1996 [R: 10.1068/p251243], added S1 from the dxd_animator card's mistaken DOI; a modern reading of Wertheimer, metadata card at most.

**Target.** 6 new (Wertheimer 2012, Cutting, Smith 2012, Schwan, Smith & Henderson, one of Hochberg
or Sekuler), 3 upgrades. Stretch: 7.

**Pointers.** dxdfound: `wagemans2012century`. spaces: `zacks2009`, `ongchoco2023`, `pitts2023`,
`leeunal2026`, `michelmann2025`, `bernhard2025`. dial: `dehaene-cohen-2007-cultural-recycling` (§4.1,
carried from the proposal).

## F3 Anthropomorphism, the ELIZA effect, the media equation (c4, c6)

**Establish.** Why a user reads an LLM reply as a character: Weizenbaum's own report of ELIZA, the
three-factor theory of anthropomorphism, the media equation, and the uncanny valley as its limit.
Stark builds his chatbot-as-animation on this ground, and the "user as final animator" (Stark 2024,
p. 1667) needs it to explain the second layer of co-optation (c6).

**Queries:**
- `ELIZA effect users attribute understanding chatbot`
- `anthropomorphism three-factor theory agents`
- `media equation social responses to computers`
- `perceived agency social cues conversational agent`
- `uncanny valley character animation`
- `large language model chatbot as character persona`

**Anchors.**
- Weizenbaum 1966, "ELIZA", *CACM* [R: 10.1145/365153.365168; Crossref also lists a 1983 reprint 10.1145/357980.357991]. The original report (c4).
- Epley, Waytz & Cacioppo 2007, *Psychological Review* [R: 10.1037/0033-295x.114.4.864] — `upgrade: epley2007seeing`. The theory (c4).
- Natale 2021, *Deceitful Media* — `pointer: natale2021` (lima). The ELIZA effect as a history of deception (c4, c6).
- Reeves & Nass 1996, *The Media Equation* — `pointer: reeves1996` (lima); dxd_animator also holds `reeves1996media`. Social responses (c6).
- Nass & Moon 2000 — `pointer: nass2000` (lima), `nass2000machines` (monograph).
- Mori, MacDorman & Kageki 2012, "The uncanny valley", *IEEE RAM* [R: 10.1109/mra.2012.2192811] — `upgrade: mori2012uncanny`. The limit of the character (c4).
- Luger & Sellen 2016, "Like having a really bad PA" [card DOI 10.1145/2858036.2858288] — `upgrade: luger2016like`. The expectation gap conversational agents open (c6); dxd_animator Q7.
- Holtgraves, Ross, Weywadt & Han 2007, "Perceiving artificial social agents", *Computers in Human Behavior* [R: 10.1016/j.chb.2006.02.017], added S1.
- Appel, von der Pütten, Krämer & Gratch 2012, "Does humanity matter?", *Advances in HCI* [R: 10.1155/2012/324694], added S1. Social cues against perceived agency (c6).
- Turkle 1984, *The Second Self* [R: OL2959131W], added S1. Computers as evocative objects; card only if S3 ranks it.
- L. Stark 2024 [R: 10.1145/3630106.3658995]: `stark2024animation`, this library's card (also F1).

**Target.** 5 new (Weizenbaum, Holtgraves, Appel, one search hit on the ELIZA effect, one on LLM
persona), 3 upgrades. Stretch: 6 (add Turkle).

**Pointers.** lima: `natale2021`, `reeves1996`, `nass2000`. monograph: `nass2000machines`. dial:
`waytz-heafner-epley-2014-mind-in-the-machine`.

## F4 Stream timing: typing delays, token pacing, latency (c5)

**Establish.** In a streamed reply the frames are literal: platforms set the token rate, pace it to
reading speed, and show typing indicators in the gap. The HF response-time literature gives the
baseline (what delay does to the user), and the chatbot delay studies show the delay itself is read as
a social cue. Together they make "missing frames" a measured design variable, which §4.1 needs.

**Queries:**
- `response time delay human performance computers`
- `chatbot response delay typing indicator perception`
- `LLM token streaming pacing reading speed`
- `perceived latency conversational interface waiting`
- `text movement eye movements generative AI chatbot`

**Anchors.**
- Gnewuch, Morana, Adam & Maedche 2022, "Opposing effects of response time in human–chatbot interaction", *BISE* [R: 10.1007/s12599-022-00755-x]. No card in any library; the PDF sits in `S/notebook_sources/A1_review_agents_streams/` (OUTLINE §4.1).
- Gnewuch et al. 2018, "Faster is not always better", ECIS [unconfirmed: no Crossref record; OpenAlex 429]. Dynamic delays; card only if S2 finds a record.
- Shneiderman 1984, "Response time and display rate in human performance with computers", *ACM Computing Surveys* [R: 10.1145/2514.2517]. The HF baseline (c5).
- Miller 1968, "Response time in man-computer conversational transactions", AFIPS [R: 10.1145/1476589.1476628], added S1. The oldest thresholds.
- Three search hits expected: typing indicators, perceived latency, streaming UX.

**Target.** 6 new. Stretch: 7.

**Pointers.** spaces: `andes2024` (Liu et al., the token pacer), `xiaoyang2025`, `hzhu2026`,
`pu2026` (agent micro-waits), `parklee2024` (text movement in chatbots), `liu2023captions`. dxdfound:
`nielsen2023paradigm`, `cho2021giving`.

## F5 Deciding with a moving goal: goal formation, constructed preference, NDM (c1, c2)

**Establish.** The commuter's goal moves from raincoat to umbrella while deciding, so the paper needs
the literature in which preferences are built during the choice, not read off beforehand (constructed
preference), and the one in which experts recognise a situation before they pick an option (NDM,
recognition-primed decision). Both put goal formation inside the interaction, which is where DXD starts
and conversion design does not. Bounded rationality and the gulfs of execution give the HF frame.

**Queries:**
- `construction of preference constructive choice processes`
- `recognition-primed decision naturalistic decision making`
- `goal formation during decision making interactive`
- `cognitive engineering gulf of execution goal`
- `preference construction digital marketplace recommendation agent`
- `sensemaking decision making uncertainty`

**Anchors.**
- Slovic 1995, "The construction of preference", *American Psychologist* [R: 10.1037/0003-066x.50.5.364] — `upgrade: slovic1995construction`.
- Payne, Bettman & Johnson 1992, "Behavioral decision research: A constructive processing perspective", *Annual Review of Psychology* [R: 10.1146/annurev.ps.43.020192.000511].
- Bettman, Luce & Payne 1998, "Constructive consumer choice processes", *JCR* [R: 10.1086/209535].
- Lichtenstein & Slovic (eds) 2006, *The Construction of Preference* [R: 10.1017/cbo9780511618031; OL18318375W]. The collection; the author may hold it.
- Klein 1993, "A recognition-primed decision (RPD) model of rapid decision making", in Klein, Orasanu, Calderwood & Zsambok (eds), *Decision Making in Action* [chapter unconfirmed; the volume is R: OL19209750W, Ablex 1993].
- Klein 1998, *Sources of Power* [R: OL2731587W, MIT Press 1998; the 2017 reissue is 10.7551/mitpress/11307.001.0001].
- Lipshitz, Klein, Orasanu & Salas 2001, "Taking stock of naturalistic decision making", *JBDM* [R: 10.1002/bdm.381], added S1. The review to cite instead of the whole field.
- Klein, Moon & Hoffman 2006, "Making sense of sensemaking 1" [card DOI 10.1109/mis.2006.75] — `upgrade: klein2006making`.
- Simon 1955, "A behavioral model of rational choice" [card DOI 10.2307/1884852] — `upgrade: simon1955behavioral`.
- Norman 1986, "Cognitive engineering", in *User Centered System Design* [R: 10.1201/9780367807320-3], added S1. The gulfs, with the goal formed first (c1); OUTLINE §2 leans on Norman 1988 through secondaries.

**Target.** 7 new (Payne et al., Bettman et al., Lichtenstein & Slovic, Klein 1993, Klein 1998,
Lipshitz et al., Norman 1986), 3 upgrades. Stretch: 8.

**Pointers.** dxdfound: `kahneman2009conditions` (Kahneman & Klein), `norman1988psychology`,
`hutchins1985direct`, `zhang1994representations`, `scaife1996external`, `risko2016cognitive`,
`risko2019offloading`. lima: `simon1997`. monograph: `eslami2016first`. research: `haublmurray2003`
(preference construction in digital marketplaces). dxd_animator (no upgrade needed): `vohs2008making`.

## F6 Choice architecture, digital nudging, dark patterns (c1)

**Establish.** What conversion-era design is made of, in its own terms: choice-architecture tools, the
digital-nudging programme the author cites, and dark patterns. The facet must show that all three take
the goal as given (the architect sets the options, the nudge steers toward a target), which is the
assumption a moving goal breaks. Jachimowicz supplies the evidence CHECK F5 asks for.

**Queries:**
- `choice architecture tools beyond nudges`
- `digital nudging interface design user choices`
- `defaults meta-analysis endorsement effect`
- `dark patterns conversational agent LLM`
- `nudging boosting autonomy steering`

**Anchors.**
- Johnson et al. 2012, "Beyond nudges: Tools of a choice architecture", *Marketing Letters* [R: 10.1007/s11002-012-9186-1] — `upgrade: johnson2012beyond`. CHECK F5.
- Weinmann, Schneider & vom Brocke 2016, "Digital nudging", *BISE* [R: 10.1007/s12599-016-0453-1]. CHECK F6; bot-walled before, so `BROWSER_LIST.md` if S4 fails again.
- Schneider, Weinmann & vom Brocke 2018, "Digital nudging: Guiding online user choices through interface design", *CACM* [R: 10.1145/3213765]. The registry's `schneider2018` (research) is a different work in *The Sociological Review*; the key here takes a title word.
- Jachimowicz, Duncan, Weber & Johnson 2019, "When and why defaults influence decisions", *Behavioural Public Policy* [R: 10.1017/bpp.2018.43]. No card in any library: the OUTLINE's "part" read lives in `decision_experience_design/literature/facets/F2_choice_architecture.md`, not a card.
- Hertwig & Grüne-Yanoff 2017 — `pointer: hertwig2017nudging` (dxdfound). Steering versus empowering, the contrast DXD wants.
- Thaler & Sunstein 2008 — `pointer: thalersunstein2008` (research), `thaler2008` (designeth).

**Target.** 4 new (Weinmann, Schneider, Jachimowicz, one search hit on dark patterns in agents), 1
upgrade. Stretch: 5.

**Pointers.** dxdfound: `gray2018dark`, `mathur2019dark`, `nouwens2020dark`, `hertwig2017nudging`.
research: `thalersunstein2008`, `thaler2018`, `yeung2017` (hypernudge), `luguristrahilevitz2021`,
`hansenjespersen2013`. spaces: `tang2026dark` (dark patterns meet GUI agents). dxd_animator (no upgrade
needed): `fogg2002persuasive`.

## F7 Platform opacity, co-optation, transparency critique (c3)

**Establish.** The three platform properties in the author's second condition, each from its source:
co-optation (D. Stark & Vanden Broeck), opacity (Burrell's three kinds; CHECK F7 wants the wording
confirmed) and the transparency critique (Ananny & Crawford). The facet is mostly pointers; its new
cards are near neighbours that already read a platform as a third party in the user's decision.

**Queries:**
- `platform opacity users folk theories algorithm`
- `co-optation platforms algorithmic management`
- `transparency ideal critique accountability seeing`
- `seamless seamful design infrastructure visibility`
- `platform as third party user decision intermediary`

**Anchors.**
- D. Stark & Vanden Broeck 2024 — `pointer: stark2024` (research, full), `stark2024principles` (monograph, coordsov). CHECK F8, F9.
- Burrell 2016 — `pointer: burrell2016` (research, lima, designeth), `burrell2016how` (monograph), `burrell2016machine` (coordsov); also `burrell2016machine` in dxd_animator (abstract). **[Lead correction, 2026-11-05]:** `burrell2016how` (monograph) and `burrell2016` (designeth) are both `read_depth: full_text`, and `burrell2016how` quotes the three forms verbatim (p. 1). CHECK F7 is resolved by pointer; no upgrade needed.
- Ananny & Crawford 2018 — `pointer: ananny2018seeing` (monograph, coordsov, hospitality), `anannycrawford2018` (designeth). CHECK F10.
- Pasquale 2015 — `pointer: pasquale2015black` (monograph, coordsov).
- Gillespie 2010, "The politics of 'platforms'" [card DOI 10.1177/1461444809342738] — exists only in dxd_animator; pointer there, no upgrade unless §3.2 defines "platform".
- Kellogg, Valentine & Christin 2020 — `pointer: kellogg2020algorithms` (monograph, dxdfound). Rahman 2021 — `pointer: rahman2021invisible` (monograph).
- Eslami et al. 2016 — `pointer: eslami2016first` (monograph), carried from the proposal.

**Target.** 3 new (search hits: seamful design, the platform as third party, user-side opacity), 0
upgrades (Burrell is a full-text pointer; lead correction 2026-11-05). Stretch: 4.

**Pointers.** As listed; plus research: `cobbe2023` (algorithmic supply chains), `yeung2017`.

## F8 The HF automation dyad versus a triad (c3, c7)

**Establish.** HF's automation models are two-node loops (operator and aid), so the facet must show the
dyad in its canonical statements and then the places where HF already lets a third party in:
AI-mediated communication (sender, AI, receiver), the moral crumple zone, mixed initiative. This is
the gap the triad of §4.3 fills, and the course's Action heading.

**Queries:**
- `human automation interaction supervisory control model`
- `joint cognitive systems coactive design`
- `mixed-initiative interface when to act expected utility`
- `AI-mediated communication third party sender receiver`
- `human-autonomy teaming triad stakeholder interests`

**Anchors.**
- Sheridan 2002, *Humans and Automation* [R: OL4274945W]. The dyad stated by its author (c3, contrast).
- Hollnagel & Woods 2005, *Joint Cognitive Systems* [R: 10.1201/9781420038194], added S1. The joint system as the unit; still two parties.
- Horvitz 1999, "Principles of mixed-initiative user interfaces" [card DOI 10.1145/302979.303030] — `upgrade: horvitz1999principles`. When an agent should act or ask: the decision-surfacing question (dxd_animator Q2).
- Hancock, Naaman & Levy 2020 — `pointer: hancock2020ai` (monograph, dxdfound). A third party inside the channel (c7).
- Elish 2019 — `pointer: elish2019moral` (monograph, dxdfound). Where responsibility lands in a human–machine pair (c7).
- Parasuraman, Sheridan & Wickens 2000 — `pointer: parasuraman2000types` (dxdfound; its card notes the two-node reading). Lee & See 2004 — `pointer: lee2004trust`. Bainbridge 1983 — `pointer: bainbridge1983ironies`. Simkute et al. 2024 — `pointer: simkute2024ironies`.
- Shneiderman & Maes 1997, direct manipulation vs agents — `pointer: shneiderman1997maes` (dxdfound).

**Target.** 4 new (Sheridan, Hollnagel & Woods, two search hits on triads in HF), 1 upgrade. Stretch: 5
(add `amershi2019guidelines` as an upgrade if §5 cites the guidelines).

**Pointers.** dxdfound: `parasuraman2000types`, `lee2004trust`, `bainbridge1983ironies`,
`simkute2024ironies`, `klein2004ten`, `sheridan1978human`, `shneiderman1997maes`, `hancock2020ai`,
`elish2019moral`. designeth: `endsleykiris1995`. spaces: `huq2026`, `zhou2026check`, `chen2026cua`,
`kim2026help` (§4.3, where users intervene).

## F9 Interface animation in HCI (c8)

**Establish.** HCI's own animation line, from Baecker & Small's "Animation at the Interface" through
cartoon principles in the UI, animated transitions and Chevalier's review of roles. CHECK F11 says
Chevalier covers interface animation, not the animator's craft, so this facet holds the interface
side and F1 the craft; §5 joins them. May, Dean & Barnard show film-cutting technique moved into
interface design before, a precedent for the move §5 proposes.

**Queries:**
- `animation at the interface roles transitions feedback`
- `cartoon animation principles user interface`
- `animated transitions comprehension perception`
- `film cutting techniques interface design`
- `design friction cognitive forcing decision interface`

**Anchors.**
- Baecker & Small 1990, "Animation at the interface", in Laurel (ed.), *The Art of Human-Computer Interface Design* [unconfirmed: no Crossref record for the chapter; OpenLibrary returned no match for the volume; OpenAlex 429]. S2 retries OpenAlex and WorldCat.
- Chang & Ungar 1993, "Animation: From cartoons to the user interface", UIST [R: 10.1145/168642.168647] — `upgrade: chang1993animation`.
- Heer & Robertson 2007, "Animated transitions in statistical data graphics", *IEEE TVCG* [R: 10.1109/tvcg.2007.70539].
- Chevalier, Henry Riche, Plaisant, Chalbi & Hurter 2016, "Animations 25 years later", AVI [R: 10.1145/2909132.2909255]. CHECK F11; cited by the author.
- Dragicevic, Bezerianos, Javed, Chevalier & Fekete 2011, "Temporal distortion for animated transitions", CHI [R: 10.1145/1978942.1979233], added S1. Timing as a design variable (c8).
- May, Dean & Barnard 2003, "Using film cutting techniques in interface design", *Human-Computer Interaction* 18(4) [R: 10.1207/s15327051hci1804_1], added S1. The precedent for borrowing from film.
- Lasseter 1987 — see F1 (`upgrade: lasseter1987principles`); tag both facets.

**Target.** 5 new (Baecker & Small, Heer & Robertson, Chevalier, Dragicevic, May et al.), 1 upgrade.
Stretch: 6.

**Pointers.** dxdfound: `cox2016design`, `disley2026designing` (cognitive friction in LLMs),
`bucinca2021trust`. spaces: `bucinca2021`, `kocaballi2026` (designers appropriating friction),
`ghosh2026`.

## F10 Agent-mediated shopping and agentic commerce (c1)

**Establish.** The raincoat case in its own literature: software agents that shop for or with a user,
from Maes's 1994 agents and the MIT survey through recommendation agents to the 2025–26 agentic-commerce
record the `research` library already holds in depth. The facet must show that the earlier work, like
conversion design, fixes the goal before the agent acts, so that the moving goal is new to it.

**Queries:**
- `agent-mediated electronic commerce survey`
- `AI shopping agent consumer decision goal`
- `recommendation agents online shopping decision quality`
- `agentic commerce LLM agents buying on behalf of users`

**Anchors.**
- Guttman, Moukas & Maes 1998, "Agent-mediated electronic commerce: A survey", *Knowledge Engineering Review* [R: 10.1017/s0269888998002082], added S1. The buying-process model with the goal fixed first (c1, contrast).
- He, Jennings & Leung 2003, "On agent-mediated electronic commerce", *IEEE TKDE* [R: 10.1109/tkde.2003.1209014], added S1; exists-only unless S3 ranks it.
- Maes 1994 — `pointer: maes1994` (designeth). Häubl & Trifts 2000 — `pointer: haubltrifts2000` (research). Xiao & Benbasat 2007 — `pointer: xiaobenbasat2007` (research).

**Target.** 2 new (Guttman et al., one search hit on LLM shopping agents and user goals). Stretch: 3
(add He et al.).

**Pointers.** research: `allouah2025`, `bichler2026`, `lucier2026`, `rothschild2025`,
`stockerlehr2025`, `chauhanjayswal2026`, `erickson2026`, `acp2026spec`, `openai2026discovery`,
`shopify2026agenticterms`, `adobe2025genaishopping`, `similarweb2026airef`, `haublmurray2003`.
dxdfound: `allouah2026what`, `alavi2026when`, `sun2026decision`. spaces: `spatharioti2025` (LLM search
and decision making), `tang2026dark`.

## G Gap check: prior work framing LLM interfaces as animation for decision design (c9)

**Establish.** Whether anyone before the author has read an LLM interface as an animation *and* drawn
design consequences for decisions. L. Stark 2024 does the first half (chatbot as animated character)
with no design programme; this facet looks for the second half and for anyone who joins them. Two
near-neighbour cards at most; the rest is a logged negative result in `GAP_CHECK.md`.

**Queries:**
- `LLM chatbot animated character interface design`
- `conversational agent puppet animator user`
- `decision experience design`
- `animation metaphor artificial intelligence interface`
- `streamed text interface perception decision design`

**Anchors.**
- L. Stark 2024 [R: 10.1145/3630106.3658995]: `stark2024animation`, the nearest prior.
- Everything else comes from the searches; a hit that frames LLM output as animation and says anything about design is carded, abstract depth, as `contrast` or `support`.

**Target.** 2 new. Stretch: 3.

**Pointers.** dxd_animator's `CALL_FOR_PAPERS.md` and README Q7 are the author's own prior framing,
not external prior work; `GAP_CHECK.md` cites them as such.

## Totals

Core: 51 new, 17 upgrades (68; Burrell moved to pointer by the lead, 2026-11-05). Stretch: 60 new. Ceiling 70. Every pointer key above was checked
against `registry.tsv` on 2026-11-05.

## Anchors marked [unconfirmed] today

Sifianos 1995; Wertheimer 1912 (the original article; the 2012 translation is confirmed); Cutting 2005
(the chapter; the volume is confirmed); Klein 1993 (the chapter; the volume is confirmed); Baecker &
Small 1990; Gnewuch et al. 2018. OpenAlex answered 503 and then 429 across four rounds today, so S2
retries these first. Nothing in their entries was filled in from memory.

## Rules for S2 and S3

1. Search each facet in at least two sources; log every query in `SEARCH_LOG.md`.
2. Every hit carries an OpenAlex id, DOI, ISBN or OpenLibrary id, or is dropped.
3. Tag hits already in `registry.tsv` as `in_registry`; they become pointers, or upgrades if the only
   card is a `dxdanimator` abstract card.
4. Keys follow `firstauthorsurnameYEARfirsttitleword` (README, "Keys").
5. Nothing from memory: each title, author, year, DOI or quotation needs a registry record or read text.

## Decisions for Checkpoint A

1. **The facet list.** F1–F10 and G as above, none merged. F2 and F3 overlap on Heider & Simmel; F1
   and F9 on Lasseter. Both are tagged twice rather than split.
2. **The home of the library — DECIDED 2026-11-05 by the author: keep both, point across.** Cards are written in `dxd_animation/library/` (frontmatter format); a dxd_animator card that gets a full read becomes a new card here with `prior_cards: [<dxd_animator key>]`, and the dxd_animator file is left alone. Was: `dxd_animation/library/` (this run) or `dxd_animator/literature/library/`
   (the 2026-11-03 project, 31 abstract-only cards, Grok-drafted CFP). The facets work for either; the
   card format differs (frontmatter here, H1 there).
3. **The ceiling.** 51 new plus 17 upgrades = 68 under a ceiling of 70; or 60 new if upgrades sit
   outside the ceiling.
4. **Books the author may hold physically** (a physical copy makes a full-text card; otherwise
   `BROWSER_LIST.md`): Thomas & Johnston 1981; Silvio 2019; Lichtenstein & Slovic 2006; Klein 1998;
   Lamarre 2009; Wells 1998; Bukatman 2012; Ngai 2004/2005; Sheridan 2002; Hollnagel & Woods 2005;
   Furniss 1998/2008; McCloud 1993; Turkle 1984.
5. **Sifianos 1995.** No registry record found. Fetch through the library, or fall back to Furniss's
   reprint of McLaren's definition and say so in the paper (CHECK F1).
6. **The dxd_animator Wertheimer card** gives Sekuler 1996's DOI as Wertheimer's. Correct it there, or
   leave it and record the correction under Caution in the upgrade (README rule 3).
7. **Gnewuch 2018.** Card it only if a record turns up; the 2022 BISE paper carries the claim.

## Checkpoint A — the author's rulings (2026-11-05)

1. Facets F1–F10 and G approved as written.
2. Home: keep both libraries, point across (see decision 2 above).
3. Ceiling: **upgrades sit outside the ceiling** — up to 60 new cards plus 17 upgrades (≈77).
4. Books held: none. Every book anchor gets a metadata card and goes on `BROWSER_LIST.md`.
5. Wertheimer DOI: leave the dxd_animator file alone; the upgrade card records the Sekuler (1996) DOI
   correction under Caution.
