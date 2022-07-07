t = int(input())


for i in range(t):
    n, k = input().split(" ")
    arr = [int(i) for i in input().split(' ')]
    n = int(n)
    k = int(k)
    for i in range(1, n+1):
        print(i, end=" ")

    print()
