""" 
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other 
uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        j = 0

        # Similar to Max Consecutive Ones 111

        # Traverse to window
        count = defaultdict(int)
        res = 0
        most_freq = 0

        for j in range(len(s)):
            # Store the count
            count[s[j]] += 1

            most_freq = max(most_freq, count[s[j]])

            # Window Len
            window_len = j - i + 1

            if window_len - most_freq > k:
                # Window Invalid
                # Shift i (left pointer)
                while window_len-most_freq > k:
                    count[s[i]] -= 1
                    i += 1
                    window_len = j - i + 1
                    most_freq = max(count.values())

            res = max(res, window_len)

        return res
