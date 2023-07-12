# https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
""" 
You are given an Undirected Graph having unit weight, Find the shortest path from src to all the vertex and 
if it is unreachable to reach any vertex, then return -1 for that vertex.

Example:

Input:
n = 9, m= 10
edges=[[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0

Output:
0 1 2 1 2 3 3 4 4
"""


class Solution:
    def shortestPath(self, edges, n, m, src):

        # Create Adj List
        adj = [[] for _ in range(n)]

        for i in range(m):
            u, v = edges[i]

            adj[u].append(v)
            adj[v].append(u)

        distance = [float('inf')]*n

        distance[src] = 0

        # Source Node and Distance Node
        queue = [(src, 0)]

        while queue:
            node, dis = queue.pop(0)

            # Traverse the adjacent nodes
            for i in adj[node]:
                # If current distance +1 is less than the previous then only add
                if dis+1 < distance[i]:
                    distance[i] = dis+1
                    queue.append((i, dis+1))

        # Mark the UnVisited Nodes as -1
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1

        return distance
