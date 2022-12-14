from collections import Counter

t = int(input())

def solve(n,l):
    d = [i for i in range(1,n+1)]   
    c = Counter(l)
    
    if c[n] > 1:
        return -1

    l.sort()
    
    if l[n-1] > n:
        return -1
    
    not_ele = []
    
    flag = 0
    for i in d:
        if i not in l:
            not_ele.append(i)
            flag = 1 
    
    if flag == 0:
        return 0
        
    # 1 1 
    # 2
    
    if n == 1:
        if l[0] == 0:
            return 1

    
    res = 0
    i = 0
    
    for i in range(n):
        if( l[i] != i+1 and l[i] < i+1):
            res += abs(l[i] - (i+1))
        elif l[i] > i+1:
            res = -1
            break
        
    # while len(not_ele) != 0 and i < n:
    #     if l[i] == 0 or l[i] == l[i+1] :
            
    #         v = min(not_ele)
            
    #         st = abs(v - l[i])
            
    #         res += st
            
    #         not_ele.remove(v)
        
    #         l[i] = v

    #     i+=1        
    # print(l)
    
    return res 

for i in range(t):
    n = int(input())
    l = [int(i) for i in input().split(" ")]
    
    print(solve(n,l))
    
    