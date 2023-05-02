""" 
Given an integer n representing number of vertices. Find out how many undirected graphs 
(not necessarily connected) can be constructed out of a given n number of vertices.


Example 1:
Input: 2
Output: 2

Example 2:
Input: 5
Output: 1024 
"""

"""
It is basically 2 ^ total unique edges
 
            Suppose there are n no of nodes. n=4 we suppose.

            Then no 1 node can connect with 3 different node with 3 unique edges -

            a. 1-2

            b. 1-3

            c. 1-4

            Again no 2 can connect with 2 unique edges and one common edge(1-2)

            d. 2-3

            e. 2-4

            Again no 3 can connect with 1 unique edge and 2 common edges(1-3, 2-3)

            f. 3-4

            And for no 4 node, we have all common edges(4-1, 4-2, 4-3)

            

            So for all combination, there can be total 3+2+1 = 6 unique edges

            So total unique edges for n nodes can be sum of 1 to n-1 = n(n-1)/2

            And posibilty for drawing each edge is 2

            So combinations = 2^((n*(n-1))/2)
"""


class Solution:
    def count(self, n):
        return 2**((n*(n-1))/2)


obj = Solution()

print(obj.count(5))
