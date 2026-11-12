#!/bin/zsh
# Rerun every check for classes 16-30. Outputs land next to this script as out_*.txt.
cd "$(dirname "$0")"
PY=/opt/homebrew/bin/python3.13
$PY parse_leetcode.py leetcode_raw search-in-a-binary-search-tree,validate-binary-search-tree,kth-largest-element-in-a-stream,top-k-frequent-elements,flood-fill,number-of-islands,find-if-path-exists-in-graph,rotting-oranges,course-schedule,course-schedule-ii,network-delay-time,path-with-minimum-effort,number-of-provinces,redundant-connection,implement-trie-prefix-tree,word-search-ii,subsets,n-queens,jump-game,candy,merge-intervals,the-skyline-problem,house-robber,coin-change,longest-increasing-subsequence,longest-common-subsequence,edit-distance,regular-expression-matching,word-ladder,find-median-from-data-stream > leetcode_statements.txt
$PY compare_key_sheet.py > out_compare_key_sheet.txt
$PY test_correctness_16_22.py > out_correctness_16_22.txt 2>&1
$PY test_correctness_23_30.py > out_correctness_23_30.txt 2>&1
$PY memory_measure.py > out_memory.txt 2>&1
$PY object_sizes.py > out_object_sizes.txt
$PY formula_recompute.py > out_formula_recompute.txt
$PY trie_layers.py > out_trie_layers.txt
$PY -u extra_checks.py > out_extra_checks.txt 2>&1
$PY bfs_frontier_check.py > out_bfs_frontier.txt
$PY check_212_unpruned.py > out_check_212_unpruned.txt
echo done
