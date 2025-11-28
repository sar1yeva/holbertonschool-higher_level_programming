#!/usr/bin/env python3
"""
Serialization and deserialization of custom Python objects using pickle.
"""

import pickle


class CustomObject:
    """A custom object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file.

        Args:
            filename (str): The file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file and return an instance of CustomObject.

        Args:
            filename (str): The file containing the serialized object.

        Returns:
            CustomObject or None: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError):
            return None
