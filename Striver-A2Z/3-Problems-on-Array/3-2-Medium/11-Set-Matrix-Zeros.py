# https://leetcode.com/problems/set-matrix-zeroes/submissions/811526213/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        row_l = list(row)
        col_l = list(col)
        
        for i in range(len(row_l)):
            for j in range(len(matrix[0])):
                matrix[ row_l[i] ][j] = 0
        
        for i in range(len(col_l)):
            for j in range(len(matrix)):
                matrix[j][col_l[i]] = 0
        
        print(matrix)   