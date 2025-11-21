#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i=0
    try:
        while i < x:
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except ValueError, TypeError:
                pass
     except IndexError:
         raise
     print()
     return count
