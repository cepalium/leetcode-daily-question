"""
66. Plus One
Easy

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    num = int("".join([str(d) for d in digits]))  # join digits into number
    num_plusOne = num + 1  # calculate num_plusOne
    result = [
        int(d) for d in str(num_plusOne)
    ]  # split num_plusOne into list of digits
    return result


if __name__ == "__main__":
    assert plusOne(digits=[1, 2, 3]) == [1, 2, 4]
    assert plusOne(digits=[4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plusOne(digits=[9]) == [1, 0]
