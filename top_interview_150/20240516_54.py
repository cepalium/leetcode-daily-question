"""
54. Spiral Matrix
Medium

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    n_rows, n_cols = len(matrix), len(matrix[0])
    # 4 corners of spiral
    top, bottom, left, right = 0, n_rows - 1, 0, n_cols - 1
    result = []

    while len(result) < n_rows * n_cols:
        # go spiral
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if (
            top <= bottom
        ):  # spiral right to left only top is still lesser than bottom
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if (
            left <= right
        ):  # spiral bottom upto top only when left is still lesser than right
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


if __name__ == "__main__":
    assert spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]
    assert spiralOrder(
        matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
