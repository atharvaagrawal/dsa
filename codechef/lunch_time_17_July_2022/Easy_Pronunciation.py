t = int(input())

for i in range(t):
    n = int(input())
    ch = input()

    ch = [word for word in ch]
    vowels = ['a','e','i','o','u']
    flag = 1
    count = 0

    if len(ch) < 4:
        print("YES")
        continue

    for i in ch:
        if i in vowels:
            count = 0
        else:
            count +=1

        if count >= 4:
            print("NO")
            flag = 0
            break
    
    if flag:
        print("YES")
    
