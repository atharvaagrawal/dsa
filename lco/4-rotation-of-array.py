def find_rotation_helper(arr,low,high):

    if(high < low):
        return "No Match"
    
    mid = (high+low)//2

    print('mid:'+str(mid))
    print('low:'+str(low))
    print('high:'+str(high)+"\n\n")

    if(mid < high and arr[mid+1] < arr[mid]):
        return (mid + 1)
    
    if(mid > low and arr[mid] < arr[mid-1]):
        return mid
    

    if(arr[high] > arr[mid]):
        return find_rotation_helper(arr,low,mid-1)
    return find_rotation_helper(arr,mid+1,high)

arr = [int(x) for x in input().split()]

res = find_rotation_helper(arr,0,len(arr)-1)

print("Ans",arr[res])