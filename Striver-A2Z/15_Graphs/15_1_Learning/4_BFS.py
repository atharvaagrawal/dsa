from typing import List
from queue import Queue


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:

        # Create adj list
        adj_list = []

        for i in range(V):
            tmp = []
            tmp.append(i)
            for j in adj[i]:
                tmp.append(j)
            adj_list.append(tmp)

        # print(adj_list)

        q = Queue()
        # put() get()

        res = []

        def bfs(vertex):
            q.put(vertex)
            visited = [0]*V

            while q.qsize():
                val = q.get()
                if visited[val] == 0:
                    res.append(val)

                visited[val] = 1

                for i in adj_list[val]:
                    if visited[i] == 0:
                        q.put(i)

        bfs(0)
        return res
