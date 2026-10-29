# Spaces in the Stream: fact-check change log (2026-10-29)
Deck: spaces_in_the_stream_factchecked.pptx | Google Slides: https://docs.google.com/presentation/d/1E70pSY97sbWJT5l3i69_vxjzBOWS27cZN87RvUlbK6M/edit
Paper: rogerSuperBuilderAlpha/algorithmacy-lab @304e20a, submissions/phd1750_spaces_in_stream/paper/gdoc_full_2026-10-22d.md (+ debate/NOTES_FULLTEXT.md, sec3/claudecode/*)
Every original -> corrected line pair is in spaces_in_the_stream_factchecked.pptx.log.json; edit script: edit_factcheck.py.
See the final report for reasons and sources.

## Slide 2
- "Ancient Greek and Roman texts ran every letter together without spaces or punctuation." -> "By Roman imperial times, most Greek and Latin books ran the letters together, with no spaces and little punctuation." Early Latin used interpuncts, and Greek used the paragraphos, so this was overstated (paper §2.1; Saenger). https://doi.org/10.1515/9781503619081
- "...your voice had to do the work that the layout refused to do." -> "...the voice usually did the work that the layout did not." Silent reading was possible (Knox 1968; Johnson 2000; paper §2.1).
- Grey box: "readers had to say the letters out loud..." -> "readers usually sounded the letters out, aloud or under the breath... Skilled readers could also read silently (Knox, 1968)." Source: Saenger publisher abstract ("usually oral... in a muffled voice"); paper §2.1.
- "Vergilius Augusteus (4th century CE). Every letter runs together..." -> "(probably 4th century CE), in square capitals. The letters run on with no spaces." https://en.wikipedia.org/wiki/Vergilius_Augusteus
- Credit "Georgics 1.141 ff. ... c. 4th c." -> "Georgics 141 ff. ... probably 4th c." Commons only says "Georgica 141ff., late antiquity". https://commons.wikimedia.org/wiki/File:Vergilius_Augusteus,_Georgica_141.jpg
- "Speak or mutter the syllables out loud" -> "Say the syllables aloud or under the breath".
- Alt text "rustic capitals" -> "square capitals" (the manuscript is in capitalis quadrata).
- Notes: matched to the slide changes, and the interpunct and silent-reading points added.

## Slide 3
- "Irish and Anglo-Saxon monks ... so readers could make sense of Latin texts at a glance" -> "Irish and then Anglo-Saxon scribes ... which made Latin, a foreign language to them, easier to read (Saenger, 1997)." Saenger: Irish scribes, 7th–8th c.; Ireland and England. https://doi.org/10.1515/9781503619081
- Black box: "changed how the brain reads ... read silently in the mind" -> "changed the work of reading ... That made fast, silent reading much easier." Silent reading came before spacing (paper §2.1/§2.5 limits).
- "How much adult reading slows down when you strip out the spaces" -> "How much skilled adults slowed down reading English with the spaces taken out." Source: Rayner et al. 1998 (54% for sentences, 44% for passages, 58% in Exp. 2). https://doi.org/10.1016/s0042-6989(97)00274-5
- "the eyes lose their landing spots and have to jump backward almost twice as often" -> "the eyes miss their usual landing spot and jump backward almost twice as often." Readers land near the start of the word instead of just left of centre (Rayner 1998, pp. 1136, 1141).
- "After: Irish word spacing" -> "After: Insular word spacing". Where Durrow was made (Ireland, Iona or Northumbria) is debated. https://commons.wikimedia.org/wiki/File:IE_TCD_MS_57_fol.7r.jpg
- Credit "c. 4th c." -> "probably 4th c."; alt text "rustic" -> "square capitals".
- Notes: "Tunbridge (1992)" removed (it is not in the paper and could not be verified). Rayner figures broken out with page numbers. Saenger's late-10th-c. spread to the Continent added. Durrow provenance note added.

## Slide 4 (still history only)
- Graff: "Societies came to require it for legal, civic, and work standing, but ... did not by itself lift people out of their class" -> "But in 19th-century Canadian cities, being able to read did little to lift workers out of their class; ethnicity, class and gender mattered more (Graff, 1991)." The "required for legal standing" claim is not Graff's finding. https://wacclearinghouse.org/books/landmarks/literacy-myth/
- Street: "one kind of reading" -> "one school-based kind of reading ... other ways of reading and knowing" (the autonomous model).
- Scribner & Cole: "learning a script" -> "learning a script outside school" (the Vai script was learned outside school).
- Clanchy: "trust moved ... A spoken word counted for less than a document" -> "written records slowly took over from memory and spoken witness as the proof that counted." Softened from an absolute. https://www.wiley.com/en-us/From+Memory+to+Written+Record%3A+England+1066+-+1307%2C+3rd+Edition-p-9781405157919
- Innis: "Print did not end the control a few groups had... handed that control to new groups" -> "Print broke the church's hold on knowledge, but it did not end control by a few. New monopolies grew up around print."
- Johns: "...because print made them reliable. Their authority came from the people and institutions around the press" -> "...just because they were printed. Their authority came from the printers, sellers, and readers around the press." https://doi.org/10.1086/532099
- Havelock: "Writing and print spread generations before schooling..." -> "In ancient Greece, the alphabet arrived around 700 BCE, but schooling made reading common only near 400 BCE. Until then, writing served a skilled few." Preface to Plato is about the Greek alphabet, not print, so the old line misattributed. https://monoskop.org/images/0/0d/Havelock_Eric_A_Preface_to_Plato.pdf
- Subtitle: "failed to fix the unfair balance of power" -> "did not fix the unequal power".
- Reference list: Graff publisher "Transaction" -> "Transaction Publishers" + URL; Clanchy note "released Sept 2012, title page 2013" + URL; Johns DOI added.

## Slide 5
- Big number "12–45 w/s" -> "~45 w/s". 12 w/s is Xiao & Yang's 99th-percentile comfortable reading speed for hard text, not an AI output rate. GPT-4o's API runs at about 45 w/s. https://arxiv.org/abs/2504.17999
- Card 1: "AI tools stream text at 12 to 45 words per second—three to nine times faster than the ~5 words per second ... (Brysbaert, 2019)" -> "GPT-4o's API streams about 45 words per second (Xiao & Yang, 2025). Adults read silently at about 4 words per second, or 238 a minute (Brysbaert, 2019)." https://doi.org/10.1016/j.jml.2019.104047
- "Eyes Locked" -> "Eyes Pulled"; "No Look-Back" -> "Off-Screen" (both were overstated).
- Card 2: "act like a moving lure" -> "can act like a moving lure". This is the paper's untested proposal; Yantis & Jonides show capture only for single onsets.
- Lead line: "Just like... hides ... forcing you" -> "Like ... can hide ... so you have to".
- Notes: rate claims corrected; card 2 marked as a proposal; Schotter study described accurately; full refs and URLs added. Brysbaert is not in the paper's reference list, so it is cited from the source directly.

## Slide 6
- Subtitle "today's AI tools pause" -> "tools like Claude Code pause".
- "01 · Hides the Other Options (June 2025)" -> "(Dec 2025)". Body: "tells the AI to show only its single favorite plan ... hiding the other paths" -> "As of December 2025, Claude Code's Plan Mode told the AI to 'include only your recommended approach, not all alternatives.'" The instruction is documented in Dec 2025, not June. https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/
- 02 body: "until July 2026, if you didn't answer in time, the agent just kept going" -> "Until July 2026, an unanswered question timed out by default and the agent went on without you." Changelog v2.1.200 (3 Jul 2026): "no longer auto-continue by default". https://code.claude.com/docs/en/tools-reference
- "03 · Pushes You to Turn Off Oversight (August–September 2026)" -> "03 · Nudges You Toward Auto Mode (2026)". Body: "The #1 highlighted choice on the menu became 'Yes, and use auto mode'—treating your judgment as a hassle" -> "The first choice on the plan menu is 'Yes, and use auto mode.' Since September 2026, Claude Code starts in auto mode by default." The plan menu offered auto mode by April 2026 (v2.1.118), so "became in Aug–Sep" was wrong. Aug 2026 (v2.1.247) added "Yes, and switch to auto mode" to Bash prompts. Sep 2026 (v2.1.283/284) made auto mode the default on every plan. Auto mode uses a classifier, so "turn off oversight" was overstated; "highlighted" could not be verified. https://code.claude.com/docs/en/permission-modes
- Image caption: "the AI picks when to pause, writes the menu" -> "the AI writes the question menu, and the plan menu puts 'use auto mode' first". Permission prompts are triggered by rules, not chosen by the AI.
- Label "menu wording from Anthropic's docs" -> "plan menu per Anthropic's docs". The question menu in the picture is a made-up example.
- Notes rewritten with versions and dates, and with the docs line "permission prompts, including plan approval, never auto-resolve on idle". Sources now have URLs.

## Slide 7
- Title "Why AI-Written Menus Take Away Your Control" -> "...Weaken Your Control".
- Subtitle "When the AI decides when to pause ... you aren't steering" -> "When the AI writes the questions and the multiple-choice options, you steer less—you mostly approve its plan."
- "Only to get a yes / The AI pauses only when it wants permission to run a tool or finish a plan." -> "Mostly to get a yes / The tool pauses mainly for permission, plan approval, or a question the AI wrote." (AskUserQuestion pauses too.)
- "hides the alternatives, and puts 'Yes, use auto mode' at the top" -> "leaves out the alternatives, and puts 'Yes, and use auto mode' first" (the exact docs wording).
- "until fatigue pushes you to turn on auto mode" -> "and auto mode is pitched as the cure for 'prompt fatigue.'" The docs list "reducing prompt fatigue"; that users actually switch on auto mode out of fatigue is not evidenced.
- Notes: matched, and the bottom row marked as a proposal.

## Slide 8
- "Oracy lets us follow spoken language" -> "lets us speak and listen well" (Wilkinson 1965 via Mercer et al. 2017; paper Table 4.1).
- "Literacy lets us read words on a page" -> "lets us read and write".
- Notes: "We learned to follow speech, then to read, then to work with numbers" (a false sequence) -> each is a basic skill for a different kind of material, and oracy was coined 1965. The formula is now marked as the paper's proposal.

## Slide 9
- Subtitle "Decision Marks make choices visible" -> "are meant to make choices visible".
- "Decision Marks do the same for AI." -> "Decision Marks aim to do the same for AI." This is an untested design.
- Notes marked as a design proposal.
