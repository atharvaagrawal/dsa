from collections import defaultdict

def union(arr1,arr2):
    h = defaultdict()

    for i in arr1:
        h[i] = 1

    for i in arr2:
        h[i] = 1

    for i in h.keys():
        print(i,end=" ")
                

def intersection(arr1,arr2):
    res = []

    p1 = 0
    p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            print(arr1[p1],end=" ")
            p1+=1
            p2+=1
        elif arr1[p1] > arr2[p2]:
            p2+=1
        elif arr1[p1] < arr2[p2]:
            p1+=1
    




arr1 = [1,2,3,4,5]
arr2 = [2,3,4,6,7,8]

print("Arr1:",arr1)
print("Arr2:",arr2)

print("\n\n Union:",end=" ")
union(arr1,arr2)
print("\n\n Intersection:",end=" ")
intersection(arr1,arr2)
