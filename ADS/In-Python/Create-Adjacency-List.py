class Node:
    def __init__(self,v):
        self.vertex = v
        self.next = None

class Solution:  
    def solve(self, n, edges):

        head = [None for i in range(n)]

        def insert(u,v):
            t = head[u]

            if t == None:
                head[u] = Node(v)
                return 

            while t.next != None:
                t = t.next
            
            t.next = Node(v);         

        for i in range(len(edges)):
            insert(edges[i][0],edges[i][1])
            insert(edges[i][1],edges[i][0])
        

        visited = [0 for i in range(n)]

        def dfs(visited,u):
            visited[u] = 1

            t = head[u]

            while t != None:
                if(  visited[t.vertex] == 0 ):
                    dfs(visited,t.vertex)
                t = t.next
        def show():
            for i in range(n):
                t = head[i]
                print("\n vertex:",i,end=" ")
                while t!=None:
                    print(t.vertex,end=" ")
                    t = t.next
        # display adjacency list
        print("Adjaceny list:")
        show()