t = int(input("Enter number of test cases:"))

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


while(t>0):
    n = int(input())
    
    A = list(map(int, input().split()[:n]))
    # A = l[::-1]
    
    t-=1
    
    reverseList(A, 0, n-1)
    
    for i in range(n):
        print(A[i],end=" ")
    print()
    