    t = 0
    t = int(input())
    str = []

    for i in range(t):
        s = input()
        str.append(s)
    

    def func(s):
        s = [char for char in s]
        s_new = []
        s_str = []
        s_s = []
        count = 0
        day = 0

        if(len(s)<=3):
            return 1


        for i in range(len(s)):
            if s[i] not in s_new:
                #print(s[i],s_new)
                s_s.append(s[i])
                #print(s_s)
                s_new.append(s[i])
                count +=1
                
                if count == 3:
                    if i < len(s)-1:
                        if s[i+1] in s_new:
                            continue
                        #print(count,day)
                    day+=1
                    count = 0
                    s_new = []
                    s_str.append(''.join(s_s))
                    s_s = []

                if count == 4:
                    day+=1
                    count = 0
                    s_new = []
                    s_str.append(''.join(s_s))
                    s_s = []
        
        #print(s_str)
        #print('c',count)
        if count > 0:
            day+=1
        return day

    for j in range(t):
        print(func(str[j]))