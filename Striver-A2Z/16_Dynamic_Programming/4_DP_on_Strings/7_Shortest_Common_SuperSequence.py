# https://leetcode.com/problems/shortest-common-supersequence/description/

""" 
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. 
If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.


Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
"""


# Tabulation
class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:

        n = len(s1)
        m = len(s2)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j], dp[i][j-1])

        # Our DP Array Created

        ind1 = n
        ind2 = m

        le = dp[n][m]-1
        s = ''

        while ind1 > 0 and ind2 > 0:

            if s1[ind1-1] == s2[ind2-1]:
                s += s1[ind1-1]
                le -= 1
                ind1 -= 1
                ind2 -= 1

            elif dp[ind1-1][ind2] > dp[ind1][ind2-1]:
                s += s1[ind1-1]
                ind1 -= 1
            else:
                s += s2[ind2-1]
                ind2 -= 1

        # Adding Remaing Characters - Only one of the below two while loops will run
        while ind1 > 0:
            s += s1[ind1-1]
            ind1 -= 1

        while ind2 > 0:
            s += s2[ind2-1]
            ind2 -= 1

        return s[::-1]
