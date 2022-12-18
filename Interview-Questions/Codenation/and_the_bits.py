a = [3,1,7]
b = [ [1,1,3,3], [1,2,3,3], [1,3,3,3]]

a = [8,6,5,9,7,7,9,3,8]
b = [[3,5,5,5]]

def solve(a,b):
    res = []
    for j in range(len(b)):
        l1 = b[j][0]
        r1 = b[j][1]    
        l2 = b[j][2]  
        r2 = b[j][3]

        # Do Bitwise AND of all integers in l1 to r1
        # and store the result in res1
        res1 = a[l1 -1]
        for k in range(l1,r1):
            res1 = res1 & a[k]

        # Do Bitwise AND of all integers in l2 to r2
        # and store the result in res2
        res2 = a[l2-1]
        for k in range(l2,r2):
           res2 = res2 & a[k]    
        
        res.append(res1 ^ res2)
    
    print(res)

solve(a,b)