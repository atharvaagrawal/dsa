# GCD or HCF

num1 = int(input("Enter any number:"))
num2 = int(input("Enter any number:"))

gcd = 0

for i in range(1,min(num1,num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print(gcd)  

# Using Euclidean’s theorem.

def gcd_(a,b):
    if b == 0:
        return a
    
    return gcd_(b,a%b)

print(gcd_(num1,num2))

# LCM
lcm = (num1 * num2) // gcd

print("LCM:",lcm)