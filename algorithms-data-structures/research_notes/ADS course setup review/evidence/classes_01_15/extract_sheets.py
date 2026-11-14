# Print, for classes 1-15 of the student sheets, the statement, example,
# starter signature and memory-estimate sentence with Markdown line numbers.
import re, sys
p = sys.argv[1]
lines = open(p).read().split('\n')
out = []
mode = None
for i, ln in enumerate(lines[:1570], 1):
    s = ln.strip()
    if not s or re.match(r'^-{5,}', s):
        continue
    if s.startswith('**#'):
        mode = 'stmt'; out.append(f'\n{i}: {s}'); continue
    if mode == 'stmt':
        if s.startswith('**Python solution'):
            mode = None; continue
        if s.startswith('**Easy') or s.startswith('**Medium') or s.startswith('[[http'):
            continue
        out.append(f'{i}: {s}')
    if s.startswith('Memory estimate, for'):
        mode = 'mem'; out.append(f'{i}: {s}'); continue
    if mode == 'mem':
        if s.startswith('|') or s.startswith('**Input') or s.startswith('**'):
            mode = None; continue
        out.append(f'{i}: {s}')
print('\n'.join(out))
