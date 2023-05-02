class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):

        visited = [0]*V
        res = []

        def dfs(vertex):
            visited[vertex] = 1
            res.append(vertex)
            for i in adj[vertex]:
                if visited[i] != 1:
                    dfs(i)

        dfs(0)

        return res
