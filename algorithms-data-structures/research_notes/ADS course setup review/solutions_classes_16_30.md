# Instructor key, classes 16 to 30: every board solution run and checked

Scope: the 30 problems in classes 16 to 30 of `ADS_In_Class_Solutions.md` (key lines 2815–6025) and the matching student sheets in `ADS_In_Class_Board_Problems.md` (sheet lines 1570–3145). "Key L1234" and "sheet L1234" below are line numbers in those Markdown conversions.

What I did. I transcribed all 30 board solutions line for line into one module (the Markdown dropped indentation, so I restored it and changed nothing else), built LeetCode's `TreeNode`, and ran four kinds of check on CPython 3.13.12 (`/opt/homebrew/bin/python3.13`): every LeetCode example, hand-picked edge cases, random inputs against a brute-force reference I wrote independently of the key, and a run at LeetCode's size limits. 142,101 checks ran; all 142,101 passed. I then measured input and auxiliary memory with `tracemalloc` at the input size the key states, recomputed every memory formula from the course's own size table, and fetched the official statement, examples, constraints and Python3 starter for all 30 problems from LeetCode's GraphQL endpoint (12 Nov 2026).

Where to rerun. All code and outputs sit in `/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/` (called T below). `T/run_all.sh` reruns everything. The files that carry the evidence:

| File | What it holds |
|---|---|
| `T/board_solutions.py` | the 30 board solutions, with key line numbers |
| `T/test_correctness_16_22.py` → `T/out_correctness_16_22.txt` | classes 16–22: 54,057 checks, 0 failures |
| `T/test_correctness_23_30.py` → `T/out_correctness_23_30.txt` | classes 23–30: 88,044 checks, 0 failures |
| `T/memory_measure.py` → `T/out_memory.txt` | tracemalloc at the key's stated sizes |
| `T/formula_recompute.py` → `T/out_formula_recompute.txt` | key formula vs my formula vs measurement |
| `T/extra_checks.py` → `T/out_extra_checks.txt` | missing import, House Robber recurrence, heap-operation count, LCS and edit-distance statistics, Hard-problem timings, line counts |
| `T/object_sizes.py` → `T/out_object_sizes.txt` | per-object bytes, `sys.getsizeof` vs `tracemalloc` |
| `T/trie_layers.py` → `T/out_trie_layers.txt` | trie node counts for the #208/#212 scenario |
| `T/compare_key_sheet.py` → `T/out_compare_key_sheet.txt` | key vs student sheet, statement and example text |
| `T/bfs_frontier_check.py` → `T/out_bfs_frontier.txt` | BFS queue size on H-tree islands (#200's "other approaches" row) |
| `T/check_212_unpruned.py` → `T/out_check_212_unpruned.txt` | #212 with and without the dead-branch pruning |
| `T/leetcode_raw/*.json`, `T/leetcode_statements.txt` | fetched LeetCode data and its plain-text parse |

The key's opening claim (key L5–9) does not survive the test. Five board solutions call `deque` without importing it, so they raise `NameError` exactly as printed; several memory figures disagree with tracemalloc by 25–50% or rest on arithmetic that does not produce the printed number; two memory scenarios break LeetCode's constraints. The algorithms themselves are sound: every board solution returns correct results.

### Summary table

Memory column: key figure vs my tracemalloc measurement at the key's stated size (KiB/MiB; the key's "KB/MB" figures match binary units, for example 5,000 × 100 B printed as "488 KB"). "Pass" means every example, edge case, random comparison and limit-size run passed.

| Class | Slot | Problem (LeetCode level) | Correctness | Complexity | Memory (key vs measured) | Statement match | Verdict |
|---|---|---|---|---|---|---|---|
| 16 | A | #700 Search in a BST (Easy) | Pass | OK | input 488 KB vs 628 KiB (values above 256 uncounted, D18) | Match | Correct; minor (D17, D18) |
| 16 | B | #98 Validate BST (Medium) | Pass; RecursionError on a chain of 1,000+ nodes (D3) | OK | aux 2.1 KB est. (frames untraced); input low as #700 | Match, but example note misleads (D2) | Fix reasoning (D2, D3) |
| 17 | A | #703 Kth Largest in a Stream (Easy, design) | Pass; interface matches | OK | aux 88 KB vs 83.7 KiB; scenario breaks limits (D4) | Match | Fix scenario (D4, D17) |
| 17 | B | #347 Top K Frequent (Medium) | Pass | OK | aux 5.0 MB vs 7.50 MiB peak; scenario impossible (D5) | Match | Fix memory (D5) |
| 18 | A | #733 Flood Fill (Easy) | Pass | OK | aux 79 KB vs 77.2 KiB | Match (sheet typo D20) | No defect in key |
| 18 | B | #200 Number of Islands (Medium) | Pass | OK | aux 3.1 MB vs 3.17 MiB | Match (sheet typo D20) | No defect in key |
| 19 | A | #1971 Find if Path Exists (Easy) | Pass with import; NameError as printed (D1) | OK | aux 20.0 MB vs 22.44 MiB | Match | Add import (D1) |
| 19 | B | #994 Rotting Oranges (Medium) | Pass with import (D1) | OK | aux 1.9 KB vs 2.2 KiB | Match (sheet typo D20) | Add import (D1) |
| 20 | A | #207 Course Schedule (Medium) | Pass with import (D1) | OK | aux 259 KB vs 204.8 KiB (D6) | Match | Add import; fix memory (D1, D6) |
| 20 | B | #210 Course Schedule II (Medium) | Pass with import (D1) | OK | aux 276 KB vs 220.1 KiB (D6) | Match | Add import; fix memory (D1, D6) |
| 21 | A | #743 Network Delay Time (Medium) | Pass | OK | input 469 KB vs 521.4 KiB; formula label wrong (D7) | Match | Minor fix (D7) |
| 21 | B | #1631 Path With Minimum Effort (Medium) | Pass | OK | aux 98 KB vs 94.4 KiB | Match (sheet typo D20) | No defect in key |
| 22 | A | #547 Number of Provinces (Medium) | Pass | OK | input 325 KB vs 325.1 KiB; aux 1.8 KB vs 2.1 KiB | Match | No defect |
| 22 | B | #684 Redundant Connection (Medium) | Pass | OK | aux 35 KB vs 31.6 KiB | Match | No defect (trivial note in D19) |
| 23 | A | #208 Implement Trie (Medium, design) | Pass; interface matches | OK | aux 11.6 MB vs 10.36 MiB; count and arithmetic inconsistent (D8) | Match | Fix memory text (D8, D17) |
| 23 | B | #212 Word Search II (Hard) | Pass (as a set; D9) | OK | aux 11.6 MB vs 10.37 MiB (D8) | Match; example order differs from code's output (D9) | Minor fix (D8, D9) |
| 24 | A | #78 Subsets (Medium) | Pass | Aux headline O(n) breaks the course rule (D10) | aux 105 KB vs 105.3 KiB; input 416 B vs 136 B (D10) | Match | Fix aux label (D10) |
| 24 | B | #51 N-Queens (Hard) | Pass, n = 1..9 | Aux headline breaks the course rule (D11) | aux 51 KB vs 50.6 KiB | Match | Fix aux label (D11) |
| 25 | A | #55 Jump Game (Medium) | Pass | OK | input 78 KB vs 78.2 KiB | Match | No defect |
| 25 | B | #135 Candy (Hard) | Pass (exhaustive reference) | OK | aux 696 KB vs 773.7 KiB; "LeetCode limit" n = 20,000 is wrong (D12) | Match | Fix limit (D12) |
| 26 | A | #56 Merge Intervals (Medium) | Pass | OK | aux 869 KB vs 864.6 KiB | Match | No defect |
| 26 | B | #218 The Skyline Problem (Hard) | Pass | OK | aux 3.4 MB vs 3.38 MiB | Match | No defect |
| 27 | A | #198 House Robber (Medium) | Pass | OK | input 3.6 KB vs 4.0 KiB | Match | Fix reasoning (D13) |
| 27 | B | #322 Coin Change (Medium) | Pass | OK | aux 316 KB vs 351.1 KiB; input 164 B vs 88 B (D14) | Match | Minor (D14) |
| 28 | A | #300 Longest Increasing Subsequence (Medium) | Pass | OK | aux 81 KB vs 90.1 KiB (int size, D19) | Match | No defect |
| 28 | B | #1143 Longest Common Subsequence (Medium) | Pass | OK | aux 8.1 MB vs 7.79 MiB; "LCS about 400" wrong (D15) | Match | Minor (D15) |
| 29 | A | #72 Edit Distance (Medium) | Pass | OK | aux 6.3 MB vs 6.67 MiB | Match | No defect (trivial note D21) |
| 29 | B | #10 Regular Expression Matching (Hard) | Pass (20,000 random vs `re.fullmatch`) | OK | aux 4.9 KB vs 5.1 KiB | Match | No defect |
| 30 | A | #127 Word Ladder (Hard) | Pass with import (D1) | OK | aux 507 KB vs 483.3 KiB | Match | Add import (D1) |
| 30 | B | #295 Find Median from Data Stream (Hard, design) | Pass; interface matches | Big-O OK; "three heap operations" is five (D16) | aux 1.8 MB vs 1.94 MiB | Match | Minor fix (D16, D17) |

Problems with no defect in the key: #733, #200, #1631, #547, #684, #55, #56, #218, #300, #72, #10. For #733, #200 and #1631 the only issue is a typo on the student sheet (D20).

### Defect list

Each entry gives the line, what the key says, what is correct, and the evidence. D1–D17 are defects in the key; D18–D21 are small or cross-cutting.

**D1. Missing `from collections import deque` (five problems).** Key L3426 (#1971), L3532 (#994), L3659 (#207), L3772 (#210), L5837 (#127) call `deque(...)`. The key prints `import heapq` above its heap solutions (L2995, L3081, L3873, L3991, L5100, L5947) but never imports `deque` anywhere in the file; a grep for `from collections` returns nothing. As printed, the code fails: `T/extra_checks.py` runs the #1971 board text in a fresh namespace and prints `NameError: name 'deque' is not defined`. Correct: add `from collections import deque` to each of the five board solutions. With the import added, all five pass every test.

**D2. #98: the example does not show the mistake the reasoning says it shows.** Key L2908–2909 annotates `[5, 1, 4, null, null, 3, 6] -> False` with "(3 is in the right subtree of 5 but is smaller than 5)", and step 1 (L2931–2933) says "each child looks fine, but 3 sits to the right of 5". Not so: the right child 4 is already smaller than 5. LeetCode's own explanation names that pair: "The root node's value is 5 but its right child's value is 4." The "children only" check the key warns against returns False on this tree (`T/out_correctness_16_22.txt`: `children-only check on key's example [5,1,4,null,null,3,6]: False`). Correct: illustrate the mistake with a tree such as `[5, 4, 6, null, null, 3, 7]`, where every parent–child pair is ordered but 3 sits right of 5; the children-only check wrongly returns True there (`... on [5,4,6,null,null,3,7]: True`), and the board solution returns False (test `98 deep violation` passes). Sheet L1636–1637 repeats the annotation.

**D3. #98: recursion depth at LeetCode's limits is not mentioned.** Key L2947–2958 gives O(h) space and a balanced-tree memory case, and never warns that h can reach n. LeetCode allows up to 10^4 nodes. With CPython's default limit (`sys.getrecursionlimit() = 1000`) the board solution fails on a right-leaning chain: `right chain of 900 nodes: returned True`, `right chain of 1000 nodes: RecursionError`, `right chain of 10000 nodes: RecursionError` (`T/out_correctness_16_22.txt`). The key makes exactly this point for #700 (L2863–2864) and #733 (L3226). Correct: add the caveat and offer an iterative in-order traversal as the alternative.

**D4. #703: the memory scenario breaks LeetCode's constraints.** Key L3048–3052 (sheet L1709–1710): "k = 10,000 (the LeetCode limit) with a stream of 100,000 distinct ints above 256". LeetCode allows `nums.length <= 10^4`, at most 10^4 calls to `add`, and values in [-10^4, 10^4], so a stream holds at most 20,000 values and at most 9,744 distinct ints above 256. The auxiliary figure survives because the heap never exceeds k: measured 83.7 KiB in the key's scenario and 83.6 KiB at LeetCode's real limits (`T/out_memory.txt`, `T/out_extra_checks.txt`), against the key's 88 KB. The input figure (2.7 MB) describes an impossible input. Correct: use 20,000 values in range.

**D5. #347: impossible scenario and missed resize peak.** Key L3135–3138 and L3145 (sheet L1760–1761): "n = 100,000 values, all distinct (d = n), and k = 100", auxiliary 5.0 MB. Two problems. (a) LeetCode bounds values to [-10^4, 10^4], so d ≤ 20,001, and with every count equal to 1 the guarantee "the answer is unique" fails for k = 100. (b) The key's own rule (L61–62: "A set or dict grows by resizing, so its peak can be about 1.5 times its final size") is not applied: tracemalloc measures a 7.50 MiB peak against the printed 5.0 MB (`T/out_memory.txt`). Recomputed with the 1.5× rule: 7.45 MiB (`T/out_formula_recompute.txt`). At LeetCode's real limits (n = 10^5 values in range) the peak is 864.2 KiB.

**D6. #207 and #210: auxiliary memory counts ints that are never created.** Key L3716–3717 and L3725–3726: "The index ints from range are new 28-byte ints above 256 … ints about 28V"; L3838–3839 repeats "ints 28V". None of these ints survive: the adjacency lists hold the course ints taken from `prerequisites`, `indegree` holds the cached 0 and 1, and the queue holds ints from the input. Measured auxiliary: 204.8 KiB (#207) and 220.1 KiB (#210), against the printed 259 KB and 276 KB. Dropping the 28V term gives 204.0 KiB and 221.6 KiB, within 1% of measurement (`T/out_memory.txt`, `T/out_formula_recompute.txt`).

**D7. #743: input formula labelled with a tuple's size.** Key L3954: "times: E triples of (64 + 8) bytes … 469 KB". Each `times[i]` is a list of three ints, which costs 56 + 3 × 8 = 80 B; 64 B is a 3-tuple. The printed formula gives 6,000 × 72 = 421.9 KiB, not 469; 469 KiB equals 6,000 × 80 B alone and leaves out the outer list. Measured: 521.4 KiB. Corrected formula: 6,000 × 80 + 56 + 8 × 6,000 = 515.7 KiB (`T/out_formula_recompute.txt`). The auxiliary row (590 KB vs 572.0 KiB) holds, and the assumed heap peak of "about half the edges" holds too (measured 2,847 of 6,000).

**D8. #208 and #212: trie node count and arithmetic do not produce the printed figure.** Key L4413–4416 (and L4545–4546 for #212): "the sum over depths d = 1..8 of min(26^d, 10,000) (the layers fill up after depth 3), roughly 53,000 nodes at about 200 bytes each", printed as 11.6 MB (L4423, L4556). Three numbers disagree with each other. The stated formula evaluates to 60,702, not 53,000. And 53,000 × 200 B is 10.1 MiB, not 11.6. The depth-3 layer holds about 7,630 nodes, not 10,000 (layers fill at depths 5–8). Over five seeds the trie has 58,192–58,268 nodes (`T/out_trie_layers.txt`); tracemalloc measures 10.36 MiB for #208 and 10.37 MiB for #212 (`T/out_memory.txt`). The printed 11.6 MB is 12% above measurement, inside the key's own 30% grading band, but no line of the key's derivation yields it. Correct: about 58,200 nodes × about 187 B (10.36 MiB ÷ 58,247 nodes measured) ≈ 10.4 MiB.

**D9. #212: the example output order differs from the board code's.** Key L4444 shows `-> ["eat", "oath"]` (LeetCode's example order). The board solution returns `['oath', 'eat']` (`T/out_correctness_23_30.txt`), because the scan reaches the "o" at (0, 0) first. The fetched LeetCode statement does not say "in any order" for #212, unlike #78 and #51. Correct: state that the order of the result does not matter, so a student comparing their trace with the key does not mark a correct answer wrong. (Whether LeetCode's judge sorts the output is in Gaps.)

**D10. #78: auxiliary headline contradicts the course rule; input over-counted.** Key L4633–4634 gives auxiliary space as "O(n) for the recursion and path (the output itself is O(n x 2^n))". The course rule (key L18–19; syllabus L160–162: "Anything you build and return counts") makes the auxiliary space O(n × 2^n), and the key's own memory table counts the output (L4647–4648). Separately, L4653 prices the input at "list of 10 ints 416 bytes", but LeetCode bounds `nums[i]` to [-10, 10], all cached small ints: 56 + 80 = 136 B, which tracemalloc confirms (`T/out_memory.txt`: input 136 B). The 105 KB auxiliary figure is right (measured 105.3 KiB).

**D11. #51: auxiliary headline contradicts the course rule; frame size off-table.** Key L4764–4765: "O(n) for the search; O(n^2) per solution for the output". Under the course rule the auxiliary space is O(S × n²), where S is the number of solutions (92 at n = 8, 352 at n = 9; `T/out_correctness_23_30.txt`). L4779 and L4787 price frames at 200 B, while the course table says 150 B (key L56; syllabus L211–212). The difference is 400 B and the 51 KB figure stands (measured 50.6 KiB).

**D12. #135: wrong "LeetCode limit".** Key L4962 (sheet L2606): "n = 20,000 children (the LeetCode limit)". LeetCode's constraints read `1 <= n == ratings.length <= 5 * 10^4` and `0 <= ratings[i] <= 5 * 10^4`. The formula is right for n = 20,000 (696.2 KiB), but at the real limit the auxiliary is 1.71 MiB by the course table and 1.90 MiB measured (`T/out_formula_recompute.txt`, `T/out_memory.txt`). Correct: n = 50,000, or drop "(the LeetCode limit)".

**D13. #198: the recurrence in the reasoning is off by one.** Key L5239–5245 defines `best[i]` as "the most money from the first i houses", sets `best[1] = nums[0]`, and then writes `best[i] = max(best[i - 1], best[i - 2] + nums[i])`. With that definition, house i is `nums[i - 1]`. Implemented literally, the stated recurrence raises `IndexError` on both LeetCode examples (`T/out_extra_checks.txt`: `[1, 2, 3, 1] -> IndexError`, `[2, 7, 9, 3, 1] -> IndexError`); with `nums[i - 1]` it returns 4 and 12. The board code (two variables) is correct; only the explanation is wrong.

**D14. #322: input counts cached ints.** Key L5371: "3 coins: list of 3 … 164 bytes" adds three 28-B ints, but 1, 2 and 5 are cached small ints (syllabus L182–183). Correct: 80 B by the table; tracemalloc shows 88 B. Trivial; the 316 KB auxiliary formula is right.

**D15. #1143: the LCS length for random strings is about 317, not 400.** Key L5560–5562: "for random strings of 1,000 letters the LCS is about 400, so the few matching cells with counts above 256 add about 0.4 MB". Over ten random pairs the LCS is 310–330, mean 317.5, and the table holds only 2,180–3,347 distinct ints above 256, about 0.1 MB (`T/out_extra_checks.txt`). The total survives (8.1 MB printed vs 7.79 MiB measured, −4%), but the stated reason does not.

**D16. #295: addNum does up to five heap operations, not three.** Key L6006–6007: "addNum does at most three heap operations". The code always does push, pop, push and, when it rebalances, a further pop and push. An instrumented run counts `[5, 3, 5, 3, 5, 3, 5]` operations over seven calls (`T/out_extra_checks.txt`). O(log n) per call is unaffected.

**D17. No "Other approaches" table for five problems.** The other 25 problems in scope each end on such a table; #700 (key L2819–2893), #98 (L2898–2975), #703 (L2980–3063), #208 (L4317–4427) and #295 (L5933–6025) end at the memory table. A grep of the key's headings and table titles confirms the gap.

**D18. #700 and #98: TreeNode values above 256 are not counted.** Key L2881–2887 and L2962–2968 price a node at "about 100 bytes". A `TreeNode` with a cached value measures 95.8 B under tracemalloc, but LeetCode's values run to 10^7 (#700) and ±2^31 (#98), and such a node measures 127.5 B with its int (`T/out_object_sizes.txt`). Measured inputs: 628.1 KiB vs 488 KB (#700) and 1.22 MiB vs 977 KB (#98). The figure is 22% low, inside the key's 30% band; state the assumption (small values) or add 28 B per node.

**D19. Cross-cutting: tracemalloc charges 32 B per int, the table says 28 B.** On CPython 3.13.12 a non-cached int reports 28 B from `sys.getsizeof` but costs 32 B under tracemalloc: #135's input `list(range(20000))` measures 773.3 KiB, which equals 160,056 + 19,744 × 32 B exactly, while the table's 28 B gives 703 KiB (`T/out_memory.txt`; `T/out_object_sizes.txt` shows 31.5 B average over 10,000 ints, a few of them cached). Every int-heavy estimate therefore sits about 10% below tracemalloc: #135 (696 KB vs 773.7 KiB), #300 (81 KB vs 90.1 KiB), #322 (316 KB vs 351.1 KiB), #295 (1.8 MB vs 1.94 MiB), #198. All stay inside the 30% band, so the grading rule absorbs it, but the key's statement that every figure "was checked against tracemalloc" cannot be literally true. The fix belongs in the syllabus table (syllabus L180–181), outside this scope. #684 shows the opposite small error: L4289–4290 and L4298 count 28n new ints from `list(range(...))`, but only 744 of the 1,001 exceed 256 (31.6 KiB measured vs 35 KB).

**D20. Student sheets: a stray capital "A".** Sheet L1814 ("for A 50 x 50 grid"), L1867 ("for A 300 x 300 grid"), L1974 ("for A 10 x 10 grid") and L2184 ("for A 100 x 100 grid") paste the key's sentence-initial "A" into mid-sentence. Typo only. Every other statement and example on the sheets matches the key word for word (`T/out_compare_key_sheet.txt`: 30 of 30 identical).

**D21. #72: "the distance is about 400".** Key L5670. Three random 500-letter pairs give 441, 445 and 446. The load-bearing claim on the same line, that about two thirds of the cells hold a new int above 256, holds: 63.9–64.1% (`T/out_extra_checks.txt`). Trivial.

## Do the board solutions return correct results, and would they pass LeetCode's constraints in Python?

### Takeaway
Every one of the 30 board solutions is correct: 142,101 checks on examples, edge cases and random inputs against independent brute-force references passed with no failure. Two caveats apply. Five solutions need a missing `deque` import to run (D1), and #98's recursion fails on deep chains that LeetCode's constraints allow (D3). At LeetCode's size limits most solutions ran in under 0.7 s on this machine; the slowest legal runs were #212 on an all-"a" board (1.1 s) and #208 under an adversarial load (5.9 s).

### Cited Findings
- Classes 16–22: 54,057 checks, 0 failures; classes 23–30: 88,044 checks, 0 failures — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt); [out_correctness_23_30.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_23_30.txt)
- The references I compared against, one per problem: node scan (#700); in-order strictly-increasing test on random trees, including duplicates and ±2^31 values (#98); sort the whole stream after each add (#703); `Counter.most_common`, keeping only inputs with a unique answer (#347); BFS with a visited set (#733); union-find (#200); Floyd–Warshall reachability (#1971); minute-by-minute simulation (#994); every permutation of courses (#207, #210, with each returned order validated); Bellman–Ford, with zero weights included (#743); threshold-by-threshold reachability (#1631); DFS components (#547); remove each edge from the back and test for a tree (#684); a Python set of words (#208); Word Search I per word (#212); `itertools.combinations` (#78); every permutation with a diagonal test, n = 1..9 (#51); forward reachability DP (#55); exhaustive search over every candy assignment, n ≤ 6 (#135); coverage of doubled coordinates (#56); maximum height at every critical x (#218); every non-adjacent subset (#198); BFS over amounts (#322); every subsequence (#300, #1143); BFS over edit operations on strings (#72); `re.fullmatch` on 20,000 random pattern pairs (#10); BFS on an explicitly built word graph (#127); a sorted list (#295) — [test_correctness_16_22.py](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/test_correctness_16_22.py); [test_correctness_23_30.py](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/test_correctness_23_30.py)
- Edge cases that passed include a single node or cell, empty `nums` with k = 1 (#703), `old == color` (#733), diagonal-only land (#200), `source == destination` (#1971), a grid with no fresh oranges and one with only fresh (#994), a self-loop and a 3-cycle (#207, #210), unreachable nodes and zero-weight edges (#743), a 1 × 1 grid (#1631), n = 1 to 9 for N-Queens, `[0]` (#55), all-equal ratings (#135), `[[1,2],[3,4]]`, which must not merge, and an unchanged input list (#56), equal left edges and coordinates up to 2^31 − 1 (#218), the greedy trap `[1,3,4], 6` and a coin of 2^31 − 1 (#322), both strings empty (#72), and `"mississippi"` / `"mis*is*p*."` (#10) — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt); [out_correctness_23_30.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_23_30.txt)
- Running the #1971 board text without an import raises `NameError: name 'deque' is not defined` (D1) — [out_extra_checks.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_extra_checks.txt)
- #98 raises `RecursionError` on right-leaning chains of 1,000 and 10,000 nodes; LeetCode allows "[1, 10^4]" nodes (D3) — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt); [LeetCode #98](https://leetcode.com/problems/validate-binary-search-tree/)
- Other recursive solutions stay shallow at LeetCode's limits: #212 recurses at most word-length deep (≤ 10), #78 at most n + 1 = 11, #51 at most n + 1 = 10 — [LeetCode #212](https://leetcode.com/problems/word-search-ii/); [LeetCode #78](https://leetcode.com/problems/subsets/); [LeetCode #51](https://leetcode.com/problems/n-queens/)
- Times at LeetCode's limits (this Mac, CPython 3.13.12): #700 5,000-node chain 0.55 ms; #703 k = 10^4 with 10^4 adds 27.5 ms; #347 n = 10^5 102 ms; #733 50 × 50 8 ms; #200 300 × 300 all land 192 ms; #1971 n = 2 × 10^5 path 360 ms; #207 + #210 V = 2,000 4.2 ms; #743 E = 6,000 11 ms; #1631 100 × 100 random 53 ms; #51 n = 9 16 ms; #135 n = 5 × 10^4 17 ms; #218 n = 10^4 39 ms; #322 12 coins × 10^4 34 ms; #300 n = 2,500 689 ms; #1143 1,000 × 1,000 334 ms; #72 500 × 500 110 ms; #127 3,125 connected words 273 ms; #295 5 × 10^4 calls 88 ms; #212 on a 12 × 12 board of "a" with 25 deep words 1.1 s, and with 30,000 words 0.5 s — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt); [out_correctness_23_30.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_23_30.txt); [out_extra_checks.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_extra_checks.txt)
- #208 under an adversarial but legal load (3 × 10^4 calls, each on a 2,000-letter word) takes 5.9 s, which is the O(total characters) cost any trie pays in Python, not a defect of this board solution — [out_correctness_23_30.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_23_30.txt); [LeetCode #208](https://leetcode.com/problems/implement-trie-prefix-tree/)

### Inferences
- I infer that the key's authors ran these solutions with a `deque` import (or inside LeetCode) that never made it onto the page; the algorithms pass, and only the printed text fails.
- After #208's adversarial case, the slowest legal runs are #212's all-"a" board (1.1 s) and #300 at n = 2,500 (689 ms). For #300 the key already lists the O(n log n) alternative, which a student should meet if the judge rejects O(n²) in Python.

### Gaps
- I did not submit to LeetCode. Its Python time limits, whether its judge raises Python's recursion limit (which decides whether #98 fails on a 10^4-node chain there), and whether its Python environment pre-imports `collections` were not verifiable from the fetched problem data.

## Do the statement, example and starter signature match LeetCode?

### Takeaway
All 30 statements, examples and starter names match LeetCode in substance, and all 30 difficulty labels match. The course drops LeetCode's `class Solution` wrapper and uses plain functions with the same names and parameter order; the three design problems keep LeetCode's class interface. Two memory scenarios and one stated limit contradict LeetCode's constraints (D4, D5, D12), and one example annotation misleads (D2).

### Cited Findings
- I fetched statement, examples, constraints and Python3 starter for all 30 slugs via the GraphQL endpoint; difficulties: Easy #700, #703, #733, #1971; Hard #212, #51, #135, #218, #10, #127, #295; Medium for the other 19, matching every label in the key — [leetcode_statements.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/leetcode_statements.txt); [LeetCode GraphQL](https://leetcode.com/graphql)
- Function names and parameter order on the sheets (sheet L1586–L3115) match LeetCode's Python3 starters, for example `networkDelayTime(self, times, n, k)`, `coinChange(self, coins, amount)`, `ladderLength(self, beginWord, endWord, wordList)`; LeetCode wraps each in `class Solution` — [leetcode_statements.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/leetcode_statements.txt)
- Design interfaces match: `KthLargest(k, nums)` / `add(val)` ([LeetCode #703](https://leetcode.com/problems/kth-largest-element-in-a-stream/)); `Trie()` / `insert` / `search` / `startsWith` ([LeetCode #208](https://leetcode.com/problems/implement-trie-prefix-tree/); the key adds a private helper `walk`, which LeetCode permits); `MedianFinder()` / `addNum` / `findMedian` ([LeetCode #295](https://leetcode.com/problems/find-median-from-data-stream/)). The key's sequences reproduce LeetCode's example outputs, and both #703 examples pass — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt)
- The key and the student sheets carry identical statement and example text for all 30 problems — [out_compare_key_sheet.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_compare_key_sheet.txt)
- Constraint mismatches: #135 allows n ≤ 5 × 10^4, not 20,000 (D12) — [LeetCode #135](https://leetcode.com/problems/candy/); #703 bounds values to [-10^4, 10^4] with ≤ 10^4 initial values and ≤ 10^4 adds (D4) — [LeetCode #703](https://leetcode.com/problems/kth-largest-element-in-a-stream/); #347 bounds values to [-10^4, 10^4] and guarantees a unique answer (D5) — [LeetCode #347](https://leetcode.com/problems/top-k-frequent-elements/)
- LeetCode's #98 example 2 explanation: "The root node's value is 5 but its right child's value is 4" (D2) — [LeetCode #98](https://leetcode.com/problems/validate-binary-search-tree/)
- Harmless omissions: #743 allows zero weights (`0 <= wi <= 100`), and the board code handles them (test `743 zero weights` passes); #218 guarantees `buildings` sorted by left, which the board code does not rely on; #127's "beginWord does not need to be in wordList" is implied by the key's wording — [LeetCode #743](https://leetcode.com/problems/network-delay-time/); [LeetCode #218](https://leetcode.com/problems/the-skyline-problem/); [LeetCode #127](https://leetcode.com/problems/word-ladder/)
- LeetCode says "any order" for #78, #51 and #347 and "any of them" for #210, but not for #212 (D9) — [leetcode_statements.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/leetcode_statements.txt)

### Inferences
- No simplification in the key changes what the problem asks. The plain-function form changes only the call syntax.

### Gaps
- I did not compare the course's example selections against LeetCode beyond the examples the key prints; the key omits some of LeetCode's examples (for instance #200 example 1, #1631 examples 2–3), and my tests ran those too.

## Are the stated time and auxiliary space correct?

### Takeaway
Every stated Big-O time is correct, and so is every auxiliary space that follows the course's own rule. Two headlines break that rule by leaving the output out (#78, #51; D10, D11), and one sentence miscounts heap operations without changing the Big-O (#295; D16).

### Cited Findings
- The course rule: "Auxiliary space is the extra memory beyond the input, including anything that is built and returned" (key L18–19); the syllabus says "Anything you build and return counts" (syllabus L160–162). #78 states O(n) and #51 states O(n), each with the output set aside in parentheses (key L4633–4634, L4764–4765) — [ADS_In_Class_Solutions.md](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_In_Class_Solutions.md); [ADS_Syllabus_Draft.md](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_Syllabus_Draft.md)
- Instrumented #295: 3 or 5 heap operations per `addNum` (D16) — [out_extra_checks.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_extra_checks.txt)
- Hidden costs the key does account for: the recursion stack (#98 O(h), #212 O(L)), the visited mark folded into the grid (#733, #200), the heap holding up to E entries (#743), the event list and heap (#218), the dp tables (#1143, #72, #10), and the O(L) string build per candidate (#127's O(N × L² × 26)). Measured heap behaviour fits the stated bounds: in #1631, random heights give 14,905 pushes on 10,000 cells (below the key's bound of 4 per cell) with a peak of 5,372 entries; #743 gives 3,004 pushes for 6,000 edges — [out_memory.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_memory.txt)
- In #98 the worst case is a chain, where h = n; the key's "as deep as the tree is tall" is right, but the RecursionError it implies goes unmentioned (D3) — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt)

### Inferences
- #212's auxiliary bound omits the `found` list (O(W) words); it is small next to the trie, so I do not count it as a defect.

### Gaps
- None for Big-O beyond D3's judge-dependent behaviour.

## Are the memory estimates right?

### Takeaway
Tracemalloc can see 29 of the 30 auxiliary figures (#98's is recursion frames only), and 24 of those 29 fall within 15% of measurement. The misses are #347 (5.0 MB printed vs a 7.50 MiB peak, −33%), #207 and #210 (+26% and +25%, from ints that never exist), and two figures under 300 B (#55, #198), where a few bytes swing the ratio. The input side has its own misses: #700 and #98 leave node values uncounted (−22%), #78 and #322 count cached ints, and #703, #347 and #135 rest on scenarios outside LeetCode's constraints. #208/#212 land within 12%, but no line of the stated derivation produces the printed figure. A systematic 32-vs-28 B int gap explains the remaining int-heavy differences of about 10%.

### Cited Findings
- Key figure, key formula re-evaluated, my formula and measurement, side by side — [out_formula_recompute.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_formula_recompute.txt); [out_memory.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_memory.txt). Auxiliary (or input where noted), key → my formula → measured:
  - #700 input 488 KB → 625.0 KiB → 628.1 KiB (D18); #98 aux 2.1 KB → 2.1 KiB → 384 B traced (recursion frames do not appear in tracemalloc, as key L62 says)
  - #703 aux 88 KB → 87.9 KiB → 83.7 KiB (scenario D4); #347 aux 5.0 MB → 7.45 MiB → 7.50 MiB (D5)
  - #733 aux 79 KB → 78.1 KiB → 77.2 KiB (peak stack 1,226 of 2,500 cells from a corner, so "about half" holds); #200 aux 3.1 MB → 3.09 MiB → 3.17 MiB (peak stack 44,851 of 90,000)
  - #1971 aux 20.0 MB → 20.03 MiB → 22.44 MiB; #994 aux 1.9 KB → 1.4 KiB → 2.2 KiB (`sys.getsizeof(deque()) = 760`, confirming the key's 760 B)
  - #207 aux 259 KB → 204.0 KiB → 204.8 KiB; #210 aux 276 KB → 221.6 KiB → 220.1 KiB (D6)
  - #743 input 469 KB → 515.7 KiB → 521.4 KiB (D7); aux 590 KB vs 572.0 KiB measured
  - #1631 aux 98 KB → 91.5 KiB → 94.4 KiB (heap peak 100 entries in the flat case; key assumed about 200)
  - #547 aux 1.8 KB → 2.1 KiB measured; #684 aux 35 KB → 28.2 KiB → 31.6 KiB
  - #208 aux 11.6 MB → 10.22 MiB → 10.36 MiB; #212 → 10.37 MiB (D8)
  - #78 aux 105 KB → 105.0 KiB → 105.3 KiB; #51 aux 51 KB → 50.1 KiB → 50.6 KiB
  - #55 aux 200 B → 300 B measured; #135 aux 696 KB → 773.7 KiB measured at n = 20,000, 1.90 MiB at n = 50,000 (D12)
  - #56 aux 869 KB → 869.2 KiB → 864.6 KiB; #218 aux 3.4 MB → 3.40 MiB → 3.38 MiB (10,001 key points on the key's rising-and-nested case)
  - #198 aux 150 B → 232 B measured; #322 aux 316 KB → 316.1 KiB → 351.1 KiB
  - #300 aux 81 KB → 80.9 KiB → 90.1 KiB; #1143 aux 8.1 MB → 7.79 MiB → 7.79 MiB (D15)
  - #72 aux 6.3 MB → 6.67 MiB (with 32-B ints) → 6.67 MiB; #10 aux 4.9 KB → 4.8 KiB → 5.1 KiB
  - #127 aux 507 KB → 506.6 KiB → 483.3 KiB; #295 aux 1.8 MB → 1.76 MiB → 1.94 MiB
- Per-object costs on CPython 3.13.12: int above 256 is 28 B by `sys.getsizeof` but about 32 B under tracemalloc; TreeNode 95.8 B with a cached value and 127.5 B with its own int; an 8-character str 49 B; a list literal of three variables 80 B; `{}` 64 B, a one-key dict 184 B, a six-key dict 272 B (the key's "184" and "about 270" hold) — [out_object_sizes.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_object_sizes.txt); [out_memory.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_memory.txt)
- The trie for 10,000 random 8-letter words has per-depth node counts [26, 676, ~7,630, ~9,890, ~9,995, 10,000, 10,000, 10,000], 58,192–58,268 in total over five seeds, against the key's "roughly 53,000" and its formula's 60,702 — [out_trie_layers.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_trie_layers.txt)

### Inferences
- The figures that match tracemalloc to within a few percent (#733, #200, #56, #218, #78, #51, #127) suggest the authors did measure some cases. The figures that miss by 25–50% (#347, #207, #210) and the #208 arithmetic suggest other figures were derived and never checked, contrary to key L7–9.
- My measured inputs depend on how I built them. In #218 my 10,000 buildings share one right-edge int, so my input (1.45 MiB) undercounts the key's three-ints-per-building input (1.6 MB); the key's formula is the better figure there.

### Gaps
- Recursion frames are invisible to tracemalloc, so I could not check the 150 B per frame figure (#98, #51); the key says as much at L62.

## Are the step-by-step reasoning and the "other approaches" tables correct?

### Takeaway
The reasoning is correct for 27 of 30 problems. #98 illustrates its key point with a tree that does not show it (D2), #198 states an off-by-one recurrence (D13), and #295 miscounts heap operations (D16). Every "other approaches" row I checked is correct, but five problems have no such table (D17).

### Cited Findings
- #98 children-only check returns False on the key's example and True on `[5,4,6,null,null,3,7]` (D2) — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt)
- #198's stated recurrence raises IndexError on both examples; the corrected one returns 4 and 12 (D13) — [out_extra_checks.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_extra_checks.txt)
- Claims inside the reasoning that I checked by running them: #322's greedy counterexample (`[1, 3, 4]`, amount 6 → 2 coins) holds; #684's "the first edge that closes a cycle is the last removable edge in the input" holds on 3,000 random graphs; #218's event ordering (taller starts first, ends after starts at the same x) holds on 5,000 random skylines, including shared edges; #10's three DP rules agree with `re.fullmatch` on 20,000 random pairs — [out_correctness_16_22.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_16_22.txt); [out_correctness_23_30.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_correctness_23_30.txt)
- #72's claim that about two thirds of cells hold a new int above 256 holds (63.9–64.1%) — [out_extra_checks.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_extra_checks.txt)
- Missing tables: #700, #98, #703, #208, #295; present for the other 25 in scope — [ADS_In_Class_Solutions.md](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_In_Class_Solutions.md)
- #200's table gives BFS an O(min(m, n)) queue (key L3389). On H-tree-shaped islands, a BFS started where `numIslands` would start peaks at 0.97, 1.02, 1.21, 1.25 and 1.45 × min(m, n) for grids of side 33, 65, 129, 257 and 513 — [out_bfs_frontier.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_bfs_frontier.txt)

### Inferences
- The rising ratio for #200's BFS suggests O(min(m, n)) is the typical case, not a worst-case bound, but my probe does not prove that, and within LeetCode's 300 × 300 the queue stayed under 1.25 × min(m, n). I do not count it as a defect.
- #51's row "Check the whole board for attacks after each placement: O(n × n!)" is right if the check scans one row, column and two diagonals (O(n)); scanning the whole n × n board would make it O(n² × n!). The wording is loose, not wrong.

### Gaps
- I checked the alternatives' Big-O claims by reasoning, not by implementing each alternative; the run-based evidence covers the board solutions and the claims listed above.

## Can a student write the Hard board solutions by hand in one class session?

### Takeaway
Judgment: #127, #295, #135 and #51 are writable in one session by a prepared student. #10 and #212 are writable but error-prone. #218 is the one I would expect most students to get wrong at the board without a hint, because its correctness rests on details the code does not show.

### Cited Findings
- Line counts of the board solutions (non-blank lines, function or class only; add one import line where noted): #212 Word Search II 29; #51 N-Queens 24; #218 Skyline 17 (+ `import heapq`); #10 Regex 17; #127 Word Ladder 17 (+ the missing `deque` import); #295 MedianFinder 13 (+ `import heapq`); #135 Candy 10. For scale, the Medium solutions in scope run 6–22 lines — [out_extra_checks.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_extra_checks.txt)
- The course announces each class's pattern in advance through the take-home, gives two problems per class with no lecturing, and requires time, auxiliary space and a memory estimate for each solution; the syllabus draft states no session length — [ADS_Syllabus_Draft.md](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_Syllabus_Draft.md) (L100–140)

### Inferences
These are my judgments, not measurements.
- #127 Word Ladder (17 lines): plain BFS with on-demand neighbours. LeetCode rates it Hard, but in the capstone it is the easiest of the Hards. Writable.
- #295 Find Median (13 lines): short. The trick is the two-heap invariant with negated values; once a student knows it, the code is quick. Writable after Class 17's heaps.
- #135 Candy (10 lines): the code is trivial and the two-pass idea is the whole difficulty. Writable if the take-home primes "satisfy one neighbour rule per pass"; otherwise most students will stall on the idea, not the code.
- #51 N-Queens (24 lines): standard choose–explore–undo backtracking with three sets; Problem A (Subsets) in the same class rehearses the shape. Writable.
- #10 Regex (17 lines): the `*` case (zero copies `dp[i][j-2]` or one more copy `dp[i-1][j]`) and the row-0 initialisation are where chalk solutions break. Writable with the 3 × 3 trace the key suggests; error-prone.
- #212 Word Search II (29 lines, the longest): it combines a trie build, grid backtracking and two pruning moves (`node.pop('$')`, `parent.pop(ch)`). Problem A (#208) supplies the trie the same day, which helps. Without the two-line `if not node: parent.pop(ch)` step, the code returns the same words on 2,000 of 2,000 random cases and takes 1.21 s instead of 0.50 s on the all-"a" board ([out_check_212_unpruned.txt](/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_16_30/out_check_212_unpruned.txt)). Writable by strong students; I would accept the unpruned version.
- #218 Skyline (17 lines): short, but correct only because of three invisible decisions: encode starts as `-height` so taller starts sort first at equal x, sort ends after starts, and keep a ground sentinel with lazy deletion. I would expect most students to get one of these wrong at the board; a hint about event ordering seems necessary.

### Gaps
- No session length is stated in the syllabus draft, and I have no data on these students, so the judgment above rests on code length and the number of non-obvious steps alone.
