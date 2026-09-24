# Capture manifest

How each source file in this folder was made and checked. The capture tool is
[`capture_gemini_share.py`](capture_gemini_share.py); it runs on the system `python3` (bs4, lxml) with
pandoc on the PATH. Raw DOM dumps stay local, outside the repo, and are identified here by sha256.

## Gemini share pages (G1–G7)

Captured 2026-09-24 with Google Chrome 153.0.8010.54 (headless) and pandoc 3.9. Each page was rendered
twice, with 20-second and 40-second virtual-time budgets; the column "20 s = 40 s" records whether the
normalized conversation text of the two renders hashed identically, which rules out lazy-loaded content.
The Markdown was then rebuilt twice from the 40-second dump and compared byte for byte (all identical).

| file | share id | Gemini title | turns | replies per turn | words | math | web markers | source chips | 20 s = 40 s | raw sha256 (40 s dump) | md sha256 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [`G1_gem_prompt_algebraic_logic.md`](G1_gem_prompt_algebraic_logic.md) | `wifYlPqIe4ce` | Interdisciplinary Algebraic Logic Notebook Prompt | 1 | 1 | 466 | 0 | 0 | 0 | yes | `64faf0a15568b872` | `88c7924ec4679a8c` |
| [`G2_ux_design_ethics.md`](G2_ux_design_ethics.md) | `INo1hh79aNsi` | Expanding UX Design Ethics Research | 2 | 1/2 | 5,810 | 0 | 109 | 0 | yes | `1b68ebc53d08e1d7` | `81c1ea670262f23f` |
| [`G3_pid_synergy_loss.md`](G3_pid_synergy_loss.md) | `2L9EOtC5Hywc` | Quantifying Synergy Loss via PID | 1 | 1 | 490 | 2 | 0 | 8 | yes | `858ce7ca900e883f` | `f3dc3fde8cec3e86` |
| [`G4_xai_information_loss.md`](G4_xai_information_loss.md) | `eWIbxgiGArtw` | Quantifying Information Loss in XAI | 4 | 1/1/1/2 | 5,450 | 66 | 83 | 0 | yes | `58f01f66ef786bc4` | `3fd176acad6dc484` |
| [`G5_iit_org_coordination.md`](G5_iit_org_coordination.md) | `LFGcgeELx0CL` | Quantifying Organizational Coordination via IIT | 1 | 1 | 1,725 | 8 | 0 | 8 | yes | `13a575d14ae857ef` | `58271a0c4575a117` |
| [`G6_foundational_literature.md`](G6_foundational_literature.md) | `cIRJ3NPUJRXz` | Foundational Literature for Research Library | 6 | 1/1/1/1/1/1 | 6,669 | 54 | 0 | 121 | yes | `c03879de35bbf4f7` | `8c8d50442d52d39f` |
| [`G7_tablets_to_algorithms.md`](G7_tablets_to_algorithms.md) | `SWkYyi5Ey3Ji` | From Tablets to Algorithms: Literacy Evolution | 4 | 1/2/1/2 | 8,774 | 0 | 180 | 0 | yes | `91aa3a72b26df2d1` | `9aebdbfb5e1653b2` |

**Columns.** *Words* counts the text as the page shows it, prompts and replies, with each formula and
each source marker counted as one word. *Math* is the number of formulas restored from Gemini's
`data-math` attributes (KaTeX renders every glyph twice, so the rendered text is never used). *Web
markers* are Gemini's numbered footnotes `[n]`. *Source chips* are the Project documents or uploaded
files Gemini cited, kept as `[source: …]`.

**Layout choices.** Each prompt sits in a `~~~~text` fence, which keeps its line breaks and indentation
exactly (Gemini pads every prompt line with one space at each end; that padding is removed). Reply
headings are shifted down two levels so a report's own `#` and `##` headings sit under the file's
`## Turn k — response` headings rather than beside them. Deep Research plan steps keep their line breaks.
Code blocks keep the language label the page shows.

**What the pages do not contain.** Four replies are Deep Research reports (G2 turn 2, G4 turn 4, G7 turns
2 and 4). Their web-source lists are not in the share DOM, and the Google Docs exports do not carry them
either: D2 and D3 have no works-cited list, and neither does the DIAL arm's export of G7's first report.
The footnote numbers therefore point nowhere recoverable from these files; `../SOURCE.md` lists this under
"Still missing". The interface elements removed from each reply (buttons, icons, source carousels, the
empty Deep Research chip, the report panel's title bar, which repeats the plan title) are counted in the
capture statistics and contain no model text.

## Checks run

| check | result |
| --- | --- |
| one `message-content` or more per prompt, none empty | pass, all seven |
| 20 s and 40 s renders give identical conversation text | pass, all seven |
| rebuild from raw is byte-identical | pass, all seven |
| turn-by-turn comparison of page text against Markdown (four independent auditors) | pass: no missing or extra model text; layout faults they found are fixed above |
| no leftover KaTeX or MathML markup | pass |
| privacy grep | pass: no email addresses; the only account name is the public repo owner, in G5's pasted prompt |
| page chrome (share links, sign-in shell, "Show more") absent | pass |

## Drive documents (D1–D6)

Read through the Google Drive connector on 2026-09-24. Two independent teams of agents each transcribed
every document; the two copies matched byte for byte for all twelve Docs read, including the duplicate
copies of D1. Each D file's header gives its Drive file id, creation time and body sha256. D4 contains a
local path from the author's machine, kept verbatim; the same path already appears in tracked files of
this repository.

## P1

The author's paste, written out as received. It has no independent copy to check against.
