"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    num_map = {
        num: i for i, num in enumerate(nums)
    }  # edge case: duplicate numbers in different indices

    for i in range(n):
        complement = target - nums[i]
        if complement in num_map.keys() and num_map[complement] != i:
            return [i, num_map[complement]]

    return []  # no solution found


if __name__ == "__main__":
    assert twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert twoSum(nums=[3, 3], target=6) == [0, 1]
