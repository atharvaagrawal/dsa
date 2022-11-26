t = int(input())
 
for i in range(t):
    s = input()
    x = [i for i in s]
   
    x.sort()
    s1 = ''.join(x)
   
    x.reverse()
    s2 = ''.join(x)

    print(s1+s2)
