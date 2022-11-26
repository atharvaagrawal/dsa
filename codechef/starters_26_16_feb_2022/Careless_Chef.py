t = int(input())

for i in range(t):
    n = int(input())
    b = [int(x) for x in input().split(" ")]

    parity_cnt_even = 0
    parity_cnt_odd = 0

    for ele in b:
        if ele % 2 == 0:
            parity_cnt_even += 1
        else:
            parity_cnt_odd += 1

    if parity_cnt_even % 2 == 0 and parity_cnt_odd % 2 == 0:
        print("YES")
    else:
        print("NO")