def quickSort(array):

    array_len = len(array)

    if array_len < 2:
        return array

    pos = 0

    for i in range(1, array_len):
        if array[i] < array[0]:
            pos = pos + 1
            array[i], array[pos] = array[pos], array[i]

    array[0], array[pos] = array[pos], array[0]

    left = quickSort(array[0:pos])
    right = quickSort(array[pos+1:])

    array = left + [array[pos]] + right

    return array


array = [6, 5, 20, 10, 9, 2]
print(array)
quickSort(array)
print(array)
