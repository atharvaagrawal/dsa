# Given an adjacency list of a graph adj  of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        color = [-1]*n

        # No 2 adjacent nodes have same color
        def dfs(v, c):
            color[v] = c

            for i in graph[v]:
                if color[i] == -1:
                    if dfs(i, not c) == False:
                        return False
                elif color[i] == c:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                if dfs(i, 0) == False:
                    return False

        return True
