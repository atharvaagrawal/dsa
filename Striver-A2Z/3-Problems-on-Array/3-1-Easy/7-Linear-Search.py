def linearSearch(arr,key):
    for i in range(len(arr)):
        if key == arr[i]:
            print("\n\n Element found at:",i+1)
            return 

    print("\n\n Element not found")
    return

arr = [10,203,1,301,33,4,13]
key = 4

linearSearch(arr,key)
