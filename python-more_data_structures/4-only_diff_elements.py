#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
     diff = set()
    for number in set_1:
        if number in not set_2:
            diff.add(number)
    return diff
