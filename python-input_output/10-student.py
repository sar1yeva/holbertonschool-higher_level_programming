#!/usr/bin/python3
"""
Student class definition.
"""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings,
        only attributes in this list are included.
        Otherwise, all attributes are included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary containing the requested attributes.
        """
        if attrs is None:
            return self.__dict__.copy()

        if isinstance(attrs, list):
            filtered_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered_dict[key] = self.__dict__[key]
            return filtered_dict

        # If attrs is not a list, return all attributes
        return self.__dict__.copy()
