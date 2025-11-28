#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize a square with a private size attribute.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
