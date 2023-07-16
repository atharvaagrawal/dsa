# https://www.codingninjas.com/studio/problems/longest-common-substring_1235207


from os import *
from sys import *
from collections import *
from math import *


def lcs(s1, s2):

    n = len(s1)
    m = len(s2)
    dp = [[-1] * (m+1) for _ in range(n+1)]

    def solve(ind1, ind2):
        if ind1 == n or ind2 == m:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        ans = float('-inf')
        if s1[ind1] == s2[ind2]:
            ans = 1 + solve(ind1+1, ind2+1)
        else:
            ans = 0

        solve(ind1+1, ind2)
        solve(ind1, ind2+1)

        dp[ind1][ind2] = ans

        return dp[ind1][ind2]

    solve(0, 0)

    ans = float('-inf')

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            ans = max(dp[i][j], ans)

    return ans
