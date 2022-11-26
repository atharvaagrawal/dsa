t = int(input())

for i in range(t):
    n, x = input().split(" ")
    x = int(x)
    n = int(x)

    arr = [int(i) for i in input().split(" ")]
    # print(arr)
    max_a = x
    max_b = x
    for i in arr:
        max_a = max_a + i

        if max_b < max_a:
            max_b = max_a
    print(max_b)
