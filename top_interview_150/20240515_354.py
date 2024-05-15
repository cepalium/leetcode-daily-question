"""
354. Russian Doll Envelopes
Hard

You are given a 2D array of integers envelopes 
where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height 
of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll 
(i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll 
is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
"""

from typing import List


def maxEnvelopes(envelopes: List[List[int]]) -> int:
    n = len(envelopes)
    if n == 1:
        return 1

    # DP
    envelopes.sort(key=lambda x: (x[0], x[1]))  # sort
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if (
                envelopes[i][0] > envelopes[j][0]
                and envelopes[i][1] > envelopes[j][1]
                and dp[i] <= dp[j]
            ):
                dp[i] = dp[j] + 1
    return max(dp)


if __name__ == "__main__":
    assert maxEnvelopes(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert maxEnvelopes(envelopes=[[1, 1], [1, 1], [1, 1]]) == 1
    assert (
        maxEnvelopes(
            envelopes=[[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]
        )
        == 3
    )
    assert (
        maxEnvelopes(
            envelopes=[
                [1, 2],
                [2, 3],
                [3, 4],
                [3, 5],
                [4, 5],
                [5, 5],
                [5, 6],
                [6, 7],
                [7, 8],
            ]
        )
        == 7
    )
    assert maxEnvelopes(envelopes=[[10, 8], [1, 12], [6, 15], [2, 18]]) == 2
