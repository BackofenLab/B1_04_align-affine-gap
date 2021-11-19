from typing import List, Tuple, Dict
from math import inf

"""
Within the algorithm of Waterman, Smith and Beyer arbitrarily large gaps are
considered. Thus, also the traceback has to investigate all gap sizes.
This can be done following two strategies:

 - check in increasing gap length (start with smallest gap)
 - check in decreasing gap length (start with largest gap)
"""


def exercise_1a():
    """
    Exercise 1 a
    Given a gap function, are the strategies (measured in absolute runtime or
    number operations) expected to be equally performant or is one of them
    better than the other? Set the correct answer to True and the others to
    False
    """

    # both are equally performant
    both = None

    # checking in increasing direction performs better
    increasing = None

    # checking in decreasing direction performs better
    decreasing = None
    return both, increasing, decreasing


def exercise_1b():
    """
    Exercise 1 b
    Does the order of checking insertion and deletions change the runtime?
    """

    # yes, checking insertions first will perform better
    insertions_first = None

    # yes, checking deletions first will perform better
    deletions_first = None

    # no, the order doesn't affect performance
    no = None

    # checking in an alternating way might improve performance
    alternating = None

    return insertions_first, deletions_first, no, alternating

def exercise_2a():
    """
    Exercise 2 a
    Match the following descriptions with the correct recursion parts (see recursion figure, labels (a)-(h)):
    1. if (i = n), k trailing gaps in A
    2. k normal gaps in B
    3. j leading gaps in A (inner block of gaps)
    4. match/missmatch case
    5. i leading gaps in B (inner block of gaps)
    6. outer block of gaps in one sequence
    7. if (j = m), k trailing gaps in B
    8. k normal gaps in A
    """

    recursion = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0
    }

    return recursion

def exercise_2b():
    """
    Exercise 2 b
    The scoring function s(x,y) is not a metric. Which of the following statements is correct?
    Assign the correct True and False values to the provided options.
    """

    # The identity clause is violated
    a = None

    # The symetry clause is violated
    b = None

    # The triangle inequality clause is violated
    c = None

    # It is possible to create a metric scoring function leading to the same optimal alignments where end gaps are free
    d = None

    # For the given scoring function a match case is as favorable as a the leading end gap case
    e = None

    return a,b,c,d,e

def exercise_3a():
    """
    Exercise 3 a
    Consider the following sequences S 1 , S 2 and the similarity scoring via
    s(x, y) and g(k).
    S1 = TCCGA
    S2 = TACGCAGA
    s(x, y) = +1 if x == y else 0
    g(k) = -4 - 1*k
    Which optimization scheme (minimization/maximization) is to be applied?
    """
    minimization = None
    maximization = None

    return minimization, maximization


def exercise_3b():
    """
    Exercise 3 b
    Consider the following sequences S 1 , S 2 and the similarity scoring via
    s(x, y) and g(k).
    S1 = TCCGA
    S2 = TACGCAGA
    s(x, y) = +1 if x == y else 0
    g(k) = -4 - 1*k
    Fill the according dynamic programming matrices using the Gotoh algorithm!
    (Remember: Dij is the match/mismatch matrix. Qij corresponds to gaps in S1
    whilst Pij corresponds to gaps in S2)
    """
    #         T    A    C    G    C    A    G    A
    d_ij = [
        [0,   0,   0,   0,   0,   0,   0,   0,   0],
        [0,   0,   0,   0,   0,  -7,  -8,  -9, -10],  # T
        [0,   0,   0,   0,   0,  -5,  -7,  -8,  -9],  # C
        [0,  -5,  -4,   2,  -3,  -4,  -5,  -6,  -7],  # C
        [0,  -6,  -5,  -3,   3,   0,   0,   0,   0],  # G
        [0,  -7,  -5,  -4,  -2,   0,   0,   0,   0],  # A
    ]

    #         T    A    C    G    C    A    G    A
    q_ij = [
        [0,   0,   0,   0,   0,   0,   0,   0,   0],
        [0,   0,   0,   0,  -6,  -7,  -8,  -9, -10],  # T
        [0,   0,   0,   0,  -5,  -6,  -7,  -8,  -9],  # C
        [0, -12, -10,  -9,  -3,  -4,  -5,  -6,  -7],  # C
        [0, -13, -11, -10,   0,   0,   0,   0,   0],  # G
        [0, -14, -12, -10,   0,   0,   0,   0,   0],  # A
    ]
    #         T    A    C    G    C    A    G    A
    p_ij = [
        [0,   0,   0,   0,   0,   0,   0,   0,   0],
        [0,   0,   0,   0, -13, -14, -15, -16, -17],  # T
        [0,   0,   0,   0, -11, -12, -13, -14, -15],  # C
        [0,  -5,  -4,  -8, -10, -10, -12, -13, -14],  # C
        [0,  -6,  -5,  -3,   0,   0,   0,   0,   0],  # G
        [0,  -7,  -6,  -4,   0,   0,   0,   0,   0],  # A
    ]
    return d_ij, q_ij, p_ij


def exercise_3c() -> Tuple[List[Tuple[str, str]], int]:
    """
    Exercise 3 a
    Consider the following sequences S 1 , S 2 and the similarity scoring via
    s(x, y) and g(k).
    S1 = TCCGA
    S2 = TACGCAGA
    s(x, y) = +1 if x == y else 0
    g(k) = -4 - 1*k
    Calculate all optimal alignments as List of tuples and the according score!
    """
    alignments = []
    score = None

    return alignments, score


def exercise_3d() -> List[Tuple[str, str]]:
    """
    Exercise 3 d
    Consider the following sequences S 1 , S 2 and the similarity scoring via
    s(x, y) and g(k).
    S1 = TCCGA
    S2 = TACGCAGA
    s(x, y) = +1 if x == y else 0
    g(k) = -4 - 1*k
    Calculate the alignments using the Waterman-Smith-Beyer algorithm instead.
    """
    alignments = []

    return alignments


########################################################
############## Programming tasks #######################
########################################################


def zero_init(seq1, seq2):
    """
    Exercise 4 a
    Implement the function zero_init() which takes two sequences S1 and S2 and
    creates the helper matrix and initiates all the matrix values
    with zeroes. You can then use this matrix for D, P and Q matrices.
    Hereby S1 should be represented by the rows and S2 by the columns.
    """
    return None


def d_matrix_init(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 b
    Implement the function d_matrix_init which takes two sequences S1 and S2 and
    the scoring schema and initializes the D matrix of the Gotoh algorithm.
    Hereby S1 should be represented by the rows and S2 by the columns.
    """
    return None


def p_matrix_init(seq1, seq2):
    """
    Exercise 4 c
    Implement the function p_matrix_init which takes two sequences S1 and S2 and
    initializes the P matrix of the Gotoh algorithm.
    Hereby S1 should be represented by the rows and S2 by the columns.
    Use inf for the infinity and '-' to indicate the empty values to complete this matrix.
    """
    return None


def q_matrix_init(seq1, seq2):
    """
    Exercise 4 d
    Implement the function q_matrix_init which takes two sequences S1 and S2 and
    initializes the Q matrix of the Gotoh algorithm.
    Hereby S1 should be represented by the rows and S2 by the columns.
    Use inf for the infinity and '-' to indicate the empty values to complete this matrix.
    """
    return None


def gotoh_init(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 e
    Implement the function gotoh_init() to complete Gotoh initialization step
    Return the D, P and Q matrices with the corresponding initial values.
    """
    d_matrix, p_matrix, q_matrix = None, None, None
    return d_matrix, p_matrix, q_matrix


def gotoh_forward(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 f
    Implement the function gotoh_forward() which takes two sequences S1 and S2 as
    well as the scoring function and fills in all the values in D, P and Q matrices
    """
    d_matrix, p_matrix, q_matrix = gotoh_init(seq1, seq2, scoring)

    # write your code here

    return d_matrix, p_matrix, q_matrix


def previous_cells(
    seq1, seq2, scoring, d_matrix, p_matrix, q_matrix, cell: Tuple[str, Tuple[int, int]]
) -> List[Tuple[str, Tuple[int, int]]]:

    """
    Exercise 4 g
    Implement the function previous_cells() which takes two sequences S1 and
    S2, scoring function, the filled in recursion matrices from the step f) and
    the cell coordinates (matrix, (row, column)) i.e. ("D", (1, 3)). The function should output the list
    of all possible previous cells.
    """
    return None


def build_all_traceback_paths(seq1, seq2, scoring, d_matrix, p_matrix, q_matrix) -> \
        List[List[Tuple[str, Tuple[int, int]]]]:
    """
    Exercise 4 h
    Implement the function which builds all possible traceback paths.
    """
    return None


def build_alignment(seq1, seq2, traceback_path) -> Tuple[str, str]:
    """
    Exercise 4 i
    Implement the function build_alignment() which takes two sequences and
    outputs the alignment.
    """
    return None
