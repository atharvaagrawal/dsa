# Detect cycle in an undirected graph

""" 
Intuition:
The cycle in a graph starts from a node and ends at the same node. DFS is a traversal technique that 
involves the idea of recursion and backtracking. DFS goes in-depth, i.e., traverses all nodes by going 
ahead, and when there are no further nodes to traverse in the current path, then it backtracks on the 
same path and traverses other unvisited nodes. The intuition is that we start from a source and go 
in-depth, and reach any node that has been previously visited in the past; it means there’s a cycle.

Approach:
The algorithm steps are as follows:

In the DFS function call make sure to store the parent data along with the source node, create a 
visited array, and initialize to 0. The parent is stored so that while checking for re-visited nodes, 
we don’t check for parents. 

We run through all the unvisited adjacent nodes using an adjacency list and call the recursive dfs function. 
Also, mark the node as visited.
If we come across a node that is already marked as visited and is not a parent node, then keep on returning t
rue indicating the presence of a cycle; otherwise return false after all the adjacent nodes have been checked 
and we did not find a cycle.

NOTE: We can call it a cycle only if the already visited node is a non-parent node because we cannot say 
we came to a node that was previously the parent node. 
"""

""" 
from typing import List, bool

class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = [0]*V
	    
	    # If same node visited again then cycle is there
	    def dfs(vertex,parent):
	        visited[vertex] = 1
	        
	        for i in adj[vertex]:
	            if visited[i] == 0:
    	            res = dfs(i,vertex)
    	            if res:
    	                return 1
    	        elif i != parent:
    	            return 1
	        return 0
	        
	    # It's component can also have
	    for i in range(V):
            if visited[i] == 0:
                res = dfs(i,-1)
        	    
        	    if res:
        	        return 1
	    
	    return 0 
"""
