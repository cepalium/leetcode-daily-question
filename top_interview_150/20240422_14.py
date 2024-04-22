"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    strs_sorted = sorted(strs)  # sort all strings alphabetically
    shortest_str = strs_sorted[0]
    longest_str = strs_sorted[-1]
    # longest common prefix must be btw the shortest and longest strings
    max_index = -1
    for i in range(len(shortest_str)):
        if shortest_str[i] == longest_str[i]:
            max_index = i
        else:
            break
    if max_index == -1:  # for-loop above could not find any common prefix
        return ""
    return shortest_str[: max_index + 1]  # return string of up to max_index


if __name__ == "__main__":
    assert longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix(strs=["dog", "racecar", "car"]) == ""
