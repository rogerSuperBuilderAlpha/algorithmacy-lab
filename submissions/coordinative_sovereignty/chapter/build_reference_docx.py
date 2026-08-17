#!/usr/bin/env python3
"""Build reference.docx — the Word styling pandoc applies when it renders chapter.md.

Pandoc's stock reference document produces a manuscript that reads as a tool dump: sans-serif
body, 20pt blue-ish headings, single spacing, no page numbers. This rebuilds it to what a
submitted chapter should look like:

  body        Times New Roman 12pt, double-spaced, no first-line indent
              (no indent so the APA reference list keeps its shape)
  headings    Times New Roman 12pt bold, APA 7 placement —
              level 1 centered, level 2 flush left, level 3 flush left italic
  page        US Letter, 1-inch margins, page number top right

Run this only when the styling needs to change; regen_exports.py uses the reference.docx it
writes. Committed alongside it so the render is reproducible.
"""

import re
import shutil
import subprocess
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "reference.docx"

FONT = "Times New Roman"

HEADER_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr><w:jc w:val="right"/></w:pPr>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    <w:r><w:t>1</w:t></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
  </w:p>
</w:hdr>
"""

# Times New Roman 12pt (sz is half-points), double-spaced, no space between paragraphs.
DOC_DEFAULTS = (
    '<w:docDefaults>'
    '<w:rPrDefault><w:rPr>'
    f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:eastAsia="{FONT}" w:cs="{FONT}"/>'
    '<w:sz w:val="24"/><w:szCs w:val="24"/>'
    '</w:rPr></w:rPrDefault>'
    '<w:pPrDefault><w:pPr>'
    '<w:spacing w:before="0" w:after="0" w:line="480" w:lineRule="auto"/>'
    '</w:pPr></w:pPrDefault>'
    '</w:docDefaults>'
)

# APA 7: L1 centered bold, L2 flush-left bold, L3 flush-left bold italic. All 12pt, no color.
HEADINGS = {
    "Heading1": ('<w:jc w:val="center"/>', "<w:b/>"),
    "Heading2": ("", "<w:b/>"),
    "Heading3": ("", "<w:b/><w:i/>"),
    "Heading4": ("", "<w:b/><w:i/>"),
}


def restyle_headings(styles: str) -> str:
    for name, (jc, runfmt) in HEADINGS.items():
        pattern = r'(<w:style [^>]*w:styleId="' + name + r'"[^>]*>)(.*?)(</w:style>)'
        m = re.search(pattern, styles, re.S)
        if not m:
            continue
        keep = re.search(r"<w:name [^/]*/>", m.group(2))
        based = re.search(r"<w:basedOn [^/]*/>", m.group(2))
        body = (
            (keep.group(0) if keep else "")
            + (based.group(0) if based else "")
            + "<w:pPr>"
            + '<w:keepNext/><w:spacing w:before="240" w:after="0" w:line="480" w:lineRule="auto"/>'
            + jc
            + "</w:pPr>"
            + "<w:rPr>"
            + f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}"/>'
            + runfmt
            + '<w:sz w:val="24"/><w:szCs w:val="24"/>'
            + "</w:rPr>"
        )
        styles = styles[: m.start()] + m.group(1) + body + m.group(3) + styles[m.end() :]
    return styles


def main() -> int:
    base = HERE / ".ref_base.docx"
    with base.open("wb") as fh:
        subprocess.run(
            ["pandoc", "--print-default-data-file", "reference.docx"], stdout=fh, check=True
        )

    src = zipfile.ZipFile(base)
    if OUT.exists():
        OUT.unlink()
    dst = zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED)

    for item in src.namelist():
        data = src.read(item)

        if item == "word/styles.xml":
            s = data.decode("utf8")
            s = re.sub(r"<w:docDefaults>.*?</w:docDefaults>", DOC_DEFAULTS, s, flags=re.S)
            s = restyle_headings(s)
            data = s.encode("utf8")

        elif item == "word/document.xml":
            s = data.decode("utf8")
            sect = (
                "<w:sectPr>"
                '<w:headerReference xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
                'w:type="default" r:id="rIdHeaderPage"/>'
                '<w:pgSz w:w="12240" w:h="15840"/>'
                '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
                'w:header="720" w:footer="720" w:gutter="0"/>'
                '<w:footnotePr><w:numRestart w:val="eachSect"/></w:footnotePr>'
                "</w:sectPr>"
            )
            s = re.sub(r"<w:sectPr>.*?</w:sectPr>", sect, s, flags=re.S)
            data = s.encode("utf8")

        elif item == "word/_rels/document.xml.rels":
            s = data.decode("utf8")
            rel = (
                '<Relationship Id="rIdHeaderPage" '
                'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" '
                'Target="header1.xml"/>'
            )
            s = s.replace("</Relationships>", rel + "</Relationships>")
            data = s.encode("utf8")

        elif item == "[Content_Types].xml":
            s = data.decode("utf8")
            override = (
                '<Override PartName="/word/header1.xml" '
                'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
            )
            s = s.replace("</Types>", override + "</Types>")
            data = s.encode("utf8")

        dst.writestr(item, data)

    dst.writestr("word/header1.xml", HEADER_XML)
    dst.close()
    src.close()
    base.unlink()
    print(f"wrote {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
