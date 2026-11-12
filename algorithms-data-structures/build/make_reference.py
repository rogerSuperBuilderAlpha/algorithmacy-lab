"""Build the Word reference document that sets the look of every course document.

pandoc copies styles, margins and the footer from this file. The script only sets
layout: fonts, sizes, spacing, borders, margins and the footer. It writes no course text.

Usage: python3 make_reference.py <footer text> <output.docx>
"""
import sys

import docx
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HERE = __file__.rsplit("/", 1)[0]
SERIF = "Times New Roman"
MONO = "Courier New"
BLACK = RGBColor(0, 0, 0)


def set_font(style, name=SERIF, size=None, bold=None, italic=None):
    font = style.font
    font.name = name
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.insert(0, fonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), name)
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if fonts.get(qn(attr)) is not None:
            del fonts.attrib[qn(attr)]
    if size is not None:
        font.size = Pt(size)
    if bold is not None:
        font.bold = bold
    if italic is not None:
        font.italic = italic
    font.color.rgb = BLACK


def spacing(style, before=0, after=6, line=None, keep_next=None):
    fmt = style.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    if line is not None:
        fmt.line_spacing = line
    if keep_next is not None:
        fmt.keep_with_next = keep_next


def bottom_border(style, size=4, color="808080", space=1):
    ppr = style.element.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), str(space))
    bottom.set(qn("w:color"), color)
    borders.append(bottom)
    # Word and LibreOffice merge identical borders on consecutive paragraphs into one box.
    # A "between" border draws the rule between each pair, so every line shows.
    between = OxmlElement("w:between")
    for k, v in (("w:val", "single"), ("w:sz", str(size)), ("w:space", str(space)), ("w:color", color)):
        between.set(qn(k), v)
    borders.append(between)
    ppr.append(borders)


def get_or_add(doc, name, kind=WD_STYLE_TYPE.PARAGRAPH, base="Normal"):
    try:
        return doc.styles[name]
    except KeyError:
        style = doc.styles.add_style(name, kind)
        if base:
            style.base_style = doc.styles[base]
        return style


def table_borders(doc):
    """Give pandoc's 'Table' style a rule above and below the table and under the header row."""
    style = doc.styles["Table"].element
    tblpr = style.find(qn("w:tblPr"))
    if tblpr is None:
        tblpr = OxmlElement("w:tblPr")
        style.append(tblpr)
    for old in tblpr.findall(qn("w:tblBorders")):
        tblpr.remove(old)
    borders = OxmlElement("w:tblBorders")
    for edge, size in (("top", 8), ("bottom", 8)):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(size))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    tblpr.append(borders)
    cellmar = OxmlElement("w:tblCellMar")
    for edge, width in (("top", 40), ("bottom", 40), ("left", 80), ("right", 80)):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), str(width))
        el.set(qn("w:type"), "dxa")
        cellmar.append(el)
    tblpr.append(cellmar)
    for old in style.findall(qn("w:tblStylePr")):
        if old.get(qn("w:type")) == "firstRow":
            style.remove(old)
    first = OxmlElement("w:tblStylePr")
    first.set(qn("w:type"), "firstRow")
    rpr = OxmlElement("w:rPr")
    rpr.append(OxmlElement("w:b"))
    first.append(rpr)
    tcpr = OxmlElement("w:tcPr")
    tcb = OxmlElement("w:tcBorders")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "0")
    bottom.set(qn("w:color"), "000000")
    tcb.append(bottom)
    tcpr.append(tcb)
    first.append(tcpr)
    style.append(first)


def footer(doc, text):
    section = doc.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)
    section.footer.is_linked_to_previous = False
    para = section.footer.paragraphs[0]
    for run in list(para.runs):
        run._r.getparent().remove(run._r)
    para.paragraph_format.tab_stops.add_tab_stop(Inches(6.7), alignment=2)
    run = para.add_run(text + "\t")
    run.font.size = Pt(8.5)
    run.font.name = SERIF
    # PAGE field for the page number
    fld_run = para.add_run()
    fld_run.font.size = Pt(10)
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    fld_run._r.append(begin)
    fld_run._r.append(instr)
    fld_run._r.append(end)


def main(footer_text, out):
    doc = docx.Document(f"{HERE}/pandoc-default-reference.docx")
    st = doc.styles

    set_font(st["Normal"], size=11)
    spacing(st["Normal"], 0, 6, 1.1)
    for name in ("Body Text", "First Paragraph"):
        set_font(st[name], size=11)
        spacing(st[name], 0, 6, 1.1)
    set_font(st["Compact"], size=11)
    spacing(st["Compact"], 0, 3, 1.1)

    set_font(st["Title"], size=24, bold=True)
    spacing(st["Title"], 0, 2, 1.0)
    st["Title"].paragraph_format.alignment = 0
    set_font(st["Subtitle"], size=13, bold=False)
    spacing(st["Subtitle"], 0, 14, 1.0)
    st["Subtitle"].paragraph_format.alignment = 0
    for name in ("Author", "Date"):
        set_font(st[name], size=11)
        st[name].paragraph_format.alignment = 0

    set_font(st["Heading 1"], size=17, bold=True)
    spacing(st["Heading 1"], 14, 4, 1.0, True)
    set_font(st["Heading 2"], size=13, bold=True)
    spacing(st["Heading 2"], 12, 4, 1.0, True)
    set_font(st["Heading 3"], size=11.5, bold=True)
    spacing(st["Heading 3"], 10, 3, 1.0, True)
    set_font(st["Heading 4"], size=11, bold=True, italic=False)
    spacing(st["Heading 4"], 8, 2, 1.0, True)

    set_font(st["Block Text"], size=11)
    set_font(st["Hyperlink"], size=None)
    st["Hyperlink"].font.underline = True

    code = get_or_add(doc, "Source Code")
    set_font(code, name=MONO, size=9.5)
    spacing(code, 2, 6, 1.0)
    code.paragraph_format.left_indent = Inches(0.25)
    verb = st["Verbatim Char"]
    set_font(verb, name=MONO, size=9.5)

    # Answer-sheet styles
    line = get_or_add(doc, "Answer Line")
    set_font(line, size=11)
    line.paragraph_format.space_before = Pt(0)
    line.paragraph_format.space_after = Pt(0)
    line.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
    line.paragraph_format.line_spacing = Pt(23)
    bottom_border(line, 4, "A0A0A0")

    field = get_or_add(doc, "Answer Field")
    set_font(field, size=11, bold=True)
    field.paragraph_format.space_before = Pt(9)
    field.paragraph_format.space_after = Pt(2)
    bottom_border(field, 4, "808080")

    sheet = get_or_add(doc, "Sheet Header")
    set_font(sheet, size=10)
    spacing(sheet, 0, 10, 1.0)

    label = get_or_add(doc, "Problem Label")
    set_font(label, size=10.5)
    spacing(label, 0, 0, 1.0, True)

    small = get_or_add(doc, "Small Print")
    set_font(small, size=9.5)
    spacing(small, 4, 4, 1.05)

    level = get_or_add(doc, "Level Line")
    set_font(level, size=10)
    spacing(level, 0, 8, 1.0)

    table_borders(doc)
    footer(doc, footer_text)
    doc.save(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
