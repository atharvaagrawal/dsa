num = int(input("Enter a number:"))

temp = num
rev = 0

while temp > 0:
    temp2 = temp % 10
    rev = rev*10 + temp2
    temp = temp //10

if num == rev:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")