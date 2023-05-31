# https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1


""" 
Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing 
the value of coins required. 


Example 1:

Input: N = 43
Output: 20 20 2 1
Explaination: 
Minimum number of coins and notes needed 
to make 43. 

Example 2:

Input: N = 1000
Output: 500 500
Explaination: minimum possible notes
is 2 notes of 500.
"""


class Solution:
    def minPartition(self, N):
        coin = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]

        res = []
        value = N

        for i in range(len(coin)-1, -1, -1):
            while coin[i] <= value:
                res.append(coin[i])
                value -= coin[i]

        return res
