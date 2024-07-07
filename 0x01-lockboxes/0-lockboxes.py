#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    This is a method that determines if all
    the boxes can be opened
    """
    total = len(boxes)
    visited = [0]
    opened = 0
    current_key = 0

    while current_key < len(visited):
        current_box = visited[current_key]

        for key in boxes[current_box]:
            if 0 < key < total and key not in  visited:
                visited.append(key)
                opened += 1

                current_key += 1

            return opened == total - 1
