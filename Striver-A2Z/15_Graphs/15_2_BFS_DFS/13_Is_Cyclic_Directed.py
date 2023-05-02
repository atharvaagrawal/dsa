# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

# Detect cycle in a directed graph
# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.

# Using DFS
""" 
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = [0]*V
        recSt = [0]*V
        
	    # If same node visited again then cycle is there
	    def dfs(vertex,parent):
	        visited[vertex] = 1
	        recSt[vertex] = 1
	        
	        for i in adj[vertex]:
	            if visited[i] == 0:
    	            res = dfs(i,vertex)
    	            if res:
    	                return 1
    	        elif recSt[i]:
    	            return 1
    	    
    	    recSt[vertex] = 0
	        
	        return 0
	        
	    # It's component can also have
	    for i in range(V):
            if visited[i] == 0:
                res = dfs(i,-1)
        	    
        	    if res:
        	        return 1
        	        
	    return 0  
"""
