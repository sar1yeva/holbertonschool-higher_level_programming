#!/usr/bin/python3
def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # First element
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element
        triangle.append(row)

    return triangle
