t = int(input())

for i in range(t):
    l = []
    l = input().split(" ")
    l[0]  = int(l[0])
    l[1]  = int(l[1])
    l[2]  = int(l[2])
    l[3]  = int(l[3])
    if l[0]+l[1] < l[2]+l[3]:
        print(l[0]+l[1])
    else:
        print(l[2]+l[3])
