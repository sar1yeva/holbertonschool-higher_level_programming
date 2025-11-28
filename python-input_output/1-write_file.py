#!/usr/bin/python3
"""
Function that writes a string to a UTF-8 text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Args:
        filename (str): Name of the file to write to.
        text (str): Text to write into the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
