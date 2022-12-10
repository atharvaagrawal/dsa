def removeDuplicate(arr):    
    j = 0

    for i in range(1,len(arr)):        
        if arr[i] != arr[j]:
            j+=1
            arr[j] = arr[i]

    print(arr)    
    return j+1


arr = [1,1,2,2,2,3,3]
removeDuplicate(arr)