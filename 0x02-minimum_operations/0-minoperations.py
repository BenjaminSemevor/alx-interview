#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get to n.
    
    :param n: The number to reach
    :return: The minimum number of operations
    """
    if n <= 1:
        return 0
    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n / op)) + op
