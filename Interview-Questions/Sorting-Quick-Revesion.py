# Insertion SOrt

def insertion(arr):
    # Asending Order
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
                                                                    
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key                                                        
    return 

def selection(arr):
    for i in range(len(arr)):
        min_idx = i  
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                min_idx = j
        
        arr[min_idx],arr[i] = arr[i],arr[min_idx]
    return 

def partition(low,high):
    i = low
    j = high
    pivot = arr[low]

    while i < j:
        while i < len(arr) and pivot >= arr[i]:
            i+=1
        
        while j >= 0 and pivot < arr[j]:
            j-=1

        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[j],arr[low] = arr[low],arr[j]
    return j

def quickSort(low,high):
    if low < high:
        i = partition(low,high)
        quickSort(low,i-1)
        quickSort(i+1,high)


def merge(low,mid,high):
    i = low
    j = mid+1
    k = low

    temp_arr = [0]*len(arr)

    while i<= mid and j <= high:

        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            i+=1
        else:
            temp_arr[k] = arr[j]
            j+=1
        k+=1

    
    while i<= mid:
        temp_arr[k] = arr[i]
        i+=1
        k+=1

    while j <= high:
        temp_arr[k] = arr[j]
        j+=1
        k+=1
    
    for i in range(low,high+1):
        arr[i] = temp_arr[i]

def mergeSort(low,high):
    if low < high:
        mid = (low+high)//2

        mergeSort(low,mid)
        mergeSort(mid+1,high)

        merge(low,mid,high)

arr = [5,3,4,6,1]
print(arr)
# insertion(arr)
# selection(arr)
# quickSort(0,len(arr)-1)
mergeSort(0,len(arr)-1)
print(arr)
