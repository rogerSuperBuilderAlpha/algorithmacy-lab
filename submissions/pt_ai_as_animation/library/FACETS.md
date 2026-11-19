# pt_ai_as_animation facets

> [Built by Fable (Claude), 2026-11-08, stage S1 of pta-lib-2026-11.] For the author's approval at
> Checkpoint A. S2 searches from this file (`tools/search.py Fn --from FACETS.md` reads the
> `**Queries:**` bullets) and S3 triages against it. Nothing below comes from memory: every
> identifier was returned by a Crossref, OpenAlex or OpenLibrary lookup on 2026-11-08, every key by
> `pt_ai_animation_local/registry.tsv` (4,603 rows, 15 libraries).
>
> Marks: **[R: id]** a record (DOI, OpenAlex W-id or OpenLibrary OL-id) matched author, title and
> year today; where the record's year differs from the citation year, the record year is given and
> S5 sets `registered_year`. **[unconfirmed]** no record matched; the detail stays as the sketch gave
> it, unfixed, and S2 retries before S4. `pointer: library/key (depth)` an existing card in a lab
> library, not re-carded. `upgrade: key` one of the four abstract- or metadata-depth cards S5 reads
> in full instead of writing a new card (silvio2019puppets, thomas1981illusion, lasseter1987principles,
> hoerl2015seeing). "Counter" names the objection a *Philosophy & Technology* reviewer will raise and
> the works that carry it; the library stocks both sides.

## Where the claims sit

| Facet | Claims | Sketch § | New | Pointer | Upgrade |
|---|---|---|---|---|---|
| F1 Philosophy of life: definitions and their critics | c3 | §2 | 8 | 1 | 0 |
| F2 Organizational and autopoietic accounts | c4 | §2 | 7 | 1 | 0 |
| F3 Intelligence and the intentional stance | c3, c5 | §2, §6 | 7 | 0 | 0 |
| F4 Animation production pipeline | c6, c1 | §3 | 6 | 7 | 2 |
| F5 Puppetry, performance capture, liveness | c10, c6 | §5 | 5 | 2 | 1 |
| F6 Animacy and apparent motion | c7 | §4.2 | 2 | 6 | 1 |
| F7 Epistemic opacity, in principle vs practical | c7 | §4.2 | 7 | 3 | 0 |
| F8 Compound AI vs model-centrism | c1, c2 | §1, §4.1 | 7 | 0 | 0 |
| F9 Co-optation, lock-in, suspension of disbelief | c8 | §4.3 | 5 | 6 | 0 |
| F10 Triadicity: lab criterion, Simmel, many animators | c9 | §4.4 | 2 | 10 | 0 |
| F11 LLMs as characters and role play | c12, c10 | §1, §5 | 3 | 6 | 0 |
| F12 Venue: *Philosophy & Technology* 2019–2026 | c12, c7, c5 | all | 10 | 1 | 0 |
| G Gap check | c12 | §1, §7 | 3 | 3 | 0 |
| **Total** | | | **72** | **46** | **4** |

Stretch anchors (marked "stretch" below) add about 14 new cards if the author lifts the ceiling.

## F1 Philosophy of life: definitions and their critics (c3)

**Establish.** Life has no consensus definition, and the paper has to say what it does about that
before it calls AI development "creating artificial life". Trifonov's vocabulary count, Machery's
argument that the definitional project is pointless, and Cleland's move from definition to theory
give §2 its three positions. Artificial life as a field (Langton, Bedau, Dorin & Stepney) supplies
the "making" sense the thesis needs and the boundary with Berthon's lineage question.

**Counter.** Machery: there is no fact of the matter to settle, so §2 should not try. Cleland and
Bich & Green: an operational definition works locally without a theory. Berthon's arm (PRs
#879/#880) already asks whether model lineages are alive; this paper must not re-run that argument.

**Queries:**
- `definition of life philosophy consensus`
- `Machery definition of life pointless`
- `theory of life not definition Cleland`
- `artificial life soft hard wet Bedau`
- `what is artificial life large language models`
- `vocabulary of definitions of life`

**Anchors.**
- Trifonov 2011, "Vocabulary of definitions of life suggests a definition", *J. Biomolecular Structure and Dynamics* 29(2) [R: 10.1080/073911011010524992]. The 123 definitions (c3).
- Machery 2012, "Why I stopped worrying about the definition of life... and why you should as well", *Synthese* 185 [R: 10.1007/s11229-011-9880-1; record year 2011, online first]. The strongest counter to any §2 definition (c3).
- Cleland 2019, *The Quest for a Universal Theory of Life*, Cambridge UP [R: 10.1017/9781139046893]. Theory, not definition (c3). Book: `BROWSER_LIST.md` unless the author holds it.
- Cleland & Chyba 2002, "Defining 'life'", *Origins of Life and Evolution of the Biosphere* 32 [R: 10.1023/a:1020503324273]. The short form of the argument; the article S5 can read in full if the book cannot be had.
- Bich & Green 2018, "Is defining life pointless? Operational definitions at the frontiers of biology", *Synthese* 195 [R: 10.1007/s11229-017-1397-9; record year 2017]. Operational definitions survive Machery (counter).
- Bedau 2003, "Artificial life: organization, adaptation and complexity from the bottom up", *TICS* 7(11) [R: 10.1016/j.tics.2003.09.012]. ALife as a making discipline (c3, c12).
- Dorin & Stepney 2024, "What is artificial life today, and where should it go?", *Artificial Life* 30(1) [R: 10.1162/artl_e_00435]. Copy held in Berthon's arm, no card: carded here. Their 2023 editorial on LLMs and ALife [R: 10.1162/artl_e_00409] is the G(B) neighbour.
- Schrödinger 1944, *What is Life?*, Cambridge UP [R: OL1210514W]. The physicist's definition the rest react to; metadata card.
- Langton 1989, *Artificial Life* (Santa Fe proceedings) [R: OL17832658W is the 1995 MIT reprint; Routledge 2019 reissue 10.4324/9780429032769; the 1989 Addison-Wesley printing itself returned no record]. Exists-only; card if S3 finds "life-as-it-could-be" is needed verbatim.
- Bedau 1998, "Four puzzles about life", *Artificial Life* 4(2) [R: 10.1162/106454698568486], stretch.

**Target.** 8 new (Trifonov, Machery, Cleland 2019, Cleland & Chyba, Bich & Green, Bedau 2003, Dorin & Stepney, Schrödinger). Stretch: 10 (Langton, Bedau 1998).

**Pointers.** The registry holds no Trifonov, Machery, Cleland, Bedau, Langton or Dorin. One
pointer: `monograph/albantakis2014evolution` (metadata), animats as evolved ALife agents, only if §2
touches evolved organization. Berthon's arm is the lab's other life-philosophy site; `GAP_CHECK.md`
cites it as the author's own prior work, not as external prior work.

## F2 Organizational and autopoietic accounts (c4)

**Establish.** The account §2 is most likely to defend: life as maintained organization (autopoiesis;
organizational closure of constraints), which fits "so much more around that LLM" because it locates
life in the maintained whole, not in a core component. Froese & Ziemke carry the account into AI;
Di Paolo adds adaptivity, which the "fallible and requiring nurturing" line needs.

**Counter.** Moreno & Mossio: closure requires *self*-production of the constraints; humans build and
maintain harnesses, so the system around the LLM is heteronomous, not autonomous. Bongard & Levin
reverse the metaphor (living things are not machines). Meincke: process, not organization, is the
better frame. The paper has to answer the self-production point or weaken c4 to "organization-like".

**Queries:**
- `autopoiesis organization of living systems`
- `organizational closure constraints biological autonomy`
- `enactive artificial intelligence autonomy`
- `self-production heteronomy artificial systems autonomy`
- `living things are not machines metaphor`
- `autopoiesis adaptivity agency Di Paolo`

**Anchors.**
- Maturana & Varela 1980, *Autopoiesis and Cognition: The Realization of the Living*, Reidel [R: OL15015691W; chapter DOIs under 10.1007/978-94-009-8947-4]. The source definition (c4). Book.
- Varela, Maturana & Uribe 1974, "Autopoiesis: the organization of living systems, its characterization and a model", *BioSystems* 5(4) [R: 10.1016/0303-2647(74)90031-8]. The article form S5 can read in full.
- Moreno & Mossio 2015, *Biological Autonomy: A Philosophical and Theoretical Enquiry*, Springer [R: 10.1007/978-94-017-9837-2]. Closure of constraints and the self-production requirement (c4 and its counter). Book.
- Montévil & Mossio 2015, "Biological organisation as closure of constraints", *J. Theoretical Biology* 372 [R: 10.1016/j.jtbi.2015.02.029]. The formal statement; replaces the sketch's "Mossio & Moreno 2010, HPLS", for which no record matched today [unconfirmed].
- Thompson 2007, *Mind in Life*, Belknap/Harvard [R: OL3475244W]. Autopoiesis to cognition (c4, c5). Book.
- Di Paolo 2005, "Autopoiesis, adaptivity, teleology, agency", *Phenomenology and the Cognitive Sciences* 4 [R: 10.1007/s11097-005-9002-y]. Adaptivity as what bare autopoiesis lacks (c4, c11).
- Froese & Ziemke 2009, "Enactive artificial intelligence: investigating the systemic organization of life and mind", *Artificial Intelligence* 173 [R: 10.1016/j.artint.2008.12.001]. The account already applied to AI; nearest neighbour inside F2 (c4, c12).
- Bongard & Levin 2021, "Living things are not (20th century) machines", *Frontiers in Ecology and Evolution* 9 [R: 10.3389/fevo.2021.650726], added S1, counter.
- Rosen 1991, *Life Itself*, Columbia UP [R: OL7941375W], stretch; Luisi 2003, "Autopoiesis: a review and a reappraisal", *Naturwissenschaften* 90 [R: 10.1007/s00114-002-0389-9], stretch; Meincke 2018, "Autopoiesis, biological autonomy and the process view of life", *EJPS* 8 [R: 10.1007/s13194-018-0228-2], stretch counter.

**Target.** 7 new (Maturana & Varela, Varela et al., Moreno & Mossio, Montévil & Mossio, Thompson, Di Paolo, Froese & Ziemke) plus Bongard & Levin if c4 stays strong. Stretch: 10.

**Pointers.** `monograph/kauffman1969metabolic` (metadata), autocatalytic organization, only if the
paper reaches Kauffman. The registry holds no Maturana, Varela, Moreno, Mossio, Thompson 2007 or
Di Paolo.

## F3 Intelligence and the intentional stance (c3, c5)

**Establish.** Intelligence has no consensus definition either (Legg & Hutter's 70-odd; Sternberg &
Detterman's symposium), and the measurement tradition (Turing, Chollet, Hernández-Orallo) is the
"rigid standard" the intelligence frame holds AI to. Dennett's intentional stance is the model for
the paper's "vital stance": treat the system as alive because that is the predictive strategy that
works, with "Real patterns" answering the charge that a stance is mere instrumentalism.

**Counter.** Stance talk is instrumentalist: if the vital stance is only a useful fiction, c4's
organizational claim and c5 cannot both stand. Floridi (F12) argues for agency *without*
intelligence, which cuts the other way: the system acts, but there is nothing to animate.

**Queries:**
- `definitions of intelligence collection Legg Hutter`
- `universal intelligence definition machine`
- `intentional stance Dennett prediction strategy`
- `real patterns instrumentalism intentional stance`
- `measure of intelligence skill acquisition Chollet`
- `evaluating natural and artificial intelligence measurement`

**Anchors.**
- Legg & Hutter 2007, "Universal intelligence: a definition of machine intelligence", *Minds and Machines* 17 [R: 10.1007/s11023-007-9079-x]. The formal definition (c3, c5).
- Legg & Hutter 2007, "A collection of definitions of intelligence", arXiv 0706.3639 [R: W2142753384; 10.48550/arxiv.0706.3639]. The 70-odd definitions the sketch cites (c3).
- Sternberg & Detterman (eds) 1986, *What Is Intelligence? Contemporary Viewpoints on Its Nature and Definition*, Ablex [R: OL18183095W]. The psychologists' two dozen answers; metadata card unless held.
- Dennett 1987, *The Intentional Stance*, MIT Press [R: OL2463706W]. The frame for "vital stance" (c5). Book.
- Dennett 1971, "Intentional systems", *J. Philosophy* 68(4) [R: 10.2307/2025382]. The article S5 reads in full.
- Dennett 1991, "Real patterns", *J. Philosophy* 88(1) [R: 10.2307/2027085]. The answer to instrumentalism (counter); Bernini's F11 subtitle names it.
- Turing 1950, "Computing machinery and intelligence", *Mind* 59(236) [R: 10.1093/mind/lix.236.433]. The behavioural standard (c5).
- Chollet 2019, "On the measure of intelligence", arXiv 1911.01547 [R: W2984217758]. Intelligence as skill-acquisition efficiency; the benchmark frame (c5, c11). Stretch.
- Hernández-Orallo 2017, *The Measure of All Minds*, Cambridge UP [R: 10.1017/9781316594179]. Stretch; book.
- Floridi & Chiriatti 2020, "GPT-3: its nature, scope, limits, and consequences", *Minds and Machines* 30 [R: 10.1007/s11023-020-09548-1]. Stretch; bridge to F12's Floridi line.

**Target.** 7 new (Legg & Hutter ×2, Sternberg & Detterman, Dennett ×3, Turing). Stretch: 10.

**Pointers.** None: the registry holds no Dennett, Legg, Hutter, Chollet or Turing 1950. A 2025
*triadic* card `ali2025intelligence` ("Intelligence without consciousness", metadata) is adjacent but
IIT-facing; cite only if Φ enters §2.

## F4 Animation production pipeline (c6, c1)

**Establish.** What the production craft is, from the people who did it: the Disney principles,
Lasseter's transfer of them to 3D, the key-pose/in-between division, and the early computer-graphics
papers that automated in-betweening (Burtnyk & Wein; Catmull; Reeves), which is the exact point where
§3's mapping says the LLM "produces its own in-betweens". Crafton and Hooks give the performance
side (an animator *acts*), and Williams the working manual.

**Counter.** "Why animation and not puppetry, theatre or robotics?" (F5 carries it). And Catmull 1978
shows that the "missing frames" were an engineering problem the field solved, which strains c7's
"there will always be missing frames" unless §4.2 restates it as motion, not frames.

**Queries:**
- `animation production pipeline key poses inbetweening`
- `computer-assisted animation inbetweening problems`
- `principles of traditional animation applied to computer animation`
- `animation performance acting for animators`
- `interactive skeleton key frame animation`
- `stop motion production process frame by frame`

**Anchors.**
- Thomas & Johnston 1981, *Disney Animation: The Illusion of Life* [OpenLibrary returned no record for this title today; the dxd_animation run recorded OL2924612W, Abbeville 1981] — `upgrade: thomas1981illusion` (dxda metadata; dxdanimator partial). The principles and the key/in-between division (c6).
- Lasseter 1987, "Principles of traditional animation applied to 3D computer animation", *SIGGRAPH '87* [R: 10.1145/37401.37407; Computer Graphics 10.1145/37402.37407] — `upgrade: lasseter1987principles` (dxda abstract). The principles survive a change of medium (c6).
- Williams 2001, *The Animator's Survival Kit*, Faber [R: OL6073254W]. Working manual for timing and spacing (c6). Book.
- Catmull 1978, "The problems of computer-assisted animation", *SIGGRAPH '78* [R: 10.1145/800248.807414]. Why in-betweening resisted automation (c6, c10).
- Burtnyk & Wein 1976, "Interactive skeleton techniques for enhancing motion dynamics in key frame animation", *CACM* 19(10) [R: 10.1145/360349.360357]. The rig: skeleton as the thing animated (c6; the "rig = weights" row of §3).
- Reeves 1981, "Inbetweening for computer animation utilizing moving point constraints", *SIGGRAPH '81* [R: 10.1145/800224.806814]. In-betweens as constrained generation (c10).
- Crafton 2013, *Shadow of a Mouse: Performance, Belief, and World-Making in Animation*, UC Press [R: 10.1525/9780520352520; record year 2012]. Animation as performance and the audience's belief (c6, c8). Book.
- Hooks, *Acting for Animators*, Routledge [R: 10.4324/9781315618272, 4th ed. 2017; 2013 ed. 10.4324/9780203816226]. The animator acts the character (c6, c11).
- Sito 2013, *Moving Innovation: A History of Computer Animation*, MIT Press [R: Choice review 10.5860/choice.51-1536; Animation review 10.1177/1746847714546254], stretch. Kerlow 2004, *The Art of 3-D Computer Animation and Effects*, Wiley [R: OL546328W], stretch, pipeline terms. Catmull & Wallace 2014, *Creativity, Inc.* [R: OL23361858W], stretch, studio as animator (c9). Bishko 2014, "Animation principles and Laban movement analysis", ETC Press [R: W2504294352], stretch, added S1.

**Target.** 6 new (Williams, Catmull, Burtnyk & Wein, Reeves, Crafton, Hooks), 2 upgrades. Stretch: 9.

**Pointers.** dxda: `wells1998understanding` (metadata), `furniss2008art` (metadata),
`bukatman2012poetics` (metadata), `lamarre2009anime` (metadata), `mccloud1993understanding`
(metadata), `chang1993animation` (metadata), `cholodenko2014first` (abstract). All seven are
metadata-depth; the paper cites them for terms, not for quotations, so no upgrade beyond the two
above.

## F5 Puppetry, performance capture, liveness (c10, c6)

**Establish.** §5's limit case. Animation is rendered in advance; a puppet and a performance-captured
character are animated live, to an audience that answers back, which is closer to an LLM in
conversation. Silvio's definition of animation already spans puppets and brands; Auslander's
liveness and Kaplin's puppet tree (distance and ratio between performer and object) give the axes on
which to place an LLM; Kleist's marionette is the canonical text on grace without consciousness.

**Counter.** "Then write about puppetry": if puppetry is the closer case, c6's choice of animation is
unmotivated. Answer from Tillis and Jurkowski: the puppet is defined by the visible double (object
and operator), which the LLM lacks; and from Allison and Bode: performance capture already blends
the two, so the question is where on Kaplin's axes the LLM sits.

**Queries:**
- `puppetry aesthetics double vision object performer`
- `liveness mediatized performance`
- `motion capture performance Andy Serkis animation`
- `puppet tree distance ratio performer object`
- `marionette theatre Kleist grace consciousness`
- `animation puppets projection Silvio`

**Anchors.**
- Silvio 2019, *Puppets, Gods, and Brands*, U. Hawai'i Press [R: OL21338441W] — `upgrade: silvio2019puppets` (dxda metadata). The definition L. Stark quotes; animation across media (c6, c10).
- Auslander, *Liveness: Performance in a Mediatized Culture*, Routledge [R: 10.4324/9780203006955, 2nd ed. 2008 (e-record 2002); 3rd ed. 2022 10.4324/9781003031314]. Liveness as a contested category (c10). Book.
- Tillis 1992, *Toward an Aesthetics of the Puppet*, Greenwood [R: Theatre Journal review 10.2307/3208478, 1994; no direct book record]. Double vision: object and life at once (c10). Book.
- Jurkowski 1988, *Aspects of Puppet Theatre* [R: 10.1007/978-1-137-33845-7, Palgrave 2013 ed.]. The puppet's language; the visible operator (counter). Book.
- Kaplin 1999, "A puppet tree: a model for the field of puppet theatre", *TDR* 43(3) [R: 10.1162/105420499760347306]. Axes for placing an LLM (c10).
- Kleist 1810, "Über das Marionettentheater" [R: 10.1017/9781571137852.007, chapter record in a 2011 Camden House companion; the 1810 original has no record: unconfirmed as a 1810 item]. Grace without consciousness (c5, c10). German first, gloss second.
- Allison 2011, "More than a man in a monkey suit: Andy Serkis, motion capture, and digital realism", *Quarterly Review of Film and Video* 28(4) [R: 10.1080/10509208.2010.500947]. Performance capture blends animator and performer (c10).
- Bode 2017, *Making Believe: Screen Performance and Special Effects in Popular Cinema*, Rutgers [R: 10.36019/9780813580005; record year 2019], stretch. Phelan 1993, *Unmarked* [R: 10.4324/9780203359433], stretch, the liveness position Auslander argues against. Bell 2008, *American Puppet Modernism* [R: 10.1057/9780230613768], stretch.

**Target.** 5 new (Auslander, Tillis, Kaplin, Kleist, Allison; Jurkowski if the counter needs it), 1 upgrade. Stretch: 8.

**Pointers.** dxda: `silvio2010animation` (abstract), "Animation: the new performance?" [R:
10.1111/j.1548-1395.2010.01078.x]; `stark2024animation` (full), which lists puppetry among the forms
animation exceeds.

## F6 Animacy and apparent motion (c7)

**Establish.** The sharpening of c7: no frame contains the motion; the viewer's perception supplies it
(Wertheimer), and the "persistence of vision" story is a myth (Anderson & Anderson). Hoerl gives the
philosophical account of what seeing apparent motion is; Scholl & Tremoulet and Gao et al. show
that animacy itself is perceived from motion patterns, which is what makes a chat stream read as a
character before any character is drawn.

**Counter.** If perception supplies the motion, opacity is in the viewer, not the object, and c7's
"in principle" claim about AI (F7) is a different kind of opacity. The paper has to say whether the
two opacities are one.

**Queries:**
- `apparent motion philosophy perception seeing motion`
- `perceptual animacy causality motion cues`
- `perception of animacy chasing psychophysics`
- `persistence of vision myth apparent motion film`
- `gestalt motion perception Wertheimer phi`

**Anchors.**
- Hoerl 2015, "Seeing motion and apparent motion", *European J. Philosophy* 23(3) [R: 10.1111/j.1468-0378.2012.00565.x; record year 2012, online first] — `upgrade: hoerl2015seeing` (dxda abstract). What apparent motion is (c7).
- Scholl & Tremoulet 2000, "Perceptual causality and animacy", *TICS* 4(8) [R: 10.1016/s1364-6613(00)01506-0]. Animacy perceived from motion (c7, c8).
- Gao, Newman & Scholl 2009, "The psychophysics of chasing: a case study in the perception of animacy", *Cognitive Psychology* 59 [R: 10.1016/j.cogpsych.2009.03.001]. The quantified case (c7).
- Michotte 1963, *The Perception of Causality*, Methuen [R: 10.4324/9781315519050, Routledge 2017], stretch. Sekuler 1996, "Motion perception: a modern view of Wertheimer's 1912 monograph", *Perception* 25 [R: 10.1068/p251243], stretch.

**Target.** 2 new (Scholl & Tremoulet; Gao et al.), 1 upgrade. Stretch: 4.

**Pointers.** dxda: `wertheimer1912experimentelle` (metadata; the dxd run flagged its DOI as Sekuler's),
`anderson1993myth` (abstract), `heider1944experimental` (metadata), `epley2007seeing` (abstract),
`mori2012uncanny` (abstract). dxdfound: `wagemans2012century` (partial). Six pointers.

## F7 Epistemic opacity, in principle vs practical (c7)

**Establish.** Roger's "in principle black box: we could have all the information possible about the
algorithm but still have opacity" is Humphreys' *essential* epistemic opacity. Burrell's third source
(opacity from the characteristics of ML at scale) is the AI-side anchor the lab already holds. Durán
& Formanek, Boge and Beisbart work out what essential opacity does and does not license.

**Counter.** Burrell, Creel and Zerilli: most opacity is practical (functional, structural, run
transparency can each be had), and Zerilli's double-standard paper argues humans are no more
transparent. Sullivan: opacity does not block understanding. L. Stark: the opacity that matters is
hidden labour. If c7 rests on essential opacity it must say why the practical remedies miss the
motion, not the frames.

**Queries:**
- `essential epistemic opacity computer simulation`
- `transparency complex computational systems functional structural run`
- `opacity machine learning in principle practical`
- `explaining machine learning decisions philosophy of science`
- `algorithmic transparency double standard human decision making`
- `understanding from opaque machine learning models link uncertainty`

**Anchors.**
- Humphreys 2009, "The philosophical novelty of computer simulation methods", *Synthese* 169 [R: 10.1007/s11229-008-9435-2; record year 2008]. Essential epistemic opacity (c7).
- Humphreys 2004, *Extending Ourselves*, Oxford UP [R: 10.1093/0195158709.001.0001]. The book form; metadata card unless held.
- Creel 2020, "Transparency in complex computational systems", *Philosophy of Science* 87(4) [R: 10.1086/709729]. Three transparencies (counter).
- Zerilli 2022, "Explaining machine learning decisions", *Philosophy of Science* 89(1) [R: 10.1017/psa.2021.13]. Practical opacity and explanation (counter).
- Zerilli, Knott, Maclaurin & Gavaghan 2019, "Transparency in algorithmic and human decision-making: is there a double standard?", *Philosophy & Technology* 32 [R: 10.1007/s13347-018-0330-6; record year 2018]. The venue's own counter (also F12).
- Durán & Formanek 2018, "Grounds for trust: essential epistemic opacity and computational reliabilism", *Minds and Machines* 28 [R: 10.1007/s11023-018-9481-6]. Trust without transparency (c7, c11).
- Boge 2022, "Two dimensions of opacity and the deep learning predicament", *Minds and Machines* 32 [R: 10.1007/s11023-021-09569-4; record year 2021]. Opacity of *what* the network represents (c7).
- Beisbart 2021, "Opacity thought through: on the intransparency of computer simulations", *Synthese* 199 [R: 10.1007/s11229-021-03305-2], stretch. Sullivan 2022, "Understanding from machine learning models", *BJPS* 73(1) [R: 10.1093/bjps/axz035], stretch counter. Lipton 2018, "The mythos of model interpretability", *CACM* 61(10) [R: 10.1145/3233231], stretch.

**Target.** 7 new (Humphreys ×2, Creel, Zerilli ×2, Durán & Formanek, Boge). Stretch: 10.

**Pointers.** monograph: `burrell2016how` (full) [R: 10.1177/2053951715622512]; the same paper sits in
seven libraries, none re-carded. dial: `ananny-crawford-2018-seeing-without-knowing` (verified),
`pasquale-2015-black-box-society` (verified). Three pointers.

## F8 Compound AI vs model-centrism (c1, c2)

**Establish.** The engineering literature already concedes the premise: the model is a small part of
a working system (Sculley et al.; Paleyes et al.; Amershi et al.), and "compound AI systems" is now
the term of art (Zaharia et al.). Retrieval, tools, reasoning loops, declarative pipelines and
generative agents are the harnesses the sketch names, each with a record.

**Counter.** "Harnesses are CS too", and "the model is still the intelligence": scaling laws and
emergent abilities (Kaplan; Wei) say capability lives in the weights. Schaeffer et al. answer that
emergence is a measurement artefact. Bommasani et al. coined "foundation model", the model-centric
view in its own words.

**Queries:**
- `hidden technical debt machine learning systems`
- `compound AI systems shift from models`
- `challenges deploying machine learning case studies survey`
- `large language model based autonomous agents survey architecture`
- `generative agents interactive simulacra`
- `emergent abilities large language models mirage`
- `foundation models opportunities risks`

**Anchors.**
- Sculley et al. 2015, "Hidden technical debt in machine learning systems", *NeurIPS 28* [unconfirmed: no Crossref or OpenAlex record for the NeurIPS paper today; only a 2021 MIT Press chapter "Technical debt in machine learning systems" 10.7551/mitpress/12440.003.0011 and citing works]. S2 tries the NeurIPS proceedings page and Semantic Scholar. The sketch depends on it (c1).
- Zaharia et al. 2024, "The shift from models to compound AI systems", BAIR blog [unconfirmed: web post, no record; OpenAlex returns only papers that cite the term]. Card as web source with access date, or replace with Paleyes et al. (c1).
- Paleyes, Urma & Lawrence 2022, "Challenges in deploying machine learning: a survey of case studies", *ACM Computing Surveys* 55(6) [R: 10.1145/3533378]. The deployment gap (c1).
- Amershi et al. 2019, "Software engineering for machine learning: a case study", *ICSE-SEIP* [R: 10.1109/icse-seip.2019.00042]. The nine-stage workflow (c1).
- Park et al. 2023, "Generative agents: interactive simulacra of human behavior", *UIST '23* [R: 10.1145/3586183.3606763]. Memory, reflection and planning around an LLM make a character (c1, c11).
- Wang et al. 2024, "A survey on large language model based autonomous agents", *Frontiers of Computer Science* 18 [R: 10.1007/s11704-024-40231-1]. The harness anatomy (c1).
- Lewis et al. 2020, "Retrieval-augmented generation for knowledge-intensive NLP tasks" [R: W3027879771; arXiv 2005.11401]. Retrieval as a layer (c1).
- Schick et al. 2023, "Toolformer" [R: W7133214447; 10.52202/075280-2997]; Yao et al. 2022, "ReAct" [R: W4304195432]; Khattab et al. 2023, "DSPy" [R: W4387430850]. Tools, loops, pipelines; one of the three is carded, the others cited from its record (c1).
- Bommasani et al. 2021, "On the opportunities and risks of foundation models" [R: W3195577433], counter. Kaplan et al. 2020, "Scaling laws for neural language models" [R: W3001279689], counter. Wei et al. 2022, "Emergent abilities of large language models", *TMLR* [R: W4283026156], counter. Schaeffer, Miranda & Koyejo 2023, "Are emergent abilities of large language models a mirage?", *NeurIPS* [R: W7133219754; 10.52202/075280-2425], answer to the counter.
- Kapoor et al. 2024, "AI agents that matter" [unconfirmed: OpenAlex returned no record], stretch.

**Target.** 7 new (Sculley, Paleyes, Amershi, Park, Wang, Lewis, one of Schick/Yao/Khattab) plus
Bommasani and Schaeffer as the counter pair. Stretch: 12 (Zaharia as web card, Kaplan, Wei).

**Pointers.** None in the registry: no Sculley, Zaharia, Paleyes, Park, Bommasani, Kaplan or Wei.
`dxdfound/hao2024training` (full) and `spaces/andes2024` are LLM-systems cards but off-claim.

## F9 Co-optation, lock-in, suspension of disbelief (c8)

**Establish.** Two literatures the paper joins. On the AI side, dependency growing with use is
lock-in (Arthur; Shapiro & Varian; Farrell & Klemperer) and platform co-optation of outside actors,
assets and activities (D. Stark & Vanden Broeck; Selznick is the organizational root). On the
animation side, the viewer "coopted into the suspended reality" is Coleridge's poetic faith, read
through Walton's make-believe and Murray's "active creation of belief".

**Counter.** Coleridge's phrase is the *willing* suspension of disbelief: the viewer consents, the
platform user may not. Tomko shows the phrase has been doing different work since 1817; Walton drops
belief altogether. If c8 treats the two as one mechanism, the consent asymmetry is the finding, not
a flaw.

**Queries:**
- `willing suspension of disbelief poetic faith Coleridge`
- `make-believe fiction belief Walton mimesis`
- `active creation of belief immersion narrative`
- `lock-in switching costs network effects dependency`
- `platform co-optation actors assets activities`
- `suspension of disbelief film animation audience consent`

**Anchors.**
- Coleridge 1817, *Biographia Literaria*, ch. XIV [R: OL26034W, 1817]. "That willing suspension of disbelief for the moment, which constitutes poetic faith" is the line to quote with a page from a named edition (c8 and its counter). Public-domain text.
- Walton 1990, *Mimesis as Make-Believe*, Harvard UP [R: OL4801866W]. Props and games of make-believe without belief (c8). Book.
- Tomko 2016, *Beyond the Willing Suspension of Disbelief: Poetic Faith from Coleridge to the Present*, Bloomsbury [R: OL21146931W; chapter DOIs 10.5040/9781474218627]. The phrase's career (counter). Book.
- Ferri 2007, *Willing Suspension of Disbelief: Poetic Faith in Film*, Continuum [R: Choice review 10.5860/choice.45-1928; no direct book record]. Film's version (c8). Book.
- Murray 1997, *Hamlet on the Holodeck*, Free Press/MIT [R: OL15855496W]. Interactive media and the "active creation of belief" (c8, c10). Book.
- Zuboff 2019, *The Age of Surveillance Capitalism* [R: OL18201749W; record year 2018], stretch, dependency by design. Schilling 2002, "Technology success and failure in winner-take-all markets", *AMJ* 45(2) [R: 10.2307/3069353], stretch. Holland 2003, "The willing suspension of disbelief: a neuro-psychoanalytic view", *PsyArt* [unconfirmed], dropped unless S2 finds it.

**Target.** 5 new (Coleridge, Walton, Tomko, Ferri, Murray). Stretch: 7.

**Pointers.** research: `shapirovarian1999` (full), `arthur1989` (full), `farrellklemperer2007`
(full), `selznick1949` (full), `stark2024` = D. Stark & Vanden Broeck, "Principles of algorithmic
management", *Organization Theory* [R: 10.1177/26317877241257213] (full; also `lima/starkvandenbroeck2024`).
dial: `seaver-2019-captivating-algorithms` (verified). Six pointers; the registry's ~40 other
co-optation cards (Coy, Selznick 1948, Burt 1980 and the autocracy literature) stay as a reserve.

## F10 Triadicity: lab criterion, Simmel, many animators (c9)

**Establish.** The lab's criterion for a genuine triad (the third commits binding determinations,
holds its own interest, keeps the parties apart) is already carded across `triadic`, `peircean` and
`monograph`. New work here is small: brokerage as the sociological form of the third (Stovel & Shaw)
and the "many hands" problem for a studio that is many animators (Nissenbaum; Thompson).

**Counter.** The moderated-dyad objection: an animator may only mediate audience and film without
determining either. L. Stark's many animators (staff, raters, moderators, authors) and his "final
uncompensated animator" (the user) both multiply the third and put the user on its side. Cameron et
al.'s social triad (user, robot, deployer) is the HRI version the paper must distinguish itself from.

**Queries:**
- `brokerage third party tertius sociology review`
- `problem of many hands responsibility computer systems`
- `social triad model deployer trust human robot`
- `Simmel triad tertius gaudens mediator`
- `moderated dyad versus triad intermediary determination`

**Anchors.**
- Stovel & Shaw 2012, "Brokerage", *Annual Review of Sociology* 38 [R: 10.1146/annurev-soc-081309-150054]. The third as broker (c9).
- Nissenbaum 1996, "Accountability in a computerized society", *Science and Engineering Ethics* 2 [R: 10.1007/bf02639315]. Many hands as the shape of a studio's responsibility (c9, counter).
- Thompson 1980, "Moral responsibility of public officials: the problem of many hands", *APSR* 74(4) [R: 10.2307/1954312], stretch. Krackhardt 1999, "The ties that torture: Simmelian tie analysis in organizations" [unconfirmed as the original; only a 2018 secondary record 10.1007/978-3-658-21742-6_70], stretch.

**Target.** 2 new (Stovel & Shaw; Nissenbaum). Stretch: 4.

**Pointers.** triadic: `simmel1902number1`, `simmel1902number2` (verified) [R: 10.1086/211115,
10.1086/211128], `caplow1956theory`, `caplow1968coalitions` (metadata). designeth: `simmel1950` ("The
triad", full). lima/research: `obstfeld2005` (full), `burt1992`. peircean: `halevy2019brokerage`
(abstract), `peirce1906prolegomena` (full). dxda: `cameron2024social` (full) [R: 10.1007/s12369-023-01048-3;
record year 2023], `stark2024animation` (full) for the many animators. Ten pointers.

## F11 LLMs as characters and role play (c12, c10)

**Establish.** The nearest prior literature reads the *character the user meets*: L. Stark's animated
character, Shanahan's role play, Bernini's fictive interaction built on Dennett's real patterns,
Magee et al.'s "automated subject", Maeda & Stark's co-animation, Jones's "enoughness". The paper
positions against all of them by reading the making, not the meeting.

**Counter.** If the character literature already covers interface, opacity (Stark's hidden labour)
and manipulation (Stark's third trait), then c12 must show that production is a different object,
not the same object seen from behind.

**Queries:**
- `large language model animated character chatbot`
- `role play dialogue agents simulacra`
- `AI as character fiction intentional stance`
- `anthropomorphism dialogue systems mirages`
- `automated subject large language model psychoanalysis`
- `talking about large language models anthropomorphic language`

**Anchors.**
- Bernini 2025, "AI as character: real patterns in fictive interactions", *Style* 59(3) [R: 10.5325/style.59.3.0466]. The sketch's short title is confirmed; the subtitle names Dennett 1991 (c12).
- Magee, Arora & Munn 2023, "Structured like a language model: analysing AI as an automated subject", *Big Data & Society* 10(2) [R: 10.1177/20539517231210273]. **The sketch's subtitle ("Interdiscursivity and the construction of large language models") does not match the record**; the record's subtitle is given here and `CITED_WORKS.md` should be corrected at S2 (c12).
- Shanahan 2024, "Talking about large language models", *CACM* 67(2) [R: 10.1145/3624724]. How to describe an LLM without anthropomorphism (c10, c12).
- Mitchell & Krakauer 2023, "The debate over understanding in AI's large language models", *PNAS* 120(13) [R: 10.1073/pnas.2215907120], stretch.

**Target.** 3 new (Bernini, Magee et al., Shanahan 2024). Stretch: 4.

**Pointers.** dxda: `stark2024animation` (full) [R: 10.1145/3630106.3658995], `shanahan2023role`
(full) [R: 10.1038/s41586-023-06647-8], `maeda2025anthropomorphism` (full) [R: 10.1609/aies.v8i2.36664,
"Anthropomorphism as social affordance: charting the co-animation of chatbots..."], `jones2026animating`
(full) [R: 10.1017/s0267190526100312, "Animating AI: language variation and 'enoughness' in voice
user interfaces", *ARAL*], `abercrombie2023mirages` (full) [R: 10.18653/v1/2023.emnlp-main.290],
`weizenbaum1966eliza` (abstract). Six pointers.

## F12 Venue: *Philosophy & Technology* 2019–2026 (c12, c7, c5)

**Establish.** What the journal has already said about opacity, anthropomorphism, agency without
intelligence, LLM intentionality and artificial life, so that §2, §4.2 and §7 speak to its own
conversation. OpenAlex source `S23735784` (ISSN 2210-5433 / 2210-5441; 1,220 works). The twelve
below are **triage candidates, not decisions**: S3 reads abstracts and keeps about ten.

**Counter.** Floridi's "agency without intelligence" line (2023, 2025, 2026) is the venue's dominant
frame for LLMs and it denies the thing the paper wants to animate; Howdle's two anthropomorphic
errors and Bottazzi & Ferrario's "bewitching AI" treat the character reading as an error to correct,
which is the reviewer the paper will meet.

**Queries:**
- `Philosophy and Technology opacity explainability black box`
- `Philosophy and Technology anthropomorphism chatbot large language models`
- `Philosophy and Technology artificial life embodiment artificial intelligence`
- `Philosophy and Technology AI agency without intelligence`
- `Philosophy and Technology large language models intentionality grounding`
- `Philosophy and Technology definition of artificial intelligence generative`

**Anchors** (all from the filtered OpenAlex query today; cited-by counts as of 2026-11-08).
- Zednik 2019, "Solving the black box problem: a normative framework for explainable AI" [R: W2955132579; 10.1007/s13347-019-00382-7] (477 cites). F7.
- Vaassen 2022, "AI, opacity, and personal autonomy" [R: W4296638419; 10.1007/s13347-022-00577-5]. F7, c11.
- Hähnel & Hauswald 2025, "Trust and opacity in artificial intelligence: mapping the discourse" [R: W4412903806; 10.1007/s13347-025-00947-9]. F7 map.
- Schmidt & Putora 2025, "The epistemic cost of opacity" [R: W4406334317; 10.1007/s13347-024-00834-9]. F7.
- Floridi 2023, "AI as agency without intelligence: on ChatGPT, large language models, and other generative models" [R: W4360957277; 10.1007/s13347-023-00621-y] (547 cites). F3 counter.
- Floridi 2025, "AI as agency without intelligence: on artificial intelligence as a new form of artificial agency" [R: W4408055303; 10.1007/s13347-025-00858-9]. F3 counter.
- Floridi 2026, "AI and semantic pareidolia: when we see intelligent consciousness where there is none" [R: W7130505239; 10.1007/s13347-026-01052-1]. F11 counter.
- Howdle 2026, "Anthropomorphising AI: two modes, two errors" [R: W7168404739; 10.1007/s13347-026-01133-1]. F11 counter.
- Bottazzi & Ferrario 2025, "The bewitching AI: the illusion of communication with large language models" [R: W4410092719; 10.1007/s13347-025-00893-6]. F9/F11: illusion as co-optation.
- Gubelmann 2024, "Large language models, agency, and why speech acts are beyond them (for now)" [R: W4392110156; 10.1007/s13347-024-00696-1]. F3.
- García-Valdecasas 2026, "Are large language models intentional? The limits of referential grounding" [R: W7140189339; 10.1007/s13347-026-01079-4]. F3.
- Rolla 2026, "The embodiment challenge for artificial intelligence" [R: W7166733588; 10.1007/s13347-026-01139-9]. F2: the autonomy tradition inside the venue.
- Also returned, lower priority: Kim 2025, "Evolutionary computation as algorithmic metaphor" [R: W7116427126]; Mollema 2026, "On large language models, de-anthropomorphized narrative production, and deflationary understanding" [R: W7118128940]; Ronge & Maier 2025, "Towards a definition of generative artificial intelligence" [R: W4408135766]; List 2021, "Group agency and artificial intelligence" [R: W2946798032] (F10-adjacent).

**Target.** 10 new from the twelve. Stretch: 13.

**Pointers.** Zerilli et al. 2019 is carded under F7 and counts there. The registry's own *P&T*
cards (`research/danaher2016`, `designeth/vallor2015`, `research/mohamed2020`,
`coordsov/floridi2020fight`) fall outside the topic or the window and are not pointers here.

## G Gap check: prior work framing AI development as animation craft, or AI as life in the making (c12)

**Establish.** Two gap claims. (A) Nobody frames AI *development* (the harness, not the interface) as
animation-like craft. (B) Nobody argues AI is better conceived as artificial life in the *making*
sense (as a craft of bringing to life), as against the lineage sense (Berthon) or the embodiment
sense (Froese & Ziemke; Rolla). Two searches are already run and count as S2 evidence:
`dxd_animation_local/consensus/G_llm_as_animation.txt` (50 papers, 2026-11-05; top hits L. Stark
2024, ChatHaruhi, Shanahan 2023) and `G_F9_animation_principles_agents.txt` (50 papers, 2026-11-05;
animation principles in virtual agents, Parmar 2022, André 1999). Both find the interface, not the
making.

**Counter.** The OpenAlex probe today found one preprint that joins Thomas & Johnston's *Illusion of
Life* to AI's "missing in-between frames" and argues the *opposite* conclusion (illusion of thinking,
not thinking); see Govind 2026 below. (A) survives as stated (it is not about development) but §4.2
must cite it.

**Queries:**
- `artificial intelligence development as animation craft character pipeline`
- `AI engineering bringing a character to life studio production`
- `large language model artificial life making sense craft`
- `illusion of life animation principles artificial intelligence inbetween frames`
- `machine organism language epistemology AI models`
- `open-ended intelligence large language models artificial life`

**Anchors.**
- Govind 2026, "The illusion of mind: what Disney animation teaches us about AI's missing inbetween frames", Zenodo preprint [R: W7133553834; 10.5281/zenodo.18859161]. Nearest prior to §4.2; argues AI is illusion of thinking as animation is illusion of life. Card as `contrast`, abstract depth, and read before §4.2 is drafted (c7, c12).
- Pasquinelli 2026, "Machine, organism and language: a comparative epistemology of AI models", *AI & Society* [R: 10.1007/s00146-026-03094-7]. Nearest prior to (B) from media theory (c12).
- Karelin, Nakajima & Soto-Astorga 2025, "Indeterminism in large language models: an unintentional step toward open-ended intelligence", PhilSci-Archive [R: W7110543113]. LLMs read through ALife's open-endedness (B neighbour; also Berthon's).
- Dorin & Stepney 2023, editorial on LLMs and ALife [R: 10.1162/artl_e_00409]: counted under F1.
- Sennett 2008, *The Craftsman* [R: OL1870880W], stretch, if "craft" needs a theory. Pasquinelli & Joler 2020, "The Nooscope manifested", *AI & Society* 36 [R: 10.1007/s00146-020-01097-6], stretch.

**Target.** 3 new (Govind, Pasquinelli 2026, Karelin et al.). Stretch: 5. Everything else is a
logged negative result in `GAP_CHECK.md`, in the form "I found no work that does X in [sources]".

**Pointers.** dxda: `stark2024animation`, `jones2026animating` (both full): the interface readings
(A) positions against. research: `seaver2017` (full), "Algorithms as culture", the ethnographic
"making" literature that never names animation. Three pointers.

## Totals

Core: 72 new, 46 pointers, 4 upgrades. Stretch adds about 14. Every pointer key above was checked
against `registry.tsv` on 2026-11-08; every [R] id was returned by a lookup the same day (about 110
requests across Crossref, OpenAlex and OpenLibrary).

## Anchors marked [unconfirmed] today

Sculley et al. 2015 (the NeurIPS paper; only a 2021 chapter and citing works have records); Zaharia
et al. 2024 (blog post, web only); Mossio & Moreno 2010, *HPLS* (replaced by Montévil & Mossio 2015);
Kleist 1810 (the original item; a 2011 chapter record confirms the text); Holland 2003 *PsyArt*;
Kapoor et al. 2024; Krackhardt 1999 (secondary record only); Thomas & Johnston 1981 on OpenLibrary
today (the dxd run's OL2924612W stands). Nothing in their entries was filled in from memory.

## Rules for S2 and S3

1. Search each facet in at least two sources; log every query in `SEARCH_LOG.md`.
2. Every hit carries an OpenAlex id, DOI, ISBN or OpenLibrary id, or is dropped.
3. Tag hits already in `registry.tsv` as `in_registry`; they become pointers, or upgrades only for the four named above.
4. Keys follow `firstauthorsurnameYEARfirsttitleword`.
5. Two Starks: `stark2024animation` is Luke Stark; `stark2024` is David Stark & Vanden Broeck. Cite with initials.
6. Nothing from memory: each title, author, year, DOI or quotation needs a record or read text.

## Checkpoint A — decisions for Roger

1. **Books to open in a browser (§2 and the two craft anchors).** The library can only write
   metadata cards for these unless you open them: Maturana & Varela 1980, *Autopoiesis and Cognition*
   [OL15015691W]; Moreno & Mossio 2015, *Biological Autonomy* [10.1007/978-94-017-9837-2, Springer,
   likely on institutional access]; Cleland 2019, *The Quest for a Universal Theory of Life*
   [10.1017/9781139046893, Cambridge Core]; Dennett 1987, *The Intentional Stance* [OL2463706W];
   Thompson 2007, *Mind in Life* [OL3475244W]; and Walton 1990, *Mimesis as Make-Believe*
   [OL4801866W] for §4.3. The article substitutes (Varela et al. 1974; Montévil & Mossio 2015;
   Cleland & Chyba 2002; Dennett 1971) are open or on standard access and carry §2 if the books stay
   closed.
2. **Vital stance or organizational claim.** The stance reading rests on F3 (Dennett ×3 plus "Real
   patterns" against instrumentalism) and makes F2 background: F2 drops to 4 cards (Maturana &
   Varela, Varela et al., Moreno & Mossio, Froese & Ziemke) and F3 rises to 9 (add Chollet,
   Hernández-Orallo). The organizational reading does the reverse (F2 at 9 with Di Paolo, Montévil &
   Mossio, Bongard & Levin, Meincke; F3 at 5) and has to answer Moreno & Mossio's self-production
   requirement head-on, since humans build the harness. The lookups favour neither; the sketch's
   "so much more around that LLM" reads organizational.
3. **F5 puppetry as its own facet.** Keep it. Every F5 anchor confirmed (Auslander, Tillis, Kaplin,
   Allison, Jurkowski, Kleist via a 2011 record), the puppet literature has its own axes (Kaplin's
   tree) that §5 needs to place an LLM, and folding it into F4 would bury the limit case under the
   pipeline. Cost: 5 cards and one upgrade.
4. **Unconfirmed anchors the sketch relies on.** Sculley et al. 2015 (no record for the NeurIPS
   paper; S2 tries the proceedings page) and Zaharia et al. 2024 (a blog post; card it as a web source
   with access date or let Paleyes et al. 2022 carry c1). Also one metadata correction: Magee, Arora &
   Munn 2023 is "Structured like a language model: analysing AI as an automated subject" (*Big Data &
   Society*), not the subtitle the sketch gives.
5. **What changes the plan.** (a) Govind 2026 (Zenodo preprint, [W7133553834]) already pairs Thomas &
   Johnston's *Illusion of Life* with AI's "missing inbetween frames" and concludes AI is the illusion
   of thinking; §4.2 must cite and answer it, and the c12 gap claim should be worded as "development,
   not interface or illusion". (b) *Philosophy & Technology*'s own LLM conversation is Floridi's
   "agency without intelligence" (2023, 547 cites; 2025; 2026) plus Howdle 2026 and Bottazzi &
   Ferrario 2025 treating the character reading as error; the paper's §2 should engage Floridi
   directly, which argues for keeping F3 at least at 7. (c) Froese & Ziemke 2009 (enactive AI) and
   Rolla 2026 (in *P&T*) already bring the autonomy tradition to AI; c4 must say what animation adds
   that enactivism lacks, which is the making.

## Checkpoint A — rulings (Roger, 2026-11-08)

Recorded by Claude from the author's answers.

1. **§2 position: organizational claim.** F2 rises to 9 cards (add Di Paolo, Montévil & Mossio,
   Bongard & Levin, Meincke). F3 goes to 7, not 5, because *P&T*'s own LLM conversation is Floridi's
   "agency without intelligence" (2023, doi 10.1007/s13347-023-00621-y, 547 cites in OpenAlex; 2025,
   doi 10.1007/s13347-025-00858-9), which §2 must engage. Moreno & Mossio's self-production
   requirement is the counter c4 must answer head-on: humans build the harness.
2. **Govind 2026: cite and answer.** Full card (Zenodo preprint, doi 10.5281/zenodo.18859161,
   record checked by Claude). §4.2 answers it; c12 is worded "AI development, not the interface or
   the illusion".
3. **Books:** no answer yet. Treated as none opened: the six books go on `BROWSER_LIST.md` at S4
   and the open article substitutes carry §2 until copies land in `pt_ai_animation_local/inbox/`.
4. **F5 puppetry** stays its own facet (Fable's recommendation; not contested).
