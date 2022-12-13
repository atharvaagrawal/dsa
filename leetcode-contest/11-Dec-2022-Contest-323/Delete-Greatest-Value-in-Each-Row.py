# https://leetcode.com/contest/weekly-contest-323/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans =  0
        m = []
        idx = -1
        
        while len(grid[0]) > 0:
            m = []
            
            for i in range(len(grid)): #row
                m1 = 0
                idx = -1
                
                for j in range(len(grid[i])): #col
                    if grid[i][j] > m1:
                        idx = j
                        m1 = grid[i][j]
                        
                    # m1 = max(grid[i][j],m1)
                
                m.append(m1)
                if idx != -1:
                    del grid[i][idx]
            ans += max(m)
            
            # print(grid,ans)
        return ans            
            