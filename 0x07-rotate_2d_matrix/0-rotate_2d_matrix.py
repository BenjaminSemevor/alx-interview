#!/usr/bin/env python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Move top to right
            matrix[i][last] = top

