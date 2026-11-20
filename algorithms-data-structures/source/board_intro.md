---
title: In-Class Board Problems
subtitle: Student answer sheets. Algorithms & Data Structures, Professor Roger Hunt
---

Use one sheet for each problem. Solve the problem at the board in chalk first, and then copy your Python solution onto the sheet and fill in the analysis below it.

1. Phones and computers are locked away for the first half of class, while you work at the board, and you work on your own.
2. Write a plain Python function. You may use anything built into Python, plus `deque` from the `collections` module and the `heapq` module.
3. State the time complexity and the auxiliary space in Big-O. Auxiliary space is the extra memory your solution uses beyond its input, and anything your solution builds and returns counts toward it.
4. Estimate the memory for the input size printed on the sheet. Give the memory that the input uses, the memory that your own data uses, and the total, in bytes, and write down your assumptions.
5. If you get stuck, you may ask for help once you have made two attempts that did not work. Write both attempts at the bottom of the sheet before you ask.
6. A correct answer earns 50 points of extra credit, which makes up for missed classes. An answer is correct when the solution works, the time and space are right, and the memory estimate is within about 30 percent of the key.

## Memory sizes in CPython 3.13 on a 64-bit machine

| Object | Approximate size |
|------------|------------------------------------------------|
| int | 28 bytes below 2^30^, about one billion. The integers from −5 to 256 are shared and cost nothing extra. |
| float | 24 bytes. |
| True, False and None | Shared, so only the 8-byte pointer to them counts. |
| str | 41 bytes plus 1 byte per character for plain ASCII text. A one-character string is shared. |
| list | 56 bytes plus 8 bytes per slot. A list built with `append` keeps up to about 13 percent spare slots, about 6 percent on average. |
| tuple | 40 bytes plus 8 bytes per item. |
| dict | 64 bytes when empty. With integer keys, about 37 bytes per entry at 1,000 entries, 30 at 10,000 and 52 at 100,000. |
| set | At least 216 bytes. About 33 bytes per element at 1,000 elements and 42 at 100,000. |
| deque | About 760 bytes plus 8.3 bytes per element. |
| node object | About 90 to 100 bytes, plus 28 bytes for a value outside −5 to 256. |
| recursive call | About 150 to 250 bytes for each call that has not yet returned. |

A list holds pointers only, so count the objects it points to separately. A dict or a set briefly holds about 1.5 times its final table while it grows. KB means 1,024 bytes and MB means 1,048,576 bytes.

## Node classes

LeetCode defines the node classes for the linked-list and tree problems as follows. You may use them without writing them out.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
