from typing import List, Tuple


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

    # checking in increasing direction performs better
    deletions_first = None

    # checking in decreasing direction performs better
    no = None

    # checking in an alternating way might improve performance
    alternating = None

    return insertions_first, deletions_first, no, alternating


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
