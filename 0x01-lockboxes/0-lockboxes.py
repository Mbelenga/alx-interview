#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    This is a method that determines if all
    the boxes can be opened
    """
    unlocked = set([0])
    keys = [0]
    len_box = len(boxes)
    counter = 0

    if len_box == 1:
        return True

    while counter < len(keys):
        index = keys[counter]
        for key in boxes[index]:
            if key not in unlocked and key < len_box:
                unlocked.add(key)
                keys.append(key)
        counter += 1
    return len(unlocked) == len_box
