#!/usr/bin/python3
"""
Function that appends a string to a UTF-8 text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file.

    Args:
        filename (str): Name of the file to append to.
        text (str): Text to append at the end of the file.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
