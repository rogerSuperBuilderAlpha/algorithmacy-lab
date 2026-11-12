# LeetCode problems in the ADS course drafts: accuracy and fit

**Summary of defects found.** Method: I parsed the four Markdown conversions, then read every problem's record from LeetCode's GraphQL endpoint (https://leetcode.com/graphql, fields questionFrontendId, title, titleSlug, difficulty, isPaidOnly, topicTags, stats.acRate), 150 slugs in all (60 in-class + 90 take-home; no slug repeats). Scripts and raw JSON: /private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads-tests/leetcode/ (lc.json holds the raw answers). The suggested /api/problems/all/ list returned HTTP 403 from Cloudflare (even with a browser User-Agent), so I did not use it; GraphQL answered with HTTP 200 for all 150.

- Hard defects (number, title, level, URL slug, free/premium): **none found.** All 150 problems match LeetCode on number, title, difficulty and slug, in every document, and none is paid_only.
- The four documents agree: Syllabus, Board and Solutions give the same number and title for all 30 classes x 2 slots; Board and Solutions also agree on level and URL for all 60.
- No problem is used twice. No take-home problem is an in-class problem (by number, across all 30 classes).
- Ramp: all 30 in-class pairs match the ramp table (Syllabus lines 218-242). Class 29 (Medium/Hard) and 30 (Hard/Hard) are consistent with the ambiguous row "Medium or Hard, then Hard".
- Problem B is never lower in LeetCode level than Problem A. But in 7 classes (3, 5, 6, 7, 20, 21, 30) B has the same level as A and a higher acceptance rate, so by that evidence B is not harder (3, 5, 6, 7, 30 are the clearest, 4 to 25 points higher).
- Fit defects (judgment, not hard errors):
  1. Class 3 (Strings and prefix sums): in-class A #14 is not a prefix-sum problem (tags Array, String, Trie); take-home #28 and #58 are not prefix-sum problems either.
  2. Class 6 B #121 carries the LeetCode tag Dynamic Programming, not Sliding Window.
  3. Class 20 take-home #1557 needs no topological sort (only in-degree 0 nodes).
  4. Class 26 take-home #228 Summary Ranges is not an interval merge/sweep problem (tag Array only).
  5. Class 18 take-home #463 can be solved without any traversal.
  6. Difficulty of take-homes does not follow the in-class ramp: Medium problems in classes 5-8 (in-class Easy/Easy), Hard #239 in class 9, Hard #778 in class 21 (in-class Medium/Medium); and "do all, in this order" lists are not easy-first in classes 8 and 13.
  7. Class 1 B #217 (Contains Duplicate) is a hash-set problem taught in class 4 (a sorting answer also works).
- Take-home problems closely related (not identical) to an in-class problem: #503 (NGE II, class 9) to #496; #219 to #217; #167 to #1; #122 to #121; #79 to #212; #213 and #746 to #198. Not a defect under the "different problem" rule, but worth knowing.

## Is each problem named, numbered, linked, rated correctly, and free?

### Takeaway
All 60 in-class and 90 take-home problems match LeetCode on number, title, difficulty and URL slug, and none is premium. I found no hard defect.

### Cited Findings
- For all 150 slugs, questionFrontendId equals the document's number, title equals the document's title (whitespace-normalised) and difficulty equals the document's level; the URL in the document equals https://leetcode.com/problems/{titleSlug}/ — [LeetCode GraphQL](https://leetcode.com/graphql) (fields questionFrontendId, title, titleSlug, difficulty)
- isPaidOnly is false for all 150 — [LeetCode GraphQL](https://leetcode.com/graphql) (field isPaidOnly)
- Syllabus schedule (ADS_Syllabus_Draft.md lines 254-347) lists numbers and titles with no URL; all 60 numbers and titles match LC, and the row-level "Easy / Easy" style labels match the LC difficulty of both slots in all 30 rows — [LeetCode GraphQL](https://leetcode.com/graphql)
- Board (ADS_In_Class_Board_Problems.md) and Solutions (ADS_In_Class_Solutions.md) each carry the number, title, level and URL for 60 problems, identical to each other and to the Syllabus for the same class and slot; Board lines run from 36 (class 1 A) onward, Solutions from 68 — own parse of the files (class/slot/number/title/level/url compared programmatically)
- Take-home tables: 3 problems per take-home x 30 take-homes = 90, every one parsed with number, title, Level column and URL; all match — own parse of ADS_Take_Homes.md plus [LeetCode GraphQL](https://leetcode.com/graphql)

### Inferences
- The professor can keep every number, title, level and link as drafted. The syllabus sentence "number and difficulty as listed on leetcode.com" (line 246-248) holds today.
- Difficulty and acceptance values are live and can shift; LeetCode relabels problems occasionally. A re-run of lc.json before term is cheap.

### Gaps
- The bulk list /api/problems/all/ was blocked (HTTP 403), so I did not cross-check against it. The GraphQL answers are from the same site.
- I did not test whether Python solutions are accepted on all problems, or whether the web pages need an account for the Python 3 judge; premium status is the only access check I made.
- Syllabus has no URLs, so URL slug checks apply to Board, Solutions and Take-Homes only.

## Do the four documents agree, and is any problem used twice?

### Takeaway
Yes, they agree, and no problem is reused: the 150 problem numbers are all distinct, so no take-home problem equals an in-class problem in any class.

### Cited Findings
- Syllabus, Board and Solutions agree on number and title for all 60 class/slot positions (own parse); Board and Solutions agree on level and URL for all 60.
- 150 distinct slugs and 150 distinct numbers across Board and Take-Homes (own parse of ADS_In_Class_Board_Problems.md and ADS_Take_Homes.md); no number appears twice.
- The syllabus rule "give different practice problems of the same type" (ADS_Syllabus_Draft.md line 353) is therefore met at the level of identity.

### Inferences
- Near-neighbours (same-family variants) exist, see Question 4. I count them as compliant, as the rule says "different".

### Gaps
- I did not check whether any take-home problem is solvable only by adapting an in-class solution that is shown in the Solutions document.

## Do the in-class pairs match the ramp, and is B at least as hard as A?

### Takeaway
All 30 pairs match the ramp table; B is never rated below A, but in 7 classes both are the same level and acceptance rate suggests B is not harder.

### Cited Findings
- Ramp table is at ADS_Syllabus_Draft.md lines 218-242; LC difficulties (classes 1-8 Easy/Easy; 9-19 Easy/Medium; 20-22 Medium/Medium; 23-26 Medium/Hard; 27-28 Medium/Medium; 29 Medium/Hard; 30 Hard/Hard) — [LeetCode GraphQL](https://leetcode.com/graphql) (field difficulty). Zero mismatches.
- Same-level classes where B's acRate exceeds A's (A vs B): class 3 #14 48.6% vs #303 73.9%; class 5 #125 54.6% vs #977 74.3%; class 6 #643 49.6% vs #121 57.6%; class 7 #20 45.4% vs #844 50.4%; class 20 #207 52.5% vs #210 56.5%; class 21 #743 61.9% vs #1631 64.3%; class 30 #127 46.9% vs #295 55.2% — [LeetCode GraphQL](https://leetcode.com/graphql) (field stats.acRate, read 2026-11-12)
- Across levels, B is lower-acceptance in most classes; e.g. class 24 Hard #51 76.8% vs Medium #78 83.0% is the same direction, so acceptance is only a weak guide — same source.

### Inferences
- Judgment: acceptance rate depends on the problem's popularity and test difficulty, not purely on conceptual difficulty. The classes with the largest gaps (3, 5) are the ones where "B harder" is least supported; #303 and #977 are well-known, templated Easy problems. Consider swapping A and B in classes 3 and 5 (professor's decision).
- Judgment: class 29's syllabus label "Medium / Hard" is a legal reading of ramp row "Medium or Hard, then Hard"; the ramp text itself is ambiguous ("29 to 30").

### Gaps
- No instructor-timed data for how long each takes at a chalkboard.

## Does each practice problem exercise the pattern its take-home names?

### Takeaway
Mostly yes. LeetCode tags support the pattern for about 80 of 90 problems. Judgment flags: #28, #58 (class 3), #1557 (class 20), #228 (class 26), #463 (class 18); class 1 is generic.

### Cited Findings
- Tag-to-pattern evidence per problem is in the take-home table below (column LC topicTags) — [LeetCode GraphQL](https://leetcode.com/graphql) (field topicTags).
- Tags missing the named pattern: #28 (Two Pointers, String, String Matching, Z Algorithm, KMP, Boyer-Moore) and #58 (String) in class 3 "Strings and prefix sums"; only #724 is tagged Prefix Sum. #1557 is tagged Graph Theory and Directed Acyclic Graph, not Topological Sort (class 20). #228 and #57 are tagged Array only (class 26 "Intervals: sort, then sweep"; only #452 is tagged Sorting).
- Class 1's three problems (#1672, #1929, #1295) are tagged Array/Matrix/Simulation/Math; the pattern "Complexity analysis" has no LC tag, so tags cannot confirm it.
- Class 11 #22 Generate Parentheses is tagged Backtracking, which is class 24's topic; it also carries Recursion-style structure (tags: String, Dynamic Programming, Backtracking, Bracket Sequences).

### Inferences
- JUDGMENT: #28 and #58 are string scans, not prefix-sum problems, and the class-3 set only has one prefix-sum item; replace #58 or #28 with e.g. a prefix-sum problem (professor's call; I did not verify candidate replacements here).
- JUDGMENT: #1557 is an in-degree-zero count; consider a problem tagged Topological Sort (e.g. #802 and #2115 are already in the set, #1557 is the weak one).
- JUDGMENT: #463 Island Perimeter can be counted cell by cell; #228 Summary Ranges is a run scan, not a sort-then-sweep.
- JUDGMENT: the take-home difficulty does not follow the ramp: classes 5-8 take-homes contain Mediums (#167, #11, #1456, #3, #155, #150, #622) while in-class is Easy/Easy; class 9 has Hard #239 and class 21 has Hard #778 while in-class B is Medium; "do all, in this order" is not easy-first in class 8 (Easy, Medium, Easy) and class 13 (Medium, Medium, Easy).
- Class 6 B in-class #121 is tagged Dynamic Programming, not Sliding Window; class 3 A #14 is tagged Trie, not Prefix Sum (judgment: both are weak fits to their class topic).

### Gaps
- I did not read the problem statements of all 90 take-homes line by line; judgments rest on tags plus my knowledge of each problem's standard solution. Mark as judgment.

