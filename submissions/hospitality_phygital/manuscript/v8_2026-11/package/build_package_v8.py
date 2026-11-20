#!/usr/bin/env python3
"""Assemble the v8 revision package into one markdown file and convert it to .docx with pandoc.

Adapted from keystone_2026-11/package/build_package.py (v7). Copies text; changes no wording except to
strip HTML comments, demote headings under each part's title, and size the figure.
Parts: cover (COVER_v8.md), the manuscript, front matter, the two letters, the v8 report, and the
marked manuscript, which tags every sentence [PB] (Pierre's, verbatim), [PB-a] (Pierre's, adapted) or
[C] (Claude's).
Usage: python3 build_package_v8.py OUT.md OUT.docx
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V8 = HERE.parent
M = V8.parent                                   # .../manuscript
out_md, out_docx = Path(sys.argv[1]), Path(sys.argv[2])
PB = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'
FIG = 'v8_2026-11/assembly/figure1/figure1_v8.png'


def clean(t, shift=1):
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    lines, infence = [], False
    for l in t.split('\n'):
        if l.startswith('```'):
            infence = not infence
        if not infence and re.match(r'^#{1,5} ', l):
            l = '#' * shift + l
        lines.append(l)
    return '\n'.join(lines).strip() + '\n'


def read(p):
    return Path(p).read_text(encoding='utf-8')


mark = "*Drafted by Claude (Opus 5.5), except the abstract and the sentences DRAFT_v8_marked.md tags as Pierre's; not yet read aloud by the authors.*\n\n"
sized = lambda t: t.replace(f'![]({FIG})', f'![]({FIG}){{width=6.5in}}')
parts = [
    clean(read(HERE / 'COVER_v8.md'), shift=0),
    '# Part 1. The manuscript (DRAFT_v8)\n\n' + mark + clean(sized(read(M / 'DRAFT_v8.md'))),
    '# Part 2. Front matter\n\n' + mark + clean(read(M / 'submission/FRONT_MATTER_v8.md')),
    '# Part 3. Response to reviewers\n\n' + mark + clean(read(M / 'submission/RESPONSE_TO_REVIEWERS_v8.md')),
    '# Part 4. Note to the special-issue editor\n\n' + mark + clean(read(M / 'submission/RESPONSE_TO_EDITOR_v8.md')),
    '# Part 5. The v8 report\n\n' + mark + clean(read(V8 / 'REPORT_V8.md')),
    '# Appendix. The manuscript with each sentence\'s provenance\n\n' + mark
    + '*[PB] Pierre\'s sentence, verbatim. [PB-a] Pierre\'s sentence, adapted, with the reason in v8_2026-11/LEDGER.md. [C] Claude\'s sentence.*\n\n'
    + clean(sized(read(M / 'DRAFT_v8_marked.md'))),
]
out_md.write_text(PB.join(parts), encoding='utf-8')
subprocess.run(['pandoc', str(out_md), '-f',
                'markdown+pipe_tables+raw_attribute+lists_without_preceding_blankline-tex_math_dollars',
                '-o', str(out_docx), '--resource-path', str(M)], check=True)
print('written', out_docx)
