# https://practice.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1

# https://www.youtube.com/watch?v=MJzZgHFc00U

""" 
Given an integer array. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to the size of the Array.

Example 1:

Input:
N = 7
arr[] = {10,20,30,50,10,70,30}
Output: 70 30 20 10 10 10 10 
Explanation: 
1.First element in output
indicates maximum of minimums of all
windows of size 1.
2.Minimums of windows of size 1 are {10},
 {20}, {30}, {50},{10}, {70} and {30}. 
 Maximum of these minimums is 70. 
3. Second element in output indicates
maximum of minimums of all windows of
size 2. 
4. Minimums of windows of size 2
are {10}, {20}, {30}, {10}, {10}, and
{30}.
5. Maximum of these minimums is 30 
Third element in output indicates
maximum of minimums of all windows of
size 3. 
6. Minimums of windows of size 3
are {10}, {20}, {10}, {10} and {10}.
7.Maximum of these minimums is 20. 
Similarly other elements of output are
computed.
Example 2:

Input:
N = 3
arr[] = {10,20,30}
Output: 30 20 10
Explanation: First element in output
indicates maximum of minimums of all
windows of size 1.Minimums of windows
of size 1 are {10} , {20} , {30}.
Maximum of these minimums are 30 and
similarly other outputs can be computed
"""


class Solution:

    # Function to find maximum of minimums of every window size.
    def maxOfMin(self, arr, n):

        right_smaller = [-1]*n
        left_smaller = [-1]*n
        res = [0]*(n+1)
        min_in_length = [-1]*n

        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                left_smaller[stack[-1]] = i
                stack.pop()

            stack.append(i)

        while stack:
            left_smaller[stack[-1]] = -1
            stack.pop()

        stack = []

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                right_smaller[stack[-1]] = i
                stack.pop()

            stack.append(i)

        while stack:
            right_smaller[stack[-1]] = n
            stack.pop()

        for i in range(n):
            min_in_length[i] = right_smaller[i] - left_smaller[i] - 1

        for i in range(n):
            res[min_in_length[i]] = max(res[min_in_length[i]], arr[i])

        for i in range(n-1, -1, -1):
            res[i] = max(res[i], res[i+1])

        return res[1:]
