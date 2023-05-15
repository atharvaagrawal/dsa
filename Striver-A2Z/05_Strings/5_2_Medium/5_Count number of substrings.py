# https://practice.geeksforgeeks.org/problems/count-number-of-substrings4528/1

""" 
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) 
that have exactly k distinct characters. 


Example 1:
Input:
S = "aba", K = 2
Output:
3
Explanation:
The substrings are:
"ab", "ba" and "aba".

Example 2:

Input: 
S = "abaaca", K = 1
Output:
7
Explanation:
The substrings are:
"a", "b", "a", "aa", "a", "c", "a".  
"""


class Solution:
    def most_k_chars(self, s, k):
        if not s:
            return 0

        char_count = {}

        num = 0
        left = 0

        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    char_count.pop(s[left])
                left += 1

            num += i - left + 1

        return num

    def substrCount(self, s, k):
        return self.most_k_chars(s, k) - self.most_k_chars(s, k - 1)
