from PIL import Image, ImageDraw, ImageFont
import math
W,H=2010,1030
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
F='/System/Library/Fonts/Supplemental/Arial.ttf'; FB='/System/Library/Fonts/Supplemental/Arial Bold.ttf'; FI='/System/Library/Fonts/Supplemental/Arial Italic.ttf'
f=ImageFont.truetype(F,34); fb=ImageFont.truetype(FB,36); fs=ImageFont.truetype(F,30); fi=ImageFont.truetype(FI,30); fsign=ImageFont.truetype(FB,38)
K=(0,0,0)
def box(x0,y0,x1,y1,lines,font=f,bold_first=False,dash=False,w=4):
    if dash:
        for (a,b,c,e) in [(x0,y0,x1,y0),(x1,y0,x1,y1),(x1,y1,x0,y1),(x0,y1,x0,y0)]:
            L=math.hypot(c-a,e-b); n=int(L//24)
            for i in range(0,n,2):
                t0=i/n; t1=min((i+1)/n,1)
                d.line([(a+(c-a)*t0,b+(e-b)*t0),(a+(c-a)*t1,b+(e-b)*t1)],fill=K,width=w)
    else: d.rectangle([x0,y0,x1,y1],outline=K,width=w)
    hs=[]; 
    for i,l in enumerate(lines):
        ft=fb if (bold_first and i==0) else font
        bb=d.textbbox((0,0),l,font=ft); hs.append((l,ft,bb[2]-bb[0],bb[3]-bb[1]))
    tot=sum(h for *_,h in hs)+12*(len(hs)-1); y=(y0+y1)/2-tot/2
    for l,ft,w_,h in hs:
        d.text(((x0+x1)/2-w_/2,y),l,font=ft,fill=K); y+=h+12
def arrow(p,q,dash=False,w=4,head=True):
    (x0,y0),(x1,y1)=p,q
    if dash:
        L=math.hypot(x1-x0,y1-y0); n=int(L//22)
        for i in range(0,n-1,2):
            t0=i/n;t1=(i+1)/n; d.line([(x0+(x1-x0)*t0,y0+(y1-y0)*t0),(x0+(x1-x0)*t1,y0+(y1-y0)*t1)],fill=K,width=w)
    else: d.line([p,q],fill=K,width=w)
    if not head: return
    a=math.atan2(y1-y0,x1-x0); s=22
    d.polygon([(x1,y1),(x1-s*math.cos(a-0.4),y1-s*math.sin(a-0.4)),(x1-s*math.cos(a+0.4),y1-s*math.sin(a+0.4))],fill=K)
# antecedents
box(40,330,420,470,['Task','interdependence'])
box(40,610,420,750,['Tenure on','the system'])
# algorithmacy
box(640,300,1180,770,['Algorithmacy','','Interpreting','Specifying intent','Tracking'],bold_first=True,w=6)
# outcomes
box(1520,330,1940,470,['Coordination quality','with the counterpart'])
box(1520,610,1940,750,['Dispute rate'])
# moderators, between the two outcome paths
box(1250,480,1470,600,['Moderators:','system authority;','rule-change freq.'],font=ImageFont.truetype(F,24))
# controls
box(1520,880,1940,990,['Controls: AI literacy,','algorithmic competency'],font=fs,dash=True)
# antecedent arrows
arrow((420,400),(640,460)); d.text((505,375),'+',font=fsign,fill=K)
arrow((420,680),(640,610)); d.text((505,655),'+',font=fsign,fill=K)
# outcome paths
arrow((1180,430),(1520,400)); d.text((1230,370),'+',font=fsign,fill=K)
arrow((1180,640),(1520,680)); d.text((1230,655),'−',font=fsign,fill=K)
# moderator arrows onto the paths
arrow((1360,480),(1360,418)); arrow((1360,600),(1360,658))
# control arrows
arrow((1730,880),(1730,750),dash=True)
d.line([(1940,935),(1975,935)],fill=K,width=4)
arrow((1975,935),(1975,400),dash=True,head=False)
d.line([(1975,400),(1950,400)],fill=K,width=4)
d.polygon([(1940,400),(1962,389),(1962,411)],fill=K)
im=im.crop((0,270,W,1010)); im.save('/private/tmp/claude-501/-Users-ludwitt/b7816862-76fb-465e-84f5-2874bdfbfe95/scratchpad/ecis_build/figure1.png',dpi=(300,300))
print('ok')
