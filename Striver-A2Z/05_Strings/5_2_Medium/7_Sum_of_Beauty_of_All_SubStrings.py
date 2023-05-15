# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/

""" 
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 
Example 1:
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

Example 2:
Input: s = "aabcbaa"
Output: 17
"""

from collections import defaultdict


class Solution:

    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(n):
            d = defaultdict(int)

            for j in range(i, n):
                d[s[j]] += 1

                most_freq = 0
                least_freq = float('inf')

                for key in d.keys():
                    most_freq = max(most_freq, d[key])
                    least_freq = min(least_freq, d[key])

                ans += (most_freq-least_freq)

        return ans


# Better Solution


class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(n):
            m = defaultdict(int)
            st = []

            for j in range(i, n):
                if s[j] in m:
                    st.remove(m[s[j]])

                m[s[j]] += 1
                st.append(m[s[j]])

                ans += max(st) - min(st)

        return ans
