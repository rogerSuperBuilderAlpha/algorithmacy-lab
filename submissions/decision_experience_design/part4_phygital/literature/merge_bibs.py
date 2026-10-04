"""Build literature/references.bib from the facet .bib files by a first-wins merge.

Run: python3 literature/merge_bibs.py          (writes references.bib and prints the dropped entries)
     python3 literature/merge_bibs.py --check  (exits 1 if references.bib is not what the merge produces)

The facet .bib files are the record; references.bib is a built file. Facets are read in the order given
in ORDER. An entry is dropped when its key, or its normalised DOI, already appeared in an earlier facet.
Dropped entries go to stdout as a Markdown table for audit/BIB_CHANGES.md. The script never edits a facet file.
"""
import re
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ORDER = ["A", "B", "C", "D", "E", "F", "G", "X", "Z"]
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
    for letter in ORDER:
        files = sorted((HERE / 'facets').glob(f'{letter}_*.bib'))
        for f in files:
            kept = 0
            chunk = []
            for m in ENTRY.finditer(f.read_text()):
                typ, key, body = m.groups()
                if typ.lower() in ('comment', 'string', 'preamble'):
                    continue
                doi = norm_doi(body)
                if key in keys:
                    dropped.append((key, letter, key, keys[key], doi or '', 'same key'))
                    continue
                if doi and doi in dois:
                    k0, l0 = dois[doi]
                    dropped.append((key, letter, k0, l0, doi, 'same DOI'))
                    continue
                keys[key] = letter
                if doi:
                    dois[doi] = (key, letter)
                chunk.append(m.group(0))
                kept += 1
            counts.append((letter, f.name, kept))
            if chunk:
                out.append(f'% facet {letter}\n' + '\n\n'.join(chunk))
    order = ', '.join(l for l, _, _ in counts)
    tally = '; '.join(f'{l} {n}' for l, _, n in counts)
    head = (f'% Merged from literature/facets/*.bib by literature/merge_bibs.py, a first-wins merge in the order {order}.\n'
            f'% Entries kept per facet: {tally}. Total {len(keys)}.\n'
            '% Built file: the facet .bib files are the record. Dropped duplicates are listed in audit/BIB_CHANGES.md.\n\n')
    return head + '\n\n'.join(out) + '\n', dropped


if __name__ == '__main__':
    unknown = [a for a in sys.argv[1:] if a != '--check']
    if unknown:
        sys.exit(f'unknown argument {unknown}; the only option is --check')
    text, dropped = merge()
    target = HERE / 'references.bib'
    if '--check' in sys.argv:
        ok = target.exists() and target.read_text() == text
        print('references.bib is current' if ok else 'references.bib is STALE: rerun literature/merge_bibs.py')
        sys.exit(0 if ok else 1)
    target.write_text(text)
    print(f'wrote {target.name}: {text.count(chr(10) + "@") + text.startswith("@")} entries; {len(dropped)} dropped\n')
    if dropped:
        print('| dropped key (facet) | kept key (facet) | DOI | reason |\n| --- | --- | --- | --- |')
        for k, l, k0, l0, d, why in dropped:
            print(f'| `{k}` ({l}) | `{k0}` ({l0}) | {d} | {why} |')
