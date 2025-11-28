#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a JSON file.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list from file, or start with empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save updated list back to the file
save_to_json_file(items, filename)
