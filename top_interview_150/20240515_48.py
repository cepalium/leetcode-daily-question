"""
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    # step 1: switch by diagonal
    # n=3: 0,1 <-> 1,0; 0,2 <-> 2,0; 1,2 <-> 2,1
    for i in range(n):
        for j in range(n):
            if i <= j:  # consider those elements on the right of diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # step 2: switch by vertical
    # n=3 (mid=1): 0,0 <-> 0,2; 1,0 <-> 1,2; 2,0 <-> 2,2
    for i in range(n):
        for j in range(n // 2):  # vertical line is mid = n//2
            matrix[i][j], matrix[i][n - 1 - j] = (
                matrix[i][n - 1 - j],
                matrix[i][j],
            )
    return matrix


if __name__ == "__main__":
    assert rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    assert rotate(
        matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
