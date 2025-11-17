#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()  # make a copy to avoid modifying original
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
