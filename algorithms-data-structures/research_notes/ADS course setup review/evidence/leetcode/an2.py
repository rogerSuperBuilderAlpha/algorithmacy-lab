import json
lc=json.load(open('lc.json'));B=json.load(open('Board.json'));T=json.load(open('TH.json'))
def q(r): return lc[r['url'].rstrip('/').split('/')[-1]]
def ac(x): return float(json.loads(x['stats'])['acRate'].strip('%'))
rank={'Easy':1,'Medium':2,'Hard':3}
ramp=lambda c:(('Easy','Easy') if c<=8 else ('Easy','Medium') if c<=19 else ('Medium','Medium') if c<=22 else ('Medium','Hard') if c<=26 else ('Medium','Medium') if c<=28 else None)
for c in range(1,31):
    a=[r for r in B if r['cls']==c and r['slot']=='A'][0];b=[r for r in B if r['cls']==c and r['slot']=='B'][0]
    qa,qb=q(a),q(b)
    flag=[]
    r=ramp(c)
    got=(qa['difficulty'],qb['difficulty'])
    if r and got!=r: flag.append(f'RAMP {got} vs {r}')
    if c==29 and not(got[0] in('Medium','Hard') and got[1]=='Hard'): flag.append('ramp29')
    if c==30 and got!=('Hard','Hard'): flag.append('ramp30')
    if rank[got[1]]<rank[got[0]]: flag.append('B<A')
    if got[0]==got[1] and ac(qb)>ac(qa): flag.append(f'B easier by AC ({ac(qa)} vs {ac(qb)})')
    print(c,a['num'],qa['difficulty'],ac(qa),'|',b['num'],qb['difficulty'],ac(qb),flag)
