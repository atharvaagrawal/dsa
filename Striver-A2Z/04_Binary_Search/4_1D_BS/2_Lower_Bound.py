# Given a sorted array arr[] of size N without duplicates, 
# and given a value x. Floor of x is defined as the largest 
# element K in arr[] such that K is smaller than or equal to x. 
# Find the index of K(0-based indexing).

""" 
N = 7, x = 5 
arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is 2 (i.e K = 2),
 whose index is 1(0-based indexing).
 """
def findFloor(A,N,x):
        #Your code here        
        low = 0
        high = N-1
        
        
        while low <= high:
            mid = (low+high)//2

            # print(mid,A[mid])
            
            if x == A[mid]:
                return mid
            
            if x > A[mid]:
                low=mid+1
                
            if x < A[mid]:
                high=mid-1
        
        return mid-1

N = 7 
x = 1
A =[1,2,8,10,11,12,19]

N = 65
x = 106
arr = "66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130"

A = [int(i) for i in arr.split(" ")]

print(findFloor(A,N,x))
print(A[40])
