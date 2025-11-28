#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """Represents a list with a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
