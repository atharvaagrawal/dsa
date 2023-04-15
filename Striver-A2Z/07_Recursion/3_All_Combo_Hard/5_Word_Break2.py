""" 
https://practice.geeksforgeeks.org/problems/word-break-part-23249/1

https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of words dict of length n, add spaces in s to construct a sentence
where each word is a valid dictionary word. Each dictionary word can be used more than once. Return 
all such possible sentences.

Follow examples for better understanding.

Example 1:

Input: s = "catsanddog", n = 5
dict = {"cats", "cat", "and", "sand", "dog"}

Output: (cats and dog)(cat sand dog)

Explanation: All the words in the given
sentences are present in the dictionary.

Example 2:

Input: s = "catsandog", n = 5
dict = {"cats", "cat", "and", "sand", "dog"}

Output: Empty

Explanation: There is no possible breaking
of the string s where all the words are present
in dict.
"""


class Solution:
    def wordBreak(self, n, dict, s):
        # code here

        return


obj = Solution()
n = 5
dict = ["cats", "cat", "and", "sand", "dog"]
s = "catsanddog"
obj.wordBreak(n, dict, s)
