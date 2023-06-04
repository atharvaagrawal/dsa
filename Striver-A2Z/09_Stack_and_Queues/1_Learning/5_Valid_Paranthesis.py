# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        l = [i for i in s]

        stack = []

        closing_tags = [']', '}', ')']

        for i in l:
            if i in closing_tags:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if i == '}' and temp == '{':
                    continue
                elif i == ')' and temp == '(':
                    continue
                elif i == ']' and temp == '[':
                    continue
                else:
                    return False

            stack.append(i)
        if len(stack) > 0:
            return False
        return True
