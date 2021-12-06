# Implement bubble sort

def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1-i):

            if arr[j] > arr[j+1]:
                swap = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = swap
    return arr


print(bubble_sort([8, 5, 2, 4, 1, 7]))

print(bubble_sort([1, 4, 5, 2, 3, 8]))
