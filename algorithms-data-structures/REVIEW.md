# Review of the ADS course documents

This review covers draft 2 of the four Algorithms & Data Structures documents, the syllabus, the take-homes, the student answer sheets and the instructor key, as they were merged into main in PR #887. Claude wrote it on 12 November 2026, together with draft 3, which rewrites all four documents. Draft 3 corrects the factual errors listed below and leaves every design decision to you. The second half of this review lists those decisions, with the evidence for each.

Seven research runs supplied the evidence. Their notes are in `research_notes/ADS course setup review/`, one file for each question, and every claim below names the note it comes from. I checked the Hult quotations, the Python documentation quotation and the Erickson chapters myself against the source documents before using them.

| Question | Notes file |
|---|---|
| Are the 150 LeetCode problems named, numbered, rated and linked correctly, and do they fit their classes? | `leetcode_problems.md` |
| Are the 60 board solutions correct, and are their complexity and memory figures right? | `solutions_classes_01_15.md`, `solutions_classes_16_30.md` |
| Are the CPython memory sizes right, and do the readings and links hold? | `memory_table_and_readings.md` |
| What does research on teaching say about each design choice? | `pedagogy.md` |
| How does the coverage compare with the ACM/IEEE CS2023 curriculum and with established courses? | `curriculum.md` |
| What do Hult's rules, the law and authorship standards require? | `hult_policy_and_governance.md` |
| What did I find in my own reading? | `coordinator_observations.md` |

## The short version

The course is well built at its core. All 60 board solutions return correct results. The tests in `tests/` check each one against LeetCode's examples, edge cases and random inputs compared with a slower brute-force solution, and `sh tests/run_tests.sh` reruns them all. All 150 LeetCode problems match LeetCode's number, title, difficulty and link, none is behind LeetCode's paywall, and no problem appears twice. The sequence respects most prerequisites, and the attention to memory in bytes is unusual and valuable.

The problems sit around that core, and they fall into two groups. The first group is factual: wrong figures in the memory table, missing imports in seven solutions, a recurrence that is off by one, a misleading example, false statements about what earlier classes taught, and a key that claimed checks it had not run. Draft 3 fixes all of these, and the table in the next section lists each fix so that you can reverse any of them. The second group is design, and the review put five of its items to you. You decided all five on 12 November 2026, and draft 3 now carries out those decisions: a per-class grading rule with extra credit, authorship that stays with students, a second half of every class spent on live projects with Java, Python, Cursor and Claude Code, attendance registered during that second half, and a restructured schedule that covers the critical algorithms and data structures. The section "Your decisions of 12 November 2026" below records what changed. The remaining items in the review are still open.

## What draft 3 corrects

Each row names the place, what draft 2 said, what draft 3 says, and the evidence. Draft 3 changes the wording of every sentence, so this table lists only changes of fact. The class and take-home numbers in these tables are those of draft 2; the restructured schedule described below renumbers many of them.

### Syllabus

| Where | Draft 2 | Draft 3 | Evidence |
|---|---|---|---|
| Memory table, list | "about 12% spare room if built with append" | between none and about 13 percent spare slots, about 6 percent on average; `[0] * n` and `list(...)` have none | Measured 10.0% at n = 1,000 and 0.12% at n = 100,000; 12.5% is the growth step (`memory_table_and_readings.md`, Table 1) |
| Memory table, dict | "184 bytes for a tiny dict"; "about 50 bytes per entry for large dicts (37 at 1,000)" | 64 bytes empty; for integer keys 37 bytes per entry at 1,000, 30 at 10,000 and 52 at 100,000; for string keys 26 and 38 | Measured (same file, Table 1; `solutions_classes_01_15.md`, D7) |
| Memory table, deque | "about 600 bytes overhead" | about 760 bytes empty | `sys.getsizeof(deque())` = 760 (same file) |
| Memory table, str | "a 1-character string is shared" | shared when the character is one of the first 256 | Measured: U+00FF shared, U+0100 not (same file) |
| Memory table, recursive call | "about 150 bytes per active call" | about 150 to 250 bytes, more with more local variables | Measured 152, 193 and 257 bytes per level for three functions (same file) |
| Memory table, int | 28 bytes | 28 bytes below 2^30^, plus 4 bytes per further 30 bits | Measured (same file) |
| Accuracy sentence | "our checks agree within about 25% to a factor of 2" | "I accept an estimate within about 30 percent of the solution key's figure", the tolerance the key already used | A factor of 2 contradicts the key's 30 percent (same file, judgment section) |
| Materials, MIT 6.006 | "Taught in Python" | "The course expects its students to program in Python 3" | OCW lists Python 3 as a prerequisite but never says the course is taught in Python (same file, bibliography table) |
| Materials, Morin and Erickson | no language given | Morin's text is pseudocode, Java and C++; Erickson's is pseudocode | Same file |
| Materials, CLRS | no year | 2022 | MIT Press page (same file) |

### Take-homes

| Where | Draft 2 | Draft 3 | Evidence |
|---|---|---|---|
| Take-Home 1, question 8 | Check the memory of a list of ints "with sys.getsizeof" | Add the sizes of the integers yourself, because `sys.getsizeof` of a list counts only the list | Python docs: "Only the memory consumption directly attributed to the object is accounted for, not the memory consumption of objects it refers to." Measured: 800,056 bytes reported against 3,600,056 with the integers (`coordinator_observations.md`) |
| Take-Home 22, builds on | union-find "uses a parent list like the array heap of class 17" | describes the parent list directly | A heap is a tree stored by index; union-find stores explicit parent links (`curriculum.md`) |
| Take-Home 24, builds on | class 18 taught "exploring and un-marking" | class 18 marked cells and never unmarked them; backtracking adds the unmarking | Class 18's search never unmarks (`curriculum.md`) |
| Take-Homes 28 and 29, builds on | "Class 28 used one sequence"; "class 29 will use two sequences" | Class 28 met its first two-dimensional table in Longest Common Subsequence | Class 28's Problem B, #1143, compares two strings (`coordinator_observations.md`, `curriculum.md`) |
| Take-Homes 7, 8, 9, readings | §3.3 "What Is a Stack?", §3.10 "What Is a Queue?", §3.15 "What Is a Deque?" | §3.3 "Stacks", §3.10 "Queues", §3.15 "Deques" | The book's own titles (`memory_table_and_readings.md`, Table 2) |
| Python documentation links | `docs.python.org/3/...` | `docs.python.org/3.13/...` | `/3/` now serves the Python 3.15 documentation, and the course uses 3.13 (same file) |
| Take-Homes 25, 28, 29 | "Erickson, Algorithms (free online)" | names the chapter and links its PDF: Chapter 4 for greedy algorithms, Chapter 3 for dynamic programming | I opened both PDFs; the greedy chapter discusses exchange arguments and the dynamic-programming chapter covers edit distance |
| Every take-home | "About 2 hours" | "at least two hours" | The syllabus says "at least 2 hours" (`pedagogy.md`) |

### Answer sheets and instructor key

| Where | Draft 2 | Draft 3 | Evidence |
|---|---|---|---|
| Key, opening claim | every solution was run, and every memory figure "was checked against tracemalloc at the stated input size" | the solutions were run, the tests ship in `tests/`, and the memory figures were recomputed from the size table, with most compared against `tracemalloc` | Several figures were 14 to 50 percent off `tracemalloc`, and frames are invisible to it (`solutions_classes_01_15.md` D24; `solutions_classes_16_30.md`) |
| #933, #102, #1971, #994, #207, #210, #127 | use `deque` with no import | `from collections import deque` added | The printed code raises `NameError` (both solutions notes, D9 and D1) |
| #98 Validate BST | example `[5, 1, 4, null, null, 3, 6]` said to fool a parent-and-child check | uses `[5, 4, 6, null, null, 3, 7]`, which does fool it | The children-only check returns `False` on the first tree and `True` on the second (`solutions_classes_16_30.md`, D2) |
| #98 and #104 | no warning about recursion depth | warns that the recursive solution fails on chains of 1,000 or more nodes and names an iterative version | `RecursionError` at 1,000 nodes; LeetCode allows 10,000 (both solutions notes) |
| #198 House Robber | recurrence `best[i - 2] + nums[i]` | `best[i - 2] + nums[i - 1]` | The stated recurrence raises `IndexError` on both LeetCode examples (`solutions_classes_16_30.md`, D13) |
| #50 Pow(x, n) | no constraints stated | states LeetCode's constraints, and the key notes the division by zero they rule out | `myPow(0.0, -1)` raises `ZeroDivisionError` (`solutions_classes_01_15.md`, D15) |
| #20, #232, #912 statements | each dropped one of LeetCode's conditions | the condition restored | `solutions_classes_01_15.md`, D10, D20 and D22 |
| #104 | second example `root = []` | LeetCode's second example, `[1, null, 2]` | Same file, nits |
| #135 Candy | n = 20,000 "(the LeetCode limit)" | n = 50,000, the real limit, with figures recomputed | LeetCode allows 5 × 10^4^ (`solutions_classes_16_30.md`, D12) |
| #703 and #347 | memory scenarios with 100,000 distinct values | scenarios within LeetCode's limits | At most 20,001 distinct values are possible (same file, D4 and D5) |
| Memory figures | wrong by more than 20 percent, or wrong in their reasoning, for #1480, #88, #1, #1331, #102, #232, #496, #509, #50, #14, #347, #207, #210, #743, #208, #212, #78, #322, #1143, #72, #700, #98 and #684 | recomputed from the size table, with the reasoning stated | Both solutions notes give the key's figure, the formula figure and the measured figure for each |
| Other approaches | missing for #283, #88, #303, #933, #232, #206, #19, #700, #98, #703, #208 and #295; wrong rows for #14, #136, #496 and #739 | tables added and rows corrected | Both solutions notes, D3, D6, D12, D16 and D17 |
| #78 and #51 | auxiliary space given without the output | the output counts, as the course's own rule says | `solutions_classes_16_30.md`, D10 and D11 |
| #704, #34, #300 | `bisect` listed without a note | marked as not allowed at the board | The sheets allow only `collections` and `heapq` (`solutions_classes_01_15.md`, D21) |
| #295 | `addNum` does "at most three heap operations" | three, and five when it rebalances | Instrumented run (`solutions_classes_16_30.md`, D16) |
| #212 | example output `["eat", "oath"]` | notes that the code returns `["oath", "eat"]` and that any order is correct | Same file, D9 |
| Four answer sheets | "for A 50 x 50 grid" and three more | the stray capital removed | Same file, D20 |

### Additions you should check

Draft 3 also adds a few sentences that draft 2 did not have. Each one states a rule that applies whether or not the syllabus mentions it, and each is easy to remove.

1. The syllabus now says that an accommodation approved by Hult's Accessibility Team applies in class, including where it conflicts with the device rule. Section 504 of the Rehabilitation Act forbids rules "such as the prohibition of tape recorders in classrooms" that limit a disabled student's participation (34 CFR 104.44(b)), and Hult's own regulations commit it to reasonable accommodations (`hult_policy_and_governance.md`, risk area 2).
2. The syllabus now says that extra credit covers an absence for the grade in this course only, because Hult counts every absence toward its 30 percent and 50 percent thresholds (Undergraduate Student Handbook §8.1.8, §8.2.2, §8.2.4).
3. The syllabus now gives the tolerance for a correct memory estimate, 30 percent, which the key already used but the syllabus never stated.
4. The "Hult policies" section now names the Accessibility Team, its email address and request form, the sections of the Academic Regulations and the Student Handbook that apply, and Hult's rule that every use of a generative AI tool must be referenced in APA format (Academic Regulations §9.6.3).
5. The answer sheets now include the size table and LeetCode's definitions of `ListNode` and `TreeNode`, because students have no devices in class.

## Your decisions of 12 November 2026

### 1. Grading

Each class now scores 100, an A, for a student who is present and goes to the board, and 0 for a missed class. The course grade is the average of the 30 class scores. Each correct board problem earns 50 points of extra credit, and every 100 points turn one missed class from 0 into 100. Extra credit cannot raise the grade above 100. The grade is now a weighted average of percentage scores, the form that Hult's Academic Regulations describe (§4.2.1). Extra credit for extension problems is still to be set.

### 2. Authorship

Students retain authorship of what they contribute, in a paper or in the live projects, and the syllabus says so. The track's first sentence still says that excellent students "are expected to contribute," as you wrote it.

### 3. The two halves of each class

The first half of each class is the LeetCode board work, in Python only, by hand, with devices locked away. In the second half, students join live projects that you are working on, using Java, Python, Cursor and Claude Code. This matches the languages and tools in Hult's published course description, and it gives outcome 8, finding bugs in code an AI tool wrote, and the build-it half of outcome 5 a place to be practiced. The syllabus adds outcome 10, applying the algorithms and data structures in real software. The licensing for Cursor and Claude Code is still to be added.

### 4. Attendance

Students register their attendance during the second half of class, when devices are out, which removes the conflict between the device ban and Hult's rule that attendance be registered during each session.

### 5. Coverage

The schedule now covers the critical algorithms and data structures. Two pointers and sliding windows share Class 5, monotonic stacks join stacks in Class 6, bit manipulation leaves the course, and intervals join greedy algorithms in Class 26. That frees four classes for new topics:

| Class | New topic | Problem A | Problem B |
|---|---|---|---|
| 11 | Sorting II: quicksort and counting sort | #1122 Relative Sort Array (Easy) | #75 Sort Colors (Medium) |
| 15 | Balanced search trees | #110 Balanced Binary Tree (Easy) | #1382 Balance a Binary Search Tree (Medium) |
| 21 | Shortest paths II: Bellman-Ford and Floyd-Warshall | #1334 Find the City With the Smallest Number of Neighbors at a Threshold Distance (Medium) | #787 Cheapest Flights Within K Stops (Medium) |
| 23 | Minimum spanning trees | #1584 Min Cost to Connect All Points (Medium) | #1489 Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree (Hard) |

Backtracking, now Class 24, comes before tries, now Class 25, so Word Search II no longer needs a technique the class has not met. The take-homes add Big-Omega and Big-Theta (Take-Home 1), hash collisions (4), recurrences and the master theorem (9), insertion sort (10), heap sort (16), adjacency matrices (17) and P, NP and NP-completeness (24). All eight new problems are free on LeetCode, their solutions pass tests against brute-force references in `tests/test_problems_4.py`, and the 22 new practice problems were checked against LeetCode's own data. Every new reading was checked: Runestone §5.12, §6.16 to §6.18 and §7.4 in a browser; Open Data Structures §1.3, Chapter 5, §11.1 and §11.2; and Erickson's Chapters 7, 8, 9 and 12 and his notes on recurrences and disjoint sets.

The eight problems that left the board are #977, #121, #496, #739, #136, #260, #56 and #218. Three of them became practice problems: #977 in Take-Home 5, and #496 and #739 in Take-Home 6. #136, #260, #56, #218 and #121 left the course. Their solutions remain in this branch's history, in draft 3 before this change.

### 6. Sequencing

Three placements break the syllabus's statement that "each class builds on the ones before it."

- Word Search II needed backtracking a class before it was taught. The new schedule fixes this, as described above.
- Class 28's Problem B, #1143 Longest Common Subsequence, is a two-dimensional table one class before the class on two-dimensional tables. Moving it to Class 29 fixes this; draft 3 only corrects the take-home text that described it wrongly.
- Class 1's Problem B, #217 Contains Duplicate, is usually solved with a set, which Class 4 introduces. The key now tells you to accept the nested-loop or sorting solutions in Class 1.

### 7. Take-homes that give away the class problem

The syllabus says that each take-home tells students "only the pattern." Four readings or notes name the problem itself: Take-Home 18 assigns the textbook's Word Ladder section, which is the final class's unlabeled Problem A; Take-Homes 26 and 27 assign §4.12, which works through coin change, Class 27's Problem B; Take-Home 28 names both of Class 28's problems; and Take-Home 29 names edit distance, Class 29's Problem A (`coordinator_observations.md`). Draft 3 keeps all of them.

### 8. Problem choices and readings

All 150 problems are correct, but some fit their class loosely (`leetcode_problems.md`). In Class 3, Problem A and two of the three practice problems involve no prefix sums. #1557 in Take-Home 19 needs no topological sort, and #463 in Take-Home 17 needs no traversal. In seven classes of draft 2's schedule, Problems A and B carried the same rating and Problem B had the higher acceptance rate, so B was not clearly the harder one; the gap was widest in Classes 3 and 5, and Class 3's pair is unchanged. The practice problems also run harder than the class problems in places, with Medium problems in Classes 5 to 8 and a Hard problem in Classes 9 and 21.

Several readings do not teach their class's pattern (`memory_table_and_readings.md`, Table 2). The Class 1 reading has no memory content, Class 3 has nothing on prefix sums, the Class 5 readings do not show two pointers, Class 13's reading has no breadth-first search, Class 19's reading teaches only the depth-first version of topological sort, and the three dynamic-programming classes read only the coin-change section. For sliding windows, monotonic stacks, tries and intervals, the take-homes still name no source but "your AI tool." Take-Home 22 now reads Erickson's notes on disjoint sets in place of the section on Prim's algorithm, which moved to Class 23, where it belongs.

### 9. Teaching design

The research supports most of the design and suggests adjustments to some of it (`pedagogy.md`).

- **Preparation before class.** Meta-analyses of flipped classrooms find moderate gains, largest when the pre-class work is checked. The written plan does that.
- **Time.** At two hours per take-home, four hours a week, the work matches the federal credit-hour floor for a two-credit course but falls short for three credits, which would need about six to seven and a half hours a week outside class (Academic Regulations §3.2.4). The credit value is still blank.
- **Working alone at the board.** Liljedahl's studies of board work used small random groups, not individuals, and measured engagement rather than learning. Behroozi and colleagues found in a randomized study that being watched at a whiteboard more than halved performance. Pair-programming meta-analyses favor pairs.
- **Two failed attempts before help.** Trying before being taught helps, but the benefit depends on instruction afterward. Weaker students, students asking in public and students working in a second language already avoid asking for help. The notes suggest wording that defines an attempt and offers a private way to ask.
- **Hard problems by hand.** Judged by line count, #127, #295, #135 and #51 are realistic in one session, #10 and #212 are writable but error-prone, and #218 is likely to need a hint about the order of events (`solutions_classes_16_30.md`). The key now says so for #218 and #212.
- **AI use.** Bastani and colleagues (PNAS 2025) found that unrestricted AI help lowered later exam scores by 17 percent, while a tutor-style tool with guardrails avoided most of that loss. The rule that students must explain their answers on the spot fits the evidence.
- **The device ban.** The strongest evidence, a randomized trial at West Point, supports banning devices for the distraction they cause, including to students who do not use them.

## Credit hours and other blanks

The course code, credit value, session length and term dates are not public; the CSB program team or the Registry will have them (`hult_policy_and_governance.md`, Gaps). The campus is Boston, the only campus that offers the degree, and the likely prerequisite is "Programming & OOP Thinking With AI," which comes before this course in the Year 1 grid, though Hult does not print a prerequisite. Draft 3 leaves these as bracketed blanks.

## How draft 3 is built

Each document now comes from hand-written Markdown in `source/`. Running `sh build/build.sh` turns the Markdown into Word files with pandoc and into PDFs with LibreOffice. The 60 problems live in one file, `source/problems.md`, which produces both the student sheets and the instructor key, so the two cannot drift apart. The draft label in every footer is set in one place, at the top of `build/build.sh`. `tests/run_tests.sh` extracts every solution from `source/problems.md` and runs the full set of tests against it.
