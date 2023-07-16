# https://leetcode.com/problems/edit-distance/

""" 
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


# Recursion
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        # word1 to word2
        def solve(ind1, ind2):

            if ind1 == n:
                return m-ind2
            if ind2 == m:
                return n-ind1

            if word1[ind1] == word2[ind2]:
                return 0+solve(ind1+1, ind2+1)
            else:
                # Insert, Delete, Replace
                insert = solve(ind1+1, ind2)
                delete = solve(ind1, ind2+1)
                replace = solve(ind1+1, ind2+1)
                return 1+min(insert, delete, replace)

        return solve(0, 0)


# Memoization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        # word1 to word2
        def solve(ind1, ind2):

            if ind1 == n:
                return m-ind2
            if ind2 == m:
                return n-ind1

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if word1[ind1] == word2[ind2]:
                dp[ind1][ind2] = 0+solve(ind1+1, ind2+1)

                return dp[ind1][ind2]
            else:
                # Insert, Delete, Replace
                insert = solve(ind1+1, ind2)
                delete = solve(ind1, ind2+1)
                replace = solve(ind1+1, ind2+1)

                dp[ind1][ind2] = 1+min(insert, delete, replace)

                return dp[ind1][ind2]
        return solve(0, 0)
