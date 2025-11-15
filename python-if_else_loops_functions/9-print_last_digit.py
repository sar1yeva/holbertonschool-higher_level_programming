#!/usr/bin/python3
def print_last_digit(number):
    if number in range(0, 10):
        print(number, end="")
        return number
    elif number < 0:
        number = abs(number)
        print(number % 10, end="")
        return number % 10
    else:
        number = number % 10
        print(number, end="")
        return number
