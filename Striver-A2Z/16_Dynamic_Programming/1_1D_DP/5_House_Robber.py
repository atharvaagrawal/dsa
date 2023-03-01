""" 
Stickler the thief wants to loot money from a society having n houses in a single line. 
He is a weird person and follows a certain rule when looting the houses. According to the rule, 
he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots.
The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy.
He asks for your help to find the maximum money he can get if he strictly follows the rule. Each house has a[i]amount
of money present in it.

Example 1:
Input:
n = 6
a[] = {5,5,10,100,10,5}
Output: 110
Explanation: 5+100+5=110

Example 2:
Input:
n = 3
a[] = {1,2,3}
Output: 4
Explanation: 1+3=4
"""

""" 
Recursion
class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        sum = 0

        def find(a,n):
            if n == 0:
                return a[n]
            
            if n < 0:
                return 0

            pick = a[n] + find(a,n-2)
            not_pick = 0 + find(a,n-1)
        
            return max(pick,not_pick)
        
        print("Max Loot:",find(a,n-1))
"""

# Memorization
class Solution:  
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        sum = 0
        dp = [-1]*n

        def find(a,n):
            if n == 0:
                return a[n]
            
            if n < 0:
                return 0

            if dp[n] != -1:
                return dp[n]

            pick = a[n] + find(a,n-2)
            not_pick = 0 + find(a,n-1)
        
            dp[n] = max(pick,not_pick)
            
            return dp[n]
        
        print("Max Loot:",find(a,n-1))

obj = Solution()
a = [5,5,10,100,10,5]
# a = [1,2,3]
# a = [10]
n = len(a)
obj.FindMaxSum(a,n) 