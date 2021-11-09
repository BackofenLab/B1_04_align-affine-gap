
"""
Within the algorithm of Waterman, Smith and Beyer arbitrarily large gaps are considered. Thus, also the traceback has to investigate all gap sizes. This can be done following two strategies:

check in increasing gap length (start with smallest gap)
check in decreasing gap length (start with largest gap)
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


