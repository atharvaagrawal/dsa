""" 
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def solve(s,open,close):
            if open == 0  and close == 0:
                res.append(s)
                return 
            
            if open==close:
                s = s+'('
                open-=1
                solve(s,open,close)
            elif open == 0:
                s = s+')'
                close -=1
                solve(s,open,close)
            else:
                solve(s+')',open,close-1)
                solve(s+'(',open-1,close)
        
        solve('',n,n)
        print(res)

obj = Solution()
obj.generateParenthesis(3)
