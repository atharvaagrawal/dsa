t = int(input())

for i in range(t):
    n = int(input())
    st = input()

    st = [word for word in st]
    st_r = st.copy()
    st_r.reverse()
    print(st)
    # print(st_r)
    
    if st_r == st:
        print("YES")
        continue
    flag = 1

    for i in range(n-2):
        
        temp = st[i]  
        st[i] = st[i+2]
        st[i+2] = temp

        print(st)
        # print(st_r)

        st_r = st.copy()
        st_r.reverse()
    
        if st_r == st:
            print("YES")
            flag = 0
            break
    if flag:
        print("NO")
        


    