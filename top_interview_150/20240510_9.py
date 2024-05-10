"""
9. Palindrome Number
Easy

Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(x: int) -> bool:
    # negative number is not palidrome
    if x < 0:
        return False

    nums = list(str(x))
    n = len(nums)
    # if the mirrored-index number is not matching, not palindrome
    for i in range(n // 2):
        if nums[i] != nums[n - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    assert isPalindrome(x=121) == True
    assert isPalindrome(x=-121) == False
    assert isPalindrome(x=10) == False
