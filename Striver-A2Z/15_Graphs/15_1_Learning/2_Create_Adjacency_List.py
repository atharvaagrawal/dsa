# https://practice.geeksforgeeks.org/problems/print-adjacency-list-1587115620/1

""" 
Given the adjacency list of a bidirectional graph. Your task is to copy/clone the adjacency list 
for each vertex and return a new list.

Input:
0 1
0 4
1 0
...


Output: 
0-> 1-> 4 
1-> 0-> 2-> 3-> 4 
2-> 1-> 3 
3-> 1-> 2-> 4 
4-> 0-> 1-> 3


Explanation:
As 0,1 and 3 is connected to 4 so 4th row
of the list containing 4 and its connected
nodes 0,1 and 3 and we have to add those in
sorted order and same for every row.
"""


class Solution:
    # Function to return the adjacency list for each vertex.
    def printGraph(self, V, adj):

        # V = Vertices
        ans = []
        for i in range(V):
            tmp = []
            tmp.append(i)
            for j in adj[i]:
                tmp.append(j)
            ans.append(tmp)

        return ans
