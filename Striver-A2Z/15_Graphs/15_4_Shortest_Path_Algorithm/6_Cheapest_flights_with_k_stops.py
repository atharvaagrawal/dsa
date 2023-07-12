""" 
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] 
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
"""

from queue import PriorityQueue, Queue
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # At Most K stops

        adj = [[] for i in range(n)]

        for i in range(len(flights)):
            adj[flights[i][0]].append([flights[i][1], flights[i][2]])

        distance = [float('inf')]*n
        distance[src] = 0

        q = Queue()

        # Distance, Source, Stops
        q.put([0, src, 0])

        while not q.empty():
            dis, node, stops = q.get()

            if stops > k:
                continue

            # Visit adjacent Nodes
            for nex, price in adj[node]:
                if stops <= k and dis+price < distance[nex]:
                    distance[nex] = dis+price
                    q.put([dis+price, nex, stops+1])

        if distance[dst] != float('inf'):
            return distance[dst]

        return -1
