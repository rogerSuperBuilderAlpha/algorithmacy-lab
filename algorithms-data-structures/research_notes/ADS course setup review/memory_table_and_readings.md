# ADS course draft: memory table and readings, fact check

Measured 12 Nov 2026 on /opt/homebrew/bin/python3.13 (Python 3.13.12, Clang 17, 64-bit macOS arm64; line 1 of `m1_scalars.out`). Scripts and their saved outputs are in `S` = `/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/memory/` (`m1_scalars.py` ... `m7_tracemalloc_objects.py`, each with a `.out` file; rerun with `/opt/homebrew/bin/python3.13 -I <script>`). Document line numbers refer to the Markdown conversions in `.../scratchpad/ads/`.

## Summary of defects

Memory table (syllabus lines 174-216; the Board Problems line 25 and the Solutions key lines 40-62 repeat it):

1. **list "about 12% spare room if built with append" is wrong as a typical figure.** Measured spare slots after n appends: 10.0% at n = 1,000, 0.12% at n = 100,000, 6.4% at n = 10,000, 5.6% at n = 1,000,000 (`m2_containers.out`, `m6_extra.out`). The 12.5% is the growth step, not the leftover; leftover ranges from 0 to about 13% (17% at tiny n) and averages 6.1% for n between 1,000 and 2,000. The Solutions key reuses "about 12%" at lines 1212 and 1499, so those two estimates are overstated (at n = 100,000 the right figure is 0.1%).
2. **dict "184 bytes for a tiny dict" is true only for a dict with string keys.** Empty `{}` is 64; `{'a':1}` is 184; `{1:1}` is 224 (and stays 224 up to 5 integer entries) (`m2_containers.out`, `m6_extra.out`).
3. **dict "37 at 1,000 / about 50 at large" holds only for integer keys.** With string keys it is 26.0 per entry at 1,000 and 38.4 at 100,000 (`m6_extra.out`). The table does not say which key type.
4. **deque "plus about 600 bytes overhead" is wrong.** An empty deque is 760 bytes. The per-element figure 8.3 is right at 100,000 (8.25) but 8.7 at 1,000 (`m2_containers.out`).
5. **int "28 bytes" is the `sys.getsizeof` value, but the heap cost is 32 bytes** (tracemalloc: 32.0 per int above 256; 36.0 per int at 2^31 and up) (`m7_tracemalloc_objects.out`). Ints also grow past 28 at 2^30 (about 1.07 billion), which LeetCode sums and products reach. This is the main reason checks "disagree" with getsizeof-based estimates.
6. **"a 1-character string is shared" is true only for characters U+0000 to U+00FF** (ASCII plus Latin-1). A 1-character string of U+0100 or higher is a fresh object (`m1_scalars.out`).
7. **"About 100 bytes" for a node is a fair round number for a plain class** (ListNode 88 bytes plus its value; TreeNode 96 plus its value) but 2.2 times too big with `__slots__` and it hides that a non-cached int value adds 32 more (`m3_nodes.out`).
8. **"About 150 bytes per active call" is right for the smallest recursive function and low for typical ones.** Measured 152 / 193 / 257 bytes per level for three small functions; the frame itself is 8 x (9 + locals + stack slots) bytes, plus every int the call creates (`m5_recursion.out`). The Solutions key admits recursion frames "are estimated, not measured" (line 61).
9. **tracemalloc cannot see call frames.** It reported only 32 to 96 bytes per level (the ints), against 152 to 257 bytes of real memory growth. A student who "checks" recursion with tracemalloc will find about a fifth of the estimate. The Solutions key (line 8) says every figure was "checked against tracemalloc", which cannot be true for recursion.
10. **"peak about 1.5 times final" is correct for the table of a dict or set** (dict 1.50 at 1,000 and 100,000; set 1.50 at 100,000, 1.25 at 1,000) but not for the whole structure if key objects are created during the build (1.14 to 1.26), nor for list or deque (1.00 to 1.01) (`m4_tracemalloc_growth.out`).
11. **"checks agree within about 25% to a factor of 2" (syllabus lines 177-179) and the key's "within about 30%" (key line 20) contradict each other** and the first is a poor thing to promise students (judgment below).

Items that check out: float 24, empty str 41 + 1 per ASCII char, small-int cache -5 to 256, list 56 + 8 per slot, tuple 40 + 8 per item (pair 56, triple 64), set 33 at 1,000 and 41.9 at 100,000, dict 37.0 at 1,000 and 52.4 at 100,000 (int keys), deque 8.25 per element at scale, default recursion limit 1000, "True/False/None shared".

Readings, links and bibliography:

12. **Three section titles are not the book's current titles.** Written "§3.3 What Is a Stack?", "§3.10 What Is a Queue?", "§3.15 What Is a Deque?"; the book's headings are "3.3 Stacks", "3.10 Queues", "3.15 Deques". Numbers and URLs are right. Affected: Classes 7, 8, 9. All other 59 of 62 distinct Runestone sections match number and title exactly.
13. **All 62 Runestone section URLs, all 90 LeetCode URLs and all 9 non-LeetCode URLs resolve (HTTP 200).** Caveat: `curl` and WebFetch get a Cloudflare challenge (403) from Runestone and LeetCode, so students will see the pages only in a browser; I checked them from a real browser session.
14. **Several readings do not teach the pattern of their class.** Strongest cases: Class 1 §2.5 (no memory content), Class 3 (nothing on prefix sums), Class 5 (neither section is two pointers), Class 15 (§6.8 has no BFS or level order), Class 20 (book teaches only the DFS version; no in-degree/Kahn), Class 22 (Prim's algorithm does not use union-find), Class 12 (§3.8 uses a stack and remainders, no bit operators). Details in the readings table.
15. **The syllabus claim "Runestone does not cover sliding windows, union-find, tries and intervals" is right** (and so are monotonic stacks, bit manipulation and greedy as chapters). But for sliding window, monotonic stack, trie and intervals the "other source" is "your AI tool" or a Python docs page that does not teach the pattern. Only union-find (VisuAlgo), greedy and DP (Erickson) and bit operations (Python docs) point to a real free source.
16. **Bibliography.** Runestone authors and edition: correct. CLRS 4th edition, 2022, four authors: correct (but the MIT 6.006 course itself lists CLRS 3rd edition). Erickson: free online, URL correct (but pseudocode, not Python, and the take-homes give no URL or chapter link for it). OCW 6.006: lecture videos and notes are free; "Taught in Python" is supported only indirectly (see below). Open Data Structures: free, but its text is Java and C++ (a pseudocode edition exists, Python only as source code on GitHub), which clashes with "Python only". VisuAlgo URL: correct.
17. **docs.python.org links use `/3/`, which now serves the 3.15.2 documentation** (page titles say so), while the course is pinned to 3.13. `/3/library/stdtypes.html` 301-redirects to `/3/builtins/stdtypes.html` (anchor still resolves). Use `/3.13/...` links.

## Table 1: memory entries

All "measured" figures are from the named script's output. Sizes are bytes. "gs" = `sys.getsizeof`; "tm" = tracemalloc.

| Entry | Document figure | Measured figure (script, quoted output) | Verdict | Suggested wording |
|---|---|---|---|---|
| int, small | 28 B | `int 0 28`, `int 1 28`, `int 2^30 28` (this label is the value 2^30 - 1) (`m1`) | Correct for gs | "28 bytes (32 on the heap)" |
| int, large | not stated | `int 2^31 32` (value 2^30), `int 2^61 36` (value 2^60), `int 2^91 40` (value 2^90) (`m1`) | Missing | "28 bytes below 2^30 (about 1.07 billion), 32 below 2^60, then +4 per 30 bits" |
| int, heap cost | not stated | tm: `int > 256  tracemalloc/obj= 32.0 getsizeof(one)=28`; `int 2^31+ ... 36.0 ... 32` (`m7`) | Gap: tm and gs disagree | "28 by getsizeof; tracemalloc and the heap use 32. Use 32 if you check with tracemalloc." |
| small-int cache | -5 to 256 shared | `shared ints range -5 256` (`m1`) | Correct | keep |
| float | 24 | `float 24`; tm `float tracemalloc/obj= 24.0` (`m1`, `m7`) | Correct | keep |
| True, False, None | shared, no extra cost | gs: `True 28`, `bool 28` (False), `None 16` (`m1`) | Correct as "shared, no extra cost"; do not tell students they are zero-size | "Shared singletons: each costs only the 8-byte pointer to it" |
| str, empty | 41 | `str empty 41` (`m1`) | Correct | keep |
| str, ASCII per char | 1 per char | `'a' 42`, `'ab' 43`, 10 chars 51, 100 chars 141, `per ascii char 1` (`m1`) | Correct | keep |
| str, 1-char shared | "a 1-character string is shared" | `1-char shared? ascii a True`, `0x80 True`, `ÿ 0xff True`, `0x100 Ā False`, `€ False`, `emoji False` (`m1`) | Partly: Latin-1 only | "A 1-character string is shared if its character is at most U+00FF" |
| str, non-ASCII | not stated | Latin-1 `'é'*10` = 67 (= 57 + 1/char); `'€'*10` = 78 (`ucs2 empty-diff 2`, = 58 + 2/char); `'😀'*10` = 100 (`4` per extra char, = 60 + 4/char) (`m1`) | Missing | "ASCII 41 + 1 per char; with any accented Latin-1 letter 57 + 1; with any other BMP character (e.g. €, Chinese) 58 + 2 per char; with any emoji 60 + 4 per char. One wide character sets the cost of the whole string." Note: gs can add 3 to a 1-char Latin-1 string when its UTF-8 form is cached (`'é' 61` vs `'éé' 59`). |
| list header and slot | 56 + 8 per slot | `list [] 56`, `[0] 64`, `[0]*10 136`, `per slot 8` (`m2`) | Correct | keep |
| list built by append, spare room | "about 12% spare" | n=1000: `append 8856 slots 1100 spare% 10.0`; n=100000: `append 800984 slots 100116 spare% 0.12`; n=10000 6.4; n=1e6 5.608; `max spare% over n in 100..2000: 17.43`, `mean over 1000..2000: 6.1` (`m2`, `m6`) | Wrong as a typical figure | "A list grown by append has between 0% and about 13% spare slots; use about 6% on average, and 10% at n = 1,000" |
| list by comprehension | not stated | n=1000 `comp 8856`; n=100000 `comp 800984` (same as append) (`m2`) | Missing | "A comprehension over-allocates like append" |
| `[0]*n`, `list(range(n))` | not stated | n=1000 `8056`; n=100000 `800056` (= 56 + 8n exactly) (`m2`) | Missing | "`[0]*n` and `list(x)` are exact: 56 + 8n, no spare room" |
| tuple | 40 + 8 per item; pair 56; triple 64 | `tuple () 40`, `(1,) 48`, `pair 56`, `triple 64`, 10 items `120` (`m2`); tm pair of two fresh ints 87.9 per pair = 56 + 32 (`m7`) | Correct | keep |
| dict, tiny | "184 bytes for a tiny dict" | `dict {} 64`, `1 entry 224` (key 1), `5 224`, `6 352`; with a str key `dict {'a':1} 184`, two str keys 184, six str keys 272 (`m2`, `m6`) | Partly: 184 only for 1-5 string keys | "Empty dict 64; 1 to 5 entries: 184 with string keys, 224 with int keys" |
| dict, 1,000 entries | 37 per entry | int keys: `dict comp 36952 37.0`; str keys `26032 26.0`; tm with keys preallocated `final= 36888 (36.9/el)` (`m2`, `m6`, `m4`) | Correct for int keys; 30% too high for str keys | "37 per entry with int keys, 26 with string keys, at 1,000 entries" |
| dict, 100,000 entries | about 50 | int keys: `5242960 52.4`; str keys `3844864 38.4`; tm `final= 5242896 (52.4/el)` (`m2`, `m6`, `m4`) | Correct for int keys (52 vs 50); str keys 38 | "About 52 per entry (int keys), 38 (string keys)" |
| dict, getsizeof vs tm | not stated | n=1000 getsizeof 36952 vs tm 36888; n=100000 5242960 vs 5242896 (`m4`) | Agree to 0.2% | keep |
| set, tiny | not stated | `set() 216`, `{1} 216` (`m2`) | Missing | "Even a one-element set is 216 bytes" |
| set, 1,000 | 33 per element | `set(range) 32984 33.0`; `set add 32984 33.0` (`m2`) | Correct | keep |
| set, 100,000 | about 42 | `4194520 41.9` (`m2`), tm `final= 4194520 (41.9/el)` (`m4`) | Correct | keep |
| growth peak, dict/set | "peak about 1.5 times final" (Solutions key lines 61, 225) | dict 1,000 `peak/final=1.50`; dict 100,000 `1.50`; set 1,000 `1.25`; set 100,000 `1.50` (`peak= 6291720` = 6.3 MB, the key's "about 6 MB"). Keys created inside the build: dict `1.26` (100k), set `1.19` (100k) (`m4`) | Correct for the table alone at large n; lower once key objects count | "While growing, a dict or set can briefly hold the old and new table: up to about 1.5 times the final table at large n" |
| growth peak, list/deque | not stated | list append 1,000 `peak/final=1.01`; 100,000 `1.00`; deque same (`m4`) | Missing | "A list or deque shows no meaningful peak (under 2%)" |
| deque per element | 8.3 | `100000 deque(range) 825496 8.25`; `append 825496 8.25`; at 1,000 `8680 8.68` (`m2`); tm `deque append n=100000 ... (8.3/el)` (`m4`) | Correct at scale | keep |
| deque overhead | "about 600" | `deque() 760`; getsizeof minus 8n = 680 at n=1,000 and 25,496 at n=100,000 (`m2`) | Wrong | "8.25 per element (528 bytes per 64-slot block) plus about 760 bytes for an empty deque" |
| node, plain class | "about 100 incl. value and pointers" | tm per object excluding its list slot: `LN 88.0`, `TN 96.0`; gs `LN 48`, `TN 48` plus `__dict__` view 296 (not a real extra). In a chain with its own non-cached int: `LN 120.0`, `TN 128.0` (`m3`) | Roughly right | "ListNode about 90, TreeNode about 100, plus 32 for each value above 256 (small values are shared)" |
| node, `__slots__` | not stated | tm: `LNs 48.0`, `TNs 56.0`; with own int `80.0`, `88.0` (`m3`) | Missing | "With `__slots__`: ListNode 48, TreeNode 56 (plus 32 per value above 256)" |
| recursion, default limit | not stated | `recursionlimit 1000` (`m1`; `default recursion limit 1000` in `m5`) | Missing | "Python stops recursion at depth 1000 by default" |
| recursion, per frame | about 150 | RSS growth per level: `f1` 152.5, `f0` 193.2, `f3` 257.0 (`m5`). tm: 32, 64, 96 (`m5`) | Right for the minimal function; low for typical | "About 150 to 250 bytes per active call, higher with more local variables; tracemalloc will not show it" |

### How the recursion measurement was made (`m5_recursion.py`)

Each run is a fresh process (`python3.13 -I`) that sets the recursion limit above the depth, warms up, then recurses to depth D with a function that returns `1 + f(n-1)`-style results. I read peak resident memory (`resource.getrusage`, `ru_maxrss`, bytes on macOS) before and after at three depths (20,000; 100,000; 200,000) and divided the difference by the difference in depth. Output: `f1 rss {20000: 2932736, 100000: 15122432, 200000: 30375936}` giving `152.5 B` (the script's "(400k-100k)" label is a typo; the depths were 200k and 100k, the result is the same for 100k-20k: 152.4). The three functions: `f1` (1 local, stack size 5), `f0` (3 locals, stack 4), `f3` (5 locals, stack 6). Each result is stable to within 0.1 byte across the two depth pairs. I also ran tracemalloc at depths 5,000 / 20,000 / 40,000 and got 32.0, 64.0 and 96.0 bytes per level: exactly the int objects created per call (one for `f1`, two for `f0`, three for `f3`, 32 bytes each), none of the frame. So CPython 3.13 allocates frames in its own data-stack chunks, which tracemalloc does not trace.

Inference (consistent with all three data points, not separately verified in the CPython source): frame bytes = 8 x (9 + nlocals + stacksize), e.g. `f1`: 8 x (9 + 1 + 5) = 120, plus one 32-byte int = 152; `f0`: 8 x 16 = 128 + 64 = 192 (measured 193); `f3`: 8 x 20 = 160 + 96 = 256 (measured 257). The nine "special" words are an inference from fitting, not read from the source.

### Judgment (labeled): "our checks agree within about 25% to a factor of 2 on the large cases"

Not a good sentence to give students. A factor of 2 is not "an estimate"; it tells a student that a 60%-off answer is as good as a 5%-off one, and the sentence contradicts the key's "within about 30%". The measurements show the spread is not random noise: it has five nameable causes (heap 32 vs getsizeof 28 for ints; string vs int dict keys; list spare room from 0% to 13%; frame size depending on locals; tracemalloc not seeing frames). Better to tell students the rule and the cause: "Expect your estimate to land within about 30% of a measurement when you state your assumptions; the main sources of error are the spare room in lists, the key type in dicts and sets, and the extra 4 bytes the heap gives each int." Then use one sentence for the grading rule: grade the method, as the key already says.

## Table 2: readings

Status "200" means an HTTP 200 returned to a real browser session (Runestone: same-origin fetch of all 62 distinct section URLs from a Runestone tab; the page `h1` is the "actual title"). `curl` gets 403 (Cloudflare "Just a moment...") for Runestone and LeetCode (`linkcheck.out`); a browser does not. Actual titles come from the book index and each page's `h1`. "Matches" means the number and title are identical.

| Take-home (class: pattern) | Reading as written | Actual section and title | Link | Does it teach the pattern? | Verdict |
|---|---|---|---|---|---|
| 1 Big-O and memory | §2.2 What Is Algorithm Analysis? | 2.2 same | 200 | Yes | OK |
| 1 | §2.3 Big O Notation | 2.3 same | 200 | Yes | OK |
| 1 | §2.5 Performance of Python Data Structures | 2.5 same | 200 | Big-O of list and dict operations with timing experiments (page opens "Big O performance for the operations on Python lists and dictionaries"). No memory content, though the class is "Big-O and Python memory" | Matches; does not support the memory half. Pair with the sys.getsizeof docs link (already there) |
| 1 | Python docs: sys.getsizeof | `docs.python.org/3/library/sys.html#sys.getsizeof` 200; anchor id present; page title says Python 3.15.2 | 200 | Yes | OK; pin to `/3.13/` |
| 2 Arrays | §2.6 Lists | 2.6 Lists | 200 | List operation costs (append, pop, insert); two-index in-place technique is not taught | Matches; partial fit |
| 2 | §1.8 Getting Started with Data | 1.8 same | 200 | Lists and strings basics, mutability: "Lists are mutable; strings are immutable" | Matches; background only |
| 3 Strings, prefix sums | §2.4 An Anagram Detection Example | 2.4 same | 200 | Teaches comparing strings by sorting and by counting letters. Prefix sums are not there | Matches; does not teach prefix sums. The take-home has no "not in Runestone" note, unlike classes 6, 9, 12, 22, 23, 25, 26, 28 to 29 |
| 3 | §1.8 Getting Started with Data | 1.8 same | 200 | String immutability yes | Matches |
| 4 Hashing | §5.5 Hashing | 5.5 same | 200 | Yes (hash tables, collisions) | OK |
| 4 | §2.7 Dictionaries | 2.7 same | 200 | Yes | OK |
| 5 Two pointers | §3.18 Palindrome Checker | 3.18 same | 200 | Solves it with a deque, taking from both ends; no two-index technique | Matches; weak fit (deque, not two pointers) |
| 5 | §5.3 The Sequential Search | 5.3 same | 200 | Linear search; not two pointers | Matches; poor fit |
| 6 Sliding window | §2.4 An Anagram Detection Example | 2.4 same | 200 | No window technique on the page (the string "window" does not occur in its text) | Matches; take-home itself says "Sliding window has no section in Runestone" (correct). Its replacement is "Python docs and your AI tool" (see Table 3) |
| 7 Stacks | §3.3 What Is a Stack? | **3.3 Stacks** | 200 | Yes | Title mismatch |
| 7 | §3.5 Implementing a Stack in Python | 3.5 same | 200 | Yes | OK |
| 7 | §3.6 Simple Balanced Parentheses | 3.6 same | 200 | Yes | OK |
| 7 | §3.7 Balanced Symbols (A General Case) | 3.7 same | 200 | Yes | OK |
| 8 Queues, deques | §3.10 What Is a Queue? | **3.10 Queues** | 200 | Yes | Title mismatch |
| 8 | §3.12 Implementing a Queue in Python | 3.12 same | 200 | Yes | OK |
| 8 | §3.13 Queue Simulation: Hot Potato | 3.13 same | 200 | Queue use | OK |
| 8 | §3.15 What Is a Deque? | **3.15 Deques** | 200 | Yes | Title mismatch |
| 9 Monotonic stack/deque | §3.15 What Is a Deque? | **3.15 Deques** | 200 | Deque only; no monotonic idea | Title mismatch; the take-home says "Monotonic stacks are not in Runestone" (correct) |
| 9 | §3.17 Implementing a Deque in Python | 3.17 same | 200 | Deque only | OK |
| 9 | Python docs: collections.deque | `/3/library/collections.html#collections.deque` 200; anchor present | 200 | Deque API | OK |
| 10 Linked lists | §3.19 Lists | 3.19 same | 200 | Yes | OK |
| 10 | §3.21 Implementing an Unordered List: Linked Lists | 3.21 same | 200 | Yes (nodes and links) | OK |
| 10 | §3.23 Implementing an Ordered List (with analysis) | 3.23 Implementing an Ordered List | 200 | Yes; "(with analysis)" is the professor's own note, not in the title | OK; mark the note as the professor's |
| 11 Recursion | §4.2 What Is Recursion? | 4.2 same | 200 | Yes | OK |
| 11 | §4.4 The Three Laws of Recursion | 4.4 same | 200 | Yes | OK |
| 11 | §4.6 Stack Frames: Implementing Recursion | 4.6 same | 200 | Yes; this is the memory-per-call topic | OK |
| 12 Bit manipulation | §3.8 Converting Decimal Numbers to Binary Numbers | 3.8 same | 200 | Repeated division by 2 with a stack; no `&`, `|`, `<<` (the word "shift" does not occur) | Matches; teaches binary representation, not bit manipulation. Take-home says no dedicated section (correct) |
| 12 | Python docs: bitwise operations on integers | `/3/library/stdtypes.html#bitwise-operations-on-integer-types` 301 to `/3/builtins/stdtypes.html`, 200; anchor id present | 200 (redirect) | Yes: lists the operators | OK; update link |
| 13 Sorting | §5.6 Sorting | 5.6 same | 200 | Yes | OK |
| 13 | §5.9 The Insertion Sort | 5.9 same | 200 | Yes | OK |
| 13 | §5.11 The Merge Sort | 5.11 same | 200 | Yes | OK |
| 13 | §5.12 The Quicksort | 5.12 same | 200 | Yes | OK |
| 14 Binary search | §5.4 The Binary Search | 5.4 same | 200 | Yes | OK |
| 14 | Python docs: bisect | `/3/library/bisect.html` 200 | 200 | Yes | OK |
| 15 Trees: traversal | §6.2 Examples of Trees | 6.2 same | 200 | Yes | OK |
| 15 | §6.3 Vocabulary and Definitions | 6.3 same | 200 | Yes | OK |
| 15 | §6.6 Nodes and References | 6.6 same | 200 | Yes | OK |
| 15 | §6.8 Tree Traversals | 6.8 same | 200 | Pre/in/post-order (recursive DFS). Breadth-first or level order is not covered here (BFS appears in §7.9) | Matches; half the pattern ("DFS and BFS") |
| 16 BST | §6.12, 6.13, 6.14, 6.15 (Binary Search Trees; Search Tree Operations; Implementation; Analysis) | all four match | 200 | Yes | OK |
| 17 Heaps | §6.9 Priority Queues with Binary Heaps; §6.10 Binary Heap Operations; §6.11 Binary Heap Implementation | all match | 200 | Yes | OK |
| 17 | Python docs: heapq | `/3/library/heapq.html` 200 | 200 | Yes | OK |
| 18 Graphs, DFS | §7.2 Vocabulary and Definitions; §7.5 An Adjacency List; §7.15 General Depth-First Search; §7.16 Depth-First Search Analysis | all four match | 200 | Yes for DFS and graph representation; grids are not covered | OK |
| 19 BFS | §7.7 The Word Ladder Problem; §7.9 Implementing Breadth-First Search; §7.10 Breadth-First Search Analysis | all three match | 200 | Yes | OK |
| 20 Topological sort | §7.17 Topological Sorting | 7.17 same | 200 | Teaches the DFS-based order. The page has no in-degree counting (Kahn's algorithm), which several of the class's problems (e.g. "Find All Possible Recipes") are usually solved with | Matches; partial fit |
| 21 Dijkstra | §7.19 Shortest Path Problems; §7.20 Dijkstra's Algorithm; §7.21 Analysis of Dijkstra's Algorithm | all three match | 200 | Yes | OK |
| 22 Union-find | §7.22 Prim's Spanning Tree Algorithm (context) | 7.22 Prim's Spanning Tree Algorithm | 200 | Prim's algorithm; the page never mentions union, disjoint sets or Kruskal | Matches; does not teach union-find (the take-home admits "Runestone has no union-find section") |
| 22 | VisuAlgo: Union-Find Disjoint Sets, `visualgo.net/en/ufds` | title "Union-Find Disjoint Sets (UFDS) - VisuAlgo" | 200 | Yes (animation) | OK |
| 23 Tries | §6.3 Vocabulary and Definitions; §6.6 Nodes and References; §2.7 Dictionaries | all match | 200 | Tree vocabulary only; no trie | Matches; take-home admits no trie section (correct) |
| 24 Backtracking | §4.9 Complex Recursive Problems; §4.11 Exploring a Maze; §7.11 The Knight's Tour Problem | all three match | 200 | Yes (maze and knight's tour are backtracking) | OK |
| 25 Greedy | §7.22 Prim's Spanning Tree Algorithm (a greedy algorithm); §4.12 Dynamic Programming (greedy vs. DP on coin change) | 7.22 and 4.12 match | 200 | Both pages use the word "greedy" (Prim's: "belongs to a family of algorithms called the greedy algorithms"; 4.12: "a greedy method" for coin change). Parenthetical notes are the professor's | OK; take-home also points to Erickson |
| 26 Intervals | §5.11 The Merge Sort; §6.9 Priority Queues with Binary Heaps | both match | 200 | Sorting and heaps only; no intervals or sweep line | Matches; take-home admits it |
| 27 DP 1D | §4.12 Dynamic Programming | 4.12 same | 200 | Coin change only (no Fibonacci, climbing stairs, knapsack, edit distance in the text) | Matches; thin for 1-D DP problems, no note in the take-home |
| 28 DP | §4.12 Dynamic Programming (read again) | 4.12 same | 200 | as above | Matches; take-home says "covers the idea but not these problems" |
| 29 DP 2D | §4.12 Dynamic Programming (read again) | 4.12 same | 200 | as above | Matches; same |
| 30 Review | §2.8 Summary; §5.13 Summary; §6.20 Summary; §7.23 Summary | all four match | 200 | Chapter summaries | OK |
| All 30 | Book index link `.../pythonds3/index.html` | title "Problem Solving with Algorithms and Data Structures using Python — Problem Solving with Algorithms and Data Structures 3rd edition" | 200 | n/a | OK |
| 90 LeetCode links | `leetcode.com/problems/<slug>/` | all 90 returned 200 with a real problem title (no "not found" titles) (`linkcheck.out` has the curl 403s; the 200s came from a browser session); 89 of 90 slugs equal the slugified problem name in the take-home row, the one exception is `sqrtx` for "Sqrt(x)", which is LeetCode's own slug (`lc_names.out`) | 200 | n/a | OK. I did not check difficulty labels or whether a problem needs LeetCode Premium |

Counts: 80 reading items in 30 take-homes (`reads.tsv`, parsed by `parse_reads.py`); 74 are Runestone sections (62 distinct URLs), 6 are Python docs, 1 VisuAlgo (and the syllabus link list adds docs.python.org, Erickson, Morin, VisuAlgo home). Number and title match for 59 of 62 distinct sections; the three exceptions are the titles listed in defect 12. Section numbers matched for every one of the 62.

## Table 3: sources outside Runestone

| Take-home | What it points to | Free and correct? |
|---|---|---|
| 6 Sliding window | "Read the section above for counting, then use the Python docs and your AI tool" | No named source. The Python docs do not teach sliding windows. Gap |
| 9 Monotonic stack | "Ask your AI tool to trace one by hand" | Not a source. Gap |
| 12 Bit manipulation | Python docs, bitwise operations | Yes, free and correct (3.13 docs section exists) |
| 22 Union-find | VisuAlgo UFDS animation, then the AI tool | VisuAlgo is free and loads (200). Erickson's site also has a free "Disjoint Sets" note (`notes/11-unionfind.pdf`, linked from the Erickson page), a better text source |
| 23 Trie | Runestone tree vocabulary, then the AI tool | No trie source. Gap |
| 25 Greedy | Erickson, "Algorithms (free online), for exchange arguments" | Free; chapter 4 "Greedy Algorithms" (`book/04-greedy.pdf`) exists on the Erickson page. I did not read the PDF, so I did not verify that it uses the phrase "exchange argument". No URL or chapter number in the take-home |
| 26 Intervals | "Re-read the sorting and heap sections and ask your AI tool to explain a sweep line" | Gap |
| 28 DP | Erickson, Dynamic Programming chapter | Free; chapter 3 "Dynamic Programming" (`book/03-dynprog.pdf`) exists. Contents not read |
| 29 DP 2D | Erickson DP chapter "for edit distance" | Chapter 3 exists; I did not confirm edit distance is in it |

## Bibliography claims in the syllabus Materials (lines 453-488)

| Claim | Finding | Source fetched |
|---|---|---|
| Miller and Ranum, Problem Solving with Algorithms and Data Structures using Python, 3rd edition, free on Runestone | Correct. Index page reads "By Brad Miller and David Ranum, Luther College"; page title says "3rd edition" | `https://runestone.academy/ns/books/published/pythonds3/index.html` (browser) |
| Pat Morin, Open Data Structures, free online, "use it for the data structure chapters" | Free and open (the page says the book and code are "free" and under a Creative Commons Attribution License). The page lists a pseudocode edition (HTML, PDF, "Python sources"), a Java edition and a C++ edition (beta), and says the structures are "implemented in Java and C++". Python exists as source code on GitHub, not as the main text. A catalogue listing (Marshall University record, via search) gives the printed AU Press version as Attribution-NonCommercial-NoDerivs, which differs from the site's licence statement; I did not resolve this. The author name "Pat Morin" is confirmed only by the AU Press catalogue listings, not by the opendatastructures.org page text | `https://opendatastructures.org/` (200, "Open Data Structures"); search results for AU Press listing |
| Jeff Erickson, Algorithms, free online, at jeffe.cs.illinois.edu/teaching/algorithms/ | Correct. The page says "a free electronic version of my self-published textbook Algorithms", "1st edition, June 2019". Chapters include Recursion, Backtracking, Dynamic Programming, Greedy Algorithms, Basic Graph Algorithms, Depth-First Search, Minimum Spanning Trees, Shortest Paths. This matches "recursion, graphs, greedy and dynamic programming". The book is in pseudocode, not Python (I did not verify its pseudocode convention beyond knowing it has no Python edition; page lists none). Server was unreachable by curl once (timeout) and fine in a browser | `https://jeffe.cs.illinois.edu/teaching/algorithms/` (200 in the first curl run; browser read later) |
| MIT OCW 6.006 Introduction to Algorithms, Spring 2020: lecture videos and notes free | Correct. Course page lists Lecture Videos, Lecture Notes, Problem Sets and solutions, Exams; licence CC BY-NC-SA 4.0. Instructors Demaine, Ku, Solomon | `https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/` |
| "Taught in Python" | Supported indirectly, not stated on the course home page. The syllabus lists as a prerequisite "6.0001 Introduction to Computer Science and Programming in Python: Basic experience programming in Python 3." Problem Session 4 is described as covering "programming in Python". A search result describes Problem Set 1 as using a Python class template; I did not open the template. Problem Set 5's page does not mention Python. | `.../pages/syllabus/`; `.../resources/problem-session-4/`; `.../resources/mit6_006s20_ps5_questions/` |
| MIT 6.006 reference text | Not in the syllabus claim but relevant: OCW's own syllabus lists CLRS "Third Edition, MIT Press" as the optional reference, not the 4th | `.../pages/syllabus/` |
| CLRS 4th edition (Cormen, Leiserson, Rivest, Stein) | Correct. MIT Press page: "Introduction to Algorithms Fourth Edition By Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein", pub date April 5, 2022, 1312 pp., Hardcover $150, ISBN 9780262046305. The syllabus gives no year; add "2022" | `https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/` (browser; WebFetch got 403) |
| VisuAlgo `https://visualgo.net/en` | Correct, 200, "visualising data structures and algorithms through animation - VisuAlgo" | `https://visualgo.net/en` |
| Python docs listed (built-in types, collections, heapq, bisect, sys.getsizeof) | All resolve; `/3/` serves 3.15.2 docs today | `linkcheck.out`, `anchors.out` |

## Findings in the requested structure

## Part 1: measured sizes

### Takeaway
Most scalar and container figures are right to within a few percent for typical inputs, but five entries mislead: list spare room (12% vs 0.1 to 10% measured), tiny dict (184 holds only for string keys), deque overhead (760, not 600), int cost (28 by getsizeof, 32 on the heap) and the frame size (about 150 to 260, and invisible to tracemalloc).

### Cited Findings
- Python 3.13.12 on arm64 macOS; `int 0 28 ... int 2^31 32` (value 2^30) — `S/m1_scalars.out`
- Small-int sharing range -5 to 256; one-char strings shared through U+00FF — `S/m1_scalars.out`
- List append spare 10.0% at 1,000 and 0.12% at 100,000; `[0]*n` exact; tuple 40 + 8k; dict 37.0 and 52.4 (int keys); set 33.0 and 41.9; deque 8.25 — `S/m2_containers.out`
- Plain-class node 88 / 96, `__slots__` 48 / 56 (excluding value) — `S/m3_nodes.out`
- Dict and set peak 1.50 times the table at 100,000; list and deque 1.00 — `S/m4_tracemalloc_growth.out`
- Recursion 152 / 193 / 257 bytes per level by RSS; tracemalloc 32 / 64 / 96 — `S/m5_recursion.out`
- Tiny dict with str keys 184; str-keyed dicts 26.0 and 38.4 per entry; list spare mean 6.1%; range iterator 40, empty instance 48, instance dict 288 — `S/m6_extra.out`
- tracemalloc per object: int 32.0, float 24.0, empty dict 64, `{"a":None}` 184, one-element set 216 — `S/m7_tracemalloc_objects.out`. (Two rows of that script, "tuple triple (no ints)" and "pair of two shared", print 0.0 because Python folds the constant tuple into the code object; ignore them.)

### Inferences
- Frame size formula 8 x (9 + locals + stack) fits three data points (see above); the nine fixed words are fitted, not sourced.
- The Solutions key's range-iterator figure of "about 150 bytes" for auxiliary space (lines 126, 308) is a round-up (range iterator measures 40); I did not check each of the key's computed totals.

### Gaps
- I did not check the in-class key's totals or each problem's estimate, only the reference tables.
- Only CPython 3.13.12 on arm64 macOS was measured; I did not test Linux or x86-64, where sizes should be equal but pymalloc behaviour can differ.

## Part 2: readings and links

### Takeaway
Every link works in a browser and the section numbers are all correct; three titles are wrong (Stacks, Queues, Deques). The larger problem is content fit: about ten readings do not teach their class's pattern, and four patterns have no free source at all.

### Cited Findings
- 62 of 62 Runestone sections return 200; 59 match number and title; 3 title mismatches — browser fetch of `https://runestone.academy/ns/books/published/pythonds3/...` pages; table of contents at `.../index.html` has no entry for sliding window, union-find, trie, interval, monotonic, greedy chapter or sweep line (keyword scan of all section titles; only the TOC, not full text)
- 90 of 90 LeetCode URLs return 200 with a real problem title — browser session on `https://leetcode.com/problems/<slug>/`
- Erickson chapters: Recursion, Backtracking, Dynamic Programming, Greedy Algorithms, Basic Graph Algorithms, DFS, MST, Shortest Paths; "Disjoint Sets" note — `https://jeffe.cs.illinois.edu/teaching/algorithms/`
- OCW 6.006 free, lists CLRS 3rd edition, Python 3 prerequisite — `https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/`
- CLRS 4th edition, 2022 — `https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/`

### Inferences
- The syllabus's statement that "Every take-home names the sections to read" is true, but a student who reads only the cited sections for Classes 3, 5, 15, 20, 22 and 27 will not meet the pattern the class is about.

### Gaps
- I did not open Erickson's Greedy or DP chapters (PDFs) to confirm "exchange arguments" or "edit distance"; only their existence.
- I did not open any 6.006 problem-set template to confirm Python directly.
- The Runestone claim "does not cover tries, intervals..." was checked by table-of-contents titles and by keyword counts on selected pages, not by reading all 100+ sections.
- The licence of Open Data Structures differs between the site (CC-BY) and a catalogue listing for the printed edition (NC-ND); not resolved.
- LeetCode problem difficulty labels, and Premium status, were not checked.
