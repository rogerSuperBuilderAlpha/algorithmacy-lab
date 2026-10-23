# Poster plan & design doc — *Coordinative Sovereignty*
### Society of Business Ethics (SBE) poster session · build target: single-slide PPTX

> **How to use this doc.** Paste it into a fresh Claude Code session opened in this repo. It is
> self-contained: it carries the full poster copy, the layout grid with coordinates, the visual system,
> four diagram specs, and a `python-pptx` build recipe. The executing session should build
> `poster/coordinative_sovereignty_poster.pptx` and export a print PDF. Source-of-truth facts are quoted
> below with repo file pointers so nothing needs re-deriving; where a number is quoted, keep it exact.
>
> **Before building, confirm the three items in §10.** The most important is the physical poster size.
>
> **Build status (2026-07-21):** a first proof is already built — `build_poster.py` (implements this spec,
> 48×36 landscape, applied-forward) → `coordinative_sovereignty_poster.pptx` (130 native shapes, geometry
> validated, QR placeholder embedded). It was **not** rendered to an image here (no LibreOffice in-env), so
> **open it in PowerPoint/Keynote and eyeball text-fit within panels before printing**, then Save-As-PDF.
> To iterate, edit `build_poster.py` and re-run `python3 build_poster.py`.

---

## 1. Deliverable & constraints

- **What:** one printed research poster for the SBE poster session (a *conceptual/framework* poster, not an
  empirical-results poster). Deadline: this is needed for a conference **next week** — build must be
  right-first-time; leave the author only content edits, not a redesign.
- **Format:** a **single-slide PowerPoint (.pptx)** sized to the poster, built with `python-pptx`, then
  exported to a single-page **PDF** for the print shop. PPTX so the author can hand-tweak in
  PowerPoint/Keynote before printing.
- **Size (CONFIRMED):** **48 in wide × 36 in tall, landscape.** Keep the build **parametric** on a single
  `(W_IN, H_IN)` anyway, so a late board-size surprise is one edit.
- **Framing (CONFIRMED): applied / platform-governance forward.** Lead the eye with the governance failure
  ("protected but unstanding" — compliance ≠ standing) and the actionable remedy (**function-not-firm**:
  aim exit at contingent gates, voice at necessary ones). The philosophical construct and the theory
  neighbors are *support*, compressed to a thin strip — present but not the headline. The **decision-tree
  diagnostic** and the **portfolio-bar** are the two images that must land first.
- **Maturity framing — do not overclaim.** This is a **construct + a formal diagnostic tested on
  coordination models + a *proposed* measurement instrument.** The formal receipts (§2) are computed on
  Boolean/IIT coordination models, **not on firms or workers**; label them that way on the poster. The
  survey instrument is *candidate items*, not a validated scale. Pitch: "a framework and a diagnostic that
  earns its keep," never "we measured platform workers." **Never demote the Φ/IIT apparatus** — its value is
  the principled exploration of irreducibility, not beating a cheap test.
- **Register:** scholarly, business-ethics audience; balanced but contribution-forward (lead the eye to the
  BE payoff). First person is fine in a byline sense; the poster voice is impersonal-active.

---

## 2. The argument, poster-condensed (content source of truth)

**Thesis (one line).** *Coordinative sovereignty is the standing to shape, contest, and share in the
governance of an algorithmic mediation you cannot exit — the autonomy proper to being irreducibly
coordinated.* (`chapter/chapter.md` §6)

**The move, in five beats:**
1. **The condition.** Most coordination now runs through platforms that stand between the parties and set
   non-negotiated terms — an *interested* third party that reads both sides and commits outcomes neither
   side controls. (`coordinative_sovereignty.md` "The condition")
2. **Why "get independent back" fails.** The mediator often does integrating work the parties cannot
   reproduce by dealing directly. Removing it does not restore an unmediated world — it dissolves the
   coordination. Demanding independence from a mediator you cannot do without spends effort on the one option
   you cannot have. (ibid. "Why preserving the old autonomy fails")
3. **The diagnostic.** Hirschman's **exit vs voice**, made decidable. Model the arrangement as
   **worker–mediator–counterpart**; run the **bypass counterfactual (q213)** — restore the direct tie the
   mediation forbids and recompute. If the mediator still binds → **necessary → only voice is available**.
   If the arrangement dissolves without it → **contingent → exit is available.** (`chapter/chapter.md` §5.2;
   `coordinative_sovereignty.md` "The connection to the lab")
4. **Coordinative ≠ digital sovereignty.** Digital sovereignty asks *who controls the infrastructure*
   (territorial/proprietary command). Coordinative sovereignty asks *what standing the actor coordinating
   through it holds.* The two **vary independently** — a firm can hold high digital and low coordinative
   sovereignty at once. (`worked_cases.md` H15)
5. **The payoff for business ethics.** It names a harm compliance misses — **"protected but unstanding"**: a
   firm or worker can satisfy GDPR / DMA / AI Act and remain strategically captured. It reframes platform
   governance from *transparency* to *standing*, and gives stakeholder theory a **function-level** diagnostic
   (disaggregate a platform into necessary vs contingent functions; aim **exit at the contingent gates,
   voice at the necessary ones**).

**Formal receipts (label: "on formal coordination models — not firms").** (`instruments/formal_standing.md`)
- The single mediator is the **pivotal / veto player in 115 of 115** sampled coordination forms.
- **Shapley share ≈ two-thirds** on the read-recipient triad; **≈ one-half** on structured mediated triads.
- Operationalization: **standing = Shapley pivotality; security = core membership.**

**Proposed voice instrument (label: "proposed, not yet validated").**
(`instruments/coordinative_sovereignty_instrument.md`) — **18 candidate 7-pt Likert items**, scoped to a
*named unexitable mediator*, across three dimensions: **non-domination · effective voice · governance share**
(+ a dependence screen). Discriminant target: psychological empowerment (Spreitzer, 1995).

**Theory neighbors (one-line differentiators).** (`literature/deep_research_report.md`)
- **Pettit — non-domination:** supplies "freedom from arbitrary power," but *protects*; does not *include*.
- **Nedelsky — relational autonomy:** autonomy is constituted through relationships, but is silent on *which*
  mediations are unexitable.
- **Markell — involvement:** adds a *share* in governance beyond insulation.
- **Ostrom — commons self-governance:** the precedent — but the platform is *enclosed/owned*, so this is
  Ostrom-via-enclosure, not a free pasture.
- **Hirschman — exit/voice:** the hinge; necessity is exactly where voice is structurally weakest
  ("lazy monopoly").

**Anticipated objection (put a small box on the poster).** *"Isn't the bypass test just make-or-buy /
brokerage substitutability relabeled?"* → The contribution is a **function-level, rule-based, remedy-linked**
classification tied to *standing* — distinct from structural holes, make-vs-buy, and essential-facilities
doctrine. The open test that would prove the apparatus adds value: a **borderline case where the naive
substitutability counterfactual and the Φ/IIT measure diverge** (author-only / open). (`reviews/08_reviewer2.md`,
`reviews/SYNTHESIS.md`)

**Four worked cases (setup → verdict).** (`chapter/chapter.md` §5.4; `worked_cases.md`)
| Platform actor | Necessary function → **voice** | Contingent gate → **exit** |
|---|---|---|
| **Gig / ride-hail driver** | real-time rider–driver matching | the rider–driver relationship gate (bypassable) |
| **App developer** | distribution + app review | in-app-payment gate → sideloading/interop (Apple fined €500M, Apr 2025) |
| **Marketplace seller** | fulfillment (necessary); demand-match (partial) | placement / Buy-Box toll; resale is reducible |
| **Citizen in a feed** | engagement-tuned recommendation → contestability | *(least developed — flag as open)* |

**The 2×2 (real firms, ready to lift — `worked_cases.md` H15):**
| | **high digital sovereignty** | **low digital sovereignty** |
|---|---|---|
| **high coordinative** | firm on its own stack (enterprise B2B) | platform workers under EU Dir. 2024/2831; CoopCycle courier-members |
| **low coordinative** | **App Store developer; Amazon Marketplace seller** ← *"protected but unstanding"* | solo gig courier |

---

## 3. Information architecture (reading order, zones, word budgets)

Balanced-but-contribution-forward flow, left→right, with the **diagnostic diagram as the visual anchor** in
the center. Nine content zones under a title band, over a footer.

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│  TITLE BAND (full width): title · subtitle/thesis · author/affiliation                     │
├───────────────────┬───────────────────┬───────────────────┬────────────────────────────────┤
│ COL 1  THE PROBLEM│ COL 2 THE CONSTRUCT│ COL 3 THE DIAGNOSTIC│ COL 4 CASES + CONTRIBUTION    │
│                   │                    │  (visual anchor)    │                               │
│ 1 The condition   │ 3 What it is (def) │ ▣ Mediated-triad dia│ 7 Four platforms decomposed   │
│   (platform bind) │                    │                     │   (cases table + portfolio bar)│
│                   │ ▣ 2×2 digital ×    │ 5 The test:         │                               │
│ 2 Why "independ-  │   coordinative     │   necessary vs      │ 8 For business ethics         │
│   ence" fails     │   (firms in cells) │   contingent        │   (protected-but-unstanding;  │
│   (exit goes empty│                    │ ▣ Decision-tree dia │   stakeholder dx; worker voice)│
│   → only voice)   │ 4 Not digital      │                     │                               │
│                   │   sovereignty      │ 6 Receipts (on      │ 9 Status, limits & next       │
│  ▸ neighbors strip│   (one-liner)      │   models) + objection│   (+ anticipated objection box)│
├───────────────────┴───────────────────┴───────────────────┴────────────────────────────────┤
│  FOOTER (full width): key references · contact/email · QR to paper · funding/logos          │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

**Word budgets (hard caps — posters die of text):** each numbered zone ≤ **70 words** of body + a ≤ 10-word
heading. Title ≤ 12 words. Thesis line ≤ 28 words. Diagram captions ≤ 20 words. Total body target **≈ 650
words** across the whole poster. If a zone runs over, cut — do not shrink the type below the §5 minimums.

---

## 4. Ready-to-place copy

**TITLE (applied-forward — primary confirmed):**
- **Protected but Unstanding: Coordinative Sovereignty and the Limits of Platform Compliance**
- *alt:* Coordinative Sovereignty: Standing Inside the Platforms You Cannot Leave
- *alt:* Beyond Compliance — Standing, Not Just Transparency, in Platform Governance

**SUBTITLE / THESIS (one line under title):**
"The standing to shape, contest, and share in the governance of an algorithmic mediation you cannot exit —
the autonomy proper to being irreducibly coordinated."

**AUTHOR / AFFILIATION:** Roger Hunt · Bentley University · rhunt@bentley.edu *(CONFIRM co-authors,
department, and whether to add a lab/project name — §10)*

**Zone 1 · The condition.** Most coordination now runs through platforms — a worker reaches riders through
an app, a seller reaches buyers through a marketplace, a developer reaches users through a store. The
platform stands between the parties and sets terms no one negotiated: it can rank, gate, price, and suspend.
It is an *interested* third party that reads both sides and commits outcomes neither side controls.

**Zone 2 · Why "independence" fails.** The reflex is to want the old autonomy back — to deal directly, to
not be mediated. But the mediator often does integrating work the parties cannot reproduce alone. Remove it
and you do not get an unmediated world; you dissolve the coordination. Where a mediator is *necessary*,
independence is not on the menu — and the only remaining power is **voice**.

**Neighbors strip (Zone 2 footer, one line, small):** Builds on Pettit (non-domination), Nedelsky
(relational autonomy), Markell (involvement), Ostrom (commons self-governance), Hirschman (exit/voice) —
and departs from each: it makes *which mediations are unexitable* the decidable question.

**Zone 3 · What coordinative sovereignty is.** Not independence from the mediator, nor command of the
infrastructure. It is **standing within** the coordination: the power to shape the terms on which one is
mediated, to contest the mediator's arbitrary power, and to hold a share in governing the arrangement one
cannot leave. Its currency is **voice made effective** — terms that hold because coordinated actors have the
standing to make them hold.

**Zone 4 · Not digital sovereignty.** Digital sovereignty asks *who owns the infrastructure* and answers by
centralizing control (a wall, a fork, a domestic cloud). It gives the *state* an exit and does little for the
seller or driver still mediated inside whatever wins. The two sovereignties **vary independently.** *(caption
for the 2×2.)*

**Zone 5 · The test: necessary vs contingent.** Model the arrangement as **worker–mediator–counterpart.**
Run the **bypass counterfactual:** restore the direct tie the mediation forbids and recompute.
**Still binds → necessary → aim voice.** **Dissolves → contingent → aim exit.** Exit maps to bypassability;
voice to necessity. The test says *which sovereignty is even available.*

**Zone 6 · Receipts (on formal coordination models — not firms).**
- Single mediator is the **pivotal/veto player in 115 / 115** sampled forms.
- **Shapley share ≈ ⅔** (read-recipient triad) · **≈ ½** (structured triad).
- **Standing = Shapley pivotality · security = core membership.**
*(Small print: computed on Boolean/IIT coordination games; the apparatus explores irreducibility — it does
not claim to beat a cheap substitutability check, and the borderline divergence case is open.)*

**Zone 7 · Four platforms, decomposed.** *(the cases table from §2 + the portfolio bar diagram.)* Dependence
is not monolithic. Split a platform into **functions**, classify each, and aim remedies **function-not-firm**:
exit at the contingent gates, voice at the necessary ones.

**Zone 8 · For business ethics.**
- **A harm compliance misses:** "**protected but unstanding**" — an App Store developer or Amazon seller can
  own its code and data, satisfy GDPR/DMA, and still be unable to contest the algorithm that ranks it.
- **Platform governance:** shift the target from *transparency* to *standing/contestability.*
- **Worker voice:** grounds EU Platform Work Directive **2024/2831** as coordinative sovereignty, and says
  when co-ops, bargaining, and data trusts actually *raise* standing.

**Zone 9 · Status, limits & next.** A construct, a diagnostic validated on coordination **models**, and a
**proposed** 18-item voice instrument (non-domination · effective voice · governance share) awaiting
validation against psychological empowerment. Next: field the instrument; find the borderline case that
separates the causal test from mere substitutability.

**Anticipated-objection box (inside Zone 9 or floating near Zone 6).**
*"Isn't the bypass test just make-or-buy substitutability relabeled?"* — No: the contribution is a
**function-level, rule-based, remedy-linked** classification tied to *standing*, distinct from structural
holes and essential-facilities doctrine. Proving the causal apparatus adds value is the open next step.

**FOOTER.** Selected references: Hirschman 1970; Pettit 1997; Nedelsky 2011; Markell 2003; Ostrom 1990;
Spreitzer 1995; EU Dir. 2024/2831. · Full paper + formal appendix: **[QR code]** · Contact:
rhunt@bentley.edu

---

## 5. Visual design system

**Canvas & grid (48×36 landscape; all in inches).** Parameterize as `W_IN, H_IN = 48, 36`.
- Outer margin: **1.0**. Title band: y `0→5.0` (height 5.0). Footer: y `34.0→36.0` (height 2.0). Content
  band: y `5.4 → 33.6` (height ≈ 28.2).
- **Four columns**, gutter **0.6**: column width `= (W_IN - 2*1.0 - 3*0.6) / 4 = 11.05`.
  - Col x-lefts: **1.00 · 12.65 · 24.30 · 35.95** (each width **11.05**, Col 4 right edge = 47.0).
- Within a column, stack zone cards top→down with **0.4** vertical gap. Give each card an internal pad of
  **0.35**. Panel headings sit in a tinted band at the card top.
- The **decision-tree** and **mediated-triad** diagrams live in Col 3; the **2×2** in Col 2; the **portfolio
  bar** in Col 4 (Zone 7). Let Col 3 run visually "taller/denser" — it is the anchor.

**Palette (hex).** High-contrast, prints well, business-ethics-serious:
| Role | Hex | Use |
|---|---|---|
| Ink | `#16202E` | body text, rules |
| Title band | `#0E2A3F` | dark band behind title (white text on it) |
| Necessary / Voice (primary) | `#1D6A96` | necessary-mediator branch, voice, headings accents |
| Contingent / Exit (secondary) | `#C0692B` | contingent branch, exit, callouts |
| Paper | `#FCFBF8` | slide background |
| Panel tint | `#EDF1F4` | card heading bands / panel fills |
| Warm panel tint | `#F3EFE7` | alternate card fill (cases/contribution side) |
| Hairline | `#C9D2D9` | dividers, borders |
| Muted | `#5A6B7B` | small print, captions |
**Semantic rule:** blue = necessary/voice everywhere; amber = contingent/exit everywhere. Keep it consistent
across all four diagrams so a reader learns the code once.

**Typography.** Prefer **Inter** or **Source Sans 3** (headings) + **Source Serif 4** or **Georgia** (body);
**fall back to Arial / Georgia** if the print machine lacks them. **Embed fonts in the PPTX** (see §7).
Type scale for 48×36 (poster legibility: title readable ~15 ft, body ~5 ft — never below 24 pt body):
| Element | Size (pt) | Weight |
|---|---|---|
| Poster title | 80 | Bold |
| Subtitle / thesis | 38 | Regular/italic |
| Author line | 28 | Medium |
| Panel heading | 34 | Bold |
| Body | 25 | Regular |
| Big-number callout (115/115, ⅔) | 66 | Bold |
| Caption / neighbors strip | 19 | Regular |
| Footer / refs | 18 | Regular |
Line spacing 1.15–1.2; measure ≤ ~50 characters per column line. Left-align everything; no justification.

---

## 6. Diagram specs (build as native PPTX shapes — vector, editable)

**Diagram A — The mediated triad (Col 3, top).** Three nodes: **Worker** (lower-left), **Counterpart**
(lower-right), **Mediator** (top-center, larger, filled `#1D6A96`, white label "interested third party —
reads both sides, commits outcomes"). Solid arrows Worker↔Mediator and Mediator↔Counterpart. A **dashed,
greyed** Worker⋯Counterpart edge labeled "direct tie the platform forbids." Caption: "The bypass test
restores the dashed edge and asks what breaks."

**Diagram B — The 2×2 (Col 2).** Axes: X = *Digital sovereignty* (control of infrastructure) low→high;
Y = *Coordinative sovereignty* (standing of the actor) low→high. Fill the four cells from the H15 table:
- high-coord / high-digital: "firm on own stack (enterprise B2B)"
- high-coord / low-digital: "EU Dir. 2024/2831 workers; CoopCycle members"
- **low-coord / high-digital: "App Store developer; Amazon seller" — badge it "protected but unstanding"** (this
  is the money cell; outline it in `#C0692B`).
- low-coord / low-digital: "solo gig courier"
Caption: "The two sovereignties vary independently."

**Diagram C — The decision-tree diagnostic (Col 3, center — the anchor).** Flow, top→down:
`Coordination through a mediator?` → `Run the bypass counterfactual` →
branch **left (blue) "Still binds → NECESSARY"** → `Only VOICE: contest terms · share governance` ;
branch **right (amber) "Dissolves → CONTINGENT"** → `EXIT available: interop · sideload · deregulate` ;
small middle branch **"Partial → mixed remedy."** Use the blue/amber semantic code. This is the poster's
takeaway image — make it the largest, cleanest element.

**Diagram D — The portfolio bar (Col 4, Zone 7).** One horizontal stacked bar = one platform (label it, e.g.
"App Store" or "a marketplace") segmented by function, each segment colored by verdict:
`Distribution (blue/necessary) · Review (blue) · Payment (amber/contingent) · Placement/Buy-Box (amber) ·
Resale (grey/reducible)`. Legend ties color→remedy: **blue → voice, amber → exit, grey → drop.** Caption:
"Aim exit at the amber, voice at the blue — function, not firm."

Keep all four diagrams on the same color grammar and the same stroke weights (2 pt lines, `#16202E`).

---

## 7. Build approach — `python-pptx`

**Environment.** `pip install python-pptx`. (For PDF export, prefer LibreOffice headless — see below — or
open in PowerPoint and Save-As-PDF.)

**Skeleton (fill in with the §4 copy, §5 coordinates, §6 diagrams):**
```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

W_IN, H_IN = 48, 36                      # <- single parametric size control
INK   = RGBColor(0x16,0x20,0x2E); BAND = RGBColor(0x0E,0x2A,0x3F)
VOICE = RGBColor(0x1D,0x6A,0x96); EXIT = RGBColor(0xC0,0x69,0x2B)
PAPER = RGBColor(0xFC,0xFB,0xF8); TINT = RGBColor(0xED,0xF1,0xF4)
WARM  = RGBColor(0xF3,0xEF,0xE7); HAIR = RGBColor(0xC9,0xD2,0xD9)
MUTED = RGBColor(0x5A,0x6B,0x7B); WHITE= RGBColor(0xFF,0xFF,0xFF)

prs = Presentation()
prs.slide_width  = Inches(W_IN)
prs.slide_height = Inches(H_IN)
slide = prs.slides.add_slide(prs.slide_layouts[6])   # blank

def rect(x,y,w,h, fill=None, line=None, line_w=1.0):
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x),Inches(y),Inches(w),Inches(h))
    sp.fill.solid(); sp.fill.fore_color.rgb = fill if fill else PAPER
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb = line; sp.line.width = Pt(line_w)
    sp.shadow.inherit = False
    return sp

def text(x,y,w,h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    # runs: list of (string, size_pt, bold, color)
    tb = slide.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h)); tf = tb.text_frame
    tf.word_wrap = True; tf.vertical_anchor = anchor
    for i,(s,sz,b,c) in enumerate(runs):
        p = tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment = align; r = p.add_run(); r.text = s
        r.font.size = Pt(sz); r.font.bold = b; r.font.color.rgb = c
        r.font.name = "Inter"     # fallback Arial/Georgia; embed at the end
    return tb

# 1) paper background
rect(0,0,W_IN,H_IN, fill=PAPER)
# 2) title band  (dark, white text)
rect(0,0,W_IN,5.0, fill=BAND)
text(1.0,0.5,W_IN-2,3.0, [("Coordinative Sovereignty: Standing Inside the Platforms You Cannot Leave",80,True,WHITE)])
text(1.0,3.4,W_IN-2,1.2, [("The standing to shape, contest, and share in governing an algorithmic mediation you cannot exit.",38,False,TINT)])
# 3) columns/zones: use the x-lefts 1.00 / 12.65 / 24.30 / 35.95, width 11.05  (see §5)
# ... build each zone card with rect()+text(); build diagrams A–D with add_shape/connectors ...
# 4) footer band, refs, QR placeholder
prs.save("poster/coordinative_sovereignty_poster.pptx")
```
**Diagram tips.** Nodes = `MSO_SHAPE.OVAL`/`ROUNDED_RECTANGLE`; branches = `add_connector(MSO_CONNECTOR.STRAIGHT, …)`;
dashed edge via the connector's `line` XML (`<a:prstDash val="dash"/>`). The 2×2 and portfolio bar are just
`rect()` grids with labels. Keep diagrams as real shapes (not images) so the author can edit them.
**QR:** generate with `qrcode[pil]` to a PNG (target: the paper's URL/DOI — placeholder OK) and
`add_picture` into the footer; or leave a labeled box for the author to drop one in.
**Font embedding:** python-pptx cannot embed fonts directly. Either (a) stick to **Arial/Georgia** (already
on every machine) and skip embedding, or (b) after building, open once in PowerPoint → *Save As* with
"Embed fonts in the file" ticked. Recommend (a) for the print shop unless Inter is confirmed installed.
**PDF export (single page):**
`soffice --headless --convert-to pdf --outdir poster poster/coordinative_sovereignty_poster.pptx`
(LibreOffice). Verify the PDF is one page at exactly 48×36 in.

---

## 8. Build task list (for the executing session)

1. `pip install python-pptx qrcode[pil]`; confirm `soffice` (LibreOffice) is available for PDF export.
2. Read the source files in §11 and lift the exact numbers/tables (do **not** paraphrase the receipts or the
   H15 cells).
3. Write `poster/build_poster.py` from the §7 skeleton: set `W_IN,H_IN`; lay the title band, four columns,
   nine zone cards (§3 map, §5 coordinates), and the footer using the §4 copy under the §5 type scale.
4. Build diagrams **A–D** (§6) as native shapes, on the shared blue/amber color grammar.
5. Enforce the §3 **word caps** — if a zone overflows its card, cut copy, never shrink below 24 pt body.
6. `python poster/build_poster.py` → `coordinative_sovereignty_poster.pptx`.
7. Export PDF via LibreOffice; open it and run the §9 checklist.
8. Save both files under `poster/`. Report: final size, any copy trimmed, and the §10 items still needing the
   author's decision. Do **not** commit to git unless asked (this is the author's working artifact).

---

## 9. QA & print checklist

- [ ] **One page**, exact **48×36 in** (or the confirmed size); no content in the outer 0.75 in (print bleed/frame).
- [ ] **Legibility:** body ≥ 24 pt; title readable across a room; ≤ ~50 chars per line.
- [ ] **Reading order** flows title → Col 1→4; the decision tree reads as the takeaway at a glance.
- [ ] **Color code consistent:** blue = necessary/voice, amber = contingent/exit, in *all* diagrams; check
      contrast (amber text on paper can be weak — use amber for fills/rules, ink for text).
- [ ] **Numbers exact & scoped:** "115/115," "≈⅔," "≈½" present and labeled **"on formal coordination models
      — not firms."** Instrument labeled **"proposed."**
- [ ] **Guards:** no claim that workers/firms were measured; Φ/IIT not demoted; "protected but unstanding" and
      the function-not-firm remedy are visible.
- [ ] **Attribution:** author/affiliation/email correct; QR resolves (or box labeled for the author).
- [ ] **Proof at 25%:** print an 8.5×11 scaled proof; if it reads at that size, it reads at full size.
- [ ] Fonts embedded **or** limited to Arial/Georgia so the print shop doesn't substitute.

---

## 10. Open decisions — confirm before printing

1. **Poster size / orientation.** ✅ **Confirmed 48×36 landscape.** (Still verify the venue board can hold it;
   the build stays parametric if a portrait board forces 36×48.)
2. **Authorship & affiliation.** Confirm co-authors, department/school, and whether to add a project/lab name
   or institutional logo (SBE posters usually carry the home-institution logo in the footer).
3. **QR target & handout.** Decide the QR destination (working-paper URL, SSRN/DOI, or a project page) and
   whether to bring a 1-page handout of the four cases + the instrument.

Minor: citation style for the footer refs (author-date is fine); whether to include the anticipated-objection
box (recommended — it pre-empts the reviewer-2 question at the board).

---

## 11. Source files to quote exactly (repo-relative)

- `org_frontier/coordinative_sovereignty/coordinative_sovereignty.md` — the construct, the condition, the
  digital-sovereignty contrast.
- `org_frontier/coordinative_sovereignty/chapter/chapter.md` — §5.2 (the test), §5.4 (worked cases), §6
  (thesis), §8 (H15/H17 folded in).
- `org_frontier/coordinative_sovereignty/research/worked_cases.md` — the **H15 2×2 table** (lift verbatim) and
  the case verdicts.
- `org_frontier/coordinative_sovereignty/instruments/formal_standing.md` — the receipts (115/115, Shapley ⅔/½,
  standing=Shapley, security=core).
- `org_frontier/coordinative_sovereignty/instruments/coordinative_sovereignty_instrument.md` — the 18-item
  proposed scale and its three dimensions.
- `org_frontier/coordinative_sovereignty/literature/deep_research_report.md` — Pettit/Nedelsky/Markell/Ostrom/
  Hirschman positioning and the digital-sovereignty differentiator.
- `org_frontier/coordinative_sovereignty/reviews/08_reviewer2.md`, `reviews/SYNTHESIS.md` — the sharpest
  objection and the agreed response (for the objection box).
