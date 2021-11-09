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

    - WARNING: Scoring Image missing

### _Exercise 3 -  Gotoh Algorithm_

Consider the following sequences S 1 , S 2 and the similarity scoring via s(x, y) and g(k).

<p align="center">
<img src="./figures/exercise3_equations.svg" alt="metric1" width=70%/>
 </p>

**a)** Which optimization scheme (minimization/maximization) is to be applied?

**b)** Fill the according dynamic programming matrices using the Gotoh algorithm!
(Remember: D<sub>ij</sub> is the match/mismatch matrix. Q<sub>ij</sub> corresponds to gaps in S1 whilst 
P<sub>ij</sub> corresponds to gaps in S2)

| D<sub>ij</sub>  | T  | A  | C  | G  | C  | A  | G  | A   |
|-----|----|----|----|----|----|----|----|-----|
| **T**   |    |    |    |    | -7 | -8 | -9 | -10 |
| **C**   |    |    |    |    | -5 | -7 | -8 | -9  |
| **C**   | -5 | -4 | 2  | -3 | -4 | -5 | -6 | -7  |
| **G**   | -6 | -5 | -3 | 3  |    |    |    |     |
| **A**   | -7 | -5 | -4 | -2 |    |    |    |     |

| Q<sub>ij</sub>  | T   | A   | C   | G  | C  | A  | G  | A   |
|-----|-----|-----|-----|----|----|----|----|-----|
| **T**    |     |     |     | -6 | -7 | -8 | -9 | -10 |
| **C**   |     |     |     | -5 | -6 | -7 | -8 | -9  |
| **C**    | -12 | -10 | -9  | -3 | -4 | -5 | -6 | -7  |
| **G**    | -13 | -11 | -10 |    |    |    |    |     |
| **A**    | -14 | -12 | -10 |    |    |    |    |     |


| P<sub>ij</sub> | T  | A  | C  | G   | C   | A   | G   | A   |
|-----|----|----|----|-----|-----|-----|-----|-----|
| **T**   |    |    |    | -13 | -14 | -15 | -16 | -17 |
| **C**   |    |    |    | -11 | -12 | -13 | -14 | -15 |
| **C**   | -5 | -4 | -8 | -10 | -10 | -12 | -13 | -14 |
| **G**   | -6 | -5 | -3 |     |     |     |     |     |
| **A**   | -7 | -6 | -4 |     |     |     |     |     |



**c)** Calculate all optimal alignments and the according score!

**d)** Are the expected alignments different when using the Waterman-Smith-Beyer algorithm instead?