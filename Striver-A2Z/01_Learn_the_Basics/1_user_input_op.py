from functools import reduce

x = int(input("Enter a Number:"))
print(x)
# Enter a Number:10
# 10


# Fetch All the even number
nums = [3,2,4,5,7,2,4,6]
even = list(filter( lambda x: x%2 == 0,nums))
print(even) # [2, 4, 2, 4, 6]


# Double the value
even = set(map(lambda x:(x*2),even))
print(even) #{8, 4, 12}


# Sum of all the values
sum = reduce(lambda x,y: x+y,even)
print(sum) #24
