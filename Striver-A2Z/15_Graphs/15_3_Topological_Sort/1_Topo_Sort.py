# https://practice.geeksforgeeks.org/problems/topological-sort/1


# Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

# DFS
class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

        visited = [0]*V

        # Using DFS
        def dfs(v):

            visited[v] = 1

            for j in adj[v]:
                if not visited[j]:
                    dfs(j)

            stack.append(v)

        stack = []

        for i in range(V):
            if not visited[i]:
                dfs(i)

        # print(stack)

        return stack[::-1]
