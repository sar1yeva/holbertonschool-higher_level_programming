#!/usr/bin/python3
"""
Function that reads a UTF-8 text file and prints it to stdout.
"""


def read_file(filename=""):
    """Read a text file (UTF-8) and print its content.

    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
