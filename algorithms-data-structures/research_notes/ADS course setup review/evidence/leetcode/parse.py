import re,json
D='/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/'
out=[]
# syllabus
L=open(D+'ADS_Syllabus_Draft.md').read().split('\n')
cls=None;lines=[]
rows=[]
i=243
# syllabus table: parse rows w/ wrapped text, by joining
for n in range(243,353):
    pass
# simpler: regex per line for "#num" occurrences
for n,l in enumerate(L[243:353],start=244):
    for m in re.finditer(r'#(\d+) (.+?)(?=\s{2,}|$)',l):
        out.append(dict(file='Syllabus',line=n,num=int(m.group(1)),title_raw=m.group(2),raw=l.strip()))
json.dump(out,open('syl_raw.json','w'),indent=1)
# board & solutions
for fn,key in (('ADS_In_Class_Board_Problems.md','Board'),('ADS_In_Class_Solutions.md','Solutions')):
    L=open(D+fn).read().split('\n')
    c=None;s=None;res=[]
    for n,l in enumerate(L,1):
        m=re.match(r'.*Class (\d+), Problem ([AB])',l)
        if m: c,s=int(m.group(1)),m.group(2)
        m=re.match(r'^Class (\d+): ',l)
        if m: c=int(m.group(1))
        m=re.match(r'^Problem ([AB]) ',l)
        if m: s=m.group(1)
        m=re.match(r'^\*\*#(\d+) (.+)\*\*$',l)
        if m:
            lv=L[n+1].strip() if n+1<len(L) else ''
            url=re.search(r'\((https://leetcode.com/problems/[^)]+)\)',L[n+2]).group(1) if n+2<len(L) and 'leetcode' in L[n+2] else None
            res.append(dict(file=key,line=n,cls=c,slot=s,num=int(m.group(1)),title=m.group(2),lvl=lv.strip('*.'),url=url))
    json.dump(res,open(key+'.json','w'),indent=1)
    print(key,len(res))
# take-homes
L=open(D+'ADS_Take_Homes.md').read().split('\n')
c=None;pat=None;res=[]
for n,l in enumerate(L,1):
    m=re.match(r'^For Class (\d+): (.*)',l)
    if m: c=int(m.group(1))
    m=re.match(r'^\*\*The pattern: (.*?)\*\*',l)
    if m: pat=m.group(1)
    m=re.match(r'^\| (\d+)\s+\| (.+?)\s+\| (Easy|Medium|Hard)\s+\|',l)
    if m:
        url=re.search(r'\((https://leetcode.com/problems/[^)]+)\)',L[n+1])
        res.append(dict(file='Take-Homes',line=n,cls=c,pat=pat,num=int(m.group(1)),title=m.group(2),lvl=m.group(3),url=url.group(1) if url else None))
json.dump(res,open('TH.json','w'),indent=1)
print(len(res))
