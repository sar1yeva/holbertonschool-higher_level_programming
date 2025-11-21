#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    try:
        result = my_list_1 / my_list_2
    except ZeroDivisionError:
        result = 0
    finally:
        print("Inside result: {}".format(result))
    return result
