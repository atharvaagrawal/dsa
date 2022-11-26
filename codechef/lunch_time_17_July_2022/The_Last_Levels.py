t = int(input())

for i in range(t):
    lev,ti,bre = input().split(" ")
    
    lev = int(lev)
    ti = int(ti)
    bre = int(bre)

    # print("lev",lev)
    # print("ti",ti)
    # print("bre",bre)

    if(lev <= 3):
        print(lev*ti)
        continue
    
    time = 0

    while(True):
        if lev > 3:
            time  += 3 * ti
            time += bre
            lev = lev - 3
        else:
            time += lev * ti
            break
    print(time)
        
        
