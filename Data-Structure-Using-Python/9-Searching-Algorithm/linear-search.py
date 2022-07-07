
def linear_search(arr, ele):

    print("\n\n Element to find:", ele)

    i = 0

    for i in range(len(arr)):
        if ele == arr[i]:
            print("Element Found at:", i)
            break

    if i == len(arr)-1:
        print("Element not found")


arr = [5, 7, 92, 5, 3, 8]
linear_search(arr, 2)
linear_search(arr, 3)
