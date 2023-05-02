""" 
https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1

Given an array A[] of size N and a positive integer K, find the first negative integer for each 
and every window(contiguous subarray) of size K.

Example 1:
Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6

Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0  
"""


def printFirstNegativeInteger(A, N, K):
    i = j = 0

    # 12, -1, -7, 8, -15, 30, 16, 28

    res = []
    c = 0
    neg = []

    while j < N:
        c += 1

        if A[j] < 0:
            neg.append(j)

        if c == K:
            val = 0
            i += 1
            if len(neg) > 0:
                ind = neg[0]
                val = A[ind]
                if ind < i:
                    neg.pop(0)
            res.append(val)
            c -= 1
        j += 1
    return res


A = [12, -1, -7, 8, -15, 30, 16, 28]

N = 8
K = 3

print(printFirstNegativeInteger(A, N, K))
