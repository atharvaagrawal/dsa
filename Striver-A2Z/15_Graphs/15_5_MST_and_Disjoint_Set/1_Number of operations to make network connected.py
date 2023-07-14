# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

""" 
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where 
connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other 
computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly 
connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. 
If it is not possible, return -1.

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
"""


from typing import List


class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.rank = [0 for i in range(n)]

    # Ultimate Parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    # Union by Size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_v] += self.size[ulp_u]

    # Union by Rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        # As it is changing Dynamically we will use: Disjoint Set
        ds = DisjointSet(n)

        # Count Extra Edges
        cntExtras = 0

        m = len(connections)  # Number of Edges

        for i in range(m):
            u = connections[i][0]
            v = connections[i][1]

            if ds.findUPar(u) == ds.findUPar(v):
                cntExtras += 1
            else:
                ds.unionBySize(u, v)

        # Count Component
        cntC = 0

        for i in range(n):
            if ds.parent[i] == i:
                cntC += 1

        ans = cntC-1

        if cntExtras >= ans:
            return ans
        return -1
