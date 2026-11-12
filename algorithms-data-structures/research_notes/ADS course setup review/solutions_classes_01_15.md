# Instructor key, classes 1-15: are the 30 solutions correct and complete?

Scope: the 30 problems in classes 1-15 of `ADS_In_Class_Solutions.md` ([key]), their student sheets ([sheets]) and the memory table in the syllabus ([syl]). I ran every board solution on CPython 3.13.12 (`/opt/homebrew/bin/python3.13`). I fetched each problem's official statement, examples, constraints and Python3 signature from LeetCode's GraphQL endpoint ([fetched]). All test code and raw output sit in `/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_01_15/` and rerun with `python3.13 -I <script>`:

- `board.py`: the 30 board solutions, transcribed verbatim with key line numbers ([board])
- `test_correctness.py` → `out_correctness.txt`: LeetCode examples, edge cases, random inputs against a brute-force reference, one timed run at LeetCode's maximum size ([corr])
- `test_memory.py` → `out_memory.txt`: tracemalloc at the key's stated input size ([mem])
- `probe_misc.py` → `out_probe.txt` and `probe_tail.py` → `out_probe_tail.txt`: targeted probes behind specific claims ([probe], [tail])
- `fetch_leetcode.py` → `fetched/*.json`, `fetched/digest.txt` ([fetched])

Units follow the key: KB = 1,024 B, MB = 1,048,576 B. "Formula" means the course's own size table (syllabus L174-216) applied to what is actually alive at the peak. "Measured" means tracemalloc: input = traced bytes after building the input, aux = peak during the call minus bytes before it, retained = bytes still alive after the call.

**Bottom line.** All 30 board solutions return correct answers on every test I ran: 30 of 30 pass ([corr]). Two caveats hold. #933 and #102 call `deque` without an import line, and #104 hits Python's recursion limit on a deep chain. Every main time and auxiliary-space claim holds. The memory figures and the "Other approaches" tables are where the defects sit. Under the key's own assumptions, three estimates are wrong by more than 20% or are wrong in kind (#1480, #88, #1). Six more rest on wrong reasoning about what is alive at the peak, even where the number lands near the measurement. Seven problems have no "Other approaches" table at all. The header's claim that every memory figure "was checked against tracemalloc at the stated input size" (key L5-9) does not survive measurement (see Q4).

## Summary table

Legend: OK = no defect found. Minor = wrong detail, no effect on a student's grade. Defect = a wrong figure or claim that could mislead grading or teaching. Memory column: key aux figure vs measured aux peak.

| Class | Slot | Problem | Correctness | Complexity (main / alternatives) | Memory (key aux vs measured) | Statement match | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | A | #1480 Running Sum | Pass | OK / OK | **Defect**: 150 B vs 382 KB retained growth; key calls it churn | Match (n = 100,000 is 100× LeetCode's 1,000; not said) | Defect (memory) |
| 1 | B | #217 Contains Duplicate | Pass | OK / OK | Number OK (4.0 MB; peak 6.00 MB measured); reasoning wrong (2^18 slots × 16 B, not 2^17 × 32 B) | Match | Minor |
| 2 | A | #283 Move Zeroes | Pass | OK / **table missing** | OK (150 B vs 236 B) | Match (n beyond LeetCode's 10^4; not said) | Minor (completeness) |
| 2 | B | #88 Merge Sorted Array | Pass | OK / **table missing** | **Defect**: input 5.1 MB vs formula 3.81 MB, measured 4.20 MB | Match (m + n far beyond LeetCode's 200; not said) | Defect (memory, completeness) |
| 3 | A | #14 Longest Common Prefix | Pass | OK / **sort row wrong** | Minor: 341 B slice vs 176 B (stated worst case returns the input object) | Match | Minor ×2 |
| 3 | B | #303 Range Sum Query | Pass | OK / **table missing** | OK (352 KB vs 396 KB, within 11%) | Match | Minor (completeness) |
| 4 | A | #242 Valid Anagram | Pass | OK / OK | OK (2.0 KB vs 1.9 KB) | Match | OK, no defect |
| 4 | B | #1 Two Sum | Pass | OK / OK | **Defect**: 781 KB vs 575 KB measured (52 B/entry used; actual 29.5) | Match | Defect (memory) |
| 5 | A | #125 Valid Palindrome | Pass | OK / OK | OK (150 B vs 236 B) | Match | Minor ("lower() cached" is false) |
| 5 | B | #977 Squares of a Sorted Array | Pass | OK / OK | OK (352 KB vs 391 KB) | Match | OK, no defect |
| 6 | A | #643 Maximum Average Subarray I | Pass | OK / OK | OK | Match | OK, no defect |
| 6 | B | #121 Best Time to Buy and Sell Stock | Pass | OK / OK | OK | Match | OK, no defect |
| 7 | A | #20 Valid Parentheses | Pass | OK / OK | OK (88 KB vs 83.5 KB) | Match; omits LeetCode's third validity rule | Minor |
| 7 | B | #844 Backspace String Compare | Pass | OK / OK | OK (3.6 KB vs 3.5 KB) | Match | OK, no defect |
| 8 | A | #933 Number of Recent Calls | Pass with import; **NameError as written** | OK / **table missing** | OK (25 KB vs 25.5 KB) | Match | Defect (board code), minor (completeness) |
| 8 | B | #232 Queue using Stacks | Pass | OK / **table missing** | Minor: 879 KB vs 783 KB steady; first pop() peaks at 1.19 MB, not mentioned | Match; omits x ∈ 1..9 and "calls are valid" | Minor |
| 9 | A | #496 Next Greater Element I | Pass | OK / brute-force space breaks convention | Number OK (55 KB vs 54.4 KB); composition wrong | Match | Minor |
| 9 | B | #739 Daily Temperatures | Pass | OK / brute-force space breaks convention | OK (4.3 MB vs 4.19 MB) | Match | Minor |
| 10 | A | #206 Reverse Linked List | Pass | OK / **table missing** | OK (488 KB vs 584 KB input, 16%) | Match | Minor (completeness) |
| 10 | B | #19 Remove Nth Node | Pass | OK / **table missing** | OK | Match; `ListNode(0, head)` relies on a class defined nowhere in the course files | Minor |
| 11 | A | #509 Fibonacci | Pass | OK / OK | Minor: counts 31 new ints, only 17 exist | Match | Minor |
| 11 | B | #50 Pow(x, n) | Pass (within constraints) | OK / OK | Minor: "32 floats" is really ~23 ints + ≤ 2 floats; total similar | Omits constraints (x = 0, n < 0 crashes the board code) | Minor |
| 12 | A | #136 Single Number | Pass | OK / **sort row says O(1); Python's sort is O(n)** | OK | Match | Minor |
| 12 | B | #260 Single Number III | Pass (incl. negatives, -2^31) | OK / OK | OK | Match | OK, no defect |
| 13 | A | #1331 Rank Transform | Pass (incl. empty array) | OK / OK | Minor-to-defect: 9.3 MB vs 10.92 MB; wrong objects named as alive at the peak | Match | Defect (memory reasoning) |
| 13 | B | #912 Sort an Array | Pass; 0.30 s at n = 5×10^4 | OK / OK | OK (830 KB vs 864 KB) | Drops "smallest space complexity possible" | Minor |
| 14 | A | #704 Binary Search | Pass | OK / bisect not marked "not for the board" | OK | Match | Minor |
| 14 | B | #34 First and Last Position | Pass (incl. empty) | OK / same bisect note | OK | Match | Minor |
| 15 | A | #104 Maximum Depth | Pass up to depth 990; **RecursionError on a 1,000-node chain**; LeetCode allows 10^4 nodes | OK / OK | OK (frames invisible to tracemalloc) | Match (second example is not LeetCode's) | Defect (recursion depth unaddressed) |
| 15 | B | #102 Level Order | Pass with import; **NameError as written** | OK / OK | Minor: 120 KB vs 94.9 KB (26% high) | Match (n = 10,000 vs LeetCode's 2,000; not said) | Defect (board code), minor (memory) |

## Defect register (every defect, with key line numbers)

Line numbers refer to `ADS_In_Class_Solutions.md` ([key]) unless marked "sheet".

**D1. #1480, memory, key L117-134. Defect.** The key says: aux "index, range iterator and one temporary int, about 150 bytes" (L126). It also says "Each update replaces an old int with a new one of the same size, so memory does not grow. (A tool such as tracemalloc shows a few hundred KB of allocator churn; that is not growth.)" (L132-134). The correct picture follows from the key's own assumption of 100,000 *distinct* ints above 256 (L117): the running sums must pass 2^30 = 1,073,741,824, because even the smallest such set (257..100,256) sums to 5,025,650,000. Past 2^30 every sum is a two-digit int, and CPython allocates it larger. The growth survives the call, so it is not churn. Measured retained growth: 382.1 KB with values up to 10^6 (97,789 sums ≥ 2^30), and 307.0 KB with the smallest possible values. At LeetCode's real limits (n ≤ 1,000, |v| ≤ 10^6) the growth is 88 B ([mem]; constraint from [LC-1480]). Big-O O(1) still holds in the fixed-width-int sense. The byte figure and the "not growth" sentence do not.

**D2. #217, memory reasoning, key L208-211. Minor.** The key says "A set that large uses a table of 2^17 slots of 32 bytes." In fact the table has 2^18 slots of 16 bytes: `sys.getsizeof` of a 100,000-element set is 4,194,520 B, which is a 216 B header plus 4,194,304 B of table, or 262,144 slots × 16 B ([probe] section h). The total (4.0 MB) and the measured peak (6.00 MB, key: "about 6 MB") are right ([mem]).

**D3. #283, #88, #303, #933, #232, #206, #19: no "Other approaches" table. Minor (completeness).** The key promises "Each problem lists other approaches with their complexity" (L27). These seven problems have none ([tail]: `Problems with NO "Other approaches" table: ['283', '88', '303', '933', '232', '206', '19']`). LeetCode's own follow-ups name the missing alternatives for two of them: #206 asks for the recursive version, and #88 asks for O(m + n), which is the board solution's own bound ([LC-206], [LC-88]).

**D4. #88, memory, key L389-400. Defect.** The key says: input "(56 + 8n + 28n) for nums1 + (56 + 8n/2 + 28n/2) for nums2" = 5.1 MB (L395-396). Here n means nums1's 100,000 slots, although the problem's own n is 50,000 (nums2's length). The correct figure: 50,000 of nums1's slots hold the shared int 0, which costs nothing. The key itself treats zeros that way in #283 (L305-306). The course formula gives (56 + 800,000 + 1,400,000) + (56 + 400,000 + 1,400,000) = 4,000,112 B = 3.81 MB, and tracemalloc measures 4.20 MB ([mem]). The key sits 35% above the formula and 23% above measurement, so a student who applies the course table correctly lands about 26% below the key's figure. That is close to the 30% acceptance edge (L21-22). Cosmetic: the total reads 5.2 MB (L400) while input plus 150 B is 5.15 MB, the same figure the input row rounds to 5.1.

**D5. #14, memory, key L478-479. Minor.** The key says the auxiliary is "the returned slice: 41 + 200 bytes, plus a few indexes = 341 bytes" for the stated worst case of 200 identical strings. In that case the loop never mismatches and the function returns `first`, the input object itself, so it creates no slice. The probe confirms `returns the input object itself: True`, with measured aux peak 176 B. A 241 B slice appears only when a mismatch occurs, as in my variant where the last string differs at character 200: 416 B peak ([mem]).

**D6. #14, other approaches, key L492-493. Minor.** The key says "Sort the strings; compare only first and last: O(S + m log m) time." Each string comparison can cost up to L characters, so the sort costs O(L · m log m) in the worst case, which is O(S log m). Sorting 200 strings of length 200 that share a 199-character prefix took 1,277 comparisons and 255,727 character comparisons, 6.4 times S = 40,000 ([probe] section k).

**D7. #1, memory, key L729-741. Defect.** The key says: aux "dict at about 52 bytes per entry + 28 bytes per stored index" = 781 KB (L738-739). The 52 B rate holds at 100,000 entries, not at 10,000. A dict of 9,999 int keys has `getsizeof` 294,992 B = 29.5 B/entry ([probe] section g: 1,000 entries 37.0, 9,999 entries 29.5, 100,000 entries 52.4). Correct formula: 294,992 + 9,742 new index ints × 28 = 554.5 KB. Measured aux peak: 574.7 KB. The key is 36% above measurement, so a student with the correct method lands about 26-29% below the key ([mem]).

**D8. #125, complexity text, key L827-828. Minor.** The key says "single-character strings from s[i] and lower() are cached, so they cost nothing." `s[i]` is cached, but `lower()` is not: `'A'.lower() is 'a'` → False, and `'a'.lower() is 'a'` → False ([probe] section e). Each `lower()` makes a fresh one-character string and frees it at once, so the O(1) claim and the 150 B figure stand (measured peak 236 B, [mem]).

**D9. #933 and #102, board code, key L1348 and L2733. Defect (board code as written does not run).** Both board solutions call `deque()` but show no `from collections import deque`. The key's board code for class 17 onward does write `import heapq` (L2995, L3081, L3873, L3991, L5100, L5947; [tail]), so the omission is inconsistent. Running the key's RecentCounter verbatim in a fresh namespace raises `NameError name 'deque' is not defined` ([probe] section d). With the import added, both pass all tests ([corr]). Whether LeetCode's judge pre-imports `deque` is a gap (see Q1).

**D10. #232, memory, key L1489-1502. Minor.** The key says aux = "one list of n pointers (about 12% growth room)" = 879 KB, "counted at the moment all n items sit in the inbox." It measures 782.7 KB at that moment, because an append-built list of 100,000 has only 0.1% spare: capacity 100,116 ([probe] section f). The first `pop()` then pours the inbox into the outbox and adds a further 434.0 KB peak, so the true peak is about 1.19 MB ([mem]). The key also assumes 28 B per item, but LeetCode restricts x to 1 ≤ x ≤ 9, which are shared small ints ([LC-232]). The key states its n = 100,000 departs from LeetCode's 100-call limit (L1489-1490).

**D11. #496, memory composition, key L1583-1584. Minor.** The key's aux = "dict about 40 bytes per entry for up to n entries + stack 8n + answer list 8n" = 55 KB. The stack and the dict cannot both be full: every popped value enters the dict. For the stated random permutation the stack peaked at 12 entries while the dict held 993 ([mem]). The measured peak, 54.4 KB, matches the key's number by coincidence: it occurs during the dict's last resize, when the old and new tables coexist. The finished objects total 36,952 B (dict) + 8,856 B (answer) ([mem]).

**D12. #496 and #739, other approaches, key L1594 and L1691. Minor.** The key lists brute force as "O(1) extra." Under the key's own convention, "anything that is built and returned" counts as auxiliary space (L17-19), so the brute force still builds the m- or n-element answer list: O(m) for #496 and O(n) for #739. The main-solution rows (L1562, L1659) do count the answer.

**D13. #509, memory, key L1922-1933. Minor.** The key says "31 values × 28 bytes." F(0)..F(13) ≤ 233 are cached small ints, so only F(14)..F(30) are new objects: 17 × 28 = 476 B, not 868 B. The formula gives 1,168 (dict, `getsizeof`, [probe] section g) + 476 + 30 × 150 = 6.0 KB against the key's 6.4 KB. Measured, tracemalloc saw a 2.3 KB peak without frames ([mem]). Measured by RSS high-water mark, the key's `go(k)` closure costs about 150 B per active call ([probe] section b), which supports the 150 B frame figure. Tracemalloc also shows 2.0 KB still alive after `fib(30)` returns. My inference is that the recursive inner function forms a reference cycle that only the cyclic garbage collector frees.

**D14. #50, memory composition, key L2013-2022. Minor.** The key says "32 frames × 150 bytes + 32 floats × 24 bytes." On the way down, the frames hold the exponents, not floats: 23 of the 32 values of n are above 256, so they are new ints. The `half` floats exist only on the way back up, at most about two at a time. Measured traced peak, frames excluded: 840 B, against the key's 768 B of floats ([mem]). The total barely changes, but the explanation is wrong. One more point: n = 2^31 is itself a 32-byte int, so the input is 56 B, not 52 B.

**D15. #50, statement, key L1957-1959 and sheet L1119-1121. Minor.** The key omits LeetCode's constraints "-100.0 < x < 100.0", "Either x is not zero or n > 0" and "-10^4 <= x^n <= 10^4" ([LC-50]). Without them, the board code fails on inputs a student may reasonably try. `myPow(0.0, -1)` and `myPow(0.5, -2000)` raise `ZeroDivisionError`, and `myPow(10.0, 400)` returns `inf` ([tail]). Inside the constraints the board code passed 5,000 random cases and the edge cases n = ±2^31 ([corr]). Its worst relative error near the 10^4 bound was 3.8e-10, an absolute error of 3.75e-6 at 9,897.12.

**D16. #136, other approaches, key L2121. Minor.** The key says "Sort, then check neighbors in pairs: O(n log n), O(1)." Python's `list.sort()` allocates a merge buffer of up to n/2 pointers. An in-place sort of 30,000 random ints peaked at 119,936 B, 4.00 B per element ([probe] section j), so the space is O(n) in Python. The key's #217 row hedges correctly with "O(1) to O(n)" (L234).

**D17. #1331, memory, key L2278-2291. Minor-to-defect.** The key says "At the peak the set is gone, but the sorted list, the dict, the 100,000 new rank ints and the answer list are all alive," giving 9.3 MB. The sorted list and the answer list are never alive together: the list iterator drops the sorted list when the `for` loop finishes, before the comprehension starts. The real peak falls inside the loop, at the dict's last resize, when the old table (about 2.6 MB) and the new table (5.24 MB, `getsizeof` 5,242,960 B) coexist. The measured peak is 10.92 MB, and it stays 10.92 MB with the final comprehension removed ([probe] section l). The key is 15% low. The key's own rule, "its peak can be about 1.5 times its final size" (L61), predicts this, but the key does not apply it here.

**D18. #102, memory, key L2788-2802. Minor.** The key adds the full result (8n) to the widest queue (n/2 × 8.3), as if both were alive at once, giving 120 KB. When the queue is widest, about 5,000 entries, the result holds only about half the values. Measured peak: 94.9 KB, so the key is 26% high ([mem]). The phrase "the last level about 1,700 to 5,000 nodes" (L2789-2790) is muddled: the last level has 1,809 nodes, the widest level has 4,096, and the queue peaks near 5,000.

**D19. #104, recursion depth, key L2682-2685. Defect (an unaddressed failure mode).** LeetCode allows up to 10^4 nodes ([LC-104]). In plain Python 3.13 (`sys.getrecursionlimit()` = 1000) the board solution handles a 990-node chain but raises `RecursionError` on chains of 1,000 and 10,000 nodes. After `sys.setrecursionlimit(10_100)`, it returns 10000 on the 10,000-node chain ([probe] section c). The key mentions the limit only inside the memory assumptions ("more than the default Python recursion limit of 1,000"). It never tells the instructor that the board solution fails on such inputs, nor what to accept instead (the iterative BFS in its own table, or an explicit stack).

**D20. #912, statement, key L2313-2314. Minor.** LeetCode requires "without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible" ([LC-912]). The key drops the space requirement. The board merge sort uses O(n) auxiliary memory, measured at 863.7 KB for n = 50,000 ([mem]), and an in-place heap sort would meet LeetCode's wording better. The solution is correct and fast: 0.30 s at n = 5 × 10^4 ([corr]).

**D21. #704 and #34, other approaches, key L2514 and L2621. Minor.** These rows list `bisect_left` / `bisect_right` without "(not for the board)." The sheet allows only "what Python gives you, plus collections and heapq" (sheet L10-11), and the key marks `itertools.accumulate` as "not for the board" (L144-145). By the same logic, bisect should carry the same mark.

**D22. #20, statement, key L1144-1146. Minor.** The key keeps two of LeetCode's three validity rules. It omits "Every close bracket has a corresponding open bracket of the same type" ([LC-20]). The board code handles stray closers correctly: ")", "]" and "(]" all return False ([corr]).

**D23. Node classes, #19 board code key L1793. Minor.** `ListNode(0, head)` assumes LeetCode's two-argument constructor. No `class ListNode` or `class TreeNode` appears in the key, the sheets or the syllabus ([tail]). With LeetCode's definition ([LC-19]) the code passes ([corr]).

**D24. Header claim, key L5-9. Defect (claim not supported).** "Every memory figure was formed from a formula and then checked against tracemalloc at the stated input size" is contradicted three ways. D1, D4, D7, D17 and D18 diverge from tracemalloc by 14-36%, or by a factor of thousands in D1. The key's own L62 and L1924-1925 say frames are "estimated, not measured" and "invisible to tracemalloc." And every 100,000-int list the key calls 3.4 MB measures 3.81 MB under tracemalloc (see Q4).

**Nits that need no change of grade (informational).**
- Input sizes beyond LeetCode's limits go unstated for #1480 (L117; limit 1,000), #283 (L299; limit 10^4), #88 (L389; m + n ≤ 200) and #102 (L2788; limit 2,000) ([LC-1480], [LC-283], [LC-88], [LC-102]). The key does say so for #232.
- #704 assumes "10,000 sorted distinct ints above 256 (the LeetCode limit)" (L2494-2495). LeetCode bounds values to -10^4 < v < 10^4, which leaves only 9,743 values above 256 ([LC-704]).
- #104's second example "root = [] -> 0" (L2636) is valid but is not one of LeetCode's examples. LeetCode's second is [1,null,2] → 2 ([LC-104]).
- #19 assumes about 100 B per node "ints included" (L1844-1845). LeetCode's values 0..100 are cached, so a node measures 88 B, and the list totals 2.6 KB against 2.9 KB ([mem]).

**Problems with no defect found:** #242, #977, #643, #121, #844, #260. Their solutions, complexity, memory figures, reasoning and alternatives all check out against my runs.

## Q1. Do the board solutions return correct results, and would they pass LeetCode's constraints in Python?

### Takeaway
Every one of the 30 board solutions returns correct results on LeetCode's examples, on edge cases, and on random inputs checked against a brute-force reference (31 exhaustive cases for #509; 1,000-8,000 random cases for the rest): 30 of 30 pass. Three practical failures remain. #933 and #102 omit the `deque` import, so they raise NameError as written. #104 raises RecursionError on chains of 1,000+ nodes in plain Python, although LeetCode allows 10^4.

### Cited Findings
- Final run: `SUMMARY: 30 PASS of 30`, `python 3.13.12`, with zero failures on examples, edge cases and random cases for every problem ([corr]).
- Random cases compared with a brute-force reference: 2,000 (#1480, #217, #283, #1, #933, #232, #206, #104, #102); 3,000 (#14, #242, #977, #643, #121, #496, #739, #19, #136, #1331, #912, #704, #34); 5,000 (#20, #844, #50); 6,000 (#260); 8,000 (#125); 1,000 (#303); 1,971 (#88); 31 (#509, every n from 0 to 30) ([corr]).
- Edge cases came from LeetCode's constraints: single elements; empty inputs where LeetCode allows them (#14 empty strings, #1331 `[]`, #34 `[]`, #206 `[]`, #104/#102 empty tree); duplicates; negatives and extremes (±10^9 for #1 and #34; -2^31 and 2^31 - 1 for #260 and #283; n = ±2^31 for #50; 10^4 '(' for #20) ([corr], constraints in [fetched]).
- One timed run at LeetCode's maximum size per problem: every run finished in ≤ 0.30 s, the slowest being #912 at 0.301 s (n = 5 × 10^4) and #1331 at 0.204 s (n = 10^5) ([corr]). MyQueue time doubles with n (0.082 → 0.109 → 0.222 s for 1-4 × 10^5 push+pop), and merge sort grows as n log n (0.228 → 0.408 → 1.206 s for n = 5 × 10^4 → 2 × 10^5) ([probe] section m).
- The #50 test I first wrote, (1.0000001, 2^30 - 1), fails, but it breaks LeetCode's |x^n| ≤ 10^4 constraint: its result is 4.3e46. I replaced it with (1.0000001, ±92,000,000), whose result is about 9,897, and the code passes with relative error 3.8e-10 ([corr]; constraint [LC-50]).
- Recursion depth: #509 reaches 30 frames, #50 about 33, #912 about 17 (log2 50,000 ≈ 15.6), all far below the limit. #104 fails at a 1,000-node chain with the default limit of 1,000 and succeeds on 10,000 nodes after `sys.setrecursionlimit(10_100)` ([probe] section c; LeetCode's 10^4-node bound [LC-104]).
- The #933 board code run verbatim raises `NameError name 'deque' is not defined` ([probe] section d).

### Inferences
- The key's first claim, that every solution was run against LeetCode examples and edge cases, matches what I found for the algorithms. It does not hold for the board text of #933 and #102, which cannot have been run as printed.
- A student who copies the #104 board solution passes LeetCode only if LeetCode's judge raises Python's recursion limit or its tests contain no deep chain. The key should say which, or present the iterative version as the safe answer.

### Gaps
- I could not verify LeetCode's judge settings: its recursion limit, its per-problem time limits, whether it pre-imports `collections.deque`, and its float tolerance for #50. The fetched statements do not state them, and I found no official page in this session. My timing runs show margins, not LeetCode verdicts.
- I ran the board solutions, not the "Other approaches" code; I checked those by reasoning and targeted probes (Q5).

## Q2. Do the statement, example and starter signature in the key and on the student sheet match LeetCode?

### Takeaway
The key and the sheets carry identical statement and example text for all 30 problems, and each example matches LeetCode's except #104's second. Function names and parameters match LeetCode's Python3 signatures, written as plain functions instead of `class Solution` methods, a consistent course choice. Five statements drop a LeetCode constraint or requirement; only #50's omission lets the board code crash on inputs a student might try.

### Cited Findings
- A text comparison of the key's statement and example block against the sheet's block for all 30 problems found `statement/example text differs for: none`. The sheets' memory-size sentences match the key's "Assumptions." sentences for all 30 ([probe] section n).
- Starter names and parameters match LeetCode's fetched Python3 snippets, e.g. `def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None` ([LC-88]) against the sheet's `def merge(nums1, m, nums2, n):` (sheet L197). The same holds for every function problem ([fetched] digest). The design problems keep LeetCode's class names (NumArray, RecentCounter, MyQueue), but the sheets list only "Start with: class NumArray" (sheet L301), "class RecentCounter" (L770) and "class MyQueue" (L821), without method signatures. The statements name the methods.
- Omitted constraints or requirements: #50 omits -100 < x < 100, "x is not zero or n > 0" and |x^n| ≤ 10^4 ([LC-50]; consequence in D15). #912 omits "smallest space complexity possible" ([LC-912]). #20 omits the third validity rule ([LC-20]). #232 omits 1 ≤ x ≤ 9 and "All the calls to pop and peek are valid" ([LC-232]). #136 states only the O(1)-space requirement, not "linear runtime" ([LC-136]). #125 omits "printable ASCII characters" ([LC-125]), which matters little because Python's `isalnum` is a superset.
- Example check: every key example appears among LeetCode's examples, except that #104 replaces LeetCode's second example [1,null,2] → 2 with [] → 0 ([LC-104]).
- Neither the key, the sheets nor the syllabus defines `ListNode` or `TreeNode`, which #206, #19, #104 and #102 rely on ([tail]).

### Inferences
- None of the omissions changes which algorithm is correct. The #50 omission matters most at the board: a student who tests x = 0 with negative n will see the "correct" key solution crash, and needs to know that LeetCode excludes that input.
- The sheets would serve students better with the ListNode/TreeNode definitions and the method signatures for the three design classes.

### Gaps
- I compared only the problem text, examples, constraints and signatures. LeetCode's hidden test sets cannot be fetched, so I cannot say which edge cases LeetCode actually tests, such as deep chains for #104.

## Q3. Are the stated time and auxiliary space correct?

### Takeaway
All 30 main time and auxiliary-space claims are correct, including the hidden costs the key names: slicing in #912 and #14, sorting in #1331, the answer list in #496 and #739, recursion stacks in #509, #50, #912 and #104, and amortized pouring in #232. The few complexity errors sit in the "Other approaches" tables (Q5), not in the main rows.

### Cited Findings
- Amortized O(1) for #232: 100,000 → 400,000 push+pop pairs take 0.082 → 0.222 s, roughly linear in n ([probe] section m).
- O(n log n) for #912 with slicing: 0.228 → 0.408 → 1.206 s as n goes 5 × 10^4 → 10^5 → 2 × 10^5 ([probe] section m).
- O(log n) depth for #50: about 33 calls at n = 2^31 (23 of the exponents exceed 256, computed in [mem]); #104's O(h) shows directly as the RecursionError on a chain ([probe] section c).
- #933's O(W) bound holds: the deque never exceeds 3,001 entries at one ping per millisecond (`final deque len 3001`, [mem]).
- Under the key's convention (L17-19) the main rows count returned output: #977 O(n), #1331 O(n), #102 O(n), #14 O(L), #260 O(1) with a 2-element result. I found no main row that omits a built output.

### Inferences
- The main complexity rows are safe to grade from as written.

### Gaps
- I validated time claims empirically only where a hidden cost could bite (#232, #912). For the other linear scans the code makes the bound evident, and every run at LeetCode's maximum size took ≤ 0.30 s ([corr]).

## Q4. Are the memory estimates right?

### Takeaway
Most figures land within the key's own 30% tolerance, but the header's claim that each was "checked against tracemalloc at the stated input size" does not hold. Three figures are wrong outright (#1480, #88, #1). Six rest on a wrong account of what is alive at the peak (#217, #14, #496, #1331, #102, #50). Tracemalloc systematically reads about 11% above every int-list input, because CPython 3.13 allocates ints made by `range` or arithmetic as 32-byte blocks while `sys.getsizeof` reports 28.

### Cited Findings
Per-problem figures, from [mem] unless noted (aux = auxiliary; measured aux is the traced peak during the call):

| # | Key input | Formula input | Measured input | Key aux | Formula aux | Measured aux peak (retained after) |
|---|---|---|---|---|---|---|
| 1480 | 3.4 MB | 3.43 MB | 3.81 MB | 150 B | 150 B, plus 4 B per sum ≥ 2^30 | 382.2 KB (382.1 KB retained) |
| 217 | 3.4 MB | 3.43 MB | 3.81 MB | 4.0 MB, peak ~6 | 4.01 MB; peak ×1.5 = 6.0 | 6.00 MB (88 B) |
| 283 | 2.1 MB | 2.10 MB | 2.29 MB | 150 B | 150 B | 236 B |
| 88 | 5.1 MB | 3.81 MB | 4.20 MB | 150 B | 150 B | 216 B |
| 14 | 49 KB | 48.7 KB | 48.7 KB | 341 B | ~0 (returns input) | 176 B |
| 303 | 352 KB | 351.6 KB | 390.7 KB | 352 KB | 361.0 KB (append room) | 396.1 KB (396.1 KB) |
| 242 | 98 KB | 97.7 KB | 97.8 KB | 2.0 KB | 1.5 KB (dict 832 B + 26 × 28) | 1.9 KB |
| 1 | 352 KB | 351.6 KB | 390.8 KB | 781 KB | 554.5 KB | 574.7 KB |
| 125 | 195 KB | 195.4 KB | 195.4 KB | 150 B | 150 B | 236 B |
| 977 | 352 KB | 351.6 KB | 387.9 KB | 352 KB | 351.6 KB | 391.0 KB (390.8 KB) |
| 643 | 3.4 MB | 3.43 MB | 3.81 MB | 150 B | 150 B | 300 B |
| 121 | 3.4 MB | 3.43 MB | 3.81 MB | 150 B | 150 B | 256 B |
| 20 | 9.8 KB | 9.8 KB | 9.8 KB | 88 KB | 87.7 KB | 83.5 KB |
| 844 | 482 B | 482 B | 570 B (incl. 88 B arg tuple) | 3.6 KB | 3.6 KB | 3.5 KB |
| 933 | 273 KB (ints only) | 266.4 KB | 382.7 KB (incl. list) | 25 KB | 24.9 KB | 25.5 KB (25.4 KB) |
| 232 | 2.7 MB (ints only) | 2.67 MB | 3.81 MB (incl. list) | 879 KB | 782 KB (0.1% spare at n = 10^5) | 782.7 KB; +434.0 KB during first pop |
| 496 | 43 KB | 43.1 KB | 47.1 KB | 55 KB | 46 KB (dict + answer + 12-entry stack) | 54.4 KB (8.9 KB) |
| 739 | 781 KB | 781.3 KB | 781.3 KB | 4.3 MB | 4.29 MB | 4.19 MB (781.4 KB) |
| 206 | 488 KB | 488.3 KB | 584.4 KB (119.7 B/node) | 150 B | 150 B | 120 B |
| 19 | 2.9 KB | 2.9 KB | 2.6 KB (cached vals) | 250 B | 250 B | 264 B |
| 509 | 28 B | 28 B | 28 B | 6.4 KB | 6.0 KB | 2.3 KB traced + frames (~150 B/call by RSS) |
| 50 | 52 B | 56 B | 56 B | 5.4 KB | 5.5 KB | 840 B traced + frames |
| 136 | 645 KB | 644.6 KB | 703.2 KB | 100 B | 100 B | 200 B |
| 260 | 645 KB | 644.6 KB | 732.6 KB | 250 B | 250 B | 256 B |
| 1331 | 3.4 MB | 3.43 MB | 3.81 MB | 9.3 MB | ≈ 11.1 MB at dict resize | 10.92 MB (3.81 MB) |
| 912 | 1.7 MB | 1.72 MB | 1.91 MB | 830 KB | 828.1 KB | 863.7 KB (435.9 KB result) |
| 704 | 352 KB | 351.6 KB | 390.7 KB | 100 B | 100 B | 248 B |
| 34 | 3.4 MB | 3.43 MB | 3.81 MB | 250 B | 250 B | 556 B |
| 104 | 977 KB | 976.6 KB | 1.06 MB (111.4 B/node) | 2.1 KB | 15 frames × 150 = 2.2 KB | 120 B traced; frames invisible |
| 102 | 977 KB | 976.6 KB | 1.22 MB (128 B/node, new-int vals) | 120 KB | ≈ 86-95 KB | 94.9 KB (83.6 KB) |

- Int size: `sys.getsizeof` reports 28 B. Tracemalloc counts 32.00 B per int made from a `range` item or by arithmetic, and 28.01 B per int made by `int("...")` or `json.loads` ([probe] section a). Every 100,000-int input list therefore measures 3.81 MB against the formula's 3.43 MB.
- Frames: 900 nested calls showed 20,632 B traced, which is the 644 int arguments above 256 (644 × 32 = 20,608 B), not frames. By RSS high-water mark at depth 200,000, an active call costs 136 B (maxDepth), 150 B (the key's `go`) and 168 B (myPow's shape, including the int it holds) ([probe] section b). The course's 150 B per call is therefore a fair estimate, but tracemalloc cannot check it. The key admits frames are "estimated, not measured" (L62).
- Course table spot checks on 3.13: `getsizeof("")` = 41 and `getsizeof("a"*200)` = 241 (str row correct). A 3-entry dict is 184 B (tiny-dict row correct). Dict cost per entry is 37.0 B at 1,000 entries, 29.5 B at 9,999 and 52.4 B at 100,000, so the per-entry cost does not rise monotonically with size. Append spare room is 0.0% at n = 200, 6.4% at n = 10,000 and 0.1% at n = 100,000 against the table's "about 12%" ([probe] sections a, f, g).

### Inferences
- The int-size gap is a syllabus-table matter (L174-216), outside this file's scope. It means a student who checks the key against tracemalloc will see about 11% more on every int list, and the key never explains why.
- Under the key's 30% rule (L21-22), the D4 (#88) and D7 (#1) figures would push a correct student answer to or past the rejection edge. Those two figures, and the #1480 aux claim, need correcting before use.

### Gaps
- RSS-based frame costs on macOS are approximate: they include any objects the frames hold and the allocator's chunking.
- I measured each problem in one input shape, the one the key states. Other shapes, such as #1 with the answer early, change the figures in ways the key does not claim to cover.

## Q5. Are the step-by-step reasoning and the "Other approaches" tables correct?

### Takeaway
The step-by-step reasoning is correct for all 30 problems. Its only errors are side remarks: #125's "lower() is cached" and the memory narratives listed in Q4. The "Other approaches" tables are missing for 7 problems. Where present, they contain four wrong complexity entries: #14's sort row, #136's sort space, and the brute-force space for #496 and #739.

### Cited Findings
- Missing tables: #283, #88, #303, #933, #232, #206, #19 ([tail]). The key's own rule says "Each problem lists other approaches" (L27).
- #14 sort row (L492-493) understates the time: 255,727 character comparisons against S = 40,000 for 200 strings sharing a 199-character prefix ([probe] section k).
- #136 sort row (L2121) says O(1) space, but Python's in-place sort peaks at 4.00 B per element, an n/2-pointer buffer ([probe] section j).
- #496 (L1594) and #739 (L1691) list brute force as "O(1) extra", contradicting the convention that returned output counts (L17-19).
- #977's "Square every value, then sorted(): O(n log n)" (L951) is right as a general bound. On this input, though, CPython's sort found two runs and made 21,058 comparisons for n = 10,000, against 120,180 for random input ([probe] section i). That makes a teaching point, not an error.
- #217's "Sort, then compare neighbors: O(1) to O(n)" (L234) is acceptable as hedged; in Python it is O(n) ([probe] section j).
- Reasoning steps I checked against runs: #260 step 3's example "6 = 110 gives 010" (6 & -6 = 2, true); #34 step 4's `first_at_least(target + 1) - 1` (passes ±10^9 targets, [corr]); #260 on negative values including -2^31 (passes, [corr]); #50 step 5's single recursive call (depth about 33).

### Inferences
- Because the key grants credit for alternatives "if they are analyzed correctly" (L27), the four wrong entries would lead a grader to mark a correct student analysis as wrong, or a wrong one as right.

### Gaps
- I did not implement and time every alternative. I checked the ones whose complexity is in doubt (#14, #136, #217, #977) with probes, and the rest by reading.

## Q6. Can a student write each board solution by hand, using only what the course allows?

### Takeaway
Yes, with two exceptions in what is printed. All 30 board solutions are short and use only built-ins, `collections.deque` or nothing more; the longest, #912 merge sort, runs to about 20 lines. The exceptions are the missing `deque` import in #933 and #102, and the bisect alternatives in #704 and #34, which the board rule does not allow and the key does not flag.

### Cited Findings
- The sheet's rule: "Write a plain Python function. Use only what Python gives you, plus collections and heapq" (sheet L10-11). The board code for classes 1-15 uses only built-ins (`set`, `dict`, `sorted`, `len`, `max`, `abs`, `enumerate`, `range`) and `deque` ([board]).
- #912 avoids the built-in sort, as LeetCode requires, and builds its merge by hand ([board]; [LC-912]).
- `deque` appears with no import in #933 (L1348) and #102 (L2733); `import heapq` does appear in later board code (L2995 onward) ([tail]); the verbatim #933 code raises NameError ([probe] section d).
- `bisect_left` / `bisect_right` appear as alternatives in #704 (L2514) and #34 (L2621) without the "(not for the board)" tag that `itertools.accumulate` carries (L144-145).

### Inferences
- Adding `from collections import deque` to the two board solutions and tagging bisect "(not for the board)" would bring the key into line with its own rule.

### Gaps
- "Reasonably written by hand" is a judgment call; I judged by length and by whether each solution needs any library beyond the allowed ones.

<!-- Reference links -->
[key]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_In_Class_Solutions.md
[sheets]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_In_Class_Board_Problems.md
[syl]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_Syllabus_Draft.md
[board]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_01_15/board.py
[corr]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_01_15/out_correctness.txt
[mem]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_01_15/out_memory.txt
[probe]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_01_15/out_probe.txt
[tail]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_01_15/out_probe_tail.txt
[fetched]: file:///private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/classes_01_15/fetched/digest.txt
[LC-1480]: https://leetcode.com/problems/running-sum-of-1d-array/
[LC-283]: https://leetcode.com/problems/move-zeroes/
[LC-88]: https://leetcode.com/problems/merge-sorted-array/
[LC-20]: https://leetcode.com/problems/valid-parentheses/
[LC-125]: https://leetcode.com/problems/valid-palindrome/
[LC-232]: https://leetcode.com/problems/implement-queue-using-stacks/
[LC-206]: https://leetcode.com/problems/reverse-linked-list/
[LC-19]: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
[LC-50]: https://leetcode.com/problems/powx-n/
[LC-136]: https://leetcode.com/problems/single-number/
[LC-912]: https://leetcode.com/problems/sort-an-array/
[LC-704]: https://leetcode.com/problems/binary-search/
[LC-104]: https://leetcode.com/problems/maximum-depth-of-binary-tree/
[LC-102]: https://leetcode.com/problems/binary-tree-level-order-traversal/
