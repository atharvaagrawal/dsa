""" 
Given an unsorted array Arr[] of N integers and an integer X, find floor and ceiling 
of X in Arr[0..N-1].

Floor of X is the largest element which is smaller than or equal to X. Floor of X 
doesn’t exist if X is smaller than smallest element of Arr[].

Ceil of X is the smallest element which is greater than or equal to X. Ceil of X 
doesn’t exist if X is greater than greatest element of Arr[].

N = 8, X = 7
Arr[] = {5, 6, 8, 9, 6, 5, 5, 6}
Output: 6 8
Explanation:
Floor of 7 is 6 and ceil of 7 
is 8.
"""

def getFloorAndCeil(arr, n, x):
    # code here
    c = -1
    f = -1
    c1 = 0
    
    for i in arr:
        if i > x:
            if c1 == 0:
                c = i
                c1+=1
            else:
                c = min(c,i)
        if i < x:
            f = max(f,i)
        
        if i == x:
            c = i
            f = i
            break
        
    return [f,c]


N = 8
X = 7
arr = [5, 6, 8, 9, 6, 5, 5, 6]