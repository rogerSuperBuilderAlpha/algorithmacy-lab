#!/bin/bash
# re-fetch suspiciously small hours with pipefail (fetch2.sh lacked it, so a failed curl could mark a partial hour done)
one(){ h=$1; set -o pipefail; tmp=ev2/$h.jsonl.tmp
 if curl -sf --retry 3 --max-time 400 https://data.gharchive.org/$h.json.gz | zcat | grep -F -e '"kubernetes/kubernetes"' -e '"facebook/react"' -e '"microsoft/vscode"' -e '"django/django"' -e '"rust-lang/rust"' | python3 extract2.py > $tmp || [ $? -eq 1 ]; then echo "$h $(wc -l < ev2/$h.jsonl) -> $(wc -l < $tmp)"; mv $tmp ev2/$h.jsonl; else echo "$h FAIL"; rm -f $tmp; fi; }
export -f one
for f in ev2/*.jsonl; do [ $(wc -l < $f) -le 5 ] && basename $f .jsonl; done | xargs -P 8 -I{} bash -c 'one {}'
