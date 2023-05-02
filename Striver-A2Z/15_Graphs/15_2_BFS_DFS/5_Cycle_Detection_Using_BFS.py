""" 
Intuition:
The cycle in a graph starts from a node and ends at the same node. So we can think of two algorithms to do this, 
in this article we will be reading about the BFS, and in the next, we will be learning how to use DFS to check. 

Breadth First Search, BFS is a traversal technique where we visit the nodes level-wise, i.e., it visits the same 
level nodes simultaneously, and then moves to the next level. 

The intuition is that we start from a node, and start doing BFS level-wise, if somewhere down the line, we visit 
a single node twice, it means we came via two paths to end up at the same node. It implies there is a cycle in the 
graph because we know that we start from different directions but can arrive at the same node only if the graph is
 connected or contains a cycle, otherwise we would never come to the same node again.  

Approach:
Initial configuration:
Queue: Define a queue and insert the source node along with parent data (<source node, parent>). 
For example, (2, 1) means 2 is the source node and 1 is its parent node.
Visited array: an array initialized to 0 indicating unvisited nodes.  



The algorithm steps are as follows:

For BFS traversal, we need a queue data structure and a visited array. 
Push the pair of the source node and its parent data (<source, parent>) in the queue, and mark the node as visited. 
The parent will be needed so that we don’t do a backward traversal in the graph, we just move frontwards. 
Start the BFS traversal, pop out an element from the queue every time and travel to all its unvisited neighbors using an adjacency list.
Repeat the steps either until the queue becomes empty, or a node appears to be already visited which is not the parent, 
even though we traveled in different directions during the traversal, indicating there is a cycle.
If the queue becomes empty and no such node is found then there is no cycle in the graph.
"""

""" 
from typing import List
from queue import Queue

class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	
		# Here also we have to check the parent
		
		visited = [0]*V
		
		def bfs(src):
		    queue = Queue()
		    queue.put([src,-1])
    		while queue.qsize():
    		    vertex, parent = queue.get()
    		    visited[vertex] = 1
    		    
    		    for i in adj[vertex]:
    		        if visited[i] == 0:
        		        queue.put([i,vertex])
    	            elif i != parent:
    	                return 1
	    
	    for i in range(V):
	        if visited[i] == 0:
	           res = bfs(i)
	           if res:
	               return 1
	        
		return 0 
"""
