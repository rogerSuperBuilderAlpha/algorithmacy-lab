# Check of the author's text (5 Nov 2026)

[DRAFTED by Claude, 2026-11-05.] This file checks every citation and factual claim in `SOURCE.md`
Pass 2. Each entry gives the claim as you wrote it, what the source says, and how I checked it.
**I changed none of your text.** Each flag is a decision for you.

Read depth: **full** means I read the text this session. **card** means a lab library card records
the read; its depth is given. **record** means I confirmed only that the work exists.

## Flags that need a decision

| # | Your text | What the source shows | Checked against | Suggested fix (your call) |
|---|---|---|---|---|
| F1 | "As Norman McLaren (**1968**) observed…" | I found no 1968 source. The earliest publication I can trace is McLaren's letter in Sifianos, G. (1995), "The definition of animation: A letter from Norman McLaren," *Animation Journal*, 3(2), p. 62. Furniss (*Art in Motion*, 2008) reprints the three-part definition. | Web search, secondhand. Two scholarly citations agree. I have not seen the journal page. **[VERIFY]** | Cite Sifianos (1995) and get the page. If you quote McLaren directly, copy the wording from that page, since online versions vary. |
| F2 | "Luke Stark (2024) **demonstrates**…" | The three traits are verified verbatim: "reliance on stereotypes, obfuscation of human labor, and manipulation of an audience's emotions" (Stark, 2024, p. 1663, abstract). But the paper is a conceptual argument with no empirical test. | **full** (FAccT '24 PDF, pp. 1663–1671, DOI 10.1145/3630106.3658995) | "argues" instead of "demonstrates" |
| F3 | Silvio's theory of animation as "the projection of human agency and persona onto non-human objects" | Silvio's own definition, as Stark quotes it: "the projection of qualities perceived as human—life, power, agency, will, personality, and so on—outside of the self, and into the sensory environment, through acts of creation, perception, and interaction" (Silvio, 2019, p. 52, quoted in Stark, 2024, p. 1664). It projects into the "sensory environment", not only onto "non-human objects", and lists "personality", not "persona". | **full** for Stark's quotation; Silvio's book itself is **record** only | Close as a paraphrase. Cite Silvio's p. 52, and check the page in the book before you quote it. |
| F4 | "Watching a stage actor is a **dyadic** encounter…" | Silvio draws this contrast: performance is "introjective" (the viewer identifies with the actor), while animation is projective and has a "numerical disjunct" between a character and the people who animate it (Stark, 2024, p. 1664). But Silvio also says "in practice, performance and animation are [hard] to separate" (Silvio, 2010, p. 432, quoted in Stark, 2024, p. 1668). A reviewer will say a play has a playwright and director too. | **full** (Stark) | Ground the dyad/triad in Silvio's introjection vs projection and her numerical disjunct, and concede her "hard to separate" line. That makes the triad an analytic distinction, not a claim about theatre. |
| F5 | "Choice architecture **proves** that how options are presented systematically shapes what people decide (Johnson et al., 2012)" | Johnson et al. (2012) is a review that sorts choice-architecture tools (structure vs. description). It reports no single test that would "prove" anything. The lab has **not read its text**: it's closed, and only a machine summary was available (`decision_experience_design/literature/facets/F2_choice_architecture.md`, B3). The lab *has* read Jachimowicz et al. (2019): 58 studies, *d* = 0.68, "substantial variation," two with negative effects (p. 159). | card (record only for Johnson; read in part for Jachimowicz) | "shows" or "demonstrates"; add Jachimowicz et al. (2019) as the evidence. Read Johnson 2012 through the library before relying on it. |
| F6 | "digital nudging tools (Weinmann, Schneider, & vom Brocke, 2016)" | The citation exists: *Business & Information Systems Engineering*, 58(6), 433–436, DOI 10.1007/s12599-016-0453-1. The lab could not open it (bot-walled); the definition it holds comes from the later CACM piece (Schneider, Weinmann & vom Brocke, 2018). | card (record only) | Fine as cited. Get the BISE text through the library if you define "digital nudging". |
| F7 | Burrell's three sources of opacity: "corporate secrecy, **technical specialization**, and the scale of machine learning" | Burrell's abstract names (1) "intentional corporate or state secrecy", (2) "technical illiteracy", and (3) opacity from "the characteristics of machine learning algorithms and the scale required to apply them usefully". | card is abstract-level (`hospitality_phygital/library/cards/burrell2016opacity.md`). A web search on 5 Nov confirms the three-way split: deliberate concealment, the reader's lack of technical knowledge, and ML itself. The quoted wording is **not yet confirmed**, because SAGE bot-walled the scripted fetch. **[VERIFY]** in a browser at doi:10.1177/2053951715622512 (open access) | "technical illiteracy", or "the specialist skill that reading code requires" if you'd rather not use her term |
| F8 | "Stark & Vanden Broeck, 2024" next to "Luke Stark (2024)" | These are two different Starks: **David** Stark (*Organization Theory*, 5(2)) and **Luke** Stark (FAccT). APA 7 §8.20: if two first authors share a surname, include initials in every citation. | — | "D. Stark & Vanden Broeck, 2024" and "L. Stark, 2024" |
| F9 | Platforms co-opt "external actors, assets, and **behaviors**" | The source says "actors, assets, and activities" are "not located within the firm" (p. 1), and "on platforms they are co-opted" (p. 1; p. 5). | card, **full text** (`lima_pdw/literature/cards/starkvandenbroeck2024.md`) | "activities" matches the source |
| F10 | "peering inside a black box is not the same as understanding how a system exercises power across a relational environment (Ananny & Crawford, 2018)" | Supported in substance: they hold that accountability means looking *across* a system, not *inside* it. But their argument concerns accountability, not a user's decision. Moving it to "help the user decide" is your step. | card (established citation, not re-read) | Keep, and mark the extension as yours ("Their argument about accountability applies equally to a user's decision…") |
| F11 | "(Chevalier et al., 2016)" for "the core methodologies of the animator" | The paper exists: Chevalier, F., Henry Riche, N., Plaisant, C., Chalbi, A., & Hurter, C. (2016), "Animations 25 years later: New roles and opportunities," *AVI '16*, DOI 10.1145/2909132.2909255. It reviews **interface** animation (transitions, feedback), following Baecker and Small's *Animation at the Interface*, and draws on interviews with 20 professionals. It does not cover the character animator's craft. | record (abstract via web search) | Keep it for interface animation. For the animator's method, add Thomas and Johnston (1981), *The Illusion of Life*. The phrase "illusion of life" already appears in Silvio (2010, p. 428). **[FETCH]** |
| F12 | The viewer "locks in" and "the perceptual gaps disappear" (no citation) | The perception literature calls this **apparent motion**, which goes back to Wertheimer (1912). Film scholars treat the older "persistence of vision" account as a myth (Anderson & Anderson, 1993, "The myth of persistence of vision revisited," *Journal of Film and Video*, 45(1), 3–12; record confirmed by web search on 5 Nov, text not read). The lab's Gestalt card (`dxd_foundation/literature/library/wagemans2012century.md`) is a lead to Wertheimer. | card (lead) | Cite apparent motion, and avoid "persistence of vision". This sentence carries the whole Perception section. |
| F13 | "Grok" (Pass 2) / "Grok Bot" (Pass 1) | The product is called Grok. | — | Pass 2 already has it right |

## Verified as written

- Stark (2024) treats LLM chatbots as animated characters. He builds on Silvio and calls animation a "structuring trope" (Silvio, 2010, p. 422, quoted in Stark, 2024, p. 1663). **full**.
- D. Stark and Vanden Broeck (2024) on co-optation: "whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted" (p. 1). **card, full text**.

## Found while checking (strengthens your argument)

- **The user is also an animator.** "The final uncompensated animator of any particular ChatGPT instance is the individual human user interacting with the system. It is, after all, a user's prompts that help populate an instance" (L. Stark, 2024, p. 1667). Your co-optive point (the viewer's own perception supplies the continuity) has a second layer here: the user's prompts supply the character too. This puts the user inside the triad rather than outside it.
- **Streamed tokens are literal frames.** Liu et al. (2024, *Andes*, preprint) set token delivery to reading speed, 4.8 tokens/s, using a client-side "token pacer". Xiao and Yang (2025) slow complex segments and speed simple ones. Platforms already set the frame rate, which makes "missing frames" a measurable design variable rather than a metaphor (`spaces/research/notes/andes2024.md`, `xiaoyang2025.md`).
- **Event boundaries matter for decisions.** Zacks, Speer and Reynolds (2009) found that viewers and readers perceive event boundaries where the situation changes. The lab's notes on Ongchoco et al. (2023) show that boundaries limit anchoring. That gives the "missing frames" a decision-level effect (`spaces/research/notes/zacks2009.md`, `ongchoco2023.md`).

## Not recorded anywhere in the repo

The final paper's due date, length and rubric. Nor whether this change of topic from the approved DIAL
proposal needs Ericson's agreement. The `dxd_foundation` change raised the same question and it was
never answered.

## Library update, run dxda-lib-2026-11 (S10)

> [DRAFTED by Claude, 2026-11-05.] The flags above are left as first written. These rows say what
> the library run found for each one; the cards are in `library/cards/`. Your text in `SOURCE.md` is
> unchanged. Each correction below is a flag for you to decide.

| Flag | Update | Card(s) |
|---|---|---|
| F1 | Still no citable McLaren source. Sifianos (1995) and Furniss (2008) are not held; both are on `library/BROWSER_LIST.md`. | `furniss2008art` (metadata) |
| F2 | Unchanged: "argues". Stark's own framing is "to demonstrate the utility of such a frame" (§1). | `stark2024animation` (full) |
| F2, "Verified as written" | **Correction to this file:** the "structuring trope" quotation is on **p. 1664**, not p. 1663 (PDF p. 2; range 1663–1671 confirmed on Crossref). | `stark2024animation` |
| F3 | Silvio's book and article are still unread; p. 52 and pp. 422/428/432 reach the lab only through Stark. Maeda & L. Stark (2025) attribute the definition to Silvio **2010**, Stark (2024) to Silvio **2019** p. 52; only Silvio's texts settle it. | `silvio2019puppets` (metadata), `silvio2010animation` (abstract), `maeda2025anthropomorphism` (full) |
| F4 | Unchanged. Stark adds that a chatbot's animators are **many** (staff, raters, moderators, authors, and the user as "final uncompensated animator", p. 1667). The singular "animator" in your text stretches him. | `stark2024animation` |
| F5 | Johnson 2012 now read (OJS republication); it supports "shows", not "proves". Jachimowicz: "58 datasets from 55 studies" (p. 163) is more exact than "58 studies". | `johnson2012beyond` (full), `jachimowicz2019when` (partial) |
| F6 | Weinmann 2016 and Schneider 2018 carded. | `weinmann2016digital` (full), `schneider2018digital` (abstract) |
| F7 | **Resolved.** The monograph library's full-text card quotes Burrell's abstract: "technical illiteracy". | pointer `burrell2016how` (D/, private) |
| F10 | Ananny & Crawford is still abstract-only; the step to the user's decision stays yours. | `ananny2018seeing` (abstract) |
| F11 | Confirmed: Chevalier et al. review interface animation, not the animator's craft. Thomas & Johnston (metadata) and Lasseter 1987 (abstract) are carded but unread. | `chevalier2016animations` (full), `thomas1981illusion`, `lasseter1987principles` |
| F12 | **The fix is disputed.** Hoerl (2015) and Steinman, Pizlo & Pizlo (2000) contest the standard apparent-motion account. Hoerl's accepted version is now held but not yet re-carded. Wertheimer is still unread (German scan not tried). | `wertheimer1912experimentelle`, `anderson1993myth`, `hoerl2015seeing`, `steinman2000phi` |

**Correction to OUTLINE.md:** OUTLINE ties the ELIZA effect to Stark p. 1667. Its definition is on
**p. 1665** (§2.1). p. 1667 carries the user-as-animator sentence.

## Library update, run dxda-lib-2026-11b (11 Nov 2026)

> [DRAFTED by Claude (Opus 5.5), 2026-11-11.] What run 2 found for each flag. The flags above and your
> text in `SOURCE.md` are unchanged; `DRAFT_v1.md` carries each flag as a bracketed note after your
> sentence.

| Flag | Update | Card(s) |
|---|---|---|
| F1 | Still no McLaren source. Lasseter (1987, p. 37), read in full, gives a citable craft statement of the same point: weight "depend[s] entirely on the spacing of the poses and not on the poses themselves". Noted in the draft, not substituted for your sentence. | `lasseter1987principles` |
| F2, F3 | Unchanged. | — |
| F4 | Unchanged; the draft treats "animator" as a seat several parties fill (MODEL D-c). | `stark2024animation` |
| F5–F10 | Unchanged; carried as notes in the draft. | — |
| F11 | **Resolved for the paper's purpose.** Lasseter (1987) states the animator's principles and is read in full; Chang & Ungar (1993) and Thomas & Calder (2001) carry them into interfaces, also in full. Chevalier et al. still do not describe the craft. Thomas & Johnston remain unread (a loan is needed). | `lasseter1987principles`, `chang1993animation`, `thomas2001applying` |
| F12 | Hoerl (2015) now read in full: cinematic motion is not Wertheimer-type apparent motion, and the motion seen at normal speed is real. The draft drops apparent motion as a mechanism (MODEL D-e) and uses Hoerl only for "inspecting frames loses what the viewer needed", with the analogy to AI output marked as the paper's. | `hoerl2015seeing` |
| new | **"Twelve principles"**: Lasseter lists eleven; Pinhanez, Ribeiro & Paiva and Schulz say twelve, citing Thomas & Johnston. The draft uses eleven. | `lasseter1987principles` |
| new | **"Intent specification"** is already used by Leveson (2000) and Vaithilingam et al. (2025); the draft contrasts them (MODEL D-l). | `leveson2000intent`, `vaithilingam2025semantic` |
