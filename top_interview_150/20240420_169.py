"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    # initilize variables
    majority_count = 1
    majority_element = nums[0]
    element_count_dict = {}

    for e in nums:
        # check element count
        if e not in element_count_dict.keys():
            element_count_dict[e] = 1
        else:
            element_count_dict[e] += 1
        # check majority element
        if element_count_dict[e] > majority_count:
            majority_count = element_count_dict[e]
            majority_element = e
    return majority_element


if __name__ == "__main__":
    assert majorityElement(nums=[3, 2, 3]) == 3
    assert majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
