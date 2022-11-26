def kthSmallest(arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        sorted(arr)


n = 5
arr = [7,10,4,20,15]
k = 4

kthSmallest(arr,0,n-1,k)