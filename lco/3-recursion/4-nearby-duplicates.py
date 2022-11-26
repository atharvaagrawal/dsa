'''
NearBy Duplicates

Input: myllccoo
Output: mylco

Input: myllccoolrc
Output: mylcolrc
'''


# Converting String to list
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


# 1 Deleting Nearby duplicates using array
def nearby_duplicates(arr, comp1, comp2, res):

    # Base Condition: If compare 1 is at the end of array we are appending and returing
    if(comp2 == len(arr)):
        res.append(arr[comp1])
        return ''.join(res)

    # If nearby elements are same the removing  it
    if(arr[comp1] == arr[comp2]):
        arr.pop(comp1)
        return nearby_duplicates(arr, comp1, comp2, res)
    # If  nearby elements are not equal then adding into list
    else:
        res.append(arr[comp1])
        return nearby_duplicates(arr, comp1+1, comp2+1, res)


# 2 Deleting Nearby duplicates using string
def near_by_duplicates(s):
    if len(s) == 1:
        return s
    elif s[0] == s[1]:
        return near_by_duplicates(s[1:])

    return s[0] + near_by_duplicates(s[1:])


input_str = "myllccoolrc"
arr = Convert(input_str)

print(nearby_duplicates(arr, 0, 1, []))

print(near_by_duplicates(input_str))
