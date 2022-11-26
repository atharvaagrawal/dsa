# Python program for implementation of Insertion Sort

# Function to do insertion sort

def insertionSort(arr):
    iter = 0
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        iter += 1
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    print(iter)


# Driver code to test above
arr = [34, 8, 64, 51, 32, 21]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
