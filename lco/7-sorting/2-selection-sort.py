def selectionSort(array):
    array_len = len(array)

    for i in range(array_len):
        min_value_index = i

        for j in range(i+1, array_len):
            if array[j] < array[min_value_index]:
                min_value_index = j

        array[i], array[min_value_index] = array[min_value_index], array[i]

    return array


array = [int(x) for x in input().split(" ")]

print(selectionSort(array))
