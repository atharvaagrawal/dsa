# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


# User function Template for python3

class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):

        # Using BFS
        # Through Topo-Sort

        indegree = [0]*V

        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1

        queue = []

        # Add all the node with indegree 0
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        cnt = 0

        while queue:
            v = queue.pop(0)

            cnt += 1

            # Reduce the indegree
            for i in adj[v]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    queue.append(i)

        if cnt == V:
            return False

        return True
