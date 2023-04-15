""" 
https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

Consider a rat placed at(0, 0) in a square matrix of order N * N. It has to reach the destination at(N - 1, N - 1).
 Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat
 can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is 
 blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.

Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other 
cell.


Example 1:
Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR

Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.

Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1

Explanation:
No path exists and destination cell is 
blocked.
"""


class Solution:
    def findPath(self, m, n):
        # code here
        res = []

        if m[n-1][n-1] == 0:
            return -1

        def solve(i, j, s):
            # print(i, j, s)
            if i >= n or j >= n or i < 0 or j < 0:
                return

            if i == n-1 and j == n-1:
                res.append(s)
                return

            if m[i][j] == 0:
                return

            val = m[i][j]
            m[i][j] = 0

            solve(i+1, j, s+'D')
            solve(i-1, j, s+'U')
            solve(i, j+1, s+'R')
            solve(i, j-1, s+'L')

            # backtrack
            m[i][j] = val

        solve(0, 0, '')
        # print(res)

        if len(res) == 0:
            return -1
        return res


obj = Solution()

N = 4
m = [[1, 0, 0, 0],
     [1, 1, 0, 1],
     [1, 1, 0, 0],
     [0, 1, 1, 1]]

obj.findPath(m, N)
