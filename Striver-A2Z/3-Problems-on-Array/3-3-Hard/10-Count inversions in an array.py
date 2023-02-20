""" 
What is an inversion of an array? 
Definition: for all i & j < size of array, if i < j then you have 
to find pair (A[i],A[j]) such that A[j] < A[i] or A[i] > A[j].

Example 1:
-----------------------------------------------------------------------------
Input Format: N = 5, array[] = {1,2,3,4,5}

Result: 0

Explanation: we have a sorted array and the sorted array 
has 0 inversions as for i < j you will never find a pair 
such that A[j] < A[i]. More clear example: 2 has index 1 
and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an  inversion.
-----------------------------------------------------------------------------
Input Format: N = 5, array[] = {5,4,3,2,1}

Result: 10

Explanation: we have a reverse sorted array and we will
get the maximum inversions as for i < j we will always
find a pair such that A[j] < A[i].
Example: 5 has index 0 and 3 has index 2 now (5,3) pair
is inversion as 0 < 2 and 5 > 3 which will satisfy out
conditions and for reverse sorted array we will get
maximum inversions and that is (n)*(n-1) / 2.

For above given array there is 4 + 3 + 2 + 1 = 10 inversions.
-----------------------------------------------------------------------------
Input Format: N = 5, array[] = {5,3,2,1,4}

Result: 7

Explanation: There are 7 pairs (5,1), (5,3), (5,2), (5,4),
(3,2), (3,1), (2,1) and we have left 2 pairs (2,4) and
(1,4) as both are not satisfy our condition.
"""


# BruteForce: Got TLE
'''
def countInversion(l):
    i = 0
    j = 1
    c = 0

    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j] < l[i]:
                c += 1
    return c

arr = [5,3,2,1,4]
print(countInversion(arr))
'''

# Python 3 program to count inversions in an array
# Function to Use Inversion Count
def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


# This Function will use MergeSort to count inversions
def _mergeSort(arr, temp_arr, left, right):
    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right) // 2

        # It will calculate inversion
        # counts in the left subarray

        inv_count += _mergeSort(arr, temp_arr, left, mid)

        # It will calculate inversion
        # counts in right subarray

        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)

        # It will merge two subarrays in
        # a sorted subarray

        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


# This function will merge two subarrays
# in a single sorted subarray


def merge(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that
            # i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


# Driver Code
# Given array is
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)


""" 
Simple:

def merge(arr,left,mid,right):
    i = left
    j = mid+1
    k = left
    temp_arr = [0]*n

    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            i+=1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i+1)
            j+=1
        k+=1

    while i <= mid:
        temp_arr[k] = arr[i]
        i+=1
        k+=1

    while j <= right:
        temp_arr[k] = arr[j]
        j+=1
        k+=1

    for i in range(left,right+1):
        arr[i] = temp_arr[i]

    return inv_count

def mergeSort(arr,left,right):
    
    inv_count = 0

    if left < right:
        mid = (left+right)//2

        inv_count += mergeSort(arr,left,mid)
        inv_count += mergeSort(arr, mid+1, right)
        inv_count += merge(arr,left,mid,right)
    
    return inv_count

arr = [40,25,19,12,9,6,2]
n = len(arr)
res = mergeSort(arr,0,n-1)
print("Inversion Count:",res)
print(arr)
 """