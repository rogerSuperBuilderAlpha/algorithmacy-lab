<!-- DRAFTED BY CLAUDE (Opus 5.5), 11 Nov 2026, run rr-2026-11-k. -->
# Assembly aids for DRAFT_v7

Copiers, not judges. `final.json` holds each ledger entry's final sentence, chosen by hand where an entry has more than one version (see LEDGER.md, 'Assembly'); `assemble.py` copies them into `../../../DRAFT_v7.md` and `../MANUSCRIPT.md` with the paragraph breaks and headings set by hand in the script; `build_letters.py` fills the two letter templates from the same sentences and checks every quotation against the draft. The scripts read and write this session's scratchpad paths; to rerun them elsewhere, change `SP` at the top of each to this folder. Any change to a sentence is made in LEDGER.md first, then in `final.json`.
