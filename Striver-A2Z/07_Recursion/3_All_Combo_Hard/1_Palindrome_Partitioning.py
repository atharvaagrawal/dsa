""" 
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome 
.Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]] 
"""
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(s):
            if s == s[::-1]:
                return True
            return False
        
        def solve(ind,l):
            if ind == n:
                res.append(l.copy())
                return  

            for i in range(ind,n):
                pad = s[ind:i+1]
                if isPalindrome(pad):    
                    l.append(pad)
                    solve(i+1,l)
                    l.pop()        

        solve(0,[])

        return res