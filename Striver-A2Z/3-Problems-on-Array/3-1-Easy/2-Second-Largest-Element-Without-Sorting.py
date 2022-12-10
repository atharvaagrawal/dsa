def secondLargest(arr):
    second_large = -1
    large = -1

    for i in arr:
        if i > large:
            second_large = large
            large = i
        elif i > second_large and large != i:
            second_large = i         
    
    print("\n Second Large:",second_large)

arr = [10,100,20,30,405,60,3,102]
secondLargest(arr)