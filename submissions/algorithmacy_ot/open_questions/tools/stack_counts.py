"""Recompute per-stack support from a stack membership TSV (oq_id, stack_id, role).

Usage: python3 tools/stack_counts.py synthesis/stacks/STACKS_X.tsv
Reports, per stack: pieces 2025-26, pieces 2023-24, distinct first authors, last ask,
editorial signal, status; plus coverage of the 605 open questions.
"""
import csv, sys, collections
q = {x['oq_id']: x for x in csv.DictReader(open('QUESTIONS.tsv'), delimiter='\t')
     if x['form'] != 'own_research_question'}
rows = list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
bad = [r['oq_id'] for r in rows if r['oq_id'] not in q]
seen = {r['oq_id'] for r in rows}
per = collections.Counter(r['oq_id'] for r in rows if r['role'] != 'residual')
print(f"rows {len(rows)}; unknown ids {len(bad)} {bad[:5]}; missing {len(set(q)-seen)} "
      f"{sorted(set(q)-seen)[:5]}; in >2 stacks {[k for k,v in per.items() if v>2]}")
S = collections.defaultdict(list)
for r in rows:
    if r['role'] != 'residual' and r['oq_id'] in q:
        S[r['stack_id']].append(q[r['oq_id']])
EDIT = {'cornelissen2024', 'hollerer2026'}
TOT = collections.Counter(x['key'] for x in q.values())
def core(m, yrs):
    c = collections.Counter(x['key'] for x in m if x['published_online'][:4] in yrs)
    return len([k for k, v in c.items() if v >= 3 or v * 2 >= TOT[k]])
out = []
for s, m in S.items():
    rec = {x['key'] for x in m if x['published_online'][:4] in ('2025', '2026')}
    old = {x['key'] for x in m if x['published_online'][:4] in ('2023', '2024')}
    fa = {x['apa_short'].split(',')[0].split(' ')[0] for x in m}
    last = max(x['published_online'] for x in m)
    st = []
    if len(rec) >= 3: st.append('prevailing')
    if rec and old: st.append('persistent')
    if not rec: st.append('fading')
    if rec and not old: st.append('new')
    out.append((len(rec), bool(rec and old), last, s, len(m), len(rec), len(old), len(fa), last, core(m,('2025','2026')), core(m,('2023','2024')), sum(x['published_online'][:4] in ('2025','2026') for x in m),
                'y' if (rec | old) & EDIT else 'n', '+'.join(st)))
out.sort(reverse=True)
print('stack\tn_oq\tpieces_25_26\tpieces_23_24\tfirst_authors\tlast_ask\tcore_25_26\tcore_23_24\tq_25_26\teditorial\tstatus')
for o in out: print('\t'.join(map(str, o[3:])))
