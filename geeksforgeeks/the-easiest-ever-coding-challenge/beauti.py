n = 90


while(True):
    arr = [int(i) for i in str(n)]
    s = 0
    for i in arr:
        s = s + i*i
    print(s)
    n = s
    if s == 1:
        print("YES")
        break
    
    if len(str(s)) == 1:
        print("NO") 
        break