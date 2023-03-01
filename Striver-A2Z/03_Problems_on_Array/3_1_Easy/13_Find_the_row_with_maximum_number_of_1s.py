# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

""" Given a boolean 2D array of n x m dimensions where each row is sorted. 
Find the 0-based index of the first row that has the maximum number of 1's.

N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based indexing).
 """
def rowWithMax1s(self,arr, n, m):    
    ct = 0
    res = 0
    rowNum = -1
    
    for i in range(n):
       
        for j in range(m):
            if arr[i][j] == 1:
                # whenever first 1 found
                ct = m - j
                if res < ct:
                    res = ct
                    rowNum = i
                break
    
        if res == m:
            return rowNum
            
    return rowNum
