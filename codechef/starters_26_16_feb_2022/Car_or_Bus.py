

t = int(input())

for i in range(t):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)

    if x == y:
        print("SAME")
    elif x > y:
        print("CAR")
    else:
        print("BIKE")
