# https://leetcode.com/problems/valid-parenthesis-string/

""" 
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true 

"""

# Solution
""" 
Intuition:
One pass on the string S,
we need to know,
how many ')' we are waiting for.

If we meet too many ')', we can return false directly.
If we wait for no ')' at the end, then we are good.


Explanation:
We count the number of ')' we are waiting for,
and it's equal to the number of open parenthesis.
This number will be in a range and we count it as [cmin, cmax]

cmax counts the maximum open parenthesis,
which means the maximum number of unbalanced '(' that COULD be paired.
cmin counts the minimum open parenthesis,
which means the number of unbalanced '(' that MUST be paired.


Example:
It's quite straight forward actually.
When you met "(", you know you need one only one ")", cmin = 1 and cmax = 1.
When you met "(*(", you know you need one/two/three ")", cmin = 1 and cmax = 3.

The string is valid for 2 condition:

cmax will never be negative.
cmin is 0 at the end.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        count_left = 0
        count_right = 0
        count_any = 0

        cmin = cmax = 0

        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            elif i == ')':
                cmax -= 1
                cmin -= 1
            elif i == '*':
                cmax += 1
                cmin -= 1
                # cmax++;  if `*` become `(` then openCount++
                # cmin--;  if `*` become `)` then openCount--
                # if `*` become `` then nothing happens
                # So openCount will be in new range [cmin-1, cmax+1]

            if cmax < 0:
                return False

            cmin = max(cmin, 0)

        return cmin == 0
