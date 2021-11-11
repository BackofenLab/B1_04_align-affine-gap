from typing import Dict, List, Tuple
from math import inf


def zero_init_correct(seq1, seq2):
    return [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]


def init_d_matrix_correct(seq1, seq2, scoring):
    match, mismatch, gap_intro, gap_extend = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
        scoring["gap_extension"]
    )
    d_matrix = zero_init_correct(seq1, seq2)
    first_row = [0] + [gap_intro + i * gap_extend for i in range(1, len(seq2) + 1)]
    d_matrix[0] = first_row
    for index, row in enumerate(d_matrix):
        if index > 0:
            row[0] = gap_intro + index * gap_extend
    return d_matrix


def init_p_matrix_correct(seq1, seq2):
    p_matrix = zero_init_correct(seq1, seq2)
    first_row = [inf for _ in range(len(seq2) + 1)]
    if first_row:
        first_row[0] = 0
    p_matrix[0] = first_row
    for index, row in enumerate(p_matrix):
        if index == 0:
            row[0] = 0
        else:
            row[0] = "-"
    return p_matrix


def init_q_matrix_correct(seq1, seq2):
    q_matrix = zero_init_correct(seq1, seq2)
    first_row = ["-" for _ in range(len(seq2) + 1)]
    if first_row:
        first_row[0] = 0
    q_matrix[0] = first_row
    for index, row in enumerate(q_matrix):
        if index == 0:
            row[0] = 0
        else:
            row[0] = inf
    return q_matrix


def gotoh_init_correct(seq1, seq2, scoring):
    d_matrix = init_d_matrix_correct(seq1, seq2, scoring)
    p_matrix = init_p_matrix_correct(seq1, seq2)
    q_matrix = init_q_matrix_correct(seq1, seq2)
    return d_matrix, p_matrix, q_matrix


def gotoh_forward_correct(seq1, seq2, scoring: Dict[str, int]):
    match_score, mismatch_score, gap_intro, gap_extend = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
        scoring["gap_extension"]
    )

    d_matrix, p_matrix, q_matrix = gotoh_init_correct(seq1, seq2, scoring)
    for row_index, row_d in enumerate(d_matrix[1:], 1):
        for column_index, column_d in enumerate(row_d[1:], 1):
            p_d = d_matrix[row_index-1][column_index] + gap_intro + gap_extend
            p_p = p_matrix[row_index-1][column_index] + gap_extend
            p_matrix[row_index][column_index] = min(p_d, p_p)

            q_d = d_matrix[row_index][column_index-1] + gap_intro + gap_extend
            q_q = q_matrix[row_index][column_index - 1] + gap_extend
            q_matrix[row_index][column_index] = min(q_d, q_q)

            char_seq_1, char_seq_2 = seq1[row_index - 1], seq2[column_index - 1]
            no_gap_score = match_score if char_seq_1 == char_seq_2 else mismatch_score
            d_diagonal = d_matrix[row_index - 1][column_index - 1] + no_gap_score
            d_p = p_matrix[row_index][column_index]
            d_q = p_matrix[row_index][column_index]
            d_matrix[row_index][column_index] = min(d_diagonal, d_p, d_q)

            print("matrix", row_index, column_index)
            print(d_diagonal, d_p, d_q, )

    return d_matrix, p_matrix, q_matrix


def previous_cells_correct(seq1, seq2, scoring, d_matrix, p_matrix, q_matrix, cell):
    match_score, mismatch_score, gap_intro, gap_extend = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
        scoring["gap_extension"]
    )

    prev_cells = []
    cell_matrix, cell_coordinates = cell[0], cell[1]

    row, column = cell_coordinates

    if cell_matrix == "D":
        cell_value = d_matrix[row][column]
        char_first, char_second = seq1[row - 1], seq2[column - 1]
        match_score_diag = match_score if char_first == char_second else mismatch_score
        if cell_value == (d_matrix[row-1][column-1] + match_score_diag):
            prev_cells.append(("D", (row-1, column-1)))
        if cell_value == p_matrix[row, column]:
            prev_cells.append(("P", (row, column)))

    elif cell_matrix == "P":
        cell_value = p_matrix[row][column]
        if cell_value == (d_matrix[row-1][column] + gap_intro + gap_extend):
            prev_cells.append(("D", (row-1, column)))
        if cell_value == (p_matrix[row-1][column] + gap_extend):
            prev_cells.append(("P", (row-1, column)))
    else:
        cell_value = q_matrix[row][column]
        if cell_value == (d_matrix[row][column - 1] + gap_intro + gap_extend):
            prev_cells.append(("D", (row, column - 1)))
        if cell_value == (p_matrix[row][column - 1] + gap_extend):
            prev_cells.append(("P", (row, column - 1)))

    return prev_cells


def main():
    scoring = {"match": 0, "mismatch": 1, "gap_introduction": 4, "gap_extension": 1}
    s1 = "CC"
    s2 = "ACCT"
    d, p, q = gotoh_init_correct(s1, s2, scoring)
    d, p, q = gotoh_forward_correct(s1, s2, scoring)

    print(d)
    print(p)
    print(q)


if __name__ == "__main__":
    main()
