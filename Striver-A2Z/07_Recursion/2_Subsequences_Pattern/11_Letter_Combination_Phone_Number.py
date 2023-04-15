# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number


""" 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        num_map = {2:['a','b','c'],
                   3: ['d','e','f'],
                   4: ['g','h','i'],
                   5: ['j','k','l'],
                   6: ['m','n','o'],
                   7: ['p','q','r','s'],
                   8: ['t','u','v'],
                   9: ['w','x','y','z']}
        
        n = len(digits)
        d = [int(i) for i in digits]
        # print(d)

        def solve(ind,s,n):
            if n == 0:
                res.append(s)
                return 

            for i in num_map[d[ind]]:
                s = s+i
                # print(s)
                solve(ind+1,s,n-1)
                s = s[:-1]
        if n == 0:
            return []

        solve(0,'',n)
        # print(res)
        return res
    
obj = Solution()
digits = "23"
digits = "456"
digits = ""
obj.letterCombinations(digits)    
