import json,re
lc=json.load(open('lc.json'));B=json.load(open('Board.json'));S=json.load(open('Solutions.json'));T=json.load(open('TH.json'));Y=json.load(open('syl.json'))
def slug(r): return r['url'].rstrip('/').split('/')[-1] if r['url'] else None
def norm(s): return re.sub(r'\s+',' ',s).strip()
iss=[]
for src in (B,S,T):
    for r in src:
        q=lc[slug(r)]
        p=[]
        if q['questionFrontendId']!=str(r['num']): p.append(f"number doc {r['num']} vs LC {q['questionFrontendId']}")
        if norm(q['title'])!=norm(r['title']): p.append(f"title doc '{r['title']}' vs LC '{q['title']}'")
        lv=r['lvl']
        if lv!=q['difficulty']: p.append(f"level doc {lv} vs LC {q['difficulty']}")
        if q['isPaidOnly']: p.append("PREMIUM")
        if r['url']!='https://leetcode.com/problems/'+q['titleSlug']+'/' and r['url']!='https://leetcode.com/problems/'+q['titleSlug']: p.append(f"url {r['url']} vs slug {q['titleSlug']}")
        if p: iss.append((r['file'],r['line'],r.get('cls'),r.get('slot'),p))
for i in iss: print(i)
print('---syllabus')
num2={}
for q in lc.values(): num2[q['questionFrontendId']]=q
for r in Y:
    for k in 'AB':
        m=re.match(r'#(\d+) (.*)',r[k]);n,t=m.group(1),norm(m.group(2))
        q=num2.get(n)
        if not q: print('syl',r['cls'],k,'num not in fetched set',n,t);continue
        if norm(q['title'])!=t: print('syl title',r['cls'],k,r['line'],n,t,'|',q['title'])
    la,lb=[x.strip() for x in r['lvl'].split('/')]
    qa=num2.get(re.match(r'#(\d+)',r['A']).group(1));qb=num2.get(re.match(r'#(\d+)',r['B']).group(1))
    if qa and qa['difficulty']!=la: print('syl lvl A',r['cls'],r['line'],la,qa['difficulty'])
    if qb and qb['difficulty']!=lb: print('syl lvl B',r['cls'],r['line'],lb,qb['difficulty'])
print('---cross-doc')
for b,s in zip(B,S):
    if (b['cls'],b['slot'],b['num'],b['title'],b['lvl'],b['url'])!=(s['cls'],s['slot'],s['num'],s['title'],s['lvl'],s['url']): print('B/S diff',b,s)
for r in Y:
    for k in 'AB':
        m=re.match(r'#(\d+) (.*)',r[k])
        for src,nm in ((B,'Board'),(S,'Sol')):
            x=[z for z in src if z['cls']==r['cls'] and z['slot']==k][0]
            if x['num']!=int(m.group(1)) or norm(x['title'])!=norm(m.group(2)): print('syl vs',nm,r['cls'],k,r[k],x['num'],x['title'])
# reuse
from collections import defaultdict
d=defaultdict(list)
for src in (B,T):
    for r in src: d[r['num']].append((r['file'],r['cls'],r.get('slot')))
print('dups',{k:v for k,v in d.items() if len(v)>1})
# Take-home class mapping and counts
from collections import Counter
print(Counter(r['cls'] for r in T))
