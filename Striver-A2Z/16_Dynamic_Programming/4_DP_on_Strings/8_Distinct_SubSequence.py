# https://leetcode.com/problems/distinct-subsequences/


""" 
Given two strings s and t, return the number of distinct 
subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
"""


# Recursion
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)

        if n < m:
            return 0

        def solve(ind1, ind2):
            if ind2 == m:
                return 1
            if ind1 == n:
                return 0

            if s[ind1] == t[ind2]:
                ans = solve(ind1+1, ind2+1) + solve(ind1+1, ind2)
                return ans
            else:
                ans = solve(ind1+1, ind2)
                return ans

        return solve(0, 0)


# Memoization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)

        if n < m:
            return 0

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def solve(ind1, ind2):
            if ind2 == m:
                return 1
            if ind1 == n:
                return 0

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if s[ind1] == t[ind2]:
                ans = solve(ind1+1, ind2+1) + solve(ind1+1, ind2)
                dp[ind1][ind2] = ans
                return ans
            else:
                ans = solve(ind1+1, ind2)
                dp[ind1][ind2] = ans
                return ans

        return solve(0, 0)
