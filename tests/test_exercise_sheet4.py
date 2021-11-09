import pytest
from exercise_sheet4 import *


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
