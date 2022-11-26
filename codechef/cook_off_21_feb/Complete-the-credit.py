t = int(input())


for i in range(t):
    n = int(input())

    if n > 65:
        print("Overload")
    elif n < 35:
        print("Underload")
    else:
        print("Normal")
