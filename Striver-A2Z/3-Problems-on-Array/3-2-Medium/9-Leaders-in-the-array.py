# https://takeuforward.org/data-structure/leaders-in-an-array/


def leader(l):
    m = l[-1]

    print(m)
    
    for i in range(len(l)-2,-1,-1):
        if l[i] >= m:
            print(l[i])
            m = l[i]
    
l = [10,22,12,3,0,6]
l = [4,7,1,0]

leader(l)
