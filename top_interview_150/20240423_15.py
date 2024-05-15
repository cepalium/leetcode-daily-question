"""
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # initialize variables
    target = 0
    n = len(nums)
    nums_sorted = sorted(nums)
    result = []

    for i in range(n - 2):
        # optimize, as i+j+k will be > target
        if nums_sorted[i] > target:
            break
        # optimize, as triplet [i, j, k] will be duplicated
        if (nums_sorted[i] == nums_sorted[i - 1]) and (i > 0):
            continue

        j, k = i + 1, n - 1
        while j < k:
            # optimize, as i+j+k will be < target
            if nums_sorted[k] < target:
                break
            # optimize, as triplet [i, j, k] will be duplicated
            if (nums_sorted[j] == nums_sorted[j - 1]) and (j > i + 1):
                j += 1
                continue

            sum_ijk = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
            if sum_ijk == target:
                result.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                j += 1
                k -= 1
            elif sum_ijk < target:
                j += 1
            else:  # sum_ijk > target
                k -= 1
    return result


if __name__ == "__main__":
    assert threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum(nums=[0, 1, 1]) == []
    assert threeSum(nums=[0, 0, 0]) == [[0, 0, 0]]
