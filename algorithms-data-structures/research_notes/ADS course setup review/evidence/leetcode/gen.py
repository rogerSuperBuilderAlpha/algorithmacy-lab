import json
lc=json.load(open('lc.json'));B=json.load(open('Board.json'));S=json.load(open('Solutions.json'));T=json.load(open('TH.json'));Y=json.load(open('syl.json'))
def q(r): return lc[r['url'].rstrip('/').split('/')[-1]]
def ac(x): return json.loads(x['stats'])['acRate']
tags=lambda x:', '.join(t['name'] for t in x['topicTags'])
inj={ # judgment notes in-class
(3,'A'):'JUDGMENT: tags Array/String/Trie; plain string scan, not prefix sums (class topic). Level OK.',
(6,'B'):'JUDGMENT: LC tag is Dynamic Programming; the usual solution is a one-pass min-so-far scan, loosely a window. Fits class 6 only loosely.',
(1,'B'):'JUDGMENT: hash-set solution appears in class 1, before hashing is taught in class 4 (a sort-based solution also works).',
(15,'B'):'JUDGMENT: BFS (level order) in a class titled "traversal"; BFS is formally taught in class 19. Minor.',
(3,'B'):'Same level as A but higher acceptance (73.9% vs 48.6%): B is not clearly harder than A.',
(5,'B'):'Same level as A, higher acceptance (74.3% vs 54.6%).',
(6,'B'):'JUDGMENT: tag is DP, not Sliding Window. Same level as A, higher acceptance (57.6% vs 49.6%).',
(7,'B'):'Same level as A, higher acceptance (50.4% vs 45.4%).',
(20,'B'):'Same level as A, higher acceptance (56.5% vs 52.5%); #210 is a direct extension of #207, so judgment: B is the natural next step.',
(21,'B'):'Same level as A, higher acceptance (64.3% vs 61.9%); JUDGMENT: tags Union-Find/Binary Search also apply, Dijkstra fits.',
(30,'B'):'Same level as A, higher acceptance (55.2% vs 46.9%).',
}
inj[(6,'B')]='JUDGMENT: LC tag is Dynamic Programming, not Sliding Window (class topic). Same level as A, higher acceptance (57.6% vs 49.6%).'
th={ # take-home judgment
28:'JUDGMENT: substring search, not prefix sums',58:'JUDGMENT: simple string scan, not prefix sums',
1557:'JUDGMENT: answer is nodes with in-degree 0; no topological ordering needed (tags: DAG only)',
228:'JUDGMENT: simple run scan; LC tags Array only, no merging of intervals',57:'LC tags Array only; JUDGMENT: sorted-interval merge, fits',
463:'JUDGMENT: solvable by counting neighbors; traversal not needed (despite DFS/BFS tags)',
622:'order: Medium listed before Easy #1700',1700:'order: Easy listed after Medium #622',
506:'order: Easy listed after two Mediums',239:'Hard in a class whose in-class B is Medium',778:'Hard in a class whose in-class B is Medium; Dijkstra only one of several tags',
167:'Medium in a class with in-class Easy/Easy',11:'Medium in a class with in-class Easy/Easy',1456:'Medium; in-class Easy/Easy',3:'Medium; in-class Easy/Easy',155:'Medium; in-class Easy/Easy',150:'Medium; in-class Easy/Easy',
22:'JUDGMENT: backtracking (class 24 pattern) rather than recursion/divide-and-conquer; tags include Backtracking',
79:'related to in-class #212 Word Search II (class 23 B); different problem',
219:'related to in-class #217 (class 1 B), different problem',
503:'related to in-class #496 (class 9 A), different problem',
122:'related to in-class #121 (class 6 B), different problem',
}
def esc(s): return s.replace('|','\\|')
o=[]
o.append('### In-class problems (60): syllabus + board + solutions vs LeetCode\n')
o.append('Doc-level column shows Syllabus slot level, then Board level, then Solutions level. All three docs matched LC on number, title and URL slug for all 60 (see Takeaway). Acceptance rate (acRate) is the live value read on 2026-11-12.\n')
o.append('| Class | Slot | # | Title | Syllabus line | Board line | Solutions line | Doc level (Syl/Board/Sol) | LC level | paid_only | acRate | LC topicTags | Verdict |')
o.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for b,s in zip(B,S):
    y=[r for r in Y if r['cls']==b['cls']][0]
    sl=[x.strip() for x in y['lvl'].split('/')][0 if b['slot']=='A' else 1]
    x=q(b)
    note=inj.get((b['cls'],b['slot']),'')
    v='OK' + (' - '+note if note else '')
    o.append(f"| {b['cls']} | {b['slot']} | {b['num']} | {esc(b['title'])} | {y['line']} | {b['line']} | {s['line']} | {sl}/{b['lvl']}/{s['lvl']} | {x['difficulty']} | {x['isPaidOnly']} | {ac(x)} | {esc(tags(x))} | {esc(v)} |")
o.append('\n### Take-home practice problems (90)\n')
o.append('Doc level is the Level column of the take-home table. Pattern is the "The pattern:" line of that take-home. Slug and title matched LC for all 90.\n')
o.append('| Class | TH line | # | Title | Pattern named | Doc level | LC level | paid_only | acRate | LC topicTags | Verdict |')
o.append('|---|---|---|---|---|---|---|---|---|---|---|')
for r in T:
    x=q(r)
    note=th.get(r['num'],'')
    o.append(f"| {r['cls']} | {r['line']} | {r['num']} | {esc(r['title'])} | {esc(r['pat'])} | {r['lvl']} | {x['difficulty']} | {x['isPaidOnly']} | {ac(x)} | {esc(tags(x))} | {'OK' + (' - '+esc(note) if note else '')} |")
open('table.md','w').write('\n'.join(o))
print(len(o))
