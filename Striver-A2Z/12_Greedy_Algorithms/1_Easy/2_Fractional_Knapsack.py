# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

""" 

Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

Note: Unlike 0/1 knapsack, you are allowed to break the item. 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 


Example 2:

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
"""


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w
        self.perunit = 0


class Solution:
    def fractionalknapsack(self, W, arr, n):

        # Single Unit Weight
        for item in arr:
            item.perunit = item.value / item.weight

        arr.sort(key=lambda x: x.perunit, reverse=True)

        res = 0

        total_weight = W
        for item in arr:
            if total_weight == 0:
                break
            if total_weight >= item.weight:
                res += item.value
                total_weight -= item.weight
            else:
                res += (total_weight)*item.perunit
                break

        return res
