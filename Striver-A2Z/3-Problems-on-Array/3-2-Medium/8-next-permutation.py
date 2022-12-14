# Printing All Possible combinations
#  
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
 
 
def permute(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]  # backtrack
 
 
arr = [1,2,3]
arr2 = [1,5,1]

n = len(arr)

print("All the permutations of the array are: ")
permute(arr,0,n)


