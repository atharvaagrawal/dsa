""" 
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

from typing import List


# DP
class Solution:
    def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break

        return dp[0]


# Doesn't Work for all test case

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # s = start_index
#         # e = end_index

#         n = len(s)

#         def solve(sind, eind):
#             if sind == n:
#                 print('n')
#                 return True
#             if eind == n:
#                 return False
#             substr = s[sind:eind+1]
#             print(substr, sind, eind+1)
#             if substr in wordDict:
#                 return solve(eind+1, eind+1)
#             else:
#                 return solve(sind, eind+1)

#         print(solve(0, 0))


obj = Solution()

s = "applepenapple"
wordDict = ["apple", "pen"]

s = "leetcode"
wordDict = ["leet", "code"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]

obj.wordBreak(s, wordDict)
