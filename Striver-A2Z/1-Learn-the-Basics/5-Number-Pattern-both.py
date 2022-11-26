""" 
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1 
"""
N = 5

for row in range(1,N+1):

    for col in range(row):
        print(col+1,end=" ")
    
    for col in range(N*2 - 2*row):
        print(end="  ")
    
    for col in range(row,0,-1):
        print(col,end=" ")
    print()
