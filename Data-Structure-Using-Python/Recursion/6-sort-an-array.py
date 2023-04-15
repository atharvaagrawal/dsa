# Sort an Array using Recurssion

def insert(arr, temp):
    if len(arr) == 0 or arr[len(arr)-1] <= temp:
        arr.append(temp)
        return
    val = arr.pop()

    insert(arr, temp)
    arr.append(val)
    return


def sort(arr):
    if len(arr) == 1:
        return

    temp = arr.pop()

    sort(arr)

    insert(arr, temp)


arr = [0,9 ,1, 5, 3, 8, 10, 2]

print("Before Sort:", arr)
sort(arr)
print("Sorted Array:", arr)
