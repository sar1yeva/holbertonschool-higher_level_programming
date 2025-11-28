#!/usr/bin/python3
"""
Function that creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Deserialize a JSON file to a Python object.

    Args:
        filename (str): The JSON file to read from.

    Returns:
        any: Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
