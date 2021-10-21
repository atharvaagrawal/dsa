
def josephus(arr, k, g, d):

    if d == n-1:
        return arr

    kil = (g+k-1) % n

    d += 1

    arr[kil] = ''

    return josephus(arr, k, (g+k) % n, d)


n = int(input("Enter number of Players:"))
k = int(input("Enter value of Killing:"))
arr = [i for i in range(n)]

print("Winner:", josephus(arr, k, g=0, d=0))
