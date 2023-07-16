# https://leetcode.com/problems/longest-palindromic-subsequence/

""" 
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting 
some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

# Recursion


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        m = len(s)

        s1 = s[::-1]

        def solve(ind1, ind2):
            if ind1 == n or ind2 == m:
                return 0

            if s[ind1] == s1[ind2]:
                return 1 + solve(ind1+1, ind2+1)

            return 0 + max(solve(ind1+1, ind2), solve(ind1, ind2+1))

        return solve(0, 0)


# Memoization
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        m = len(s)

        s1 = s[::-1]

        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def solve(ind1, ind2):
            if ind1 == n or ind2 == m:
                return 0

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if s[ind1] == s1[ind2]:
                dp[ind1][ind2] = 1 + solve(ind1+1, ind2+1)
                return dp[ind1][ind2]

            dp[ind1][ind2] = 0 + max(solve(ind1+1, ind2), solve(ind1, ind2+1))

            return dp[ind1][ind2]

        return solve(0, 0)
