import math
import sys

t = int(input())

for i in range(t):
    n, x, y = input().split(" ")

    x = int(x)  # Bus - 100 People
    n = int(n)
    y = int(y)  # Car - 4 People

    ans = sys.maxsize

    for bus in range(0, math.ceil(n/100)+1):
        print(bus, "a")
        cars = int(max(0, math.ceil((n-bus*100)/4)))
        #print("Cars:", cars)
        smoke = bus * x + cars * y
        ans = min(ans, smoke)
    print(ans)
