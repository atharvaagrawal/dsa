t = int(input())

for i in range(t):
    val = int(input())
    
    if val < 3:
        print("LIGHT")
    elif val >= 3 and val < 7:
        print("MODERATE")
    elif val >= 7:
        print("HEAVY")
        
        