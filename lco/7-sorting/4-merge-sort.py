def mergeSort(array):

    if len(array) > 1:

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
        print("i", i, "j", j, "k", k, "left", left, "right", right)
        # while i < len(left) and j < len(right):

    return array


array = [6, 5, 20, 10, 9, 2]
print(array)
mergeSort(array)
print(array)
