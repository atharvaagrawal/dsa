# https://leetcode.com/problems/delete-operation-for-two-strings/description/

""" 
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string. 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""

# Recursion


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def solve(ind1, ind2):

            if ind1 == n or ind2 == m:
                return 0

            if word1[ind1] == word2[ind2]:
                ans = 1 + solve(ind1+1, ind2+1)
                return ans

            ans = 0 + max(solve(ind1+1, ind2), solve(ind1, ind2+1))

            return ans

        ans = solve(0, 0)
        print(ans)

        # In ans we got same
        return m+n-ans-ans


# Memoization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def solve(ind1, ind2):

            if ind1 == n or ind2 == m:
                return 0

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if word1[ind1] == word2[ind2]:
                ans = 1 + solve(ind1+1, ind2+1)
                dp[ind1][ind2] = ans
                return ans

            ans = 0 + max(solve(ind1+1, ind2), solve(ind1, ind2+1))
            dp[ind1][ind2] = ans
            return ans

        ans = solve(0, 0)

        # In ans we got same
        return m+n-ans-ans
