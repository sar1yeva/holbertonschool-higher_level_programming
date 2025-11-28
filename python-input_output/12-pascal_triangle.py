#!/usr/bin/python3
"""
12-pascal_triangle module.

This module contains a function pascal_triangle(n) that
returns a list of lists representing Pascal's triangle
with n rows.
"""

 def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): Number of rows

    Returns:
        list of lists: Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
