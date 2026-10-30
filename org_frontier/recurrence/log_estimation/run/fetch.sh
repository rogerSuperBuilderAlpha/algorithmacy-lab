#!/bin/bash
# Stream GH Archive hourly files, keep only events for the study repos, compact fields. No raw files stored.
# Window: 90 days 2024-04-01..2024-06-29 (2024 chosen: 2025-26 archive coverage is visibly degraded).
mkdir -p ev
one(){ h=$1; out=ev/$h.jsonl; [ -s $out.done ] && return
 curl -sf --retry 3 https://data.gharchive.org/$h.json.gz | zcat 2>/dev/null | grep -F -e '"kubernetes/kubernetes"' -e '"facebook/react"' -e '"microsoft/vscode"' -e '"django/django"' -e '"rust-lang/rust"' | python3 extract.py > $out && echo ok > $out.done; }
export -f one
for d in $(python3 -c "import datetime as D;s=D.date(2024,4,1);print(' '.join(str(s+D.timedelta(i)) for i in range(90)))"); do for H in $(seq 0 23); do echo $d-$H; done; done | xargs -P 8 -I{} bash -c 'one {}'
