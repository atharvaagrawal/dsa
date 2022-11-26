'''
MAX MIN ARRAY
'''


def max_min_arr(arr):
    global_max = arr[0]
    global_min = arr[0]
    for ele in arr:
        if ele > global_max:
            global_max = ele
        if ele < global_min:
            global_min = ele

    return [global_max, global_min]


def max_min_recurr(i, min, max):
    if i == len(arr)-1:
        return [max, min]

    if arr[i] > max:
        max = arr[i]

    if arr[i] < min:
        min = arr[i]

    return max_min_recurr(i+1, min, max)


#arr = [int(i) for i in input("Enter array elements:").split()]

arr = [5, 2, 5, 8, 1, 6]

print("MIN MAX:", max_min_arr(arr))
print("MIN MAX:", max_min_recurr(0, arr[0], arr[0]))
