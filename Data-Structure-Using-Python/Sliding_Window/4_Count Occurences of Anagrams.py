# Count Occurences of Anagrams
# Anagrams = Rearranging

""" 
https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1

Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Example 1:
----------
Input:
txt = forxxorfxdofr
pat = for

Output: 3

Explanation: for, orf and ofr appears
in the txt, hence answer is 3.

Example 2:
----------
Input:
txt = aabaabaa
pat = aaba

Output: 4

Explanation: aaba is present 4 times
in txt. 
"""

from collections import Counter, defaultdict


class Solution:
    def search(self, pat, txt):
        # Window size will be the pat size
        k = len(pat)

        # txt size in which we have to search
        n = len(txt)

        # Count occurance as it is Anagram
        occurance = Counter(pat)

        c = 0
        i = j = 0
        check = defaultdict(lambda: 0)
        res = 0
        while j < n:
            c += 1
            check[txt[j]] += 1

            if c == k:
                flag = 0
                # Now check if the occurance are there or not
                for item in occurance:
                    if occurance[item] != check[item]:
                        flag = 1
                        break
                if flag == 0:
                    res += 1

                check[txt[i]] -= 1
                i += 1
                c -= 1

            j += 1
        return res


obj = Solution()

txt = 'forxxorfxdofr'
pat = 'for'

print(obj.search(pat, txt))
