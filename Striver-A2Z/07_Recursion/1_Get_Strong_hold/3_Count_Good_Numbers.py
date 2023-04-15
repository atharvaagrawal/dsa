# https://leetcode.com/problems/count-good-numbers/

'''
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

Example 1:
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Example 2:
Input: n = 4
Output: 400

Example 3:
Input: n = 50
Output: 564908303
'''
# Iterative
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def check_good(num):
            num = [int(i) for i in str(num)]
            
            for i in range(len(num)):
                # Even indice
                if i%2 == 0:
                    if num[i]%2 != 0:
                        return False
                else:
                    # Odd Indice
                    prime_no = [2,3,5,7]
                    if num[i] not in prime_no:
                        return False
            return True
        
        cnt = 0 

        for i in range(10**n):
            if check_good(i):
                cnt+=1
            # print(i,end=' ')
        print(cnt)   
        return cnt     

from math import ceil,floor
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5,ceil(n/2),1000_000_007) * pow(4,floor(n/2),1000_000_007))% 1000_000_007


obj = Solution()
obj.countGoodNumbers(4)

        