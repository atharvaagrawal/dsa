""" 
Max Sum without Adjacents

Given an array Arr of size N containing positive integers. Find the maximum sum of a 
subsequence such that no two numbers in the sequence should be adjacent in the array.

Example 1:

Input:
N = 6
Arr[] = {5, 5, 10, 100, 10, 5}

Output: 110

Explanation: If you take indices 0, 3
and 5, then Arr[0]+Arr[3]+Arr[5] =
5+100+5 = 110. 
"""

""" 
# Using Recursion
class Solution:
    def findMaxSum(self,arr, n):      
          
        def adjacent(arr,n):
            if n == 0:
                return arr[n]
            
            if n < 0:
                return 0
            
            pick = arr[n] + adjacent(arr,n-2) 
            not_pick = 0 + adjacent(arr,n-1) 

            return max(pick,not_pick)
        
        print("Max Sum:",adjacent(arr,n-1))
"""

""" 
# Using Memorization
class Solution:
    def findMaxSum(self,arr, n):      
        
        dp = [-1]*n

        def adjacent(arr,n):
            if n == 0:
                return arr[n]

            if n < 0:
                return 0

            if dp[n] != -1:
                return dp[n]
                        
            pick = arr[n] + adjacent(arr,n-2) 
            not_pick = 0 + adjacent(arr,n-1) 

            dp[n] = max(pick,not_pick)

            return dp[n]    
        print("Max Sum:",adjacent(arr,n-1))
"""

# Using Tabulation
class Solution:
    def findMaxSum(self,arr, n):      
        
        if n == 1:
            return arr[0]

        dp = [-1]*n
        dp[0] = arr[0]
        dp[1] = arr[1]

        for i in range(2,n):
            pick = dp[i-2] + arr[i]
            not_pick = dp[i-1] + 0
            dp[i] = max(pick,not_pick)
        
        print("Max Sum:",dp[n-1])

obj = Solution()
arr = [5, 5, 10, 100, 10, 5]
n = len(arr)

obj.findMaxSum(arr,n)

""" 
# Space Optimized Code

def solve(n, arr):
    prev = arr[0]
    prev2 = 0
    
    for i in range(1, n):
        pick = arr[i]
        if i > 1:
            pick += prev2
        non_pick = 0 + prev
        
        cur_i = max(pick, non_pick)
        prev2 = prev
        prev = cur_i
        
    return prev

def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    print(solve(n, arr))

if __name__ == "__main__":
    main() 
"""