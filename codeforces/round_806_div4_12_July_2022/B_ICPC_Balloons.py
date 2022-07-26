t = int(input())
arr = []

char_arr = set()
for i in range(65,91):
    char_arr.add(chr(i))

def solve(arr1):
    arr1 = [char for char in arr1]
    count = 0
    for i in range(65,91):
        char_arr.add(chr(i))
    for i in arr1:  
        if i in char_arr:
            count+=2
            char_arr.remove(i)
        else:
            count+=1
    print(count)

for j in range(t):
    n = int(input())
    a = input()
    solve(a)
