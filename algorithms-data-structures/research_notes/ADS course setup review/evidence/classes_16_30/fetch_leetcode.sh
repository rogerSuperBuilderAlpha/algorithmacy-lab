#!/bin/zsh
# Fetch official LeetCode statements (content, examples, Python3 starter) for classes 16-30.
OUT=/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/leetcode_raw
for s in search-in-a-binary-search-tree validate-binary-search-tree kth-largest-element-in-a-stream top-k-frequent-elements flood-fill number-of-islands find-if-path-exists-in-graph rotting-oranges course-schedule course-schedule-ii network-delay-time path-with-minimum-effort number-of-provinces redundant-connection implement-trie-prefix-tree word-search-ii subsets n-queens jump-game candy merge-intervals the-skyline-problem house-robber coin-change longest-increasing-subsequence longest-common-subsequence edit-distance regular-expression-matching word-ladder find-median-from-data-stream; do
  curl -s -X POST https://leetcode.com/graphql -H 'Content-Type: application/json' -H 'Referer: https://leetcode.com' \
   -d "{\"query\":\"query q(\$s:String!){question(titleSlug:\$s){questionFrontendId title difficulty content exampleTestcases codeSnippets{langSlug code}}}\",\"variables\":{\"s\":\"$s\"}}" > "$OUT/$s.json"
  echo "$s $(wc -c < $OUT/$s.json)"
  sleep 1
done
