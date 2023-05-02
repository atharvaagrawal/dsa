# First Completely Painted Row or Column

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0]*m
        cols = [0]*n
        loc = {}

        for i in range(m):
            for j in range(n):
                loc[mat[i][j]] = (i, j)

        for k, x in enumerate(arr):
            # print(k,x)
            i, j = loc[x]

            rows[i] += 1
            cols[j] += 1

            if rows[i] == n or cols[j] == m:
                return k
