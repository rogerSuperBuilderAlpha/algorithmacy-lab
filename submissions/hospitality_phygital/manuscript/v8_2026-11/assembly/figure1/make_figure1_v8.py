# Draws DRAFT_v8's Figure 1 as SVG: v7's figure (keystone_2026-11/figure1/) with three labels changed to match v8 (V8 assembly, 13 Nov 2026).
from xml.sax.saxutils import escape as E
W,H=1500,960
F='Helvetica, Arial, sans-serif'
out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#222"/></marker></defs>',
 f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
def text(x,y,s,size=16,weight='normal',anchor='middle',style='normal',fill='#111'):
    out.append(f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{weight}" font-style="{style}" text-anchor="{anchor}" fill="{fill}">{E(s)}</text>')
def box(x,y,w,h,lines,fill='#ffffff',dash=False,bold_first=True,size=15):
    d=' stroke-dasharray="7,5"' if dash else ''
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="#222" stroke-width="1.6"{d}/>')
    n=len(lines); lh=size+5; y0=y+h/2-(n-1)*lh/2+size*0.35
    for i,l in enumerate(lines):
        text(x+w/2,y0+i*lh,l,size=size+(1 if i==0 and bold_first else 0),weight='bold' if (i==0 and bold_first) else 'normal')
def arrow(x1,y1,x2,y2,dash=False):
    d=' stroke-dasharray="6,5"' if dash else ''
    out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#222" stroke-width="1.6" marker-end="url(#a)"{d}/>')
def heading(y,s): text(30,y,s,size=18,weight='bold',anchor='start')
GREY='#e6e6e6'
# Panel A
heading(36,"A   What binds the duty, and what it contains")
g=[(110,"Holding out",["settles who took up the role, and when"]),(570,"The guest's reliance",["makes the duty run to this guest"]),(1030,"Control of the guest's space",["stops a notice writing the duty away"])]
for x,t,l in g:
    box(x,52,360,70,[t]+l)
    arrow(x+180,122,x+180 if x==570 else (x+180+ (120 if x==110 else -120)),164)
box(300,166,900,46,["The role of host specifies the duty: its content, when it arises, and who holds it"],bold_first=False,size=16)
arrow(560,212,430,248); arrow(940,212,1070,248)
box(130,250,600,128,["Before the stay: admission","the duty to receive travellers (hotel proprietors)","not to refuse a guest on a protected ground","(every provider of services, Great Britain)"])
box(770,250,600,128,["During the stay: reception","reasonable care for the guest's safety","services performed with care (traders to consumers)","reasonable adjustments (disabled guests)"])
# Panel B
heading(424,"B   Who holds it when others do the work")
hb=[("Owner and operator",["hold the duty of care,","each to its degree of control"]),
    ("Brand",["may answer as the","operator's principal (agency)"]),
    ("Booking platform",["answers as provider only where","it acts or appears as one"]),
    ("Software maker",["answers to the guest for defective","products (EU, from December 2026)"]),
    ("Placing public body",["keeps its public duty","when contractors perform it"])]
x=40
for t,l in hb:
    box(x,440,264,96,[t]+l); x+=285
text(W/2,566,"What stays with the host depends on the duty and on the doctrine that governs it.",size=15,style='italic')
# Panel C
heading(612,"C   During the stay: the further duty (the paper's own step)")
fl=[(40,200,["Guest","inside the host's space"]),(290,220,["A failure in","the guest's case"]),(560,220,["Touchpoint","staff or system"]),(830,300,["Someone able to correct it","power over the single case"]),(1180,280,["Correction","while the stay lasts"])]
for i,(x,w,l) in enumerate(fl):
    box(x,676,w,80,l,fill=GREY)
    if i<len(fl)-1:
        nx=fl[i+1][0]; arrow(x+w,716,nx-2,716)
# bracket above the route
out.append('<path d="M 40 664 L 40 654 L 1130 654 L 1130 664" fill="none" stroke="#222" stroke-width="1.3"/>')
text(585,632,"some timely means by which the failure reaches them; where only the guest perceives it,",size=15)
text(585,649,"a route the guest can use without depending on the host's goodwill",size=15)
# automation note
out.append('<line x1="880" y1="756" x2="840" y2="800" stroke="#222" stroke-width="1.2" stroke-dasharray="5,4"/>')
text(700,818,"automation can move this person behind the machine",size=15,style='italic')
# routing proposal and after-stay
box(300,846,700,58,["Among several firms, the party in control of the guest's space routes the report","to the firm with power over the failing part (our proposal)"],dash=True,bold_first=False,size=14)
arrow(1000,860,1050,758,dash=True)
arrow(1320,756,1320,844)
box(1120,846,340,58,["After the stay: repair, and","accountability before a forum"],bold_first=False,size=15)
# legend
text(30,944,"Unshaded: the paper's reading of the field, the philosophy and the law.   Shaded: the further duty, the paper's own step.   Dashed: a proposal.",size=13,anchor='start',fill='#333')
out.append('</svg>')
open('figure1_v8.svg','w').write('\n'.join(out))
print('svg written')
