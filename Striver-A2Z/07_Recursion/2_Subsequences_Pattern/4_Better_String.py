# https://practice.geeksforgeeks.org/problems/better-string/1

""" 
Given a pair of strings, Geek wants to find the better string. The better string is the string having more number of distinct subsequences.

If both the strings have equal count of distinct subsequence then return str1. 

Input:
str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 7 distinct subsequences whereas "ggg" have 4 distinct subsequences. 


Input: str1 = "a", str2 = "b"
Output: "a"
Explanation: Both the strings have only 1 distinct subsequence.
"""

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         def solve(ind,op):
#             if ind == n:
#                 res.append(op.copy())
#                 return

#             op.append(nums[ind])
#             solve(ind+1,op)
#             op.pop()
#             solve(ind+1,op)

#         solve(0,[])
#         # print(res)
#         return res

# TLE    
class Solution:
    def betterString(self, str1, str2):
        
        def solve(ind,op,n,cnt,str):
            if ind == n:
                cnt.add(op)
                # print(op,str,cnt)
                return 
            
            op = op + str[ind]
            solve(ind+1,op,n,cnt,str)
            
            op = op[:-1]
            solve(ind+1,op,n,cnt,str)

        cnt1 = set()
        # cnt1.append(0)
        solve(0,'',len(str1),cnt1,str1)
        
        cnt2 = set()
        # cnt2.append(0)
        solve(0,'',len(str2),cnt2,str2)
        print(cnt1,cnt2)
        cnt1 = len(cnt1)
        cnt2 = len(cnt2)

        print(cnt1,cnt2)
        if cnt1 == cnt2:
            return str1
        elif cnt1 < cnt2:
            return str2
        return str1 

obj = Solution()
str1 = "gfg"
str2 = "ggg"
print(obj.betterString(str1,str2))



