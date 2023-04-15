# https://practice.geeksforgeeks.org/problems/generate-all-binary-strings/1

""" 
Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.

A binary string is that string which contains only 0 and 1.

Example 1:

Input:
N = 3
Output:
000 , 001 , 010 , 100 , 101
Explanation:
None of the above strings contain consecutive 1s. "110" is not an answer as it has '1's occuring consecutively. 
"""

class Solution:
    def generateBinaryStrings(self, n):
        # Approach: take or not take        
        l = ['0','1']
        res = []
        
        def solve(l,n):
            if n == 0:
                return l
            
            res = []
            for i in range(len(l)):
                ele = l[i]

                ele1 = l[i]+'0'
                res.append(ele1)

                if ele[-1] != '1':
                    ele2 = l[i] + '1'
                    res.append(ele2)
            print(res)
            return solve(res,n-1)

        return solve(l,n)
        

"""     # Count All Binary Strings without Zeros
    def countBinaryStrings(self, n):
        
        # Approach: take or not take        
        def solve():                
            pass
        
        res = []
        l = [0 for i in range(n)]
        solve(n)      """

obj = Solution()
obj.generateBinaryStrings(4)