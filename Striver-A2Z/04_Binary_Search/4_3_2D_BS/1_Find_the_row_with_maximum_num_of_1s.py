# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

""" 
Given a boolean 2D array of n x m dimensions where each row is sorted. 
Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input: 
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input: 
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).
"""


class Solution:

    def rowWithMax1s(self, arr, n, m):
        # code here
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


class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here

        def binarySearch(row):
            low = 0
            high = m-1
            ans = -1
            
            while low <= high:
                
                mid = (low+high)//2
                
                if arr[row][mid] == 1:
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            
            if ans == -1:
                return 0
            
            
            return m-ans
        
        maxi = 0
        row = -1
        
        
        for i in range(n):
            
            ans = binarySearch(i)
            
            if ans > maxi:
                maxi = ans
                row = i
        
        return row