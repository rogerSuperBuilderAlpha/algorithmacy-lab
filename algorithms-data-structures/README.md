# Algorithms & Data Structures

Professor Roger Hunt wrote this course for Hult International Business School. It runs for 30 classes and uses Python only. In every class, students solve two LeetCode problems by hand at the chalkboard, an easier one and a harder one, and state the running time, the auxiliary space and an estimate of the total memory of each solution in bytes. The problems start at LeetCode's Easy level and end at Hard. Before each class, a take-home names the pattern the class will use, assigns a reading, and lists practice problems.

These documents are draft 3. Claude rewrote all four on 12 November 2026 from draft 2, after a review and seven research runs; the footer of every page says so. [REVIEW.md](REVIEW.md) lists every factual correction draft 3 makes, with its evidence, and every design decision left to the instructor. The term, dates, room, credit hours and several grading values are still blank.

## Documents

- [Syllabus](ADS_Syllabus_Draft.pdf): the course, the 30-class schedule, the table of CPython memory sizes, the grading rule, the AI policy and Hult's policies. Word file: [ADS_Syllabus_Draft.docx](ADS_Syllabus_Draft.docx).
- [Take-homes](ADS_Take_Homes.pdf): one two-sided sheet per class, with the pattern, the reading and the practice problems on the front and the student's plan on the back. Word file: [ADS_Take_Homes.docx](ADS_Take_Homes.docx).
- [In-class board problems](ADS_In_Class_Board_Problems.pdf): the student answer sheet for each of the 60 problems. Word file: [ADS_In_Class_Board_Problems.docx](ADS_In_Class_Board_Problems.docx).
- [In-class solutions](ADS_In_Class_Solutions.pdf): the instructor key, with a tested Python solution, its explanation, its time and space, a memory estimate and other approaches for every problem. Word file: [ADS_In_Class_Solutions.docx](ADS_In_Class_Solutions.docx).

## Editing and rebuilding

Edit the Markdown in `source/`, not the Word files, which the build overwrites. `source/problems.md` holds all 60 problems and produces both the answer sheets and the key.

```sh
sh algorithms-data-structures/build/build.sh       # Word and PDF files; needs pandoc 3, python-docx and LibreOffice
sh algorithms-data-structures/tests/run_tests.sh   # runs every solution in the key; needs Python 3.13
```

The draft label in the footer is set once, at the top of `build/build.sh`.

## Research

`research_notes/ADS course setup review/` holds the notes from the seven research runs, and its `evidence/` folder holds the scripts and their output.
