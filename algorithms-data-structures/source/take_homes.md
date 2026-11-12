---
title: Take-Homes
subtitle: One take-home for each of the 30 classes. Algorithms & Data Structures, Professor Roger Hunt
---

Each take-home prepares you for one class. It names the pattern you will meet in that class, explains the idea behind it, assigns a reading, and lists LeetCode practice problems of the same type. The problems you solve in class are different from the practice problems, and you see them only when class begins.

Plan on at least two hours for each take-home. Read the assigned sections first, then attempt the practice problems on LeetCode, and then write your plan on paper. You may use AI tools to learn the pattern, and I expect you to.

Most readings come from the free textbook *Problem Solving with Algorithms and Data Structures using Python*, on Runestone Academy: <https://runestone.academy/ns/books/published/pythonds3/index.html>. Where the textbook does not cover a pattern, the take-home says so and points you to another source.

::: {#standard-plan}
## Your plan

Choose one of the practice problems and write a plan for it on paper before you write any code. Your plan answers these six questions.

1. What does the problem ask, in your own words, and what is the size of the input, n?
2. What is the brute-force approach, meaning the simplest approach that tries every possibility, and what is its Big-O running time?
3. Which pattern will you use, and why does it fit this problem?
4. What are the steps of your solution, written in plain English rather than in code?
5. What running time and auxiliary space do you expect, and how many bytes of memory will your solution use when n is 100,000?
6. Which two edge cases must your solution handle? An edge case is an unusual input, such as an empty list, that a correct solution must still handle.

Bring your written plan to class. Phones and computers are locked away during class, so the plan must be on paper.
:::

# Take-Home 1: Big-O and Python memory

*For Class 1. I post this take-home before the first class, and it is due on paper at the start of Class 1. Plan on at least two hours.*

## The pattern: complexity analysis

Big-O notation describes how the cost of a solution grows as its input grows. The cost can be time, counted as the number of basic steps the solution takes, or space, counted as the extra memory it needs. To find the Big-O, keep only the term that grows fastest and drop any constant factor: a loop that takes 3n + 5 steps is O(n). Python adds a second kind of cost, which you will estimate in every class: the actual number of bytes. Every Python integer is an object of about 28 bytes, and a list stores an 8-byte pointer to each of its elements, so a list of n large integers uses about 36n bytes.

## How this builds on earlier classes

This is the first class. Every class after it uses these two tools, Big-O and the byte count, to judge a solution.

## Reading

- [§2.2 What Is Algorithm Analysis?](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html)
- [§2.3 Big O Notation](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/BigONotation.html)
- [§2.5 Performance of Python Data Structures](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/PerformanceofPythonDataStructures.html)
- [Python documentation: sys.getsizeof](https://docs.python.org/3.13/library/sys.html#sys.getsizeof)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy |
| 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy |
| 1295 | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. For one of the practice problems, count how many times your loop runs as a function of n, and write the Big-O.
8. Predict how many bytes a list of 100,000 integers uses, at 8 bytes for each pointer plus 28 bytes for each integer. Then, outside class, check your prediction in Python. Keep in mind that `sys.getsizeof` of a list counts only the list and its pointers, so you must add the sizes of the integers yourself.

# Take-Home 2: Arrays and in-place updates

*For Class 2. I hand this out at the end of Class 1, and it is due on paper at the start of Class 2. Plan on at least two hours.*

## The pattern: a read index and a write index

A Python list is a dynamic array: a block of memory that holds pointers in order and grows when it fills up. Reading or writing any position by its index takes O(1) time, and appending at the end takes O(1) time on average. Inserting or deleting at the front takes O(n) time, because every later element has to shift by one place. Many array problems can be solved in place, inside the input list itself, with two indexes: a read index that scans every element and a write index that marks where the next value you keep should go.

## How this builds on earlier classes

Class 1 gave you Big-O and the memory model. In this class you apply them to the most basic structure in Python, the list.

## Reading

- [§2.6 Lists](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/Lists.html)
- [§1.8 Getting Started with Data](https://runestone.academy/ns/books/published/pythonds3/Introduction/GettingStartedwithData.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Easy |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. Which list operations in your plan take O(1) time and which take O(n)? Name each one.
8. Could your plan work with O(1) extra space? If so, what would you have to change inside the input list to make it work?

# Take-Home 3: Strings and prefix sums

*For Class 3. I hand this out at the end of Class 2, and it is due on paper at the start of Class 3. Plan on at least two hours.*

## The pattern: strings and prefix sums

A Python string cannot be changed after it is created, so every slice and every concatenation builds a new string, and that costs time and memory in proportion to the string's length. A prefix sum is a list of running totals, in which each entry holds the sum of all the values before it. You build it once, in O(n) time, and afterward you can find the sum of any range of values with a single subtraction. Doing work once, up front, so that many later questions become cheap is a trade of memory for time, and you will see that trade throughout the course.

## How this builds on earlier classes

Class 2 worked with indexes into lists. A string behaves like a list that you can read but not change, and a prefix-sum list is a list that you build once and then reuse.

## Reading

- [§2.4 An Anagram Detection Example](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/AnAnagramDetectionExample.html)
- [§1.8 Getting Started with Data](https://runestone.academy/ns/books/published/pythonds3/Introduction/GettingStartedwithData.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy |
| 28 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | Easy |
| 58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. Which step in your plan copies a string or a list, and what does that copy cost?
8. If your solution had to answer many questions about the same input, what could you compute once, up front?

# Take-Home 4: Hash sets and hash maps

*For Class 4. I hand this out at the end of Class 3, and it is due on paper at the start of Class 4. Plan on at least two hours.*

## The pattern: hashing with sets and dicts

A hash table finds, inserts and deletes a key in O(1) time on average. It does this by turning the key into a position in an array, so that it can go straight to the key instead of searching for it. Python gives you two hash tables. A set remembers which values you have seen. A dict, short for dictionary, remembers something about each value you have seen, such as how many times it appeared or where. Spending O(n) memory on a hash table often turns an O(n²) search into an O(n) one.

## How this builds on earlier classes

Class 3 stored values you had computed in advance in a list, where you find each one by its position. A hash table stores values by key, so you can find a value without knowing where it sits.

## Reading

- [§5.5 Hashing](https://runestone.academy/ns/books/published/pythonds3/SortSearch/Hashing.html)
- [§2.7 Dictionaries](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/Dictionaries.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | Easy |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy |
| 219 | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. What are the keys and the values in your dict, or what does your set hold?
8. What is the Big-O of the brute-force approach, and what does the hash table change?

# Take-Home 5: Two pointers

*For Class 5. I hand this out at the end of Class 4, and it is due on paper at the start of Class 5. Plan on at least two hours.*

## The pattern: two pointers

In the two-pointer pattern you keep two indexes and move them according to a rule. In one version the pointers start at the two ends of a list and move toward each other. In the other version both pointers move forward, one reading and one writing, as they did in Class 2. Each pointer only ever moves in one direction, so together they cross the list at most once, and the scan takes O(n) time and O(1) extra space.

## How this builds on earlier classes

Class 2 used a read index and a write index. This class adds the version with a pointer at each end, which takes advantage of a list that is sorted or a string that reads the same in both directions.

## Reading

- [§3.18 Palindrome Checker](https://runestone.academy/ns/books/published/pythonds3/BasicDS/PalindromeChecker.html)
- [§5.3 The Sequential Search](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheSequentialSearch.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Where does each pointer start, and what rule decides which pointer moves?
8. Why does your rule never skip over a correct answer? Justify it in one sentence.

# Take-Home 6: Sliding window

*For Class 6. I hand this out at the end of Class 5, and it is due on paper at the start of Class 6. Plan on at least two hours.*

## The pattern: sliding window

A window is a stretch of neighboring elements in a list, marked by a left index and a right index. Instead of recomputing everything about the window each time it moves, you update it: you add the element that enters on the right and remove the element that leaves on the left. For a window of fixed size k, this turns an O(nk) scan into an O(n) scan. Other windows change size as they move: the right edge grows the window, and the left edge shrinks it whenever a condition stops holding.

## How this builds on earlier classes

Class 5 moved two pointers along a list, and a window is the stretch between two such pointers. The prefix sums of Class 3 kept running totals, which is the same idea as the running sum that a window keeps.

## Reading

- [§2.4 An Anagram Detection Example](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/AnAnagramDetectionExample.html)

Runestone has no section on sliding windows. Read the section above for its counting technique, and then study fixed-size and variable-size windows with the Python documentation and your AI tool.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 1984 | [Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) | Easy |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What do you keep track of for the window: a sum, a count, or a set?
8. Write the two update steps: what happens when an element enters the window, and what happens when an element leaves it?

# Take-Home 7: Stacks

*For Class 7. I hand this out at the end of Class 6, and it is due on paper at the start of Class 7. Plan on at least two hours.*

## The pattern: the stack, last in and first out

A stack works like a pile of plates: you add and remove items only at the top, so the last item in is the first item out. Both operations, called push and pop, take O(1) time. Use a stack when the most recent unfinished item has to be dealt with first, as with matching brackets, undo, backspaces and anything nested inside something else. In Python a list works as a stack: `append` pushes an item, and `pop` removes the item on top.

## How this builds on earlier classes

Class 4 used extra memory to remember what you had already seen. A stack also remembers the past, but it keeps it in order, with the newest item always on top.

## Reading

- [§3.3 Stacks](https://runestone.academy/ns/books/published/pythonds3/BasicDS/WhatisaStack.html)
- [§3.5 Implementing a Stack in Python](https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementingaStackinPython.html)
- [§3.6 Simple Balanced Parentheses](https://runestone.academy/ns/books/published/pythonds3/BasicDS/SimpleBalancedParentheses.html)
- [§3.7 Balanced Symbols (A General Case)](https://runestone.academy/ns/books/published/pythonds3/BasicDS/BalancedSymbolsAGeneralCase.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 682 | [Baseball Game](https://leetcode.com/problems/baseball-game/) | Easy |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What do you push onto the stack, and what event makes you pop?
8. What does the stack hold at the end if the input is valid, and what does it hold if the input is not valid?

# Take-Home 8: Queues and deques

*For Class 8. I hand this out at the end of Class 7, and it is due on paper at the start of Class 8. Plan on at least two hours.*

## The pattern: the queue, first in and first out

A queue serves items in the order they arrived, like a line at a counter: you add items at the back and remove them from the front. A Python list makes a poor queue, because removing from the front with `pop(0)` takes O(n) time while every other element shifts forward. The `deque` from Python's `collections` module, whose name is short for double-ended queue, adds and removes items at both ends in O(1) time. Queues also model streams of events in which only the recent events matter.

## How this builds on earlier classes

The stacks of Class 7 give items back in reverse order, while queues keep them in their original order. Together they are the two basic structures for holding items in a line.

## Reading

- [§3.10 Queues](https://runestone.academy/ns/books/published/pythonds3/BasicDS/WhatIsaQueue.html)
- [§3.12 Implementing a Queue in Python](https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementingaQueueinPython.html)
- [§3.13 Queue Simulation: Hot Potato](https://runestone.academy/ns/books/published/pythonds3/BasicDS/SimulationHotPotato.html)
- [§3.15 Deques](https://runestone.academy/ns/books/published/pythonds3/BasicDS/WhatIsaDeque.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy |
| 622 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | Medium |
| 1700 | [Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. At which end do items enter, and at which end do they leave?
8. How can you build a queue out of stacks, or a stack out of queues, and what does that cost for each operation?

# Take-Home 9: Monotonic stack and deque

*For Class 9. I hand this out at the end of Class 8, and it is due on paper at the start of Class 9. Plan on at least two hours.*

## The pattern: a stack kept in sorted order

A monotonic stack keeps its items in sorted order. Before you push a new item, you pop every item that can no longer be the answer to any later question. Each item is pushed once and popped at most once, so a search that looks like O(n²), such as finding the next larger value for every element of a list, takes only O(n) time. A monotonic deque applies the same idea at both of its ends and solves problems such as finding the largest value in every window of a list.

## How this builds on earlier classes

Class 7 gave you the stack and Class 8 gave you the deque. In this class you keep them in sorted order while you scan, which answers questions of the form "what is the next larger value?"

## Reading

- [§3.15 Deques](https://runestone.academy/ns/books/published/pythonds3/BasicDS/WhatIsaDeque.html)
- [§3.17 Implementing a Deque in Python](https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementingaDequeinPython.html)
- [Python documentation: collections.deque](https://docs.python.org/3.13/library/collections.html#collections.deque)

Runestone does not cover monotonic stacks. Ask your AI tool to trace one by hand on a small list, and then redo the trace yourself without help.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium |
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | Medium |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard |

::: plan
:::

## Two more questions about this pattern

7. Do the values on your stack increase or decrease from bottom to top, and why?
8. Each element is pushed once and popped at most once. Use that fact to argue what the total running time is.

# Take-Home 10: Linked lists

*For Class 10. I hand this out at the end of Class 9, and it is due on paper at the start of Class 10. Plan on at least two hours.*

## The pattern: rewiring pointers

A linked list stores each value in its own node, and each node points to the next node. Inserting or deleting at a node you already hold takes O(1) time, but reaching the kth node takes O(k) time, because you must walk there from the head, the first node. Most linked-list problems are solved by walking the list with one or two pointers and carefully changing the `next` pointers. A dummy node placed in front of the head often removes special cases, such as deleting the head itself.

## How this builds on earlier classes

The two pointers of Class 5 now walk from node to node instead of from index to index. The queues of Class 8 can also be built out of linked nodes.

## Reading

- [§3.19 Lists](https://runestone.academy/ns/books/published/pythonds3/BasicDS/Lists.html)
- [§3.21 Implementing an Unordered List: Linked Lists](https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html)
- [§3.23 Implementing an Ordered List](https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganOrderedList.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. Draw the list as boxes and arrows before and after your change. Which pointers change, and in what order?
8. What happens when the list is empty, when it has one node, and when you have to change the head?

# Take-Home 11: Recursion

*For Class 11. I hand this out at the end of Class 10, and it is due on paper at the start of Class 11. Plan on at least two hours.*

## The pattern: recursion and divide and conquer

A recursive function solves a problem by solving smaller copies of the same problem, and a base case stops the recursion. The running time depends on how many calls the function makes and how much work each call does. The space depends on how deep the calls go, because every call that has not yet returned keeps a frame on the call stack. When the same smaller problem is solved again and again, as in the naive Fibonacci function, recursion takes exponential time unless you store the answers you have already found. Divide and conquer is the form of recursion that splits a problem into parts, solves each part, and combines the results.

## How this builds on earlier classes

Class 10 walked a list one node at a time. Recursion lets a function call itself on the rest of the structure. The call stack that keeps track of those calls is the stack from Class 7.

## Reading

- [§4.2 What Is Recursion?](https://runestone.academy/ns/books/published/pythonds3/Recursion/WhatIsRecursion.html)
- [§4.4 The Three Laws of Recursion](https://runestone.academy/ns/books/published/pythonds3/Recursion/TheThreeLawsofRecursion.html)
- [§4.6 Stack Frames: Implementing Recursion](https://runestone.academy/ns/books/published/pythonds3/Recursion/StackFramesImplementingRecursion.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 231 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Easy |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. State the base case and the recursive case, in one sentence each.
8. Draw the tree of recursive calls for a small input. How many calls are there, and how deep does the tree go?

# Take-Home 12: Bit manipulation

*For Class 12. I hand this out at the end of Class 11, and it is due on paper at the start of Class 12. Plan on at least two hours.*

## The pattern: working with bits

Python stores integers in binary, and the operators `&` (and), `|` (or), `^` (exclusive or, called XOR), `<<` (shift left) and `>>` (shift right) work on each bit separately. XOR follows two useful rules, x ^ x = 0 and x ^ 0 = x, so values that appear in pairs cancel each other out. The expression `x & -x` keeps only the lowest bit of x that is set to 1. Tricks like these often need O(1) extra space where a hash table would need O(n).

## How this builds on earlier classes

In Class 11 you halved a number at each step of a recursion; a right shift halves a number in a single operation. In Class 4 a hash table spent O(n) memory, and XOR can sometimes avoid that cost.

## Reading

- [§3.8 Converting Decimal Numbers to Binary Numbers](https://runestone.academy/ns/books/published/pythonds3/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html)
- [Python documentation: bitwise operations on integer types](https://docs.python.org/3.13/builtins/stdtypes.html#bitwise-operations-on-integer-types)

Runestone has no section on bit manipulation. Read the Python documentation, and then trace each operator by hand on 8-bit numbers.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. Write the numbers in your example in binary. What does each operator in your plan do to them?
8. Which rule, such as x ^ x = 0, does your plan depend on?

# Take-Home 13: Sorting

*For Class 13. I hand this out at the end of Class 12, and it is due on paper at the start of Class 13. Plan on at least two hours.*

## The pattern: merge sort and sorting first

No sorting method that works by comparing pairs of elements can do better than O(n log n) time in the worst case. Merge sort reaches that bound: it splits the list in half, sorts each half, and merges the two sorted halves in O(n) time. Merge sort is stable, which means that equal elements keep their original order, and it needs O(n) extra space. Sorting first often makes the rest of a problem easy, because duplicates end up next to each other, pairs can be found with two pointers, and binary search becomes possible.

## How this builds on earlier classes

Merge sort has the shape of the recursion from Class 11, and its merge step is the two-pointer scan from Class 5, the same scan that merged two sorted lists in Class 2.

## Reading

- [§5.6 Sorting](https://runestone.academy/ns/books/published/pythonds3/SortSearch/sorting.html)
- [§5.9 The Insertion Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheInsertionSort.html)
- [§5.11 The Merge Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheMergeSort.html)
- [§5.12 The Quicksort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheQuickSort.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) | Medium |
| 506 | [Relative Ranks](https://leetcode.com/problems/relative-ranks/) | Easy |

::: plan
:::

## Two more questions about this pattern

7. Which sort will you use, and what are its running time and its extra space?
8. Does the order of equal elements matter in your problem? In other words, do you need a stable sort?

# Take-Home 14: Binary search

*For Class 14. I hand this out at the end of Class 13, and it is due on paper at the start of Class 14. Plan on at least two hours.*

## The pattern: halving a sorted range

On a sorted list, binary search compares the target with the middle element and throws away the half that cannot contain it. That takes O(log n) time and O(1) space. The hard part is the details: which half to keep, whether the middle element stays in the range, and when to stop. Practice writing the loop around an invariant, a statement that is true at the top of every pass through the loop, such as "if the answer exists, it lies between lo and hi."

## How this builds on earlier classes

Class 13 produced sorted data, and sorted data is what binary search needs. The halving you saw in the recursion of Class 11 becomes a loop here.

## Reading

- [§5.4 The Binary Search](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheBinarySearch.html)
- [Python documentation: bisect](https://docs.python.org/3.13/library/bisect.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy |
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Write your invariant in words: what is true about lo and hi at the top of every pass through your loop?
8. Trace a list with one element and a list with two elements through your loop. This checks for off-by-one errors, mistakes in which an index ends up one too high or one too low.

# Take-Home 15: Trees and traversal

*For Class 15. I hand this out at the end of Class 14, and it is due on paper at the start of Class 15. Plan on at least two hours.*

## The pattern: depth-first and breadth-first search on a binary tree

A node in a binary tree holds a value and points to at most two children, a left child and a right child. Depth-first search, or DFS, goes as deep as it can before backing up, and you write it as a recursion on the left and right subtrees. It comes in three orders, called preorder, inorder and postorder, which differ in when you visit the node itself. Breadth-first search, or BFS, visits the tree one level at a time and uses a queue. Both searches visit every node once, so both take O(n) time. DFS needs extra space in proportion to the tree's height, and BFS needs extra space in proportion to the tree's widest level.

## How this builds on earlier classes

The recursion of Class 11 matches the shape of a tree, in which every subtree is itself a smaller tree. The queues of Class 8 drive the level-by-level traversal.

## Reading

- [§6.2 Examples of Trees](https://runestone.academy/ns/books/published/pythonds3/Trees/ExamplesofTrees.html)
- [§6.3 Vocabulary and Definitions](https://runestone.academy/ns/books/published/pythonds3/Trees/VocabularyandDefinitions.html)
- [§6.6 Nodes and References](https://runestone.academy/ns/books/published/pythonds3/Trees/NodesandReferences.html)
- [§6.8 Tree Traversals](https://runestone.academy/ns/books/published/pythonds3/Trees/TreeTraversals.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Easy |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What does your function return for an empty tree, and what does it return for a leaf, a node with no children?
8. Is DFS or BFS the better fit for this problem? How much extra space does each one need on a tree that is a single long chain?

# Take-Home 16: Binary search trees

*For Class 16. I hand this out at the end of Class 15, and it is due on paper at the start of Class 16. Plan on at least two hours.*

## The pattern: the binary-search-tree property

In a binary search tree, every value in a node's left subtree is smaller than the node's value, and every value in its right subtree is larger. Search, insert and delete each follow a single path from the root down toward a leaf, so they take O(h) time, where h is the height of the tree. That is O(log n) when the tree is balanced and O(n) when the tree has become a single chain. An inorder traversal of a binary search tree visits the values in sorted order.

## How this builds on earlier classes

The traversals of Class 15 visit every node. The binary search of Class 14 halves a sorted list, and a binary search tree stores the same halving in its pointers.

## Reading

- [§6.12 Binary Search Trees](https://runestone.academy/ns/books/published/pythonds3/Trees/BinarySearchTrees.html)
- [§6.13 Search Tree Operations](https://runestone.academy/ns/books/published/pythonds3/Trees/SearchTreeOperations.html)
- [§6.14 Search Tree Implementation](https://runestone.academy/ns/books/published/pythonds3/Trees/SearchTreeImplementation.html)
- [§6.15 Search Tree Analysis](https://runestone.academy/ns/books/published/pythonds3/Trees/SearchTreeAnalysis.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Use the binary-search-tree property to decide which subtree to visit and which to skip.
8. What does an inorder traversal of a valid binary search tree produce, and how can you use that in your solution?

# Take-Home 17: Heaps and priority queues

*For Class 17. I hand this out at the end of Class 16, and it is due on paper at the start of Class 17. Plan on at least two hours.*

## The pattern: the heap

A binary heap keeps the smallest element at the root of a tree that is filled level by level and stored in a list; a max-heap keeps the largest element there instead. Adding an element and removing the smallest each take O(log n) time, and looking at the smallest takes O(1) time. Use a heap when you repeatedly need the current best item: the top k items, the kth largest item, or the next item from several sorted streams. Python's `heapq` module gives you a min-heap, which keeps the smallest element at the root.

## How this builds on earlier classes

The binary search trees of Class 16 keep every value in order through pointers. A heap keeps only a partial order, and it keeps it in a plain list. Sorting, from Class 13, costs O(n log n) time, while a heap that never holds more than k items lets you find the top k in O(n log k) time.

## Reading

- [§6.9 Priority Queues with Binary Heaps](https://runestone.academy/ns/books/published/pythonds3/Trees/PriorityQueueswithBinaryHeaps.html)
- [§6.10 Binary Heap Operations](https://runestone.academy/ns/books/published/pythonds3/Trees/BinaryHeapOperations.html)
- [§6.11 Binary Heap Implementation](https://runestone.academy/ns/books/published/pythonds3/Trees/BinaryHeapImplementation.html)
- [Python documentation: heapq](https://docs.python.org/3.13/library/heapq.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Do you need a min-heap or a max-heap? Python has only a min-heap, so how will you get the behavior of a max-heap? One way is to store each value with its sign reversed.
8. How many items does your heap hold at most, and why does that size give the running time you claim?

# Take-Home 18: Graphs and depth-first search

*For Class 18. I hand this out at the end of Class 17, and it is due on paper at the start of Class 18. Plan on at least two hours.*

## The pattern: depth-first search on graphs and grids

A graph is a set of vertices, also called nodes, joined by edges. You can store a graph as an adjacency list, which is a dict that maps each vertex to the list of its neighbors. You can also treat a grid as a graph in which each cell is a vertex with up to four neighbors. Depth-first search follows one path as far as it goes before it backs up and tries another, and a visited set keeps it from going around a cycle forever. Depth-first search takes O(V + E) time, where V is the number of vertices and E the number of edges, and it needs O(V) extra space.

## How this builds on earlier classes

Depth-first search on a tree, from Class 15, is the same search on a graph that has no cycles. The visited set uses the hashing of Class 4 to break cycles.

## Reading

- [§7.2 Vocabulary and Definitions](https://runestone.academy/ns/books/published/pythonds3/Graphs/VocabularyandDefinitions.html)
- [§7.5 An Adjacency List](https://runestone.academy/ns/books/published/pythonds3/Graphs/AnAdjacencyList.html)
- [§7.15 General Depth-First Search](https://runestone.academy/ns/books/published/pythonds3/Graphs/GeneralDepthFirstSearch.html)
- [§7.16 Depth-First Search Analysis](https://runestone.academy/ns/books/published/pythonds3/Graphs/DepthFirstSearchAnalysis.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 463 | [Island Perimeter](https://leetcode.com/problems/island-perimeter/) | Easy |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What are the vertices, what are the edges, and how do you list the neighbors of one vertex?
8. At what point do you mark a cell as visited, and what goes wrong if you mark it too late?

# Take-Home 19: Breadth-first search

*For Class 19. I hand this out at the end of Class 18, and it is due on paper at the start of Class 19. Plan on at least two hours.*

## The pattern: breadth-first search and the shortest path in edges

Breadth-first search explores every vertex one edge away from the start, then every vertex two edges away, and so on, using a queue. The first time it reaches a vertex, it has found the shortest path to that vertex, measured in number of edges. A multi-source breadth-first search starts with several vertices in the queue at once and spreads outward from all of them together. Breadth-first search takes O(V + E) time and O(V) space.

## How this builds on earlier classes

The depth-first search of Class 18 used a stack of calls. Breadth-first search replaces that stack with the queue from Class 8, and in exchange it finds shortest paths.

## Reading

- [§7.7 The Word Ladder Problem](https://runestone.academy/ns/books/published/pythonds3/Graphs/TheWordLadderProblem.html)
- [§7.9 Implementing Breadth-First Search](https://runestone.academy/ns/books/published/pythonds3/Graphs/ImplementingBreadthFirstSearch.html)
- [§7.10 Breadth-First Search Analysis](https://runestone.academy/ns/books/published/pythonds3/Graphs/BreadthFirstSearchAnalysis.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 542 | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Medium |
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium |
| 752 | [Open the Lock](https://leetcode.com/problems/open-the-lock/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What counts as one step, and what is the starting state, or what are the starting states?
8. Do you mark a state as visited when you add it to the queue or when you take it out? Why does it matter?

# Take-Home 20: Topological sort

*For Class 20. I hand this out at the end of Class 19, and it is due on paper at the start of Class 20. Plan on at least two hours.*

## The pattern: ordering tasks that depend on each other

A directed graph is a graph whose edges point one way. A topological order lists the vertices of a directed graph so that every edge goes from an earlier vertex to a later one. Getting dressed is an example: socks come before shoes, so any workable order of dressing is a topological order. Such an order exists only when the graph has no cycle. The number of edges that point into a vertex is called its in-degree. Kahn's algorithm builds the order by repeatedly removing a vertex whose in-degree is 0, and it keeps those vertices in a queue. A second method, based on depth-first search, orders the vertices by the time each one finishes. Both methods take O(V + E) time, and both detect a cycle when one exists.

## How this builds on earlier classes

The breadth-first search of Class 19, with its queue, becomes Kahn's algorithm. The graphs of Class 18 now have edges with a direction.

## Reading

- [§7.17 Topological Sorting](https://runestone.academy/ns/books/published/pythonds3/Graphs/TopologicalSorting.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 1557 | [Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) | Medium |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Medium |
| 2115 | [Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Which way does each edge point: from the thing that must come first to the thing that depends on it, or the other way? Write down the rule for computing each vertex's in-degree.
8. How will your algorithm notice that the graph has a cycle?

# Take-Home 21: Shortest paths with Dijkstra's algorithm

*For Class 21. I hand this out at the end of Class 20, and it is due on paper at the start of Class 21. Plan on at least two hours.*

## The pattern: Dijkstra's algorithm with a heap

Dijkstra's algorithm finds the cheapest path from a starting vertex to every other vertex, in a graph whose edges have costs, called weights, that are never negative. It keeps a min-heap of pairs (distance, vertex). At each step it takes out the closest vertex it has not yet finished, and it tries to improve the distance to each of that vertex's neighbors by going through it. With a binary heap this takes O((V + E) log V) time and O(V + E) space. Many problems hide Dijkstra's algorithm by defining the distance of a path as something other than a sum of edge costs, such as the largest single step along the path.

## How this builds on earlier classes

The breadth-first search of Class 19 is Dijkstra's algorithm on a graph in which every edge costs 1. The heap from Class 17 replaces the plain queue of breadth-first search.

## Reading

- [§7.19 Shortest Path Problems](https://runestone.academy/ns/books/published/pythonds3/Graphs/ShortestPathProblems.html)
- [§7.20 Dijkstra's Algorithm](https://runestone.academy/ns/books/published/pythonds3/Graphs/DijkstrasAlgorithm.html)
- [§7.21 Analysis of Dijkstra's Algorithm](https://runestone.academy/ns/books/published/pythonds3/Graphs/AnalysisofDijkstrasAlgorithm.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium |
| 1514 | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium |
| 778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard |

::: plan
:::

## Two more questions about this pattern

7. What is the distance you are minimizing, and how do you combine the distance so far with the cost of the next edge?
8. Why can the same vertex come out of the heap more than once, and how do you skip the outdated entries?

# Take-Home 22: Union-find

*For Class 22. I hand this out at the end of Class 21, and it is due on paper at the start of Class 22. Plan on at least two hours.*

## The pattern: union-find, also called disjoint sets

Union-find keeps track of items that are divided into groups. It supports two operations: find, which tells you which group an item belongs to, and union, which merges two groups into one. Each group is stored as a tree, and the root of the tree serves as the group's label. Two improvements make both operations fast. Path compression points every item on the path of a find straight at the root, and union by size hangs the smaller tree under the larger one. With both improvements, each operation takes very nearly O(1) time on average over a long run of operations; the exact bound uses the inverse Ackermann function, which stays below 5 for any input you could store. Use union-find to count connected groups and to find the edge that closes a cycle.

## How this builds on earlier classes

Class 18 found connected groups with depth-first search. Union-find keeps track of the groups as edges arrive one at a time, and it stores every group's tree in one plain list, in which each item's entry names its parent.

## Reading

- [§7.22 Prim's Spanning Tree Algorithm](https://runestone.academy/ns/books/published/pythonds3/Graphs/PrimsSpanningTreeAlgorithm.html), for background on connecting a graph
- [VisuAlgo: Union-Find Disjoint Sets](https://visualgo.net/en/ufds)

Runestone has no section on union-find. Watch the VisuAlgo animation, and then ask your AI tool to explain path compression and union by size.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 990 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Medium |
| 1319 | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Medium |
| 721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What are the items, and what does it mean in this problem for two items to be in the same group?
8. Write find with path compression in four lines, and say what changes without path compression.

# Take-Home 23: Tries

*For Class 23. I hand this out at the end of Class 22, and it is due on paper at the start of Class 23. Plan on at least two hours.*

## The pattern: the trie, or prefix tree

A trie stores strings one character at a time along the edges of a tree, so all the strings that share a prefix share a path from the root. Inserting a word, searching for a word, and checking whether any stored word starts with a given prefix each take O(L) time for a word of length L, no matter how many words the trie holds. Combined with depth-first search, a trie lets you explore many words at once.

## How this builds on earlier classes

A trie combines three earlier ideas: the trees of Class 15, the dicts of Class 4, which hold each node's children, and the depth-first search of Class 18.

## Reading

- [§6.3 Vocabulary and Definitions](https://runestone.academy/ns/books/published/pythonds3/Trees/VocabularyandDefinitions.html)
- [§6.6 Nodes and References](https://runestone.academy/ns/books/published/pythonds3/Trees/NodesandReferences.html)
- [§2.7 Dictionaries](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/Dictionaries.html)

Runestone has no section on tries. Read the sections above for the vocabulary of trees, then ask your AI tool to explain tries, and trace an insert by hand yourself.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 720 | [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | Medium |
| 648 | [Replace Words](https://leetcode.com/problems/replace-words/) | Medium |
| 1268 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What does each node store, such as its children and a flag that marks the end of a word, and how do you represent the children?
8. In the worst case, how many nodes can a trie hold if it stores m words of at most L letters each?

# Take-Home 24: Backtracking

*For Class 24. I hand this out at the end of Class 23, and it is due on paper at the start of Class 24. Plan on at least two hours.*

## The pattern: choose, explore, undo

Backtracking builds an answer one choice at a time. At each step you make a choice, explore every way to finish the answer from there, and then undo the choice and try the next one. The undoing is the backtrack. You prune a branch, which means you stop exploring it, as soon as you can tell that it cannot lead to a valid answer. The running time is the number of nodes in the tree of choices, which is usually exponential. The space is the depth of the recursion plus the partial answer you are building.

## How this builds on earlier classes

The recursion of Class 11 gives backtracking its shape. The depth-first search of Class 18 marked each cell as visited and left it marked; backtracking adds one step, unmarking a cell when you back out of it, so that a later path can use it again. Class 23 showed how a prefix can cut a search short.

## Reading

- [§4.9 Complex Recursive Problems](https://runestone.academy/ns/books/published/pythonds3/Recursion/ComplexRecursiveProblems.html)
- [§4.11 Exploring a Maze](https://runestone.academy/ns/books/published/pythonds3/Recursion/ExploringaMaze.html)
- [§7.11 The Knight's Tour Problem](https://runestone.academy/ns/books/published/pythonds3/Graphs/TheKnightsTourProblem.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Medium |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What is one choice, what is the partial answer, and when is the answer complete?
8. Which branches can you cut early? State your pruning rule.

# Take-Home 25: Greedy algorithms

*For Class 25. I hand this out at the end of Class 24, and it is due on paper at the start of Class 25. Plan on at least two hours.*

## The pattern: the greedy choice

A greedy algorithm makes the choice that looks best at each step and never goes back on it. A greedy algorithm is correct only when you can argue that the local choice cannot make the final answer worse. The usual argument is an exchange argument: you show that any best answer can be changed, one step at a time, into the greedy answer without getting worse. Greedy algorithms are usually fast, because they need only a sort or a single scan, which means O(n log n) or O(n) time. Always test your rule on a small input that might break it before you trust it.

## How this builds on earlier classes

The sorting of Class 13 often sets up a greedy scan. The backtracking of Class 24 explored every choice, while a greedy algorithm commits to one.

## Reading

- [§7.22 Prim's Spanning Tree Algorithm](https://runestone.academy/ns/books/published/pythonds3/Graphs/PrimsSpanningTreeAlgorithm.html), which is a greedy algorithm
- [§4.12 Dynamic Programming](https://runestone.academy/ns/books/published/pythonds3/Recursion/DynamicProgramming.html), which shows a greedy rule failing on a coin-change example

Runestone has no chapter on greedy algorithms. For exchange arguments, read Chapter 4, "Greedy Algorithms," of Jeff Erickson's free textbook *Algorithms* (<https://jeffe.cs.illinois.edu/teaching/algorithms/book/04-greedy.pdf>), or ask your AI tool for a worked example.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What is your greedy rule, in one sentence?
8. Try to break your rule: write a small input on which a different choice would do better. If you cannot find one, explain why.

# Take-Home 26: Intervals and the sweep line

*For Class 26. I hand this out at the end of Class 25, and it is due on paper at the start of Class 26. Plan on at least two hours.*

## The pattern: sort, then sweep

Most interval problems start by sorting the intervals by their start, or sometimes by their end. A single scan from left to right, called a sweep, then merges intervals that overlap, counts how many intervals are open at the same moment, or finds the fewest intervals to remove so that none overlap. When the sweep needs to know which open interval ends first, or which one is tallest at the moment, a heap keeps track of the open intervals.

## How this builds on earlier classes

This class combines the sorting of Class 13 with the greedy scans of Class 25. The heaps of Class 17 handle the harder sweeps.

## Reading

- [§5.11 The Merge Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheMergeSort.html)
- [§6.9 Priority Queues with Binary Heaps](https://runestone.academy/ns/books/published/pythonds3/Trees/PriorityQueueswithBinaryHeaps.html)

Runestone has no section on intervals. Reread the sorting and heap sections above, and ask your AI tool to explain a sweep line.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | Easy |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. What do you sort by, and what does that order guarantee for your scan?
8. Once the intervals are sorted by their start, write the test for whether two intervals (a, b) and (c, d) overlap.

# Take-Home 27: Dynamic programming in one dimension

*For Class 27. I hand this out at the end of Class 26, and it is due on paper at the start of Class 27. Plan on at least two hours.*

## The pattern: a one-dimensional table

Dynamic programming solves a problem by combining the answers to smaller versions of the same problem, and it stores each answer so that it is computed only once. You write the answer for state i in terms of earlier states, a formula called the recurrence. Then you choose the base cases and fill in the table in order. A one-dimensional table gives O(n) time and O(n) space, and you can often cut the space to O(1) by keeping only the last few values.

## How this builds on earlier classes

The naive recursion of Class 11 repeated the same work many times. Dynamic programming is that recursion with a memory: either a dict, from Class 4, that stores answers as you find them, or a list, from Class 2, that you fill from the bottom up.

## Reading

- [§4.12 Dynamic Programming](https://runestone.academy/ns/books/published/pythonds3/Recursion/DynamicProgramming.html)

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy |
| 746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Define the state in words, in the form "dp[i] means ...". Then write the recurrence and the base cases.
8. Which earlier states does dp[i] need? Can you keep only those?

# Take-Home 28: Dynamic programming on sequences

*For Class 28. I hand this out at the end of Class 27, and it is due on paper at the start of Class 28. Plan on at least two hours.*

## The pattern: states that are positions in a sequence

When the state is a position in a sequence, the recurrence usually asks one of two questions: what is the best answer that ends exactly at position i, or what is the best answer that uses only the first i items? The longest increasing subsequence and the longest common subsequence are the standard examples. The running time is the number of states multiplied by the work for each state: O(n²) for the longest increasing subsequence computed with a simple scan, and O(mn) for the longest common subsequence of two strings of lengths m and n.

## How this builds on earlier classes

Class 27 introduced one-dimensional tables, in which each state depends on a few states just before it. Here a state can depend on every earlier state, and the longest common subsequence brings in a second sequence, which leads to the two-dimensional tables of Class 29.

## Reading

- [§4.12 Dynamic Programming](https://runestone.academy/ns/books/published/pythonds3/Recursion/DynamicProgramming.html), read again

Runestone explains the idea of dynamic programming but does not cover these problems. Use Chapter 3, "Dynamic Programming," of Jeff Erickson's free textbook *Algorithms* (<https://jeffe.cs.illinois.edu/teaching/algorithms/book/03-dynprog.pdf>), together with your AI tool.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | Medium |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Define the state in the form "dp[i] means ...". Does it describe an answer that ends at position i, or one that uses the first i items?
8. How many states are there, and how much work does each one need? Multiply the two to get the running time.

# Take-Home 29: Dynamic programming in two dimensions

*For Class 29. I hand this out at the end of Class 28, and it is due on paper at the start of Class 29. Plan on at least two hours.*

## The pattern: a two-dimensional table

When a problem involves two sequences, or a grid, the state needs two indexes: dp[i][j] is the answer for the first i items of one input and the first j items of the other. Each cell depends on its neighbors above it and to its left. Time and space are both O(mn). A row often needs only the row above it, so you can usually cut the space to the length of one row.

## How this builds on earlier classes

Class 28 met its first two-dimensional table in the longest common subsequence, and this class makes such tables the main subject. The backtracking of Class 24 pruned a search, while dynamic programming removes the repeated work instead.

## Reading

- [§4.12 Dynamic Programming](https://runestone.academy/ns/books/published/pythonds3/Recursion/DynamicProgramming.html), read again

For edit distance, use Chapter 3, "Dynamic Programming," of Jeff Erickson's free textbook *Algorithms* (<https://jeffe.cs.illinois.edu/teaching/algorithms/book/03-dynprog.pdf>). Use your AI tool for traces that show how a table fills in.

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium |
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium |
| 221 | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium |

::: plan
:::

## Two more questions about this pattern

7. Define dp[i][j] in words, and write down the first row and the first column of the table.
8. Draw the table for a tiny input and fill in three cells by hand.

# Take-Home 30: Choosing the pattern

*For Class 30. I hand this out at the end of Class 29, and it is due on paper at the start of Class 30. Plan on at least two hours.*

## The pattern: every pattern, mixed

The final class introduces no new pattern. You will get two Hard problems with no topic label, and you must decide which structure and which algorithm to use, justify your choice, and work out the time, the space and the memory. Review the one-line idea behind every pattern in the course: arrays, hashing, two pointers, sliding windows, stacks, queues, linked lists, recursion, bit manipulation, sorting, binary search, trees, heaps, graphs, union-find, tries, backtracking, greedy algorithms, intervals and dynamic programming.

## How this builds on earlier classes

This class builds on every earlier class. Hard problems usually combine two patterns.

## Reading

- [§2.8 Summary](https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/Summary.html) of the chapter on algorithm analysis
- [§5.13 Summary](https://runestone.academy/ns/books/published/pythonds3/SortSearch/Summary.html) of the chapter on searching and sorting
- [§6.20 Summary](https://runestone.academy/ns/books/published/pythonds3/Trees/Summary.html) of the chapter on trees
- [§7.23 Summary](https://runestone.academy/ns/books/published/pythonds3/Graphs/Summary.html) of the chapter on graphs

## Practice problems on LeetCode

Do all three problems, in the order listed.

| # | Problem | Level |
|----:|---------------------------------------------|--------|
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard |

::: plan
:::

## Two more questions about this pattern

7. For each practice problem, write the name of the pattern and the Big-O of the brute-force approach, without writing any code.
8. Write a one-page summary of the course's patterns. For each pattern, write down the clue in a problem's wording that tells you to use it.
