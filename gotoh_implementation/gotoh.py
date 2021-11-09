from math import inf


def zero_init_correct(seq1, seq2):
    return [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

def init_d_matrix(seq1, seq2, scoring):
    pass


def init_p_matrix(seq1 ,seq2, scoring):
    pass


def init_q_matrix(seq1, seq2, scoring):
    pass


def gotoh_init(seq1, seq2, scoring):
    d_matrix = init_d_matrix(seq1, seq2, scoring)
    p_matrix = init_p_matrix(seq1, seq2, scoring)
    q_matrix = init_q_matrix(seq1, seq2, scoring)
    return