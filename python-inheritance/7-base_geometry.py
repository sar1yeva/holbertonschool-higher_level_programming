#!/usr/bin/python3
"""
Defines a BaseGeometry class with area() and integer_validator().
"""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """
        Raises an exception because area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer > 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
