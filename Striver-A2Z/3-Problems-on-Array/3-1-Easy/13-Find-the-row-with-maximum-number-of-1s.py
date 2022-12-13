# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1
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
