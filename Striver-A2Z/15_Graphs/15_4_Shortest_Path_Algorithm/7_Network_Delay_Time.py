# https://leetcode.com/problems/network-delay-time/description/

""" 
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list 
of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, 
vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all 
the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
"""


from typing import List
from queue import Queue


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for i in range(n+1)]

        for i in range(len(times)):
            adj[times[i][0]].append([times[i][1], times[i][2]])

        distance = [float('inf')]*(n+1)
        distance[k] = 0

        q = Queue()

        # Distance, Source
        q.put([0, k])

        while not q.empty():
            dis, src = q.get()

            # Visit Adjacent
            for node, t in adj[src]:

                if t+dis < distance[node]:
                    distance[node] = t+dis
                    q.put([t+dis, node])

        for i in range(1, len(distance)):
            if distance[i] == float('inf'):
                return -1

        return max(distance[1::])
