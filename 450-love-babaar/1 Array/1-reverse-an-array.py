'''
Reverse an Array
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
'''


# Time Complexity: o(n)
def reverse_array_on(arr):
    rev_arr = []
    for i in range(len(arr)-1, -1, -1):
        rev_arr.append(arr[i])

    return rev_arr


# Time Complexity: O(1)
def reverse_array_o1(arr):
    return list(reversed(arr))


rev_arr = []


# Using Recurrsion
def reverse_array_recurr(arr, i):
    if i == -1:
        return rev_arr

    rev_arr.append(arr[i])
    return reverse_array_recurr(arr, i-1)


# Reverse the array itself
def reverse_arr_itself(arr, start, end):
    if start > end:
        return

    arr[start], arr[end] = arr[end], arr[start]

    reverse_arr_itself(arr, start+1, end-1)


arr = [int(i) for i in input("Enter the Array Elements:").split()]

print(reverse_array_on(arr))
print(reverse_array_o1(arr))
print("Recurrsion:", reverse_array_recurr(arr, len(arr)-1))
reverse_arr_itself(arr, 0, len(arr)-1)
print("Reverse Array:", arr)
