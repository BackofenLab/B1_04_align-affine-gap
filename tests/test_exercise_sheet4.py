import pytest
from exercise_sheet4 import *
from math import inf


def test_exercise_1a():
    """
    Large gaps are considered rare events in evolutionary related sequences,
    thus one should check for match/mismatch before screening for gaps. As we
    expect the existing gaps to be small, we would expect to find the optimal
    traceback (on average) earlier when using the “increasing gap length”
    strategy.
    """
    both, increasing, decreasing = exercise_1a()
    assert both is False
    assert increasing is True
    assert decreasing is False


def test_exercise_1b():
    """
    One could improve the runtime even more by checking both
    directions (insertion/deletion) alternatingly instead of checking one
    direction completely before switching to the other direction.
    """
    insertions_first, deletions_first, no, alternating = exercise_1b()
    assert insertions_first is False
    assert deletions_first is False
    assert no is False
    assert alternating is True


def test_exercise_3a():
    """
    Maximization since we are scoring a similarity and not a distance.
    """
    minimization, maximization = exercise_3a()
    assert minimization is False
    assert maximization is True


def test_exercise_3b():
    d_ij, q_ij, p_ij = exercise_3b()

    #          T    A    C    G    C    A    G    A
    expected_d_ij = [
        [0,   -5,  -6,  -7,  -8,  -9, -10, -11, -12],
        [-5,   1,  -4,  -5,  -6,  -7,  -8,  -9, -10],  # T
        [-6,  -4,   1,  -3,  -5,  -5,  -7,  -8,  -9],  # C
        [-7,  -5,  -4,   2,  -3,  -4,  -5,  -6,  -7],  # C
        [-8,  -6,  -5,  -3,   3,  -2,  -3,  -4,  -5],  # G
        [-9,  -7,  -5,  -4,  -2,   3,  -1,  -3,  -3],  # A
    ]

    assert d_ij == expected_d_ij

    #         T    A    C    G    C    A    G    A
    expected_q_ij = [
        [0,   0,   0,   0,   0,   0,   0,   0,   0],
        [-inf, -10,  -4,  -5,  -6,  -7,  -8,  -9, -10],  # T
        [-inf, -11,  -9,  -4,  -5,  -6,  -7,  -8,  -9],  # C
        [-inf, -12, -10,  -9,  -3,  -4,  -5,  -6,  -7],  # C
        [-inf, -13, -11, -10,  -8,  -2,  -3,  -4,  -5],  # G
        [-inf, -14, -12, -10,  -9,  -7,  -2,  -3,  -4],  # A
    ]
    assert q_ij == expected_q_ij
    expected_p_ij = [
        [0,-inf,-inf,-inf,-inf,-inf,-inf,-inf,-inf],
        [0, -10, -11, -12, -13, -14, -15, -16, -17],  # T
        [0, -4,  -9,  -10, -11, -12, -13, -14, -15],  # C
        [0, -5,  -4,   -8, -10, -10, -12, -13, -14],  # C
        [0, -6,  -5,   -3,  -8,  -9, -10, -11, -12],  # G
        [0, -7,  -6,   -4,  -2,  -7,  -8,  -9, -10],  # A
    ]

    assert p_ij == expected_p_ij


def test_exercise_3c():
    alignments, score = exercise_3c()
    expected_alignments = [
        ("T---CCGA",
         "TACGCAGA"),
        ("TCC---GA",
         "TACGCAGA"),
        ("TCCG---A",
         "TACGCAGA")
    ]

    assert score == -3
    assert set(alignments) == set(expected_alignments)


def test_exercise_3d():
    """
    The same alignments as in 3c, since the same scoring function is optimized.
    Calculation is just less efficient.
    """
    alignments = exercise_3d()
    expected_alignments = [
        ("T---CCGA",
         "TACGCAGA"),
        ("TCC---GA",
         "TACGCAGA"),
        ("TCCG---A",
         "TACGCAGA")
    ]

    assert set(alignments) == set(expected_alignments)
