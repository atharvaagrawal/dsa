N = 4
for row in range(N):
    for col in range(N-row):
        print("*",end="")
    
    for col in range(row*2):
        print(end=" ")

    for col in range(N-row):
        print("*",end="")
    print()

for row in range(1,N+1):
    for col in range(row):
        print("*",end="")
    
    for col in range(N*2-row*2):
        print(end=" ")

    for col in range(row):
        print("*",end="")    
    print()