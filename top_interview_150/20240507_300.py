"""
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # DP
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)


if __name__ == "__main__":
    assert lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
    assert lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
