def largestElement(arr):
    l = -1

    for i in arr:
        if i > l:
            l = i 
    
    print("Largest Element:",l)

arr = [10,100,20,30,405,60,3,102]
largestElement(arr)
