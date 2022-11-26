# Find the smallest common element in sorted of 3 array

arr1 = [int(x) for x in input().split(' ')]
arr2 = [int(x) for x in input().split(' ')]
arr3 = [int(x) for x in input().split(' ')]


def find_smallest(ele1, ele2, ele3):

    if((ele1 < len(arr1)) and (ele2 < len(arr2)) and (ele3 < len(arr3))):

        if(arr1[ele1] == arr2[ele2] == arr3[ele3]):
            return arr1[ele1]

        if(arr1[ele1] <= arr2[ele2] and arr1[ele1] <= arr3[ele3]):
            return find_smallest(ele1+1, ele2, ele3)

        elif(arr2[ele2] <= arr1[ele1] and arr2[ele2] <= arr3[ele3]):
            return find_smallest(ele1, ele2+1, ele3)

        elif(arr3[ele3] <= arr1[ele1] and arr3[ele3] <= arr2[ele2]):
            return find_smallest(ele1, ele2, ele3+1)
    else:
        return "NO Match"


print(find_smallest(0, 0, 0))
