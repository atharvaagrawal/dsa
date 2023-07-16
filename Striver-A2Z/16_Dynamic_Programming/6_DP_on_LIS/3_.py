# https://www.codingninjas.com/studio/problems/longest-common-substring_1235207

# A substring of a string is a subsequence in which all the characters are consecutive.
# Given two strings, we need to find the longest common substring.


# Tabulation
def lcs(s1, s2):

    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                val = 1 + dp[i - 1][j - 1]
                dp[i][j] = val
                ans = max(ans, val)
            else:
                dp[i][j] = 0

    return ans
