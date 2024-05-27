"""
215. Kth Largest Element in an Array
Medium

Given an integer array nums and an integer k, 
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    nums_sorted = sorted(nums, reverse=True)
    result = nums_sorted[k - 1]
    return result


if __name__ == "__main__":
    assert findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
    assert findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
