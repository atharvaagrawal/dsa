# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1

""" 
A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
Follow Up: Can you optimize it to O(N)
 

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 

Example 2:

Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.
 """


class Solution:

    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):

        def knows(a, b):
            if M[a][b] == 1:
                return True
            else:
                return False

        stack = []

        # Push all element inside stack
        for i in range(n):
            stack.append(i)

        while len(stack) > 1:
            a = stack[-1]
            stack.pop()

            b = stack[-1]
            stack.pop()

            if knows(a, b):
                stack.append(b)
            else:
                stack.append(a)

        candidate = stack[-1]

        # Check Row
        rowCheck = False
        colCheck = False
        zeroCount = 0
        oneCount = 0

        for i in range(n):
            if M[candidate][i] == 0:
                zeroCount += 1

            if M[i][candidate] == 1:
                oneCount += 1

        if zeroCount == n:
            rowCheck = True
        if oneCount == n-1:
            colCheck = True

        if colCheck and rowCheck:
            return candidate

        return -1
