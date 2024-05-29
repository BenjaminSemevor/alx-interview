#!/usr/bin/python3
"""
N queens solution finder module.
"""
import sys

solutions = []
n = 0
pos = None

def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    return n

def is_attacking(pos0, pos1):
    """Determines if two queens are in an attacking position.

    Args:
        pos0 (list or tuple): 1st queen's position.
        pos1 (list or tuple): 2nd queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    return pos0[0] == pos1[0] or pos0[1] == pos1[1] or abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

def group_exists(group):
    """Checks if a group exists in the list of solutions.

    Args:
        group (list of list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    for stn in solutions:
        if all(any(stn_pos == grp_pos for stn_pos in stn) for grp_pos in group):
            return True
    return False

def build_solution(row, group):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of list of integers): The group of valid positions.
    """
    if row == n:
        if not group_exists(group):
            solutions.append(group.copy())
    else:
        for col in range(n):
            pos_index = row * n + col
            new_position = pos[pos_index]
            if not any(is_attacking(new_position, grp_pos) for grp_pos in group):
                group.append(new_position)
                build_solution(row + 1, group)
                group.pop()

def get_solutions():
    """Gets the solutions for the given chessboard size."""
    global pos
    pos = [[i // n, i % n] for i in range(n ** 2)]
    build_solution(0, [])

if __name__ == "__main__":
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)
