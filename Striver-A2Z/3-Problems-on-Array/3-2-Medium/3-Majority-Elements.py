# https://leetcode.com/problems/majority-element/description/

from collections import Counter

def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1
            
        c = Counter(nums)
        res = dict(c.most_common(n//2))
        
        
        for k in res.keys():
            return k    