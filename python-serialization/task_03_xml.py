#!/usr/bin/env python3
"""
Task 03: Serialize and deserialize Python dictionaries using XML.

This module defines two functions:
- serialize_to_xml: Convert a dictionary to XML and save it to a file.
- deserialize_from_xml: Read XML from a file and reconstruct a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The output XML filename.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML from a file and return a Python dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: The reconstructed Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except FileNotFoundError:
        return {}
    except ET.ParseError:
        return {}
