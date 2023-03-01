# https://leetcode.com/problems/pascals-triangle/description/
class Solution:
    def generate(self, numRows):

        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        l = [[1],[1,1]]
        
        for i in range(2,numRows):
            l1 = [1]
            ind = 0
            for j in range(i-1):
                num = l[i-1][ind] + l[i-1][ind+1]
                ind+=1
                l1.append(num)
            l1.append(1)
            
            l.append(l1)
            
        return l