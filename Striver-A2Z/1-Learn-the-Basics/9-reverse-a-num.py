num = int(input("Enter a number:"))

rev = 0

while num > 0:
    temp = num %10
    rev = rev*10+temp
    num = num //10

print("Reverse:",rev)