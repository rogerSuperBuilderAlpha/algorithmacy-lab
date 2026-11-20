import re,sys
t=open("/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_Take_Homes.md").read().split("\n")
cls=None; inread=False; buf=[]; out=[]
for i,l in enumerate(t,1):
    m=re.match(r"For Class (\d+): (.*)",l)
    if m: cls=(m.group(1),m.group(2))
    if l.startswith("**Read**"): inread=True; buf=[]; continue
    if inread:
        if l.startswith("**Practice") : inread=False
        else: buf.append((i,l))
        if l.startswith("**Practice"):
            txt=" ".join(x[1].lstrip("> ").strip() for x in buf)
            for it in re.findall(r"•\s*\[\[(.*?)\]\{\.underline\}\]\((.*?)\)",txt):
                out.append((cls[0],cls[1],it[0],it[1],buf[0][0]))
for o in out: print("\t".join(map(str,o)))
