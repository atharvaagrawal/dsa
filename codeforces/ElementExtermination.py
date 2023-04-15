# https://codeforces.com/contest/1375/problem/C 

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split(" ")]

    if arr[0] < arr[-1]:
        print("YES")
    else:
        print("NO")