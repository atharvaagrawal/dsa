# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=check-if-an-array-is-sorted

def checkSorted(arr):
    prev = arr[0]
    flag = 0
    for i in range(1,len(arr)):
        if arr[i] >= prev:
            pass
        else:
            flag = 1
            break
        prev = arr[i]

    if flag:
        print("\n\n Not Sorted")
    else:
        print("\n\n Sorted")    

arr = [1,6,3,4,5]
checkSorted(arr)