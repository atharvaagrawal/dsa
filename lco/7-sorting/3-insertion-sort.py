def insertionSort(array):

    for i in range(1, len(array)+1):
        for j in range(i-1, 0, -1):
            if j > 0 and array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

    return array


array = [int(x) for x in input().split(" ")]

print(insertionSort(array))
