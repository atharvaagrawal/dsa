# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
""" 
Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

Example 1:
Input:
S = "aabacbebebe", K = 3
Output: 7
Explanation: "cbebebe" is the longest 
substring with K distinct characters.

Example 2:
Input: 
S = "aaaa", K = 2
Output: -1
Explanation: There's no substring with K
distinct characters. 
"""

from collections import defaultdict


class Solution:
    def longestKSubstr(self, s, k):

        i = j = 0
        d = defaultdict(int)

        total = 0
        res = 0

        for j in range(len(s)):
            d[s[j]] += 1
            total += 1
            # print(d, j, i)
            while len(d) > k:
                d[s[i]] -= 1

                if d[s[i]] == 0:
                    d.pop(s[i])
                # print(d, s[i], i, j)
                i += 1
                total -= 1

            if len(d) == k:
                res = max(res, total)

        if res == 0:
            return -1

        return res


obj = Solution()

s = "aabacbebebe"
k = 3

print(obj.longestKSubstr(s, k))
