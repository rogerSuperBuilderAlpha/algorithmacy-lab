#!/bin/bash
# usage: linkcheck.sh URL -> prints: status<TAB>final_url<TAB>title<TAB>url
u="$1"
tmp=$(mktemp)
code=$(curl -sS -L -m 30 -A "Mozilla/5.0 (Macintosh) linkcheck" -o "$tmp" -w "%{http_code}\t%{url_effective}" "$u" 2>/dev/null) || code="ERR\t-"
title=$(tr '\n' ' ' < "$tmp" | grep -oiE '<title[^>]*>[^<]*' | head -1 | sed -E 's/<title[^>]*>//; s/[[:space:]]+/ /g')
printf "%s\t%s\t%s\n" "$code" "$title" "$u"
rm -f "$tmp"
