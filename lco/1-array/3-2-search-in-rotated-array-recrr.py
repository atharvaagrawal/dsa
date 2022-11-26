def rotated_search_helper(arr, low, high, key):
    if(low > high):
        return "NO MATCH"

    mid = (low+high)//2

    if arr[mid] == key:
        return mid

    if arr[low] <= arr[mid] and key <= arr[mid] and key >= arr[low]:
        return rotated_search_helper(arr, low, mid-1, key)

    elif arr[mid] <= arr[high] and key >= arr[mid] and key <= arr[high]:
        return rotated_search_helper(arr, mid+1, high, key)

    elif arr[high] <= arr[mid]:
        return rotated_search_helper(arr, mid+1, high, key)

    elif arr[low] >= arr[mid]:
        return rotated_search_helper(arr, low, mid-1, key)

    return -1


def rotated_search(arr, key):
    return rotated_search_helper(arr, 0, len(arr) - 1, key)
