t = int(input())

for i in range(t):
    n,k = map(int,input().split(" "))
    a = [int(i) for i in input().split(" ")]
    b = [int(i) for i in input().split(" ")]
    
    d = dict()
    
    for i in range(n):
        if a[i] in d:
            d[a[i]] = min(d[a[i]],b[i])
        else:
            d[a[i]] = b[i]

    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}   
    
    if len(d) < k:
        print(-1)
        continue
    
    s = 0
    
    for i in d.keys():
        if k == 0:
            break
        s += d[i]
        k-=1 
    
    print(s)