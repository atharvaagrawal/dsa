# https://leetcode.com/problems/longest-common-subsequence/
""" 
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) 
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def solve(ind1, ind2):
            if ind1 < 0 or ind2 < 0:
                return 0

            if text1[ind1] == text2[ind2]:
                return 1 + solve(ind1-1, ind2-1)

            return 0 + max(solve(ind1-1, ind2), solve(ind1, ind2-1))

        return solve(len(text1)-1, len(text2)-1)


# Memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def solve(ind1, ind2):
            if ind1 < 0 or ind2 < 0:
                return 0

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if text1[ind1] == text2[ind2]:
                dp[ind1][ind2] = 1 + solve(ind1-1, ind2-1)
                return dp[ind1][ind2]

            dp[ind1][ind2] = 0 + max(solve(ind1-1, ind2), solve(ind1, ind2-1))

            return dp[ind1][ind2]

        return solve(len(text1)-1, len(text2)-1)


# Tabulation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for ind1 in range(1, len(text1)+1):
            for ind2 in range(1, len(text2)+1):
                if text1[ind1-1] == text2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = 0 + \
                        max(dp[ind1-1][ind2], dp[ind1][ind2-1])

        return dp[len(text1)][len(text2)]


# Space Optimization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        prev = [0 for i in range(len(text2)+1)]
        curr = [0 for i in range(len(text2)+1)]

        for ind1 in range(1, len(text1)+1):
            for ind2 in range(1, len(text2)+1):
                if text1[ind1-1] == text2[ind2-1]:
                    curr[ind2] = 1 + prev[ind2-1]
                else:
                    curr[ind2] = 0 + max(prev[ind2], curr[ind2-1])

            prev = curr[:]

        return prev[len(text2)]
