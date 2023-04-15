# https://leetcode.com/problems/combination-sum/

""" 
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def solve(ind,tar,l):
            if ind == n:
                if tar == 0:
                    res.append(l.copy())
                return

            if candidates[ind] <= tar:
                # print(ind,tar,l)
                l.append(candidates[ind])
                solve(ind,tar-candidates[ind],l)
                l.pop()
                solve(ind+1,tar,l)  
            else:
                solve(ind+1,tar,l)
        l = []
        solve(0,target,l)

        return res