# Longest Substring Without Repeating Characters
""" 
Given a string s, find the length of the longest  substring
without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        starting_point = 0
        pointer = 0
        global_max = 0
        key_value = {}

        for char in s:
            if char in key_value:
                starting_point = max(starting_point, key_value[char]+1)

            key_value[char] = pointer
            global_max = max(global_max, (pointer-starting_point)+1)
            pointer += 1

        return global_max
