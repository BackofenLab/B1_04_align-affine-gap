import pytest
from exercise_sheet4 import *
from gotoh_implementation.gotoh import *
from math import inf
import pprint
import random

HELPER = {
    0: "d",
    1: "p",
    2: "q"
}

SCORING = [
    {"match": -1, "mismatch": 0, "gap_introduction": 4, "gap_extension": 1},
    {"match": -1, "mismatch": 0, "gap_introduction": 2, "gap_extension": 1 },
    {"match": -1, "mismatch": 1, "gap_introduction": 2, "gap_extension": 1},
    {"match": -2, "mismatch": 1, "gap_introduction": 2, "gap_extension": 1},
]


def random_seq_generator(length, random_seed):
    random.seed(random_seed)
    return "".join(
        [random.choice(["A", "T", "C", "G"]) for _ in range(length)]
    )

def check_none(*args):
    if None in args:
        print("you have not filled in all the fields")
        raise ValueError

def check_zero_in_dict(d):
    val = d.values()
    if 0 in val:
        print("you have not filled in all the fields")
        raise ValueError

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

def test_exercise_2a():
    answer = exercise_2a()
    check_zero_in_dict(answer)
    assert answer["a"] == 6
    assert answer["b"] == 4
    assert answer["c"] == 8
    assert answer["d"] == 2
    assert answer["e"] == 3
    assert answer["f"] == 5
    assert answer["g"] == 1
    assert answer["h"] == 7

def test_exercise_2b():
    """
    The identity clause is violated: for x = y, s(x,y) = -1, which is not 0
    The triangle inequality clause is violated: s(x,x) > s(x,x) + s(x,x), when x=y=z
    It is not possible to create a metric. To create a metric we need to ensure the indentity clause is fulfilled,
    by setting s(x,y) = 0, when x=y. Thereby, we would cuse the match case to be as favorable as the leading/trailing
    end gap case. Setting s(x,y) = 0 leads to more optimal alignments, including an alignment
    where both sequences are aligned to gaps.
    """
    a,b,c,d,e = exercise_2b()
    assert a is True
    assert b is False
    assert c is True
    assert d is False
    assert e is False

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


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
def test_exercise_4a(seq1, seq2):
    matrix_expected = zero_init_correct(seq1, seq2)
    matrix = zero_init(seq1, seq2)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your init matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4b(seq1, seq2, scoring):
    matrix_expected = init_d_matrix_correct(seq1, seq2, scoring)
    matrix = d_matrix_init(seq1, seq2, scoring)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your d-matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
def test_exercise_4c(seq1, seq2):
    matrix_expected = init_p_matrix_correct(seq1, seq2)
    matrix = p_matrix_init(seq1, seq2)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your p-matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
def test_exercise_4d(seq1, seq2):
    matrix_expected = init_q_matrix_correct(seq1, seq2)
    matrix = q_matrix_init(seq1, seq2)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your q-matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4e(seq1, seq2, scoring):
    expected_matrices = gotoh_init_correct(seq1, seq2, scoring)
    matrices = gotoh_init(seq1, seq2, scoring)
    for x, matrix in enumerate(matrices):
        if matrix != expected_matrices[x]:
            print(
                f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
            print(f"Your {HELPER[x]}-matrix is:")
            pprint.pprint(matrix)
            print("It is supposed to look like:")
            pprint.pprint(expected_matrices[x])
    assert matrices == expected_matrices


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4f(seq1, seq2, scoring):
    expected_matrices = gotoh_forward_correct(seq1, seq2, scoring)
    matrices = gotoh_forward(seq1, seq2, scoring)
    for x, matrix in enumerate(matrices):
        if matrix != expected_matrices[x]:
            print(
                f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
            print(f"Your {HELPER[x]}-matrix is:")
            pprint.pprint(matrix)
            print("It is supposed to look like:")
            pprint.pprint(expected_matrices[x])
    assert matrices == expected_matrices


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
@pytest.mark.parametrize(
    "cell",
    [
        ("D", (3, 2)),
        ("D", (3, 3)),
        ("D", (2, 2)),
        ("D", (3, 1)),
        ("P", (3, 2)),
        ("Q", (3, 2)),
        ("Q", (3, 3)),
     ]
)
def test_exercise_4g(seq1, seq2, scoring, cell):
    d, p, q = gotoh_forward_correct(seq1, seq2, scoring)
    expected_prev = previous_cells_correct(seq1, seq2, scoring, d, p, q, cell)
    prev = previous_cells(seq1, seq2, scoring, d, p, q, cell)
    expected_cells = set(expected_prev)
    actual_cells = set(prev)
    if actual_cells != expected_cells:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\ncell: {cell}\n"
              f"scoring: {scoring}")
        print(f"Your previous cells are:\n{actual_cells}")
        print(f"It should be:\n{expected_cells}")
    assert actual_cells == expected_cells


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4h(seq1, seq2, scoring):
    d, p, q = gotoh_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(seq1, seq2, scoring, d, p, q)
    expected_paths = [tuple(x) for x in expected_paths]
    expected_paths = set(expected_paths)
    actual_paths = build_all_traceback_paths(seq1, seq2, scoring, d, p, q)
    actual_paths = [tuple(x) for x in actual_paths]
    actual_paths = set(actual_paths)
    if actual_paths != expected_paths:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your paths are:")
        pprint.pprint(actual_paths)
        print(f"It should be:")
        pprint.pprint(expected_paths)
    assert expected_paths == actual_paths


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4i(seq1, seq2, scoring):
    d, p, q = gotoh_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(
        seq1, seq2, scoring, d, p, q)
    for traceback_path in expected_paths:
        expected_alignment = build_alignment_correct(seq1, seq2,
                                                     traceback_path)
        actual_alignment = build_alignment(seq1, seq2, traceback_path)
        if actual_alignment != expected_alignment:
            print(
                f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}\npath: {traceback_path}")
            print("Your alignment is:")
            print(f"S1: {actual_alignment[0]}\nS2: {actual_alignment[1]}")
            print("It should be:")
            print(f"S1: {expected_alignment[0]}\nS2: {expected_alignment[1]}")
        assert expected_alignment == actual_alignment




