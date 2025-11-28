#!/usr/bin/python3
"""
Function that returns the Python object representation of a JSON string.
"""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string to be deserialized.

    Returns:
        any: Python object represented by the JSON string.
    """
    return json.loads(my_str)
