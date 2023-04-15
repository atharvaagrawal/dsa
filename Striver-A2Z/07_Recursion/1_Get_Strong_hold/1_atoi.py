# https://leetcode.com/problems/string-to-integer-atoi/description/

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

""" 
Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
"""

class Solution:
    def myAtoi(se, s: str) -> int:
        su,num,flag = 1,0,0

        s = s.strip()

        if len(s) == 0:
            return 0
        
        if s[0] == "-":
            su = -1

        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
                flag = 1
            elif (i == "+" or i == "-") and (flag == 0):
                flag = 1
                pass
            else: 
                break
                
        num = num*su
        
        if (-2**31<=num<=(2**31)-1):
            return num
        
        if num<0:
            return -2**31
        else:
            return 2**31-1

obj = Solution()
print(obj.myAtoi("42"))
