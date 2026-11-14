#!/bin/bash
# check that each docs.python.org page resolves and the named anchor id exists
cd "$(dirname "$0")/dl"
while read -r path anchor; do
  code=$(curl -sL -m 40 -o pg.html -w "%{http_code} %{url_effective}" "https://docs.python.org/$path")
  n=$(grep -c "id=\"$anchor\"" pg.html)
  echo "$code | anchor '$anchor' id-matches=$n | requested $path"
done <<LIST
3/library/stdtypes.html bitwise-operations-on-integer-types
3/library/sys.html sys.getsizeof
3/library/collections.html collections.deque
3.13/library/stdtypes.html bitwise-operations-on-integer-types
3.13/library/sys.html sys.getsizeof
3.13/library/collections.html collections.deque
LIST
