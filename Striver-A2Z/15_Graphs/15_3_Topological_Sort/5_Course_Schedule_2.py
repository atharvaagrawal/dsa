# https://leetcode.com/problems/course-schedule-ii/description/
""" 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. 
So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished 
both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Using Topo Sort
        indegree = [0]*numCourses

        # Create Adj List
        adj = [[] for i in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
            # To take 'u' course 'v' course should be finished

        for i in range(numCourses):
            for v in adj[i]:
                indegree[v] += 1

        res = []
        queue = []

        # Insert all with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Intution: you should able to finish atleast 1 course before taking other
        while queue:
            v = queue.pop()

            res.append(v)

            # Reduce the indgree of others
            for i in adj[v]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if len(res) >= numCourses:
            return reversed(res)

        return []
