t = int(input())


for i in range(t):
    n, w = input().split(" ")
    n = int(n)
    w = int(w)

    ai = [int(x) for x in input().split(" ")]

    sum = 0

    ai.sort()
    ai.reverse()

    for i in range(len(ai)):
        sum += ai[i]

        if sum >= w:
            print(len(ai)-i-1)
            break
