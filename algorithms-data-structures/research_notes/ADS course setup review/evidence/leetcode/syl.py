import re,json
L=open('/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_Syllabus_Draft.md').read().split('\n')
# column starts from header line
hdr=[l for l in L[243:253] if 'Problem A' in l][0]
a=hdr.index('**Problem A'); b=hdr.index('**Problem B'); lv=hdr.index('**Level'); 
rows=[];cur=None
for n in range(246,353):
    l=L[n-1]
    m=re.match(r'^\s+(?:(\d+)\s+)?(\d+)\s{2,}',l)
    if m and l.strip() and re.match(r'^\s+(\d+\s+)?\d+\s{3,}',l) :
        cur=dict(cls=int(m.group(2)),line=n,A=l[a:b].strip(),B=l[b:].strip(),lvl=l[lv:a].strip(),lines=[n]);rows.append(cur);continue
    if cur and l.strip() and not l.strip().startswith('---') and n<350:
        cur['A']+=' '+l[a:b].strip(); cur['B']+=' '+l[b:].strip(); cur['lvl']+=' '+l[lv:a].strip(); cur['lines'].append(n)
for r in rows:
    r['A']=r['A'].strip();r['B']=r['B'].strip();r['lvl']=r['lvl'].strip()
json.dump(rows,open('syl.json','w'),indent=1)
print(len(rows))
for r in rows: print(r['cls'],r['line'],'|',r['lvl'],'|',r['A'],'|',r['B'])
