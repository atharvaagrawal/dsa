# https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1


# TLE
def sumOfSeries(N):
        if N==0:
            return 0
        
        res = N*N*N
        res +=sumOfSeries(N-1)
    
        return res 


def sumOfSeries_(n):
        n = n*(n+1)//2
        
        res = n*n
        
        return res

print(sumOfSeries_(10))