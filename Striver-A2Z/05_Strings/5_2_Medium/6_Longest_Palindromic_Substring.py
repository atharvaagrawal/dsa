# https://leetcode.com/problems/longest-palindromic-substring/description/

""" 
Given a string s, return the longest 
palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right-left-1
        start = end = 0

        for i in range(len(s)):

            odd = expand(s, i, i)
            even = expand(s, i, i+1)

            length = max(odd, even)

            if length > end-start:
                # Even length (6) -> 2  start--> i-2, end --> i+3
                # Odd len (5) -> 2 start i-2, end -> i+2
                start = i - (length-1)//2

                end = i + length//2

        return s[start:end+1]
