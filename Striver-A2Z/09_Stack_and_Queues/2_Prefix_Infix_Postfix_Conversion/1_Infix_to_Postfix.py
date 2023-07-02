# https://practice.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
""" 
Given an infix expression in the form of string str. Convert this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. 
Example 1:

Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be abcd^e-fgh*+^*+i-

Example 2:

Input: str = "A*(B+C)/D"
Output: ABC+*D/
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be ABC+*D/
 """


class Solution:

    # Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        # code here

        stack = []
        precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

        res = []
        for ele in exp:
            print(ele, stack, res)
            if ele == '(':
                stack.append(ele)
            elif ele in precedence:
                if stack and stack[-1] == '(':
                    stack.append(ele)
                else:
                    while stack and stack[-1] != '(' and precedence[ele] <= precedence[stack[-1]]:
                        res.append(stack[-1])
                        stack.pop()
                    stack.append(ele)
            elif ele == ')':
                while stack and stack[-1] != '(':
                    res.append(stack[-1])
                    stack.pop()
                stack.pop()
            else:
                res.append(ele)

        while stack:
            res.append(stack[-1])
            stack.pop()

        return ''.join(res)


ob = Solution()
str = "a+b*(c^d-e)^(f+g*h)-i"
print(ob.InfixtoPostfix(str))
