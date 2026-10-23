#!/usr/bin/env python3
"""Build the Coordinative Sovereignty poster (SBE) — single-slide PPTX, 48x36 landscape.

Applied / platform-governance-forward framing. Native shapes only (editable). See POSTER_PLAN.md.
    python3 build_poster.py   ->   coordinative_sovereignty_poster.pptx
Export PDF in PowerPoint/Keynote (Save As PDF) or: soffice --headless --convert-to pdf <file>
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- size (single parametric control) --------------------------------------
W_IN, H_IN = 48, 36

# ---- palette ---------------------------------------------------------------
INK   = RGBColor(0x16,0x20,0x2E); BAND = RGBColor(0x0E,0x2A,0x3F)
VOICE = RGBColor(0x1D,0x6A,0x96); EXIT = RGBColor(0xC0,0x69,0x2B)
PAPER = RGBColor(0xFC,0xFB,0xF8); TINT = RGBColor(0xED,0xF1,0xF4)
WARM  = RGBColor(0xF3,0xEF,0xE7); HAIR = RGBColor(0xC9,0xD2,0xD9)
MUTED = RGBColor(0x5A,0x6B,0x7B); WHITE= RGBColor(0xFF,0xFF,0xFF)
GREY  = RGBColor(0xB6,0xBE,0xC6)

HEAD_FONT = "Arial"      # print-shop-safe; swap to Inter/Source Sans if embedding
BODY_FONT = "Georgia"

prs = Presentation()
prs.slide_width  = Inches(W_IN)
prs.slide_height = Inches(H_IN)
slide = prs.slides.add_slide(prs.slide_layouts[6])   # blank


# ---- helpers ---------------------------------------------------------------
def rect(x, y, w, h, fill=None, line=None, line_w=1.0, shape=MSO_SHAPE.RECTANGLE):
    sp = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(line_w)
    sp.shadow.inherit = False
    return sp


def text(x, y, w, h, paras, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font=BODY_FONT,
         space_after=4, line_spacing=1.12):
    """paras: list of paragraphs; each paragraph is a list of runs (str, size, bold, color)."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Pt(2); tf.margin_top = tf.margin_bottom = Pt(2)
    for i, runs in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space_after); p.line_spacing = line_spacing
        for (s, sz, b, c) in runs:
            r = p.add_run(); r.text = s
            r.font.size = Pt(sz); r.font.bold = b; r.font.color.rgb = c; r.font.name = font
    return tb


def card(x, y, w, h, heading, fill=TINT):
    """A panel with a colored heading band and a body area; returns the inner body box (x,y,w,h)."""
    rect(x, y, w, h, fill=PAPER, line=HAIR, line_w=1.25)
    rect(x, y, w, 1.15, fill=fill)
    text(x + 0.3, y + 0.12, w - 0.6, 0.95, [[(heading, 28, True, BAND)]], font=HEAD_FONT,
         anchor=MSO_ANCHOR.MIDDLE)
    return (x + 0.35, y + 1.35, w - 0.7, h - 1.6)


def dash(connector):
    ln = connector.line._get_or_add_ln()
    d = ln.makeelement(qn('a:prstDash'), {'val': 'dash'}); ln.append(d)


def connect(x1, y1, x2, y2, color=INK, w=2.0, dashed=False, arrow=True):
    cn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1),
                                    Inches(x2), Inches(y2))
    cn.line.color.rgb = color; cn.line.width = Pt(w)
    if dashed: dash(cn)
    if arrow:
        ln = cn.line._get_or_add_ln()
        end = ln.makeelement(qn('a:tailEnd'), {'type': 'triangle', 'w': 'med', 'len': 'med'})
        ln.append(end)
    cn.shadow.inherit = False
    return cn


# ---- layout constants ------------------------------------------------------
M = 1.0
COL_W = 11.05
COLX = [1.00, 12.65, 24.30, 35.95]
CONTENT_TOP = 5.4
CONTENT_BOT = 33.6


# ---- background + title band ----------------------------------------------
rect(0, 0, W_IN, H_IN, fill=PAPER)
rect(0, 0, W_IN, 5.0, fill=BAND)
text(M, 0.45, W_IN - 2*M, 2.6,
     [[("Protected but Unstanding: Coordinative Sovereignty and the Limits of Platform Compliance",
        70, True, WHITE)]], font=HEAD_FONT, anchor=MSO_ANCHOR.TOP)
text(M, 3.30, W_IN - 2*M - 11, 1.3,
     [[("The standing to shape, contest, and share in governing an algorithmic mediation you cannot exit "
        "— the autonomy proper to being irreducibly coordinated.", 33, False, TINT)]],
     font=BODY_FONT)
text(W_IN - M - 11, 3.35, 11, 1.3,
     [[("Roger Hunt", 27, True, WHITE)],
      [("Bentley University · rhunt@bentley.edu", 22, False, TINT)]],
     font=HEAD_FONT, align=PP_ALIGN.RIGHT)


# ===========================================================================
# COLUMN 1 — THE PROBLEM (platform governance failure)
# ===========================================================================
x = COLX[0]
bx, by, bw, bh = card(x, CONTENT_TOP, COL_W, 7.6, "1 · The condition")
text(bx, by, bw, bh, [
    [("Most coordination now runs through platforms. A driver reaches riders through an app, a seller "
      "reaches buyers through a marketplace, a developer reaches users through a store.", 25, False, INK)],
    [("The platform stands between the parties and sets terms no one negotiated — it can rank, gate, "
      "price, and suspend. It is an ", 25, False, INK),
     ("interested", 25, True, EXIT),
     (" third party that reads both sides and commits outcomes neither controls.", 25, False, INK)],
])

bx, by, bw, bh = card(x, CONTENT_TOP + 8.1, COL_W, 8.7, "2 · Compliance is not standing")
text(bx, by, bw, bh, [
    [("The reflex is to want the old autonomy back — to deal directly, unmediated. But the mediator "
      "often does integrating work the parties cannot reproduce alone. Remove it and you do not get an "
      "unmediated world; you dissolve the coordination.", 25, False, INK)],
    [("So a firm can satisfy GDPR, the DMA, and the AI Act and remain strategically captured: ", 25, False, INK),
     ("protected but unstanding.", 25, True, EXIT)],
    [("Transparency shows a developer how it is ranked; it still cannot contest the algorithm that ranks "
      "it. The missing thing is not disclosure. It is ", 25, False, INK),
     ("standing.", 25, True, VOICE)],
])

# neighbors strip (thin, support)
bx, by, bw, bh = card(x, CONTENT_TOP + 17.3, COL_W, 4.2, "Where it stands in theory", fill=WARM)
text(bx, by, bw, bh, [
    [("Builds on Pettit (non-domination), Nedelsky (relational autonomy), Markell (involvement), Ostrom "
      "(commons self-governance), and Hirschman (exit / voice).", 22, False, INK)],
    [("It departs from each by making one question decidable: ", 22, False, INK),
     ("which mediations can actually be exited.", 22, True, BAND)],
])


# ===========================================================================
# COLUMN 2 — THE CONSTRUCT + the 2x2
# ===========================================================================
x = COLX[1]
bx, by, bw, bh = card(x, CONTENT_TOP, COL_W, 7.4, "3 · What coordinative sovereignty is")
text(bx, by, bw, bh, [
    [("Not independence from the mediator, nor command of the infrastructure. It is ", 25, False, INK),
     ("standing within", 25, True, VOICE),
     (" the coordination:", 25, False, INK)],
    [("the power to shape the terms on which one is mediated, to contest the mediator’s arbitrary "
      "power, and to hold a share in governing the arrangement one cannot leave.", 25, False, INK)],
    [("Its currency is ", 25, False, INK), ("voice made effective", 25, True, VOICE),
     (" — terms that hold because coordinated actors have the standing to make them hold.", 25, False, INK)],
])

# ---- Diagram B: the 2x2 -----------------------------------------------------
gy = CONTENT_TOP + 7.9
bx, by, bw, bh = card(x, gy, COL_W, 10.6, "4 · Not digital sovereignty")
text(bx, by, bw, 1.5, [
    [("Digital sovereignty asks who ", 22, False, INK), ("owns the infrastructure", 22, True, INK),
     ("; coordinative sovereignty asks what ", 22, False, INK),
     ("standing", 22, True, VOICE), (" the actor holds. They vary independently.", 22, False, INK)]])
# 2x2 grid
gx, gyy = bx + 1.7, by + 2.0
cw, ch = (bw - 1.7) / 2, 2.85
cells = [
    (0, 0, "Firm on its own stack\n(enterprise B2B)", TINT, None),
    (1, 0, "EU Dir. 2024/2831 workers;\nCoopCycle courier-members", TINT, None),
    (0, 1, "App Store developer;\nAmazon Marketplace seller", WARM, EXIT),   # money cell
    (1, 1, "Solo gig courier", TINT, None),
]
for cxi, cyi, label, fill, outline in cells:
    cxp = gx + cxi * cw; cyp = gyy + cyi * ch
    rect(cxp, cyp, cw - 0.12, ch - 0.12, fill=fill, line=(outline or HAIR),
         line_w=(3.0 if outline else 1.0))
    text(cxp + 0.15, cyp + 0.15, cw - 0.4, ch - 0.4,
         [[(label, 19, bool(outline), (EXIT if outline else INK))]], font=HEAD_FONT,
         anchor=MSO_ANCHOR.MIDDLE)
# badge on money cell
rect(gx + 0.15, gyy + ch + 0.15, cw - 0.5, 0.7, fill=EXIT)
text(gx + 0.15, gyy + ch + 0.18, cw - 0.5, 0.64, [[("← “protected but unstanding”", 17, True, WHITE)]],
     font=HEAD_FONT, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
# axis labels
text(gx, gyy + 2*ch + 0.05, 2*cw, 0.5, [[("Digital sovereignty  →", 18, True, MUTED)]],
     font=HEAD_FONT, align=PP_ALIGN.CENTER)
tb = text(bx - 0.1, by + 2.0, 1.6, 2*ch, [[("Coordinative sovereignty  →", 18, True, MUTED)]],
          font=HEAD_FONT, anchor=MSO_ANCHOR.MIDDLE)
tb.rotation = 270

# neighbors / differentiator caption
bx, by, bw, bh = card(x, gy + 11.1, COL_W, 3.1, "The precedent, enclosed", fill=WARM)
text(bx, by, bw, bh, [
    [("Ostrom showed interdependent actors can govern a shared resource themselves. The platform is the "
      "shared resource — but ", 22, False, INK), ("owned and enclosed.", 22, True, EXIT),
     (" Coordinative sovereignty extends the precedent to a shared mediation.", 22, False, INK)]])


# ===========================================================================
# COLUMN 3 — THE DIAGNOSTIC (visual anchor)
# ===========================================================================
x = COLX[2]

# ---- Diagram A: mediated triad ---------------------------------------------
bx, by, bw, bh = card(x, CONTENT_TOP, COL_W, 6.4, "5 · The mediated triad")
mx = bx + bw/2
# mediator (top center)
rect(mx - 2.2, by + 0.1, 4.4, 1.5, fill=VOICE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(mx - 2.1, by + 0.15, 4.2, 1.4, [[("MEDIATOR", 20, True, WHITE)],
     [("reads both sides,\ncommits the outcome", 15, False, TINT)]], font=HEAD_FONT,
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, space_after=1, line_spacing=1.0)
# worker / counterpart
wy = by + 3.6
rect(bx + 0.1, wy, 3.6, 1.35, fill=TINT, line=HAIR, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(bx + 0.1, wy, 3.6, 1.35, [[("WORKER", 19, True, INK)]], font=HEAD_FONT, anchor=MSO_ANCHOR.MIDDLE,
     align=PP_ALIGN.CENTER)
rect(bx + bw - 3.7, wy, 3.6, 1.35, fill=TINT, line=HAIR, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(bx + bw - 3.7, wy, 3.6, 1.35, [[("COUNTERPART", 19, True, INK)]], font=HEAD_FONT,
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
# edges
connect(bx + 1.9, wy, mx - 1.2, by + 1.6, color=INK, w=2.5, arrow=False)
connect(bx + bw - 1.9, wy, mx + 1.2, by + 1.6, color=INK, w=2.5, arrow=False)
connect(bx + 3.7, wy + 0.67, bx + bw - 3.7, wy + 0.67, color=GREY, w=2.5, dashed=True, arrow=False)
text(bx + 3.7, wy + 0.75, bw - 7.4, 0.7, [[("direct tie the platform forbids", 15, False, MUTED)]],
     font=HEAD_FONT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)

# ---- Zone 5 text + Diagram C: decision tree --------------------------------
ty = CONTENT_TOP + 6.8
bx, by, bw, bh = card(x, ty, COL_W, 13.6, "The test: necessary vs contingent")
text(bx, by, bw, 2.4, [
    [("Run the ", 24, False, INK), ("bypass counterfactual", 24, True, INK),
     (": restore the forbidden direct tie and recompute. What happens to the coordination tells you which "
      "sovereignty is even available.", 24, False, INK)]])

# tree
tcx = bx + bw/2
# node 0
n0y = by + 2.7
rect(tcx - 3.4, n0y, 6.8, 1.2, fill=BAND, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(tcx - 3.4, n0y, 6.8, 1.2, [[("Restore the forbidden tie", 21, True, WHITE)]], font=HEAD_FONT,
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
# split
sply = n0y + 1.9
connect(tcx, n0y + 1.2, tcx, sply, color=INK, w=2.5, arrow=False)
lx = bx + bw*0.26; rx = bx + bw*0.74
connect(tcx, sply, lx, sply, color=INK, w=2.5, arrow=False)
connect(tcx, sply, rx, sply, color=INK, w=2.5, arrow=False)
connect(lx, sply, lx, sply + 0.5, color=VOICE, w=2.5)
connect(rx, sply, rx, sply + 0.5, color=EXIT, w=2.5)
# necessary (left, voice)
b1y = sply + 0.6
rect(lx - 2.5, b1y, 5.0, 1.5, fill=VOICE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(lx - 2.5, b1y, 5.0, 1.5, [[("Still binds", 18, False, TINT)], [("NECESSARY", 22, True, WHITE)]],
     font=HEAD_FONT, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, space_after=1, line_spacing=1.0)
connect(lx, b1y + 1.5, lx, b1y + 2.0, color=VOICE, w=2.5)
rect(lx - 2.6, b1y + 2.1, 5.2, 2.2, fill=PAPER, line=VOICE, line_w=2.5, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(lx - 2.45, b1y + 2.2, 4.9, 2.0, [[("Only VOICE", 20, True, VOICE)],
     [("contest the terms · share the governance", 17, False, INK)]], font=HEAD_FONT,
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, space_after=2, line_spacing=1.0)
# contingent (right, exit)
rect(rx - 2.5, b1y, 5.0, 1.5, fill=EXIT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(rx - 2.5, b1y, 5.0, 1.5, [[("Dissolves", 18, False, WARM)], [("CONTINGENT", 22, True, WHITE)]],
     font=HEAD_FONT, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, space_after=1, line_spacing=1.0)
connect(rx, b1y + 1.5, rx, b1y + 2.0, color=EXIT, w=2.5)
rect(rx - 2.6, b1y + 2.1, 5.2, 2.2, fill=PAPER, line=EXIT, line_w=2.5, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(rx - 2.45, b1y + 2.2, 4.9, 2.0, [[("EXIT available", 20, True, EXIT)],
     [("interoperate · sideload · deregulate", 17, False, INK)]], font=HEAD_FONT,
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, space_after=2, line_spacing=1.0)
# partial note
text(bx, b1y + 4.5, bw, 0.8, [[("Partial → mixed remedy. ", 18, True, MUTED),
     ("Exit maps to bypassability; voice, to necessity (Hirschman).", 18, False, MUTED)]],
     font=HEAD_FONT, align=PP_ALIGN.CENTER)

# ---- Zone 6: receipts + objection ------------------------------------------
ry = ty + 14.0
bx, by, bw, bh = card(x, ry, COL_W, 6.4, "6 · Receipts, on formal models", fill=WARM)
text(bx, by, 3.4, 2.2, [[("115", 60, True, VOICE)], [("of 115", 24, True, VOICE)]], font=HEAD_FONT,
     align=PP_ALIGN.CENTER, space_after=0, line_spacing=0.95)
text(bx + 3.5, by + 0.1, bw - 3.5, 2.2, [
    [("sampled coordination forms: the single mediator is the pivotal party — the veto player and "
      "Shapley-argmax.", 21, False, INK)]])
text(bx, by + 2.5, bw, 1.4, [
    [("Mediator’s Shapley share ≈ ", 21, False, INK), ("two-thirds", 21, True, VOICE),
     (" (read-recipient triad), a little over ", 21, False, INK), ("half", 21, True, VOICE),
     (" (structured triads). Standing = Shapley pivotality; security = core membership.", 21, False, INK)]])
text(bx, by + 4.0, bw, 1.2, [
    [("Computed on Boolean / integrated-information coordination games — not firms or workers. The "
      "apparatus explores irreducibility; the open next step is a case where the causal test and a cheap "
      "substitutability check diverge.", 16, False, MUTED)]])


# ===========================================================================
# COLUMN 4 — APPLIED PAYOFF
# ===========================================================================
x = COLX[3]

# ---- Zone 7: four platforms decomposed + portfolio bar ---------------------
bx, by, bw, bh = card(x, CONTENT_TOP, COL_W, 11.4, "7 · Four platforms, decomposed")
text(bx, by, bw, 1.5, [
    [("Dependence is not monolithic. Split a platform into ", 24, False, INK), ("functions", 24, True, INK),
     (", classify each, and aim remedies ", 24, False, INK), ("function, not firm.", 24, True, EXIT)]])
rows = [
    ("Gig / ride-hail driver", "real-time matching", "the rider–driver relationship gate"),
    ("App developer", "distribution + review", "in-app-payment gate (Apple fined €500M, 2025)"),
    ("Marketplace seller", "fulfillment; demand-match (partial)", "placement / Buy-Box toll; resale reducible"),
    ("Citizen in a feed", "engagement-tuned ranking", "(least developed — open)"),
]
ryy = by + 1.7
# header
text(bx, ryy, bw*0.30, 0.6, [[("Actor", 17, True, MUTED)]], font=HEAD_FONT)
text(bx + bw*0.30, ryy, bw*0.36, 0.6, [[("Necessary → VOICE", 17, True, VOICE)]], font=HEAD_FONT)
text(bx + bw*0.66, ryy, bw*0.34, 0.6, [[("Contingent → EXIT", 17, True, EXIT)]], font=HEAD_FONT)
ryy += 0.7
for actor, nec, con in rows:
    rect(bx, ryy, bw, 1.5, fill=None, line=HAIR, line_w=0.75)
    text(bx + 0.1, ryy + 0.1, bw*0.30 - 0.1, 1.3, [[(actor, 18, True, INK)]], font=HEAD_FONT,
         anchor=MSO_ANCHOR.MIDDLE)
    text(bx + bw*0.30 + 0.1, ryy + 0.1, bw*0.36 - 0.15, 1.3, [[(nec, 17, False, VOICE)]],
         anchor=MSO_ANCHOR.MIDDLE)
    text(bx + bw*0.66 + 0.1, ryy + 0.1, bw*0.34 - 0.15, 1.3, [[(con, 17, False, EXIT)]],
         anchor=MSO_ANCHOR.MIDDLE)
    ryy += 1.5

# ---- Diagram D: portfolio bar ----------------------------------------------
pby = ryy + 0.35
text(bx, pby, bw, 0.5, [[("One platform, one bar (App Store):", 18, True, INK)]], font=HEAD_FONT)
segs = [("Distribution", 0.24, VOICE), ("Review", 0.16, VOICE), ("Payment", 0.24, EXIT),
        ("Buy-Box", 0.22, EXIT), ("Resale", 0.14, GREY)]
sx = bx; sw_total = bw
pbar_y = pby + 0.6
for name, frac, col in segs:
    w = sw_total * frac
    rect(sx, pbar_y, w - 0.05, 1.1, fill=col)
    text(sx, pbar_y + 0.05, w - 0.05, 1.0, [[(name, 14, True, WHITE)]], font=HEAD_FONT,
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    sx += w
text(bx, pbar_y + 1.2, bw, 0.6, [[("■ voice ", 16, True, VOICE), ("(necessary)   ", 16, False, MUTED),
     ("■ exit ", 16, True, EXIT), ("(contingent)   ", 16, False, MUTED),
     ("■ drop ", 16, True, GREY), ("(reducible)", 16, False, MUTED)]], font=HEAD_FONT)

# ---- Zone 8: for business ethics -------------------------------------------
bx, by, bw, bh = card(x, CONTENT_TOP + 11.9, COL_W, 7.8, "8 · For business ethics", fill=WARM)
text(bx, by, bw, bh, [
    [("Platform governance: ", 24, True, EXIT),
     ("shift the target from transparency to ", 24, False, INK), ("standing and contestability.",
      24, True, VOICE)],
    [("Stakeholder theory: ", 24, True, EXIT),
     ("disaggregate a platform’s power into necessary and contingent functions, then aim exit and "
      "voice where each can work.", 24, False, INK)],
    [("Worker voice: ", 24, True, EXIT),
     ("grounds the EU Platform Work Directive 2024/2831 as coordinative sovereignty — and says when "
      "co-ops, bargaining, and data trusts actually raise standing.", 24, False, INK)],
])

# ---- Zone 9: status + objection box ----------------------------------------
bx, by, bw, bh = card(x, CONTENT_TOP + 20.2, COL_W, 3.4, "9 · Status & next")
text(bx, by, bw, bh, [
    [("A construct, a diagnostic validated on coordination ", 20, False, INK), ("models", 20, True, INK),
     (", and a ", 20, False, INK), ("proposed", 20, True, EXIT),
     (" 18-item voice scale (non-domination · effective voice · governance share) awaiting "
      "validation. Next: field the scale; find the case that separates the causal test from mere "
      "substitutability.", 20, False, INK)]])


# ===========================================================================
# FOOTER
# ===========================================================================
rect(0, 34.0, W_IN, 2.0, fill=BAND)
text(M, 34.15, W_IN - 2*M - 6.5, 1.8, [
    [("Selected references: ", 17, True, TINT),
     ("Hirschman 1970 · Pettit 1997 · Nedelsky 2011 · Markell 2003 · Ostrom 1990 · "
      "Spreitzer 1995 · EU Directive 2024/2831.", 17, False, WHITE)],
    [("Full paper + formal appendix on request · rhunt@bentley.edu", 17, False, TINT)]],
    font=HEAD_FONT, anchor=MSO_ANCHOR.MIDDLE)

# QR (placeholder target — replace with the paper URL)
try:
    import qrcode
    img = qrcode.make("https://www.bentley.edu/")   # PLACEHOLDER — swap for paper/SSRN URL
    qr_path = os.path.join(HERE, "_qr.png"); img.save(qr_path)
    slide.shapes.add_picture(qr_path, Inches(W_IN - M - 1.5), Inches(34.25), Inches(1.5), Inches(1.5))
    text(W_IN - M - 6.4, 34.5, 4.7, 1.0, [[("scan for the paper", 16, False, TINT)],
         [("(placeholder — replace)", 13, False, MUTED)]], font=HEAD_FONT, align=PP_ALIGN.RIGHT)
except Exception as e:
    rect(W_IN - M - 1.5, 34.25, 1.5, 1.5, fill=WHITE, line=HAIR)
    text(W_IN - M - 1.5, 34.25, 1.5, 1.5, [[("QR", 16, True, MUTED)]], font=HEAD_FONT,
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

out = os.path.join(HERE, "coordinative_sovereignty_poster.pptx")
prs.save(out)
print("saved", out)
