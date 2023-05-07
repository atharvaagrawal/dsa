""" 
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        i = j = 0
        t_count = Counter(t)
        c = len(t)

        res = ""
        res_c = float('inf')

        for j in range(len(s)):
            print(c, i, j)
            if s[j] in t_count:
                t_count[s[j]] -= 1
                c -= 1

            if c == 0:
                if res_c > (j-i+1):
                    res = s[i:j+1]

                    res_c = j-i+1

            while c < 0:
                if s[i] in t_count:
                    t_count[s[i]] += 1
                    c += 1
                i += 1
            print(t_count)
        print(c, i, j)
        print(t_count)
        return res
