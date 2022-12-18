import sys
sys.setrecursionlimit(10 ** 9)

class Node:
    def __init__(self,v):
        self.vertex = v
        self.next = None
        
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        #  Creating Adjacency  List
        head = [None for i in range(n)]
        
        def insert(u,v):
            t = head[u]

            if t == None:
                head[u] = Node(v)
                return 

            while t.next != None:
                if t.vertex == v:
                    return True
                t = t.next
            
            t.next = Node(v);         
        
        
        for i,j in edges:
            # print(i,j)
            insert(i-1,j-1)
            insert(j-1,i-1)
        
        # Checking for Even
        def is_Even():
            for i in range(n):
                t = head[i]
                ct = 0
                
                l = []
  
                while t!=None:
                    ct+=1
            
                    t = t.next
            
                if ct % 2 != 0:
                    return False
                
            return True
        
        # Checking
        if is_Even():
            return True
        
        # Try Adding Edge
        def is_Even_ls():
            for i in range(n):
                t = head[i]
                ct = 0
                
                l = []
  
                while t!=None:
                    ct+=1        
                    t = t.next
    
                l.append(ct)            
            
            return l
        
        l = is_Even_ls()
        e = []
        print(l)
        for i in range(len(l)):
            if l[i] % 2 != 0:
                e.append(i)
        ct = 0
        print(e)
        
        for i in range(len(e)):
            sour= e[i]
            for j in range(n):
                if sour == j:
                    continue
                
                if insert(sour,j):
                    continue
                insert(j,sour)
                
                ct+=1
                if ct > 2:
                    return False
                
                if is_Even():
                    return True
        
        if ct > 2:
            return False
        
        return True if is_Even() else False        
        