# https://practice.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1


from queue import PriorityQueue


class Solution:
    def shortestPath(self, n, m, edges):

        # Create Adj List
        adj = [[] for _ in range(n+1)]

        for i in range(m):
            adj[edges[i][0]].append([edges[i][1], edges[i][2]])
            adj[edges[i][1]].append([edges[i][0], edges[i][2]])

        # We will store the where it came from
        distance = [float('inf')]*(n+1)
        distance[1] = 0

        parent = [i for i in range(n+1)]

        # distance, node

        queue = PriorityQueue()

        queue.put((0, 1))

        # Find the shortest path between the vertex 1 and the vertex n
        while not queue.empty():
            dist, node = queue.get()

            # Traverse adj nodes
            for i, w in adj[node]:
                if dist+w < distance[i]:
                    distance[i] = dist+w
                    parent[i] = node
                    queue.put((dist+w, i))

        # If Path Not Exist
        if distance[-1] == float('inf'):
            return [-1]

        path = []
        node = n

        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)
        return path[::-1]
