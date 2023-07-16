# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
""" 
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.


Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
"""


# Recursion
class Solution:
    def minInsertions(self, s: str) -> int:

        m = n = len(s)
        s1 = s[::-1]

        def solve(ind1, ind2):
            if ind1 == n or ind2 == m:
                return 0

            if s[ind1] == s1[ind2]:
                ans = 1+solve(ind1+1, ind2+1)

                return ans

            ans = 0 + max(solve(ind1+1, ind2), solve(ind1, ind2+1))
            return ans

        ans = solve(0, 0)

        return m-ans


# Memoization
class Solution:
    def minInsertions(self, s: str) -> int:

        m = n = len(s)
        s1 = s[::-1]

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def solve(ind1, ind2):
            if ind1 == n or ind2 == m:
                return 0

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if s[ind1] == s1[ind2]:
                ans = 1+solve(ind1+1, ind2+1)
                dp[ind1][ind2] = ans
                return ans

            ans = 0 + max(solve(ind1+1, ind2), solve(ind1, ind2+1))
            dp[ind1][ind2] = ans
            return ans

        ans = solve(0, 0)

        return m-ans
