t = int(input())
arr = []

for i in range(t):
    arr.append(input())

for i in arr:
    if ((i[0]=='Y' or i[0]=='y') and  (i[1]=='e' or i[1]=='E') and (i[2]=='S' or i[2]=='s')):
        print("YES")
    else:
        print("NO")
