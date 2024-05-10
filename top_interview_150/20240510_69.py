"""
69. Sqrt(x)
Easy

Given a non-negative integer x, 
return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., 
and since we round it down to the nearest integer, 2 is returned.
"""


def mySqrt(x: int) -> int:
    b = (x // 2) + 1
    while b * b > x:
        b = (b + x // b) // 2  # newton
    return b


if __name__ == "__main__":
    assert mySqrt(x=4) == 2
    assert mySqrt(x=8) == 2
