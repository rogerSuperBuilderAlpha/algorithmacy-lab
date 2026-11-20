# Coordinator observations (my own reading of the draft 2 documents)

Locators are line numbers in the pandoc Markdown conversion of draft 2
(`scratchpad/ads/ADS_Take_Homes.md`, `ADS_Syllabus_Draft.md`), made on 12 Nov 2026.

## Take-homes that point at the in-class problem

The syllabus says students learn the pattern, not the problems ("Problems are given in class. The take-home for each class tells you only the pattern", syllabus line 352). Several take-home readings or pattern notes name the in-class problem itself.

| Take-home | What it names | In-class problem it reveals |
|---|---|---|
| 19 | Reading §7.7 "The Word Ladder Problem" | Class 30 Problem A, #127 Word Ladder (the capstone is meant to carry no topic label) |
| 25 and 27 | Reading §4.12 "Dynamic Programming", which works through coin change | Class 27 Problem B, #322 Coin Change |
| 28 | Pattern note names "longest increasing subsequence and longest common subsequence" | Class 28 Problem A #300 and Problem B #1143 |
| 29 | Note: "Use Erickson ... for edit distance" | Class 29 Problem A, #72 Edit Distance |
| 21 | Pattern note: "defining distance as ... the largest step on the path" | Class 21 Problem B, #1631 Path With Minimum Effort |
| 22 | Pattern note: "detecting the edge that closes a cycle" | Class 22 Problem B, #684 Redundant Connection |

Judgment: the last two are fair teaching of the pattern. The first four hand students the problem. Decision for the instructor; the rewrite keeps every reading and note.

## Statements in the take-homes that are wrong or misleading

1. Take-Home 1, question 8 (TH line 72-74): "Predict the memory of a list of 100,000 ints using 8 bytes per pointer plus 28 bytes per int. Then check your prediction with sys.getsizeof." `sys.getsizeof(lst)` returns only the list object (header plus pointer array), not the ints it points to, so a student following the instruction gets about 800 KB against a prediction of about 3.6 MB and concludes the model is wrong. Rewrite tells the student to add the ints' sizes. (Python docs, sys.getsizeof: "Only the memory consumption directly attributed to the object is accounted for, not the memory consumption of objects it refers to.")
2. Take-Home 29, "Builds on" (TH 29): "Class 28 used one sequence; now two sequences or a grid give a table." Class 28 Problem B is #1143 Longest Common Subsequence, which takes two strings and fills a two-dimensional table. The rewrite says Class 28 met its first two-dimensional table in LCS.
3. Take-Home 28, "Builds on": "class 29 will use two sequences at once" has the same problem: Class 28 already does.

## Sequencing

- Class 1 Problem B, #217 Contains Duplicate, is solved in the key with a set. Hashing is taught in Class 4. The syllabus says "Each class builds on the ones before it" (line 47). A student meeting #217 in Class 1 has the sort-then-compare or nested-loop approaches available; the key's set solution assumes Class 4. Decision for the instructor.
- Class 28 Problem B (#1143 LCS) is a two-dimensional DP problem placed one class before "Dynamic programming: 2D tables" (Class 29).

## Corrections taken from curriculum.md (applied in the rewrite)

4. Take-Home 24, "Builds on": draft 2 says class 18 DFS supplies "the idea of exploring and un-marking". Class 18's DFS marks cells visited and never un-marks them (curriculum.md, sequence check, citing T:1249, T:1310, T:1691-1693). The rewrite says backtracking adds the un-marking step.
5. Take-Home 22, "Builds on": draft 2 says union-find "uses a parent list like the array heap of class 17". A heap stores a complete tree by index arithmetic; union-find stores explicit parent links. The rewrite drops the heap comparison and describes the parent list directly.
