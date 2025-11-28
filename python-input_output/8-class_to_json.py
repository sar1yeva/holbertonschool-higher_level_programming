#!/usr/bin/python3
"""
Function that returns the dictionary
description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Return a dictionary representation of obj suitable for JSON serialization.

    Args:
        obj (any): Instance of a class.

    Returns:
        dict: Dictionary containing all simple data attributes of obj.
    """
    return obj.__dict__.copy()

