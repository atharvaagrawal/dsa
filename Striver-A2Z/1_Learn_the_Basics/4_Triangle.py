for row in range(1,6):

    for col in range(6-row):
        print(end=" ")
    
    for col in range(row):
        print("*",end=" ")

    print()