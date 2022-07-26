t = int(input())
    
def solve(s,e):
    earr = [char for char in e]
    
    for ele in earr:
        # print(ele,s)
        if ele == 'D':
            # s = down;(s)
            if(s==9):
                s = 0
            else:
                s = s+1
        elif ele == 'U':
            # s = up(s)
            if(s==0):
                s = 9
            else:
                s = s -1
    return s

for i in range(t):
    no_wheel = int(input())
    final_seq = [int(i) for i in input().split(" ")]
    a = 0
    res_arr=[]

    for seq in final_seq:
        arr = [i for i in input().split(" ")]
        res_arr.append(solve(seq,arr[1]))
    
    for i in res_arr:
        print(i,end=" ")
    print()
        
