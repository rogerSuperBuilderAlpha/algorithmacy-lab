# Chapter manuscript — "Algorithmacy and Sovereignty"

IGI Global volume *Organizational Implications of Digital Sovereignty in the Age of AI*
(ed. Samuel Fosso Wamba). Abstract accepted. Full chapter due **2026-08-30**.
Double-anonymized. Academic APA.

**Authors:** Roger Hunt (Bentley), Pierre Berthon (Bentley), Sara Whitmer (Iowa).

## What to edit

| File | Role |
| --- | --- |
| [`chapter.md`](chapter.md) | **Live manuscript.** The only submittable text. One paragraph per block. |
| [`STYLE_SPEC.md`](STYLE_SPEC.md) | House bars (G1–G16) for this chapter. |
| [`IGI_REQUIREMENTS.md`](IGI_REQUIREMENTS.md) | Venue checklist. |
| [`exports/Full Paper - Alg & Sov.docx`](exports/Full%20Paper%20-%20Alg%20%26%20Sov.docx) | Upload target. Times New Roman 12pt, double-spaced, US Letter, APA 7, anonymized. |

`exports/chapter_grammarly.md` and the Word file are generated. Never hand-edit them.

```bash
python3 regen_exports.py           # rewrite both exports from chapter.md
python3 regen_exports.py --check   # fail if either has drifted
```

Word styling comes from `reference.docx`, rebuilt by `build_reference_docx.py`.

## Process archive

Sentence-by-sentence rebuild, cadence pass, gate reports, and drafting ledgers live under
[`process/`](process/). They record how the draft was built; they are not alternate manuscripts.

Older drafts: [`../archive/drafts/`](../archive/drafts/). Presentation materials:
[`../presentations/`](../presentations/).
