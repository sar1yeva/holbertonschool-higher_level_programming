#!/usr/bin/env python3
"""
Task 01: Pickle serialization of a custom Python object.

This module defines the CustomObject class that can be serialized to and
deserialized from a file using the pickle module. It safely handles errors
such as non-existent or corrupted files.
"""

import pickle


class CustomObject:
    """Custom object with name, age, and student status attributes."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Args:
            filename (str): File to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            pass  # Ignore errors silently

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject from a file.

        Args:
            filename (str): File containing the serialized object.

        Returns:
            CustomObject or None: The deserialized object,
        or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError, EOFError):
            return None
