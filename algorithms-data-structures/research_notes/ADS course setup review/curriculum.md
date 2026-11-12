# Curriculum coverage and sequence: draft "Algorithms & Data Structures" (30 classes, Python)

Research notes, 12 Nov 2026. Scope: topic coverage, sequence, prerequisites and learning-outcome coverage of the draft course, compared with CS2023 and with established courses.

**Citation keys.** `S:n` is line n of `ADS_Syllabus_Draft.md`. `T:n` is line n of `ADS_Take_Homes.md`. Both files sit in the session scratchpad (`.../scratchpad/ads/`). Every claim about an outside course or standard carries a link to the page I fetched. Claims marked **[Judgment]** are my reading of the evidence, not verified fact.

**How these notes are organized.** The assignment asked for six parts (summary, CS2023 table, comparison table, sequence check, outcome table, changes). The research template asked for Takeaway / Cited Findings / Inferences / Gaps under each question. I used the six parts as the top-level sections and put the template's four headings inside each. "Inferences" holds the judgment.

---

## 1. Summary of findings

### Takeaway
The draft covers nearly everything CS2023 assigns to a second-semester Data Structures (CS2) course, plus graphs, greedy, backtracking and dynamic programming from the third, algorithms-level course. It misses several CS Core topics that every comparator university course teaches: balanced search trees, hash-collision handling, minimum spanning trees, Big-Omega/Theta notation and tractability (P, NP). Two "builds on" chains run backwards (classes 23→24 and 28→29). Three of the eight learning outcomes (3, 5, 8) are practiced thinly or not at all, and none is assessed for the grade.

### Cited Findings
- The syllabus calls the course "A core computer science course in which you learn algorithms and data structures by solving problems" (S:39-40). It is organized by LeetCode pattern, two problems per class (S:40-45, S:244-350), with the pattern announced in advance and the problems withheld (S:121-123, S:352-353).
- CS2023 defines CS Core as topics every CS graduate is expected to know, and it lists 32 CS Core hours for Algorithmic Foundations (AL), spread across CS1, CS2 and a third algorithms course in its packaging examples — [CS2023 final report, AL knowledge area and "Course Packaging Suggestions"](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm).
- CS2023's CS2 "Data Structures" packaging lists: ADTs, binary search, multi-dimensional arrays, linked lists, "Hash Tables/Maps including conflict resolution strategies," records, sets, stacks/queues/deques, trees with BFS/DFS, O(n²) and O(n log n) sorts, brute force, decrease-and-conquer, divide-and-conquer, iteration vs recursion, the space/time trade-off, and the complexity framework — [CS2023 report](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm). The draft covers all of these except conflict resolution in hash tables, which it never practices (section 2).
- CS Core topics with no class in the draft: minimum spanning trees (Prim, Kruskal), balanced trees (AVL, Red-Black), Big-Omega and Big-Theta, P/NP/NP-complete and reductions, the AL-Models unit (automata, decidability), and the AL-SEP unit (society and ethics). Section 2 gives the line-level evidence.
- The three comparator university courses each teach balanced search trees: MIT 6.006 Lecture 7 "Binary Trees, Part 2: AVL" ([MIT OCW calendar](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/calendar/)); Princeton COS 226 Lecture 10 "Balanced Search Trees" ([COS 226 Spring 2025 lectures](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures.php)); Rochester CSC 162, a Python course on the same Miller and Ranum textbook, "AVL Trees 1 / AVL Trees 2" ([CSC 162 lectures](https://cs.rochester.edu/~hbeadle/csc162/lectures.html)).
- Of the draft's 60 class problems, 37 are in NeetCode 150 and 23 in Blind 75 (my count against [NeetCode's site data file](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json)). Of the 75 problems in the Grind 75 plan, 51 appear in the course: 22 as class problems and 29 as take-home practice (my count against [Tech Interview Handbook study plan](https://www.techinterviewhandbook.org/coding-interview-study-plan/)).
- Grading: "Attend every class and put in solid effort, as judged by me, and you earn an A" (S:359-360). Correct answers earn only extra credit (S:369-374).

### Inferences
- **[Judgment] Title and "core" claim.** The draft is a hybrid: a CS2-level data-structures course taught through interview patterns, with algorithms-course strategies bolted on at the back. "Algorithms & Data Structures" is a defensible title once the CS Core gaps in section 6 close. "A core computer science course" (S:39) overstates the draft as written. Its organizing unit is the LeetCode pattern; 17 of NeetCode 150's 18 categories get a dedicated class (section 3). Board work asks students to *use* structures far more than to *build* them, and the topics every university comparator includes but interview lists omit (balanced trees, MST, intractability) are exactly the ones missing. As written it reads closer to an algorithmic problem-solving / interview-patterns course with strong complexity and memory analysis.
- **[Judgment] Distinctive strengths.** The draft does some things better than any comparator I fetched. Students state time, auxiliary space *and* a byte-level memory estimate for every solution (S:128-130, S:165-168, S:174-216). They write a plan before code every class (S:111-115, T:55-65). They also write Python by hand under time pressure (S:59-60, S:125-126). No comparator page I read mentions memory estimation in bytes.

### Gaps
- I could not read the Runestone textbook (pythonds3): runestone.academy returned a Cloudflare challenge to both WebFetch and curl. I therefore could not check whether the assigned "Hashing" section (T:236-237) covers collision resolution, or which balanced-tree sections exist in the 3rd edition.
- I did not open LeetCode problem pages (they need JavaScript). Statements about what a specific problem requires are marked [Judgment].

---

## 2. CS2023 mapping table

### Takeaway
The draft covers the SDF data-structure and algorithm units in full and most of AL-Foundational and AL-Strategies. It is thin or absent on AL-Complexity's formal side (Ω/Θ, tractability), on algorithmic correctness, and on four AL-Foundational items: hash collisions, balanced trees, adjacency matrices and MST. Amortized analysis, recurrences and the master theorem, all candidates in the brief, turn out to be **KA Core, not CS Core**, in the final CS2023 text.

### Cited Findings
Source for every CS2023 tier and topic below: [CS2023 final report, AL knowledge area and SDF knowledge area (ACM/IEEE-CS/AAAI, January 2024; HTML version on csed.acm.org)](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm). AL hours: AL-Foundational 11 CS Core + 6 KA Core; AL-Strategies 6 CS Core; AL-Complexity 6 + 3; AL-Models 9 + 23; AL-SEP counted in SEP hours; total 32 + 32. The report adds that AL-Foundational's 11 CS Core hours come "in addition to 9 hours counted in SDF and 3 hours counted in MSF."

Status key: **Covered** = taught and practiced at the board; **Thin** = mentioned or read but not practiced, or practiced only in part; **Absent** = no class, reading or take-home item.

| CS2023 topic (unit, tier) | Draft classes | Status | Evidence in the course |
|---|---|---|---|
| ADT and dictionary operations: insert, delete, find (AL-Found., CS Core) | 4, 16, 23 | Covered for use; BST insert/delete only in reading | S:264; S:302-303; T:1111-1114 |
| Arrays: strings; vector vs matrix (AL-Found., CS Core) | 1-3, 6; grids 18-19; 2D tables 29 | Covered | S:254-271; S:308-313; S:343-345 |
| Records/tuples/objects (AL-Found., CS Core) | memory table | Covered implicitly | S:198-199, S:211-213 |
| Linked lists: single vs double, linear vs circular (AL-Found., CS Core) | 10 | Thin: singly linked only | S:282-283; T:658-663 |
| Stacks (AL-Found., CS Core) | 7, 9 | Covered | S:273-280; T:433-436 |
| Queues and deques; heap-based priority queue (AL-Found., CS Core) | 8, 9, 17 | Covered | S:276-280; S:305-306 |
| Hash tables: "Collision resolution and complexity (e.g., probing, chaining, rehash)" (AL-Found., CS Core); outcome 5 "Explain how collision avoidance and collision resolution is handled" | 4 | **Thin**: board problems use dict/set (#242, #1); pattern text gives "O(1) on average" with no collision content; collisions appear at most in the Runestone reading | S:264; T:225-229; T:236-237 |
| Graphs; "Graph representation: adjacency list vs matrix" (AL-Found., CS Core) | 18-22 | **Thin**: adjacency list and implicit grid only; no matrix reading | T:1246-1249; T:1259-1262 |
| Trees: binary, n-ary, search; "Balanced (e.g., AVL, Red-Black, Heap)" (AL-Found., CS Core) | 15, 16, 17 (heap), 23 (trie) | **Thin**: AVL/Red-Black absent; "balanced" appears once as a condition | T:1096-1100 |
| Sets (AL-Found., CS Core) | 4 | Covered | T:225-229 |
| Search: linear, binary, DFS/BFS tree search (AL-Found., CS Core) | 14, 15 | Covered | S:294-300 |
| Sorting: stable/unstable; O(n²) insertion, selection; O(n log n) quicksort, merge, timsort (AL-Found., CS Core) | 13 | **Thin**: one class; insertion and quicksort in reading only; board = #1331 (use a sort) and #912 (implement one); stability asked | S:291-292; T:886-898; T:937-940 |
| Shortest path (e.g., Dijkstra, Floyd) (AL-Found., CS Core) | 21 | Covered (Dijkstra) | S:318-319; T:1460-1466 |
| Minimal spanning tree (e.g., Prim, Kruskal) (AL-Found., CS Core) | none | **Absent**: Prim appears only as "context" reading for union-find and as a greedy example | T:1547-1548; T:1769-1770 |
| Heapsort; counting/radix sort (AL-Found., KA Core) | none | Absent | — |
| Transitive closure; topological sort (AL-Found., KA Core) | 20 | Topological sort covered | S:315-316; T:1394-1399 |
| String matching (KMP, Boyer-Moore); LCS; regex matching (AL-Found., KA Core) | 28, 29 | LCS (#1143) and regex (#10) covered as DP; KMP absent | S:339-345 |
| Brute force (AL-Strat., CS Core) | every class | Covered: plan item 2 every take-home | S:112-113; T:57 |
| Decrease-and-conquer: insertion sort, topological sort, binary search, Euclid (AL-Strat., CS Core) | 13, 14, 20 | Covered (paradigm never named) | S:291-316 |
| Divide-and-conquer: binary search, quicksort, mergesort, Strassen (AL-Strat., CS Core) | 11, 13 | **Thin**: named in a title, but the readings are recursion basics, with no D&C reading and no recurrence | T:731; T:742-754; S:285-292 |
| Greedy: Dijkstra, Kruskal, knapsack (AL-Strat., CS Core); outcome 6 "Evaluate whether a greedy approach leads to an optimal solution" | 25, 21 | Covered; exchange argument and counterexample asked | T:1757-1762; T:1815-1818 |
| Transform-and-conquer: presort; heapsort; reduction; DP (e.g., Floyd, Warshall, Bellman-Ford) (AL-Strat., CS Core) | 13 (presort), 27-29 (DP) | DP covered; Bellman-Ford, Floyd, Warshall, heapsort absent | T:879-881; S:336-345 |
| Space vs time trade-offs (hashing) (AL-Strat., CS Core) | 3, 4 | Covered strongly | T:157-159; T:228-229 |
| Handling exponential growth: A*, branch-and-bound, backtracking (AL-Strat., CS Core) | 24 | Covered | T:1684-1689 |
| Iteration vs recursion (AL-Strat., CS Core) | 11, 14, 27 | Covered | T:958-959; T:1908-1910 |
| Approximation, iterative improvement, randomized (AL-Strat., KA Core) | none | Absent | — |
| Complexity framework: best/average/worst; order of growth; input size; time and space (AL-Compl., CS Core) | all | Covered for time/space; best/average/worst only in passing | S:128-130; T:8-10; T:226; T:1099 |
| "Big-O, Big-Omega, and Big-Theta formal notations" (AL-Compl., CS Core) | 1 | **Thin**: Big-O only | S:42-43; S:66; T:8-10 |
| Complexity classes O(1) … O(n!) with examples (AL-Compl., CS Core) | throughout | Covered | T:735-736; T:1688 |
| Empirical measurements of performance (AL-Compl., CS Core) | outside class | Thin: timeit / getsizeof only outside class | S:446-448; T:72-74 |
| "P, NP, and NP-Complete Complexity Classes"; NP-complete problems; reductions (AL-Compl., CS Core) | none | **Absent**: no class or take-home mentions P or NP | — |
| Time and space trade-offs (AL-Compl., CS Core) | 3, 4, 12 | Covered | T:157-159; T:807-808 |
| Formal recursive analysis; Master Theorem (outcomes 14-15); amortized analysis (AL-Compl., **KA Core**) | 11; mentions in 2, 8, 9, 22 | Recurrences and master theorem absent (recursion tree only); amortized cost stated, argued once | T:792-793; T:86; T:569-570; T:646-647; T:1538 |
| Automata, grammars, decidability, Church-Turing (AL-Models, CS Core) | none | Absent | — |
| "Algorithmic correctness: Invariants (e.g., in iteration, recursion, tree search)" (AL-Models, CS Core) | 5, 9, 14, 25 | **Thin**: one loop-invariant exercise; one-sentence justifications | T:954-955; T:1006-1007; T:352-353; T:646-647; T:1759-1760 |
| AL-SEP (CS Core): fairness, accountability, "Economic and other impacts of inefficient algorithms," sustainability | none | **Absent** | — |
| SDF-Data-Structures (CS Core): standard ADTs (lists, stacks, queues, sets, maps); selecting a structure; performance implications; strings | 2-10, 15-17 | Covered | S:254-306 |
| SDF-Algorithms (CS Core): concept of algorithm and efficiency; sorting, searching, tree and graph traversal; time-space impact | 13-15, 18-19 | Covered | S:291-313 |
| SDF-Practices (CS Core): "Basic testing, including test case design"; IDE and debugger | plan item 6 | Thin: "Two edge cases" only; no IDE by design | T:65; S:132-133 |

Further CS2023 facts that bear on the mapping:
- CS2023 says AL-SEP implications should "be addressed in some manner during every lecture hour of focus in this AL knowledge area," and gives as an illustrative outcome "Develop algorithmic solutions to real-world societal problems, such as routing an ambulance to a hospital" — [CS2023 report](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm).
- The packaging examples "assume Big-O analysis is introduced in the Data Structures (CS2) course and that graphs are taught in the third Algorithms course," and place AL-Models in that third course or in a separate theory course — [CS2023 report](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm).
- The third-course ("Algorithms-C") packaging lists: graphs and graph algorithms, tractability, exponential and factorial classes, brute force, decrease-and-conquer (topological sort), divide-and-conquer, greedy (Dijkstra, Kruskal), transform-and-conquer (heapsort; 2-3, AVL and Red-Black trees), DP (Warshall, Floyd, Bellman-Ford), handling exponential growth, and all AL-Models CS Core — [CS2023 report](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm).

### Inferences
- **[Judgment]** Against the CS2 packaging the draft scores well. Its one real CS2 gap is hash-table internals. Against the third-course packaging it covers graphs, greedy, DP, backtracking and topological sort, but not Kruskal, balanced trees, Bellman-Ford/Floyd/Warshall, tractability or AL-Models. A program that uses this draft as its only algorithms course would leave those CS Core items uncovered.
- **[Judgment]** The brief's candidate list sorts into three groups. Truly CS Core and missing or thin: hash collisions, balanced search trees, graph representations (matrix), MST, correctness and invariants, P/NP, divide-and-conquer analysis, the comparison-sort material. KA Core only: amortized analysis, recurrences, master theorem. Present only as an "e.g." example: Bellman-Ford (any DP example satisfies the topic). Even the KA Core items matter here, because learning outcome 1 promises "recursive Python code, including amortized cost" (S:66-68).
- **[Judgment]** AL-Models (automata, decidability) is not a fair expectation for this course. CS2023 itself puts it in a third or theory course.

### Gaps
- I used the final report's HTML text (downloaded with curl, because WebFetch truncated the 7 MB page). I did not cross-check page numbers in the PDF/ACM DL version.

---

## 3. Comparison with established courses

### Takeaway
The draft's topic *list* tracks NeetCode 150's categories almost one to one. Its *order* follows a CS2 textbook front end (analysis, linear structures, recursion, sorting, search, trees, heaps, graphs) and then the interview back end (tries, backtracking, greedy, intervals, DP). Every university comparator teaches balanced trees and an explicit asymptotic-analysis unit. Princeton also teaches MST and intractability; MIT also teaches Bellman-Ford and complexity. The draft has none of these.

### Cited Findings
Sources:
- MIT 6.006 Spring 2020: [calendar](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/calendar/), [syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/).
- Princeton COS 226 Spring 2025: [lectures page](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures.php), [course page](https://www.cs.princeton.edu/courses/archive/spring25/cos226), [algs4 table of contents](https://algs4.cs.princeton.edu/home/).
- Python course: University of Rochester CSC 162 "The Art of Data Structures" (summer 2021, Python 3.7+, textbook Miller and Ranum, the draft's primary text): [syllabus](https://cs.rochester.edu/~hbeadle/csc162/), [lectures](https://cs.rochester.edu/~hbeadle/csc162/lectures.html), [schedule](https://cs.rochester.edu/~hbeadle/csc162/schedule.html).
- Interview lists: [NeetCode site data (neetcode150 flags and pattern labels)](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json); [Tech Interview Handbook study plan (topics by priority + Grind 75 list)](https://www.techinterviewhandbook.org/coding-interview-study-plan/).

| Topic | Draft (class) | MIT 6.006 SP20 (lecture) | Princeton COS 226 SP25 (lecture; algs4 §) | Rochester CSC 162 (Python, M&R) | NeetCode 150 category | TIH study-plan topic (priority) |
|---|---|---|---|---|---|---|
| Asymptotic analysis | 1 | L1 Introduction | L2 Analysis of Algorithms (1.4) | Runtime Analysis | — | — |
| Memory in bytes | 1 and every class | — | — | — | — | — |
| Dynamic / resizable arrays | 2 (stated, not practiced) | L2 Data Structures; syllabus lists "dynamic arrays" | L3 Stacks and Queues I: Resizable Arrays (1.3) | — | Arrays & Hashing | Array (High) |
| Strings, prefix sums | 3 | — | ch. 5 Strings (5.1-5.5) | — | Arrays & Hashing | String (High) |
| Hashing incl. collisions | 4 (use only) | L4 Hashing | L14 Hash Tables (3.4) | Hashing; "Hash Table ADT" notebook | Arrays & Hashing | Hash Table (Mid) |
| Two pointers; sliding window | 5, 6 | — | — | — | Two Pointers; Sliding Window | — |
| Stacks, queues, deques | 7, 8 | — | L3-L4 Stacks and Queues I/II (1.3) | Stacks; Queues; Deques | Stack | Stack, Queue (Mid) |
| Monotonic stack/deque | 9 | — | — | — | inside Stack (#739 is NC150 Stack) | — |
| Linked lists | 10 | — | L4 Linked Lists (1.3) | Lists (M&R 4.19-4.23) | Linked List | Linked List (Mid) |
| Recursion | 11 | L15 DP Part 1: Recursive Algorithms | — | Recursion | — | Recursion (Mid) |
| Bit manipulation | 12 | — | — | — | Bit Manipulation (listed last) | Binary (Low) |
| Elementary O(n²) sorts | 13 (reading only) | — | L5 Elementary Sorts (2.1) | Bubble, Selection, Insertion, Shell | — | Sorting and searching (High) |
| Mergesort, quicksort | 13 | L3 Sorting | L6 Mergesort (2.2); L7 Quicksort (2.3) | Merge Sort; Quick Sort | — | Sorting and searching (High) |
| Linear-time sorting | — | L5 Linear Sorting | 5.1 String Sorts | — | — | — |
| Binary search | 14 | — | — | Searching | Binary Search | Sorting and searching (High) |
| Binary trees, traversal | 15 | L6 Binary Trees, Part 1 | — | Trees | Trees | Tree (High) |
| Binary search trees | 16 | L6 | L9 Elementary Symbol Tables / BSTs (3.1-3.2) | Binary Search Trees | Trees | Tree (High) |
| **Balanced BSTs** | **—** | **L7 Binary Trees, Part 2: AVL** | **L10 Balanced Search Trees (3.3)** | **AVL Trees 1, 2 (M&R 7.15-7.17)** | — | — |
| Heaps / priority queues | 17 | L8 Binary Heaps | L8 Priority Queues (2.4) | Binary Heaps | Heap / Priority Queue | Heap (Mid) |
| Graphs, BFS, DFS | 18, 19 | L9 BFS; L10 DFS | L15-16 Graphs and Digraphs I/II (4.1-4.2) | Graphs; Graph Search 1-3 | Graphs | Graph (High); Matrix (High) |
| Topological sort | 20 | — (not a lecture title) | — (not a lecture title) | — | Graphs (#207, #210) | — |
| Dijkstra | 21 | L13 Dijkstra's Algorithm | L18 Shortest Paths (4.4) | Dijkstra's Algorithm | Advanced Graphs (#743) | — |
| **Bellman-Ford / negative weights** | **—** | **L11 Weighted Shortest Paths; L12 Bellman-Ford; L14 Johnson's** | L18 Shortest Paths (content not checked) | — | Advanced Graphs includes #787 | — |
| **Minimum spanning trees** | **—** | — | **L17 Minimum Spanning Trees (4.3)** | — | **Advanced Graphs includes #1584 Min Cost to Connect All Points** | — |
| Union-find | 22 | — | L1 Introduction / Union-Find (1.5) | — | Graphs (#684) | — |
| Tries | 23 | — | 5.2 Tries | — | Tries | Trie (Mid) |
| Backtracking | 24 | — | — | — | Backtracking | — |
| Greedy | 25 | — | — | — | Greedy | — |
| Intervals, sweep line | 26 | — | L13 Geometric Applications of BSTs | — | Intervals | Interval (Mid) |
| Dynamic programming | 27-29 | L15-L18 DP Parts 1-4 | L19 Dynamic Programming | Dynamic Programming (M&R 5.12) + LCS notebook | 1-D DP; 2-D DP | Dynamic programming (Low) |
| **Complexity / intractability** | **—** | **L19 Complexity** | **L23 Intractability; algs4 6.5 Reductions, 6.6 Intractability** | — | — | — |
| Maxflow; randomness; multiplicative weights | — | — | L20 Maxflows and Mincuts (6.4); L21; L22 Randomness | — | — | — |
| Math, geometry, matrix | — (#50 Pow in class 11) | — | — | — | Math & Geometry | Matrix (High); Math, Geometry (Low) |

Further verified facts:
- **Size.** NeetCode 150 has 18 categories in this order in the data file: Arrays & Hashing (9), Two Pointers (5), Sliding Window (6), Stack (7), Binary Search (7), Linked List (11), Trees (15), Tries (3), Heap / Priority Queue (7), Backtracking (9), Graphs (13), Advanced Graphs (6), 1-D DP (12), 2-D DP (11), Greedy (8), Intervals (6), Math & Geometry (8), Bit Manipulation (7) — [NeetCode data](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json).
- **NeetCode's advanced graphs.** NeetCode 150's "Advanced Graphs" are #332 Reconstruct Itinerary, #1584 Min Cost to Connect All Points, #743 Network Delay Time, #778 Swim In Rising Water, #269 Alien Dictionary, #787 Cheapest Flights Within K Stops — [NeetCode data](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json). So even the interview list includes an MST problem (#1584), which the draft lacks.
- **Grind 75 topics.** Tech Interview Handbook ranks topics High/Mid/Low and says the Week 5-12 list is "a Grind 75 plan." It ranks Dynamic programming and Binary as Low priority, and Array, String, Sorting and searching, Matrix, Tree and Graph as High — [TIH study plan](https://www.techinterviewhandbook.org/coding-interview-study-plan/).
- **Grind 75 problems the course never uses** (24): 3Sum, Add Binary, Balanced Binary Tree, Basic Calculator, Construct Binary Tree from Preorder and Inorder Traversal, Diameter of Binary Tree, Find All Anagrams in a String, First Bad Version, LRU Cache, Largest Rectangle in Histogram, Letter Combinations of a Phone Number, Longest Palindrome, Longest Palindromic Substring, Lowest Common Ancestor of a Binary Tree, Majority Element, Maximum Profit in Job Scheduling, Minimum Height Trees, Partition Equal Subset Sum, Product of Array Except Self, Serialize and Deserialize Binary Tree, Spiral Matrix, String to Integer (atoi), Task Scheduler, Time Based Key-Value Store (my set difference against the [TIH list](https://www.techinterviewhandbook.org/coding-interview-study-plan/)).
- **Assessment.** MIT 6.006 grades by Quiz 1 20%, Quiz 2 15%, Quiz 3 10%, Final 35%, Problem Sets 18%, Recitation 2%. It lists prerequisites "Basic experience programming in Python 3" and discrete mathematics including "proofs" — [MIT syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/). COS 226 Spring 2025 held an in-class midterm and an in-person final — [COS 226 course page](https://www.cs.princeton.edu/courses/archive/spring25/cos226). Rochester CSC 162 grades 70% weekly individual labs, 30% in-class workshop problems — [CSC 162 syllabus](https://cs.rochester.edu/~hbeadle/csc162/). The draft grades attendance and effort (S:359-365).
- **Order.** MIT 6.006 runs: data structures → sorting → hashing → linear sorting → binary trees/AVL → heaps → BFS → DFS → weighted shortest paths → Bellman-Ford → Dijkstra → Johnson → DP ×4 → complexity — [MIT calendar](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/calendar/). COS 226 opens with union-find and analysis, then stacks/queues, sorts, PQs, BSTs, balanced trees, hash tables, graphs, MST, shortest paths, DP, maxflow, intractability — [COS 226 lectures](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures.php). Rochester puts DP right after recursion (week 3), and hashing before sorting — [CSC 162 schedule](https://cs.rochester.edu/~hbeadle/csc162/schedule.html).
- The draft's language matches CS2023's CS2 assumption: Rochester, on the same textbook, is a six-week summer course (Jul 7 – Aug 13, 2021) and still schedules AVL trees and a hash-table ADT notebook — [CSC 162 schedule](https://cs.rochester.edu/~hbeadle/csc162/schedule.html), [lectures](https://cs.rochester.edu/~hbeadle/csc162/lectures.html).

### Inferences
- **[Judgment]** The draft's topic set equals NeetCode 150's categories plus a CS2 front end. Each NeetCode category except Math & Geometry has its own class: Arrays & Hashing (2, 4), Two Pointers (5), Sliding Window (6), Stack (7, 9), Linked List (10), Bit Manipulation (12), Binary Search (14), Trees (15, 16), Heap (17), Graphs (18-20, 22), Advanced Graphs (21), Tries (23), Backtracking (24), Greedy (25), Intervals (26), 1-D DP (27), 2-D DP (29). The CS2 additions are Big-O and memory (1), queues (8), recursion (11) and sorting (13).
- **[Judgment]** Where the draft departs from the university courses, it departs toward the interview lists. It adds two pointers, sliding window, monotonic stacks, bit tricks and intervals, and it drops balanced trees, MST, linear sorting, Bellman-Ford and intractability. MIT and Princeton spend about two lectures each on what the draft gives one class (sorting), and both give balanced trees a full lecture.
- **[Judgment]** The draft's placement of DP last matches MIT, Princeton and NeetCode. Its placement of union-find late (22) differs from Princeton (lecture 1) but is sound, because the draft introduces union-find after DFS components.
- **[Judgment]** MIT 6.006 Spring 2020 also lacks MST, union-find, tries, greedy and backtracking as lecture titles. The draft is not uniquely thin there; MIT covers those in a follow-on course (not verified, see Gaps).

### Gaps
- The neetcode.io roadmap page rendered no content (JavaScript). I used NeetCode's GitHub data file, which gives categories and order but not the roadmap's prerequisite arrows.
- MIT and Princeton pages give lecture *titles*. I did not check lecture contents, so I cannot say whether MIT L10 covers topological sort or whether COS 226 L18 covers Bellman-Ford.
- I did not verify which follow-on MIT course covers MST.
- The syllabus says MIT 6.006 is "Taught in Python" (S:469-470). The OCW syllabus lists Python 3 as a prerequisite, but neither the syllabus nor the course home page I fetched states the language of the coursework. The claim is plausible but unverified from the pages I fetched.
- I found only one Python data-structures course (Rochester) with a public, complete schedule. Columbia, Washington and Lee and others came up in search but I did not open them.

---

## 4. Prerequisite and sequence check

### Takeaway
The macro order is sound: recursion precedes trees, backtracking and DP; heaps precede Dijkstra; graphs precede topological sort and union-find; sorting precedes binary search, greedy and intervals. Two local inversions break the syllabus's promise that "Each class builds on the ones before it" (S:47). Class 23's Hard problem needs class 24's backtracking, and class 28's harder problem needs class 29's 2-D table. Two "builds on" paragraphs are false (T:1691-1693, T:2047-2049) and one is partly false (T:1975-1977).

### Cited Findings
**The brief's specific checks.**
- Recursion (11) before trees (15-16), backtracking (24) and DP (27-29): holds (S:285, S:299-303, S:327, S:336). The take-homes say so (T:1027-1029, T:1691, T:1908-1910).
- Heaps (17) before Dijkstra (21): holds (S:305, S:318; T:1468-1469).
- Graphs (18-19) before topological sort (20) and union-find (22): holds (S:308-322; T:1401-1402; T:1541-1542).
- Recursion and memoization before DP: recursion yes (class 11). Memoization appears as one clause, "exponential unless you remember answers" (T:735-736), and no class-11 problem requires it. #509 Fibonacci (S:285) can be solved naively.
- Sorting (13) before binary search (14): holds (T:957-958). Sorting before greedy (25) and intervals (26): holds (T:1764, T:1836).

**Class-by-class "builds on" claims.** Verdict: **True**, **Partly** (true but misleading or incomplete), **False**.

| Class | Claim (lines) | Verdict | Evidence |
|---|---|---|---|
| 1 | First class (T:15-16) | True | — |
| 2 | Class 1 gave Big-O and memory (T:92-93) | True | S:254 |
| 3 | Class 2 indexes; strings as read-only lists (T:161-163) | True | S:257 |
| 4 | Class 3 stored precomputed values in a list (T:231-232) | True | #303 prefix list, S:262 |
| 5 | Class 2 read/write index (T:300-302) | True | #283, S:257 |
| 6 | Class 5 pointers; class 3 prefix sums (T:369-371) | True | S:261-268 |
| 7 | Class 4 extra memory remembers the past (T:438-440) | True (weak link) | — |
| 8 | Class 7 stacks reverse order (T:513-514) | True | — |
| 9 | Class 7 stack, class 8 deque (T:588-590) | True | — |
| 10 | Class 5 two pointers walk nodes; class 8 queues from nodes (T:665-666) | True | #19 uses two pointers, S:283 |
| 11 | Class 10 walked a list; call stack is class 7's stack (T:738-740) | True | — |
| 12 | Class 11 halves numbers; class 4 hashing memory XOR avoids (T:810-812) | True | #50 halves n, S:286 |
| 13 | Class 11 recursion; class 5 two pointers do the merge (T:883-884) | Partly | True, but class 2's #88 Merge Sorted Array (S:257-258) *is* the merge step and goes uncited |
| 14 | Class 13 sorted data; class 11 halving becomes a loop (T:957-959) | True | — |
| 15 | Class 11 recursion; class 8 queues (T:1027-1029) | True | — |
| 16 | Class 15 traversals; class 14 halving in pointers (T:1102-1103) | True | — |
| 17 | Class 16 pointers vs list; sort O(n log n) vs heap O(n log k) (T:1176-1178) | True | — |
| 18 | Class 15 tree DFS; class 4 visited set (T:1253-1254) | True | — |
| 19 | Class 18 DFS stack; class 8 queue (T:1328-1329) | Partly | True, but omits class 15's level-order BFS (#102, S:300), the students' first BFS |
| 20 | Class 19 BFS → Kahn; class 18 graphs get directions (T:1401-1402) | Partly | Kahn's link is true. The take-home also offers "a DFS version orders vertices by finishing time" (T:1397-1398); class 18 never mentions finishing times (T:1246-1251) |
| 21 | Class 19 BFS = Dijkstra with unit weights; class 17 heap (T:1468-1469) | True | — |
| 22 | Class 18 DFS components; "a parent list like the array heap of class 17" (T:1541-1543) | Partly | **[Judgment]** The heap analogy misleads. A binary heap's parent is computed from the index; union-find stores arbitrary parent pointers. Both use a list, and that is all they share |
| 23 | Class 15 trees, class 4 dicts, class 18 DFS (T:1614-1615) | True for the trie | But Problem B #212 Word Search II (S:325) needs grid backtracking (see below) |
| 24 | "class 18 DFS the idea of exploring and un-marking, and class 23 shows pruning a search by prefix" (T:1691-1693) | **False** | Class 18 DFS marks visited and never un-marks (T:1249-1250; Q8 "Where do you mark a cell visited," T:1310-1311). "Class 23 shows pruning a search" holds only because class 23's Problem B is already a backtracking search: the inversion |
| 25 | Class 13 sorting; class 24 explored every choice (T:1764-1765) | True | — |
| 26 | Class 13 sorting, class 25 greedy, class 17 heaps (T:1836-1837) | True | — |
| 27 | Class 11 naive recursion; memo dict (class 4); bottom-up list (class 2) (T:1908-1910) | True | #509 Fibonacci, S:285 |
| 28 | "a state depends on all earlier states, and class 29 will use two sequences at once" (T:1975-1977) | **Partly false** | Class 28's own Problem B is #1143 Longest Common Subsequence (S:339-341), a two-sequence problem; the take-home itself gives LCS as O(mn) (T:1971-1973) |
| 29 | "Class 28 used one sequence; now two sequences or a grid give a table" (T:2047-2049) | **False** | Class 28 already solved LCS on two sequences (S:339-341). Class 29 defines its pattern as "When two sequences … dp[i][j]" (T:2040-2042), which is LCS |
| 30 | Every earlier class (T:2118-2119) | True | — |

**Problem-level forward references** (a board problem that leans on a later class):
- Class 23 Problem B #212 Word Search II (S:324-325, labelled Hard). Class 24 assigns its single-word version, #79 Word Search, as backtracking practice (T:1722). NeetCode labels #79 "Backtracking" — [NeetCode data](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json). The class-23 pattern text already asks students to "Combine a trie with DFS to explore many words at once" (T:1611-1612). **[Judgment]** #212 needs choose-explore-unmark on a grid, which class 24 teaches.
- Class 28 Problem B #1143 LCS needs the 2-D table of class 29. NeetCode labels #1143 "2-D Dynamic Programming" — [NeetCode data](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json).
- Class 1 Problem B #217 Contains Duplicate (S:254-255). NeetCode labels it "Arrays & Hashing" — [NeetCode data](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json). **[Judgment]** Its O(n) answer uses a set, which class 4 introduces. That works only if class 1 accepts the O(n²) or sort-based answer.
- Class 30 Problem A #127 Word Ladder (S:347). The class-19 reading is "§7.7 The Word Ladder Problem" (T:1333-1334). **[Judgment]** The capstone's "no topic label" problem (T:2110-2112) is the worked example of an earlier reading, which weakens it as a test of pattern choice.
- Take-home practice #22 Generate Parentheses (T:765) sits in class 11 (recursion). **[Judgment]** It is a generate-all-candidates problem that reads more naturally after backtracking. NeetCode files it under "Stack" — [NeetCode data](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json). Minor.
- Take-home 21 practice #787 Cheapest Flights Within K Stops (T:1490). **[Judgment, unverified]** The k-stop limit breaks plain Dijkstra on distance alone. The usual approaches are k+1 rounds of Bellman-Ford relaxation or BFS by stops, neither of which the course teaches. I did not fetch a LeetCode editorial to confirm.
- Take-home 25 reads the DP section (T:1772-1773) two classes before DP. That works as motivation; it is not a defect.

**Difficulty ramp vs schedule.** The ramp table (S:218-242) and the schedule (S:254-349) agree class by class: 1-8 Easy/Easy, 9-19 Easy/Medium, 20-22 Medium/Medium, 23-26 Medium/Hard, 27-28 Medium/Medium, 29 Medium/Hard, 30 Hard/Hard.

### Inferences
- **[Judgment]** Swapping the order of classes 23 and 24 fixes the first inversion without touching the ramp, since both are Medium/Hard (S:324-328). Moving #1143 from class 28 to class 29 fixes the second. Section 6 gives details.
- **[Judgment]** The sequence places bit manipulation (12) between recursion and sorting with no later class depending on it. No learning outcome names bits (S:66-92). Class 12 is the cheapest slot to repurpose.

### Gaps
- I did not open LeetCode problem pages, so the requirements I attribute to #212, #217, #787 and #22 rest on NeetCode's labels and on my reading, marked as judgment.

---

## 5. Learning-outcome coverage

### Takeaway
Outcomes 2, 4, 6 and 7 are taught and practiced in every or nearly every class. Outcome 1 is practiced except for its "recursive … amortized" promise, which gets recursion trees and assertions rather than derivations. Outcome 3 is practiced in one class out of 30, because the take-home names the pattern every other time. Outcome 5 is practiced for 4 of its 10 structures. Outcome 8 is never practiced. No outcome is assessed for the grade.

### Cited Findings
| # | Outcome (S:lines) | Where taught | Where practiced | Graded? | Verdict |
|---|---|---|---|---|---|
| 1 | Derive Big-O time and auxiliary space of iterative and recursive code, "including amortized cost," and justify in writing and aloud (S:66-68) | T:8-13 (class 1); T:731-736 (recursion); amortized stated T:86, T:1538 | Every board solution (S:128-130, S:158-163); recursion tree T:792-793; aggregate argument T:646-647; stack-from-queue cost T:569-570; "aloud" via S:414-417 | Extra credit only (S:369-372) | **Partly**: no recurrence relations, no amortized derivation (e.g., doubling array) |
| 2 | Estimate total memory from CPython object sizes (S:70-72) | S:174-216; T:11-13 | Every board solution (S:165-168); plan item 5 "memory for n = 100,000" (T:63); T:72-74 | Extra credit only | **Covered strongly** |
| 3 | Recognize which pattern a new problem belongs to and defend by comparing complexity (S:74-75) | — | Only class 30 (S:347-349; T:2110-2113; T:2172-2176). Elsewhere "You are told the pattern in the take-home" (S:121-123, S:352-353) | Extra credit only | **Thin**: 1 class in 30 |
| 4 | Write correct Python by hand, Easy to Hard (S:77-78) | — | Every class (S:40-45, S:125-126); Hard problems in classes 23-26, 29, 30 (S:324-349) | Extra credit only | **Covered** |
| 5 | Implement dynamic arrays, linked lists, stacks, queues, hash tables, heaps, binary trees, tries, union-find, graph representations without a computer (S:80-82) | Readings: T:85-90; T:1189 (heap implementation) | See breakdown below | Extra credit only | **Partly**: 4 of 10 structures built at the board |
| 6 | Apply and trace sorting, binary search, tree/graph traversal, topological sort, Dijkstra, backtracking, greedy, interval sweeps, DP (S:84-86) | Classes 13-15, 18-21, 24-29 | Two board problems each (S:291-345) | Extra credit only | **Covered** (one class per algorithm) |
| 7 | Plan before coding: brute force, pattern, steps, complexity, edge cases in writing (S:88-89) | S:111-115 | Every take-home, items 1-6 (T:55-65 and repeated) | Required for "solid effort" (S:362-365) | **Covered** |
| 8 | Find correctness bugs and hidden inefficiencies in AI-generated code by reading and tracing it, and correct them (S:91-92) | AI policy advice only: "AI tools regularly produce code that runs but is wrong or slower than claimed. Check complexity claims by hand" (S:405-407) | **None.** No class problem, take-home item or practice problem asks students to read or fix AI-generated code. Every take-home mention of AI casts it as tutor (T:382, T:606-607, T:1556-1557, T:1631-1632, T:1778-1779, T:1850-1851, T:1987-1988, T:2059-2060) | No | **Absent** |

**Outcome 5, structure by structure:**

| Structure | Built at the board? | Evidence |
|---|---|---|
| Dynamic array | No. Class 2 problems use a list (#283, #88); the take-home explains amortized append but asks for no implementation | S:257-258; T:85-90 |
| Linked list | Partly: pointer rewiring on given nodes (#206, #19); no insert/delete/search API | S:282-283 |
| Stack | Partly: list as stack (T:436); #232 builds a queue *from* stacks | S:276-277 |
| Queue | Yes: #232 Implement Queue using Stacks; practice #622 Design Circular Queue | S:277; T:542 |
| Hash table | **No.** Board problems use dict/set | S:264 |
| Heap | **No.** #703 and #347 may use heapq (S:155-156); implementation is reading only (T:1189) | S:305-306 |
| Binary tree | Partly: traversal and search on given trees; building one only in practice (#108, T:1127) | S:299-303 |
| Trie | Yes: #208 Implement Trie | S:324 |
| Union-find | Yes: #547, #684; find with path compression in Q8 | S:321-322; T:1596-1597 |
| Graph representation | Yes for adjacency lists (built from edge lists in #1971, #743); **no** adjacency matrix | S:312, S:318; T:1247 |

**Assessment.** The grade comes "from attendance and effort under this rule" (S:364-365). "Solid effort" means asking for help with two failed attempts and arriving with the plan written (S:362-364). A correct answer, defined as "a working solution and the right time, space and memory analysis" (S:370-371), earns extra-credit points, usable to cover absences (S:369-374).

### Inferences
- **[Judgment]** "Taught and practiced" holds for outcomes 2, 4, 6 and 7; "assessed" does not hold for any outcome in a grade-bearing sense. The extra-credit check on correctness (S:370-371) comes closest, and it evidences outcomes 1, 2, 4 and 6, but only for students who attempt it. If an accreditor or program review asks for evidence that outcomes are assessed, the answer sheets (S:126) could be scored formatively without changing the grading rule.
- **[Judgment]** Outcome 8 is the largest mismatch. It is the outcome most specific to this course, and nothing in the 30 classes or 30 take-homes trains it. The take-homes already contain ready-made bug material: `list.pop(0)` is O(n) (T:509-510), string slicing and concatenation copy (T:155-157), marking visited too late (T:1310-1311), stale heap entries (T:1522-1523).
- **[Judgment]** Outcome 3 is structurally blocked by the format. Announcing the pattern (S:121-123) is good for learning a pattern but prevents recognizing one, except in class 30.

### Gaps
- None beyond those already listed. All findings in this section come from the two course documents.

---

## 6. Recommended minimal changes

### Takeaway
Ten changes close the sequence breaks, the CS Core gaps and the outcome gaps. They keep 30 classes, two LeetCode problems per class and the difficulty ramp (S:218-242). Most are problem swaps or one added take-home question. All recommendations are **[Judgment]**. Each cites the evidence it rests on. LeetCode numbers and levels I propose come from [NeetCode's data file](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json) where listed. Verify each on leetcode.com before adopting.

### Cited Findings
Problem levels used below, from [NeetCode data](https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json): #706 Design HashMap Easy; #705 Design HashSet Easy; #380 Insert Delete GetRandom O(1) Medium; #707 Design Linked List Medium; #146 LRU Cache Medium (NC150); #1584 Min Cost to Connect All Points Medium (NC150, Advanced Graphs); #787 Cheapest Flights Within K Stops Medium (NC150); #110 Balanced Binary Tree Easy (NC150); #701 Insert into a BST Medium; #450 Delete Node in a BST Medium; #23 Merge K Sorted Lists Hard (NC150); #1631 Path with Minimum Effort Medium; #135 Candy Hard. #547, #700 and #218 are not in the NeetCode file.

### Inferences (the recommendations)

**A. Fix the two sequence inversions (no new content)**

1. **Swap classes 23 and 24.** Backtracking becomes class 23, tries class 24. Both are Medium/Hard (S:324-328), so the ramp is unchanged. #212 Word Search II (trie + grid backtracking) then follows backtracking. Rewrite the two "builds on" paragraphs. The new class-24 (tries) text can say class 23 backtracking supplies the search and the trie prunes it by prefix. Drop "class 18 DFS the idea of exploring and un-marking" (T:1692), which is false (section 4).
2. **Move #1143 LCS from class 28 to class 29.** Class 28 keeps #300 LIS as Problem A and takes a one-sequence Medium as Problem B, such as #139 Word Break or #152 Maximum Product Subarray (both already class-28 practice, T:1996-2004). Class 29 becomes #1143 LCS (A) and #10 Regular Expression Matching (B, Hard), which keeps the Medium/Hard ramp (S:343). Move #72 Edit Distance into take-home 29 practice. Then edit T:1971-1973 (drop LCS or flag it as a preview of class 29) and T:2047 (which then becomes true).

**B. Correct the inaccurate "builds on" text** (wording is the author's to choose; these are the facts to fix)

3. T:1975-1977 and T:2047-2049: fixed by change 2. T:1691-1693: fixed by change 1. T:1542-1543 (heap analogy): say instead that union-find stores parent pointers in a list. T:883-884: add class 2's #88 as the merge step. T:1328-1329: add class 15's level-order BFS. T:1397-1398: either add finishing times to take-home 18 or drop the DFS version from take-home 20.

**C. Close CS Core gaps with swaps, not new classes**

4. **Repurpose class 12 (bits) as "Hash tables and dynamic arrays from scratch."** Problem A: #706 Design HashMap (Easy), with no dict allowed and chaining required. Problem B: #380 Insert Delete GetRandom O(1) (Medium), which leans on list append and swap-with-last pop. Take-home questions: draw the table after five inserts that collide; show what rehashing does; derive amortized O(1) append by the doubling argument. This covers the CS Core hash-collision topic and outcome 5's two missing structures, and it gives outcome 1's "amortized cost" a derivation. The ramp (Easy/Medium for 9-19, S:228-230) holds. The slot also fits the sequence: it follows linked lists (10), which chaining uses, and dicts (4). Bit manipulation names no learning outcome (S:66-92), and Tech Interview Handbook ranks "Binary" Low ([TIH](https://www.techinterviewhandbook.org/coding-interview-study-plan/)). Keep XOR as a take-home 4 practice item (#136 against a set).
5. **Add MST to class 22 (union-find).** Replace Problem A #547 with #684 Redundant Connection (Medium, now Problem B), and make Problem B #1584 Min Cost to Connect All Points (Medium), solved with Kruskal: sort edges plus union-find. The ramp stays Medium/Medium (S:321-322). Prim's section is already assigned (T:1547-1548); add Kruskal to the reading. This covers CS Core "Minimal spanning tree (e.g., Prims, Kruskals)" and Kruskal as a greedy example ([CS2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)), matches COS 226 L17 ([lectures](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures.php)), and matches NeetCode 150's #1584.
6. **Add balanced trees to class 16 (BSTs).** Add a balanced-BST reading to take-home 16 and one question: "Insert 1-7 in order into a BST; draw it and give its height. Then show the AVL rotations that rebalance it." Optionally swap Problem A #700 for #110 Balanced Binary Tree (Easy, NC150, in Grind 75). This covers CS Core "Balanced (e.g., AVL, Red-Black…)" and the AL-Complexity outcome "Explain how tree balance affects the efficiency of binary search tree operations" ([CS2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)). All three university comparators teach it (section 3).
7. **Add Bellman-Ford to take-home 21 (Dijkstra)** as a reading plus one question: "Why does Dijkstra fail with a negative edge? Run Bellman-Ford on this 4-vertex graph." CS2023 lists Bellman-Ford as a DP example, and MIT gives it a lecture (L12, [calendar](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/calendar/)). A stronger option swaps class 21 Problem B #1631 for #787 (both Medium), taught as hop-bounded Bellman-Ford, but confirm #787's intended method first (section 4, unverified).
8. **Add formal notation, the sorting lower bound and one recurrence.**
   (a) Take-home 1: define Ω and Θ next to O. CS Core lists "Big-O, Big-Omega, and Big-Theta formal notations" ([CS2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)).
   (b) Take-home 13 says "Comparison sorts cannot beat O(n log n)" (T:876-877). **Flag for the author:** a lower bound is conventionally written with Ω. The precise claim is that any comparison sort needs Ω(n log n) comparisons in the worst case. The author decides the wording. Add one question: "How many leaves must a decision tree for sorting n items have?"
   (c) Take-home 11 or 13: "Write T(n) = 2T(n/2) + cn for merge sort and solve it with a recursion tree." This serves outcome 1's "recursive code" (S:66-67). CS2023 lists formal recursive analysis and the master theorem as KA Core.
9. **Add tractability and SEP as take-home questions.**
   (a) Take-home 24 (backtracking): one reading and one question on P, NP and NP-completeness. "N-Queens and subsets are exponential; name a problem with no known polynomial algorithm and say what NP-complete means." This is CS Core "P, NP, and NP-Complete Complexity Classes" ([CS2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)).
   (b) One SEP question in two or three take-homes, using CS2023's own examples: ambulance routing for Dijkstra, and the "Economic and other impacts of inefficient algorithms" and sustainability topics for the memory and Big-O classes (take-home 1 or 2).

**D. Make outcomes 3, 5 and 8 practiced**

10. **Outcome 8, AI-generated code.** Add item 9 to each take-home, or at least every third. Give a short AI-produced solution to one practice problem with one planted correctness bug or hidden O(n²) step. The take-homes already supply the bug catalogue: `pop(0)` (T:509-510), copying slices (T:155-157), visited marked too late (T:1310-1311), stale heap entries (T:1522-1523), missing base case (T:790). Students trace it, name the flaw and fix it. In class, the extension problem's format is still "TBD" (S:141-143); making it an AI-code audit puts outcome 8 in the room without breaking the two-problem format. If none of this is adopted, the honest alternative is to drop outcome 8.

Further changes, smaller and optional:
- **Outcome 5.** Add to take-home 17: "Write sift-up and sift-down by hand; no heapq." Add #707 Design Linked List (Medium) or #146 LRU Cache (Medium) to take-home 10 practice. Change 4 covers hash tables and dynamic arrays.
- **Outcome 3.** In two mid-term classes (e.g., 10 and 20), make Problem A an unlabeled review problem from earlier patterns, and add take-home 30's "name the pattern" item (T:2172-2173) to take-homes 10 and 20.
- **Capstone.** Replace class 30 Problem A #127 Word Ladder, which is the class-19 reading's worked example (T:1333-1334), with #23 Merge K Sorted Lists (Hard), which is now take-home 30 practice (T:2151). Move #127 into the practice list.
- **Class 1.** If class 1 expects the O(n) answer to #217, swap it with #1929 Concatenation of Array (T:44) and move #217 to class 4.
- **Title and description.** Either close gaps 4-9 and keep "Algorithms & Data Structures … A core computer science course" (S:3, S:39), or keep the draft's coverage and describe it accurately. A title such as "Data Structures and Algorithmic Problem Solving in Python" would do, with "core" dropped from S:39. The draft also leaves prerequisites blank (S:32). CS2023's packaging assumes this material follows a CS1 course ([CS2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)), and MIT 6.006 lists both programming and discrete-mathematics prerequisites ([MIT syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/)).

### Gaps
- I could not confirm Runestone section numbers for balanced BSTs or Bellman-Ford in the pythonds3 edition (Cloudflare block). Rochester's lecture page cites AVL as "M&R Ch. 7.15-7.17" in the edition it used ([CSC 162 lectures](https://cs.rochester.edu/~hbeadle/csc162/lectures.html)), so the book has AVL content, but section numbers in the 3rd edition will differ.
- I did not verify which chapter of Erickson's *Algorithms* covers NP-hardness or MST, so I name no chapter for changes 5 and 9.
- I did not verify #787's intended solution method or the full LeetCode statement of #912 (Sort an Array).
