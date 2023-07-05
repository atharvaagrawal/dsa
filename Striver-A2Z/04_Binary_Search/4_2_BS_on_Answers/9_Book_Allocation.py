# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

""" 
You have N books, each with Ai number of pages. M students need to be allocated contiguous 
books, with each student getting at least one book. Out of all the permutations, the goal 
is to find the permutation where the student with the most pages allocated to him gets 
the minimum number of pages, out of all possible permutations.

Note: Return -1 if a valid assignment is not possible, and allotment should be in 
contiguous order (see the explanation for better understanding).

 

Example 1:

Input:
N = 4
A[] = {12,34,67,90}
M = 2
Output:113
Explanation:Allocation can be done in 
following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90} Maximum Pages =113.
Therefore, the minimum of these cases is 113,
which is selected as the output.

Example 2:

Input:
N = 3
A[] = {15,17,20}
M = 2
Output:32
Explanation: Allocation is done as
{15,17} and {20}
"""


class Solution:

    # Function to find minimum number of pages.
    def findPages(self, A, N, M):
        # code here

        if M > N:
            return -1

        def check(pages):
            stud = 1
            stud_pages = 0

            for i in range(N):
                if stud_pages+A[i] <= pages:
                    stud_pages += A[i]
                else:
                    stud += 1
                    stud_pages = A[i]

            return stud

        low = max(A)
        high = sum(A)

        ans = float('inf')

        while low <= high:

            mid = (low+high)//2

            # Number of Student is greater than M so we have to include
            # More Pages and Check
            if check(mid) > M:
                low = mid + 1
            else:
                high = mid - 1

        return low
