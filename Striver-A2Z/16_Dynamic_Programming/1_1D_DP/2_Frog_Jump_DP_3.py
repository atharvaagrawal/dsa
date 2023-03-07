"""  
 Geek wants to climb from the 0th stair to the (n-1)th stair. At a time the Geek can climb either one or two steps. 
 A height[N] array is also given. Whenever the geek jumps from stair i to stair j, the energy consumed in the jump 
 is abs(height[i]- height[j]), where abs() means the absolute difference. return the minimum energy that can be used 
 by the Geek to jump from stair 0 to stair N-1. 

Example:
    Input:
        n = 4
        height = {10 20 30 10}
    Output:
        20
Explanation:
Geek jump from 1st to 2nd stair(|20-10| = 10 energy lost).
Then a jump from the 2nd to the last stair(|10-20| = 10 energy lost).
so, total energy lost is 20 which is the minimum
"""

""" 
Input: 30 10 60 10 60 50 

30-10 = 20
10-10 = 0
10-50 = 40
--------
20+40 = 60
Greedy Approach ans:50
------------------------
30-60 = 30
60-60 = 0
60-50 = 10
--------
30+10 = 40
using dp ans = 40
------------------------

class Solution:
    def minimumEnergy(self, height, n):
        lost = 0
        i = 0 #stair
        
        while i < n-1:
            print(i)
            if(abs(height[i] - height[i+1]) <  abs(height[i] - height[i+2])):
                lost += abs(height[i] - height[i+1])
                i+=1
            else:
                lost += abs(height[i] - height[i+2])
                i+=2
                
        if i == n-2:
            lost += abs(height[i] - height[i+1])
        elif i == n-3:
            lost += min(abs(height[i] - height[i+1]) , abs(height[i] - height[i+2]))
        
        return lost
 """

""" 
import sys
import math

def solve(ind, height, dp):
    if ind == 0:
        return 0

    if dp[ind] != -1:
        return dp[ind]

    jumpTwo = sys.maxsize
    jumpOne = solve(ind-1, height, dp) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jumpTwo = solve(ind-2, height, dp) + abs(height[ind] - height[ind-2])
    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print(solve(n-1, height, dp))
"""    
""" 
Memorization DP
class Solution:
    def minimumEnergy(self, height, n):
        dp = [-1 for i in range(n+1)]
        
        # Memorization DP top down
        def minE(height,n):
            if n <= 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            left = minE(height,n-1) + abs(height[n]-height[n-1])
            right = float('inf')
            
            if n > 1:   
                right = minE(height,n-2) + abs(height[n]-height[n-2])
            
            dp[n] =  min(left,right)
            
            return dp[n]
            
        return minE(height,n-1)  
"""

# Tabulation  
class Solution:
    def minimumEnergy(self, height, n):
        dp = [-1 ]*n
        print(len(dp))
        dp[0] = 0
        
        for i in range(1,n):
            oneJump = dp[i-1] + abs(height[i]-height[i-1])
            twoJump = float('inf')
            if i > 1:
                twoJump = dp[i-2] + abs(height[i]-height[i-2])
            
            dp[i] = min(oneJump,twoJump)
        return dp[n-1]

obj = Solution()
height = [10,20,30,10]
n = len(height)
obj.minimumEnergy(height,n)

""" 
Space Optimization Way:

import sys
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    prev = 0
    prev2 = 0
    for i in range(1, n):
        jumpTwo = sys.maxsize
        jumpOne = prev + abs(height[i] - height[i - 1])
        if i > 1:
            jumpTwo = prev2 + abs(height[i] - height[i - 2])

        cur_i = min(jumpOne, jumpTwo)
        prev2 = prev
        prev = cur_i

    print(prev)

if __name__ == "__main__":
    main() 
"""