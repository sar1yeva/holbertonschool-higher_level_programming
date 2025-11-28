#!/usr/bin/env python3
"""
Task 02: Convert a CSV file to JSON.

This module defines a function that
reads data from a CSV file and serializes
it into a JSON file named 'data.json'.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and save it to data.json.

    Args:
        csv_filename (str): The path to the CSV file to convert.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        data_list = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
