# https://practice.geeksforgeeks.org/problems/bit-manipulation-1666686020/1

""" 
Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 

1. Get ith bit

2. Set ith bit

3. Clear ith bit

Note : For better understanding, we are starting bits from 1 instead 0. (1-based)

Example 1:

Input: 70 3
Output: 1 70 66
Explanation: Bit at the 3rd position from LSB is 1. (1 0 0 0 1 1 0)
The value of the given number after setting the 3rd bit is 70. 
The value of the given number after clearing 3rd bit is 66. (1 0 0 0 0 1 0)

Example 2:

Input: 8 1
Output: 0 9 8
Explanation: Bit at the first position from LSB is 0. (1 0 0 0)
The value of the given number after setting the 1st bit is 9. (1 0 0 1)
The value of the given number after clearing 1st bit is 8. (1 0 0 0)
"""


class Solution:
    def bitManipulation(self, n, i):
        getbit = 1 if n & (1 << (i-1)) else 0

        setbit = n | (1 << (i-1))

        clearbit = n & ~(1 << (i-1))

        print(getbit, setbit, clearbit, end="")
