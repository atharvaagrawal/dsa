# https://practice.geeksforgeeks.org/problems/print-adjacency-list-1587115620/1

""" 
Given the adjacency list of a bidirectional graph. Your task is to copy/clone the adjacency list 
for each vertex and return a new list.
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
