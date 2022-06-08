#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda idx: idx * idx), elm)) for elm in matrix]
