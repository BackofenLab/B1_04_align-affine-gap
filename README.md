Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

Course ILIAS: [web page link](https://ilias.uni-freiburg.de/ilias.php?ref_id=2339316&cmdClass=ilobjcoursegui&cmd=view&cmdNode=zf:ns&baseClass=ilRepositoryGUI)

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 4: Sequence Alignment - affine gap costs
---

### _Exercise 1 -  Waterman-Smith-Beyer traceback_

Within the algorithm of Waterman, Smith and Beyer arbitrarily large gaps are considered. Thus,
also the traceback has to investigate all gap sizes. This can be done following two strategies:

 - check in increasing gap length (start with smallest gap)
 - check in decreasing gap length (start with largest gap)

**a)** Given a gap function, are the strategies (measured in absolute runtime or number operations)
expected to be equally performant or is one of them better than the other?

 - [ ] both are equally performant.
 - [ ] checking in increasing direction performs better
 - [ ] checking in decreasing direction performs better

**b)** Does the order of checking insertion and deletions change the runtime?

 - [ ] yes, checking insertions first will perform better
 - [ ] yes, checking deletions first will perform better
 - [ ] no, the order doesn't affect performance
 - [ ] checking in an alternating way might improve performance


### _Exercise 2 -  Waterman-Smith-Beyer with free end gaps_

Given the Waterman-Smith-Beyer algorithm with the following scoring function:

<p align="center">
<img src="./figures/exercise2_substitution.svg" alt="scoring" width=30%/>
 </p>

When aligning sequences of very different lengths the penalizing of *leading and trailing gaps*, i.e unaligned sequence ends, dominates the alignment score.

We distinguish between leading and trailing gaps (example):

    A-CC-CC-G
    -TCCGCCT-

In this case the leading gaps are:

    A-
    -T

The trailing gaps are:

    -G
    T-

The algorithm by Waterman, Smith and Beyer can be adapted to treat end gaps with a score of 0.
The adapted recursion formula is defined here, where n and m are the lengths of the respective sequences:

<p align="center">
<img src="./figures/exercise2_recursion.svg" alt="recursion" width=50%/>
 </p>

**a)** Match the following descriptions with the correct recursion parts (see recursion figure, labels (a)-(h)):

1. if (i = n), k trailing end gaps in B
2. k normal gaps in A
3. j leading gaps in B (inner block of gaps)
4. match/missmatch case
5. i leading gaps in A (inner block of gaps)
6. outer block of gaps in one sequence
7. if (j = m), k trailing gaps in A
8. k normal gaps in B

**b)** The scoring function s(x,y) is not a metric. Which of the following statements is correct?

 - [ ] The identity clause is violated
 - [ ] The symetry clause is violated
 - [ ] The triangle inequality clause is violated
 - [ ] It is possible to create a metric scoring function leading to the same optimal alignments where end gaps are free
 - [ ] For the given scoring function a match case is as favorable as a the leading end gap case



### _Exercise 3 -  Gotoh Algorithm_

Consider the following sequences S 1 , S 2 and the similarity scoring via s(x, y) and g(k).

<p align="center">
<img src="./figures/exercise3_equations.svg" alt="metric1" width=70%/>
 </p>

**a)** Which optimization scheme (minimization/maximization) is to be applied?

**b)** Fill the according dynamic programming matrices using the Gotoh algorithm!
(Remember: D<sub>ij</sub> is the match/mismatch matrix. Q<sub>ij</sub> corresponds to gaps in S1 whilst
P<sub>ij</sub> corresponds to gaps in S2)

| D<sub>ij</sub>|   | T  | A  | C  | G  | C  | A  | G  | A   |
|---------------|---|----|----|----|----|----|----|----|-----|
|               |   |    |    |    |    |    |    |    |     |
| **T**         |   |    |    |    |    | -7 | -8 | -9 | -10 |
| **C**         |   |    |    |    |    | -5 | -7 | -8 | -9  |
| **C**         |   | -5 | -4 | 2  | -3 | -4 | -5 | -6 | -7  |
| **G**         |   | -6 | -5 | -3 | 3  |    |    |    |     |
| **A**         |   | -7 | -5 | -4 | -2 |    |    |    |     |

| Q<sub>ij</sub>|   | T   | A   | C   | G  | C  | A  | G  | A   |
|---------------|---|-----|-----|-----|----|----|----|----|-----|
|               |   |     |     |     |    |    |    |    |     |
| **T**         |   |     |     |     | -6 | -7 | -8 | -9 | -10 |
| **C**         |   |     |     |     | -5 | -6 | -7 | -8 | -9  |
| **C**         |   | -12 | -10 | -9  | -3 | -4 | -5 | -6 | -7  |
| **G**         |   | -13 | -11 | -10 |    |    |    |    |     |
| **A**         |   | -14 | -12 | -10 |    |    |    |    |     |




| P<sub>ij</sub> |   | T  | A  | C  | G   | C   | A   | G   | A   |
|----------------|---|----|----|----|-----|-----|-----|-----|-----|
|                |   |    |    |    |     |     |     |     |     |
| **T**          |   |    |    |    | -13 | -14 | -15 | -16 | -17 |
| **C**          |   |    |    |    | -11 | -12 | -13 | -14 | -15 |
| **C**          |   | -5 | -4 | -8 | -10 | -10 | -12 | -13 | -14 |
| **G**          |   | -6 | -5 | -3 |     |     |     |     |     |
| **A**          |   | -7 | -6 | -4 |     |     |     |     |     |



**c)** Calculate all optimal alignments and the according score!

**d)** Calculate the alignments using the Waterman-Smith-Beyer algorithm instead.


### _Exercise 4 - Programming assignment: Implementation of Gotoh algorithm_

The programming assignment will use a scoring function as parameters which is a dictionary with 4 entries.
This will look as follows:

<p align="center">
scoring = {"match": -1,
               "mismatch": 1,
               "gap_introduction": 4,
               "gap_extension: 1}
</p>

You do not need to write the scoring function by yourself. However, make sure you use the correct keys in your implementation.
An example will be provided in the skeleton of part *a)*.

Despite most implementations of Gotoh will use a maximization at the optimization step, we will stick to the lecture and use minimization (score(match) < score(gap)). Also, have a look at return typehints in the skeleton functions and read carefully how the results should be returned.


**a)** Implement the function zero_init() which takes two sequences S1 and S2 and creates the Needleman-Wunsch matrix and initiates all the matrix values with zeroes. Hereby S1 should be represented by the rows and S2 by the columns.


**b)** Implement the function d_matrix_init() which takes two sequences S1 and S2 as well as the scoring function and fills in the values for the first row and first column of the D matrix with the correct values. Utilize *a)* in your implementation.

**c)** Implement the function p_matrix_init() which takes two sequences S1 and S2 and fills in the values for the first row and first column of the P matrix with the correct values. Utilize *a)* in your implementation.

**d)** Implement the function q_matrix_init() which takes two sequences S1 and S2 and fills in the values for the first row and first column of the Q matrix with the correct values. Utilize *a)* in your implementation.

**e)** Implement the function gotoh_init() which initializes all three matrices. Utilize *b)*, *c)*, *d)* in your implementation.

**f)** Implement the function gothoh_forward() which takes the two sequences S1 and S2 and the scoring function and output the complete matrices D, P and Q filled in with the Gotoh approach.

The following steps will help you with implementing the traceback.

**g)** Implement the function previous_cells() which takes two sequences S1 and S2, scoring function, the filled in recursion matrices from the step *f)* and the cell coordinates as a tuple with the matrix name and the coordinates pair (matrix, (row, column)). I.e. ("D", (2, 3))
The function should output a list of tuples of all possible previous cells. The tuples should be again structured like (matrix, (row, column)). Use capital D, P and Q to refer to the corresponding matrix

**h)** Implement the function build_all_traceback_paths() which builds all possible traceback paths. This function should return a list of possible paths which themselves are a list of tuples (matrix, (row, column)). The ordering must be decreasing. Meaning paths should start in the lower right corner of the matrix D.

**i)** Implement the function build_alignment() which takes two sequences and a path as a list of tuples. This function should return an alignment tuple. Meaning two strings of same length with introduced gaps.

---
