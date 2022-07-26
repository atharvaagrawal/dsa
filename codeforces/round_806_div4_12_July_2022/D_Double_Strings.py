# Any two string combination to single string

t = int(input())

def solve(arr):
    res = []

    for i in range(len(arr)):
        flag = 0
        
        if len(arr[i]) == 1:
            res.append(0)
            continue

        for j in range(len(arr)):
            if i == j:
                continue
            
            if len(arr[i]) < len(arr[j]):
                continue
            
            if arr[i] == arr[j]+arr[j]:
                res.append(1)
                flag =1
                break
            flag2 = 0
            for k in range(len(arr)):
                #print(arr[i],arr[j],arr[k])
                if j == k or k == i:
                    continue
                
                if len(arr[i]) < len(arr[k]):
                    continue

                # print(arr[i],arr[j],arr[k])
                
                if arr[i] == arr[j]+arr[k]:
                    res.append(1)
                    flag = 1
                    flag2 = 1
                    break

                if arr[i] == arr[k]+arr[j]:
                    res.append(1)
                    flag = 1
                    flag2 = 1
                    break
            if flag2 == 1:
                break

        if flag == 0:
            res.append(0)
            
    for ele in res:
        print(ele,end="")
    print()

for i in range(t):
    p = int(input())
    arr = []
    
    for j in range(p):
        arr.append(input())
    
    solve(arr)