""" 
https://leetcode.com/problems/number-of-provinces/description/

Given an undirected graph with V vertices. We say two vertices u and v belong to a single province 
if there is a path from u to v or v to u. Your task is to find the number of provinces.
Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group.


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""


class Solution:
    def numProvinces(self, adj, V):

        # Given a Adjacency Matrix

        visited = [0]*V

        # DFS
        # In this we take vertex and visit

        def dfs(v):
            visited[v] = 1

            for i in range(V):
                if visited[i] != 1 and adj[v][i] == 1:
                    dfs(i)
        c = 0

        for i in range(V):
            if visited[i] == 0:
                dfs(i)
                c += 1

        return c
