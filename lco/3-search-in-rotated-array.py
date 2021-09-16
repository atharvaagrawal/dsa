list_search = [int(x) for x in input().split()]

low = 0
high = len(list_search) - 1
res = 0
while(low <= high):
    mid = (low+high)//2

    print('mid:'+str(mid))
    print('low:'+str(low))
    print('high:'+str(high)+"\n\n")

    if list_search[mid] < list_search[mid+1]:
        if list_search[mid] < list_search[high]:
            high = mid -1
        else:
            low = mid +1
    else:
        res = mid +1
        break
else:
    print("Sorted")

# Search

search = int(input("Enter Search Element:"))

low = 0
high = len(list_search) - 1 

if(list_search[low] <= search): 
    high = res - 1
else:
    low = res


mid = (low + high)//2

print('*******')
print('mid:'+str(mid))
print('low:'+str(low))
print('high:'+str(high)+"\n\n")

while(True):
    if(search==list_search[mid]):
        print("value found at:",mid)
        break
    elif(search > list_search[mid]):
        low = mid + 1
        mid = (low + high)//2
    elif(search <  list_search[mid]):
        high = mid - 1
        mid = (low + high)//2
    if(low > high):
        print("Value not present")
        break
