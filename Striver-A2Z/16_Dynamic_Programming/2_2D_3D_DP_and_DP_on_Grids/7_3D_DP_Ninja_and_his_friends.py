'''
We are given an ‘N*M’ matrix. Every cell of the matrix has some chocolates on it, mat[i][j] gives us the number of chocolates. 
We have two friends ‘Alice’ and ‘Bob’. initially, Alice is standing on the cell(0,0) and Bob is standing on the cell(0, M-1). 
Both of them can move only to the cells below them in these three directions: to the bottom cell (↓), 
to the bottom-right cell(↘), or to the bottom-left cell(↙).

When Alica and Bob visit a cell, they take all the chocolates from that cell with them. 
It can happen that they visit the same cell, in that case, the chocolates need to be considered only once.
They cannot go out of the boundary of the given matrix, we need to return the maximum number of chocolates that Bob 
and Alice can together collect.


Input: 'R' = 3, 'C' = 4
'GRID' = [[2, 3, 1, 2], [3, 4, 2, 2],
[5, 6, 3, 5]]

Output: 21

Initially Alice is at the position (0,0) he can follow the path (0,0) -> (1,1) -> (2,1) and
will collect 2 + 4 + 6 = 12 chocolates.

Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1,3) -> (2, 3)
and will colllect 2 + 2 + 5 = 9 chocolates.

Hence the total number of chocolates collected will be 12 + 9 = 21. there is no other possible
way to collect a greater number of chocolates than 21.
'''

# Recursion 
class Solution:
    def solve(self, n, m, grid):
        
        def rec(i,j1,j1):
            # Base Case

            if j1 < 0 || j2 < 0 || j1 > m || j2 > m:
                return -int(1e8)

            if i == n-1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]
            
            # Alice and Bob 9 Combination    
            maxi = 0

            for dj1 in [-1,0,1]:
                for dj2 in [-1,0,1]:
                    if j1 == j2:
                        maxi = max(maxi, grid[i][j1] + rec(i+1,j1+dj1,j2+dj2))
                    else:
                        maxi = max(maxi, grid[i][j1]+ grid[i][j2] + rec(i+1,j1+dj1,j2+dj2))
            
            return maxi
                        
        print( rec(0,0,m-1) )

r = 3
c = 4
grid = [[2, 3, 1, 2], 
        [3, 4, 2, 2],
        [5, 6, 3, 5]]

obj = Solution()
obj.solve(r,c,grid)

        