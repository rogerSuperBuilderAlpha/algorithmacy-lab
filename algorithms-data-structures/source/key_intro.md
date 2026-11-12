---
title: In-Class Solutions
subtitle: Instructor key. Algorithms & Data Structures, Professor Roger Hunt
---

This key gives, for each of the 60 board problems, a solution that a student can write at the board, an explanation of how it works, its time and auxiliary space, a memory estimate at the input size printed on the student's sheet, and other approaches with their cost.

Every board solution in this key has been run on Python 3.13 against LeetCode's examples, against edge cases at LeetCode's limits, and against random inputs checked by a slower brute-force solution, and every one returned correct results. The test scripts are in the `tests` folder beside this document, so you can run them again. Every memory figure was recomputed from the course's table of sizes, and most were also compared with measurements from `tracemalloc`. Those measurements run about 10 percent higher on inputs full of integers, because `tracemalloc` counts 32 bytes for each integer rather than 28, and they miss recursive calls entirely, because `tracemalloc` does not count call frames.

# How to use this key

**Credit.** An answer earns extra credit only if the student can explain and defend it. Ask why the solution works, why its complexity is what the student wrote, and what would change for a different input.

**Auxiliary space.** Auxiliary space is the extra memory a solution uses beyond its input, and it includes anything the solution builds and returns. Where the output dominates, as in Subsets or N-Queens, the key says so.

**Memory estimates.** The memory figures are estimates. Accept any answer within about 30 percent of the key's figure when the student writes down sensible assumptions, such as a different n, a differently shaped input or a different version of Python. Grade the method: the student should count list pointers and object sizes, use the right n, and count the input separately from the auxiliary data. KB means 1,024 bytes and MB means 1,048,576 bytes.

**Other approaches.** Each problem lists other approaches with their cost. Accept any of them if the student analyzes it correctly.

**Asking for help.** A student who asks for help must first show two failed attempts at the bottom of the answer sheet.

**Recursion.** Python stops a recursion at a depth of 1,000 unless the limit is raised. Where a recursive solution can exceed that depth at LeetCode's limits, the key says so and names a version without recursion.

# Memory sizes in CPython 3.13 on a 64-bit machine

| Object | Approximate size |
|------------|------------------------------------------------|
| int | 28 bytes below 2^30^, about one billion, and 4 bytes more for each further 30 bits. The integers from −5 to 256 are shared and cost nothing extra. |
| float | 24 bytes. |
| True, False and None | Shared, so only the 8-byte pointer to them counts. |
| str | 41 bytes plus 1 byte per character for plain ASCII text. A one-character string is shared when the character is one of the first 256. |
| list | 56 bytes plus 8 bytes per slot. `[0] * n` and `list(...)` give exactly n slots; a list built with `append` or a comprehension keeps up to about 13 percent spare slots, about 6 percent on average. |
| tuple | 40 bytes plus 8 bytes per item: 56 for a pair and 64 for a triple. |
| dict | 64 bytes when empty, and 184 bytes with one to five string keys. With integer keys, about 37 bytes per entry at 1,000 entries, 30 at 10,000 and 52 at 100,000; with string keys, about 26 at 1,000 and 38 at 100,000. |
| set | At least 216 bytes. About 33 bytes per element at 1,000 elements and 42 at 100,000. |
| deque | About 760 bytes plus 8.3 bytes per element. |
| node object | About 90 bytes for a ListNode and 100 for a TreeNode, plus 28 bytes for a value outside −5 to 256. |
| recursive call | About 150 to 250 bytes for each call that has not yet returned, more for a function with many local variables. |

A dict or a set grows by building a bigger table and copying itself into it, so at large sizes it briefly holds about 1.5 times its final table. Lists and deques grow without such a jump.
