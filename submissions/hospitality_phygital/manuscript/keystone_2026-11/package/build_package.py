# Assembles the v7 revision package (cover, manuscript, front matter, letters, report, appendices) into one
# markdown file and converts it to .docx with pandoc. Copies text; changes no wording except to strip HTML
# comments, demote headings under each part's title, and size the figure.
import re,subprocess,sys
from pathlib import Path
M=Path(__file__).resolve().parents[2]          # .../manuscript
K=M/'keystone_2026-11'
out_md=Path(sys.argv[1]); out_docx=Path(sys.argv[2])
PB='\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'
def clean(t,shift=1):
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    lines=[]
    infence=False
    for l in t.split('\n'):
        if l.startswith('```'): infence=not infence
        if not infence and re.match(r'^#{1,5} ',l): l='#'*shift+l
        lines.append(l)
    return '\n'.join(lines).strip()+'\n'
mark="*Drafted by Claude (Opus 5.5); not yet read aloud by the authors.*\n\n"
parts=[]
parts.append(clean((K/'package/COVER.md').read_text(encoding='utf-8'),shift=0))
draft=(M/'DRAFT_v7.md').read_text(encoding='utf-8').replace('![](keystone_2026-11/figure1/figure1_v7.png)','![](keystone_2026-11/figure1/figure1_v7.png){width=6.5in}')
parts.append('# Part 1. The manuscript (DRAFT_v7)\n\n'+mark+clean(draft))
parts.append('# Part 2. Front matter\n\n'+mark+clean((M/'submission/FRONT_MATTER_v7.md').read_text(encoding='utf-8')))
parts.append('# Part 3. Response to reviewers\n\n'+mark+clean((M/'submission/RESPONSE_TO_REVIEWERS_v7.md').read_text(encoding='utf-8')))
parts.append('# Part 4. Note to the special-issue editor\n\n'+mark+clean((M/'submission/RESPONSE_TO_EDITOR_v7.md').read_text(encoding='utf-8')))
parts.append('# Part 5. The research report\n\n'+mark+clean((K/'REPORT.md').read_text(encoding='utf-8')))
parts.append('# Appendix A. Figure 1: every label and the sentence it rests on\n\n'+mark+clean((K/'figure1/README.md').read_text(encoding='utf-8')))
parts.append('# Appendix B. The argument dossier (ARGUMENT.md)\n\n'+mark+clean((K/'ARGUMENT.md').read_text(encoding='utf-8')))
out_md.write_text(PB.join(parts),encoding='utf-8')
subprocess.run(['pandoc',str(out_md),'-f','markdown+pipe_tables+raw_attribute+lists_without_preceding_blankline-tex_math_dollars','-o',str(out_docx),'--resource-path',str(M)],check=True)
print('written',out_docx)
