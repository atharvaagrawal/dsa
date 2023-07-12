# https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

""" 
Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector)
edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with 
a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to 
reach any vertex, then return -1 for that vertex.

Example1:

Input:
N = 4, M = 2
edge = [[0,1,2],[0,2,1]
Output:
0 2 1 -1
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 2. 
Shortest path from 0 to 2 is 0->2 with edge weight 1.
There is no way we can reach 3, so it's -1 for 3.

Example2:

Input:
N = 6, M = 7
edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
Output:
0 2 3 6 1 5
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 2. 
Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3.
Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6.
Shortest path from 0 to 4 is 0->4 with edge weight 1.
Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.
"""

from typing import List


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:

        # Create Adj List with Weight
        adj = [[] for _ in range(n)]

        for i in range(m):
            adj[edges[i][0]].append([edges[i][1], edges[i][2]])

        # Create Distance Array
        distance = [float('inf')]*n

        distance[0] = 0

        # Source and Distance
        queue = [(0, 0)]

        while queue:
            node, dis = queue.pop(0)

            # Adjacent Nodes
            for adjnode, d in adj[node]:
                if dis+d < distance[adjnode]:
                    distance[adjnode] = dis+d

                    queue.append((adjnode, dis+d))

        # Mark Unvisited Nodes
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1

        return distance


# Using TopoSort
class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:

        # Create Adj List with Weight
        adj = [[] for _ in range(n)]

        for i in range(m):
            adj[edges[i][0]].append([edges[i][1], edges[i][2]])

        # Apply topo sort
        stack = []

        visited = [0]*n

        def topoSort(vertex):

            visited[vertex] = 1

            # Visit Adj Nodes
            for i, w in adj[vertex]:
                if not visited[i]:
                    topoSort(i)

            stack.append(vertex)

        # If Component
        for i in range(n):
            if not visited[i]:
                topoSort(i)

        # Relax the Edges

        # Create Distance Array
        distance = [float('inf')]*n

        distance[0] = 0

        while stack:
            node = stack.pop()

            dis = distance[node]

            # Visit adjacent nodes
            for i, w in adj[node]:
                if dis+w < distance[i]:
                    distance[i] = dis+w

        # If node not visited
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1

        return distance
