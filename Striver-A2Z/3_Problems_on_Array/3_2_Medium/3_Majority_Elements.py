# https://leetcode.com/problems/majority-element/description/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Boyer Moore’s Voting Algorithm

from collections import Counter

def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1
            
        c = Counter(nums)
        res = dict(c.most_common(n//2))
        
        
        for k in res.keys():
            return k    