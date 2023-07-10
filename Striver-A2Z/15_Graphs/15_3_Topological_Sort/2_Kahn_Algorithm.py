# https://practice.geeksforgeeks.org/problems/topological-sort/1


from collections import defaultdict


class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

        indegree = [0]*V

        # Calculate Indegree for each Node
        for v in range(V):
            for i in adj[v]:
                indegree[i] += 1

        queue = []

        # Add all the Node with Indegree 0
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        res = []

        while queue:

            node = queue.pop(0)

            res.append(node)

            # Reduce the indegree of other nodes
            for j in adj[node]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)

        return res
