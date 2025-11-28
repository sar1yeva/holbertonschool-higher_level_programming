#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj (any): The object to convert to JSON.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
