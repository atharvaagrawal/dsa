'''
arr[] = {10,5,10,15,10,5};
Output: 10  3
	    5  2
        15  1
'''

arr = [int(i) for i in input().split()]

d = dict()

for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d) 
