#!/usr/bin/python3
"""
aaaa
"""


def minOperations(n):
    """
    aaaaaa
    """
    if n <= 1:
        return 0
    num = n
    div = 2
    operations = 0

    while num > 1:
        if num % div == 0:
            num = num / div
            operations = operations + div
        else:
            div += 1
    return operations
