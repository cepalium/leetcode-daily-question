"""
11. Container With Most Water
Medium

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

from typing import List


def maxArea(height: List[int]) -> int:
    # initialize variables
    i, j = 0, len(height) - 1  # 2 pointers
    max_area = min(height[i], height[j]) * (j - i)

    while i < j:
        # calculate area depending on current i & j
        # area = lower height btw i & j * width, with width = j-1
        if height[i] <= height[j]:
            area = height[i] * (j - i)
            i += 1
        else:
            area = height[j] * (j - i)
            j -= 1
        if area > max_area:
            max_area = area
    return max_area


if __name__ == "__main__":
    assert maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea(height=[1, 1]) == 1
