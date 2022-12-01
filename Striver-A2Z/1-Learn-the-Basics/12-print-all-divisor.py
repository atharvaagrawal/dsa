import math
# Print All the divisor

n = int(input("Enter any number:")) 

for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")

# Square Root Method
print("\nBy Square Method:")
for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
        print(i,end=" ")
        t = n//i
        if n%t == 0:
            print(t,end=" ")
