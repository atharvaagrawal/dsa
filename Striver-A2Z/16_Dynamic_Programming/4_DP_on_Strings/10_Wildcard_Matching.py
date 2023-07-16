# https://leetcode.com/problems/wildcard-matching/


""" 
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""


# Recursion
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # ? Match any single char
        # a-z matches single char
        # * match any sequence char

        n = len(s)
        m = len(p)

        def isAllStar(ind):
            for j in range(ind, m):
                if p[j] != '*':
                    return False

            return True

        def solve(ind1, ind2):
            # If both string reach end
            if ind1 == n and ind2 == m:
                return True

            # If wildcard char end and string remaining
            if ind1 < n and ind2 == m:
                return False

            # If some wildcard are remaining and string completed
            if ind1 == n and ind2 < m:
                return isAllStar(ind2)

            # If Same Char or ?
            if s[ind1] == p[ind2] or p[ind2] == '?':
                return solve(ind1+1, ind2+1)
            # If *
            elif p[ind2] == '*':
                return solve(ind1+1, ind2) or solve(ind1, ind2+1)

            return False

        return solve(0, 0)


# Memoization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # ? Match any single char
        # a-z matches single char
        # * match any sequence char

        n = len(s)
        m = len(p)

        def isAllStar(ind):
            for j in range(ind, m):
                if p[j] != '*':
                    return False

            return True

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def solve(ind1, ind2):
            # If both string reach end
            if ind1 == n and ind2 == m:
                return True

            # If wildcard char end and string remaining
            if ind1 < n and ind2 == m:
                return False

            # If some wildcard are remaining and string completed
            if ind1 == n and ind2 < m:
                return isAllStar(ind2)

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            # If Same Char or ?
            if s[ind1] == p[ind2] or p[ind2] == '?':
                dp[ind1][ind2] = solve(ind1+1, ind2+1)
                return dp[ind1][ind2]
            # If *
            elif p[ind2] == '*':
                dp[ind1][ind2] = solve(ind1+1, ind2) or solve(ind1, ind2+1)
                return dp[ind1][ind2]

            return False

        return solve(0, 0)
