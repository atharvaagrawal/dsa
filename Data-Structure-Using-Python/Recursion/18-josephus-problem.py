# Josephus Problem

def solve(n, k, arr, index):
    if len(arr) == 1:
        print(arr[0])
        return

    index = (index + k) % len(arr)

    arr.pop(index)

    solve(n, k, arr, index)


n = 40
k = 7

arr = list(range(1, n+1))
k -= 1
solve(n, k, arr, 0)
