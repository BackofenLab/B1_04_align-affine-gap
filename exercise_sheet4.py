from typing import List, Tuple, Dict


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
