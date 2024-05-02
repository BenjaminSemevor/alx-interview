#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    if not isinstance(boxes, list) or not boxes:
        return False

    unlocked = [0]
    for box in unlocked:
        for key in boxes[box]:
            if key not in unlocked and 0 <= key < len(boxes):
                unlocked.append(key)
    return len(unlocked) == len(boxes)
