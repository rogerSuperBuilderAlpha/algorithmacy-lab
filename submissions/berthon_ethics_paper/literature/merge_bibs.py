"""Build literature/references.bib from the two arms' built bibs by a first-wins merge.

Adapted from berthon_ethics_course/literature/merge_bibs.py: same entry regex, DOI normalizer and
first-wins rule, but the inputs are whole bibs, read in the order given in INPUTS.

Run: python3 -I literature/merge_bibs.py          (writes references.bib, prints dropped entries)
     python3 -I literature/merge_bibs.py --check  (exits 1 if references.bib is stale)

algorithmacy_design_ethics has no .bib; its references are covered by its cards (CARD_INDEX.md).
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SUB = HERE.parent.parent
INPUTS = [
    ("berthon", SUB / "berthon_ethics_course/literature/references.bib"),
    ("part2", HERE / "dxd_part2/references.bib"),
]
ENTRY = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}', flags=re.S)
DOI = re.compile(r'\bdoi\s*=\s*[{"]\s*([^}"]+?)\s*[}"]', flags=re.I)


def norm_doi(body):
    m = DOI.search(body)
    if not m:
        return None
    d = m.group(1).strip().lower()
    return re.sub(r'^https?://(dx\.)?doi\.org/', '', d) or None


def merge():
    keys, dois, out, dropped, counts = {}, {}, [], [], []
    for label, path in INPUTS:
        chunk = []
        for m in ENTRY.finditer(path.read_text()):
            typ, key, body = m.groups()
            if typ.lower() in ('comment', 'string', 'preamble'):
                continue
            doi = norm_doi(body)
            if key in keys:
                dropped.append((key, label, key, keys[key], doi or '', 'same key'))
                continue
            if doi and doi in dois:
                k0, l0 = dois[doi]
                dropped.append((key, label, k0, l0, doi, 'same DOI'))
                continue
            keys[key] = label
            if doi:
                dois[doi] = (key, label)
            chunk.append(m.group(0))
        counts.append((label, len(chunk)))
        out.append(f'% from {label}: {path.relative_to(SUB)}\n' + '\n\n'.join(chunk))
    head = ('% Merged by literature/merge_bibs.py, first-wins in the order '
            + ', '.join(l for l, _ in counts) + '. Kept: '
            + '; '.join(f'{l} {n}' for l, n in counts) + f'. Total {len(keys)}.\n'
            '% Built file: the origin bibs are the record.\n\n')
    return head + '\n\n'.join(out) + '\n', dropped


def main():
    text, dropped = merge()
    target = HERE / 'references.bib'
    if '--check' in sys.argv:
        ok = target.exists() and target.read_text() == text
        print('references.bib is current' if ok else 'references.bib is stale')
        return 0 if ok else 1
    target.write_text(text)
    print('| dropped key | from | kept key | from | DOI | reason |\n|---|---|---|---|---|---|')
    for row in dropped:
        print('| ' + ' | '.join(row) + ' |')
    print(f'\n{len(dropped)} dropped')
    return 0


if __name__ == '__main__':
    sys.exit(main())
