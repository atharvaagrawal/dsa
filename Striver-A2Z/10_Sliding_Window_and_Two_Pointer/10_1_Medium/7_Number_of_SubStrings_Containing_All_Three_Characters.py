""" 
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", 
"abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1 
"""
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        def atMost(k):
            if k < 0:
                return 0

            i = j = 0
            d = defaultdict(int)
            res = 0

            for j in range(len(s)):
                d[s[j]] += 1

                while len(d) > k:
                    d[s[i]] -= 1

                    if not d[s[i]]:
                        d.pop(s[i])

                    i += 1

                res += (j-i)+1
            return res

        return atMost(3) - atMost(2)
