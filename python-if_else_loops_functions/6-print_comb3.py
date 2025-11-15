#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        end_char = ", " if not (i == 8 and j == 9) else "\n"
        print("{:02}".format(i*10 + j), end=end_char)
