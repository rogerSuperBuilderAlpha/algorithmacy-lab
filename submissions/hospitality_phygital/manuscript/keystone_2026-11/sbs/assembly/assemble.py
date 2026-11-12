# Finding aid and copier: rebuilds DRAFT_v7.md and sbs/MANUSCRIPT.md from final.json (each ledger entry's final sentence).
# It decides nothing: which sentence is final, where paragraphs break, and every cut are set by hand in final.json and below.
import json,sys
SP='/private/tmp/claude-501/-Users-ludwitt/726e3364-a25c-4111-89c8-312a57b9f782/scratchpad/assembly'
M='/Users/ludwitt/iit-playground/wt-hs-rr/submissions/hospitality_phygital/manuscript'
f=json.load(open(SP+'/final.json'))
L=open(M+'/keystone_2026-11/sbs/LEDGER.md',encoding='utf-8').read()
def block(h):
    out=[];on=False
    for line in L.split('\n'):
        if line.startswith(f'### {h} '): on=True; continue
        if on and line.startswith('### '): break
        if on and line.startswith('>'): out.append(line[2:] if line.startswith('> ') else '')
    return '\n'.join(out)
starts={1,8,15,20, 25,34,40,49,55,62,70,79,87, 91,100,109,117,123,129,138,146,
        152,156,162,169,175,182,188,194,197,202,207,215,225,234, 237,240,250,256,260}
heads={1:'## Introduction',25:"## The host's power and the host's duty",91:"## Delegation and the guest's claim: Beyond the host in person?",
       152:'## Assembled hosts at the touchpoint',156:'### Where the person with power sits',175:'### Who must be at the end of the route',
       194:'### Six questions and four cases',207:"### When the route is owed, and the law's floor",225:'### Designing for correction during the stay',237:'## Conclusion'}
after={154:"![](keystone_2026-11/figure1/figure1_v7.png)\n\n**Figure 1.** The host's duty, its holders, and the further duty during the stay.",195:block('L-1'),213:block('T1'),235:block('T2')}
out=[];cur=[]
def flush():
    global cur
    if cur: out.append(' '.join(cur)); cur=[]
for i in range(1,264):
    if i in starts: flush()
    if i in heads: out.append(heads[i])
    t=f[f'S-{i:03d}']
    if t[0]!='cut': cur.append(t[1])
    for sfx in 'abc':
        x=f.get(f'S-{i:03d}{sfx}')
        if x and x[0]!='cut': cur.append(x[1])
    if i in after: flush(); out.append(after[i])
flush()
body='\n\n'.join(out)+'\n'
abstract=' '.join(f[f'A-{i}'][1] for i in range(1,7))
kw='\n\n**Keywords:** phygital hospitality; algorithmic mediation; host duties; assembled host; service failure; accountability\n\n'
title='# Who hosts the guest? Algorithmic mediation, standing and responsibility in phygital hospitality\n\n## Abstract\n\n'
head=open(SP+'/draft_head.txt').read(); tail=open(SP+'/draft_tail.txt').read()
open(M+'/DRAFT_v7.md','w',encoding='utf-8').write(head+title+abstract+kw+body+tail)
sb="<!-- DRAFTED BY CLAUDE (Opus 5.5), 11 Nov 2026. Stage 5 of ~/.claude/skills/sentence-by-sentence/: the prose of v7, in ledger order, each sentence in its final form as recorded in LEDGER.md (the rewritten form where an entry has one; the gate and assembly revisions where a section was cut). Every word here is Claude's; none is the authors'. -->\n\n"
open(M+'/keystone_2026-11/sbs/MANUSCRIPT.md','w',encoding='utf-8').write(sb+title+abstract+kw+body)
print('written')
