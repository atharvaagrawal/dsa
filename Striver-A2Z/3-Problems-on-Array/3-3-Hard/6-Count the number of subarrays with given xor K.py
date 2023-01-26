'''
Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays
having bitwise XOR of all elements equal to B.

Examples:

Input Format:  A = [4, 2, 2, 6, 4] , B = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 w  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

Input Format: A = [5, 6, 7, 8, 9], B = 5
Result: 2
Explanation:The subarrays having XOR of their elements as 2 are [5] and [5, 6, 7, 8, 9]
'''

'''
All SubArray:

def subarray(a, n):
    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(a[k], end=" ")
            print("\n", end=" ")


a = [1, 2, 3, 4, 5]
n = len(a)
print("all non - empty subarrays are: -")
subarray(a, n)
'''

# Brute Force Method Checking All the Available possiblity
def subArrayXOR_Brute(l,b):
    c = 0
    for i in range(len(l)):
        current_xor = 0
        print("\n",i)
        for j in range(i,len(l)):
            print(j,end=" ")
            current_xor = current_xor ^ l[j]

            if current_xor == b:
                c+=1
    print("Number of XOR:",c)

def subArrayXOR(l,b):
    c = 0
    d = dict()

    xor = 0

    for i in l:
        xor = xor ^ i

        if xor == b:
            c+=1

        # y = prefix_xor ^ b
        y = xor ^ b

        if y in d.keys():
            c+=d[y]

        if xor in d.keys():
            d[xor]+=1
        else:
            d[xor] = 1

        print(i,xor,y,c,d)
    return c

l = [4,2,2,6,4]
b = 6

print(subArrayXOR(l,b))