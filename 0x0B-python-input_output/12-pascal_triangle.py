#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """ returns list of integers representing
    the Pascal triangle of n """

    if n <= 0:
        return []

    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
            continue
        if i == 1:
            result.append([1, 1])
            continue
        row = []
        # init row
        for j in range(i + 1):
            row.append(j)
        for j in range(1, i):
            row[0] = 1
            row[i] = 1
            row[j] = result[i - 1][j] + result[i - 1][j - 1]
        result.append(row)

    return result
