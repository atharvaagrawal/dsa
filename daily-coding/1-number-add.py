'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


# Using Recursion
def target_double(arr, k, start, end):
    # if start and end crosses each other then it means all elements are checked
    if start >= end:
        return False

    # If start + end is equal to k then return it
    if arr[start]+arr[end] == k:
        print(arr[start], arr[end])
        return True
    # if start+end is greater than k then reduce end by 1
    elif arr[start]+arr[end] > k:
        return target_double(arr, k, start, end-1)
    # if start+end is less than k then increase start by 1
    elif arr[start]+arr[end] < k:
        return target_double(arr, k, start+1, end)


# Using Iteration
def sum_of_two(arr, k):
    start = 0
    end = len(arr)-1
    arr.sort()

    while(1):
        if start >= end:
            return False

        if arr[start]+arr[end] == k:
            return True
        elif arr[start]+arr[end] > k:
            end -= 1
        elif arr[start]+arr[end] < k:
            start += 1


# [int(i) for i in input("Enter Array Elements:").split()]
arr = [15, 0, 3, 2]
k = 15  # int(input("Enter addition:"))
arr.sort()


print(target_double(arr, k, 0, len(arr)-1))
print(sum_of_two(arr, k))
