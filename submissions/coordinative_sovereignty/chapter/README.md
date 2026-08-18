# Chapter manuscript — "Algorithmacy and Sovereignty"

IGI Global volume *Organizational Implications of Digital Sovereignty in the Age of AI*
(ed. Samuel Fosso Wamba). Abstract accepted. Full chapter due **2026-08-30**.
Double-anonymized. Academic APA.

**Authors:** Roger Hunt (Bentley), Pierre Berthon (Bentley), Sara Whitmer (Iowa).

## What to edit

- **Draft:** [`chapter.md`](chapter.md) — the only submittable text. One paragraph per block.
- **Venue rules:** [`IGI_REQUIREMENTS.md`](IGI_REQUIREMENTS.md).
- **Submission file:** [`exports/Full Paper - Alg & Sov.docx`](exports/Full%20Paper%20-%20Alg%20%26%20Sov.docx).
  Times New Roman 12pt, double-spaced, US Letter, APA 7 headings, anonymized.

`exports/chapter_grammarly.md` and the Word file are generated. Never hand-edit them.

```bash
python3 regen_exports.py           # rewrite both exports from chapter.md
python3 regen_exports.py --check   # fail if either has drifted
```

Word styling comes from `reference.docx`, rebuilt by `build_reference_docx.py`.

Presentation materials live in [`../presentations/`](../presentations/). Older drafts and
process logs live in [`../archive/`](../archive/).
