arr = [int(x) for x in input().split()]
low = 0
high = len(arr) - 1

def find_rotation_helper(arr,low,high):
    mid = (low+high)//2

    while(low <= high):
        mid = (low+high)//2

        print('mid:'+str(mid))
        print('low:'+str(low))
        print('high:'+str(high)+"\n\n")

        if arr[mid] < arr[mid+1]:
            if arr[mid] < arr[high]:
                high = mid -1
                return find_rotation_helper(arr,low,high)
            else:
                low = mid +1
                return find_rotation_helper(arr,low,high)
        else:
            res = mid +1
            return res
            
    else:
        print("Sorted")
        return  -999


res = find_rotation_helper(arr,low,high)


# Search
search = int(input("Enter Search Element:"))

low = 0
high = len(arr) - 1 

if(arr[low] <= search): 
    high = res - 1
else:
    low = res


mid = (low + high)//2 

def search_rotation_helper(arr,low,high,search):
    mid = (low+high)//2

    while(True):
        if(search==arr[mid]):
            print("value found at:",mid)
            return 0
        elif(search > arr[mid]):
            low = mid + 1
            return search_rotation_helper(arr,low,high,search)
        elif(search <  arr[mid]):
            high = mid - 1
            return search_rotation_helper(arr,low,high,search)
            
        if(low > high):
            print("Value not present")
            return 1

res = search_rotation_helper(arr,low,high,search)