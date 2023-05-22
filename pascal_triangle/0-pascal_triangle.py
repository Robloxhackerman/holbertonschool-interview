#!/usr/bin/python3
"""
aaaaaa
"""


def pascal_triangle(n):
    """
    aaaaa
    """
    pascal_list = []
    if n <= 0:
        return pascal_list
    for PEPE1 in range(n):
        row = [1]
        if pascal_list:
            last_row = pascal_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal_list.append(row)
    return pascal_list
