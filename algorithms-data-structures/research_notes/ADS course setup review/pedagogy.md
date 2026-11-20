# Pedagogy evidence for the draft Algorithms & Data Structures course: design choices (a) to (i)

Scope and method. I read the draft syllabus (`ADS_Syllabus_Draft.md`, cited as "Syl. L#") and Take-Home 1 (`ADS_Take_Homes.md` lines 1-80, cited as "TH L#"). I checked every study's author, year, title and venue this session against a DOI record (OpenAlex, Crossref, Semantic Scholar or ERIC). Every finding below comes from a passage I read: the abstract unless I give a page or section. Where I could read only a secondary source, I say so. I did not use machine-generated summaries (Semantic Scholar "TLDR" lines) as evidence. Text marked **Judgment** is my inference, not a finding. Strength labels: **Strong** = meta-analysis or large randomized trial in a comparable population; **Moderate** = one controlled study, or a meta-analysis of a different population; **Weak** = small, single-site, qualitative, experience report or commentary; **Indirect** = evidence from a different setting that I extrapolate. "Preprint" means the work is not peer reviewed.

## (a) No lecturing; a take-home of at least 2 hours before every class (Syl. L96-97, L99-115, L119; TH L1-76)

### Takeaway
Meta-analyses find that flipped designs beat lecture by a small-to-moderate margin overall (g = 0.36 to 0.50), but by less in IT courses (g = 0.30). The gain grows when class time is not cut and when pre-class work is checked by quizzes, and the most-reported failure is students arriving unprepared. Two hours per class (4 hours a week) meets the US federal credit-hour floor for a 2-credit course and falls below the floor for 3 or more credits. The real workload risk is the open-ended "at least" in the syllabus wording.

### Cited Findings
**Meta-analyses and reviews of flipped classrooms**
- Van Alten, Phielix, Janssen and Kester meta-analysed 114 studies in secondary and postsecondary education: "We found a small positive effect on learning outcomes, but no effect was found on student satisfaction". They also reported "considerable heterogeneity between studies" (abstract). Strength: **Strong**. — [van Alten et al. 2019, Educational Research Review 28, 100281](https://doi.org/10.1016/j.edurev.2019.05.003)
- In the same meta-analysis, two moderators mattered: "students in flipped classrooms achieve higher learning outcomes when the face-to-face class time was not reduced compared to non-flipped classrooms, or when quizzes were added in the flipped classrooms" (abstract). — [van Alten et al. 2019](https://doi.org/10.1016/j.edurev.2019.05.003)
- Strelan, Osborn and Palmer pooled 198 studies with 33,678 students and found "a moderate positive effect (g = .50)". The effect was weakest "for IT, g = 0.30; k = 14". They also concluded that "the primary contributing factor to the flipped classroom effect is the opportunity it provides for structured, active learning and problem-solving" (abstract). Strength: **Strong** overall; the IT subset is small. — [Strelan et al. 2020, Educational Research Review 30, 100314](https://doi.org/10.1016/j.edurev.2020.100314)
- Almassri and colleagues meta-analysed 27 programming-course studies and found "g = 0.56; p < 0.001, 95% confidence interval; 0.33-0.79" in favour of flipped classrooms (abstract). The authors themselves note that "robust experimental studies on the flipped classroom in programming education are limited" (Introduction). Strength: **Moderate to Weak**; the journal sits outside the top tier, and the base studies are thin. — [Almassri et al. 2023, International Journal of Instruction](https://doi.org/10.29333/iji.2023.16216a)
- Akçayır and Akçayır reviewed 71 SSCI-indexed studies. They found that most reported challenges "are related to out-of-class activities, such as much reported inadequate student preparation prior to class" (abstract). Strength: **Moderate** (a review of what studies report). — [Akçayır & Akçayır 2018, Computers & Education](https://doi.org/10.1016/j.compedu.2018.07.021)

**Course studies of what makes pre-class work count**
- In an introductory programming course, Ruiz de Miras, Balsas-Almagro and García combined "out-of-class study and on-line homework questionnaires" with peer instruction. They reported better pass rates (χ2 = 12.94, p < .001) and dropout rates than earlier years, and "significant positive correlations between the work performed at home and the grade obtained in the final exam (ρ = 0.51, p < .001)" (abstract). Strength: **Weak to Moderate** (six offerings compared with earlier years, not randomized). — [Ruiz de Miras et al. 2021, Computer Applications in Engineering Education](https://doi.org/10.1002/cae.22447)
- Yong and colleagues surveyed 204 students in a flipped introductory programming class. They found that "students are not fully ready for a flipped classroom" and that "Pre-class self-study has no impact on students' test performance, except for those without prior programming experience" (abstract). Strength: **Weak** (one course). — [Yong et al. 2020, Int. J. of Virtual and Personal Learning Environments](https://doi.org/10.4018/ijvple.2021010102)
- Zhang and Niu describe a programming-course design in which "2 days before class, Students were required to complete pre-class test", after which a teaching assistant prepared "a pre-class test analysis report" that the lecturer used to plan class (abstract). Strength: **Weak** (single-course design report). — [Zhang & Niu 2022, IEEE FIE](https://doi.org/10.1109/fie56618.2022.9962430)

**Workload standard**
- US federal regulation defines a credit hour as work that "Reasonably approximates not less than— (i) One hour of classroom or direct faculty instruction and a minimum of two hours of out-of-class student work each week for approximately fifteen weeks for one semester or trimester hour of credit". The definition also lets an institution account for "a variety of delivery methods" (34 CFR 600.2, "Credit hour"). — [34 CFR 600.2 (Cornell LII)](https://www.law.cornell.edu/cfr/text/34/600.2)

### Inferences
- **Judgment (workload arithmetic).** The take-home asks for 2 hours × 2 classes = 4 hours a week (Syl. L107). Under 34 CFR 600.2, a 2-credit course implies at least 4 hours a week out of class, and a 3-credit course at least 6. So 4 hours fits a 2-credit course and stays under the floor for 3 or more credits. Credit hours are still TBD (Syl. L15). The syllabus says "at least 2 hours" (Syl. L107), but Take-Home 1 says "About 2 hours" (TH L6). The two documents should agree. Students who are not CS majors may need more than 2 hours for 2-3 LeetCode problems plus the reading and the plan, especially in Medium and Hard weeks.
- **Judgment (risk).** The written plan (TH L53-65) is the course's only pre-class accountability device, and its link to the grade is unclear. The grading rule counts "attendance and effort", and preparation appears only as "Separately, you are expected to arrive prepared" (Syl. L363-365). Van Alten et al.'s quiz moderator and Akçayır and Akçayır's preparation finding both predict that unchecked preparation will be patchy.
- **Judgment (adjustments that keep "no lecturing").** (1) Check the plan at the door as a pass/fail item that counts toward "solid effort", using the six parts already listed in TH L55-65. (2) Optionally open class with a 3-minute written retrieval question on the named pattern. This is a quiz, not a lecture, and it is the moderator van Alten et al. found. (3) Replace "at least 2 hours" with a time box, for example: "Plan on about 2 hours. If one practice problem takes more than 40 minutes, stop, write down where you got stuck, and bring it to class." This caps workload, and the written note doubles as practice for the failed-attempts box in (c). (4) Keep full class time; van Alten et al. found gains when face-to-face time was not reduced.

### Gaps
- I found no study of a flipped course with zero in-class instruction. Most flipped designs keep short clarifications or debriefs.
- I did not check Hult's own credit-hour definition, or UK or ECTS rules for its non-US campuses.
- I found no flipped-classroom study with business-school students who are not CS majors.

## (b) Solve two problems individually by hand: chalk at the board, then copied to paper, with no collaboration (Syl. L39-45, L59-60, L121-126, L135)

### Takeaway
Liljedahl's case for vertical whiteboards comes from high-school mathematics groups of 2-4, with one marker per group and visibly random groups. He measured engagement proxies, not individual learning, so the evidence does not transfer directly to solo board work. Behroozi et al. found that being watched while solving at a whiteboard more than halved performance and raised stress, and the studies of hand-written code are small and mixed. Meta-analyses of pair programming favour pairs on exams and pass rates. That tells the professor what strict individual work costs; it does not mean the rule should go.

### Cited Findings
**Liljedahl, "Building Thinking Classrooms" (what was measured)**
- Method: "Research into each of these was done using design-based methods" (p. 366). Effectiveness was measured with "proxies for engagement—observable and measurable (either qualitatively or quantitatively) student behaviours" (p. 366). Liljedahl calls the board study "the following pseudo-quantitative study" (p. 367). — [Liljedahl 2016, in Felmer et al. (eds), Posing and Solving Mathematical Problems, Springer, pp. 361-386](https://doi.org/10.1007/978-3-319-28023-3_21) (I read the author-uploaded copy of the published chapter)
- Sample and grouping: "five high school classrooms; two grade 12 (n = 31, 30), two grade 11 (n = 32, 31) and one grade 10 (n = 31). In each of these classes, students were put into groups of two to four" (p. 367). "each group was provided with only one felt" pen (p. 368). — [Liljedahl 2016](https://doi.org/10.1007/978-3-319-28023-3_21)
- Results (Table 1, p. 370; 10 groups at vertical whiteboards, 8 at notebooks). Eagerness scored 3.0 vs 0.9, discussion 2.8 vs 0.6, participation 2.8 vs 0.9 and persistence 2.6 vs 1.9 (maximum score 3). Time to first notation was 20.3 s at a vertical whiteboard vs 2.4 min on vertical flipchart paper. Liljedahl's explanation: "With the ease of erasing available to them, students risk more and risk sooner" (p. 370), and "sitting, even while working at a whiteboard, still gives students the opportunity to become anonymous, to hide and to not participate. Standing doesn't afford this." (p. 370). Strength: **Weak to Moderate** for group engagement; the chapter reports no learning outcomes and no individual condition. — [Liljedahl 2016](https://doi.org/10.1007/978-3-319-28023-3_21)
- Random groups are part of the design: "when the randomization was done in full view of the students, changes were immediately noticed" (p. 376), including "Reliance on the teacher for answers decreased" (p. 377). His recommendation reads: "a visibly random method is used to assign students to a group of 2–4 for the duration of that class" and "there should be only one felt pen or piece of chalk per group" (p. 381). — [Liljedahl 2016](https://doi.org/10.1007/978-3-319-28023-3_21)
- Two more elements of his design bear on this course. On consolidation ("levelling"): "When every group has passed a minimum threshold, the teacher needs to engage in discussion about the experience ... This should involve a reification and formalization of the work done by the groups and often constitutes the 'lesson'". On assessment: it "needs to include both group work and individual work" (p. 382). He also notes that "there were not enough whiteboards and blackboards available for all groups" in many rooms (p. 367). — [Liljedahl 2016](https://doi.org/10.1007/978-3-319-28023-3_21)

**Stress at the whiteboard**
- Behroozi, Shirolkar, Barik and Parnin ran "a randomized controlled trial with 48 Computer Science students". They found "that performance is reduced by more than half, by simply being watched by an interviewer" and that "stress and cognitive load were significantly higher in a traditional technical interview" (abstract on the conference program page). Strength: **Moderate** (randomized, but small and in an interview, not a class). — [Behroozi et al. 2020, ESEC/FSE, pp. 481-492](https://doi.org/10.1145/3368089.3409712); abstract read at [FSE 2020 program page](https://2020.esec-fse.org/details/fse-2020-papers/140/Does-Stress-Impact-Technical-Interview-Performance-)
- Both conditions used a whiteboard. The private group was "asked to solve their problem on a whiteboard in a private room", and "all of the women who took the public interview failed, while all of the women who took the private interview passed". Parnin cautioned that a larger sample is needed. **Secondary source:** the university press release; I could not open the full paper (ACM returned 403). — [NC State news release on Behroozi et al. 2020](https://news.ncsu.edu/?p=509799)
- In an earlier qualitative study of Hacker News posts, developers reported that technical interviews "cause unnecessary anxiety and frustration" (abstract). Strength: **Weak** (self-selected posts). — [Behroozi, Parnin & Barik 2019, IEEE VL/HCC](https://doi.org/10.1109/vlhcc.2019.8818836)

**Writing code by hand**
- Grissom, Murphy, McCauley and Fitzgerald compared their computer-based exam with an earlier paper-based study of the same recursive binary-tree problem. "students who took the computer-based exams were more successful than those who took the paper-based exams (58% vs. 17% correct solutions)", yet "42% of students taking the computer-based exam still made errors" (abstract). Strength: **Weak to Moderate** (comparison across two studies, not randomized). — [Grissom et al. 2016, SIGCSE, pp. 6-11](https://doi.org/10.1145/2839509.2844587)
- Öqvist and Nouri split 20 novices into a pen-and-paper group and a computer group and found "no statistical significant difference between the groups in terms of performance" (abstract). Strength: **Weak** (n = 20). — [Öqvist & Nouri 2018, Journal of Computers in Education 5(2), 199-219](https://doi.org/10.1007/s40692-018-0103-3)

**Individual versus paired work**
- Umapathy and Ritzhaupt meta-analysed 18 manuscripts (28 effect sizes, N = 3,308 students) and found "positive results in favor of pair programming in three of four domains with exception to affective measures". The four domains were programming assignments, exams, passing rates and affective measures (abstract). Strength: **Strong** for computing courses. — [Umapathy & Ritzhaupt 2017, ACM TOCE 17(4)](https://doi.org/10.1145/2996201)
- Hannay, Dybå, Arisholm and Sjøberg found "a small significant positive overall effect of pair programming on quality, a medium significant positive overall effect on duration, and a medium significant negative overall effect on effort". They also found "signs of publication bias" (abstract). Strength: **Moderate** (mostly not course settings). — [Hannay et al. 2009, Information and Software Technology 51(7)](https://doi.org/10.1016/j.infsof.2009.02.001)

### Inferences
- **Judgment (mismatch).** The rule "Everyone works on their own" (Syl. L135) removes most of what Liljedahl credits for the benefit: shared talk, one marker per group, and knowledge moving between groups. What survives is standing, visibility and erasability. Visibility is double-edged. The same exposure that stops students from hiding resembles Behroozi et al.'s "being watched" condition, which more than halved performance.
- **Judgment (who carries the risk).** Students most exposed are anxious students, women (per the press-release result, small n) and students working in a second language. Copying from board to paper also doubles writing time without adding feedback. Grissom et al.'s data suggest that hand-written solutions with no tests carry persistent errors. Board space is a practical risk too: individual work needs one board segment per student. Visible boards also make copying from a neighbour easy, which works against "no collaboration".
- **Judgment (adjustments that keep individual work).**
  1. Make the board explicitly ungraded scratch space; grading and any oral check use the paper sheet. The instructor circulates to give hints, not to evaluate at the board, which reduces the "watched" effect while keeping visibility and erasability.
  2. Give one piece of chalk per student, check the room's board length against enrolment, and space students apart.
  3. Allow seated paper work as an accommodation (see (f)).
  4. Add a short end-of-class consolidation, Liljedahl's "levelling" (p. 382), where the instructor compares two or three board solutions. This is not lecturing, but the professor should decide whether it conflicts with "No lecturing" (Syl. L119).
  5. Optional, and it touches the no-collaboration rule: after both sheets are handed in, a 3-minute walk past other boards keeps solving individual while recovering some knowledge mobility.
  6. Print a one-page Python reference on the answer sheet (deque and heapq method names) and grade logic over syntax. This removes recall load that none of Learning Outcomes 1-8 targets.

### Gaps
- I found no study of individual (rather than group) work at vertical surfaces, and none specific to chalk.
- Behroozi et al. studied interviews, not classes; their result about women rests on a press release, because I could not open the full paper.

## (c) Asking for help requires two failed attempts, written in a box (Syl. L137-139, L170-171, L362-363)

### Takeaway
Two bodies of evidence support attempting before receiving help. Problem solving followed by instruction beats the reverse (g = 0.36), and tutor-log data link attempting before asking to better learning on low-prior-knowledge steps. Two problems remain. Productive failure works only when followed by instruction, a phase this syllabus lacks. And help-seeking research identifies the students most likely to skip asking: lower achievers, students worried about how they look, students who would have to ask in public, and non-native speakers. A gate on asking raises the cost for exactly those students.

### Cited Findings
**Productive failure: problem solving followed by instruction**
- Sinha and Kapur meta-analysed 53 studies (166 comparisons) of "problem solving followed by instruction (PS-I)" against "instruction followed by problem solving (I-PS)". They found "a significant, moderate effect in favor of PS-I (Hedge's g 0.36 [95% confidence interval 0.20; 0.51])", "even stronger (Hedge's g ranging between 0.37 and 0.58) when PS-I was implemented with high fidelity to the principles of Productive Failure". They also found "Contrasting trends ... for younger age learners (second to fifth graders) and for the learning of domain-general skills, for which effect sizes favored I-PS" (abstract). Strength: **Strong**. — [Sinha & Kapur 2021, Review of Educational Research 91(5), 761-798](https://doi.org/10.3102/00346543211019105)
- Kapur's original study had eleventh-graders solve ill-structured problems in groups. "despite failing in their collaborative efforts, these students outperformed their counterparts in the well-structured condition on individual near- and far-transfer measures" (abstract). Strength: **Moderate**; the failure phase was collaborative. — [Kapur 2008, Cognition and Instruction 26(3), 379-424](https://doi.org/10.1080/07370000802212669)

**Help-seeking and the assistance dilemma**
- Roll and colleagues analysed two months of Geometry Cognitive Tutor logs from 38 high-school students. They found that "asking for help on challenging steps is associated with productive learning, and overusing help is associated with poorer learning". They also found that "contrary to many help-seeking theories, avoiding help (and failing repeatedly) is associated with better learning than seeking help on steps for which students have low prior knowledge", and concluded that "novice learners may benefit from engaging in solution attempts before they can make sense of given assistance" (abstract). Strength: **Moderate** (correlational, small n, tutor software). — [Roll et al. 2014, Journal of the Learning Sciences](https://doi.org/10.1080/10508406.2014.883977)
- Koedinger and Aleven frame the balance between giving and withholding help as an open problem: "How best to achieve this balance remains a fundamental open problem in instructional science. We call this problem the 'assistance dilemma'" (abstract). — [Koedinger & Aleven 2007, Educational Psychology Review](https://doi.org/10.1007/s10648-007-9049-0)
- Aleven, Stahl, Schworm, Fischer and Wallace reviewed help use in learning software. They found that "learners are not using help facilities effectively" and that "The interaction between metacognitive skills and cognitive factors is important for appropriate help seeking" (abstract). — [Aleven et al. 2003, Review of Educational Research 73(3), 277-320](https://doi.org/10.3102/00346543073003277)

**Who avoids asking for help**
- Ryan, Pintrich and Midgley's review relates help avoidance to "perceived academic and social competence and achievement- and social-goal orientations" and to classroom "rules and norms" and "achievement goal structure" (abstract). — [Ryan, Pintrich & Midgley 2001, Educational Psychology Review 13(2), 93-114](https://doi.org/10.1023/A:1009013420053)
- Ryan, Hicks and Midgley surveyed 443 fifth graders. They found "that lower-achieving students with relative ability goals were more likely to avoid help-seeking than were higher-achieving students", and that "Being oriented to developing ability (task-focused goals) was related negatively to perceiving threat and avoiding help-seeking" (abstract). Strength: **Moderate**; participants were children. — [Ryan, Hicks & Midgley 1997, Journal of Early Adolescence](https://doi.org/10.1177/0272431697017002003)
- Peeters, Robinson and Rubie-Davies observed and interviewed 18 high-school mathematics students. "students were much more likely to seek help privately than publicly, not because the help provided in private situations was more effective but because they anticipated fewer psychological risks" (abstract). Strength: **Weak** (qualitative), but directly on point. — [Peeters et al. 2020, Journal of Educational Psychology](https://doi.org/10.1037/edu0000423)
- Davison, Malmberg and Sylva collected 6,592 task reports from 290 UK pupils aged 8-11. "Pupils for whom English was an additional language were less likely than classmates to seek help when they needed it" (abstract). Strength: **Moderate**, but **Indirect** (children). — [Davison et al. 2022, British Journal of Educational Psychology](https://doi.org/10.1111/bjep.12538)
- Liljedahl sorts student questions into "proximity questions", "stop-thinking questions—most often of the form 'is this right'", and "keep-thinking questions". He argues that "Only the third of these types should be answered" (p. 382). — [Liljedahl 2016](https://doi.org/10.1007/978-3-319-28023-3_21)

### Inferences
- **Judgment (fit).** The rule matches the "attempt first" half of productive failure and Roll et al.'s log data. It does not include the second half. Sinha and Kapur's PS-I always ends with instruction, and the syllabus has no consolidation step (see (b), adjustment 4).
- **Judgment (risks).** (1) The gate raises the cost of asking for students already prone to avoid it, and in this room every request is public. (2) Because "Solid effort means this: if you are stuck, you ask for help, and when you ask for help you show at least 2 failed attempts" (Syl. L362-363), a student who asks without two attempts may appear to fail the effort standard that sets the grade. (3) On Hard problems, two full attempts could use up most of the period.
- **Judgment (wording that keeps the rule and keeps students asking).** Suggested replacement for Syl. L137-139:
  > "Stuck? Asking for help is part of solid effort. Before you ask, write two things you tried in the attempts box. An attempt can be short: a brute-force idea, a hand trace of the example, or a pattern you ruled out and why. Then raise your card and I will come to you, and we start from what you wrote. Questions about what the problem statement means need no attempts."
  
  Four features carry the weight. A minimal definition of "attempt" lowers the cost of asking. The private card responds to Peeters et al. Exempting clarification questions keeps the gate to solution help. Answering with a "keep-thinking" hint follows Liljedahl. Students working in a second language could write attempts as pseudocode or diagrams.

### Gaps
- I found no study that tests a mandatory "N attempts before help" rule in a live classroom. Roll et al.'s evidence is correlational and comes from software logs.
- Price, Liu, Cateté and Barnes (ICER 2017, [doi:10.1145/3105726.3106179](https://doi.org/10.1145/3105726.3106179)) studied programming students' help-seeking. I verified the record, but its abstract states no findings, so I drew nothing from it.

## (d) Every solution states Big-O time, auxiliary space, and total memory in bytes from a CPython size table (Syl. L66-72, L128-130, L151-216; TH L8-13, L63, L72-74)

### Takeaway
Students hold persistent misconceptions about complexity analysis, centred on tracing code and on the mathematics (summations, nested loops). In one controlled study, guided step-by-step practice outperformed unscaffolded by-hand practice (d = 0.84). I found no research on teaching byte-level memory estimation.

### Cited Findings
- Farghally, Koh, Ernst and Shaffer used a Delphi panel of instructors to identify algorithm-analysis topics "considered both important and hard". Piloting with students "revealed that a sufficient number of students held most of the misconceptions identified in the list" (abstract; post-CS2 level). Strength: **Moderate**. — [Farghally et al. 2017, SIGCSE, pp. 207-212](https://doi.org/10.1145/3017680.3017756)
- Al-Bluwi and Zeng compared 5 instructors with 14 students in think-aloud interviews. Experts "clearly differentiate between the task of formulating a summation describing the number of operations performed by the code and the task of solving that summation". Novices erred "because of not explicitly tracing the code and because of not explicitly describing the number of performed operations using a summation", and "Many of the novices also seemed inclined to approach the analysis of nested loops by multiplying two running times, even when that is incorrect" (abstract). Strength: **Weak to Moderate** (qualitative). — [Al-Bluwi & Zeng 2021, Australasian Computing Education Conference](https://doi.org/10.1145/3441636.3441855)
- Parker and Lewis interviewed two students and concluded that difficulties with big-O come from "the mathematical function used in the analysis and/or the techniques they used to solve the problem" (abstract). Strength: **Weak** (n = 2). — [Parker & Lewis 2013, Koli Calling](https://doi.org/10.1145/2526968.2526996)
- Gal-Ezer and Zur report "a study that revealed misconceptions in perceiving the efficiency of algorithms by high school students" (abstract; the abstract names no specific misconceptions). — [Gal-Ezer & Zur 2004, Computers & Education 42(3), 215-226](https://doi.org/10.1016/j.compedu.2003.07.004)
- In a CS1 course at the Open University of Israel, Gal-Ezer, Vilner and Zur used three-part questions. Students identify the problem an algorithm solves, analyse its complexity, and "design a new algorithm that performs the same task, while increasing efficiency by an order of magnitude". "Using the new approach has raised the percentage of students who pass the course" (abstract). Strength: **Weak** (single institution). — [Gal-Ezer, Vilner & Zur 2004, Computer Science Education](https://doi.org/10.1080/0899340042000302736)
- Smith and Rixner's tool, Compigorithm, scaffolds analysis "by breaking down the analysis process into five concrete steps"; "When students make mistakes, they are provided with automated hints and allowed to re-attempt". In a controlled experiment in an introductory algorithms course, the tool group "outperformed the control group by a significant margin (p < 0.00001; Cohen's d = 0.84)". The control group "analyzed the same algorithms by hand" (abstract). Strength: **Moderate** (one controlled experiment). — [Smith & Rixner 2020, ITiCSE](https://doi.org/10.1145/3341525.3387390)

### Inferences
- **Judgment (fit).** Stating time, space and memory, together with the plan's "brute force, then pattern" step (TH L57-59), matches Gal-Ezer et al.'s analyse-then-improve approach. The evidence locates the difficulty in tracing and in summation mathematics. That is the layer where business-school students without a mathematics background are most likely to struggle. Adding byte arithmetic in the same timed sitting adds load.
- **Judgment (grading risk).** The syllabus states that its own estimates can be off by "about 25% to a factor of 2" (Syl. L177-179). Yet extra credit requires "the right time, space and memory analysis" (Syl. L370). Without a stated tolerance, "right" is undefined for the memory estimate.
- **Judgment (adjustments).**
  1. Print a fixed analysis scaffold on the answer sheet, modelled on the step structure Smith and Rixner found effective and on Al-Bluwi and Zeng's tracing finding. For example: (i) name n; (ii) count loop iterations or calls as a sum; (iii) simplify; (iv) list each structure built and its maximum size; (v) multiply by the table sizes.
  2. Grade the memory estimate on method and stated assumptions, accepting answers within a factor of 2, which is the syllabus's own error band.
  3. Print the size table (Syl. L181-216) on the answer sheet, since devices are locked away. The syllabus says "Use these sizes" but does not say students will have the table in class.
  4. Early in the term, ask only for the memory of the dominant structure; phase in "input + auxiliary + total" later.

### Gaps
- I found no peer-reviewed study on teaching or learning byte-level memory estimation, or on students' use of CPython object sizes.
- Danielsiek, Paul and Vahrenhold (SIGCSE 2012, [doi:10.1145/2157136.2157148](https://doi.org/10.1145/2157136.2157148)) worked toward a concept inventory for algorithms and data structures. I verified the record but read no abstract, so I drew nothing from it. (A DOI I first tried for this paper resolved to an unrelated paper; the one given here is from Crossref.)

## (e) Real LeetCode problems ramping Easy, Medium, Hard, ending with Hard problems (Syl. L218-242, L250-350)

The Hard problems in the draft are #212 Word Search II (class 23), #51 N-Queens (24), #135 Candy (25), #218 The Skyline Problem (26), #10 Regular Expression Matching (29), and #127 and #295 in the capstone (Syl. L324-348).

### Takeaway
The evidence for contest-style or online-judge problems as a curriculum is mostly experience reports. I found no study of solving LeetCode Hard problems by hand in one session. Cognitive-load research supports the direction of the ramp: novices learn more with high assistance, and assistance should fade as knowledge grows. It does not support handing novices unscaffolded Hard problems.

### Cited Findings
- Tetzlaff and colleagues meta-analysed 60 experiments (5,924 participants) on the expertise reversal effect. "Low prior knowledge learners learn better from high-assistance instruction (d = 0.505). High prior knowledge learners learn better from low-assistance instruction (d = −0.428)." They add: "providing novices with assistance has a stronger effect than withholding assistance from experts" (abstract). Strength: **Strong**. — [Tetzlaff et al. 2025, Learning and Instruction](https://doi.org/10.1016/j.learninstruc.2025.102142)
- Morrison, Margulieux and Guzdial found that subgoal-label gains established in mathematics and science "did not replicate as expected in the introductory CS task". They suggest that "Computer science may require different kinds of problem-solving or may generate different cognitive demands" (abstract). Strength: **Moderate**; it cautions that scaffolds do not transfer automatically. — [Morrison et al. 2015, ICER, pp. 21-29](https://doi.org/10.1145/2787622.2787733)
- Wang and colleagues analysed online-judge submission data from Project CodeNet. They recommend that "problem difficulty and order should be considered and adjusted according to the users' abilities and progress, to provide appropriate challenges and support, balance the cognitive load" (abstract). Strength: **Weak** (observational data from a platform). — [Wang et al. 2023, Heliyon](https://doi.org/10.1016/j.heliyon.2023.e20947)
- Yuen, Liu and Leong ran a Python contest with an automatic judge alongside an introductory course. They found that "Not many junior contestants could solve at least one problem(s)" (abstract). Strength: **Weak** (case study). — [Yuen et al. 2023, Computer Applications in Engineering Education](https://doi.org/10.1002/cae.22610)
- Verdú and colleagues tested an online-judge system in "three algorithms and programming courses" and report that "the experiment also showed an improvement in students' academic outcomes" (abstract). Strength: **Weak**. — [Verdú et al., Computers & Education (online 2011)](https://doi.org/10.1016/j.compedu.2011.08.015)
- **Preprint.** Dickey describes a competitive-programming course sequence built on "mastery-oriented online-judge problem sets", "sampled oral code interviews" and "fading scaffolds", with timed competition deferred. He states that the work is "a transparent design case rather than an efficacy trial" (abstract). Strength: **Weak**. — [Dickey 2026, arXiv](https://doi.org/10.48550/arxiv.2609.26139)
- Cui and colleagues analysed "over 300,000 user profiles from LeetCode" to estimate interview-preparation effort. The abstract I read reports no numbers, so I draw nothing further from it. — [Cui et al. 2024, CSEE&T research track](https://conf.researchr.org/details/cseet-2024/cseet-2024-research-track/33/How-Much-Effort-Do-You-Need-to-Expend-on-a-Technical-Interview-A-Study-of-LeetCode-P)

### Inferences
- **Judgment (feasibility).** Most of the listed Hard problems combine two or more patterns. Word Search II needs a trie plus grid backtracking; The Skyline Problem needs a sweep line plus a heap; Regular Expression Matching needs 2D DP with a "*" case. A correct hand-written solution, plus three analyses, plus a paper copy, in one session (length TBD), about 12 weeks after starting at Easy, is plausible for a minority. Yuen et al.'s result points the same way.
- **Judgment (where the risk falls).** The grade rests on effort (Syl. L359-360), so failing a Hard problem does not lower the grade directly. The risks are motivation and class time spent stuck. Learning Outcome 4 also promises students will "Write correct Python solutions by hand to Easy, Medium and Hard problems" (Syl. L77-78), and many may not reach it. The draft already drops back to Medium when dynamic programming begins (Syl. L237-238), which fits the expertise-reversal logic.
- **Judgment (adjustments that keep real Hard problems).**
  1. Put milestones on the sheet and count each as progress: (M1) brute force plus its Big-O; (M2) the key data structure or recurrence; (M3) a full solution.
  2. Offer a partially worked version, a faded worked example, to students who reach no milestone by mid-session. Tetzlaff et al. found that assistance helps novices more than withholding it helps experts.
  3. Keep stretch for strong students in the extension problems (Syl. L141-143) rather than raising the floor.
  4. Once class length is set, check it against a realistic time to write a Hard solution by hand.

### Gaps
- I found no study of LeetCode, or of contest problems generally, as the core problem set of a credit course, with learning outcomes measured.
- I found no data on how long it takes to solve LeetCode Hard problems by hand.
- **Judgment:** LeetCode's Easy/Medium/Hard labels are platform labels, not validated difficulty measures.

## (f) Phones and computers locked away for the whole session (Syl. L132-133, L450-451; accommodations L503-507)

### Takeaway
Two experiments found that permitting devices in lectures lowered exam scores, including for students who did not use them: a West Point randomized trial (0.18 SD) and a within-student experiment. The longhand note-taking advantage did not replicate. This course has no lecture and no note-taking, so the distraction mechanism applies and the note-taking one does not. A blanket ban needs an explicit exception for disability accommodations.

### Cited Findings
**Device studies**
- Carter, Greenberg and Walker "prohibited computer devices in randomly selected classrooms of an introductory economics course at the United States Military Academy". Exam scores "among students assigned to classrooms that allowed computers were 0.18 standard deviations lower" (abstract, p. 118). The effect "is as large as the average difference in exam scores for two students whose cumulative GPAs at the start of the semester differ by one-third of a standard deviation" (p. 119). The negative effect appeared both with unrestricted laptops and tablets and with tablets that "must remain flat on the desk" (abstract). Strength: **Strong** (randomized trial), but specific to one setting. — [Carter, Greenberg & Walker 2017, Economics of Education Review 56, 118-132](https://doi.org/10.1016/j.econedurev.2016.12.005)
- Glass and Kang permitted devices in half the lectures of a two-section course, "in a within-student, within-item counterbalanced experimental design". Devices "did not reduce comprehension of the lecture, as measured by within-class quiz questions. Instead, divided attention reduced long-term retention". "Exam performance was significantly worse than the no-device control condition both for students who did and did not use electronic devices during that class" (abstract). Strength: **Moderate to Strong**. — [Glass & Kang 2019, Educational Psychology 39(3), 395-408](https://doi.org/10.1080/01443410.2018.1489046)

**Longhand vs laptop note-taking**
- Mueller and Oppenheimer found in three studies "that students who took notes on laptops performed worse on conceptual questions than students who took notes longhand", which they attributed to laptop note-takers' "tendency to transcribe lectures verbatim" (abstract). — [Mueller & Oppenheimer 2014, Psychological Science 25(6), 1159-1168](https://doi.org/10.1177/0956797614524581)
- Morehead, Dunlosky and Rawson ran a direct replication. "performance did not consistently differ between any groups". A meta-analysis of the direct replications "revealed small (nonsignificant) effects favoring longhand", and "concluding which method is superior for improving the functions of note-taking seems premature" (abstract). — [Morehead, Dunlosky & Rawson 2019, Educational Psychology Review 31(3), 753-780](https://doi.org/10.1007/s10648-019-09468-2)
- Urry and colleagues directly replicated Study 1 (laptop n = 74, longhand n = 68). They report that "laptop participants did not perform better than longhand participants on the quiz" and that, in mini meta-analyses of eight similar studies, "results do not support the idea that longhand note taking improves immediate learning via better encoding of information" (abstract). — [Urry et al. 2021, Psychological Science 32(3), 326-339](https://doi.org/10.1177/0956797620965541)

**Accommodations law (US)**
- The Section 504 regulations require institutions to "make such modifications to its academic requirements as are necessary to ensure that such requirements do not discriminate", including "adaptation of the manner in which specific courses are conducted". Auxiliary aids "may include ... classroom equipment adapted for use by students with manual impairments". However, "Academic requirements that the recipient can demonstrate are essential to the instruction being pursued ... will not be regarded as discriminatory" (34 CFR 104.44(a), (d)). — [34 CFR 104.44 (Cornell LII)](https://www.law.cornell.edu/cfr/text/34/104.44)

### Inferences
- **Judgment (fit).** The ban fits the distraction evidence. Glass and Kang's spillover result, that non-users were also harmed, supports a room-wide rule over individual choice. The note-taking studies do not apply to a course with no lecture, and their main result is contested anyway.
- **Judgment (risks).** The draft has no stated exception for:
  - screen readers or magnification;
  - motor impairments that make chalk writing hard;
  - medical devices that run on phones, such as glucose monitors;
  - emergency contact.
  
  The accommodations paragraph (Syl. L503-507) is generic. A student whose device is approved must also use it in a room where nobody else has one, which makes the accommodation visible. Hult has non-US campuses whose laws I did not check.
- **Judgment (adjustments).** Next to Syl. L132-133 and L450-451, add: "except devices approved through Hult's accessibility office, and medical devices". Add an emergency-contact procedure. Offer seated paper work and large-print answer sheets as standard alternatives to board work, so that using them does not single anyone out.

### Gaps
- I found no device-ban study in a no-lecture, problem-solving classroom.
- For Carter et al. I read the abstract and pp. 118-119 only, not the sample tables.
- I did not check UK, UAE or other non-US accommodation law.

## (g) AI allowed and expected outside class; in class, explain and defend any answer on the spot (Syl. L390-417; L91-92; L498-500)

### Takeaway
In a randomized trial with about 1,000 students, unrestricted AI during practice raised practice grades but cut later unassisted exam grades by 17%. A tutor-style AI with guardrails largely removed that harm. Struggling novices who use AI show compounded metacognitive problems and an "illusion of competence", and a third of students cannot explain their own correct code. That last finding supports the "explain and defend" rule.

### Cited Findings
- Bastani and colleagues gave nearly 1,000 high-school mathematics students either "GPT Base" or "GPT Tutor" (prompts "designed to safeguard learning"). During practice, AI access raised grades by "48% improvement in grades for GPT Base and 127% for GPT Tutor". When access was removed, GPT Base students "perform worse than those who never had access (17% reduction in grades for GPT Base)", and "These negative learning effects are largely mitigated by the safeguards in GPT Tutor" (abstract). The authors "preregistered this RCT with a designated primary analysis of comparing students' unassisted exam outcomes across arms" (main text, as excerpted in Consensus). Strength: **Strong** (large preregistered RCT), but **Indirect** (high-school mathematics). — [Bastani et al. 2025, PNAS 122(26), e2422633122](https://doi.org/10.1073/pnas.2422633122)
- Kazemitabaar and colleagues ran a controlled experiment with 69 novices aged 10-17. Codex access "significantly increased code-authoring performance (1.15x increased completion rate and 1.8x higher scores) while not decreasing performance on manual code-modification tasks". Codex users did "slightly better" on one-week post-tests, a difference that "did not reach statistical significance", and "learners with higher Scratch pre-test scores performed significantly better on retention post-tests, if they had prior access to Codex" (abstract). Strength: **Moderate**, **Indirect** (young novices). — [Kazemitabaar et al. 2023, CHI](https://doi.org/10.1145/3544548.3580919)
- Prather and colleagues observed 21 lab sessions. "for students who struggled, our findings indicate that previously known metacognitive difficulties persist, and that GenAI unfortunately can compound them and even introduce new metacognitive difficulties". These students "thought they performed better than they did, and finished with an illusion of competence" (abstract). Strength: **Weak to Moderate** (qualitative, n = 21). — [Prather et al. 2024, ICER, pp. 469-486](https://doi.org/10.1145/3632620.3671116)
- Lehtinen, Lukkarinen and Haaranen asked students questions about their own submitted programs. "One third of the students struggled to explain their own program code", and "answering properly aligned QLCs correctly has stronger correlation with student success and retention than merely submitting a correct program" (abstract). Strength: **Moderate**. — [Lehtinen et al. 2021, ITiCSE, pp. 206-212](https://doi.org/10.1145/3430665.3456322)
- Li, Liu and Dong's quasi-experiment found that GenAI "demonstrates strong potential to enhance learning outcomes and self-efficacy but negatively affects long-term knowledge transfer". They found that "excessive reliance on GenAI and cognitive outsourcing impede effective knowledge acquisition", and that high performers showed "greater epistemic agency" (abstract). Strength: **Moderate to Weak**. — [Li, Liu & Dong 2025, Australasian Journal of Educational Technology](https://doi.org/10.14742/ajet.9932)
- **Preprint.** Azimi randomly assigned 33 master's students to a scaffolded AI coach or unrestricted AI. "Assignment performance did not differ between the conditions", and "Students who had formulated their own rules for when to use AI performed better in both conditions" (abstract). — [Azimi 2026, arXiv](https://doi.org/10.48550/arxiv.2609.16784)
- **Preprint.** Sankaranarayanan (N = 78) found that unrestricted AI users "suffered a 77% failure rate on a subsequent 30-minute AI-blackout maintenance task, vs. only 39% in the scaffolded group". The scaffold was an "Explanation Gate ... enforcing a teach-back protocol" (abstract). — [Sankaranarayanan 2026, arXiv](https://doi.org/10.48550/arxiv.2602.20206)

### Inferences
- **Judgment (fit).** The policy already contains Bastani et al.'s key guardrail in student-facing form: "Write your plan and your attempt first. Then use AI to check" (Syl. L401-403). The device-free class plays the role of their unassisted exam. Lehtinen et al.'s finding directly supports the explain-and-defend rule (Syl. L414-417), and both preprints point the same way (teach-back, self-set rules).
- **Judgment (risks).** (1) Nothing enforces "attempt first" at home. Prather et al.'s struggling students are the ones likely to use AI as a crutch while feeling competent, so the first unassisted test of their skill is the board in class. That is Bastani et al.'s "access taken away" condition. (2) Questioning on the spot in front of others adds the "watched" stress from (b) to an explanation check.
- **Judgment (adjustments).**
  1. Give students a short tutor-mode prompt to paste into any AI: ask for hints rather than code, quiz me, and do not show a full solution until I have shown my attempt. This mirrors GPT Tutor.
  2. Extend the Transparency bullet (Syl. L409-410) with one line per AI use in the take-home: what I asked, and what I changed.
  3. Run the explain-and-defend check privately at the student's sheet, using a fixed three-question set: why it is correct; a trace on a small input; what changes under a different constraint. Let students first write a two-line explanation on the sheet, which follows the "retrospective think-aloud" idea in Behroozi et al.'s summary (paraphrase, not a quote).

### Gaps
- I found no randomized study of AI policy in a university algorithms course.
- The strongest trial (Bastani et al.) is in high-school mathematics, and Kazemitabaar et al. studied ages 10-17.
- Several recent studies are preprints.

## (h) Grading: attend every class with solid effort "as judged by me" for an A; correct answers earn extra credit that can cover absences (Syl. L355-388)

### Takeaway
Attendance predicts grades strongly (ρ = .44), but the effect of mandatory attendance policies rests on only three studies (d = .21). Alternative grading in computing (specifications, contracts) shows promise, but outcome evidence is thin, and one report found engagement fell once a passing grade was secure. Two risks are specific to this draft. Grading by judgment admits measurable grader bias (g = 0.36). And extra credit is mostly earned by students already doing well, so tying absence coverage to correct answers helps strong students and not those most likely to miss class.

### Cited Findings
**Attendance**
- Credé, Roch and Kieszczynka found that attendance "has strong relationships with both class grades (k = 69, N = 21,195, ρ = .44) and GPA (k = 33, N = 9,243, ρ = .41)", and that "Mandatory attendance policies appear to have a small positive impact on average grades (k = 3, N = 1,421, d = .21)" (abstract). Strength: **Strong** for the correlation, **Weak** for the policy effect (k = 3). — [Credé et al. 2010, Review of Educational Research 80(2), 272-295](https://doi.org/10.3102/0034654310362998)

**Bias in judgment-based grading**
- Malouff and Thorsteinsson meta-analysed 20 experimental studies with 1,935 graders exposed to irrelevant information about students. "The statistically significant overall between-groups effect size was g = 0.36"; "bias can occur in subjective grading when graders are aware of irrelevant information about the students" (abstract). Strength: **Strong to Moderate** (experiments, mostly on essay grading). — [Malouff & Thorsteinsson 2016, Australian Journal of Education 60(3), 245-256](https://doi.org/10.1177/0004944116664618)

**Extra credit**
- Moore found that 81% of introductory biology students said they would submit extra credit. "When given two chances for extra-credit work, fewer than one-fourth of students submitted one or both assignments". Those who did "were more likely to attend class, attend optional help sessions, and earn higher grades than other students, even when the points earned from the extra-credit work were excluded" (ERIC abstract). Strength: **Weak** (one course). — [Moore 2005, Journal of College Science Teaching (ERIC EJ714406)](https://eric.ed.gov/?id=EJ714406)

**Alternative grading in computing**
- Harrington and colleagues reviewed specifications and contract grading in CS education. They found "a good deal of promising research" but "a great deal of variation in methodologies and a sparsity of evaluation of the efficacy of learning outcomes" (abstract). Strength: **Moderate** (literature review). — [Harrington et al. 2024, SIGCSE](https://doi.org/10.1145/3626252.3630929)
- Largent, Roberson and Pérez-Quiñones summarise Nilson's specifications grading as relying "on pass/fail grading of assignments and assessments, the structuring of course content into modules linked to learning outcomes, and the bundling of assignments and assessments". In their words, "One intention ... is to align assessment more closely with student attainment of intended learning outcomes" (abstract of a tutorial; a description, not evidence). — [Largent et al. 2025, SIGCSE tutorial](https://doi.org/10.1145/3641555.3704758)
- Tuson and Hickey combined mastery learning with specifications grading in a 128-student discrete mathematics course: "By the end of the semester, 75% of the students had mastered at least nine of the ten skill areas" (abstract). Strength: **Weak** (case study). — [Tuson & Hickey 2022, ITiCSE](https://doi.org/10.1145/3502718.3524766)
- Montagner and colleagues compared three specifications-grading policies. Pass rates rose under pass/fail, but "lab and project grades decrease after students receive a passing grade in the first exam, indicating a possible decrease in engagement" (abstract). Strength: **Weak** (experience report), but on point for a guaranteed-A design. — [Montagner et al. 2025, SIGCSE](https://doi.org/10.1145/3641554.3701925)
- Butler compared alternative grading systems in mathematics, computer science and statistics courses. Specifications grading and standards-based grading were reported as less stressful by "79% and 83% of students, respectively", with the caveat that "the study's sample size limits the generalizability" (abstract). Strength: **Weak**. — [Butler 2025, Assessment & Evaluation in Higher Education](https://doi.org/10.1080/02602938.2025.2475068)

**Records verified, texts not read (no claims drawn)**
- Nilson and Stanny, *Specifications Grading*, 2nd edition, Routledge 2023 ([doi:10.4324/9781003447061](https://doi.org/10.4324/9781003447061)). I did not verify the 2015 first edition.
- Inoue, *Labor-Based Grading Contracts*, WAC Clearinghouse 2019 ([doi:10.37514/PER-B.2019.0216.0](https://doi.org/10.37514/PER-B.2019.0216.0)).
- Carillo, *Hidden Inequities in Labor-Based Contract Grading*, 2021 ([doi:10.7330/9781646422678](https://doi.org/10.7330/9781646422678)).
- Blum (ed.), *Ungrading*: I verified this only through published reviews, for example [Teaching Philosophy 44(4)](https://doi.org/10.5840/teachphil2021444159).

### Inferences
- **Judgment (risks).**
  1. "as judged by me" (Syl. L359-360) cannot be checked by students and exposes the grade to the bias Malouff and Thorsteinsson measured. It is also hard to defend in an appeal. The syllabus defines effort only by help-seeking (Syl. L362-363), so a student who never gets stuck, or never asks, meets no defined criterion.
  2. The A certifies attendance and effort, not Learning Outcomes 1-8 (Syl. L64-92). Hult's assurance-of-learning rules may matter here; I did not research them.
  3. Montagner et al.'s engagement drop suggests a guaranteed-A design needs effort criteria that apply every class.
  4. Covering absences with correct-answer points runs against the intent. Moore's data imply those points go mostly to students who need them least, while students absent through illness or work, who are often weaker, cannot earn cover.
- **Judgment (adjustments that keep "attend + effort = A").**
  1. Publish "solid effort" as a short binary checklist recorded each class, specifications-style: (i) take-home plan with all six parts; (ii) both problems attempted on the sheet with the time, space and memory lines filled, even if wrong; (iii) attempts box filled when help was requested; (iv) worked until the end of the session.
  2. Replace "as judged by me" with "as recorded on the checklist", reserving the instructor's judgment for documented exceptions.
  3. Offer two routes to cover an absence: correct-answer points, as now, or an effort-based make-up (the missed class's two problems on paper with a plan, one explained in office hours).
  4. Fill the TBD table (Syl. L375-388) before term.

### Gaps
- I found no study of grading on attendance plus effort, nor of extra credit used to cover absences.
- I did not read the books by Nilson, Inoue, Carillo or Blum.
- I did not read Hult's grading and attendance policies.

## (i) Students who excel are "expected to contribute to, and receive coauthor credit on" a journal paper (Syl. L145-147, L419-440)

### Takeaway
Undergraduate research is a recognized high-impact practice with self-reported gains. The students who benefit most from such practices reach them least often. Embedding it in a course where the same instructor grades students with discretion creates power and coercion risks. Authorship standards (ACM) tie credit to contribution, drafting and accountability, so authorship cannot be promised in advance.

### Cited Findings
**Benefits and access**
- **Secondary source.** Sullivan and McConnell, citing Kuh's 2008 AAC&U report, write that "disadvantaged students who stand to benefit the most from HIPs gain access to them least often (Kuh, 2008, p. 17; Finley & McNair, 2013)" (ERIC abstract). The AAC&U page for Kuh's report returned 404, so I did not read the primary. — [Sullivan & McConnell (ERIC EJ1195817)](https://eric.ed.gov/?id=EJ1195817)
- Greenman, Chepp and Burton write that the benefits of high-impact practices are "well-documented, especially for students from groups that have been historically underserved by higher education". However, "relative to their more traditionally advantaged counterparts, these populations face greater barriers in accessing these beneficial learning experiences" (ERIC abstract). — [Greenman, Chepp & Burton 2022, Teaching in Higher Education (ERIC EJ1337599)](https://eric.ed.gov/?id=EJ1337599)
- Lopatto surveyed 1,135 undergraduate researchers from 41 institutions. "Over 83% ... began or continued to plan for postgraduate education in the sciences", and "Women and men reported similar levels of benefits" (abstract). Strength: **Moderate** (self-report). — [Lopatto 2004, Cell Biology Education 3(4), 270-277](https://doi.org/10.1187/cbe.04-07-0045)
- Auchincloss and colleagues drafted "an operational definition of a CURE", a course-based undergraduate research experience, and summarised assessment needs (abstract). This is the model for research built into a course. — [Auchincloss et al. 2014, CBE-Life Sciences Education 13(1), 29-40](https://doi.org/10.1187/cbe.14-01-0004)

**Authorship standards and power**
- Fine and Kurdek propose "that authorship credit and order decisions should be based on the relative scholarly abilities and professional contributions of the collaborators". They recommend "that both faculty and students participate in the authorship decision-making process early in the collaborative endeavor" (abstract). — [Fine & Kurdek 1993, American Psychologist 48(11), 1141-1147](https://doi.org/10.1037/0003-066X.48.11.1141)
- ACM's authorship policy, as reproduced by SIGCSE, requires every author to meet four criteria:
  1. "They have made substantial intellectual contributions to some components of the original work described in the manuscript;"
  2. "They have participated in drafting and/or revision of the manuscript"
  3. "They are aware the manuscript has been submitted for publication;"
  4. "They agree to be held accountable for any issues relating to the correctness or integrity of the work"
  
  The ACM page itself returned 403 to my fetch. — [SIGCSE 2025 authorship policies page](https://sigcse2025.sigcse.org/info/authorship-policies)
- Goddiksen and colleagues surveyed 1,336 European PhD students. "Approximately three in ten reported that they had granted at least one guest authorship to 'a person in power'. Half of these indicated that they had done so because they had been told to do so" (abstract). Strength: **Moderate** (survey), **Indirect** (PhD students). — [Goddiksen et al. 2023, PLoS ONE](https://doi.org/10.1371/journal.pone.0280018)
- Nishikawa and colleagues describe one nursing school's policy: "co-authorship with faculty could not be included as part of the required activities of any course", and "co-authorship agreements must be finalized outside the context of a student's coursework in which the coauthor is the instructor, and only after course grades from a co-authoring instructor have been finalized" (article text). Strength: **Weak** (a policy description). — [Nishikawa et al. 2014, Nurse Author & Editor](https://doi.org/10.1111/j.1750-4910.2014.tb00190.x)
- Rendos and Wilburn recommend "that faculty avoid recruiting students they directly evaluate". They cite a focus-group finding that coercion was minimized "when the faculty member conducting the research was not in an evaluative role over the students" (Sarpel et al. 2013; I did not read Sarpel directly). Strength: **Weak** (commentary). — [Rendos & Wilburn 2025, Journal of Academic Ethics](https://doi.org/10.1007/s10805-025-09629-9)

### Inferences
- **Judgment (risks).**
  1. "expected to contribute to, and receive coauthor credit" (Syl. L145-147, L421-423) promises authorship before anyone has contributed. ACM's criteria require drafting or revision and accountability, so the promise invites guest authorship.
  2. "Expected", combined with an instructor who also grades by discretion ("as judged by me"), makes declining feel risky. Goddiksen et al. show how often power shapes authorship.
  3. Selection by direct invitation (Syl. L427), based on in-class performance, may under-select the students Kuh and Greenman et al. flag. It may also under-select students hurt by public board work in (b).
  4. If the paper uses course data (student work or performance), students become research subjects, which requires ethics review and consent. A paper on algorithm benchmarks would not.
- **Judgment (adjustments that keep the track).**
  1. Change "expected to" to "invited to apply", and state that taking part, or declining, has no effect on the course grade.
  2. Sign authorship agreements only after grades are posted (Nishikawa et al.).
  3. Keep the written agreement already planned (Syl. L435-437), base it on the ACM criteria, and acknowledge contributors who do not meet them.
  4. Publish the selection criteria and open the call to every student who meets a threshold, rather than inviting individuals only.
  5. If student data is used, obtain ethics approval and have consent collected by someone other than the instructor.

### Gaps
- I found no study of coauthorship offered within a taught undergraduate course in business or computing.
- I did not read Kuh's 2008 report itself.
- I did not check Hult's research-ethics policy.
