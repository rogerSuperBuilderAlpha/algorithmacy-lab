# Decision Experience Design and the animator (research project — opened 2026-11-03)

**Owner:** Roger Hunt. **Status:** opened 2026-11-03. Call for papers drafted
([`CALL_FOR_PAPERS.md`](CALL_FOR_PAPERS.md)); first-round card library of 31 verified sources, all read
from abstract and record only. Agent-drafted; the author has not reviewed it.

**What this project is.** A call for papers, and the research behind it, that re-focuses Decision
Experience Design (DXD) on one proposal: when people use LLM agents they are engaging an animation, so
the designer of a decision experience should learn the animator's methods. It builds on the DXD arm in
[`../decision_experience_design/`](../decision_experience_design/) (Part 1, published 2026-09-30) and the
card library in [`../dxd_foundation/literature/library/`](../dxd_foundation/literature/library/INDEX.md),
which already carries cards for `gray2018dark` and `mathur2019dark` read in full.

**The shift.** Design used to guide a user to an end both sides agreed on (buy the raincoat). With
agents, the user is often still working out the end (raincoat or umbrella?). DXD measures how well the
user reaches their own decision and is then shown ways to act on it, not conversion or stickiness.

## Three pillars

| Pillar | Claim | Cards |
|---|---|---|
| 1. The human user | The user is the human: cognitive, biological, emotional. Agent experience is set aside. | Simon 1955; Slovic 1995; Klein et al. 2006; Vohs et al. 2008; Thaler & Sunstein 2008; Johnson et al. 2012; Fogg 2002; Gray et al. 2018; Mathur et al. 2019; Horvitz 1999; Lee & See 2004; Luger & Sellen 2016; Amershi et al. 2019; Bansal et al. 2021; Vasconcelos et al. 2023 |
| 2. The platform | The environment is a platform: opaque, cooptive, triadic. | Gillespie 2010; Burrell 2016; Kellogg et al. 2020; Rahman 2021 |
| 3. The animator's aesthetic | LLMs are engaged as animations: missing frames (opaque), lock-in (cooptive), character moved by an animator (triadic). | Wertheimer 1912; Heider & Simmel 1944; Thomas & Johnston 1981; Lasseter 1987; Anderson & Anderson 1993; Chang & Ungar 1993; McCloud 1993; Reeves & Nass 1996; Wells 1998; Epley et al. 2007; Lamarre 2009; Mori et al. 2012 |

## Open research questions

1. What does a DXD interface measure in place of conversion? Can "the user reached a decision they
   endorse" be operationalised?
2. Which decisions should an agent surface, and when? (Horvitz's expected-utility account is a start.)
3. Is the lock-in of animation (closure, apparent motion) the same mechanism by which users stop
   seeing an agent's gaps? Anderson & Anderson (1993) warn against the persistence-of-vision myth;
   the analogy must rest on apparent motion and active viewers, not passive ones.
4. Do the animator's principles (timing, anticipation, staging) transfer from motion to dialogue and
   decision steps, as Lasseter showed they transferred from paper to 3D?
5. Limited animation (Lamarre) makes gaps part of the style. Should DXD show an agent's missing frames
   rather than hide them?
6. In the triad user–character–animator, who is the animator of a chat agent: the model provider, the
   platform, or the retailer? How does that differ from the triads in `org_frontier/`?
7. Where does the animation analogy break (users talk back; characters in film do not)?

## Reading list

The 31 cards, with full references and citation counts, are indexed in
[`literature/library/INDEX.md`](literature/library/INDEX.md); BibTeX keys are in
[`literature/references.bib`](literature/references.bib). Next step: read the pillar-3 sources in full
first, since they carry the new argument.

| File | What it is |
|---|---|
| `CALL_FOR_PAPERS.md` | The DXD call, from the author's framing of 2026-11-03 |
| `literature/references.bib` | Verified references |
| `literature/library/` | One card per source; `build_index.py` builds `INDEX.md` |
